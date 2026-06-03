#!/usr/bin/env python3
"""Convert a local HTML pamphlet to PDF with Chromium's printToPDF API."""

from __future__ import annotations

import argparse
import base64
import json
import os
import shutil
import socket
import struct
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


COMMON_BROWSERS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
    "brave-browser",
    "microsoft-edge",
]


class CDPError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a local HTML pamphlet to a print-ready PDF."
    )
    parser.add_argument("html", help="Path to the source HTML file.")
    parser.add_argument(
        "-o",
        "--output",
        help="Output PDF path. Defaults to the HTML path with .pdf extension.",
    )
    parser.add_argument(
        "--browser",
        help="Browser executable path. Defaults to Chrome/Brave/Chromium lookup.",
    )
    parser.add_argument(
        "--wait-ms",
        type=int,
        default=750,
        help="Extra wait after load before printing. Default: 750.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="Browser and page operation timeout in seconds. Default: 30.",
    )
    parser.add_argument(
        "--scale",
        type=float,
        default=1.0,
        help="Print scale passed to Chrome DevTools. Default: 1.0.",
    )
    return parser.parse_args()


def find_browser(explicit: str | None) -> str:
    candidates = []
    if explicit:
        candidates.append(explicit)
    if os.environ.get("HTML_PAMPHLET_BROWSER"):
        candidates.append(os.environ["HTML_PAMPHLET_BROWSER"])
    candidates.extend(COMMON_BROWSERS)

    for candidate in candidates:
        expanded = os.path.expanduser(candidate)
        if os.path.isabs(expanded) and os.access(expanded, os.X_OK):
            return expanded
        found = shutil.which(candidate)
        if found:
            return found

    raise SystemExit(
        "No Chromium browser found. Pass --browser with Chrome, Brave, or Edge."
    )


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def http_json(url: str, timeout: float, method: str = "GET") -> dict:
    request = urllib.request.Request(url, method=method)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def wait_for_devtools(port: int, timeout: float) -> None:
    deadline = time.time() + timeout
    url = f"http://127.0.0.1:{port}/json/version"
    while time.time() < deadline:
        try:
            http_json(url, timeout=1)
            return
        except (urllib.error.URLError, TimeoutError, OSError):
            time.sleep(0.1)
    raise CDPError("Timed out waiting for browser DevTools endpoint.")


def websocket_connect(ws_url: str, timeout: float) -> socket.socket:
    parsed = urllib.parse.urlparse(ws_url)
    host = parsed.hostname or "127.0.0.1"
    port = parsed.port or 80
    path = parsed.path
    if parsed.query:
        path += "?" + parsed.query

    sock = socket.create_connection((host, port), timeout=timeout)
    key = base64.b64encode(os.urandom(16)).decode("ascii")
    request = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host}:{port}\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        f"Sec-WebSocket-Key: {key}\r\n"
        "Sec-WebSocket-Version: 13\r\n\r\n"
    )
    sock.sendall(request.encode("ascii"))

    response = b""
    while b"\r\n\r\n" not in response:
        chunk = sock.recv(4096)
        if not chunk:
            break
        response += chunk
    if b" 101 " not in response.split(b"\r\n", 1)[0]:
        raise CDPError("WebSocket handshake with Chrome DevTools failed.")
    return sock


def send_ws(sock: socket.socket, payload: str, opcode: int = 1) -> None:
    data = payload.encode("utf-8")
    header = bytearray([0x80 | opcode])
    length = len(data)
    if length < 126:
        header.append(0x80 | length)
    elif length < (1 << 16):
        header.append(0x80 | 126)
        header.extend(struct.pack("!H", length))
    else:
        header.append(0x80 | 127)
        header.extend(struct.pack("!Q", length))

    mask = os.urandom(4)
    masked = bytes(byte ^ mask[index % 4] for index, byte in enumerate(data))
    sock.sendall(bytes(header) + mask + masked)


def recv_exact(sock: socket.socket, size: int) -> bytes:
    chunks = []
    remaining = size
    while remaining:
        chunk = sock.recv(remaining)
        if not chunk:
            raise CDPError("WebSocket closed unexpectedly.")
        chunks.append(chunk)
        remaining -= len(chunk)
    return b"".join(chunks)


def recv_ws(sock: socket.socket) -> str:
    message = bytearray()
    while True:
        first, second = recv_exact(sock, 2)
        fin = bool(first & 0x80)
        opcode = first & 0x0F
        masked = bool(second & 0x80)
        length = second & 0x7F
        if length == 126:
            length = struct.unpack("!H", recv_exact(sock, 2))[0]
        elif length == 127:
            length = struct.unpack("!Q", recv_exact(sock, 8))[0]

        mask = recv_exact(sock, 4) if masked else b""
        payload = recv_exact(sock, length) if length else b""
        if masked:
            payload = bytes(byte ^ mask[index % 4] for index, byte in enumerate(payload))

        if opcode == 8:
            raise CDPError("Chrome DevTools WebSocket closed.")
        if opcode == 9:
            send_ws(sock, payload.decode("utf-8", "ignore"), opcode=10)
            continue
        if opcode in (1, 2, 0):
            message.extend(payload)
            if fin:
                return message.decode("utf-8")


