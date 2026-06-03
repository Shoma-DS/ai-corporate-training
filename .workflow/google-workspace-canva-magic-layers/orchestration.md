# Orchestration: Google Workspace Canva Image-first Presentation

## Execution Rules

- Keep the image-first objective intact.
- Do not use Canva MCP `_image_to_design` for every slide unless the user explicitly switches to the legacy all-page Magic Layers route.
- Keep immediate blocking work local.
- Simulate packets when no subagent runner is needed.
- Integrate packet results before final verification.

## Sequence

1. Confirm repository rules and local skills.
2. Build image inventory for the Google Workspace course.
3. Create or verify Google Drive synced project folders.
4. Create or verify Canva project folders.
5. Build one upload bundle per session, preferably a PPTX with each `Sxx.png` as one full-slide page.
6. Create one image-based Canva presentation per session by uploading the bundle or images.
7. Move each generated presentation to the matching Canva session folder.
8. Record session-level presentation URLs and IDs in private logs only.
9. Create a manual Magic Layers target list for high-edit pages only.
10. Generate private CSV/Markdown indexes in `非公開/Canva/` and the Google Drive synced folders.
11. Verify counts, folder existence, workflow artifacts, and public-repo safety.

## Branching Rules

- If Canva upload/import fails once, retry that session once after logging the error.
- If the same session fails twice, record it in the private log as failed and continue only if the remaining sessions can still be processed independently.
- If Canva folder creation fails, stop before creating new presentations because designs would not be organized as requested.
- If Google Drive sync folder is unavailable, create private URL files in `非公開/Canva/` and report the Drive-side blocker.
- If the user explicitly requires every page to be editable, switch to the legacy all-page Magic Layers route and document the higher token/API cost before starting.

## Packet Prompts

- P1 owns local inventory and Drive folder preparation.
- P2 owns Canva folder hierarchy.
- P3 owns session upload bundle creation.
- P4 owns Canva image-based presentation creation and movement.
- P5 owns manual Magic Layers target-page planning.
- P6 owns aggregation and verification.

## Completion Audit

- Verify total and per-session page counts.
- Verify URL indexes exist privately and in Drive folders.
- Verify manual Magic Layers target list exists.
- Verify workflow artifact completeness.
- Verify public repo safety.
