You are worker-72, generating exactly one claimed GAS course diagram part.

Coordinator already read repository rules and selected this task. Do not browse. Do not inspect the whole repo. Use only the task JSON and prompt block below.

Hard rules:
- Use built-in Codex image generation / GPT image 2 / imagegen only.
- Do not use OpenAI API keys, SDK scripts, SVG, HTML/CSS, canvas, PIL, ImageMagick, browser screenshots, local drawing, local text overlays, or global generated_images search.
- Output must be a single complete PNG copied to the exact target.
- Make it a wide, slightly vertically compact, high-density Japanese business training reference diagram.
- Do not render course name, session name, S番号, section header, or full slide title inside the image.
- Use readable Japanese card/table/process text from the prompt block. Reject placeholders, fake UI/logos, empty boxes, unreadable tiny text, or sparse decorative visuals.

Task JSON:
```json
{
  "course": "生成AI・GASで実践する業務変革・DX推進講座",
  "session_no": "06",
  "session_dir": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成",
  "slide_id": "S04",
  "title": "章見出し/現在位置 1/7: 導入と提案書の考え方",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S04.png",
  "status": "claimed",
  "task_id": "06-S04",
  "worker": "worker-72",
  "claim_token": "a567cac2-1bd1-48b9-b289-12cda514e27e",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:26:10+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782901570.1847308
}
```

Diagram prompt block:
```markdown
## S04 章見出し/現在位置 1/7: 導入と提案書の考え方

- セクション: 導入と提案書の考え方
- スライド側ヘッドライン（画像内には原則入れない）: 導入と提案書の考え方では、提案書を作ったものの紹介ではなく、導入判断の材料として設計することで、提案書骨子の前提整理につなげる
- 推奨図解パターン: roadmap-timeline（章見出し/現在位置）
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S04 / 導入と提案書の考え方.
Slide topic for context: 章見出し/現在位置 1/7: 導入と提案書の考え方.
Concept to visualize: 導入と提案書の考え方では、提案書を作ったものの紹介ではなく、導入判断の材料として設計することで、提案書骨子の前提整理につなげる.
Suggested visual pattern: roadmap-timeline（章見出し/現在位置）.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: 導入と提案書の考え方では、提案書を作ったものの紹介ではなく、導入判断の材料として設計することで、提案書骨子の前提整理につなげる
**内容ブロック①：目次の中の現在地**
| 位置 | 目次項目 | 時間 | 状態 |
|---|---|---:|---|
| 前 | 表紙・成果物・目次 | - | ここまで確認済み |
| 今 | 導入と提案書の考え方 | 15分 | S01–S06を扱う |
| 次 | 課題整理とユースケース選定 | - | 次に接続 |
**内容ブロック②：これから見る判断軸**
- 最終回の位置づけ
- 導入判断の材料
- 8セクション
- 安全確認
**内容ブロック③：成果物・レビューへの接続**
- この章で支える成果物: 提案書骨子の前提整理
- ねらい: 提案書を「作ったものの紹介」ではなく「導入判断の材料」として捉える
- 見るポイント: 何をAI/GAS/人に任せ、どこを人が確認するかを毎回言語化する
- 次の作業: 章末のデモ・ワーク・自己レビューで、ワークシートへ反映する
Visible text candidates to use when useful, without reducing the source density: 目次の中の現在地 / これから見る判断軸 / 成果物・レビューへの接続 / 位置 / 目次項目 / 前 / 表紙・成果物・目次 / 今 / 導入と提案書の考え方 / 次 / 課題整理とユースケース選定 / 最終回の位置づけ / 導入判断の材料 / 8セクション / 安全確認 / この章で支える成果物 / ねらい / 見るポイント / 次の作業 / 作ったものの紹介.
Create a dense supplemental image, not a decorative icon. Use 2-4 structured zones such as a comparison table, process table, hierarchy diagram, checklist, decision canvas, output map, or industry-example list according to the source slide. Preserve the source slide's key information density by showing the main judgment axis, learner action, output, concrete examples, and review/risk point when they exist.
Visible text inside the image: include readable Japanese headings, table cells, card text, and concrete examples, not only labels. For dense source slides, use roughly 8-20 readable text cells/short phrases across the image. Keep text readable at slide size; numeric notes such as `5〜8個` or `10個以内` are allowed. Avoid long paragraphs, but do not remove core Before/After rows, process steps, hierarchy levels, or industry examples.
The editable Google Slides template will manage the course title, session title, S-number, section header/current position, and full slide title. The generated image may include its own concise content heading and the dense table/canvas text needed to understand the material, but it should not consume the title/header area like a full-slide screenshot.
If the slide needs official screenshots or logos, leave the diagram generic and do not invent real Google UI or brand marks.
```

ネガティブプロンプト:

```text
Do not include the editable deck header/footer, S-number, course title, session title, section header, fake Google logos or UI, personal data, placeholders, empty dashed frames, poster/recruitment/ad layouts, unreadable small text, incorrect Japanese, text-free decorative icon-only output, or short-label-only output with no explanation. Avoid long paragraph dumps and speaker notes. Use readable Japanese headings, table cells, card text, and examples as dense supplemental information.
```
```

Required commands after image generation:
1. Before calling imagegen, ensure marker exists:
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-72-06-S04-1782901570.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S04.png' --marker '/tmp/gas-diagram-markers/worker-72-06-S04-1782901570.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S04.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-72 --task-id 06-S04 --claim-token a567cac2-1bd1-48b9-b289-12cda514e27e --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S04.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-72 --task-id 06-S04 --claim-token a567cac2-1bd1-48b9-b289-12cda514e27e --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
