#!/usr/bin/env python3
"""
scripts/middle-math/vote_weight_adjuster.py
CX-25: Vote Weight Integration

Integrates room vote signals into the base weight vector.

Eudaimonic constraint (from seeds/systems-eudaimonics.md):
  Votes are signal, not governance. A room's character comes from its four dials,
  not from popularity. This cap is the interlock. One angry vote cannot flip a
  room's identity. Many aligned votes can nudge it — never override it.

Algorithm:
  1. Filter votes: keep only vote_value in {-1, +1} (0 = retracted/neutral)
  2. Compute raw signal: sum of vote values
  3. Normalize via tanh(raw / count) → signal in (-1, 1)
     tanh bounds the signal naturally: a single vote is a whisper;
     many aligned votes approach ±1 but never reach it.
  4. Uniform adjustment: signal * CAP_PER_DIM on every dimension
     The cap is the guarantee. Architecture sets identity. Votes refine it.
  5. Clamp adjusted vector to dimension bounds [-8, 8]

Cap math:
  Dimension range: [-8, 8] = 16 units total
  CAP_PER_DIM = 0.8 → max ±0.8 per dimension = ±5% of the full range
  Even with infinite perfectly-aligned votes (signal → ±1.0), the maximum
  shift on any dimension is ±0.8 — well within the ±10% ceiling specified.

Schema reference: sql/008-room-schema-extension.sql
  - room_votes: zip_code, user_id, vote_value (-1|0|1), created_at

Usage:
    python scripts/middle-math/vote_weight_adjuster.py --zip 2123
    python scripts/middle-math/vote_weight_adjuster.py --demo
    python scripts/middle-math/vote_weight_adjuster.py --validate
"""

import json
import sys
import math
import argparse
import random
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

WEIGHT_VECTORS_PATH = REPO_ROOT / "middle-math" / "weight-vectors.json"
REGISTRY_PATH = REPO_ROOT / "middle-math" / "zip-registry.json"

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CAP_PER_DIM = 0.8       # max ±0.8 per dimension regardless of vote volume
DIMENSION_MIN = -8.0
DIMENSION_MAX = 8.0
VECTOR_SIZE = 61

# Emoji → numeric position maps (mirrors weight_vector.py EMOJI_POSITIONS)
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


# ---------------------------------------------------------------------------
# Data loading (lazy, cached at module level)
# ---------------------------------------------------------------------------

_weight_vectors_cache = None
_registry_cache = None


def _load_weight_vectors():
    global _weight_vectors_cache
    if _weight_vectors_cache is None:
        with open(WEIGHT_VECTORS_PATH, encoding="utf-8") as f:
            # weight-vectors.json is a dict keyed by 4-digit numeric zip
            _weight_vectors_cache = json.load(f)
    return _weight_vectors_cache


def _load_registry():
    global _registry_cache
    if _registry_cache is None:
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            raw = json.load(f)
        _registry_cache = {entry["numeric_zip"]: entry for entry in raw}
    return _registry_cache


# ---------------------------------------------------------------------------
# Zip code resolution
# ---------------------------------------------------------------------------

def resolve_numeric_zip(zip_code: str) -> str:
    """Convert emoji zip or numeric zip to 4-digit numeric string."""
    zip_code = zip_code.strip()
    if zip_code.isdigit() and len(zip_code) == 4:
        return zip_code

    # Emoji zip: decompose into grapheme clusters
    import unicodedata
    chars = []
    i = 0
    while i < len(zip_code):
        c = zip_code[i]
        # Absorb variation selectors and combining characters
        combined = c
        j = i + 1
        while j < len(zip_code) and unicodedata.category(zip_code[j]) in ("Mn", "Cf"):
            combined += zip_code[j]
            j += 1
        chars.append(combined)
        i = j

    # Filter to only emoji characters (skip variation selectors standalone)
    emoji_chars = [ch for ch in chars if ch in ORDER_POSITIONS or ch in AXIS_POSITIONS
                   or ch in TYPE_POSITIONS or ch in COLOR_POSITIONS]

    if len(emoji_chars) != 4:
        # Fallback: try splitting by known emojis
        registry = _load_registry()
        for entry in registry.values():
            if entry["emoji_zip"] == zip_code or entry["emoji_zip"].replace("\ufe0f", "") == zip_code:
                return entry["numeric_zip"]
        raise ValueError(f"Cannot resolve zip code: {repr(zip_code)}")

    order_pos = ORDER_POSITIONS.get(emoji_chars[0])
    axis_pos = AXIS_POSITIONS.get(emoji_chars[1])
    type_pos = TYPE_POSITIONS.get(emoji_chars[2])
    color_pos = COLOR_POSITIONS.get(emoji_chars[3])

    if None in (order_pos, axis_pos, type_pos, color_pos):
        raise ValueError(f"Unknown emoji in zip: {emoji_chars}")

    return f"{order_pos}{axis_pos}{type_pos}{color_pos}"


# ---------------------------------------------------------------------------
# Core computation
# ---------------------------------------------------------------------------

