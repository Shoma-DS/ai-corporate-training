You are worker-77, generating exactly one claimed GAS course diagram part.

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
  "slide_id": "S39",
  "title": "テスト観点6つ",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S39.png",
  "status": "claimed",
  "task_id": "05-S39",
  "worker": "worker-77",
  "claim_token": "4d57dcb2-dfdb-410e-9225-8ec248df2144",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:17:16+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782901036.250148
}
```

Diagram prompt block:
```markdown
## S39 テスト観点6つ

- セクション: ログ・テスト・復旧
- スライド側ヘッドライン（画像内には原則入れない）: 正常系・空欄・重複・AI誤分類・権限ミス・通知漏れの6観点でテストすることで、本番稼働後の想定外エラーが激減する
- 推奨図解パターン: checklist-confirmation
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第5回 AI/GAS自動化の要件定義・運用設計 / S39 / ログ・テスト・復旧.
Slide topic for context: テスト観点6つ.
Concept to visualize: 正常系・空欄・重複・AI誤分類・権限ミス・通知漏れの6観点でテストすることで、本番稼働後の想定外エラーが激減する.
Suggested visual pattern: checklist-confirmation.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: 正常系・空欄・重複・AI誤分類・権限ミス・通知漏れの6観点でテストすることで、本番稼働後の想定外エラーが激減する
**内容ブロック①：テスト観点6つと確認方法**
| 観点 | テスト内容 | 期待される動作 |
|---|---|---|
| 正常系 | 通常の入力をフォームから送信する | 転記・通知が正常に実行される |
| 空欄 | 必須でない項目を空欄にして送信する | エラーなく処理され、ログに「空欄スキップ」が記録される |
| 重複 | 同じ内容を2回送信する | 2件目に「重複フラグ」が立ちダブり通知が送られない |
| AI誤分類 | 境界的・曖昧な入力を送信する | 「不明」カテゴリに分類され、要確認フラグが立つ |
| 権限ミス | 閲覧者権限のアカウントでGASを実行する | 権限エラーが記録され、処理が止まらず管理者に通知が届く |
| 通知漏れ | 担当者のメールアドレスを変更してから送信する | 旧アドレスに通知が送られず、エラーログに記録される |
**内容ブロック②：テストデータの作り方（ダミーデータ原則）**
- テストには必ずダミーデータを使う。実際の顧客名・メールアドレスは使わない
- ダミーデータの命名例: 顧客名「架空山 テスト男」、メール「test-dummy@example.com」
**内容ブロック③：テスト結果の記録**
- テストケースごとに「実行日・入力内容・期待動作・実際の動作・合否」を記録する
- 「テストケースサンプル.csv」に記入して演習で提出する（S45演習で使用）
Visible text candidates to use when useful, without reducing the source density: テスト観点6つと確認方法 / テストデータの作り方 / テスト結果の記録 / 観点 / テスト内容 / 正常系 / 通常の入力をフォームから送信する / 空欄 / 必須でない項目を空欄にして送信する / 重複 / 同じ内容を2回送信する / AI誤分類 / 境界的・曖昧な入力を送信する / 権限ミス / 閲覧者権限のアカウントでGASを実行する / 通知漏れ / 担当者のメールアドレスを変更してから送信する / テストには必ずダミーデータを使う / ダミーデータの命名例 / 「テストケースサンプル.csv」に記入して演習で提出する.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-77-05-S39-1782901036.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S39.png' --marker '/tmp/gas-diagram-markers/worker-77-05-S39-1782901036.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S39.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-77 --task-id 05-S39 --claim-token 4d57dcb2-dfdb-410e-9225-8ec248df2144 --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S39.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-77 --task-id 05-S39 --claim-token 4d57dcb2-dfdb-410e-9225-8ec248df2144 --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
