#!/usr/bin/env python3
"""
scripts/middle-math/envelope_stamper.py
CX-30: Envelope Schema & Stamping Prototype

The envelope is the atomic retrieval unit for the PPL± system.
Every room lookup, every Operis sandbox selection, every exercise recommendation
resolves through an envelope. This script stamps envelopes.

Design reference: seeds/scl-envelope-architecture.md
  "Every piece of content carries a frozen weight vector envelope capturing the
  SCL state at creation time. Condition-based matching (not calendar-based)
  using 61-dimension similarity between content envelopes and the live vector."

Envelope schema (version 1.0):
  {
    "envelope_version": "1.0",
    "stamped_at": "<ISO8601>",
    "zip": {
      "numeric": "2123",
      "emoji": "⛽🏛🪡🔵",
      "order": {"position": 2, "emoji": "⛽", "name": "Strength"},
      "axis":  {"position": 1, "emoji": "🏛", "name": "Basics"},
      "type":  {"position": 2, "emoji": "🪡", "name": "Pull"},
      "color": {"position": 3, "emoji": "🔵", "name": "Structured"},
      "operator": {"emoji": "🤌", "name": "facio"},
      "deck_number": 7,
      "gold_eligible": false,
      "polarity": "expressive"
    },
    "weight_vector": {
      "base": [61 floats],
      "vote_adjusted": [61 floats] | null
    },
    "user_context": {
      "user_id": null,
      "bloom_level": null,
      "bloom_description": null,
      "superscript": null,
      "subscript": null
    }
  }

Tier distinction:
  Anonymous envelope — base identity + weight vector. Free tier. No user context.
  Full envelope     — includes vote adjustment, bloom level, superscript, subscript.
                      Requires user context. Paid tier.

Usage:
    python scripts/middle-math/envelope_stamper.py --zip 2123 --anonymous
    python scripts/middle-math/envelope_stamper.py --zip 2123 --full
    python scripts/middle-math/envelope_stamper.py --zip ⛽🏛🪡🔵 --anonymous
    python scripts/middle-math/envelope_stamper.py --deck 07 --anonymous
    python scripts/middle-math/envelope_stamper.py --deck 07 --full
"""

import json
import sys
import argparse
import random
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
REGISTRY_PATH = REPO_ROOT / "middle-math" / "zip-registry.json"
WEIGHT_VECTORS_PATH = REPO_ROOT / "middle-math" / "weight-vectors.json"

SCRIPTS_PATH = REPO_ROOT / "scripts" / "middle-math"
sys.path.insert(0, str(SCRIPTS_PATH))

# ---------------------------------------------------------------------------
# Import sibling engines
# ---------------------------------------------------------------------------

from vote_weight_adjuster import compute_adjusted as _compute_vote_adjusted
from bloom_engine import compute_bloom, BLOOM_LEVELS

# compute_superscript_record requires all_vectors and registry_lookup
# We import it and supply the loaded data at call time
from compute_superscript import compute_superscript_record, find_adjacent_zips

ENVELOPE_VERSION = "1.0"

# ---------------------------------------------------------------------------
# Data loading (lazy, module-level cache)
# ---------------------------------------------------------------------------

_registry_by_numeric = None
_weight_vectors = None


def _load_registry() -> dict:
    global _registry_by_numeric
    if _registry_by_numeric is None:
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            raw = json.load(f)
        _registry_by_numeric = {entry["numeric_zip"]: entry for entry in raw}
    return _registry_by_numeric


def _load_weight_vectors() -> dict:
    global _weight_vectors
    if _weight_vectors is None:
        with open(WEIGHT_VECTORS_PATH, encoding="utf-8") as f:
            _weight_vectors = json.load(f)
    return _weight_vectors


# ---------------------------------------------------------------------------
# Zip resolution (shared with vote_weight_adjuster)
# ---------------------------------------------------------------------------

ORDER_POSITIONS = {
    "🐂": 1, "⛽": 2, "🦋": 3, "🏟": 4, "🌾": 5, "⚖": 6, "🖼": 7,
}
AXIS_POSITIONS = {
    "🏛": 1, "🔨": 2, "🌹": 3, "🪐": 4, "⌛": 5, "🐬": 6,
}
TYPE_POSITIONS = {
    "🛒": 1, "🪡": 2, "🍗": 3, "➕": 4, "➖": 5,
}
COLOR_POSITIONS = {
    "⚫": 1, "🟢": 2, "🔵": 3, "🟣": 4, "🔴": 5, "🟠": 6, "🟡": 7, "⚪": 8,
}


