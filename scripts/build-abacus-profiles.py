#!/usr/bin/env python3
"""build-abacus-profiles.py — Generate per-abacus context profiles.

For each of the 35 abaci, produces a JSON profile containing:
- Archetype identity (name, domain, description, axis_bias, weights)
- Zip assignments (working + bonus)
- Filtered exercise pool (exercises available to this archetype)
- Block preferences (emphasized/de-emphasized blocks)
- Color postures (per-color natural-language descriptions)
- Identity statement (auto-generated, refinable by human)

Usage:
    python scripts/build-abacus-profiles.py              # build all 35 profiles
    python scripts/build-abacus-profiles.py --slug general-strength  # build one
    python scripts/build-abacus-profiles.py --stats       # print summary from existing profiles
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
ABACUS_REGISTRY = REPO_ROOT / "middle-math" / "abacus-registry.json"
EXERCISE_REGISTRY = REPO_ROOT / "middle-math" / "exercise-registry.json"
PROFILES_DIR = REPO_ROOT / "middle-math" / "abacus-profiles"

# Import ARCHETYPES from compile-abacus
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from compile_abacus_loader import load_archetypes

# ---------------------------------------------------------------------------
# SCL Constants
# ---------------------------------------------------------------------------
ORDER_EMOJIS = ["🐂", "⛽", "🦋", "🏟", "🌾", "⚖", "🖼"]
AXIS_EMOJIS = ["🏛", "🔨", "🌹", "🪐", "⌛", "🐬"]
TYPE_EMOJIS = ["🛒", "🪡", "🍗", "➕", "➖"]
COLOR_EMOJIS = ["⚫", "🟢", "🔵", "🟣", "🔴", "🟠", "🟡", "⚪"]

AXIS_NAME_TO_EMOJI = {
    "Basics": "🏛", "Functional": "🔨", "Aesthetic": "🌹",
    "Challenge": "🪐", "Time": "⌛", "Partner": "🐬",
}
AXIS_EMOJI_TO_NAME = {v: k for k, v in AXIS_NAME_TO_EMOJI.items()}

AXIS_AFFINITY_KEY = {
    "🏛": "classic", "🔨": "functional", "🌹": "aesthetic",
    "🪐": "challenge", "⌛": "time", "🐬": "partner",
}

ORDER_AFFINITY_KEY = {
    "🐂": "foundation", "⛽": "strength", "🦋": "hypertrophy",
    "🏟": "performance", "🌾": "full_body", "⚖": "balance", "🖼": "restoration",
}

TYPE_NAME_MAP = {
    "🛒": "Push", "🪡": "Pull", "🍗": "Legs", "➕": "Plus", "➖": "Ultra",
}

COLOR_NAMES = {
    "⚫": "Teaching", "🟢": "Bodyweight", "🔵": "Structured", "🟣": "Technical",
    "🔴": "Intense", "🟠": "Circuit", "🟡": "Fun", "⚪": "Mindful",
}

COLOR_TIERS = {
    "⚫": (2, 3), "🟢": (0, 2), "🔵": (2, 3), "🟣": (2, 5),
    "🔴": (2, 4), "🟠": (0, 3), "🟡": (0, 5), "⚪": (0, 3),
}

GOLD_COLORS = {"🟣", "🔴"}

# Block preferences by domain
DOMAIN_BLOCK_PREFERENCES = {
    "strength": {
        "emphasized": ["🧈", "▶️", "🪜", "🧩"],
        "de_emphasized": ["🏖", "🌎", "🪞", "🎱"],
    },
    "hypertrophy": {
        "emphasized": ["🧈", "🗿", "🪞", "🧩"],
        "de_emphasized": ["🪜", "🏗"],
    },
    "conditioning": {
        "emphasized": ["🧈", "🎱", "🌎"],
        "de_emphasized": ["🗿", "🪞", "🪜"],
    },
    "functional": {
        "emphasized": ["🧈", "🎼", "🌎", "🛠"],
        "de_emphasized": ["🪞", "🗿"],
    },
    "life-stage": {
        "emphasized": ["🧈", "🔢", "🛠", "🧬"],
        "de_emphasized": ["🌋", "🎱"],
    },
    "recovery": {
        "emphasized": ["🧈", "🪫", "🏗", "🧬"],
        "de_emphasized": ["🌋", "🎱", "🪜"],
    },
    "specialty": {
        "emphasized": ["🧈", "🛠", "▶️"],
        "de_emphasized": ["🪞"],
    },
}

# ---------------------------------------------------------------------------
# Identity Statement Templates (by domain)
# ---------------------------------------------------------------------------

DOMAIN_IDENTITY_TEMPLATES = {
    "strength": (
        "{name} is built for moving heavy things. {description}. "
        "The {axis_word} bias means exercises lean toward {axis_feel}. "
        "You walk in, load up, execute the program, and leave stronger."
    ),
    "hypertrophy": (
        "{name} is built for building muscle. {description}. "
        "The {axis_word} bias means exercises lean toward {axis_feel}. "
        "Volume drives growth; form keeps it honest."
    ),
    "conditioning": (
        "{name} is built for energy systems. {description}. "
        "The {axis_word} bias means sessions lean toward {axis_feel}. "
        "Capacity is the currency — aerobic, anaerobic, or mixed."
    ),
    "functional": (
        "{name} is built for transfer. {description}. "
        "The {axis_word} bias means exercises lean toward {axis_feel}. "
        "If it does not transfer outside the gym, it does not belong here."
    ),
    "life-stage": (
        "{name} is built for where you are right now. {description}. "
        "The {axis_word} bias means exercises lean toward {axis_feel}. "
        "The program meets the person, not the other way around."
    ),
    "recovery": (
        "{name} is built for restoration. {description}. "
        "The {axis_word} bias means sessions lean toward {axis_feel}. "
        "You leave fresher than you entered."
    ),
    "specialty": (
        "{name} is built for a specific craft. {description}. "
        "The {axis_word} bias means exercises lean toward {axis_feel}. "
        "Precision in the discipline is the measure."
    ),
}

AXIS_FEEL = {
    "🏛": "proven bilateral classics — barbell staples, bilateral over unilateral",
    "🔨": "athletic transfer — unilateral, standing, ground-based movement",
    "🌹": "isolation and feel — mind-muscle connection, full ROM, cables and machines",
    "🪐": "the hardest variation — deficit, pause, tempo, bands, chains",
    "⌛": "timed protocols — EMOM, AMRAP, density blocks, steady state",
    "🐬": "partner-compatible movements — spottable, alternating, synchronized",
}

# ---------------------------------------------------------------------------
# Color Posture Templates (by domain × color)
# ---------------------------------------------------------------------------

COLOR_POSTURE_TEMPLATES = {
    # Default postures (domain-agnostic)
    "default": {
        "⚫": "Walk-through session with coaching cues, extended rest, comprehension over exertion",
        "🟢": "Bodyweight-only version — no gym required, prove the pattern transfers",
        "🔵": "Prescribed sets, reps, rest — trackable, repeatable, progressive",
        "🟣": "Precision session — lower volume, extended rest, quality focus",
        "🔴": "Maximum effort — high volume, reduced rest, push the ceiling",
        "🟠": "Station-based rotation — no barbells, tissue-trading loop logic",
        "🟡": "Exploration and variety — structured play within constraints",
        "⚪": "Slow tempo (4s eccentrics), extended rest (2+ min), breath-paced",
    },
    # Domain-specific overrides
    "strength": {
        "⚫": "Teaches barbell setup, loading sequence, and safety positions for heavy compound lifts",
        "🟢": "Bodyweight strength check — does gym strength transfer? Advanced calisthenics apply",
        "🔵": "Linear progression tracking — same weight, same reps, add load when form holds",
        "🟣": "Single-rep quality at competition-relevant loads — bar path, timing, setup",
        "🔴": "Heavy working sets with full recovery — push the ceiling, earn every rep",
        "🟠": "Station rotation with implements — keep tissues trading under heavy demand",
        "🟡": "Unconventional loading patterns — grip variations, odd positions, new challenges",
        "⚪": "4s eccentrics under moderate barbell load — tendon adaptation, breath-paced",
    },
    "hypertrophy": {
        "⚫": "Teaches mind-muscle connection, tempo awareness, and tension quality under moderate load",
        "🟢": "Bodyweight hypertrophy — high reps, slow tempo, squeeze and hold patterns",
        "🔵": "Volume tracking — prescribed sets and reps, progressive overload through logging",
        "🟣": "Precision isolation — feel every fiber, full ROM, cable and machine emphasis",
        "🔴": "Chase the pump — high volume, low rest, supersets allowed, metabolic stress",
        "🟠": "Muscle group circuit — each station hits a different angle on the target tissue",
        "🟡": "Novel exercises for new stimulus — variety drives adaptation when volume plateaus",
        "⚪": "Time under tension protocol — slow eccentrics build tissue that fast reps miss",
    },
    "conditioning": {
        "⚫": "Teaches pacing, zone awareness, and movement economy for energy system work",
        "🟢": "Bodyweight conditioning — no gym, no excuses, cardio and movement flow",
        "🔵": "Prescribed intervals — zone targets, heart rate windows, timed rest",
        "🟣": "Technical conditioning — rowing stroke, cycling cadence, running gait precision",
        "🔴": "All-out intervals — max effort, full recovery, repeat until capacity drops",
        "🟠": "Mixed-modality circuit — each station changes the energy demand",
        "🟡": "Unconventional cardio — explore modalities outside normal training",
        "⚪": "Zone 2 steady state — conversational pace, extended duration, aerobic base",
    },
    "functional": {
        "⚫": "Teaches movement quality, ground-based patterns, and transfer mechanics",
        "🟢": "Bodyweight functional — park, field, living room — prove the pattern works anywhere",
        "🔵": "Prescribed functional progressions — track load, complexity, and movement quality",
        "🟣": "Movement precision — deceleration, landing mechanics, rotational control",
        "🔴": "High-output functional work — explosive repeats, full effort, game-speed",
        "🟠": "Athletic circuit — each station trains a different movement pattern",
        "🟡": "Movement exploration — unconventional patterns, play with load and position",
        "⚪": "Controlled functional movement — slow transitions, balance holds, proprioception",
    },
    "life-stage": {
        "⚫": "Teaching session — learn the movement, understand the cues, build confidence",
        "🟢": "Bodyweight only — safe, accessible, no equipment barrier to entry",
        "🔵": "Structured progression — small increments, clear targets, consistent tracking",
        "🟣": "Quality focus — fewer movements, more attention, technique over load",
        "🔴": "Effort within safe limits — work hard at appropriate intensity",
        "🟠": "Gentle circuit — station rotation with manageable transitions",
        "🟡": "Fun and discovery — explore movements that feel good and build capability",
        "⚪": "Recovery and restoration — breath work, gentle movement, nervous system regulation",
    },
    "recovery": {
        "⚫": "Teaches what recovery feels like — coaching the nervous system, not the muscles",
        "🟢": "Floor work, breath, gentle movement — restore with what your body provides",
        "🔵": "Follow the restoration sequence as prescribed — each position has a purpose",
        "🟣": "Precise positioning in restorative holds — depth over speed, accuracy over range",
        "🔴": "Active recovery — move enough to flush, not enough to fatigue",
        "🟠": "Restoration circuit — each station addresses a different tissue or system",
        "🟡": "Somatic exploration — movements you would not normally try, body awareness",
        "⚪": "Deep parasympathetic work — breathe into each position, leave fresher than you entered",
    },
    "specialty": {
        "⚫": "Teaches the craft-specific positions, timing, and coordination demands",
        "🟢": "Bodyweight drills for the discipline — positional strength without load",
        "🔵": "Prescribed progression in the discipline — structured path to mastery",
        "🟣": "Masterclass — 1-on-1 with a world-class coach at this exact skill",
        "🔴": "Competition-intensity effort — perform at full capacity, discipline-specific",
        "🟠": "Skill circuit — rotate through craft-specific stations",
        "🟡": "Cross-training exploration — adjacent skills that improve the primary craft",
        "⚪": "Recovery within the discipline — slow, mindful practice of the core positions",
    },
}


# ---------------------------------------------------------------------------
# Exercise Pool Filtering
# ---------------------------------------------------------------------------

def score_exercise_for_archetype(exercise: dict, archetype: dict) -> float:
    """Score an exercise's fit for an archetype using axis/order affinity weights."""
    score = 1.0

    # Axis affinity scoring
    axis_weights = archetype["axis_weights"]
    ex_axis = exercise.get("axis_affinity", {})
    for emoji, weight in axis_weights.items():
        key = AXIS_AFFINITY_KEY.get(emoji, "")
        if key and key in ex_axis:
            # Normalize: axis_affinity values are 1-10, weights are 0-1
            score += weight * (ex_axis[key] / 10.0)

    # Order bias scoring
    order_bias = archetype.get("order_bias", {})
    ex_order = exercise.get("order_affinity", {})
    for emoji, bias in order_bias.items():
        key = ORDER_AFFINITY_KEY.get(emoji, "")
        if key and key in ex_order:
            score += (bias - 1.0) * (ex_order[key] / 10.0)

    # Type bias
    type_bias = archetype.get("type_bias", {})
    for ex_type in exercise.get("scl_types", []):
        type_emoji = {"Push": "🛒", "Pull": "🪡", "Legs": "🍗", "Plus": "➕", "Ultra": "➖"}.get(ex_type)
        if type_emoji and type_emoji in type_bias:
            score *= type_bias[type_emoji]

    return score


