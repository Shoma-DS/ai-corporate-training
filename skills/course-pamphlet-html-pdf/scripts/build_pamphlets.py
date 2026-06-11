#!/usr/bin/env python3
"""Build course pamphlet HTML and PDF files for the AI法人研修 repo."""

from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
COURSES_DIR = ROOT / "講座"
WHOLE_DIR = "全体"
HTML_NAME = "パンフレット.html"
PDF_NAME = "パンフレット.pdf"
LEGACY_MD_NAMES = ("パンフレット原稿.md", "パンフレット.md")
PDF_CONVERTER = Path(__file__).resolve().with_name("html_to_pdf.py")


def pamphlet_html_path(whole_dir: Path) -> Path:
    """講座名付きの `<講座名>_パンフレット.html` を正とし、旧 `パンフレット.html` にフォールバックする。"""
    named = whole_dir / f"{whole_dir.parent.name}_{HTML_NAME}"
    if named.exists():
        return named
    legacy = whole_dir / HTML_NAME
    if legacy.exists():
        return legacy
    return named


@dataclass(frozen=True)
class PamphletTarget:
    whole_dir: Path
    markdown_path: Path | None
    html_path: Path
    pdf_path: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate <講座名>_パンフレット.html and <講座名>_パンフレット.pdf from course pamphlet sources."
    )
    parser.add_argument(
        "--course-dir",
        action="append",
        default=[],
        help="Course directory such as 講座/COURSE. Can be passed multiple times.",
    )
    parser.add_argument(
        "--input-md",
        action="append",
        default=[],
        help="Specific legacy Markdown pamphlet source to convert.",
    )
    parser.add_argument(
        "--input-html",
        action="append",
        default=[],
        help="Specific pamphlet HTML source to convert to PDF.",
    )
    parser.add_argument("--no-pdf", action="store_true", help="Only build HTML.")
    parser.add_argument("--force-md", action="store_true", help="Regenerate HTML even when it is newer than Markdown.")
    parser.add_argument("--force-pdf", action="store_true", help="Regenerate PDF even when it is newer than HTML.")
    parser.add_argument("--browser", help="Browser executable for html_to_pdf.py.")
    parser.add_argument("--wait-ms", type=int, default=1000, help="Wait before printing PDF. Default: 1000.")
    return parser.parse_args()


def resolve_path(raw: str) -> Path:
    path = Path(raw).expanduser()
    if not path.is_absolute():
        path = ROOT / path
    return path.resolve()


def discover_targets(args: argparse.Namespace) -> list[PamphletTarget]:
    targets: dict[Path, PamphletTarget] = {}

    def add_whole_dir(whole_dir: Path, markdown_path: Path | None = None) -> None:
        whole_dir = whole_dir.resolve()
        html_path = pamphlet_html_path(whole_dir)
        if markdown_path is None:
            for name in LEGACY_MD_NAMES:
                candidate = whole_dir / name
                if candidate.exists():
                    markdown_path = candidate
                    break
        if markdown_path is None and not html_path.exists():
            return
        targets[whole_dir] = PamphletTarget(
            whole_dir=whole_dir,
            markdown_path=markdown_path.resolve() if markdown_path else None,
            html_path=html_path,
            pdf_path=html_path.with_suffix(".pdf"),
        )

    for raw in args.course_dir:
        course_dir = resolve_path(raw)
        whole_dir = course_dir / WHOLE_DIR if course_dir.name != WHOLE_DIR else course_dir
        add_whole_dir(whole_dir)

    for raw in args.input_md:
        markdown_path = resolve_path(raw)
        add_whole_dir(markdown_path.parent, markdown_path)

    for raw in args.input_html:
        html_path = resolve_path(raw)
        whole_dir = html_path.parent
        targets[whole_dir] = PamphletTarget(
            whole_dir=whole_dir,
            markdown_path=None,
            html_path=html_path,
            pdf_path=html_path.with_suffix(".pdf"),
        )

    if not targets:
        for whole_dir in sorted(COURSES_DIR.glob(f"*/{WHOLE_DIR}")):
            add_whole_dir(whole_dir)

    return sorted(targets.values(), key=lambda target: str(target.whole_dir))


def needs_rebuild(source: Path, output: Path, *, force: bool) -> bool:
    if force or not output.exists():
        return True
    return source.stat().st_mtime >= output.stat().st_mtime


def plain_heading(line: str) -> str:
    return line.lstrip("#").strip()


def extract_title_and_subtitle(markdown_text: str, markdown_path: Path) -> tuple[str, str]:
    title = ""
    subtitle = ""
    for raw_line in markdown_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("# "):
            heading = plain_heading(line)
            if ":" in heading:
                maybe_title = heading.split(":", 1)[1].strip()
                if maybe_title:
                    title = maybe_title
            elif "パンフレット原稿" not in heading:
                title = heading
            continue
        if line.startswith("## ") and not title:
            heading = plain_heading(line)
            if "パンフレット原稿" not in heading:
                title = heading
            continue
        if not line.startswith("#") and not subtitle:
            subtitle = line
            break

    if not title:
        title = markdown_path.parent.parent.name
    return title, subtitle


