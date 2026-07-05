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
  "slide_id": "S09",
  "title": "課題は3つ以内に絞る",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S09.png",
  "status": "claimed",
  "task_id": "06-S09",
  "worker": "worker-74",
  "claim_token": "f58c9b83-c852-469d-97f3-f0f5688e461a",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:30:54+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782901854.053217
}
```

Diagram prompt block:
```markdown
## S09 課題は3つ以内に絞る

- セクション: 課題整理とユースケース選定
- スライド側ヘッドライン（画像内には原則入れない）: 課題を3つ以内・「誰が・何に困っているか」の具体的な言葉で書くことで、提案の説得力が上がり読む側が共感しやすくなる
- 推奨図解パターン: checklist-confirmation
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S09 / 課題整理とユースケース選定.
Slide topic for context: 課題は3つ以内に絞る.
Concept to visualize: 課題を3つ以内・「誰が・何に困っているか」の具体的な言葉で書くことで、提案の説得力が上がり読む側が共感しやすくなる.
Suggested visual pattern: checklist-confirmation.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: 課題を3つ以内・「誰が・何に困っているか」の具体的な言葉で書くことで、提案の説得力が上がり読む側が共感しやすくなる
**内容ブロック①：課題の書き方フォーマット**
- NG: 「業務が属人化しています」（抽象的すぎる）
- NG: 「Excelの管理が非効率です」（手段を課題として書いている）
- OK: 「受付メールを担当者が手動でExcelに転記しており、1件あたり約5分かかる。月40件で月3時間以上が転記作業に費やされている」
- OK: 「担当者が不在のとき、フォーム回答への対応が翌日以降になり、顧客からの催促が月2〜3件発生している」
**内容ブロック②：課題を3つ以内に絞る理由**
- 4つ以上ある場合: 最も業務インパクトが大きいものを3つに絞る
- 「あれもこれも」書くと焦点が散漫になり、解決策も散漫になる
- 3つが整理できたら、残りは「今後の拡張課題」として最後のセクションに回す
**内容ブロック③：業種別の課題記述例**
| 業種 | 課題例（具体的な書き方） |
|---|---|
| 不動産業 | メール問い合わせを担当者が手動でコピーして管理表に貼り付けており、1件あたり10分かかる。週20件で週3時間超が転記作業 |
| 建設業 | 現場日報が紙で提出されるため、月次集計に事務が丸2日かかる。書き方のバラつきで読み取りエラーも多い |
| 美容室 | 電話予約の記録を手書きした後Googleカレンダーに手入力しており、ダブルブッキングが月1〜2件発生している |
Visible text candidates to use when useful, without reducing the source density: 課題の書き方フォーマット / 課題を3つ以内に絞る理由 / 業種別の課題記述例 / NG / OK / 4つ以上ある場合 / 「あれもこれも」書くと焦点が散漫になり、解決策も散漫になる / 課題例 / 不動産業 / 建設業 / 現場日報が紙で提出されるため、月次集計に事務が丸2日かかる / 美容室 / 誰が・何に困っているか / 業務が属人化しています / Excelの管理が非効率です / あれもこれも / 今後の拡張課題.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-74-06-S09-1782901854.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S09.png' --marker '/tmp/gas-diagram-markers/worker-74-06-S09-1782901854.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S09.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-74 --task-id 06-S09 --claim-token f58c9b83-c852-469d-97f3-f0f5688e461a --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S09.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-74 --task-id 06-S09 --claim-token f58c9b83-c852-469d-97f3-f0f5688e461a --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
