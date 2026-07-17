#!/usr/bin/env python3
"""Validate a local KDP project package without external dependencies."""

from __future__ import annotations

import argparse
import json
import struct
from pathlib import Path


REQUIRED_FILES = [
    "00_企画/book_plan.md",
    "01_原稿/manuscript.md",
    "02_メタデータ/kdp_metadata.json",
    "02_メタデータ/description.md",
    "03_表紙/cover_brief.md",
    "04_提出パッケージ/upload_checklist.md",
]

REQUIRED_METADATA = [
    "title",
    "author",
    "language",
    "format_plan",
    "description",
    "keywords",
    "categories",
    "target_reader",
    "reader_promise",
    "publishing_rights",
    "ai_disclosure_notes",
]


def read_png_size(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as f:
        data = f.read(24)
    if data.startswith(b"\x89PNG\r\n\x1a\n") and data[12:16] == b"IHDR":
        return struct.unpack(">II", data[16:24])
    return None


def read_jpeg_size(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as f:
        if f.read(2) != b"\xff\xd8":
            return None
        while True:
            marker_start = f.read(1)
            if not marker_start:
                return None
            if marker_start != b"\xff":
                continue
            marker = f.read(1)
            while marker == b"\xff":
                marker = f.read(1)
            if marker in {b"\xd8", b"\xd9"}:
                continue
            length_bytes = f.read(2)
            if len(length_bytes) != 2:
                return None
            length = struct.unpack(">H", length_bytes)[0]
            if marker in {b"\xc0", b"\xc1", b"\xc2", b"\xc3", b"\xc5", b"\xc6", b"\xc7", b"\xc9", b"\xca", b"\xcb", b"\xcd", b"\xce", b"\xcf"}:
                payload = f.read(5)
                if len(payload) != 5:
                    return None
                height, width = struct.unpack(">HH", payload[1:5])
                return width, height
            f.seek(length - 2, 1)


def image_size(path: Path) -> tuple[int, int] | None:
    suffix = path.suffix.lower()
    if suffix == ".png":
        return read_png_size(path)
    if suffix in {".jpg", ".jpeg"}:
        return read_jpeg_size(path)
    return None


def nonempty_text(path: Path) -> bool:
    return path.exists() and bool(path.read_text(encoding="utf-8").strip())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", help="Kindle publishing project directory")
    args = parser.parse_args()
    project = Path(args.project_dir)

    errors: list[str] = []
    warnings: list[str] = []

    if not project.exists():
        errors.append(f"Project directory not found: {project}")
    else:
        for rel_path in REQUIRED_FILES:
            path = project / rel_path
            if not path.exists():
                errors.append(f"Missing required file: {rel_path}")
            elif path.suffix in {".md", ".json"} and not path.read_text(encoding="utf-8").strip():
                errors.append(f"Required file is empty: {rel_path}")

    metadata_path = project / "02_メタデータ/kdp_metadata.json"
    metadata = {}
    if metadata_path.exists():
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid JSON metadata: {exc}")

    if metadata:
        for key in REQUIRED_METADATA:
            value = metadata.get(key)
            if value in ("", [], None):
                warnings.append(f"Metadata not filled: {key}")
        if len(metadata.get("keywords", [])) > 7:
            warnings.append("KDP keyword slots are typically prepared as seven entries; review keyword count.")

    manuscript = project / "01_原稿/manuscript.md"
    if manuscript.exists() and nonempty_text(manuscript):
        text = manuscript.read_text(encoding="utf-8")
        h2_count = sum(1 for line in text.splitlines() if line.startswith("## "))
        if h2_count < 2:
            warnings.append("Manuscript has fewer than two chapter/section headings.")
        if "\t" in text:
            warnings.append("Manuscript contains tab characters; KDP guidance discourages tab-based paragraph indentation.")
        if len(text) < 10000:
            warnings.append("Manuscript is under 10,000 characters; confirm this is intentional.")

    cover_candidates = sorted((project / "03_表紙").glob("cover.*")) if (project / "03_表紙").exists() else []
    image_candidates = [p for p in cover_candidates if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".tif", ".tiff"}]
    if not image_candidates:
        warnings.append("No ebook cover image found at 03_表紙/cover.(jpg|jpeg|png|tif|tiff).")
    else:
        cover = image_candidates[0]
        if cover.stat().st_size >= 50 * 1024 * 1024:
            errors.append(f"Cover image is 50MB or larger: {cover}")
        size = image_size(cover)
        if size is None:
            warnings.append(f"Could not inspect cover dimensions: {cover}")
        else:
            width, height = size
            ratio = height / width if width else 0
            if height < 1000 or width < 625:
                errors.append(f"Cover below KDP minimum dimensions: {width}x{height}")
            if height > 10000 or width > 10000:
                errors.append(f"Cover above KDP maximum dimensions: {width}x{height}")
            if ratio < 1.6:
                warnings.append(f"Cover ratio is below 1.6:1: {width}x{height}")

    checklist = project / "04_提出パッケージ/upload_checklist.md"
    if checklist.exists():
        text = checklist.read_text(encoding="utf-8")
        if "- [ ]" in text:
            warnings.append("Upload checklist still has unchecked items.")

    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARN: {item}")
    if errors:
        print(f"Result: failed with {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"Result: passed with {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
