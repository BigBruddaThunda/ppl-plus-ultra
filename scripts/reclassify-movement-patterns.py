#!/usr/bin/env python3
"""
reclassify-movement-patterns.py — Exercise Library v.1 Wave 1

Fixes the movement_pattern catch-all in exercise-registry.json.
1,339 exercises have 'core-stability' as a parsing artifact.
This script applies section-based defaults + name keyword matching
to reclassify them to correct patterns.

Usage:
  python scripts/reclassify-movement-patterns.py              # Apply and write
  python scripts/reclassify-movement-patterns.py --dry-run     # Preview changes
  python scripts/reclassify-movement-patterns.py --stats       # Show distribution before/after
"""

import argparse
import json
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

REPO_ROOT = Path(__file__).parent.parent
REGISTRY_PATH = REPO_ROOT / "middle-math" / "exercise-registry.json"

# ─────────────────────────────────────────────────────────────────────────────
# SECTION DEFAULT PATTERNS — fallback when no keyword match found
# ─────────────────────────────────────────────────────────────────────────────
SECTION_DEFAULTS = {
    "A": "isolation",       # Head & Neck — isolation/isometric
    "B": "vertical-press",  # Shoulders — pressing is primary; overridden by keywords for pulls
    "C": "horizontal-press",# Chest
    "D": "horizontal-pull", # Back — most back work is pulls; overridden for hinge/vertical
    "E": "isolation-curl",  # Arms — biceps default; overridden for triceps
    "F": "core-stability",  # Core — legitimately core-stability
    "G": "hip-hinge",       # Hips & Glutes
    "H": "squat",           # Thighs
    "I": "leg-isolation",   # Lower Leg & Foot
    "J": "olympic",         # Olympic Lifts
    "K": "plyometric",      # Plyometrics
    "L": "hip-hinge",       # Kettlebell — varies; hinge is most common
    "M": "conditioning",    # Cardio & Conditioning
    "N": "conditioning",    # Sport Focused
    "O": "conditioning",    # Footwork & Agility
    "P": "mobility",        # Stretching/Mobility — new pattern or isolation
    "Q": "carry",           # Strongman — varies; carry is characteristic
}

