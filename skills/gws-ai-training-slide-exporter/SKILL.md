---
name: gws-ai-training-slide-exporter
description: Use only as a downstream export/delivery helper after corporate-training-course-builder has produced local course materials and slide images, or when the user explicitly asks only for Google Drive/Google Slides/PPTX/Canva export; do not use as the entrypoint for 講座作成 or broad training-material creation.
---

# GWS AI Training Slide Exporter

## Purpose

Publish local AI法人研修 session assets to Google Drive as structured course folders and Google Slides decks.

This is a downstream export skill. If the user asks to create, rebuild, revise, or regenerate a course/session, first use `skills/corporate-training-course-builder/SKILL.md`. Return to this skill only after local course materials and `スライド画像/Sxx.png` are complete.

Do not define course content, curriculum standards, slide-image rules, or Canva policy independently here. Those live in `skills/corporate-training-course-builder/SKILL.md` and its references. This skill only executes the delivery phase selected by that workflow.

This skill is for repository sessions that contain:

- `スライド画像/Sxx.png`
- `講師台本.md`
- `スライド案.md`
- `演習データ/`

It creates or reuses this Drive hierarchy and avoids creating duplicate files when the same name already exists:

```text
AI法人研修/
  講座名/
    回数フォルダ名/
      講師台本.md
      スライド案.md
      Googleスライド
      演習データ/
        local exercise files
```

The deck contains one local slide image per Google Slides page. Speaker notes are populated from the matching `Sxx` block in `講師台本.md`.

## Canva Route: 画像アップロード先行プレゼンを標準にする

Canvaで「回ごと1本の複数ページプレゼンテーション」を作る場合、標準は **画像アップロード先行** とする。全ページをCanva MCPでMagic Layers化しない。

```text
スライド画像/S01.png, S02.png, ...
  -> 回ごとに1本のPPTXまたはCanvaプレゼンへ画像として取り込み
  -> Canva上で全ページを確認
  -> 編集頻度が高いページだけ手動でMagic Layersを適用
```

理由:

- Canva MCPで全ページをMagic Layers化すると、1画像ごとの変換・移動・命名・結合が必要になり、トークンと外部API処理が膨らむ。
- 研修スライドは多くのページが固定説明、図解、画面遷移、演習案内であり、全ページを編集可能レイヤーにする必要がない。
- 画像ベースなら生成済みスライドの見た目を崩さず、レビュー・共有・納品までの速度が出る。
- 表紙、日付、企業名、講師名、カリキュラム表など、差し替え頻度が高いページだけをCanva上で手動Magic Layers化すればよい。

### Phase 1: ローカル画像とPPTX準備

まず `スライド画像/Sxx.png` の連番、枚数、空ファイル有無を確認する。

```bash
python3 skills/gws-ai-training-slide-exporter/scripts/export_ai_training_slides_to_gws.py \
  --course-dir '講座/COURSE' \
  --all-sessions \
  --dry-run
```

Canvaにインポートしやすい講座単位PPTXを作る場合:

```bash
python3 skills/gws-ai-training-slide-exporter/scripts/export_ai_training_slides_to_gws.py \
  --course-dir '講座/COURSE' \
  --canva-course-pptx-only \
  --canva-pptx-dir '書き出し/canva-pptx'
```

出力先は `書き出し/canva-pptx/<講座名>/<講座名>.pptx` になる。

回別PPTXを作る場合:

```bash
python3 skills/gws-ai-training-slide-exporter/scripts/export_ai_training_slides_to_gws.py \
  --course-dir '講座/COURSE' \
  --all-sessions \
  --canva-pptx-only \
  --canva-pptx-dir '書き出し/canva-pptx/COURSE'
```

回別PPTXの出力先は `書き出し/canva-pptx/<講座名>/<回フォルダ名>.pptx` になる。

事前確認だけなら `--dry-run` を追加する。PPTXは画像をページ全面に配置したCanva取り込み用の中間成果物として扱う。これらのオプションはGoogle DriveフォルダやGoogle Slidesを作らない。

品質を保ちやすい設定・工夫は `references/canva-quality-checklist.md` を読む。PPTX化やCanva取り込みで品質劣化を減らせる選択肢がある場合は、ユーザーの追加指示を待たずに積極的に採用する。

