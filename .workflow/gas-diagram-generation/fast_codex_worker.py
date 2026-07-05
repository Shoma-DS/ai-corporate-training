#!/usr/bin/env python3
"""Fast terminal worker: claim tasks, pass one compact image prompt to codex exec."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path("/Users/deguchishouma/Desktop/AI法人研修")
WORKFLOW_DIR = ROOT / ".workflow/gas-diagram-generation"
QUEUE = WORKFLOW_DIR / "shared_queue.py"
STATE = WORKFLOW_DIR / "shared-queue-state.json"


def run(cmd: list[str], *, input_text: str | None = None, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=ROOT,
        input=input_text,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=False,
    )


def run_codex_to_log(prompt: str, log_path: Path, timeout: int) -> int:
    with log_path.open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            ["codex", "exec", "--dangerously-bypass-approvals-and-sandbox", "-C", str(ROOT), "-"],
            cwd=ROOT,
            stdin=subprocess.PIPE,
            stdout=log,
            stderr=subprocess.STDOUT,
            text=True,
        )
        assert process.stdin is not None
        process.stdin.write(prompt)
        process.stdin.close()
        try:
            return process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
            raise


def queue_cmd(*args: str) -> dict:
    result = run(["python3", str(QUEUE), *args])
    if result.returncode != 0:
        raise RuntimeError(result.stdout)
    return json.loads(result.stdout)


def task_state(task_id: str) -> dict | None:
    data = json.loads(STATE.read_text(encoding="utf-8"))
    for task in data["tasks"]:
        if task["task_id"] == task_id:
            return task
    return None


def extract_prompt_block(prompt_file: Path, slide_id: str) -> str:
    text = prompt_file.read_text(encoding="utf-8")
    pattern = rf"^## {re.escape(slide_id)}\b.*?(?=^## S\d{{2}}\b|\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    if not match:
        raise RuntimeError(f"prompt block not found: {prompt_file} {slide_id}")
    return match.group(0).strip()


def build_codex_prompt(worker: str, task: dict, prompt_block: str, marker: Path) -> str:
    target = task["target"]
    task_id = task["task_id"]
    token = task["claim_token"]
    return f"""You are {worker}, generating exactly one claimed GAS course diagram part.

Coordinator already read repository rules and selected this task. Do not browse. Do not inspect the whole repo. Use only the task JSON and prompt block below.

Hard rules:
- Use built-in Codex image generation / GPT image 2 / imagegen only.
- Do not use OpenAI API keys, SDK scripts, SVG, HTML/CSS, canvas, PIL, ImageMagick, browser screenshots, local drawing, local text overlays, or global generated_images search.
- Output must be a single complete PNG copied to the exact target.
- Make it a wide, slightly vertically compact, high-density Japanese business training reference diagram.
- Do not render course name, session name, S番号, section header, or full slide title inside the image.
- Use readable Japanese card/table/process text from the prompt block. Reject placeholders, fake UI/logos, empty boxes, unreadable tiny text, or sparse decorative visuals.

Task JSON:
```json
{json.dumps(task, ensure_ascii=False, indent=2)}
```

Diagram prompt block:
```markdown
{prompt_block}
```

Required commands after image generation:
1. Before calling imagegen, ensure marker exists:
   `mkdir -p {marker.parent} && touch {marker}`
2. After imagegen, copy from your own Codex session only. Use the UUID-like `session id` printed in this codex exec startup banner, for example `019f...`; do not use the timestamp-like id sometimes shown by the image tool. Use:
   `python3 scripts/copy_latest_generated_image.py --target {target!r} --marker {str(marker)!r} --session-id <uuid-session-id-from-startup-banner> --expect-mime image/png --allow-latest-in-session`
3. Verify:
   `file {target!r}`
4. If valid and acceptable, mark complete:
   `python3 .workflow/gas-diagram-generation/shared_queue.py complete --worker {worker} --task-id {task_id} --claim-token {token} --target {target!r} --note 'PNG生成・コピー・file確認済み'`
5. If imagegen fails or output is unacceptable, mark requeue:
   `python3 .workflow/gas-diagram-generation/shared_queue.py fail --worker {worker} --task-id {task_id} --claim-token {token} --note '<short reason>' --requeue`

Proceed now. Generate the image; do not only describe the plan.
"""


def append_report(path: Path, line: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(line.rstrip() + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", required=True)
    parser.add_argument("--max-tasks", type=int, default=0)
    parser.add_argument("--stale-minutes", type=int, default=90)
    parser.add_argument("--codex-timeout", type=int, default=2400)
    parser.add_argument("--log-dir", required=True)
    args = parser.parse_args()

    log_dir = Path(args.log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)
    report = WORKFLOW_DIR / "reports" / f"{args.worker}.md"

    completed = 0
    requeued = 0

    while True:
        if args.max_tasks > 0 and completed >= args.max_tasks:
            break

        claim = queue_cmd("claim", "--worker", args.worker, "--stale-minutes", str(args.stale_minutes))
        if claim.get("status") == "empty":
            break

        task = claim["task"]
        task_id = task["task_id"]
        target = task["target"]
        marker = Path("/tmp/gas-diagram-markers") / f"{args.worker}-{task_id}-{int(time.time())}.marker"

        prompt_block = extract_prompt_block(ROOT / task["prompt_file"], task["slide_id"])
        codex_prompt = build_codex_prompt(args.worker, task, prompt_block, marker)
        prompt_path = log_dir / f"{args.worker}-{task_id}.prompt.md"
        log_path = log_dir / f"{args.worker}-{task_id}.codex.log"
        prompt_path.write_text(codex_prompt, encoding="utf-8")

        start = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        append_report(report, f"- {start} {task_id} claimed target={target}")

        try:
            returncode = run_codex_to_log(codex_prompt, log_path, args.codex_timeout)
        except subprocess.TimeoutExpired as exc:
            with log_path.open("a", encoding="utf-8") as f:
                f.write("\nTIMEOUT\n")
            queue_cmd(
                "fail",
                "--worker",
                args.worker,
                "--task-id",
                task_id,
                "--claim-token",
                task["claim_token"],
                "--note",
                "codex exec timeout; requeued",
                "--requeue",
            )
            requeued += 1
            append_report(report, f"  -> requeued timeout log={log_path}")
            continue

        state = task_state(task_id)
        if state and state.get("status") == "complete":
            completed += 1
            append_report(report, f"  -> complete log={log_path}")
        else:
            current_token = state.get("claim_token") if state else task["claim_token"]
            if current_token:
                queue_cmd(
                    "fail",
                    "--worker",
                    args.worker,
                    "--task-id",
                    task_id,
                    "--claim-token",
                    current_token,
                    "--note",
                    f"codex exec exited without completing; returncode={returncode}",
                    "--requeue",
                )
            requeued += 1
            append_report(report, f"  -> requeued returncode={returncode} log={log_path}")

        time.sleep(2)

    print(json.dumps({"worker": args.worker, "completed": completed, "requeued": requeued}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
