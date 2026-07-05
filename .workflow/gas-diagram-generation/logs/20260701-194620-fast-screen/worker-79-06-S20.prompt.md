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
  "slide_id": "S20",
  "title": "Gemini連携と代替運用をセットにする",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S20.png",
  "status": "claimed",
  "task_id": "06-S20",
  "worker": "worker-79",
  "claim_token": "71d1e8b6-f82a-4a2c-b45f-24a72a0426c0",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:46:30+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782902790.1963031
}
```

Diagram prompt block:
```markdown
## S20 Gemini連携と代替運用をセットにする

- セクション: プロトタイプと技術構成
- スライド側ヘッドライン（画像内には原則入れない）: Gemini連携の提案には必ず「使えない場合の代替手順」をセットで書くことで、環境差や制限があっても業務が止まらない設計になる
- 推奨図解パターン: before-after-transformation
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S20 / プロトタイプと技術構成.
Slide topic for context: Gemini連携と代替運用をセットにする.
Concept to visualize: Gemini連携の提案には必ず「使えない場合の代替手順」をセットで書くことで、環境差や制限があっても業務が止まらない設計になる.
Suggested visual pattern: before-after-transformation.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: Gemini連携の提案には必ず「使えない場合の代替手順」をセットで書くことで、環境差や制限があっても業務が止まらない設計になる
**内容ブロック①：Gemini連携の利用可否と代替設計**
| 状況 | 利用可否 | 代替手順 |
|---|---|---|
| Workspace Business以上（有料） | 利用可 | 標準構成で実施 |
| 個人アカウントまたはFree | APIは利用不可 | Gemini.google.comを手動で使い、結果をSheetsに貼り付け |
| 管理者がAPI接続を制限 | 利用不可 | GASのみの構成（分類なし）で運用 |
| 入力に個人情報が含まれる可能性 | 条件付き利用可 | 匿名化処理後のみGeminiへ渡す |
**内容ブロック②：「Geminiが使えない場合でも動く」設計の意味**
- プロトタイプ段階でGemini連携が動かなくても、GAS単体でフローは動く
- Gemini連携は「あると効果的だが、なくても業務は続けられる」という位置づけにする
- 提案書に「GASのみ版」と「GAS＋Gemini版」の2段階を書くと、承認者が選択しやすい
**内容ブロック③：段階的な導入計画の提案例**
- 第1フェーズ（1か月）: GASのみで自動転記・通知。Geminiなし
- 第2フェーズ（2〜3か月）: Geminiによる分類案を追加（有料プラン確認後）
- 第3フェーズ（以降）: Meet文字起こし連携・帳票自動生成の拡張
Visible text candidates to use when useful, without reducing the source density: Gemini連携の利用可否と代替設計 / 「Geminiが使えない場合でも動く」設計の意味 / 段階的な導入計画の提案例 / 状況 / 利用可否 / Workspace Business以上 / 利用可 / 個人アカウントまたはFree / APIは利用不可 / 管理者がAPI接続を制限 / 利用不可 / 入力に個人情報が含まれる可能性 / 条件付き利用可 / 第1フェーズ / 第2フェーズ / 第3フェーズ / 使えない場合の代替手順 / GASのみ版 / GAS＋Gemini版.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-79-06-S20-1782902790.marker`
2. After imagegen, copy from your own Codex session only. Use the UUID-like `session id` printed in this codex exec startup banner, for example `019f...`; do not use the timestamp-like id sometimes shown by the image tool. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S20.png' --marker '/tmp/gas-diagram-markers/worker-79-06-S20-1782902790.marker' --session-id <uuid-session-id-from-startup-banner> --expect-mime image/png --allow-latest-in-session`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S20.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-79 --task-id 06-S20 --claim-token 71d1e8b6-f82a-4a2c-b45f-24a72a0426c0 --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S20.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-79 --task-id 06-S20 --claim-token 71d1e8b6-f82a-4a2c-b45f-24a72a0426c0 --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