def filter_exercise_pool(exercises: list[dict], archetype: dict) -> dict:
    """Filter exercises to create the abacus's available pool, organized by Type."""
    pool_by_type: dict[str, list[dict]] = {t: [] for t in ["Push", "Pull", "Legs", "Plus", "Ultra"]}
    gold_exercises: list[str] = []

    # Determine which equipment tiers are available based on color weights
    # Colors with weight >= 0.2 are considered "available" in this archetype
    available_tiers = set()
    color_weights = archetype["color_weights"]
    for color_emoji, weight in color_weights.items():
        if weight >= 0.15:  # Low threshold — most colors are available
            lo, hi = COLOR_TIERS[color_emoji]
            for t in range(lo, hi + 1):
                available_tiers.add(t)

    for ex in exercises:
        # Equipment tier check
        ex_tier = ex.get("equipment_tier", [0, 5])
        if not any(t in available_tiers for t in range(ex_tier[0], ex_tier[1] + 1)):
            continue

        # GOLD gate check
        is_gold = ex.get("gold_gated", False)
        if is_gold and not archetype.get("gold_affinity", False):
            # Still include in pool — but only for 🔴/🟣 contexts
            # Mark as gold for downstream filtering
            pass

        # Score the exercise
        score = score_exercise_for_archetype(ex, archetype)

        for ex_type in ex.get("scl_types", []):
            if ex_type in pool_by_type:
                pool_by_type[ex_type].append({
                    "exercise_id": ex["exercise_id"],
                    "name": ex["name"],
                    "score": round(score, 3),
                    "gold_gated": is_gold,
                    "family_id": ex.get("family_id", "unknown"),
                    "equipment_tier": ex_tier,
                })

        if is_gold:
            gold_exercises.append(ex["exercise_id"])

    # Sort each type pool by score (descending)
    for type_name in pool_by_type:
        pool_by_type[type_name].sort(key=lambda x: x["score"], reverse=True)

    # Build ID-only lists for the profile (full scored list is too large)
    pool_ids_by_type = {}
    for type_name, entries in pool_by_type.items():
        pool_ids_by_type[type_name] = [e["exercise_id"] for e in entries]

    total = sum(len(v) for v in pool_by_type.values())

    # Also track excluded families (families with 0 exercises in pool)
    all_families = set()
    pool_families = set()
    for ex in exercises:
        fam = ex.get("family_id", "unknown")
        all_families.add(fam)
    for type_entries in pool_by_type.values():
        for entry in type_entries:
            pool_families.add(entry["family_id"])
    excluded = sorted(all_families - pool_families)

    return {
        "total": total,
        "by_type": pool_ids_by_type,
        "by_type_scored": {t: entries[:20] for t, entries in pool_by_type.items()},  # Top 20 per type for reference
        "gold_exercises": sorted(set(gold_exercises)),
        "excluded_families": excluded,
    }


