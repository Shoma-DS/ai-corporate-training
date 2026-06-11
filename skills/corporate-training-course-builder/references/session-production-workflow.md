# Session Production Workflow

Use this checklist when turning a session request into complete materials.

## Intake

- Identify course folder and target session folder.
- Treat one-phrase requests such as "4回目の台本とスライド画像まで作って" or "何回目の台本とスライド作って" as end-to-end production requests, not outline-only requests. Continue through script, prompts, handouts/data, and final slide images.
- Read prior and next session summaries to preserve continuity.
- Read existing slide plan, worksheet, syllabus, brochure, and whole-course notes.
- Decide the learner output for this session: worksheet, data table, proposal, prompt set, prototype, operating plan, or presentation.
- If the material is for Manabi DX level 3 or advanced digital talent positioning, decide the business-transformation capability first. Do not start from the tool list.
- If the material will be submitted for subsidy screening, set the acceptance standard before writing: the pamphlet and slides alone must explain the course well enough for pass/fail review. Instructor comments, speaker notes, and scripts are not screening evidence.
- Check whether this session looks too similar to nearby sessions or previous courses. If the only differences are tool names, rewrite the session around theme-specific concepts, data, constraints, demos, and outputs.

## Research

- Browse when facts may have changed or when official logos/screenshots/service capabilities are needed.
- Prefer official product docs, official brand resources, public case studies, public-sector sources, or primary vendor updates.
- When the user asks to check online concrete examples, practitioner examples, use cases, Udemy-like course curricula, or ways to add course-specific color, also read `public-case-research-workflow.md`. Include public course outlines, official sources, and practitioner sources such as Qiita, Zenn, note, personal blogs, company tech blogs, forums, and public walkthroughs.
- For a session in a course that feels generic, use research to add a theme-specific deep dive: official feature constraints, public course-outline omissions, realistic edge cases, data models, governance points, or a signature exercise.
- Save a concise memo in the course-level `全体/調査/` with URL, access date, and how the source affects the course/session.

## Slide Plan

