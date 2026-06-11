# Course Production Unified Workflow

Use this workflow when creating, rebuilding, or coordinating a whole corporate training course. It consolidates course planning, session production, image generation, and delivery handoff into one sequence.

## Role Split

- `corporate-training-course-builder`: the single entrypoint and source of truth for course/session production.
- `imagegen`: final raster image generation only. Use GPT image 2 / built-in image generation for complete bitmap slide images.
- `course-pamphlet-html-pdf`: downstream pamphlet builder for `<講座名>_パンフレット.html` and `<講座名>_パンフレット.pdf`.
- `gws-ai-training-slide-exporter`: downstream export only, after local slide images and scripts are complete.
- `codex-dynamic-workflows`: optional coordination layer for large, risky, or parallel work. It must not define a separate content standard.

## Entry Point Rule

For requests such as "講座作成", "講座を作成してください", "研修資料を作って", or similarly broad course-production language, start here through `corporate-training-course-builder`. Do not start from export, Canva, browser automation, subagent orchestration, or a newly created helper skill.

When a new local skill, checklist, or script is added for this repository, attach it to this sequence at the phase where it belongs:

- course planning and public/private source handling
- session script, slide plan, worksheet, handout, and exercise data production
- slide image prompt and GPT image 2 generation
- verification and public-safety review
- downstream pamphlet PDF, Google Drive, Google Slides, PPTX, Canva, or browser Magic Layers delivery

If a new helper cannot be placed in one of these phases, it probably should be a reference under `corporate-training-course-builder` rather than an independent skill.

## Full-Course Sequence

1. Read `AGENTS.md`, the course folder, `全体/` files, existing session folders, and relevant private source extracts without copying private details into public files.
2. Confirm course category, learner level, delivery format, standard hours, LMS/log requirements, outputs, and public-safety constraints.
3. Run a course-specific differentiation pass before drafting the syllabus. Do not simply copy the previous course's six-session shape. Identify the target theme's unique chapters, official-source constraints, public learning-market patterns, signature exercise, and theme-specific outputs.
4. Research official/vendor/public primary sources and, where useful, public course outlines such as Udemy curriculum pages, public syllabi, YouTube/blog course outlines, Qiita, Zenn, note, and product-community walkthroughs. Extract only themes, chapter ideas, learner pain points, and gaps; do not copy paid content, copyrighted prose, screenshots, quizzes, datasets, or private details.
5. Write a course-level differentiation memo in `全体/調査/` or another course-level design memo. Include: nearby existing courses compared, what will not be reused blindly, official sources that change the curriculum, public course-outline patterns, signature chapter/exercise, and theme-specific outputs.
6. Select one slide template for the course or a justified template per session. Record the template ID in slide plans and image prompts.
7. Build or revise course-level files: overview, syllabus, all-session worksheet, instructor notes, exercise-data index, `<講座名>_パンフレット.html`, `<講座名>_パンフレット.pdf`, and source memo. Do not create new pamphlets as Markdown-first deliverables; migrate existing `パンフレット原稿.md` or `パンフレット.md` only when needed. Treat the submitted pamphlet title or the user's latest explicit correction as the public-facing training-name source of truth.
8. Produce each session with `session-production-workflow.md`: slide plan, instructor script, worksheet, handouts, exercise data, image prompts, and final slide images.
9. Generate all final slide images as complete raster images with GPT image 2 / built-in image generation. Save only final PNGs in each session's `スライド画像/`. Each image must meet the repository dense-slide benchmark: So What headline, compact course/session context, structured cards/table/process/checklist/canvas, learner output or review point, and needed risk/source/screenshot handling.
10. Verify every session: slide count, prompt count, script slide markers, data references, logo/source notes, public-safety risks, image readability, course-name consistency, and whether the session still has theme-specific content rather than generic copied structure.
11. Only after local production is complete, use downstream helpers: `course-pamphlet-html-pdf` for pamphlet PDF refresh, then `gws-ai-training-slide-exporter` for Google Slides, Drive, PPTX, or Canva-ready output.

## High-Density Slide Plan Rebuild

Use this gate when the user asks to rebuild an existing course by matching another course's "情報量", "構図", "具体度", "例の出し方", or "スライドの密度". This is a quality and structure transfer, not a content transfer.