# ---------------------------------------------------------------------------
# Identity Statement Generation
# ---------------------------------------------------------------------------

def generate_identity_statement(archetype: dict) -> str:
    """Generate a natural-language identity statement for the archetype."""
    domain = archetype["domain"]
    template = DOMAIN_IDENTITY_TEMPLATES.get(domain, DOMAIN_IDENTITY_TEMPLATES["strength"])

    axis_bias = archetype.get("axis_bias_emoji", "🏛")
    if not axis_bias:
        # Derive from axis_weights
        weights = archetype["axis_weights"]
        axis_bias = max(weights, key=weights.get)

    axis_word = AXIS_EMOJI_TO_NAME.get(axis_bias, "Basics")
    axis_feel = AXIS_FEEL.get(axis_bias, "proven fundamentals")

    return template.format(
        name=archetype["name"],
        description=archetype["description"],
        axis_word=axis_word,
        axis_feel=axis_feel,
    )


# ---------------------------------------------------------------------------
# Color Posture Generation
# ---------------------------------------------------------------------------

def generate_color_postures(archetype: dict) -> dict[str, str]:
    """Generate per-color posture descriptions for the archetype."""
    domain = archetype["domain"]
    postures = dict(COLOR_POSTURE_TEMPLATES.get("default", {}))

    # Override with domain-specific postures
    domain_postures = COLOR_POSTURE_TEMPLATES.get(domain, {})
    postures.update(domain_postures)

    return postures


