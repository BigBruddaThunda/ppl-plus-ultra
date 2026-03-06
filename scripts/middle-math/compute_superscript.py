#!/usr/bin/env python3
"""
scripts/middle-math/compute_superscript.py
CX-27: Superscript/Subscript Data Model

Superscript = system suggestions derived from weight vector + visit history.
Subscript   = user overrides (equipment preferences, injury flags, bookmarks).

These two layers work together to personalize the experience without
surveillance or manipulation. The system makes suggestions. The user overrides.
There is no dark pattern — user preferences always win.

Design principle (from seeds/systems-eudaimonics.md):
  Superscript suggests; subscript decides. The system earns trust by being
  right more often than it is wrong. User overrides are permanent until removed.

Schema: Adds user_preferences and superscript_cache tables.
Source tables: rooms, zip_metadata (from sql/008-room-schema-extension.sql)

Usage:
    python scripts/middle-math/compute_superscript.py --demo
    python scripts/middle-math/compute_superscript.py --schema
    python scripts/middle-math/compute_superscript.py --zip 2123 --demo
"""

import json
import sys
import argparse
import random
from pathlib import Path
from datetime import date, timedelta

REPO_ROOT     = Path(__file__).resolve().parent.parent.parent
REGISTRY_PATH = REPO_ROOT / "middle-math" / "zip-registry.json"
VECTORS_PATH  = REPO_ROOT / "middle-math" / "weight-vectors.json"

# ---------------------------------------------------------------------------
# Schema definitions
# ---------------------------------------------------------------------------

SQL_SCHEMA = """
-- CX-27: Superscript/Subscript schema additions
-- Extends sql/008-room-schema-extension.sql

-- ---------------------------------------------------------------------------
-- user_preferences: The subscript layer — permanent user overrides
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS user_preferences (
  id              UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id         UUID        NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,

  -- Equipment preferences (subscript)
  max_equipment_tier   INTEGER     DEFAULT 5,          -- 0–5, default = all equipment
  excluded_tiers       INTEGER[]   DEFAULT '{}',       -- specific tiers to exclude
  no_barbell           BOOLEAN     NOT NULL DEFAULT FALSE,
  no_machines          BOOLEAN     NOT NULL DEFAULT FALSE,

  -- Injury flags (subscript)
  injury_flags         TEXT[]      DEFAULT '{}',
  -- Known valid flags: 'no_overhead', 'no_squat', 'no_deadlift', 'no_running',
  --                    'no_pushing', 'no_pulling', 'no_rotation', 'no_impact'

  -- Bookmarks (handled in room_bookmarks, referenced here for join efficiency)
  bookmark_count  INTEGER     NOT NULL DEFAULT 0,

  -- Preferred orders / colors (positive signal)
  preferred_orders     TEXT[]      DEFAULT '{}',
  preferred_colors     TEXT[]      DEFAULT '{}',

  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_user_preferences_user
  ON user_preferences (user_id);

ALTER TABLE user_preferences ENABLE ROW LEVEL SECURITY;
CREATE POLICY user_preferences_user_policy ON user_preferences
  FOR ALL USING (auth.uid() = user_id);

-- ---------------------------------------------------------------------------
-- superscript_cache: Pre-computed system suggestions per user per zip
-- Refreshed on visit, on log, or on schedule.
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS superscript_cache (
  id              UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id         UUID        NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  numeric_zip     CHAR(4)     NOT NULL REFERENCES zip_metadata(numeric_zip),

  -- Weight-vector-derived adjacent suggestions (top 3)
  adjacent_zips   JSONB       NOT NULL DEFAULT '[]',
  -- Format: [{"numeric_zip": "2123", "emoji_zip": "⛽🏛🪡🔵", "score": 42.1, "reason": "Same deck, higher bloom"}, ...]

  -- Recency signal
  days_since_visit     INTEGER,    -- NULL if never visited
  last_visit_date      DATE,

  -- Bloom-weighted boost
  bloom_at_zip    INTEGER     NOT NULL DEFAULT 0,

  -- Staleness tracking
  computed_at     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  valid_until     TIMESTAMPTZ,    -- NULL = always valid until next visit

  UNIQUE (user_id, numeric_zip)
);

CREATE INDEX IF NOT EXISTS idx_superscript_cache_user_zip
  ON superscript_cache (user_id, numeric_zip);

ALTER TABLE superscript_cache ENABLE ROW LEVEL SECURITY;
CREATE POLICY superscript_cache_user_policy ON superscript_cache
  FOR ALL USING (auth.uid() = user_id);

-- ---------------------------------------------------------------------------
-- room_bookmarks: User bookmarks (the subscript bookmark layer)
-- ---------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS room_bookmarks (
  id          UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id     UUID        NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  numeric_zip CHAR(4)     NOT NULL REFERENCES zip_metadata(numeric_zip),
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  UNIQUE (user_id, numeric_zip)
);

ALTER TABLE room_bookmarks ENABLE ROW LEVEL SECURITY;
CREATE POLICY room_bookmarks_user_policy ON room_bookmarks
  FOR ALL USING (auth.uid() = user_id);
"""


