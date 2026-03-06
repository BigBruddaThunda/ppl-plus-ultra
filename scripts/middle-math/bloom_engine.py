#!/usr/bin/env python3
"""
scripts/middle-math/bloom_engine.py
CX-24: Bloom State Engine

Computes depth-of-engagement (bloom level) per user per room.

Bloom is NOT gamification. There are no streaks. No decay. No loss-aversion.
Bloom only grows or plateaus — it never punishes absence.
The metric rewards genuine depth of engagement, not frequency alone.

Bloom levels:
  0 — Unvisited
  1 — Visited at least once
  2 — Visited 3+ times
  3 — Logged at least one session (actual workout completed)
  4 — Logged 3+ sessions
  5 — Voted (quality signal) AND logged 5+ sessions

Design principle (from seeds/systems-eudaimonics.md):
  Value accrues through use, not withholding. Bloom reflects real training
  depth. A user who visits once and never returns stays at bloom=1 forever.
  A user who trains consistently reaches bloom=5 at their own pace.
  There is no timer. There is no punishment for absence.

Schema reference: sql/008-room-schema-extension.sql
  - rooms.bloom_level (int, 0–5)
  - room_visits (append-only log)
  - bloom_history (append-only transition log)

Usage:
    python scripts/middle-math/bloom_engine.py --demo
    python scripts/middle-math/bloom_engine.py --schema
"""

import json
import sys
import argparse
import random
from pathlib import Path
from datetime import datetime, timedelta

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
REGISTRY_PATH = REPO_ROOT / "middle-math" / "zip-registry.json"

# ---------------------------------------------------------------------------
# Bloom level thresholds
# ---------------------------------------------------------------------------

# Each level specifies the MINIMUM required to reach it.
# Levels are cumulative: level 3 requires level 2's conditions PLUS a logged session.
BLOOM_LEVELS = {
    0: {"description": "Unvisited",                    "requires": "no visits"},
    1: {"description": "Visited",                      "requires": "visit_count >= 1"},
    2: {"description": "Regular",                      "requires": "visit_count >= 3"},
    3: {"description": "Active",                       "requires": "logged_count >= 1"},
    4: {"description": "Committed",                    "requires": "logged_count >= 3"},
    5: {"description": "Deep",                         "requires": "voted == True AND logged_count >= 5"},
}


def compute_bloom(visit_count: int, logged_count: int, voted: bool) -> int:
    """
    Compute the bloom level for a user-room pair.

    Bloom is monotone: it never decreases.
    The returned level reflects the HIGHEST level whose conditions are met.

    Args:
        visit_count:  Total number of times the user has visited this room.
        logged_count: Number of completed workout sessions logged at this room.
        voted:        True if the user has submitted a quality vote for this room.

    Returns:
        int: bloom level 0–5
    """
    if voted and logged_count >= 5:
        return 5
    if logged_count >= 3:
        return 4
    if logged_count >= 1:
        return 3
    if visit_count >= 3:
        return 2
    if visit_count >= 1:
        return 1
    return 0


def should_transition(
    current_bloom: int,
    visit_count: int,
    logged_count: int,
    voted: bool,
) -> bool:
    """
    Determine whether a bloom transition should occur.

    Returns True if the computed bloom level exceeds the current recorded level.
    Bloom never decreases, so transitions only move upward.

    Args:
        current_bloom: The bloom level currently stored in the database.
        visit_count:   Total visit count.
        logged_count:  Total logged session count.
        voted:         Whether the user has voted.

    Returns:
        bool: True if the bloom level should increase.
    """
    new_bloom = compute_bloom(visit_count, logged_count, voted)
    return new_bloom > current_bloom


def bloom_label(level: int) -> str:
    """Return the human-readable label for a bloom level."""
    return BLOOM_LEVELS.get(level, {}).get("description", f"Level {level}")