def render_inline(value: str) -> str:
    escaped = html.escape(value.strip())
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    return escaped


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def render_table(lines: list[str]) -> str:
    rows = [split_table_row(line) for line in lines]
    header: list[str] | None = None
    body_rows = rows
    if len(rows) >= 2 and is_separator_row(rows[1]):
        header = rows[0]
        body_rows = rows[2:]

    out = ["<table>"]
    if header:
        out.append("<thead><tr>")
        out.extend(f"<th>{render_inline(cell)}</th>" for cell in header)
        out.append("</tr></thead>")
    out.append("<tbody>")
    for row in body_rows:
        out.append("<tr>")
        out.extend(f"<td>{render_inline(cell)}</td>" for cell in row)
        out.append("</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def render_markdown_blocks(markdown_text: str, title: str, subtitle: str) -> str:
    lines = markdown_text.splitlines()
    parts: list[str] = []
    index = 0
    skipped_intro_section = False
    skipped_title_heading = False
    skipped_subtitle = False

    while index < len(lines):
        raw_line = lines[index]
        line = raw_line.strip()
        if not line:
            index += 1
            continue

        if line.startswith("## "):
            heading = plain_heading(line)
            if re.search(r"タイトル.*訴求", heading):
                skipped_intro_section = True
                index += 1
                continue
            skipped_intro_section = False
            if heading == title and not skipped_title_heading:
                skipped_title_heading = True
                index += 1
                continue
            parts.append(f"<h2>{render_inline(heading)}</h2>")
            index += 1
            continue

        if skipped_intro_section:
            index += 1
            continue

        if line.startswith("# "):
            index += 1
            continue

        if line.startswith("### "):
            parts.append(f"<h3>{render_inline(plain_heading(line))}</h3>")
            index += 1
            continue

        if line.startswith("|") and "|" in line[1:]:
            table_lines = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index].strip())
                index += 1
            parts.append(render_table(table_lines))
            continue

        if line.startswith("- "):
            items = []
            while index < len(lines) and lines[index].strip().startswith("- "):
                items.append(lines[index].strip()[2:])
                index += 1
            parts.append("<ul>")
            parts.extend(f"<li>{render_inline(item)}</li>" for item in items)
            parts.append("</ul>")
            continue

        paragraph_lines = []
        while index < len(lines):
            candidate = lines[index].strip()
            if not candidate:
                index += 1
                break
            if candidate.startswith(("#", "- ", "|")):
                break
            paragraph_lines.append(candidate)
            index += 1
        paragraph = " ".join(paragraph_lines)
        if paragraph == subtitle and not skipped_subtitle:
            skipped_subtitle = True
            continue
        if paragraph.endswith(":"):
            parts.append(f"<p class=\"label\">{render_inline(paragraph)}</p>")
        else:
            parts.append(f"<p>{render_inline(paragraph)}</p>")

    return "\n".join(parts)


def extract_chips(markdown_text: str) -> list[str]:
    candidates = []
    patterns = [
        r"標準学習時間[:：]\s*([^\n]+)",
        r"提供方式[:：]\s*([^\n]+)",
        r"形式[:：]\s*([^\n]+)",
        r"受講管理[:：]\s*([^\n]+)",
        r"(6回、各120分、合計約12時間)",
    ]
    for pattern in patterns:
        match = re.search(pattern, markdown_text)
        if match:
            candidates.append(match.group(1).strip("- "))
    if not candidates:
        candidates.extend(["法人向け研修", "実務アウトプット重視", "LMS受講管理"])
    return candidates[:4]


