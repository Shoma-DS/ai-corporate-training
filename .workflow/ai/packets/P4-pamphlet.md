Packet ID: P4
Objective: Refresh and verify course pamphlet HTML/PDF.
Ownership: `全体/AIエージェント実装・連携設計アカデミー_パンフレット.html` and `.pdf`.

Do:
- Run the pamphlet builder because `パンフレット原稿.md` was newer than HTML.
- Verify the PDF text directly.
- Confirm e-learning/LMS/120-minute wording and stale wording absence.

Do not:
- Add prices, contacts, Drive links, Canva links, credentials, or customer-specific information.

Expected output:
- Updated pamphlet HTML/PDF and result note.

Verification:
- `pdftotext` stale wording scan.
