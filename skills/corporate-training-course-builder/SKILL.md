---
name: corporate-training-course-builder
description: Use as the single entrypoint when creating or updating corporate training courses and sessions end to end, including broad requests like 講座作成, 講座を作成してください, 研修資料を作って, session scripts, slide images, handouts, data, verification, and export handoff; downstream helpers must be reached through this workflow unless the user explicitly asks only for export or workflow orchestration.
---

# Corporate Training Course Builder

## Purpose

Create complete, session-level corporate training materials that are ready for delivery: slide plan, instructor script, image prompts, generated slide images, handouts, worksheets, sample data, and source notes.

This skill is the course-production orchestrator. Use it for any corporate training course, not only Google Workspace/GAS. Apply the repository's `AGENTS.md` first when present.

## Unified Course Workflow

Use this skill as the single production entrypoint for course creation. Other local course-related skills are downstream helpers, not competing workflows.

- Production source of truth: this skill and `references/session-production-workflow.md`.
- Export helper: `skills/gws-ai-training-slide-exporter/SKILL.md` is used only after local materials and `スライド画像/Sxx.png` exist, for Google Slides, Google Drive, PPTX, and Canva-ready bundles.
- Pamphlet helper: `skills/course-pamphlet-html-pdf/SKILL.md` is used when course-level pamphlet content must be authored, migrated from legacy Markdown, or converted to client-ready PDF.
- Workflow planning helper: `skills/codex-dynamic-workflows/SKILL.md` is used only when a task is large enough to require explicit packets, approvals, or reusable orchestration notes.
- Image generation helper: the system `imagegen` skill is used for final bitmap slide images. It does not replace this course workflow.
- If a user gives a broad creation request, do not jump directly to an export, Canva, browser, or subagent helper. First run this course workflow, then invoke helpers only at the matching phase.
- When adding a new repository-local skill or workflow detail, integrate it here or in a directly linked reference file unless it is a narrow downstream helper. Every helper must state when this skill calls it and must not define a separate course-production standard.

For a full-course build or rebuild, follow `references/course-production-unified-workflow.md` before session-specific checklists.

When the user asks to rebuild an existing course by "matching the information density", "情報量を見習って", "構図や具体度を見習って", or similar wording, treat it as a **high-density slide plan rebuild**, not as a content-copy request. Use the reference course only for slide density, So What headlines, visible structures, concrete examples, screenshot/case usage, and exercise specificity. Keep the target course's theme, official constraints, learner outputs, and examples distinct. For full-course rebuilds, use `references/course-production-unified-workflow.md` and the high-density rebuild gate there before final verification.

For `講座/AX・DXワークショップ講座/`, always consult the accepted reference PDFs `AX・DXワークショップ講座_第1回 .pdf` and `AX・DXワークショップ講座_第2回.pdf` when creating or revising slide plans, scripts, image prompts, or slide images. Use them as density and structure benchmarks only: page granularity, agenda recurrence, comparison tables, case-study density, process diagrams, risk-example separation, and summary style. Do not copy the PDFs' prose into public files and do not store the source PDFs in the public repository. As a practical benchmark, Session 1 should stay around 52 slides/pages and Session 2 around 64 slides/pages unless the user explicitly changes the target duration or format.

If the user asks to "continue with a dynamic workflow", "Goalアクションに登録", "クリップボードに入れて", or resumes after a session/context limit, create a compact handoff prompt before further execution. The handoff prompt must include the unchanged objective, course path, current artifacts, packet/status table, public/private constraints, downstream helper sequence, and verification commands. Copy it to the clipboard only when the user explicitly asks for clipboard placement; otherwise save it under `.workflow/<slug>/handoff-prompt.md`.

## One-Phrase Session Requests

When the user says "4回目の台本とスライド画像まで作って", "第4回の台本とスライド作って", "何回目の台本とスライド作って", or "N回目の講師台本とスライド画像まで", treat it as an end-to-end target-session request, not only a planning request.

1. Parse the course name and session number from the message and recent context. If the message literally says "何回目" and context does not identify the session, ask one concise clarification.
2. Locate the unique target session folder by checking course folders and numbered session names such as `04-...`, `第4回...`, or `4回目...`. If a folder is missing but the course is clear, create the standard session structure.
3. Read the target folder, adjacent sessions, whole-course curriculum, template catalog, and `references/session-production-workflow.md`, then run the standard workflow through script, prompts, handouts/data, and slide images.
4. Do not stop after `スライド案.md`, `講師台本.md`, or `画像生成プロンプト.md`. Continue until `講師台本.md`, `画像生成プロンプト.md`, required handouts/data, and target-session `スライド画像/Sxx.png` are complete or a real blocker is found.