### Phase 2: Canvaへ回別プレゼンとして取り込み

次のどちらかで、回ごとに1本のCanvaプレゼンテーションを作る。

- Canva UIで、回別PPTXをアップロードしてデザイン化する。
- Canva Connect APIで、画像またはPPTXをアップロードし、回別の複数ページプレゼンテーションを作る。

Canva MCPの `_image_to_design` を全スライドへ順次かける作業は標準では行わない。MCPは必要に応じてフォルダ作成、デザイン移動、URL整理など低トークンな補助に使う。

Canva MCP/APIで作れる場合は、ブラウザ操作の前に次を満たす状態まで作る。

- `S01.png` から最終スライドまでが、Canvaプレゼンテーションの1ページ目から順番に並んでいる。
- 1回分または1講座分が、ばらばらの1ページデザインではなく複数ページプレゼンテーションとして開ける。
- ページ数、デザイン名、保存先フォルダ、編集URLを `非公開/Canva/` に記録している。
- publicリポジトリにはCanva URL、design ID、アクセストークン、顧客別メモを書いていない。

### Phase 3: 手動Magic Layers対象を選ぶ

全ページをMagic Layers化せず、次のような編集対象ページだけをCanva上で手動変換する。

- 表紙、章扉、クロージング
- 企業名、実施日、講師名、部署名を差し替えるページ
- カリキュラム表、受講対象、成果物一覧
- 営業・提案時に文言変更が起きやすいページ
- 受講企業ごとに一部カスタマイズするケース紹介ページ

画像のままでよいページ:

- 固定の業務フロー図、概念図、Before/After図
- 画面共有への遷移スライド
- 操作画面・スクリーンショット中心の説明
- 演習手順、確認観点、まとめ

### Phase 3B: ブラウザMagic Layers検証ループ

ユーザーが「ブラウザのCanvaでMagic Layersを適用して検証して」と明示した場合だけ、このループを実行する。Kimi WebBridgeなど実ブラウザ操作を使う前に、対象のCanvaプレゼンテーションURL、対象ページ、期待する検証観点を `非公開/Canva/` の作業メモに置く。

1. Kimi WebBridgeなどのブラウザ操作スキルを使う場合は、最初にヘルスチェックを行い、1タスク1セッション名でCanvaを開く。
2. 対象ページを開き、Magic Layersを1ページだけ適用する。
3. Canvaの処理が終わるまで数秒待つ。読み込み中表示、レイヤー生成中表示、ページの再描画が残っている間は判定しない。
4. スクリーンショットを取り、元の `スライド画像/Sxx.png` または直前のCanva表示と比べる。
5. 次のいずれかがあれば失敗扱いにする: 日本語の文字化け、文言の勝手な変更、文字欠落、表やカードの崩れ、要素の重なり、ロゴの誤変形、スクリーンショット部分の不自然な分解。
6. 失敗したらCommand+Z、Canvaの戻る、履歴、またはページ復元で適用前に戻し、同じページで再試行する。
7. 同じページでMagic Layersが3回以上失敗した場合は、それ以上試さず元画像ページのまま残す。`status=kept_image` または `needs_manual_fix` として記録する。
8. 成功したページだけ次ページへ進む。
9. 失敗時にわかった崩れ方、崩れやすいページ種別、確認すべき箇所は `references/canva-quality-checklist.md` にチェック項目として追記し、次回以降の検証で重点的に見る。

ページごとに次を `非公開/Canva/<講座名>_Magic_Layers検証ログ.csv` へ記録する。

```text
session_no,page_no,slide_file,status,retry_count,issues,action,checked_at,notes
```

`status` は `ok`, `retried_ok`, `kept_image`, `needs_manual_fix`, `failed` のいずれかにする。

#### ブラウザ操作のエージェント分担

ブラウザ操作はトークン消費が大きいため、サブエージェントとモデル選択が使える環境では次の分担を優先する。

