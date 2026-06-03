# Canva Quality Checklist

Use this checklist when converting `スライド画像/Sxx.png` into PPTX and importing the deck into Canva, and when applying Magic Layers in the Canva browser. Add new failure patterns here when validation finds a reusable risk.

## Quality-Preserving Defaults

- Use 16:9 slide size consistently from source PNG to PPTX to Canva.
- Place each PNG as a full-page image with no margins, no crop, no shadow, no transparency effect, and no additional text overlays.
- Prefer PNG source images for text-heavy training slides. Avoid converting to JPEG before Canva import.
- Keep the original `スライド画像/Sxx.png` as the source of truth. Do not replace it with a Canva-rendered copy.
- Generate a Canva-ready PPTX from source images, then verify page count and order before opening browser-based editing.
- Preserve page order as `S01`, `S02`, `S03` through the final slide. Do not sort by unpadded filenames.
- Avoid applying Magic Layers to pages dominated by screenshots, detailed diagrams, dense tables, exercise instructions, or small Japanese text unless editability is clearly needed.
- Keep fixed explanation pages as image pages when visual fidelity matters more than editability.

## PPTX And Canva Import Checks

- Page count in Canva matches the local `スライド画像/Sxx.png` count.
- First, middle, and final pages match the expected `Sxx` order.
- Slide aspect ratio remains 16:9; no white border, black border, crop, or stretched image appears.
- Text edges are not noticeably blurred compared with the source image.
- Colors are close enough for corporate training use; no unexpected darkening, washed-out backgrounds, or brand color shifts.
- Logos and screenshots are intact as image content.
- No page has been converted into unrelated stock-like imagery or a different design.

## Magic Layers Checks

- Japanese text has no mojibake, missing characters, random substitutions, or changed terminology.
- Slide title and key phrases match the source image.
- Tables retain row and column structure; no cells overlap or drift.
- Cards, arrows, icons, and callout boxes keep their relative positions.
- Official logos are not redrawn, distorted, recolored, or replaced.
- Screenshots remain visually coherent; UI elements are not split into nonsensical layers.
- Small labels, footnotes, and numbered steps remain readable.
- Dense pages do not become cluttered with many misaligned editable objects.
- Background image, title, and foreground objects do not reorder incorrectly.

## Retry And Fallback Rule

- A Magic Layers attempt fails when text, layout, logo, screenshot, or page structure no longer matches the source image closely enough for training delivery.
- On failure, undo or restore the page to the pre-Magic-Layers image state before retrying.
- Retry at most 2 additional times after the first failed attempt.
- If the same page fails 3 times total, stop applying Magic Layers to that page and keep the original image.
- Record the page as `kept_image` or `needs_manual_fix` in `非公開/Canva/<講座名>_Magic_Layers検証ログ.csv`.

## Failure Patterns To Watch

- Dense Japanese body text becomes fragmented or rewritten.
- Curriculum tables lose alignment.
- Screenshot-heavy pages are split into unrelated pieces.
- Logo areas become distorted after layer extraction.
- Fine divider lines disappear or shift.
- Numbered workflow arrows lose order.
- Light-gray cards blend into the background.

## Running Notes

Append new reusable findings below. Keep entries abstract and public-safe. Do not include Canva URLs, design IDs, customer names, private screenshots, or credential-like values.

### Added Findings

- Initial baseline: no project-specific Canva failures recorded yet.
