#!/usr/bin/env python3
"""Create a local HTML PDF preview index for pamphlet PDFs."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "書き出し" / "pdf-preview.html"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a browser-openable PDF preview page for local PDFs."
    )
    parser.add_argument(
        "pdfs",
        nargs="*",
        help="PDF files to include. Defaults to all 講座/*/全体/パンフレット.pdf files.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=str(DEFAULT_OUTPUT),
        help=f"Output HTML path. Default: {DEFAULT_OUTPUT}",
    )
    return parser.parse_args()


def find_default_pdfs() -> list[Path]:
    return sorted((ROOT / "講座").glob("*/全体/パンフレット.pdf"))


def as_file_url(path: Path) -> str:
    return path.resolve().as_uri()


def build_html(pdfs: list[Path]) -> str:
    items = []
    for pdf in pdfs:
        rel = pdf.resolve().relative_to(ROOT)
        course_name = pdf.parents[1].name
        items.append(
            {
                "label": course_name,
                "path": str(rel),
                "url": as_file_url(pdf),
            }
        )

    data_json = json.dumps(items, ensure_ascii=False)
    first_url = items[0]["url"] if items else ""
    first_label = items[0]["label"] if items else "PDFが見つかりません"

    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AI法人研修 PDF Preview</title>
  <style>
    :root {{
      --ink: #172033;
      --muted: #64748b;
      --line: #d8e2ee;
      --bg: #f4f7fb;
      --panel: #ffffff;
      --blue: #2a76a8;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      background: var(--bg);
      font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Yu Gothic", "YuGothic", "Noto Sans JP", sans-serif;
    }}
    .app {{
      display: grid;
      grid-template-columns: 320px 1fr;
      min-height: 100vh;
    }}
    aside {{
      background: var(--panel);
      border-right: 1px solid var(--line);
      padding: 18px;
    }}
    h1 {{
      margin: 0 0 4px;
      font-size: 18px;
      line-height: 1.25;
    }}
    .hint {{
      margin: 0 0 16px;
      color: var(--muted);
      font-size: 12px;
      line-height: 1.5;
    }}
    .list {{
      display: grid;
      gap: 8px;
    }}
    button {{
      width: 100%;
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      padding: 10px 11px;
      text-align: left;
      font: inherit;
      font-size: 13px;
      cursor: pointer;
    }}
    button.active {{
      border-color: var(--blue);
      background: #eaf4fb;
      font-weight: 700;
    }}
    main {{
      display: grid;
      grid-template-rows: auto 1fr;
      min-width: 0;
    }}
    .bar {{
      display: flex;
      gap: 10px;
      align-items: center;
      justify-content: space-between;
      padding: 12px 16px;
      background: #fff;
      border-bottom: 1px solid var(--line);
    }}
    .title {{
      min-width: 0;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      font-weight: 700;
    }}
    .actions {{
      display: flex;
      gap: 8px;
      flex: 0 0 auto;
    }}
    a {{
      color: var(--blue);
      text-decoration: none;
      font-size: 13px;
      font-weight: 700;
    }}
    iframe {{
      width: 100%;
      height: 100%;
      border: 0;
      background: #fff;
    }}
    .empty {{
      padding: 32px;
      color: var(--muted);
    }}
    @media (max-width: 900px) {{
      .app {{ grid-template-columns: 1fr; }}
      aside {{ border-right: 0; border-bottom: 1px solid var(--line); }}
      main {{ min-height: 75vh; }}
    }}
  </style>
</head>
<body>
  <div class="app">
    <aside>
      <h1>PDF Preview</h1>
      <p class="hint">リポジトリ内のパンフレットPDFをブラウザ内で確認します。</p>
      <div class="list" id="list"></div>
    </aside>
    <main>
      <div class="bar">
        <div class="title" id="title">{html.escape(first_label)}</div>
        <div class="actions">
          <a id="openLink" href="{html.escape(first_url)}" target="_blank" rel="noreferrer">別タブで開く</a>
        </div>
      </div>
      <iframe id="viewer" src="{html.escape(first_url)}"></iframe>
    </main>
  </div>
  <script>
    const pdfs = {data_json};
    const list = document.getElementById('list');
    const title = document.getElementById('title');
    const viewer = document.getElementById('viewer');
    const openLink = document.getElementById('openLink');

    if (pdfs.length === 0) {{
      list.innerHTML = '<div class="empty">PDFが見つかりません。</div>';
      viewer.replaceWith(Object.assign(document.createElement('div'), {{
        className: 'empty',
        textContent: '講座/*/全体/パンフレット.pdf を生成してから再実行してください。'
      }}));
    }}

    function selectPdf(index) {{
      const item = pdfs[index];
      title.textContent = item.label;
      viewer.src = item.url;
      openLink.href = item.url;
      document.querySelectorAll('button[data-index]').forEach((button) => {{
        button.classList.toggle('active', Number(button.dataset.index) === index);
      }});
    }}

    pdfs.forEach((item, index) => {{
      const button = document.createElement('button');
      button.type = 'button';
      button.dataset.index = String(index);
      button.innerHTML = `<strong>${{item.label}}</strong><br><small>${{item.path}}</small>`;
      button.addEventListener('click', () => selectPdf(index));
      list.appendChild(button);
    }});

    if (pdfs.length > 0) selectPdf(0);
  </script>
</body>
</html>
"""


def main() -> int:
    args = parse_args()
    pdfs = [Path(pdf).resolve() for pdf in args.pdfs] if args.pdfs else find_default_pdfs()
    missing = [pdf for pdf in pdfs if not pdf.exists()]
    if missing:
        for pdf in missing:
            print(f"missing PDF: {pdf}")
        return 1

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_html(pdfs), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