- 司令塔: 高精度モデルのまま、対象ページ、合否基準、最終判断、ログ統合を担当する。
- ブラウザ操作担当: `codex-5.3spark` / `GPT-5.3 Codex Spark` 相当の低コストモデルを最優先で使い、Spark利用枠を積極的に消費する。Kimi WebBridgeのクリック、待機、スクリーンショット、ページ移動、単純な表示確認だけを担当する。
- 画像再生成担当: Magic Layersでは直せず、元スライド画像の再生成が必要な場合だけ、GPT image 2を使える高精度・画像対応モデルで再生成する。

モデル指定やサブエージェント呼び出しができない環境では、同じ役割を手順として分け、スクリーンショット回数、`snapshot` 回数、ページ移動回数を抑える。モデル指定が可能な環境で、ブラウザ操作を高精度モデル単体で長時間抱え込まない。

### Phase 4: URLと編集メモを非公開で集約

- Drive側は `Canva_URL一覧.csv` のみ作成する。
- publicリポジトリにCanva URL、design ID、認証情報を書かない。
- 回ごとのURL一覧、Magic Layers対象ページメモ、手動編集結果は `非公開/Canva/` とGoogle Drive同期先に置く。

推奨するURL一覧の列:

```text
session_no,session_name,course_name,presentation_design_id,edit_url,view_url,page_count,magic_layers_pages,notes
```

### Legacy Route: 全ページMagic Layers化して結合する例外ルート

ユーザーが明示的に「全ページをMagic Layers化したい」「編集可能レイヤー化を優先する」と指定した場合だけ、旧ルートを使う。

```text
S01.png -> Canva MCP _image_to_design -> 1ページのMagic Layersデザイン
S02.png -> Canva MCP _image_to_design -> 1ページのMagic Layersデザイン
...
Canva Connect API /v1/merges -> 回ごと1本の複数ページデザイン
```

現行のCanva MCP `_image_to_design` は、1回の呼び出しで新しい独立デザインを作る。既存プレゼンテーションへページ追加しながらMagic Layers化する用途には使わない。

#### Legacy Phase 1: Canvaフォルダ階層

`_create_folder` で不足フォルダを作成し、フォルダIDを `state.json` または非公開メモに記録する。

```text
AI法人研修/
  講座名/
    01-セッション名/
    02-セッション名/
    ...
```

#### Legacy Phase 2: 画像ごとにMagic Layers化

各スライド画像を S01, S02, S03... の昇順で処理する。

```text
_image_to_design(
  image_file: "/absolute/path/to/スライド画像/S01.png",
  title: "01-S01_01-セッション名"
)
```

- `image_file` は絶対パスで渡す。
- 返ってきた `design_id`, `edit_url`, `view_url` を `非公開/Canva/*.jsonl` に記録する。
- `_move_item_to_folder` で対応するセッションフォルダへ移動する。
- 失敗時は1回リトライし、2回失敗したらfailedで記録して次へ進む。

#### Legacy Phase 3: Canva上のデザイン名を揃える

既存デザイン名を `回番号-Sxx_セッション名` にする。

```text
01-S01_01-業務DXの基礎とGoogle Workspace活用設計
01-S02_01-業務DXの基礎とGoogle Workspace活用設計
```

タイトル変更はCanva MCPの編集トランザクションで実施する:

```text
start_editing_transaction -> perform_editing_operations(update_title) -> commit_editing_transaction
```

#### Legacy Phase 4: Canva Connect APIで回ごとに結合

Magic Layers化済みの1ページデザインを、Canva Connect API Design Mergeで回ごとに1本へまとめる。

Requirements:

- `CANVA_ACCESS_TOKEN`
- OAuth scopes: `design:content:write`, `design:meta:read`
- To create/move folders with the same script, also enable `folder:read` and `folder:write`.
- Design Merge API is preview. First run with `--dry-run` or a small session.

Dry run:

```bash
python3 .workflow/google-workspace-canva-magic-layers/merge_magic_layers_designs.py \
  --session 01 \
  --dry-run
```

Run:

```bash
CANVA_ACCESS_TOKEN="$CANVA_ACCESS_TOKEN" \
python3 .workflow/google-workspace-canva-magic-layers/merge_magic_layers_designs.py \
  --session 01
```

Create a Canva folder and move merged decks into it:

```bash
CANVA_ACCESS_TOKEN="$CANVA_ACCESS_TOKEN" \
python3 .workflow/google-workspace-canva-magic-layers/merge_magic_layers_designs.py \
  --create-folder "Google Workspace・GASで進めるAI業務効率化-DX実践講座"
```

