#!/usr/bin/env python3
"""
weight-vector-to-css.py — Bridge from SCL weight vectors to CSS custom properties.

Reads a 61-dimensional weight vector for a given zip code and generates
CSS custom properties that drive the Ppl± HTML experience layer.

Usage:
    python scripts/weight-vector-to-css.py 🐂🏛🛒⚫
    python scripts/weight-vector-to-css.py 1111
    python scripts/weight-vector-to-css.py 🐂🏛🛒⚫ --file html/prototype/room-vars.css
    python scripts/weight-vector-to-css.py 🐂🏛🛒⚫ --inline

Reference: middle-math/weight-css-spec.md, middle-math/design-tokens.json
"""

import argparse
import json
import os
import sys

# ---------------------------------------------------------------------------
# Paths — resolve relative to repo root
# ---------------------------------------------------------------------------
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEIGHT_VECTORS_PATH = os.path.join(REPO_ROOT, "middle-math", "weight-vectors.json")
DESIGN_TOKENS_PATH = os.path.join(REPO_ROOT, "middle-math", "design-tokens.json")

# ---------------------------------------------------------------------------
# Emoji-to-numeric mappings
# ---------------------------------------------------------------------------
ORDER_MAP = {"🐂": 1, "⛽": 2, "🦋": 3, "🏟": 4, "🌾": 5, "⚖": 6, "🖼": 7}
AXIS_MAP = {"🏛": 1, "🔨": 2, "🌹": 3, "🪐": 4, "⌛": 5, "🐬": 6}
TYPE_MAP = {"🛒": 1, "🪡": 2, "🍗": 3, "➕": 4, "➖": 5}
COLOR_MAP = {"⚫": 1, "🟢": 2, "🔵": 3, "🟣": 4, "🔴": 5, "🟠": 6, "🟡": 7, "⚪": 8}

# Reverse maps for display
ORDER_EMOJI = {v: k for k, v in ORDER_MAP.items()}
AXIS_EMOJI = {v: k for k, v in AXIS_MAP.items()}
TYPE_EMOJI = {v: k for k, v in TYPE_MAP.items()}
COLOR_EMOJI = {v: k for k, v in COLOR_MAP.items()}

# Index-to-token-key mappings
ORDER_KEYS = ["foundation", "strength", "hypertrophy", "performance",
              "full-body", "balance", "restoration"]
COLOR_KEYS = ["teaching", "bodyweight", "structured", "technical",
              "intense", "circuit", "fun", "mindful"]

# Axis gradient angles
AXIS_GRADIENT_ANGLES = ["0deg", "45deg", "90deg", "135deg", "180deg", "270deg"]

# Density descriptor to numeric spacing multiplier
DENSITY_MULTIPLIERS = {
    "spacious": 1.4,
    "compact": 0.75,
    "comfortable": 1.1,
    "sparse": 0.6,
    "flowing": 1.2,
    "precise": 0.9,
    "airy": 1.5,
}


# ---------------------------------------------------------------------------
# Zip code parsing
# ---------------------------------------------------------------------------
def parse_emoji_zip(raw: str) -> str:
    """Convert an emoji zip code to its 4-digit numeric form."""
    # Extract emoji characters from the string
    emojis = []
    i = 0
    chars = list(raw)
    # Walk through the string collecting emoji codepoints
    # Emojis may be multi-byte; we match against known sets
    remaining = raw
    for dial_map in [ORDER_MAP, AXIS_MAP, TYPE_MAP, COLOR_MAP]:
        found = False
        for emoji in dial_map:
            if remaining.startswith(emoji):
                emojis.append(dial_map[emoji])
                remaining = remaining[len(emoji):]
                found = True
                break
        if not found:
            print(f"Error: Could not parse emoji zip '{raw}'. "
                  f"Stuck at: '{remaining}'", file=sys.stderr)
            sys.exit(1)
    return "".join(str(d) for d in emojis)


def is_numeric_zip(raw: str) -> bool:
    """Check if the input is a 4-digit numeric zip."""
    return len(raw) == 4 and raw.isdigit()


def resolve_zip(raw: str) -> str:
    """Return the 4-digit numeric zip from either emoji or numeric input."""
    stripped = raw.strip()
    if is_numeric_zip(stripped):
        return stripped
    return parse_emoji_zip(stripped)


