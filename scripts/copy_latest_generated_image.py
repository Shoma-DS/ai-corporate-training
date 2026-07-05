#!/usr/bin/env python3
"""Copy one newly generated Codex image into the project after validation."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import time
from pathlib import Path


BITMAP_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}
MAGIC_TO_MIME = (
    (b"\x89PNG\r\n\x1a\n", "image/png"),
    (b"\xff\xd8\xff", "image/jpeg"),
    (b"RIFF", "image/webp"),
)
TARGET_SUFFIX_TO_MIME = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
}


def detect_bitmap_mime(path: Path) -> str:
    header = path.read_bytes()[:16]
    for magic, mime in MAGIC_TO_MIME:
        if mime == "image/webp":
            if header.startswith(magic) and header[8:12] == b"WEBP":
                return mime
            continue
        if header.startswith(magic):
            return mime
    raise ValueError(f"unsupported or invalid bitmap content: {path}")


def generated_root() -> Path:
    codex_home = os.environ.get("CODEX_HOME") or str(Path.home() / ".codex")
    return Path(codex_home).expanduser() / "generated_images"


def candidate_files(root: Path, marker: Path) -> list[Path]:
    if not marker.is_file():
        raise FileNotFoundError(f"marker file does not exist: {marker}")
    if not root.is_dir():
        raise FileNotFoundError(f"copy source directory does not exist: {root}")
    marker_mtime = marker.stat().st_mtime_ns
    candidates: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in BITMAP_SUFFIXES:
            continue
        if path.stat().st_mtime_ns > marker_mtime:
            candidates.append(path)
    return sorted(candidates, key=lambda p: p.stat().st_mtime_ns)


def wait_for_candidates(root: Path, marker: Path, wait_seconds: float, poll_interval: float) -> list[Path]:
    deadline = time.monotonic() + max(0.0, wait_seconds)
    last_missing_root: FileNotFoundError | None = None
    while True:
        try:
            candidates = candidate_files(root, marker)
            last_missing_root = None
        except FileNotFoundError as exc:
            if "copy source directory does not exist" not in str(exc):
                raise
            candidates = []
            last_missing_root = exc
        if candidates:
            return candidates
        if time.monotonic() >= deadline:
            if last_missing_root is not None:
                raise last_missing_root
            return []
        time.sleep(max(0.1, poll_interval))


def emit_result(result: dict[str, object], status_json: str | None = None, *, stream=None) -> None:
    text = json.dumps(result, ensure_ascii=False, indent=2)
    print(text, file=stream or sys.stdout)
    if status_json:
        status_path = Path(status_json)
        status_path.parent.mkdir(parents=True, exist_ok=True)
        status_path.write_text(text + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, help="Destination file path inside the project")
    parser.add_argument("--marker", required=True, help="Marker file touched immediately before imagegen")
    parser.add_argument(
        "--session-id",
        help="Restrict copy source to CODEX_HOME/generated_images/<session-id>",
    )
    parser.add_argument(
        "--search-root",
        help="Override generated image root. Defaults to CODEX_HOME/generated_images or ~/.codex/generated_images.",
    )
    parser.add_argument(
        "--expect-mime",
        default="image/png",
        choices=("image/png", "image/jpeg", "image/webp"),
        help="Required source bitmap MIME. Defaults to image/png for slide/diagram PNGs.",
    )
    parser.add_argument(
        "--allow-latest-in-session",
        action="store_true",
        help="If multiple generated bitmaps exist after the marker inside a restricted session directory, copy the newest one.",
    )
    parser.add_argument(
        "--wait-seconds",
        type=float,
        default=0.0,
        help="Poll for delayed Codex App Server output before failing. Useful after transient 502/transport errors.",
    )
    parser.add_argument(
        "--poll-interval",
        type=float,
        default=2.0,
        help="Polling interval in seconds used with --wait-seconds.",
    )
    parser.add_argument(
        "--missing-ok",
        action="store_true",
        help="Return success with copied=false when no generated bitmap is found, so batch jobs can continue.",
    )
    parser.add_argument(
        "--status-json",
        help="Optional path to write the same JSON status that is printed to stdout/stderr.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = Path(args.target)
    marker = Path(args.marker)
    root = Path(args.search_root).expanduser() if args.search_root else generated_root()
    if args.session_id:
        root = root / args.session_id

    try:
        candidates = wait_for_candidates(root, marker, args.wait_seconds, args.poll_interval)
        if not candidates:
            if args.missing_ok:
                emit_result(
                    {
                        "copied": False,
                        "target": str(target),
                        "source_root": str(root),
                        "reason": "no generated bitmap newer than marker",
                    },
                    args.status_json,
                )
                return 0
            raise RuntimeError(f"no generated bitmap newer than marker under {root}")
        if len(candidates) > 1 and not (args.allow_latest_in_session and args.session_id):
            names = "\n".join(str(path) for path in candidates[-10:])
            raise RuntimeError(
                f"ambiguous generated bitmap source: {len(candidates)} files newer than marker under {root}\n{names}"
            )
        if len(candidates) > 1:
            candidates = candidates[-1:]

        source = candidates[0]
        source_mime = detect_bitmap_mime(source)
        target_mime = TARGET_SUFFIX_TO_MIME.get(target.suffix.lower())
        if source_mime != args.expect_mime:
            raise RuntimeError(f"expected {args.expect_mime}, got {source_mime}: {source}")
        if target_mime != source_mime:
            raise RuntimeError(
                f"target suffix {target.suffix!r} does not match source content type {source_mime}; "
                "do not rename generated images across formats"
            )

        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        emit_result(
            {
                "copied": True,
                "source": str(source),
                "target": str(target),
                "mime": source_mime,
                "bytes": target.stat().st_size,
            },
            args.status_json,
        )
        return 0
    except Exception as exc:
        if args.missing_ok and "copy source directory does not exist" in str(exc):
            emit_result(
                {
                    "copied": False,
                    "target": str(target),
                    "source_root": str(root),
                    "reason": str(exc),
                },
                args.status_json,
            )
            return 0
        if args.status_json:
            emit_result(
                {
                    "copied": False,
                    "target": str(target),
                    "source_root": str(root),
                    "reason": str(exc),
                },
                args.status_json,
                stream=sys.stderr,
            )
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
