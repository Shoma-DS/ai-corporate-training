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
  "slide_id": "S11",
  "title": "To-Beは「人の確認まで含める」",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S11.png",
  "status": "claimed",
  "task_id": "06-S11",
  "worker": "worker-73",
  "claim_token": "6f1890ae-bf8b-4a0f-9456-3db04a7659e5",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:34:45+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782902085.279393
}
```

Diagram prompt block:
```markdown
## S11 To-Beは「人の確認まで含める」

- セクション: 課題整理とユースケース選定
- スライド側ヘッドライン（画像内には原則入れない）: To-Beフローに自動化の範囲だけでなく「人が確認・判断するステップ」を明示することで、安全な自動化計画になる
- 推奨図解パターン: process-flow
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S11 / 課題整理とユースケース選定.
Slide topic for context: To-Beは「人の確認まで含める」.
Concept to visualize: To-Beフローに自動化の範囲だけでなく「人が確認・判断するステップ」を明示することで、安全な自動化計画になる.
Suggested visual pattern: process-flow.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: To-Beフローに自動化の範囲だけでなく「人が確認・判断するステップ」を明示することで、安全な自動化計画になる
**内容ブロック①：To-Beフローの5ステップ（改善後）**
| ステップ | 自動化後（To-Be）の例 | 人がやること |
|---|---|---|
| 入力 | 顧客がGoogleフォームで問い合わせを送信 | フォーム設計（初期のみ） |
| 処理 | GASが自動でSheetsに転記・受付番号を発行 | 設計・テスト（初期のみ） |
| 確認 | Geminiが問い合わせ種別を分類（案）・確認フラグを立てる | 担当者が「確認済み」にチェック |
| 保存 | GASが指定フォルダにDocs形式で自動保存 | 保存先の設定（初期のみ） |
| 通知 | GASが担当者へ自動メール通知 | 通知内容・宛先の事前確認 |
**内容ブロック②：「自動化=全自動」ではない**
- To-Beに「人の確認ステップ」がないと、承認者に不安感を与える
- 「AIが全部やる」ではなく「AIが下書き・人が確認・確定」という設計を明示する
- 外部送信・承認・支払い・法的対応は「自動化の対象外」と明記する
**内容ブロック③：「Before/After」ではなく「As-Is/To-Be」と表現する理由**
- Before/Afterは「変えた結果」。As-Is/To-Beは「目指す姿へのプロセス」
- 提案段階では To-Be はまだ未実現。「目指す状態」として提示する
- As-IsとTo-Beを並べることで「変化の方向性」が視覚的に伝わる
Visible text candidates to use when useful, without reducing the source density: To-Beフローの5ステップ / 「自動化=全自動」ではない / 自動化後の例 / 入力 / 顧客がGoogleフォームで問い合わせを送信 / 処理 / GASが自動でSheetsに転記・受付番号を発行 / 確認 / Geminiが問い合わせ種別を分類・確認フラグを立てる / 保存 / GASが指定フォルダにDocs形式で自動保存 / 通知 / GASが担当者へ自動メール通知 / To-Beに「人の確認ステップ」がないと、承認者に不安感を与える / 外部送信・承認・支払い・法的対応は「自動化の対象外」と明記する / Before/Afterは「変えた結果」 / 提案段階では To-Be はまだ未実現 / As-IsとTo-Beを並べることで「変化の方向性」が視覚的に伝わる / 人の確認まで含める / 人が確認・判断するステップ.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-73-06-S11-1782902085.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S11.png' --marker '/tmp/gas-diagram-markers/worker-73-06-S11-1782902085.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S11.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-73 --task-id 06-S11 --claim-token 6f1890ae-bf8b-4a0f-9456-3db04a7659e5 --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S11.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-73 --task-id 06-S11 --claim-token 6f1890ae-bf8b-4a0f-9456-3db04a7659e5 --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