def zip_to_emoji(numeric: str) -> str:
    """Convert numeric zip back to emoji for display."""
    digits = [int(d) for d in numeric]
    o = ORDER_EMOJI.get(digits[0], "?")
    a = AXIS_EMOJI.get(digits[1], "?")
    t = TYPE_EMOJI.get(digits[2], "?")
    c = COLOR_EMOJI.get(digits[3], "?")
    return f"{o}{a}{t}{c}"


# ---------------------------------------------------------------------------
# Weight vector math
# ---------------------------------------------------------------------------
def normalize(weight: float) -> float:
    """Normalize an octave-scale weight (-8 to +8) to 0.0–1.0."""
    return (weight + 8.0) / 16.0


def dominant_dim(vector: list, start: int, end: int) -> int:
    """Return the index of the maximum value in vector[start..end] inclusive."""
    max_idx = start
    max_val = vector[start]
    for i in range(start + 1, end + 1):
        if vector[i] > max_val:
            max_val = vector[i]
            max_idx = i
    return max_idx


def mean_normalized(vector: list, start: int, end: int) -> float:
    """Return normalized mean of vector[start..end] inclusive."""
    segment = vector[start:end + 1]
    if not segment:
        return 0.5
    raw_mean = sum(segment) / len(segment)
    return normalize(raw_mean)


# ---------------------------------------------------------------------------
# CSS generation
# ---------------------------------------------------------------------------
def generate_css_properties(vector: list, tokens: dict) -> dict:
    """Generate all CSS custom properties from a 61-float weight vector."""
    props = {}

    # --- ORDER (indices 0-6) ---
    order_dim = dominant_dim(vector, 0, 6)
    order_key = ORDER_KEYS[order_dim]
    order_tokens = tokens["orders"][order_key]

    # Density descriptor -> numeric
    density_str = order_tokens["density"]
    spacing_mult = DENSITY_MULTIPLIERS.get(density_str, 1.0)

    props["--ppl-weight-density"] = f"{spacing_mult:.2f}"
    props["--ppl-weight-lineheight"] = str(order_tokens["lineHeight"])
    props["--ppl-weight-font-weight"] = str(order_tokens["fontWeight"])
    props["--ppl-weight-letter-spacing"] = str(order_tokens["letterSpacing"])
    props["--ppl-weight-spacing-multiplier"] = f"{spacing_mult:.2f}"
    props["--ppl-weight-font-size-base"] = str(order_tokens["fontSizeBase"])
    props["--ppl-weight-font-size-display"] = str(order_tokens["fontSizeDisplay"])
    props["--ppl-weight-font-weight-display"] = str(order_tokens["fontWeightDisplay"])

    # --- AXIS (indices 7-12) ---
    axis_dim = dominant_dim(vector, 7, 12)
    axis_norm = normalize(vector[axis_dim])
    axis_index = axis_dim - 7  # 0-based within axis range

    props["--ppl-weight-typography-bias"] = f"{axis_norm:.3f}"
    props["--ppl-weight-visual-rhythm"] = f"{axis_norm:.3f}"
    props["--ppl-axis-gradient-angle"] = AXIS_GRADIENT_ANGLES[axis_index]

    # --- TYPE (indices 13-17) ---
    type_names = ["push", "pull", "legs", "plus", "ultra"]
    for i in range(5):
        val = normalize(vector[13 + i])
        props[f"--ppl-weight-emphasis-{type_names[i]}"] = f"{val:.3f}"

    # --- COLOR (indices 18-25) ---
    color_dim = dominant_dim(vector, 18, 25)
    color_index = color_dim - 18  # 0-based within color range
    color_key = COLOR_KEYS[color_index]
    color_tokens = tokens["colors"][color_key]
    color_norm = normalize(vector[color_dim])

    props["--ppl-theme-primary"] = color_tokens["primary"]
    props["--ppl-theme-secondary"] = color_tokens["secondary"]
    props["--ppl-theme-background"] = color_tokens["background"]
    props["--ppl-theme-surface"] = color_tokens["surface"]
    props["--ppl-theme-text"] = color_tokens["text"]
    props["--ppl-theme-text-on-light"] = color_tokens["textOnLight"]
    props["--ppl-theme-accent"] = color_tokens["accent"]
    props["--ppl-theme-border"] = color_tokens["border"]
    props["--ppl-weight-saturation"] = f"{color_norm:.3f}"
    props["--ppl-weight-contrast"] = f"{color_norm:.3f}"

    # --- DERIVED (indices 26-60) ---
    props["--ppl-weight-rest-emphasis"] = f"{mean_normalized(vector, 26, 35):.3f}"
    props["--ppl-weight-rep-display"] = f"{mean_normalized(vector, 36, 50):.3f}"
    props["--ppl-weight-block-spacing"] = f"{mean_normalized(vector, 26, 60):.3f}"
    props["--ppl-weight-cue-density"] = f"{mean_normalized(vector, 51, 60):.3f}"

    return props


