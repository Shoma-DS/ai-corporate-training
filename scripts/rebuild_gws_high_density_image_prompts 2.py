#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


COURSE_DIR = Path("講座/生成AI・GASで実践する業務変革・DX推進講座")
SESSION_DIRS = sorted(p for p in COURSE_DIR.iterdir() if p.is_dir() and re.match(r"^\d\d-", p.name))

BASE_PROMPT = """16:9、1920x1080の法人研修用スライド画像を、GPT image 2 / built-in image generationで1枚の完成ラスター画像として生成する。白背景、ネイビー見出し、ブルー/ティール/ミントのアクセント、薄いグレー罫線、角丸カード、控えめな影、法人向けでフォーマルな情報設計にする。審査資料として、スライド単体で内容が理解できるように、タイトル、So What型ヘッドライン、本文カード、比較表、手順フロー、チェックリスト、業務例、成果物、確認観点を読みやすく配置する。講師コメントを読まなくても、何を学び、何を作り、どこを確認するかが分かる密度にする。"""

NEGATIVE_PROMPT = """SVG、HTML/CSS、canvas、ブラウザスクリーンショット、ローカル変換、後載せテキスト合成で作ったような見た目にしない。文字化け、誤字、余計な文字、小さすぎる文字、読めない日本語、意味のないダミー文字、過度な長文詰め込み、参照画像なしでのGoogleロゴ再現、参照画像なしでの実在UI再現、架空のGoogle画面、架空のGoogleロゴ、実在企業名、人物名、メールアドレス、電話番号、価格、連絡先、QRコード、透かし、素材配置枠、公式ロゴという文字、空の破線枠、暗い背景、派手なグラデーション、装飾過多、漫画風、手書き風、雑然としたレイアウトを避ける。"""


def clean_line(line: str) -> str:
    line = line.strip()
    if not line.startswith("**"):
        line = re.sub(r"^\s*[-*]\s*", "", line)
    line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
    return line.strip()


def truncate(text: str, limit: int = 1400) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text.strip())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def extract_plan_meta(text: str) -> tuple[str, str]:
    title = text.splitlines()[0].lstrip("# ").strip()
    allocation = ""
    m = re.search(r"## 120分の時間配分[\s\S]*?(?=\n---|\n## スライド詳細|\n## Slide|\Z)", text)
    if m:
        allocation = m.group(0).strip()
    return title, allocation


def split_slides(text: str) -> list[tuple[str, str, str]]:
    matches = list(re.finditer(r"^### (S\d\d)\s+(.+)$", text, re.M))
    slides: list[tuple[str, str, str]] = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        slides.append((match.group(1), clean_line(match.group(2)), text[start:end].strip()))
    return slides


def extract_field(block: str, label: str) -> str:
    m = re.search(rf"^\*\*{re.escape(label)}:\*\*\s*(.+)$", block, re.M)
    return clean_line(m.group(1)) if m else ""


def extract_content(block: str) -> str:
    lines: list[str] = []
    keep = False
    for raw in block.splitlines():
        line = raw.rstrip()
        if line.startswith("**内容ブロック"):
            keep = True
            lines.append(clean_line(line.replace("：", ":")))
            continue
        if line.startswith("- **図解パターン:**") or line.startswith("- **テンプレートID:**") or line.startswith("- **スクリーンショット:**"):
            keep = False
        if keep and line.strip():
            lines.append(clean_line(line))
    if not lines:
        body = re.sub(r"^### .+$", "", block, flags=re.M)
        body = re.sub(r"^\*\*ヘッドライン:\*\*.+$", "", body, flags=re.M)
        body = re.sub(r"^- \*\*(図解パターン|テンプレートID|スクリーンショット):\*\*.+$", "", body, flags=re.M)
        lines = [clean_line(x) for x in body.splitlines() if clean_line(x)]
    return truncate("\n".join(lines), 1700)


def infer_layout(title: str, content: str, pattern: str) -> str:
    source = f"{title}\n{content}\n{pattern}"
    if "Before" in source or "After" in source or "比較" in source or "違い" in source:
        return "左右比較またはBefore/After表。左に課題・現状、右に改善後・設計後を置き、差分が一目で分かる構成。"
    if "手順" in source or "フロー" in source or "流れ" in source or "ステップ" in source:
        return "横または縦のプロセスフロー。各ステップに短い説明、入力、処理、出力、確認ポイントを付ける。"
    if "演習" in source or "ワーク" in source:
        return "演習指示スライド。使うファイル、作業手順、完成物、自己レビュー基準を4つのカードで明示する。"
    if "リスク" in source or "権限" in source or "情報管理" in source or "禁止" in source:
        return "リスク管理・チェックリスト型。注意点、確認者、禁止事項、代替手順をカードで整理する。"
    if "|" in content:
        return "読みやすい表またはカード型マトリクス。列見出しを明確にし、行数を絞って可読性を優先する。"
    return "3〜6枚の情報カードを中心に、業務例、判断軸、成果物、確認観点を併記する。"