# ---------------------------------------------------------------------------
# Profile Builder
# ---------------------------------------------------------------------------

def build_profile(archetype: dict, registry_data: dict, exercises: list[dict]) -> dict:
    """Build a complete abacus profile for one archetype."""

    # Find this archetype in the registry
    abacus_entry = None
    for ab in registry_data["abaci"]:
        if ab["id"] == archetype["id"]:
            abacus_entry = ab
            break

    if not abacus_entry:
        print(f"  WARNING: Archetype {archetype['id']} ({archetype['name']}) not found in registry")
        return None

    # Derive axis_bias emoji from archetype weights
    axis_weights = archetype["axis_weights"]
    axis_bias_emoji = max(axis_weights, key=axis_weights.get)

    # Build exercise pool
    exercise_pool = filter_exercise_pool(exercises, archetype)

    # Build block preferences
    domain = archetype["domain"]
    block_prefs = DOMAIN_BLOCK_PREFERENCES.get(domain, DOMAIN_BLOCK_PREFERENCES["strength"])

    # Generate identity statement
    archetype_with_bias = dict(archetype)
    archetype_with_bias["axis_bias_emoji"] = axis_bias_emoji
    identity = generate_identity_statement(archetype_with_bias)

    # Generate color postures
    color_postures = generate_color_postures(archetype)

    # Assemble zips
    working_zips = abacus_entry.get("working_zips", [])
    bonus_zips = abacus_entry.get("bonus_zips", [])
    all_zips = list(working_zips) + [b["zip"] for b in bonus_zips]

    profile = {
        "id": archetype["id"],
        "name": archetype["name"],
        "slug": archetype["slug"],
        "domain": domain,
        "description": archetype["description"],
        "axis_bias": axis_bias_emoji,
        "identity_statement": identity,

        "weights": {
            "axis_weights": archetype["axis_weights"],
            "color_weights": archetype["color_weights"],
            "order_bias": archetype.get("order_bias", {}),
            "type_bias": archetype.get("type_bias", {}),
            "gold_affinity": archetype.get("gold_affinity", False),
        },

        "zips": {
            "working": working_zips,
            "bonus": bonus_zips,
            "all": all_zips,
        },

        "exercise_pool": {
            "total": exercise_pool["total"],
            "by_type": exercise_pool["by_type"],
            "top_scored": exercise_pool["by_type_scored"],
            "gold_exercises": exercise_pool["gold_exercises"],
            "excluded_families": exercise_pool["excluded_families"],
        },

        "block_preferences": {
            "emphasized": block_prefs.get("emphasized", []),
            "de_emphasized": block_prefs.get("de_emphasized", []),
            "forbidden": block_prefs.get("forbidden", []),
        },

        "color_postures": color_postures,
    }

    return profile


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def print_stats():
    """Print summary from existing profiles."""
    if not PROFILES_DIR.exists():
        print("No profiles directory found.")
        return

    profiles = sorted(PROFILES_DIR.glob("*.json"))
    profiles = [p for p in profiles if p.name != "index.json"]

    if not profiles:
        print("No profiles found.")
        return

    print(f"PPL± Abacus Profiles — {len(profiles)} profiles")
    print("=" * 60)

    for p in profiles:
        data = json.loads(p.read_text(encoding="utf-8"))
        pool = data.get("exercise_pool", {})
        zips = data.get("zips", {})
        by_type = pool.get("by_type", {})
        type_counts = {t: len(ids) for t, ids in by_type.items()}

        print(f"\n  {data['id']:2d}. {data['name']}")
        print(f"      Domain: {data['domain']} | Axis: {data['axis_bias']} | Gold: {data['weights']['gold_affinity']}")
        print(f"      Zips: {len(zips.get('working', []))} working + {len(zips.get('bonus', []))} bonus")
        print(f"      Exercises: {pool.get('total', 0)} total | {' '.join(f'{t}:{c}' for t, c in type_counts.items())}")
        print(f"      Gold: {len(pool.get('gold_exercises', []))} | Excluded families: {len(pool.get('excluded_families', []))}")

    # Index summary
    index_path = PROFILES_DIR / "index.json"
    if index_path.exists():
        idx = json.loads(index_path.read_text(encoding="utf-8"))
        print(f"\n  Index: {len(idx.get('profiles', []))} entries")


