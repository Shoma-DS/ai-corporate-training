from __future__ import annotations

from pathlib import Path
import re


COURSE_DIR = Path("講座/AIエージェント実装・連携設計アカデミー")


def split_table_line(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def parse_slide_rows(plan_text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    headers: list[str] = []
    in_table = False
    for line in plan_text.splitlines():
        cells = split_table_line(line)
        if not cells:
            continue
        if cells[0] in {"No.", "No", "番号"}:
            headers = cells
            in_table = True
            continue
        if in_table and all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            continue
        if in_table and cells[0].startswith("S"):
            row = dict(zip(headers, cells))
            row["No."] = row.get("No.", row.get("No", row.get("番号", cells[0])))
            rows.append(row)
    return rows


def parse_existing_blocks(script_text: str) -> tuple[str, dict[str, str], str]:
    marker = re.compile(r"^スライド切替:\nS(\d{2})「.*?」\n", re.M)
    matches = list(marker.finditer(script_text))
    if not matches:
        return script_text.rstrip() + "\n", {}, ""
    prefix = script_text[: matches[0].start()].rstrip() + "\n\n"
    blocks: dict[str, str] = {}
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(script_text)
        blocks[f"S{match.group(1)}"] = script_text[match.start() : end].strip() + "\n"
    return prefix, blocks, ""


def fallback_block(row: dict[str, str]) -> str:
    no = row["No."]
    title = row.get("タイトル", "")
    main = row.get("主な内容", row.get("内容", ""))
    pattern = row.get("図解パターン", "")
    material = row.get("画面・素材", row.get("素材", ""))
    if title.startswith("ワーク") or "自己レビュー" in title or "確認" in title and no not in {"S02", "S37"}:
        return (
            f"スライド切替:\n{no}「{title}」\n\n"
            "ワーク指示:\n"
            f"「ここで動画を一時停止して、スライドの確認観点に沿って取り組んでください。テーマは{main}です。"
            "入力、処理、出力、人の確認、保存先、停止条件が書けているかを見直し、取り組めたら再生してください。」\n"
        )
    if title.startswith("画面共有"):
        return (
            f"スライド切替:\n{no}「{title}」\n\n"
            "読み上げ:\n"
            f"「ここから画面共有で、{main}を確認します。画面にはダミーデータまたは講師の記入例だけを表示します。"
            "実データ、個人情報、契約情報、認証情報は使いません。見るポイントは、成果物へつながる入力、確認者、保存先、停止条件です。」\n"
        )
    return (
        f"スライド切替:\n{no}「{title}」\n\n"
        "読み上げ:\n"
        f"「このスライドでは、{main}を確認します。図解パターンは{pattern}です。"
        f"素材は{material or '生成図解'}を前提に、ツール名だけでなく、業務課題、入力情報、AIエージェントの役割、人の確認、成果物までつなげて見てください。」\n"
    )


def add_timeline(rows: list[dict[str, str]]) -> str:
    lines = [
        "## スライド切替タイムライン",
        "",
        "| No. | タイトル | 操作概要 |",
        "| --- | --- | --- |",
    ]
    for row in rows:
        no = row["No."]
        title = row.get("タイトル", "")
        main = row.get("主な内容", row.get("内容", ""))
        lines.append(f"| {no} | {title} | {main} |")
    return "\n".join(lines) + "\n"


def add_demo_timeline(text: str) -> str:
    demos = []
    pattern = re.compile(r"^画面共有 ── 実演(\d+)「(.+?)」\n⏱ 約(.+?)\n", re.M)
    for match in pattern.finditer(text):
        demo_no, title, duration = match.groups()
        tail = text[match.end() : match.end() + 500]
        point = ""
        point_match = re.search(r"【見せるポイント】\n(.+)", tail)
        if point_match:
            point = point_match.group(1).splitlines()[0]
        demos.append((demo_no, title, duration, point))
    if not demos:
        return ""
    lines = [
        "## 作業風景タイムライン",
        "",
        "| 実演 | タイトル | ⏱ 時間 | 操作概要 |",
        "| --- | --- | --- | --- |",
    ]
    for demo_no, title, duration, point in demos:
        lines.append(f"| 実演{demo_no} | {title} | 約{duration} | {point or 'ダミーデータまたは講師記入例で確認する'} |")
    return "\n".join(lines) + "\n"


def normalize_screen_share_blocks(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    for i, line in enumerate(lines):
        out.append(line)
        if line.startswith("画面共有 ── 実演"):
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            if not next_line.startswith("⏱ 約"):
                out.append("⏱ 約4分")
    normalized = "\n".join(out) + "\n"
    normalized = re.sub(r"^【手順(\d+)】", r"【手順\1 – 約1分】", normalized, flags=re.M)
    return normalized


def main() -> None:
    for session_name in [
        "01-DX業務課題整理とCodex活用設計",
        "02-業務リポジトリと安全な作業環境の設計",
        "03-Codexによる業務改善プロトタイプ実装",
        "04-MCPで社内ツールとデータをつなぐ設計",
        "05-評価-権限-運用設計と定着化",
        "06-DX業務効率化提案書と展開計画",
    ]:
        session_dir = COURSE_DIR / session_name
        script_path = session_dir / "講師台本.md"
        plan_path = session_dir / "スライド案.md"
        script_text = script_path.read_text(encoding="utf-8")
        base_script = re.split(r"\n## スライド切替タイムライン\n|\n## 作業風景タイムライン\n", script_text)[0].rstrip() + "\n"
        rows = parse_slide_rows(plan_path.read_text(encoding="utf-8"))
        prefix, blocks, _ = parse_existing_blocks(base_script)
        parts = [prefix.rstrip()]
        for row in rows:
            parts.append(blocks.get(row["No."], fallback_block(row)).rstrip())
        merged = "\n\n".join(parts).rstrip() + "\n\n"
        merged = normalize_screen_share_blocks(merged)
        demo_timeline = add_demo_timeline(merged)
        merged += add_timeline(rows) + "\n"
        if demo_timeline:
            merged += demo_timeline
        script_path.write_text(merged, encoding="utf-8")
        print(script_path)


if __name__ == "__main__":
    main()
