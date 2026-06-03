# Course Production Unified Workflow

Use this workflow when creating, rebuilding, or coordinating a whole corporate training course. It consolidates course planning, session production, image generation, and delivery handoff into one sequence.

## Role Split

- `corporate-training-course-builder`: the single entrypoint and source of truth for course/session production.
- `imagegen`: final raster image generation only. Use GPT image 2 / built-in image generation for complete bitmap slide images.
- `gws-ai-training-slide-exporter`: downstream export only, after local slide images and scripts are complete.
- `codex-dynamic-workflows`: optional coordination layer for large, risky, or parallel work. It must not define a separate content standard.

## Entry Point Rule

For requests such as "講座作成", "講座を作成してください", "研修資料を作って", or similarly broad course-production language, start here through `corporate-training-course-builder`. Do not start from export, Canva, browser automation, subagent orchestration, or a newly created helper skill.

When a new local skill, checklist, or script is added for this repository, attach it to this sequence at the phase where it belongs:

- course planning and public/private source handling
- session script, slide plan, worksheet, handout, and exercise data production
- slide image prompt and GPT image 2 generation
- verification and public-safety review
- downstream Google Drive, Google Slides, PPTX, Canva, or browser Magic Layers delivery

If a new helper cannot be placed in one of these phases, it probably should be a reference under `corporate-training-course-builder` rather than an independent skill.

## Full-Course Sequence

1. Read `AGENTS.md`, the course folder, `全体/` files, existing session folders, and relevant private source extracts without copying private details into public files.
2. Confirm course category, learner level, delivery format, standard hours, LMS/log requirements, outputs, and public-safety constraints.
3. Select one slide template for the course or a justified template per session. Record the template ID in slide plans and image prompts.
4. Build or revise course-level files: overview, syllabus, all-session worksheet, instructor notes, exercise-data index, pamphlet, and source memo.
5. Produce each session with `session-production-workflow.md`: slide plan, instructor script, worksheet, handouts, exercise data, image prompts, and final slide images.
6. Generate all final slide images as complete raster images with GPT image 2 / built-in image generation. Save only final PNGs in each session's `スライド画像/`.
7. Verify every session: slide count, prompt count, script slide markers, data references, logo/source notes, public-safety risks, and image readability.
8. Only after local production is complete, use `gws-ai-training-slide-exporter` for Google Slides, Drive, PPTX, or Canva-ready output.

## Hard Image Rule

For slide images, do not use SVG, HTML/CSS, canvas, browser screenshots, ImageMagick, PIL, rsvg conversion, local rasterization, tracing, local compositing, or text/logo overlays as a substitute for GPT image 2 generation.

Allowed:

- Writing `スライド案.md`, `講師台本.md`, and `画像生成プロンプト.md`.
- Using official logos/screenshots as references when license and source notes are acceptable.
- Generating one complete bitmap image per slide with GPT image 2 / built-in image generation.
- Moving or copying the generated bitmap into `スライド画像/Sxx.png` without pixel modification.

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

- Google Slides: use image pages plus speaker notes from `講師台本.md`.
- Canva standard route: create the multi-page image-first presentation through MCP/API or PPTX import first, then use browser Magic Layers only for high-edit pages.
- Canva exception route: all-page Magic Layers only when the user explicitly asks for fully editable pages.
- Browser Magic Layers route: open the created Canva presentation, apply Magic Layers one page at a time, wait for processing, verify text and layout, undo/retry failed pages, and record page-level status in `非公開/Canva/`.
- Agent split: if subagents and model selection are available, use low-cost browser workers for Kimi WebBridge/Canva clicking and screenshots, keep final QA and orchestration in the main agent, and reserve high-accuracy image-capable models for GPT image 2 regeneration.
- Keep Drive/Canva URLs, design IDs, and private editing notes in `非公開/` or private Drive destinations.