def main():
    parser = argparse.ArgumentParser(description="Build abacus context profiles")
    parser.add_argument("--slug", help="Build only this archetype (by slug)")
    parser.add_argument("--stats", action="store_true", help="Print summary from existing profiles")
    args = parser.parse_args()

    if args.stats:
        print_stats()
        return

    # Load data
    print("Loading abacus registry...")
    registry_data = json.loads(ABACUS_REGISTRY.read_text(encoding="utf-8"))

    print("Loading exercise registry...")
    exercises = json.loads(EXERCISE_REGISTRY.read_text(encoding="utf-8"))
    print(f"  {len(exercises)} exercises loaded")

    print("Loading archetypes...")
    archetypes = load_archetypes()
    print(f"  {len(archetypes)} archetypes loaded")

    # Create output directory
    PROFILES_DIR.mkdir(parents=True, exist_ok=True)

    # Filter to single slug if requested
    if args.slug:
        archetypes = [a for a in archetypes if a["slug"] == args.slug]
        if not archetypes:
            print(f"ERROR: No archetype with slug '{args.slug}'")
            sys.exit(1)

    # Build profiles
    index_entries = []
    for arch in archetypes:
        print(f"  Building profile: {arch['id']:2d}. {arch['name']}...")
        profile = build_profile(arch, registry_data, exercises)
        if profile is None:
            continue

        # Write profile
        out_path = PROFILES_DIR / f"{arch['slug']}.json"
        out_path.write_text(
            json.dumps(profile, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        pool = profile["exercise_pool"]
        print(f"      → {pool['total']} exercises | {len(profile['zips']['all'])} zips | wrote {out_path.name}")

        index_entries.append({
            "id": profile["id"],
            "name": profile["name"],
            "slug": profile["slug"],
            "domain": profile["domain"],
            "axis_bias": profile["axis_bias"],
            "gold_affinity": profile["weights"]["gold_affinity"],
            "exercise_count": pool["total"],
            "zip_count": len(profile["zips"]["all"]),
            "working_count": len(profile["zips"]["working"]),
            "bonus_count": len(profile["zips"]["bonus"]),
        })

    # Write index
    index_path = PROFILES_DIR / "index.json"
    index_data = {
        "total_profiles": len(index_entries),
        "profiles": index_entries,
    }
    index_path.write_text(
        json.dumps(index_data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"\nWrote index: {index_path}")
    print(f"Done. {len(index_entries)} profiles built.")


if __name__ == "__main__":
    main()
