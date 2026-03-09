#!/usr/bin/env python3
"""fix-exercise-types.py — Correct scl_types in exercise-registry.json.

Applies known corrections for exercises with wrong Type mappings,
validated against anatomy-index.json and CLAUDE.md routing rules.

Usage:
  python scripts/fix-exercise-types.py --dry-run    # preview changes
  python scripts/fix-exercise-types.py               # apply changes
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "middle-math" / "exercise-registry.json"

# Corrections derived from diagnose-type-misroutes.py analysis
# Format: canonical_name (lowercase) → correct scl_types
CORRECTIONS = {
    # Plyometrics with leg focus → dual type
    "single-leg pogo hops": ["Plus", "Legs"],
    "box jump": ["Plus", "Legs"],
    "box jump (step down)": ["Plus", "Legs"],
    "depth jump": ["Plus", "Legs"],
    "depth jump (to box)": ["Plus", "Legs"],
    "broad jump": ["Plus", "Legs"],
    "lateral bound": ["Plus", "Legs"],
    "tuck jump": ["Plus", "Legs"],
    "squat jump": ["Plus", "Legs"],

    # Push pattern exercises
    "scapular push-up": ["Push"],

    # Pull pattern exercises
    "band pull-apart": ["Pull"],
    "seated good morning": ["Pull"],

    # Plus (carries, kettlebell, strongman)
    "single-arm overhead carry": ["Plus"],
    "single-arm kettlebell swing": ["Plus"],
    "sandbag carry": ["Plus"],
    "kettlebell snatch": ["Plus"],

    # Get-up variants (all are Plus — full body anti-rotation)
    "double kettlebell get-up": ["Plus"],
    "naked get-up (bodyweight only)": ["Plus"],
    "half turkish get-up (to elbow)": ["Plus"],
    "turkish get-up (full)": ["Plus"],
    "turkish get-up (to seated)": ["Plus"],
    "turkish get-up (to kneeling)": ["Plus"],
    "bottoms-up turkish get-up": ["Plus"],
    "slow turkish get-up (10+ seconds per position)": ["Plus"],

    # Balance exercises with leg component
    "bosu ball single-leg balance": ["Legs", "Plus"],

    # Mobility/flexibility → correct routing
    "standing quad stretch": ["Legs"],

    # Jump rope variants → Ultra (conditioning)
    "single-leg jump rope": ["Ultra"],
    "double-unders (jump rope)": ["Ultra"],
    "double-unders": ["Ultra"],
    "jump rope": ["Ultra"],
    "jump rope (basic)": ["Ultra"],
}


# Movement-pattern → correct SCL Types routing (from CLAUDE.md)
# Used to fix catch-all exercises that have all 5 types
PATTERN_TYPE_MAP = {
    "hip-hinge": ["Pull"],           # Hinge = Pull (lats, erectors, posterior chain)
    "carry": ["Plus"],               # Carries = Plus (full body power)
    "anti-rotation": ["Plus"],       # Core anti-rotation = Plus
    "vertical-press": ["Push"],      # Vertical press = Push
    "horizontal-press": ["Push"],    # Horizontal press = Push
    "squat": ["Legs"],               # Squat = Legs
    "lunge": ["Legs"],               # Lunge = Legs
    "olympic": ["Plus"],             # Olympic lifts = Plus
    "plyometric": ["Plus", "Legs"],  # Plyometrics = Plus + Legs
    "isolation": ["Legs"],           # Default isolation to Legs (context-dependent)
    "mobility": ["Legs"],            # Mobility often legs-focused
    "row": ["Pull"],                 # Rows = Pull
    "pulldown": ["Pull"],            # Pulldowns = Pull
}


def main():
    parser = argparse.ArgumentParser(description="Fix exercise-registry.json scl_types")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    changes = []

    for entry in registry:
        name = entry.get("canonical_name", entry.get("name", "")).lower().strip()
        old_types = entry.get("scl_types", [])

        # Priority 1: explicit name-based corrections
        if name in CORRECTIONS:
            new_types = CORRECTIONS[name]
            if set(old_types) != set(new_types):
                changes.append({
                    "name": entry.get("canonical_name", name),
                    "from": old_types,
                    "to": new_types,
                    "reason": "explicit correction",
                })
                if not args.dry_run:
                    entry["scl_types"] = new_types
            continue

        # Priority 2: fix catch-all exercises (5 types) using movement_pattern
        if len(old_types) >= 5:
            pattern = entry.get("movement_pattern", "").lower().strip()
            if pattern in PATTERN_TYPE_MAP:
                new_types = PATTERN_TYPE_MAP[pattern]
                changes.append({
                    "name": entry.get("canonical_name", name),
                    "from": old_types,
                    "to": new_types,
                    "reason": f"pattern:{pattern}",
                })
                if not args.dry_run:
                    entry["scl_types"] = new_types

    print(f"Exercise-Type corrections: {len(changes)} exercises")
    for c in changes:
        reason = c.get('reason', '')
        print(f"  {c['name']}: {c['from']} → {c['to']}  [{reason}]")

    if not args.dry_run and changes:
        REGISTRY_PATH.write_text(
            json.dumps(registry, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"\nWritten {len(changes)} corrections to {REGISTRY_PATH}")
    elif args.dry_run:
        print(f"\n[DRY RUN] Would write {len(changes)} corrections")
    else:
        print("\nNo corrections needed.")


if __name__ == "__main__":
    main()
