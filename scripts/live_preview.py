#!/usr/bin/env python3
"""Small local preview server for AI法人研修 HTML/PDF files."""

from __future__ import annotations

import argparse
import html
import json
import mimetypes
import os
import socket
import threading
import time
import webbrowser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import quote, unquote, urlparse


DEFAULT_ROOT = Path.cwd()
WATCH_SUFFIXES = {".html", ".css", ".js", ".md", ".pdf"}


LIVE_RELOAD = """
<script>
(() => {
  const started = Date.now() / 1000;
  async function check() {
    try {
      const res = await fetch('/__livepreview__/mtime', {cache: 'no-store'});
      const data = await res.json();
      if (data.mtime > started + 0.5) location.reload();
    } catch (_) {}
  }
  setInterval(check, 1200);
})();
</script>
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a local HTML/PDF preview server.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument(
        "--root",
        default=str(DEFAULT_ROOT),
        help="Directory to preview. Default: current working directory.",
    )
    parser.add_argument("--no-open", action="store_true", help="Do not open a browser.")
    parser.add_argument(
        "--path",
        default="/__livepreview__/",
        help="Initial path to open. Default: /__livepreview__/",
    )
    return parser.parse_args()


def find_free_port(host: str, preferred: int) -> int:
    for port in range(preferred, preferred + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind((host, port))
            except OSError:
                continue
            return port
    raise RuntimeError(f"No free port found from {preferred}")


def iter_preview_files(root: Path) -> list[Path]:
    ignored_parts = {".git", "非公開"}
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored_parts for part in path.relative_to(root).parts):
            continue
        if path.suffix.lower() in {".html", ".pdf"}:
            files.append(path)
    return sorted(files, key=lambda p: str(p.relative_to(root)))


def latest_mtime(root: Path) -> float:
    newest = 0.0
    ignored_parts = {".git", "非公開"}
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel_parts = path.relative_to(root).parts
        if any(part in ignored_parts for part in rel_parts):
            continue
        if path.suffix.lower() not in WATCH_SUFFIXES:
            continue
        try:
            newest = max(newest, path.stat().st_mtime)
        except OSError:
            pass
    return newest


def make_index(root: Path) -> bytes:
    rows = []
    files = iter_preview_files(root)
    for file_path in files:
        rel = file_path.relative_to(root)
        url = "/" + quote(str(rel))
        kind = file_path.suffix.lower().lstrip(".").upper()
        rows.append(
            f"<li><a href='{url}' target='preview'>{html.escape(str(rel))}</a><span>{kind}</span></li>"
        )
    body = "\n".join(rows) or "<li>HTML/PDFが見つかりません。</li>"
    first_src = "/" + quote(str(files[0].relative_to(root))) if files else "about:blank"
    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AI法人研修 Live Preview</title>
  <style>
    :root {{ --ink:#172033; --muted:#64748b; --line:#d8e2ee; --bg:#f4f7fb; --blue:#2a76a8; }}
    body {{ margin:0; background:var(--bg); color:var(--ink); font-family:-apple-system,BlinkMacSystemFont,"Hiragino Sans","Yu Gothic","YuGothic","Noto Sans JP",sans-serif; }}
    header {{ padding:18px 22px; background:#fff; border-bottom:1px solid var(--line); }}
    h1 {{ margin:0 0 4px; font-size:20px; }}
    p {{ margin:0; color:var(--muted); font-size:13px; }}
    .wrap {{ display:grid; grid-template-columns:360px 1fr; min-height:calc(100vh - 74px); }}
    nav {{ padding:16px; background:#fff; border-right:1px solid var(--line); overflow:auto; }}
    ul {{ list-style:none; padding:0; margin:0; display:grid; gap:7px; }}
    li {{ display:grid; grid-template-columns:1fr auto; gap:8px; align-items:center; border:1px solid var(--line); background:#fff; padding:9px 10px; }}
    a {{ color:var(--blue); text-decoration:none; font-size:13px; overflow-wrap:anywhere; }}
    span {{ color:var(--muted); font-size:11px; font-weight:700; }}
    iframe {{ width:100%; height:100%; min-height:760px; border:0; background:#fff; }}
    @media (max-width: 960px) {{ .wrap {{ grid-template-columns:1fr; }} nav {{ border-right:0; border-bottom:1px solid var(--line); }} }}
  </style>
</head>
<body>
  <header>
    <h1>AI法人研修 Live Preview</h1>
    <p>{html.escape(str(root))}</p>
    <p>HTML/PDFをクリックすると右側で開きます。HTMLは保存後に自動リロードします。</p>
  </header>
  <div class="wrap">
    <nav><ul>{body}</ul></nav>
    <iframe name="preview" src="{first_src}"></iframe>
  </div>
</body>
</html>
""".encode("utf-8")


class PreviewHandler(SimpleHTTPRequestHandler):
    server_version = "AITrainingLivePreview/1.0"
    preview_root = DEFAULT_ROOT

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(self.preview_root), **kwargs)

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"[live-preview] {self.address_string()} - {fmt % args}")

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/__livepreview__/" or parsed.path == "/__livepreview__":
            content = make_index(self.preview_root)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return
        if parsed.path == "/__livepreview__/mtime":
            content = json.dumps({"mtime": latest_mtime(self.preview_root)}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return
        return super().do_GET()

    def do_HEAD(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/__livepreview__/" or parsed.path == "/__livepreview__":
            content = make_index(self.preview_root)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            return
        if parsed.path == "/__livepreview__/mtime":
            content = json.dumps({"mtime": latest_mtime(self.preview_root)}).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            return
        return super().do_HEAD()

    def send_head(self):
        parsed = urlparse(self.path)
        request_path = Path(unquote(parsed.path.lstrip("/")))
        target = (self.preview_root / request_path).resolve()
        try:
            target.relative_to(self.preview_root)
        except ValueError:
            self.send_error(403)
            return None
        if target.is_file() and target.suffix.lower() == ".html":
            raw = target.read_text(encoding="utf-8")
            if "</body>" in raw:
                raw = raw.replace("</body>", LIVE_RELOAD + "\n</body>")
            else:
                raw += LIVE_RELOAD
            content = raw.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            return MemoryFile(content)
        return super().send_head()


class MemoryFile:
    def __init__(self, content: bytes):
        self.content = content
        self.sent = False

    def read(self, _size: int = -1) -> bytes:
        if self.sent:
            return b""
        self.sent = True
        return self.content

    def close(self) -> None:
        pass


def main() -> int:
    mimetypes.add_type("application/pdf", ".pdf")
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(f"Preview root must be an existing directory: {root}")
        return 1
    PreviewHandler.preview_root = root
    port = find_free_port(args.host, args.port)
    server = ThreadingHTTPServer((args.host, port), PreviewHandler)
    url = f"http://{args.host}:{port}{args.path}"
    print(f"Live preview: {url}")
    print("Press Ctrl+C to stop.")

    if not args.no_open:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping live preview.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
