#!/usr/bin/env python3
"""Export AI training slide images and scripts to Google Drive/Slides via gws."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from pathlib import Path
from typing import Any


FOLDER_MIME = "application/vnd.google-apps.folder"
GOOGLE_SLIDES_MIME = "application/vnd.google-apps.presentation"
PPTX_MIME = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
SLIDE_CX = 12192000
SLIDE_CY = 6858000


class ExportError(RuntimeError):
    pass


def run(cmd: list[str], *, dry_run: bool = False) -> dict[str, Any]:
    if dry_run:
        print("$ " + " ".join(cmd))
        return {}
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != 0:
        raise ExportError(
            "Command failed:\n"
            + " ".join(cmd)
            + "\n\nSTDOUT:\n"
            + proc.stdout
            + "\nSTDERR:\n"
            + proc.stderr
        )
    out = proc.stdout.strip()
    if not out:
        return {}
    try:
        return json.loads(out)
    except json.JSONDecodeError as exc:
        raise ExportError(f"Expected JSON from command: {' '.join(cmd)}\n{out}") from exc


def gws(
    *parts: str,
    params: dict[str, Any] | None = None,
    body: dict[str, Any] | None = None,
    upload: Path | None = None,
    upload_content_type: str | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    cmd = ["gws", *parts, "--format", "json"]
    if params is not None:
        cmd += ["--params", json.dumps(params, ensure_ascii=False)]
    if body is not None:
        cmd += ["--json", json.dumps(body, ensure_ascii=False)]
    if upload is not None:
        cmd += ["--upload", str(upload)]
    if upload_content_type is not None:
        cmd += ["--upload-content-type", upload_content_type]
    return run(cmd, dry_run=dry_run)


def drive_literal(value: str) -> str:
    return "'" + value.replace("\\", "\\\\").replace("'", "\\'") + "'"


def dryrun_id(prefix: str, name: str) -> str:
    digest = hashlib.sha1(f"{prefix}:{name}".encode("utf-8")).hexdigest()[:10]
    return f"DRYRUN-{prefix}-{digest}"


def find_files(
    name: str,
    parent_id: str | None,
    *,
    dry_run: bool,
    mime_type: str | None = None,
    page_size: int = 10,
) -> list[dict[str, Any]]:
    q = f"name = {drive_literal(name)} and trashed = false"
    if mime_type:
        q += f" and mimeType = {drive_literal(mime_type)}"
    if parent_id:
        q += f" and {drive_literal(parent_id)} in parents"
    result = gws(
        "drive",
        "files",
        "list",
        params={
            "q": q,
            "fields": "files(id,name,mimeType,webViewLink,modifiedTime)",
            "pageSize": page_size,
            "supportsAllDrives": True,
            "includeItemsFromAllDrives": True,
        },
        dry_run=dry_run,
    )
    return result.get("files", [])


def find_folder(name: str, parent_id: str | None, *, dry_run: bool) -> dict[str, Any] | None:
    files = find_files(name, parent_id, dry_run=dry_run, mime_type=FOLDER_MIME)
    if len(files) > 1:
        raise ExportError(f"Drive folder name is duplicated: {name}. Use --root-folder-id or rename folders.")
    return files[0] if files else None


def ensure_folder(name: str, parent_id: str | None, *, dry_run: bool) -> dict[str, Any]:
    existing = find_folder(name, parent_id, dry_run=dry_run)
    if existing:
        return {**existing, "created": False}
    body: dict[str, Any] = {"name": name, "mimeType": FOLDER_MIME}
    if parent_id:
        body["parents"] = [parent_id]
    created = gws(
        "drive",
        "files",
        "create",
        params={"fields": "id,name,webViewLink", "supportsAllDrives": True},
        body=body,
        dry_run=dry_run,
    )
    if dry_run:
        created = {"id": dryrun_id("folder", name), "name": name}
    return {**created, "created": True}


def find_existing_file(
    name: str,
    parent_id: str | None,
    *,
    dry_run: bool,
    mime_type: str | None = None,
) -> dict[str, Any] | None:
    files = find_files(name, parent_id, dry_run=dry_run, mime_type=mime_type)
    if not files:
        return None
    return {**files[0], "duplicateCount": len(files)}


def upload_mime_type(path: Path) -> str:
    explicit = {
        ".csv": "text/csv",
        ".md": "text/markdown",
        ".markdown": "text/markdown",
        ".txt": "text/plain",
        ".json": "application/json",
        ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ".pptx": PPTX_MIME,
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".pdf": "application/pdf",
    }
    if path.suffix.lower() in explicit:
        return explicit[path.suffix.lower()]
    return mimetypes.guess_type(path.name)[0] or "application/octet-stream"


def public_safe_path(path: Path) -> None:
    if "非公開" in path.resolve().parts:
        raise ExportError(f"Refusing to export private file or folder: {path}")


def upload_file_if_missing(
    path: Path,
    parent_id: str,
    *,
    dry_run: bool,
    label: str,
) -> dict[str, Any]:
    public_safe_path(path)
    existing = find_existing_file(path.name, parent_id, dry_run=dry_run)
    if existing:
        return {
            "label": label,
            "localPath": str(path),
            "driveFile": existing,
            "created": False,
            "skipped": True,
        }
    created = gws(
        "drive",
        "files",
        "create",
        params={"fields": "id,name,mimeType,webViewLink,modifiedTime", "supportsAllDrives": True},
        body={"name": path.name, "parents": [parent_id]},
        upload=path,
        upload_content_type=upload_mime_type(path),
        dry_run=dry_run,
    )
    if dry_run:
        created = {"id": dryrun_id("file", path.name), "name": path.name}
    return {
        "label": label,
        "localPath": str(path),
        "driveFile": created,
        "created": True,
        "skipped": False,
    }


def iter_uploadable_files(root: Path) -> list[Path]:
    if not root.is_dir():
        return []
    public_safe_path(root)
    files = [
        p
        for p in root.rglob("*")
        if p.is_file() and not any(part.startswith(".") for part in p.relative_to(root).parts)
    ]
    return sorted(files, key=lambda p: p.relative_to(root).as_posix())


def ensure_relative_drive_folder(base: dict[str, Any], base_local_dir: Path, file_path: Path, *, dry_run: bool) -> dict[str, Any]:
    parent = base
    rel_parent = file_path.parent.relative_to(base_local_dir)
    for part in rel_parent.parts:
        parent = ensure_folder(part, parent.get("id"), dry_run=dry_run)
    return parent


def upload_session_materials(session_dir: Path, session_folder: dict[str, Any], *, dry_run: bool) -> dict[str, Any]:
    uploaded: list[dict[str, Any]] = []
    warnings: list[str] = []
    session_folder_id = session_folder.get("id")
    if not session_folder_id:
        raise ExportError(f"Missing Drive session folder id for: {session_dir}")

    for filename in ["講師台本.md", "スライド案.md"]:
        path = session_dir / filename
        if path.is_file():
            uploaded.append(upload_file_if_missing(path, session_folder_id, dry_run=dry_run, label=filename))
        else:
            warnings.append(f"Missing session material: {path}")

    exercise_dir = session_dir / "演習データ"
    exercise_files = iter_uploadable_files(exercise_dir)
    exercise_folder: dict[str, Any] | None = None
    if exercise_files:
        exercise_folder = ensure_folder("演習データ", session_folder_id, dry_run=dry_run)
        for path in exercise_files:
            parent = ensure_relative_drive_folder(exercise_folder, exercise_dir, path, dry_run=dry_run)
            uploaded.append(
                upload_file_if_missing(
                    path,
                    parent.get("id"),
                    dry_run=dry_run,
                    label="演習データ/" + path.relative_to(exercise_dir).as_posix(),
                )
            )
    elif exercise_dir.is_dir():
        warnings.append(f"No uploadable exercise data files found in: {exercise_dir}")
    else:
        warnings.append(f"Missing exercise data directory: {exercise_dir}")

    return {
        "exerciseFolder": exercise_folder,
        "uploadedFiles": uploaded,
        "warnings": warnings,
    }


def temp_parent_dir(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = Path.cwd() / path
    path.mkdir(parents=True, exist_ok=True)
    return path


def natural_slide_key(path: Path) -> tuple[int, str]:
    m = re.search(r"S(\d+)", path.stem, re.IGNORECASE)
    return (int(m.group(1)) if m else 9999, path.name)


def collect_slide_images(session_dir: Path) -> list[Path]:
    image_dir = session_dir / "スライド画像"
    if not image_dir.is_dir():
        raise ExportError(f"Missing slide image directory: {image_dir}")
    images = sorted(
        [p for p in image_dir.iterdir() if p.is_file() and re.match(r"S\d+\.(png|jpg|jpeg)$", p.name, re.I)],
        key=natural_slide_key,
    )
    if not images:
        raise ExportError(f"No Sxx.png slide images found in: {image_dir}")
    return images


def parse_speaker_notes(script_path: Path) -> dict[str, str]:
    if not script_path.is_file():
        raise ExportError(f"Missing instructor script: {script_path}")
    notes: dict[str, list[str]] = {}
    current: str | None = None
    current_lines: list[str] = []
    slide_re = re.compile(r"^(S\d{2,3})「(.+?)」\s*$")
    for raw in script_path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
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


def xml(text: str) -> str:
    return html.escape(text, quote=True)


def content_types(slide_count: int, exts: set[str]) -> str:
    image_defaults = []
    if "png" in exts:
        image_defaults.append('<Default Extension="png" ContentType="image/png"/>')
    if "jpg" in exts or "jpeg" in exts:
        image_defaults.append('<Default Extension="jpg" ContentType="image/jpeg"/>')
        image_defaults.append('<Default Extension="jpeg" ContentType="image/jpeg"/>')
    slide_overrides = "\n".join(
        f'<Override PartName="/ppt/slides/slide{i}.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(1, slide_count + 1)
    )
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
{''.join(image_defaults)}
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
<Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
<Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
<Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
{slide_overrides}
</Types>'''


def root_rels() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''


def core_props(title: str) -> str:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:title>{xml(title)}</dc:title>
<dc:creator>AI法人研修 gws exporter</dc:creator>
<cp:lastModifiedBy>AI法人研修 gws exporter</cp:lastModifiedBy>
<dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>
<dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>
</cp:coreProperties>'''


def app_props(slide_count: int) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
<Application>AI法人研修 gws exporter</Application>
<PresentationFormat>On-screen Show (16:9)</PresentationFormat>
<Slides>{slide_count}</Slides>
</Properties>'''


def presentation_xml(slide_count: int) -> str:
    slide_ids = "\n".join(
        f'<p:sldId id="{255 + i}" r:id="rId{i + 1}"/>' for i in range(1, slide_count + 1)
    )
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
<p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst>
<p:sldIdLst>{slide_ids}</p:sldIdLst>
<p:sldSz cx="{SLIDE_CX}" cy="{SLIDE_CY}" type="wide"/>
<p:notesSz cx="6858000" cy="9144000"/>
<p:defaultTextStyle><a:defPPr><a:defRPr lang="ja-JP"/></a:defPPr></p:defaultTextStyle>
</p:presentation>'''


def presentation_rels(slide_count: int) -> str:
    rels = ['<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>']
    rels.extend(
        f'<Relationship Id="rId{i + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>'
        for i in range(1, slide_count + 1)
    )
    return '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n' + "\n".join(rels) + "\n</Relationships>"


def group_shape_xml() -> str:
    return '''<p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'''


def slide_master_xml() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
<p:cSld><p:spTree>{group_shape_xml()}</p:spTree></p:cSld>
<p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
<p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst>
<p:txStyles><p:titleStyle/><p:bodyStyle/><p:otherStyle/></p:txStyles>
</p:sldMaster>'''


def slide_master_rels() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/>
</Relationships>'''


def slide_layout_xml() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1">
<p:cSld name="Blank"><p:spTree>{group_shape_xml()}</p:spTree></p:cSld>
<p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sldLayout>'''


def slide_layout_rels() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>
</Relationships>'''


def theme_xml() -> str:
    return '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="AI Training">
<a:themeElements>
<a:clrScheme name="Office"><a:dk1><a:sysClr val="windowText" lastClr="000000"/></a:dk1><a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="1F497D"/></a:dk2><a:lt2><a:srgbClr val="EEECE1"/></a:lt2><a:accent1><a:srgbClr val="4F81BD"/></a:accent1><a:accent2><a:srgbClr val="C0504D"/></a:accent2><a:accent3><a:srgbClr val="9BBB59"/></a:accent3><a:accent4><a:srgbClr val="8064A2"/></a:accent4><a:accent5><a:srgbClr val="4BACC6"/></a:accent5><a:accent6><a:srgbClr val="F79646"/></a:accent6><a:hlink><a:srgbClr val="0000FF"/></a:hlink><a:folHlink><a:srgbClr val="800080"/></a:folHlink></a:clrScheme>
<a:fontScheme name="Office"><a:majorFont><a:latin typeface="Arial"/><a:ea typeface="Yu Gothic"/></a:majorFont><a:minorFont><a:latin typeface="Arial"/><a:ea typeface="Yu Gothic"/></a:minorFont></a:fontScheme>
<a:fmtScheme name="Office"><a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst><a:lnStyleLst><a:ln w="9525"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst><a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst><a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst></a:fmtScheme>
</a:themeElements><a:objectDefaults/><a:extraClrSchemeLst/>
</a:theme>'''


def slide_xml(image_name: str) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
<p:cSld><p:spTree>{group_shape_xml()}
<p:pic><p:nvPicPr><p:cNvPr id="2" name="{xml(image_name)}"/><p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr/></p:nvPicPr>
<p:blipFill><a:blip r:embed="rId1"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>
<p:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{SLIDE_CX}" cy="{SLIDE_CY}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr>
</p:pic></p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>'''


def slide_rels(image_index: int, image_ext: str) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/image{image_index}.{image_ext}"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>'''


def build_pptx(images: list[Path], out_path: Path, title: str) -> None:
    exts = {("jpg" if p.suffix.lower() == ".jpeg" else p.suffix.lower().lstrip(".")) for p in images}
    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types(len(images), exts))
        zf.writestr("_rels/.rels", root_rels())
        zf.writestr("docProps/core.xml", core_props(title))
        zf.writestr("docProps/app.xml", app_props(len(images)))
        zf.writestr("ppt/presentation.xml", presentation_xml(len(images)))
        zf.writestr("ppt/_rels/presentation.xml.rels", presentation_rels(len(images)))
        zf.writestr("ppt/slideMasters/slideMaster1.xml", slide_master_xml())
        zf.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", slide_master_rels())
        zf.writestr("ppt/slideLayouts/slideLayout1.xml", slide_layout_xml())
        zf.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", slide_layout_rels())
        zf.writestr("ppt/theme/theme1.xml", theme_xml())
        for idx, image in enumerate(images, start=1):
            ext = "jpg" if image.suffix.lower() == ".jpeg" else image.suffix.lower().lstrip(".")
            zf.writestr(f"ppt/slides/slide{idx}.xml", slide_xml(image.name))
            zf.writestr(f"ppt/slides/_rels/slide{idx}.xml.rels", slide_rels(idx, ext))
            zf.write(image, f"ppt/media/image{idx}.{ext}")


def write_canva_bundle(
    pptx_path: Path,
    output_dir: str,
    session_dir: Path,
    *,
    dry_run: bool,
) -> Path:
    target_dir = Path(output_dir).expanduser()
    if not dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"{session_dir.name}.pptx"
    if not dry_run:
        shutil.copy2(pptx_path, target)
    return target



def presentation_from_drive(presentation_id: str, *, dry_run: bool) -> dict[str, Any]:
    last_error: Exception | None = None
    for _ in range(10):
        try:
            return gws("slides", "presentations", "get", params={"presentationId": presentation_id}, dry_run=dry_run)
        except Exception as exc:
            last_error = exc
            if dry_run:
                return {}
            time.sleep(3)
    raise ExportError(f"Google Slides conversion did not become readable: {presentation_id}") from last_error


def insert_speaker_notes(presentation_id: str, images: list[Path], notes: dict[str, str], *, dry_run: bool) -> list[str]:
    presentation = presentation_from_drive(presentation_id, dry_run=dry_run)
    slides = presentation.get("slides", [])
    warnings: list[str] = []
    requests: list[dict[str, Any]] = []
    if len(slides) != len(images) and not dry_run:
        warnings.append(f"Converted slide count differs: local={len(images)} google={len(slides)}")
    for idx, image in enumerate(images):
        if idx >= len(slides):
            warnings.append(f"No Google slide for {image.name}")
            continue
        slide_id = image.stem.upper()
        note = notes.get(slide_id, "")
        if not note:
            warnings.append(f"Missing speaker notes for {slide_id}")
            continue
        notes_id = (
            slides[idx]
            .get("slideProperties", {})
            .get("notesPage", {})
            .get("notesProperties", {})
            .get("speakerNotesObjectId")
        )
        if not notes_id:
            warnings.append(f"Missing speakerNotesObjectId for {slide_id}")
            continue
        requests.append({"insertText": {"objectId": notes_id, "insertionIndex": 0, "text": note}})
    for start in range(0, len(requests), 50):
        chunk = requests[start : start + 50]
        gws(
            "slides",
            "presentations",
            "batchUpdate",
            params={"presentationId": presentation_id},
            body={"requests": chunk},
            dry_run=dry_run,
        )
    return warnings


def session_title(session_dir: Path) -> str:
    return session_dir.name


def course_title(course_dir: Path) -> str:
    return course_dir.name


def numbered_sessions(course_dir: Path) -> list[Path]:
    return sorted([p for p in course_dir.iterdir() if p.is_dir() and re.match(r"\d{2}-", p.name)], key=lambda p: p.name)


def export_session(session_dir: Path, args: argparse.Namespace, root_folder: dict[str, Any] | None = None) -> dict[str, Any]:
    session_dir = session_dir.resolve()
    if "非公開" in session_dir.parts:
        raise ExportError(f"Refusing to export private folder: {session_dir}")
    course_dir = session_dir.parent
    images = collect_slide_images(session_dir)
    notes = parse_speaker_notes(session_dir / "講師台本.md")
    missing_notes = [p.stem.upper() for p in images if p.stem.upper() not in notes]
    if missing_notes and not args.allow_missing_notes:
        raise ExportError("Missing notes for slide images: " + ", ".join(missing_notes))

    print(f"Session: {session_dir}")
    print(f"Slide images: {len(images)}")
    print(f"Speaker-note blocks: {len(notes)}")
    if args.dry_run:
        print("Dry run: no Drive or Slides changes will be made.")

    root = root_folder
    if root is None:
        if args.root_folder_id:
            root = {"id": args.root_folder_id, "name": args.root_folder_name, "created": False}
        else:
            root = ensure_folder(args.root_folder_name, None, dry_run=args.dry_run)
    course_folder = ensure_folder(course_title(course_dir), root.get("id"), dry_run=args.dry_run)
    session_folder = ensure_folder(session_title(session_dir), course_folder.get("id"), dry_run=args.dry_run)
    materials = upload_session_materials(session_dir, session_folder, dry_run=args.dry_run)

    deck_title = args.deck_title or session_title(session_dir)
    canva_bundle_path: Path | None = None
    warnings = []
    existing_deck = find_existing_file(
        deck_title,
        session_folder.get("id"),
        dry_run=args.dry_run,
        mime_type=GOOGLE_SLIDES_MIME,
    )
    if existing_deck:
        if args.canva_pptx_dir:
            with tempfile.TemporaryDirectory(prefix="ai-training-gws-", dir=temp_parent_dir(args.tmp_dir)) as tmp:
                pptx_path = Path(tmp) / f"{deck_title}.pptx"
                build_pptx(images, pptx_path, deck_title)
                canva_bundle_path = write_canva_bundle(
                    pptx_path,
                    args.canva_pptx_dir,
                    session_dir,
                    dry_run=args.dry_run,
                )
        if existing_deck.get("duplicateCount", 1) > 1:
            warnings.append(f"Multiple Google Slides decks already exist for: {deck_title}")
        presentation = {**existing_deck, "created": False, "skipped": True}
    else:
        with tempfile.TemporaryDirectory(prefix="ai-training-gws-", dir=temp_parent_dir(args.tmp_dir)) as tmp:
            pptx_path = Path(tmp) / f"{deck_title}.pptx"
            build_pptx(images, pptx_path, deck_title)
            if args.keep_pptx:
                keep_path = Path(args.keep_pptx).expanduser()
                keep_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(pptx_path, keep_path)
            presentation = gws(
                "drive",
                "files",
                "create",
                params={"fields": "id,name,mimeType,webViewLink,modifiedTime", "supportsAllDrives": True},
                body={"name": deck_title, "parents": [session_folder.get("id")], "mimeType": GOOGLE_SLIDES_MIME},
                upload=pptx_path,
                upload_content_type=PPTX_MIME,
                dry_run=args.dry_run,
            )
            if args.canva_pptx_dir:
                canva_bundle_path = write_canva_bundle(
                    pptx_path,
                    args.canva_pptx_dir,
                    session_dir,
                    dry_run=args.dry_run,
                )
        if args.dry_run:
            presentation = {"id": dryrun_id("slides", deck_title), "name": deck_title}
        presentation = {**presentation, "created": True, "skipped": False}
        if presentation.get("id") and not args.dry_run:
            warnings = insert_speaker_notes(presentation["id"], images, notes, dry_run=args.dry_run)
    warnings.extend(materials.get("warnings", []))

    result = {
        "rootFolder": root,
        "courseFolder": course_folder,
        "sessionFolder": session_folder,
        "presentation": presentation,
        "materials": materials,
        "canvaPptxPath": str(canva_bundle_path) if canva_bundle_path else "",
        "slideImageCount": len(images),
        "speakerNoteBlockCount": len(notes),
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--session-dir", help="One session folder containing スライド画像/ and 講師台本.md")
    parser.add_argument("--course-dir", help="Course folder. Use with --all-sessions.")
    parser.add_argument("--all-sessions", action="store_true", help="Export all numbered sessions under --course-dir")
    parser.add_argument("--root-folder-name", default="AI法人研修", help="Drive root folder name")
    parser.add_argument("--root-folder-id", help="Known Drive folder ID to use as root")
    parser.add_argument("--deck-title", help="Override Google Slides title for a single session")
    parser.add_argument("--allow-missing-notes", action="store_true", help="Continue even when Sxx image has no script block")
    parser.add_argument(
        "--canva-pptx-dir",
        help="Write per-session PPTX bundle here for Canva single-presentation import workflows",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print planned gws commands without changing Drive")
    parser.add_argument("--report-json", help="Write JSON report. Prefer 非公開/ for Drive links.")
    parser.add_argument("--keep-pptx", help="Keep the temporary PPTX at this path for debugging")
    parser.add_argument(
        "--tmp-dir",
        default="書き出し/gws-ai-training-slide-exporter/tmp",
        help=(
            "Repository-local temp directory for PPTX upload files used by this gws-based exporter. "
            "Some gws --upload calls in this environment reject files outside the current repository; "
            "this does not apply to rclone Drive copies."
        ),
    )
    args = parser.parse_args()
    if args.all_sessions:
        if not args.course_dir:
            parser.error("--all-sessions requires --course-dir")
    elif not args.session_dir:
        parser.error("Provide --session-dir, or --course-dir with --all-sessions")
    if args.deck_title and args.all_sessions:
        parser.error("--deck-title is only valid with one --session-dir")
    return args


def main() -> int:
    args = parse_args()
    try:
        sessions = numbered_sessions(Path(args.course_dir)) if args.all_sessions else [Path(args.session_dir)]
        root_folder = {"id": args.root_folder_id, "name": args.root_folder_name, "created": False} if args.root_folder_id else None
        if args.all_sessions and not args.root_folder_id:
            root_folder = ensure_folder(args.root_folder_name, None, dry_run=args.dry_run)
        results = [export_session(session, args, root_folder=root_folder) for session in sessions]
        if args.report_json:
            report_path = Path(args.report_json)
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
        return 0
    except ExportError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