## Standard Session Folder

Use a course folder plus session folders. Prefer this structure.

Course-level:

- `全体/`
- `全体/調査/`

Put course-wide materials in `全体/`: course overview, detailed syllabus, all-session worksheet, all-session instructor notes, exercise-data index, `パンフレット.html`, `パンフレット.pdf`, course-level slide outline, level mapping, and use-case/data design notes. Put course-wide source and research notes in `全体/調査/`.

Repository-level shared assets:

- `素材/ロゴ/`

Each session folder:

- `スライド案.md`
- `講師台本.md`
- `画像生成プロンプト.md`
- `ワークシート.md`
- `スライド画像/`
- `スクリーンショット/`
- `配布資料/`
- `演習データ/`

Do not create per-session `素材/ロゴ/`, `素材/スクリーンショット/`, `素材/作業風景/`, or `調査/` folders. Official logos are shared across courses, so keep them in repository-level `素材/ロゴ/`. Research normally belongs to the course, not to one session, so keep source notes in `全体/調査/`.

## Slide Style Templates

Use the repository slide template files as the source of truth for visual style. Do not rely on memory or invent a new visual direction when making slide outlines, image prompts, or slide images.

- Template catalog: `スライド/テンプレート/カタログ.yml`
- Selection flow: `スライド/スライド生成テンプレート選択フロー.md`
- Current main template: `スライド/テンプレート/アイソメトリック法人向けクリーン.md`
- Overview note: `スライド/アイソメトリック資料画像プロンプトテンプレート.md`

Before creating or revising `画像生成プロンプト.md` or `スライド画像/Sxx.png`:

1. Read `スライド/テンプレート/カタログ.yml`.
2. Pick one best matching template for the session's course, audience, slide purpose, and tone. If more than one template fits, follow `スライド/スライド生成テンプレート選択フロー.md`.
3. Read the selected template's `source_file`.
4. Apply its style tags, palette, diagram patterns, screenshot/logo rules, and default slide mapping.
5. Record the selected template ID and diagram pattern in `画像生成プロンプト.md` for each slide.

Within one session, keep the same template ID and visual style across `スライド案.md`, `講師台本.md`, `画像生成プロンプト.md`, and all generated `スライド画像/Sxx.png` by default. Mix templates only when the user explicitly asks for it.

For the current `isometric-corporate-clean` style, keep the visual direction clean, white-background, navy/teal, card-based, corporate, isometric, and screenshot/logo-compatible. Service logos and UI screens remain real referenced assets, not prompt-invented drawings.

## Subsidy Review Submission Principle

For subsidy screening and Manabi DX-related submissions, the reviewer judges the course from the submitted **pamphlet and slides only**. Instructor comments, speaker notes, internal scripts, oral explanations, and follow-up messages are not part of the screening material. Treat this as a hard production constraint.

Submission-facing pamphlets and slides must therefore answer, on their own:

- What course this is and what business capability it develops.
- Who the course is for and what prior knowledge is assumed.
- What learners do in each session, not only what the instructor explains.
- What practical outputs learners create and take back to work.
- How the course moves from business issue identification to workflow design, implementation/prototype, review, operation, KPI, and proposal.
- How e-learning, LMS records, learning time, completion confirmation, assignments, and learner progress management are handled.
- What information management, AI output review, privacy, copyright, hallucination, and human confirmation rules are taught.

Do not create slides that look good only with narration. If a slide cannot be understood without `講師台本.md`, it is not ready for submission. Add enough slide text, labels, examples, process steps, output names, checkpoints, and source notes to make the learning content clear while keeping the layout structured.

Use structured slide writing:

- Put the So What or conclusion in the headline. Avoid title-only headings such as `概要`, `AI活用について`, or `レベル3相当の評価観点`.
- Convert bullet lists into visible structures: sequence, comparison, classification, issue -> action -> effect, cause -> result, output map, checklist, curriculum table, or conclusion + reasons.
- Keep one main message per slide, but do not make the slide sparse. A submission slide should usually show a headline, 3-6 meaningful content blocks, and the learner output or review point where relevant.
- If the script contains a core explanation, promote a short version into the slide or pamphlet. Do not leave core screening evidence only in narration.
- Use real screenshots, official logos, tables, or sample outputs when they explain the course better than abstract diagrams, while following public-safety and official-asset rules.

Public-facing wording rules from stakeholder feedback:

- For e-learning reskilling courses, assume **e-learning only** unless the user explicitly says otherwise. Do not write `オンラインワークショップ`, `ハイブリッド`, live discussion, or classroom-style delivery as a default.
- Use this LMS wording or a close equivalent when describing the delivery format: `eラーニング。本研修は、LMS(学習管理システム:Learning Management System)を利用し、各自の受講状況や受講時間を全て記録することで、受講者の学習状況の把握を行い、適切なスキルアップをサポートいたします。`
- Do not make the public pamphlet/slides look like they were created only for Manabi DX screening. Avoid labels such as `レベル3相当の評価観点` in public-facing headings. Prefer learner-centered labels such as `本講座受講後の到達点`.
- If internal level mapping is needed, keep it in source notes, level mapping files, or internal planning sections, not as the main public-facing label.
- Curriculum time tables must total the stated session length. For the standard 6-session reskilling format, each session should total 120 minutes and the whole course should total about 12 hours.

## Course-Specific Differentiation Principle

Do not let new courses become clones of prior courses with only the tool name changed. Reusing the screening-ready structure is allowed, but the content, chapter logic, examples, exercises, and outputs must clearly belong to the requested theme.

Before creating a new full course or rebuilding a course, run a differentiation pass:

- Identify the theme-specific question: "What can only this course reasonably teach, compared with the existing courses in this repo?"
- Compare against nearby existing courses and list what must not be blindly copied: chapter titles, session flow, repeated exercises, generic DX wording, repeated CSV bundles, repeated risk slides, and template-like learner outputs.
- Research official/vendor/public primary information for the target theme. If official docs, product updates, brand guides, public case studies, or public-sector sources reveal important capabilities, restrictions, workflows, or risks, build at least one chapter or exercise around them.
- Research public learning-market and practitioner patterns when useful, including Udemy course outlines, public syllabi, YouTube/blog walkthroughs, Qiita, Zenn, note, product communities, and company tech blogs. Extract themes and gaps, not copyrighted prose, slides, screenshots, paid content, or private details.
- Add a course-specific "signature chapter" or "signature exercise" that would not naturally appear in another course. It should be useful for corporate training, not novelty for its own sake.
- Make outputs theme-specific. Avoid every course ending with the same generic "DX提案書" unless the proposal contents, required evidence, workflow, data model, and evaluation criteria are different for that theme.
- If a course uses the same six-part progression for eligibility reasons, vary the internal chapter focus: theme-specific data sources, constraints, governance risks, implementation choices, evaluation metrics, operating model, and business scenarios.
- Record the differentiation decisions in course-level `全体/調査/` or a course-level design memo so later sessions do not drift back into a generic template.

Good differentiation examples:

- NotebookLM courses should deeply handle source selection, source reliability, citations, information boundaries, source refresh, FAQ/knowledge-base maintenance, and grounded answer review.
- Google Workspace/GAS courses should deeply handle Forms/Sheets data design, Apps Script triggers, quotas/limits, logs, permissions, error recovery, and Google Workspace feature availability.
- Dify/RAG courses should deeply handle data chunking, retrieval quality, permissions, evaluation datasets, hallucination checks, prompt/app operations, and update workflows.
- Copilot/Microsoft 365 courses should deeply handle tenant settings, M365 document workflows, meeting/email/document review, sensitivity labels, permission boundaries, and human approval.

## Workflow

1. Read the course folder, target session folder, previous session outputs, whole-course curriculum, `AGENTS.md`, existing `スライド案.md`, and `ワークシート.md`.
   - For full-course creation, rebuild, or cross-session consistency work, read `references/course-production-unified-workflow.md` first and use it as the master checklist.