def _resolve_numeric_zip(zip_code: str) -> str:
    """Accept emoji or 4-digit numeric zip, return 4-digit numeric."""
    zip_code = zip_code.strip()
    if zip_code.isdigit() and len(zip_code) == 4:
        return zip_code

    registry = _load_registry()
    for entry in registry.values():
        if entry.get("emoji_zip") == zip_code:
            return entry["numeric_zip"]

    # Try matching by emoji components
    all_emojis = {**ORDER_POSITIONS, **AXIS_POSITIONS, **TYPE_POSITIONS, **COLOR_POSITIONS}
    found = [ch for ch in zip_code if ch in all_emojis]
    if len(found) == 4:
        o = ORDER_POSITIONS.get(found[0])
        a = AXIS_POSITIONS.get(found[1])
        t = TYPE_POSITIONS.get(found[2])
        c = COLOR_POSITIONS.get(found[3])
        if None not in (o, a, t, c):
            return f"{o}{a}{t}{c}"

    raise ValueError(f"Cannot resolve zip code: {repr(zip_code)}")


# ---------------------------------------------------------------------------
# Mock user context (for --full demo mode)
# ---------------------------------------------------------------------------

def _mock_user_context(numeric_zip: str, seed: int = None) -> dict:
    """Generate a plausible mock user context for demo purposes."""
    rng = random.Random(seed or int(numeric_zip))
    visit_count = rng.randint(0, 20)
    logged_count = rng.randint(0, min(visit_count, 10))
    voted = rng.random() > 0.6 and logged_count >= 2
    bookmarked = rng.random() > 0.7

    # Simulate recent votes
    n_votes = rng.randint(0, 25)
    votes = [
        {
            "user_id": f"mock_user_{rng.randint(1000, 9999)}",
            "vote_value": rng.choice([-1, 1]),
            "timestamp": "2026-03-06T10:00:00Z",
        }
        for _ in range(n_votes)
    ]

    return {
        "user_id": f"mock_user_{int(numeric_zip):04d}",
        "visit_count": visit_count,
        "logged_count": logged_count,
        "voted": voted,
        "bookmarked": bookmarked,
        "last_visit_date": "2026-03-05" if visit_count > 0 else None,
        "preferences": {
            "max_equipment_tier": 5,
            "no_barbell": False,
            "injury_flags": [],
        },
        "votes": votes,
    }


# ---------------------------------------------------------------------------
# Core envelope assembly
# ---------------------------------------------------------------------------

def stamp_envelope(zip_code: str, user_context: dict = None) -> dict:
    """
    Stamp a complete envelope for a zip code.

    Args:
        zip_code:     Emoji zip or 4-digit numeric zip.
        user_context: Dict with user engagement data, or None for anonymous envelope.

    Returns:
        Complete envelope dict (anonymous or full depending on user_context).
    """
    numeric_zip = _resolve_numeric_zip(zip_code)
    registry = _load_registry()
    weight_vectors = _load_weight_vectors()

    if numeric_zip not in registry:
        raise KeyError(f"Zip {numeric_zip} not found in zip-registry.json")
    if numeric_zip not in weight_vectors:
        raise KeyError(f"Zip {numeric_zip} not found in weight-vectors.json")

    reg_entry = registry[numeric_zip]
    base_vector = weight_vectors[numeric_zip]["vector"]

    # --- Zip identity block ---
    zip_block = {
        "numeric": numeric_zip,
        "emoji": reg_entry["emoji_zip"],
        "order": reg_entry["order"],
        "axis": reg_entry["axis"],
        "type": reg_entry["type"],
        "color": reg_entry["color"],
        "operator": reg_entry["operator"],
        "deck_number": reg_entry["deck_number"],
        "gold_eligible": reg_entry.get("gold_eligible", False),
        "polarity": reg_entry.get("polarity", "unknown"),
    }

    # --- Weight vector block ---
    if user_context is not None:
        votes = user_context.get("votes", [])
        vote_result = _compute_vote_adjusted(numeric_zip, votes)
        vote_adjusted = vote_result["adjusted_vector"]
        vote_summary = vote_result["vote_summary"]
    else:
        vote_adjusted = None
        vote_summary = None

    weight_block = {
        "base": base_vector,
        "vote_adjusted": vote_adjusted,
        "vote_summary": vote_summary,
    }

    # --- User context block ---
    if user_context is not None:
        visit_count = user_context.get("visit_count", 0)
        logged_count = user_context.get("logged_count", 0)
        voted = user_context.get("voted", False)

        bloom_level = compute_bloom(visit_count, logged_count, voted)
        bloom_description = BLOOM_LEVELS[bloom_level]["description"]

        # Superscript and subscript from compute_superscript
        super_sub = compute_superscript_record(
            numeric_zip,
            all_vectors=weight_vectors,
            zip_registry_lookup=registry,
            user_context={
                "bloom_level": bloom_level,
                "last_visit_date": user_context.get("last_visit_date"),
                "bookmarked": user_context.get("bookmarked", False),
                "preferences": user_context.get("preferences", {}),
            },
        )

        user_block = {
            "user_id": user_context.get("user_id"),
            "bloom_level": bloom_level,
            "bloom_description": bloom_description,
            "visit_count": visit_count,
            "logged_count": logged_count,
            "voted": voted,
            "superscript": super_sub["superscript"],
            "subscript": super_sub["subscript"],
        }
    else:
        user_block = {
            "user_id": None,
            "bloom_level": None,
            "bloom_description": None,
            "visit_count": None,
            "logged_count": None,
            "voted": None,
            "superscript": None,
            "subscript": None,
        }

    return {
        "envelope_version": ENVELOPE_VERSION,
        "stamped_at": datetime.now(timezone.utc).isoformat(),
        "zip": zip_block,
        "weight_vector": weight_block,
        "user_context": user_block,
    }