# ---------------------------------------------------------------------------
# Superscript computation
# ---------------------------------------------------------------------------

def cosine_similarity(a: list, b: list) -> float:
    """Compute cosine similarity between two vectors."""
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = sum(x * x for x in a) ** 0.5
    mag_b = sum(x * x for x in b) ** 0.5
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot / (mag_a * mag_b)


def dot_product(a: list, b: list) -> float:
    return sum(x * y for x, y in zip(a, b))


def find_adjacent_zips(
    target_zip: str,
    all_vectors: dict,
    top_n: int = 3,
    same_deck_only: bool = True,
) -> list:
    """
    Find the most similar zip codes to the target using vector similarity.

    Adjacent = semantically close (similar weight vector), not necessarily
    the same deck. same_deck_only=True restricts to same deck for UI coherence.

    Returns list of {numeric_zip, emoji_zip, score, reason} dicts.
    """
    if target_zip not in all_vectors:
        return []

    target_data = all_vectors[target_zip]
    target_vec  = target_data["vector"]
    target_deck = target_data.get("deck")

    scored = []
    for zip_code, data in all_vectors.items():
        if zip_code == target_zip:
            continue
        if same_deck_only and data.get("deck") != target_deck:
            continue

        vec   = data["vector"]
        score = cosine_similarity(target_vec, vec)
        scored.append((score, zip_code, data["emoji_zip"]))

    scored.sort(reverse=True)
    top = scored[:top_n]

    return [
        {
            "numeric_zip": z,
            "emoji_zip":   e,
            "score":       round(s, 4),
            "reason":      "Same deck, high vector similarity",
        }
        for s, z, e in top
    ]


# ---------------------------------------------------------------------------
# Subscript filters
# ---------------------------------------------------------------------------

