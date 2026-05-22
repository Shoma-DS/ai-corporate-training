---
name: corporate-training-course-builder
description: >-
  Use when creating or updating corporate training course sessions end to end: curriculum expansion, 120-minute instructor scripts, slide outlines, image-generation prompts, GPT image 2 raster slide images, handouts, worksheets, exercise CSV/sample data, session-specific exercise-data splitting, official logos/screenshots, public/private source notes, and per-session folder organization. Also use for revising handouts or exercise data while checking online concrete examples, public practitioner use cases, and current official facts; and for instructor script polish: screen-share detailing, SME metaphors, industry-specific examples, and script readability. Trigger for one-phrase requests such as "第2回作って", "第4回の台本とスライド作って", "何回目の台本とスライド作って", "N回目の講師台本とスライド画像まで", "講師台本とスライド画像まで", "研修資料を一式作成", "配布資料と演習データも作って", "各回の演習データをその回で使うものだけにして", "全部同じに見えるCSVを直して", "ネットで具体例や活用事例を確認しながら練り直して", "スライド画像を再生成", "GPT image 2で1枚まるごと生成", "台本をブラッシュアップ", "画面共有を詳細化", or "メタファーを追加".
---

# Corporate Training Course Builder

## Purpose

Create complete, session-level corporate training materials that are ready for delivery: slide plan, instructor script, image prompts, generated slide images, handouts, worksheets, sample data, and source notes.

This skill is generic. Use it for any corporate training course, not only Google Workspace/GAS. Apply the repository's `AGENTS.md` first when present.

## One-Phrase Session Requests

When the user says "4回目の台本とスライド画像まで作って", "第4回の台本とスライド作って", "何回目の台本とスライド作って", or "N回目の講師台本とスライド画像まで", treat it as an end-to-end target-session request, not only a planning request.

1. Parse the course name and session number from the message and recent context. If the message literally says "何回目" and context does not identify the session, ask one concise clarification.
2. Locate the unique target session folder by checking course folders and numbered session names such as `04-...`, `第4回...`, or `4回目...`. If a folder is missing but the course is clear, create the standard session structure.
3. Read the target folder, adjacent sessions, whole-course curriculum, template catalog, and `references/session-production-workflow.md`, then run the standard workflow through script, prompts, handouts/data, and slide images.
4. Do not stop after `スライド案.md`, `講師台本.md`, or `画像生成プロンプト.md`. Continue until `講師台本.md`, `画像生成プロンプト.md`, required handouts/data, and target-session `スライド画像/Sxx.png` are complete or a real blocker is found.

## Standard Session Folder

Use a course folder plus session folders. Prefer this structure.

Course-level:

- `全体/`
- `全体/調査/`

Put course-wide materials in `全体/`: course overview, detailed syllabus, all-session worksheet, all-session instructor notes, exercise-data index, pamphlets, course-level slide outline, level mapping, and use-case/data design notes. Put course-wide source and research notes in `全体/調査/`.

Repository-level shared assets:

- `素材/ロゴ/`

Each session folder:

- `スライド案.md`
- `講師台本.md`
- `画像生成プロンプト.md`
- `ワークシート.md`
- `スライド画像/`
- `スクリーンショット/`
- `配布資料/`
- `演習データ/`

Do not create per-session `素材/ロゴ/`, `素材/スクリーンショット/`, `素材/作業風景/`, or `調査/` folders. Official logos are shared across courses, so keep them in repository-level `素材/ロゴ/`. Research normally belongs to the course, not to one session, so keep source notes in `全体/調査/`.

## Slide Style Templates

Use the repository slide template files as the source of truth for visual style. Do not rely on memory or invent a new visual direction when making slide outlines, image prompts, or slide images.

- Template catalog: `スライド/テンプレート/カタログ.yml`
- Selection flow: `スライド/スライド生成テンプレート選択フロー.md`
- Current main template: `スライド/テンプレート/アイソメトリック法人向けクリーン.md`
- Overview note: `スライド/アイソメトリック資料画像プロンプトテンプレート.md`

Before creating or revising `画像生成プロンプト.md` or `スライド画像/Sxx.png`:

