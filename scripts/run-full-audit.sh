#!/usr/bin/env bash
# run-full-audit.sh
# Input contract:
#   bash scripts/run-full-audit.sh [--require-all-checks] <deck-path>
# Output contract:
#   Runs baseline full audit sequence and exits non-zero on any hard failure.
#   Optional strict mode additionally enforces contract-stub implementation checks.

set -euo pipefail

STRICT_MODE=false
DECK_PATH=""

while [ $# -gt 0 ]; do
  case "$1" in
    --require-all-checks)
      STRICT_MODE=true
      shift
      ;;
    -h|--help)
      cat <<'USAGE'
Usage:
  bash scripts/run-full-audit.sh <deck-folder-path>
  bash scripts/run-full-audit.sh --require-all-checks <deck-folder-path>

Modes:
  default                Run baseline implemented audit checks.
  --require-all-checks   Run baseline checks, then require all contract checks
                         to be implemented (passes --require-implementation).
USAGE
      exit 0
      ;;
    --*)
      echo "Unknown flag: $1"
      exit 1
      ;;
    *)
      if [ -n "$DECK_PATH" ]; then
        echo "Error: multiple deck paths provided ('$DECK_PATH' and '$1')."
        exit 1
      fi
      DECK_PATH="$1"
      shift
      ;;
  esac
done

if [ -z "$DECK_PATH" ]; then
  echo "Usage: bash scripts/run-full-audit.sh [--require-all-checks] <deck-folder-path>"
  exit 1
fi

ARTIFACT_DIR="scripts/.artifacts"
mkdir -p "$ARTIFACT_DIR"

echo "[1/6] Lint SCL rules"
python scripts/lint-scl-rules.py --deck "$DECK_PATH"

echo "[2/6] Validate deck"
bash scripts/validate-deck.sh "$DECK_PATH"

echo "[3/6] Audit primary exercise coverage"
python scripts/audit-exercise-coverage.py "$DECK_PATH"

echo "[4/6] Check card schema"
python scripts/check-card-schema.py --deck "$DECK_PATH"

echo "[5/6] Validate junction bridges"
python scripts/validate-junction-bridges.py --deck "$DECK_PATH"

echo "[6/6] Build card inventory artifacts"
python scripts/index-card-inventory.py \
  --cards-root cards \
  --strict-status \
  --out-json "$ARTIFACT_DIR/card-inventory.json" \
  --out-csv "$ARTIFACT_DIR/card-inventory.csv"

if [ "$STRICT_MODE" = true ]; then
  echo "[strict] Require contract-stub implementations"
  python scripts/check-weight-declarations.py --require-implementation
  python scripts/check-exercise-family-tree.py --require-implementation
  python scripts/run-selector-prototype.py --require-implementation
  python scripts/check-fatigue-model.py --require-implementation
  python scripts/build-canonicalization-pack.py --require-implementation
  python scripts/validate-agent-handoffs.py --require-implementation
  python scripts/run-agent-fixtures.py --require-implementation
  python scripts/validate-session-templates.py --require-implementation
fi

echo "✅ Full audit sequence passed${STRICT_MODE:+ (strict mode)}"
