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
  "slide_id": "S47",
  "title": "今日の振り返りと次アクション確認",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S47.png",
  "status": "claimed",
  "task_id": "06-S47",
  "worker": "worker-72",
  "claim_token": "37280a2f-186f-4a9f-8520-cc488f9ce5ff",
  "attempts": 1,
  "claimed_at": "2026-07-01T20:14:45+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782904485.115536
}
```

Diagram prompt block:
```markdown
## S47 今日の振り返りと次アクション確認

- セクション: 講座後の実践計画
- スライド側ヘッドライン（画像内には原則入れない）: 今日完成させた3つの成果物と次アクションを確認して講座を締めることで、学習から実践への橋渡しができる
- 推奨図解パターン: module-block
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S47 / 講座後の実践計画.
Slide topic for context: 今日の振り返りと次アクション確認.
Concept to visualize: 今日完成させた3つの成果物と次アクションを確認して講座を締めることで、学習から実践への橋渡しができる.
Suggested visual pattern: module-block.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: 今日完成させた3つの成果物と次アクションを確認して講座を締めることで、学習から実践への橋渡しができる
**内容ブロック①：今日完成させた3つの成果物の確認**
- 提案書骨子: 8セクションに自分の業務ケースが入っているか確認する
- KPI表: 測定項目・仮置き数値・測定方法・確認時期が入っているか確認する
- 次アクションメモ: 誰が・何を・いつまでにが3行入っているか確認する
**内容ブロック②：講座全体のまとめメッセージ**
- 「AIを使う」ことではなく「業務課題を解決する」ことが目的
- GAS・Gemini・Google Workspaceは「解決するための手段」
- 今日の骨子を持って、まず1つの業務で試してみてください
**内容ブロック③：保存・持ち帰りの確認**
- 演習データ・ワークシート・提案書骨子を自分のDriveフォルダに保存する
- 「全6回の成果物フォルダ」として1か所にまとめておく
- 次アクションメモを手帳・Tasksに転記して、実行管理に入れる
Visible text candidates to use when useful, without reducing the source density: 今日完成させた3つの成果物の確認 / 講座全体のまとめメッセージ / 保存・持ち帰りの確認 / 提案書骨子 / KPI表 / 次アクションメモ / 「AIを使う」ことではなく「業務課題を解決する」ことが目的 / 今日の骨子を持って、まず1つの業務で試してみてください / 「全6回の成果物フォルダ」として1か所にまとめておく / 次アクションメモを手帳・Tasksに転記して、実行管理に入れる / AIを使う / 業務課題を解決する / 解決するための手段 / 全6回の成果物フォルダ.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-72-06-S47-1782904485.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S47.png' --marker '/tmp/gas-diagram-markers/worker-72-06-S47-1782904485.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S47.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-72 --task-id 06-S47 --claim-token 37280a2f-186f-4a9f-8520-cc488f9ce5ff --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S47.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-72 --task-id 06-S47 --claim-token 37280a2f-186f-4a9f-8520-cc488f9ce5ff --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
