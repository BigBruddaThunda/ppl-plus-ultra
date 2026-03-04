#!/usr/bin/env bash
# run-full-audit.sh
# Input contract:
#   bash scripts/run-full-audit.sh <deck-path>
# Output contract:
#   Runs baseline full audit sequence and exits non-zero on any hard failure.

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: bash scripts/run-full-audit.sh <deck-folder-path>"
  exit 1
fi

DECK_PATH="$1"
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

echo "✅ Full audit sequence passed"
