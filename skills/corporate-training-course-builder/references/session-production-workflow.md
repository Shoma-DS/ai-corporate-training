# Session Production Workflow

Use this checklist when turning a session request into complete materials.

## Intake

- Identify course folder and target session folder.
- Treat one-phrase requests such as "4回目の台本とスライド画像まで作って" or "何回目の台本とスライド作って" as end-to-end production requests, not outline-only requests. Continue through script, prompts, handouts/data, and final slide images.
- Read prior and next session summaries to preserve continuity.
- Read existing slide plan, worksheet, syllabus, brochure, and whole-course notes.
- Decide the learner output for this session: worksheet, data table, proposal, prompt set, prototype, operating plan, or presentation.
- If the material is for Manabi DX level 3 or advanced digital talent positioning, decide the business-transformation capability first. Do not start from the tool list.

## Research

- Browse when facts may have changed or when official logos/screenshots/service capabilities are needed.
- Prefer official product docs, official brand resources, public case studies, public-sector sources, or primary vendor updates.
- When the user asks to check online concrete examples, practitioner examples, or use cases, also read `public-case-research-workflow.md` and include public practitioner sources such as Qiita, Zenn, note, personal blogs, company tech blogs, forums, and public walkthroughs.
- Save a concise memo in the course-level `全体/調査/` with URL, access date, and how the source affects the course/session.

## Slide Plan

- Read `スライド/テンプレート/カタログ.yml` before planning visuals.
- If multiple templates fit, follow `スライド/スライド生成テンプレート選択フロー.md`; otherwise state the selected template ID and reason.
- Read the selected template's `source_file` and use its style tags, palette, default slide mapping, and diagram patterns.
- For 120 minutes, target roughly 35-45 slides unless the format clearly needs fewer or more.
- Add a slide when the topic changes, the instructor switches to a work screen, an exercise begins, or a case/example is introduced.
- Mark each slide with selected template ID, material type, and diagram pattern when relevant: diagram, screenshot, official logo, screen-share transition, exercise, source/case, or summary.
- Do not make every slide an abstract diagram. Use real screenshots for UI and service explanation.
- When a live operation or recorded work screen is planned, create a transition slide such as "ここから画面共有で確認します" rather than embedding a fake work-scene frame in the slide.
- For level 3-facing slides, keep "business transformation -> requirements -> workflow/data design -> implementation -> operation -> KPI/proposal" visible as the learning progression. Avoid titles that make the deck look like "Google Workspace活用", "GAS入門", or another tool-introduction course unless that is explicitly the user's intent.

## Instructor Script

- Write exactly what the instructor says.
- Include slide-change markers, demo actions, screen-share instructions, exercise timing, and fallback paths.
- Include setup notes for files to open before class.
- Keep examples practical and reusable for business learners.

## Handouts And Data

- Create worksheets and handouts under `配布資料/` or the session root when already established locally.
- Create CSV/sample files under `演習データ/`.
- Each session's `演習データ/` should contain only files used in that session's demos, worksheet, handout, or learner output. Do not leave the same generic CSV bundle in every session.
- Use sample/anonymized data for demos and public files.
- When revising from online examples, extract workflow patterns and edge cases, then abstract them into fictional scenarios, columns, review checks, fallback steps, and source notes. Do not copy exact source prose, code, screenshots, company details, or operational data.
- If the same exercise data is duplicated in multiple session folders, read `session-specific-exercise-data-workflow.md`, decide whether the course intentionally reuses a shared dataset or the copies should diverge by session, then verify the result.
- For session-specific data revisions, add or update `演習データ/README.md`, `配布資料/演習ガイド.md`, `ワークシート.md`, and a course-level `全体/演習データ回別一覧.md` or equivalent index.
- After removing or renaming data files, update stale references in `講師台本.md`, `スライド案.md`, worksheets, handouts, syllabus, and course overview files.
- If learners will apply the workflow to their own real business data later, say so explicitly and include permission/share-range checks.

## Image Prompts And Slide Images

- Use existing slide template catalog when available.
- Treat `スライド/テンプレート/カタログ.yml` and the selected template `source_file` as the visual style source of truth.
- For the current main style, use `isometric-corporate-clean`: clean white or very pale blue-gray background, navy/blue/teal/mint/light-gray palette, card-based organization, subtle lines and shadows, corporate isometric diagrams, and compatibility with real screenshots and official logos.
- Each prompt should include the exact in-image Japanese text.
- Each prompt should include the selected template ID and diagram pattern, or explain why the slide uses a screenshot/official logo/screen-share transition instead of a diagram.
- For official logos, use local reference assets from repository-level `素材/ロゴ/`; do not invent them from memory.
- When regenerating a flawed slide image, create a whole new raster image with `imagegen` if the user asks for regeneration or GPT image 2. Do not patch over the old image with overlays or deterministic redraws unless explicitly requested.
- If the request specifically says GPT image 2, one complete image, or no overlay/local conversion, generate the final visual as a bitmap image. Do not create SVG, HTML/CSS, canvas, screenshots, ImageMagick/rsvg/PIL conversions, tracing, or local compositing as intermediates.
- Copy or move the generated bitmap into `スライド画像/Sxx.png` without modifying its pixels.
- Load relevant logo files from `素材/ロゴ/` as image references before generating. If logo files exist, do not include `素材配置枠`, `公式ロゴ`, dashed logo boxes, or empty placeholder slots.
- Use the user's latest wording exactly. Remove stale labels and old product pairings from the prompt and inspect the final image for those terms before saving.
- For UI/screens, use session-local `スクリーンショット/`.
- Save final images as `スライド画像/Sxx.png`.
- Inspect images for readable text, wrong wording, layout overlap, and old terminology.

## Parallel Production

- When the user asks for subagents or parallelization, the main agent chooses one fixed template ID for the session before assigning work.
- Split parallel slide image generation into disjoint `Sxx` batches and make each image worker responsible only for its assigned files.
- Image workers must generate complete raster slide images with GPT image 2 / built-in image generation only. Do not use SVG, HTML/CSS, canvas, browser screenshots, local conversion, local compositing, or overlays.
- The main agent keeps progress visible, reconciles subagent outputs, and checks that scripts, prompts, handouts/data, filenames, and generated images match.

## Verification

- Count slides in every artifact and compare titles.
- Confirm that `画像生成プロンプト.md` records a selected template ID and that diagram pattern IDs match `スライド/テンプレート/カタログ.yml` or the selected template file.
- Parse all changed CSV files with Python's `csv` module.
- Confirm each session references only data in its own `演習データ/` folder unless a shared course-level dataset is explicitly documented.
- Search for stale deleted filenames after session-specific data cleanup.
- Search for stale paths such as per-session `素材/ロゴ/`, `素材/スクリーンショット/`, `素材/作業風景/`, or per-session `調査/`.
- Search for unsafe data patterns: emails, phone numbers, real names, customer-like records, prices, contact details, API keys.
- Confirm that source notes exist for logos, screenshots, external facts, and case studies.
- For public-example-driven revisions, confirm the source memo separates official facts from practitioner patterns and records rejected ideas that were outdated, paid-feature dependent, unsafe, or too specific.
- For level 3-facing brochures or application materials, search for stale tool-first framing such as "ツール操作", "ツール紹介", "○○活用講座", or a title that leads with a product name. Reframe to issue analysis, As-Is/To-Be, requirements definition, operating design, logs/exception handling, KPI, rollout, and improvement proposal.