2. For full-course work, run the **Course-Specific Differentiation Principle** before drafting the syllabus. Do not start from a prior course outline until you have identified the target theme's unique chapters, signature exercises, official-source constraints, and public-learning-market patterns.
3. If current facts, services, laws, tool capabilities, pricing-adjacent details, logos, or case studies matter, browse official or primary sources and save a concise source memo in course-level `全体/調査/`.
4. If the user asks to check online concrete examples, practitioner examples, use cases, Udemy-like public course positioning, or ways to avoid generic course design, read `references/public-case-research-workflow.md`. Use official sources for current capabilities and general public examples for practical patterns; do not copy private details, paid content, or reproduce a specific company's workflow.
5. If the user says exercise data looks duplicated, asks for "その回に必要なデータだけ", or asks to fully fix CSV/sample data, read `references/session-specific-exercise-data-workflow.md`. Split or rebuild `演習データ/` by the learner output and demo actually used in each session, then update stale file references.
6. Choose the slide style template from `スライド/テンプレート/カタログ.yml` and read the selected template before writing slide plans or image prompts.
7. Expand the session to fit the intended duration. For a 120-minute session, use enough slides for clear pacing, usually around 35-45 slides when demos and exercises are included.
8. Create or revise `スライド案.md` with slide numbers, titles, purpose, selected template ID, visual/material type, diagram pattern, demo/screenshot needs, and exercise timing.
   - Follow the **Subsidy Review Submission Principle**. Slides must be understandable without instructor comments and must show enough content for a reviewer to understand what the course teaches and what learners do.
   - Each submission-facing slide should have a conclusion-style headline, enough body text to identify the learning content, and a visible structure such as process, comparison, checklist, table, issue-to-solution flow, or output map. Avoid sparse mood slides and bullet-only lists.
   - For high-density rebuilds, every slide should normally include `**ヘッドライン:**`, 3-6 meaningful content blocks, a selected template ID, a diagram/material pattern, and a screenshot/source instruction when useful. Add industry-specific examples, Before/After, numeric sense, output names, review points, and exercise steps. Do not copy a reference course's topics, chapter order, or examples.
9. Create `講師台本.md` as a word-for-word script. Include when to change slides, when to show work screens, what the instructor says, exercise instructions, time marks, and fallback explanations. Follow the **Instructor Script Rules** section below for block types, screen-share format, and SME metaphors.
10. Create all required `配布資料/`, `演習データ/`, CSV files, sample text, and worksheets inside the target session folder.
11. Create `画像生成プロンプト.md` for every slide. Include selected template ID, exact in-image text, visual pattern, official-logo inputs, screenshot inputs, screen-share transition slides, and negative prompt.
12. Use official logos/screenshots as reference assets when needed. Save official logos in repository-level `素材/ロゴ/` with source notes. Save screen captures for a session in that session's `スクリーンショット/`. Do not ask image generation to invent brand marks from memory.
13. Use the `imagegen` skill and its rules for raster slide images. Save final images in the target session's `スライド画像/Sxx.png`.
    - For generated training slide images, use GPT image 2 / built-in image generation as a complete bitmap image. Do not create SVG, HTML, CSS, canvas, browser screenshots, or local conversion outputs as slide-image intermediates.
14. For course-level pamphlets, create or update `全体/パンフレット.html` as the source of truth and generate `全体/パンフレット.pdf` before delivery. Use `skills/course-pamphlet-html-pdf/SKILL.md` for legacy Markdown migration and HTML-to-PDF conversion. Do not create new pamphlets as Markdown-first deliverables.
15. Verify text accuracy, slide count, per-session time totals, theme-specific differentiation, asset paths, selected template usage, pamphlet HTML/PDF existence, public-safety constraints, and that scripts/slides/handouts agree.
    - For submission-facing materials, review the pamphlet and slides without reading `講師台本.md`. If the course content is not understandable from those two artifacts alone, revise the slides/pamphlet before delivery.

For a detailed checklist, read `references/session-production-workflow.md`.

## Parallel Subagents

If subagents are available and the user asks for parallelization, split the work aggressively but keep file ownership exclusive. The main agent coordinates context, resolves conflicts, and performs final integration.

- For browser automation, use subagents even when the user did not explicitly ask for parallelization if the environment supports it. Assign browser clicking, waiting, screenshots, page navigation, and repetitive visual checks to `codex-5.3spark` / `GPT-5.3 Codex Spark` equivalent first so the Spark usage allowance is not wasted.
- Keep the main agent or higher-accuracy model responsible for planning, acceptance decisions, public-safety judgment, final wording, course design, and file integration. Do not let the browser subagent rewrite course content or make final quality decisions.
- Before assigning work, the main agent chooses one session template ID and shares it with every subagent. All subagents must use that template/style unless the user explicitly approved mixing templates.
- The main agent keeps progress visible to the user, tracks which slide numbers are assigned, reconciles outputs, and verifies that filenames, slide titles, prompts, handouts/data, and generated images agree.
- Slide plan owner: edits only `スライド案.md`.
- Instructor script owner: edits only `講師台本.md`.
- Prompt/image owner: edits only `画像生成プロンプト.md` and `スライド画像/Sxx.png`, following the selected template and `imagegen` rules.
- If slide image generation is parallelized, split it into disjoint `Sxx` batches such as `S01-S10`, `S11-S20`, and `S21-S30`. Each image worker uses the same fixed template ID for the session and writes only its assigned `スライド画像/Sxx.png` files.
- Handout/data owner: edits only `ワークシート.md`, `配布資料/`, and `演習データ/`.
- Source/official asset owner: checks official sources, logos, screenshots, and writes only course-level `全体/調査/` notes or repository-level `素材/ロゴ/` assets.
- Verification owner: read-only review of slide counts, wording, paths, source notes, public-safety risks, and consistency; fixes are applied by the owning agent or main agent.

