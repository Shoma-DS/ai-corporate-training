You are worker-79, generating exactly one claimed GAS course diagram part.

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
  "slide_id": "S27",
  "title": "画面共有 ── 実演3「KPI表と効果試算の記入例を確認する」",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S27.png",
  "status": "claimed",
  "task_id": "06-S27",
  "worker": "worker-79",
  "claim_token": "b554c525-4b86-4912-a31e-615607cc7194",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:55:01+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782903301.642174
}
```

Diagram prompt block:
```markdown
## S27 画面共有 ── 実演3「KPI表と効果試算の記入例を確認する」

- セクション: KPIと効果試算
- スライド側ヘッドライン（画像内には原則入れない）: KPI表と効果試算の記入例を実際に見ることで、「控えめな数値の書き方」と「仮置きの明示の仕方」が具体的にわかる
- 推奨図解パターン: scene-environment
- 参照素材・スクリーンショット: `スクリーンショット/S27_KPI表記入例.png`（演習データSheetsの画面）

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S27 / KPIと効果試算.
Slide topic for context: 画面共有 ── 実演3「KPI表と効果試算の記入例を確認する」.
Concept to visualize: KPI表と効果試算の記入例を実際に見ることで、「控えめな数値の書き方」と「仮置きの明示の仕方」が具体的にわかる.
Suggested visual pattern: scene-environment.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: KPI表と効果試算の記入例を実際に見ることで、「控えめな数値の書き方」と「仮置きの明示の仕方」が具体的にわかる
**内容ブロック①：画面共有の流れ**
- 開くファイル: `演習データ/KPI表_効果試算_記入例.csv`（またはSheetsで開く）
- 確認する列: 測定項目・仮置き数値・測定方法・確認時期・前提条件の注記
- 注目ポイント: 全数値に「演習上の仮置き数値」と注記されている
**内容ブロック②：見せるポイント**
- 「月○時間削減」の根拠（現状工数の確認方法）がKPI表に書かれていることを強調
- 効果試算に「実装コスト・教育コスト」も含まれている行を見せる
Visible text candidates to use when useful, without reducing the source density: 画面共有の流れ / 見せるポイント / 開くファイル / 確認する列 / 注目ポイント / 「月○時間削減」の根拠がKPI表に書かれていることを強調 / 効果試算に「実装コスト・教育コスト」も含まれている行を見せる / 控えめな数値の書き方 / 仮置きの明示の仕方 / 演習上の仮置き数値 / 月○時間削減 / 実装コスト・教育コスト.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-79-06-S27-1782903301.marker`
2. After imagegen, copy from your own Codex session only. Use the UUID-like `session id` printed in this codex exec startup banner, for example `019f...`; do not use the timestamp-like id sometimes shown by the image tool. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S27.png' --marker '/tmp/gas-diagram-markers/worker-79-06-S27-1782903301.marker' --session-id <uuid-session-id-from-startup-banner> --expect-mime image/png --allow-latest-in-session`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S27.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-79 --task-id 06-S27 --claim-token b554c525-4b86-4912-a31e-615607cc7194 --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S27.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-79 --task-id 06-S27 --claim-token b554c525-4b86-4912-a31e-615607cc7194 --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
