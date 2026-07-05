#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import re
import struct
import sys
from collections import defaultdict
from pathlib import Path


COURSE_DIR = Path("講座/生成AI・GASで実践する業務変革・DX推進講座")


def png_size(path: Path) -> tuple[int, int] | None:
    data = path.read_bytes()[:24]
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", data[16:24])


def expected_slide_numbers(prompt_file: Path) -> list[str]:
    text = prompt_file.read_text(encoding="utf-8")
    return re.findall(r"^## (S\d{2})\b", text, flags=re.MULTILINE)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if not COURSE_DIR.exists():
        print(f"missing course dir: {COURSE_DIR}", file=sys.stderr)
        return 2

    all_ok = True
    hashes: dict[str, list[Path]] = defaultdict(list)

    for session_dir in sorted(p for p in COURSE_DIR.iterdir() if p.is_dir() and re.match(r"^\d\d-", p.name)):
        prompt_file = session_dir / "図解パーツ生成プロンプト.md"
        parts_dir = session_dir / "図解パーツ"
        if not prompt_file.exists():
            continue

        expected = expected_slide_numbers(prompt_file)
        missing: list[str] = []
        bad_png: list[str] = []
        odd_size: list[str] = []

        for slide_no in expected:
            image = parts_dir / f"{slide_no}.png"
            if not image.exists():
                missing.append(slide_no)
                continue
            size = png_size(image)
            if size is None:
                bad_png.append(slide_no)
                continue
            width, height = size
            # GPT image output sizes vary, but diagram parts should be plausible
            # landscape assets for 16:9 editable slides, not tiny placeholders.
            if width < 900 or height < 500 or width < height:
                odd_size.append(f"{slide_no}:{width}x{height}")
            hashes[sha256(image)].append(image)

        status = "ok" if not (missing or bad_png or odd_size) else "needs_fix"
        print(
            f"{session_dir.name}: {len(expected) - len(missing)}/{len(expected)} {status}"
            f" missing={','.join(missing[:8]) or '-'}"
            f" bad_png={','.join(bad_png[:8]) or '-'}"
            f" odd_size={','.join(odd_size[:8]) or '-'}"
        )
        if missing or bad_png or odd_size:
            all_ok = False

    duplicate_groups = {h: paths for h, paths in hashes.items() if len(paths) > 1}
    if duplicate_groups:
        all_ok = False
        print("duplicate_hash_groups:")
        for digest, paths in sorted(duplicate_groups.items(), key=lambda item: (-len(item[1]), item[0])):
            print(f"- {digest[:16]} count={len(paths)}")
            for path in paths[:12]:
                print(f"  {path}")
            if len(paths) > 12:
                print(f"  ... {len(paths) - 12} more")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