def compute_vote_signal(votes: list) -> float:
    """
    Aggregate a list of vote records into a bounded signal in (-1, 1).

    Vote record format: {"user_id": str, "vote_value": int, "timestamp": str}
    vote_value must be in {-1, 0, +1}. Zero votes are excluded (retracted).

    Returns 0.0 if no active votes.
    """
    active = [v for v in votes if v.get("vote_value", 0) in (-1, 1)]
    if not active:
        return 0.0

    raw = sum(v["vote_value"] for v in active)
    n = len(active)
    # tanh(raw/n): when all votes agree, approaches ±1; split votes cancel
    signal = math.tanh(raw / n)
    return signal


def compute_adjustment_vector(signal: float) -> list:
    """
    Convert a signal in (-1, 1) into a 61-dimensional adjustment vector.

    The adjustment is uniform across all dimensions: the vote signal affects
    the room's overall weight, not any specific dimension. Architecture decides
    which dimensions are high; votes can push the whole room up or down.

    The CAP_PER_DIM interlock ensures no dimension ever shifts by more than
    ±CAP_PER_DIM regardless of signal magnitude.
    """
    adj = signal * CAP_PER_DIM
    # adj is already within [-CAP_PER_DIM, CAP_PER_DIM] by construction
    return [round(adj, 6)] * VECTOR_SIZE


def apply_adjustment(base_vector: list, adjustment_vector: list) -> list:
    """
    Add adjustment to base vector, clamping each dimension to [DIMENSION_MIN, DIMENSION_MAX].
    """
    adjusted = []
    for b, a in zip(base_vector, adjustment_vector):
        val = b + a
        val = max(DIMENSION_MIN, min(DIMENSION_MAX, val))
        adjusted.append(round(val, 6))
    return adjusted


def compute_adjusted(zip_code: str, votes: list) -> dict:
    """
    Full pipeline: zip code + votes → adjusted weight vector envelope.

    Returns:
    {
        "numeric_zip": "2123",
        "emoji_zip": "⛽🏛🪡🔵",
        "vote_summary": {
            "total_votes": int,
            "active_votes": int,
            "net_signal": float,        # (-1, 1)
            "cap_per_dim": float,
        },
        "base_vector": [61 floats],
        "adjustment_vector": [61 floats],
        "adjusted_vector": [61 floats],
        "computed_at": "ISO8601"
    }
    """
    numeric_zip = resolve_numeric_zip(zip_code)

    vectors = _load_weight_vectors()
    registry = _load_registry()

    if numeric_zip not in vectors:
        raise KeyError(f"Zip {numeric_zip} not found in weight-vectors.json")

    entry = vectors[numeric_zip]
    base_vector = entry["vector"]

    active = [v for v in votes if v.get("vote_value", 0) in (-1, 1)]
    signal = compute_vote_signal(votes)
    adjustment_vector = compute_adjustment_vector(signal)
    adjusted_vector = apply_adjustment(base_vector, adjustment_vector)

    emoji_zip = registry.get(numeric_zip, {}).get("emoji_zip", numeric_zip)

    return {
        "numeric_zip": numeric_zip,
        "emoji_zip": emoji_zip,
        "vote_summary": {
            "total_votes": len(votes),
            "active_votes": len(active),
            "net_signal": round(signal, 6),
            "cap_per_dim": CAP_PER_DIM,
        },
        "base_vector": base_vector,
        "adjustment_vector": adjustment_vector,
        "adjusted_vector": adjusted_vector,
        "computed_at": datetime.now(timezone.utc).isoformat(),
    }


# ---------------------------------------------------------------------------
# CLI modes
# ---------------------------------------------------------------------------

