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

## Fixed Wireframe Standard (2026-07-07 revision)

All future editable decks use one fixed 16:9 wireframe (720x405pt) on every slide. Coordinates below are pt, matching `skills/gws-ai-training-slide-exporter/scripts/export_editable_ai_training_slides_to_gws.py`. This revision compacts the header into one row and moves the headline below the diagram as a closing statement, based on a manually-tuned reference slide; do not revert to the pre-2026-07-07 two-row-header / headline-under-title layout.

- Shared background: `全体/素材/スライド背景ワイヤーフレーム.png` (text-free header band, teal rule, footer band) set as the page background for every slide. Generated once per course via GPT image 2 from `全体/素材/スライド背景ワイヤーフレーム生成プロンプト.md`.
- Header is a single compact row: course title (x26,y10,w445,h14,font7.4,gray), session/text name (x198,y9.5,w445,h16,font8.2,teal bold) placed inline to the right of the course title, section name (x471,y15,w218,h17,font7.4,gray), Sxx (x632,y10,w55,h22,font15,teal bold). No separator line/rule below the header.
- Title sits directly under the header: x27,y32,w658,h32,font19,navy bold. This is the topic label for the slide (do not pair it with a headline directly beneath it anymore).
- Diagram zone is unchanged in size/position by default: x60,y58,w600,h322. All `図解パーツ/Sxx.png` are generated at the same 1536x1024 size with the top ~20% left blank so the overlaid header/title stay readable. (A course may instead ask for a wider diagram zone spanning the full content width, e.g. x26,w668 — confirm with the user before changing this per-course, since it changes the image's effective aspect ratio.)
- Headline is placed as a closing/conclusion statement overlaid near the bottom of the diagram zone, just above the TOC strip: x51,y356,w617,h22,font12.5,teal bold. Because both the title and the headline are drawn on top of the diagram image, the exporter draws two opaque white background rectangles first so text stays legible regardless of what the diagram image contains at that position: a header band (x24,y6,w672,h60, behind course/session/sid/section/title) and a headline band (x24,y350,w672,h32, behind the headline). Diagram content that happens to fall under either band will be visually covered — this is expected, not a bug; if a specific diagram's important content is being hidden, regenerate that diagram to keep its top ~20% and bottom ~8% blank rather than shrinking the bands.
- Bottom TOC strip on every page: six/seven chapter chips (short names from the plan's `## 目次ストリップ表示名` table), current chapter teal-filled; drawn by the exporter, so the current position is visible on every slide.
- Chapter divider slides (`章見出し` in the title) are intentionally low-density hero visuals: the current chapter name rendered huge with a chapter rail (done/current/next) and one output line. The prompt builder emits a special sparse transition prompt for them; do not apply the 8-20-cell density rule to dividers. They use the same header/title/headline positions as regular slides.
- Reduce slide count by merging duplicated content (repeated divider boilerplate, duplicated case studies, repeated check-scene tables, duplicated fill-in examples, per-chapter summary slides), never by deleting information. Record the old-to-new mapping table inside `スライド案.md`.
- Target slide count per 120-minute session going forward is **around 30 slides** (down from the earlier 35-45 guidance), applied by merging repeated phrasing and boilerplate, not by cutting content. See "Session Density Target" below.

## Session Density Target (2026-07-07)

For new sessions built after 2026-07-07, aim for **~30 slides per 120-minute session** (previously 35-45). This is a merging/tightening pass, not a content cut:

- Before finalizing `スライド案.md`, do a redundancy pass across the whole session: find slides that restate the same judgment axis, repeat the same closing/summary phrasing, duplicate a case study or example already shown, or re-explain an exercise that was already explained. Merge these into the earlier or later slide that already carries the same information, and record the merge in an old-to-new mapping table in `スライド案.md` (see the GAS course session files for the mapping table format).
- Do not shorten individual slides' information density to hit the count; a merged slide may legitimately carry more content blocks than a single-purpose slide did before.
- Chapter divider slides, screen-share transition slides, and exercise/self-review slides are the most common source of repeated boilerplate phrasing across a session — check these first.
- (2026-07-08 update) The user explicitly asked to retrofit the GAS course too, once the full-raster wireframe workflow (see SKILL.md's "Fixed Layout Wireframe Standard") replaced the editable-Slides pilot as the default. The GAS course is no longer exempt: apply the ~30-slide target and the wireframe-referenced full-raster regeneration to all 6 GAS sessions.
- (2026-07-15 incident) The 2026-07-08 GAS course retrofit only rebuilt local `スライド案.md`/`画像生成プロンプト.md`/`スライド画像/Sxx.png`. The client-reviewed Drive decks for sessions 3-6 (and initially the images for session 2) were never re-exported with `export_full_raster_slides_per_image_to_gws.py --replace-existing-decks`, so the client kept seeing the old editable-template export — the exact header/headline white-background-rectangle-over-diagram behavior described above (line 37), which reads as "a leftover text box placed after the fact" once the diagram underneath it is already a complete full-raster image. See SKILL.md's "Export-Method Consistency And Legacy Artifact Cleanup" section: retrofitting a session away from this workflow is not complete until its Drive deck is re-exported and its `Googleスライド編集用アウトライン.md` / `図解パーツ生成プロンプト.md` / `図解パーツ/` are deleted, not just left unused locally.

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
