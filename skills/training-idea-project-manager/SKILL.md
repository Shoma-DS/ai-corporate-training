---
name: training-idea-project-manager
description: Capture, classify, and maintain AI corporate-training ideas in the GitHub Project for this repository, using draft items by default and public Issues only when the content is safe to publish. Use when the user says to save a course idea, add a curriculum or slide idea to the project, organize training concepts, tag ideas as business-expansion reskilling versus prior subsidy courses, or review the idea backlog.
---

# Training Idea Project Manager

## Purpose

Turn an unstructured course idea into a searchable backlog item. Distinguish `事業展開等リスキリング`, `従来の助成金講座`, `制度共通`, and `未判定` before saving.

Read `references/project-schema.md` before changing the Project configuration or classification vocabulary.

## Classification

Set all of these fields:

- 制度区分: `事業展開等リスキリング` / `従来の助成金講座` / `制度共通` / `未判定`
- アイデア種別: `新規講座` / `既存講座改善` / `教材ネタ` / `制度対応` / `調査`
- 職務直結度: `直接` / `要具体化` / `対象外候補`
- 優先度: `高` / `中` / `低`
- 対象職務: free text
- 根拠確認日: official source check date

For `事業展開等リスキリング`, require an occupation, a direct recurring task, and a concrete job output. If any is missing, use `職務直結度=要具体化` and add the next question to the item.

## Privacy Rule

Create a private Project draft item by default. Create a public repository Issue only when the user explicitly requests public issue tracking or the content is clearly safe and reusable.

Never publish customer names, employee names, applications, prices, contact details, private URLs, Drive/Canva links, contracts, credentials, or internal sales information. Keep them out of both public issues and the repository.

## Add an Idea

Use the bundled script. The default target is the private GitHub Project owned by `Shoma-DS`, project number `1`.

```bash
python3 skills/training-idea-project-manager/scripts/add_training_idea.py \
  --title '営業職向け 商品提案書レビュー演習' \
  --summary '提案書の構成・文章・根拠を生成AIで改善する演習案' \
  --scheme '事業展開等リスキリング' \
  --idea-type '教材ネタ' \
  --job '法人営業担当者' \
  --job-task '商談メモから商品提案書の初稿と修正版を作る' \
  --output '商品提案書レビューシート' \
  --directness '直接' \
  --priority '中' \
  --evidence-url 'https://www.mhlw.go.jp/content/11800000/001731966.pdf'
```

Add `--public-issue` only for a public-safe GitHub Issue. The script then applies the matching repository labels and adds the Issue to the Project.

## Review the Backlog

1. List Project items and group by `制度区分`.
2. Within `事業展開等リスキリング`, surface items with `要具体化` or `対象外候補` first.
3. Flag items whose official-source confirmation date is stale or missing.
4. Do not promote an idea into course production until the target occupation, direct task, business output, and scheme route are all clear.
5. When production starts, set Status to `In Progress`; set `Done` only after the linked course folder and deliverables exist.

## Project Changes

Before creating or renaming fields, labels, issues, or items, restate the exact GitHub owner, repository, and Project number. Preserve existing field options unless the user asks to migrate them.
