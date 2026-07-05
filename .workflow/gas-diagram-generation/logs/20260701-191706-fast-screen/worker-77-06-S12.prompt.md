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
  "session_no": "06",
  "session_dir": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成",
  "slide_id": "S12",
  "title": "GapとGAS/AI解決策を対応させる",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S12.png",
  "status": "claimed",
  "task_id": "06-S12",
  "worker": "worker-77",
  "claim_token": "772f23d2-e741-4078-a5b0-0ed735a6d6ee",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:36:35+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782902195.392708
}
```

Diagram prompt block:
```markdown
## S12 GapとGAS/AI解決策を対応させる

- セクション: 課題整理とユースケース選定
- スライド側ヘッドライン（画像内には原則入れない）: As-IsとTo-Beの差分（Gap）を1つひとつ列挙し、各Gapにどのツール・処理が対応するかを示すことで、提案の実現可能性が伝わる
- 推奨図解パターン: before-after-transformation
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S12 / 課題整理とユースケース選定.
Slide topic for context: GapとGAS/AI解決策を対応させる.
Concept to visualize: As-IsとTo-Beの差分（Gap）を1つひとつ列挙し、各Gapにどのツール・処理が対応するかを示すことで、提案の実現可能性が伝わる.
Suggested visual pattern: before-after-transformation.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: As-IsとTo-Beの差分（Gap）を1つひとつ列挙し、各Gapにどのツール・処理が対応するかを示すことで、提案の実現可能性が伝わる
**内容ブロック①：Gap対応表の構造**
| Gap（現状との差分） | 解決手段 | 使うツール |
|---|---|---|
| メール受信→手動転記に時間がかかる | フォーム送信→GAS自動転記 | Google Forms ＋ GAS |
| 対応漏れが発生する | 担当者へ自動メール通知 | GAS（MailApp） |
| 問い合わせ種別の分類に時間がかかる | Geminiが分類案を生成（人が確認） | Gem/Gemini API |
| ファイルがローカル保存で共有できない | Drive指定フォルダに自動保存 | GAS ＋ Google Drive |
| 月次集計に時間がかかる | Sheetsで自動集計・ピボット | GAS ＋ Google Sheets |
**内容ブロック②：Gapが多い場合の優先順位のつけ方**
- 「時間削減効果が最大のGap」から着手する
- 「失敗した場合の影響が小さいGap」から着手する
- 第1フェーズ: 最もインパクトが大きく安全な1〜2個のGap
- 第2フェーズ以降: 残りのGapと拡張機能
**内容ブロック③：業種別のGap対応例**
- ホテル: Gap「電話予約のダブルブッキング」→ フォーム集約＋受付番号採番でダブり防止
- 製造業: Gap「紙日報の転記ミス」→ 日報フォーム化＋GAS自動集計で転記ゼロ化
Visible text candidates to use when useful, without reducing the source density: Gap対応表の構造 / Gapが多い場合の優先順位のつけ方 / 業種別のGap対応例 / Gap / 解決手段 / メール受信→手動転記に時間がかかる / フォーム送信→GAS自動転記 / 対応漏れが発生する / 担当者へ自動メール通知 / 問い合わせ種別の分類に時間がかかる / Geminiが分類案を生成 / ファイルがローカル保存で共有できない / Drive指定フォルダに自動保存 / 月次集計に時間がかかる / Sheetsで自動集計・ピボット / 「時間削減効果が最大のGap」から着手する / 「失敗した場合の影響が小さいGap」から着手する / 第1フェーズ / 第2フェーズ以降 / ホテル.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-77-06-S12-1782902195.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S12.png' --marker '/tmp/gas-diagram-markers/worker-77-06-S12-1782902195.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S12.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-77 --task-id 06-S12 --claim-token 772f23d2-e741-4078-a5b0-0ed735a6d6ee --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S12.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-77 --task-id 06-S12 --claim-token 772f23d2-e741-4078-a5b0-0ed735a6d6ee --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
