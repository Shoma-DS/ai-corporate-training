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
  "slide_id": "S13",
  "title": "非対象範囲を先に書く",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S13.png",
  "status": "claimed",
  "task_id": "06-S13",
  "worker": "worker-76",
  "claim_token": "e69e5a8b-0320-4d07-ac2a-8b72d3d46a9f",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:39:52+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782902392.143799
}
```

Diagram prompt block:
```markdown
## S13 非対象範囲を先に書く

- セクション: 課題整理とユースケース選定
- スライド側ヘッドライン（画像内には原則入れない）: 「今回やらないこと」を提案書に明示することで、スコープの誤解・後から増える要求・過剰な期待を防げる
- 推奨図解パターン: governance-risk
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S13 / 課題整理とユースケース選定.
Slide topic for context: 非対象範囲を先に書く.
Concept to visualize: 「今回やらないこと」を提案書に明示することで、スコープの誤解・後から増える要求・過剰な期待を防げる.
Suggested visual pattern: governance-risk.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: 「今回やらないこと」を提案書に明示することで、スコープの誤解・後から増える要求・過剰な期待を防げる
**内容ブロック①：非対象範囲として明示すべき5カテゴリ**
| カテゴリ | 非対象例 |
|---|---|
| 外部送信 | 顧客へのメール返信の自動送信（人が確認してから送信） |
| 承認・決裁フロー | 稟議・契約・支払いの承認 |
| 個人情報を含む処理 | AIへの個人情報入力・個人情報を含むファイルの自動処理 |
| 他システム連携 | 既存の会計ソフト・ERPシステムへの自動連携 |
| 未確認機能 | 有料プランが必要な機能（事前確認が必要） |
**内容ブロック②：「非対象範囲」は提案書の信頼を高める**
- 「全部できます」と言う提案書より「ここまでできて、ここはスコープ外」と言う提案書の方が信頼される
- 非対象範囲は「今回やらない」であって「永遠にやらない」ではない
- 「第2フェーズの拡張候補」として将来の余地を残す
**内容ブロック③：非対象範囲の書き方例（箇条書き）**
- 今回の対象外: 顧客への返信メールの自動送信（人が確認・送信）
- 今回の対象外: 既存の販売管理システムとの直接連携
- 今回の対象外: モバイルアプリからの操作・入力
- 将来の拡張候補: Gemini APIによる分類精度の向上（Workspace有料プランで確認後）
Visible text candidates to use when useful, without reducing the source density: 非対象範囲として明示すべき5カテゴリ / 「非対象範囲」は提案書の信頼を高める / 非対象範囲の書き方例 / カテゴリ / 非対象例 / 外部送信 / 顧客へのメール返信の自動送信 / 承認・決裁フロー / 稟議・契約・支払いの承認 / 個人情報を含む処理 / AIへの個人情報入力・個人情報を含むファイルの自動処理 / 他システム連携 / 既存の会計ソフト・ERPシステムへの自動連携 / 未確認機能 / 有料プランが必要な機能 / 非対象範囲は「今回やらない」であって「永遠にやらない」ではない / 「第2フェーズの拡張候補」として将来の余地を残す / 今回の対象外 / 将来の拡張候補 / 今回やらないこと.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-76-06-S13-1782902392.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S13.png' --marker '/tmp/gas-diagram-markers/worker-76-06-S13-1782902392.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S13.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-76 --task-id 06-S13 --claim-token e69e5a8b-0320-4d07-ac2a-8b72d3d46a9f --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S13.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-76 --task-id 06-S13 --claim-token e69e5a8b-0320-4d07-ac2a-8b72d3d46a9f --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
