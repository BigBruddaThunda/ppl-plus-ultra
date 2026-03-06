#!/usr/bin/env python3
"""
scripts/middle-math/weight_vector.py
CX-14: Weight Vector Computation Engine

Computes a 61-dimensional weight vector for each of the 1,680 zip codes
defined in middle-math/zip-registry.json, using the 6 SCL weight declaration
files in middle-math/weights/.

Output: middle-math/weight-vectors.json

Usage:
    python scripts/middle-math/weight_vector.py              # compute all 1,680
    python scripts/middle-math/weight_vector.py --stats      # print statistics
    python scripts/middle-math/weight_vector.py --validate   # run validation checks
    python scripts/middle-math/weight_vector.py --zip ⛽🏛🪡🔵  # single zip
"""

import json
import re
import sys
import argparse
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
WEIGHTS_DIR = REPO_ROOT / "middle-math" / "weights"
REGISTRY_PATH = REPO_ROOT / "middle-math" / "zip-registry.json"
OUTPUT_PATH = REPO_ROOT / "middle-math" / "weight-vectors.json"

# ---------------------------------------------------------------------------
# 61-emoji position map
# Positions 0–6:   Orders
# Positions 7–12:  Axes
# Positions 13–17: Types
# Positions 18–25: Colors
# Positions 26–48: Blocks (22 blocks + 🧮 SAVE = 23 slots)
# Positions 49–60: Operators (12 operators)
# ---------------------------------------------------------------------------
EMOJI_POSITIONS = {
    # Orders (7)
    "🐂": 0, "⛽": 1, "🦋": 2, "🏟": 3, "🌾": 4, "⚖": 5, "🖼": 6,
    # Axes (6)
    "🏛": 7, "🔨": 8, "🌹": 9, "🪐": 10, "⌛": 11, "🐬": 12,
    # Types (5)
    "🛒": 13, "🪡": 14, "🍗": 15, "➕": 16, "➖": 17,
    # Colors (8)
    "⚫": 18, "🟢": 19, "🔵": 20, "🟣": 21, "🔴": 22, "🟠": 23, "🟡": 24, "⚪": 25,
    # Blocks (22 + SAVE = 23)
    "♨️": 26, "🎯": 27, "🔢": 28, "🧈": 29, "🫀": 30, "▶️": 31, "🎼": 32,
    "♟️": 33, "🪜": 34, "🌎": 35, "🎱": 36, "🌋": 37, "🪞": 38, "🗿": 39,
    "🛠": 40, "🧩": 41, "🪫": 42, "🏖": 43, "🏗": 44, "🧬": 45, "🚂": 46,
    "🔠": 47, "🧮": 48,
    # Operators (12)
    "🧲": 49, "🐋": 50, "🤌": 51, "🧸": 52, "✒️": 53, "🦉": 54,
    "🥨": 55, "🦢": 56, "📍": 57, "👀": 58, "🪵": 59, "🚀": 60,
}

POSITION_EMOJIS = {v: k for k, v in EMOJI_POSITIONS.items()}
VECTOR_SIZE = 61

# Sort emojis by length descending so longer sequences match before shorter ones
EMOJIS_SORTED = sorted(EMOJI_POSITIONS.keys(), key=len, reverse=True)

# Hard suppression threshold: Order or Color weights at or below this lock the result
HARD_SUPPRESS_THRESHOLD = -6

# Dial priority for interaction resolution (lower index = higher priority)
DIAL_ORDER = ["order", "color", "axis", "type"]


# ---------------------------------------------------------------------------
# Weight file parsers
# ---------------------------------------------------------------------------

def _find_emoji_in_cell(cell_text: str) -> str | None:
    """Extract the leading emoji from a table cell, or None if not found."""
    text = cell_text.strip()
    for emoji in EMOJIS_SORTED:
        if text.startswith(emoji):
            return emoji
    return None


def _parse_weight(weight_str: str) -> int | None:
    """Parse '+6', '-5', '+8' → integer. Returns None if not parseable."""
    s = weight_str.strip()
    try:
        return int(s.lstrip("+"))
    except ValueError:
        return None


