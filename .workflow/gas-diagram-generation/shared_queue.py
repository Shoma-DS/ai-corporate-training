#!/usr/bin/env python3
"""File-locked shared queue for GAS diagram image generation workers."""

from __future__ import annotations

import argparse
import fcntl
import json
import mimetypes
import sys
import time
import uuid
from collections import Counter
from contextlib import contextmanager
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
SOURCE_QUEUE = ROOT / "queue.jsonl"
STATE_FILE = ROOT / "shared-queue-state.json"
LOCK_FILE = ROOT / "shared-queue.lock"


def now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


@contextmanager
def locked_state() -> Any:
    LOCK_FILE.touch()
    with LOCK_FILE.open("r+", encoding="utf-8") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "updated_at": now(), "tasks": []}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    data["updated_at"] = now()
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def load_source_tasks() -> list[dict[str, Any]]:
    tasks: list[dict[str, Any]] = []
    for line in SOURCE_QUEUE.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        item["task_id"] = f"{item['session_no']}-{item['slide_id']}"
        item["status"] = "pending"
        item["worker"] = None
        item["claim_token"] = None
        item["attempts"] = 0
        item["claimed_at"] = None
        item["completed_at"] = None
        item["failed_at"] = None
        item["note"] = None
        tasks.append(item)
    return tasks


def looks_like_png(path: Path) -> bool:
    if not path.exists() or path.stat().st_size == 0:
        return False
    guessed = mimetypes.guess_type(path.name)[0]
    try:
        with path.open("rb") as fh:
            signature = fh.read(8)
    except OSError:
        return False
    return guessed == "image/png" and signature == b"\x89PNG\r\n\x1a\n"


def cmd_init(args: argparse.Namespace) -> None:
    threshold = None
    if args.mark_existing_newer_than:
        threshold = time.mktime(time.strptime(args.mark_existing_newer_than, "%Y-%m-%d %H:%M:%S"))
    tasks = load_source_tasks()
    marked = 0
    if threshold is not None:
        for task in tasks:
            target = Path(task["target"])
            if looks_like_png(target) and target.stat().st_mtime >= threshold:
                task["status"] = "complete"
                task["worker"] = "preexisting-after-threshold"
                task["completed_at"] = now()
                task["note"] = f"Existing PNG newer than {args.mark_existing_newer_than}"
                marked += 1
    state = {"version": 1, "created_at": now(), "updated_at": now(), "tasks": tasks}
    with locked_state():
        if STATE_FILE.exists() and not args.force:
            raise SystemExit(f"{STATE_FILE} already exists; use --force to rebuild it")
        write_json(STATE_FILE, state)
    print(json.dumps({"ok": True, "tasks": len(tasks), "marked_complete": marked}, ensure_ascii=False))


def reset_stale_claims(state: dict[str, Any], stale_minutes: int) -> int:
    cutoff = time.time() - stale_minutes * 60
    reset = 0
    for task in state["tasks"]:
        if task["status"] != "claimed" or not task.get("claimed_at_epoch"):
            continue
        if task["claimed_at_epoch"] < cutoff:
            task["status"] = "pending"
            task["note"] = f"Reset stale claim from {task.get('worker')}"
            task["worker"] = None
            task["claim_token"] = None
            task["claimed_at"] = None
            task["claimed_at_epoch"] = None
            reset += 1
    return reset


def cmd_claim(args: argparse.Namespace) -> None:
    with locked_state():
        state = read_json(STATE_FILE)
        reset = reset_stale_claims(state, args.stale_minutes) if args.stale_minutes else 0
        selected = None
        for task in state["tasks"]:
            if task["status"] == "pending":
                selected = task
                break
        if not selected:
            write_json(STATE_FILE, state)
            print(json.dumps({"ok": True, "status": "empty", "stale_reset": reset}, ensure_ascii=False))
            return
        token = str(uuid.uuid4())
        selected["status"] = "claimed"
        selected["worker"] = args.worker
        selected["claim_token"] = token
        selected["attempts"] = int(selected.get("attempts") or 0) + 1
        selected["claimed_at"] = now()
        selected["claimed_at_epoch"] = time.time()
        selected["note"] = None
        write_json(STATE_FILE, state)
        print(json.dumps({"ok": True, "status": "claimed", "task": selected, "stale_reset": reset}, ensure_ascii=False))


def find_task(state: dict[str, Any], task_id: str) -> dict[str, Any]:
    for task in state["tasks"]:
        if task["task_id"] == task_id:
            return task
    raise SystemExit(f"Unknown task_id: {task_id}")


def guard_claim(task: dict[str, Any], args: argparse.Namespace) -> None:
    if task.get("worker") != args.worker:
        raise SystemExit(f"Task {task['task_id']} is owned by {task.get('worker')}, not {args.worker}")
    if args.claim_token and task.get("claim_token") != args.claim_token:
        raise SystemExit(f"Task {task['task_id']} claim token mismatch")