def bloom_transition_reason(
    old_level: int,
    new_level: int,
    visit_count: int,
    logged_count: int,
    voted: bool,
) -> str:
    """Generate a human-readable reason string for a bloom transition."""
    reasons = {
        (0, 1): f"First visit (visit #{visit_count})",
        (1, 2): f"3rd visit reached (visit #{visit_count})",
        (2, 3): f"First session logged (log #{logged_count})",
        (3, 4): f"3rd session logged (log #{logged_count})",
        (4, 5): f"Quality vote submitted + 5 sessions logged",
    }
    return reasons.get((old_level, new_level), f"Level {old_level} → {new_level}")


# ---------------------------------------------------------------------------
# Bloom state record
# ---------------------------------------------------------------------------

class BloomState:
    """Represents the bloom state for a user-room pair."""

    def __init__(
        self,
        numeric_zip: str,
        emoji_zip: str,
        visit_count: int,
        logged_count: int,
        voted: bool,
        current_stored_bloom: int = 0,
    ):
        self.numeric_zip         = numeric_zip
        self.emoji_zip           = emoji_zip
        self.visit_count         = visit_count
        self.logged_count        = logged_count
        self.voted               = voted
        self.stored_bloom        = current_stored_bloom
        self.computed_bloom      = compute_bloom(visit_count, logged_count, voted)
        self.needs_transition    = should_transition(
            current_stored_bloom, visit_count, logged_count, voted
        )

    def to_dict(self) -> dict:
        return {
            "zip":                self.numeric_zip,
            "emoji_zip":          self.emoji_zip,
            "visit_count":        self.visit_count,
            "logged_count":       self.logged_count,
            "voted":              self.voted,
            "stored_bloom":       self.stored_bloom,
            "computed_bloom":     self.computed_bloom,
            "bloom_label":        bloom_label(self.computed_bloom),
            "needs_transition":   self.needs_transition,
        }


# ---------------------------------------------------------------------------
# Schema output
# ---------------------------------------------------------------------------

SQL_SCHEMA = """
-- Bloom state computed view (or materialized column)
-- Source: sql/008-room-schema-extension.sql (base tables)
-- CX-24: Bloom Engine schema additions

-- Option A: Computed column approach (for PostgreSQL 12+ generated columns)
-- Add to the rooms table ALTER TABLE or inline in 008-room-schema-extension.sql:

ALTER TABLE rooms
  ADD COLUMN IF NOT EXISTS bloom_level_computed INTEGER
  GENERATED ALWAYS AS (
    CASE
      WHEN bloom_voted AND bloom_logged_count >= 5 THEN 5
      WHEN bloom_logged_count >= 3                 THEN 4
      WHEN bloom_logged_count >= 1                 THEN 3
      WHEN bloom_visit_count >= 3                  THEN 2
      WHEN bloom_visit_count >= 1                  THEN 1
      ELSE 0
    END
  ) STORED;

-- Supporting columns (add to rooms table if not present):
ALTER TABLE rooms
  ADD COLUMN IF NOT EXISTS bloom_visit_count  INTEGER NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS bloom_logged_count INTEGER NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS bloom_voted        BOOLEAN NOT NULL DEFAULT FALSE;

-- Option B: Function (more portable)
CREATE OR REPLACE FUNCTION compute_bloom(
  p_visit_count  INTEGER,
  p_logged_count INTEGER,
  p_voted        BOOLEAN
) RETURNS INTEGER AS $$
BEGIN
  IF p_voted AND p_logged_count >= 5 THEN RETURN 5; END IF;
  IF p_logged_count >= 3             THEN RETURN 4; END IF;
  IF p_logged_count >= 1             THEN RETURN 3; END IF;
  IF p_visit_count >= 3              THEN RETURN 2; END IF;
  IF p_visit_count >= 1              THEN RETURN 1; END IF;
  RETURN 0;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- Bloom history log (append-only, matches 008-room-schema-extension.sql pattern)
CREATE TABLE IF NOT EXISTS bloom_history (
  id             UUID        PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id        UUID        NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  numeric_zip    CHAR(4)     NOT NULL REFERENCES zip_metadata(numeric_zip),
  old_bloom      INTEGER     NOT NULL,
  new_bloom      INTEGER     NOT NULL,
  reason         TEXT,
  transitioned_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Index for fast user+zip lookup
CREATE INDEX IF NOT EXISTS idx_bloom_history_user_zip
  ON bloom_history (user_id, numeric_zip);

-- RLS: users see only their own bloom history
ALTER TABLE bloom_history ENABLE ROW LEVEL SECURITY;
CREATE POLICY bloom_history_user_policy ON bloom_history
  FOR ALL USING (auth.uid() = user_id);
"""


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

