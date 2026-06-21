Packet ID: P2
Objective: Make every session slide plan mechanically verifiable and dense enough for review.
Ownership: Six session `スライド案.md` files and `.workflow/ai/sync_slide_plan_details.py`.

Do:
- Add `## 高密度スライド詳細` to each session slide plan.
- Include `### Sxx`, `**ヘッドライン:**`, template ID, diagram pattern, material, content blocks, and output/check points for every slide.
- Use `画像生成プロンプト.md` as the source for headlines and content block detail.

Do not:
- Change generated slide images or create local-rendered placeholders.

Expected output:
- 40 detail sections and 40 headlines per session.

Verification:
- Count `^### S\d\d` and `^\*\*ヘッドライン:\*\*` inside each detail section.
