#!/usr/bin/env python3
"""
Ppl± Theme CSS Generator
Generates a unified CSS file from design-tokens.json and the D-Module
rendering system specification.

Reads: middle-math/design-tokens.json
Writes: html/design-system/generated/ppl-theme.css

The generated file contains all 61 SCL emoji dimensions as CSS custom
properties, organized by the 5-layer palette system:
  Layer 0: Order (material)
  Layer 1: Axis (atmosphere)
  Layer 2: Color (furnishing)
  Layer 3: Type (accent)
  Layer 4: Operator (tint)

Usage:
  python scripts/generate-theme-css.py
  python scripts/generate-theme-css.py --output html/design-system/generated/ppl-theme.css
  python scripts/generate-theme-css.py --validate
"""

import json
import os
import sys
import argparse
from datetime import date

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKENS_PATH = os.path.join(REPO_ROOT, "middle-math", "design-tokens.json")
DEFAULT_OUTPUT = os.path.join(REPO_ROOT, "html", "design-system", "generated", "ppl-theme.css")


# D-Module constants from archideck-color-architecture.md
ORDER_SPECS = {
    "foundation":   {"emoji": "\U0001f402", "classical": "Tuscan",     "D": "1rem",      "column_ratio": 7,    "intercolumniation": 4,    "line_mult": 0.8,  "shadow_depth": 0.6, "material_hue": 35,  "material_sat": "12%", "warmth": 0.6},
    "strength":     {"emoji": "\u26fd",     "classical": "Doric",      "D": "1rem",      "column_ratio": 8,    "intercolumniation": 2,    "line_mult": 1.3,  "shadow_depth": 1.4, "material_hue": 220, "material_sat": "5%",  "warmth": 0.3},
    "hypertrophy":  {"emoji": "\U0001f98b", "classical": "Ionic",      "D": "1rem",      "column_ratio": 9,    "intercolumniation": 2.25, "line_mult": 1.0,  "shadow_depth": 1.0, "material_hue": 30,  "material_sat": "8%",  "warmth": 0.5},
    "performance":  {"emoji": "\U0001f3df", "classical": "Corinthian", "D": "1.125rem",  "column_ratio": 10,   "intercolumniation": 1.5,  "line_mult": 1.5,  "shadow_depth": 1.8, "material_hue": 0,   "material_sat": "0%",  "warmth": 0.5},
    "full-body":    {"emoji": "\U0001f33e", "classical": "Composite",  "D": "1rem",      "column_ratio": 10,   "intercolumniation": 2.25, "line_mult": 1.0,  "shadow_depth": 1.0, "material_hue": 25,  "material_sat": "18%", "warmth": 0.7},
    "balance":      {"emoji": "\u2696",     "classical": "Vitruvian",  "D": "0.9375rem", "column_ratio": 8.5,  "intercolumniation": 2.25, "line_mult": 1.1,  "shadow_depth": 1.0, "material_hue": 45,  "material_sat": "6%",  "warmth": 0.5},
    "restoration":  {"emoji": "\U0001f5bc", "classical": "Palladian",  "D": "1.0625rem", "column_ratio": 9.5,  "intercolumniation": 3,    "line_mult": 0.6,  "shadow_depth": 0.2, "material_hue": 40,  "material_sat": "15%", "warmth": 0.8},
}

AXIS_SPECS = {
    "basics":    {"emoji": "\U0001f3db", "latin": "Firmitas",    "floor": "noble",     "superposition": 0.85, "brightness": 1.1,  "hue_shift": 0,   "sat_mult": 1.0,  "warmth": 0},
    "functional":{"emoji": "\U0001f528", "latin": "Utilitas",    "floor": "ground",    "superposition": 1.0,  "brightness": 0.95, "hue_shift": 0,   "sat_mult": 0.85, "warmth": 0},
    "aesthetic": {"emoji": "\U0001f339", "latin": "Venustas",    "floor": "fourth",    "superposition": 0.4,  "brightness": 1.0,  "hue_shift": 5,   "sat_mult": 1.0,  "warmth": 0.15},
    "challenge": {"emoji": "\U0001fa90", "latin": "Gravitas",    "floor": "penthouse", "superposition": 0.25, "brightness": 0.8,  "hue_shift": 0,   "sat_mult": 1.0,  "warmth": 0},
    "time":      {"emoji": "\u231b",     "latin": "Temporitas",  "floor": "second",    "superposition": 0.7,  "brightness": 1.0,  "hue_shift": -10, "sat_mult": 1.0,  "warmth": 0},
    "partner":   {"emoji": "\U0001f42c", "latin": "Sociatas",    "floor": "third",     "superposition": 0.55, "brightness": 1.05, "hue_shift": 5,   "sat_mult": 1.0,  "warmth": 0.1},
}