For a full-course high-density rebuild, a good packet split is by session pairs plus cross-cutting assets and final verification:

- Packet A: sessions 1-2 slide plans.
- Packet B: sessions 3-4 slide plans.
- Packet C: sessions 5-6 slide plans.
- Packet D: official logos, official/product screenshots, public examples, source notes, and screenshot acquisition memos.
- Packet E: integration review for slide count, headline count, time totals, theme-specificity, duplicated examples, stale paths, public-safety patterns, and workflow artifacts.

Each packet edits only its owned session files or source notes. The main agent reconciles style, progression, terminology, and public-safety decisions before completion.

Never let multiple agents edit the same file. If ownership would overlap, have subagents return drafts, findings, or patch suggestions instead of writing directly.
For image batches, do not use SVG, HTML/CSS, canvas, browser screenshots, local conversion, or overlays. Final slide images must be generated as complete raster images with GPT image 2 / built-in image generation only.

## Slide Image Generation Rules

When a user says a slide image is wrong and asks to "regenerate", "作り直して", "再生成", use "GPT image 2", or create "1枚まるごと" as an image, treat this as a full-image generation request unless they explicitly ask for a deterministic layout edit.

- Do not repair the existing PNG by overlaying text, hiding elements, or rebuilding it as HTML/SVG and rasterizing it.
- Use the current slide only as a layout/style reference. Generate one complete new raster slide with the `imagegen` skill.
- Generate final visuals with GPT image 2 / built-in `image_gen` as bitmap images.
- Do not create SVG, HTML, CSS, canvas, PDF, or code-native graphics as an intermediate for the final image.
- Do not use ImageMagick, `convert`, `magick`, `rsvg-convert`, PIL/Pillow, Python drawing libraries, browser screenshots, PDF/PPTX exports, local rasterization, tracing, or compositing to make the final slide image.
- Never save locally drawn placeholder images into `スライド画像/Sxx.png`. If GPT image 2 / built-in `image_gen` has not generated the image, mark the slide image as missing or pending instead of pretending it is complete.
- Course-generation scripts may write slide plans, scripts, image prompts, handouts, exercise data, and PPTX decks assembled from already generated images. They must not draw, rasterize, screenshot, convert, or composite final `スライド画像/Sxx.png` files.
- Copying or moving a generated PNG/WebP into the project is allowed. Converting or redrawing it locally is not.
- If exact text is required, keep text short and ask GPT image 2 to render it directly. Do not overlay text locally.
- Before generating, inspect repository-level `素材/ロゴ/` and load the needed official logo files as image references. Do not leave logo placeholders when logo assets exist.
- Use only official logo files already present in the repo when the user asks for real service logos. Do not ask GPT image 2 to invent or redraw real logos from memory.
- Explicitly prohibit placeholder artifacts in the prompt: dashed boxes, empty logo slots, `素材配置枠`, `公式ロゴ`, watermarks, and fake UI/screenshots.
- Preserve exact in-slide wording from the user's latest correction. Search for and remove stale wording such as old product pairings or prior draft labels before saving.
- If the built-in image tool cannot save directly to the requested project path, generate first, then copy or move the generated bitmap file without modifying its pixels.
- After generation, inspect the image before replacing `スライド画像/Sxx.png`. Check product names, Japanese text, logo placement, card spacing, and whether the output still contains forbidden placeholder text.
- If you start considering SVG, HTML/CSS, canvas, screenshots, or local conversion for a GPT image 2 request, stop and switch back to bitmap generation.

## Canva Delivery Policy

When the finished slide images will be turned into a Canva presentation, use an image-first delivery flow by default.

- Create complete raster slide images in `スライド画像/Sxx.png` first.
- Build or export one multi-page presentation per session from those images.
- Prefer Canva MCP/API or PPTX import for the initial multi-page presentation, so `S01.png` through the final slide are placed in order before any browser-based editing begins.
- Do not plan to Magic Layers-convert every slide through Canva MCP unless the user explicitly asks for all pages to be editable.
- Mark only high-edit pages for manual Magic Layers in Canva: cover, section dividers, date/company/instructor placeholders, curriculum tables, audience/output lists, and customer-specific proposal pages.
- Leave fixed diagrams, screenshots, screen-share transition slides, exercise instructions, summaries, and completed visual explanations as image pages.
- Keep Canva URLs, design IDs, and manual editing notes in `非公開/Canva/` or the private Google Drive sync destination, not in public course files.

