#!/usr/bin/env bash
# canvas-to-production.sh — One-way copy from canvas/components/ to production directories.
#
# Usage:
#   bash canvas/scripts/canvas-to-production.sh <canvas-artifact-path>
#
# Example:
#   bash canvas/scripts/canvas-to-production.sh canvas/components/BlockHeader.html
#
# Rules:
#   - Source must be inside canvas/components/
#   - Destination is determined by file extension
#   - Never overwrites an existing file (cp -n)
#   - Never writes to prohibited directories (middle-math, scripts, seeds, scl-deep)

set -euo pipefail

# ─── Validate argument ────────────────────────────────────────────────────────

if [[ $# -lt 1 ]]; then
  echo "ERROR: No source path provided." >&2
  echo "Usage: bash canvas/scripts/canvas-to-production.sh <canvas-artifact-path>" >&2
  exit 1
fi

SOURCE="$1"
FILENAME="$(basename "$SOURCE")"
EXT="${FILENAME##*.}"

# ─── Validate source path ─────────────────────────────────────────────────────

if [[ ! -f "$SOURCE" ]]; then
  echo "ERROR: Source file not found: $SOURCE" >&2
  exit 1
fi

# Normalize path: strip leading ./ if present
NORMALIZED_SOURCE="${SOURCE#./}"

if [[ "$NORMALIZED_SOURCE" != canvas/components/* ]]; then
  echo "ERROR: Source path must be inside canvas/components/. Got: $SOURCE" >&2
  exit 1
fi

# ─── Route by extension ───────────────────────────────────────────────────────

case "$EXT" in
  html)
    DEST="html/${FILENAME}"
    ;;
  tsx|ts)
    DEST="web/src/components/canvas/${FILENAME}"
    ;;
  css)
    DEST="html/design-system/${FILENAME}"
    ;;
  md)
    echo "ERROR: .md files require explicit deck path." >&2
    echo "Use: cp -n ${SOURCE} cards/<order>/<axis>/<type>/${FILENAME}" >&2
    exit 1
    ;;
  *)
    echo "ERROR: Unknown file type: .${EXT}" >&2
    exit 1
    ;;
esac

# ─── Boundary check: prohibited destination prefixes ─────────────────────────

PROHIBITED=("middle-math" "scripts" "seeds" "scl-deep")
for PREFIX in "${PROHIBITED[@]}"; do
  if [[ "$DEST" == "${PREFIX}"* ]]; then
    echo "ERROR: Destination falls in prohibited directory: ${PREFIX}/" >&2
    exit 1
  fi
done

# ─── Create destination directory and copy ────────────────────────────────────

DEST_DIR="$(dirname "$DEST")"
mkdir -p "$DEST_DIR"

if [[ -e "$DEST" ]]; then
  echo "ERROR: Destination already exists: $DEST" >&2
  exit 1
fi

cp "$SOURCE" "$DEST"

echo "COPIED: $SOURCE -> $DEST"
