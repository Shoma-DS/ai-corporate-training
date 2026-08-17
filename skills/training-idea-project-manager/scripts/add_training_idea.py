#!/usr/bin/env python3
"""Create and classify a private Project draft item or a public training-idea Issue."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from typing import Any


SCHEMES = ["事業展開等リスキリング", "従来の助成金講座", "制度共通", "未判定"]
IDEA_TYPES = ["新規講座", "既存講座改善", "教材ネタ", "制度対応", "調査"]
DIRECTNESS = ["直接", "要具体化", "対象外候補"]
PRIORITIES = ["高", "中", "低"]


def gh(*args: str, json_output: bool = False) -> Any:
    command = ["gh", *args]
    result = subprocess.run(command, check=True, text=True, capture_output=True)
    if json_output:
        return json.loads(result.stdout)
    return result.stdout.strip()


def public_safety_errors(text: str) -> list[str]:
    checks = {
        r"https?://(?:drive\.google\.com|docs\.google\.com|www\.canva\.com)": "private-work URL",
        r"[A-Za-z0-9._%+-]+@(?!example\.com\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,}": "email address",
        r"(?:API[_ -]?KEY|SECRET|PASSWORD)\s*[:=]": "credential-like value",
        r"0\d{1,4}-\d{1,4}-\d{3,4}": "phone-number-like value",
    }
    return [reason for pattern, reason in checks.items() if re.search(pattern, text, re.IGNORECASE)]


def build_body(args: argparse.Namespace) -> str:
    evidence = "\n".join(f"- {url}" for url in args.evidence_url) or "- 未登録"
    next_step = args.next_step or (
        "対象職務・直接業務・成果物を具体化する"
        if args.directness != "直接"
        else "講座構成または教材案へ展開する"
    )
    return f"""## アイデア
{args.summary}

## 分類
- 制度区分: {args.scheme}
- アイデア種別: {args.idea_type}
- 職務直結度: {args.directness}
- 優先度: {args.priority}

## 職務への接続
- 対象職務: {args.job}
- 直接業務: {args.job_task}
- 業務成果物: {args.output}

## 根拠
{evidence}
- 確認日: {args.checked_date}

## 次の判断
- {next_step}
"""


def field_map(owner: str, project_number: str) -> dict[str, dict[str, Any]]:
    payload = gh(
        "project", "field-list", project_number, "--owner", owner, "--format", "json",
        json_output=True,
    )
    return {field["name"]: field for field in payload["fields"]}


def option_id(field: dict[str, Any], name: str) -> str:
    for option in field.get("options", []):
        if option["name"] == name:
            return option["id"]
    raise ValueError(f"option not found for {field['name']}: {name}")


def set_single(project_id: str, item_id: str, field: dict[str, Any], value: str) -> None:
    gh(
        "project", "item-edit",
        "--id", item_id,
        "--project-id", project_id,
        "--field-id", field["id"],
        "--single-select-option-id", option_id(field, value),
    )


def labels_for(args: argparse.Namespace) -> list[str]:
    labels: list[str] = []
    scheme_map = {
        "事業展開等リスキリング": "制度:事業展開等リスキリング",
        "従来の助成金講座": "制度:従来助成金講座",
        "制度共通": "制度:共通",
    }
    type_map = {
        "新規講座": "種別:講座案",
        "教材ネタ": "種別:教材ネタ",
        "制度対応": "種別:制度対応",
    }
    if args.scheme in scheme_map:
        labels.append(scheme_map[args.scheme])
    if args.idea_type in type_map:
        labels.append(type_map[args.idea_type])
    if args.scheme == "未判定":
        labels.append("判定:要制度確認")
    if args.directness == "要具体化":
        labels.append("職務直結:要具体化")
    return labels


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--scheme", choices=SCHEMES, required=True)
    parser.add_argument("--idea-type", choices=IDEA_TYPES, required=True)
    parser.add_argument("--job", required=True)
    parser.add_argument("--job-task", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--directness", choices=DIRECTNESS, required=True)
    parser.add_argument("--priority", choices=PRIORITIES, default="中")
    parser.add_argument("--evidence-url", action="append", default=[])
    parser.add_argument("--checked-date", default=dt.date.today().isoformat())
    parser.add_argument("--next-step")
    parser.add_argument("--owner", default="Shoma-DS")
    parser.add_argument("--project-number", default="1")
    parser.add_argument("--repo", default="Shoma-DS/ai-corporate-training")
    parser.add_argument("--public-issue", action="store_true")
    args = parser.parse_args()

    body = build_body(args)
    if args.public_issue:
        unsafe = public_safety_errors(f"{args.title}\n{body}")
        if unsafe:
            print("refusing public Issue: " + ", ".join(unsafe), file=sys.stderr)
            return 2

    project = gh(
        "project", "view", args.project_number, "--owner", args.owner, "--format", "json",
        json_output=True,
    )
    fields = field_map(args.owner, args.project_number)

    if args.public_issue:
        command = ["issue", "create", "--repo", args.repo, "--title", args.title, "--body", body]
        for label in labels_for(args):
            command.extend(["--label", label])
        issue_url = gh(*command)
        item = gh(
            "project", "item-add", args.project_number, "--owner", args.owner,
            "--url", issue_url, "--format", "json",
            json_output=True,
        )
        item_url = issue_url
    else:
        item = gh(
            "project", "item-create", args.project_number, "--owner", args.owner,
            "--title", args.title, "--body", body, "--format", "json",
            json_output=True,
        )
        item_url = "private Project draft"

    item_id = item["id"]
    set_single(project["id"], item_id, fields["Status"], "Todo")
    set_single(project["id"], item_id, fields["制度区分"], args.scheme)
    set_single(project["id"], item_id, fields["アイデア種別"], args.idea_type)
    set_single(project["id"], item_id, fields["職務直結度"], args.directness)
    set_single(project["id"], item_id, fields["優先度"], args.priority)
    gh(
        "project", "item-edit", "--id", item_id, "--project-id", project["id"],
        "--field-id", fields["対象職務"]["id"], "--text", args.job,
    )
    gh(
        "project", "item-edit", "--id", item_id, "--project-id", project["id"],
        "--field-id", fields["根拠確認日"]["id"], "--date", args.checked_date,
    )
    print(json.dumps({"item_id": item_id, "location": item_url}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
