#!/usr/bin/env python3
"""Check generated diagram-part PNGs for editable Google Slides decks."""

from __future__ import annotations

import argparse
import importlib.util
import json
import struct
import sys
from pathlib import Path
from typing import Any


def load_source_builder(repo_root: Path) -> Any:
    path = repo_root / "scripts" / "build_editable_google_slides_sources.py"
    spec = importlib.util.spec_from_file_location("editable_sources_check", path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot load source builder: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules["editable_sources_check"] = module
    spec.loader.exec_module(module)
    return module


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as f:
        header = f.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return int(width), int(height)


def check_session(session_dir: Path, source_builder: Any) -> dict[str, Any]:
    slides, _sections = source_builder.build_slide_objects(session_dir)
    diagram_dir = session_dir / "図解パーツ"
    missing: list[str] = []
    invalid: list[dict[str, Any]] = []
    present: list[dict[str, Any]] = []

    for slide in slides:
        path = diagram_dir / f"{slide.slide_id}.png"
        if not path.exists():
            missing.append(slide.slide_id)
            continue
        if path.stat().st_size == 0:
            invalid.append({"slide": slide.slide_id, "path": str(path), "reason": "empty"})
            continue
        try:
            width, height = png_dimensions(path)
        except ValueError as exc:
            invalid.append({"slide": slide.slide_id, "path": str(path), "reason": str(exc)})
            continue
        present.append({"slide": slide.slide_id, "path": str(path), "bytes": path.stat().st_size, "width": width, "height": height})

    return {
        "session": session_dir.name,
        "expected": len(slides),
        "present": len(present),
        "missing": missing,
        "invalid": invalid,
        "files": present,
        "ok": not missing and not invalid,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--course-dir",
        default="講座/生成AI・GASで実践する業務変革・DX推進講座",
        help="Course folder containing numbered sessions",
    )
    parser.add_argument("--json", action="store_true", help="Print JSON instead of a text summary")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path.cwd()
    course_dir = Path(args.course_dir)
    source_builder = load_source_builder(repo_root)
    sessions = sorted(p for p in course_dir.iterdir() if p.is_dir() and p.name[:2].isdigit())
    results = [check_session(session, source_builder) for session in sessions]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for result in results:
            status = "ok" if result["ok"] else "missing"
            print(
                f"{result['session']}: {result['present']}/{result['expected']} {status}"
                + (f" missing={','.join(result['missing'][:8])}" if result["missing"] else "")
            )
    return 0 if all(result["ok"] for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
