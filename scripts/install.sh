#!/usr/bin/env bash
set -euo pipefail

# 使用客户端自己的插件管理命令，不直接改写用户配置。
repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
target="${1:-}"
case "$target" in
  claude)
    command -v claude >/dev/null || { echo 'Install Claude Code first.' >&2; exit 1; }
    claude plugin marketplace add "$repo_dir"
    claude plugin install loova@loova-agent-plugins --scope user
    echo 'Open Claude Code, run /mcp, and authorize Loova. Restart the session to load skills.'
    ;;
  codex)
    command -v codex >/dev/null || { echo 'Install Codex first.' >&2; exit 1; }
    codex plugin add --help >/dev/null || { echo 'This Codex version lacks plugin add. Use the skills-only installer.' >&2; exit 1; }
    codex plugin marketplace add "$repo_dir"
    codex plugin add loova@loova-agent-plugins
    echo 'Authorize the plugin Loova MCP connection in your client and start a new session.'
    ;;
  *)
    echo 'Usage: bash scripts/install.sh claude|codex' >&2
    echo 'Skills only: python3 scripts/install_skills.py --target /path/to/agent/skills' >&2
    exit 2
    ;;
esac
