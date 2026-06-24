#!/usr/bin/env python3
"""Build editable Google Slides source outlines and diagram-part prompts.

This script does not create final slide images. It keeps slide text editable in
Google Slides and limits image prompts to supplemental diagram parts.
"""

from __future__ import annotations

import datetime as dt
import re
from dataclasses import dataclass
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
        sections.append(SectionRange(name=name, start=int(match.group(1)), end=int(match.group(2))))
    return sections


def section_for(slide_no: int, sections: list[SectionRange]) -> str:
    for section in sections:
        if section.start <= slide_no <= section.end:
            return section.name
    return "未設定セクション"


def field_value(body: str, label: str) -> str:
    pattern = rf"^\*\*{re.escape(label)}:\*\*\s*(.+)$"
    match = re.search(pattern, body, re.MULTILINE)
    return clean_cell(match.group(1)) if match else ""


def parse_slides(text: str) -> list[tuple[int, str, str]]:
    matches = list(re.finditer(r"^### S(\d{2})\s+(.+)$", text, re.MULTILINE))
    slides: list[tuple[int, str, str]] = []
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        slides.append((int(match.group(1)), clean_cell(match.group(2)), text[start:end].strip()))
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
        "- 図解: `図解パーツ生成プロンプト.md` で作った `図解パーツ/Sxx.png`、公式素材、または安全なスクリーンショットを本文の補助として配置する。",
        "",
        "## 共通ヘッダー",
        "",
        "| 位置 | 表示テキスト |",
        "| --- | --- |",
        f"| 左上1行目 | {COURSE_TITLE} |",
        f"| 左上2行目 | 第{int(no)}回 {session_title} |",
        "| 右上1行目 | Sxx |",
        "| 右上2行目 | セクション名 |",
        "",
        "## セクション",
        "",
        "| セクション | スライド範囲 |",
        "| --- | --- |",
    ]
    if sections:
        for section in sections:
            lines.append(f"| {section.name} | S{section.start:02d}-S{section.end:02d} |")
    else:
        lines.append("| 要確認 | スライド案.mdの120分時間配分表から補完 |")
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
                "- タイトルとヘッドラインは上部に固定する。",
                "- 本文ブロックはカード、表、プロセス、チェックリストとしてGoogle Slides上に配置する。",
        "- 図解パーツは本文を置き換えず、中央または右側の補助ビジュアルとして配置する。画像内に講座名、S番号、本文長文を固定しない。",
                "- 演習、成果物、確認観点、リスクは下部帯に残す。",
                "",
            ]
        )
    (session_dir / "Googleスライド編集用アウトライン.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def short_labels(slide: Slide) -> list[str]:
    labels = [slide.title, slide.headline]
    for match in re.finditer(r"\*\*内容ブロック[^*]*\*\*\s*\n([^\n]+)", slide.body):
        labels.append(clean_cell(match.group(1)).lstrip("- "))
    return [label for label in labels if label][:5]


def write_diagram_prompts(session_dir: Path, slides: list[Slide]) -> None:
    no = session_no(session_dir)
    session_title = SESSION_TITLES.get(no, session_dir.name.split("-", 1)[-1])
    generated_at = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    lines = [
        f"# 第{int(no)}回 図解パーツ生成プロンプト",
        "",
        f"- 生成日時: {generated_at}",
        f"- 講座名: {COURSE_TITLE}",
        f"- セッション/テキスト名: 第{int(no)}回 {session_title}",
        "- 用途: Google Slides上で編集可能テキストを配置したうえで、補助図解だけを1枚ずつ画像生成する。",
        "- 保存先: 生成・検品済みPNGを `図解パーツ/Sxx.png` として保存し、Google Slidesへ埋め込む。",
        "- 重要: 講座名、セッション名、S番号、セクション名、本文長文、表本文は画像内に固定しない。Google Slides側のテキストボックスで管理する。",
        "- 画像内テキスト: 文字なし固定ではない。図解の理解に必要な場合は、スライド本文と矛盾しない短い日本語ラベルだけを画像内に入れてよい。",
        "- 共通画風: `isometric-corporate-clean`。白背景、ネイビー/ティール、薄いグレー罫線、法人研修向け、公式ロゴや実在UIを想像生成しない。",
        "",
        "## 共通ネガティブプロンプト",
        "",
        "```text",
        "Do not create a full finished slide. Do not render course title, session title, slide number, section header, full slide title, full headline, long body text, full tables, speaker notes, fake Google logos, fake Google UI, real personal data, email addresses, phone numbers, prices, QR codes, placeholder boxes, unreadable or incorrect Japanese, recruitment-ad or poster layouts, dramatic manga advertising, decorative dark backgrounds, or text areas meant to be filled later. The output is a supplemental diagram part only. Short Japanese labels are allowed only when they clarify the diagram.",
        "```",
        "",
    ]
    for slide in slides:
        labels = " / ".join(short_labels(slide))
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
                "Create one supplemental isometric corporate diagram part for a Japanese business training Google Slides page.",
                "Canvas should be clean white with generous margins, usable as a center/right-side visual asset inside an editable Google Slides layout.",
                "Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.",
                f"Context only, do not render visible header text: {COURSE_TITLE} / 第{int(no)}回 {session_title} / {slide.slide_id} / {slide.section}.",
                f"Slide topic for context: {slide.title}.",
                f"Concept to visualize: {slide.headline}.",
                f"Suggested visual pattern: {slide.diagram_pattern}.",
                f"Context-only wording for choosing optional short labels; do not render this full wording as visible text: {labels}.",
                "Visible text inside the image: optional. Use no text when icons and process shapes are enough. If labels improve clarity, include only 1-4 short Japanese labels such as role names, process verbs, or output names, preferably under 8 Japanese characters each. Do not use full titles or sentences.",
                "The main slide title, headline, body cards, tables, exercise instructions, and slide number will be editable Google Slides text, so do not bake them into the image.",
                "If the slide needs official screenshots or logos, leave the diagram generic and do not invent real Google UI or brand marks.",
                "```",
                "",
                "ネガティブプロンプト:",
                "",
                "```text",
                "Do not create a complete slide, do not include a header/footer, do not include S-number, do not include course title, session title, section header, full title, full headline, long body text, full tables, fake Google logos or UI, personal data, placeholders, empty dashed frames, poster/recruitment/ad layouts, unreadable small text, or incorrect Japanese. Short accurate labels are allowed only when useful.",
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
    if not COURSE_DIR.is_dir():
        raise SystemExit(f"Missing course dir: {COURSE_DIR}")
    session_results: list[tuple[Path, list[Slide], list[SectionRange], list[str]]] = []
    for session_dir in sorted(p for p in COURSE_DIR.iterdir() if p.is_dir() and re.match(r"\d{2}-", p.name)):
        slides, sections = build_slide_objects(session_dir)
        write_editable_outline(session_dir, slides, sections)
        write_diagram_prompts(session_dir, slides)
        session_results.append((session_dir, slides, sections, scan_warnings(session_dir, slides)))
    write_course_report(session_results)


if __name__ == "__main__":
    main()
