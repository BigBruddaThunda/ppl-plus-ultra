#!/usr/bin/env python3
"""
scripts/middle-math/city_compiler.py
The City Compiler — SCL Universal Resolution Engine

Takes any SCL address (zip code, emoji, deck number, abacus ID) and returns
every derived value in one JSON object. The single resolution function that
ties together: weight vectors, design tokens, D-module architecture, dual
register palettes (cathedral/watercolor), RPG archetype personality, graph
connections, and macro aggregation (deck/abacus centroids).

Seed: seeds/city-compiler-architecture.md
Depends: weight-vectors.json, design-tokens.json, zip-registry.json,
         navigation-graph.json, abacus-profiles/

Usage:
  python city_compiler.py ⛽🏛🪡🔵              # Resolve zip (emoji)
  python city_compiler.py 2123                   # Resolve zip (numeric)
  python city_compiler.py --deck 07              # Resolve deck (centroid)
  python city_compiler.py --abacus 1             # Resolve abacus (centroid)
  python city_compiler.py --city                 # Full city compilation
  python city_compiler.py 2123 --format css      # Output as CSS custom properties
  python city_compiler.py 2123 --register cathedral  # Dark register
  python city_compiler.py --validate             # Validate all 1,680
"""

from __future__ import annotations

import argparse
import colorsys
import json
import math
import os
import sys
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).parent
MM_DIR = SCRIPT_DIR.parent.parent / "middle-math"
REPO_ROOT = SCRIPT_DIR.parent.parent

WEIGHT_VECTORS_PATH = MM_DIR / "weight-vectors.json"
DESIGN_TOKENS_PATH = MM_DIR / "design-tokens.json"
ZIP_REGISTRY_PATH = MM_DIR / "zip-registry.json"
NAV_GRAPH_PATH = MM_DIR / "navigation-graph.json"
ABACUS_INDEX_PATH = MM_DIR / "abacus-profiles" / "index.json"
ABACUS_DIR = MM_DIR / "abacus-profiles"
COMPILED_DIR = MM_DIR / "compiled"

# ---------------------------------------------------------------------------
# SCL Constants (from zip_converter.py, inlined for zero-dependency)
# ---------------------------------------------------------------------------

ORDERS = {
    1: ("🐂", "Foundation", "foundation", "Tuscan"),
    2: ("⛽", "Strength", "strength", "Doric"),
    3: ("🦋", "Hypertrophy", "hypertrophy", "Ionic"),
    4: ("🏟", "Performance", "performance", "Corinthian"),
    5: ("🌾", "Full Body", "full-body", "Composite"),
    6: ("⚖", "Balance", "balance", "Vitruvian"),
    7: ("🖼", "Restoration", "restoration", "Palladian"),
}

AXES = {
    1: ("🏛", "Basics", "basics", "Firmitas"),
    2: ("🔨", "Functional", "functional", "Utilitas"),
    3: ("🌹", "Aesthetic", "aesthetic", "Venustas"),
    4: ("🪐", "Challenge", "challenge", "Gravitas"),
    5: ("⌛", "Time", "time", "Temporitas"),
    6: ("🐬", "Partner", "partner", "Sociatas"),
}

TYPES = {
    1: ("🛒", "Push", "push", ["chest", "front delts", "triceps"]),
    2: ("🪡", "Pull", "pull", ["lats", "rear delts", "biceps", "traps", "erectors"]),
    3: ("🍗", "Legs", "legs", ["quads", "hamstrings", "glutes", "calves"]),
    4: ("➕", "Plus", "plus", ["full body power", "core"]),
    5: ("➖", "Ultra", "ultra", ["cardiovascular system"]),
}

COLORS = {
    1: ("⚫", "Teaching", "teaching", "2-3", False, "preparatory"),
    2: ("🟢", "Bodyweight", "bodyweight", "0-2", False, "preparatory"),
    3: ("🔵", "Structured", "structured", "2-3", False, "expressive"),
    4: ("🟣", "Technical", "technical", "2-5", True, "expressive"),
    5: ("🔴", "Intense", "intense", "2-4", True, "expressive"),
    6: ("🟠", "Circuit", "circuit", "0-3", False, "expressive"),
    7: ("🟡", "Fun", "fun", "0-5", False, "preparatory"),
    8: ("⚪", "Mindful", "mindful", "0-3", False, "preparatory"),
}

OPERATOR_TABLE = {
    "🏛": (("📍", "pono"), ("🤌", "facio")),
    "🔨": (("🧸", "fero"), ("🥨", "tendo")),
    "🌹": (("👀", "specio"), ("🦢", "plico")),
    "🪐": (("🪵", "teneo"), ("🚀", "mitto")),
    "⌛": (("🐋", "duco"), ("✒️", "grapho")),
    "🐬": (("🧲", "capio"), ("🦉", "logos")),
}

OPERATOR_HOUSES = {
    "📍": "The Architects", "🫴": "The Receivers", "🧸": "The Carriers",
    "👀": "The Observers", "🥨": "The Extenders", "🤌": "The Executors",
    "🏹": "The Launchers", "🪢": "The Layerers", "🪵": "The Anchors",
    "🎻": "The Conductors", "✍️": "The Scribes", "🧿": "The Interpreters",
    # Canonical aliases (from CLAUDE.md)
    "🧲": "The Receivers", "🚀": "The Launchers", "🦢": "The Layerers",
    "🐋": "The Conductors", "✒️": "The Scribes", "🦉": "The Interpreters",
}

OPERATOR_TINTS = {
    "📍": {"name": "Slate", "hsl": (210, 15, 45)},
    "🧲": {"name": "Copper", "hsl": (20, 50, 45)},
    "🫴": {"name": "Copper", "hsl": (20, 50, 45)},
    "🧸": {"name": "Sienna", "hsl": (15, 40, 40)},
    "👀": {"name": "Silver", "hsl": (210, 10, 65)},
    "🥨": {"name": "Vermillion", "hsl": (8, 55, 50)},
    "🤌": {"name": "Iron", "hsl": (220, 15, 35)},
    "🚀": {"name": "Fire-orange", "hsl": (20, 65, 50)},
    "🏹": {"name": "Fire-orange", "hsl": (20, 65, 50)},
    "🦢": {"name": "Orchid", "hsl": (285, 30, 55)},
    "🪢": {"name": "Orchid", "hsl": (285, 30, 55)},
    "🪵": {"name": "Oak", "hsl": (30, 35, 40)},
    "🐋": {"name": "Deep teal", "hsl": (185, 45, 35)},
    "🎻": {"name": "Deep teal", "hsl": (185, 45, 35)},
    "✒️": {"name": "Ink", "hsl": (230, 30, 25)},
    "✍️": {"name": "Ink", "hsl": (230, 30, 25)},
    "🦉": {"name": "Ivory", "hsl": (40, 25, 85)},
    "🧿": {"name": "Ivory", "hsl": (40, 25, 85)},
}