def build_html(markdown_path: Path) -> str:
    markdown_text = markdown_path.read_text(encoding="utf-8")
    title, subtitle = extract_title_and_subtitle(markdown_text, markdown_path)
    body = render_markdown_blocks(markdown_text, title, subtitle)
    chips = "\n".join(f"<span>{render_inline(chip)}</span>" for chip in extract_chips(markdown_text))
    subtitle_html = f"<p class=\"cover-lead\">{render_inline(subtitle)}</p>" if subtitle else ""
    source_name = html.escape(markdown_path.name)

    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    @page {{
      size: A4;
      margin: 12mm;
    }}

    :root {{
      --ink: #172033;
      --muted: #5d6878;
      --line: #d7e1ec;
      --navy: #123a5a;
      --blue: #2876a8;
      --teal: #1f9f9a;
      --orange: #f0a04b;
      --paper: #ffffff;
      --soft: #f4f8fb;
    }}

    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      color: var(--ink);
      background: #edf1f5;
      font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Yu Gothic", "YuGothic", "Noto Sans JP", sans-serif;
      line-height: 1.62;
      letter-spacing: 0;
    }}

    .pamphlet {{
      width: 210mm;
      min-height: 297mm;
      margin: 0 auto;
      background: var(--paper);
      box-shadow: 0 12px 34px rgba(24, 39, 56, .15);
    }}

    .cover {{
      min-height: 104mm;
      padding: 18mm 18mm 14mm;
      color: #ffffff;
      background:
        linear-gradient(135deg, rgba(18, 58, 90, .98), rgba(18, 58, 90, .86) 52%, rgba(31, 159, 154, .88)),
        linear-gradient(45deg, #f9fbfd, #dcecf8);
      break-after: avoid-page;
    }}

    .eyebrow {{
      margin: 0 0 14px;
      color: #cfe9ff;
      font-size: 11px;
      font-weight: 800;
    }}

    h1 {{
      width: 86%;
      margin: 0 0 14px;
      font-size: 30px;
      line-height: 1.22;
      letter-spacing: 0;
    }}

    .cover-lead {{
      width: 88%;
      margin: 0 0 18px;
      font-size: 13px;
      font-weight: 700;
    }}

    .chips {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 12px;
    }}

    .chips span {{
      border: 1px solid rgba(255, 255, 255, .48);
      background: rgba(255, 255, 255, .12);
      padding: 5px 8px;
      font-size: 9.5px;
      font-weight: 800;
    }}

    .content {{
      padding: 14mm 18mm 18mm;
    }}

    h2 {{
      margin: 18px 0 8px;
      padding-left: 9px;
      border-left: 5px solid var(--orange);
      color: var(--navy);
      font-size: 17px;
      line-height: 1.3;
      break-after: avoid;
    }}

    h3 {{
      margin: 12px 0 6px;
      color: var(--ink);
      font-size: 12.5px;
      break-after: avoid;
    }}

    p {{
      margin: 0 0 8px;
      font-size: 10.2px;
    }}

    .label {{
      margin-top: 10px;
      margin-bottom: 3px;
      color: var(--blue);
      font-weight: 800;
    }}

    ul {{
      margin: 5px 0 10px 18px;
      padding: 0;
      font-size: 9.8px;
    }}

    li {{
      margin: 3px 0;
    }}

    table {{
      width: 100%;
      margin: 8px 0 13px;
      border-collapse: collapse;
      font-size: 8.7px;
      break-inside: avoid;
    }}

    th {{
      border: 1px solid #b9d2e4;
      background: #d9ebf6;
      color: var(--navy);
      padding: 5px 6px;
      text-align: left;
      font-weight: 800;
    }}

    td {{
      border: 1px solid var(--line);
      padding: 5px 6px;
      vertical-align: top;
    }}

    code {{
      padding: 1px 4px;
      border: 1px solid #dce5ef;
      background: #f7fbff;
      color: #294057;
      font-family: "SFMono-Regular", Consolas, monospace;
      font-size: .92em;
    }}

    .source-note {{
      margin-top: 18px;
      padding-top: 6px;
      border-top: 1px solid #e4ebf2;
      color: var(--muted);
      font-size: 8.2px;
    }}

    @media print {{
      body {{
        background: #ffffff;
      }}

      .pamphlet {{
        width: auto;
        min-height: auto;
        margin: 0;
        box-shadow: none;
      }}
    }}
  </style>
</head>
<body>
  <main class="pamphlet">
    <section class="cover">
      <p class="eyebrow">AI法人研修 / 法人向け研修パンフレット</p>
      <h1>{html.escape(title)}</h1>
      {subtitle_html}
      <div class="chips">
        {chips}
      </div>
    </section>
    <section class="content">
      {body}
      <p class="source-note">生成元: {source_name}。価格、申込先、助成率、申請期限など変わり得る情報は固定せず、提出前に最新情報を確認してください。</p>
    </section>
  </main>
</body>
</html>
"""


def write_html_from_markdown(target: PamphletTarget, *, force: bool) -> bool:
    if target.markdown_path is None:
        return False
    if not needs_rebuild(target.markdown_path, target.html_path, force=force):
        return False
    target.html_path.write_text(build_html(target.markdown_path), encoding="utf-8")
    print(f"HTML {target.html_path.relative_to(ROOT)}")
    return True


def write_pdf(target: PamphletTarget, args: argparse.Namespace) -> bool:
    if args.no_pdf:
        return False
    if not target.html_path.exists():
        print(f"skip PDF, HTML missing: {target.html_path}", file=sys.stderr)
        return False
    if not needs_rebuild(target.html_path, target.pdf_path, force=args.force_pdf):
        return False

    command = [
        sys.executable,
        str(PDF_CONVERTER),
        str(target.html_path),
        "--output",
        str(target.pdf_path),
        "--wait-ms",
        str(args.wait_ms),
    ]
    if args.browser:
        command.extend(["--browser", args.browser])
    subprocess.run(command, check=True)
    return True


def main() -> int:
    args = parse_args()
    targets = discover_targets(args)
    if not targets:
        print("No pamphlet sources found.", file=sys.stderr)
        return 1

    for target in targets:
        write_html_from_markdown(target, force=args.force_md)
        write_pdf(target, args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