def generate_demo_data(registry: list, n: int = 10) -> list:
    """Generate synthetic visit history for demo output."""
    random.seed(42)
    sample_zips = random.sample(registry, min(n, len(registry)))

    scenarios = [
        # (visit_count, logged_count, voted, description)
        (0,  0, False, "Never visited"),
        (1,  0, False, "One visit, no log"),
        (3,  0, False, "3 visits, no log"),
        (5,  1, False, "5 visits, 1 log"),
        (8,  3, False, "8 visits, 3 logs"),
        (12, 5, False, "12 visits, 5 logs, no vote"),
        (15, 5, True,  "15 visits, 5 logs + voted"),
        (2,  0, False, "2 visits, no log"),
        (10, 2, False, "10 visits, 2 logs"),
        (20, 8, True,  "20 visits, 8 logs + voted"),
    ]

    results = []
    for entry, (visits, logs, voted, desc) in zip(sample_zips, scenarios[:len(sample_zips)]):
        state = BloomState(
            numeric_zip=entry["numeric_zip"],
            emoji_zip=entry["emoji_zip"],
            visit_count=visits,
            logged_count=logs,
            voted=voted,
            current_stored_bloom=0,
        )
        results.append({"state": state, "scenario": desc})
    return results


def print_demo(demo_data: list) -> None:
    """Print demo bloom state table."""
    print("\n" + "═" * 70)
    print("  CX-24 Bloom Engine — Demo")
    print("  No streaks. No decay. Bloom only grows.")
    print("═" * 70)
    header = f"  {'ZIP':<12} {'EMOJI':<14} {'VISITS':>6} {'LOGS':>5} {'VOTED':>6} {'BLOOM':>6}  LABEL"
    print(header)
    print("  " + "─" * 66)

    for item in demo_data:
        s = item["state"]
        voted_str = "yes" if s.voted else "no"
        bloom_lbl = bloom_label(s.computed_bloom)
        transition = " ← TRANSITION" if s.needs_transition else ""
        print(
            f"  {s.numeric_zip:<12} {s.emoji_zip:<14} {s.visit_count:>6} "
            f"{s.logged_count:>5} {voted_str:>6} {s.computed_bloom:>6}  "
            f"{bloom_lbl}{transition}"
        )
        print(f"    Scenario: {item['scenario']}")

    print("\n  Bloom level definitions:")
    for level, defn in BLOOM_LEVELS.items():
        print(f"    {level} — {defn['description']:<14}  ({defn['requires']})")

    print("\n  Eudaimonic guarantee: absence has ZERO negative effect.")
    print("  Bloom cannot decrease. It only grows or plateaus.\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="CX-24: PPL± Bloom State Engine"
    )
    parser.add_argument("--demo",   action="store_true",
                        help="Simulate 10 zips with sample visit history")
    parser.add_argument("--schema", action="store_true",
                        help="Print SQL schema for bloom state columns and history table")
    parser.add_argument("--compute", nargs=3,
                        metavar=("VISITS", "LOGS", "VOTED"),
                        help="Compute bloom for given values: VISITS LOGS VOTED(0|1)")

    args = parser.parse_args()

    if args.schema:
        print(SQL_SCHEMA)
        return

    if args.compute:
        visits = int(args.compute[0])
        logs   = int(args.compute[1])
        voted  = bool(int(args.compute[2]))
        level  = compute_bloom(visits, logs, voted)
        print(f"  Bloom({visits} visits, {logs} logs, voted={voted}) → {level} ({bloom_label(level)})")
        return

    if args.demo:
        registry  = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        demo_data = generate_demo_data(registry, n=10)
        print_demo(demo_data)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
