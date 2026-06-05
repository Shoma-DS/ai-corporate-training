# Google Workspace Slide Image and Canva Rebuild Plan

Goal: 新しくなったGoogle Workspace/GAS講座の `スライド案.md` を正として、全回の `画像生成プロンプト.md`、`スライド画像/Sxx.png`、Canva用PPTX、CanvaブラウザMagic Layers適用記録まで作る。

## Scope

- Course: `講座/Google Workspace・GASで進めるAI業務効率化-DX実践講座`
- Sessions:
  - 01: 43 slides
  - 02: 40 slides
  - 03: 44 slides
  - 04: 40 slides
  - 05: 40 slides
  - 06: 40 slides
- Total: 247 slide images

## Constraints

- Final slide images must be complete raster images generated with GPT image 2 / built-in image generation.
- Do not create final slide images from SVG, HTML/CSS, canvas, browser screenshots, PIL, ImageMagick, local rasterization, or post-generation text/logo overlays.
- Do not ask image generation to invent Google logos, product UI, or real screenshots.
- Use official/static assets and dummy-environment screenshots only when safe. Keep private URLs and Canva IDs under `非公開/`.
- Canva first receives image-based multi-page decks. Magic Layers is then applied in browser only to selected editable pages, with page-level status logged under `非公開/Canva/`.

## Work Stages

1. Prompt sync
   - Generate canonical `画像生成プロンプト.md` for every session from the current `スライド案.md`.
   - Verify slide counts, headline counts, and prompt counts match.
2. Slide image regeneration
   - Treat all 247 slides as regeneration scope.
   - Start with missing images so every deck has complete page coverage.
   - Continue in batches by session and slide range.
3. Export preparation
   - Use `skills/gws-ai-training-slide-exporter` after image coverage is complete.
   - Create session PPTX bundles under `書き出し/canva-pptx/Google Workspace・GASで進めるAI業務効率化-DX実践講座/`.
4. Canva import and Magic Layers
   - Import image-first PPTX into Canva.
   - Apply Magic Layers page by page only to target pages unless user requires all pages.
   - Validate Japanese text, wording, layout, screenshots, logos, and overlaps.
   - Undo/retry failed pages up to 3 attempts, then keep flat image page and record status.
5. Final verification
   - Verify prompt/image/PPTX counts and Canva log completeness.
   - Keep goal active until all requested end-state evidence exists.

## Verification Commands

```bash
for d in '講座/Google Workspace・GASで進めるAI業務効率化-DX実践講座'/[0-9][0-9]-*; do
  printf '%s\n' "$d"
  rg -c '^### S[0-9][0-9]' "$d/スライド案.md"
  rg -c '^## Slide S[0-9][0-9]' "$d/画像生成プロンプト.md"
  find "$d/スライド画像" -maxdepth 1 -type f -name 'S*.png' | wc -l
done
python3 scripts/validate_local_skills.py
```
