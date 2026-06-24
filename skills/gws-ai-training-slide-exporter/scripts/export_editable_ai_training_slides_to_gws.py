#!/usr/bin/env python3
"""Export editable AI training slide outlines to native Google Slides via gws."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import re
import struct
import sys
from pathlib import Path
from typing import Any


SLIDE_W = 720.0
SLIDE_H = 405.0
NAVY = {"red": 0.05, "green": 0.16, "blue": 0.28}
TEAL = {"red": 0.0, "green": 0.47, "blue": 0.52}
GRAY = {"red": 0.34, "green": 0.39, "blue": 0.45}
DIAGRAM_DIR_NAME = "図解パーツ"
DIAGRAM_X = 506.0
DIAGRAM_Y = 156.0
DIAGRAM_W = 168.0
DIAGRAM_H = 140.0
BODY_W_WITH_DIAGRAM = 458.0


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


def repo_root() -> Path:
    current = Path.cwd().resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "AGENTS.md").is_file() and (candidate / "scripts").is_dir():
            return candidate
    raise BASE.ExportError("Could not find repository root from current working directory.")


ROOT = repo_root()
SOURCE_BUILDER = load_module(ROOT / "scripts" / "build_editable_google_slides_sources.py", "editable_sources")


def text_style(font_size: float, color: dict[str, float], *, bold: bool = False) -> dict[str, Any]:
    return {
        "fontFamily": "Arial",
        "fontSize": {"magnitude": font_size, "unit": "PT"},
        "foregroundColor": {"opaqueColor": {"rgbColor": color}},
        "bold": bold,
    }


def create_text_box(
    object_id: str,
    page_id: str,
    text: str,
    *,
    x: float,
    y: float,
    w: float,
    h: float,
    font_size: float,
    color: dict[str, float] = NAVY,
    bold: bool = False,
) -> list[dict[str, Any]]:
    return [
        {
            "createShape": {
                "objectId": object_id,
                "shapeType": "TEXT_BOX",
                "elementProperties": {
                    "pageObjectId": page_id,
                    "size": {
                        "width": {"magnitude": w, "unit": "PT"},
                        "height": {"magnitude": h, "unit": "PT"},
                    },
                    "transform": {
                        "scaleX": 1,
                        "scaleY": 1,
                        "translateX": x,
                        "translateY": y,
                        "unit": "PT",
                    },
                },
            }
        },
        {"insertText": {"objectId": object_id, "insertionIndex": 0, "text": text}},
        {
            "updateTextStyle": {
                "objectId": object_id,
                "style": text_style(font_size, color, bold=bold),
                "fields": "fontFamily,fontSize,foregroundColor,bold",
            }
        },
    ]


def create_line(object_id: str, page_id: str, *, x: float, y: float, w: float) -> list[dict[str, Any]]:
    return [
        {
            "createShape": {
                "objectId": object_id,
                "shapeType": "RECTANGLE",
                "elementProperties": {
                    "pageObjectId": page_id,
                    "size": {
                        "width": {"magnitude": w, "unit": "PT"},
                        "height": {"magnitude": 1.2, "unit": "PT"},
                    },
                    "transform": {
                        "scaleX": 1,
                        "scaleY": 1,
                        "translateX": x,
                        "translateY": y,
                        "unit": "PT",
                    },
                },
            }
        },
        {
            "updateShapeProperties": {
                "objectId": object_id,
                "shapeProperties": {
                    "shapeBackgroundFill": {"solidFill": {"color": {"rgbColor": TEAL}, "alpha": 1}}
                },
                "fields": "shapeBackgroundFill.solidFill.color,shapeBackgroundFill.solidFill.alpha",
            }
        },
    ]


def body_text(slide: Any, max_chars: int = 2200) -> str:
    text = SOURCE_BUILDER.normalize_body_for_outline(slide.body, max_chars=max_chars)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    text = text.replace("**", "")
    return text


def body_font_size(text: str, *, has_diagram: bool = False) -> float:
    length = len(text)
    if has_diagram and length > 1700:
        return 6.6
    if has_diagram and length > 1200:
        return 7.3
    if has_diagram and length > 700:
        return 8.2
    if length <= 700:
        return 10.5
    if length <= 1200:
        return 9.3
    if length <= 1700:
        return 8.3
    return 7.6


def create_image(
    object_id: str,
    page_id: str,
    image_url: str,
    *,
    x: float,
    y: float,
    w: float,
    h: float,
) -> list[dict[str, Any]]:
    return [
        {
            "createImage": {
                "objectId": object_id,
                "url": image_url,
                "elementProperties": {
                    "pageObjectId": page_id,
                    "size": {
                        "width": {"magnitude": w, "unit": "PT"},
                        "height": {"magnitude": h, "unit": "PT"},
                    },
                    "transform": {
                        "scaleX": 1,
                        "scaleY": 1,
                        "translateX": x,
                        "translateY": y,
                        "unit": "PT",
                    },
                },
            }
        }
    ]


def slide_requests(
    page_id: str,
    slide: Any,
    session_label: str,
    course_title: str,
    *,
    diagram_url: str | None = None,
) -> list[dict[str, Any]]:
    body = body_text(slide)
    has_diagram = bool(diagram_url)
    font_size = body_font_size(body, has_diagram=has_diagram)
    diagram_line = (
        f"図解: {DIAGRAM_DIR_NAME}/{slide.slide_id}.png / {slide.diagram_pattern}"
        if has_diagram
        else f"図解/素材: {slide.diagram_pattern} / {slide.screenshot}"
    )
    body_width = BODY_W_WITH_DIAGRAM if has_diagram else 650
    prefix = page_id
    requests: list[dict[str, Any]] = [
        {
            "createSlide": {
                "objectId": page_id,
                "slideLayoutReference": {"predefinedLayout": "BLANK"},
            }
        }
    ]
    requests += create_text_box(
        f"{prefix}_course",
        page_id,
        course_title,
        x=26,
        y=10,
        w=445,
        h=14,
        font_size=7.4,
        color=GRAY,
    )
    requests += create_text_box(
        f"{prefix}_session",
        page_id,
        session_label,
        x=26,
        y=24,
        w=445,
        h=16,
        font_size=8.2,
        color=TEAL,
        bold=True,
    )
    requests += create_text_box(
        f"{prefix}_sid",
        page_id,
        slide.slide_id,
        x=632,
        y=10,
        w=55,
        h=22,
        font_size=15,
        color=TEAL,
        bold=True,
    )
    requests += create_text_box(
        f"{prefix}_section",
        page_id,
        slide.section,
        x=500,
        y=31,
        w=188,
        h=17,
        font_size=7.4,
        color=GRAY,
    )
    requests += create_line(f"{prefix}_line1", page_id, x=26, y=49, w=662)
    requests += create_text_box(
        f"{prefix}_title",
        page_id,
        slide.title,
        x=31,
        y=59,
        w=658,
        h=35,
        font_size=19,
        color=NAVY,
        bold=True,
    )
    requests += create_text_box(
        f"{prefix}_headline",
        page_id,
        slide.headline,
        x=31,
        y=96,
        w=658,
        h=40,
        font_size=12.5,
        color=TEAL,
        bold=True,
    )
    requests += create_text_box(
        f"{prefix}_body",
        page_id,
        body,
        x=35,
        y=142,
        w=body_width,
        h=196,
        font_size=font_size,
        color=NAVY,
    )
    if diagram_url:
        requests += create_image(
            f"{prefix}_diagram",
            page_id,
            diagram_url,
            x=DIAGRAM_X,
            y=DIAGRAM_Y,
            w=DIAGRAM_W,
            h=DIAGRAM_H,
        )
    requests += create_line(f"{prefix}_line2", page_id, x=31, y=347, w=658)
    requests += create_text_box(
        f"{prefix}_bottom",
        page_id,
        diagram_line,
        x=35,
        y=356,
        w=650,
        h=25,
        font_size=7.8,
        color=GRAY,
    )
    return requests


def chunked(items: list[dict[str, Any]], size: int) -> list[list[dict[str, Any]]]:
    return [items[i : i + size] for i in range(0, len(items), size)]


def drive_download_url(file_id: str) -> str:
    return f"https://drive.google.com/uc?export=download&id={file_id}"


def make_drive_file_readable_by_link(file_id: str, *, dry_run: bool) -> dict[str, Any]:
    if dry_run:
        return {"id": BASE.dryrun_id("permission", file_id), "type": "anyone", "role": "reader"}
    existing = BASE.gws(
        "drive",
        "permissions",
        "list",
        params={
            "fileId": file_id,
            "supportsAllDrives": True,
            "fields": "permissions(id,type,role,allowFileDiscovery)",
        },
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


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return int(width), int(height)


def validate_diagram_png(path: Path) -> tuple[int, int]:
    width, height = png_dimensions(path)
    if width < 900 or height < 500 or width < height:
        raise ValueError(f"unexpected diagram dimensions: {width}x{height}")
    return width, height


def prepare_diagram_assets(
    session_dir: Path,
    slides: list[Any],
    session_folder_id: str,
    args: argparse.Namespace,
) -> tuple[dict[str, str], list[dict[str, Any]], list[str]]:
    if not args.embed_diagram_parts:
        return {}, [], []
    if not args.make_diagram_images_readable_by_link and not args.dry_run:
        raise BASE.ExportError(
            "--embed-diagram-parts requires --make-diagram-images-readable-by-link "
            "because Google Slides createImage fetches images by URL."
        )

    diagram_dir = session_dir / DIAGRAM_DIR_NAME
    warnings: list[str] = []
    uploaded: list[dict[str, Any]] = []
    diagram_urls: dict[str, str] = {}
    if not diagram_dir.is_dir():
        return diagram_urls, uploaded, [f"Missing diagram parts folder: {diagram_dir}"]

    drive_diagram_folder = BASE.ensure_folder(DIAGRAM_DIR_NAME, session_folder_id, dry_run=args.dry_run)
    drive_diagram_folder_id = drive_diagram_folder.get("id")
    if not drive_diagram_folder_id:
        raise BASE.ExportError(f"Missing Drive diagram folder id: {session_dir}")

    for slide in slides:
        path = diagram_dir / f"{slide.slide_id}.png"
        if not path.is_file():
            warnings.append(f"Missing diagram part: {path.name}")
            continue
        if path.stat().st_size == 0:
            warnings.append(f"Empty diagram part: {path.name}")
            continue
        try:
            validate_diagram_png(path)
        except ValueError as exc:
            warnings.append(f"Invalid diagram part: {path.name}: {exc}")
            continue
        uploaded_file = BASE.upload_file_if_missing(
            path,
            drive_diagram_folder_id,
            dry_run=args.dry_run,
            label=f"diagram-{slide.slide_id}",
        )
        drive_file = uploaded_file.get("driveFile") or {}
        file_id = drive_file.get("id")
        if not file_id:
            warnings.append(f"Missing Drive file id for diagram part: {path.name}")
            continue
        permission = None
        if args.make_diagram_images_readable_by_link:
            permission = make_drive_file_readable_by_link(file_id, dry_run=args.dry_run)
        uploaded_file["permission"] = permission
        uploaded.append(uploaded_file)
        diagram_urls[slide.slide_id] = drive_download_url(file_id)

    return diagram_urls, uploaded, warnings


def create_native_presentation(title: str, parent_id: str, *, dry_run: bool) -> dict[str, Any]:
    if dry_run:
        return {"id": BASE.dryrun_id("editable-slides", title), "name": title, "webViewLink": "", "dryRun": True}
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
    return [{"deleteObject": {"objectId": slide["objectId"]}} for slide in presentation.get("slides", [])]


def insert_speaker_notes(presentation_id: str, slides: list[Any], notes: dict[str, str], *, dry_run: bool) -> list[str]:
    warnings: list[str] = []
    if dry_run:
        return warnings
    presentation = BASE.presentation_from_drive(presentation_id, dry_run=dry_run)
    google_slides = presentation.get("slides", [])
    requests: list[dict[str, Any]] = []
    for idx, slide in enumerate(slides):
        if idx >= len(google_slides):
            warnings.append(f"No Google slide for {slide.slide_id}")
            continue
        note = notes.get(slide.slide_id, "")
        if not note:
            warnings.append(f"Missing speaker notes for {slide.slide_id}")
            continue
        notes_id = (
            google_slides[idx]
            .get("slideProperties", {})
            .get("notesPage", {})
            .get("notesProperties", {})
            .get("speakerNotesObjectId")
        )
        if not notes_id:
            warnings.append(f"Missing speakerNotesObjectId for {slide.slide_id}")
            continue
        requests.append({"insertText": {"objectId": notes_id, "insertionIndex": 0, "text": note}})
    for chunk in chunked(requests, 50):
        BASE.gws(
            "slides",
            "presentations",
            "batchUpdate",
            params={"presentationId": presentation_id},
            body={"requests": chunk},
            dry_run=dry_run,
        )
    return warnings


def upload_extra_sources(session_dir: Path, session_folder_id: str, *, dry_run: bool) -> list[dict[str, Any]]:
    uploaded: list[dict[str, Any]] = []
    for filename in [
        "Googleスライド編集用アウトライン.md",
        "図解パーツ生成プロンプト.md",
        "画像生成プロンプト.md",
        "ワークシート.md",
    ]:
        path = session_dir / filename
        if path.is_file():
            uploaded.append(BASE.upload_file_if_missing(path, session_folder_id, dry_run=dry_run, label=filename))
    return uploaded


def export_session(session_dir: Path, args: argparse.Namespace, root_folder: dict[str, Any] | None = None) -> dict[str, Any]:
    session_dir = session_dir.resolve()
    if "非公開" in session_dir.parts:
        raise BASE.ExportError(f"Refusing export private folder: {session_dir}")

    course_dir = session_dir.parent
    session_no = SOURCE_BUILDER.session_no(session_dir)
    session_title = SOURCE_BUILDER.SESSION_TITLES.get(session_no, session_dir.name.split("-", 1)[-1])
    session_label = f"第{int(session_no)}回 {session_title}"
    deck_title = args.deck_title or session_dir.name
    slides, sections = SOURCE_BUILDER.build_slide_objects(session_dir)
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
    diagram_urls, diagram_uploads, diagram_warnings = prepare_diagram_assets(
        session_dir,
        slides,
        session_folder_id,
        args,
    )

    existing_decks = BASE.find_files(
        deck_title,
        session_folder_id,
        dry_run=args.dry_run,
        mime_type=BASE.GOOGLE_SLIDES_MIME,
        page_size=100,
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
        warnings = [f"Google Slides already exists: {deck_title}. Use --replace-existing-decks to recreate."]
    else:
        presentation = create_native_presentation(deck_title, session_folder_id, dry_run=args.dry_run)
        presentation = {**presentation, "created": True, "skipped": False}
        default_slide_deletions = clear_default_slides(presentation.get("id", ""), dry_run=args.dry_run)
        requests: list[dict[str, Any]] = []
        for idx, slide in enumerate(slides, start=1):
            page_id = f"p{session_no}{idx:03d}"
            requests.extend(
                slide_requests(
                    page_id,
                    slide,
                    session_label,
                    SOURCE_BUILDER.COURSE_TITLE,
                    diagram_url=diagram_urls.get(slide.slide_id),
                )
            )
        requests.extend(default_slide_deletions)
        for chunk in chunked(requests, 180):
            BASE.gws(
                "slides",
                "presentations",
                "batchUpdate",
                params={"presentationId": presentation.get("id", "")},
                body={"requests": chunk},
                dry_run=args.dry_run,
            )
        warnings = insert_speaker_notes(presentation.get("id", ""), slides, notes, dry_run=args.dry_run)
    warnings.extend(diagram_warnings)

    materials = BASE.upload_session_materials(
        session_dir,
        session_folder,
        dry_run=args.dry_run,
        exercise_csv_as_sheets=args.exercise_csv_as_sheets,
        replace_exercise_sheets=args.replace_exercise_sheets,
    )
    extra_uploads = upload_extra_sources(session_dir, session_folder_id, dry_run=args.dry_run)
    materials.setdefault("uploadedFiles", []).extend(extra_uploads)
    warnings.extend(materials.get("warnings", []))
    if len(notes) < len(slides) and not args.allow_missing_notes:
        warnings.append(f"Speaker note block count differs: slides={len(slides)} notes={len(notes)}")

    result = {
        "rootFolder": root,
        "courseFolder": course_folder,
        "sessionFolder": session_folder,
        "presentation": presentation,
        "replacedPresentations": replaced_decks,
        "materials": materials,
        "diagramParts": {
            "enabled": bool(args.embed_diagram_parts),
            "uploadedFiles": diagram_uploads,
            "embeddedCount": len(diagram_urls),
            "expectedCount": len(slides),
        },
        "mode": "editable-google-slides",
        "slideImageCount": len(slides),
        "editableSlideCount": len(slides),
        "sectionCount": len(sections),
        "speakerNoteBlockCount": len(notes),
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session-dir", help="One numbered session folder")
    parser.add_argument("--course-dir", help="Course folder. Use with --all-sessions.")
    parser.add_argument("--all-sessions", action="store_true", help="Export all numbered sessions under --course-dir")
    parser.add_argument("--root-folder-name", default="AI法人研修", help="Drive root folder name")
    parser.add_argument("--root-folder-id", help="Known Drive folder ID to use as root")
    parser.add_argument("--deck-title", help="Override Google Slides title for one session")
    parser.add_argument("--replace-existing-decks", action="store_true", help="Delete same-name Google Slides before creating")
    parser.add_argument("--allow-missing-notes", action="store_true", help="Continue without requiring speaker notes")
    parser.add_argument("--exercise-csv-as-sheets", action="store_true", help="Combine CSV/TSV exercise files into one Google Sheet")
    parser.add_argument("--replace-exercise-sheets", action="store_true", help="Replace legacy exercise sheet uploads")
    parser.add_argument("--embed-diagram-parts", action="store_true", help="Upload and embed 図解パーツ/Sxx.png into editable slides")
    parser.add_argument(
        "--make-diagram-images-readable-by-link",
        action="store_true",
        help="Grant anyone-with-link reader permission to uploaded diagram PNGs so Slides can fetch them by URL",
    )
    parser.add_argument("--write-link-index", action="store_true", help="Write course-level Google_Driveリンク一覧.md")
    parser.add_argument("--link-index-path", help="Override link index output path")
    parser.add_argument("--report-json", help="Write full export report JSON")
    parser.add_argument("--dry-run", action="store_true", help="Print intended actions without creating Drive/Slides files")
    args = parser.parse_args()
    if args.all_sessions:
        if not args.course_dir:
            parser.error("--all-sessions requires --course-dir")
    elif not args.session_dir:
        parser.error("Provide --session-dir, or --course-dir with --all-sessions")
    if args.deck_title and args.all_sessions:
        parser.error("--deck-title is only valid with one --session-dir")
    if args.link_index_path and not args.write_link_index:
        parser.error("--link-index-path requires --write-link-index")
    if args.write_link_index and not args.all_sessions:
        parser.error("--write-link-index requires --course-dir with --all-sessions")
    return args


def main() -> int:
    args = parse_args()
    try:
        if args.all_sessions:
            root = (
                {"id": args.root_folder_id, "name": args.root_folder_name, "created": False}
                if args.root_folder_id
                else BASE.ensure_folder(args.root_folder_name, None, dry_run=args.dry_run)
            )
            sessions = BASE.numbered_sessions(Path(args.course_dir))
            results = [export_session(session, args, root_folder=root) for session in sessions]
        else:
            results = [export_session(Path(args.session_dir), args)]
        if args.report_json:
            report_path = Path(args.report_json)
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
        if args.write_link_index and args.dry_run:
            print("Dry run: skipping link index write.")
        elif args.write_link_index:
            BASE.write_link_index(results, BASE.link_index_target(args))
        return 0
    except BASE.ExportError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
