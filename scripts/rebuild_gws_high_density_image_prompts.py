#!/usr/bin/env python3
"""Build per-slide full-raster image generation prompts (wireframe-referenced standard).

Each slide is generated as ONE complete raster image (not a template + embedded
diagram). Every generation must reference the fixed layout wireframe image at
`skills/corporate-training-course-builder/references/assets/講座スライドレイアウトワイヤフレーム.png`
so that every slide across every course shares the same chrome: 講座タイトル /
スライド番号・全体の枚数 header, スライド見出し title bar, 図解 content area,
今回のまとめ bar, and 目次見出し bottom strip (current chapter highlighted).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_editable_google_slides_sources as SOURCE_BUILDER  # noqa: E402

WIREFRAME_IMAGE = ROOT / "skills" / "corporate-training-course-builder" / "references" / "assets" / "講座スライドレイアウトワイヤフレーム.png"

COURSE_DIR = Path("講座/生成AI・GASで実践する業務変革・DX推進講座")

BASE_PROMPT = """16:9、1920x1080の法人研修用スライド画像を、Codex App Server / GPT image 2 / imagegenスキルで1枚の完成ラスター画像として生成する。白背景、ネイビー見出し、ブルー/ティール/ミントのアクセント、薄いグレー罫線、角丸カード、控えめな影、法人向けでフォーマルな情報設計にする。審査資料として、スライド単体で内容が理解できるように、タイトル、So What型ヘッドライン、本文カード、比較表、手順フロー、チェックリスト、業務例、成果物、確認観点を読みやすく配置する。講師コメントを読まなくても、何を学び、何を作り、どこを確認するかが分かる密度にする。"""

NEGATIVE_PROMPT = """SVG、HTML/CSS、canvas、ブラウザスクリーンショット、ローカル変換、後載せテキスト合成で作ったような見た目にしない。文字化け、誤字、余計な文字、小さすぎる文字、読めない日本語、意味のないダミー文字、過度な長文詰め込み、参照画像なしでのGoogleロゴ再現、参照画像なしでの実在UI再現、架空のGoogle画面、架空のGoogleロゴ、実在企業名、人物名、メールアドレス、電話番号、価格、連絡先、QRコード、透かし、素材配置枠、公式ロゴという文字、空の破線枠、暗い背景、派手なグラデーション、装飾過多、漫画風、手書き風、雑然としたレイアウトを避ける。参照レイアウト画像にある帯・枠・比率を無視した独自レイアウトにしない。"""

WIREFRAME_INSTRUCTION = """必ず添付の参照レイアウト画像（講座スライドレイアウトワイヤフレーム.png）を見て、その帯構成・比率・罫線をそのまま踏襲する。上段左に講座タイトル帯、上段右に「スライド番号 / 全体の枚数」帯、その下に横幅いっぱいのスライド見出し帯（枠線付き太字タイトル）、中央に大きな図解エリア（表・カード・フロー・チェックリストなどをここに密に配置する）、その下に「今回のまとめ」帯（左に見出しラベル、右に要点・結論・次のアクションの一文）、最下段に目次見出しストリップ（複数チップ、現在の章だけを塗りつぶしてハイライトし、他は白背景に薄い枠線）を配置する。ワイヤーフレーム画像の余白比率・帯の高さ・罫線の太さ・フォントの太さ感を再現し、そこに実際のテキスト・表・図を書き込む。"""

# 章見出し(目次切り替え)スライド専用: 通常スライドの固定ワイヤーフレーム(参照画像)は使わず、
# 全面フルブリードのヒーロー表示にする。現在の章名だけを画面いっぱいに大きく見せることを最優先する。
HERO_NEGATIVE_PROMPT = """SVG、HTML/CSS、canvas、ブラウザスクリーンショット、ローカル変換で作ったような見た目にしない。文字化け、誤字、読めない日本語、意味のないダミー文字、実在企業名、人物名、価格、連絡先、QRコード、透かし、架空ロゴ、架空UIを入れない。通常スライドのワイヤーフレーム（講座タイトル帯・S番号帯・目次ストリップ・表・カード・チェックリストなどの高密度レイアウト）を再現しない。小さい文字を大量に詰め込まない。情報カード、比較表、業種別リストなど通常スライドの密度要素を入れない。"""


def build_hero_prompt(
    slide_no: str,
    title: str,
    headline: str,
    course_title: str,
    section_idx: int,
    section_total: int,
    current_name: str,
    prev_name: str | None,
    next_name: str | None,
    minutes: str,
    slide_range: str,
) -> tuple[str, str]:
    """Return (image_prompt, negative_prompt) for a chapter-divider hero slide."""
    prev_line = f"画面の隅に、前の章「{prev_name}」を小さく薄い色のチップとして添える(あれば)。" if prev_name else "前の章がないため、前の章の表示は省略する。"
    next_line = f"現在の章の右下または下に、次の章「{next_name}」を、現在の章よりはっきり小さいサイズで示す(あれば)。" if next_name else "最後の章のため、次の章の表示は省略し、代わりに「まとめへ」のような一言を小さく添えてもよい。"
    body = "\n".join(
        [
            "16:9、1920x1080の法人研修スライド画像を、Codex App Server / GPT image 2 / imagegenスキルで1枚の完成ラスター画像として生成する。これは通常の情報密度が高いスライドではなく、章が切り替わる瞬間だけに使う「フルブリードのヒーロー表示」スライドである。",
            "参照レイアウト画像(講座スライドレイアウトワイヤフレーム.png)にある帯構成・ヘッダー・フッター・目次ストリップ・表組みレイアウトは今回は使わない。画面いっぱいを使う、全く別の専用デザインにする。",
            "背景は白またはごく薄いグラデーション地に、ネイビーとティールを基調とした大胆な幾何学アクセント(斜めの帯、太いライン、大きな数字の透かしなど)を1〜2箇所置き、法人研修らしい上質さを保つ。",
            f"画面の中央に、現在の章の番号と章名だけを画面の半分以上を占めるくらい極端に大きく、太いフォントで表示する: 「{section_idx}」「{current_name}」。数字と章名はセットで、この1枚で最も目立つ主役にする。",
            f"現在の章の近くに、進捗を示す小さな表記を1つだけ添える: 「{section_idx} / {section_total}」。",
            prev_line,
            next_line,
            f"画面の隅の小さな文字で、講座タイトル「{course_title}」とスライド番号「{slide_no}」だけを控えめに示してよいが、主役にはしない。",
            f"章の要点を伝える一文があれば、章名の下に小さめの一行で添えてよい: 「{headline}」。",
            f"参考情報(画像内に大きくは出さない): この章の時間目安は{minutes}、対象スライド範囲は{slide_range}。",
            "全体として、情報を詰め込まず、余白を大きく取り、章が変わったことが一瞬でわかる、雑誌の扉ページや基調講演のオープニングスライドのような、少ないが力強い要素構成にする。",
        ]
    )
    return body, HERO_NEGATIVE_PROMPT


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


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
    if "章見出し" in title or "現在位置" in title:
        return "目次切り替え専用の簡素なレイアウト。図解エリアには現在の章を大きく、次の章を右に、前の章を左に小さく、進捗(何分の何)を添えるだけにし、詳細な表やカードは入れない。"
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


def build_prompt_file(session_dir: Path, course_title: str) -> str:
    plan_path = session_dir / "スライド案.md"
    text = plan_path.read_text(encoding="utf-8")
    plan_title, allocation = extract_plan_meta(text)
    slides = split_slides(text)
    total = len(slides)
    sections = SOURCE_BUILDER.parse_sections(text)
    toc_labels = SOURCE_BUILDER.parse_toc_strip_labels(text)
    for idx, section in enumerate(sections, start=1):
        section.short_name = toc_labels.get(idx, f"{idx} {section.name[:6]}")

    def section_for(no: int) -> "SOURCE_BUILDER.SectionRange | None":
        for section in sections:
            if section.start <= no <= section.end:
                return section
        return None

    lines: list[str] = [
        f"# {session_dir.name} 画像生成プロンプト（1枚まるごとラスター・ワイヤーフレーム参照版）",
        "",
        f"対象講座: {course_title}",
        f"対象セッション: {plan_title}",
        f"対象スライド: S01-S{total:02d}",
        "採用テンプレート: `isometric-corporate-clean` + 固定レイアウトワイヤーフレーム参照",
        f"参照レイアウト画像（毎回必ず添付する）: `{WIREFRAME_IMAGE}`",
        "",
        "このファイルは、編集可能Google Slidesテンプレート方式ではなく、1スライド=1枚の完成ラスター画像を毎回ワイヤーフレーム参照画像付きで生成する標準に基づく。講師コメントがなくても、スライドだけで内容を想像できる密度を維持しつつ、レイアウトの再現性をワイヤーフレーム参照で担保する。",
        "",
        "## 共通ルール",
        "",
        "- Codex App Server / GPT image 2 / `imagegen` スキルで1枚まるごとの完成ラスター画像として生成する。",
        f"- 生成のたびに参照レイアウト画像 `{WIREFRAME_IMAGE.name}` を添付し、帯構成・比率・罫線をそのまま踏襲する。テキストで説明するだけでなく、画像そのものを参照入力として渡す。",
        "- SVG、HTML/CSS、canvas、ブラウザスクリーンショット、PIL/Pillow、ImageMagick、PDF/PPTX書き出し、ローカル変換、後載せテキスト合成は使わない。",
        "- 1枚ごとに、講座タイトル帯、スライド番号/全体の枚数帯、スライド見出し帯、図解エリア（3〜6個の本文ブロック・具体例・成果物・確認観点）、今回のまとめ帯、目次見出しストリップを必ず入れる。",
        "- 画像内テキストは、スライド案にある語句を優先し、勝手な要約や別概念を足さない。長すぎる本文は、意味を保ってカード・表・フローに分割する。",
        "- 目次見出しストリップは、現在の章のチップだけを塗りつぶしてハイライトし、他のチップは白背景・薄い枠線にする。",
        "- 実在ロゴや実在UIは参照素材がある場合だけ使う。参照素材なしにGoogleロゴやGoogle画面を描かせない。",
        "- 会社名、顧客名、社員名、メールアドレス、価格、連絡先、契約情報、APIキー、社内固有情報は入れない。",
        "- `素材配置枠`、`公式ロゴ`、空の破線枠、透かし、QRコード、架空UI、架空ロゴを入れない。",
        "",
        "## 共通ベースプロンプト",
        "",
        "```text",
        BASE_PROMPT,
        "```",
        "",
        "## ワイヤーフレーム参照指示（共通・毎回付与）",
        "",
        "```text",
        WIREFRAME_INSTRUCTION,
        "```",
        "",
        "## 共通ネガティブプロンプト",
        "",
        "```text",
        NEGATIVE_PROMPT,
        "```",
        "",
    ]
    if sections:
        lines += ["## 目次見出しストリップ（章構成）", ""]
        for section in sections:
            lines.append(f"- {section.short_name}（S{section.start:02d}-S{section.end:02d}）")
        lines.append("")
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
        no_int = int(slide_no[1:])
        headline = extract_field(block, "ヘッドライン")
        pattern = extract_field(block, "図解パターン")
        screenshot = extract_field(block, "スクリーンショット") or "なし"
        content = extract_content(block)
        layout = infer_layout(title, content, pattern)
        section = section_for(no_int)
        toc_desc = ""
        current_chip_label = ""
        if sections:
            toc_desc = " / ".join(s.short_name for s in sections)
            if section:
                current_chip_label = section.short_name
        is_divider = "章見出し" in title or "現在位置" in title
        if is_divider and section:
            section_idx = sections.index(section) + 1
            prev_name = sections[section_idx - 2].name if section_idx >= 2 else None
            next_name = sections[section_idx].name if section_idx < len(sections) else None
            hero_body, hero_negative = build_hero_prompt(
                slide_no,
                title,
                headline,
                course_title,
                section_idx,
                len(sections),
                section.name,
                prev_name,
                next_name,
                section.minutes or "-",
                f"S{section.start:02d}-S{section.end:02d}",
            )
            lines += [
                f"## Slide {slide_no}. {title}",
                "",
                "- 種別: 章見出し/目次切り替え専用スライド(フルブリードのヒーロー表示。通常ワイヤーフレームは使わない)",
                f"- 現在の章: {section_idx}/{len(sections)} {section.name}",
                f"- 前の章: {prev_name or 'なし'}",
                f"- 次の章: {next_name or 'なし'}",
                f"- 章の一言(画像内は小さく): {headline}",
                "",
                "- 画像プロンプト:",
                "",
                "```text",
                hero_body,
                "```",
                "",
                "- ネガティブプロンプト:",
                "",
                "```text",
                hero_negative,
                "```",
                "",
            ]
            continue
        lines += [
            f"## Slide {slide_no}. {title}",
            "",
            f"- 講座タイトル帯: {course_title}",
            f"- スライド番号/全体の枚数帯: {slide_no} / {total}",
            f"- スライド見出し帯: {title}",
            f"- 今回のまとめ帯（要点・結論・次のアクション）: {headline}",
            f"- 目次見出しストリップのチップ文字（左から順に、この文字列だけを表示。記号や★は付けない）: {toc_desc or '章区分なし'}",
            f"- 目次見出しストリップでハイライト（塗りつぶし）するチップ: {current_chip_label or 'なし'}",
            f"- 図解パターン: `{pattern or 'high-density-structured-slide'}`",
            f"- 参照素材・スクリーンショット: {screenshot}",
            f"- 推奨レイアウト（図解エリア内）: {layout}",
            "- 審査向け密度: タイトルだけ、抽象アイコンだけ、短いラベルだけで終わらせない。本文ブロックを、読める表・カード・フロー・チェックリストとして図解エリア内に配置する。",
            "- 図解エリアに必ず入れる内容:",
            "",
            "```markdown",
            content,
            "```",
            "",
            "- 画像プロンプト:",
            "",
            "```text",
            BASE_PROMPT,
            WIREFRAME_INSTRUCTION,
            f"添付の参照レイアウト画像を使い、以下のテキストをその帯構成にそのまま流し込む。",
            f"講座タイトル帯（そのまま表示）: {course_title}",
            f"スライド番号/全体の枚数帯（そのまま表示）: {slide_no} / {total}",
            f"スライド見出し帯（そのまま表示）: {title}",
            f"今回のまとめ帯（そのまま表示、右側に要点・結論・次のアクションとして）: {headline}",
            f"目次見出しストリップのチップ文字（左から順にこの文字列だけを表示、記号や★などの装飾は一切付け加えない）: {toc_desc or '章区分なし'}",
            f"目次見出しストリップで塗りつぶしてハイライトするチップはこれだけ（チップの文字自体は変えない）: {current_chip_label or 'なし'}",
            f"図解エリアの推奨構成: {layout}",
            "図解エリアには、以下のSOURCE TEXTを、読める表・カード・プロセス・チェックリストとして密に配置する。文言を勝手に変えたり、無関係な主張を足したりしない。",
            "--- SOURCE TEXT START ---",
            content,
            "--- SOURCE TEXT END ---",
            f"参照素材・スクリーンショット: {screenshot}",
            "講師コメントなしでも、何を学び、何を作り、どこを確認するかが分かる密度にする。フォーマルな法人研修トーンを維持する。",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course-dir", default=str(COURSE_DIR), help="対象講座ディレクトリ")
    parser.add_argument("--course-title", default=None, help="講座名。省略時はフォルダ名から補完")
    parser.add_argument("--session", default=None, help="対象セッション番号（例: 01）。省略時は全セッション")
    args = parser.parse_args()

    course_dir = Path(args.course_dir)
    course_title = args.course_title or course_dir.name
    if not course_dir.is_dir():
        raise SystemExit(f"Missing course dir: {course_dir}")
    session_dirs = sorted(p for p in course_dir.iterdir() if p.is_dir() and re.match(r"^\d\d-", p.name))
    if args.session:
        session_dirs = [p for p in session_dirs if SOURCE_BUILDER.session_no(p) == args.session]
    if not session_dirs:
        raise SystemExit(f"No session directories found under {course_dir}")
    for session_dir in session_dirs:
        prompt = build_prompt_file(session_dir, course_title)
        (session_dir / "画像生成プロンプト.md").write_text(prompt, encoding="utf-8")
        print(f"built: {session_dir / '画像生成プロンプト.md'}")
        split_dir = session_dir / "画像生成プロンプト"
        if split_dir.exists():
            readme = split_dir / "README.md"
            readme.write_text(
                "# 画像生成プロンプト分割ファイル\n\n"
                "旧分割プロンプトは使用しません。現在の正本は、同じ回の `画像生成プロンプト.md` です。\n"
                "1枚まるごとラスター・ワイヤーフレーム参照版に統一するため、再生成時は正本から必要なスライド番号を参照してください。\n",
                encoding="utf-8",
            )


if __name__ == "__main__":
    main()
