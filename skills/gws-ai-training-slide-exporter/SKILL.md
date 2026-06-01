---
name: gws-ai-training-slide-exporter
description: >-
  Use when exporting AI法人研修 course materials to Google Drive/Google Slides with gws CLI: create Drive folders, upload session materials, build Slides decks with speaker notes, or convert slide images into Canva presentations with Magic Layers (one presentation per session) via Canva MCP.
---

# GWS AI Training Slide Exporter

## Purpose

Publish local AI法人研修 session assets to Google Drive as structured course folders and Google Slides decks.

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

## Canva Route: Magic Layers済みデザインを回ごとに結合する

Canvaで「回ごと1本の複数ページプレゼンテーション」を作る場合は、この順番を使う。

```text
S01.png -> Canva MCP _image_to_design -> 1ページのMagic Layersデザイン
S02.png -> Canva MCP _image_to_design -> 1ページのMagic Layersデザイン
...
Canva Connect API /v1/merges -> 回ごと1本の複数ページデザイン
```

現行のCanva MCP `_image_to_design` は、1回の呼び出しで新しい独立デザインを作る。既存プレゼンテーションへページ追加しながらMagic Layers化する用途には使わない。

### Phase 1: Canvaフォルダ階層

`_create_folder` で不足フォルダを作成し、フォルダIDを `state.json` または非公開メモに記録する。

```text
AI法人研修/
  講座名/
    01-セッション名/
    02-セッション名/
    ...
```

### Phase 2: 画像ごとにMagic Layers化

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

### Phase 3: Canva上のデザイン名を揃える

既存デザイン名を `回番号-Sxx_セッション名` にする。

```text
01-S01_01-業務DXの基礎とGoogle Workspace活用設計
01-S02_01-業務DXの基礎とGoogle Workspace活用設計
```

タイトル変更はCanva MCPの編集トランザクションで実施する:

```text
start_editing_transaction -> perform_editing_operations(update_title) -> commit_editing_transaction
```

### Phase 4: Canva Connect APIで回ごとに結合

Magic Layers化済みの1ページデザインを、Canva Connect API Design Mergeで回ごとに1本へまとめる。

Requirements:

- `CANVA_ACCESS_TOKEN`
- OAuth scopes: `design:content:write`, `design:meta:read`
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

All sessions:

```bash
CANVA_ACCESS_TOKEN="$CANVA_ACCESS_TOKEN" \
python3 .workflow/google-workspace-canva-magic-layers/merge_magic_layers_designs.py
```

Output:

- Input plan: `非公開/Canva/google_workspace_canva_rename_titles_plan.json`
- Result: `非公開/Canva/google_workspace_canva_merge_results.json`
- Use `final_response.job.result.design.urls.edit_url` and `view_url` as the merged presentation URLs.

### Phase 5: URL集約

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
- Do not save Google Drive file IDs, URLs, or customer-specific links into public tracked files unless the user explicitly asks.
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
- `--canva-pptx-dir`: output one PPTX per session for Canva single-presentation import workflows.

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

### Workflow (Canva MCP branch)

1. Confirm target course/session and request scope (session-only / full-course / selected sessions).
2. Check `スライド画像/` completeness and slide numbering sequence (`--dry-run` first).
3. Phase 1: Create or verify the Canva folder hierarchy with `_create_folder`.
4. Phase 2: For each slide image in session order (S01→Sxx):
   - Call `_image_to_design` with `image_file` (absolute path) and a title like `01-S01_セッション名`.
   - Move the created one-page design to the matching session folder.
   - On failure: retry once, then mark failed in JSONL and continue.
5. Phase 3: Generate or update `非公開/Canva/google_workspace_canva_rename_titles_plan.json` from the successful Magic Layers logs.
6. Phase 4: Use Canva Connect API merge to create one multi-page design per session:
   - Run `merge_magic_layers_designs.py --dry-run` first.
   - Run `merge_magic_layers_designs.py` with `CANVA_ACCESS_TOKEN`.
   - Save results to `非公開/Canva/google_workspace_canva_merge_results.json`.
7. Phase 5: Aggregate private/public indexes:
   - `非公開/Canva/<課題名>.jsonl` — per-slide Magic Layers log
   - `非公開/Canva/google_workspace_canva_merge_results.json` — merged session deck results
   - `非公開/Canva/<講座名>_Canva_URL一覧.csv` — session-level merged deck summary
   - Google Drive sync folder: `Canva_URL一覧.csv`
8. Verify page counts per session. Report failures and missing slides.

### Output artifacts (Canva route)

- `非公開/Canva/`:
  - `<講座名>.jsonl`（スライドごとの処理ログ）
  - `<講座名>_Canva_URL一覧.csv`（回ごとのプレゼンテーションURL一覧）
- Google Drive sync root/course folder:
  - `Canva_URL一覧.csv`（`session_no,session_name,course_name,presentation_design_id,edit_url,view_url,page_count,expected_count`）

### Rebuild command (Canva route)

JSONLログが確定したら再集計:

```bash
python3 .workflow/<課題名>/aggregate_urls.py
```

## Implementation Notes

The script avoids public image URLs. It first creates/reuses Drive folders and uploads session Markdown/CSV/sample exercise files. It then builds a temporary PPTX locally from the PNG slide images, uploads the PPTX through `gws drive files create`, and asks Drive to convert it into a native Google Slides presentation. After conversion, it calls `gws slides presentations get` to find each speaker-notes object and `gws slides presentations batchUpdate` to insert the matching script text.

Do not replace this with HTML/SVG/browser screenshots. The goal is to preserve the already generated slide images exactly as slide pages.

### Notes for Canva Route

- **標準フローは「1枚ずつMagic Layers化 → Canva Connect API mergeで回ごと1本化」**。
- `_image_to_design` は毎回新規呼び出しが必要。前回のデザイン状態の再利用や、既存プレゼンへのページ追加前提で運用しない。
- 複数ページ化には Canva Connect API `/v1/merges` を使う。必要スコープは `design:content:write` と `design:meta:read`。
- `--canva-pptx-dir` は補助用途（ローカルPPTX確認など）に残してある。
- 写真・スクリーンショット系スライドはMagic Layersの分解精度が低下する場合がある。品質確認パスを設けること。
- Canva URLはすべて `非公開/` のみに保存し、publicリポジトリには書かない。