If the user names the Google Workspace/GAS course, or says "Google Workspace講座くらいの情報量", use `講座/Google Workspace・GASで進めるAI業務効率化-DX実践講座/` as the repository density benchmark. The target course must match that course's per-slide density: concrete output names, comparison tables, Before/After, process flows, industry examples, exercise instructions, review criteria, screenshot/material notes, and risk checks. Do not proceed to image generation or export while target slides still look like repeated generic bullets.

For slide images, also use the recent S02 "導入判断キャンバス" sample level as the minimum acceptance benchmark: a finished white-background Google Workspace-style slide with a clear headline, multiple structured content cards or a decision canvas, visible learner exercise/output, risk or confirmation notes where relevant, and a composed isometric business scene. A title-only image, blank template, or generic diagram does not pass even if it looks clean.

### Intake Pattern

When the user gives a request like "Google Workspace講座をこのスライドの情報量を見習って作って", apply this exact interpretation:

- The reference deck is a quality benchmark only. Imitate density, layout logic, specificity, and example style; do not inherit the reference deck's content, chapter order, claims, or examples.
- The target course keeps its own business purpose, official product constraints, data model, tools, exercises, and learner outputs.
- For all six sessions, first inspect the existing `スライド案.md`, whole-course files, and nearby accepted slides before editing.
- If the user asks for screenshots or public examples, use Web search and official/public sources to collect URLs and downloadable assets, then save only safe assets/source notes in the allowed folders.
- For large full-course changes, use a dynamic workflow with packet ownership and final integration instead of editing sessions opportunistically.

### Reference Handling

- Use the reference course only for observable production qualities: So What headlines, 3-6 content blocks per slide, tables/comparison/process/checklist structures, concrete industry examples, numeric sense, exercise detail, screenshot/case usage, and clear learner outputs.
- Do not copy the reference course's topic sequence, chapter titles, examples, claims, exercises, or wording into the target course.
- Before writing, identify what must remain target-course specific: official capabilities, constraints, data model, learner outputs, demos, risks, and final deliverables.
- For AX/DX workshop course work, the accepted PDFs `AX・DXワークショップ講座_第1回 .pdf` and `AX・DXワークショップ講座_第2回.pdf` are local quality benchmarks under this same rule. Use them only to calibrate per-slide density, concrete explanatory value, visible structures, and risk/case/example treatment. Do not treat their page counts as mandatory and do not create a separate AX/DX production workflow.

### Rebuild Shape

For each 120-minute session:

- Target 35-45 slides unless the course format requires otherwise.
- Total slide count may vary by course/session purpose, exercise load, and submission format. Do not increase or reduce slide count merely to match a reference deck; first match the density and concrete value of each individual slide.
- Keep or create a 120-minute time allocation table whose slide ranges match the actual slide headings.
- Use `### Sxx ...` for every slide and `**ヘッドライン:**` for every slide.
- Use visible structures instead of loose bullets: comparison table, process flow, classification map, checklist, Before/After, issue -> action -> effect, output map, or review rubric.
- Add 3-6 meaningful blocks per slide where appropriate: business context, tool role, example, learner action, output, check point, risk, source note, screenshot instruction. Blocks must not be repeated boilerplate; they must name the specific business situation, data/file used, decision criterion, or learner output for that slide.
- For image prompts, name the exact visible cards, labels, table columns, process steps, bottom exercise/output band, and right-side or corner isometric scene. Do not write prompts that rely on adding the real slide text later.
- At least most slides should include one concrete structured element that can stand alone in a submitted deck, such as a table, flow, checklist, case card, sample output, rubric, or exercise instruction. A headline plus generic bullets is not acceptable for a high-density rebuild.
- Place demos and exercises at natural chapter ends. Exercise slides must include steps, files/data used, output, review criteria, self-check, and how the output connects to later sessions.
- Add industry examples across the course, but keep them fictional or abstracted from public patterns. Do not use private customer details.
- Mark material needs per slide: `なし`, `スクリーンショット/...`, official logo, public case/source, screen-share transition, exercise data, or generated diagram.

### Official Assets and Screenshots

