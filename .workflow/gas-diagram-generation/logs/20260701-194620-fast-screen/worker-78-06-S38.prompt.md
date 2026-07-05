You are worker-78, generating exactly one claimed GAS course diagram part.

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
  "slide_id": "S38",
  "title": "演習: 提案書骨子・KPI表・次アクションメモを完成させる",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S38.png",
  "status": "claimed",
  "task_id": "06-S38",
  "worker": "worker-78",
  "claim_token": "142aa218-9a38-4d35-83c4-8f082f4fc6c7",
  "attempts": 1,
  "claimed_at": "2026-07-01T20:08:53+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782904133.5592241
}
```

Diagram prompt block:
```markdown
## S38 演習: 提案書骨子・KPI表・次アクションメモを完成させる

- セクション: 提案書骨子の作成と自己レビュー
- スライド側ヘッドライン（画像内には原則入れない）: ワークシートに記入することで、今日中に「上司に見せられる提案書骨子」が完成する
- 推奨図解パターン: checklist-confirmation
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S38 / 提案書骨子の作成と自己レビュー.
Slide topic for context: 演習: 提案書骨子・KPI表・次アクションメモを完成させる.
Concept to visualize: ワークシートに記入することで、今日中に「上司に見せられる提案書骨子」が完成する.
Suggested visual pattern: checklist-confirmation.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: ワークシートに記入することで、今日中に「上司に見せられる提案書骨子」が完成する
**内容ブロック①：演習の手順（動画を一時停止して20分取り組んでください）**
1. 使うファイル: `ワークシート.md` の提案書骨子テンプレート
2. 参照ファイル: `演習データ/提案書骨子_記入例.md`・`KPI表_効果試算_記入例.csv`
3. 記入する順番: ①課題（3つ）→ ②As-Is → ③To-Be → ④Gap解決策 → ⑤KPI → ⑥技術構成 → ⑦リスク・非対象 → ⑧次アクション
**内容ブロック②：KPI表の記入手順**
1. 削減したい作業を1つ選ぶ
2. 現状の工数を「1件あたり○分×月○件=月○分」で計算する
3. GAS自動化後の見込み工数を「1件あたり○秒×月○件=月○分」で計算する
4. 差分を「削減見込み（演習上の仮置き数値）」として記入する
5. 測定方法・確認時期を記入する
**内容ブロック③：次アクションメモの3行記入**
| アクション番号 | 誰が | 何を | いつまでに |
|---|---|---|---|
| アクション① | 自分 | 上司に3分版で概要を説明する | 今月末 |
| アクション② | 自分 | 技術担当者にGASの動作環境を確認する | 2週間以内 |
| アクション③ | 自分 | ワークシートを10分版提案書に書き直す | 来月上旬 |
Visible text candidates to use when useful, without reducing the source density: 演習の手順 / KPI表の記入手順 / 次アクションメモの3行記入 / アクション番号 / 誰が / アクション① / 自分 / アクション② / アクション③ / 上司に見せられる提案書骨子.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-78-06-S38-1782904133.marker`
2. After imagegen, copy from your own Codex session only. Use the UUID-like `session id` printed in this codex exec startup banner, for example `019f...`; do not use the timestamp-like id sometimes shown by the image tool. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S38.png' --marker '/tmp/gas-diagram-markers/worker-78-06-S38-1782904133.marker' --session-id <uuid-session-id-from-startup-banner> --expect-mime image/png --allow-latest-in-session`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S38.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-78 --task-id 06-S38 --claim-token 142aa218-9a38-4d35-83c4-8f082f4fc6c7 --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S38.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-78 --task-id 06-S38 --claim-token 142aa218-9a38-4d35-83c4-8f082f4fc6c7 --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
