---
name: business-expansion-reskilling-builder
description: Create or update occupation-specific courses under `事業展開等リスキリング講座/` for the 人材開発支援助成金「事業展開等リスキリング支援コース」, including lecture-friendly editable HTML slides, slide PDFs, curricula, and HTML/PDF pamphlets. Use when the user names this subsidy course, asks for a course that reflects the 2026-08-03 rule change, or asks for a lighter lecture-first alternative to the repository's dense screening-slide standard. This is a scoped downstream helper of `corporate-training-course-builder`, not a replacement entrypoint for general course creation.
---

# Business Expansion Reskilling Builder

## Purpose

Build job-specific training that an instructor can teach smoothly and a learner can follow on screen. Keep the subsidy evidence in the curriculum and pamphlet, but do not reuse the dense Manabi DX screening-slide pattern.

Apply the repository `AGENTS.md`, then the nearer `事業展開等リスキリング講座/AGENTS.md`. For this subtree, the nearer file defines the slide style and artifact set.

## Required References

Read these before drafting:

- `references/eligibility-gate.md`: official-source eligibility and wording gate.
- `references/lecture-slide-standard.md`: the scoped lecture-first visual and narrative standard.
- `references/course-folder-standard.md`: required folders and files.

If the official guidance has changed since the recorded confirmation date, browse the latest Ministry of Health, Labour and Welfare page and update the source memo before producing public material.

## Workflow

1. Start through `skills/corporate-training-course-builder/SKILL.md`, then route here when the target is under `事業展開等リスキリング講座/`.
2. State the exact target occupation and recurring task. Reject a topic that is only generic literacy, manners, DX concepts, or general prompt writing.
3. Write a one-sentence job transfer: `対象職務で、何を入力し、どの手順で処理し、何を成果物として出し、誰がどう確認するか`.
4. Choose one official route: business expansion, DX/GX for a current job, or a planned future job under a documented personnel-development plan. Do not mix routes just to make a course sound eligible.
5. Create the course structure from `references/course-folder-standard.md` and write `全体/講座設計.yml` first.
6. Create the HTML-first pamphlet as `全体/<講座名>_講座カリキュラムパンフレット.html`. Generate the matching PDF with the repository pamphlet PDF helper.
7. Create one `slides.json` and one editable `講義スライド.html` per session. Use `scripts/build_lecture_slides.py` to render the HTML, then convert it to PDF. Do not create `スライド画像/Sxx.png` for this workflow.
8. Keep slides teachable: one conclusion, one concrete job example, and one learner action at most per normal slide. Put detailed proof, schedules, and eligibility notes in the pamphlet or appendix rather than filling every slide.
9. Include demonstrations, pauses, and self-checks in the flow. E-learning wording must tell learners to pause the video instead of implying live facilitation.
10. Validate the course with `scripts/validate_reskilling_course.py` and verify the generated PDFs directly.

## Hard Gates

- Do not say or imply that subsidy approval is guaranteed.
- Do not publish fixed claims about rates, deadlines, or required forms without a confirmation date and official URL.
- Do not treat generic AI prompts, DX concepts, digital literacy, manners, leadership, or ordinary tool operation as sufficient job specificity.
- Do not make the training a consulting engagement that creates the customer's actual management plan or production deliverable. Use dummy or anonymized data and teach transferable methods.
- For e-learning, show standard learning time, completion requirements, LMS evidence, and a broadly offered course page. Do not describe a customer-exclusive course as eligible e-learning.
- Keep customer names, employees, applications, prices, private links, and internal records out of the public repository.

## Build Commands

Render one session:

```bash
python3 skills/business-expansion-reskilling-builder/scripts/build_lecture_slides.py \
  '事業展開等リスキリング講座/COURSE/01-SESSION/slides.json'
```

Convert the rendered HTML to PDF:

```bash
python3 skills/course-pamphlet-html-pdf/scripts/html_to_pdf.py \
  '事業展開等リスキリング講座/COURSE/01-SESSION/講義スライド.html'
```

Validate a completed course:

```bash
python3 skills/business-expansion-reskilling-builder/scripts/validate_reskilling_course.py \
  --course-dir '事業展開等リスキリング講座/COURSE'
```

## Handoff

After a course idea is accepted, use `skills/training-idea-project-manager/SKILL.md` to register or update the idea in the GitHub Project. Set `制度区分=事業展開等リスキリング` and record the target occupation and official-source confirmation date.
