#!/usr/bin/env python3
"""
scripts/middle-math/envelope_retrieval.py
CX-31: Envelope Similarity & Retrieval Engine

The capstone of the CX architecture. Every room lookup, Operis sandbox
selection, exercise recommendation, and content retrieval in the PPL± system
resolves through this function.

Architecture reference: seeds/scl-envelope-architecture.md
  "Condition-based matching, not calendar-based. The system finds content
  whose envelope is most similar to the live weight vector state."

Core mechanics:
  - Cosine similarity in 61-dimensional weight space
  - Content-type-specific retrieval profiles (Tier 1–4 dimension weighting)
  - Query vector composition: base + vote adjustment + bloom modifier
  - Four CLI modes: --query, --deck, --operis, --validate, --stats

Dimension layout (61 dims, indices 0–60):
  [0–6]   Order weights   (7 dims)
  [7–12]  Axis weights    (6 dims)
  [13–17] Type weights    (5 dims)
  [18–25] Color weights   (8 dims)
  [26–60] Derived weights (35 dims: blocks, operators, interaction rules)

Retrieval tiers:
  Tier 1 — Order-level, seasonal content  → Order dims ×2, seasonal ×2
  Tier 2 — Deck/Type-level content        → Type dims ×1.5, Axis dims ×1.5
  Tier 3 — Exercise cluster               → Derived (block/operator) dims ×2
  Tier 4 — Exercise-specific              → All dims ×1.0, threshold ≥ 0.9

Usage:
    python scripts/middle-math/envelope_retrieval.py --query 2123
    python scripts/middle-math/envelope_retrieval.py --query ⛽🏛🪡🔵
    python scripts/middle-math/envelope_retrieval.py --deck 07
    python scripts/middle-math/envelope_retrieval.py --operis 2026-03-06
    python scripts/middle-math/envelope_retrieval.py --validate
    python scripts/middle-math/envelope_retrieval.py --stats
"""

import json
import sys
import math
import argparse
import random
import unicodedata
from pathlib import Path
from datetime import date, datetime, timezone

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

WEIGHT_VECTORS_PATH       = REPO_ROOT / "middle-math" / "weight-vectors.json"
REGISTRY_PATH             = REPO_ROOT / "middle-math" / "zip-registry.json"
CONTENT_TYPE_REGISTRY_PATH = REPO_ROOT / "middle-math" / "content-type-registry.json"

# ---------------------------------------------------------------------------
# Dimension layout constants
# ---------------------------------------------------------------------------

VECTOR_SIZE = 61
DIM_MIN     = -8.0
DIM_MAX     = 8.0

DIM_ORDER   = list(range(0, 7))    # 7 dims: Order weights
DIM_AXIS    = list(range(7, 13))   # 6 dims: Axis weights
DIM_TYPE    = list(range(13, 18))  # 5 dims: Type weights
DIM_COLOR   = list(range(18, 26))  # 8 dims: Color weights
DIM_DERIVED = list(range(26, 61))  # 35 dims: Blocks, operators, interaction rules

# Within derived dims, indices 26–35 approximate block-level seasonal/temporal
# context (time-of-session, seasonal markers, rest period ratios).
# These are amplified in Tier 1 seasonal retrieval.
DIM_SEASONAL = list(range(26, 36))  # 10 dims within derived cluster

# Dims 36–50 approximate exercise family and operator affinity clusters.
# Amplified in Tier 3 (exercise cluster) retrieval.
DIM_EXERCISE_FAMILY = list(range(36, 51))  # 15 dims

# ---------------------------------------------------------------------------
# Emoji → numeric position maps (mirrors vote_weight_adjuster.py)
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

