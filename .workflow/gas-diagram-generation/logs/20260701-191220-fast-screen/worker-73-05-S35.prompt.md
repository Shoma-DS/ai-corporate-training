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
  "slide_id": "S35",
  "title": "スコープ（権限）とセキュリティ設定",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S35.png",
  "status": "claimed",
  "task_id": "05-S35",
  "worker": "worker-73",
  "claim_token": "181b854c-67f7-4105-b2b9-04ca40cb8410",
  "attempts": 2,
  "claimed_at": "2026-07-01T19:12:30+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782900750.613655
}
```

Diagram prompt block:
```markdown
## S35 スコープ（権限）とセキュリティ設定

- セクション: 権限・制限・情報管理
- スライド側ヘッドライン（画像内には原則入れない）: GASが要求するスコープ（権限）を最小限にすることで、スクリプトによる意図しないデータアクセスのリスクが下がる
- 推奨図解パターン: governance-risk
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第5回 AI/GAS自動化の要件定義・運用設計 / S35 / 権限・制限・情報管理.
Slide topic for context: スコープ（権限）とセキュリティ設定.
Concept to visualize: GASが要求するスコープ（権限）を最小限にすることで、スクリプトによる意図しないデータアクセスのリスクが下がる.
Suggested visual pattern: governance-risk.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: GASが要求するスコープ（権限）を最小限にすることで、スクリプトによる意図しないデータアクセスのリスクが下がる
**内容ブロック①：よく使うスコープと必要な理由**
| スコープ | 用途 | 最小化のポイント |
|---|---|---|
| spreadsheets（読み書き） | 台帳への転記・ログ書き込み | 読み取り専用でよい処理は `readonly` スコープを使う |
| gmail（送信） | 通知メール送信 | `gmail.send` のみ。メール読み取りは不要なら要求しない |
| drive（ファイル操作） | Docs生成・Drive保存 | `drive.file`（GASが作成したファイルのみ）を使う |
| forms（回答取得） | フォーム回答の取得 | `forms.responses.readonly` のみ |
**内容ブロック②：スコープ設定の確認場所**
- GASエディタ > 左サイドバー「サービス」で追加したスコープを確認
- 「OAuth同意画面」に表示されるスコープが適切かを管理者が確認する
- 第三者が作成したGASスクリプトを使う場合は、要求スコープを特に慎重に確認する
**内容ブロック③：スコープの「いつか使うかも」は禁止**
- 必要になってから追加する。使わないスコープを事前に要求しない
- 特に「Drive全体の読み書き」を要求するスクリプトは慎重に扱う
- 組織内で共有するGASは、管理者が要求スコープをレビューしてから展開する
Visible text candidates to use when useful, without reducing the source density: よく使うスコープと必要な理由 / スコープ設定の確認場所 / スコープの「いつか使うかも」は禁止 / スコープ / 用途 / spreadsheets / 台帳への転記・ログ書き込み / gmail / 通知メール送信 / drive / Docs生成・Drive保存 / forms / フォーム回答の取得 / GASエディタ > 左サイドバー「サービス」で追加したスコープを確認 / 「OAuth同意画面」に表示されるスコープが適切かを管理者が確認する / 必要になってから追加する / 特に「Drive全体の読み書き」を要求するスクリプトは慎重に扱う / サービス / OAuth同意画面 / いつか使うかも.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-73-05-S35-1782900750.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S35.png' --marker '/tmp/gas-diagram-markers/worker-73-05-S35-1782900750.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S35.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-73 --task-id 05-S35 --claim-token 181b854c-67f7-4105-b2b9-04ca40cb8410 --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S35.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-73 --task-id 05-S35 --claim-token 181b854c-67f7-4105-b2b9-04ca40cb8410 --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
