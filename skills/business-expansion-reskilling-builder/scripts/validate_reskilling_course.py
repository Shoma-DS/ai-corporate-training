#!/usr/bin/env python3
"""Validate a scoped business-expansion reskilling course folder."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


BANNED_PUBLIC_PATTERNS = {
    "助成対象です": "受給保証に見える断定",
    "必ず助成": "受給保証に見える断定",
    "オンラインワークショップ": "ライブ前提の提供方式",
    "チャットで共有": "ライブ前提の受講指示",
    "isometric-corporate-clean": "別コンテキストの高密度画像様式",
    "目次ストリップ": "別コンテキストの固定ナビゲーション",
}


def yaml_scalar(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", text)
    return match.group(1).strip(" '\"") if match else None


def yaml_list(text: str, key: str) -> list[str]:
    match = re.search(rf"(?ms)^{re.escape(key)}:\s*\n((?:\s+- .+\n?)+)", text)
    if not match:
        return []
    return [line.split("-", 1)[1].strip() for line in match.group(1).splitlines() if "-" in line]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--course-dir", required=True, type=Path)
    args = parser.parse_args()
    course = args.course_dir.resolve()
    errors: list[str] = []

    design = course / "全体" / "講座設計.yml"
    if not design.exists():
        errors.append(f"missing {design}")
        design_text = ""
    else:
        design_text = design.read_text(encoding="utf-8")

    title = yaml_scalar(design_text, "course_title")
    role = yaml_scalar(design_text, "target_role")
    route = yaml_scalar(design_text, "scheme_route")
    minutes_text = yaml_scalar(design_text, "standard_learning_minutes")
    direct_tasks = yaml_list(design_text, "direct_tasks")
    outputs = yaml_list(design_text, "business_outputs")
    if not title:
        errors.append("講座設計.yml: course_title is required")
    if not role:
        errors.append("講座設計.yml: target_role is required")
    if route not in {"business_expansion", "dx_current_job", "planned_future_job"}:
        errors.append("講座設計.yml: scheme_route must be one supported route")
    if not minutes_text or not minutes_text.isdigit() or int(minutes_text) < 600:
        errors.append("講座設計.yml: standard_learning_minutes must be at least 600")
    if not direct_tasks:
        errors.append("講座設計.yml: direct_tasks must not be empty")
    if not outputs:
        errors.append("講座設計.yml: business_outputs must not be empty")

    if title:
        html_pamphlet = course / "全体" / f"{title}_講座カリキュラムパンフレット.html"
        pdf_pamphlet = course / "全体" / f"{title}_講座カリキュラムパンフレット.pdf"
        for path in (html_pamphlet, pdf_pamphlet):
            if not path.exists() or path.stat().st_size == 0:
                errors.append(f"missing or empty {path}")

    session_dirs = sorted(path for path in course.iterdir() if path.is_dir() and re.match(r"^\d{2}-", path.name))
    if not session_dirs:
        errors.append("no session directories found")

    session_minutes = 0
    for session in session_dirs:
        source = session / "slides.json"
        slide_html = session / "講義スライド.html"
        slide_pdf = session / "講義スライド.pdf"
        notes = session / "講師進行メモ.md"
        for path in (source, slide_html, slide_pdf, notes):
            if not path.exists() or path.stat().st_size == 0:
                errors.append(f"missing or empty {path}")
        if not source.exists():
            continue
        try:
            data = json.loads(source.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{source}: invalid JSON: {exc}")
            continue
        slides = data.get("slides", [])
        if not 16 <= len(slides) <= 24:
            errors.append(f"{source}: expected 16-24 slides, found {len(slides)}")
        stated = int(data.get("session_minutes", 0))
        actual = sum(int(slide.get("minutes", 0)) for slide in slides)
        if actual != stated:
            errors.append(f"{source}: minutes total {actual}, stated {stated}")
        session_minutes += stated
        for index, slide in enumerate(slides, start=1):
            if len(slide.get("bullets", [])) > 5:
                errors.append(f"{source}: slide {index} exceeds five bullets")

    if minutes_text and minutes_text.isdigit() and session_minutes != int(minutes_text):
        errors.append(
            f"session minutes total {session_minutes}, course design states {minutes_text}"
        )

    public_files = [path for path in course.rglob("*") if path.suffix.lower() in {".md", ".html", ".json", ".yml"}]
    for path in public_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern, reason in BANNED_PUBLIC_PATTERNS.items():
            if pattern in text:
                errors.append(f"{path}: {reason}: {pattern}")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"reskilling course ok: {course}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