def build_prompt_file(session_dir: Path) -> str:
    plan_path = session_dir / "スライド案.md"
    text = plan_path.read_text()
    plan_title, allocation = extract_plan_meta(text)
    slides = split_slides(text)
    lines: list[str] = [
        f"# {session_dir.name} 画像生成プロンプト（審査向け高密度版）",
        "",
        "対象講座: 生成AI・GASで実践する業務変革・DX推進講座",
        f"対象セッション: {plan_title}",
        f"対象スライド: S01-S{len(slides):02d}",
        "採用テンプレート: `isometric-corporate-clean`",
        "",
        "このファイルは、クライアントフィードバック「講師コメントがなくても、スライドだけで内容を想像できるようにする」を反映した画像生成プロンプト正本です。既存の薄い表紙風・抽象図解風プロンプトではなく、審査資料として読める情報量を優先します。",
        "",
        "## 共通ルール",
        "",
        "- GPT image 2 / built-in `image_gen` で1枚まるごとの完成ラスター画像として生成する。",
        "- SVG、HTML/CSS、canvas、ブラウザスクリーンショット、PIL/Pillow、ImageMagick、PDF/PPTX書き出し、ローカル変換、後載せテキスト合成は使わない。",
        "- 1枚ごとに、タイトル、So What型ヘッドライン、3〜6個の本文ブロック、具体例、成果物、確認観点のいずれかを必ず見せる。",
        "- 画像内テキストは、スライド案にある語句を優先し、勝手な要約や別概念を足さない。長すぎる本文は、意味を保ってカード・表・フローに分割する。",
        "- マナビDX等の審査では講師コメントが見られない前提で、スライド単体で何を学ぶか、何を作るか、何を確認するかが分かる構成にする。",
        "- 実在ロゴや実在UIは参照素材がある場合だけ使う。参照素材なしにGoogleロゴやGoogle画面を描かせない。",
        "- 会社名、顧客名、社員名、メールアドレス、価格、連絡先、契約情報、APIキー、社内固有情報は入れない。",
        "- `素材配置枠`、`公式ロゴ`、空の破線枠、透かし、QRコード、架空UI、架空ロゴを入れない。",
        "- `Course` や `Session` は生成時の文脈情報であり、画像内の見出しやヘッダーとして描かない。画像内に出す文字は原則 `SOURCE TEXT` の日本語だけにする。",
        "",
        "## 共通ベースプロンプト",
        "",
        "```text",
        BASE_PROMPT,
        "```",
        "",
        "## 共通ネガティブプロンプト",
        "",
        "```text",
        NEGATIVE_PROMPT,
        "```",
        "",
    ]
    if allocation:
        lines += [
            "## セッション全体の時間配分",
            "",
            "画像生成時の文脈として参照する。時間配分そのものを全スライドに入れる必要はない。",
            "",
            "```markdown",
            allocation,
            "```",
            "",
        ]
    for slide_no, title, block in slides:
        headline = extract_field(block, "ヘッドライン")
        pattern = extract_field(block, "図解パターン")
        template = extract_field(block, "テンプレートID") or "isometric-corporate-clean"
        screenshot = extract_field(block, "スクリーンショット") or "なし"
        content = extract_content(block)
        layout = infer_layout(title, content, pattern)
        lines += [
            f"## Slide {slide_no}. {title}",
            "",
            f"- 使用テンプレート: `isometric-corporate-clean`",
            f"- 図解パターン: `{pattern or 'high-density-structured-slide'}`",
            f"- テンプレート統一: スライド案側の旧指定が `{template}` でも、画像生成は全回 `isometric-corporate-clean` に統一する。",
            f"- ヘッドライン: {headline}",
            f"- 参照素材・スクリーンショット: {screenshot}",
            f"- 推奨レイアウト: {layout}",
            "- 審査向け密度: タイトルだけ、抽象アイコンだけ、短いラベルだけで終わらせない。本文ブロックを、読める表・カード・フロー・チェックリストとして画面内に配置する。",
            "- 画像内に必ず入れる内容:",
            "",
            "```markdown",
            f"タイトル: {title}",
            f"ヘッドライン: {headline}",
            content,
            "```",
            "",
            "- 画像プロンプト:",
            "",
            "```text",
            BASE_PROMPT,
            "Context only, do not render as visible text: Course title = 生成AI・GASで実践する業務変革・DX推進講座",
            f"Context only, do not render as visible text: Session folder = {session_dir.name}",
            f"Slide {slide_no}: {title}",
            f"Headline: {headline}",
            f"Diagram/layout pattern: {pattern or 'high-density-structured-slide'}",
            f"Recommended layout: {layout}",
            "Use the following Japanese text as the source of truth. Render it as readable cards, tables, process steps, checklist items, and output labels. Keep wording faithful; do not add unrelated claims.",
            "--- SOURCE TEXT START ---",
            f"タイトル: {title}",
            f"ヘッドライン: {headline}",
            content,
            "--- SOURCE TEXT END ---",
            f"Reference assets/screenshots: {screenshot}",
            "Make the slide understandable without speaker notes. Show learner action, business purpose, output, review point, and next connection where relevant. Use a formal corporate training tone.",
            "```",
            "",
            "- ネガティブプロンプト:",
            "",
            "```text",
            NEGATIVE_PROMPT,
            "```",
            "",
        ]
    return "\n".join(lines)


def main() -> None:
    if not SESSION_DIRS:
        raise SystemExit(f"No session directories found under {COURSE_DIR}")
    for session_dir in SESSION_DIRS:
        prompt = build_prompt_file(session_dir)
        (session_dir / "画像生成プロンプト.md").write_text(prompt)
        split_dir = session_dir / "画像生成プロンプト"
        if split_dir.exists():
            readme = split_dir / "README.md"
            readme.write_text(
                "# 画像生成プロンプト分割ファイル\n\n"
                "旧分割プロンプトは使用しません。現在の正本は、同じ回の `画像生成プロンプト.md` です。\n"
                "審査向けの高密度プロンプトに統一するため、再生成時は正本から必要なスライド番号を参照してください。\n"
            )


if __name__ == "__main__":
    main()
