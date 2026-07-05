#!/usr/bin/env python3
"""Build a shared queue for regenerating all GAS editable-slide diagram parts."""

from __future__ import annotations

import json
import re
from pathlib import Path


COURSE_DIR = Path("講座/生成AI・GASで実践する業務変革・DX推進講座")
OUT_DIR = Path(".workflow/gas-diagram-generation")
SHARDS_DIR = OUT_DIR / "shards"


def slide_titles(plan: Path) -> dict[str, str]:
    text = plan.read_text(encoding="utf-8")
    return {
        f"S{int(match.group(1)):02d}": match.group(2).strip()
        for match in re.finditer(r"^### S(\d{2})\s+(.+)$", text, re.MULTILINE)
    }


def prompt_ids(prompt_path: Path) -> list[str]:
    text = prompt_path.read_text(encoding="utf-8")
    return re.findall(r"^## (S\d{2})\b", text, re.MULTILINE)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    SHARDS_DIR.mkdir(parents=True, exist_ok=True)
    tasks: list[dict[str, str]] = []
    for session_dir in sorted(p for p in COURSE_DIR.glob("[0-9][0-9]-*") if p.is_dir()):
        no = session_dir.name[:2]
        titles = slide_titles(session_dir / "スライド案.md")
        prompt_path = session_dir / "図解パーツ生成プロンプト.md"
        for slide_id in prompt_ids(prompt_path):
            tasks.append(
                {
                    "course": COURSE_DIR.name,
                    "session_no": no,
                    "session_dir": str(session_dir),
                    "slide_id": slide_id,
                    "title": titles.get(slide_id, ""),
                    "prompt_file": str(prompt_path),
                    "target": str(session_dir / "図解パーツ" / f"{slide_id}.png"),
                    "status": "pending",
                }
            )

    (OUT_DIR / "queue.jsonl").write_text(
        "\n".join(json.dumps(task, ensure_ascii=False) for task in tasks) + "\n",
        encoding="utf-8",
    )

    for old in SHARDS_DIR.glob("worker-*.jsonl"):
        old.unlink()
    by_session: dict[str, list[dict[str, str]]] = {}
    for task in tasks:
        by_session.setdefault(task["session_no"], []).append(task)
    for no, session_tasks in sorted(by_session.items()):
        (SHARDS_DIR / f"worker-{no}.jsonl").write_text(
            "\n".join(json.dumps(task, ensure_ascii=False) for task in session_tasks) + "\n",
            encoding="utf-8",
        )

    summary = [
        "# GAS図解パーツ生成キュー",
        "",
        f"- 対象講座: `{COURSE_DIR}`",
        f"- 総タスク数: {len(tasks)}",
        "- 方針: 全S番号を新しい `図解パーツ生成プロンプト.md` から再生成する。既存PNGはS番号ずれの可能性があるため完成扱いにしない。",
        "- 実行経路: Codex App Server / GPT image 2 / `imagegen` のみ。ローカル描画、HTML/SVG/canvas、PIL、ImageMagick、スクリーンショット代替は禁止。",
        "- コピー元: 各ワーカー自身の `generated_images/<session-id>/` のみ。他ワーカーの画像を拾わない。",
        "",
        "## シャード",
        "",
        "| ワーカー | セッション | 枚数 | キューファイル |",
        "|---|---|---:|---|",
    ]
    for no, session_tasks in sorted(by_session.items()):
        session_dir = Path(session_tasks[0]["session_dir"]).name
        summary.append(f"| worker-{no} | {session_dir} | {len(session_tasks)} | `shards/worker-{no}.jsonl` |")
    (OUT_DIR / "README.md").write_text("\n".join(summary) + "\n", encoding="utf-8")
    print(f"wrote {len(tasks)} tasks to {OUT_DIR / 'queue.jsonl'}")


if __name__ == "__main__":
    main()
