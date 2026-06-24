# Editable Google Slides Workflow

Use this workflow when a submission or reviewer specifically needs text that can be inspected and edited in Google Slides, especially Manabi DX comments about template consistency, section boundaries, slide numbers, text names, or session-output consistency.

## When To Use

- A reviewer says the deck is hard to examine because slide templates, course names, text names, or Sxx slide numbers are inconsistent.
- A reviewer says a 35-45 slide session lacks visible section/block names.
- The user asks to keep the existing information density but make the material editable in Google Slides.
- The user asks to generate diagrams separately and place editable text in Google Slides.

Do not use this workflow to replace GPT image 2 / full-raster slide-image generation for image-first Canva delivery, visual decks, or user requests for one complete bitmap slide. This is a submission-text workflow.

## Source Files

Course-level:

- `全体/Google_Slides編集可能テンプレート仕様.md`
- `全体/再申請用_テキスト名成果物対応表.md`
- `全体/Google_Slides編集可能化_整合性レポート.md`

Session-level:

- `Googleスライド編集用アウトライン.md`
- `図解パーツ生成プロンプト.md`
- `図解パーツ/Sxx.png` when the user requests generated diagrams embedded into the editable deck
- Existing `画像生成プロンプト.md` may remain as a historical full-raster prompt, but must clearly say it is reference-only when this workflow is active.

## Production Steps

1. Keep `スライド案.md` as the dense content source. Do not thin the slide text to make layout easier.
2. Create a course-level editable template specification that fixes the same header positions for course title, session/text name, Sxx number, and section name.
3. Create or refresh the text/output correspondence table. Each session should have a clear 2-hour text name and a consistent primary-output count, usually 3 primary outputs for the GAS course.
4. Generate session-level editable outlines and diagram-part prompts:

```bash
python3 scripts/build_editable_google_slides_sources.py
```

5. Use `図解パーツ生成プロンプト.md` only for supplemental diagram parts. Do not generate full slide-body images from it. Diagram prompts are not required to be text-free: use no text when icons/process shapes are enough, and use short Japanese labels when they make the visual easier to understand. Keep authoritative course title, session title, Sxx number, section names, full headlines, body text, and tables as editable Google Slides objects.
6. When the user asks to embed diagrams, generate one inspected PNG per slide as `図解パーツ/Sxx.png` using Codex App Server / GPT image 2 through the `imagegen` skill. If the user writes `imagen`, treat it as this same path. Do not use `OPENAI_API_KEY`, OpenAI API CLI fallback, one-off SDK scripts, or API-key checks for this normal course-image path. Do not create placeholders for missing diagrams, do not use local drawing/rasterization as a substitute for image generation, and reject images that contain wrong or unreadable Japanese labels, excessive slide-body text, fake UI/logos, recruitment-ad layouts, or stale course names.
   - In parallel diagram generation, each worker must copy only from its own `$CODEX_HOME/generated_images/<session-id>/` directory. Do not select the newest image from the global generated image tree, because that can place another worker's diagram into the wrong `図解パーツ/Sxx.png`.
   - In single-worker sequential generation, touch a marker file immediately before each `imagegen` call, then copy with `python3 scripts/copy_latest_generated_image.py --marker <marker> --target '<session>/図解パーツ/Sxx.png' --expect-mime image/png`. If more than one new bitmap appears, stop instead of guessing. Do not rename WebP/JPEG output to `.png`; regenerate until a real PNG is available.
7. Export native editable Google Slides through the downstream GWS helper. Without diagram embedding:

```bash
python3 skills/gws-ai-training-slide-exporter/scripts/export_editable_ai_training_slides_to_gws.py \
  --course-dir '講座/COURSE' \
  --all-sessions \
  --replace-existing-decks \
  --write-link-index \
  --report-json '非公開/gws-export/editable-slides-report.json'
```

With generated diagram parts embedded:

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

Use `--dry-run` first unless the user explicitly asks to create/upload immediately. `--make-diagram-images-readable-by-link` is required for the Slides API image URL fetch path; use it only for public-safe generated diagram PNGs.

## Verification

- Slide counts match between `スライド案.md`, `Googleスライド編集用アウトライン.md`, and `図解パーツ生成プロンプト.md`.
- If diagrams are embedded, `図解パーツ/Sxx.png` exists for every slide that should have a diagram, is non-empty, and was inspected before export.
- Short labels inside diagrams, when used, are readable, accurate, and consistent with the editable slide text. Label-free diagrams are acceptable only when the visual meaning is clear without labels.
- Run `python3 scripts/check_diagram_integrity.py` before export. Duplicate hashes across different `図解パーツ/Sxx.png` files, non-PNG files, portrait/tiny placeholder dimensions, or missing images fail verification and must be regenerated.
- The editable Slides exporter also validates embedded diagram files as real landscape PNGs before upload; invalid `Sxx.png` files are skipped with warnings instead of being sent to Drive/Slides with the wrong content type.
- Every Google Slides page has course title, session/text name, Sxx number, and section name in the same location.
- Embedded diagrams do not replace the editable text, do not cover text boxes, and are positioned as center/right-side supplemental visuals.
- The deck does not rely on speaker notes for screening evidence.
- Session names and primary outputs match `全体/再申請用_テキスト名成果物対応表.md`.
- Existing full-raster `画像生成プロンプト.md` files are marked reference-only when the editable workflow is active.
- Search for legacy course names and accidental cross-session slide references such as `第4回 S02` inside a different session.