1. Read `スライド/テンプレート/カタログ.yml`.
2. Pick one best matching template for the session's course, audience, slide purpose, and tone. If more than one template fits, follow `スライド/スライド生成テンプレート選択フロー.md`.
3. Read the selected template's `source_file`.
4. Apply its style tags, palette, diagram patterns, screenshot/logo rules, and default slide mapping.
5. Record the selected template ID and diagram pattern in `画像生成プロンプト.md` for each slide.

Within one session, keep the same template ID and visual style across `スライド案.md`, `講師台本.md`, `画像生成プロンプト.md`, and all generated `スライド画像/Sxx.png` by default. Mix templates only when the user explicitly asks for it.

For the current `isometric-corporate-clean` style, keep the visual direction clean, white-background, navy/teal, card-based, corporate, isometric, and screenshot/logo-compatible. Service logos and UI screens remain real referenced assets, not prompt-invented drawings.

## Workflow

1. Read the course folder, target session folder, previous session outputs, whole-course curriculum, `AGENTS.md`, existing `スライド案.md`, and `ワークシート.md`.
2. If current facts, services, laws, tool capabilities, pricing-adjacent details, logos, or case studies matter, browse official or primary sources and save a concise source memo in course-level `全体/調査/`.
3. If the user asks to check online concrete examples, practitioner examples, or use cases while revising worksheets, handouts, or exercise data, read `references/public-case-research-workflow.md`. Use official sources for current capabilities and general public examples for practical patterns; do not copy private details or reproduce a specific company's workflow.
4. If the user says exercise data looks duplicated, asks for "その回に必要なデータだけ", or asks to fully fix CSV/sample data, read `references/session-specific-exercise-data-workflow.md`. Split or rebuild `演習データ/` by the learner output and demo actually used in each session, then update stale file references.
5. Choose the slide style template from `スライド/テンプレート/カタログ.yml` and read the selected template before writing slide plans or image prompts.
6. Expand the session to fit the intended duration. For a 120-minute session, use enough slides for clear pacing, usually around 35-45 slides when demos and exercises are included.
7. Create or revise `スライド案.md` with slide numbers, titles, purpose, selected template ID, visual/material type, diagram pattern, demo/screenshot needs, and exercise timing.
8. Create `講師台本.md` as a word-for-word script. Include when to change slides, when to show work screens, what the instructor says, exercise instructions, time marks, and fallback explanations. Follow the **Instructor Script Rules** section below for block types, screen-share format, and SME metaphors.
9. Create all required `配布資料/`, `演習データ/`, CSV files, sample text, and worksheets inside the target session folder.
10. Create `画像生成プロンプト.md` for every slide. Include selected template ID, exact in-image text, visual pattern, official-logo inputs, screenshot inputs, screen-share transition slides, and negative prompt.
11. Use official logos/screenshots as reference assets when needed. Save official logos in repository-level `素材/ロゴ/` with source notes. Save screen captures for a session in that session's `スクリーンショット/`. Do not ask image generation to invent brand marks from memory.
12. Use the `imagegen` skill and its rules for raster slide images. Save final images in the target session's `スライド画像/Sxx.png`.
13. Verify text accuracy, slide count, asset paths, selected template usage, public-safety constraints, and that scripts/slides/handouts agree.

For a detailed checklist, read `references/session-production-workflow.md`.

## Parallel Subagents

If subagents are available and the user asks for parallelization, split the work aggressively but keep file ownership exclusive. The main agent coordinates context, resolves conflicts, and performs final integration.

- Before assigning work, the main agent chooses one session template ID and shares it with every subagent. All subagents must use that template/style unless the user explicitly approved mixing templates.
- The main agent keeps progress visible to the user, tracks which slide numbers are assigned, reconciles outputs, and verifies that filenames, slide titles, prompts, handouts/data, and generated images agree.
- Slide plan owner: edits only `スライド案.md`.
- Instructor script owner: edits only `講師台本.md`.
- Prompt/image owner: edits only `画像生成プロンプト.md` and `スライド画像/Sxx.png`, following the selected template and `imagegen` rules.
- If slide image generation is parallelized, split it into disjoint `Sxx` batches such as `S01-S10`, `S11-S20`, and `S21-S30`. Each image worker uses the same fixed template ID for the session and writes only its assigned `スライド画像/Sxx.png` files.
- Handout/data owner: edits only `ワークシート.md`, `配布資料/`, and `演習データ/`.
- Source/official asset owner: checks official sources, logos, screenshots, and writes only course-level `全体/調査/` notes or repository-level `素材/ロゴ/` assets.
- Verification owner: read-only review of slide counts, wording, paths, source notes, public-safety risks, and consistency; fixes are applied by the owning agent or main agent.

