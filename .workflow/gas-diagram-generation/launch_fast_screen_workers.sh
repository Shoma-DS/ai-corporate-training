#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/deguchishouma/Desktop/AI法人研修"
WORKFLOW_DIR="$ROOT/.workflow/gas-diagram-generation"
WORKER_COUNT="${1:-6}"
START_INDEX="${2:-71}"
MAX_TASKS_PER_WORKER="${MAX_TASKS_PER_WORKER:-0}"
STAMP="$(date '+%Y%m%d-%H%M%S')"
SESSION_NAME="gas-fast-$STAMP"
LOG_DIR="$WORKFLOW_DIR/logs/$STAMP-fast-screen"

mkdir -p "$LOG_DIR"

if ! command -v screen >/dev/null 2>&1; then
  echo "screen command not found" >&2
  exit 1
fi

make_run_file() {
  local worker_id="$1"
  local run_file="$LOG_DIR/run-$worker_id.sh"
  local outer_log="$LOG_DIR/$worker_id.outer.log"
  python3 - "$run_file" "$ROOT" "$worker_id" "$MAX_TASKS_PER_WORKER" "$LOG_DIR" "$outer_log" <<'PY'
from pathlib import Path
import shlex
import sys

run_file, root, worker, max_tasks, log_dir, outer_log = sys.argv[1:]
cmd = [
    "python3",
    ".workflow/gas-diagram-generation/fast_codex_worker.py",
    "--worker",
    worker,
    "--max-tasks",
    max_tasks,
    "--log-dir",
    log_dir,
]
script = "\n".join(
    [
        "#!/usr/bin/env bash",
        "set -euo pipefail",
        f"cd {shlex.quote(root)}",
        " ".join(shlex.quote(part) for part in cmd) + f" 2>&1 | tee {shlex.quote(outer_log)}",
        "",
    ]
)
Path(run_file).write_text(script, encoding="utf-8")
PY
  chmod +x "$run_file"
  printf '%s\n' "$run_file"
}

echo "Launching $WORKER_COUNT fast screen Codex workers"
echo "screen_session=$SESSION_NAME"
echo "log_dir=$LOG_DIR"
echo "max_tasks_per_worker=$MAX_TASKS_PER_WORKER"

for ((i=0; i<WORKER_COUNT; i++)); do
  worker_num=$((START_INDEX + i))
  worker_id="$(printf 'worker-%02d' "$worker_num")"
  run_file="$(make_run_file "$worker_id")"
  echo "$worker_id $run_file" | tee -a "$LOG_DIR/workers.txt"

  if [[ $i -eq 0 ]]; then
    screen -dmS "$SESSION_NAME" -t "$worker_id" bash "$run_file"
  else
    screen -S "$SESSION_NAME" -X screen -t "$worker_id" bash "$run_file"
  fi
done

echo "Started fast screen workers."
echo "Attach: screen -r '$SESSION_NAME'"
echo "Detach from screen: Ctrl-a then d"
echo "Status: python3 '$WORKFLOW_DIR/shared_queue.py' status --sample 20"
echo "Logs: tail -f '$LOG_DIR'/*.outer.log"
