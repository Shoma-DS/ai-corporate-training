#!/usr/bin/env python3
"""Copy one newly generated Codex image into the project after validation."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
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
    if not root.is_dir():
        raise FileNotFoundError(f"copy source directory does not exist: {root}")
    if not marker.is_file():
        raise FileNotFoundError(f"marker file does not exist: {marker}")
    marker_mtime = marker.stat().st_mtime_ns
    candidates: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in BITMAP_SUFFIXES:
            continue
        if path.stat().st_mtime_ns > marker_mtime:
            candidates.append(path)
    return sorted(candidates, key=lambda p: p.stat().st_mtime_ns)


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
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = Path(args.target)
    marker = Path(args.marker)
    root = Path(args.search_root).expanduser() if args.search_root else generated_root()
    if args.session_id:
        root = root / args.session_id

    try:
        candidates = candidate_files(root, marker)
        if not candidates:
            raise RuntimeError(f"no generated bitmap newer than marker under {root}")
        if len(candidates) > 1:
            names = "\n".join(str(path) for path in candidates[-10:])
            raise RuntimeError(
                f"ambiguous generated bitmap source: {len(candidates)} files newer than marker under {root}\n{names}"
            )

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
        print(
            json.dumps(
                {
                    "copied": True,
                    "source": str(source),
                    "target": str(target),
                    "mime": source_mime,
                    "bytes": target.stat().st_size,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
