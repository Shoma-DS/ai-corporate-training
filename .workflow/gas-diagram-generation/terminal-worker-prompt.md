You are __WORKER_ID__ in `/Users/deguchishouma/Desktop/AI法人研修`.

Read `.workflow/gas-diagram-generation/worker-instructions.md`, then execute it for worker id `__WORKER_ID__`.

Important overrides:
- Use the shared queue, not fixed shards.
- Use only built-in Codex App Server / GPT image 2 / imagegen for images.
- Do not use browser, API key fallback, local drawing, SVG/HTML/canvas/PIL/ImageMagick, screenshots, or overlays.
- Claim one task at a time with `python3 .workflow/gas-diagram-generation/shared_queue.py claim --worker __WORKER_ID__ --stale-minutes 90`.
- Stop when the queue is empty, or after __MAX_TASKS__ successful tasks if __MAX_TASKS__ is greater than 0.
- Append progress only to `.workflow/gas-diagram-generation/reports/__WORKER_ID__.md`.