- Read `スライド/テンプレート/カタログ.yml` before planning visuals.
- If multiple templates fit, follow `スライド/スライド生成テンプレート選択フロー.md`; otherwise state the selected template ID and reason.
- Read the selected template's `source_file` and use its style tags, palette, default slide mapping, and diagram patterns.
- For 120 minutes, target roughly 35-45 slides unless the format clearly needs fewer or more.
- For submission-facing decks such as Manabi DX screening, assume reviewers see only slides and pamphlets. Slides must be understandable without instructor comments, speaker notes, or a live explanation.
- Each slide should show the main point in a conclusion-style headline, then use body text and a visible structure to explain the content. Include what learners do, the business purpose, key steps, outputs, and review/checkpoints when relevant.
- Do not leave important explanations only in `講師台本.md`. If the script contains a concept needed for screening, promote a concise version onto the slide or into the pamphlet.
- Avoid both extremes: do not make sparse decorative slides that require narration, and do not use unstructured bullet dumps. Rebuild bullets into sequence, comparison, classification, issue -> action -> effect, cause -> result, or conclusion + reasons.
- Use slide density appropriate for screening. A clean slide is not enough if it only shows a mood image, a title, or a few abstract labels. Include 3-6 meaningful content blocks when needed: learning action, procedure, tool role, output, review point, and business connection.
- For future slide images in any course, use the recent S02 "導入判断キャンバス" sample as the minimum visual-density benchmark: a finished Google Workspace-style slide with a So What headline, compact course/session header, multiple structured cards or a table/process/checklist/canvas, an output or exercise band, and risk/source/review notes when relevant.
- Make session-opening and exercise slides especially explicit. They should show what the learner will create, what files/data are used, how the work is checked, and how it connects to the final practical output.
- If a stakeholder says "講師コメントを読めば分かるがスライドだけでは想像しにくい", treat that as a slide failure. Rewrite the slide text and structure rather than only changing the script.
- Add a slide when the topic changes, the instructor switches to a work screen, an exercise begins, or a case/example is introduced.
- Mark each slide with selected template ID, material type, and diagram pattern when relevant: diagram, screenshot, official logo, screen-share transition, exercise, source/case, or summary.
- Do not make every slide an abstract diagram. Use real screenshots for UI and service explanation.
- When a live operation or recorded work screen is planned, create a transition slide such as "ここから画面共有で確認します" rather than embedding a fake work-scene frame in the slide.
- For level 3-facing slides, keep "business transformation -> requirements -> workflow/data design -> implementation -> operation -> KPI/proposal" visible as the learning progression. Avoid titles that make the deck look like "Google Workspace活用", "GAS入門", or another tool-introduction course unless that is explicitly the user's intent.
- Add slides that prove this is the requested theme, not a generic DX course: official-feature deep dives, theme-specific workflow diagrams, actual data/source types, tool-specific constraints, distinctive risks, and a signature learner output.
- When rebuilding a session to match another course's "情報量" or "具体度", transfer only the density pattern: So What headline, 3-6 content blocks, visible structure, industry examples, numeric sense, screenshot/source instruction, and detailed exercise output. Do not transfer the reference course's content, chapter order, wording, or examples.
- For AX/DX workshop sessions, the accepted PDFs `AX・DXワークショップ講座_第1回 .pdf` and `AX・DXワークショップ講座_第2回.pdf` are the local density benchmarks. Keep the same single entrypoint and checklist here; do not create a separate skill or separate AX/DX-only workflow. Use the PDFs to judge each slide's information density and specificity, not to force the same total slide count or chapter order.
- For high-density rebuilds, every slide should normally include:
  - `**ヘッドライン:**` with the conclusion or So What.
  - A visible structure such as comparison, process, checklist, Before/After, issue -> action -> effect, output map, or rubric.
  - 3-6 meaningful blocks when the slide is explanatory or submission-facing.
  - `**図解パターン:**` or another material/pattern marker.
  - `**テンプレートID:**`.
  - `**スクリーンショット:**` or `なし`, with source/capture condition when useful.
- Exercise and demo slides must identify the file/data to open, the learner action, the output, the review/self-check criteria, and the next-session or final-output connection.
- Do not fill every slide with generic bullets just to increase volume. Increase density by adding concrete business context, tool-specific constraints, realistic examples, output names, review criteria, and operation checks.
- When a slide is about an actual service, UI, or operation flow, decide explicitly whether the best material is an official/public screenshot, a dummy-environment screenshot, an official logo, a public case image, a generated diagram, or a screen-share transition. Record that decision in the slide plan.
- If the user asks for "Web検索→自動DL" of examples or screenshots, first prefer official/static assets that can be downloaded safely. If a page requires login, contains private user data, or is JS-rendered, save the URL and capture instructions instead of forcing an unsafe download.

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
- Make exercise data and handouts theme-specific. Avoid reusing the same CSV columns, sample scenarios, and output names across different courses unless the reuse is intentionally documented.

## Image Prompts And Slide Images

