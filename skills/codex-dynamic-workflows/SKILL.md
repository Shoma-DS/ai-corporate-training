---
name: codex-dynamic-workflows
description: Downstream coordination helper for the AI法人研修 course-production workflow. Use only when corporate-training-course-builder needs explicit orchestration, goal mode, subagents or simulated work packets, approval gates, integration, verification, or reusable workflow artifacts, or when the user explicitly asks only for workflow/subagent orchestration. Do not use as the entrypoint for "講座作成", "講座を作成してください", or broad training-material production.
---

# AI Agent Dynamic Workflows

Use this skill to turn a large task into a supervised AI-agent workflow: draft an orchestration artifact, enter goal mode when sustained execution is requested, delegate disjoint work to subagents when available, integrate results, verify the outcome, and save reusable workflow artifacts.

In this repository, this skill is a downstream coordination helper. For "講座作成", "講座を作成してください", or any broad training-material production request, start with `skills/corporate-training-course-builder/SKILL.md` and use this skill only if that course workflow needs explicit packets, approvals, subagents, or reusable orchestration notes. This skill must not create a separate course-production standard.

This skill works in agents that support skills. Do not claim that a local script can call subagent tools unless the current environment exposes such a runner. When no programmable runner exists, create a human-readable orchestration script and operate it through the available agent tools.

## Decision Rule

Use dynamic orchestration when at least two are true:

- The task has independent research, coding, review, migration, QA, docs, or design tracks.
- The task is broad enough that an explicit success contract would reduce drift.
- The task has risk: destructive edits, external writes, deploys, secrets, production data, billing, user accounts, or large repo-wide changes.
- Verification benefits from a separate pass from implementation.
- The workflow could become a reusable recipe for future tasks.
- The user explicitly asks for a dynamic workflow, swarm, subagents, parallel agents, or Claude Code-style workflow.

If the task is small, do it directly and mention that full workflow orchestration was unnecessary.

## Operating Contract

When using this skill:

1. Restate the goal and success criteria.
2. Create or update a workflow artifact before delegating.
3. Ask for approval before risky, expensive, external, or destructive steps.
4. Enter goal mode when the user explicitly requests sustained execution or when the invoked task clearly requires multi-turn completion.
5. Split work into disjoint packets with clear ownership.
6. Spawn subagents only when the current environment allows it and the user has authorized delegated or parallel agent work.
7. Simulate subagents with isolated packet notes when no subagent runner is available.
8. Integrate results explicitly; do not paste raw subagent dumps as the final answer.
9. Verify with checks matched to the task's blast radius.
10. Save reusable artifacts only when they will help future work.

## Workflow Artifacts

Prefer creating a local run directory:

