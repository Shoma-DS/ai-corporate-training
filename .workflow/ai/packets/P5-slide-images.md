Packet ID: P5
Objective: Track and generate missing slide images.
Ownership: Session `スライド画像/Sxx.png` files and image-generation progress notes.

Do:
- Keep a current missing-image list.
- Generate missing images with GPT image 2 / built-in `image_gen`, one complete bitmap per slide.
- Copy only verified generated bitmaps into `スライド画像/Sxx.png` without pixel modification.
- Inspect generated images for old course names, wrong Japanese, placeholders, sparse layout, overlap, missing output/risk bands, and public-safety issues.

Do not:
- Use SVG, HTML/CSS, canvas, browser screenshots, PIL, ImageMagick, local rasterization, local compositing, or text overlays.
- Mark missing slides complete with placeholders.

Expected output:
- Eventually, 240 valid slide images across the six sessions.

Verification:
- File-count audit, image provenance notes, visual/OCR checks.
