#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any


REPO = Path("/Users/deguchishouma/Desktop/AI法人研修")
PRIVATE_DIR = REPO / "非公開/Canva"
PLAN_PATH = PRIVATE_DIR / "google_workspace_canva_rename_titles_plan.json"
OUT_PATH = PRIVATE_DIR / "google_workspace_canva_merge_results.json"
API_BASE = "https://api.canva.com/rest/v1"


SESSION_TITLES = {
    "01": "01-業務DXの基礎とGoogle Workspace活用設計",
    "02": "02-業務データ基盤の設計",
    "03": "03-GASによる業務プロセス自動化",
    "04": "04-Gem-Geminiを使った文書作成-分類-要約",
    "05": "05-AI-GAS自動化の要件定義-運用設計",
    "06": "06-AI業務効率化プロジェクト提案書の作成",
}


class CanvaApiError(RuntimeError):
    pass


def log(message: str) -> None:
    print(message, file=sys.stderr, flush=True)


def progress_bar(done: int, total: int, width: int = 24) -> str:
    filled = int(width * done / total) if total else width
    return "[" + "#" * filled + "-" * (width - filled) + f"] {done}/{total}"


def slide_no(value: str) -> int:
    try:
        return int(str(value).upper().replace("S", ""))
    except ValueError:
        return 9999


def request_json(
    method: str,
    path: str,
    token: str,
    body: dict[str, Any] | None = None,
    *,
    attempts: int = 8,
) -> dict[str, Any]:
    data = None if body is None else json.dumps(body, ensure_ascii=False).encode("utf-8")
    headers = {"Authorization": f"Bearer {token}"}
    if body is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(f"{API_BASE}{path}", data=data, headers=headers, method=method)
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as res:
                raw = res.read().decode("utf-8")
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as exc:
            message = exc.read().decode("utf-8", errors="replace")
            if exc.code == 429 and attempt < attempts:
                retry_after = exc.headers.get("Retry-After")
                wait_seconds = float(retry_after) if retry_after else min(60.0, 5.0 * attempt)
                log(f"rate limited: {method} {path}; retrying in {wait_seconds:.0f}s ({attempt}/{attempts})")
                time.sleep(wait_seconds)
                continue
            raise CanvaApiError(f"{method} {path} failed: HTTP {exc.code}\n{message}") from exc
    raise CanvaApiError(f"{method} {path} failed after {attempts} attempts")


def create_folder(token: str, name: str, parent_folder_id: str = "root") -> dict[str, Any]:
    return request_json(
        "POST",
        "/folders",
        token,
        {
            "name": name,
            "parent_folder_id": parent_folder_id,
        },
    )


def move_to_folder(token: str, item_id: str, folder_id: str) -> dict[str, Any]:
    return request_json(
        "POST",
        "/folders/move",
        token,
        {
            "to_folder_id": folder_id,
            "item_id": item_id,
        },
    )


def result_design_id(result: dict[str, Any]) -> str:
    job = result.get("final_response", {}).get("job", {})
    design = job.get("result", {}).get("design", {})
    return design.get("id") or ""


def load_plan(path: Path) -> list[dict[str, Any]]:
    rows = json.loads(path.read_text(encoding="utf-8"))
    return [row for row in rows if row.get("design_id") and row.get("session_no") and row.get("slide")]


def group_sessions(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["session_no"])].append(row)
    return {
        session_no: sorted(items, key=lambda row: slide_no(str(row.get("slide", ""))))
        for session_no, items in sorted(grouped.items())
    }


def build_insert_operation(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "type": "insert_pages",
        "source": {
            "type": "design",
            "design_id": row["design_id"],
            "page_numbers": [1],
        },
    }


def build_create_payload(session_no: str, row: dict[str, Any]) -> dict[str, Any]:
    return {
        "type": "create_new_design",
        "operations": [build_insert_operation(row)],
        "title": SESSION_TITLES.get(session_no, f"{session_no}-merged-canva-design"),
    }


def build_modify_payload(design_id: str, row: dict[str, Any]) -> dict[str, Any]:
    return {
        "type": "modify_existing_design",
        "design_id": design_id,
        "operations": [build_insert_operation(row)],
    }


def wait_for_job(token: str, job_id: str, *, poll_seconds: float, timeout_seconds: float) -> dict[str, Any]:
    deadline = time.time() + timeout_seconds
    while True:
        result = request_json("GET", f"/merges/{job_id}", token)
        job = result.get("job", {})
        if job.get("status") in {"success", "failed"}:
            return result
        if time.time() >= deadline:
            raise CanvaApiError(f"Timed out waiting for merge job: {job_id}")
        time.sleep(poll_seconds)