def apply_subscript_filters(
    zip_entry: dict,
    prefs: dict,
) -> dict:
    """
    Apply user subscript preferences to determine if a zip is accessible.

    Args:
        zip_entry: Registry entry for the zip code.
        prefs:     User preferences dict.

    Returns:
        {"accessible": bool, "blocked_reasons": [str], "modified": bool}
    """
    blocked_reasons = []
    color_emoji = zip_entry.get("color", {}).get("emoji", "")

    # Equipment tier check
    COLOR_TIER_MIN = {
        "⚫": 2, "🟢": 0, "🔵": 2, "🟣": 2,
        "🔴": 2, "🟠": 0, "🟡": 0, "⚪": 0,
    }
    color_tier_min = COLOR_TIER_MIN.get(color_emoji, 0)

    if prefs.get("no_barbell") and color_tier_min >= 3:
        blocked_reasons.append(
            f"no_barbell preference: {color_emoji} requires tier ≥3 (barbell)"
        )

    if prefs.get("no_machines"):
        COLOR_TIER_MAX = {
            "⚫": 3, "🟢": 2, "🔵": 3, "🟣": 5,
            "🔴": 4, "🟠": 3, "🟡": 5, "⚪": 3,
        }
        color_tier_max = COLOR_TIER_MAX.get(color_emoji, 5)
        if color_tier_max >= 4:
            blocked_reasons.append(
                f"no_machines preference: {color_emoji} allows tier 4+ (machines/cables)"
            )

    # Injury flag checks (movement-level filtering — affects exercise selection, not zip)
    injury_flags = prefs.get("injury_flags", [])
    type_emoji   = zip_entry.get("type", {}).get("emoji", "")

    INJURY_TYPE_CONFLICTS = {
        "no_overhead": {"🛒"},   # Push includes overhead press
        "no_pushing":  {"🛒"},
        "no_pulling":  {"🪡"},
        "no_squat":    {"🍗"},
        "no_deadlift": {"🪡"},   # Deadlift is Pull-type
        "no_running":  {"➖"},
        "no_impact":   {"➕", "➖"},
    }

    for flag in injury_flags:
        conflicting_types = INJURY_TYPE_CONFLICTS.get(flag, set())
        if type_emoji in conflicting_types:
            blocked_reasons.append(
                f"Injury flag '{flag}': conflicts with {type_emoji} Type exercises"
            )

    accessible = len(blocked_reasons) == 0
    return {
        "accessible":      accessible,
        "blocked_reasons": blocked_reasons,
        "modified":        len(injury_flags) > 0 and accessible,
    }


# ---------------------------------------------------------------------------
# Full superscript record
# ---------------------------------------------------------------------------

def compute_superscript_record(
    numeric_zip: str,
    all_vectors: dict,
    zip_registry_lookup: dict,
    user_context: dict,
) -> dict:
    """
    Compute the complete superscript record for a user-zip pair.

    Args:
        numeric_zip:         The 4-digit zip code.
        all_vectors:         Loaded weight-vectors.json dict.
        zip_registry_lookup: Lookup by numeric zip from zip-registry.json.
        user_context:        Synthetic or real user context dict.

    Returns:
        Full superscript record dict.
    """
    zip_entry    = zip_registry_lookup.get(numeric_zip, {})
    emoji_zip    = zip_entry.get("emoji_zip", numeric_zip)

    # Superscript: adjacent suggestions
    adjacent = find_adjacent_zips(numeric_zip, all_vectors, top_n=3)

    # Visit context
    last_visit  = user_context.get("last_visit_date")
    days_since  = None
    if last_visit:
        try:
            last_dt    = date.fromisoformat(last_visit)
            days_since = (date.today() - last_dt).days
        except ValueError:
            pass

    bloom = user_context.get("bloom_level", 0)

    # Subscript: filter assessment
    prefs        = user_context.get("preferences", {})
    filter_result = apply_subscript_filters(zip_entry, prefs)
    bookmarked   = user_context.get("bookmarked", False)

    return {
        "numeric_zip": numeric_zip,
        "emoji_zip":   emoji_zip,
        "superscript": {
            "adjacent_suggestions": adjacent,
            "days_since_visit":     days_since,
            "last_visit_date":      last_visit,
            "bloom_level":          bloom,
        },
        "subscript": {
            "bookmarked":        bookmarked,
            "preferences_active": len(prefs) > 0,
            "filter_result":     filter_result,
        },
    }


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

