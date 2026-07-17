#!/usr/bin/env python3
"""Create a KDP publishing project folder with starter files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9\-_.\u3040-\u30ff\u3400-\u9fff]+", "", text)
    return text.strip("-_.") or "kindle-book"


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="Book title")
    parser.add_argument("--author", default="", help="Author name")
    parser.add_argument("--root", default="出版", help="Output root directory")
    parser.add_argument("--slug", default="", help="Folder slug")
    args = parser.parse_args()

    slug = args.slug or slugify(args.title)
    project = Path(args.root) / slug

    metadata = {
        "title": args.title,
        "subtitle": "",
        "author": args.author,
        "language": "ja-JP",
        "format_plan": "ebook",
        "description": "",
        "keywords": [],
        "categories": [],
        "target_reader": "",
        "reader_promise": "",
        "publishing_rights": "",
        "ai_disclosure_notes": "",
        "kdp_select_decision": "",
        "price_assumption": "",
        "official_requirements_checked_on": "",
    }

    files = {
        "00_企画/book_plan.md": f"# {args.title}\n\n## 読者\n\n## 読者の悩み\n\n## 本の約束\n\n## 章立て方針\n\n## 非対象\n\n",
        "00_企画/reader_profile.md": "# Reader Profile\n\n- 読者:\n- 前提知識:\n- 購入動機:\n- 読後にできること:\n",
        "00_企画/competing_books.md": "# Competing Books\n\n| Title | Reader | Promise | Useful pattern | Gap |\n|---|---|---|---|---|\n",
        "01_原稿/manuscript.md": f"# {args.title}\n\n著者: {args.author}\n\n## はじめに\n\n## 第1章\n\n",
        "01_原稿/revision_notes.md": "# Revision Notes\n\n## AI Usage Notes\n\n## Source Check Notes\n\n## Revision Log\n\n",
        "02_メタデータ/kdp_metadata.json": json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        "02_メタデータ/description.md": "# Store Description\n\n",
        "02_メタデータ/keywords.md": "# Keywords\n\n1. \n2. \n3. \n4. \n5. \n6. \n7. \n",
        "02_メタデータ/categories.md": "# Categories\n\n- \n",
        "03_表紙/cover_brief.md": "# Cover Brief\n\n## Required text\n\n## Visual direction\n\n## Thumbnail test\n\n## Prohibited elements\n\n",
        "03_表紙/sources.md": "# Cover Sources\n\nRecord asset source URLs, license notes, and created asset paths.\n",
        "04_提出パッケージ/upload_checklist.md": "# KDP Upload Checklist\n\n- [ ] Official KDP requirements checked near upload\n- [ ] Manuscript previewed\n- [ ] Cover dimensions checked\n- [ ] Metadata finalized\n- [ ] Rights confirmed\n- [ ] AI disclosure reviewed\n- [ ] Pricing/KDP Select decision made\n",
        "04_提出パッケージ/validation_report.md": "# Validation Report\n\nRun `validate_kdp_package.py` and paste or summarize results here.\n",
        "05_販促/launch_plan.md": "# Launch Plan\n\n## Audience\n\n## Channels\n\n## Timeline\n\n",
        "05_販促/sales_copy.md": "# Sales Copy\n\n## Short\n\n## Medium\n\n## Social posts\n\n",
    }

    created = []
    for rel_path, content in files.items():
        path = project / rel_path
        if write_if_missing(path, content):
            created.append(path)

    print(f"project: {project}")
    print(f"created: {len(created)}")
    for path in created:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
