#!/usr/bin/env bash
set -euo pipefail

pip install pyyaml

echo "PPL± development environment ready."
echo "Try: python scripts/inventory.py"
echo "Try: python scripts/deck-readiness.py"
echo "Try: python scripts/middle-math/zip_converter.py --convert 2131"
