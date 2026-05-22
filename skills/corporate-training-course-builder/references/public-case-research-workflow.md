# Public Case Research Workflow

Use this when the user asks to revise worksheets, handouts, exercise data, demos, or scripts while checking online concrete examples or public use cases.

## Source Mix

- Use official/vendor docs for current capabilities, quotas, supported editions, logos, screenshots, and restrictions.
- Use public practitioner examples for realistic workflow patterns: Qiita, Zenn, note, personal blogs, company tech blogs, public forums, product communities, and public YouTube/blog walkthroughs.
- Use public customer stories only as high-level inspiration. Do not reproduce a named company's internal workflow, performance claims, pricing, contact details, or confidential-sounding process.
- Prefer several small sources over one source. A useful mix is 2-3 official sources plus 3-6 practitioner/public examples when time allows.

## Search Pattern

Search in Japanese and English, combining:

- The target tool: `Google Apps Script`, `GAS`, `Googleフォーム`, `スプレッドシート`, `Gemini`, `Google Workspace`, `Meet 文字起こし`
- The workflow: `問い合わせ管理`, `申請承認`, `日報`, `リマインド`, `PDF 自動作成`, `メール通知`, `重複チェック`, `議事録`, `期限管理`
- The source type: `Qiita`, `Zenn`, `note`, `個人ブログ`, `事例`, `業務効率化`, `automation`, `workflow`

When current behavior matters, verify dates and cross-check with official docs. Treat older practitioner posts as examples of patterns, not proof that a feature still works.

## What To Extract

Extract patterns, not prose:

- Business trigger: form submitted, CSV imported, status changed, due date approaching, transcript created, weekly report due.
- Data shape: columns, required fields, master tables, status values, owner fields, due dates, review flags, log fields.
- Automation shape: Apps Script trigger, custom menu, time-driven batch, Gmail/Chat notification, Docs/PDF generation, Calendar event, Drive filing.
- AI shape: classification, summarization, reply draft, action extraction, report draft, code explanation, human review.
- Edge cases: missing attachment, duplicate row, blank owner, overdue task, ambiguous AI output, permission error, quota/limit, unavailable Gemini/Meet feature, manual recovery.
- Teaching value: what the learner can build or decide after the exercise.

Do not copy source text, code, screenshots, exact business data, or named-customer detail unless the user explicitly asks and the license allows it. Paraphrase and cite the source memo.

## Source Memo

Save a concise memo in the course-level `全体/調査/` folder. Include:

- Title, access date, and URL for each source.
- Source type: official doc, customer story, practitioner article, community thread, video/blog.
- Extracted pattern: one or two bullets explaining what should influence the course.
- Course impact: which session, worksheet, handout, demo, or exercise data should change.
- Rejected ideas: patterns that were too tool-specific, outdated, paid-feature dependent, unsafe for public repo, or too close to a real company's details.

Keep company/private materials out of public notes. If a private Drive or `非公開/` source is used, record only an abstracted influence in public files.

## Revising Handouts

Make handouts help learners turn examples into their own safe workflow:

- Add a case-pattern selector: intake, approval, reporting, CSV cleanup, due-date reminder, meeting follow-up, document generation.
- Add an As-Is/To-Be table with input, processing, output, review, notification, logging, and fallback.
- Add a data dictionary: column name, source, required/optional, update method, owner, validation, privacy risk.
- Add an AI/GAS role split: mechanical processing by Sheets/GAS, language judgment/draft by AI, final approval by human.
- Add fallback and availability checks for paid/admin-dependent features such as Gemini Workspace integration or Meet transcripts.
- Add a review checklist for AI outputs: fact, assumption, missing context, personal data, wording risk, approval needed.

## Revising Exercise Data

Exercise data must be fictional, public-safe, and operationally realistic:

- Use dummy people such as `担当A` and dummy departments. Do not use real names, emails, domains, prices, contracts, addresses, or customer records.
- Keep exercise data session-specific. If different sessions teach different workflows, each `演習データ/` folder should contain different files suited to that session rather than the same common CSV set.
- Add enough rows to support filtering, duplicates, overdue checks, status updates, summaries, and error handling.
- Include imperfect cases deliberately: duplicate IDs, blank assignees, inconsistent category labels, missing attachments, ambiguous free-text requests, overdue tasks, and "needs human review" rows.
- Add columns that support operations, not just content: `受付ID`, `入力元`, `ステータス`, `優先度`, `担当者`, `期限`, `AI分類`, `人の確認`, `通知ログ`, `エラー`, `次アクション`.
- For each session, decide whether duplicated `演習データ/` files should stay synchronized across all sessions or diverge for a session-specific exercise. If the user complains that all sessions look the same, prefer divergence by actual exercise purpose and read `session-specific-exercise-data-workflow.md`.

## Public Safety Checks

Before finishing:

- Search changed public files for email addresses, phone numbers, company-specific names, real customer-like records, prices, credentials, API keys, and private Drive details.
- Confirm every external source has a public source memo with access date.
- Confirm examples are abstracted into reusable patterns and do not imply guaranteed results.
- Confirm worksheets/data still match the syllabus, instructor script, and slide plan.
