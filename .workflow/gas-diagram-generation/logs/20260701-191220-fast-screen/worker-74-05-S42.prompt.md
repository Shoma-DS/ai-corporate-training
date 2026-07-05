You are worker-74, generating exactly one claimed GAS course diagram part.

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
  "slide_id": "S42",
  "title": "代替運用を先に書く",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S42.png",
  "status": "claimed",
  "task_id": "05-S42",
  "worker": "worker-74",
  "claim_token": "a0e44e91-4eea-4e9e-9a44-4550e3e6a44e",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:18:26+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782901106.804088
}
```

Diagram prompt block:
```markdown
## S42 代替運用を先に書く

- セクション: ログ・テスト・復旧
- スライド側ヘッドライン（画像内には原則入れない）: GAS・Gemini・通知が使えない場合の代替手順を先に設計することで、障害時も業務を止めずに続けられる
- 推奨図解パターン: before-after-transformation
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第5回 AI/GAS自動化の要件定義・運用設計 / S42 / ログ・テスト・復旧.
Slide topic for context: 代替運用を先に書く.
Concept to visualize: GAS・Gemini・通知が使えない場合の代替手順を先に設計することで、障害時も業務を止めずに続けられる.
Suggested visual pattern: before-after-transformation.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: GAS・Gemini・通知が使えない場合の代替手順を先に設計することで、障害時も業務を止めずに続けられる
**内容ブロック①：代替運用の4パターン**
| 障害ケース | 代替手順 | 再開の目安 |
|---|---|---|
| GASが止まった | 担当者がフォーム回答をSheetsで手動確認し、台帳に貼り付ける | GAS修正後に再開（目安: 当日中） |
| Gemini連携が使えない | 手動でGemini.google.comを使い、分類結果を台帳に手入力 | 連携復旧まで手動継続 |
| 通知メールが届かない | 担当者が台帳を直接確認する朝のルーティンに切り替え | 通知設定修正後に再開 |
| 文字起こしが取れない | 会議メモを手書き・テキストメモで代替。議事録は手動作成 | 次回会議から再開 |
**内容ブロック②：代替運用は「誰でもできる」手順にする**
- GASを知らない担当者でも実行できる手順を書く
- 「Sheetsを開いて、A列のフォーム回答を確認して、B列の台帳へコピーする」レベルで書く
- 代替手順書は `配布資料/代替運用手順.pdf` として印刷・保存しておく
**内容ブロック③：業種別の代替運用例**
- ホテル: 予約フォームGAS停止時 → フロントが1時間ごとにフォーム回答を手動確認
- 製造業: 日報GAS停止時 → 現場スタッフがグループLINEで報告 → 事務担当が翌朝手動集計
Visible text candidates to use when useful, without reducing the source density: 代替運用の4パターン / 代替運用は「誰でもできる」手順にする / 業種別の代替運用例 / 障害ケース / 代替手順 / GASが止まった / 担当者がフォーム回答をSheetsで手動確認し、台帳に貼り付ける / Gemini連携が使えない / 通知メールが届かない / 担当者が台帳を直接確認する朝のルーティンに切り替え / 文字起こしが取れない / 会議メモを手書き・テキストメモで代替 / GASを知らない担当者でも実行できる手順を書く / ホテル / 製造業 / 誰でもできる.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-74-05-S42-1782901107.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S42.png' --marker '/tmp/gas-diagram-markers/worker-74-05-S42-1782901107.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S42.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-74 --task-id 05-S42 --claim-token a0e44e91-4eea-4e9e-9a44-4550e3e6a44e --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S42.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-74 --task-id 05-S42 --claim-token a0e44e91-4eea-4e9e-9a44-4550e3e6a44e --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