def _parse_standard_weight_file(filepath: Path) -> dict:
    """
    Parse order-weights.md, axis-weights.md, type-weights.md, color-weights.md,
    and operator-weights.md.

    Structure:
        ## <emoji> <Name>
        Self: +8 when primary ...
        ### Affinities
        | Emoji | Weight | Source Rule |
        | <emoji> <name> | +N | ... |
        ### Suppressions
        | Emoji | Weight | Source Rule |
        | <emoji> <name> | -N | ... |

    Returns:
        {
          emoji_str: {
            "affinities": {target_emoji: weight, ...},
            "suppressions": {target_emoji: weight, ...}
          }, ...
        }
    """
    text = filepath.read_text(encoding="utf-8")
    declarations = {}

    # Split on ## section headers
    sections = re.split(r"^## ", text, flags=re.MULTILINE)
    for section in sections[1:]:
        lines = section.split("\n")
        header = lines[0].strip()

        section_emoji = _find_emoji_in_cell(header)
        if not section_emoji:
            continue

        declarations[section_emoji] = {"affinities": {}, "suppressions": {}}
        mode = None

        for line in lines[1:]:
            # Detect subsection headers
            stripped = line.strip()
            if re.match(r"^###\s+Affinities", stripped):
                mode = "affinities"
                continue
            elif re.match(r"^###\s+Suppressions", stripped):
                mode = "suppressions"
                continue
            elif stripped.startswith("###"):
                mode = None
                continue
            elif stripped.startswith("## ") and not stripped.startswith("###"):
                break  # next top-level section

            if mode is None:
                continue

            # Parse table rows
            if not stripped.startswith("|") or "---" in stripped:
                continue
            cells = [c.strip() for c in stripped.split("|")]
            cells = [c for c in cells if c]
            if len(cells) < 2:
                continue

            # Skip header rows (first column is "Emoji", "Order", "Color", etc.)
            first_cell = cells[0].strip()
            if first_cell.lower() in ("emoji", "order", "color", "axis", "type",
                                       "block", "operator", "emoji | weight"):
                continue

            target_emoji = _find_emoji_in_cell(first_cell)
            if not target_emoji:
                continue  # Non-emoji rows: "Barbell exercises", "GOLD exercises", etc.

            weight = _parse_weight(cells[1])
            if weight is None:
                continue

            declarations[section_emoji][mode][target_emoji] = weight

    return declarations


def _parse_block_weight_file(filepath: Path) -> dict:
    """
    Parse block-weights.md.

    Structure:
        ## <block_emoji> <Name>
        Self: +N when active
        ### Order Affinities
        | Order | Weight | Source Rule |
        | <order_emoji> <name> | +N | ... |
        ### Color Affinities
        | Color | Weight | Source Rule |
        | <color_emoji> <name> | +N | ... |
        ### Order Suppressions / ### Color Suppressions
        ...

    Returns the same shape as _parse_standard_weight_file:
        {
          block_emoji: {
            "affinities": {dial_emoji: weight, ...},
            "suppressions": {dial_emoji: weight, ...}
          }, ...
        }
    """
    text = filepath.read_text(encoding="utf-8")
    declarations = {}

    sections = re.split(r"^## ", text, flags=re.MULTILINE)
    for section in sections[1:]:
        lines = section.split("\n")
        header = lines[0].strip()

        block_emoji = _find_emoji_in_cell(header)
        if not block_emoji:
            continue

        declarations[block_emoji] = {"affinities": {}, "suppressions": {}}
        mode = None

        for line in lines[1:]:
            stripped = line.strip()

            # Detect subsections: Order Affinities, Color Affinities, Positional Notes, etc.
            if re.match(r"^###\s+(Order|Color)\s+Affinities", stripped):
                mode = "affinities"
                continue
            elif re.match(r"^###\s+(Order|Color)\s+Suppressions", stripped):
                mode = "suppressions"
                continue
            elif stripped.startswith("###"):
                mode = None
                continue
            elif stripped.startswith("## ") and not stripped.startswith("###"):
                break

            if mode is None:
                continue

            if not stripped.startswith("|") or "---" in stripped:
                continue
            cells = [c.strip() for c in stripped.split("|")]
            cells = [c for c in cells if c]
            if len(cells) < 2:
                continue

            first_cell = cells[0].strip()
            if first_cell.lower() in ("order", "color", "emoji", "axis", "type"):
                continue

            target_emoji = _find_emoji_in_cell(first_cell)
            if not target_emoji:
                continue

            weight = _parse_weight(cells[1])
            if weight is None:
                continue

            declarations[block_emoji][mode][target_emoji] = weight

    return declarations