Never let multiple agents edit the same file. If ownership would overlap, have subagents return drafts, findings, or patch suggestions instead of writing directly.
For image batches, do not use SVG, HTML/CSS, canvas, browser screenshots, local conversion, or overlays. Final slide images must be generated as complete raster images with GPT image 2 / built-in image generation only.

## Slide Image Generation Rules

When a user says a slide image is wrong and asks to "regenerate", "作り直して", "再生成", use "GPT image 2", or create "1枚まるごと" as an image, treat this as a full-image generation request unless they explicitly ask for a deterministic layout edit.

- Do not repair the existing PNG by overlaying text, hiding elements, or rebuilding it as HTML/SVG and rasterizing it.
- Use the current slide only as a layout/style reference. Generate one complete new raster slide with the `imagegen` skill.
- Generate final visuals with GPT image 2 / built-in `image_gen` as bitmap images.
- Do not create SVG, HTML, CSS, canvas, PDF, or code-native graphics as an intermediate for the final image.
- Do not use ImageMagick, `convert`, `magick`, `rsvg-convert`, PIL, browser screenshots, local rasterization, tracing, or compositing to make the final slide image.
- Copying or moving a generated PNG/WebP into the project is allowed. Converting or redrawing it locally is not.
- If exact text is required, keep text short and ask GPT image 2 to render it directly. Do not overlay text locally.
- Before generating, inspect repository-level `素材/ロゴ/` and load the needed official logo files as image references. Do not leave logo placeholders when logo assets exist.
- Use only official logo files already present in the repo when the user asks for real service logos. Do not ask GPT image 2 to invent or redraw real logos from memory.
- Explicitly prohibit placeholder artifacts in the prompt: dashed boxes, empty logo slots, `素材配置枠`, `公式ロゴ`, watermarks, and fake UI/screenshots.
- Preserve exact in-slide wording from the user's latest correction. Search for and remove stale wording such as old product pairings or prior draft labels before saving.
- If the built-in image tool cannot save directly to the requested project path, generate first, then copy or move the generated bitmap file without modifying its pixels.
- After generation, inspect the image before replacing `スライド画像/Sxx.png`. Check product names, Japanese text, logo placement, card spacing, and whether the output still contains forbidden placeholder text.
- If you start considering SVG, HTML/CSS, canvas, screenshots, or local conversion for a GPT image 2 request, stop and switch back to bitmap generation.

## Quality Rules

- Start from business problems, not tool features.
- For Manabi DX level 3 or advanced digital talent materials, avoid framing the course as a named-tool usage class. Lead with business transformation, requirements definition, operating design, continuous operation, improvement proposals, DX promotion, and practical outputs. Tools such as Google Workspace, GAS, Gemini/Gem, Dify, RAG, NotebookLM, or Copilot should appear as means inside the business process, not as the course's main value.
- Every session must end in a practical output learners can use or adapt.
- Use demos and screenshots when a service or UI is clearer than abstract diagrams.
- When the instructor will switch to a live work screen or recording, do not make a slide that tries to contain the work scene. Make a transition slide that says the screen will be shown now, then describe the demo in `講師台本.md`.
- For AI/data safety, distinguish normal business use from external AI/public materials. Business spreadsheets/forms may contain real operational data; demos, public materials, and AI inputs should use sample, anonymized, or minimum necessary data.
- Official logos must come from official sites, brand guidelines, or press kits where possible, with source notes.
- Public files must not contain private company materials, real customer/employee data, prices, contact details, credentials, API keys, or unreleased internal content.

## Level 3 Framing Checks

