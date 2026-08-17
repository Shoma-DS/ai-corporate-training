#!/usr/bin/env python3
"""Render a lecture-first editable HTML deck from a session slides.json file."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any


SKILL_DIR = Path(__file__).resolve().parents[1]
CSS_PATH = SKILL_DIR / "assets" / "lecture-deck.css"


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def render_list(items: list[str]) -> str:
    return "<ul>" + "".join(f"<li>{esc(item)}</li>" for item in items) + "</ul>"


def render_steps(steps: list[str]) -> str:
    cards = []
    for index, step in enumerate(steps, start=1):
        cards.append(f'<div class="step"><strong>STEP {index}</strong><p>{esc(step)}</p></div>')
    return f'<div class="steps" style="--step-count:{min(len(steps), 4)}">{"".join(cards)}</div>'


def render_slide(slide: dict[str, Any], meta: dict[str, Any], index: int, total: int) -> str:
    kind = slide.get("kind", "normal")
    title = esc(slide["title"])
    section = esc(slide.get("section", ""))
    note = esc(slide.get("speaker_note", ""))
    minutes = esc(slide.get("minutes", ""))
    header = (
        '<div class="topline">'
        f'<span class="section-name">{section}</span>'
        f'<span class="slide-no">S{index:02d} / {total:02d}</span>'
        "</div>"
    )
    footer = (
        '<div class="footer">'
        f'<span>{esc(meta["course_title"])}｜第{esc(meta["session_no"])}回</span>'
        f'<span>目安 {minutes}分</span>'
        "</div>"
    )
    notes = f'<aside class="speaker-note">{note}</aside>'

    if kind == "cover":
        return (
            '<section class="slide cover">'
            f'<p class="eyebrow">{esc(meta["course_title"])}</p>'
            f'<h1>{title}</h1>'
            f'<p class="subtitle">{esc(slide.get("subtitle", ""))}</p>'
            f'<p class="cover-meta">第{esc(meta["session_no"])}回｜標準学習時間 {esc(meta["session_minutes"])}分</p>'
            f'{notes}</section>'
        )

    if kind == "section":
        return (
            '<section class="slide section-slide">'
            f'<div class="section-index">{esc(slide.get("section_index", ""))}</div>'
            f'<h1>{title}</h1>'
            f'<p class="takeaway">{esc(slide.get("takeaway", ""))}</p>'
            f'{footer}{notes}</section>'
        )

    body = ""
    takeaway = slide.get("takeaway")
    if takeaway:
        body += f'<p class="takeaway">{esc(takeaway)}</p>'

    if kind in {"process", "demo"}:
        body += render_steps(slide.get("steps", []))
        if slide.get("checkpoints"):
            body += f'<div class="checklist"><strong>確認:</strong> {esc(" / ".join(slide["checkpoints"]))}</div>'
    elif kind == "exercise":
        left = f'<div class="panel"><span class="label">WORK</span>{render_list(slide.get("steps", []))}</div>'
        right_parts = []
        if slide.get("deliverable"):
            right_parts.append(f'<div class="example"><span class="label">成果物</span><p>{esc(slide["deliverable"])}</p></div>')
        if slide.get("self_check"):
            right_parts.append(f'<div class="action"><span class="label">自己チェック</span><p>{esc(slide["self_check"])}</p></div>')
        body += f'<div class="exercise-grid">{left}<div>{"".join(right_parts)}</div></div>'
    else:
        left = render_list(slide.get("bullets", [])) if slide.get("bullets") else ""
        right_parts = []
        if slide.get("example"):
            right_parts.append(f'<div class="example"><span class="label">業務例</span><p>{esc(slide["example"])}</p></div>')
        if slide.get("action"):
            right_parts.append(f'<div class="action"><span class="label">次にすること</span><p>{esc(slide["action"])}</p></div>')
        body += f'<div class="two-column"><div>{left}</div><div>{"".join(right_parts)}</div></div>'

    return f'<section class="slide">{header}<h2>{title}</h2>{body}{footer}{notes}</section>'


def validate(data: dict[str, Any], source: Path) -> None:
    required = ["course_title", "session_no", "session_title", "session_minutes", "slides"]
    missing = [key for key in required if key not in data]
    if missing:
        raise ValueError(f"{source}: missing keys: {', '.join(missing)}")
    if not isinstance(data["slides"], list) or not data["slides"]:
        raise ValueError(f"{source}: slides must be a non-empty list")
    total_minutes = sum(int(slide.get("minutes", 0)) for slide in data["slides"])
    if total_minutes != int(data["session_minutes"]):
        raise ValueError(
            f"{source}: slide minutes total {total_minutes}, expected {data['session_minutes']}"
        )
    for index, slide in enumerate(data["slides"], start=1):
        if not slide.get("title"):
            raise ValueError(f"{source}: slide {index} has no title")
        bullets = slide.get("bullets", [])
        if len(bullets) > 5:
            raise ValueError(f"{source}: slide {index} has more than five bullets")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Path to slides.json")
    parser.add_argument("--output", type=Path, help="Output HTML path")
    args = parser.parse_args()

    source = args.source.resolve()
    data = json.loads(source.read_text(encoding="utf-8"))
    validate(data, source)
    output = args.output.resolve() if args.output else source.with_name("講義スライド.html")
    css = CSS_PATH.read_text(encoding="utf-8")
    slides = "".join(
        render_slide(slide, data, index, len(data["slides"]))
        for index, slide in enumerate(data["slides"], start=1)
    )
    document = f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(data['course_title'])}｜第{esc(data['session_no'])}回 {esc(data['session_title'])}</title>
  <style>{css}</style>
</head>
<body>
  <main class="deck">{slides}</main>
</body>
</html>
"""
    output.write_text(document, encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
