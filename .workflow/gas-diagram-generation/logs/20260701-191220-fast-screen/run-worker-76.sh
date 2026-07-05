#!/usr/bin/env bash
set -euo pipefail
cd '/Users/deguchishouma/Desktop/AI法人研修'
python3 .workflow/gas-diagram-generation/fast_codex_worker.py --worker worker-76 --max-tasks 0 --log-dir '/Users/deguchishouma/Desktop/AI法人研修/.workflow/gas-diagram-generation/logs/20260701-191220-fast-screen' 2>&1 | tee '/Users/deguchishouma/Desktop/AI法人研修/.workflow/gas-diagram-generation/logs/20260701-191220-fast-screen/worker-76.outer.log'
