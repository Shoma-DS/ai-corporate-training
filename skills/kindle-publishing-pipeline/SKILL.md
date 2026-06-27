---
name: kindle-publishing-pipeline
description: Create, revise, package, and quality-check Kindle Direct Publishing book projects. Use when Codex is asked to make a Kindle/KDP publishing workflow, turn an idea or manuscript into a publishable book project, prepare ebook/paperback metadata, outline chapters, draft or edit manuscript files, create KDP submission checklists, validate cover/manuscript readiness, or manage Kindle publishing assets and launch materials.
---

# Kindle Publishing Pipeline

## Purpose

Build KDP-ready book projects from idea, draft, or existing manuscript. Keep the workflow practical: clarify the reader promise, create a sellable structure, produce manuscript and metadata assets, check KDP constraints, and leave the user with a clean package for upload.

Use official KDP pages as source of truth for mutable rules. Read `references/kdp-current-requirements.md` before finalizing upload-facing files, and browse official KDP help again if pricing, royalty, categories, AI disclosure, file formats, cover specifications, or review rules matter to the task.

## Project Layout

Use this structure for new books unless the user gives another path:

```text
出版/<book-slug>/
├── 00_企画/
│   ├── book_plan.md
│   ├── reader_profile.md
│   └── competing_books.md
├── 01_原稿/
│   ├── manuscript.md
│   └── revision_notes.md
├── 02_メタデータ/
│   ├── kdp_metadata.json
│   ├── description.md
│   ├── keywords.md
│   └── categories.md
├── 03_表紙/
│   ├── cover_brief.md
│   └── sources.md
├── 04_提出パッケージ/
│   ├── upload_checklist.md
│   └── validation_report.md
└── 05_販促/
    ├── launch_plan.md
    └── sales_copy.md
```

Run `scripts/init_kindle_project.py` to create this layout and starter files.

## Workflow

1. Define the book strategy.
   - Identify target reader, concrete problem, promise, scope, and non-goals.
   - Decide format: Kindle ebook only, paperback too, or later paperback.
   - For business/how-to books, force each chapter toward a usable outcome: checklist, template, decision rule, workflow, sample prompt, or case.

2. Build the outline.
   - Use a progression readers can follow: pain/problem -> principles -> practical workflow -> examples -> implementation -> mistakes/FAQ -> next action.
   - Avoid chapter titles that only name topics. Prefer outcome titles such as `第3章: ChatGPTを社内FAQ作成に使う手順`.
   - Create a table of contents early because Kindle ebooks need navigable chapter structure.

3. Draft or revise the manuscript.
   - Keep claims evidence-based. Mark unverifiable claims and current facts for source checking.
   - Do not include private company data, personal data, unpublished client materials, or copied paid content in public manuscript files.
   - If AI helped produce text, record the role of AI in `01_原稿/revision_notes.md` and prepare any KDP-required disclosure based on current KDP policy.

4. Prepare upload metadata.
   - Fill `02_メタデータ/kdp_metadata.json`: title, subtitle, author, language, contributors, description, keywords, categories, audience, rights, AI disclosure notes, and pricing assumptions.
   - Write description copy for the store page separately from the manuscript.
   - Treat categories, keywords, royalties, KDP Select, and price as current-market decisions; verify official KDP and Amazon store behavior before final advice.

5. Prepare cover direction.
   - Create a `cover_brief.md` with title, subtitle, author, genre shelf, promise, audience, visual direction, required text, and prohibited elements.
   - Do not invent third-party logos or copyrighted imagery. Use licensed, original, public-domain, or properly sourced assets.
   - For ebook covers, validate dimensions and file size using `scripts/validate_kdp_package.py`.

6. Build export files.
   - Prefer Markdown as working source. Convert to DOCX/EPUB/PDF only when the repo has an established toolchain or the user asks.
   - For reflowable Kindle ebooks, avoid layout-dependent tricks: text boxes, forced page numbers, tiny tables, image-only text, and manual tab indentation.
   - For paperback, produce a separate print manuscript and check trim, margins, bleed, headers, footers, page count, and PDF output.

7. Validate before upload.
   - Run `scripts/validate_kdp_package.py <project-dir>`.
   - Fix critical issues before telling the user the package is upload-ready.
   - Leave final manual upload steps in `04_提出パッケージ/upload_checklist.md`; do not claim KDP publication has happened unless browser/API work actually completed it.

## Scripts

- `scripts/init_kindle_project.py`: create a Kindle publishing project folder with starter files and metadata JSON.
- `scripts/validate_kdp_package.py`: inspect required files, metadata completeness, manuscript basics, cover image dimensions, and upload checklist readiness.

## References

- `references/kdp-current-requirements.md`: current KDP upload-facing constraints and official source links.
- `references/book-production-checklist.md`: practical checklist for strategy, manuscript, metadata, cover, validation, and launch assets.

## Quality Bar

Do not mark a Kindle project complete if it only contains a generic outline. A usable package should have a reader-specific promise, concrete chapter outcomes, a manuscript or drafting plan, KDP metadata, cover brief, validation report, and a manual upload checklist.
