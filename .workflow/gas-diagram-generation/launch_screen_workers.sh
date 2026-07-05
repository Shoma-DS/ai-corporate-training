#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/deguchishouma/Desktop/AI法人研修"
WORKFLOW_DIR="$ROOT/.workflow/gas-diagram-generation"
TEMPLATE="$WORKFLOW_DIR/terminal-worker-prompt.md"
WORKER_COUNT="${1:-6}"
START_INDEX="${2:-61}"
MAX_TASKS_PER_WORKER="${MAX_TASKS_PER_WORKER:-0}"
STAMP="$(date '+%Y%m%d-%H%M%S')"
SESSION_NAME="gas-diagram-$STAMP"
LOG_DIR="$WORKFLOW_DIR/logs/$STAMP-screen"

mkdir -p "$LOG_DIR"

if ! command -v screen >/dev/null 2>&1; then
  echo "screen command not found" >&2
  exit 1
fi

make_worker_files() {
  local worker_id="$1"
  local prompt_file="$LOG_DIR/$worker_id.prompt.md"
  local log_file="$LOG_DIR/$worker_id.log"
  local run_file="$LOG_DIR/run-$worker_id.sh"

  python3 - "$TEMPLATE" "$prompt_file" "$worker_id" "$MAX_TASKS_PER_WORKER" <<'PY'
from pathlib import Path
import sys

template, out, worker, max_tasks = sys.argv[1:]
text = Path(template).read_text(encoding="utf-8")
text = text.replace("__WORKER_ID__", worker).replace("__MAX_TASKS__", max_tasks)
Path(out).write_text(text, encoding="utf-8")
PY

  python3 - "$run_file" "$ROOT" "$prompt_file" "$log_file" <<'PY'
from pathlib import Path
import shlex
import sys

run_file, root, prompt_file, log_file = sys.argv[1:]
script = "\n".join(
    [
        "#!/usr/bin/env bash",
        "set -euo pipefail",
        f"cd {shlex.quote(root)}",
        "codex exec --dangerously-bypass-approvals-and-sandbox - "
        f"< {shlex.quote(prompt_file)} 2>&1 | tee {shlex.quote(log_file)}",
        "",
    ]
)
Path(run_file).write_text(script, encoding="utf-8")
PY
  chmod +x "$run_file"
  printf '%s\n' "$run_file"
}

echo "Launching $WORKER_COUNT screen Codex workers"
echo "screen_session=$SESSION_NAME"
echo "log_dir=$LOG_DIR"
echo "max_tasks_per_worker=$MAX_TASKS_PER_WORKER"

first_run_file=""
for ((i=0; i<WORKER_COUNT; i++)); do
  worker_num=$((START_INDEX + i))
  worker_id="$(printf 'worker-%02d' "$worker_num")"
  run_file="$(make_worker_files "$worker_id")"
  echo "$worker_id $run_file" | tee -a "$LOG_DIR/workers.txt"

  if [[ $i -eq 0 ]]; then
    first_run_file="$run_file"
    screen -dmS "$SESSION_NAME" -t "$worker_id" bash "$first_run_file"
  else
    screen -S "$SESSION_NAME" -X screen -t "$worker_id" bash "$run_file"
  fi
done

echo "Started screen workers."
echo "Attach: screen -r '$SESSION_NAME'"
echo "Detach from screen: Ctrl-a then d"
echo "Status: python3 '$WORKFLOW_DIR/shared_queue.py' status --sample 20"
echo "Logs: tail -f '$LOG_DIR'/worker-*.log"
