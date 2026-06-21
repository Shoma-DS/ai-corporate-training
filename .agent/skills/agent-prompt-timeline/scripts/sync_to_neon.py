#!/usr/bin/env python3
# Syncs local prompt-timeline JSONL events to the deployed Neon-backed ingest API.

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

import record_event


def ingest_url(args: argparse.Namespace, site: dict) -> str:
    if args.url:
        return args.url
    env_url = os.environ.get("PROMPT_TIMELINE_INGEST_URL", "").strip()
    if env_url:
        return env_url
    vercel_url = str(site.get("vercel_url") or "").strip()
    if vercel_url.startswith(("http://", "https://")):
        return f"{vercel_url.rstrip('/')}/api/timeline/events"
    return ""


def post_batch(url: str, token: str, repo_label: str, events: list[dict], timeout: float) -> dict:
    payload = json.dumps(
        {"repo_label": repo_label, "events": events},
        ensure_ascii=False,
    ).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "agent-prompt-timeline-sync/1",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read().decode("utf-8")
    loaded = json.loads(body) if body else {}
    return loaded if isinstance(loaded, dict) else {}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync prompt timeline JSONL events to the Neon-backed API.")
    parser.add_argument("--url", default="", help="Ingest endpoint URL. Defaults to PROMPT_TIMELINE_INGEST_URL or site.json vercel_url + /api/timeline/events.")
    parser.add_argument("--token", default="", help="Bearer token. Defaults to PROMPT_TIMELINE_INGEST_TOKEN.")
    parser.add_argument("--repo-label", default="", help="Repository label stored in Neon. Defaults to site.json repo_label/repo_name.")
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    site = record_event.load_site_metadata()
    url = ingest_url(args, site)
    token = args.token or os.environ.get("PROMPT_TIMELINE_INGEST_TOKEN", "").strip()
    repo_label = args.repo_label or record_event.current_repo_label(site)
    events = record_event.load_events()
    for event in events:
        event.setdefault("repo_label", repo_label)

    if args.dry_run:
        print(json.dumps({
            "repo": str(record_event.REPO_ROOT),
            "repo_label": repo_label,
            "events": len(events),
            "url": url,
            "dry_run": True,
        }, ensure_ascii=False, indent=2, sort_keys=True))
        return 0

    if not url:
        print("Missing ingest URL. Set PROMPT_TIMELINE_INGEST_URL or prompt-timeline/data/site.json vercel_url.", file=sys.stderr)
        return 2
    if not token:
        print("Missing ingest token. Set PROMPT_TIMELINE_INGEST_TOKEN.", file=sys.stderr)
        return 2

    synced = 0
    batches = 0
    try:
        for index in range(0, len(events), max(1, args.batch_size)):
            batch = events[index:index + max(1, args.batch_size)]
            response = post_batch(url, token, repo_label, batch, args.timeout)
            synced += int(response.get("upserted") or len(batch))
            batches += 1
    except (OSError, urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as exc:
        print(f"Sync failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps({
        "repo": str(record_event.REPO_ROOT),
        "repo_label": repo_label,
        "events": len(events),
        "synced": synced,
        "batches": batches,
        "url": url,
    }, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