- Use existing slide template catalog when available.
- Treat `スライド/テンプレート/カタログ.yml` and the selected template `source_file` as the visual style source of truth.
- For the current main style, use `isometric-corporate-clean`: clean white or very pale blue-gray background, navy/blue/teal/mint/light-gray palette, card-based organization, subtle lines and shadows, corporate isometric diagrams, and compatibility with real screenshots and official logos.
- Each prompt should include the exact in-image Japanese text.
- Each prompt should include the selected template ID and diagram pattern, or explain why the slide uses a screenshot/official logo/screen-share transition instead of a diagram.
- Each prompt should describe the complete finished slide, not a blank design template. Include exact card labels, table columns, process steps, exercise/output/review text, risk/source notes, and where the isometric scene or official material appears.
- Do not use prompt boilerplate that only changes the title. If the prompt does not specify the content blocks and layout, repair it before image generation.
- For official logos, use local reference assets from repository-level `素材/ロゴ/`; do not invent them from memory.
- When regenerating a flawed slide image, create a whole new raster image with `imagegen` if the user asks for regeneration or GPT image 2. Do not patch over the old image with overlays or deterministic redraws unless explicitly requested.
- If the request specifically says GPT image 2, one complete image, or no overlay/local conversion, generate the final visual as a bitmap image. Do not create SVG, HTML/CSS, canvas, screenshots, ImageMagick/rsvg/PIL conversions, tracing, or local compositing as intermediates.
- Copy or move the generated bitmap into `スライド画像/Sxx.png` without modifying its pixels.
- Load relevant logo files from `素材/ロゴ/` as image references before generating. If logo files exist, do not include `素材配置枠`, `公式ロゴ`, dashed logo boxes, or empty placeholder slots.
- Use the user's latest wording exactly. Remove stale labels and old product pairings from the prompt and inspect the final image for those terms before saving.
- For UI/screens, use session-local `スクリーンショット/`.
- Save final images as `スライド画像/Sxx.png`.
- Inspect images for readable text, wrong wording, layout overlap, and old terminology.
- Reject and regenerate the whole image if it has important Japanese text errors, wrong service/output names, empty placeholders, missing exercise/output/risk content, sparse title-only composition, unreadable tiny text, or visible overlap. Do not repair with local text overlays.
- If the user objects to SVG/HTML generation, asks for GPT image 2, or asks to rebuild from image generation, delete stale generated slide images only after confirming the scope, then regenerate complete bitmap images. Keep plans/scripts/prompts unless explicitly told to delete them.
- Never create slide images through SVG, HTML/CSS, canvas, browser screenshots, ImageMagick, PIL, rsvg conversion, local rasterization, tracing, local compositing, or post-generation text/logo overlays.
- The only acceptable final-image path for generated training slides is GPT image 2 / built-in image generation as a complete raster slide, followed by moving or copying the generated bitmap into `スライド画像/Sxx.png` without pixel modification.

## Canva Delivery

- Default to image-first Canva delivery: one multi-page presentation per session made from `スライド画像/Sxx.png`.
- Use `skills/gws-ai-training-slide-exporter` for Google Slides export, speaker notes, and Canva-ready PPTX bundles.
- Create the initial Canva deck through MCP/API or PPTX import before any browser Magic Layers work, with `S01.png` through the final slide arranged as consecutive pages.
- Do not make all pages Magic Layers by default. This is too costly for high-slide-count training decks and often unnecessary.
- Create a private manual Magic Layers target list for only pages likely to be edited after import: cover, section dividers, company/date/instructor placeholders, curriculum tables, learner output summaries, and proposal/customization pages.
- Leave fixed visual explanation pages, screenshots, screen-share transition pages, exercise instructions, and summaries as flat images unless the user explicitly asks otherwise.
- If browser Magic Layers is requested, apply it one page at a time, wait for completion, compare the result against the source image for Japanese text corruption, wording changes, missing objects, overlaps, and layout collapse, then undo and retry failed pages before moving on.
- If the same page fails Magic Layers 3 times, stop converting that page and keep the original image page. Record the failure pattern and add any reusable check item to `skills/gws-ai-training-slide-exporter/references/canva-quality-checklist.md`.
- Store page-level Magic Layers status, retries, and repair notes under `非公開/Canva/`; do not write design IDs or edit URLs into public files.
- Store Canva URLs, design IDs, and editing notes only in `非公開/Canva/` or the private Google Drive sync destination.

## Parallel Production

