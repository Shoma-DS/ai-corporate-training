# AIエージェント実装連携設計アカデミー完成

## Goal
`講座/AIエージェント実装・連携設計アカデミー` を、録画eラーニング用の法人研修コースとして提出・制作継続できる状態へ完成させる。

Original objective: 講座/AIエージェント実装・連携設計アカデミー の講座を完成させてください。

## Success Criteria
- Course-level files exist under `全体/`: overview, detailed syllabus, all-session worksheet, instructor notes, exercise-data index, use-case/data design, level mapping, pamphlet HTML, pamphlet PDF, and source memo.
- Six session folders exist and each has `スライド案.md`, `講師台本.md`, `画像生成プロンプト.md`, `ワークシート.md`, `配布資料/`, `演習データ/`, `スクリーンショット/`, and `スライド画像/`.
- Each session is 40 slides for a 120-minute session, and slide plan details expose `### Sxx` and `**ヘッドライン:**` for all slides.
- Slide numbers and titles match across slide plan, instructor script, image prompts, and generated images.
- Public-facing course name is consistently `AIエージェント実装・連携設計アカデミー`; legacy names do not appear as visible course titles.
- Delivery language is e-learning/LMS based, not live workshop based.
- Public files contain only dummy or abstracted data, no private Drive/Canva URLs, credentials, customer records, prices, contacts, or real personal data.
- Final slide images are complete GPT image 2 / built-in image generation raster images, not local renderings or overlays. Missing images are explicitly tracked until generated.
- `python3 scripts/validate_local_skills.py` and `python3 skills/codex-dynamic-workflows/scripts/verify_workflow.py .workflow/ai` pass before final completion.

## Current Context
- Repository: `/Users/deguchishouma/Desktop/AI法人研修`
- Course path: `講座/AIエージェント実装・連携設計アカデミー`
- Required entrypoint: `skills/corporate-training-course-builder/SKILL.md`
- Stakeholder context: `クライアント指示コンテキスト.md`
- Template: `isometric-corporate-clean`
- Current audit: all six sessions have 40 slide rows and 40 image prompt sections. Session 1 has `S01`-`S40.png`; sessions 2-6 have no slide images yet.
- Current audit: session 1 and session 2 instructor scripts do not contain a `スライド切替` marker for every slide; sessions 3-6 mostly do.
- Current audit: existing slide plans are table-first and need generated `### Sxx` detail sections for mechanical high-density verification.

## Constraints
- Public repository. Do not commit or expose private source files, Drive/Canva URLs, IDs, customer data, employee data, prices, contacts, credentials, or API keys.
- Use `isometric-corporate-clean` only.
- Do not generate final `スライド画像/Sxx.png` through SVG, HTML/CSS, canvas, browser screenshots, PIL, ImageMagick, local rasterization, or local text/logo overlays.
- Course images must be generated as complete raster images with GPT image 2 / built-in `image_gen`, or copied from already generated bitmap files without modifying pixels.
- Screen-share and exercise wording must assume pre-recorded async video. Use pause-and-resume instructions, not live chat, discussion, timers, or verbal sharing.
- Preserve unrelated dirty worktree changes under `.agent/` and `prompt-timeline/`.

## Risks
- The full course requires 200 remaining slide images after session 1. This is large and may need continued Goal-mode work.
- Existing generated-image cache may contain usable images, but only images with trustworthy provenance and matching content can be copied into session folders.
- Existing image prompts are dense but partly boilerplate; final visual acceptance still requires image inspection.
- Course-level source facts about Codex/MCP/tools can become stale, so public materials must include official-info recheck cautions.

## Approval Required
- Ask before deleting existing generated images, replacing Drive/Slides/Canva assets, pushing to remote, or running destructive Git operations.
- No approval is required for local read-only audits, local Markdown edits in the course folder, pamphlet PDF regeneration, or workflow notes.

## Work Packets
- P1: Course-level audit and public-safety scan.
- P2: Slide-plan high-density detail sync for sessions 1-6.
- P3: Instructor-script continuity fixes for sessions 1-2.
- P4: Pamphlet HTML/PDF refresh and PDF text verification.
- P5: Slide-image generation tracking and first missing-image batch.
- P6: Integrated verification and final report.

## Integration Policy
- Edit only course files and `.workflow/ai/` for this objective.
- Do not touch unrelated dirty files from `.agent/` or `prompt-timeline/`.
- Use current files as authoritative evidence; previous handoff notes are hints only.
- Keep missing slide images explicitly marked as incomplete rather than creating placeholders.

## Verification
- Count table slides, `### Sxx`, headlines, prompt sections, script markers, and images per session.
- Confirm session time tables total 120 minutes.
- Parse all course CSV files with Python's `csv` module.
- Search for stale course names and live-workshop wording.
- Search for unsafe patterns: private URLs, credentials/API keys, real-looking emails/phones, prices, contacts.
- Verify pamphlet PDF text after regeneration.
- Run local skill validator and workflow verifier.

## Reusable Artifacts
- `.workflow/ai/final-report.md` will record current completion status, missing images, verification evidence, and next actions.
