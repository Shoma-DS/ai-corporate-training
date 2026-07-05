You are worker-53 in `/Users/deguchishouma/Desktop/AI法人研修`.

Read `.workflow/gas-diagram-generation/worker-instructions.md`, then execute it for worker id `worker-53`.

Important overrides:
- Use the shared queue, not fixed shards.
- Use only built-in Codex App Server / GPT image 2 / imagegen for images.
- Do not use browser, API key fallback, local drawing, SVG/HTML/canvas/PIL/ImageMagick, screenshots, or overlays.
- Claim one task at a time with `python3 .workflow/gas-diagram-generation/shared_queue.py claim --worker worker-53 --stale-minutes 90`.
- Stop when the queue is empty, or after 1 successful tasks if 1 is greater than 0.
- Append progress only to `.workflow/gas-diagram-generation/reports/worker-53.md`.