ORDER_NAMES = {
    "🐂": "Foundation", "⛽": "Strength", "🦋": "Hypertrophy",
    "🏟": "Performance", "🌾": "Full Body", "⚖": "Balance", "🖼": "Restoration",
}
AXIS_NAMES = {
    "🏛": "Basics", "🔨": "Functional", "🌹": "Aesthetic",
    "🪐": "Challenge", "⌛": "Time", "🐬": "Partner",
}
TYPE_NAMES = {
    "🛒": "Push", "🪡": "Pull", "🍗": "Legs", "➕": "Plus", "➖": "Ultra",
}
COLOR_NAMES = {
    "⚫": "Teaching", "🟢": "Bodyweight", "🔵": "Structured",
    "🟣": "Technical", "🔴": "Intense", "🟠": "Circuit", "🟡": "Fun", "⚪": "Mindful",
}

# ---------------------------------------------------------------------------
# Rotation engine constants (mirrors generate_room_manifest.py)
# ---------------------------------------------------------------------------

WEEKDAY_TO_ORDER = {
    0: "🐂", 1: "⛽", 2: "🦋", 3: "🏟", 4: "🌾", 5: "⚖", 6: "🖼",
}
TYPE_CYCLE = ["🛒", "🪡", "🍗", "➕", "➖"]
MONTH_TO_AXIS = {
    1: "🏛", 2: "🔨", 3: "🌹", 4: "🪐", 5: "⌛", 6: "🐬",
    7: "🏛", 8: "🔨", 9: "🌹", 10: "🪐", 11: "⌛", 12: "🐬",
}
COLORS_ALL = ["⚫", "🟢", "🔵", "🟣", "🔴", "🟠", "🟡", "⚪"]

# ---------------------------------------------------------------------------
# Data loading (lazy, module-level cache)
# ---------------------------------------------------------------------------

_weight_vectors_cache = None
_registry_cache       = None
_content_types_cache  = None


def _load_weight_vectors() -> dict:
    global _weight_vectors_cache
    if _weight_vectors_cache is None:
        with open(WEIGHT_VECTORS_PATH, encoding="utf-8") as f:
            _weight_vectors_cache = json.load(f)
    return _weight_vectors_cache


def _load_registry() -> dict:
    global _registry_cache
    if _registry_cache is None:
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            raw = json.load(f)
        _registry_cache = {entry["numeric_zip"]: entry for entry in raw}
    return _registry_cache


def _load_content_types() -> list:
    global _content_types_cache
    if _content_types_cache is None:
        with open(CONTENT_TYPE_REGISTRY_PATH, encoding="utf-8") as f:
            _content_types_cache = json.load(f)
    return _content_types_cache


# ---------------------------------------------------------------------------
# Zip code resolution
# ---------------------------------------------------------------------------

def resolve_numeric_zip(zip_code: str) -> str:
    """Convert emoji zip or 4-digit numeric string to 4-digit numeric string."""
    zip_code = zip_code.strip()
    if zip_code.isdigit() and len(zip_code) == 4:
        return zip_code

    # Decompose emoji zip into grapheme clusters
    chars = []
    i = 0
    while i < len(zip_code):
        c = zip_code[i]
        combined = c
        j = i + 1
        while j < len(zip_code) and unicodedata.category(zip_code[j]) in ("Mn", "Cf"):
            combined += zip_code[j]
            j += 1
        chars.append(combined)
        i = j

    emoji_chars = [
        ch for ch in chars
        if ch in ORDER_POSITIONS or ch in AXIS_POSITIONS
        or ch in TYPE_POSITIONS or ch in COLOR_POSITIONS
    ]
    if len(emoji_chars) != 4:
        raise ValueError(
            f"Cannot resolve zip code '{zip_code}': "
            f"expected 4 SCL emoji, got {len(emoji_chars)}: {emoji_chars}"
        )

    order_e, axis_e, type_e, color_e = emoji_chars
    return (
        f"{ORDER_POSITIONS[order_e]}"
        f"{AXIS_POSITIONS[axis_e]}"
        f"{TYPE_POSITIONS[type_e]}"
        f"{COLOR_POSITIONS[color_e]}"
    )


def make_numeric_zip_from_emojis(order_e, axis_e, type_e, color_e) -> str:
    return (
        f"{ORDER_POSITIONS[order_e]}"
        f"{AXIS_POSITIONS[axis_e]}"
        f"{TYPE_POSITIONS[type_e]}"
        f"{COLOR_POSITIONS[color_e]}"
    )