# ---------------------------------------------------------------------------
# Deck helpers
# ---------------------------------------------------------------------------

def _get_deck_zips(deck_number: int) -> list:
    """Return all numeric zips for a given deck number (40 per deck)."""
    registry = _load_registry()
    return [
        nz for nz, entry in registry.items()
        if entry["deck_number"] == deck_number
    ]


def _parse_deck_arg(deck_arg: str) -> int:
    """Convert '07' or '7' to integer deck number."""
    return int(deck_arg.strip())


# ---------------------------------------------------------------------------
# CLI modes
# ---------------------------------------------------------------------------

def _print_json(obj: dict, compact: bool = False):
    if compact:
        print(json.dumps(obj, ensure_ascii=False))
    else:
        print(json.dumps(obj, ensure_ascii=False, indent=2))


def run_single(zip_arg: str, mode: str):
    """Stamp a single envelope in anonymous or full mode."""
    user_ctx = None
    if mode == "full":
        numeric_zip = _resolve_numeric_zip(zip_arg)
        user_ctx = _mock_user_context(numeric_zip)

    envelope = stamp_envelope(zip_arg, user_ctx)
    _print_json(envelope)


def run_deck(deck_arg: str, mode: str):
    """Stamp all 40 envelopes for a deck."""
    deck_number = _parse_deck_arg(deck_arg)
    zips = _get_deck_zips(deck_number)

    if not zips:
        print(f"No zips found for deck {deck_number}", file=sys.stderr)
        sys.exit(1)

    # Sort for deterministic output
    zips_sorted = sorted(zips)

    envelopes = []
    for nz in zips_sorted:
        user_ctx = None
        if mode == "full":
            user_ctx = _mock_user_context(nz, seed=int(nz))
        env = stamp_envelope(nz, user_ctx)
        envelopes.append(env)

    output = {
        "deck_number": deck_number,
        "envelope_count": len(envelopes),
        "mode": mode,
        "envelopes": envelopes,
    }
    _print_json(output)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=(
            "CX-30: Envelope Stamper — atomic retrieval unit for the PPL± system.\n"
            "Stamps envelopes combining zip identity, weight vector, and optional user context."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    target = parser.add_mutually_exclusive_group(required=True)
    target.add_argument(
        "--zip",
        metavar="ZIP",
        help="Single zip code (4-digit numeric or emoji)",
    )
    target.add_argument(
        "--deck",
        metavar="DECK",
        help="Deck number (e.g. 07 or 7) — stamps all 40 envelopes in the deck",
    )

    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        "--anonymous",
        action="store_true",
        help="Stamp without user context — base identity + weight vector only (free-tier envelope)",
    )
    mode_group.add_argument(
        "--full",
        action="store_true",
        help="Stamp with mock user context — demonstrates complete envelope shape (paid-tier envelope)",
    )

    args = parser.parse_args()

    # Default to anonymous if neither flag given
    mode = "full" if args.full else "anonymous"

    if args.zip:
        run_single(args.zip, mode)
    else:
        run_deck(args.deck, mode)


if __name__ == "__main__":
    main()
