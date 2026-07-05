#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/deguchishouma/Desktop/AI法人研修"
WORKFLOW_DIR="$ROOT/.workflow/gas-diagram-generation"
TEMPLATE="$WORKFLOW_DIR/terminal-worker-prompt.md"
WORKER_COUNT="${1:-6}"
START_INDEX="${2:-41}"
MAX_TASKS_PER_WORKER="${MAX_TASKS_PER_WORKER:-0}"
STAMP="$(date '+%Y%m%d-%H%M%S')"
LOG_DIR="$WORKFLOW_DIR/logs/$STAMP"

mkdir -p "$LOG_DIR"

if ! command -v codex >/dev/null 2>&1; then
  echo "codex command not found" >&2
  exit 1
fi

echo "Launching $WORKER_COUNT terminal Codex workers"
echo "root=$ROOT"
echo "log_dir=$LOG_DIR"
echo "max_tasks_per_worker=$MAX_TASKS_PER_WORKER"

for ((i=0; i<WORKER_COUNT; i++)); do
  worker_num=$((START_INDEX + i))
  worker_id="$(printf 'worker-%02d' "$worker_num")"
  prompt_file="$LOG_DIR/$worker_id.prompt.md"
  log_file="$LOG_DIR/$worker_id.log"

  python3 - "$TEMPLATE" "$prompt_file" "$worker_id" "$MAX_TASKS_PER_WORKER" <<'PY'
from pathlib import Path
import sys

template, out, worker, max_tasks = sys.argv[1:]
text = Path(template).read_text(encoding="utf-8")
text = text.replace("__WORKER_ID__", worker).replace("__MAX_TASKS__", max_tasks)
Path(out).write_text(text, encoding="utf-8")
PY

  cmd=(codex exec --dangerously-bypass-approvals-and-sandbox -C "$ROOT")
  if [[ -n "${CODEX_WORKER_MODEL:-}" ]]; then
    cmd+=(-m "$CODEX_WORKER_MODEL")
  fi
  if [[ -n "${CODEX_WORKER_PROFILE:-}" ]]; then
    cmd+=(-p "$CODEX_WORKER_PROFILE")
  fi
  cmd+=(-)

  nohup "${cmd[@]}" < "$prompt_file" > "$log_file" 2>&1 &

  pid=$!
  echo "$pid $worker_id $log_file" | tee -a "$LOG_DIR/pids.txt"
done

echo "Started workers. Monitor with:"
echo "  tail -f '$LOG_DIR'/worker-*.log"
echo "  python3 '$WORKFLOW_DIR/shared_queue.py' status --sample 20"
