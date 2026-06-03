---
name: course-pamphlet-html-pdf
description: Use as a downstream helper for AI法人研修 pamphlets after course content exists: create or refresh print-ready `パンフレット.html` from legacy `パンフレット原稿.md` or `パンフレット.md`, convert pamphlet HTML to `パンフレット.pdf`, and keep future pamphlet production HTML-first rather than Markdown-first.
---

# Course Pamphlet HTML PDF

## Purpose

Build client-submission pamphlets as print-ready HTML and PDF files for this repository.

This is a downstream helper. For course creation, start from `skills/corporate-training-course-builder/SKILL.md`; use this skill only when the pamphlet phase is reached or when the user explicitly asks for pamphlet HTML/PDF conversion.

## Source Policy

- New pamphlets are authored as `講座/<講座名>/全体/パンフレット.html`.
- The deliverable PDF is `講座/<講座名>/全体/パンフレット.pdf`.
- Existing `パンフレット原稿.md` or `パンフレット.md` files are legacy sources. If one exists and is newer than `パンフレット.html`, refresh the HTML from Markdown before PDF conversion.
- Do not write private company materials, actual prices, contact details, Canva URLs, Drive URLs, credentials, or customer-specific notes into public HTML/PDF outputs.

## Commands

Build every course pamphlet found under `講座/*/全体/`:

```bash
python3 skills/course-pamphlet-html-pdf/scripts/build_pamphlets.py
```

Build one course:

```bash
python3 skills/course-pamphlet-html-pdf/scripts/build_pamphlets.py \
  --course-dir '講座/COURSE'
```

Force migration from legacy Markdown to HTML and regenerate PDF:

```bash
python3 skills/course-pamphlet-html-pdf/scripts/build_pamphlets.py \
  --course-dir '講座/COURSE' \
  --force-md \
  --force-pdf
```

Convert an already-authored HTML pamphlet to PDF:

```bash
python3 skills/course-pamphlet-html-pdf/scripts/html_to_pdf.py \
  '講座/COURSE/全体/パンフレット.html'
```

## Verification

After generation:

1. Confirm `パンフレット.html` and `パンフレット.pdf` exist and the PDF is non-empty.
2. Run `git diff --check`.
3. Run `python3 scripts/validate_local_skills.py` if skill files changed.
4. Before commit or push, confirm no `非公開/`, source PDFs, `.DS_Store`, credentials, real contact details, or private URLs are staged.

## Notes

The bundled `html_to_pdf.py` uses a local Chromium-family browser and Chrome DevTools `Page.printToPDF` with print backgrounds and CSS page size enabled. If no browser is found, pass `--browser` with the executable path.