# ─────────────────────────────────────────────────────────────────────────────
# KEYWORD RULES — name-based pattern detection (order matters: first match wins)
# ─────────────────────────────────────────────────────────────────────────────
KEYWORD_RULES = [
    # Olympic patterns
    (["clean and jerk", "clean & jerk"], "olympic"),
    (["power clean", "hang clean", "squat clean", "full clean", "muscle clean"], "olympic"),
    (["power snatch", "hang snatch", "squat snatch", "muscle snatch", "full snatch"], "olympic"),
    (["clean pull", "snatch pull", "clean high pull", "snatch high pull"], "olympic"),
    (["jerk", "split jerk", "push jerk"], "olympic"),
    (["stone load", "stone lift", "atlas stone", "tire flip", "log clean"], "olympic"),

    # Carries
    (["carry", "farmer", "suitcase", "rack walk", "yoke walk", "loaded walk",
      "overhead walk", "sandbag carry", "keg carry", "zercher carry"], "carry"),

    # Conditioning
    (["sprint", "run ", "running", "treadmill", "bike", "cycling", "rowing machine",
      "rower", "assault bike", "ski erg", "jump rope", "skipping", "swim",
      "sled push", "sled pull", "sled drag", "prowler", "hiit", "interval",
      "steady state", "walk ", "walking", "stair", "shuttle", "burpee",
      "battle rope", "agility", "ladder drill", "cone drill", "footwork",
      "shuffle", "t-drill", "5-10-5"], "conditioning"),

    # Plyometric
    (["box jump", "broad jump", "depth jump", "tuck jump", "jump squat",
      "bound", "skip for", "hop ", "lateral hop", "single-leg hop",
      "plyometric", "reactive", "altitude drop"], "plyometric"),

    # Vertical pull
    (["pull-up", "pullup", "chin-up", "chinup", "lat pulldown", "pulldown",
      "pull down", "pull-down", "straight-arm pulldown", "straight arm pulldown",
      "shrug", "upright row"], "vertical-pull"),

    # Horizontal pull
    (["row", "face pull", "pull-apart", "band pull", "rear delt", "rear raise",
      "reverse fly", "reverse flye", "rear fly", "rear flye",
      "inverted row", "meadows row", "t-bar", "seal row", "chest-supported row",
      "cable row", "machine row", "pendlay"], "horizontal-pull"),

    # Vertical press
    (["overhead press", "shoulder press", "military press", "ohp",
      "push press", "lateral raise", "front raise", "arnold press",
      "z-press", "viking press", "log press", "axle press",
      "landmine press", "pike push", "handstand push",
      "bottoms-up press", "kettlebell press"], "vertical-press"),

    # Horizontal press
    (["bench press", "push-up", "pushup", "chest press",
      "flye", "fly ", "cable fly", "pec deck", "machine press",
      "dips", "decline press", "incline press", "floor press",
      "landmine chest", "svend press", "squeeze press",
      "cable crossover", "pullover"], "horizontal-press"),

    # Hip hinge
    (["deadlift", "rdl", "romanian", "good morning", "hip thrust",
      "glute bridge", "hyperextension", "back extension", "reverse hyper",
      "kettlebell swing", "stiff-leg", "rack pull", "hip hinge",
      "hip extension", "barbell hip", "dumbbell hip thrust"], "hip-hinge"),

    # Squat
    (["squat", "leg press", "hack squat", "goblet squat",
      "front squat", "back squat", "box squat", "pistol squat",
      "sissy squat", "zercher squat", "overhead squat"], "squat"),

    # Lunge
    (["lunge", "split squat", "bulgarian", "step-up", "step up",
      "curtsy", "walking lunge", "reverse lunge", "lateral lunge"], "lunge"),

    # Leg isolation
    (["leg curl", "leg extension", "calf raise", "tibialis",
      "hip abduction", "hip adduction", "clamshell", "donkey kick",
      "fire hydrant", "monster walk", "glute kickback", "nordic curl",
      "glute-ham raise", "ghr", "seated calf", "standing calf",
      "toe raise", "arch raise", "eversion", "inversion",
      "popliteus", "shin splint"], "leg-isolation"),

    # Isolation curl (biceps, forearm flexion)
    (["curl", "hammer curl", "preacher", "concentration curl",
      "spider curl", "cable curl", "incline curl", "reverse curl",
      "zottman", "wrist curl", "wrist flexion", "forearm curl",
      "pinch grip", "crush grip", "support grip", "grip training",
      "towel hang", "plate pinch", "gripper"], "isolation-curl"),

    # Isolation extension (triceps, forearm extension)
    (["tricep", "skull crusher", "pushdown", "push-down", "pressdown",
      "kickback", "overhead extension", "french press", "jm press",
      "close-grip bench", "diamond push", "wrist extension",
      "forearm extension", "pronation", "supination"], "isolation-extension"),

    # Anti-rotation
    (["pallof", "woodchop", "wood chop", "russian twist", "rotation",
      "rotational", "chop", "anti-rotation", "side bend",
      "windmill", "turkish get", "landmine rotation",
      "medicine ball throw", "medicine ball slam",
      "chest pass", "rotational throw", "lateral throw"], "anti-rotation"),

    # Core stability
    (["plank", "hollow", "dead bug", "bird dog", "crunch",
      "sit-up", "situp", "rollout", "ab wheel", "v-up",
      "mountain climber", "flutter kick", "leg raise",
      "bear crawl", "superman", "world's greatest",
      "hanging knee", "hanging leg", "toe-to-bar",
      "l-sit", "dragon flag", "protraction"], "core-stability"),

    # Isolation (generic — neck, face, jaw, stretching)
    (["neck ", "cervical", "chin tuck", "jaw", "face exercise",
      "scalene", "sternocleidomastoid", "neck bridge",
      "neck car", "head nod", "self-massage"], "isolation"),

    # Mobility (stretching, foam rolling, corrective)
    (["stretch", "mobility", "foam roll", "lacrosse ball",
      "trigger point", "pnf", "car ", "cars ", "yoga",
      "pigeon", "child's pose", "cat-cow", "hip circle",
      "hip car", "shoulder car", "thoracic", "somatic",
      "breathing", "pelvic floor", "diaphragm",
      "90/90", "frog stretch", "couch stretch",
      "world's greatest stretch"], "mobility"),
]

# Valid v.1 pattern vocabulary — expanded from 16 to 18
VALID_PATTERNS_V1 = {
    "hip-hinge", "squat", "lunge",
    "horizontal-press", "vertical-press",
    "horizontal-pull", "vertical-pull",
    "isolation-curl", "isolation-extension",
    "leg-isolation", "carry", "anti-rotation",
    "core-stability", "olympic", "conditioning",
    "plyometric", "isolation", "mobility",
}

# Anatomy updates for new patterns
ANATOMY_FOR_NEW_PATTERNS = {
    "isolation": {
        "primary_movers": ["target_muscle"],
        "secondary_movers": [],
        "stabilizers": ["core"],
        "joint_actions": ["single_joint_action"],
    },
    "mobility": {
        "primary_movers": ["target_tissue"],
        "secondary_movers": [],
        "stabilizers": [],
        "joint_actions": ["joint_mobilization", "tissue_lengthening"],
    },
}


def classify_exercise(exercise: dict) -> tuple:
    """Returns (new_pattern, reason) or (None, None) if no change needed."""
    current = exercise["movement_pattern"]

    # Only reclassify catch-all assignments
    if current != "core-stability":
        return None, None

    section = exercise.get("source_section", "")
    name_lower = exercise["name"].lower()

    # Section F exercises are legitimately core-stability — but check keywords first
    # to catch anti-rotation, carries, etc. in Section F

    # Try keyword rules first (most precise)
    for keywords, pattern in KEYWORD_RULES:
        for kw in keywords:
            if kw in name_lower:
                if pattern != current:
                    return pattern, f"keyword:{kw}"
                else:
                    return None, None  # Already correct

    # Fall back to section default
    section_default = SECTION_DEFAULTS.get(section, "core-stability")
    if section_default != current:
        return section_default, f"section:{section}"

    return None, None