If a user asks for Canva export without specifying Magic Layers, assume they want a visually faithful image-based Canva deck, not fully decomposed editable layers.

If the user explicitly asks to run Magic Layers in the Canva browser:

- Use `skills/gws-ai-training-slide-exporter/SKILL.md` as the execution guide after local slide images are complete.
- Apply Magic Layers page by page inside the already-created multi-page Canva presentation, not by creating detached one-page designs unless the user asks for the legacy all-page conversion route.
- After each page, wait for Canva processing to finish, then inspect the page for Japanese mojibake, changed wording, missing text, distorted tables, overlapped elements, incorrect logos, and layout collapse.
- If a page fails, undo or return to the pre-Magic-Layers state, retry once or twice, then either keep the image page or mark it for manual repair in `非公開/Canva/`.
- Treat browser automation as high-cost. When subagents and model selection are available, delegate browser navigation and repetitive Canva checks to a `codex-5.3spark` / `GPT-5.3 Codex Spark` browser subagent first, using available Spark allowance before higher-cost models. Keep orchestration and final QA in the main agent, and reserve image generation for the image-capable high-accuracy model.

## Pamphlet HTML/PDF Policy

Course pamphlets are client-facing submission artifacts, so they must be available as print-ready HTML and PDF.

- New pamphlets are authored directly as `全体/パンフレット.html`.
- Always generate or refresh `全体/パンフレット.pdf` from the HTML before delivery.
- For e-learning reskilling courses, describe the delivery format as e-learning only unless the user explicitly says otherwise. Use LMS wording that explains `LMS(学習管理システム:Learning Management System)` and that each learner's attendance status and learning time are recorded.
- Do not label learner outcomes in public-facing pamphlets or slides as `レベル3相当の評価観点`. Use learner-centered wording such as `本講座受講後の到達点` so the material does not look like it was made only for Manabi DX screening.
- Check that every curriculum table row group totals the stated session duration, usually 120 minutes per session. If a table totals 140 minutes or another mismatched value, adjust before PDF generation.
- After generating PDF, verify the PDF text or preview itself, not only the HTML. Use `pdftotext` or a visual preview to confirm corrected wording is actually reflected in `パンフレット.pdf`.
- Search the final HTML/PDF text for stale public-facing delivery words such as `オンラインワークショップ`, `ハイブリッド`, and stale screening labels such as `レベル3相当の評価観点`.
- Existing `パンフレット原稿.md` or `パンフレット.md` files are legacy migration sources. If their content changes, run the pamphlet helper to regenerate HTML and PDF.
- Standard build command:

```bash
python3 skills/course-pamphlet-html-pdf/scripts/build_pamphlets.py --course-dir '講座/COURSE'
```
- Do not put prices, application contacts, customer-specific notes, private URLs, Canva URLs, Drive URLs, credentials, or unpublished internal details into public pamphlet HTML/PDF.

## Quality Rules

- Start from business problems, not tool features.
- For Manabi DX level 3 or advanced digital talent materials, avoid framing the course as a named-tool usage class. Lead with business transformation, requirements definition, operating design, continuous operation, improvement proposals, DX promotion, and practical outputs. Tools such as Google Workspace, GAS, Gemini/Gem, Dify, RAG, NotebookLM, or Copilot should appear as means inside the business process, not as the course's main value.
- For Manabi DX screening materials, assume reviewers see only slides and pamphlets, not instructor comments. Slides must carry the main explanation themselves: what the learner does, why it matters, what steps are followed, what output is created, and how it connects to the course goal.
- Convert weak bullet lists into structured slides. Choose a structure such as sequence, comparison, classification, issue -> action -> effect, cause -> result, or conclusion + three reasons. Put the So What in the headline and keep facts/evidence in the body.
- Do not under-explain slides for submission. A slide can be visually clean and still contain enough text to show the learning content. Prefer structured, readable density over decorative minimalism when the slide is used for screening.
- Do not overfit to previous course structures. Reuse only the compliance skeleton; redesign the chapter focus, demos, examples, exercises, and outputs around the current theme's official capabilities, constraints, public use patterns, and corporate training value.
- Include at least one clearly theme-specific chapter, case, or exercise per course. If a reviewer could swap the course title with another course and the slide still mostly works, the course is too generic.
- Every session must end in a practical output learners can use or adapt.
- Use demos and screenshots when a service or UI is clearer than abstract diagrams.
- When the instructor will switch to a live work screen or recording, do not make a slide that tries to contain the work scene. Make a transition slide that says the screen will be shown now, then describe the demo in `講師台本.md`.
- For AI/data safety, distinguish normal business use from external AI/public materials. Business spreadsheets/forms may contain real operational data; demos, public materials, and AI inputs should use sample, anonymized, or minimum necessary data.
- Official logos must come from official sites, brand guidelines, or press kits where possible, with source notes.
- Public files must not contain private company materials, real customer/employee data, prices, contact details, credentials, API keys, or unreleased internal content.

