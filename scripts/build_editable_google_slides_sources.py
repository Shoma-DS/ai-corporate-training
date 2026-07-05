#!/usr/bin/env python3
"""Build editable Google Slides source outlines and dense diagram prompts.

This script does not create final slide images. It keeps slide text editable in
Google Slides and writes prompts for generated raster reference-sheet images.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from dataclasses import dataclass, field
from pathlib import Path


COURSE_DIR = Path("講座/生成AI・GASで実践する業務変革・DX推進講座")
COURSE_TITLE = "生成AI・GASで実践する業務変革・DX推進講座"

SESSION_TITLES = {
    "01": "業務DXの基礎とGoogle Workspace活用設計",
    "02": "業務データ基盤の設計",
    "03": "GASによる業務プロセス自動化",
    "04": "Gem/Geminiを使った文書作成・分類・要約",
    "05": "AI/GAS自動化の要件定義・運用設計",
    "06": "AI業務効率化プロジェクト提案書の作成",
}


@dataclass
class SectionRange:
    name: str
    start: int
    end: int
    minutes: str = ""
    short_name: str = ""


@dataclass
class Slide:
    number: int
    slide_id: str
    title: str
    body: str
    headline: str
    diagram_pattern: str
    screenshot: str
    section: str


def session_no(session_dir: Path) -> str:
    match = re.match(r"(\d{2})-", session_dir.name)
    if not match:
        raise ValueError(f"Session folder must start with NN-: {session_dir}")
    return match.group(1)


def clean_cell(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def clean_markdown(value: str) -> str:
    value = value.strip()
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"\1", value)
    value = re.sub(r"^\s*[-*]\s*", "", value)
    return clean_cell(value)


def parse_sections(text: str) -> list[SectionRange]:
    sections: list[SectionRange] = []
    lines = text.splitlines()
    start_index = next((idx for idx, line in enumerate(lines) if "120分の時間配分" in line), -1)
    if start_index >= 0:
        table_lines: list[str] = []
        for line in lines[start_index + 1 :]:
            if line.strip().startswith("|"):
                table_lines.append(line)
                continue
            if table_lines and line.strip():
                break
        source_lines = table_lines
    else:
        source_lines = lines
    for line in source_lines:
        if not line.strip().startswith("|"):
            continue
        cells = [clean_cell(cell) for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        range_cell = next((cell for cell in cells if re.search(r"S\d{2}\s*[–-]\s*S\d{2}", cell)), "")
        if not range_cell:
            continue
        match = re.search(r"S(\d{2})\s*[–-]\s*S(\d{2})", range_cell)
        if not match:
            continue
        name = cells[0]
        if name in {"ブロック", "大項目", "---"}:
            continue
        minutes = cells[1] if len(cells) > 1 else ""
        sections.append(SectionRange(name=name, start=int(match.group(1)), end=int(match.group(2)), minutes=minutes))
    return sections


def parse_toc_strip_labels(text: str) -> dict[int, str]:
    """Parse the optional `## 目次ストリップ表示名` table into {chapter_no: label}."""
    labels: dict[int, str] = {}
    match = re.search(r"^##\s*目次ストリップ表示名\s*$", text, re.MULTILINE)
    if not match:
        return labels
    for line in text[match.end() :].splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            break
        if not stripped.startswith("|"):
            if labels:
                break
            continue
        cells = [clean_cell(cell) for cell in stripped.strip("|").split("|")]
        if len(cells) >= 2 and re.fullmatch(r"\d+", cells[0]):
            labels[int(cells[0])] = cells[1]
    return labels


def section_for(slide_no: int, sections: list[SectionRange]) -> str:
    for section in sections:
        if section.start <= slide_no <= section.end:
            return section.name
    return "未設定セクション"


def field_value(body: str, label: str) -> str:
    pattern = rf"^\s*(?:[-*]\s*)?\*\*{re.escape(label)}:\*\*\s*(.+)$"
    match = re.search(pattern, body, re.MULTILINE)
    return clean_cell(match.group(1)) if match else ""


def parse_slides(text: str) -> list[tuple[int, str, str]]:
    matches = list(re.finditer(r"^### S(\d{2})\s+(.+)$", text, re.MULTILINE))
    slides: list[tuple[int, str, str]] = []
    for idx, match in enumerate(matches):
        start = match.end()
        if idx + 1 < len(matches):
            end = matches[idx + 1].start()
        else:
            next_top_heading = re.search(r"^##\s+", text[start:], re.MULTILINE)
            end = start + next_top_heading.start() if next_top_heading else len(text)
        body = text[start:end].strip()
        body = re.sub(r"\A(?:\s*---\s*\n)+", "", body).strip()
        body = re.sub(r"(?:\n\s*---\s*)+\Z", "", body).strip()
        slides.append((int(match.group(1)), clean_cell(match.group(2)), body))
    return slides


def normalize_body_for_outline(body: str, max_chars: int = 2400) -> str:
    lines: list[str] = []
    for line in body.splitlines():
        stripped = line.rstrip()
        if stripped.startswith("- **図解パターン:**"):
            continue
        if stripped.startswith("- **テンプレートID:**"):
            continue
        if stripped.startswith("- **スクリーンショット:**"):
            continue
        lines.append(stripped)
    normalized = "\n".join(lines).strip()
    if len(normalized) <= max_chars:
        return normalized
    return normalized[:max_chars].rstrip() + "\n\n（以降はスライド案.mdの該当S番号から補完）"


def build_slide_objects(session_dir: Path) -> tuple[list[Slide], list[SectionRange]]:
    plan_path = session_dir / "スライド案.md"
    text = plan_path.read_text(encoding="utf-8")
    sections = parse_sections(text)
    toc_labels = parse_toc_strip_labels(text)
    for idx, section in enumerate(sections, start=1):
        section.short_name = toc_labels.get(idx, f"{idx} {section.name[:6]}")
    slides: list[Slide] = []
    for number, title, body in parse_slides(text):
        headline = field_value(body, "ヘッドライン") or "要確認: ヘッドライン未設定"
        diagram_pattern = field_value(body, "図解パターン") or field_value(body, "図解パターン:**") or "内容に合わせて選定"
        screenshot = field_value(body, "スクリーンショット") or "なし"
        slides.append(
            Slide(
                number=number,
                slide_id=f"S{number:02d}",
                title=title,
                body=body,
                headline=headline,
                diagram_pattern=diagram_pattern,
                screenshot=screenshot,
                section=section_for(number, sections),
            )
        )
    return slides, sections


def write_editable_outline(session_dir: Path, slides: list[Slide], sections: list[SectionRange]) -> None:
    no = session_no(session_dir)
    session_title = SESSION_TITLES.get(no, session_dir.name.split("-", 1)[-1])
    generated_at = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    lines = [
        f"# 第{int(no)}回 Google Slides編集用アウトライン",
        "",
        f"- 生成日時: {generated_at}",
        f"- 講座名: {COURSE_TITLE}",
        f"- セッション/テキスト名: 第{int(no)}回 {session_title}",
        "- 方針: 既存スライド案の情報量を保ち、本文はGoogle Slidesの編集可能テキストとして配置する。",
        "- 固定ワイヤーフレーム: 全スライドを同一の16:9（720×405pt）とし、共通背景画像・講座名・セッション名・S番号・セクション名・タイトル・ヘッドライン・下端の目次ストリップを全ページ全く同じ位置・デザインに置く。",
        "- 背景: 講座`全体/素材/スライド背景ワイヤーフレーム.png`（文字なし）を全ページの背景に敷く。",
        "- 図解: `図解パーツ生成プロンプト.md` で作った1536×1024の横長 `図解パーツ/Sxx.png` を、全ページ同一の図解ゾーン（x60, y58, 幅600, 高さ322pt）へ配置する。画像上部約20%は白余白とし、テンプレート側のタイトル・ヘッドラインと干渉させない。",
        "- 目次/現在位置: 各回の冒頭に目次/全体像スライドを置き、各セクション開始位置に章見出し/現在位置スライドを置く。全スライド下端の目次ストリップで現在章をハイライトし、右上のセクション名でも現在位置を示す。",
        "",
        "## 共通ヘッダー・固定ワイヤーフレーム",
        "",
        "| 位置 | 表示テキスト・要素 |",
        "| --- | --- |",
        f"| 左上1行目（x26, y9） | {COURSE_TITLE} |",
        f"| 左上2行目（x26, y23） | 第{int(no)}回 {session_title} |",
        "| 右上1行目（x632, y8） | Sxx |",
        "| 右上2行目（x470, y31） | セクション名 |",
        "| 区切り罫（y49） | ティールの水平罫線 |",
        "| タイトル（x31, y57） | スライドタイトル |",
        "| ヘッドライン（x31, y89） | So What一文 |",
        "| 図解ゾーン（x60, y58, 600×322） | 図解パーツ/Sxx.png |",
        "| 下端目次ストリップ（y384） | 6章チップ。現在章のみティール塗り＋白文字 |",
        "",
        "## セクション",
        "",
        "| セクション | スライド範囲 | 目次ストリップ表示名 |",
        "| --- | --- | --- |",
    ]
    if sections:
        for section in sections:
            lines.append(
                f"| {section.name} | S{section.start:02d}-S{section.end:02d} | {section.short_name} |"
            )
    else:
        lines.append("| 要確認 | スライド案.mdの120分時間配分表から補完 | 要確認 |")
    lines.extend(["", "## スライド別編集ソース", ""])

    for slide in slides:
        body = normalize_body_for_outline(slide.body)
        lines.extend(
            [
                f"### {slide.slide_id} {slide.title}",
                "",
                "| 項目 | 編集可能テキスト |",
                "| --- | --- |",
                f"| 講座名 | {COURSE_TITLE} |",
                f"| セッション/テキスト名 | 第{int(no)}回 {session_title} |",
                f"| スライド番号 | {slide.slide_id} |",
                f"| セクション名 | {slide.section} |",
                f"| タイトル | {slide.title} |",
                f"| ヘッドライン | {slide.headline} |",
                f"| 図解/素材 | {slide.diagram_pattern} / {slide.screenshot} |",
                "",
                "**本文ブロック（Google Slides上で編集可能テキストとして配置）**",
                "",
                body,
                "",
                "**配置メモ**",
                "",
                "- 固定ワイヤーフレームに従う: 背景画像・講座名・セッション名・S番号・セクション名・タイトル・ヘッドライン・目次ストリップは全ページ同じ位置・デザイン。",
                "- タイトル（x31, y57）とヘッドライン（x31, y89）は上部固定。図解パーツは全ページ同一の図解ゾーン（x60, y58, 600×322pt）に配置する。",
                "- 図解パーツは1536×1024で生成し、画像上部約20%を白余白にしてタイトル・ヘッドラインと干渉させない。画像内に講座名、S番号、長い段落、スピーカーノートは固定しないが、中核となる比較表・プロセス表・業種別例の短いセル文は入れてよい。",
                "- 下端の目次ストリップで現在章をハイライトする（現在章のみティール塗り＋白文字）。",
                "- 演習、成果物、確認観点、リスクは図解パーツ内の下部帯に残す。",
                "",
            ]
        )
    (session_dir / "Googleスライド編集用アウトライン.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def short_labels(slide: Slide) -> list[str]:
    labels: list[str] = []
    generic_headers = {
        "---",
        "なし",
        "内容",
        "使い道",
        "NG例",
        "OK例",
        "原則",
        "ケース",
        "パターン",
        "業種",
        "項目",
        "列名",
        "ステップ",
        "入力元",
        "設問タイプ",
        "手段",
        "成果物",
        "回",
        "図解パターン",
        "テンプレートID",
        "スクリーンショット",
    }

    def add(label: str) -> None:
        label = clean_markdown(label)
        label = re.sub(r"[。:：].*$", "", label).strip()
        label = re.sub(r"（.*?）|\(.*?\)", "", label).strip()
        if not label or label in generic_headers:
            return
        if any(token in label for token in ("@", "株式会社", "○○", "太郎", "花子")):
            return
        if len(label) > 34:
            return
        if label not in labels:
            labels.append(label)

    for match in re.finditer(r"^\*\*内容ブロック[^:：]*[:：]\s*([^*]+)\*\*$", slide.body, re.MULTILINE):
        add(match.group(1))
    for line in slide.body.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and "---" not in stripped:
            cells = [clean_markdown(cell) for cell in stripped.strip("|").split("|")]
            for cell in cells[:2]:
                add(cell)
        elif stripped.startswith("- "):
            if re.match(r"^-\s+\*\*(図解パターン|テンプレートID|スクリーンショット):\*\*", stripped):
                continue
            add(stripped)
    source = f"{slide.title}\n{slide.headline}\n{slide.body}"
    for match in re.finditer(r"「([^」]{1,14})」", source):
        add(match.group(1))
    return labels[:20]


def is_section_transition(slide: Slide) -> bool:
    return "章見出し" in slide.title


def section_context(slide: Slide, sections: list[SectionRange]) -> tuple[int, SectionRange | None, SectionRange | None, SectionRange | None]:
    for idx, section in enumerate(sections):
        if section.name == slide.section or section.start <= slide.number <= section.end:
            previous = sections[idx - 1] if idx > 0 else None
            next_section = sections[idx + 1] if idx + 1 < len(sections) else None
            return idx, previous, section, next_section
    return -1, None, None, None


def section_transition_labels(slide: Slide, sections: list[SectionRange]) -> list[str]:
    idx, previous, current, next_section = section_context(slide, sections)
    if not current:
        return ["現在地", slide.section, "次の章", "ここから切り替え"]
    labels = [
        "現在地",
        f"{idx + 1}/{len(sections)}",
        current.name,
        f"S{current.start:02d}-S{current.end:02d}",
    ]
    if current.minutes:
        labels.append(current.minutes)
    if previous:
        labels += ["前の章", previous.name]
    if next_section:
        labels += ["次の章", next_section.name]
    else:
        labels += ["次の章", "まとめ・実務へ接続"]
    return labels


def section_transition_source_text(slide: Slide, sections: list[SectionRange]) -> str:
    idx, previous, current, next_section = section_context(slide, sections)
    if not current:
        return f"現在章: {slide.section}\n次に扱う内容が分かる目次切り替えスライドにする。"
    lines = [
        "このスライドは目次切り替え専用。通常解説スライドより情報量を減らす。",
        f"現在章: {idx + 1}/{len(sections)} {current.name}",
        f"現在章の範囲: S{current.start:02d}-S{current.end:02d}",
    ]
    if current.minutes:
        lines.append(f"時間目安: {current.minutes}")
    if previous:
        lines.append(f"前の章: {previous.name}")
    lines.append(f"次の章: {next_section.name if next_section else 'まとめ・実務への接続'}")
    lines.extend(
        [
            "表示優先度: 現在章を最も大きく、次の章を次に大きく、前の章は小さく薄いチップで表示する。",
            "表示要素は6〜8個程度まで。長い説明、比較表、チェックリスト、複数カード、業種別例は入れない。",
            f"上部ヘッドラインの意味: {slide.headline}",
        ]
    )
    return "\n".join(lines)


def diagram_source_text(slide: Slide, max_chars: int = 3000) -> str:
    lines = [f"ヘッドライン: {slide.headline}"]
    for raw in slide.body.splitlines():
        stripped = raw.rstrip()
        if not stripped:
            continue
        if stripped.startswith("**ヘッドライン:**"):
            continue
        if stripped.startswith("- **図解パターン:**"):
            continue
        if stripped.startswith("- **テンプレートID:**"):
            continue
        if stripped.startswith("- **スクリーンショット:**"):
            continue
        lines.append(stripped)
    text = "\n".join(lines).strip()
    text = re.sub(r"```[a-zA-Z0-9_-]*", "コード例:", text)
    text = text.replace("```", "")
    text = text.replace("田中 太郎（顧客名）", "顧客A")
    text = text.replace("佐藤 一郎", "顧客A")
    text = text.replace("株式会社○○", "架空会社A")
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "\n（以降は元スライド案の同S番号を参照）"


def write_diagram_prompts(session_dir: Path, slides: list[Slide], sections: list[SectionRange]) -> None:
    no = session_no(session_dir)
    session_title = SESSION_TITLES.get(no, session_dir.name.split("-", 1)[-1])
    generated_at = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    lines = [
        f"# 第{int(no)}回 図解パーツ生成プロンプト",
        "",
        f"- 生成日時: {generated_at}",
        f"- 講座名: {COURSE_TITLE}",
        f"- セッション/テキスト名: 第{int(no)}回 {session_title}",
        "- 用途: HTML/Google Slides上で編集可能な講座名・回・S番号・タイトル・ヘッドラインを残したうえで、スライド本文の情報量を落とさない横長資料画像を1枚ずつ生成する。",
        "- 生成サイズ: 全スライド共通で1536×1024（横3:2）。1枚ごとにサイズや縦横比を変えない。全ページ同一の図解ゾーン（600×322pt・約1.86:1）へ一括配置されるため、横に少し引き伸ばされる前提で平たく横長の構図にする。",
        "- 上部余白: 画像上部約20%は白余白として空ける。テンプレートが編集可能なタイトルとヘッドラインをその位置に重ねる。下端にも小さな余白を残す（すぐ下に目次ストリップが来る）。",
        "- 保存先: 生成・検品済みPNGを `図解パーツ/Sxx.png` として保存し、HTML/Google Slidesテンプレートへ添付する。",
        "- 重要: 講座名、セッション名、S番号、セクション名、スピーカーノート、長い段落は画像内に固定しない。比較表、プロセス表、判断表、業種別例など元スライドの中核となる短いセル文は画像内に入れてよい。",
        "- 画像内テキスト: 文字なし固定は禁止。役割名・プロセス名・成果物名・判断軸・手順・確認観点・具体例を、見出し、表セル、カード内説明として入れる。",
        "- 密度基準: 元の全面スライド画像/スライド案にある判断軸、成果物、手順、リスク、確認観点、具体例を落とさない。S04のようなスライドでは、Before/After表、階層図、業種別例を1枚に併置し、2〜4領域・8〜20個程度の読める見出し/セル/短文を入れる。短いラベルだけの抽象図にしない。",
        "- 例外: `章見出し/現在位置` または `章見出し` の目次切り替えスライドだけは、ユーザー指示により情報量を減らす。現在の目次項目を最も大きく、次の目次項目を次に大きく、前後関係と進捗だけを見せる。通常解説用の比較表・詳細カード・業種別例は入れない。",
        "- 添付ルール: 生成後は `--embed-diagram-parts` でテンプレートへ挿入する。未生成・未添付・文字なしの飾り画像は完成扱いにしない。",
        "- 共通画風: `isometric-corporate-clean`。白背景、ネイビー/ティール、薄いグレー罫線、法人研修向け、公式ロゴや実在UIを想像生成しない。",
        "",
        "## 共通ネガティブプロンプト",
        "",
        "```text",
        "Do not create the editable template chrome. Do not render course title, session title, slide number, section header, speaker notes, long paragraph dumps, fake Google logos, fake Google UI, real personal data, email addresses, phone numbers, prices, QR codes, placeholder boxes, unreadable or incorrect Japanese, recruitment-ad or poster layouts, dramatic manga advertising, decorative dark backgrounds, or text areas meant to be filled later. The output is a dense supplemental diagram/reference-sheet image. Do not make it text-free, icon-only, or short-label-only; use readable Japanese headings, table cells, card text, and examples. If a comparison table or example table is the core source information, preserve it as visible structured text.",
        "```",
        "",
    ]
    for slide in slides:
        transition_slide = is_section_transition(slide)
        labels = " / ".join(section_transition_labels(slide, sections) if transition_slide else short_labels(slide))
        labels = labels or "入力 / 処理 / 出力 / 確認"
        source_text = section_transition_source_text(slide, sections) if transition_slide else diagram_source_text(slide)
        transition_instruction = [
            "This is a chapter/agenda transition visual. The latest user instruction explicitly says to reduce information only at agenda-change timing.",
            "Make the current agenda item the dominant visual: huge central Japanese text, with a clear progress mark such as 1/6 or 3/7.",
            "Show the next agenda item clearly as the second-largest element, preferably on the right or lower-right with an arrow or '次は'.",
            "Show the previous agenda item only as a small muted chip when available. Use a simple left-to-right transition feel.",
            "Do not use detailed comparison tables, many content cards, checklists, industry examples, or dense learner-output blocks on this slide.",
            "Use only about 6-8 readable text elements. The purpose is to make the section switch obvious at a glance.",
        ] if transition_slide else [
            "Create a dense supplemental image, not a decorative icon. Use 2-4 structured zones such as a comparison table, process table, hierarchy diagram, checklist, decision canvas, output map, or industry-example list according to the source slide. Preserve the source slide's key information density by showing the main judgment axis, learner action, output, concrete examples, and review/risk point when they exist.",
            "Visible text inside the image: include readable Japanese headings, table cells, card text, and concrete examples, not only labels. For dense source slides, use roughly 8-20 readable text cells/short phrases across the image. Keep text readable at slide size; numeric notes such as `5〜8個` or `10個以内` are allowed. Avoid long paragraphs, but do not remove core Before/After rows, process steps, hierarchy levels, or industry examples.",
        ]
        opening_instruction = (
            "Create one simple agenda-transition reference image for a Japanese business training slide template."
            if transition_slide
            else "Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template."
        )
        source_instruction = (
            "Agenda transition source context. Use only the current, previous, next, progress, and time labels needed to make location obvious at a glance:"
            if transition_slide
            else "Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:"
        )
        lines.extend(
            [
                f"## {slide.slide_id} {slide.title}",
                "",
                f"- セクション: {slide.section}",
                f"- スライド側ヘッドライン（画像内には原則入れない）: {slide.headline}",
                f"- 推奨図解パターン: {slide.diagram_pattern}",
                f"- 参照素材・スクリーンショット: {slide.screenshot}",
                "",
                "```text",
                opening_instruction,
                "Canvas: clean white, landscape 1536x1024 (3:2). The image is placed into a fixed 600x322pt zone (about 1.86:1) on every slide, so it will be displayed slightly wider than generated; prefer flat, wide, horizontal compositions and avoid shapes whose meaning depends on being perfectly round or square.",
                "Reserve the top 20 percent of the canvas as clean empty white space: the editable template overlays the slide title and headline there. Compose all diagram content in the lower 80 percent, and keep a small clean margin along the bottom edge because the deck's chapter strip sits just below the image.",
                "Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.",
                f"Context only, do not render visible header text: {COURSE_TITLE} / 第{int(no)}回 {session_title} / {slide.slide_id} / {slide.section}.",
                f"Slide topic for context: {slide.title}.",
                f"Concept to visualize: {slide.headline}.",
                f"Suggested visual pattern: {slide.diagram_pattern}.",
                source_instruction,
                source_text,
                (
                    f"Visible text candidates to use, keeping the transition simple and not dense: {labels}."
                    if transition_slide
                    else f"Visible text candidates to use when useful, without reducing the source density: {labels}."
                ),
                *transition_instruction,
                (
                    "The editable Google Slides template will manage the course title, session title, S-number, section header/current position, and full slide title. The generated transition image should stay visually simple: big current agenda item, clear next agenda item, small previous chip, and a compact progress indicator."
                    if transition_slide
                    else "The editable Google Slides template will manage the course title, session title, S-number, section header/current position, and full slide title. The generated image may include its own concise content heading and the dense table/canvas text needed to understand the material, but it should not consume the title/header area like a full-slide screenshot."
                ),
                "If the slide needs official screenshots or logos, leave the diagram generic and do not invent real Google UI or brand marks.",
                "```",
                "",
                "ネガティブプロンプト:",
                "",
                "```text",
                (
                    "Do not include the editable deck header/footer, S-number, course title, session title, section header, fake Google logos or UI, personal data, placeholders, empty dashed frames, poster/recruitment/ad layouts, unreadable small text, incorrect Japanese, dense comparison tables, many content cards, industry-example lists, or long explanations. This is an agenda transition slide: keep it simple and make the current/next agenda items large and obvious."
                    if transition_slide
                    else "Do not include the editable deck header/footer, S-number, course title, session title, section header, fake Google logos or UI, personal data, placeholders, empty dashed frames, poster/recruitment/ad layouts, unreadable small text, incorrect Japanese, text-free decorative icon-only output, or short-label-only output with no explanation. Avoid long paragraph dumps and speaker notes. Use readable Japanese headings, table cells, card text, and examples as dense supplemental information."
                ),
                "```",
                "",
            ]
        )
    (session_dir / "図解パーツ生成プロンプト.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def scan_warnings(session_dir: Path, slides: list[Slide]) -> list[str]:
    no = session_no(session_dir)
    current = int(no)
    max_slide = max((slide.number for slide in slides), default=0)
    warnings: list[str] = []
    seen = [slide.number for slide in slides]
    expected = list(range(1, max(seen) + 1)) if seen else []
    missing = sorted(set(expected) - set(seen))
    if missing:
        warnings.append(f"欠番: {', '.join(f'S{n:02d}' for n in missing)}")
    duplicates = sorted({n for n in seen if seen.count(n) > 1})
    if duplicates:
        warnings.append(f"重複: {', '.join(f'S{n:02d}' for n in duplicates)}")
    cross_slide_patterns = [
        re.compile(r"(第|セッション)\s*([1-6])\s*回?\s*[-ー:：]?\s*S(\d{2})"),
        re.compile(r"S(\d{2})\s*[-ー:：]?\s*(第|セッション)\s*([1-6])\s*回?"),
    ]
    for slide in slides:
        text = slide.body + "\n" + slide.title
        overview_or_transition = any(
            token in text
            for token in ("ロードマップ", "つながり", "対応表", "前回", "次回", "橋渡し", "準備")
        )
        for pattern in cross_slide_patterns:
            for match in pattern.finditer(text):
                found = int(match.group(2) if match.re.pattern.startswith("(第") else match.group(3))
                if found == current:
                    continue
                if slide.number <= 6 and overview_or_transition:
                    continue
                if found == current + 1 and slide.number >= max_slide - 1 and overview_or_transition:
                    continue
                warnings.append(f"{slide.slide_id}: 別回スライド混入の可能性 `{match.group(0)}`")
    return warnings


def write_course_report(session_results: list[tuple[Path, list[Slide], list[SectionRange], list[str]]]) -> None:
    generated_at = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    lines = [
        "# Google Slides編集可能化 整合性レポート",
        "",
        f"- 生成日時: {generated_at}",
        f"- 対象講座: {COURSE_TITLE}",
        "- 方針: 情報量は維持し、審査上必要なヘッダー、セクション、テキスト名、S番号をGoogle Slides上の編集可能テキストとして統一する。",
        "",
        "## 回別サマリー",
        "",
        "| 回 | セッション/テキスト名 | スライド数 | セクション数 | 生成ファイル | 警告 |",
        "| ---: | --- | ---: | ---: | --- | --- |",
    ]
    for session_dir, slides, sections, warnings in session_results:
        no = session_no(session_dir)
        session_title = SESSION_TITLES.get(no, session_dir.name.split("-", 1)[-1])
        files = "`Googleスライド編集用アウトライン.md`, `図解パーツ生成プロンプト.md`"
        warning_text = "<br>".join(warnings) if warnings else "なし"
        lines.append(f"| {int(no)} | {session_title} | {len(slides)} | {len(sections)} | {files} | {warning_text} |")
    lines.extend(
        [
            "",
            "## 再申請前の重点確認",
            "",
            "- 各回Google Slidesで、講座名、セッション/テキスト名、S番号、セクション名が全ページ同じ位置に出ること。",
            "- `Googleスライド編集用アウトライン.md` の本文ブロックをGoogle Slides上の編集可能テキストとして配置すること。",
            "- `図解パーツ生成プロンプト.md` は補助図解だけに使い、全面スライド画像を再生成する用途に使わないこと。",
            "- 第3回の次回予告は最後のまとめ/準備スライドだけに限定し、本文途中に第4回スライドが混入したような構成にしないこと。",
            "- パンフレット、詳細シラバス、Web掲載用カリキュラム、Google Slidesのテキスト名と成果物名を突合すること。",
        ]
    )
    out_path = COURSE_DIR / "全体" / "Google_Slides編集可能化_整合性レポート.md"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--session",
        default=None,
        help="対象セッション番号（例: 01）。省略時は全セッションを再生成する。",
    )
    args = parser.parse_args()
    if not COURSE_DIR.is_dir():
        raise SystemExit(f"Missing course dir: {COURSE_DIR}")
    session_results: list[tuple[Path, list[Slide], list[SectionRange], list[str]]] = []
    for session_dir in sorted(p for p in COURSE_DIR.iterdir() if p.is_dir() and re.match(r"\d{2}-", p.name)):
        if args.session and session_no(session_dir) != args.session:
            continue
        slides, sections = build_slide_objects(session_dir)
        write_editable_outline(session_dir, slides, sections)
        write_diagram_prompts(session_dir, slides, sections)
        session_results.append((session_dir, slides, sections, scan_warnings(session_dir, slides)))
    if not args.session:
        write_course_report(session_results)


if __name__ == "__main__":
    main()