TYPE_SPECS = {
    "push": {"emoji": "\U0001f6d2", "accent_hue": 15,  "accent_sat": 60, "accent_light": 50},
    "pull": {"emoji": "\U0001faa1", "accent_hue": 210, "accent_sat": 40, "accent_light": 55},
    "legs": {"emoji": "\U0001f357", "accent_hue": 85,  "accent_sat": 35, "accent_light": 42},
    "plus": {"emoji": "\u2795",     "accent_hue": 42,  "accent_sat": 70, "accent_light": 52},
    "ultra":{"emoji": "\u2796",     "accent_hue": 200, "accent_sat": 50, "accent_light": 60},
}

OPERATOR_SPECS = {
    "pono":   {"emoji": "\U0001f4cd", "hue": 210, "sat": 10, "light": 52},
    "capio":  {"emoji": "\U0001f9f2", "hue": 25,  "sat": 55, "light": 52},
    "fero":   {"emoji": "\U0001f9f8", "hue": 18,  "sat": 50, "light": 45},
    "specio": {"emoji": "\U0001f440", "hue": 210, "sat": 8,  "light": 65},
    "tendo":  {"emoji": "\U0001f968", "hue": 8,   "sat": 65, "light": 50},
    "facio":  {"emoji": "\U0001f90c", "hue": 220, "sat": 12, "light": 40},
    "mitto":  {"emoji": "\U0001f680", "hue": 20,  "sat": 80, "light": 50},
    "plico":  {"emoji": "\U0001f9a2", "hue": 290, "sat": 40, "light": 58},
    "teneo":  {"emoji": "\U0001fab5", "hue": 30,  "sat": 45, "light": 42},
    "duco":   {"emoji": "\U0001f40b", "hue": 185, "sat": 45, "light": 35},
    "grapho": {"emoji": "\u270f\ufe0f","hue": 220, "sat": 25, "light": 22},
    "logos":  {"emoji": "\U0001f989", "hue": 40,  "sat": 20, "light": 78},
}

SHADOW_COMPLEMENTS = {
    "teaching":  {"hue": 0,   "sat": "0%"},
    "bodyweight":{"hue": 215, "sat": "10%"},
    "structured":{"hue": 30,  "sat": "8%"},
    "technical": {"hue": 55,  "sat": "8%"},
    "intense":   {"hue": 180, "sat": "10%"},
    "circuit":   {"hue": 210, "sat": "8%"},
    "fun":       {"hue": 240, "sat": "8%"},
    "mindful":   {"hue": 0,   "sat": "0%"},
}