Move merged decks into an existing Canva folder:

```bash
CANVA_ACCESS_TOKEN="$CANVA_ACCESS_TOKEN" \
python3 .workflow/google-workspace-canva-magic-layers/merge_magic_layers_designs.py \
  --folder-id "FA..."
```

All sessions:

```bash
CANVA_ACCESS_TOKEN="$CANVA_ACCESS_TOKEN" \
python3 .workflow/google-workspace-canva-magic-layers/merge_magic_layers_designs.py
```

Output:

- Input plan: `非公開/Canva/google_workspace_canva_rename_titles_plan.json`
- Result: `非公開/Canva/google_workspace_canva_merge_results.json`
- Use `final_response.job.result.design.urls.edit_url` and `view_url` as the merged presentation URLs.
- If `--create-folder` is used, the created folder ID is stored in `folder_create_response.folder.id`.

#### Legacy Phase 5: URL集約

- Drive側は `Canva_URL一覧.csv` のみ作成する。
- publicリポジトリにCanva URL、design ID、認証情報を書かない。
- 回ごとのURL一覧は `非公開/Canva/` とGoogle Drive同期先に置く。

### スライドソース確認コマンド

```bash
python3 skills/gws-ai-training-slide-exporter/scripts/export_ai_training_slides_to_gws.py \
  --course-dir '講座/COURSE' \
  --all-sessions \
  --dry-run
```

`--dry-run` でスライド枚数と回の一覧を確認してから実行する。

## Safety Rules

- Do not upload files under `非公開/`.
- Do not save Google Drive file IDs, URLs, or customer-specific links into public tracked files unless the user explicitly asks. When they ask for a public link list, generate only the sharing index at `講座/COURSE/全体/Google_Driveリンク一覧.md`; keep raw reports and API responses under `非公開/`.
- Use generated/public-safe slide images and dummy data only.
- Run `gws auth status` before export. If it fails, stop and ask the user to run Google Workspace authentication.
- If a folder name is duplicated in Drive under the same parent, stop and ask for an explicit parent/root folder ID.
- If the target Google Slides deck or material file already exists in the session folder, skip it unless the user explicitly asks to replace/recreate.

## Main Command

Use the bundled script:

```bash
python3 skills/gws-ai-training-slide-exporter/scripts/export_ai_training_slides_to_gws.py \
  --session-dir "講座/COURSE/06-SESSION"
```

Useful options:

- `--root-folder-name "AI法人研修"`: default root folder name.
- `--root-folder-id <drive-folder-id>`: use a known Drive folder instead of searching by name.
- `--course-dir "講座/COURSE"` with `--all-sessions`: export every numbered session with slide images, scripts, slide outlines, and exercise data.
- `--dry-run`: inspect the planned folder/deck work without calling `gws`.
- `--report-json 非公開/.../export-report.json`: save Drive IDs/URLs outside public tracked files.
- `--tmp-dir 書き出し/gws-ai-training-slide-exporter/tmp`: default repository-local PPTX temp directory for this gws-based exporter. Some `gws --upload` calls in this environment reject files outside the current repository. This is a gws CLI constraint for this script, not a general Drive-copy rule.
- `--replace-existing-decks`: when a session deck with the same title already exists in the target Drive session folder, delete that Google Slides deck first, then create a fresh deck from the current local `スライド画像/Sxx.png`.
- `--write-link-index`: after a full-course Drive/Google Slides export, write `講座/COURSE/全体/Google_Driveリンク一覧.md` with the Drive root, course folder, session folders, Google Slides links, slide counts, replacement counts, and warnings.
- `--link-index-path <path>`: override the public Markdown link index destination. Use only with `--write-link-index`.
- `--canva-pptx-dir`: output one PPTX per session for Canva single-presentation import workflows.
- `--canva-pptx-only`: only create Canva-ready PPTX bundles from `スライド画像/Sxx.png`; do not create Drive folders or Google Slides.
- `--canva-course-pptx-only`: create one Canva-ready PPTX for the whole course at `<canva-pptx-dir>/<講座名>/<講座名>.pptx`; do not create Drive folders or Google Slides.

