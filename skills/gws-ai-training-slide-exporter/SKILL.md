---
name: gws-ai-training-slide-exporter
description: >-
  Use when exporting AI法人研修 course materials to Google Drive/Google Slides with gws CLI: create an AI法人研修 root folder, create course and session folders, convert local slide images into a Google Slides deck, and insert each slide's instructor script into speaker notes.
---

# GWS AI Training Slide Exporter

## Purpose

Publish local AI法人研修 session assets to Google Drive as structured course folders and Google Slides decks.

This skill is for repository sessions that contain:

- `スライド画像/Sxx.png`
- `講師台本.md`

It creates or reuses this Drive hierarchy:

```text
AI法人研修/
  講座名/
    回数フォルダ名/
      Googleスライド
```

The deck contains one local slide image per Google Slides page. Speaker notes are populated from the matching `Sxx` block in `講師台本.md`.

## Safety Rules

- Do not upload files under `非公開/`.
- Do not save Google Drive file IDs, URLs, or customer-specific links into public tracked files unless the user explicitly asks.
- Use generated/public-safe slide images and dummy data only.
- If `gws auth status` fails, stop and ask the user to run Google Workspace authentication.
- If a folder name is duplicated in Drive under the same parent, stop and ask for an explicit parent/root folder ID.

## Main Command

Use the bundled script:

```bash
python3 skills/gws-ai-training-slide-exporter/scripts/export_ai_training_slides_to_gws.py \
  --session-dir "講座/COURSE/06-SESSION"
```

Useful options:

- `--root-folder-name "AI法人研修"`: default root folder name.
- `--root-folder-id <drive-folder-id>`: use a known Drive folder instead of searching by name.
- `--course-dir "講座/COURSE"` with `--all-sessions`: export every numbered session with slide images.
- `--dry-run`: inspect the planned folder/deck work without calling `gws`.
- `--report-json 非公開/.../export-report.json`: save Drive IDs/URLs outside public tracked files.

## Workflow

1. Confirm target session/course from the user's request.
2. Check local inputs:
   - `スライド画像/Sxx.png` exists and is non-empty.
   - `講師台本.md` has `Sxx「...」` blocks.
3. Run `--dry-run` first for a new course or ambiguous target.
4. Run the export command.
5. Read the command output and report:
   - root/course/session folder names
   - created Google Slides title
   - deck URL, unless the user requested not to display it
   - any missing notes or slide-count warnings

## Implementation Notes

The script avoids public image URLs. It first builds a temporary PPTX locally from the PNG slide images, uploads the PPTX through `gws drive files create`, and asks Drive to convert it into a native Google Slides presentation. After conversion, it calls `gws slides presentations get` to find each speaker-notes object and `gws slides presentations batchUpdate` to insert the matching script text.

Do not replace this with HTML/SVG/browser screenshots. The goal is to preserve the already generated slide images exactly as slide pages.
