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
  "session_no": "06",
  "session_dir": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成",
  "slide_id": "S29",
  "title": "リスクを先に書く（5カテゴリ）",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S29.png",
  "status": "claimed",
  "task_id": "06-S29",
  "worker": "worker-73",
  "claim_token": "68f13b81-6563-4c9f-896a-32eb4e28d691",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:56:18+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782903378.761526
}
```

Diagram prompt block:
```markdown
## S29 リスクを先に書く（5カテゴリ）

- セクション: リスク・運用・ロードマップ
- スライド側ヘッドライン（画像内には原則入れない）: リスクを「権限・通知漏れ・停止・教育・運用負荷」の5カテゴリで整理し、対策とセットで提案書に書くことで、承認者の不安を先取りして解消できる
- 推奨図解パターン: governance-risk
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S29 / リスク・運用・ロードマップ.
Slide topic for context: リスクを先に書く（5カテゴリ）.
Concept to visualize: リスクを「権限・通知漏れ・停止・教育・運用負荷」の5カテゴリで整理し、対策とセットで提案書に書くことで、承認者の不安を先取りして解消できる.
Suggested visual pattern: governance-risk.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: リスクを「権限・通知漏れ・停止・教育・運用負荷」の5カテゴリで整理し、対策とセットで提案書に書くことで、承認者の不安を先取りして解消できる
**内容ブロック①：リスクと対策の5カテゴリ**
| リスクカテゴリ | 具体的なリスク | 対策 |
|---|---|---|
| 権限 | 担当者変更時にスクリプト設定が引き継げない | 引き継ぎ設計書の整備・代替担当者の設定 |
| 通知漏れ | 担当者のメールアドレスが変わって通知が届かない | 通知先管理シートで一元管理・定期確認 |
| 停止 | GASがエラーで止まる | 実行ログ＋トリガー失敗通知の設定 |
| 教育 | 新しい担当者が操作を覚えられない | 操作手順書の整備・代替運用手順の紙保存 |
| 運用負荷 | ログ確認・エラー対応の作業が増える | 日次1分の確認ルーティン・月次30分の改善会議 |
**内容ブロック②：リスクの書き方で提案の印象が変わる**
- 「〇〇というリスクがあります」だけで終わる → 不安を増幅させる
- 「〇〇というリスクがあります。対策として〇〇を設計しています」と書く → 信頼感が増す
- 「対策で完全に防げます」とは書かない。「発生した場合の対応手順を整備しています」
**内容ブロック③：業種別のリスク例と対策**
- ホテル: 繁忙期にフォーム送信が急増してメール送信制限に達するリスク → 送信件数上限の事前確認・制限接近時の手動切り替え手順
- 士業: 顧客情報を誤ってGeminiに渡すリスク → 匿名化処理GASの設計と入力禁止情報チェックリストの整備
Visible text candidates to use when useful, without reducing the source density: リスクと対策の5カテゴリ / リスクの書き方で提案の印象が変わる / 業種別のリスク例と対策 / リスクカテゴリ / 具体的なリスク / 権限 / 担当者変更時にスクリプト設定が引き継げない / 通知漏れ / 担当者のメールアドレスが変わって通知が届かない / 停止 / GASがエラーで止まる / 教育 / 新しい担当者が操作を覚えられない / 運用負荷 / ログ確認・エラー対応の作業が増える / 「〇〇というリスクがあります」だけで終わる → 不安を増幅させる / 「〇〇というリスクがあります / 「対策で完全に防げます」とは書かない / ホテル / 士業.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-73-06-S29-1782903378.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S29.png' --marker '/tmp/gas-diagram-markers/worker-73-06-S29-1782903378.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S29.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-73 --task-id 06-S29 --claim-token 68f13b81-6563-4c9f-896a-32eb4e28d691 --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S29.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-73 --task-id 06-S29 --claim-token 68f13b81-6563-4c9f-896a-32eb4e28d691 --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