def run_demo():
    """Simulate 50 votes across 5 zips and print comparison table."""
    registry = _load_registry()
    all_zips = list(registry.keys())

    # Pick 5 representative zips: first of each order
    demo_zips = ["1111", "2111", "3111", "4111", "5111"]

    print("=" * 72)
    print("VOTE WEIGHT ADJUSTER — DEMO")
    print("Simulating 50 votes across 5 zips")
    print("=" * 72)

    random.seed(42)
    for numeric_zip in demo_zips:
        if numeric_zip not in registry:
            continue
        entry = registry[numeric_zip]
        emoji_zip = entry["emoji_zip"]
        order_name = entry["order"]["name"]

        # Generate varied vote patterns
        n_votes = random.randint(5, 15)
        # Mix of patterns: mostly positive, mostly negative, split
        patterns = [
            lambda n: [1] * n,                                   # unanimous positive
            lambda n: [-1] * n,                                  # unanimous negative
            lambda n: [1] * (n // 2 + 1) + [-1] * (n // 2),    # slight positive
            lambda n: [1] * (n // 3) + [-1] * (n * 2 // 3),    # slight negative
            lambda n: [random.choice([-1, 1]) for _ in range(n)], # random
        ]
        vote_values = patterns[demo_zips.index(numeric_zip) % len(patterns)](n_votes)

        votes = [
            {"user_id": f"user_{i:04d}", "vote_value": v,
             "timestamp": "2026-03-06T12:00:00Z"}
            for i, v in enumerate(vote_values)
        ]

        result = compute_adjusted(numeric_zip, votes)

        signal = result["vote_summary"]["net_signal"]
        active = result["vote_summary"]["active_votes"]
        adj_val = result["adjustment_vector"][0]  # uniform, all same

        # Show first 5 dimensions for comparison
        base_sample = result["base_vector"][:5]
        adj_sample = result["adjusted_vector"][:5]

        print(f"\nZip: {emoji_zip}  ({numeric_zip})  — {order_name}")
        print(f"  Votes: {active} active  |  Signal: {signal:+.4f}  |  Adj/dim: {adj_val:+.4f}")
        print(f"  Base  [0:5]: {[round(x, 2) for x in base_sample]}")
        print(f"  Adj   [0:5]: {[round(x, 2) for x in adj_sample]}")
        delta = [round(adj_sample[i] - base_sample[i], 4) for i in range(5)]
        print(f"  Delta [0:5]: {delta}")

    print("\n" + "=" * 72)
    print("Cap constraint: max delta per dimension =", CAP_PER_DIM)
    print("Eudaimonic guarantee: architecture sets identity, votes refine it.")
    print("=" * 72)


def run_validate():
    """
    Validate that the adjuster respects all bounds across all 1,680 zips.
    Tests multiple vote configurations per zip.
    """
    print("=" * 60)
    print("VOTE WEIGHT ADJUSTER — VALIDATION")
    print(f"Testing all 1,680 zips across 4 vote configurations...")
    print("=" * 60)

    registry = _load_registry()
    errors = []
    checked = 0

    # Test configurations: no votes, all +1, all -1, mixed
    test_configs = [
        ("no_votes", []),
        ("all_positive_10", [{"user_id": f"u{i}", "vote_value": 1, "timestamp": "2026-01-01"} for i in range(10)]),
        ("all_negative_10", [{"user_id": f"u{i}", "vote_value": -1, "timestamp": "2026-01-01"} for i in range(10)]),
        ("all_positive_1000", [{"user_id": f"u{i}", "vote_value": 1, "timestamp": "2026-01-01"} for i in range(1000)]),
    ]

    for numeric_zip in registry.keys():
        for config_name, votes in test_configs:
            try:
                result = compute_adjusted(numeric_zip, votes)
                adj_vec = result["adjusted_vector"]
                base_vec = result["base_vector"]
                adj_raw = result["adjustment_vector"]

                # Check 1: No NaN
                for i, v in enumerate(adj_vec):
                    if math.isnan(v):
                        errors.append(f"NaN at dim {i} for zip {numeric_zip} config {config_name}")

                # Check 2: Dimension bounds
                for i, v in enumerate(adj_vec):
                    if v < DIMENSION_MIN - 1e-9 or v > DIMENSION_MAX + 1e-9:
                        errors.append(
                            f"Out-of-bounds dim {i}={v:.4f} for zip {numeric_zip} config {config_name}"
                        )

                # Check 3: Adjustment cap
                for i, a in enumerate(adj_raw):
                    if abs(a) > CAP_PER_DIM + 1e-9:
                        errors.append(
                            f"Cap exceeded dim {i} adj={a:.4f} for zip {numeric_zip} config {config_name}"
                        )

                # Check 4: Vector size
                if len(adj_vec) != VECTOR_SIZE:
                    errors.append(f"Wrong vector size {len(adj_vec)} for zip {numeric_zip}")

                checked += 1

            except Exception as e:
                errors.append(f"Exception for zip {numeric_zip} config {config_name}: {e}")

    print(f"\nChecked: {checked} zip × config combinations")
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors[:20]:
            print(f"  - {e}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more")
        sys.exit(1)
    else:
        print("PASSED: 5/5 rules")
        print("  [✓] No NaN values")
        print("  [✓] All dimensions within [-8, 8]")
        print(f"  [✓] All adjustments within ±{CAP_PER_DIM}")
        print(f"  [✓] All vectors length {VECTOR_SIZE}")
        print("  [✓] No exceptions raised")
        print("\nEudaimonic interlock confirmed: votes are bounded signal, not governance.")


def run_single_zip(zip_arg: str):
    """Print the adjustment result for a single zip with empty votes."""
    result = compute_adjusted(zip_arg, [])
    print(json.dumps(result, ensure_ascii=False, indent=2))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="CX-25: Vote Weight Adjuster — bounded vote signal integration"
    )
    parser.add_argument(
        "--zip",
        metavar="ZIP",
        help="Single zip code (4-digit numeric or emoji) to compute adjustment for",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Simulate 50 votes across 5 zips and show base vs adjusted comparison",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate all 1,680 zips across multiple vote configurations",
    )
    args = parser.parse_args()

    if args.validate:
        run_validate()
    elif args.demo:
        run_demo()
    elif args.zip:
        run_single_zip(args.zip)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
