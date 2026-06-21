#!/usr/bin/env python3
"""Update Google Slides speaker notes in place for existing decks.

The main exporter (export_ai_training_slides_to_gws.py) only inserts speaker
notes when it CREATES a new deck; for an existing deck it skips notes. This
script updates the speaker notes of already-existing decks WITHOUT recreating
them, so the presentation IDs / share URLs stay the same.

For each numbered session under --course-dir it:
  1. parses speaker-note blocks from 講師台本.md (keyed by S01, S02, ...),
  2. looks up the existing presentation ID from the Drive link index,
  3. for each slide, clears the current speaker-notes text and inserts the
     matching 講師台本 block via the Slides API batchUpdate.

Slide N (1-based, in deck order) receives the note for key S{N:02d}, matching
how the deck was built from S01.png, S02.png, ... in order.

Run with --dry-run first to preview without touching Drive.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


class NotesError(RuntimeError):
    pass


def run_gws(*parts: str, params: dict[str, Any] | None = None, body: dict[str, Any] | None = None) -> dict[str, Any]:
    cmd = ["gws", *parts, "--format", "json"]
    if params is not None:
        cmd += ["--params", json.dumps(params, ensure_ascii=False)]
    if body is not None:
        cmd += ["--json", json.dumps(body, ensure_ascii=False)]
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise NotesError("gws failed:\n" + " ".join(cmd) + "\nSTDOUT:\n" + proc.stdout + "\nSTDERR:\n" + proc.stderr)
    out = proc.stdout.strip()
    if not out:
        return {}
    try:
        data = json.loads(out)
    except json.JSONDecodeError as exc:
        raise NotesError(f"Expected JSON from: {' '.join(cmd)}\n{out}") from exc
    if isinstance(data, dict) and data.get("error"):
        raise NotesError(f"API error: {json.dumps(data['error'], ensure_ascii=False)}")
    return data


def natural_slide_key(path: Path) -> tuple[int, str]:
    m = re.match(r"S(\d+)", path.name, re.I)
    return (int(m.group(1)) if m else 1_000_000, path.name)


def count_slide_images(session_dir: Path) -> int:
    image_dir = session_dir / "スライド画像"
    if not image_dir.is_dir():
        return 0
    return len([p for p in image_dir.iterdir() if p.is_file() and re.match(r"S\d+\.(png|jpg|jpeg)$", p.name, re.I)])


def parse_speaker_notes(script_path: Path) -> dict[str, str]:
    if not script_path.is_file():
        raise NotesError(f"Missing instructor script: {script_path}")
    notes: dict[str, list[str]] = {}
    current: str | None = None
    current_lines: list[str] = []
    slide_re = re.compile(r"^(S\d{2,3})「(.+?)」\s*$")
    for raw in script_path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.startswith("## スライド切替タイムライン") or line.startswith("## 作業風景タイムライン"):
            break
        match = slide_re.match(line)
        if match:
            if current:
                notes[current] = current_lines
            current = match.group(1)
            current_lines = [line, ""]
            continue
        if line == "スライド切替:":
            continue
        if current:
            current_lines.append(line)
    if current:
        notes[current] = current_lines
    return {key: "\n".join(lines).strip() for key, lines in notes.items()}


def parse_link_index(link_index: Path) -> dict[str, str]:
    """Map session folder name -> presentation ID from the Markdown link index."""
    mapping: dict[str, str] = {}
    if not link_index.is_file():
        return mapping
    pres_re = re.compile(r"presentation/d/([A-Za-z0-9_-]+)")
    for line in link_index.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        m = pres_re.search(line)
        if not m:
            continue
        pres_id = m.group(1)
        # session name appears as a plain cell (e.g. "01-業務データ基盤の設計") or inside a link
        for cell in cells:
            name = cell
            lm = re.match(r"\[(.+?)\]\(", cell)
            if lm:
                name = lm.group(1)
            if re.match(r"^\d{2}-", name):
                mapping[name] = pres_id
                break
    return mapping


def get_presentation(presentation_id: str) -> dict[str, Any]:
    last: Exception | None = None
    for _ in range(5):
        try:
            return run_gws("slides", "presentations", "get", params={"presentationId": presentation_id})
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(2)
    raise NotesError(f"Could not read presentation {presentation_id}: {last}")


def notes_shape_text(slide: dict[str, Any], notes_obj_id: str) -> str:
    notes_page = slide.get("slideProperties", {}).get("notesPage", {})
    for el in notes_page.get("pageElements", []):
        if el.get("objectId") != notes_obj_id:
            continue
        text = el.get("shape", {}).get("text", {})
        buf = []
        for te in text.get("textElements", []):
            run = te.get("textRun")
            if run and run.get("content"):
                buf.append(run["content"])
        return "".join(buf)
    return ""


def build_requests(presentation: dict[str, Any], notes: dict[str, str]) -> tuple[list[dict[str, Any]], list[str]]:
    slides = presentation.get("slides", [])
    warnings: list[str] = []
    requests: list[dict[str, Any]] = []
    for idx, slide in enumerate(slides):
        key = f"S{idx + 1:02d}"
        note = notes.get(key, "")
        if not note:
            warnings.append(f"No script block for {key}")
            continue
        notes_obj_id = (
            slide.get("slideProperties", {})
            .get("notesPage", {})
            .get("notesProperties", {})
            .get("speakerNotesObjectId")
        )
        if not notes_obj_id:
            warnings.append(f"No speakerNotesObjectId for slide {idx + 1} ({key})")
            continue
        existing = notes_shape_text(slide, notes_obj_id)
        # Slides keeps a trailing newline in an "empty" notes shape; only delete real content.
        if existing.strip():
            requests.append({"deleteText": {"objectId": notes_obj_id, "textRange": {"type": "ALL"}}})
        requests.append({"insertText": {"objectId": notes_obj_id, "insertionIndex": 0, "text": note}})
    return requests, warnings


def numbered_sessions(course_dir: Path) -> list[Path]:
    return sorted([p for p in course_dir.iterdir() if p.is_dir() and re.match(r"^\d{2}-", p.name)], key=lambda p: p.name)


def update_session(session_dir: Path, presentation_id: str, *, dry_run: bool) -> dict[str, Any]:
    notes = parse_speaker_notes(session_dir / "講師台本.md")
    image_count = count_slide_images(session_dir)
    presentation = get_presentation(presentation_id)
    slides = presentation.get("slides", [])
    requests, warnings = build_requests(presentation, notes)
    if len(slides) != image_count:
        warnings.append(f"Slide count differs: deck={len(slides)} images={image_count}")
    if len(slides) != len(notes):
        warnings.append(f"Note-block count differs: deck={len(slides)} notes={len(notes)}")

    sent = 0
    if not dry_run:
        for start in range(0, len(requests), 50):
            chunk = requests[start : start + 50]
            run_gws("slides", "presentations", "batchUpdate", params={"presentationId": presentation_id}, body={"requests": chunk})
            sent += len(chunk)
            time.sleep(0.5)

    result = {
        "session": session_dir.name,
        "presentationId": presentation_id,
        "deckSlides": len(slides),
        "imageCount": image_count,
        "noteBlocks": len(notes),
        "requests": len(requests),
        "sentRequests": sent,
        "dryRun": dry_run,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course-dir", required=True, help="Course folder containing numbered session subfolders")
    parser.add_argument("--link-index", help="Path to Google_Driveリンク一覧.md (default: <course-dir>/全体/Google_Driveリンク一覧.md)")
    parser.add_argument("--session", help="Only update this session folder name (e.g. 01-...)")
    parser.add_argument("--presentation-id", help="Override presentation ID; requires --session")
    parser.add_argument("--dry-run", action="store_true", help="Preview without modifying Google Slides")
    args = parser.parse_args()

    course_dir = Path(args.course_dir).resolve()
    if "非公開" in course_dir.parts:
        raise NotesError(f"Refusing to operate on private folder: {course_dir}")
    if not course_dir.is_dir():
        raise NotesError(f"Course dir not found: {course_dir}")

    link_index = Path(args.link_index) if args.link_index else course_dir / "全体" / "Google_Driveリンク一覧.md"
    mapping = parse_link_index(link_index)

    sessions = numbered_sessions(course_dir)
    if args.session:
        sessions = [p for p in sessions if p.name == args.session]
        if not sessions:
            raise NotesError(f"Session not found: {args.session}")

    results = []
    for session_dir in sessions:
        pres_id = args.presentation_id if (args.presentation_id and args.session) else mapping.get(session_dir.name)
        if not pres_id:
            print(json.dumps({"session": session_dir.name, "error": "No presentation ID in link index"}, ensure_ascii=False))
            continue
        results.append(update_session(session_dir, pres_id, dry_run=args.dry_run))

    total_warnings = sum(len(r.get("warnings", [])) for r in results)
    print(f"\n== Summary: {len(results)} session(s), {total_warnings} warning(s), dry_run={args.dry_run} ==")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except NotesError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