def _get_deck_zips(deck_number: int) -> list:
    """Return all numeric zips for a given deck (40 per deck)."""
    order_pos = (deck_number - 1) // 6 + 1   # 1–7
    axis_pos  = (deck_number - 1) % 6  + 1   # 1–6
    zips = []
    for type_pos in range(1, 6):
        for color_pos in range(1, 9):
            zips.append(f"{order_pos}{axis_pos}{type_pos}{color_pos}")
    return zips


# ---------------------------------------------------------------------------
# Retrieval tier weight profiles
# ---------------------------------------------------------------------------

def _make_weight_array(tier: str) -> list:
    """
    Return a 61-element weight array for the given retrieval tier.

    Tier 1 — Order-level, seasonal: amplify Order dims and seasonal derived dims.
    Tier 2 — Deck/Type-level: amplify Type and Axis dims.
    Tier 3 — Exercise cluster: amplify exercise-family and block/operator derived dims.
    Tier 4 — Exercise-specific: all dims equal, threshold ≥ 0.9 enforced by caller.
    """
    weights = [1.0] * VECTOR_SIZE

    if tier == "tier1":
        for i in DIM_ORDER:
            weights[i] = 2.0
        for i in DIM_SEASONAL:
            weights[i] = 2.0

    elif tier == "tier2":
        for i in DIM_AXIS:
            weights[i] = 1.5
        for i in DIM_TYPE:
            weights[i] = 1.5

    elif tier == "tier3":
        for i in DIM_EXERCISE_FAMILY:
            weights[i] = 2.0
        # Also give moderate boost to block/operator dims outside exercise family
        for i in DIM_DERIVED:
            if weights[i] == 1.0:
                weights[i] = 1.3

    # tier4: all 1.0 (default, already set)

    return weights


# ---------------------------------------------------------------------------
# Core similarity function
# ---------------------------------------------------------------------------

def compute_similarity(
    vector_a: list,
    vector_b: list,
    weights: list = None,
) -> float:
    """
    Compute weighted cosine similarity between two 61-dimensional vectors.

    Returns a float in [-1.0, 1.0].
    Returns 0.0 if either vector is the zero vector (undefined cosine).

    Args:
        vector_a: 61-float weight vector.
        vector_b: 61-float weight vector.
        weights:  Optional 61-float dimension weight array. If None, uniform weights.

    Returns:
        Cosine similarity in [-1.0, 1.0].
    """
    if len(vector_a) != VECTOR_SIZE or len(vector_b) != VECTOR_SIZE:
        raise ValueError(
            f"Vector length mismatch: got {len(vector_a)}, {len(vector_b)}, "
            f"expected {VECTOR_SIZE}"
        )

    if weights is None:
        weights = [1.0] * VECTOR_SIZE

    # Apply dimension weights: scale each component
    wa = [weights[i] * vector_a[i] for i in range(VECTOR_SIZE)]
    wb = [weights[i] * vector_b[i] for i in range(VECTOR_SIZE)]

    dot  = sum(wa[i] * wb[i]         for i in range(VECTOR_SIZE))
    mag_a = math.sqrt(sum(x * x       for x in wa))
    mag_b = math.sqrt(sum(x * x       for x in wb))

    if mag_a == 0.0 or mag_b == 0.0:
        return 0.0

    raw = dot / (mag_a * mag_b)

    # Clamp to [-1.0, 1.0] to guard against floating-point drift
    return max(-1.0, min(1.0, raw))


# ---------------------------------------------------------------------------
# Query vector construction
# ---------------------------------------------------------------------------