- Browse current official or primary sources when facts, capabilities, logos, UI screens, quotas, brand assets, or public cases matter.
- Save course-wide source notes in `全体/調査/` with URL, publisher, confirmation date, and how the source affected the course.
- Save official logos only in repository-level `素材/ロゴ/` with source notes.
- Save session-specific screen captures in the session's `スクリーンショット/`.
- Prefer official product pages, official docs, official help pages, official blogs, and public customer stories for source facts.
- For operation screenshots, use dummy environments or exercise data. Do not capture real accounts, customer data, file names, email addresses, API keys, billing, contract details, or private Drive/Canva URLs.
- If `curl` cannot capture a JS-rendered help/product page reliably, record the URL and capture instructions. Use browser automation only when needed, preferably through a low-cost browser worker if available.
- Do not ask image generation to invent real logos, product UI, customer screenshots, or exact official screens.

For Google Workspace/GAS courses specifically, check official Google Workspace, Google Help, Google Developers, Workspace Updates, and public customer-story pages before adding current feature claims. Download only public/official static images that are safe to store, such as official Open Graph images or press-kit/brand assets, and record their URL and use in `全体/調査/`. For screenshots of Forms, Sheets, Apps Script, Gemini, Drive, Gmail, Calendar, or Admin screens, prefer official public screenshots or a dummy environment; never capture personal Drive contents, account names, email addresses, project IDs, OAuth credentials, billing, or private file names.

### Dynamic Workflow Pattern

For a six-session full-course rebuild, use `skills/codex-dynamic-workflows/SKILL.md` as a downstream helper when parallelism or auditability helps. A reliable packet split is:

- P1: sessions 1-2 slide-plan rebuild, quality verification, and補修.
- P2: sessions 3-4 slide-plan rebuild, quality verification, and補修.
- P3: sessions 5-6 slide-plan rebuild, quality verification, and補修.
- P4: official assets, screenshots, public examples, source notes, and screenshot acquisition memos.
- P5: integrated verification, public-safety scan, workflow artifacts, and final report.

Create `.workflow/<slug>/plan.md`, `state.json`, `orchestration.md`, `packets/`, `results/`, and `final-report.md`. Run the dynamic workflow verifier before calling the rebuild complete.

Each session packet should write or repair the current `スライド案.md` directly only for its owned sessions. It should report slide count, headline count, chapter ranges, exercise count, screenshot/source needs, and any stale-path or public-safety fixes. The integration packet must inspect current files after all packet work finishes; subagent completion logs alone are not acceptance evidence.

### Goal/Handoff Prompt

When a long rebuild needs to continue in Goal mode or another agent session, prepare a handoff prompt with this structure:

```text
Objective:
Course path:
Reference quality benchmark:
Do:
Do not:
Workflow artifacts:
Packet status:
Required source/asset rules:
Verification commands:
Completion report format:
```

If the user explicitly says "クリップボードに入れて", copy this prompt with `pbcopy`. If clipboard access is unavailable, save it as `.workflow/<slug>/handoff-prompt.md` and tell the user the path.

### Completion Gate

Before completion, prove the rebuild with current-state evidence:

- For every session, count `^### S[0-9][0-9]` and `^\*\*ヘッドライン:\*\*`; counts must match.
- Confirm every 120-minute session table totals 120 minutes and references existing slide ranges.
- Confirm slide counts are usually 35-45 for 120-minute sessions.
- Search for stale slide numbers, old session ranges, old filenames, and reference-course terminology that does not belong to the target course.
- Search for unsafe data patterns and public-repo risks: real-looking emails, phone numbers, personal names, customer records, prices, contact details, credentials, API keys, private URLs, and contract details. Keep occurrences only when they are explicit "do not include" warnings or safe dummy examples such as `test-dummy@example.com`.
- Confirm source notes exist for official logos, screenshots, current service capabilities, quotas/limits, and public cases.
- Confirm screenshot folders either contain the referenced assets or the slide plan/source memo states exactly what to capture from a dummy environment.
- Confirm the public-facing course/training name is consistent across pamphlet HTML/PDF, course-level files, `スライド案.md`, `講師台本.md`, `画像生成プロンプト.md`, generated slide images, and export scripts. Search old `/` and `-` title variants, and do not allow path-only benchmark names to appear as visible titles.
- Confirm `Course`, `Session`, folder names, and other metadata in image prompts are marked as context-only when they are not intended to be rendered as visible slide text.
- Confirm image prompts and generated slide images meet the dense-slide benchmark. Reject blank templates, sparse mood images, placeholder slots, wrong Japanese text, missing output/exercise/risk areas, and any slide that is clearly thinner than the S02 sample.
- Run `python3 scripts/validate_local_skills.py`.
- If a dynamic workflow artifact exists, run `python3 skills/codex-dynamic-workflows/scripts/verify_workflow.py .workflow/<slug>`.

