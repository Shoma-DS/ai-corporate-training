Packet ID: P3
Objective: Ensure instructor scripts are complete for recorded e-learning delivery.
Ownership: Six session `講師台本.md` files and `.workflow/ai/sync_script_slide_markers.py`.

Do:
- Ensure all six scripts contain S01-S40 `スライド切替` markers.
- Preserve existing detailed screen-share blocks.
- Add fallback read-aloud/work blocks only where slide markers are missing.
- Add `スライド切替タイムライン` and `作業風景タイムライン`.
- Normalize every screen-share block to include `⏱ 約○分`, `【手順N – 約○分】`, and `【見せるポイント】`.

Do not:
- Add live-chat, live presentation, mutual feedback, or timer callouts.

Expected output:
- 40 script slide markers for every session.

Verification:
- Regex counts for slide markers, demos, time lines, steps, and points.
