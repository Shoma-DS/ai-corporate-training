#!/usr/bin/env bash
set -euo pipefail
cd '/Users/deguchishouma/Desktop/AI法人研修'
python3 .workflow/gas-diagram-generation/fast_codex_worker.py --worker worker-71 --max-tasks 1 --log-dir '/Users/deguchishouma/Desktop/AI法人研修/.workflow/gas-diagram-generation/logs/20260701-191003-fast-screen' 2>&1 | tee '/Users/deguchishouma/Desktop/AI法人研修/.workflow/gas-diagram-generation/logs/20260701-191003-fast-screen/worker-71.outer.log'