def reclassify(registry: list, dry_run: bool = False) -> dict:
    """Reclassify movement patterns. Returns stats dict."""
    changes = []
    by_section = defaultdict(list)

    for ex in registry:
        new_pattern, reason = classify_exercise(ex)
        if new_pattern:
            changes.append({
                "id": ex["exercise_id"],
                "name": ex["name"],
                "section": ex.get("source_section", "?"),
                "old": ex["movement_pattern"],
                "new": new_pattern,
                "reason": reason,
            })
            if not dry_run:
                ex["movement_pattern"] = new_pattern
                # Update anatomy if moving to a new pattern with known anatomy
                if new_pattern in ANATOMY_FOR_NEW_PATTERNS:
                    anatomy = ANATOMY_FOR_NEW_PATTERNS[new_pattern]
                    # Only update if current anatomy is the generic core-stability one
                    if ex.get("primary_movers") == ["core", "transversus_abdominis", "rectus_abdominis"]:
                        ex["primary_movers"] = anatomy["primary_movers"]
                        ex["secondary_movers"] = anatomy["secondary_movers"]
                        ex["stabilizers"] = anatomy["stabilizers"]
                        ex["joint_actions"] = anatomy["joint_actions"]
            by_section[ex.get("source_section", "?")].append(new_pattern)

    return {
        "total_changes": len(changes),
        "changes": changes,
        "by_section": dict(by_section),
    }


def print_distribution(registry: list, label: str) -> None:
    """Print movement pattern distribution."""
    patterns = Counter(e["movement_pattern"] for e in registry)
    print(f"\n{'='*52}")
    print(f"Movement Pattern Distribution — {label}")
    print(f"{'='*52}")
    for p, c in patterns.most_common():
        pct = 100 * c / len(registry)
        bar = "#" * int(pct / 2)
        print(f"  {p:24} {c:5d} ({pct:5.1f}%) {bar}")
    print(f"\n  Total exercises: {len(registry)}")
    print(f"  Unique patterns: {len(patterns)}")

    # Check for catch-all dominance
    cs_count = patterns.get("core-stability", 0)
    cs_pct = 100 * cs_count / len(registry)
    if cs_pct > 40:
        print(f"\n  WARNING: core-stability is {cs_pct:.1f}% — catch-all likely still present")
    else:
        print(f"\n  core-stability: {cs_pct:.1f}% — within expected range")


def main():
    parser = argparse.ArgumentParser(description="Reclassify movement patterns in exercise registry")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--stats", action="store_true", help="Show before/after distribution")
    parser.add_argument("--verbose", action="store_true", help="Show each change")
    args = parser.parse_args()

    with open(REGISTRY_PATH, encoding="utf-8") as f:
        registry = json.load(f)

    print(f"Loaded {len(registry)} exercises from {REGISTRY_PATH}")

    if args.stats:
        print_distribution(registry, "BEFORE")

    result = reclassify(registry, dry_run=args.dry_run)

    if args.verbose:
        print(f"\n{'='*52}")
        print(f"Changes ({result['total_changes']} exercises)")
        print(f"{'='*52}")
        for c in result["changes"]:
            print(f"  {c['id']} [{c['section']}] {c['old']:20} → {c['new']:20} ({c['reason']}) — {c['name']}")

    if args.stats:
        if not args.dry_run:
            print_distribution(registry, "AFTER")
        else:
            # Simulate for stats
            temp = json.loads(json.dumps(registry))
            reclassify(temp, dry_run=False)
            print_distribution(temp, "AFTER (simulated)")

    print(f"\nReclassified: {result['total_changes']} exercises")

    # Section breakdown
    section_counts = defaultdict(int)
    for changes in result["by_section"].values():
        for _ in changes:
            pass
    for c in result["changes"]:
        section_counts[c["section"]] += 1
    if section_counts:
        print("\nBy section:")
        for s, c in sorted(section_counts.items()):
            print(f"  Section {s}: {c} reclassified")

    # Validate all patterns are in vocabulary
    invalid = set()
    for ex in registry:
        if ex["movement_pattern"] not in VALID_PATTERNS_V1:
            invalid.add(ex["movement_pattern"])
    if invalid:
        print(f"\nWARNING: Invalid patterns found: {invalid}", file=sys.stderr)
        sys.exit(1)

    if not args.dry_run:
        with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
            json.dump(registry, f, indent=2, ensure_ascii=False)
        size_kb = REGISTRY_PATH.stat().st_size // 1024
        print(f"\nWrote {REGISTRY_PATH} (~{size_kb} KB)")
    else:
        print("\nDry run — no changes written.")


if __name__ == "__main__":
    main()
