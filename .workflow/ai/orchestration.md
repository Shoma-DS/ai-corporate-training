# Orchestration: AIエージェント実装連携設計アカデミー完成

## Execution Rules

- Keep the original objective intact.
- Ask for approval before risky, expensive, external, or destructive actions.
- Keep immediate blocking work local.
- Delegate only bounded, disjoint, materially useful packets.
- Integrate packet results before final verification.

## Branching Rules
- If text artifacts fail counts, repair source Markdown first and do not move to image generation.
- If pamphlet PDF text differs from HTML/Markdown, regenerate PDF and verify with `pdftotext`.
- If an image is missing, do not create a placeholder. Use GPT image 2 / built-in `image_gen` or copy a verified generated bitmap without modifying pixels.
- If generated-image provenance is uncertain, leave the slide marked missing.

## Packet Prompts
- P1: Audit course-level files, names, public-safety risks, CSV parse status, and pamphlet state.
- P2: Sync `画像生成プロンプト.md` headline/content-block evidence into each `スライド案.md` as `### Sxx` high-density detail sections.
- P3: Ensure every `講師台本.md` has S01-S40 `スライド切替` markers, screen-share time/steps/points, and end timelines.
- P4: Refresh `<講座名>_パンフレット.pdf` and verify PDF text for delivery/LMS/stale wording.
- P5: Track missing slide images and generate/copy only valid complete raster images.
- P6: Run integrated verification and write the final report from current-state evidence.

## Completion Audit
- Current text completion requires six sessions with 40 slide rows, 40 detailed `### Sxx` entries, 40 headlines, 40 prompt sections, and 40 script markers.
- Current image completion requires 240 valid `スライド画像/Sxx.png` files. As of this workflow run, session 1 has 40, session 2 has S01-S02, and sessions 3-6 have 0.
- Do not mark the overall goal complete until image generation and inspection are complete for sessions 2-6.