# D-Module Architecture (from archideck-color-architecture.md)

ORDER_D_VALUES = {
    1: "1rem", 2: "1rem", 3: "1rem", 4: "1.125rem",
    5: "1rem", 6: "0.9375rem", 7: "1.0625rem",
}

ORDER_COLUMN_RATIOS = {1: 7, 2: 8, 3: 9, 4: 10, 5: 10, 6: 8.5, 7: 9.5}

ORDER_INTERCOLUMNIATION = {
    1: 4.0, 2: 2.75, 3: 2.25, 4: 2.0, 5: 2.25, 6: 2.25, 7: 3.0,
}

ORDER_LINE_MULTIPLIERS = {
    1: 0.8, 2: 1.3, 3: 1.0, 4: 1.5, 5: 1.0, 6: 1.1, 7: 0.6,
}

ORDER_MATERIALS = {
    1: {"name": "Rough-hewn travertine", "hue": 35, "sat": 12, "warmth": 0.6,
        "texture": "porous, matte", "shadow": "soft, diffused"},
    2: {"name": "Pentelic marble", "hue": 220, "sat": 5, "warmth": 0.3,
        "texture": "dense, polished", "shadow": "sharp, defined"},
    3: {"name": "Carrara marble", "hue": 30, "sat": 8, "warmth": 0.5,
        "texture": "smooth, veined", "shadow": "medium, directional"},
    4: {"name": "White marble + gilding", "hue": 0, "sat": 0, "warmth": 0.5,
        "texture": "mirror-polished", "shadow": "high contrast, theatrical"},
    5: {"name": "Sandstone + terracotta", "hue": 25, "sat": 18, "warmth": 0.7,
        "texture": "textured, layered", "shadow": "organic, integrated"},
    6: {"name": "Limestone", "hue": 45, "sat": 6, "warmth": 0.5,
        "texture": "fine-grained", "shadow": "geometrically precise"},
    7: {"name": "Stucco + fresco", "hue": 40, "sat": 15, "warmth": 0.8,
        "texture": "chalky, soft", "shadow": "almost none, flat"},
}

AXIS_ATMOSPHERES = {
    1: {"brightness": 1.1, "hue_shift": 0, "sat_mult": 1.0, "warmth": 0.0,
        "name": "Grand hall", "typography": "Geometric sans-serif. Classical. Stable."},
    2: {"brightness": 0.95, "hue_shift": 0, "sat_mult": 0.85, "warmth": 0.0,
        "name": "Workshop", "typography": "Condensed sans-serif. Utilitarian. Compact."},
    3: {"brightness": 1.0, "hue_shift": 5, "sat_mult": 1.0, "warmth": 0.15,
        "name": "Gallery", "typography": "Light sans-serif. Elegant."},
    4: {"brightness": 0.8, "hue_shift": 0, "sat_mult": 1.0, "warmth": 0.0,
        "name": "Archive", "typography": "Heavy sans-serif. Monumental."},
    5: {"brightness": 1.0, "hue_shift": -10, "sat_mult": 1.0, "warmth": 0.0,
        "name": "Clock tower", "typography": "Monospace accents. Tabular. Precise."},
    6: {"brightness": 1.05, "hue_shift": 5, "sat_mult": 1.0, "warmth": 0.1,
        "name": "Piazza", "typography": "Rounded sans-serif. Open. Warm."},
}

AXIS_SUPERPOSITION = {1: 0.85, 2: 1.0, 3: 0.4, 4: 0.25, 5: 0.7, 6: 0.55}

TYPE_ACCENTS = {
    1: {"name": "Warm red-amber", "hsl": (15, 60, 50)},
    2: {"name": "Cool blue-steel", "hsl": (210, 40, 55)},
    3: {"name": "Earth brown-green", "hsl": (85, 35, 42)},
    4: {"name": "Gold-bronze", "hsl": (42, 70, 52)},
    5: {"name": "Sky blue-silver", "hsl": (200, 50, 60)},
}

# Shadow complement hues per Color (from archideck spec)
COLOR_SHADOW_HUES = {
    1: (0, 0), 2: (215, 10), 3: (30, 8), 4: (55, 8),
    5: (180, 10), 6: (210, 8), 7: (240, 8), 8: (0, 0),
}

# Cathedral register Order materials
ORDER_CATHEDRAL = {
    1: "Cave walls. Firelight on porous stone. The oldest rooms.",
    2: "Polished obsidian. Cool candlelight on dark mirror. Sharp reflections.",
    3: "Warm marble chapel. Votive candles in alcoves. Veining visible.",
    4: "Grand cathedral nave. Spotlit altar. Maximum drama.",
    5: "Crypt. Layered earth tones. Multiple lanterns. Organic warmth.",
    6: "Scriptorium. Even desk-lamp lighting. Precise, calibrated.",
    7: "Dimmed fresco chapel. Frescoes barely visible in candlelight. Serene.",
}

# Block sequence guidelines by Order
ORDER_BLOCK_SEQUENCES = {
    1: ["♨️", "🔢", "🛠", "🧈", "🧩", "🧬", "🚂", "🧮"],
    2: ["♨️", "▶️", "🧈", "🧩", "🪫", "🚂", "🧮"],
    3: ["♨️", "▶️", "🧈", "🗿", "🪞", "🧩", "🪫", "🚂", "🧮"],
    4: ["♨️", "🪜", "🧈", "🚂", "🧮"],
    5: ["♨️", "🎼", "🧈", "🧩", "🪫", "🚂", "🧮"],
    6: ["♨️", "🏗", "🧈", "🧩", "🪫", "🚂", "🧮"],
    7: ["🎯", "🪫", "🧈", "🧬", "🚂", "🧮"],
}

# CNS demand per Order
ORDER_CNS = {
    1: "low", 2: "high", 3: "moderate", 4: "high",
    5: "moderate", 6: "moderate", 7: "low",
}

ORDER_DIFFICULTY_MAX = {1: 2, 2: 4, 3: 3, 4: 5, 5: 3, 6: 3, 7: 2}

# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

_cache: Dict[str, Any] = {}


def _load_json(path: Path, key: str) -> Any:
    if key not in _cache:
        with open(path, "r", encoding="utf-8") as f:
            _cache[key] = json.load(f)
    return _cache[key]


def load_weight_vectors() -> Dict[str, dict]:
    return _load_json(WEIGHT_VECTORS_PATH, "wv")


def load_design_tokens() -> dict:
    return _load_json(DESIGN_TOKENS_PATH, "dt")


def load_zip_registry() -> List[dict]:
    return _load_json(ZIP_REGISTRY_PATH, "zr")