- When the user asks for subagents or parallelization, the main agent chooses one fixed template ID for the session before assigning work.
- Split parallel slide image generation into disjoint `Sxx` batches and make each image worker responsible only for its assigned files.
- Image workers must generate complete raster slide images with GPT image 2 / built-in image generation only. Do not use SVG, HTML/CSS, canvas, browser screenshots, local conversion, local compositing, or overlays.
- For Canva or other browser operations, use a separate browser-control worker when the environment supports subagents and model selection, even if the user did not explicitly ask for parallelization. Prefer `codex-5.3spark` / `GPT-5.3 Codex Spark` for repetitive Kimi WebBridge navigation, clicking, waiting, screenshots, and first-pass visual checks so the Spark usage allowance is used. Keep the main agent responsible for acceptance decisions, public-safety judgment, wording, and integration. Use image-capable high-accuracy generation only when a slide image must be regenerated.
- The main agent keeps progress visible, reconciles subagent outputs, and checks that scripts, prompts, handouts/data, filenames, and generated images match.

## Verification

- Count slides in every artifact and compare titles.
- Confirm the session has at least one theme-specific concept, example, dataset, official-source point, or exercise that would not fit unchanged in another course.
- Confirm public course-outline research, if used, influenced the structure only as abstracted themes/gaps and did not copy paid or copyrighted course content.
- For submission-facing decks, sample the slides without reading `講師台本.md` and confirm a first-time reviewer can identify the topic, learning action, expected output, and reason for the slide.
- Perform a reviewer-only pass: open only `<講座名>_パンフレット.pdf` and the slide deck/images, then answer "what course is this?", "what does each session do?", "what outputs are created?", and "how are learning hours/LMS/completion handled?". If any answer requires `講師台本.md`, revise the submitted materials.
- Search for public-facing labels such as `レベル3相当の評価観点`; replace them with learner-centered wording such as `本講座受講後の到達点` unless the user explicitly wants internal mapping language.
- Confirm delivery format language. For e-learning reskilling courses, use e-learning and LMS recording language; do not leave `オンラインワークショップ` or `ハイブリッド` in public-facing pamphlet text unless explicitly requested.
- Use the stakeholder-approved LMS wording or a close equivalent: `eラーニング。本研修は、LMS(学習管理システム:Learning Management System)を利用し、各自の受講状況や受講時間を全て記録することで、受講者の学習状況の把握を行い、適切なスキルアップをサポートいたします。`
- Add the minute values inside each session curriculum table and confirm they total the stated duration, usually 120 minutes.
- If an HTML pamphlet was changed, regenerate `<講座名>_パンフレット.pdf` and verify the PDF text/preview contains the correction. Do not assume the PDF was updated just because the HTML was updated.
- Confirm that `画像生成プロンプト.md` records a selected template ID and that diagram pattern IDs match `スライド/テンプレート/カタログ.yml` or the selected template file.
- Confirm that prompts and generated images meet the dense-slide benchmark; blank templates and "text later" assumptions fail verification.
- Parse all changed CSV files with Python's `csv` module.
- Confirm each session references only data in its own `演習データ/` folder unless a shared course-level dataset is explicitly documented.
- Search for stale deleted filenames after session-specific data cleanup.
- Search for stale paths such as per-session `素材/ロゴ/`, `素材/スクリーンショット/`, `素材/作業風景/`, or per-session `調査/`.
- Search for unsafe data patterns: emails, phone numbers, real names, customer-like records, prices, contact details, API keys.
- Confirm that source notes exist for logos, screenshots, external facts, and case studies.
- For high-density rebuilds, mechanically verify the basics:
  - `rg -c '^### S[0-9][0-9]' スライド案.md`
  - `rg -c '^\*\*ヘッドライン:\*\*' スライド案.md`
  - Confirm both counts match.
  - Confirm the time allocation table totals the stated duration, usually 120 minutes.
  - Confirm screenshot references either point to existing files, official URLs, or clearly marked dummy-environment capture tasks.
- For public-example-driven revisions, confirm the source memo separates official facts from practitioner patterns and records rejected ideas that were outdated, paid-feature dependent, unsafe, or too specific.
- For level 3-facing brochures or application materials, search for stale tool-first framing such as "ツール操作", "ツール紹介", "○○活用講座", or a title that leads with a product name. Reframe to issue analysis, As-Is/To-Be, requirements definition, operating design, logs/exception handling, KPI, rollout, and improvement proposal.
