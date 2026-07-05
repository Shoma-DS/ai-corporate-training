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
  "slide_id": "S23",
  "title": "KPIは「導入後に測るもの」として設計する",
  "prompt_file": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ生成プロンプト.md",
  "target": "講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S23.png",
  "status": "claimed",
  "task_id": "06-S23",
  "worker": "worker-72",
  "claim_token": "4a0fa6eb-f333-4f11-8628-fb3fe0ac4d4b",
  "attempts": 1,
  "claimed_at": "2026-07-01T19:49:58+0900",
  "completed_at": null,
  "failed_at": null,
  "note": null,
  "claimed_at_epoch": 1782902998.509459
}
```

Diagram prompt block:
```markdown
## S23 KPIは「導入後に測るもの」として設計する

- セクション: KPIと効果試算
- スライド側ヘッドライン（画像内には原則入れない）: KPIを「導入後に測る指標」として定義することで、提案書が「効果の約束」ではなく「効果の測り方の提案」になる
- 推奨図解パターン: data-insight
- 参照素材・スクリーンショット: なし

```text
Create one dense supplemental isometric corporate diagram/reference-sheet image for a Japanese business training slide template.
Canvas should be clean white with generous margins, wide landscape and slightly shorter vertically than a full 16:9 slide, usable as a center, lower, or right-side attached visual inside an HTML/editable Google Slides layout. Leave room in the final template for editable title, S-number, session, and current-section labels.
Style: clean white, navy and teal accents, light gray thin card borders, subtle soft shadows, calm corporate isometric infographic, screenshot-compatible.
Context only, do not render visible header text: 生成AI・GASで実践する業務変革・DX推進講座 / 第6回 AI業務効率化プロジェクト提案書の作成 / S23 / KPIと効果試算.
Slide topic for context: KPIは「導入後に測るもの」として設計する.
Concept to visualize: KPIを「導入後に測る指標」として定義することで、提案書が「効果の約束」ではなく「効果の測り方の提案」になる.
Suggested visual pattern: data-insight.
Source slide information to preserve. Do not paste long paragraphs or speaker notes, but do preserve the core structures and short table/example cells as visible visual blocks when they carry the slide meaning:
ヘッドライン: KPIを「導入後に測る指標」として定義することで、提案書が「効果の約束」ではなく「効果の測り方の提案」になる
**内容ブロック①：KPIの4要素**
| 要素 | 決めること | 例 |
|---|---|---|
| 測定項目 | 何を測るか | 転記作業の月間工数（時間） |
| 仮置き数値 | 現状の数値と目標 | 現状: 月3時間 → 目標: 月30分以内 |
| 測定方法 | どうやって測るか | GAS実行ログの処理件数×1件あたり処理時間で換算 |
| 確認時期 | いつ測るか | 稼働1か月後・3か月後 |
**内容ブロック②：KPI設計の5カテゴリ**
| カテゴリ | 測定項目の例 | 測定方法 |
|---|---|---|
| 削減時間 | 転記・集計工数の月間削減時間 | GASログ×処理時間 |
| 対応速度 | フォーム送信から担当者通知までの時間 | ログのタイムスタンプ差 |
| ミス削減 | 転記ミス・通知漏れの件数 | 月次の手動確認記録 |
| 品質安定 | AI分類の一致率（担当者確認との比較） | 台帳の分類案vs確認済み欄の比較 |
| 属人化解消 | 担当者不在時の代替対応成功率 | 代替手順書に基づく運用記録 |
**内容ブロック③：「KPIは仮置き数値」と明示する**
- 提案書段階のKPIは「実測値ではなく演習上の仮置き数値」として明記する
- 「月3時間削減」は「現状の手動転記が月3時間という前提での試算」と書く
- 実際のKPIは稼働後のログ・記録から測定し、3か月後に報告する計画を提案書に含める
Visible text candidates to use when useful, without reducing the source density: KPIの4要素 / KPI設計の5カテゴリ / 「KPIは仮置き数値」と明示する / 要素 / 決めること / 測定項目 / 何を測るか / 仮置き数値 / 現状の数値と目標 / 測定方法 / どうやって測るか / 確認時期 / いつ測るか / カテゴリ / 測定項目の例 / 削減時間 / 転記・集計工数の月間削減時間 / 対応速度 / フォーム送信から担当者通知までの時間 / ミス削減.
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
   `mkdir -p /tmp/gas-diagram-markers && touch /tmp/gas-diagram-markers/worker-72-06-S23-1782902998.marker`
2. After imagegen, copy from your own Codex session only. Your session id is printed in this codex exec startup banner. Use:
   `python3 scripts/copy_latest_generated_image.py --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S23.png' --marker '/tmp/gas-diagram-markers/worker-72-06-S23-1782902998.marker' --session-id <your-session-id> --expect-mime image/png`
3. Verify:
   `file '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S23.png'`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker worker-72 --task-id 06-S23 --claim-token 4a0fa6eb-f333-4f11-8628-fb3fe0ac4d4b --target '講座/生成AI・GASで実践する業務変革・DX推進講座/06-AI業務効率化プロジェクト提案書の作成/図解パーツ/S23.png' --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker worker-72 --task-id 06-S23 --claim-token 4a0fa6eb-f333-4f11-8628-fb3fe0ac4d4b --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