# ---------------------------------------------------------------------------
# Load all weight declarations
# ---------------------------------------------------------------------------

def load_all_weights() -> dict:
    """
    Load all 6 weight declaration files.

    Returns:
        {
          "order":    {order_emoji: {affinities, suppressions}, ...},
          "axis":     {axis_emoji:  {affinities, suppressions}, ...},
          "type":     {type_emoji:  {affinities, suppressions}, ...},
          "color":    {color_emoji: {affinities, suppressions}, ...},
          "block":    {block_emoji: {affinities, suppressions}, ...},
          "operator": {op_emoji:    {affinities, suppressions}, ...},
        }
    """
    return {
        "order":    _parse_standard_weight_file(WEIGHTS_DIR / "order-weights.md"),
        "axis":     _parse_standard_weight_file(WEIGHTS_DIR / "axis-weights.md"),
        "type":     _parse_standard_weight_file(WEIGHTS_DIR / "type-weights.md"),
        "color":    _parse_standard_weight_file(WEIGHTS_DIR / "color-weights.md"),
        "block":    _parse_block_weight_file(WEIGHTS_DIR / "block-weights.md"),
        "operator": _parse_standard_weight_file(WEIGHTS_DIR / "operator-weights.md"),
    }


# ---------------------------------------------------------------------------
# Polarity table for operator derivation
# (source: scl-directory.md / CLAUDE.md)
# ---------------------------------------------------------------------------
PREPARATORY_COLORS = {"⚫", "🟢", "⚪", "🟡"}
EXPRESSIVE_COLORS  = {"🔵", "🟣", "🔴", "🟠"}

OPERATOR_TABLE = {
    # Axis       Preparatory  Expressive
    "🏛": ("📍", "🤌"),
    "🔨": ("🧸", "🥨"),
    "🌹": ("👀", "🦢"),
    "🪐": ("🪵", "🚀"),
    "⌛": ("🐋", "✒️"),
    "🐬": ("🧲", "🦉"),
}


def derive_operator(axis_emoji: str, color_emoji: str) -> str:
    """Derive the default operator emoji from Axis × Color polarity."""
    pair = OPERATOR_TABLE.get(axis_emoji, ("📍", "🤌"))
    return pair[0] if color_emoji in PREPARATORY_COLORS else pair[1]


# ---------------------------------------------------------------------------
# Vector computation
# ---------------------------------------------------------------------------

