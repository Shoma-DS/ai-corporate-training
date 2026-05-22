#!/usr/bin/env python3
"""Validate local repository skills without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing YAML frontmatter")
    try:
        header = text.split("---\n", 2)[1]
    except IndexError as exc:
        raise ValueError(f"{path}: malformed YAML frontmatter") from exc

    data: dict[str, str] = {}
    for lineno, raw_line in enumerate(header.splitlines(), start=2):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"{path}:{lineno}: expected key: value")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if key in {"name", "description"}:
            data[key] = value
    return data


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{skill_dir}: missing SKILL.md"]

    try:
        frontmatter = parse_frontmatter(skill_md)
    except ValueError as exc:
        return [str(exc)]

    expected_name = skill_dir.name
    if frontmatter.get("name") != expected_name:
        errors.append(f"{skill_md}: name must be {expected_name!r}")
    if not frontmatter.get("description"):
        errors.append(f"{skill_md}: missing description")

    text = skill_md.read_text(encoding="utf-8")
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if any(marker in line for marker in ("Do not create", "Search for stale paths", "作らない")):
            continue
        for rel in re.findall(r"`([^`]+/[^`]+)`", line):
            if rel.startswith(("skills/", "スライド/", "素材/")):
                target = ROOT / rel
                if not target.exists():
                    errors.append(f"{skill_md}: referenced path does not exist: {rel}")

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print("No local skills directory found.")
        return 0

    errors: list[str] = []
    for skill_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        errors.extend(validate_skill(skill_dir))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("local skills ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