def build_query_vector(zip_code: str, user_context: dict = None) -> list:
    """
    Construct the live query vector for a zip code.

    Composition:
      1. Base weight vector (from weight-vectors.json)
      2. Vote adjustment (if user_context.votes present)
      3. Bloom modifier — bloom level adds a small uniform nudge to the
         primary dial dims, reflecting depth of engagement

    Args:
        zip_code:     4-digit numeric or emoji zip code.
        user_context: Optional dict with keys: votes (list), visit_count (int),
                      logged_count (int), voted (bool).

    Returns:
        61-float list representing the live query vector.
    """
    numeric_zip = resolve_numeric_zip(zip_code)
    vectors = _load_weight_vectors()

    if numeric_zip not in vectors:
        raise KeyError(f"Zip '{numeric_zip}' not found in weight-vectors.json")

    base_vector = list(vectors[numeric_zip]["vector"])

    if user_context is None:
        return base_vector

    # ------------------------------------------------------------------
    # Vote adjustment
    # ------------------------------------------------------------------
    votes = user_context.get("votes", [])
    if votes:
        # Inline vote adjustment (mirrors vote_weight_adjuster logic)
        active_votes = [v for v in votes if v.get("vote_value") in (-1, 1)]
        if active_votes:
            raw_sum    = sum(v["vote_value"] for v in active_votes)
            signal     = math.tanh(raw_sum / len(active_votes))
            cap_per_dim = 0.8
            adjustment = [signal * cap_per_dim] * VECTOR_SIZE
            base_vector = [
                max(DIM_MIN, min(DIM_MAX, base_vector[i] + adjustment[i]))
                for i in range(VECTOR_SIZE)
            ]

    # ------------------------------------------------------------------
    # Bloom modifier — depth of engagement nudge
    # ------------------------------------------------------------------
    visit_count  = user_context.get("visit_count", 0)
    logged_count = user_context.get("logged_count", 0)
    voted        = user_context.get("voted", False)

    bloom = 0
    if voted and logged_count >= 5:
        bloom = 5
    elif logged_count >= 3:
        bloom = 4
    elif logged_count >= 1:
        bloom = 3
    elif visit_count >= 3:
        bloom = 2
    elif visit_count >= 1:
        bloom = 1

    if bloom > 0:
        # Bloom nudge: +0.05 × bloom_level on primary Order/Axis/Type/Color dims
        bloom_nudge = bloom * 0.05
        primary_dims = DIM_ORDER + DIM_AXIS + DIM_TYPE + DIM_COLOR
        for i in primary_dims:
            base_vector[i] = max(DIM_MIN, min(DIM_MAX, base_vector[i] + bloom_nudge))

    return base_vector


# ---------------------------------------------------------------------------
# Top-N retrieval
# ---------------------------------------------------------------------------

def retrieve_top_n(
    query_vector: list,
    candidate_envelopes: list = None,
    n: int = 10,
    tier: str = "tier2",
    threshold: float = None,
) -> list:
    """
    Retrieve the top-n most similar envelopes to the query vector.

    If candidate_envelopes is None, all 1,680 base vectors are used as candidates.

    Args:
        query_vector:        61-float query vector.
        candidate_envelopes: Optional list of envelope dicts (must have
                             "numeric_zip", "emoji_zip", "vector" keys).
                             If None, loads all 1,680 from weight-vectors.json.
        n:                   Number of results to return.
        tier:                Retrieval profile tier ("tier1"–"tier4").
        threshold:           Optional minimum similarity score. Tier 4 defaults to 0.9.

    Returns:
        List of dicts sorted descending by similarity score:
        [{"numeric_zip", "emoji_zip", "score", "rank", "tier"}, ...]
    """
    if tier == "tier4" and threshold is None:
        threshold = 0.9

    weights = _make_weight_array(tier)

    if candidate_envelopes is None:
        vectors = _load_weight_vectors()
        candidates = [
            {"numeric_zip": nzip, "emoji_zip": entry["emoji_zip"], "vector": entry["vector"]}
            for nzip, entry in vectors.items()
        ]
    else:
        candidates = candidate_envelopes

    results = []
    for candidate in candidates:
        vec = candidate.get("vector")
        if vec is None:
            continue
        score = compute_similarity(query_vector, vec, weights)
        if threshold is not None and score < threshold:
            continue
        results.append({
            "numeric_zip": candidate["numeric_zip"],
            "emoji_zip":   candidate["emoji_zip"],
            "score":       score,
            "tier":        tier,
        })

    results.sort(key=lambda r: r["score"], reverse=True)

    for rank, result in enumerate(results[:n], start=1):
        result["rank"] = rank

    return results[:n]


