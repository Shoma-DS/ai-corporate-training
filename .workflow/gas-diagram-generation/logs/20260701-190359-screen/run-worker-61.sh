#!/usr/bin/env bash
set -euo pipefail
cd '/Users/deguchishouma/Desktop/AI法人研修'
codex exec --dangerously-bypass-approvals-and-sandbox - < '/Users/deguchishouma/Desktop/AI法人研修/.workflow/gas-diagram-generation/logs/20260701-190359-screen/worker-61.prompt.md' 2>&1 | tee '/Users/deguchishouma/Desktop/AI法人研修/.workflow/gas-diagram-generation/logs/20260701-190359-screen/worker-61.log'
