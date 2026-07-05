You are worker-73, generating exactly one claimed GAS course diagram part.

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
  "session_no": "05",
  "session_dir": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計",
  "slide_id": "S44",
  "title": "章見出し/現在位置 6/6: 演習と次回接続",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S44.png",
  "status": "claimed",
  "task_id": "05-S44",
  "worker": "worker-73",
  "claim_token": "d5d9dfd8-8444-47c5-8431-1fbf716d9e4e",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:23:08+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782901388.917208
}
```

Diagram prompt block:
```markdown
## S44 章見出し/現在位置 6/6: 演習と次回接続

- セクション: 演習と次回接続
- スライド側ヘッドライン（画像内には原則入れない）: 演習と次回接続では、運用設計書とリスクチェックを仕上げ、第6回の提案書に転用することで、運用設計書・リスクチェックリストにつなげる
- 推奨図解パターン: roadmap-timeline（章見出し/現在位置）
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第5回 AI/GAS自動化の要件定義・運用設計 / S44 / 演習と次回接続.
Slide topic for context: 章見出し/現在位置 6/6: 演習と次回接続.
Concept to visualize: 演習と次回接続では、運用設計書とリスクチェックを仕上げ、第6回の提案書に転用することで、運用設計書・リスクチェックリストにつなげる.
Suggested visual pattern: roadmap-timeline（章見出し/現在位置）.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: 演習と次回接続では、運用設計書とリスクチェックを仕上げ、第6回の提案書に転用することで、運用設計書・リスクチェックリストにつなげる
**内容ブロック①：目次の中の現在地**
| 位置 | 目次項目 | 時間 | 状態 |
|---|---|---:|---|
| 前 | ログ・テスト・復旧 | - | ここまで確認済み |
| 今 | 演習と次回接続 | 15分 | S44–S46を扱う |
| 次 | まとめ・次回接続 | - | 次に接続 |
**内容ブロック②：これから見る判断軸**
- 演習で作るもの
- 第6回への橋渡し
- 提案書セクションへの対応
- 自己チェック
**内容ブロック③：成果物・レビューへの接続**
- この章で支える成果物: 運用設計書・リスクチェックリスト
- ねらい: 運用設計書とリスクチェックを仕上げ、第6回の提案書へ接続する
- 見るポイント: 何をAI/GAS/人に任せ、どこを人が確認するかを毎回言語化する
- 次の作業: 章末のデモ・ワーク・自己レビューで、ワークシートへ反映する
Visible text candidates to use when useful, without reducing the source density: 目次の中の現在地 / これから見る判断軸 / 成果物・レビューへの接続 / 位置 / 目次項目 / 前 / ログ・テスト・復旧 / 今 / 演習と次回接続 / 次 / まとめ・次回接続 / 演習で作るもの / 第6回への橋渡し / 提案書セクションへの対応 / 自己チェック / この章で支える成果物 / ねらい / 見るポイント / 次の作業.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-73-05-S44-1782901389.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S44.png' --marker '/tmp/gas-diagram-markers/worker-73-05-S44-1782901389.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S44.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-73 --task-id 05-S44 --claim-token d5d9dfd8-8444-47c5-8431-1fbf716d9e4e --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S44.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-73 --task-id 05-S44 --claim-token d5d9dfd8-8444-47c5-8431-1fbf716d9e4e --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