def compute_vector(
    order_e: str, axis_e: str, type_e: str, color_e: str,
    weights: dict,
    operator_e: str | None = None,
) -> list:
    """
    Compute the 61-value weight vector for a zip code (order, axis, type, color).

    Algorithm (from weight-system-spec.md and interaction-rules.md):
    1. Primary weights: +8 for each active dial emoji's own slot.
    2. Affinity cascade: each dial adds positive weights to other emoji slots.
    3. Suppression cascade: each dial adds negative weights to other emoji slots.
    4. Operator cascade (supplemental): derived operator adds its weights.
    5. Block supplemental: block-weights perspective fills in block slots.
    6. Interaction resolution:
       - ORDER hard suppression (≤-6) → locks that slot at Order's declared value.
       - Else COLOR hard suppression (≤-6) → locks that slot at Color's declared value.
       - Else: sum all accumulated weights, clamp to [-8, +8].

    Returns: list of 61 integers in range [-8, +8].
    """
    if operator_e is None:
        operator_e = derive_operator(axis_e, color_e)

    # Active dials in priority order for interaction resolution
    active = {
        "order": order_e,
        "axis":  axis_e,
        "type":  type_e,
        "color": color_e,
    }

    # Step 1: Initialize accumulation buckets per dial
    # We track each dial's contribution separately for interaction resolution.
    per_dial = {d: [0] * VECTOR_SIZE for d in DIAL_ORDER}
    operator_contrib = [0] * VECTOR_SIZE

    # Primary weights: each dial's own emoji gets +8 from that dial's bucket
    if order_e in EMOJI_POSITIONS:
        per_dial["order"][EMOJI_POSITIONS[order_e]] = 8
    if axis_e in EMOJI_POSITIONS:
        per_dial["axis"][EMOJI_POSITIONS[axis_e]] = 8
    if type_e in EMOJI_POSITIONS:
        per_dial["type"][EMOJI_POSITIONS[type_e]] = 8
    if color_e in EMOJI_POSITIONS:
        per_dial["color"][EMOJI_POSITIONS[color_e]] = 8

    # Step 2+3: Affinity and suppression cascades per dial
    for dial_name, dial_emoji in active.items():
        dial_decl = weights.get(dial_name, {}).get(dial_emoji, {})
        aff  = dial_decl.get("affinities", {})
        supp = dial_decl.get("suppressions", {})

        for target, w in aff.items():
            if target in EMOJI_POSITIONS:
                idx = EMOJI_POSITIONS[target]
                # Don't double-count the dial's own self-weight (already set in primary)
                if target == dial_emoji:
                    continue
                per_dial[dial_name][idx] += w

        for target, w in supp.items():
            if target in EMOJI_POSITIONS:
                idx = EMOJI_POSITIONS[target]
                per_dial[dial_name][idx] += w  # w is already negative

    # Step 4: Operator cascade (supplemental — lower priority than Type)
    op_decl = weights.get("operator", {}).get(operator_e, {})
    for target, w in op_decl.get("affinities", {}).items():
        if target in EMOJI_POSITIONS and target != operator_e:
            operator_contrib[EMOJI_POSITIONS[target]] += w
    for target, w in op_decl.get("suppressions", {}).items():
        if target in EMOJI_POSITIONS:
            operator_contrib[EMOJI_POSITIONS[target]] += w

    # Also set the operator's own primary weight
    if operator_e in EMOJI_POSITIONS:
        operator_contrib[EMOJI_POSITIONS[operator_e]] += 8

    # Note: block-weights.md provides a complementary perspective on the same
    # relationships already declared by the 4 dial files. It is NOT added here
    # to avoid double-counting. It is used by external validation tooling only.

    # Step 5: Interaction resolution
    result = [0] * VECTOR_SIZE
    for i in range(VECTOR_SIZE):
        order_contrib = per_dial["order"][i]
        color_contrib = per_dial["color"][i]
        axis_contrib  = per_dial["axis"][i]
        type_contrib  = per_dial["type"][i]
        op_c          = operator_contrib[i]

        # Hard suppression check: Order priority (≤ threshold locks the slot)
        if order_contrib <= HARD_SUPPRESS_THRESHOLD:
            result[i] = max(-8, min(8, order_contrib))
            continue

        # Hard suppression check: Color priority
        if color_contrib <= HARD_SUPPRESS_THRESHOLD:
            result[i] = max(-8, min(8, color_contrib))
            continue

        # Soft: sum all contributions and clamp
        raw = order_contrib + color_contrib + axis_contrib + type_contrib + op_c
        result[i] = max(-8, min(8, raw))

    return result


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

# Blocks that must be suppressed in certain Order/Color contexts (hard rules)
GUTTER_IDX    = EMOJI_POSITIONS["🌋"]
ORDERS_BLOCK_GUTTER = {"🖼", "🐂"}   # Order emojis that hard-block Gutter
COLORS_BLOCK_GUTTER = {"⚪"}          # Color emojis that hard-block Gutter

VANITY_IDX = EMOJI_POSITIONS["🪞"]
ORDERS_SUPPRESS_VANITY = {"🏟"}  # Performance hard-suppresses Vanity

JUNK_SUPP_IDX = EMOJI_POSITIONS["🧩"]
ORDERS_SUPPRESS_SUPP = {"🏟"}   # Performance: "No junk volume"


def validate_hard_suppression(
    numeric_zip: str, vector: list,
    order_e: str, color_e: str,
) -> list:
    """
    Run hard-suppression checks on a computed vector.
    Returns list of violation strings (empty = clean).
    """
    violations = []

    # Gutter never in 🖼 Restoration Order
    if order_e in ORDERS_BLOCK_GUTTER and vector[GUTTER_IDX] > -6:
        violations.append(
            f"[{numeric_zip}] 🌋 Gutter not hard-suppressed under Order {order_e} "
            f"(got {vector[GUTTER_IDX]}, expected ≤-6)"
        )

    # Gutter never in ⚪ Mindful Color
    if color_e in COLORS_BLOCK_GUTTER and vector[GUTTER_IDX] > -6:
        violations.append(
            f"[{numeric_zip}] 🌋 Gutter not hard-suppressed under Color {color_e} "
            f"(got {vector[GUTTER_IDX]}, expected ≤-6)"
        )

    # Vanity suppressed in 🏟 Performance
    if order_e in ORDERS_SUPPRESS_VANITY and vector[VANITY_IDX] > -5:
        violations.append(
            f"[{numeric_zip}] 🪞 Vanity not suppressed under Order {order_e} "
            f"(got {vector[VANITY_IDX]}, expected ≤-5)"
        )

    # No junk volume (Supplemental) in 🏟 Performance
    if order_e in ORDERS_SUPPRESS_SUPP and vector[JUNK_SUPP_IDX] > -5:
        violations.append(
            f"[{numeric_zip}] 🧩 Supplemental not suppressed under Order {order_e} "
            f"(got {vector[JUNK_SUPP_IDX]}, expected ≤-5)"
        )

    return violations


