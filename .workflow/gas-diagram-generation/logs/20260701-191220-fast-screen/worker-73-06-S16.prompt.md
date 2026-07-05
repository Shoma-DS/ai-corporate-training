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
  "slide_id": "S16",
  "title": "プロトタイプは「判断材料」として見せる",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S16.png",
  "status": "claimed",
  "task_id": "06-S16",
  "worker": "worker-73",
  "claim_token": "087a54da-0f07-44f8-a92d-4e8d63312b10",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:42:01+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782902521.647559
}
```

Diagram prompt block:
```markdown
## S16 プロトタイプは「判断材料」として見せる

- セクション: プロトタイプと技術構成
- スライド側ヘッドライン（画像内には原則入れない）: 画面・台帳・ログ・AI出力レビューの4点セットを提案書に含めることで、「本当に動くのか」という疑問に答えられる
- 推奨図解パターン: comparison-contrast
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S16 / プロトタイプと技術構成.
Slide topic for context: プロトタイプは「判断材料」として見せる.
Concept to visualize: 画面・台帳・ログ・AI出力レビューの4点セットを提案書に含めることで、「本当に動くのか」という疑問に答えられる.
Suggested visual pattern: comparison-contrast.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: 画面・台帳・ログ・AI出力レビューの4点セットを提案書に含めることで、「本当に動くのか」という疑問に答えられる
**内容ブロック①：プロトタイプとして見せる4つの素材**
| 素材 | 何を見せるか | 提案書でのポジション |
|---|---|---|
| フォーム画面 | 入力項目・UIの完成度 | 「受け付け方がわかる」 |
| Sheets台帳 | 転記・分類・ログの列設計 | 「データがどう管理されるかがわかる」 |
| 実行ログ | 処理件数・成功率・エラー件数 | 「安定して動いているかがわかる」 |
| AI出力レビュー | Geminiが出した分類案と人の確認結果 | 「AIが何をして、人が何を確認するかがわかる」 |
**内容ブロック②：プロトタイプの「見せ方」の注意点**
- 完成版でなくてよい。「動作確認ができた段階」で見せる
- スクリーンショットには個人情報・社内情報が写り込まないようにダミーデータを使う
- 「精度100%」「ミスゼロ」は言わない。「テスト段階では〇件中〇件正常動作」と事実を書く
**内容ブロック③：プロトタイプの段階と提案のタイミング**
| 段階 | プロトタイプの状態 | 提案に使える素材 |
|---|---|---|
| 0段階 | まだ作っていない | フロー図・設計書のみ |
| 1段階 | GASで基本動作確認 | 台帳の転記結果・ログ |
| 2段階 | フォーム＋GAS＋通知が動作 | フォーム画面＋台帳＋ログ |
| 3段階 | AI連携まで動作 | 上記＋AI出力レビュー結果 |
Visible text candidates to use when useful, without reducing the source density: プロトタイプとして見せる4つの素材 / プロトタイプの「見せ方」の注意点 / プロトタイプの段階と提案のタイミング / 素材 / 何を見せるか / フォーム画面 / 入力項目・UIの完成度 / Sheets台帳 / 転記・分類・ログの列設計 / 実行ログ / 処理件数・成功率・エラー件数 / AI出力レビュー / Geminiが出した分類案と人の確認結果 / 完成版でなくてよい / 「精度100%」「ミスゼロ」は言わない / 段階 / プロトタイプの状態 / 0段階 / まだ作っていない / 1段階.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-73-06-S16-1782902521.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S16.png' --marker '/tmp/gas-diagram-markers/worker-73-06-S16-1782902521.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S16.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-73 --task-id 06-S16 --claim-token 087a54da-0f07-44f8-a92d-4e8d63312b10 --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S16.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-73 --task-id 06-S16 --claim-token 087a54da-0f07-44f8-a92d-4e8d63312b10 --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