# ---------------------------------------------------------------------------
# Operis retrieval
# ---------------------------------------------------------------------------

def retrieve_for_operis(date_str: str, n: int = 13) -> dict:
    """
    Retrieve the n most relevant envelopes for an Operis edition date.

    Uses the rotation engine to derive the day's Order/Axis/Type dials,
    then uses 🔵 Structured as the canonical Color for the base query.
    Retrieves with Tier 1 profile (Order/seasonal emphasis) to surface
    content that resonates with the day's training character.

    Args:
        date_str: ISO date string, e.g. "2026-03-06".
        n:        Number of envelopes to retrieve (Operis uses 13).

    Returns:
        Dict with date info, derived dials, query zip, and top-n envelopes.
    """
    d = date.fromisoformat(date_str)

    # Rotation engine
    order_e = WEEKDAY_TO_ORDER[d.weekday()]
    jan1    = date(d.year, 1, 1)
    type_e  = TYPE_CYCLE[(d - jan1).days % 5]
    axis_e  = MONTH_TO_AXIS[d.month]
    color_e = "🔵"  # Structured — canonical Operis query color

    query_zip    = make_numeric_zip_from_emojis(order_e, axis_e, type_e, color_e)
    query_vector = build_query_vector(query_zip)

    envelopes = retrieve_top_n(query_vector, n=n, tier="tier1")

    return {
        "date":        date_str,
        "weekday":     d.strftime("%A"),
        "dials": {
            "order": {"emoji": order_e, "name": ORDER_NAMES.get(order_e, "")},
            "axis":  {"emoji": axis_e,  "name": AXIS_NAMES.get(axis_e, "")},
            "type":  {"emoji": type_e,  "name": TYPE_NAMES.get(type_e, "")},
            "color": {"emoji": color_e, "name": COLOR_NAMES.get(color_e, "")},
        },
        "query_zip": {
            "numeric": query_zip,
            "emoji":   f"{order_e}{axis_e}{type_e}{color_e}",
        },
        "top_n":      n,
        "envelopes":  envelopes,
    }


# ---------------------------------------------------------------------------
# CLI: --query
# ---------------------------------------------------------------------------

def run_query(zip_arg: str, n: int = 10, tier: str = "tier2") -> None:
    numeric_zip = resolve_numeric_zip(zip_arg)
    vectors     = _load_weight_vectors()

    if numeric_zip not in vectors:
        print(f"ERROR: zip '{numeric_zip}' not found in weight-vectors.json", file=sys.stderr)
        sys.exit(1)

    entry   = vectors[numeric_zip]
    emoji   = entry["emoji_zip"]
    query_v = build_query_vector(numeric_zip)

    print(f"\nEnvelope Retrieval — Query: {emoji} ({numeric_zip})  Tier: {tier}  Top: {n}")
    print("=" * 72)
    print(f"{'Rank':<5} {'Zip':<6} {'Emoji':<10} {'Score':>7}  Label")
    print("-" * 72)

    results = retrieve_top_n(query_v, n=n, tier=tier)
    registry = _load_registry()

    for r in results:
        nzip = r["numeric_zip"]
        reg  = registry.get(nzip, {})
        label = reg.get("emoji_zip", r["emoji_zip"])
        print(f"  {r['rank']:<4} {nzip:<6} {r['emoji_zip']:<10} {r['score']:>7.4f}  {label}")

    print()


# ---------------------------------------------------------------------------
# CLI: --deck
# ---------------------------------------------------------------------------

