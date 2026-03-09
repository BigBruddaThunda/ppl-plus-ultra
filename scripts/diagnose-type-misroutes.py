#!/usr/bin/env python3
"""diagnose-type-misroutes.py — Root-cause analysis for exercise-Type mismatches.

Reads the quality audit JSON and exercise-registry.json, groups mismatches by
exercise name and card Type, and determines whether the issue is:
  (a) Wrong scl_types in the registry (library error)
  (b) Exercise placed in wrong card Type (generation error)

Usage:
  python scripts/diagnose-type-misroutes.py reports/deck-quality-audit-pre-rebuild.json
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_registry() -> dict[str, dict]:
    """Load exercise registry, index by lowercase canonical name."""
    path = ROOT / "middle-math" / "exercise-registry.json"
    entries = json.loads(path.read_text(encoding="utf-8"))
    index = {}
    for e in entries:
        name = e.get("canonical_name", e.get("name", "")).lower().strip()
        if name:
            index[name] = e
    return index


# CLAUDE.md Type routing rules
SECTION_TYPE_MAP = {
    "C": ["Push"],       # Chest
    "B": ["Push"],       # Shoulders (anterior/lateral) — some posterior = Pull
    "D": ["Pull"],       # Back
    "E": ["Push", "Pull"],  # Arms (triceps=Push, biceps=Pull)
    "G": ["Pull", "Legs"],  # Hips (hinge=Pull, glute=Legs)
    "H": ["Legs"],       # Thighs
    "I": ["Legs"],       # Lower Leg
    "F": ["Plus"],       # Core
    "J": ["Plus"],       # Olympic Lifts
    "K": ["Plus", "Ultra"],  # Plyometrics
    "L": ["Plus"],       # Kettlebell
    "Q": ["Plus"],       # Strongman
    "M": ["Ultra"],      # Cardio & Conditioning
    "O": ["Ultra"],      # Footwork & Agility
    "N": ["Ultra"],      # Sport Focused
}

# Known corrections based on exercise anatomy and CLAUDE.md routing
KNOWN_CORRECTIONS = {
    "single-leg jump rope": ["Ultra"],        # Cardio/conditioning, not Legs
    "double-unders (jump rope)": ["Ultra"],   # Cardio/conditioning
    "double-unders": ["Ultra"],
    "jump rope": ["Ultra"],
    "single-leg pogo hops": ["Plus", "Legs"], # Plyometric with leg focus
    "box jump": ["Plus", "Legs"],             # Plyometric with leg focus
    "box jump (step down)": ["Plus", "Legs"],
    "turkish get-up": ["Plus"],               # Full body power/core
    "turkish get-up (partial - shoulder focus)": ["Plus", "Push"],
    "push jerk": ["Plus"],                    # Olympic lift derivative
    "push jerk (barbell)": ["Plus"],
    "power snatch": ["Plus"],                 # Olympic lift
    "power snatch (barbell)": ["Plus"],
    "muscle snatch": ["Plus"],
    "muscle snatch (barbell)": ["Plus"],
    "yoke walk": ["Plus"],                    # Strongman
    "sandbag carry": ["Plus"],
    "standing quad stretch": ["Legs"],        # Correctly Legs
    "bosu ball single-leg balance": ["Legs", "Plus"],
    "scapular push-up": ["Push"],             # Push pattern
    "single-arm kettlebell swing": ["Plus"],  # Kettlebell = Plus
    "single-arm overhead carry": ["Plus"],    # Carry = Plus
    "single-leg romanian deadlift": ["Legs", "Pull"],  # Hinge + legs
    "seated good morning": ["Pull"],          # Hinge = Pull
    "band pull-apart": ["Pull"],              # Rear delt/upper back = Pull
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/diagnose-type-misroutes.py <audit.json>")
        sys.exit(1)

    audit_path = sys.argv[1]
    audit = json.loads(Path(audit_path).read_text(encoding="utf-8"))
    registry = load_registry()

    # Collect all TYPE_MISMATCH flags
    mismatches = []
    for card in audit["cards"]:
        for flag in card.get("flags", []):
            if flag.startswith("TYPE_MISMATCH:"):
                detail = flag.split(":", 1)[1]
                ex_name, claimed_types = detail.split("→", 1)
                mismatches.append({
                    "exercise": ex_name,
                    "claimed_types": claimed_types.split(","),
                    "card_type": card.get("type_name", "?"),
                    "card_zip": card.get("zip", "?"),
                    "deck": card.get("deck", "?"),
                })

    print(f"\n{'='*60}")
    print(f"TYPE MISROUTE DIAGNOSIS — {len(mismatches)} total flags")
    print(f"{'='*60}\n")

    # Group by exercise
    by_exercise = defaultdict(list)
    for m in mismatches:
        by_exercise[m["exercise"]].append(m)

    print(f"{'EXERCISE':<45} {'COUNT':>5}  {'REGISTRY scl_types':<25} {'CARD TYPES':<20} {'DIAGNOSIS'}")
    print("-" * 130)

    library_errors = 0
    generation_errors = 0
    both_errors = 0

    for ex_name, items in sorted(by_exercise.items(), key=lambda x: -len(x[1])):
        count = len(items)
        card_types = set(m["card_type"] for m in items)
        claimed = set()
        for m in items:
            claimed.update(m["claimed_types"])

        # Look up in registry
        reg_entry = registry.get(ex_name.lower().strip())
        if reg_entry:
            reg_types = reg_entry.get("scl_types", [])
        else:
            reg_types = ["(not found)"]

        # Determine if this is a known correction
        known = KNOWN_CORRECTIONS.get(ex_name.lower().strip())

        # Diagnose
        if known:
            # Check if registry matches known correct types
            reg_matches_known = set(reg_types) == set(known)
            cards_match_known = all(ct in known for ct in card_types)

            if not reg_matches_known and not cards_match_known:
                diagnosis = "BOTH: registry wrong + card misplaced"
                both_errors += count
            elif not reg_matches_known:
                diagnosis = "REGISTRY: scl_types need correction"
                library_errors += count
            elif not cards_match_known:
                diagnosis = "GENERATION: exercise in wrong card Type"
                generation_errors += count
            else:
                diagnosis = "FALSE POSITIVE: audit matching issue"
        else:
            # No known correction — flag for review
            diagnosis = "NEEDS REVIEW"

        print(f"{ex_name:<45} {count:>5}  {','.join(reg_types):<25} {','.join(card_types):<20} {diagnosis}")

    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"  Registry errors:   {library_errors:>5} flags")
    print(f"  Generation errors: {generation_errors:>5} flags")
    print(f"  Both:              {both_errors:>5} flags")
    print(f"  Total:             {len(mismatches):>5} flags")
    print(f"  Unique exercises:  {len(by_exercise):>5}")

    # Output corrections needed
    print(f"\n{'='*60}")
    print(f"REGISTRY CORRECTIONS NEEDED")
    print(f"{'='*60}")
    corrections = {}
    for ex_name in by_exercise:
        known = KNOWN_CORRECTIONS.get(ex_name.lower().strip())
        if known:
            reg_entry = registry.get(ex_name.lower().strip())
            if reg_entry:
                current = reg_entry.get("scl_types", [])
                if set(current) != set(known):
                    corrections[ex_name] = {"from": current, "to": known}

    for ex_name, change in corrections.items():
        print(f"  {ex_name}: {change['from']} → {change['to']}")

    print(f"\n  Total corrections: {len(corrections)}")


if __name__ == "__main__":
    main()
