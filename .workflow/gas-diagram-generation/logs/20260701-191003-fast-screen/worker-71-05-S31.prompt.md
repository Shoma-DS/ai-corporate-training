You are worker-71, generating exactly one claimed GAS course diagram part.

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
  "slide_id": "S31",
  "title": "権限は閲覧と編集を分ける",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S31.png",
  "status": "claimed",
  "task_id": "05-S31",
  "worker": "worker-71",
  "claim_token": "73131d0b-31d3-4704-9129-7a66ae3cf34d",
  "attempts": 4,
  "claimed_at": "2026-07-01T19:10:11+0900",
  "completed_at": null,
  "failed_at": "2026-07-01T19:08:35+0900",
  "note": null,
  "claimed_at_epoch": 1782900611.202862
}
```

Diagram prompt block:
```markdown
## S31 権限は閲覧と編集を分ける

- セクション: 権限・制限・情報管理
- スライド側ヘッドライン（画像内には原則入れない）: 閲覧者・編集者・管理者・外部共有禁止の4段階を設計することで、情報漏洩と誤操作のリスクを同時に下げられる
- 推奨図解パターン: matrix-classification
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第5回 AI/GAS自動化の要件定義・運用設計 / S31 / 権限・制限・情報管理.
Slide topic for context: 権限は閲覧と編集を分ける.
Concept to visualize: 閲覧者・編集者・管理者・外部共有禁止の4段階を設計することで、情報漏洩と誤操作のリスクを同時に下げられる.
Suggested visual pattern: matrix-classification.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: 閲覧者・編集者・管理者・外部共有禁止の4段階を設計することで、情報漏洩と誤操作のリスクを同時に下げられる
**内容ブロック①：4段階の権限設計**
| 権限レベル | 誰が持つか | できること | できないこと |
|---|---|---|---|
| 管理者 | 1名（＋代替1名） | すべての操作・スクリプト設定 | - |
| 編集者 | 確認担当者・事務担当 | 台帳の入力・確認列へのチェック | スクリプト設定変更 |
| 閲覧者 | 上司・報告受け手 | データを読む | データ変更・スクリプト操作 |
| 外部共有禁止 | ログ・設定シート・APIキー管理シート | （設定なし） | 誰も外部共有できない |
**内容ブロック②：権限設定でよくあるミス**
- 台帳を「リンクを知っている人全員が編集可」で共有してしまう
- GASのスクリプト本体に編集権限が誰でも入れる状態になっている
- 外部の業者や顧客を「編集者」として追加してしまう
**内容ブロック③：権限設計テンプレートの活用**
- 演習データ `権限保存設計サンプル.csv` に列構成あり
- 確認する項目: ファイル名・閲覧者・編集者・外部共有可否・ログ閲覧権限
Visible text candidates to use when useful, without reducing the source density: 4段階の権限設計 / 権限設定でよくあるミス / 権限設計テンプレートの活用 / 権限レベル / 誰が持つか / 管理者 / 1名 / 編集者 / 確認担当者・事務担当 / 閲覧者 / 上司・報告受け手 / 外部共有禁止 / ログ・設定シート・APIキー管理シート / 台帳を「リンクを知っている人全員が編集可」で共有してしまう / GASのスクリプト本体に編集権限が誰でも入れる状態になっている / 外部の業者や顧客を「編集者」として追加してしまう / 演習データ 権限保存設計サンプル.csv に列構成あり / 確認する項目.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-71-05-S31-1782900611.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S31.png' --marker '/tmp/gas-diagram-markers/worker-71-05-S31-1782900611.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S31.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-71 --task-id 05-S31 --claim-token 73131d0b-31d3-4704-9129-7a66ae3cf34d --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S31.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-71 --task-id 05-S31 --claim-token 73131d0b-31d3-4704-9129-7a66ae3cf34d --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
