---
name: course-pamphlet-html-pdf
description: Use as a downstream helper for AI法人研修 pamphlets after course content exists: create or refresh print-ready `<講座名>_パンフレット.html` from legacy Markdown pamphlet sources, convert pamphlet HTML to `<講座名>_パンフレット.pdf`, and keep future pamphlet production HTML-first rather than Markdown-first.
---

# Course Pamphlet HTML PDF

## Purpose

Build client-submission pamphlets as print-ready HTML and PDF files for this repository.

This is a downstream helper. For course creation, start from `skills/corporate-training-course-builder/SKILL.md`; use this skill only when the pamphlet phase is reached or when the user explicitly asks for pamphlet HTML/PDF conversion.

## Source Policy

- New pamphlets are authored as `講座/<講座名>/全体/<講座名>_パンフレット.html` so the file name identifies the course on its own.
- The deliverable PDF is `講座/<講座名>/全体/<講座名>_パンフレット.pdf`.
- Legacy `パンフレット.html` / `パンフレット.pdf` names are read as fallback only; when touching a course that still uses them, rename to the `<講座名>_パンフレット.*` form with `git mv`.
- Existing `パンフレット原稿.md` or `パンフレット.md` files are legacy sources. If one exists and is newer than the pamphlet HTML, refresh the HTML from Markdown before PDF conversion.
- For subsidy screening, the pamphlet PDF is one of the core pass/fail artifacts together with the slides. It must stand alone without instructor comments, internal notes, or verbal explanation.
- For e-learning reskilling courses, public-facing delivery text should state e-learning only unless the user explicitly says otherwise. Do not leave stale `オンラインワークショップ` or `ハイブリッド` wording in the PDF.
- Use LMS wording that explains `LMS(学習管理システム:Learning Management System)` and that each learner's attendance status and learning time are recorded. The stakeholder-approved wording is: `eラーニング。本研修は、LMS(学習管理システム:Learning Management System)を利用し、各自の受講状況や受講時間を全て記録することで、受講者の学習状況の把握を行い、適切なスキルアップをサポートいたします。`
- Public-facing learner outcome headings should be learner-centered, such as `本講座受講後の到達点`, not screening-centered labels such as `レベル3相当の評価観点`.
- Curriculum tables must total the stated session duration. In the standard six-session format, each session should total 120 minutes and the course should total about 12 hours.
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
  '講座/COURSE/全体/COURSE_パンフレット.html'
```

## Verification

After generation:

1. Confirm `<講座名>_パンフレット.html` and `<講座名>_パンフレット.pdf` exist and the PDF is non-empty.
2. Verify the generated PDF itself, not only the HTML. Use `pdftotext` or a visual preview to confirm corrected wording appears in the pamphlet PDF.
3. Search HTML and extracted PDF text for stale wording: `オンラインワークショップ`, `ハイブリッド`, `レベル3相当の評価観点`, mismatched minute totals such as `140分`, and any old stakeholder-rejected phrasing.
4. For submission artifacts, read the PDF as a reviewer would and confirm the course purpose, target learners, delivery/LMS management, curriculum, exercises, outputs, and precautions are understandable without scripts.
5. Run `git diff --check`.
6. Run `python3 scripts/validate_local_skills.py` if skill files changed.
7. Before commit or push, confirm no `非公開/`, source PDFs, `.DS_Store`, credentials, real contact details, or private URLs are staged.

## Notes

The bundled `html_to_pdf.py` uses a local Chromium-family browser and Chrome DevTools `Page.printToPDF` with print backgrounds and CSS page size enabled. If no browser is found, pass `--browser` with the executable path.
