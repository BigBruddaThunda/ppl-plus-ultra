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

echo "[1/5] Lint SCL rules"
python scripts/lint-scl-rules.py --deck "$DECK_PATH"

echo "[2/5] Validate deck"
bash scripts/validate-deck.sh "$DECK_PATH"

echo "[3/5] Audit primary exercise coverage"
python scripts/audit-exercise-coverage.py "$DECK_PATH"

echo "[4/5] Check card schema"
python scripts/check-card-schema.py --deck "$DECK_PATH"

echo "[5/5] Validate junction bridges"
python scripts/validate-junction-bridges.py --deck "$DECK_PATH"

echo "[inventory] Build truth table outputs"
python scripts/index-card-inventory.py \
  --cards-root cards \
  --strict-status \
  --out-json "$ARTIFACT_DIR/card-inventory.json" \
  --out-csv "$ARTIFACT_DIR/card-inventory.csv"

echo "✅ Full audit sequence passed"
