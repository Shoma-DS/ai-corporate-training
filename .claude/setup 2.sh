#\!/usr/bin/env bash
# AI エージェント環境のセットアップ（初回クローン後に1回実行）
# 使い方: bash .claude/setup.sh

set -euo pipefail

REPO_NAME="AI法人研修"
SKILL_DIR="$HOME/.claude/skills/prompt-optimizer/scripts"

echo "=== セットアップ: $REPO_NAME ==="

if [ \! -f "$SKILL_DIR/setup-eval.sh" ]; then
  echo "prompt-optimizer スキルが見つかりません。"
  echo "Claude Code でインストール後に再実行してください。"
  exit 1
fi

bash "$SKILL_DIR/setup-eval.sh"
bash "$SKILL_DIR/select-vault.sh"

echo ""
echo "=== 完了 ==="
