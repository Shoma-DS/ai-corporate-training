Packet ID: P6
Objective: Prove current completion status from current-state evidence.
Ownership: Read-only checks plus `.workflow/ai/final-report.md`.

Do:
- Run local skill validation, workflow verifier, CSV parser, stale wording scans, time totals, slide/prompt/script/image counts, pamphlet PDF scan, and diff checks.
- Update final report with accepted results, rejected/incomplete items, remaining risks, and next actions.

Do not:
- Mark the user goal complete unless all explicit requirements, including slide images, are proven complete.

Expected output:
- `final-report.md` with evidence and current blockers/remaining work.

Verification:
- `python3 skills/codex-dynamic-workflows/scripts/verify_workflow.py .workflow/ai`