def merge_session(
    token: str,
    session_no: str,
    rows: list[dict[str, Any]],
    *,
    dry_run: bool,
    poll_seconds: float,
    timeout_seconds: float,
    folder_id: str | None,
) -> dict[str, Any]:
    if not rows:
        raise CanvaApiError(f"No rows to merge for session {session_no}")
    create_payload = build_create_payload(session_no, rows[0])
    if dry_run:
        modify_payloads = [
            build_modify_payload("DRY_RUN_CREATED_DESIGN_ID", row)
            for row in rows[1:]
        ]
        return {
            "session_no": session_no,
            "title": create_payload["title"],
            "source_count": len(rows),
            "dry_run": True,
            "payloads": [create_payload, *modify_payloads],
        }

    created = request_json("POST", "/merges", token, create_payload)
    log(f"{session_no} {progress_bar(0, len(rows))} create deck from {rows[0].get('slide')}")
    job = created.get("job", {})
    job_id = job.get("id")
    if not job_id:
        raise CanvaApiError(f"Merge job response did not include job.id: {created}")
    completed = wait_for_job(token, job_id, poll_seconds=poll_seconds, timeout_seconds=timeout_seconds)
    design_id = result_design_id({"final_response": completed})
    if not design_id:
        raise CanvaApiError(f"Initial merge job did not return a design ID for session {session_no}: {completed}")
    log(f"{session_no} {progress_bar(1, len(rows))} added {rows[0].get('slide')}")
    modify_steps = []
    for index, row in enumerate(rows[1:], start=2):
        log(f"{session_no} {progress_bar(index - 1, len(rows))} adding {row.get('slide')}")
        payload = build_modify_payload(design_id, row)
        step_created = request_json("POST", "/merges", token, payload)
        step_job = step_created.get("job", {})
        step_job_id = step_job.get("id")
        if not step_job_id:
            raise CanvaApiError(f"Merge job response did not include job.id: {step_created}")
        step_completed = wait_for_job(token, step_job_id, poll_seconds=poll_seconds, timeout_seconds=timeout_seconds)
        modify_steps.append(
            {
                "slide": row.get("slide"),
                "source_design_id": row.get("design_id"),
                "create_response": step_created,
                "final_response": step_completed,
            }
        )
        log(f"{session_no} {progress_bar(index, len(rows))} added {row.get('slide')}")
    result = {
        "session_no": session_no,
        "title": create_payload["title"],
        "source_count": len(rows),
        "create_response": created,
        "final_response": completed,
        "modify_steps": modify_steps,
    }
    if folder_id:
        log(f"{session_no} moving merged deck to folder {folder_id}")
        result["folder_move_response"] = move_to_folder(token, design_id, folder_id)
        result["folder_id"] = folder_id
        log(f"{session_no} moved merged deck to folder {folder_id}")
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Merge one-page Canva Magic Layers designs into session decks.")
    parser.add_argument("--plan", default=str(PLAN_PATH), help="JSON plan containing design_id/session_no/slide rows")
    parser.add_argument("--out", default=str(OUT_PATH), help="Private JSON output path for merge results")
    parser.add_argument("--session", action="append", help="Session number to merge, e.g. 01. Repeatable.")
    parser.add_argument("--dry-run", action="store_true", help="Write planned Canva merge payloads without calling Canva")
    parser.add_argument("--poll-seconds", type=float, default=3.0, help="Polling interval for merge jobs")
    parser.add_argument("--timeout-seconds", type=float, default=600.0, help="Timeout per merge job")
    parser.add_argument("--folder-id", help="Move each merged presentation into this Canva folder ID")
    parser.add_argument("--create-folder", help="Create this Canva folder first, then move merged presentations into it")
    parser.add_argument("--parent-folder-id", default="root", help="Parent folder ID for --create-folder. Defaults to root.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    token = os.environ.get("CANVA_ACCESS_TOKEN", "")
    if not token and not args.dry_run:
        print("ERROR: Set CANVA_ACCESS_TOKEN with design:content:write and design:meta:read scopes.", file=sys.stderr)
        return 2

    plan = load_plan(Path(args.plan))
    grouped = group_sessions(plan)
    wanted = set(args.session or grouped.keys())
    folder_id = args.folder_id
    folder_create_response = None
    if args.create_folder:
        if args.dry_run:
            folder_id = "DRY_RUN_FOLDER_ID"
            folder_create_response = {
                "dry_run": True,
                "folder": {"id": folder_id, "name": args.create_folder, "parent_folder_id": args.parent_folder_id},
            }
        else:
            folder_create_response = create_folder(token, args.create_folder, args.parent_folder_id)
            folder_id = folder_create_response.get("folder", {}).get("id")
            if not folder_id:
                raise CanvaApiError(f"Create folder response did not include folder.id: {folder_create_response}")

    results = []
    for session_no, rows in grouped.items():
        if session_no not in wanted:
            continue
        results.append(
            merge_session(
                token,
                session_no,
                rows,
                dry_run=args.dry_run,
                poll_seconds=args.poll_seconds,
                timeout_seconds=args.timeout_seconds,
                folder_id=folder_id,
            )
        )

    output = {
        "folder_create_response": folder_create_response,
        "results": results,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {"sessions": len(results), "out": str(out), "dry_run": args.dry_run, "folder_id": folder_id or ""},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