def load_nav_graph() -> Dict[str, dict]:
    return _load_json(NAV_GRAPH_PATH, "ng")


def load_abacus_index() -> dict:
    return _load_json(ABACUS_INDEX_PATH, "ai")


def _build_registry_lookup() -> Dict[str, dict]:
    """Build numeric_zip -> registry entry lookup."""
    if "zr_lookup" not in _cache:
        _cache["zr_lookup"] = {e["numeric_zip"]: e for e in load_zip_registry()}
    return _cache["zr_lookup"]


def _build_abacus_zip_map() -> Dict[int, dict]:
    """Build abacus_id -> {working: [...], bonus: [...]} lookup."""
    if "abacus_map" not in _cache:
        abacus_map = {}
        index = load_abacus_index()
        for profile in index["profiles"]:
            aid = profile["id"]
            slug = profile.get("slug", profile["name"].lower().replace(" ", "-").replace("/", "-"))
            profile_path = ABACUS_DIR / f"{slug}.json"
            if profile_path.exists():
                with open(profile_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                abacus_map[aid] = {
                    "name": profile["name"],
                    "slug": slug,
                    "domain": profile.get("domain", ""),
                    "axis_bias": profile.get("axis_bias", ""),
                    "working": data.get("zips", {}).get("working", []),
                    "bonus": [b["zip"] if isinstance(b, dict) else b
                              for b in data.get("zips", {}).get("bonus", [])],
                }
            else:
                abacus_map[aid] = {
                    "name": profile["name"], "slug": slug,
                    "domain": profile.get("domain", ""),
                    "axis_bias": profile.get("axis_bias", ""),
                    "working": [], "bonus": [],
                }
        _cache["abacus_map"] = abacus_map
    return _cache["abacus_map"]


# ---------------------------------------------------------------------------
# Color math utilities
# ---------------------------------------------------------------------------

def hsl_to_hex(h: float, s: float, l: float) -> str:
    """Convert HSL (h=0-360, s=0-100, l=0-100) to hex string."""
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"


def hex_to_hsl(hex_color: str) -> Tuple[float, float, float]:
    """Convert hex to (h, s, l) with h=0-360, s=0-100, l=0-100."""
    hex_color = hex_color.lstrip("#")
    r, g, b = int(hex_color[:2], 16) / 255, int(hex_color[2:4], 16) / 255, int(hex_color[4:6], 16) / 255
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return round(h * 360, 1), round(s * 100, 1), round(l * 100, 1)


def adjust_lightness(hex_color: str, delta: float) -> str:
    """Shift lightness by delta (positive = lighter)."""
    h, s, l = hex_to_hsl(hex_color)
    l = max(0, min(100, l + delta))
    return hsl_to_hex(h, s, l)


def adjust_saturation(hex_color: str, factor: float) -> str:
    """Multiply saturation by factor."""
    h, s, l = hex_to_hsl(hex_color)
    s = max(0, min(100, s * factor))
    return hsl_to_hex(h, s, l)


def shift_hue(hex_color: str, degrees: float) -> str:
    """Rotate hue by degrees."""
    h, s, l = hex_to_hsl(hex_color)
    h = (h + degrees) % 360
    return hsl_to_hex(h, s, l)


def contrast_ratio(hex1: str, hex2: str) -> float:
    """Compute WCAG contrast ratio between two hex colors."""
    def relative_luminance(hex_c: str) -> float:
        hex_c = hex_c.lstrip("#")
        r, g, b = int(hex_c[:2], 16) / 255, int(hex_c[2:4], 16) / 255, int(hex_c[4:6], 16) / 255
        vals = []
        for c in (r, g, b):
            vals.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
        return 0.2126 * vals[0] + 0.7152 * vals[1] + 0.0722 * vals[2]

    l1 = relative_luminance(hex1)
    l2 = relative_luminance(hex2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def ensure_contrast(fg: str, bg: str, minimum: float = 4.5) -> str:
    """Adjust foreground lightness until contrast meets minimum."""
    ratio = contrast_ratio(fg, bg)
    if ratio >= minimum:
        return fg
    h, s, l = hex_to_hsl(fg)
    bg_h, bg_s, bg_l = hex_to_hsl(bg)
    # Determine direction: if bg is dark, lighten fg; if bg is light, darken fg
    direction = 1 if bg_l < 50 else -1
    for _ in range(80):
        l = l + direction * 2
        l = max(5, min(95, l))
        candidate = hsl_to_hex(h, s, l)
        if contrast_ratio(candidate, bg) >= minimum:
            return candidate
    return hsl_to_hex(h, s, l)


# ---------------------------------------------------------------------------
# Cosine similarity
# ---------------------------------------------------------------------------

def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Cosine similarity between two vectors."""
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x * x for x in a))
    mag_b = math.sqrt(sum(x * x for x in b))
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot / (mag_a * mag_b)


def vector_centroid(vectors: List[List[float]]) -> List[float]:
    """Element-wise mean of vectors."""
    if not vectors:
        return [0.0] * 61
    n = len(vectors)
    dims = len(vectors[0])
    return [sum(v[i] for v in vectors) / n for i in range(dims)]


def vector_magnitude(v: List[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


# ---------------------------------------------------------------------------
# Zip parsing
# ---------------------------------------------------------------------------

_EMOJI_TO_ORDER = {v[0]: k for k, v in ORDERS.items()}
_EMOJI_TO_AXIS = {v[0]: k for k, v in AXES.items()}
_EMOJI_TO_TYPE = {v[0]: k for k, v in TYPES.items()}
_EMOJI_TO_COLOR = {v[0]: k for k, v in COLORS.items()}


def parse_zip(zip_code: str) -> Tuple[int, int, int, int]:
    """Parse a zip code (emoji or numeric) into (order, axis, type, color) positions."""
    zip_code = zip_code.strip()
    if zip_code.isdigit() and len(zip_code) == 4:
        return int(zip_code[0]), int(zip_code[1]), int(zip_code[2]), int(zip_code[3])
    # Emoji parsing
    chars = list(zip_code)
    emojis = []
    i = 0
    while i < len(chars):
        # Handle multi-char emojis (variation selectors, ZWJ)
        emoji = chars[i]
        while i + 1 < len(chars) and chars[i + 1] in ('\ufe0e', '\ufe0f', '\u200d', '\u20e3'):
            i += 1
            emoji += chars[i]
            if chars[i] == '\u200d' and i + 1 < len(chars):
                i += 1
                emoji += chars[i]
        emojis.append(emoji)
        i += 1
    # Filter to known emojis
    known = []
    for e in emojis:
        base = e.rstrip('\ufe0e\ufe0f')
        if base in _EMOJI_TO_ORDER or base in _EMOJI_TO_AXIS or base in _EMOJI_TO_TYPE or base in _EMOJI_TO_COLOR:
            known.append(base)
    if len(known) < 4:
        raise ValueError(f"Cannot parse zip code: {zip_code!r} (found {len(known)} known emojis: {known})")
    return (
        _EMOJI_TO_ORDER.get(known[0], 0),
        _EMOJI_TO_AXIS.get(known[1], 0),
        _EMOJI_TO_TYPE.get(known[2], 0),
        _EMOJI_TO_COLOR.get(known[3], 0),
    )


def numeric_zip(order: int, axis: int, type_: int, color: int) -> str:
    return f"{order}{axis}{type_}{color}"


def emoji_zip(order: int, axis: int, type_: int, color: int) -> str:
    return f"{ORDERS[order][0]}{AXES[axis][0]}{TYPES[type_][0]}{COLORS[color][0]}"


def derive_operator(axis_pos: int, color_pos: int) -> Tuple[str, str]:
    """Derive operator (emoji, name) from axis × color polarity."""
    axis_emoji = AXES[axis_pos][0]
    color_polarity = COLORS[color_pos][5]  # "preparatory" or "expressive"
    prep, expr = OPERATOR_TABLE[axis_emoji]
    return prep if color_polarity == "preparatory" else expr


def zip_to_deck(order: int, axis: int) -> int:
    return (order - 1) * 6 + axis


# ---------------------------------------------------------------------------
# Operator profiles (from weight vectors — dims 49-60)
# ---------------------------------------------------------------------------

def _build_operator_profiles() -> Dict[str, List[float]]:
    """Build average weight profiles per operator from all 1,680 vectors."""
    if "op_profiles" not in _cache:
        wv = load_weight_vectors()
        reg = _build_registry_lookup()
        op_vectors: Dict[str, List[List[float]]] = {}
        for nzip, entry in wv.items():
            reg_entry = reg.get(nzip)
            if reg_entry:
                op_emoji = reg_entry["operator"]["emoji"]
                op_vectors.setdefault(op_emoji, []).append(entry["vector"])
        _cache["op_profiles"] = {
            op: vector_centroid(vecs) for op, vecs in op_vectors.items()
        }
    return _cache["op_profiles"]


# ---------------------------------------------------------------------------
# Palette generation
# ---------------------------------------------------------------------------

def _generate_light_palette(color_pos: int, order_pos: int, tokens: dict) -> dict:
    """Generate watercolor (light) register palette."""
    color_info = COLORS[color_pos]
    color_slug = color_info[2]
    color_tokens = tokens["colors"].get(color_slug, tokens["colors"]["structured"])

    # Base saturation interaction (Order × Color)
    sat_table = {
        (5, 2): 0.9, (8, 7): 0.2, (7, 3): 0.75, (1, 0): 0.05,
    }
    # Default: use color position to derive saturation
    base_sat = 0.6 + (color_pos - 1) * 0.04  # Range ~0.6 to ~0.88
    # Specific overrides
    if color_pos == 5 and order_pos == 2:  # 🔴 + ⛽
        base_sat = 0.9
    elif color_pos == 8 and order_pos == 7:  # ⚪ + 🖼
        base_sat = 0.2
    elif color_pos == 1:  # ⚫ always desaturated
        base_sat = 0.05

    primary_hsl = hex_to_hsl(color_tokens["primary"])
    cr = contrast_ratio(color_tokens.get("textOnLight", color_tokens["text"]),
                        color_tokens["background"])

    return {
        "name": "watercolor",
        "philosophy": "Transparent glazed layers over a bright ground. Selective saturation. Paper showing through.",
        "primary": color_tokens["primary"],
        "secondary": color_tokens["secondary"],
        "background": color_tokens["background"],
        "surface": color_tokens["surface"],
        "text": color_tokens.get("textOnLight", color_tokens["text"]),
        "accent": color_tokens["accent"],
        "border": color_tokens["border"],
        "type_accent": None,  # Filled by caller
        "operator_tint": None,  # Filled by caller
        "saturation_level": round(base_sat, 3),
        "contrast_ratio": round(cr, 1),
    }


def _generate_cathedral_palette(color_pos: int, order_pos: int, tokens: dict) -> dict:
    """Generate cathedral (dark) register palette from the watercolor palette."""
    color_info = COLORS[color_pos]
    color_slug = color_info[2]
    color_tokens = tokens["colors"].get(color_slug, tokens["colors"]["structured"])
    material = ORDER_MATERIALS[order_pos]

    # Background: dark stone tinted by Order material
    bg_hue = material["hue"]
    bg_sat = max(material["sat"] * 0.5, 2)
    bg = hsl_to_hex(bg_hue, bg_sat, 7)
    surface = hsl_to_hex(bg_hue, bg_sat, 10)

    # Primary: shift toward warm, lighten for glow
    primary = shift_hue(color_tokens["primary"], 10)
    primary = adjust_lightness(primary, 15)

    # Text: warm parchment
    text = hsl_to_hex(35, 15, 82)

    # Accent: gilded shift
    accent = shift_hue(color_tokens["accent"], 15)
    accent = adjust_lightness(accent, 10)
    accent = adjust_saturation(accent, 0.8)

    # Border: stone joints
    border = hsl_to_hex(bg_hue, bg_sat + 3, 15)

    # Ensure WCAG AA
    text = ensure_contrast(text, bg, 4.5)
    primary = ensure_contrast(primary, bg, 3.0)

    # Saturation: reduced from light register
    light_sat = 0.6 + (color_pos - 1) * 0.04
    if color_pos == 1:
        light_sat = 0.05
    dark_sat = round(light_sat * 0.65, 3)

    cr = contrast_ratio(text, bg)

    return {
        "name": "cathedral",
        "philosophy": "Warm pools of light on dark surfaces. Selective illumination. Stone walls absorbing candlelight.",
        "cathedral_character": ORDER_CATHEDRAL.get(order_pos, ""),
        "primary": primary,
        "secondary": adjust_lightness(primary, -5),
        "background": bg,
        "surface": surface,
        "text": text,
        "accent": accent,
        "border": border,
        "type_accent": None,
        "operator_tint": None,
        "saturation_level": dark_sat,
        "contrast_ratio": round(cr, 1),
    }


def _color_wheel_info(color_pos: int, tokens: dict) -> dict:
    """Color theory analysis of the active Color."""
    color_slug = COLORS[color_pos][2]
    color_tokens = tokens["colors"].get(color_slug, tokens["colors"]["structured"])
    h, s, l = hex_to_hsl(color_tokens["primary"])
    return {
        "hue": h, "saturation": s, "lightness": l,
        "complement_hue": (h + 180) % 360,
        "split_complements": [(h + 150) % 360, (h + 210) % 360],
        "analogous": [(h + 30) % 360, (h - 30) % 360],
    }


# ---------------------------------------------------------------------------
# Register suggestion
# ---------------------------------------------------------------------------

def suggest_register(order_pos: int, color_pos: int, hour: int = 12) -> str:
    """Suggest cathedral or watercolor based on zip + time of day."""
    time_bias = 0.0
    if hour >= 20 or hour < 6:
        time_bias = 0.4
    elif hour >= 17:
        time_bias = 0.2

    color_bias = {5: 0.3, 4: 0.25, 8: 0.15, 1: 0.1}.get(color_pos, 0) - \
                 {2: 0.3, 7: 0.25, 6: 0.15, 3: 0.1}.get(color_pos, 0)

    order_bias = {2: 0.15, 4: 0.2, 1: -0.15, 7: -0.1}.get(order_pos, 0)

    total = time_bias + color_bias + order_bias
    if total > 0.2:
        return "cathedral"
    elif total < -0.2:
        return "watercolor"
    return "user_preference"


# ---------------------------------------------------------------------------
# Guild alignment
# ---------------------------------------------------------------------------

def resolve_guild_alignment(vector: List[float]) -> dict:
    """Compute cosine similarity between vector and all 12 operator profiles."""
    profiles = _build_operator_profiles()
    sims = {}
    for op_emoji, op_vec in profiles.items():
        sims[op_emoji] = cosine_similarity(vector, op_vec)

    ranked = sorted(sims.items(), key=lambda x: x[1], reverse=True)

    def _entry(item):
        emoji, sim = item
        return {
            "emoji": emoji,
            "name": next((OPERATOR_TABLE[a][0][1] if OPERATOR_TABLE[a][0][0] == emoji
                          else OPERATOR_TABLE[a][1][1]
                          for a in OPERATOR_TABLE
                          if OPERATOR_TABLE[a][0][0] == emoji or OPERATOR_TABLE[a][1][0] == emoji), "unknown"),
            "guild": OPERATOR_HOUSES.get(emoji, "Unknown"),
            "similarity": round(sim, 4),
        }

    return {
        "primary": _entry(ranked[0]),
        "secondary": _entry(ranked[1]),
        "tertiary": _entry(ranked[2]),
        "anti": _entry(ranked[-1]),
    }


# ---------------------------------------------------------------------------
# Abacus membership
# ---------------------------------------------------------------------------

def find_abacus_memberships(nzip: str) -> List[dict]:
    """Find which abaci contain this zip code."""
    abacus_map = _build_abacus_zip_map()
    memberships = []
    for aid, data in abacus_map.items():
        if nzip in data["working"]:
            slot_num = data["working"].index(nzip) + 1
            memberships.append({
                "id": aid, "name": data["name"], "domain": data["domain"],
                "slot": "working", "slot_number": slot_num,
            })
        elif nzip in data["bonus"]:
            memberships.append({
                "id": aid, "name": data["name"], "domain": data["domain"],
                "slot": "bonus", "bonus_role": "variety",
            })
    return memberships


# ---------------------------------------------------------------------------
# Core resolution
# ---------------------------------------------------------------------------

def resolve_zip(zip_code: str, register: str = "auto", hour: int = 12) -> dict:
    """Resolve a single zip code into the full resolution object."""
    order, axis, type_, color = parse_zip(zip_code)
    nzip = numeric_zip(order, axis, type_, color)
    ezip = emoji_zip(order, axis, type_, color)
    op_emoji, op_name = derive_operator(axis, color)
    deck = zip_to_deck(order, axis)

    tokens = load_design_tokens()
    wv = load_weight_vectors()
    nav = load_nav_graph()

    vector = wv.get(nzip, {}).get("vector", [0] * 61)

    # -- Address --
    address = {
        "zip_emoji": ezip,
        "zip_numeric": nzip,
        "order": {"emoji": ORDERS[order][0], "name": ORDERS[order][1],
                  "index": order - 1, "classical": ORDERS[order][3]},
        "axis": {"emoji": AXES[axis][0], "name": AXES[axis][1],
                 "index": axis - 1, "latin": AXES[axis][3]},
        "type": {"emoji": TYPES[type_][0], "name": TYPES[type_][1],
                 "index": type_ - 1, "muscles": TYPES[type_][3]},
        "color": {"emoji": COLORS[color][0], "name": COLORS[color][1],
                  "index": color - 1, "tier": COLORS[color][3],
                  "gold": COLORS[color][4], "polarity": COLORS[color][5]},
        "operator": {"emoji": op_emoji, "name": op_name,
                     "house": OPERATOR_HOUSES.get(op_emoji, "Unknown")},
        "deck": deck,
        "url": f"/zip/{nzip}",
    }

    # -- Architecture (D-module) --
    material = ORDER_MATERIALS[order]
    atmosphere = AXIS_ATMOSPHERES[axis]
    icol = ORDER_INTERCOLUMNIATION[order]
    d_val = ORDER_D_VALUES[order]

    architecture = {
        "D": d_val,
        "column_ratio": ORDER_COLUMN_RATIOS[order],
        "intercolumniation": icol,
        "superposition": AXIS_SUPERPOSITION[axis],
        "line_multiplier": ORDER_LINE_MULTIPLIERS[order],
        "material": material,
        "atmosphere": {
            "name": atmosphere["name"],
            "brightness": atmosphere["brightness"],
            "hue_shift": atmosphere["hue_shift"],
            "sat_multiplier": atmosphere["sat_mult"],
            "warmth_modifier": atmosphere["warmth"],
        },
        "shadow": {
            "depth_multiplier": ORDER_LINE_MULTIPLIERS[order],
            "hue": COLOR_SHADOW_HUES[color][0],
            "saturation": COLOR_SHADOW_HUES[color][1],
            "character": material["shadow"],
        },
    }

    # -- Palette (dual register) --
    light = _generate_light_palette(color, order, tokens)
    dark = _generate_cathedral_palette(color, order, tokens)

    # Apply type accent and operator tint
    type_acc = TYPE_ACCENTS[type_]
    type_accent_hex = hsl_to_hex(*type_acc["hsl"])
    op_tint = OPERATOR_TINTS.get(op_emoji, {"hsl": (0, 0, 50)})
    op_tint_hex = hsl_to_hex(*op_tint["hsl"])

    light["type_accent"] = type_accent_hex
    light["operator_tint"] = op_tint_hex
    dark["type_accent"] = adjust_lightness(type_accent_hex, 15)
    dark["operator_tint"] = adjust_lightness(op_tint_hex, 20)

    if register == "auto":
        register = suggest_register(order, color, hour)

    palette = {
        "active_register": register,
        "light_register": light,
        "dark_register": dark,
        "color_wheel": _color_wheel_info(color, tokens),
    }

    # -- Typography --
    order_tokens = tokens["orders"].get(ORDERS[order][2], tokens["orders"]["strength"])
    typography = {
        "font_family": tokens["typography"]["fontFamily"]["body"],
        "font_character": atmosphere["typography"],
        "body_size": order_tokens["fontSizeBase"],
        "display_size": order_tokens["fontSizeDisplay"],
        "font_weight_body": order_tokens["fontWeight"],
        "font_weight_display": order_tokens["fontWeightDisplay"],
        "letter_spacing": order_tokens["letterSpacing"],
        "line_height": order_tokens["lineHeight"],
        "density": order_tokens["density"],
        "tonal_register": {
            "name": COLORS[color][2],
            "character": order_tokens.get("uiNote", ""),
        },
    }

    # -- Personality --
    guild = resolve_guild_alignment(vector)
    abacus_memberships = find_abacus_memberships(nzip)

    personality = {
        "house": guild,
        "neighborhood": {
            "abacus_memberships": abacus_memberships,
            "primary_abacus": abacus_memberships[0] if abacus_memberships else None,
        },
        "city_position": {
            "building": f"{ORDERS[order][1]} Hall ({ORDERS[order][3]})",
            "floor": f"{AXES[axis][3]} ({AXES[axis][1]})",
            "wing": f"{TYPES[type_][1]} Wing",
            "room": f"{COLORS[color][1]} Room",
        },
        "difficulty_class": ORDER_DIFFICULTY_MAX[order],
        "cns_demand": ORDER_CNS[order],
    }

    # -- Connections --
    nav_entry = nav.get(nzip, {})
    # Find zips in same deck (same order × axis)
    same_deck = [numeric_zip(order, axis, t, c)
                 for t in range(1, 6) for c in range(1, 9)
                 if not (t == type_ and c == color)]

    # Nearest by cosine similarity (top 5)
    all_vecs = load_weight_vectors()
    sims = []
    for other_nzip, other_entry in all_vecs.items():
        if other_nzip != nzip:
            sim = cosine_similarity(vector, other_entry["vector"])
            sims.append((other_nzip, sim))
    sims.sort(key=lambda x: x[1], reverse=True)
    nearest_5 = [s[0] for s in sims[:5]]
    farthest = sims[-1][0] if sims else None

    connections = {
        "navigation": nav_entry,
        "same_deck_zips": len(same_deck),
        "junction_suggestions": nearest_5[:3],
        "abacus_membership": abacus_memberships,
        "cosine_nearest_5": nearest_5,
        "cosine_farthest": farthest,
    }

    # -- Metadata --
    # Check card status
    reg_entry = _build_registry_lookup().get(nzip, {})
    card_path = reg_entry.get("card_path", "")

    metadata = {
        "deck": deck,
        "deck_name": f"{ORDERS[order][0]}{AXES[axis][0]} {ORDERS[order][1]} {AXES[axis][1]}",
        "operator_default": {"emoji": op_emoji, "name": op_name},
        "block_sequence": ORDER_BLOCK_SEQUENCES.get(order, []),
        "block_count": len(ORDER_BLOCK_SEQUENCES.get(order, [])),
        "weight_vector": vector,
        "vector_magnitude": round(vector_magnitude(vector), 2),
    }

    return {
        "address": address,
        "architecture": architecture,
        "palette": palette,
        "typography": typography,
        "personality": personality,
        "connections": connections,
        "metadata": metadata,
    }


# ---------------------------------------------------------------------------
# Deck resolution (macro aggregation)
# ---------------------------------------------------------------------------

def resolve_deck(deck_number: int) -> dict:
    """Resolve a deck (42 possible) by computing centroid of its 40 constituent zips."""
    order = (deck_number - 1) // 6 + 1
    axis = (deck_number - 1) % 6 + 1

    wv = load_weight_vectors()
    vectors = []
    zips = []
    for t in range(1, 6):
        for c in range(1, 9):
            nzip = numeric_zip(order, axis, t, c)
            entry = wv.get(nzip)
            if entry:
                vectors.append(entry["vector"])
                zips.append(nzip)

    centroid = vector_centroid(vectors)
    spread = _vector_std(vectors)

    # Resolve the centroid through the same pipeline
    tokens = load_design_tokens()
    guild = resolve_guild_alignment(centroid)

    return {
        "deck_number": deck_number,
        "order": {"emoji": ORDERS[order][0], "name": ORDERS[order][1], "classical": ORDERS[order][3]},
        "axis": {"emoji": AXES[axis][0], "name": AXES[axis][1], "latin": AXES[axis][3]},
        "deck_name": f"{ORDERS[order][0]}{AXES[axis][0]} {ORDERS[order][1]} {AXES[axis][1]}",
        "constituent_count": len(vectors),
        "centroid": [round(v, 3) for v in centroid],
        "centroid_magnitude": round(vector_magnitude(centroid), 2),
        "vector_spread": round(spread, 3),
        "guild_affinity": guild,
        "architecture": {
            "D": ORDER_D_VALUES[order],
            "column_ratio": ORDER_COLUMN_RATIOS[order],
            "intercolumniation": ORDER_INTERCOLUMNIATION[order],
            "material": ORDER_MATERIALS[order],
            "atmosphere": AXIS_ATMOSPHERES[axis]["name"],
            "line_multiplier": ORDER_LINE_MULTIPLIERS[order],
        },
        "zips": zips,
    }


def _vector_std(vectors: List[List[float]]) -> float:
    """Average standard deviation across all dimensions."""
    if not vectors:
        return 0.0
    n = len(vectors)
    dims = len(vectors[0])
    total_std = 0.0
    for d in range(dims):
        vals = [v[d] for v in vectors]
        mean = sum(vals) / n
        variance = sum((x - mean) ** 2 for x in vals) / n
        total_std += math.sqrt(variance)
    return total_std / dims


# ---------------------------------------------------------------------------
# Abacus resolution (macro aggregation)
# ---------------------------------------------------------------------------

def resolve_abacus(abacus_id: int) -> dict:
    """Resolve an abacus (35 possible) by computing centroid of its constituent zips."""
    abacus_map = _build_abacus_zip_map()
    ab = abacus_map.get(abacus_id)
    if not ab:
        return {"error": f"Abacus {abacus_id} not found"}

    wv = load_weight_vectors()
    all_zips = ab["working"] + ab["bonus"]
    vectors = []
    for nzip in all_zips:
        entry = wv.get(nzip)
        if entry:
            vectors.append(entry["vector"])

    centroid = vector_centroid(vectors)
    spread = _vector_std(vectors)
    guild = resolve_guild_alignment(centroid)

    # Order/Color distribution
    order_dist = {}
    color_dist = {}
    for nzip in all_zips:
        o, a, t, c = int(nzip[0]), int(nzip[1]), int(nzip[2]), int(nzip[3])
        order_dist[ORDERS[o][1]] = order_dist.get(ORDERS[o][1], 0) + 1
        color_dist[COLORS[c][1]] = color_dist.get(COLORS[c][1], 0) + 1

    return {
        "abacus_id": abacus_id,
        "name": ab["name"],
        "slug": ab["slug"],
        "domain": ab["domain"],
        "axis_bias": ab["axis_bias"],
        "constituent_count": len(vectors),
        "working_count": len(ab["working"]),
        "bonus_count": len(ab["bonus"]),
        "centroid": [round(v, 3) for v in centroid],
        "centroid_magnitude": round(vector_magnitude(centroid), 2),
        "vector_spread": round(spread, 3),
        "guild_affinity": guild,
        "order_distribution": order_dist,
        "color_distribution": color_dist,
        "zips_working": ab["working"],
        "zips_bonus": ab["bonus"],
    }


# ---------------------------------------------------------------------------
# Full city compilation
# ---------------------------------------------------------------------------

def compile_city() -> dict:
    """Compile the entire city: all 1,680 zips + 42 decks + 35 abaci."""
    print("Compiling city...")

    # Deck centroids
    print("  Computing 42 deck centroids...")
    deck_centroids = {}
    for d in range(1, 43):
        resolved = resolve_deck(d)
        deck_centroids[d] = resolved
    print(f"  ✓ {len(deck_centroids)} decks resolved")

    # Abacus centroids
    print("  Computing 35 abacus centroids...")
    abacus_centroids = {}
    abacus_map = _build_abacus_zip_map()
    for aid in sorted(abacus_map.keys()):
        resolved = resolve_abacus(aid)
        if "error" not in resolved:
            abacus_centroids[aid] = resolved
    print(f"  ✓ {len(abacus_centroids)} abaci resolved")

    # Guild halls (zip most similar to each operator profile)
    print("  Finding 12 guild halls...")
    op_profiles = _build_operator_profiles()
    wv = load_weight_vectors()
    guild_halls = {}
    for op_emoji, op_vec in op_profiles.items():
        best_zip = None
        best_sim = -1
        for nzip, entry in wv.items():
            sim = cosine_similarity(op_vec, entry["vector"])
            if sim > best_sim:
                best_sim = sim
                best_zip = nzip
        guild_halls[op_emoji] = {
            "zip": best_zip,
            "similarity": round(best_sim, 4),
            "house": OPERATOR_HOUSES.get(op_emoji, "Unknown"),
        }
    print(f"  ✓ {len(guild_halls)} guild halls found")

    # City centroid
    all_vecs = [entry["vector"] for entry in wv.values()]
    city_centroid = vector_centroid(all_vecs)

    return {
        "city": {
            "total_rooms": len(wv),
            "buildings": 7,
            "floors": 6,
            "wings": 5,
            "rooms_per_wing": 8,
            "districts": 42,
            "neighborhoods": len(abacus_centroids),
            "guilds": len(guild_halls),
            "centroid": [round(v, 3) for v in city_centroid],
        },
        "guild_halls": guild_halls,
        "deck_centroids": {str(k): {
            "deck_number": v["deck_number"],
            "deck_name": v["deck_name"],
            "centroid_magnitude": v["centroid_magnitude"],
            "vector_spread": v["vector_spread"],
            "guild_primary": v["guild_affinity"]["primary"]["guild"],
        } for k, v in deck_centroids.items()},
        "abacus_centroids": {str(k): {
            "name": v["name"],
            "domain": v["domain"],
            "centroid_magnitude": v["centroid_magnitude"],
            "vector_spread": v["vector_spread"],
            "guild_primary": v["guild_affinity"]["primary"]["guild"],
        } for k, v in abacus_centroids.items()},
    }


# ---------------------------------------------------------------------------
# CSS output
# ---------------------------------------------------------------------------

def resolution_to_css(resolution: dict) -> str:
    """Convert a resolution object to CSS custom properties."""
    arch = resolution["architecture"]
    pal = resolution["palette"]
    typo = resolution["typography"]

    register = pal["active_register"]
    if register in ("cathedral", "user_preference"):
        active_pal = pal["dark_register"]
    else:
        active_pal = pal["light_register"]

    lines = [
        f"/* City Compiler — {resolution['address']['zip_emoji']} ({resolution['address']['zip_numeric']}) */",
        f"/* Register: {register} */",
        "",
        ":root {",
        f"  /* === MODULE === */",
        f"  --ppl-D: {arch['D']};",
        f"  --ppl-column-ratio: {arch['column_ratio']};",
        f"  --ppl-intercolumniation: {arch['intercolumniation']};",
        f"  --ppl-superposition: {arch['superposition']};",
        f"  --ppl-line-multiplier: {arch['line_multiplier']};",
        "",
        f"  /* === MATERIAL (Order: {resolution['address']['order']['classical']}) === */",
        f"  --ppl-material-hue: {arch['material']['hue']};",
        f"  --ppl-material-sat: {arch['material']['sat']}%;",
        f"  --ppl-material-warmth: {arch['material']['warmth']};",
        "",
        f"  /* === THEME (Color: {resolution['address']['color']['name']}) === */",
        f"  --ppl-theme-primary: {active_pal['primary']};",
        f"  --ppl-theme-secondary: {active_pal['secondary']};",
        f"  --ppl-theme-background: {active_pal['background']};",
        f"  --ppl-theme-surface: {active_pal['surface']};",
        f"  --ppl-theme-text: {active_pal['text']};",
        f"  --ppl-theme-accent: {active_pal['accent']};",
        f"  --ppl-theme-border: {active_pal['border']};",
        f"  --ppl-weight-saturation: {active_pal['saturation_level']};",
        f"  --ppl-weight-contrast: {active_pal['contrast_ratio']};",
        "",
        f"  /* === SHADOW === */",
        f"  --ppl-shadow-hue: {arch['shadow']['hue']};",
        f"  --ppl-shadow-sat: {arch['shadow']['saturation']}%;",
        f"  --ppl-shadow-depth: {arch['shadow']['depth_multiplier']};",
        "",
        f"  /* === TYPOGRAPHY === */",
        f"  --ppl-font-family: {typo['font_family']};",
        f"  --ppl-font-size-body: {typo['body_size']};",
        f"  --ppl-font-size-display: {typo['display_size']};",
        f"  --ppl-font-weight-body: {typo['font_weight_body']};",
        f"  --ppl-font-weight-display: {typo['font_weight_display']};",
        f"  --ppl-letter-spacing: {typo['letter_spacing']};",
        f"  --ppl-line-height: {typo['line_height']};",
        "",
        f"  /* === TYPE ACCENT === */",
        f"  --ppl-type-accent: {active_pal['type_accent']};",
        f"  --ppl-operator-tint: {active_pal['operator_tint']};",
        "}",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Summary output
# ---------------------------------------------------------------------------

def resolution_to_summary(resolution: dict) -> str:
    """Human-readable summary of a resolution."""
    a = resolution["address"]
    arch = resolution["architecture"]
    pal = resolution["palette"]
    pers = resolution["personality"]
    conn = resolution["connections"]
    meta = resolution["metadata"]

    lines = [
        f"╔══════════════════════════════════════════════════════╗",
        f"║  {a['zip_emoji']}  ({a['zip_numeric']})  —  Deck {a['deck']}",
        f"╚══════════════════════════════════════════════════════╝",
        "",
        f"  Order:    {a['order']['emoji']} {a['order']['name']} ({a['order']['classical']})",
        f"  Axis:     {a['axis']['emoji']} {a['axis']['name']} ({a['axis']['latin']})",
        f"  Type:     {a['type']['emoji']} {a['type']['name']} — {', '.join(a['type']['muscles'])}",
        f"  Color:    {a['color']['emoji']} {a['color']['name']} | Tier {a['color']['tier']} | GOLD: {'Yes' if a['color']['gold'] else 'No'}",
        f"  Operator: {a['operator']['emoji']} {a['operator']['name']} ({a['operator']['house']})",
        "",
        f"  ── Architecture ──",
        f"  D: {arch['D']}  |  Column ratio: {arch['column_ratio']}D  |  Intercolumniation: {arch['intercolumniation']}D",
        f"  Material: {arch['material']['name']}  |  Line weight: ×{arch['line_multiplier']}",
        f"  Atmosphere: {arch['atmosphere']['name']}  |  Superposition: {arch['superposition']}",
        "",
        f"  ── Palette ──",
        f"  Register: {pal['active_register']}",
        f"  Light: {pal['light_register']['primary']} on {pal['light_register']['background']} (CR: {pal['light_register']['contrast_ratio']}:1)",
        f"  Dark:  {pal['dark_register']['primary']} on {pal['dark_register']['background']} (CR: {pal['dark_register']['contrast_ratio']}:1)",
        "",
        f"  ── Personality ──",
        f"  Guild: {pers['house']['primary']['emoji']} {pers['house']['primary']['guild']} ({pers['house']['primary']['similarity']})",
        f"  CNS: {pers['cns_demand']}  |  Difficulty: {pers['difficulty_class']}/5",
    ]

    if pers["neighborhood"]["primary_abacus"]:
        pa = pers["neighborhood"]["primary_abacus"]
        lines.append(f"  Neighborhood: {pa['name']} ({pa['domain']})")

    lines.append("")
    lines.append(f"  ── Connections ──")
    lines.append(f"  Nearest 5: {', '.join(conn['cosine_nearest_5'])}")
    lines.append(f"  Farthest:  {conn['cosine_farthest']}")
    lines.append(f"  Abacus memberships: {len(conn['abacus_membership'])}")
    lines.append("")
    lines.append(f"  ── Metadata ──")
    lines.append(f"  Blocks: {' → '.join(meta['block_sequence'])}")
    lines.append(f"  Vector magnitude: {meta['vector_magnitude']}")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_all() -> dict:
    """Resolve all 1,680 zips and check for consistency."""
    wv = load_weight_vectors()
    errors = []
    warnings = []

    print(f"Validating {len(wv)} zip codes...")

    for i, nzip in enumerate(sorted(wv.keys())):
        try:
            res = resolve_zip(nzip, register="watercolor")

            # Check WCAG contrast
            light_cr = res["palette"]["light_register"]["contrast_ratio"]
            dark_cr = res["palette"]["dark_register"]["contrast_ratio"]
            if light_cr < 4.5:
                warnings.append(f"{nzip}: light register contrast {light_cr}:1 < 4.5:1")
            if dark_cr < 4.5:
                warnings.append(f"{nzip}: dark register contrast {dark_cr}:1 < 4.5:1")

            # Check vector exists
            if not res["metadata"]["weight_vector"] or all(v == 0 for v in res["metadata"]["weight_vector"]):
                errors.append(f"{nzip}: zero/missing weight vector")

        except Exception as e:
            errors.append(f"{nzip}: {e}")

        if (i + 1) % 200 == 0:
            print(f"  {i + 1}/{len(wv)}...")

    print(f"\n  ✓ {len(wv)} zips resolved")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")

    if errors:
        print("\n  ERRORS:")
        for e in errors[:20]:
            print(f"    ✗ {e}")
    if warnings:
        print(f"\n  WARNINGS (showing first 20 of {len(warnings)}):")
        for w in warnings[:20]:
            print(f"    ⚠ {w}")

    return {"total": len(wv), "errors": len(errors), "warnings": len(warnings)}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="City Compiler — SCL Universal Resolution Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python city_compiler.py ⛽🏛🪡🔵           Resolve a zip (emoji)
  python city_compiler.py 2123                Resolve a zip (numeric)
  python city_compiler.py --deck 7            Resolve a deck
  python city_compiler.py --abacus 1          Resolve an abacus
  python city_compiler.py --city              Compile full city
  python city_compiler.py 2123 --format css   Output as CSS
  python city_compiler.py 2123 --format summary  Human-readable
  python city_compiler.py --validate          Validate all 1,680
        """,
    )

    parser.add_argument("zip_code", nargs="?", help="Zip code (emoji or numeric)")
    parser.add_argument("--deck", type=int, help="Resolve deck by number (1-42)")
    parser.add_argument("--abacus", type=int, help="Resolve abacus by ID (1-35)")
    parser.add_argument("--city", action="store_true", help="Compile full city")
    parser.add_argument("--validate", action="store_true", help="Validate all 1,680 zips")
    parser.add_argument("--format", choices=["json", "css", "summary"], default="json",
                        help="Output format (default: json)")
    parser.add_argument("--register", choices=["cathedral", "watercolor", "auto"],
                        default="auto", help="Dark/light register (default: auto)")
    parser.add_argument("--hour", type=int, default=12,
                        help="Hour of day for auto register suggestion (0-23)")
    parser.add_argument("--write", action="store_true",
                        help="Write compiled output to middle-math/compiled/")

    args = parser.parse_args()

    if args.validate:
        result = validate_all()
        if args.format == "json":
            print(json.dumps(result, indent=2))
        return

    if args.city:
        result = compile_city()
        if args.write:
            COMPILED_DIR.mkdir(parents=True, exist_ok=True)
            out_path = COMPILED_DIR / "city-compilation.json"
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            print(f"  Written to {out_path}")
        else:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    if args.deck:
        result = resolve_deck(args.deck)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    if args.abacus:
        result = resolve_abacus(args.abacus)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    if args.zip_code:
        result = resolve_zip(args.zip_code, register=args.register, hour=args.hour)
        if args.format == "css":
            print(resolution_to_css(result))
        elif args.format == "summary":
            print(resolution_to_summary(result))
        else:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    parser.print_help()


if __name__ == "__main__":
    main()
