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
  "slide_id": "S21",
  "title": "画面共有 ── 実演2「プロトタイプ構成を確認する」",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S21.png",
  "status": "claimed",
  "task_id": "06-S21",
  "worker": "worker-73",
  "claim_token": "82cbf5a1-8bce-40b4-96a7-19a750df5fd6",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:48:30+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782902910.813329
}
```

Diagram prompt block:
```markdown
## S21 画面共有 ── 実演2「プロトタイプ構成を確認する」

- セクション: プロトタイプと技術構成
- スライド側ヘッドライン（画像内には原則入れない）: フォーム・台帳・ログ・Meetサンプルの4点セットを実際に見ることで、プロトタイプとして提案書に使える素材の完成度がわかる
- 推奨図解パターン: scene-environment
- 参照素材・スクリーンショット: `スクリーンショット/S21_プロトタイプ構成.png`（台帳とログシートの画面）

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S21 / プロトタイプと技術構成.
Slide topic for context: 画面共有 ── 実演2「プロトタイプ構成を確認する」.
Concept to visualize: フォーム・台帳・ログ・Meetサンプルの4点セットを実際に見ることで、プロトタイプとして提案書に使える素材の完成度がわかる.
Suggested visual pattern: scene-environment.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: フォーム・台帳・ログ・Meetサンプルの4点セットを実際に見ることで、プロトタイプとして提案書に使える素材の完成度がわかる
**内容ブロック①：画面共有の流れ**
- 開くファイル①: フォームの回答画面（ダミーデータ入力済み）
- 開くファイル②: Sheets台帳（転記結果・AI分類案列・確認済みフラグ列）
- 開くファイル③: 実行ログシート（実行日時・処理件数・成功件数・エラー件数）
- 開くファイル④: `演習データ/Meet文字起こし入力サンプル.md`（アクション台帳との対応）
**内容ブロック②：見せるポイント**
- 台帳の「AI分類案」列と「確認済み」列の役割の違い（人が確認してから次の処理へ）
- 実行ログの「エラー件数」列が0であることを「安定動作の証拠」として示せることを強調
Visible text candidates to use when useful, without reducing the source density: 画面共有の流れ / 見せるポイント / 開くファイル① / 開くファイル② / 開くファイル③ / 開くファイル④ / 台帳の「AI分類案」列と「確認済み」列の役割の違い / プロトタイプ構成を確認する / AI分類案 / 確認済み / エラー件数 / 安定動作の証拠.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-73-06-S21-1782902910.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S21.png' --marker '/tmp/gas-diagram-markers/worker-73-06-S21-1782902910.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S21.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-73 --task-id 06-S21 --claim-token 82cbf5a1-8bce-40b4-96a7-19a750df5fd6 --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S21.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-73 --task-id 06-S21 --claim-token 82cbf5a1-8bce-40b4-96a7-19a750df5fd6 --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