## rclone Copy Policy

Using `rclone` to copy files or folders to Google Drive is allowed when that is the right tool for the job. Do not treat the gws CLI's current-directory upload constraint as a global prohibition.

- Source files may be outside the current repository when `rclone` supports that path.
- Keep the public-safety rules: do not copy `非公開/`, credentials, customer data, internal sales details, or source PDFs unless the user explicitly asks for a private Drive-only transfer.
- Use the intended Google Drive destination folder, and avoid creating duplicates when the destination already has the same file/folder.
- For native Google Slides generation with speaker notes, keep using this script and `gws` unless the user asks for a raw file/folder copy.

## Workflow

1. Confirm target session/course from the user's request.
2. Check local inputs:
   - `スライド画像/Sxx.png` exists and is non-empty.
   - `講師台本.md` has `Sxx「...」` blocks.
   - `スライド案.md` and `演習データ/` exist when the user requested full session materials.
3. Run `--dry-run` first for a new course or ambiguous target.
4. Run the export command.
5. Read the command output and report:
   - root/course/session folder names
   - created Google Slides title
   - uploaded or skipped `講師台本.md`, `スライド案.md`, and exercise-data files
   - deck URL, unless the user requested not to display it
   - any missing notes or slide-count warnings

### Workflow (Google Slides replacement after slide-image updates)

When local `スライド画像/Sxx.png` have been regenerated and the user wants Drive/Google Slides updated, use replacement rather than creating duplicate decks.

1. Confirm the target course/session and ensure the local slide images are the approved final raster images from the course workflow.
2. Run `gws auth status`. If auth is invalid, stop and ask the user to authenticate.
3. Run a dry-run against the target course/session to verify local slide counts, speaker-note blocks, and Drive folder names.
4. Use the same Drive root/course/session folder names as the prior export. Do not create a new course folder just because the public-facing training name changed; the repository course folder remains the stable Drive path unless the user explicitly asks to move it.
5. Run the exporter with `--replace-existing-decks` and `--report-json` under `非公開/`. If the user wants a shareable link list, also add `--write-link-index`.
6. The exporter deletes only Google Slides files with the same deck title inside each target session folder, then uploads a new image-based Google Slides deck from the current local images and inserts speaker notes.
7. Keep replacement reports under `非公開/`. When `--write-link-index` is used, review and commit only `講座/COURSE/全体/Google_Driveリンク一覧.md` as the public sharing index.
8. After export, verify each returned deck has the expected page count. If a conversion or speaker-note insertion warning appears, report it and rerun only the affected session after fixing the local source.

Recommended full-course replacement command:

```bash
python3 skills/gws-ai-training-slide-exporter/scripts/export_ai_training_slides_to_gws.py \
  --course-dir '講座/COURSE' \
  --all-sessions \
  --replace-existing-decks \
  --write-link-index \
  --report-json '非公開/gws-exports/COURSE/replace-report.json'
```

### Workflow (Canva image-first branch)

1. Confirm target course/session and request scope (session-only / full-course / selected sessions).
2. Check `スライド画像/` completeness and slide numbering sequence (`--dry-run` first).
3. Create one image-based presentation per session:
   - Preferred local bundle: run `--canva-pptx-dir` and import each PPTX into Canva.
   - API route: upload the slide images or PPTX through Canva Connect API and create one multi-page design per session.
4. Before browser editing, verify the Canva presentation has every page in `Sxx` order from first to last.
5. Move or organize the created presentation into the matching Canva course/session folder.
6. Create a private edit plan that lists only pages needing manual Magic Layers:
   - title/cover, section dividers, company/date/instructor placeholders, curriculum tables, customer-specific case pages.
   - leave fixed diagrams, screenshots, screen-share transition pages, exercise instructions, and summaries as images.
7. If the user explicitly requested browser Magic Layers, run the Phase 3B page-by-page verification loop and record results under `非公開/Canva/`.
8. Store only private indexes:
   - `非公開/Canva/<講座名>_Canva_URL一覧.csv` — session-level presentation summary.
   - `非公開/Canva/<講座名>_Magic_Layers対象ページ.md` — manual Magic Layers page list and notes.
   - `非公開/Canva/<講座名>_Magic_Layers検証ログ.csv` — browser Magic Layers page status when used.
   - Google Drive sync folder: `Canva_URL一覧.csv`.
