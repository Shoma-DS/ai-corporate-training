You are worker-74, generating exactly one claimed GAS course diagram part.

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
  "slide_id": "S17",
  "title": "スクリーンショットの安全確認",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S17.png",
  "status": "claimed",
  "task_id": "06-S17",
  "worker": "worker-74",
  "claim_token": "a175369f-8408-48e4-91cc-23c800b1792d",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:44:35+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782902675.121357
}
```

Diagram prompt block:
```markdown
## S17 スクリーンショットの安全確認

- セクション: プロトタイプと技術構成
- スライド側ヘッドライン（画像内には原則入れない）: 提案書に使うスクリーンショットから個人情報・社内情報を事前に除外することで、情報漏洩リスクをゼロにできる
- 推奨図解パターン: governance-risk
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S17 / プロトタイプと技術構成.
Slide topic for context: スクリーンショットの安全確認.
Concept to visualize: 提案書に使うスクリーンショットから個人情報・社内情報を事前に除外することで、情報漏洩リスクをゼロにできる.
Suggested visual pattern: governance-risk.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: 提案書に使うスクリーンショットから個人情報・社内情報を事前に除外することで、情報漏洩リスクをゼロにできる
**内容ブロック①：スクリーンショットから除外する情報**
| 情報の種類 | 具体例 | 対処法 |
|---|---|---|
| 個人情報 | 顧客名・電話番号・メールアドレス | ダミーデータに差し替えてから撮影 |
| 社内情報 | 社員名・部署名・会社固有のファイル名 | 架空のロール名（担当者A・部門B）に置換 |
| メールアドレス | 送信先・送信元のアドレス | @example.comのダミーアドレスに差し替え |
| APIキー・接続情報 | スクリプト内のキー・URL | 撮影範囲から外すかモザイク |
| 契約・未公開情報 | 価格・取引条件・未発表計画 | 撮影対象から外す |
**内容ブロック②：ダミーデータ環境の作り方（簡易版）**
- フォームとSheetsを「テスト用」として別途作成し、そちらで撮影する
- テスト用のメールアドレスは `test-dummy@example.com` を使う
- 会社名・顧客名・担当者名はすべて架空名称に統一する
**内容ブロック③：チェックリスト（提出前）**
- [ ] スクリーンショット内に実在の名前・連絡先が写っていないか
- [ ] シートの見出し行・列名に社内固有の固有名詞が入っていないか
- [ ] Googleアカウントのアイコン・メールアドレスが写り込んでいないか
- [ ] スクリプトのURLや設定情報が見えていないか
Visible text candidates to use when useful, without reducing the source density: スクリーンショットから除外する情報 / ダミーデータ環境の作り方 / チェックリスト / 情報の種類 / 具体例 / 個人情報 / 顧客名・電話番号・メールアドレス / 社内情報 / 社員名・部署名・会社固有のファイル名 / メールアドレス / 送信先・送信元のアドレス / APIキー・接続情報 / スクリプト内のキー・URL / 契約・未公開情報 / 価格・取引条件・未発表計画 / 会社名・顧客名・担当者名はすべて架空名称に統一する / [ ] スクリーンショット内に実在の名前・連絡先が写っていないか / [ ] シートの見出し行・列名に社内固有の固有名詞が入っていないか / [ ] スクリプトのURLや設定情報が見えていないか / テスト用.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-74-06-S17-1782902675.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S17.png' --marker '/tmp/gas-diagram-markers/worker-74-06-S17-1782902675.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S17.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-74 --task-id 06-S17 --claim-token a175369f-8408-48e4-91cc-23c800b1792d --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S17.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-74 --task-id 06-S17 --claim-token a175369f-8408-48e4-91cc-23c800b1792d --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