## Level 3 Framing Checks

When creating brochures, syllabi, slide outlines, or application-facing summaries for Manabi DX level 3:

- First-viewport or opening copy should say what business capability the learner gains, such as independently organizing issues, designing As-Is/To-Be, defining requirements, separating automation scope, designing operation, setting KPIs, and proposing improvements.
- Session titles should not be tool-first if that makes the course look like a basic operations class. Prefer titles like "業務課題整理とAs-Is/To-Be設計", "AI/GAS活用の要件定義・運用設計", and "DX推進に向けたKPI設計・導入提案".
- If tool names are necessary, pair them with purpose and workflow: input, processing, output, human review, logs, exception handling, recovery, and continuous improvement.
- Explicitly include outputs that evidence level 3 work: requirements memo, operating design, risk checklist, prototype, KPI/effect estimate, rollout roadmap, and implementation proposal.

## Delivery Format

This course is delivered as **pre-recorded video for async reskilling** (録画動画によるリスキリング講座). There is no live instructor–learner interaction. All script blocks must be written with this in mind.

### Video-format rules (mandatory)

- **ワーク時間の指示**: 「今から○分取ります」は使わない。代わりに「ここで動画を一時停止して、○分ほど取り組んでください。取り組めたら再生してください。」を使う。
- **声がけ・タイマー管理**: 「1分経過で声がけする」「残り1分でアナウンス」のような 講師メモは書かない。
- **ライブ共有・発表・討議**: `共有指示:` ブロック、「チャットでも構いません」、「口頭で共有してください」、「発表してください（ライブ）」、相互フィードバックは使わない。
- **「受講者に〜させる」**: 実演ブロックの手順に「受講者に自分のワークシートを見直させる」のような指示は書かない。「ここで動画を一時停止して〜してください」という読み上げ文に変える。
- **発表・相互レビュー**: グループ発表や相互フィードバックは行わない。代わりに「自己レビュー」と「講師の記入例との比較」に置き換える。
- **フォールバック**: 環境差がある場合の代替手順は引き続き記載する（録画中に説明すべき内容のため）。

## Instructor Script Rules

### Block types (use only these five — do not add others)

```
スライド切替:
S番号「スライドタイトル」

読み上げ:
「〜〜〜。」

画面共有 ── 実演N「タイトル」
⏱ 約○分
【手順1 – 約○秒】〜
【手順2 – 約○秒】〜
【見せるポイント】〜

ワーク指示:
「〜〜〜。」

講師メモ:
（読み上げない。進行管理・注意喚起のみ）
```

### Screen-share format (required for every 画面共有 block)

"何を見せるか" alone is not enough. Always write all of the following.

```markdown
**画面共有 ── 実演N「タイトル」**
⏱ 約○分

【手順1 – 約○秒/分】
何の画面を開くか。どのデータを使うか。どんな操作をするか。何を声に出して説明するか。

【手順2 – 約○秒/分】
（以下同様）

【手順N – 約○秒/分】
操作の最後に「このあと、〜につながります」という予告を入れると全体像が伝わりやすい。

【見せるポイント】
この画面共有で受講者に何を気づかせたいか。1〜2文で書く。
```

Time guides:

| Demo type | Typical duration |
| --- | --- |
| Before/After comparison | 1–2 min |
| End-to-end tool walkthrough | 3–5 min |
| Switching screens in sequence | 1–2 min |
| Showing instructor's filled-in example | 2–4 min |

### Polish priorities (for brush-up requests)

1. **Screen-share detailing** (highest priority): expand "what to show" into "⏱ time · step-by-step · talking points"
2. **Metaphor addition**: add 1–2 SME-appropriate metaphors to abstract explanations
3. **Industry-specific examples**: replace generic examples ("問い合わせ管理") with sector-specific ones
4. **Natural phrasing**: rewrite read-aloud text so the instructor can say it comfortably in one breath

### SME Metaphor Bank

Use at most 1–2 metaphors per explanation. Do not overuse.

