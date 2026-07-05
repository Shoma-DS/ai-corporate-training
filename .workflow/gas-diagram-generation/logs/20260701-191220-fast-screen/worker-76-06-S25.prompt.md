You are worker-76, generating exactly one claimed GAS course diagram part.

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
  "slide_id": "S25",
  "title": "AI活用の効果はどう測るか",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S25.png",
  "status": "claimed",
  "task_id": "06-S25",
  "worker": "worker-76",
  "claim_token": "7e9ca4dc-2110-41eb-a46d-1f6daef7a316",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:53:05+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782903185.403708
}
```

Diagram prompt block:
```markdown
## S25 AI活用の効果はどう測るか

- セクション: KPIと効果試算
- スライド側ヘッドライン（画像内には原則入れない）: AI活用の効果は「分類一致率・確認時間の変化・再利用率」で測ることで、「AIを入れた効果」を具体的に説明できる
- 推奨図解パターン: checklist-confirmation
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S25 / KPIと効果試算.
Slide topic for context: AI活用の効果はどう測るか.
Concept to visualize: AI活用の効果は「分類一致率・確認時間の変化・再利用率」で測ることで、「AIを入れた効果」を具体的に説明できる.
Suggested visual pattern: checklist-confirmation.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: AI活用の効果は「分類一致率・確認時間の変化・再利用率」で測ることで、「AIを入れた効果」を具体的に説明できる
**内容ブロック①：AI活用効果の測定指標**
| 指標 | 測り方 | 目標（仮置き） |
|---|---|---|
| 分類一致率 | AI分類案と確認者の最終分類が一致した割合 | 80%以上（確認者の修正負荷が低い状態） |
| 確認時間の変化 | AI分類なし→あり での確認作業時間の差 | 確認時間が50%以下に（試算） |
| 下書き再利用率 | Geminiが作成した下書きをそのまま使用した割合 | 60%以上（大幅修正が必要な案の割合が低い） |
| 要確認フラグ発生率 | 全件に対して「AI不明」フラグが立った割合 | 10%以内（安定運用の目安） |
**内容ブロック②：AI効果の測定データはSheetsから取る**
- 台帳の「AI分類案」列と「確認済み」列の差分を毎月集計する
- GAS実行ログの「成功件数」「エラー件数」から成功率を算出する
- これらを「月次AI効果レポート」としてSheetsのピボットで可視化する
**内容ブロック③：「AIの効果が出ない」場合の対処**
- 分類一致率が低い → プロンプト（Gemの指示文）を修正する
- 要確認フラグが多い → フォームの選択肢設計を見直す（入力のバラつきを減らす）
- 下書き再利用率が低い → プロンプトに業種・業務特有の言葉を追加する
Visible text candidates to use when useful, without reducing the source density: AI活用効果の測定指標 / AI効果の測定データはSheetsから取る / 「AIの効果が出ない」場合の対処 / 指標 / 測り方 / 分類一致率 / AI分類案と確認者の最終分類が一致した割合 / 確認時間の変化 / AI分類なし→あり での確認作業時間の差 / 下書き再利用率 / Geminiが作成した下書きをそのまま使用した割合 / 要確認フラグ発生率 / 全件に対して「AI不明」フラグが立った割合 / 台帳の「AI分類案」列と「確認済み」列の差分を毎月集計する / GAS実行ログの「成功件数」「エラー件数」から成功率を算出する / 分類一致率が低い → プロンプトを修正する / 要確認フラグが多い → フォームの選択肢設計を見直す / 下書き再利用率が低い → プロンプトに業種・業務特有の言葉を追加する / AIを入れた効果 / AI不明.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-76-06-S25-1782903185.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S25.png' --marker '/tmp/gas-diagram-markers/worker-76-06-S25-1782903185.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S25.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-76 --task-id 06-S25 --claim-token 7e9ca4dc-2110-41eb-a46d-1f6daef7a316 --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S25.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-76 --task-id 06-S25 --claim-token 7e9ca4dc-2110-41eb-a46d-1f6daef7a316 --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
