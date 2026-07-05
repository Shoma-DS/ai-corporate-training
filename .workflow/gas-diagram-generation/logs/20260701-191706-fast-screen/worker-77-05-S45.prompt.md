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
  "slide_id": "S45",
  "title": "演習: 運用設計書とリスクチェックリストを作る",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S45.png",
  "status": "claimed",
  "task_id": "05-S45",
  "worker": "worker-77",
  "claim_token": "baec0a15-716c-4e70-b419-97a7365da541",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:23:19+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782901399.6540601
}
```

Diagram prompt block:
```markdown
## S45 演習: 運用設計書とリスクチェックリストを作る

- セクション: 演習と次回接続
- スライド側ヘッドライン（画像内には原則入れない）: ワークシートを使って運用設計書とリスクチェックリストを完成させることで、自社業務への適用準備が整う
- 推奨図解パターン: checklist-confirmation
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第5回 AI/GAS自動化の要件定義・運用設計 / S45 / 演習と次回接続.
Slide topic for context: 演習: 運用設計書とリスクチェックリストを作る.
Concept to visualize: ワークシートを使って運用設計書とリスクチェックリストを完成させることで、自社業務への適用準備が整う.
Suggested visual pattern: checklist-confirmation.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: ワークシートを使って運用設計書とリスクチェックリストを完成させることで、自社業務への適用準備が整う
**内容ブロック①：演習の手順**
- 動画を一時停止して20分取り組んでください
- 使うファイル: `ワークシート.md`（または配布資料の運用設計書テンプレート）
- 参照ファイル: 演習データ `要件定義ケース_問い合わせ通知.csv`・`権限保存設計サンプル.csv`
**内容ブロック②：作成する成果物と記入欄**
| 成果物 | 記入する内容 |
|---|---|
| 運用設計書 | 対象業務1文・処理フロー5ステップ・役割表・代替運用手順 |
| リスクチェックリスト | AI入力禁止情報の明示・権限設計・GAS制限への対策・テストケース |
| 引き継ぎ設計書（骨子） | 担当者・設定ファイルの場所・よくあるエラーの記録欄 |
**内容ブロック③：自己レビューの3観点**
1. 非対象範囲（外部送信・承認・個人情報含む処理）を明示したか
2. 代替運用手順が「GASを知らない担当者でも読める」レベルで書かれているか
3. リスクチェックリストの全項目に○/×/該当なしを記入したか
**内容ブロック④：確認ポイント（動画再開後）**
- 対象業務の1文が「誰の・どの業務を・何のために・除外範囲は何か」を含んでいるか
- 実行ログの6列（実行日時・処理件数・成功件数・エラー件数・エラー内容・備考）が設計に入っているか
- 代替運用手順が最低1つ書かれているか
Visible text candidates to use when useful, without reducing the source density: 演習の手順 / 作成する成果物と記入欄 / 自己レビューの3観点 / 確認ポイント / 動画を一時停止して20分取り組んでください / 使うファイル / 参照ファイル / 記入する内容 / 運用設計書 / 対象業務1文・処理フロー5ステップ・役割表・代替運用手順 / リスクチェックリスト / AI入力禁止情報の明示・権限設計・GAS制限への対策・テストケース / 引き継ぎ設計書 / 担当者・設定ファイルの場所・よくあるエラーの記録欄 / 実行ログの6列が設計に入っているか / 代替運用手順が最低1つ書かれているか.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-77-05-S45-1782901399.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S45.png' --marker '/tmp/gas-diagram-markers/worker-77-05-S45-1782901399.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S45.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-77 --task-id 05-S45 --claim-token baec0a15-716c-4e70-b419-97a7365da541 --target '講座/生成AI・GASで実践する業務変革・DX推進講座/05-AI-GAS自動化の要件定義-運用設計/図解パーツ/S45.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-77 --task-id 05-S45 --claim-token baec0a15-716c-4e70-b419-97a7365da541 --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
