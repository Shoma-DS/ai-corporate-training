Packet ID: P1
Objective: Course-level audit and public-safety scan.
Ownership: Read-only audit plus workflow notes.

Do:
- Confirm course folder, six session folders, and `全体/` artifacts exist.
- Check stale public-facing names and live-workshop wording.
- Parse CSV files.
- Confirm pamphlet HTML/PDF presence.

Do not:
- Modify private source materials or unrelated dirty files.

Expected output:
- Result note under `results/P1-course-audit.md`.

Verification:
- `rg` stale wording scans.
- Python CSV parse.
- PDF text extraction where relevant.
