#!/usr/bin/env python3
"""Export full-raster slide images (one PNG = one slide) to native Google Slides.

Unlike export_ai_training_slides_to_gws.py (which bundles every slide image into
one large PPTX and uploads it in a single request), this script uploads each
スライド画像/Sxx.png individually to Drive, then places each as a full-bleed
image on its own page via the Slides API. This avoids large single-request
uploads that are prone to transient TLS/connection failures on unstable
networks; each individual image upload is a few MB at most.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any

SLIDE_W = 720.0
SLIDE_H = 405.0


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


SCRIPT_DIR = Path(__file__).resolve().parent
BASE = load_module(SCRIPT_DIR / "export_ai_training_slides_to_gws.py", "image_exporter_base")


def drive_download_url(file_id: str) -> str:
    return f"https://drive.google.com/uc?export=download&id={file_id}"


def make_drive_file_readable_by_link(file_id: str, *, dry_run: bool) -> dict[str, Any]:
    if dry_run:
        return {"id": BASE.dryrun_id("permission", file_id), "type": "anyone", "role": "reader"}
    existing = BASE.gws(
        "drive",
        "permissions",
        "list",
        params={"fileId": file_id, "supportsAllDrives": True, "fields": "permissions(id,type,role,allowFileDiscovery)"},
        dry_run=dry_run,
    )
    for permission in existing.get("permissions", []):
        if permission.get("type") == "anyone" and permission.get("role") in {"reader", "commenter", "writer"}:
            return {**permission, "created": False}
    return BASE.gws(
        "drive",
        "permissions",
        "create",
        params={"fileId": file_id, "supportsAllDrives": True, "sendNotificationEmail": False},
        body={"type": "anyone", "role": "reader", "allowFileDiscovery": False},
        dry_run=dry_run,
    )


def create_native_presentation(title: str, parent_id: str, *, dry_run: bool) -> dict[str, Any]:
    if dry_run:
        return {"id": BASE.dryrun_id("full-raster-slides", title), "name": title, "webViewLink": "", "dryRun": True}
    return BASE.gws(
        "drive",
        "files",
        "create",
        params={"fields": "id,name,mimeType,webViewLink,parents", "supportsAllDrives": True},
        body={"name": title, "mimeType": BASE.GOOGLE_SLIDES_MIME, "parents": [parent_id]},
        dry_run=dry_run,
    )


def clear_default_slides(presentation_id: str, *, dry_run: bool) -> list[dict[str, Any]]:
    if dry_run:
        return []
    presentation = BASE.presentation_from_drive(presentation_id, dry_run=dry_run)
    return [{"deleteObject": {"objectId": s["objectId"]}} for s in presentation.get("slides", [])]


def numbered_slide_images(session_dir: Path) -> list[tuple[str, Path]]:
    slide_dir = session_dir / "スライド画像"
    if not slide_dir.is_dir():
        raise BASE.ExportError(f"Missing スライド画像 folder: {slide_dir}")
    items: list[tuple[str, Path]] = []
    for path in sorted(slide_dir.glob("S*.png")):
        match = re.match(r"^(S\d{2,3})\.png$", path.name)
        if not match:
            continue
        items.append((match.group(1), path))
    items.sort(key=lambda pair: int(pair[0][1:]))
    return items


def chunked(items: list[dict[str, Any]], size: int) -> list[list[dict[str, Any]]]:
    return [items[i : i + size] for i in range(0, len(items), size)]


def delete_existing_files(name: str, parent_id: str, *, dry_run: bool) -> list[dict[str, Any]]:
    existing_files = BASE.find_files(name, parent_id, dry_run=dry_run, page_size=100)
    deleted: list[dict[str, Any]] = []
    for existing in existing_files:
        if existing.get("id"):
            BASE.delete_drive_file(existing["id"], dry_run=dry_run)
            deleted.append(existing)
    return deleted


def export_session(session_dir: Path, args: argparse.Namespace, root_folder: dict[str, Any] | None = None) -> dict[str, Any]:
    session_dir = session_dir.resolve()
    if "非公開" in session_dir.parts:
        raise BASE.ExportError(f"Refusing export private folder: {session_dir}")

    course_dir = session_dir.parent
    slide_images = numbered_slide_images(session_dir)
    if not slide_images:
        raise BASE.ExportError(f"No スライド画像/Sxx.png found: {session_dir}")

    notes = {} if args.allow_missing_notes else BASE.parse_speaker_notes(session_dir / "講師台本.md")

    root = root_folder or (
        {"id": args.root_folder_id, "name": args.root_folder_name, "created": False}
        if args.root_folder_id
        else BASE.ensure_folder(args.root_folder_name, None, dry_run=args.dry_run)
    )
    course_folder = BASE.ensure_folder(BASE.course_title(course_dir), root.get("id"), dry_run=args.dry_run)
    session_folder = BASE.ensure_folder(session_dir.name, course_folder.get("id"), dry_run=args.dry_run)
    session_folder_id = session_folder.get("id")
    if not session_folder_id:
        raise BASE.ExportError(f"Missing Drive session folder id: {session_dir}")

    image_folder = BASE.ensure_folder("スライド画像", session_folder_id, dry_run=args.dry_run)
    image_folder_id = image_folder.get("id")
    if not image_folder_id:
        raise BASE.ExportError(f"Missing Drive スライド画像 folder id: {session_dir}")

    warnings: list[str] = []
    uploaded: list[dict[str, Any]] = []
    replaced_images: list[dict[str, Any]] = []
    image_urls: dict[str, str] = {}
    for slide_id, path in slide_images:
        if args.replace_existing_decks:
            replaced_images.extend(delete_existing_files(path.name, image_folder_id, dry_run=args.dry_run))
        uploaded_file = BASE.upload_file_if_missing(path, image_folder_id, dry_run=args.dry_run, label=f"slide-{slide_id}")
        drive_file = uploaded_file.get("driveFile") or {}
        file_id = drive_file.get("id")
        if not file_id:
            warnings.append(f"Missing Drive file id for slide image: {path.name}")
            continue
        permission = make_drive_file_readable_by_link(file_id, dry_run=args.dry_run)
        uploaded_file["permission"] = permission
        uploaded.append(uploaded_file)
        image_urls[slide_id] = drive_download_url(file_id)

    deck_title = args.deck_title or session_dir.name
    existing_decks = BASE.find_files(
        deck_title, session_folder_id, dry_run=args.dry_run, mime_type=BASE.GOOGLE_SLIDES_MIME, page_size=100
    )
    replaced_decks: list[dict[str, Any]] = []
    if existing_decks and args.replace_existing_decks:
        for deck in existing_decks:
            if deck.get("id"):
                BASE.delete_drive_file(deck["id"], dry_run=args.dry_run)
                replaced_decks.append(deck)
        existing_decks = []

    if existing_decks:
        presentation = {**existing_decks[0], "created": False, "skipped": True}
    else:
        presentation = create_native_presentation(deck_title, session_folder_id, dry_run=args.dry_run)
        presentation = {**presentation, "created": True, "skipped": False}
        default_slide_deletions = clear_default_slides(presentation.get("id", ""), dry_run=args.dry_run)
        requests: list[dict[str, Any]] = []
        for idx, (slide_id, _path) in enumerate(slide_images, start=1):
            page_id = f"page{idx:03d}"
            requests.append({"createSlide": {"objectId": page_id, "insertionIndex": idx - 1}})
            url = image_urls.get(slide_id)
            if not url:
                warnings.append(f"Missing uploaded image URL for {slide_id}; slide left blank")
                continue
            requests.append(
                {
                    "createImage": {
                        "objectId": f"{page_id}-image",
                        "url": url,
                        "elementProperties": {
                            "pageObjectId": page_id,
                            "size": {
                                "width": {"magnitude": SLIDE_W, "unit": "PT"},
                                "height": {"magnitude": SLIDE_H, "unit": "PT"},
                            },
                            "transform": {
                                "scaleX": 1,
                                "scaleY": 1,
                                "translateX": 0,
                                "translateY": 0,
                                "unit": "PT",
                            },
                        },
                    }
                }
            )
        requests.extend(default_slide_deletions)
        for chunk in chunked(requests, 40):
            BASE.gws(
                "slides",
                "presentations",
                "batchUpdate",
                params={"presentationId": presentation.get("id", "")},
                body={"requests": chunk},
                dry_run=args.dry_run,
            )

        speaker_note_warnings: list[str] = []
        if not args.dry_run:
            gs_presentation = BASE.presentation_from_drive(presentation.get("id", ""), dry_run=args.dry_run)
            google_slides = gs_presentation.get("slides", [])
            note_requests: list[dict[str, Any]] = []
            for idx, (slide_id, _path) in enumerate(slide_images):
                if idx >= len(google_slides):
                    speaker_note_warnings.append(f"No Google slide for {slide_id}")
                    continue
                note = notes.get(slide_id, "")
                if not note:
                    speaker_note_warnings.append(f"Missing speaker notes for {slide_id}")
                    continue
                notes_id = (
                    google_slides[idx]
                    .get("slideProperties", {})
                    .get("notesPage", {})
                    .get("notesProperties", {})
                    .get("speakerNotesObjectId")
                )
                if not notes_id:
                    speaker_note_warnings.append(f"Missing speakerNotesObjectId for {slide_id}")
                    continue
                note_requests.append({"insertText": {"objectId": notes_id, "insertionIndex": 0, "text": note}})
            for chunk in chunked(note_requests, 50):
                BASE.gws(
                    "slides",
                    "presentations",
                    "batchUpdate",
                    params={"presentationId": presentation.get("id", "")},
                    body={"requests": chunk},
                    dry_run=args.dry_run,
                )
        warnings.extend(speaker_note_warnings)

    return {
        "sessionDir": str(session_dir),
        "rootFolder": root,
        "courseFolder": course_folder,
        "sessionFolder": session_folder,
        "presentation": presentation,
        "replacedDecks": replaced_decks,
        "replacedImages": replaced_images,
        "uploadedImages": uploaded,
        "slideImageCount": len(slide_images),
        "speakerNoteBlockCount": len(notes),
        "warnings": warnings,
        "mode": "full-raster-per-image",
    }


def write_link_index(results: list[dict[str, Any]], out_path: Path) -> None:
    if not results:
        raise BASE.ExportError("No export results available for link index.")
    first = results[0]
    root_folder = first.get("rootFolder", {})
    course_folder = first.get("courseFolder", {})
    lines = [
        "# Google Drive / Google Slides リンク一覧",
        "",
        f"- 講座フォルダ: [講座フォルダ]({BASE.drive_folder_url(course_folder)})",
        f"- Driveルート: [{root_folder.get('name', 'Drive root')}]({BASE.drive_folder_url(root_folder)})",
        "",
        "| 回 | セッション | Driveフォルダ | Google Slides | スライド数 | 警告 |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for result in results:
        session_dir = Path(result["sessionDir"])
        session_folder = result.get("sessionFolder", {})
        presentation = result.get("presentation", {})
        match = re.match(r"(\d{2})-", session_dir.name)
        no = match.group(1) if match else "?"
        warnings = result.get("warnings", [])
        warning_text = f"{len(warnings)}件" if warnings else "なし"
        lines.append(
            f"| {no} | {session_dir.name} | [回フォルダ]({BASE.drive_folder_url(session_folder)}) | "
            f"[{presentation.get('name', session_dir.name)}]({presentation.get('webViewLink', '')}) | "
            f"{result.get('slideImageCount', 0)} | {warning_text} |"
        )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session-dir")
    parser.add_argument("--course-dir")
    parser.add_argument("--all-sessions", action="store_true")
    parser.add_argument("--root-folder-name", default="AI法人研修")
    parser.add_argument("--root-folder-id")
    parser.add_argument("--deck-title")
    parser.add_argument("--replace-existing-decks", action="store_true")
    parser.add_argument("--allow-missing-notes", action="store_true")
    parser.add_argument("--write-link-index", action="store_true")
    parser.add_argument("--link-index-path")
    parser.add_argument("--report-json")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results: list[dict[str, Any]] = []
    if args.all_sessions:
        if not args.course_dir:
            raise SystemExit("--all-sessions requires --course-dir")
        course_dir = Path(args.course_dir)
        root_folder: dict[str, Any] | None = None
        for session_dir in BASE.numbered_sessions(course_dir):
            result = export_session(session_dir, args, root_folder)
            root_folder = result["rootFolder"]
            results.append(result)
    else:
        if not args.session_dir:
            raise SystemExit("Provide --session-dir or --all-sessions with --course-dir")
        results = [export_session(Path(args.session_dir), args)]

    if args.write_link_index:
        if not args.course_dir:
            raise SystemExit("--write-link-index requires --course-dir with --all-sessions")
        out_path = Path(args.link_index_path) if args.link_index_path else Path(args.course_dir) / "全体" / "Google_Driveリンク一覧.md"
        write_link_index(results, out_path)

    if args.report_json:
        Path(args.report_json).write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
