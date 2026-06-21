from __future__ import annotations

from pathlib import Path
import re


COURSE_DIR = Path("講座/AIエージェント実装・連携設計アカデミー")
DETAIL_MARKER = "## 高密度スライド詳細"


def split_table_line(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def parse_slide_table(plan_text: str) -> dict[str, dict[str, str]]:
    slides: dict[str, dict[str, str]] = {}
    in_slide_table = False
    headers: list[str] = []
    for line in plan_text.splitlines():
        cells = split_table_line(line)
        if not cells:
            continue
        if cells and cells[0] in {"No.", "No", "番号"}:
            headers = cells
            in_slide_table = True
            continue
        if in_slide_table and all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            continue
        if in_slide_table and cells[0].startswith("S") and len(cells) >= 3:
            row = dict(zip(headers, cells))
            no = row.get("No.", row.get("No", row.get("番号", cells[0])))
            slides[no] = row
            continue
        if in_slide_table and cells[0] and not cells[0].startswith("S"):
            continue
    return slides


def extract_prompt_section(prompt_text: str, slide_no: str) -> str:
    pattern = re.compile(
        rf"^## Slide {re.escape(slide_no)}\..*?(?=^## Slide S\d{{2}}\.|\Z)",
        re.M | re.S,
    )
    match = pattern.search(prompt_text)
    return match.group(0) if match else ""


def find_field(section: str, label: str) -> str:
    match = re.search(rf"^- {re.escape(label)}:\s*(.+)$", section, re.M)
    return match.group(1).strip() if match else ""


def find_headline(section: str) -> str:
    for pattern in [
        r"^- ヘッドライン:\s*(.+)$",
        r"^ヘッドライン:\s*(.+)$",
        r"^Headline:\s*(.+)$",
    ]:
        match = re.search(pattern, section, re.M)
        if match:
            return match.group(1).strip()
    return ""


def find_source_blocks(section: str) -> list[tuple[str, list[str]]]:
    source_match = re.search(
        r"--- SOURCE TEXT START ---\n(.*?)\n--- SOURCE TEXT END ---",
        section,
        re.S,
    )
    source = source_match.group(1) if source_match else section
    blocks: list[tuple[str, list[str]]] = []
    block_pattern = re.compile(
        r"^\*\*内容ブロック[①②③④⑤⑥0-9]+：(.+?)\*\*\n(.*?)(?=^\*\*内容ブロック|^```|\Z)",
        re.M | re.S,
    )
    for match in block_pattern.finditer(source):
        title = match.group(1).strip()
        body = match.group(2)
        bullets = []
        for raw in body.splitlines():
            line = raw.strip()
            if not line or line.startswith("|") or line.startswith("---"):
                continue
            if line.startswith("- "):
                bullets.append(line)
        blocks.append((title, bullets[:4]))
    return blocks


def build_details(plan_text: str, prompt_text: str) -> str:
    slides = parse_slide_table(plan_text)
    parts: list[str] = [
        DETAIL_MARKER,
        "",
        "この節は `画像生成プロンプト.md` のヘッドライン、内容ブロック、図解パターンと同期した検証用の詳細です。スライド単体で内容が伝わるかを確認するため、各スライドにヘッドライン、構造、素材、成果物・確認観点を明示します。",
        "",
    ]
    for slide_no in sorted(slides, key=lambda x: int(x[1:])):
        row = slides[slide_no]
        section = extract_prompt_section(prompt_text, slide_no)
        title = row.get("タイトル", "")
        main = row.get("主な内容", row.get("内容", ""))
        template = row.get("使用テンプレート", "isometric-corporate-clean") or "isometric-corporate-clean"
        pattern = row.get("図解パターン", "")
        material = row.get("画面・素材", row.get("素材", ""))
        headline = find_headline(section) or f"{title}を業務成果物・確認観点・安全条件まで具体化する"
        layout = find_field(section, "推奨レイアウト")
        reference = find_field(section, "参照素材・スクリーンショット")
        blocks = find_source_blocks(section)
        parts.extend(
            [
                f"### {slide_no} {title}",
                "",
                f"**ヘッドライン:** {headline}",
                f"**テンプレートID:** `{template}`",
                f"**図解パターン:** `{pattern}`",
                f"**素材・画面:** {material or reference or '生成図解'}",
                f"**主な内容:** {main}",
            ]
        )
        if layout:
            parts.append(f"**推奨レイアウト:** {layout}")
        if reference and reference != material:
            parts.append(f"**参照素材・スクリーンショット:** {reference}")
        if blocks:
            parts.extend(["", "**内容ブロック:**"])
            for name, bullets in blocks[:5]:
                parts.append(f"- {name}")
                for bullet in bullets[:3]:
                    parts.append(f"  - {bullet[2:]}")
        else:
            parts.extend(
                [
                    "",
                    "**内容ブロック:**",
                    f"- 業務文脈: {main}",
                    "- 学習行動: 動画を一時停止してワークシートまたは演習データへ反映する",
                    "- 確認観点: 入力、処理、出力、人の確認、ログ/保存先、停止条件を点検する",
                ]
            )
        parts.extend(
            [
                "",
                "**成果物・確認観点:** 業務棚卸し、Codexタスクブリーフ、業務改善リポジトリ、MCP連携設計、運用設計書、DX業務効率化提案書のいずれかへ接続し、実データ・顧客情報・認証情報・未公開資料を使わないことを確認する。",
                "",
            ]
        )
    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    for session_dir in sorted(COURSE_DIR.iterdir()):
        if not session_dir.is_dir() or not re.match(r"\d{2}-", session_dir.name):
            continue
        plan_path = session_dir / "スライド案.md"
        prompt_path = session_dir / "画像生成プロンプト.md"
        if not plan_path.exists() or not prompt_path.exists():
            continue
        plan_text = plan_path.read_text(encoding="utf-8")
        prompt_text = prompt_path.read_text(encoding="utf-8")
        base = plan_text.split(DETAIL_MARKER)[0].rstrip()
        details = build_details(base, prompt_text)
        plan_path.write_text(base + "\n\n" + details, encoding="utf-8")
        print(plan_path)


if __name__ == "__main__":
    main()