When creating brochures, syllabi, slide outlines, or application-facing summaries for Manabi DX level 3:

- First-viewport or opening copy should say what business capability the learner gains, such as independently organizing issues, designing As-Is/To-Be, defining requirements, separating automation scope, designing operation, setting KPIs, and proposing improvements.
- Session titles should not be tool-first if that makes the course look like a basic operations class. Prefer titles like "業務課題整理とAs-Is/To-Be設計", "AI/GAS活用の要件定義・運用設計", and "DX推進に向けたKPI設計・導入提案".
- If tool names are necessary, pair them with purpose and workflow: input, processing, output, human review, logs, exception handling, recovery, and continuous improvement.
- Explicitly include outputs that evidence level 3 work: requirements memo, operating design, risk checklist, prototype, KPI/effect estimate, rollout roadmap, and implementation proposal.

## Delivery Format

This course is delivered as **pre-recorded video for async reskilling** (録画動画によるリスキリング講座). There is no live instructor–learner interaction. All script blocks must be written with this in mind.

### Video-format rules (mandatory)

- **ワーク時間の指示**: 「今から○分取ります」は使わない。代わりに「ここで動画を一時停止して、○分ほど取り組んでください。取り組めたら再生してください。」を使う。
- **声がけ・タイマー管理**: 「1分経過で声がけする」「残り1分でアナウンス」のような 講師メモは書かない。
- **ライブ共有・発表・討議**: `共有指示:` ブロック、「チャットでも構いません」、「口頭で共有してください」、「発表してください（ライブ）」、相互フィードバックは使わない。
- **「受講者に〜させる」**: 実演ブロックの手順に「受講者に自分のワークシートを見直させる」のような指示は書かない。「ここで動画を一時停止して〜してください」という読み上げ文に変える。
- **発表・相互レビュー**: グループ発表や相互フィードバックは行わない。代わりに「自己レビュー」と「講師の記入例との比較」に置き換える。
- **フォールバック**: 環境差がある場合の代替手順は引き続き記載する（録画中に説明すべき内容のため）。

## Instructor Script Rules

### Block types (use only these five — do not add others)

```
スライド切替:
S番号「スライドタイトル」

読み上げ:
「〜〜〜。」

画面共有 ── 実演N「タイトル」
⏱ 約○分
【手順1 – 約○秒】〜
【手順2 – 約○秒】〜
【見せるポイント】〜

ワーク指示:
「〜〜〜。」

講師メモ:
（読み上げない。進行管理・注意喚起のみ）
```

### Screen-share format (required for every 画面共有 block)

"何を見せるか" alone is not enough. Always write all of the following.

```markdown
**画面共有 ── 実演N「タイトル」**
⏱ 約○分

【手順1 – 約○秒/分】
何の画面を開くか。どのデータを使うか。どんな操作をするか。何を声に出して説明するか。

【手順2 – 約○秒/分】
（以下同様）

【手順N – 約○秒/分】
操作の最後に「このあと、〜につながります」という予告を入れると全体像が伝わりやすい。

【見せるポイント】
この画面共有で受講者に何を気づかせたいか。1〜2文で書く。
```

Time guides:

| Demo type | Typical duration |
| --- | --- |
| Before/After comparison | 1–2 min |
| End-to-end tool walkthrough | 3–5 min |
| Switching screens in sequence | 1–2 min |
| Showing instructor's filled-in example | 2–4 min |

### Polish priorities (for brush-up requests)

1. **Screen-share detailing** (highest priority): expand "what to show" into "⏱ time · step-by-step · talking points"
2. **Metaphor addition**: add 1–2 SME-appropriate metaphors to abstract explanations
3. **Industry-specific examples**: replace generic examples ("問い合わせ管理") with sector-specific ones
4. **Natural phrasing**: rewrite read-aloud text so the instructor can say it comfortably in one breath

### SME Metaphor Bank

Use at most 1–2 metaphors per explanation. Do not overuse.

