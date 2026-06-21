#!/usr/bin/env python3
"""演習データを Google Workspace 上に作成する。

1つの回（セッション）の `演習データ/` から:

- `*.csv` を1つの Google スプレッドシートにまとめる。CSV が複数ある場合は、
  CSV ごとにシート（タブ）を追加し、1回につき演習用スプレッドシートを1つにする。
- ワークシート系（`*.md` / `*.txt`）は Google ドキュメントとして1ファイルずつ作成する。
- 作成したスプレッドシート・ドキュメントは、Google ドライブの「演習データ」
  フォルダの中に入れる。

ドライブ操作・ファイル作成は外部送信を伴うため、まず `--dry-run` で確認し、
ユーザー承認後に本実行する。

依存: `gws`（Google Workspace CLI）が認証済みであること。

例:
    # 1) どう作られるか確認（API を呼ばない）
    python3 build_exercise_gws_docs.py \
        --session-dir '講座/COURSE/01-セッション名' --dry-run

    # 2) 演習データの Drive フォルダ ID を直接指定して本実行
    python3 build_exercise_gws_docs.py \
        --session-dir '講座/COURSE/01-セッション名' \
        --drive-folder-id 1AbCxyz...

    # 3) ルートフォルダから 講座名/回名/演習データ を自動で辿って作成
    python3 build_exercise_gws_docs.py \
        --session-dir '講座/COURSE/01-セッション名' \
        --root-folder-id 1RootXyz...
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

FOLDER_MIME = "application/vnd.google-apps.folder"
WORKSHEET_SUFFIXES = {".md", ".txt"}
# Sheets のタブ名・Drive の名前で問題になりやすい文字
TAB_FORBIDDEN = re.compile(r"[\[\]\*/\\\?:]")


class BuildError(RuntimeError):
    pass


# ---------------------------------------------------------------------------
# gws 呼び出し
# ---------------------------------------------------------------------------

def run_gws(args: list[str], *, dry_run: bool, label: str) -> dict[str, Any]:
    """gws を実行し JSON を返す。dry_run のときは呼ばずにダミーを返す。"""
    if dry_run:
        print(f"[dry-run] gws {' '.join(args)}", file=sys.stderr)
        return {}
    proc = subprocess.run(
        ["gws", *args],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise BuildError(f"gws {label} failed: {proc.stderr.strip() or proc.stdout.strip()}")
    out = proc.stdout.strip()
    if not out:
        return {}
    try:
        return json.loads(out)
    except json.JSONDecodeError as exc:
        raise BuildError(f"gws {label} returned non-JSON: {out[:200]}") from exc


def drive_literal(value: str) -> str:
    return "'" + value.replace("\\", "\\\\").replace("'", "\\'") + "'"


# ---------------------------------------------------------------------------
# Drive フォルダ解決
# ---------------------------------------------------------------------------

def find_folder(name: str, parent_id: str | None, *, dry_run: bool) -> dict[str, Any] | None:
    q = f"name = {drive_literal(name)} and mimeType = {drive_literal(FOLDER_MIME)} and trashed = false"
    if parent_id:
        q += f" and {drive_literal(parent_id)} in parents"
    res = run_gws(
        ["drive", "files", "list", "--params", json.dumps({"q": q, "fields": "files(id,name)"})],
        dry_run=dry_run,
        label="files.list",
    )
    files = res.get("files", []) if res else []
    if len(files) > 1:
        raise BuildError(f"Drive フォルダ名が重複しています: {name}。--drive-folder-id で直接指定してください。")
    return files[0] if files else None


def ensure_folder(name: str, parent_id: str | None, *, dry_run: bool) -> dict[str, Any]:
    existing = find_folder(name, parent_id, dry_run=dry_run)
    if existing:
        return existing
    body: dict[str, Any] = {"name": name, "mimeType": FOLDER_MIME}
    if parent_id:
        body["parents"] = [parent_id]
    created = run_gws(
        ["drive", "files", "create", "--json", json.dumps(body), "--params", json.dumps({"fields": "id,name"})],
        dry_run=dry_run,
        label="files.create(folder)",
    )
    if dry_run:
        return {"id": f"dryrun-folder-{name}", "name": name}
    return created


def resolve_exercise_folder(session_dir: Path, *, drive_folder_id: str | None, root_folder_id: str | None, dry_run: bool) -> str:
    """演習データを入れる Drive フォルダ ID を返す。"""
    if drive_folder_id:
        return drive_folder_id
    if not root_folder_id:
        raise BuildError("--drive-folder-id か --root-folder-id のどちらかを指定してください。")
    # root/講座名/回名/演習データ を辿る（無ければ作成）
    course_name = session_dir.parent.name
    session_name = session_dir.name
    course_folder = ensure_folder(course_name, root_folder_id, dry_run=dry_run)
    session_folder = ensure_folder(session_name, course_folder.get("id"), dry_run=dry_run)
    exercise_folder = ensure_folder("演習データ", session_folder.get("id"), dry_run=dry_run)
    return exercise_folder.get("id", f"dryrun-folder-演習データ")


def move_into_folder(file_id: str, folder_id: str, *, dry_run: bool) -> None:
    """新規作成ファイル（My Drive 直下）を演習データフォルダへ移動する。"""
    run_gws(
        [
            "drive", "files", "update",
            "--params", json.dumps({"fileId": file_id, "addParents": folder_id, "removeParents": "root", "fields": "id,parents"}),
        ],
        dry_run=dry_run,
        label="files.update(move)",
    )


# ---------------------------------------------------------------------------
# CSV → スプレッドシート
# ---------------------------------------------------------------------------

def sanitize_tab_name(stem: str, used: set[str]) -> str:
    name = TAB_FORBIDDEN.sub(" ", stem).strip() or "シート"
    name = name[:100]
    base = name
    i = 2
    while name in used:
        suffix = f"_{i}"
        name = base[: 100 - len(suffix)] + suffix
        i += 1
    used.add(name)
    return name


def read_csv_rows(path: Path) -> list[list[str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return [list(row) for row in csv.reader(f)]


def build_spreadsheet(csv_paths: list[Path], title: str, folder_id: str, *, dry_run: bool) -> dict[str, Any]:
    used: set[str] = set()
    tab_for_csv = [(p, sanitize_tab_name(p.stem, used)) for p in csv_paths]

    create_body = {
        "properties": {"title": title},
        "sheets": [{"properties": {"title": tab}} for _, tab in tab_for_csv],
    }
    created = run_gws(
        ["sheets", "spreadsheets", "create", "--json", json.dumps(create_body)],
        dry_run=dry_run,
        label="spreadsheets.create",
    )
    spreadsheet_id = created.get("spreadsheetId") if created else None
    if dry_run:
        spreadsheet_id = f"dryrun-sheet-{title}"

    # 各タブに CSV の中身を書き込む
    data = []
    for path, tab in tab_for_csv:
        rows = read_csv_rows(path)
        if not rows:
            continue
        data.append({"range": f"'{tab}'!A1", "values": rows})
    if data and not dry_run:
        run_gws(
            [
                "sheets", "spreadsheets", "values", "batchUpdate",
                "--params", json.dumps({"spreadsheetId": spreadsheet_id}),
                "--json", json.dumps({"valueInputOption": "RAW", "data": data}),
            ],
            dry_run=dry_run,
            label="values.batchUpdate",
        )
    elif dry_run:
        for path, tab in tab_for_csv:
            print(f"[dry-run] '{tab}' <- {path.name}", file=sys.stderr)

    if spreadsheet_id:
        move_into_folder(spreadsheet_id, folder_id, dry_run=dry_run)
    return {
        "type": "spreadsheet",
        "title": title,
        "spreadsheetId": spreadsheet_id,
        "tabs": [tab for _, tab in tab_for_csv],
        "url": f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit" if spreadsheet_id and not dry_run else None,
    }


# ---------------------------------------------------------------------------
# ワークシート → Google ドキュメント
# ---------------------------------------------------------------------------

def build_document(path: Path, folder_id: str, *, dry_run: bool) -> dict[str, Any]:
    title = path.stem
    created = run_gws(
        ["docs", "documents", "create", "--json", json.dumps({"title": title})],
        dry_run=dry_run,
        label="documents.create",
    )
    doc_id = created.get("documentId") if created else None
    if dry_run:
        doc_id = f"dryrun-doc-{title}"

    text = path.read_text(encoding="utf-8")
    if text and not dry_run:
        run_gws(
            [
                "docs", "documents", "batchUpdate",
                "--params", json.dumps({"documentId": doc_id}),
                "--json", json.dumps({"requests": [{"insertText": {"location": {"index": 1}, "text": text}}]}),
            ],
            dry_run=dry_run,
            label="documents.batchUpdate",
        )

    if doc_id:
        move_into_folder(doc_id, folder_id, dry_run=dry_run)
    return {
        "type": "document",
        "title": title,
        "documentId": doc_id,
        "source": path.name,
        "url": f"https://docs.google.com/document/d/{doc_id}/edit" if doc_id and not dry_run else None,
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="演習データを Google スプレッドシート/ドキュメントとして作成する")
    p.add_argument("--session-dir", required=True, help="回（セッション）フォルダのパス")
    p.add_argument("--drive-folder-id", help="作成物を入れる演習データ Drive フォルダ ID（最優先）")
    p.add_argument("--root-folder-id", help="講座/回/演習データ を辿る起点の Drive フォルダ ID")
    p.add_argument("--sheet-title", help="スプレッドシートのタイトル（既定: <回名>_演習データ）")
    p.add_argument("--dry-run", action="store_true", help="API を呼ばず、作成内容だけ表示する")
    return p.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    session_dir = Path(args.session_dir)
    exercise_dir = session_dir / "演習データ"
    if not exercise_dir.is_dir():
        raise BuildError(f"演習データフォルダがありません: {exercise_dir}")

    files = sorted(p for p in exercise_dir.iterdir() if p.is_file())
    csv_paths = [p for p in files if p.suffix.lower() == ".csv"]
    worksheet_paths = [p for p in files if p.suffix.lower() in WORKSHEET_SUFFIXES and p.name.lower() != "readme.md"]

    if not csv_paths and not worksheet_paths:
        raise BuildError(f"CSV もワークシート（.md/.txt）も見つかりません: {exercise_dir}")

    folder_id = resolve_exercise_folder(
        session_dir,
        drive_folder_id=args.drive_folder_id,
        root_folder_id=args.root_folder_id,
        dry_run=args.dry_run,
    )

    results: list[dict[str, Any]] = []
    if csv_paths:
        title = args.sheet_title or f"{session_dir.name}_演習データ"
        results.append(build_spreadsheet(csv_paths, title, folder_id, dry_run=args.dry_run))
    for path in worksheet_paths:
        results.append(build_document(path, folder_id, dry_run=args.dry_run))

    summary = {
        "sessionDir": str(session_dir),
        "exerciseFolderId": folder_id,
        "dryRun": args.dry_run,
        "created": results,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except BuildError as exc:
        print(f"エラー: {exc}", file=sys.stderr)
        sys.exit(1)
