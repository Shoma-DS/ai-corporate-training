# Editable Google Slides Workflow

Use this workflow when a submission or reviewer specifically needs text that can be inspected and edited in Google Slides or an HTML/editable slide template, especially Manabi DX comments about template consistency, section boundaries, slide numbers, text names, or session-output consistency.

## When To Use

- A reviewer says the deck is hard to examine because slide templates, course names, text names, or Sxx slide numbers are inconsistent.
- A reviewer says a 35-45 slide session lacks visible section/block names.
- The user asks to keep the existing information density but make the material editable in Google Slides.
- The user asks to generate diagrams or supplemental reference-sheet images separately and attach them to an HTML/editable slide template.

Do not use this workflow to replace GPT image 2 / full-raster slide-image generation for image-first Canva delivery, visual decks, or user requests for one complete bitmap slide. This is a submission-text workflow.

## Source Files

Course-level:

- `全体/Google_Slides編集可能テンプレート仕様.md`
- `全体/再申請用_テキスト名成果物対応表.md`
- `全体/Google_Slides編集可能化_整合性レポート.md`

Session-level:

- `Googleスライド編集用アウトライン.md`
- `図解パーツ生成プロンプト.md`
- `図解パーツ/Sxx.png` as generated raster supplemental diagrams/reference-sheet images embedded into the editable deck
- Existing `画像生成プロンプト.md` may remain as a historical full-raster prompt, but must clearly say it is reference-only when this workflow is active.

## Production Steps

1. Keep `スライド案.md` as the dense content source. Do not thin the slide text to make layout easier.
2. Create a course-level editable template specification that fixes the same header positions for course title, session/text name, Sxx number, and section name.
3. Create or refresh the text/output correspondence table. Each session should have a clear 2-hour text name and a consistent primary-output count, usually 3 primary outputs for the GAS course.
   - For every course, not only GAS, make the session navigation explicit. Add an early `目次/全体像` slide and a `章見出し/現在位置` slide at each major section boundary. The section slide must show the current agenda item, nearby agenda items, upcoming decision points, and the output it supports.
4. Generate session-level editable outlines and diagram-part prompts:

```bash
python3 scripts/build_editable_google_slides_sources.py
```

5. Use `図解パーツ生成プロンプト.md` only for dense supplemental diagram/reference-sheet images that will be attached to the editable template. Do not generate duplicate full deck pages with editable headers from it. Diagram prompts are not text-free by default and are not short-label-only by default: each required image should normally include readable Japanese headings, table cells, card text, process names, output names, decision axes, learner actions, concrete examples, and review/risk notes. Keep authoritative course title, session title, Sxx number, section names, full slide titles, speaker notes, and long paragraphs as editable Google Slides/HTML objects, but allow core comparison/process/example table cells inside the generated image when they are the source slide's main information. Prefer wide landscape images that are slightly shorter vertically than a full slide so the template title, current section, and slide number remain clear.
6. Generate one PNG per required slide as `図解パーツ/Sxx.png` using Codex App Server / GPT image 2 through the `imagegen` skill. If the user writes `imagen`, treat it as this same path. Do not use `OPENAI_API_KEY`, OpenAI API CLI fallback, one-off SDK scripts, or API-key checks for this normal course-image path. Do not create placeholders for missing diagrams, do not use local drawing/rasterization as a substitute for image generation, and reject images that contain wrong or unreadable Japanese text, fake UI/logos, recruitment-ad layouts, stale course names, decorative text-free visuals, or short-label-only visuals with no supplemental explanation. A diagram that is visibly much sparser than the source slide, such as reducing a Before/After table and industry examples to a few icons, also fails.
   - Run lightweight checks on every generated diagram PNG: missing files, valid bitmap/MIME, dimensions/aspect, abnormal file size, duplicate hashes, generation-log pending/error states, stale course names, and forbidden terms by OCR/search where available. Visually inspect only diagrams flagged by lightweight checks, diagrams with suspicious OCR, diagrams using official logos/screenshots/new UI material, or diagrams the user specifically asks to inspect.
   - If Codex App Server / `imagegen` returns `502 Bad Gateway`, response-not-complete, WebSocket close, or similar transport error, do not stop the batch. Check the current worker's `$CODEX_HOME/generated_images/<session-id>/`, copy delayed output with `scripts/copy_latest_generated_image.py --wait-seconds 120 --missing-ok --status-json ...` when available, and otherwise mark that Sxx pending and continue.
   - In parallel diagram generation, each worker must copy only from its own `$CODEX_HOME/generated_images/<session-id>/` directory. Do not select the newest image from the global generated image tree, because that can place another worker's diagram into the wrong `図解パーツ/Sxx.png`.
   - In single-worker sequential generation, touch a marker file immediately before each `imagegen` call, then copy with `python3 scripts/copy_latest_generated_image.py --marker <marker> --target '<session>/図解パーツ/Sxx.png' --expect-mime image/png --wait-seconds 120 --missing-ok --status-json '非公開/imagegen-status/Sxx.json'`. If no new bitmap appears, record the slide pending and continue instead of stopping the whole batch. If more than one new bitmap appears, stop instead of guessing unless restricted by `--session-id` and `--allow-latest-in-session`. Do not rename WebP/JPEG output to `.png`; regenerate until a real PNG is available.