| Tool / concept | Metaphor |
| --- | --- |
| Googleフォーム（入力の入口） | ファミレスのタッチパネル注文機。客が自分で入力するから転記ミスがない。 |
| Googleスプレッドシート（台帳） | 全員がリアルタイムで見られる掲示板兼ホワイトボード。Excelは誰かのパソコンの中に閉じ込められていた。 |
| GAS（自動化） | 決まった仕事を自動でこなす事務担当ロボット。給料不要、土日も動く。ただし例外判断はしない。 |
| Gemini/Gem（AI補助） | 文章の仕分けや下書きが得意な補助スタッフ。正しいかどうかは人が確認する。最終判断は常に人。 |
| データ整備の重要性 | 食材がバラバラな冷蔵庫で料理ロボットを動かしても毎回エラーが出る。材料の規格を揃えることが先。 |
| 属人化リスク | Aさんだけが知っている作業。Aさんが休んだら月次処理が止まる。 |
| DXの入口 | 工場でいえば、新しい機械を入れる前に材料の置き場所を決めて手順書を作ること。 |
| Google Workspace全体 | 受付窓口（Forms）・台帳（Sheets）・郵便（Gmail）・書類棚（Drive）・事務ロボット（GAS）・補助スタッフ（Gemini）のセット。 |
| As-Is/To-Be | 間取り変更の前に、今の部屋でどう動いているかを確認する作業。 |

### Industry-Specific Examples

Replace generic examples with sector-specific ones when the audience is known.

| Industry | Common manual-work example |
| --- | --- |
| サービス業（美容・ホテル・飲食） | 電話予約をメモ→Excelに転記。キャンセル・変更のたびに手直し。 |
| 不動産業 | メール問い合わせをコピーして管理表に貼る。担当者の割当を上司に口頭確認。 |
| 士業（税理士・行政書士・社労士） | 申告・申請依頼をメールで受け、各担当者のExcelファイルで管理。最新がどれかわからない。 |
| 製造業・卸売り | FAX/メールで注文が来て手書き台帳に転記。月末に集計してExcelにまとめる。 |
| 建設業 | 現場日報を紙で提出→事務がExcelに転記。書き方が人によってバラバラ。 |
| 社内横断（どの業種でも） | 月末に未対応を目で探す。期限が近い人を探して一件ずつメールを書く。先月のファイルをコピーして数字だけ書き換える。 |

## Completion Checklist

Before finishing, confirm:

- The target session has the standard folder structure.
- `スライド案.md`, `講師台本.md`, `画像生成プロンプト.md`, `ワークシート.md`, and needed handouts/data exist.
- Slide numbers and titles match across slide plan, script, prompts, and images.
- `画像生成プロンプト.md` records the selected slide template ID and uses a diagram pattern from `スライド/テンプレート/カタログ.yml` or the selected `source_file`.
- One session uses one template ID and one visual style across prompts and generated images, unless the user explicitly requested mixed templates.
- `スライド画像/` contains all required images.
- Asset references point to repository-level `素材/ロゴ/`, course-level `全体/調査/`, or session-local `スクリーンショット/`, `演習データ/`, and `配布資料/`.
- Source memos exist for current facts and official assets.
- Public-safety checks pass.
- すべての画面共有ブロックに `⏱ 約○分`・`【手順1〜N】`・`【見せるポイント】` が書かれているか
- 各ブロックのメタファーは中小企業の実態に合っているか（IT前提のメタファーを使っていないか）
- 読み上げ文は講師が一息で自然に読めるか（1文が長すぎないか）
- ワーク指示に「今から○分取ります」が使われていないか（動画では「ここで動画を一時停止して○分ほど取り組んでください」を使う）
- 「チャット」「挙手」「口頭共有」「声がけタイミング（残り1分など）」など、ライブ配信前提の表現が含まれていないか
- `共有指示:` ブロックが使われていないか（動画形式では自己レビューに置き換える）
- 発表・相互フィードバックのブロックがないか（動画では自己レビューと講師記入例との比較に置き換える）
- 実演ブロックの手順に「受講者に〜させる」が含まれていないか（読み上げ文として「動画を止めて〜してください」に変える）
- スライド切替タイムライン表が末尾に整理されているか
- 作業風景タイムライン表（番号・タイトル・⏱ 時間・操作概要）が末尾にあるか
- 有料プラン・管理者設定が必要な機能を「必須演習」にしていないか