# ---------------------------------------------------------------------------
# Batch computation
# ---------------------------------------------------------------------------

def compute_all_vectors(weights: dict) -> dict:
    """
    Compute weight vectors for all 1,680 zip codes.

    Returns: {numeric_zip: {emoji_zip, vector, deck, gold_eligible}}
    """
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    result = {}

    for entry in registry:
        numeric_zip = entry["numeric_zip"]
        emoji_zip   = entry["emoji_zip"]
        order_e     = entry["order"]["emoji"]
        axis_e      = entry["axis"]["emoji"]
        type_e      = entry["type"]["emoji"]
        color_e     = entry["color"]["emoji"]
        operator_e  = entry.get("operator", {}).get("emoji")
        deck        = entry.get("deck_number")
        gold_elig   = entry.get("gold_eligible", False)

        vector = compute_vector(order_e, axis_e, type_e, color_e, weights, operator_e)

        result[numeric_zip] = {
            "emoji_zip":     emoji_zip,
            "vector":        vector,
            "deck":          deck,
            "gold_eligible": gold_elig,
        }

    return result


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------

def cmd_stats(vectors: dict) -> None:
    """Print statistics about the computed vectors."""
    zips = list(vectors.keys())
    n = len(zips)
    all_vectors = [vectors[z]["vector"] for z in zips]

    total_weights = [sum(v) for v in all_vectors]
    min_total = min(total_weights)
    max_total = max(total_weights)
    mean_total = sum(total_weights) / n

    # Find the dimension (position) with highest and lowest mean weight
    dim_means = []
    for i in range(VECTOR_SIZE):
        dim_means.append(sum(v[i] for v in all_vectors) / n)

    highest_dim = max(range(VECTOR_SIZE), key=lambda i: dim_means[i])
    lowest_dim  = min(range(VECTOR_SIZE), key=lambda i: dim_means[i])

    # Highest and lowest weighted zips by total
    highest_zip = max(zips, key=lambda z: sum(vectors[z]["vector"]))
    lowest_zip  = min(zips, key=lambda z: sum(vectors[z]["vector"]))

    print(f"--- Weight Vector Statistics ---")
    print(f"Total zip codes processed:  {n}")
    print(f"Vector dimensionality:      {VECTOR_SIZE}")
    print(f"Total weight per vector:")
    print(f"  min:   {min_total:.0f}")
    print(f"  max:   {max_total:.0f}")
    print(f"  mean:  {mean_total:.1f}")
    print(f"Highest-weighted zip: {highest_zip} ({vectors[highest_zip]['emoji_zip']}, total={sum(vectors[highest_zip]['vector'])})")
    print(f"Lowest-weighted zip:  {lowest_zip} ({vectors[lowest_zip]['emoji_zip']}, total={sum(vectors[lowest_zip]['vector'])})")
    print(f"Highest mean-weight dimension: {highest_dim} ({POSITION_EMOJIS.get(highest_dim,'?')}, mean={dim_means[highest_dim]:.2f})")
    print(f"Lowest mean-weight dimension:  {lowest_dim} ({POSITION_EMOJIS.get(lowest_dim,'?')}, mean={dim_means[lowest_dim]:.2f})")


