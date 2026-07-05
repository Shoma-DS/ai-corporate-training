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
  "slide_id": "S18",
  "title": "技術構成は「入力・処理・出力」で見せる",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S18.png",
  "status": "claimed",
  "task_id": "06-S18",
  "worker": "worker-76",
  "claim_token": "6ebfcaff-6e66-4b2c-970d-ffa5e73df209",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:45:29+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782902729.8072839
}
```

Diagram prompt block:
```markdown
## S18 技術構成は「入力・処理・出力」で見せる

- セクション: プロトタイプと技術構成
- スライド側ヘッドライン（画像内には原則入れない）: 技術構成をForms→GAS→Sheets→Drive→Gmail→Gem/Geminiの流れで整理することで、承認者にもIT担当者にも伝わる説明になる
- 推奨図解パターン: process-flow
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S18 / プロトタイプと技術構成.
Slide topic for context: 技術構成は「入力・処理・出力」で見せる.
Concept to visualize: 技術構成をForms→GAS→Sheets→Drive→Gmail→Gem/Geminiの流れで整理することで、承認者にもIT担当者にも伝わる説明になる.
Suggested visual pattern: process-flow.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: 技術構成をForms→GAS→Sheets→Drive→Gmail→Gem/Geminiの流れで整理することで、承認者にもIT担当者にも伝わる説明になる
**内容ブロック①：技術構成の標準フロー図**
コード例:
[入力]          [処理]              [出力]
Googleフォーム → GAS（転記・採番） → Sheets台帳
                ↓                  ↓
          Gemini（分類案）    Drive（Docs保存）
                ↓                  ↓
          GAS（確認ステップ）  Gmail（担当者通知）
コード例:
**内容ブロック②：ツールごとの役割と制限の明示**
| ツール | 役割 | 確認が必要な制限 |
|---|---|---|
| Google Forms | 入力の受け付け | スパム対策（reCAPTCHAの有無） |
| Google Sheets | データ管理・台帳・ログ | 同時アクセス時の競合 |
| GAS | 処理・転記・通知 | 実行時間6分・メール1,500件/日 |
| Gem/Gemini | 分類・要約（案）の生成 | Workspace有料プラン・API利用ポリシー |
| Google Drive | ファイル保存 | 保存容量・共有権限 |
**内容ブロック③：技術構成図を「読む人に合わせて」変える**
- 承認者向け: ツール名を使わず「受付→自動整理→担当者通知」の流れ図で見せる
- IT担当者向け: ツール名・API接続・権限設定・制限値を含む詳細な構成図で見せる
- 現場担当者向け: 「自分の作業がどこに変わるか」だけを1枚で見せる
Visible text candidates to use when useful, without reducing the source density: 技術構成の標準フロー図 / ツールごとの役割と制限の明示 / 技術構成図を「読む人に合わせて」変える / ツール / 役割 / Google Forms / 入力の受け付け / Google Sheets / データ管理・台帳・ログ / GAS / 処理・転記・通知 / Gem/Gemini / 分類・要約の生成 / Google Drive / ファイル保存 / 承認者向け / IT担当者向け / 現場担当者向け / 入力・処理・出力 / 読む人に合わせて.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-76-06-S18-1782902729.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S18.png' --marker '/tmp/gas-diagram-markers/worker-76-06-S18-1782902729.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S18.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-76 --task-id 06-S18 --claim-token 6ebfcaff-6e66-4b2c-970d-ffa5e73df209 --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S18.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-76 --task-id 06-S18 --claim-token 6ebfcaff-6e66-4b2c-970d-ffa5e73df209 --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