9. Verify page counts per session, import quality, Magic Layers status for targeted pages, and that no Canva URLs or IDs were written to public tracked files.

### Workflow (Legacy all-page Magic Layers branch)

Use this branch only when the user explicitly asks to Magic Layers-convert every slide.

1. Confirm target course/session and request scope.
2. Check `スライド画像/` completeness and slide numbering sequence (`--dry-run` first).
3. Create or verify the Canva folder hierarchy with `_create_folder`.
4. For each slide image in session order (S01→Sxx):
   - Call `_image_to_design` with `image_file` (absolute path) and a title like `01-S01_セッション名`.
   - Move the created one-page design to the matching session folder.
   - On failure: retry once, then mark failed in JSONL and continue.
5. Generate or update `非公開/Canva/google_workspace_canva_rename_titles_plan.json` from the successful Magic Layers logs.
6. Use Canva Connect API merge to create one multi-page design per session:
   - Run `merge_magic_layers_designs.py --dry-run` first.
   - Run `merge_magic_layers_designs.py` with `CANVA_ACCESS_TOKEN`.
   - Save results to `非公開/Canva/google_workspace_canva_merge_results.json`.
7. Aggregate private/public indexes and verify page counts.

### Output artifacts (Canva image-first route)

- `非公開/Canva/`:
  - `<講座名>_Canva_URL一覧.csv`（回ごとのプレゼンテーションURL一覧）
  - `<講座名>_Magic_Layers対象ページ.md`（手動Magic Layers化するページの一覧）
- Google Drive sync root/course folder:
  - `Canva_URL一覧.csv`（`session_no,session_name,course_name,presentation_design_id,edit_url,view_url,page_count,magic_layers_pages,notes`）

### Rebuild command (Legacy all-page Magic Layers route)

JSONLログが確定したら再集計:

```bash
python3 非公開/Canva/<課題名>/aggregate_urls.py
```

実URL、folder ID、design IDをハードコードする集計スクリプトはpublicリポジトリ配下に置かない。

## Implementation Notes

The script avoids public image URLs. It first creates/reuses Drive folders and uploads session Markdown/CSV/sample exercise files. It then builds a temporary PPTX locally from the PNG slide images, uploads the PPTX through `gws drive files create`, and asks Drive to convert it into a native Google Slides presentation. After conversion, it calls `gws slides presentations get` to find each speaker-notes object and `gws slides presentations batchUpdate` to insert the matching script text.

Do not replace this with HTML/SVG/browser screenshots. The goal is to preserve the already generated slide images exactly as slide pages.

### Notes for Canva Route

- **標準フローは「画像ベースの複数ページプレゼンを先に作る → 必要ページだけCanva上で手動Magic Layers化」**。
- Canva MCP/APIまたはPPTX取り込みで、先に1本の複数ページプレゼンテーションを作る。ブラウザ操作は、その完成済みプレゼンを開いて必要ページだけ検証しながら編集する段階に限定する。
- 品質維持のため、`references/canva-quality-checklist.md` の推奨設定と検証観点を使う。新しい失敗パターンを見つけたら同ファイルへ追記する。
- `--canva-pptx-dir` はCanva単一プレゼン取り込み用の標準的な中間成果物として使う。
- `_image_to_design` による1枚ずつのMagic Layers化と `/v1/merges` による結合は、全ページ編集可能化が明示された場合だけ使う高コスト例外ルート。
- フォルダー作成は `/v1/folders`、完成デザインの移動は `/v1/folders/move` を使う。必要スコープは `folder:read` と `folder:write`。
- 写真・スクリーンショット系スライドはMagic Layersの分解精度が低下する場合があるため、原則として画像のまま残す。
- Magic Layers後の文字化け、文言変化、レイアウト崩れは成功扱いにしない。戻す、再試行する、画像ページのまま残す、手動修正に回す、のいずれかをページ単位で判断する。同一ページで3回以上失敗したらMagic Layersを諦め、元画像を採用する。
- Canva URLはすべて `非公開/` のみに保存し、publicリポジトリには書かない。