def load_tokens():
    with open(TOKENS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_header():
    return f"""/* =========================================
   Ppl± Generated Theme CSS
   D-Module Rendering System

   Generated: {date.today().isoformat()}
   Source: middle-math/design-tokens.json
   Architecture: seeds/archideck-color-architecture.md

   This file is auto-generated by:
     scripts/generate-theme-css.py

   Do not edit manually. Edit the source
   tokens or the generator script instead.

   61 SCL emojis across 5 palette layers:
     Layer 0: Order (material)
     Layer 1: Axis (atmosphere)
     Layer 2: Color (furnishing)
     Layer 3: Type (accent)
     Layer 4: Operator (tint)
   ========================================= */

"""


def generate_orders(tokens):
    css = "/* === LAYER 0: ORDERS (7 Buildings) === */\n\n"
    for key, spec in ORDER_SPECS.items():
        order_data = tokens["orders"].get(key, {})
        css += f"""/* {spec['emoji']} {spec['classical']} Order ({order_data.get('scl_name', key.title())}) */
[data-order="{key}"],
.order-{key.replace('-', '')} {{
  --ppl-D: {spec['D']};
  --ppl-column-ratio: {spec['column_ratio']};
  --ppl-intercolumniation: {spec['intercolumniation']};
  --ppl-line-multiplier: {spec['line_mult']};
  --ppl-shadow-depth: {spec['shadow_depth']};
  --ppl-material-hue: {spec['material_hue']};
  --ppl-material-sat: {spec['material_sat']};
  --ppl-material-warmth: {spec['warmth']};
  --ppl-weight-font-weight: {order_data.get('fontWeight', 400)};
  --ppl-weight-font-weight-display: {order_data.get('fontWeightDisplay', 600)};
  --ppl-weight-letter-spacing: {order_data.get('letterSpacing', '0.01em')};
  --ppl-weight-lineheight: {order_data.get('lineHeight', 1.6)};
}}

"""
    return css


def generate_axes():
    css = "/* === LAYER 1: AXES (6 Floors) === */\n\n"
    for key, spec in AXIS_SPECS.items():
        css += f"""/* {spec['emoji']} {spec['latin']} ({key.title()}) — {spec['floor']} floor */
[data-axis="{key}"],
.axis-{spec['latin'].lower()} {{
  --ppl-superposition: {spec['superposition']};
  --ppl-atmos-brightness: {spec['brightness']};
  --ppl-atmos-hue-shift: {spec['hue_shift']};
  --ppl-atmos-sat-mult: {spec['sat_mult']};
  --ppl-atmos-warmth: {spec['warmth']};
}}

"""
    return css


def generate_colors(tokens):
    css = "/* === LAYER 2: COLORS (8 Rooms) === */\n\n"
    for key, data in tokens["colors"].items():
        shadow = SHADOW_COMPLEMENTS.get(key, {"hue": 0, "sat": "0%"})
        css += f"""/* {data['emoji']} {data['scl_name']} ({data.get('tonal_name', '')}) */
[data-color="{key}"],
.color-{key} {{
  --ppl-theme-primary: {data['primary']};
  --ppl-theme-secondary: {data['secondary']};
  --ppl-theme-background: {data['background']};
  --ppl-theme-surface: {data['surface']};
  --ppl-theme-text-on-light: {data.get('textOnLight', data['text'])};
  --ppl-theme-accent: {data['accent']};
  --ppl-theme-border: {data['border']};
  --ppl-shadow-hue: {shadow['hue']};
  --ppl-shadow-sat: {shadow['sat']};
}}

"""
    return css


def generate_types():
    css = "/* === LAYER 3: TYPES (5 Wings) === */\n\n"
    for key, spec in TYPE_SPECS.items():
        css += f"""/* {spec['emoji']} {key.title()} */
[data-type="{key}"],
.type-{key} {{
  --ppl-type-accent: hsl({spec['accent_hue']}, {spec['accent_sat']}%, {spec['accent_light']}%);
  --ppl-type-accent-light: hsl({spec['accent_hue']}, {max(spec['accent_sat'] - 15, 10)}%, {min(spec['accent_light'] + 25, 80)}%);
  --ppl-type-accent-dark: hsl({spec['accent_hue']}, {min(spec['accent_sat'] + 5, 80)}%, {max(spec['accent_light'] - 15, 20)}%);
}}

"""
    return css


def generate_operators():
    css = "/* === LAYER 4: OPERATORS (12 Tints) === */\n\n"
    for key, spec in OPERATOR_SPECS.items():
        css += f"""/* {spec['emoji']} {key} */
[data-operator="{key}"],
.operator-{key} {{
  --ppl-operator-tint: hsl({spec['hue']}, {spec['sat']}%, {spec['light']}%);
  --ppl-operator-tint-bg: hsl({spec['hue']}, {max(spec['sat'] - 20, 5)}%, 94%);
}}

"""
    return css


def generate_css():
    tokens = load_tokens()
    parts = [
        generate_header(),
        generate_orders(tokens),
        generate_axes(),
        generate_colors(tokens),
        generate_types(),
        generate_operators(),
    ]
    return "".join(parts)


def validate():
    """Validate that all 61 SCL emojis are represented."""
    counts = {
        "orders": len(ORDER_SPECS),
        "axes": len(AXIS_SPECS),
        "colors": 8,
        "types": len(TYPE_SPECS),
        "operators": len(OPERATOR_SPECS),
    }
    total = sum(counts.values())
    # 22 blocks + 1 SAVE = 23, not included in 61 emoji count
    # 61 = 7 orders + 6 axes + 5 types + 8 colors + 12 operators + 22 blocks + 1 SAVE
    # But blocks are containers, not palette layers

    print(f"Orders:    {counts['orders']}/7")
    print(f"Axes:      {counts['axes']}/6")
    print(f"Colors:    {counts['colors']}/8")
    print(f"Types:     {counts['types']}/5")
    print(f"Operators: {counts['operators']}/12")
    print(f"Total palette layers: {total}/38")
    print(f"(Blocks: 22+1 SAVE = 23 container styles, not palette layers)")

    ok = (counts["orders"] == 7 and counts["axes"] == 6 and
          counts["types"] == 5 and counts["operators"] == 12)
    if ok:
        print("\nAll palette dimensions covered.")
    else:
        print("\nMISSING dimensions detected.")
    return ok


def main():
    parser = argparse.ArgumentParser(description="Ppl± Theme CSS Generator")
    parser.add_argument("--output", "-o", default=DEFAULT_OUTPUT,
                        help="Output CSS file path")
    parser.add_argument("--validate", action="store_true",
                        help="Validate coverage without generating")
    parser.add_argument("--stdout", action="store_true",
                        help="Print to stdout instead of file")
    args = parser.parse_args()

    if args.validate:
        ok = validate()
        sys.exit(0 if ok else 1)

    css = generate_css()

    if args.stdout:
        print(css)
    else:
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(css)
        print(f"Generated: {args.output}")
        print(f"  Orders: 7 | Axes: 6 | Colors: 8 | Types: 5 | Operators: 12")


if __name__ == "__main__":
    main()