def cmd_validate(vectors: dict) -> bool:
    """Run validation checks on all vectors. Returns True if all pass."""
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    registry_zips = {e["numeric_zip"] for e in registry}
    vector_zips   = set(vectors.keys())

    violations = []

    # Check 1: All zips present
    missing = registry_zips - vector_zips
    extra   = vector_zips - registry_zips
    if missing:
        violations.append(f"Missing vectors for {len(missing)} zip(s): {sorted(missing)[:5]}...")
    if extra:
        violations.append(f"Extra vectors not in registry: {sorted(extra)[:5]}...")

    # Check 2: Vector size and value range
    for z, data in vectors.items():
        v = data["vector"]
        if len(v) != VECTOR_SIZE:
            violations.append(f"[{z}] Vector length {len(v)} ≠ {VECTOR_SIZE}")
        for i, val in enumerate(v):
            if not isinstance(val, int):
                violations.append(f"[{z}] Non-integer at position {i}: {val}")
            elif val < -8 or val > 8:
                violations.append(f"[{z}] Out-of-range value at position {i}: {val}")

    # Check 3: Hard suppression rules
    zip_lookup = {e["numeric_zip"]: e for e in registry}
    for z, data in vectors.items():
        entry = zip_lookup.get(z, {})
        order_e = entry.get("order", {}).get("emoji", "")
        color_e = entry.get("color", {}).get("emoji", "")
        supp_violations = validate_hard_suppression(z, data["vector"], order_e, color_e)
        violations.extend(supp_violations)

    if violations:
        print(f"--- VALIDATION FAILED: {len(violations)} violation(s) ---")
        for v in violations[:20]:
            print(f"  ✗ {v}")
        if len(violations) > 20:
            print(f"  ... and {len(violations) - 20} more")
        return False
    else:
        print(f"--- VALIDATION PASSED: {len(vectors)} vectors, {VECTOR_SIZE} dimensions ---")
        print("  ✓ All zip codes present")
        print("  ✓ All vector dimensions valid (int, in range [-8, +8])")
        print("  ✓ Hard suppression rules enforced (Gutter, Vanity, Supplemental)")
        return True


def cmd_single_zip(emoji_or_numeric: str, weights: dict) -> None:
    """Compute and display the vector for a single zip code."""
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))

    entry = None
    for e in registry:
        if e["numeric_zip"] == emoji_or_numeric or e["emoji_zip"] == emoji_or_numeric:
            entry = e
            break

    if not entry:
        print(f"Zip code not found: {emoji_or_numeric}", file=sys.stderr)
        sys.exit(1)

    order_e    = entry["order"]["emoji"]
    axis_e     = entry["axis"]["emoji"]
    type_e     = entry["type"]["emoji"]
    color_e    = entry["color"]["emoji"]
    operator_e = entry.get("operator", {}).get("emoji")
    vector     = compute_vector(order_e, axis_e, type_e, color_e, weights, operator_e)

    print(f"Zip: {entry['numeric_zip']} {entry['emoji_zip']}")
    print(f"     Order={order_e} Axis={axis_e} Type={type_e} Color={color_e} Op={operator_e}")
    print(f"Vector [{VECTOR_SIZE} dimensions]:")
    for i, val in enumerate(vector):
        emoji = POSITION_EMOJIS.get(i, "?")
        bar = "+" * max(0, val) if val >= 0 else "-" * abs(val)
        print(f"  [{i:2d}] {emoji:3s} {val:+3d}  {bar}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="CX-14: Weight Vector Computation Engine for PPL±"
    )
    parser.add_argument("--stats",    action="store_true", help="Print vector statistics")
    parser.add_argument("--validate", action="store_true", help="Run validation checks")
    parser.add_argument("--zip",      type=str,            help="Compute vector for a single zip code")
    parser.add_argument("--no-write", action="store_true", help="Skip writing output file")
    args = parser.parse_args()

    print("Loading weight declaration files...", end=" ", flush=True)
    weights = load_all_weights()
    loaded = {k: len(v) for k, v in weights.items()}
    print(f"done. {loaded}")

    if args.zip:
        cmd_single_zip(args.zip, weights)
        return

    print(f"Computing vectors for all 1,680 zip codes...", end=" ", flush=True)
    vectors = compute_all_vectors(weights)
    print(f"done. {len(vectors)} vectors computed.")

    if args.stats:
        cmd_stats(vectors)

    if args.validate:
        passed = cmd_validate(vectors)
        if not passed:
            sys.exit(1)

    if not args.no_write:
        OUTPUT_PATH.write_text(
            json.dumps(vectors, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        size_kb = OUTPUT_PATH.stat().st_size // 1024
        print(f"Written: {OUTPUT_PATH.relative_to(REPO_ROOT)} ({size_kb} KB)")

    if not args.stats and not args.validate and not args.no_write:
        print("Run with --stats to see statistics, --validate to check hard suppression rules.")


if __name__ == "__main__":
    main()