def format_css(props: dict, zip_numeric: str, zip_emoji: str,
               inline: bool = False) -> str:
    """Format CSS properties as a string with comment header."""
    lines = []
    lines.append(f"/* Ppl± Room Variables — {zip_emoji} ({zip_numeric}) */")
    lines.append(f"/* Generated by weight-vector-to-css.py */")
    lines.append("")

    prop_lines = []
    for key, val in props.items():
        prop_lines.append(f"  {key}: {val};")
    prop_block = "\n".join(prop_lines)

    if inline:
        lines.append(prop_block)
    else:
        lines.append(":root {")
        lines.append(prop_block)
        lines.append("}")

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Generate CSS custom properties from a Ppl± zip code weight vector."
    )
    parser.add_argument("zip", help="Zip code in emoji (🐂🏛🛒⚫) or numeric (1111) format")
    parser.add_argument("--file", dest="outfile", default=None,
                        help="Write output to a .css file instead of stdout")
    parser.add_argument("--inline", action="store_true",
                        help="Output without :root wrapper (for embedding in style tags)")
    args = parser.parse_args()

    # Resolve zip code
    zip_numeric = resolve_zip(args.zip)
    zip_emoji = zip_to_emoji(zip_numeric)

    # Validate numeric zip ranges
    digits = [int(d) for d in zip_numeric]
    if not (1 <= digits[0] <= 7):
        print(f"Error: Order digit must be 1-7, got {digits[0]}", file=sys.stderr)
        sys.exit(1)
    if not (1 <= digits[1] <= 6):
        print(f"Error: Axis digit must be 1-6, got {digits[1]}", file=sys.stderr)
        sys.exit(1)
    if not (1 <= digits[2] <= 5):
        print(f"Error: Type digit must be 1-5, got {digits[2]}", file=sys.stderr)
        sys.exit(1)
    if not (1 <= digits[3] <= 8):
        print(f"Error: Color digit must be 1-8, got {digits[3]}", file=sys.stderr)
        sys.exit(1)

    # Load weight vectors
    if not os.path.exists(WEIGHT_VECTORS_PATH):
        print(f"Error: Weight vectors not found at {WEIGHT_VECTORS_PATH}", file=sys.stderr)
        sys.exit(1)
    with open(WEIGHT_VECTORS_PATH, "r", encoding="utf-8") as f:
        weight_vectors = json.load(f)

    if zip_numeric not in weight_vectors:
        print(f"Error: Zip code {zip_numeric} ({zip_emoji}) not found in weight-vectors.json",
              file=sys.stderr)
        sys.exit(1)

    vector = weight_vectors[zip_numeric]["vector"]
    if len(vector) != 61:
        print(f"Error: Expected 61-dimensional vector, got {len(vector)} for {zip_numeric}",
              file=sys.stderr)
        sys.exit(1)

    # Load design tokens
    if not os.path.exists(DESIGN_TOKENS_PATH):
        print(f"Error: Design tokens not found at {DESIGN_TOKENS_PATH}", file=sys.stderr)
        sys.exit(1)
    with open(DESIGN_TOKENS_PATH, "r", encoding="utf-8") as f:
        tokens = json.load(f)

    # Generate CSS
    props = generate_css_properties(vector, tokens)
    css_output = format_css(props, zip_numeric, zip_emoji, inline=args.inline)

    # Output
    if args.outfile:
        outpath = args.outfile
        if not os.path.isabs(outpath):
            outpath = os.path.join(REPO_ROOT, outpath)
        outdir = os.path.dirname(outpath)
        if outdir and not os.path.exists(outdir):
            os.makedirs(outdir, exist_ok=True)
        with open(outpath, "w", encoding="utf-8") as f:
            f.write(css_output)
        print(f"Written to {outpath}")
    else:
        print(css_output)


if __name__ == "__main__":
    main()