def run_deck(deck_arg: str, n: int = 5, tier: str = "tier2") -> None:
    try:
        deck_number = int(deck_arg)
    except ValueError:
        print(f"ERROR: deck argument must be a number, got '{deck_arg}'", file=sys.stderr)
        sys.exit(1)

    zips = _get_deck_zips(deck_number)
    vectors  = _load_weight_vectors()
    registry = _load_registry()

    print(f"\nDeck {deck_number:02d} — Top {n} similar envelopes per zip  (Tier: {tier})")
    print("=" * 80)

    for nzip in zips:
        if nzip not in vectors:
            print(f"  {nzip}: not found in weight-vectors.json — skipping")
            continue

        entry   = vectors[nzip]
        emoji   = entry["emoji_zip"]
        query_v = build_query_vector(nzip)
        results = retrieve_top_n(query_v, n=n + 1, tier=tier)  # +1 to skip self

        # Skip the query zip itself (rank 1, score ~1.0)
        results = [r for r in results if r["numeric_zip"] != nzip][:n]

        print(f"\n  {emoji} ({nzip}):")
        for r in results:
            print(f"    {r['rank']:>2}. {r['emoji_zip']} ({r['numeric_zip']})  {r['score']:.4f}")

    print()


# ---------------------------------------------------------------------------
# CLI: --operis
# ---------------------------------------------------------------------------

def run_operis(date_arg: str, n: int = 13) -> None:
    try:
        result = retrieve_for_operis(date_arg, n=n)
    except ValueError as e:
        print(f"ERROR: invalid date '{date_arg}': {e}", file=sys.stderr)
        sys.exit(1)

    dials = result["dials"]
    qzip  = result["query_zip"]

    print(f"\nOperis Retrieval — {result['date']} ({result['weekday']})")
    print("=" * 72)
    print(f"  Rotation:  {dials['order']['emoji']} {dials['order']['name']}"
          f"  /  {dials['axis']['emoji']} {dials['axis']['name']}"
          f"  /  {dials['type']['emoji']} {dials['type']['name']}")
    print(f"  Query zip: {qzip['emoji']} ({qzip['numeric']})  [🔵 Structured — canonical Operis query]")
    print(f"  Profile:   Tier 1 (Order + seasonal emphasis)")
    print(f"\n  Top {result['top_n']} envelopes for Operis Sandbox:\n")
    print(f"  {'Rank':<5} {'Zip':<6} {'Emoji':<12} {'Score':>7}")
    print(f"  {'-'*40}")

    for r in result["envelopes"]:
        print(f"  {r['rank']:<5} {r['numeric_zip']:<6} {r['emoji_zip']:<12} {r['score']:>7.4f}")

    print()


# ---------------------------------------------------------------------------
# CLI: --validate
# ---------------------------------------------------------------------------

