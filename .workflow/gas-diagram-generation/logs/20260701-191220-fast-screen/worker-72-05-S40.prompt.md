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
  "session_no": "05",
  "session_dir": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計",
  "slide_id": "S40",
  "title": "手動復旧の5ステップ",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S40.png",
  "status": "claimed",
  "task_id": "05-S40",
  "worker": "worker-72",
  "claim_token": "46703abc-90e3-45b9-a661-7b8ad4565bbe",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:18:07+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782901087.7028139
}
```

Diagram prompt block:
```markdown
## S40 手動復旧の5ステップ

- セクション: ログ・テスト・復旧
- スライド側ヘッドライン（画像内には原則入れない）: 処理が止まったとき「気づく・止める・戻す・再実行・記録する」の5ステップを事前に決めることで、復旧を属人化させずに済む
- 推奨図解パターン: process-flow
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第5回 AI/GAS自動化の要件定義・運用設計 / S40 / ログ・テスト・復旧.
Slide topic for context: 手動復旧の5ステップ.
Concept to visualize: 処理が止まったとき「気づく・止める・戻す・再実行・記録する」の5ステップを事前に決めることで、復旧を属人化させずに済む.
Suggested visual pattern: process-flow.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: 処理が止まったとき「気づく・止める・戻す・再実行・記録する」の5ステップを事前に決めることで、復旧を属人化させずに済む
**内容ブロック①：手動復旧の5ステップ**
| ステップ | やること | 誰がやるか |
|---|---|---|
| 1. 気づく | ログのエラー・通知の停止・担当者からの問い合わせ | 確認者・管理者 |
| 2. 止める | トリガーを一時停止。GASの「トリガー無効化」 | 管理者 |
| 3. 戻す | 誤処理されたデータをSheetsで手動修正 | 管理者 or 確認者 |
| 4. 再実行 | 手動実行モードで問題件数だけ再処理 | 管理者 |
| 5. 記録する | 発生日時・原因・対応内容・再発防止策をログに記録 | 管理者 |
**内容ブロック②：「戻す」ためのバックアップ設計**
- Sheetsのデータは処理前にバックアップシートへコピーするステップをGASに入れる
- GASが書き込む前の状態を「バックアップ_YYYYMMDD」シートとして保存
- 誤処理が判明したときにバックアップから復元できる
**内容ブロック③：業種別の復旧ケース例**
- 建設業: 月報集計GASが途中で止まった → バックアップから月報データを復元 → 残件を手動集計
- 士業: 書類依頼の分類が誤分類で全件「不明」になった → 台帳の分類列を手動で修正 → 再通知
Visible text candidates to use when useful, without reducing the source density: 手動復旧の5ステップ / 「戻す」ためのバックアップ設計 / 業種別の復旧ケース例 / やること / 1. 気づく / ログのエラー・通知の停止・担当者からの問い合わせ / 2. 止める / トリガーを一時停止 / 3. 戻す / 誤処理されたデータをSheetsで手動修正 / 4. 再実行 / 手動実行モードで問題件数だけ再処理 / 5. 記録する / 発生日時・原因・対応内容・再発防止策をログに記録 / 誤処理が判明したときにバックアップから復元できる / 建設業 / 士業 / トリガー無効化 / 戻す / 不明.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-72-05-S40-1782901087.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S40.png' --marker '/tmp/gas-diagram-markers/worker-72-05-S40-1782901087.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S40.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-72 --task-id 05-S40 --claim-token 46703abc-90e3-45b9-a661-7b8ad4565bbe --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S40.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-72 --task-id 05-S40 --claim-token 46703abc-90e3-45b9-a661-7b8ad4565bbe --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
