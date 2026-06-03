#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import json
import os
import secrets
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any


AUTH_URL = "https://www.canva.com/api/oauth/authorize"
TOKEN_URL = "https://api.canva.com/rest/v1/oauth/token"
REDIRECT_URI = "http://127.0.0.1:3001/oauth/redirect"
CREDENTIALS_PATH = Path.home() / ".secrets" / "canva_credentials.txt"
SAVE_PATH = Path.home() / ".secrets" / "canva_tokens.json"
ENV_PATH = Path.home() / ".secrets" / "canva_access_token.env"
SCOPES = [
    "design:content:read",
    "design:content:write",
    "design:meta:read",
    "asset:read",
    "asset:write",
    "folder:read",
    "folder:write",
]


received: dict[str, str] = {}


def load_credentials() -> tuple[str, str]:
    client_id = os.environ.get("CANVA_CLIENT_ID", "").strip()
    client_secret = os.environ.get("CANVA_CLIENT_SECRET", "").strip()
    if CREDENTIALS_PATH.exists():
        for line in CREDENTIALS_PATH.read_text(encoding="utf-8").splitlines():
            if "=" not in line or line.lstrip().startswith("#"):
                continue
            key, value = line.split("=", 1)
            if key.strip() == "CANVA_CLIENT_ID" and not client_id:
                client_id = value.strip()
            elif key.strip() == "CANVA_CLIENT_SECRET" and not client_secret:
                client_secret = value.strip()
    if not client_id or not client_secret:
        raise RuntimeError(f"Missing CANVA_CLIENT_ID or CANVA_CLIENT_SECRET in env or {CREDENTIALS_PATH}")
    return client_id, client_secret


def b64url(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode("ascii")


def new_pkce() -> tuple[str, str]:
    verifier = b64url(secrets.token_bytes(32))
    challenge = b64url(hashlib.sha256(verifier.encode("ascii")).digest())
    return verifier, challenge


class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        received["code"] = params.get("code", [""])[0]
        received["state"] = params.get("state", [""])[0]
        received["error"] = params.get("error", [""])[0]
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("Canva authorization received. You can close this tab.".encode("utf-8"))

    def log_message(self, *_args: Any) -> None:
        return


def start_server() -> HTTPServer:
    server = HTTPServer(("127.0.0.1", 3001), CallbackHandler)
    thread = threading.Thread(target=server.handle_request, daemon=True)
    thread.start()
    return server


def exchange_code(code: str, verifier: str, client_id: str, client_secret: str) -> dict[str, Any]:
    basic = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("ascii")
    data = urllib.parse.urlencode(
        {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
            "code_verifier": verifier,
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        TOKEN_URL,
        data=data,
        method="POST",
        headers={
            "Authorization": f"Basic {basic}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as res:
            return json.loads(res.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Token exchange failed: HTTP {exc.code}\n{body}") from exc


def main() -> int:
    client_id, client_secret = load_credentials()
    verifier, challenge = new_pkce()
    state = secrets.token_urlsafe(16)
    params = {
        "code_challenge_method": "s256",
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "scope": " ".join(SCOPES),
        "code_challenge": challenge,
        "state": state,
    }
    auth_url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"
    start_server()
    print(auth_url, flush=True)
    deadline = time.time() + 180
    while time.time() < deadline:
        if received.get("error"):
            raise RuntimeError(f"Authorization failed: {received['error']}")
        if received.get("code"):
            break
        time.sleep(0.5)
    if not received.get("code"):
        raise RuntimeError("Timed out waiting for Canva OAuth redirect.")
    if received.get("state") != state:
        raise RuntimeError("OAuth state mismatch.")
    tokens = exchange_code(received["code"], verifier, client_id, client_secret)
    SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)
    SAVE_PATH.write_text(json.dumps(tokens, ensure_ascii=False, indent=2), encoding="utf-8")
    SAVE_PATH.chmod(0o600)
    access_token = tokens.get("access_token", "")
    ENV_PATH.write_text(f"export CANVA_ACCESS_TOKEN={access_token!r}\n", encoding="utf-8")
    ENV_PATH.chmod(0o600)
    print(json.dumps({"saved": str(SAVE_PATH), "env": str(ENV_PATH), "has_refresh_token": "refresh_token" in tokens}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
