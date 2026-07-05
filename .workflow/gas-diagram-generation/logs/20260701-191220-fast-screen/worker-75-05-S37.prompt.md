You are worker-75, generating exactly one claimed GAS course diagram part.

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
  "slide_id": "S37",
  "title": "ログは「守るため」に書く",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S37.png",
  "status": "claimed",
  "task_id": "05-S37",
  "worker": "worker-75",
  "claim_token": "740a4d93-7579-41ce-810a-73d359776aad",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:12:36+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782900756.8892212
}
```

Diagram prompt block:
```markdown
## S37 ログは「守るため」に書く

- セクション: ログ・テスト・復旧
- スライド側ヘッドライン（画像内には原則入れない）: 実行ログをSheetsに記録することで、「いつ・何件・成功/失敗」が後から追えるようになり、問題の早期発見と原因調査が速くなる
- 推奨図解パターン: data-insight
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第5回 AI/GAS自動化の要件定義・運用設計 / S37 / ログ・テスト・復旧.
Slide topic for context: ログは「守るため」に書く.
Concept to visualize: 実行ログをSheetsに記録することで、「いつ・何件・成功/失敗」が後から追えるようになり、問題の早期発見と原因調査が速くなる.
Suggested visual pattern: data-insight.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: 実行ログをSheetsに記録することで、「いつ・何件・成功/失敗」が後から追えるようになり、問題の早期発見と原因調査が速くなる
**内容ブロック①：実行ログに必ず含める6列**
| 列名 | 記録する内容 | 例 |
|---|---|---|
| 実行日時 | タイムスタンプ | 2026-06-04 09:00:00 |
| 処理件数 | 今回処理した行数 | 12件 |
| 成功件数 | 正常に処理できた件数 | 11件 |
| エラー件数 | エラーになった件数 | 1件 |
| エラー内容 | エラーメッセージ（先頭100文字） | TypeError: Cannot read… |
| 備考 | 手動実行・スキップ理由など | 手動実行（テスト） |
**内容ブロック②：ログから読み取れるサイン**
- 処理件数が急に0になった → 入力元のフォームかシートの設定が変わった可能性
- エラー件数が増えている → 想定外の入力が増えている（例外処理の見直しが必要）
- 実行時間が伸びている → データ件数が増えてきた（処理分割の検討タイミング）
**内容ブロック③：ログ確認の運用ルール（定着のために）**
- 毎朝1分: 実行ログの「エラー件数」列を目視確認
- 週次: 処理件数の推移を確認し、急増・急減がないか確認
- 月次: エラー内容の集計から「繰り返し起きるエラー」を特定して設計改善
Visible text candidates to use when useful, without reducing the source density: 実行ログに必ず含める6列 / ログから読み取れるサイン / ログ確認の運用ルール / 記録する内容 / 実行日時 / タイムスタンプ / 処理件数 / 今回処理した行数 / 成功件数 / 正常に処理できた件数 / エラー件数 / エラーになった件数 / エラー内容 / エラーメッセージ / 備考 / 手動実行・スキップ理由など / エラー件数が増えている → 想定外の入力が増えている / 実行時間が伸びている → データ件数が増えてきた / 毎朝1分 / 週次.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-75-05-S37-1782900757.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S37.png' --marker '/tmp/gas-diagram-markers/worker-75-05-S37-1782900757.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S37.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-75 --task-id 05-S37 --claim-token 740a4d93-7579-41ce-810a-73d359776aad --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S37.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-75 --task-id 05-S37 --claim-token 740a4d93-7579-41ce-810a-73d359776aad --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
