#!/usr/bin/env bash
# validate-deck.sh — PPL± Batch Deck Validator
# Usage: bash scripts/validate-deck.sh cards/⛽-strength/🏛-basics/
#
# Runs validate-card.py on every .md card in the given deck folder.
# Prints a summary and exits 1 if any failures occurred.

set -uo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: bash scripts/validate-deck.sh <deck-folder-path>"
    exit 1
fi

DECK_PATH="$1"

if [ ! -d "$DECK_PATH" ]; then
    echo "ERROR: Directory not found: $DECK_PATH"
    exit 1
fi

# Locate the repo root (parent of scripts/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

PASSED=0
FAILED=0
STUBS=0

echo "Validating deck: $DECK_PATH"
echo "════════════════════════════════════════"

# Find all .md files recursively, excluding AGENTS.md
while IFS= read -r -d '' card_file; do
    # Skip AGENTS.md files
    basename_file="$(basename "$card_file")"
    if [ "$basename_file" = "AGENTS.md" ]; then
        continue
    fi

    echo ""
    echo "── $basename_file"

    # Capture output and exit code
    output=$(python "$SCRIPT_DIR/validate-card.py" "$card_file" 2>&1)
    exit_code=$?

    echo "$output"

    # Check if it was a stub (exits 0 with stub message)
    if echo "$output" | grep -q "STUB:"; then
        STUBS=$((STUBS + 1))
    elif [ $exit_code -eq 0 ]; then
        PASSED=$((PASSED + 1))
    else
        FAILED=$((FAILED + 1))
    fi

done < <(find "$DECK_PATH" -name "*.md" -print0 | sort -z)

echo ""
echo "════════════════════════════════════════"
echo "Summary: $PASSED passed, $FAILED failed, $STUBS stubs skipped"

if [ $FAILED -gt 0 ]; then
    echo "❌ $FAILED card(s) failed validation"
    exit 1
else
    echo "✅ All checks passed"
    exit 0
fi