```text
.workflow/<slug>/
|-- plan.md
|-- state.json
|-- orchestration.md
|-- packets/
|-- results/
`-- final-report.md
```

Use `scripts/new_workflow.py` to scaffold this structure:

```bash
python3 /path/to/codex-dynamic-workflows/scripts/new_workflow.py "Task title"
```

Keep `plan.md` human-readable. Use `state.json` for status, packet IDs, approval state, and verification state. Use `orchestration.md` as the executable mental model: the sequence the agent will follow, the branching rules, and the packet prompts.

## Orchestration Plan

Draft a concise plan with:

```text
Goal:
Success criteria:
Current context:
Constraints:
Risks:
Approval required:
Workflow artifact path:
Work packets:
Integration policy:
Verification:
Reusable artifacts:
```

Do not over-plan obvious work. The plan should be detailed enough to guide delegation and verification, not a substitute for execution.

## Approval Gates

Ask one clear approval question before:

- deleting, overwriting, mass-renaming, or force-pushing
- running migrations or broad codemods
- deploying, publishing, emailing, posting, or changing external systems
- touching credentials, secrets, production data, billing, or user accounts
- spawning many agents or long-running expensive jobs
- making irreversible Git or repository operations

If approval is denied or unavailable, continue only with safe read-only planning, local drafts, or non-destructive checks.

Read `references/risk-gates.md` when risk is unclear.

## Goal Mode

If goal mode tools are available and the user has asked this skill to run the workflow, call goal mode with the full objective. Keep the objective intact; do not shrink it to the next step.

Do not enter goal mode for a small one-shot task, a purely advisory discussion, or when the user asks only for a plan.

### Goal Action Handoff Prompt

When the user asks for a Goal action prompt, asks to continue after a session/context limit, or says "クリップボードに入れて", prepare a compact continuation prompt instead of a loose summary. It must be executable by the next agent without rereading the whole conversation.

Include:

- Original objective and success criteria.
- Repository path and target course/session paths.
- Current completed work and remaining packets.
- Workflow artifact path such as `.workflow/<slug>/`.
- File ownership and public/private safety constraints.
- Required downstream helpers and forbidden shortcuts.
- Verification commands and completion-report format.

If clipboard access is requested, copy the prompt with `pbcopy` and also save a copy as `.workflow/<slug>/handoff-prompt.md` when a workflow directory exists. If clipboard access fails, leave the file copy and report the path.

## Work Packets

Each packet must be self-contained:

```text
Packet ID:
Objective:
Context:
Files / sources:
Ownership:
Do:
Do not:
Expected output:
Verification:
```

Prefer packets with disjoint ownership:

- codebase discovery
- dependency or API research
- implementation slice
- tests and fixtures
- docs and examples
- UX or product review
- security or risk review
- final verification

For code-edit packets, assign non-overlapping files or modules. Tell workers they are not alone in the codebase, must not revert others' edits, and must adapt to concurrent changes.

### Course High-Density Rebuild Packets

In this repository, when `corporate-training-course-builder` calls this helper for a full-course slide plan rebuild that should match another course's information density, use a packet split like this unless the course structure demands otherwise:

```text
P1: Sessions 1-2 slide-plan rebuild, quality verification and補修
P2: Sessions 3-4 slide-plan rebuild, quality verification and補修
P3: Sessions 5-6 slide-plan rebuild, quality verification and補修
P4: Official assets, screenshots, public examples, source notes
P5: Integrated verification, public-safety scan, final report
```

Each session packet should verify and, if owned, fix:

- 35-45 slides for a 120-minute session unless justified otherwise.
- Slide count equals `**ヘッドライン:**` count.
- Time allocation table totals 120 minutes and references real slide ranges.
- Each slide uses a So What headline, 3-6 meaningful blocks where appropriate, and a visible structure such as comparison, process, checklist, Before/After, output map, or rubric.
- Exercises include steps, files/data, learner output, review/self-check criteria, and next-session/final-output connection.
- Content is target-course specific and does not copy the reference course's topics, chapter order, examples, or wording.

The asset/source packet should verify and, if owned, fix:

- Official/current sources are checked for product capabilities, quotas, logos, UI screenshots, and public cases.
- Source memos are saved under course-level `全体/調査/` with confirmation date and usage notes.
- Official logos are saved only under repository-level `素材/ロゴ/`.
- Session screenshots are saved under each session's `スクリーンショット/`.
- Uncaptured screenshots have exact official URLs or dummy-environment capture instructions.
- Real customer/employee data, private URLs, prices, contacts, credentials, API keys, and contract details are not saved in public files.
- For Google Workspace/GAS courses, prefer official Google Workspace, Google Help, Google Developers, Workspace Updates, and public customer-story sources. Download only safe public/static images and record the source URL; otherwise record browser capture instructions for a dummy environment.

The integration packet should run or record:

```bash
python3 scripts/validate_local_skills.py
python3 skills/codex-dynamic-workflows/scripts/verify_workflow.py .workflow/<slug>
```

It should also include a short per-session table with slide count, headline count, time total, main補修 points, acquired assets, remaining human screenshot checks, and public-safety scan notes.

Do not mark the workflow complete just because background agents or packet notes finished. The main agent must inspect current files, run the verifier, and write `final-report.md` from the integrated state.

## Subagents

When a subagent runner is available:

- Spawn only concrete, bounded, materially useful subtasks.
- Keep immediate blocking work local.
- Delegate sidecar work that can run while the main agent makes progress.
- Avoid duplicate work across agents.
- Ask workers to edit directly only when their write scope is disjoint and clear.
- Wait for subagents only when their result is needed for the next critical-path step.

When no subagent runner is available:

- Simulate the swarm with isolated packet passes.
- Read only packet-relevant files during each pass.
- Write packet notes under `results/`.
- Integrate only after packet outputs are separate.

## Integration

After packets complete, synthesize:

```text
Accepted:
Rejected:
Conflicts:
Decisions:
Final changes:
Remaining risks:
```

Resolve conflicts explicitly. If two packets disagree, inspect the authoritative source before choosing.

Use `scripts/collect_results.py` to produce an integration checklist from result files:

```bash
python3 /path/to/codex-dynamic-workflows/scripts/collect_results.py .workflow/<slug>
```

## Verification

Run the narrowest reliable checks first, then broaden as risk warrants:

- unit tests for touched code
- typecheck or lint
- build
- browser or UI smoke test
- script dry run
- source citation check
- migration dry run
- manual checklist for non-code work

Use `scripts/verify_workflow.py` to check workflow artifact completeness:

```bash
python3 /path/to/codex-dynamic-workflows/scripts/verify_workflow.py .workflow/<slug>
```

Report skipped checks honestly. Do not treat a workflow as complete until the evidence proves the original success criteria.

For course high-density rebuilds, workflow completion is not proven by subagent completion alone. The main agent must inspect current files and prove:

- `plan.md`, `state.json`, `orchestration.md`, `packets/`, `results/`, and `final-report.md` exist and pass the verifier.
- Per-session slide counts, headline counts, and time totals pass current-state checks.
- Source notes and screenshot/asset paths are consistent with the course files.
- Public-safety scans were performed and any hits are either warnings, safe dummy data, or fixed.

## Reusable Recipes

When a run produces a useful pattern, save a concise recipe in a project-appropriate location, such as `.workflow/recipes/<name>.md` or a repo docs folder. Include:

- trigger
- plan shape
- packet list
- verification checklist
- known risks

Do not save transcripts, secrets, bulky logs, credentials, or sensitive personal details.

## References

- Read `references/plan-schema.md` when a machine-readable workflow plan is useful.
- Read `references/risk-gates.md` before risky or ambiguous operations.
- Read `references/validation-examples.md` when forward-testing or improving this skill.