Report the final result with: changed files, per-session slide counts, major補修 points, acquired assets/source notes, verification commands, and any remaining human screenshot checks.

## Differentiation Gate

Before a new full-course outline is accepted, answer these questions in the course-level memo:

- What is the one-line promise of this course that would not fit the previous courses?
- Which 2-4 chapters or exercises are specific to this theme?
- Which official capabilities, limitations, risks, or recommended workflows deserve deeper coverage?
- What do public course outlines such as Udemy curricula commonly cover, and what useful corporate-training angle is missing from them?
- Which public practitioner patterns are worth abstracting into fictional exercises?
- Which reused structure is kept only for eligibility/compliance, and how is the actual content different?
- If the course title were hidden, could a reviewer still tell the theme from the chapter names, exercises, sample data, and outputs?

## Hard Image Rule

For slide images, do not use SVG, HTML/CSS, canvas, browser screenshots, ImageMagick, PIL, rsvg conversion, local rasterization, tracing, local compositing, or text/logo overlays as a substitute for GPT image 2 generation.

Allowed:

- Writing `スライド案.md`, `講師台本.md`, and `画像生成プロンプト.md`.
- Using official logos/screenshots as references when license and source notes are acceptable.
- Generating one complete bitmap image per slide with GPT image 2 / built-in image generation.
- Moving or copying the generated bitmap into `スライド画像/Sxx.png` without pixel modification.
- Inspecting the generated bitmap and regenerating the whole image when text, density, placeholders, or layout fail.

Not allowed:

- Building a slide as SVG, HTML, CSS, canvas, or a browser-rendered page and converting it to PNG.
- Repairing generated slides by covering old text or adding overlays.
- Asking GPT image 2 to imagine real logos or exact product UI without official reference assets.

## Rebuild Rules

When the user says "全部削除して画像生成からやり直して", "再生成", "GPT image 2", or "SVG/HTML生成はやめて":

1. Identify the exact course/session scope.
2. Delete only the stale generated slide images in `スライド画像/` unless the user explicitly asks to delete plans, scripts, prompts, or handouts too.
3. Keep `スライド案.md`, `講師台本.md`, and `画像生成プロンプト.md` as source artifacts unless they contain the same flawed approach.
4. Regenerate final images with GPT image 2 / built-in image generation only.
5. Inspect and report any slides not yet regenerated.

## Export Handoff

Run export only after `スライド画像/Sxx.png` exists and passes verification.

- Pamphlet PDF: ensure `全体/<講座名>_パンフレット.html` and `全体/<講座名>_パンフレット.pdf` exist. If legacy Markdown exists and is newer than HTML, regenerate HTML/PDF through `skills/course-pamphlet-html-pdf/scripts/build_pamphlets.py`.
- Google Slides: use image pages plus speaker notes from `講師台本.md`.
- Canva standard route: create the multi-page image-first presentation through MCP/API or PPTX import first, then use browser Magic Layers only for high-edit pages.
- Canva exception route: all-page Magic Layers only when the user explicitly asks for fully editable pages.
- Browser Magic Layers route: open the created Canva presentation, apply Magic Layers one page at a time, wait for processing, verify text and layout, undo/retry failed pages, and record page-level status in `非公開/Canva/`.
- Agent split: if subagents and model selection are available, use `codex-5.3spark` / `GPT-5.3 Codex Spark` browser workers for Kimi WebBridge/Canva clicking, waiting, screenshots, and repetitive checks, using Spark allowance before higher-cost models. Keep final QA, public-safety judgment, wording, and orchestration in the main agent, and reserve high-accuracy image-capable models for GPT image 2 regeneration.
- Keep Drive/Canva URLs, design IDs, and private editing notes in `非公開/` or private Drive destinations.