class CDPClient:
    def __init__(self, ws_url: str, timeout: float) -> None:
        self.sock = websocket_connect(ws_url, timeout)
        self.sock.settimeout(timeout)
        self.next_id = 1
        self.events: list[dict] = []

    def close(self) -> None:
        try:
            self.sock.close()
        except OSError:
            pass

    def call(self, method: str, params: dict | None = None, timeout: float = 30.0) -> dict:
        message_id = self.next_id
        self.next_id += 1
        payload = {"id": message_id, "method": method}
        if params is not None:
            payload["params"] = params
        send_ws(self.sock, json.dumps(payload, separators=(",", ":")))

        deadline = time.time() + timeout
        while time.time() < deadline:
            self.sock.settimeout(max(0.1, deadline - time.time()))
            received = json.loads(recv_ws(self.sock))
            if received.get("id") == message_id:
                if "error" in received:
                    raise CDPError(f"{method} failed: {received['error']}")
                return received.get("result", {})
            if "method" in received:
                self.events.append(received)
        raise CDPError(f"Timed out waiting for {method}.")

    def wait_event(self, method: str, timeout: float) -> dict:
        deadline = time.time() + timeout
        while time.time() < deadline:
            for index, event in enumerate(self.events):
                if event.get("method") == method:
                    return self.events.pop(index)
            self.sock.settimeout(max(0.1, deadline - time.time()))
            received = json.loads(recv_ws(self.sock))
            if received.get("method") == method:
                return received
            if "method" in received:
                self.events.append(received)
        raise CDPError(f"Timed out waiting for {method}.")


def launch_browser(browser: str, port: int, user_data_dir: str) -> subprocess.Popen:
    command = [
        browser,
        "--headless=new",
        f"--remote-debugging-port={port}",
        f"--user-data-dir={user_data_dir}",
        "--allow-file-access-from-files",
        "--disable-background-networking",
        "--disable-default-apps",
        "--disable-dev-shm-usage",
        "--disable-gpu",
        "--disable-sync",
        "--hide-scrollbars",
        "--no-default-browser-check",
        "--no-first-run",
        "about:blank",
    ]
    return subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )


def create_target(port: int, url: str, timeout: float) -> dict:
    endpoint = f"http://127.0.0.1:{port}/json/new?{urllib.parse.quote(url, safe='')}"
    return http_json(endpoint, timeout=timeout, method="PUT")


def wait_for_assets(client: CDPClient, timeout: float) -> None:
    expression = """
    Promise.all([
      document.fonts && document.fonts.ready ? document.fonts.ready : true,
      Promise.all(Array.from(document.images).map((img) => {
        if (img.complete) return true;
        return new Promise((resolve) => {
          img.onload = resolve;
          img.onerror = resolve;
        });
      }))
    ]).then(() => true)
    """
    client.call(
        "Runtime.evaluate",
        {
            "expression": expression,
            "awaitPromise": True,
            "returnByValue": True,
        },
        timeout=timeout,
    )


def convert(html_path: Path, output_path: Path, browser: str, wait_ms: int, timeout: float, scale: float) -> None:
    port = free_port()
    with tempfile.TemporaryDirectory(prefix="html-pamphlet-pdf-") as user_data_dir:
        process = launch_browser(browser, port, user_data_dir)
        client = None
        try:
            wait_for_devtools(port, timeout)
            target = create_target(port, "about:blank", timeout)
            client = CDPClient(target["webSocketDebuggerUrl"], timeout)
            client.call("Page.enable", timeout=timeout)
            client.call("Runtime.enable", timeout=timeout)
            client.call("Emulation.setEmulatedMedia", {"media": "print"}, timeout=timeout)
            client.call("Page.navigate", {"url": html_path.as_uri()}, timeout=timeout)
            client.wait_event("Page.loadEventFired", timeout=timeout)
            wait_for_assets(client, timeout=timeout)
            if wait_ms > 0:
                time.sleep(wait_ms / 1000)

            result = client.call(
                "Page.printToPDF",
                {
                    "printBackground": True,
                    "preferCSSPageSize": True,
                    "displayHeaderFooter": False,
                    "scale": scale,
                },
                timeout=timeout,
            )
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(base64.b64decode(result["data"]))
        except Exception:
            stderr = ""
            if process.poll() is not None and process.stderr:
                try:
                    stderr = process.stderr.read(4000)
                except Exception:
                    stderr = ""
            if stderr:
                print(stderr, file=sys.stderr)
            raise
        finally:
            if client:
                client.close()
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()


def main() -> int:
    args = parse_args()
    html_path = Path(args.html).expanduser().resolve()
    if not html_path.is_file():
        print(f"HTML file not found: {html_path}", file=sys.stderr)
        return 2
    output_path = (
        Path(args.output).expanduser().resolve()
        if args.output
        else html_path.with_suffix(".pdf")
    )
    if output_path.suffix.lower() != ".pdf":
        print(f"Output path must end with .pdf: {output_path}", file=sys.stderr)
        return 2

    browser = find_browser(args.browser)
    convert(html_path, output_path, browser, args.wait_ms, args.timeout, args.scale)

    size = output_path.stat().st_size
    if size <= 0:
        print(f"PDF was created but is empty: {output_path}", file=sys.stderr)
        return 1
    print(f"Wrote {output_path} ({size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
