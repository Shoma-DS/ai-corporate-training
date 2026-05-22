# Session-Specific Exercise Data Workflow

Use this when the user says per-session exercise data looks the same, asks for only the data used in each session, or asks whether CSV/sample data was actually fixed.

## Goal

Each session folder's `演習データ/` must contain only the files needed for that session's demos, worksheets, and learner outputs. Do not copy one common CSV bundle into every session unless the course intentionally reuses a shared dataset and the materials say so.

## Workflow

1. Map the session outcomes.
   - Read `スライド案.md`, `講師台本.md`, `ワークシート.md`, `配布資料/`, syllabus, and course overview.
   - Write down what learners produce in each session: issue inventory, data dictionary, automation table, AI review sheet, requirements memo, proposal, or another artifact.

2. Inventory current data.
   - List every `*/演習データ/*` file and identify duplicated bundles, old generic files, stale filenames, and files never referenced by the target session.
   - If files are identical across sessions, treat that as a problem to resolve unless the lesson explicitly builds on the same shared dataset.

3. Design data by teaching purpose.
   - Session 01: business issue inventory, improvement theme selection, before/after observation data.
   - Session 02: form responses, ledger column definitions, master tables, validation examples.
   - Session 03: GAS-ready rows, CSV import samples, status updates, due dates, notification logs, error cases.
   - Session 04: AI classification inputs, summary inputs, transcript/action extraction samples, AI output review rows.
   - Session 05: requirements, operations, permissions, risk, test cases, recovery paths.
   - Session 06: proposal materials, KPI/effect estimates, roadmap, risk countermeasures, review criteria.
   - Adapt these categories to the course; the rule is purpose-fit, not fixed filenames.

4. Rebuild per-session folders.
   - Keep only files used in that session's script, worksheet, handout, or demo.
   - Create `演習データ/README.md` explaining each file, where it is used, and the expected output.
   - Create or update `配布資料/演習ガイド.md` so the learner can connect the data to the exercise.
   - Create or update `ワークシート.md` to reference only files in that session.
   - If the user explicitly asked to fix the duplicated data, remove irrelevant duplicated files from each session. Otherwise, explain the proposed deletion before doing it.

5. Add a course-level map.
   - Create or refresh `全体/演習データ回別一覧.md` or an equivalent course-level index.
   - For each session, list file names, learner task, source pattern, and why the file belongs only to that session.

6. Update references.
   - Search and update `講師台本.md`, `スライド案.md`, `ワークシート.md`, `配布資料/`, `全体/詳細シラバス.md`, `全体/講座概要.md`, and source notes.
   - Remove references to deleted generic filenames such as old shared inquiry, approval, report, sales, task, customer-follow, or meeting-note samples.

## Data Design Rules

- Use fictional, public-safe data only: dummy departments, `担当A`, sample IDs, and generic business cases.
- Do not include real names, emails, phone numbers, domains, addresses, prices, contracts, customer records, API keys, tokens, or private Drive details.
- Include realistic imperfections when useful: duplicate IDs, blank owners, inconsistent labels, missing attachments, overdue due dates, ambiguous AI output, permission risks, and manual recovery rows.
- Keep row counts big enough for filtering, summary, validation, or error handling, but small enough for learners to inspect in a recorded lesson.
- Keep columns operational: ID, source, status, priority, owner, due date, AI classification, human review, notification log, error, next action.

## Verification

Run checks before finishing:

```bash
find '講座/対象講座名' -path '*/演習データ/*' -type f | sort
```

```bash
python3 - <<'PY'
from pathlib import Path
import csv

root = Path('講座/対象講座名')
for path in sorted(root.glob('*/演習データ/*.csv')):
    with path.open(encoding='utf-8-sig', newline='') as f:
        list(csv.reader(f))
print('csv ok')
PY
```

```bash
rg -n '古いCSV名|削除したファイル名|共通データ名' '講座/対象講座名'
```

```bash
rg -n '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}|0[0-9]{1,4}[-(][0-9]{1,4}|API[_ -]?KEY|SECRET|PASSWORD|TOKEN' '講座/対象講座名'
```

Also verify manually:

- Each session has different data when its exercise goal is different.
- Every data file is referenced by that session's materials, or the README explains why it is preparatory.
- No session references a file that exists only in another session.
- Course-level source notes in `全体/調査/` cite official facts and public practitioner patterns when online examples influenced the redesign.