def run_validate() -> None:
    """
    Validation suite. Four checks:
      1. Bounded: all similarity scores in [-1.0, 1.0]
      2. No NaN: no NaN values in any similarity computation
      3. Symmetric: sim(a, b) == sim(b, a)
      4. Self-similarity: sim(a, a) == 1.0 (or very close)
      5. Top-1 is self: for any zip, retrieve_top_n returns the zip itself first
    """
    vectors = _load_weight_vectors()
    all_zips = list(vectors.keys())

    SAMPLE_SIZE = 50  # zips to check per test
    random.seed(42)
    sample = random.sample(all_zips, min(SAMPLE_SIZE, len(all_zips)))

    print("\nEnvelope Retrieval — Validation Suite")
    print("=" * 60)

    results = {}

    # ------------------------------------------------------------------
    # Check 1 & 2: Bounded + No NaN
    # ------------------------------------------------------------------
    print("\n  [1/5] Bounding check: all scores in [-1.0, 1.0] ...")
    print("  [2/5] NaN check: no NaN in similarity results ...")

    bounded_ok = True
    nan_ok     = True
    pairs_checked = 0

    pairs = []
    for i in range(min(30, len(sample))):
        for j in range(i + 1, min(30, len(sample))):
            pairs.append((sample[i], sample[j]))

    for zip_a, zip_b in pairs:
        va = vectors[zip_a]["vector"]
        vb = vectors[zip_b]["vector"]
        score = compute_similarity(va, vb)
        pairs_checked += 1

        if math.isnan(score):
            nan_ok = False
            print(f"    NaN detected: sim({zip_a}, {zip_b})")
            break

        if score < -1.0 - 1e-9 or score > 1.0 + 1e-9:
            bounded_ok = False
            print(f"    Out of bounds: sim({zip_a}, {zip_b}) = {score}")
            break

    print(f"    Pairs checked: {pairs_checked}")
    results["bounded"] = bounded_ok
    results["no_nan"]  = nan_ok
    print(f"    Bounded: {'PASS' if bounded_ok else 'FAIL'}")
    print(f"    No NaN:  {'PASS' if nan_ok else 'FAIL'}")

    # ------------------------------------------------------------------
    # Check 3: Symmetry
    # ------------------------------------------------------------------
    print("\n  [3/5] Symmetry check: sim(a,b) == sim(b,a) ...")
    sym_ok = True
    sym_pairs = random.sample(pairs, min(20, len(pairs)))

    for zip_a, zip_b in sym_pairs:
        va = vectors[zip_a]["vector"]
        vb = vectors[zip_b]["vector"]
        s_ab = compute_similarity(va, vb)
        s_ba = compute_similarity(vb, va)
        if abs(s_ab - s_ba) > 1e-12:
            sym_ok = False
            print(f"    Asymmetry detected: sim({zip_a},{zip_b})={s_ab:.10f} != sim({zip_b},{zip_a})={s_ba:.10f}")
            break

    results["symmetric"] = sym_ok
    print(f"    Symmetry:  {'PASS' if sym_ok else 'FAIL'} ({len(sym_pairs)} pairs checked)")

    # ------------------------------------------------------------------
    # Check 4: Self-similarity == 1.0
    # ------------------------------------------------------------------
    print("\n  [4/5] Self-similarity check: sim(a,a) == 1.0 ...")
    self_ok = True
    self_sample = random.sample(all_zips, min(50, len(all_zips)))

    for nzip in self_sample:
        v = vectors[nzip]["vector"]
        score = compute_similarity(v, v)
        if abs(score - 1.0) > 1e-9:
            self_ok = False
            print(f"    Self-similarity != 1.0: sim({nzip},{nzip}) = {score:.12f}")
            break

    results["self_sim_1"] = self_ok
    print(f"    Self-similarity:  {'PASS' if self_ok else 'FAIL'} ({len(self_sample)} zips checked)")

    # ------------------------------------------------------------------
    # Check 5: Top-1 for any zip is itself
    # ------------------------------------------------------------------
    print("\n  [5/5] Top-1 self check: retrieve_top_n returns self as rank 1 ...")
    top1_ok  = True
    top1_sample = random.sample(all_zips, min(20, len(all_zips)))

    for nzip in top1_sample:
        qv      = build_query_vector(nzip)
        results_list = retrieve_top_n(qv, n=1, tier="tier2")
        if not results_list or results_list[0]["numeric_zip"] != nzip:
            top1_ok = False
            got = results_list[0]["numeric_zip"] if results_list else "nothing"
            print(f"    Top-1 not self for {nzip}: got {got}")
            break

    results["top1_is_self"] = top1_ok
    print(f"    Top-1 self:  {'PASS' if top1_ok else 'FAIL'} ({len(top1_sample)} zips checked)")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    all_pass = all(results.values())
    passed   = sum(results.values())
    total    = len(results)

    print(f"\n{'='*60}")
    print(f"  RESULT: {passed}/{total} checks passed  ({'ALL PASS' if all_pass else 'FAILURES DETECTED'})")
    print()

    sys.exit(0 if all_pass else 1)


# ---------------------------------------------------------------------------
# CLI: --stats
# ---------------------------------------------------------------------------