| Tool / concept | Metaphor |
| --- | --- |
| Googleフォーム（入力の入口） | ファミレスのタッチパネル注文機。客が自分で入力するから転記ミスがない。 |
| Googleスプレッドシート（台帳） | 全員がリアルタイムで見られる掲示板兼ホワイトボード。Excelは誰かのパソコンの中に閉じ込められていた。 |
| GAS（自動化） | 決まった仕事を自動でこなす事務担当ロボット。給料不要、土日も動く。ただし例外判断はしない。 |
| Gemini/Gem（AI補助） | 文章の仕分けや下書きが得意な補助スタッフ。正しいかどうかは人が確認する。最終判断は常に人。 |
| データ整備の重要性 | 食材がバラバラな冷蔵庫で料理ロボットを動かしても毎回エラーが出る。材料の規格を揃えることが先。 |
| 属人化リスク | Aさんだけが知っている作業。Aさんが休んだら月次処理が止まる。 |
| DXの入口 | 工場でいえば、新しい機械を入れる前に材料の置き場所を決めて手順書を作ること。 |
| Google Workspace全体 | 受付窓口（Forms）・台帳（Sheets）・郵便（Gmail）・書類棚（Drive）・事務ロボット（GAS）・補助スタッフ（Gemini）のセット。 |
| As-Is/To-Be | 間取り変更の前に、今の部屋でどう動いているかを確認する作業。 |

### Industry-Specific Examples

Replace generic examples with sector-specific ones when the audience is known.

| Industry | Common manual-work example |
| --- | --- |
| サービス業（美容・ホテル・飲食） | 電話予約をメモ→Excelに転記。キャンセル・変更のたびに手直し。 |
| 不動産業 | メール問い合わせをコピーして管理表に貼る。担当者の割当を上司に口頭確認。 |
| 士業（税理士・行政書士・社労士） | 申告・申請依頼をメールで受け、各担当者のExcelファイルで管理。最新がどれかわからない。 |
| 製造業・卸売り | FAX/メールで注文が来て手書き台帳に転記。月末に集計してExcelにまとめる。 |
| 建設業 | 現場日報を紙で提出→事務がExcelに転記。書き方が人によってバラバラ。 |
| 社内横断（どの業種でも） | 月末に未対応を目で探す。期限が近い人を探して一件ずつメールを書く。先月のファイルをコピーして数字だけ書き換える。 |

## Completion Checklist

Before finishing, confirm:

- The target session has the standard folder structure.
- `スライド案.md`, `講師台本.md`, `画像生成プロンプト.md`, `ワークシート.md`, and needed handouts/data exist.
- Slide numbers and titles match across slide plan, script, prompts, and images.
- `画像生成プロンプト.md` records the selected slide template ID and uses a diagram pattern from `スライド/テンプレート/カタログ.yml` or the selected `source_file`.
- One session uses one template ID and one visual style across prompts and generated images, unless the user explicitly requested mixed templates.
- `スライド画像/` contains all required images, and those images were generated by GPT image 2 / built-in `image_gen` or are approved official screenshots/assets. Locally rendered placeholders do not satisfy this check.
- Asset references point to repository-level `素材/ロゴ/`, course-level `全体/調査/`, or session-local `スクリーンショット/`, `演習データ/`, and `配布資料/`.
- Source memos exist for current facts and official assets.
- Public-safety checks pass.
- すべての画面共有ブロックに `⏱ 約○分`・`【手順1〜N】`・`【見せるポイント】` が書かれているか
- 各ブロックのメタファーは中小企業の実態に合っているか（IT前提のメタファーを使っていないか）
- 読み上げ文は講師が一息で自然に読めるか（1文が長すぎないか）
- ワーク指示に「今から○分取ります」が使われていないか（動画では「ここで動画を一時停止して○分ほど取り組んでください」を使う）
- 「チャット」「挙手」「口頭共有」「声がけタイミング（残り1分など）」など、ライブ配信前提の表現が含まれていないか
- `共有指示:` ブロックが使われていないか（動画形式では自己レビューに置き換える）
- 発表・相互フィードバックのブロックがないか（動画では自己レビューと講師記入例との比較に置き換える）
- 実演ブロックの手順に「受講者に〜させる」が含まれていないか（読み上げ文として「動画を止めて〜してください」に変える）
- スライド切替タイムライン表が末尾に整理されているか
- 作業風景タイムライン表（番号・タイトル・⏱ 時間・操作概要）が末尾にあるか
- 有料プラン・管理者設定が必要な機能を「必須演習」にしていないか