DEMO_USER_CONTEXTS = [
    {
        "label":          "New user, no preferences",
        "last_visit_date": None,
        "bloom_level":    0,
        "bookmarked":     False,
        "preferences":    {},
    },
    {
        "label":          "Regular user, no barbell",
        "last_visit_date": (date.today() - timedelta(days=3)).isoformat(),
        "bloom_level":    2,
        "bookmarked":     False,
        "preferences":    {"no_barbell": True},
    },
    {
        "label":          "Active user, bookmarked, shoulder injury",
        "last_visit_date": (date.today() - timedelta(days=1)).isoformat(),
        "bloom_level":    4,
        "bookmarked":     True,
        "preferences":    {"injury_flags": ["no_overhead"]},
    },
    {
        "label":          "Deep user, no machines",
        "last_visit_date": (date.today() - timedelta(days=14)).isoformat(),
        "bloom_level":    5,
        "bookmarked":     True,
        "preferences":    {"no_machines": True},
    },
    {
        "label":          "Lapsed user, no preferences",
        "last_visit_date": (date.today() - timedelta(days=90)).isoformat(),
        "bloom_level":    3,
        "bookmarked":     False,
        "preferences":    {},
    },
]

DEMO_ZIPS = ["2123", "1111", "3345", "5251", "7168"]


def run_demo(
    zip_list: list,
    all_vectors: dict,
    zip_registry_lookup: dict,
) -> None:
    """Print demo superscript table for sample zips."""
    random.seed(42)

    print("\n" + "═" * 72)
    print("  CX-27 Superscript/Subscript Data Model — Demo")
    print("  Superscript = system suggestions | Subscript = user overrides")
    print("═" * 72)

    for i, (numeric_zip, user_ctx) in enumerate(zip(zip_list, DEMO_USER_CONTEXTS)):
        zip_entry = zip_registry_lookup.get(numeric_zip, {})
        emoji_zip = zip_entry.get("emoji_zip", numeric_zip)

        record = compute_superscript_record(
            numeric_zip, all_vectors, zip_registry_lookup, user_ctx
        )

        sup = record["superscript"]
        sub = record["subscript"]

        print(f"\n  {emoji_zip} ({numeric_zip})  —  {user_ctx['label']}")
        print(f"  {'─' * 68}")
        print(f"  SUPERSCRIPT (system suggestions):")
        print(f"    Bloom level:       {sup['bloom_level']}")
        print(f"    Days since visit:  {sup['days_since_visit'] if sup['days_since_visit'] is not None else 'never'}")
        if sup["adjacent_suggestions"]:
            print(f"    Adjacent zips:")
            for adj in sup["adjacent_suggestions"]:
                print(f"      {adj['emoji_zip']} ({adj['numeric_zip']})  score={adj['score']:.4f}  {adj['reason']}")
        else:
            print(f"    Adjacent zips:     (none found)")

        print(f"\n  SUBSCRIPT (user overrides):")
        print(f"    Bookmarked:        {'yes' if sub['bookmarked'] else 'no'}")
        fr = sub["filter_result"]
        if fr["accessible"]:
            if fr["modified"]:
                print(f"    Accessible:        yes (injury flags active — exercise-level filtering applies)")
            else:
                print(f"    Accessible:        yes")
        else:
            print(f"    Accessible:        NO — blocked by preferences:")
            for reason in fr["blocked_reasons"]:
                print(f"      ✗ {reason}")

    print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="CX-27: PPL± Superscript/Subscript Data Model"
    )
    parser.add_argument("--demo",   action="store_true",
                        help="Show 5 sample zips with synthetic user contexts")
    parser.add_argument("--schema", action="store_true",
                        help="Print SQL schema for user_preferences and superscript_cache tables")
    parser.add_argument("--zip",    type=str,
                        help="Compute superscript for a specific zip code (with --demo)")

    args = parser.parse_args()

    if args.schema:
        print(SQL_SCHEMA)
        return

    if args.demo:
        print("Loading data...", end=" ", flush=True)
        registry    = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        all_vectors = json.loads(VECTORS_PATH.read_text(encoding="utf-8"))
        zip_lookup  = {e["numeric_zip"]: e for e in registry}
        print(f"done. {len(registry)} zips, {len(all_vectors)} vectors.")

        if args.zip:
            # Single zip, cycle through all demo contexts
            zip_list = [args.zip] * len(DEMO_USER_CONTEXTS)
        else:
            zip_list = DEMO_ZIPS

        run_demo(zip_list, all_vectors, zip_lookup)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
