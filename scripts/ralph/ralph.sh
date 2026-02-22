#!/bin/bash
# Ralph Loop for PPL± Zip-Web Population
# Usage: ./scripts/ralph/ralph.sh [max_iterations] [--tool claude|amp]
#
# Iterates through prd.json user stories, running one per iteration.
# Each iteration reads RALPH-PROMPT.md and pipes it to the configured tool.
# Stop condition: all stories have passes: true

set -euo pipefail

TOOL="claude"
MAX_ITERATIONS=42

while [[ $# -gt 0 ]]; do
  case $1 in
    --tool) TOOL="$2"; shift 2 ;;
    [0-9]*) MAX_ITERATIONS="$1"; shift ;;
    *) echo "Unknown argument: $1"; exit 1 ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PRD="$SCRIPT_DIR/prd.json"
PROMPT="$SCRIPT_DIR/RALPH-PROMPT.md"

if [[ ! -f "$PRD" ]]; then
  echo "ERROR: prd.json not found at $PRD"
  exit 1
fi

if [[ ! -f "$PROMPT" ]]; then
  echo "ERROR: RALPH-PROMPT.md not found at $PROMPT"
  exit 1
fi

if ! command -v jq &>/dev/null; then
  echo "ERROR: jq is required (brew install jq or apt install jq)"
  exit 1
fi

echo "=== PPL± Ralph Loop ==="
echo "Tool: $TOOL | Max iterations: $MAX_ITERATIONS"
echo ""

for i in $(seq 1 $MAX_ITERATIONS); do
  echo "=== Iteration $i of $MAX_ITERATIONS ==="

  # Check remaining incomplete stories
  REMAINING=$(jq '[.userStories[] | select(.passes == false)] | length' "$PRD")

  if [[ "$REMAINING" -eq 0 ]]; then
    echo "All stories complete. Exiting."
    break
  fi

  echo "Stories remaining: $REMAINING"
  NEXT_STORY=$(jq -r '[.userStories[] | select(.passes == false)] | sort_by(.priority) | .[0].id' "$PRD")
  NEXT_TITLE=$(jq -r --arg id "$NEXT_STORY" '.userStories[] | select(.id == $id) | .title' "$PRD")
  echo "Next story: $NEXT_STORY — $NEXT_TITLE"
  echo ""

  if [[ "$TOOL" == "claude" ]]; then
    cat "$PROMPT" | claude --print
  elif [[ "$TOOL" == "amp" ]]; then
    cat "$PROMPT" | amp
  else
    echo "ERROR: Unknown tool '$TOOL'. Use 'claude' or 'amp'."
    exit 1
  fi

  echo ""
  echo "=== Iteration $i complete ==="
  echo ""

  # Re-check if all complete after this iteration
  REMAINING=$(jq '[.userStories[] | select(.passes == false)] | length' "$PRD")
  if [[ "$REMAINING" -eq 0 ]]; then
    echo "All stories complete after iteration $i."
    break
  fi
done

echo "=== Ralph Loop finished ==="
REMAINING=$(jq '[.userStories[] | select(.passes == false)] | length' "$PRD")
echo "Stories remaining: $REMAINING"