def cmd_complete(args: argparse.Namespace) -> None:
    target = Path(args.target) if args.target else None
    if target and not looks_like_png(target):
        raise SystemExit(f"Target is not a valid PNG: {target}")
    with locked_state():
        state = read_json(STATE_FILE)
        task = find_task(state, args.task_id)
        guard_claim(task, args)
        task["status"] = "complete"
        task["completed_at"] = now()
        task["failed_at"] = None
        task["claim_token"] = None
        task["note"] = args.note
        write_json(STATE_FILE, state)
    print(json.dumps({"ok": True, "status": "complete", "task_id": args.task_id}, ensure_ascii=False))


def cmd_fail(args: argparse.Namespace) -> None:
    with locked_state():
        state = read_json(STATE_FILE)
        task = find_task(state, args.task_id)
        guard_claim(task, args)
        task["status"] = "pending" if args.requeue else "failed"
        task["failed_at"] = now()
        task["claim_token"] = None
        task["note"] = args.note
        if args.requeue:
            task["worker"] = None
            task["claimed_at"] = None
            task["claimed_at_epoch"] = None
        write_json(STATE_FILE, state)
    print(json.dumps({"ok": True, "status": task["status"], "task_id": args.task_id}, ensure_ascii=False))


def cmd_status(args: argparse.Namespace) -> None:
    state = read_json(STATE_FILE)
    counts = Counter(task["status"] for task in state["tasks"])
    by_worker = Counter(task.get("worker") or "unassigned" for task in state["tasks"] if task["status"] == "complete")
    pending = [task["task_id"] for task in state["tasks"] if task["status"] == "pending"][: args.sample]
    claimed = [
        {"task_id": task["task_id"], "worker": task.get("worker"), "claimed_at": task.get("claimed_at")}
        for task in state["tasks"]
        if task["status"] == "claimed"
    ][: args.sample]
    print(
        json.dumps(
            {
                "ok": True,
                "total": len(state["tasks"]),
                "counts": dict(counts),
                "complete_by_worker": dict(by_worker),
                "pending_sample": pending,
                "claimed_sample": claimed,
                "updated_at": state.get("updated_at"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def cmd_sync_existing(args: argparse.Namespace) -> None:
    threshold = time.mktime(time.strptime(args.mark_existing_newer_than, "%Y-%m-%d %H:%M:%S"))
    changed = 0
    skipped_claimed = 0
    with locked_state():
        state = read_json(STATE_FILE)
        for task in state["tasks"]:
            if task["status"] == "claimed":
                skipped_claimed += 1
                continue
            if task["status"] == "complete" and not args.force_complete:
                continue
            target = Path(task["target"])
            if looks_like_png(target) and target.stat().st_mtime >= threshold:
                task["status"] = "complete"
                task["worker"] = task.get("worker") or "sync-existing"
                task["claim_token"] = None
                task["completed_at"] = task.get("completed_at") or now()
                task["failed_at"] = None
                task["note"] = f"Synced existing PNG newer than {args.mark_existing_newer_than}"
                changed += 1
        write_json(STATE_FILE, state)
    print(json.dumps({"ok": True, "synced_complete": changed, "skipped_claimed": skipped_claimed}, ensure_ascii=False))


def cmd_reset_stale(args: argparse.Namespace) -> None:
    with locked_state():
        state = read_json(STATE_FILE)
        reset = reset_stale_claims(state, args.stale_minutes)
        write_json(STATE_FILE, state)
    print(json.dumps({"ok": True, "stale_reset": reset}, ensure_ascii=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    init = sub.add_parser("init")
    init.add_argument("--force", action="store_true")
    init.add_argument("--mark-existing-newer-than")
    init.set_defaults(func=cmd_init)

    claim = sub.add_parser("claim")
    claim.add_argument("--worker", required=True)
    claim.add_argument("--stale-minutes", type=int, default=0)
    claim.set_defaults(func=cmd_claim)

    complete = sub.add_parser("complete")
    complete.add_argument("--worker", required=True)
    complete.add_argument("--task-id", required=True)
    complete.add_argument("--claim-token")
    complete.add_argument("--target")
    complete.add_argument("--note")
    complete.set_defaults(func=cmd_complete)

    fail = sub.add_parser("fail")
    fail.add_argument("--worker", required=True)
    fail.add_argument("--task-id", required=True)
    fail.add_argument("--claim-token")
    fail.add_argument("--note", required=True)
    fail.add_argument("--requeue", action="store_true")
    fail.set_defaults(func=cmd_fail)

    status = sub.add_parser("status")
    status.add_argument("--sample", type=int, default=10)
    status.set_defaults(func=cmd_status)

    sync = sub.add_parser("sync-existing")
    sync.add_argument("--mark-existing-newer-than", required=True)
    sync.add_argument("--force-complete", action="store_true")
    sync.set_defaults(func=cmd_sync_existing)

    reset_stale = sub.add_parser("reset-stale")
    reset_stale.add_argument("--stale-minutes", type=int, required=True)
    reset_stale.set_defaults(func=cmd_reset_stale)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        args.func(args)
    except BrokenPipeError:
        sys.exit(1)


if __name__ == "__main__":
    main()