7. Export native editable Google Slides through the downstream GWS helper. Text-only export is a debugging exception only:

```bash
python3 skills/gws-ai-training-slide-exporter/scripts/export_editable_ai_training_slides_to_gws.py \
  --course-dir '講座/COURSE' \
  --all-sessions \
  --replace-existing-decks \
  --allow-text-only-template-export \
  --write-link-index \
  --report-json '非公開/gws-export/editable-slides-text-only-debug.json' \
  --dry-run
```

Do not use the text-only exception for a finished deck.

Standard live export with generated diagram parts embedded:

```bash
python3 skills/gws-ai-training-slide-exporter/scripts/export_editable_ai_training_slides_to_gws.py \
  --course-dir '講座/COURSE' \
  --all-sessions \
  --replace-existing-decks \
  --embed-diagram-parts \
  --make-diagram-images-readable-by-link \
  --write-link-index \
  --report-json '非公開/gws-export/editable-slides-with-diagrams-report.json'
```

Use `--dry-run` first unless the user explicitly asks to create/upload immediately. `--make-diagram-images-readable-by-link` is required for the Slides API image URL fetch path; use it only for public-safe generated diagram PNGs. Exporting without `--embed-diagram-parts` is an exception for debugging or text-only review, not the finished route for future courses.

## Verification

- Slide counts match between `スライド案.md`, `Googleスライド編集用アウトライン.md`, and `図解パーツ生成プロンプト.md`.
- `図解パーツ/Sxx.png` exists for every slide that should have a supplemental visual, is non-empty, and has passed lightweight checks before export.
- Visual inspection records list only diagrams escalated from lightweight checks, suspicious OCR, official logo/screenshot/new UI material, or explicit user request.
- Image text is readable, accurate, and consistent with the editable slide text. Short labels alone are not enough when the source slide carries process, criteria, outputs, risks, or examples; include enough table cells, card text, and concrete examples so the image can be understood when viewed on its own. Use S04-style density when the source slide contains multiple structures.
- Run `python3 scripts/check_diagram_parts.py --course-dir '講座/COURSE'` before export. Duplicate hashes across different `図解パーツ/Sxx.png` files, non-PNG files, portrait/tiny placeholder dimensions, or missing images fail verification and must be regenerated. Use the older `scripts/check_diagram_integrity.py` only for the fixed Google Workspace/GAS course.
- The editable Slides exporter also validates embedded diagram files as real landscape PNGs before upload; invalid `Sxx.png` files are skipped with warnings instead of being sent to Drive/Slides with the wrong content type.
- Every Google Slides page has course title, session/text name, Sxx number, and section name in the same location.
- Each session has an agenda/overview slide and section-start signpost slides that clearly show the current position. A deck where reviewers must infer the section from slide titles alone is not complete.
- Embedded diagrams/reference-sheet images do not cover editable text boxes and are positioned as center, lower, or right-side reference visuals attached to the template. For dense slides, the image may be the main visual body while the template keeps the header/title/section text editable.
- The deck does not rely on speaker notes for screening evidence.
- Session names and primary outputs match `全体/再申請用_テキスト名成果物対応表.md`.
- Existing full-raster `画像生成プロンプト.md` files are marked reference-only when the editable workflow is active.
- Search for legacy course names and accidental cross-session slide references such as `第4回 S02` inside a different session.
