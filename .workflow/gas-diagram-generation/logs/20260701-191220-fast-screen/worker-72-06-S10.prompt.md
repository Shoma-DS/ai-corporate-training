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
  "slide_id": "S10",
  "title": "As-Isを業務の流れで描く",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S10.png",
  "status": "claimed",
  "task_id": "06-S10",
  "worker": "worker-72",
  "claim_token": "c46cb104-20bd-414b-9a64-7fb3371f0f2b",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:32:32+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782901952.749845
}
```

Diagram prompt block:
```markdown
## S10 As-Isを業務の流れで描く

- セクション: 課題整理とユースケース選定
- スライド側ヘッドライン（画像内には原則入れない）: 現状の業務フローを「入力→処理→確認→保存→通知」の5ステップで描くことで、どこに問題があるかが一目でわかる
- 推奨図解パターン: process-flow
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S10 / 課題整理とユースケース選定.
Slide topic for context: As-Isを業務の流れで描く.
Concept to visualize: 現状の業務フローを「入力→処理→確認→保存→通知」の5ステップで描くことで、どこに問題があるかが一目でわかる.
Suggested visual pattern: process-flow.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: 現状の業務フローを「入力→処理→確認→保存→通知」の5ステップで描くことで、どこに問題があるかが一目でわかる
**内容ブロック①：As-Isフローの5ステップ**
| ステップ | 現状（As-Is）の例 | 問題点 |
|---|---|---|
| 入力 | 顧客がメールで問い合わせを送る | 件名・内容の書き方がバラバラ |
| 処理 | 担当者が1件ずつメールを読んで管理表にコピー | 手作業で属人化・時間がかかる |
| 確認 | 担当者が表を目視して対応漏れを探す | 件数が多いと見落としが発生 |
| 保存 | 担当者のローカルExcelに保存 | 他の人が見られない・バックアップなし |
| 通知 | 対応が必要な場合は担当者が口頭またはメールで個別連絡 | 通知が遅れる・漏れる |
**内容ブロック②：As-Isフローの描き方のコツ**
- 「誰が」「何を使って」「何をするか」を各ステップに書く
- 時間・件数・頻度を数字で入れると課題の重さが伝わりやすい
- 使っているツール（Excel・メール・紙・口頭）を明示する
**内容ブロック③：業種別As-Isフロー例（問い合わせ対応）**
- 士業: メール受信（Gmail）→担当者が手動でExcelに転記（約10分/件）→口頭で上司に報告→Excelを保存して閉じる→対応漏れは翌週の会議で発覚
- 小売業: 電話で在庫問い合わせ受信→担当者が手書きメモ→翌日Excelに転記→管理者に口頭報告→ファイルをメールで共有（最新版が誰のパソコンにあるか不明）
Visible text candidates to use when useful, without reducing the source density: As-Isフローの5ステップ / As-Isフローの描き方のコツ / 業種別As-Isフロー例 / 現状の例 / 入力 / 顧客がメールで問い合わせを送る / 処理 / 担当者が1件ずつメールを読んで管理表にコピー / 確認 / 担当者が表を目視して対応漏れを探す / 保存 / 担当者のローカルExcelに保存 / 通知 / 対応が必要な場合は担当者が口頭またはメールで個別連絡 / 「誰が」「何を使って」「何をするか」を各ステップに書く / 時間・件数・頻度を数字で入れると課題の重さが伝わりやすい / 使っているツールを明示する / 士業 / 小売業 / 入力→処理→確認→保存→通知.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-72-06-S10-1782901952.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S10.png' --marker '/tmp/gas-diagram-markers/worker-72-06-S10-1782901952.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S10.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-72 --task-id 06-S10 --claim-token c46cb104-20bd-414b-9a64-7fb3371f0f2b --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S10.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-72 --task-id 06-S10 --claim-token c46cb104-20bd-414b-9a64-7fb3371f0f2b --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
