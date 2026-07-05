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
  "slide_id": "S19",
  "title": "Meet文字起こし活用を提案に含める",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S19.png",
  "status": "claimed",
  "task_id": "06-S19",
  "worker": "worker-78",
  "claim_token": "270bf111-8b19-4533-bef4-a32346f4b719",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:46:27+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782902787.721478
}
```

Diagram prompt block:
```markdown
## S19 Meet文字起こし活用を提案に含める

- セクション: プロトタイプと技術構成
- スライド側ヘッドライン（画像内には原則入れない）: Meet文字起こし→GAS→アクション台帳の流れを技術構成に含めることで、会議後のアクション管理も提案範囲に加えられる
- 推奨図解パターン: process-flow
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S19 / プロトタイプと技術構成.
Slide topic for context: Meet文字起こし活用を提案に含める.
Concept to visualize: Meet文字起こし→GAS→アクション台帳の流れを技術構成に含めることで、会議後のアクション管理も提案範囲に加えられる.
Suggested visual pattern: process-flow.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: Meet文字起こし→GAS→アクション台帳の流れを技術構成に含めることで、会議後のアクション管理も提案範囲に加えられる
**内容ブロック①：Meet文字起こし活用の技術構成**
1. MeetでAI文字起こしをON（Workspaceの有料プランで利用可能）
2. 会議終了後、Googleドキュメントとして指定フォルダに自動保存
3. GASが新規Docsを検出・本文を取得
4. Geminiが「アクション候補」「決定事項」「懸念点」を抽出（案）
5. アクション台帳（Sheets）に追記・担当者へ通知
**内容ブロック②：提案に含める場合の条件と注意事項**
- 条件: Google Workspace有料プランの確認（文字起こし機能の有無）
- 注意: 会議の録音・文字起こしに関する社内ポリシーの事前確認
- AI入力前: 発言者名の削除・個人情報の匿名化処理をGASで実施
**内容ブロック③：導入効果の書き方（控えめ・事実ベース）**
- NG: 「会議の生産性が50%向上します」（根拠なし）
- OK: 「アクション台帳への手動転記（1回あたり約15分）をGAS自動処理に置き換えることで、転記工数を削減できる見込みです（演習上の仮置き数値）」
Visible text candidates to use when useful, without reducing the source density: Meet文字起こし活用の技術構成 / 提案に含める場合の条件と注意事項 / 導入効果の書き方 / 条件 / 注意 / AI入力前 / NG / OK / アクション候補 / 決定事項 / 懸念点.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-78-06-S19-1782902787.marker`
2. After imagegen, copy from your own Codex session only. Use the UUID-like `session id` printed in this codex exec startup banner, for example `019f...`; do not use the timestamp-like id sometimes shown by the image tool. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S19.png' --marker '/tmp/gas-diagram-markers/worker-78-06-S19-1782902787.marker' --session-id <uuid-session-id-from-startup-banner> --expect-mime image/png --allow-latest-in-session`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S19.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-78 --task-id 06-S19 --claim-token 270bf111-8b19-4533-bef4-a32346f4b719 --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S19.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-78 --task-id 06-S19 --claim-token 270bf111-8b19-4533-bef4-a32346f4b719 --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