def run_stats() -> None:
    """
    Report aggregate statistics about the similarity space.
      - Dimensionality
      - Average similarity (sampled pairs)
      - Tightest cluster (most similar non-self pair)
      - Loosest outlier (most dissimilar pair)
      - Per-tier average similarity
    """
    vectors  = _load_weight_vectors()
    all_zips = list(vectors.keys())

    SAMPLE_PAIRS = 500
    random.seed(99)

    pairs = []
    while len(pairs) < SAMPLE_PAIRS:
        a, b = random.sample(all_zips, 2)
        if a != b:
            pairs.append((a, b))

    print(f"\nEnvelope Retrieval — Similarity Statistics")
    print("=" * 60)
    print(f"  Total zip codes:     {len(all_zips)}")
    print(f"  Vector dimensions:   {VECTOR_SIZE}")
    print(f"  Sample pairs:        {len(pairs)}")

    for tier in ["tier1", "tier2", "tier3", "tier4"]:
        weights = _make_weight_array(tier)
        scores  = []
        tightest_score = -2.0
        loosest_score  =  2.0
        tightest_pair  = None
        loosest_pair   = None

        for zip_a, zip_b in pairs:
            va = vectors[zip_a]["vector"]
            vb = vectors[zip_b]["vector"]
            score = compute_similarity(va, vb, weights)
            scores.append(score)

            if score > tightest_score:
                tightest_score = score
                tightest_pair  = (zip_a, zip_b)
            if score < loosest_score:
                loosest_score = score
                loosest_pair  = (zip_a, zip_b)

        avg  = sum(scores) / len(scores) if scores else 0.0
        stddev = math.sqrt(
            sum((s - avg) ** 2 for s in scores) / len(scores)
        ) if scores else 0.0

        ta_emoji = vectors[tightest_pair[0]]["emoji_zip"] if tightest_pair else ""
        tb_emoji = vectors[tightest_pair[1]]["emoji_zip"] if tightest_pair else ""
        la_emoji = vectors[loosest_pair[0]]["emoji_zip"]  if loosest_pair  else ""
        lb_emoji = vectors[loosest_pair[1]]["emoji_zip"]  if loosest_pair  else ""

        print(f"\n  [{tier.upper()}]")
        print(f"    Avg similarity:   {avg:.4f}  (σ = {stddev:.4f})")
        print(f"    Tightest pair:    {ta_emoji} ↔ {tb_emoji}  ({tightest_score:.4f})")
        print(f"    Loosest outlier:  {la_emoji} ↔ {lb_emoji}  ({loosest_score:.4f})")

    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="envelope_retrieval.py",
        description="CX-31: PPL± Envelope Similarity & Retrieval Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python scripts/middle-math/envelope_retrieval.py --query 2123
    python scripts/middle-math/envelope_retrieval.py --query ⛽🏛🪡🔵 --tier tier1
    python scripts/middle-math/envelope_retrieval.py --deck 07
    python scripts/middle-math/envelope_retrieval.py --operis 2026-03-06
    python scripts/middle-math/envelope_retrieval.py --validate
    python scripts/middle-math/envelope_retrieval.py --stats
        """,
    )

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--query",
        metavar="ZIP",
        help="Use the zip's base vector as a query; show top-N most similar envelopes",
    )
    mode.add_argument(
        "--deck",
        metavar="NUMBER",
        help="Show top-5 most similar envelopes for each zip in the deck",
    )
    mode.add_argument(
        "--operis",
        metavar="DATE",
        help="Retrieve 13 envelopes for the given date's Operis edition (YYYY-MM-DD)",
    )
    mode.add_argument(
        "--validate",
        action="store_true",
        help="Run validation suite: bounded, no NaN, symmetric, self-similarity, top-1 self",
    )
    mode.add_argument(
        "--stats",
        action="store_true",
        help="Report aggregate similarity statistics across all tiers",
    )

    parser.add_argument(
        "--n",
        type=int,
        default=10,
        help="Number of results to return (default: 10)",
    )
    parser.add_argument(
        "--tier",
        choices=["tier1", "tier2", "tier3", "tier4"],
        default="tier2",
        help="Retrieval profile tier (default: tier2)",
    )

    args = parser.parse_args()

    if args.query:
        run_query(args.query, n=args.n, tier=args.tier)
    elif args.deck:
        run_deck(args.deck, n=args.n, tier=args.tier)
    elif args.operis:
        run_operis(args.operis, n=args.n)
    elif args.validate:
        run_validate()
    elif args.stats:
        run_stats()


if __name__ == "__main__":
    main()
