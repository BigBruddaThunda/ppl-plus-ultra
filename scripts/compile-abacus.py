#!/usr/bin/env python3
"""compile-abacus.py — Assign 48 zip codes to each of 35 training archetypes.

Usage:
    python scripts/compile-abacus.py              # compile + write JSON + report
    python scripts/compile-abacus.py --stats       # report from existing JSON
    python scripts/compile-abacus.py --dry-run     # compile + report, skip JSON write
    python scripts/compile-abacus.py --report      # compile + write JSON + markdown report
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = REPO_ROOT / "middle-math" / "zip-registry.json"
OUTPUT_PATH = REPO_ROOT / "middle-math" / "abacus-registry.json"

# ---------------------------------------------------------------------------
# SCL constants (mirrors zip_converter.py)
# ---------------------------------------------------------------------------
ORDER_EMOJIS = ["🐂", "⛽", "🦋", "🏟", "🌾", "⚖", "🖼"]
AXIS_EMOJIS = ["🏛", "🔨", "🌹", "🪐", "⌛", "🐬"]
TYPE_EMOJIS = ["🛒", "🪡", "🍗", "➕", "➖"]
COLOR_EMOJIS = ["⚫", "🟢", "🔵", "🟣", "🔴", "🟠", "🟡", "⚪"]

ORDER_NAMES = {
    "🐂": "Foundation", "⛽": "Strength", "🦋": "Hypertrophy",
    "🏟": "Performance", "🌾": "Full Body", "⚖": "Balance", "🖼": "Restoration",
}
AXIS_NAMES = {
    "🏛": "Basics", "🔨": "Functional", "🌹": "Aesthetic",
    "🪐": "Challenge", "⌛": "Time", "🐬": "Partner",
}

GOLD_COLORS = {"🟣", "🔴"}

# ---------------------------------------------------------------------------
# 35 Archetype Definitions
# ---------------------------------------------------------------------------
# axis_weights: affinity for each Axis (higher = prefer)
# color_weights: affinity for each Color (higher = prefer)
# order_bias: per-Order multiplier (empty = uniform)
# type_bias: per-Type multiplier (empty = uniform)
# gold_affinity: boost GOLD-eligible zips

def _uniform_axis():
    return {a: 0.5 for a in AXIS_EMOJIS}

def _uniform_color():
    return {c: 0.5 for c in COLOR_EMOJIS}

ARCHETYPES = [
    # ── Strength Domain (7) ──────────────────────────────────────────────
    {
        "id": 1, "name": "General Strength", "slug": "general-strength",
        "domain": "strength",
        "description": "Barbell classics, linear progression, balanced push/pull/legs",
        "axis_weights": {"🏛": 1.0, "🔨": 0.6, "🌹": 0.3, "🪐": 0.5, "⌛": 0.2, "🐬": 0.2},
        "color_weights": {"⚫": 0.4, "🟢": 0.3, "🔵": 1.0, "🟣": 0.6, "🔴": 0.7, "🟠": 0.2, "🟡": 0.3, "⚪": 0.3},
        "order_bias": {"⛽": 1.3, "🐂": 1.1},
        "type_bias": {},
        "gold_affinity": False,
    },
    {
        "id": 2, "name": "Powerlifting", "slug": "powerlifting",
        "domain": "strength",
        "description": "Squat/bench/deadlift focus, peaking cycles, competition prep",
        "axis_weights": {"🏛": 1.0, "🔨": 0.3, "🌹": 0.1, "🪐": 0.7, "⌛": 0.2, "🐬": 0.1},
        "color_weights": {"⚫": 0.3, "🟢": 0.1, "🔵": 1.0, "🟣": 0.8, "🔴": 0.6, "🟠": 0.1, "🟡": 0.1, "⚪": 0.2},
        "order_bias": {"⛽": 1.5, "🏟": 1.3, "🖼": 0.5},
        "type_bias": {"🛒": 1.2, "🪡": 1.2, "🍗": 1.2, "➖": 0.4},
        "gold_affinity": False,
    },
    {
        "id": 3, "name": "Strongman / Odd Object", "slug": "strongman",
        "domain": "strength",
        "description": "Carries, stones, yokes, implements",
        "axis_weights": {"🏛": 0.5, "🔨": 0.9, "🌹": 0.1, "🪐": 0.8, "⌛": 0.3, "🐬": 0.3},
        "color_weights": {"⚫": 0.3, "🟢": 0.1, "🔵": 0.7, "🟣": 0.9, "🔴": 1.0, "🟠": 0.3, "🟡": 0.3, "⚪": 0.1},
        "order_bias": {"⛽": 1.3, "🏟": 1.2},
        "type_bias": {"➕": 1.3, "➖": 0.5},
        "gold_affinity": True,
    },
    {
        "id": 4, "name": "Calisthenics Strength", "slug": "calisthenics-strength",
        "domain": "strength",
        "description": "Advanced bodyweight: muscle-ups, levers, planches",
        "axis_weights": {"🏛": 0.7, "🔨": 0.8, "🌹": 0.3, "🪐": 0.9, "⌛": 0.4, "🐬": 0.3},
        "color_weights": {"⚫": 0.4, "🟢": 1.0, "🔵": 0.5, "🟣": 0.7, "🔴": 0.5, "🟠": 0.4, "🟡": 0.4, "⚪": 0.3},
        "order_bias": {"⛽": 1.2},
        "type_bias": {},
        "gold_affinity": False,
    },
    {
        "id": 5, "name": "Kettlebell Strength", "slug": "kettlebell-strength",
        "domain": "strength",
        "description": "KB-first programming, swings, TGUs, complexes",
        "axis_weights": {"🏛": 0.5, "🔨": 1.0, "🌹": 0.2, "🪐": 0.5, "⌛": 0.6, "🐬": 0.3},
        "color_weights": {"⚫": 0.4, "🟢": 0.3, "🔵": 0.8, "🟣": 0.7, "🔴": 0.6, "🟠": 0.7, "🟡": 0.4, "⚪": 0.3},
        "order_bias": {"⛽": 1.2, "🌾": 1.2},
        "type_bias": {"➕": 1.2},
        "gold_affinity": False,
    },
    {
        "id": 6, "name": "Senior Strength", "slug": "senior-strength",
        "domain": "strength",
        "description": "Joint-friendly loading, machine-assisted, balance integration",
        "axis_weights": {"🏛": 0.8, "🔨": 0.6, "🌹": 0.5, "🪐": 0.2, "⌛": 0.3, "🐬": 0.4},
        "color_weights": {"⚫": 0.7, "🟢": 0.5, "🔵": 0.9, "🟣": 0.3, "🔴": 0.2, "🟠": 0.5, "🟡": 0.4, "⚪": 0.7},
        "order_bias": {"🐂": 1.4, "⚖": 1.3, "🖼": 1.2, "🏟": 0.3},
        "type_bias": {},
        "gold_affinity": False,
    },
    {
        "id": 7, "name": "Post-Rehab Strength", "slug": "post-rehab-strength",
        "domain": "strength",
        "description": "Return-to-training progressions, conservative loading",
        "axis_weights": {"🏛": 0.7, "🔨": 0.6, "🌹": 0.5, "🪐": 0.2, "⌛": 0.3, "🐬": 0.3},
        "color_weights": {"⚫": 0.8, "🟢": 0.6, "🔵": 0.8, "🟣": 0.3, "🔴": 0.1, "🟠": 0.4, "🟡": 0.3, "⚪": 0.7},
        "order_bias": {"🐂": 1.4, "⚖": 1.4, "🖼": 1.2, "🏟": 0.2, "⛽": 0.5},
        "type_bias": {},
        "gold_affinity": False,
    },
    # ── Hypertrophy Domain (5) ───────────────────────────────────────────
    {
        "id": 8, "name": "Bodybuilding", "slug": "bodybuilding",
        "domain": "hypertrophy",
        "description": "Isolation-heavy, pump focus, aesthetic dominant",
        "axis_weights": {"🏛": 0.5, "🔨": 0.3, "🌹": 1.0, "🪐": 0.3, "⌛": 0.2, "🐬": 0.2},
        "color_weights": {"⚫": 0.3, "🟢": 0.2, "🔵": 0.8, "🟣": 0.4, "🔴": 1.0, "🟠": 0.3, "🟡": 0.3, "⚪": 0.3},
        "order_bias": {"🦋": 1.5, "⛽": 0.8},
        "type_bias": {"🛒": 1.1, "🪡": 1.1},
        "gold_affinity": False,
    },
    {
        "id": 9, "name": "Physique / Recomp", "slug": "physique-recomp",
        "domain": "hypertrophy",
        "description": "Balanced hypertrophy + conditioning, leaner bias",
        "axis_weights": {"🏛": 0.6, "🔨": 0.5, "🌹": 0.8, "🪐": 0.3, "⌛": 0.4, "🐬": 0.2},
        "color_weights": {"⚫": 0.3, "🟢": 0.4, "🔵": 0.8, "🟣": 0.4, "🔴": 0.8, "🟠": 0.6, "🟡": 0.3, "⚪": 0.3},
        "order_bias": {"🦋": 1.3, "🌾": 1.1},
        "type_bias": {"➖": 1.2},
        "gold_affinity": False,
    },
    {
        "id": 10, "name": "Athletic Hypertrophy", "slug": "athletic-hypertrophy",
        "domain": "hypertrophy",
        "description": "Size that transfers: power-building, sport-hybrid",
        "axis_weights": {"🏛": 0.6, "🔨": 0.9, "🌹": 0.4, "🪐": 0.5, "⌛": 0.3, "🐬": 0.3},
        "color_weights": {"⚫": 0.3, "🟢": 0.4, "🔵": 0.9, "🟣": 0.5, "🔴": 0.8, "🟠": 0.4, "🟡": 0.3, "⚪": 0.2},
        "order_bias": {"🦋": 1.2, "⛽": 1.1, "🌾": 1.1},
        "type_bias": {"➕": 1.1},
        "gold_affinity": False,
    },
    {
        "id": 11, "name": "Minimalist Hypertrophy", "slug": "minimalist-hypertrophy",
        "domain": "hypertrophy",
        "description": "3x/week full compounds, time-efficient muscle gain",
        "axis_weights": {"🏛": 1.0, "🔨": 0.4, "🌹": 0.5, "🪐": 0.2, "⌛": 0.3, "🐬": 0.2},
        "color_weights": {"⚫": 0.3, "🟢": 0.5, "🔵": 1.0, "🟣": 0.3, "🔴": 0.5, "🟠": 0.3, "🟡": 0.3, "⚪": 0.3},
        "order_bias": {"🦋": 1.3, "🌾": 1.2},
        "type_bias": {},
        "gold_affinity": False,
    },
    {
        "id": 12, "name": "Aesthetic Specialization", "slug": "aesthetic-specialization",
        "domain": "hypertrophy",
        "description": "Weak-point targeting, balance + aesthetic cross",
        "axis_weights": {"🏛": 0.3, "🔨": 0.3, "🌹": 1.0, "🪐": 0.3, "⌛": 0.2, "🐬": 0.2},
        "color_weights": {"⚫": 0.3, "🟢": 0.2, "🔵": 0.7, "🟣": 0.4, "🔴": 0.9, "🟠": 0.3, "🟡": 0.4, "⚪": 0.4},
        "order_bias": {"🦋": 1.3, "⚖": 1.3},
        "type_bias": {},
        "gold_affinity": False,
    },
    # ── Conditioning Domain (5) ──────────────────────────────────────────
    {
        "id": 13, "name": "General Conditioning", "slug": "general-conditioning",
        "domain": "conditioning",
        "description": "Broad aerobic base, mixed modality, Ultra dominant",
        "axis_weights": {"🏛": 0.4, "🔨": 0.6, "🌹": 0.2, "🪐": 0.3, "⌛": 0.9, "🐬": 0.3},
        "color_weights": {"⚫": 0.3, "🟢": 0.6, "🔵": 0.7, "🟣": 0.2, "🔴": 0.7, "🟠": 0.8, "🟡": 0.4, "⚪": 0.3},
        "order_bias": {"🌾": 1.2},
        "type_bias": {"➖": 1.5, "➕": 1.1},
        "gold_affinity": False,
    },
    {
        "id": 14, "name": "Marathon / Distance Running", "slug": "marathon-distance",
        "domain": "conditioning",
        "description": "Zone 2 heavy, running-specific mobility and strength",
        "axis_weights": {"🏛": 0.4, "🔨": 0.6, "🌹": 0.3, "🪐": 0.3, "⌛": 1.0, "🐬": 0.2},
        "color_weights": {"⚫": 0.2, "🟢": 0.7, "🔵": 0.8, "🟣": 0.2, "🔴": 0.4, "🟠": 0.5, "🟡": 0.3, "⚪": 0.6},
        "order_bias": {"🖼": 1.3, "🐂": 1.1, "🏟": 0.5},
        "type_bias": {"➖": 1.6, "🍗": 1.2, "➕": 0.8},
        "gold_affinity": False,
    },
    {
        "id": 15, "name": "Sprint / Power Conditioning", "slug": "sprint-power-conditioning",
        "domain": "conditioning",
        "description": "Short intervals, explosive repeats, plyometrics",
        "axis_weights": {"🏛": 0.4, "🔨": 0.7, "🌹": 0.2, "🪐": 0.7, "⌛": 0.8, "🐬": 0.3},
        "color_weights": {"⚫": 0.2, "🟢": 0.5, "🔵": 0.6, "🟣": 0.6, "🔴": 1.0, "🟠": 0.6, "🟡": 0.3, "⚪": 0.1},
        "order_bias": {"🏟": 1.3, "⛽": 1.1},
        "type_bias": {"➖": 1.3, "➕": 1.2, "🍗": 1.1},
        "gold_affinity": True,
    },
    {
        "id": 16, "name": "Sport Conditioning", "slug": "sport-conditioning",
        "domain": "conditioning",
        "description": "Field sport energy systems, agility, lateral movement",
        "axis_weights": {"🏛": 0.3, "🔨": 0.9, "🌹": 0.1, "🪐": 0.5, "⌛": 0.7, "🐬": 0.5},
        "color_weights": {"⚫": 0.3, "🟢": 0.6, "🔵": 0.6, "🟣": 0.3, "🔴": 0.8, "🟠": 0.8, "🟡": 0.4, "⚪": 0.2},
        "order_bias": {"🌾": 1.2, "🏟": 1.1},
        "type_bias": {"➖": 1.3, "➕": 1.2},
        "gold_affinity": False,
    },
    {
        "id": 17, "name": "Fasting Cardio + Strength", "slug": "fasting-cardio-strength",
        "domain": "conditioning",
        "description": "Low-intensity AM conditioning paired with PM strength",
        "axis_weights": {"🏛": 0.7, "🔨": 0.5, "🌹": 0.3, "🪐": 0.2, "⌛": 0.6, "🐬": 0.2},
        "color_weights": {"⚫": 0.3, "🟢": 0.7, "🔵": 0.8, "🟣": 0.3, "🔴": 0.4, "🟠": 0.5, "🟡": 0.3, "⚪": 0.6},
        "order_bias": {"🐂": 1.2, "🖼": 1.1},
        "type_bias": {"➖": 1.3},
        "gold_affinity": False,
    },
    # ── Functional / Athletic Domain (5) ─────────────────────────────────
    {
        "id": 18, "name": "General Functional Fitness", "slug": "general-functional",
        "domain": "functional",
        "description": "Functional dominant, transfer-focused",
        "axis_weights": {"🏛": 0.4, "🔨": 1.0, "🌹": 0.2, "🪐": 0.5, "⌛": 0.4, "🐬": 0.4},
        "color_weights": {"⚫": 0.4, "🟢": 0.7, "🔵": 0.7, "🟣": 0.4, "🔴": 0.6, "🟠": 0.7, "🟡": 0.5, "⚪": 0.3},
        "order_bias": {"🌾": 1.2},
        "type_bias": {"➕": 1.1},
        "gold_affinity": False,
    },
    {
        "id": 19, "name": "CrossFit-Style", "slug": "crossfit-style",
        "domain": "functional",
        "description": "Mixed modal, EMOM/AMRAP, Olympic lifts + conditioning",
        "axis_weights": {"🏛": 0.4, "🔨": 0.7, "🌹": 0.1, "🪐": 0.7, "⌛": 1.0, "🐬": 0.4},
        "color_weights": {"⚫": 0.2, "🟢": 0.3, "🔵": 0.6, "🟣": 0.7, "🔴": 1.0, "🟠": 0.8, "🟡": 0.4, "⚪": 0.1},
        "order_bias": {"⛽": 1.1, "🏟": 1.2, "🌾": 1.1},
        "type_bias": {"➕": 1.3, "➖": 1.1},
        "gold_affinity": True,
    },
    {
        "id": 20, "name": "Combat Sport Prep", "slug": "combat-sport-prep",
        "domain": "functional",
        "description": "Rotational power, grip, neck, conditioning circuits",
        "axis_weights": {"🏛": 0.3, "🔨": 0.9, "🌹": 0.1, "🪐": 0.7, "⌛": 0.6, "🐬": 0.5},
        "color_weights": {"⚫": 0.3, "🟢": 0.5, "🔵": 0.6, "🟣": 0.5, "🔴": 1.0, "🟠": 0.8, "🟡": 0.3, "⚪": 0.2},
        "order_bias": {"⛽": 1.1, "🌾": 1.1},
        "type_bias": {"➕": 1.3, "➖": 1.1, "🪡": 1.1},
        "gold_affinity": False,
    },
    {
        "id": 21, "name": "Field Sport Athlete", "slug": "field-sport-athlete",
        "domain": "functional",
        "description": "Sprint, jump, cut, decelerate — movement-first",
        "axis_weights": {"🏛": 0.3, "🔨": 1.0, "🌹": 0.1, "🪐": 0.5, "⌛": 0.5, "🐬": 0.5},
        "color_weights": {"⚫": 0.3, "🟢": 0.6, "🔵": 0.7, "🟣": 0.5, "🔴": 0.7, "🟠": 0.6, "🟡": 0.4, "⚪": 0.2},
        "order_bias": {"🏟": 1.2, "🌾": 1.1},
        "type_bias": {"🍗": 1.2, "➕": 1.2, "➖": 1.1},
        "gold_affinity": True,
    },
    {
        "id": 22, "name": "Climbing / Grip Sport", "slug": "climbing-grip",
        "domain": "functional",
        "description": "Pull dominance, finger strength, shoulder stability",
        "axis_weights": {"🏛": 0.4, "🔨": 0.8, "🌹": 0.3, "🪐": 0.8, "⌛": 0.4, "🐬": 0.3},
        "color_weights": {"⚫": 0.3, "🟢": 0.8, "🔵": 0.6, "🟣": 0.7, "🔴": 0.5, "🟠": 0.4, "🟡": 0.4, "⚪": 0.4},
        "order_bias": {"⛽": 1.1},
        "type_bias": {"🪡": 1.4, "➕": 1.1, "🛒": 0.7},
        "gold_affinity": False,
    },
    # ── Life Stage Domain (5) ────────────────────────────────────────────
    {
        "id": 23, "name": "New to Gym", "slug": "new-to-gym",
        "domain": "life-stage",
        "description": "Foundation heavy, teaching-focused, Teaching dominant",
        "axis_weights": {"🏛": 1.0, "🔨": 0.5, "🌹": 0.3, "🪐": 0.1, "⌛": 0.2, "🐬": 0.3},
        "color_weights": {"⚫": 1.0, "🟢": 0.6, "🔵": 0.7, "🟣": 0.2, "🔴": 0.1, "🟠": 0.4, "🟡": 0.5, "⚪": 0.4},
        "order_bias": {"🐂": 1.6, "🖼": 1.1, "🏟": 0.2, "⛽": 0.4},
        "type_bias": {},
        "gold_affinity": False,
    },
    {
        "id": 24, "name": "Return After Break", "slug": "return-after-break",
        "domain": "life-stage",
        "description": "Ramp-back protocol, conservative progression",
        "axis_weights": {"🏛": 0.9, "🔨": 0.5, "🌹": 0.4, "🪐": 0.2, "⌛": 0.3, "🐬": 0.3},
        "color_weights": {"⚫": 0.7, "🟢": 0.6, "🔵": 0.8, "🟣": 0.3, "🔴": 0.2, "🟠": 0.4, "🟡": 0.4, "⚪": 0.5},
        "order_bias": {"🐂": 1.5, "⚖": 1.2, "🖼": 1.2, "🏟": 0.3, "⛽": 0.5},
        "type_bias": {},
        "gold_affinity": False,
    },
    {
        "id": 25, "name": "50+ Active Living", "slug": "fifty-plus",
        "domain": "life-stage",
        "description": "Joint health, balance, bone density, functional independence",
        "axis_weights": {"🏛": 0.7, "🔨": 0.7, "🌹": 0.4, "🪐": 0.2, "⌛": 0.3, "🐬": 0.5},
        "color_weights": {"⚫": 0.6, "🟢": 0.6, "🔵": 0.8, "🟣": 0.3, "🔴": 0.2, "🟠": 0.5, "🟡": 0.5, "⚪": 0.7},
        "order_bias": {"🐂": 1.3, "⚖": 1.4, "🖼": 1.3, "🏟": 0.3, "⛽": 0.6},
        "type_bias": {"🍗": 1.1},
        "gold_affinity": False,
    },
    {
        "id": 26, "name": "Pre/Post Natal", "slug": "pre-post-natal",
        "domain": "life-stage",
        "description": "Pelvic floor, core restoration, modified loading",
        "axis_weights": {"🏛": 0.5, "🔨": 0.6, "🌹": 0.7, "🪐": 0.1, "⌛": 0.3, "🐬": 0.3},
        "color_weights": {"⚫": 0.5, "🟢": 0.8, "🔵": 0.6, "🟣": 0.2, "🔴": 0.1, "🟠": 0.3, "🟡": 0.3, "⚪": 1.0},
        "order_bias": {"🖼": 1.5, "🐂": 1.3, "⚖": 1.3, "🏟": 0.1, "⛽": 0.2},
        "type_bias": {"➕": 1.2},
        "gold_affinity": False,
    },
    {
        "id": 27, "name": "Youth Athletic Development", "slug": "youth-athletic",
        "domain": "life-stage",
        "description": "Movement literacy, bodyweight mastery, no maximal loading",
        "axis_weights": {"🏛": 0.6, "🔨": 0.8, "🌹": 0.2, "🪐": 0.3, "⌛": 0.4, "🐬": 0.7},
        "color_weights": {"⚫": 0.7, "🟢": 1.0, "🔵": 0.5, "🟣": 0.3, "🔴": 0.2, "🟠": 0.6, "🟡": 0.8, "⚪": 0.3},
        "order_bias": {"🐂": 1.5, "🌾": 1.2, "🏟": 0.3, "⛽": 0.3},
        "type_bias": {"➕": 1.1, "➖": 1.1},
        "gold_affinity": False,
    },
    # ── Recovery / Wellness Domain (4) ───────────────────────────────────
    {
        "id": 28, "name": "Active Recovery", "slug": "active-recovery",
        "domain": "recovery",
        "description": "Restoration dominant, mobility, somatic, Mindful heavy",
        "axis_weights": {"🏛": 0.3, "🔨": 0.4, "🌹": 0.8, "🪐": 0.1, "⌛": 0.4, "🐬": 0.3},
        "color_weights": {"⚫": 0.4, "🟢": 0.7, "🔵": 0.4, "🟣": 0.2, "🔴": 0.1, "🟠": 0.3, "🟡": 0.5, "⚪": 1.0},
        "order_bias": {"🖼": 1.6, "⚖": 1.2, "🐂": 1.1, "🏟": 0.1, "⛽": 0.3},
        "type_bias": {},
        "gold_affinity": False,
    },
    {
        "id": 29, "name": "Stress Management", "slug": "stress-management",
        "domain": "recovery",
        "description": "Parasympathetic training, breath work, low-CNS movement",
        "axis_weights": {"🏛": 0.3, "🔨": 0.3, "🌹": 0.7, "🪐": 0.1, "⌛": 0.5, "🐬": 0.4},
        "color_weights": {"⚫": 0.3, "🟢": 0.6, "🔵": 0.4, "🟣": 0.2, "🔴": 0.1, "🟠": 0.3, "🟡": 0.5, "⚪": 1.0},
        "order_bias": {"🖼": 1.6, "⚖": 1.1, "🏟": 0.1, "⛽": 0.2},
        "type_bias": {"➖": 1.2},
        "gold_affinity": False,
    },
    {
        "id": 30, "name": "Flexibility / Mobility", "slug": "flexibility-mobility",
        "domain": "recovery",
        "description": "ROM-focused, somatic aesthetic in Restoration context",
        "axis_weights": {"🏛": 0.3, "🔨": 0.5, "🌹": 1.0, "🪐": 0.2, "⌛": 0.4, "🐬": 0.2},
        "color_weights": {"⚫": 0.3, "🟢": 0.7, "🔵": 0.5, "🟣": 0.3, "🔴": 0.1, "🟠": 0.3, "🟡": 0.4, "⚪": 1.0},
        "order_bias": {"🖼": 1.5, "🐂": 1.2, "⚖": 1.2, "🏟": 0.1, "⛽": 0.3},
        "type_bias": {},
        "gold_affinity": False,
    },
    {
        "id": 31, "name": "Injury Prevention / Prehab", "slug": "injury-prevention",
        "domain": "recovery",
        "description": "Balance dominant, corrective, Reformance heavy",
        "axis_weights": {"🏛": 0.4, "🔨": 0.6, "🌹": 0.5, "🪐": 0.2, "⌛": 0.3, "🐬": 0.3},
        "color_weights": {"⚫": 0.5, "🟢": 0.6, "🔵": 0.7, "🟣": 0.3, "🔴": 0.1, "🟠": 0.4, "🟡": 0.3, "⚪": 0.8},
        "order_bias": {"⚖": 1.5, "🖼": 1.3, "🐂": 1.2, "🏟": 0.2, "⛽": 0.4},
        "type_bias": {},
        "gold_affinity": False,
    },
    # ── Specialty Domain (4) ─────────────────────────────────────────────
    {
        "id": 32, "name": "Olympic Lifting", "slug": "olympic-lifting",
        "domain": "specialty",
        "description": "Snatch/clean/jerk progression, Technical dominant",
        "axis_weights": {"🏛": 0.6, "🔨": 0.4, "🌹": 0.1, "🪐": 0.7, "⌛": 0.3, "🐬": 0.2},
        "color_weights": {"⚫": 0.4, "🟢": 0.1, "🔵": 0.6, "🟣": 1.0, "🔴": 0.7, "🟠": 0.1, "🟡": 0.2, "⚪": 0.2},
        "order_bias": {"⛽": 1.3, "🏟": 1.2, "🐂": 1.1},
        "type_bias": {"➕": 1.4, "🪡": 1.1, "➖": 0.5},
        "gold_affinity": True,
    },
    {
        "id": 33, "name": "Endurance Sport Cross-Training", "slug": "endurance-cross-training",
        "domain": "specialty",
        "description": "Cyclist/swimmer/runner strength complement",
        "axis_weights": {"🏛": 0.5, "🔨": 0.7, "🌹": 0.3, "🪐": 0.3, "⌛": 0.6, "🐬": 0.2},
        "color_weights": {"⚫": 0.3, "🟢": 0.6, "🔵": 0.8, "🟣": 0.3, "🔴": 0.4, "🟠": 0.6, "🟡": 0.3, "⚪": 0.5},
        "order_bias": {"🐂": 1.2, "🖼": 1.1, "⚖": 1.1},
        "type_bias": {"🍗": 1.2, "➖": 1.2},
        "gold_affinity": False,
    },
    {
        "id": 34, "name": "Tactical / First Responder", "slug": "tactical-first-responder",
        "domain": "specialty",
        "description": "Occupational fitness, carry capacity, sustained output",
        "axis_weights": {"🏛": 0.5, "🔨": 0.9, "🌹": 0.1, "🪐": 0.6, "⌛": 0.5, "🐬": 0.4},
        "color_weights": {"⚫": 0.3, "🟢": 0.5, "🔵": 0.8, "🟣": 0.4, "🔴": 0.8, "🟠": 0.6, "🟡": 0.3, "⚪": 0.2},
        "order_bias": {"⛽": 1.2, "🌾": 1.1},
        "type_bias": {"➕": 1.2, "➖": 1.1},
        "gold_affinity": False,
    },
    {
        "id": 35, "name": "Explorer / Outdoor Athlete", "slug": "explorer-outdoor",
        "domain": "specialty",
        "description": "Hiking, rucking, trail movement, minimal equipment",
        "axis_weights": {"🏛": 0.4, "🔨": 0.8, "🌹": 0.2, "🪐": 0.5, "⌛": 0.5, "🐬": 0.3},
        "color_weights": {"⚫": 0.3, "🟢": 1.0, "🔵": 0.5, "🟣": 0.3, "🔴": 0.4, "🟠": 0.5, "🟡": 0.6, "⚪": 0.4},
        "order_bias": {"🌾": 1.2, "🖼": 1.1},
        "type_bias": {"🍗": 1.1, "➖": 1.2, "➕": 1.1},
        "gold_affinity": False,
    },
]

assert len(ARCHETYPES) == 35, f"Expected 35 archetypes, got {len(ARCHETYPES)}"


# ---------------------------------------------------------------------------
# Load zip registry
# ---------------------------------------------------------------------------

def load_zip_registry() -> list[dict]:
    if not REGISTRY_PATH.exists():
        print(f"❌ Zip registry not found: {REGISTRY_PATH}")
        sys.exit(1)
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_zip(z: dict, arch: dict) -> float:
    axis_e = z["axis"]["emoji"]
    color_e = z["color"]["emoji"]
    order_e = z["order"]["emoji"]
    type_e = z["type"]["emoji"]

    s = (arch["axis_weights"].get(axis_e, 0.5)
         * arch["color_weights"].get(color_e, 0.5)
         * arch.get("order_bias", {}).get(order_e, 1.0)
         * arch.get("type_bias", {}).get(type_e, 1.0))

    if arch.get("gold_affinity") and z.get("gold_eligible"):
        s *= 1.5

    return s


# ---------------------------------------------------------------------------
# Working slot assignment (35 per abacus)
# ---------------------------------------------------------------------------

def _compute_axis_quotas(axis_weights: dict[str, float]) -> dict[str, int]:
    """Distribute 35 working slots across 6 axes proportional to weights."""
    total_w = sum(axis_weights.get(ae, 0.0) for ae in AXIS_EMOJIS) or 1.0
    raw = {ae: 35 * axis_weights.get(ae, 0.0) / total_w for ae in AXIS_EMOJIS}

    # Floor each, then distribute remainder to highest fractional parts
    floored = {ae: int(raw[ae]) for ae in AXIS_EMOJIS}
    remainder = 35 - sum(floored.values())
    fracs = sorted(AXIS_EMOJIS, key=lambda ae: raw[ae] - floored[ae], reverse=True)
    for ae in fracs[:remainder]:
        floored[ae] += 1

    return floored


def assign_working_slots(
    zips: list[dict],
    arch: dict,
    globally_covered: set[str] | None = None,
) -> list[str]:
    """Assign 35 working zips with axis diversity via quota distribution.

    Each Order appears exactly 5× and each Type appears exactly 7×.
    Axes are distributed proportionally to axis_weights across the 35 cells.
    Uncovered zips (not in globally_covered) get a score boost.
    """
    axis_quotas = _compute_axis_quotas(arch["axis_weights"])
    covered = globally_covered or set()

    def _eff_score(z: dict) -> float:
        s = score_zip(z, arch)
        if z["numeric_zip"] not in covered:
            s *= 5.0  # Strongly prefer uncovered zips
        return s

    # Group zips by (Order, Type, Axis)
    by_cell_axis: dict[tuple[str, str, str], list[tuple[dict, float]]] = defaultdict(list)
    for z in zips:
        key = (z["order"]["emoji"], z["type"]["emoji"], z["axis"]["emoji"])
        by_cell_axis[key].append((z, _eff_score(z)))
    for key in by_cell_axis:
        by_cell_axis[key].sort(key=lambda x: x[1], reverse=True)

    # Build all 35 Order×Type cells
    cells = [(oe, te) for oe in ORDER_EMOJIS for te in TYPE_EMOJIS]

    # First, compute best score per (cell, axis) — i.e., best color for that combo
    cell_axis_best: dict[tuple[str, str, str], tuple[dict, float]] = {}
    for (oe, te) in cells:
        for ae in AXIS_EMOJIS:
            candidates = by_cell_axis.get((oe, te, ae), [])
            if candidates:
                cell_axis_best[(oe, te, ae)] = candidates[0]

    # Greedy assignment: iterate axes by quota (largest first),
    # for each axis pick its best unassigned cells
    assigned_cells: dict[tuple[str, str], tuple[str, str]] = {}  # cell -> (axis, numeric_zip)
    remaining_cells = set(cells)
    axis_remaining = dict(axis_quotas)

    # Sort axes by quota descending for stable assignment
    for ae in sorted(AXIS_EMOJIS, key=lambda a: axis_remaining.get(a, 0), reverse=True):
        quota = axis_remaining[ae]
        if quota <= 0:
            continue

        # Score unassigned cells for this axis
        cell_scores = []
        for (oe, te) in remaining_cells:
            best = cell_axis_best.get((oe, te, ae))
            if best:
                cell_scores.append(((oe, te), best[1], best[0]))

        cell_scores.sort(key=lambda x: x[1], reverse=True)

        filled = 0
        for (oe, te), score, z in cell_scores:
            if filled >= quota:
                break
            if (oe, te) in remaining_cells:
                assigned_cells[(oe, te)] = (ae, z["numeric_zip"])
                remaining_cells.discard((oe, te))
                filled += 1

    # Handle any unassigned cells (fallback: pick best available)
    for (oe, te) in list(remaining_cells):
        best_score = -1
        best_zip = None
        for ae in AXIS_EMOJIS:
            cand = cell_axis_best.get((oe, te, ae))
            if cand and cand[1] > best_score:
                best_score = cand[1]
                best_zip = cand[0]
        if best_zip:
            assigned_cells[(oe, te)] = (best_zip["axis"]["emoji"], best_zip["numeric_zip"])
            remaining_cells.discard((oe, te))

    working = [assigned_cells[cell][1] for cell in cells if cell in assigned_cells]
    assert len(working) == 35, f"{arch['name']}: expected 35 working, got {len(working)}"
    return working


# ---------------------------------------------------------------------------
# Bonus slot assignment (13 per abacus)
# ---------------------------------------------------------------------------

def assign_bonus_slots(
    zips: list[dict],
    arch: dict,
    working: list[str],
    all_archetypes: list[dict],
    globally_covered: set[str],
) -> list[dict]:
    """Assign 13 bonus zips with role constraints.

    Prioritizes uncovered zips (not in globally_covered) to maximize
    total system coverage across all 35 abaci.
    """
    working_set = set(working)
    zip_by_num = {z["numeric_zip"]: z for z in zips}

    # Candidate pool: everything not in this archetype's working slots
    candidates = [z for z in zips if z["numeric_zip"] not in working_set]

    # Coverage bonus: uncovered zips get a strong score multiplier
    def _boosted_score(z: dict) -> float:
        s = score_zip(z, arch)
        if z["numeric_zip"] not in globally_covered:
            s *= 10.0
        return s

    bonus = []
    used = set()

    # --- 3 junction bridges: zips that score well for OTHER archetypes ---
    # Prefer uncovered ones
    junction_scores = []
    for z in candidates:
        nz = z["numeric_zip"]
        other_scores = [score_zip(z, a) for a in all_archetypes if a["id"] != arch["id"]]
        avg_other = sum(other_scores) / len(other_scores) if other_scores else 0
        if nz not in globally_covered:
            avg_other *= 10.0
        junction_scores.append((nz, avg_other))
    junction_scores.sort(key=lambda x: x[1], reverse=True)

    for nz, _ in junction_scores:
        if nz not in used and nz not in working_set:
            bonus.append({"zip": nz, "role": "junction"})
            used.add(nz)
            if len(bonus) >= 3:
                break

    # --- 2 harder variations: 🪐 Challenge axis ---
    working_types = {zip_by_num[nz]["type"]["emoji"] for nz in working if nz in zip_by_num}
    challenge_candidates = [
        (z, _boosted_score(z))
        for z in candidates
        if z["axis"]["emoji"] == "🪐"
        and z["numeric_zip"] not in used
        and z["type"]["emoji"] in working_types
    ]
    challenge_candidates.sort(key=lambda x: x[1], reverse=True)
    for z, _ in challenge_candidates[:2]:
        bonus.append({"zip": z["numeric_zip"], "role": "variation"})
        used.add(z["numeric_zip"])

    # --- 2 recovery alternatives: 🖼 Order or ⚪ Color ---
    recovery_candidates = [
        (z, _boosted_score(z))
        for z in candidates
        if (z["order"]["emoji"] == "🖼" or z["color"]["emoji"] == "⚪")
        and z["numeric_zip"] not in used
    ]
    recovery_candidates.sort(key=lambda x: x[1], reverse=True)
    for z, _ in recovery_candidates[:2]:
        bonus.append({"zip": z["numeric_zip"], "role": "recovery"})
        used.add(z["numeric_zip"])

    # --- Fill remaining with highest-affinity variety, preferring uncovered ---
    scored = [(z, _boosted_score(z)) for z in candidates]
    scored.sort(key=lambda x: x[1], reverse=True)

    for z, _ in scored:
        if len(bonus) >= 13:
            break
        nz = z["numeric_zip"]
        if nz not in used and nz not in working_set:
            bonus.append({"zip": nz, "role": "variety"})
            used.add(nz)

    return bonus[:13]


# ---------------------------------------------------------------------------
# Coverage sweep
# ---------------------------------------------------------------------------

def coverage_sweep(
    all_zips: list[dict],
    abaci_data: list[dict],
) -> tuple[int, int, list[str]]:
    """Check coverage and attempt safe orphan resolution.

    Returns (covered_count, orphans_placed, free_agent_zips).

    Orphans are resolved by swapping low-affinity bonus variety zips
    for orphans in the best-fit archetype — but ONLY when the evicted
    zip retains coverage elsewhere. Remaining orphans become free agents
    (DLC pack candidates), not force-assigned.
    """
    covered = set()
    for ab in abaci_data:
        for nz in ab["working_zips"]:
            covered.add(nz)
        for b in ab["bonus_zips"]:
            covered.add(b["zip"])

    all_numeric = {z["numeric_zip"] for z in all_zips}
    orphans = sorted(all_numeric - covered)
    initial_orphan_count = len(orphans)

    if orphans:
        zip_by_num = {z["numeric_zip"]: z for z in all_zips}

        # Count how many abaci each zip appears in (for eviction priority)
        zip_abacus_count = Counter()
        for ab in abaci_data:
            for nz in ab["working_zips"]:
                zip_abacus_count[nz] += 1
            for b in ab["bonus_zips"]:
                zip_abacus_count[b["zip"]] += 1

        for orphan_nz in orphans:
            z = zip_by_num[orphan_nz]
            # Find the best swap: evict a bonus zip that appears in MANY
            # other abaci (so coverage isn't lost) for this orphan
            best_arch_idx = -1
            best_swap_pos = -1
            best_evict_score = -1  # higher = better candidate for eviction

            for i, ab in enumerate(abaci_data):
                orphan_score = score_zip(z, ARCHETYPES[i])
                if orphan_score < 0.01:
                    continue  # Skip archetypes with zero affinity

                working_set = set(ab["working_zips"])
                for j, b in enumerate(ab["bonus_zips"]):
                    existing_nz = b["zip"]
                    if existing_nz in working_set:
                        continue  # Don't evict if it's also a working zip

                    # Prefer evicting zips that appear in many other abaci
                    other_count = zip_abacus_count.get(existing_nz, 1) - 1
                    evict_score = other_count + orphan_score
                    if evict_score > best_evict_score:
                        best_evict_score = evict_score
                        best_arch_idx = i
                        best_swap_pos = j

            if best_arch_idx >= 0 and best_swap_pos >= 0:
                evicted_nz = abaci_data[best_arch_idx]["bonus_zips"][best_swap_pos]["zip"]
                # Only evict if the evicted zip still has coverage elsewhere
                if zip_abacus_count.get(evicted_nz, 0) > 1:
                    zip_abacus_count[evicted_nz] -= 1
                    abaci_data[best_arch_idx]["bonus_zips"][best_swap_pos] = {
                        "zip": orphan_nz, "role": "variety"
                    }
                    zip_abacus_count[orphan_nz] = zip_abacus_count.get(orphan_nz, 0) + 1
                    covered.add(orphan_nz)

        # Second pass: for remaining orphans, do chain swaps
        # Evict a singly-covered bonus zip that has BETTER affinity elsewhere,
        # then assign the orphan. The evicted zip gets reassigned to its
        # best-fit archetype in place of a multiply-covered zip.
        covered2 = set()
        for ab in abaci_data:
            for nz in ab["working_zips"]:
                covered2.add(nz)
            for b in ab["bonus_zips"]:
                covered2.add(b["zip"])

        remaining_orphans = sorted(all_numeric - covered2)
        for orphan_nz in remaining_orphans:
            z = zip_by_num[orphan_nz]
            placed = False
            for i, ab in enumerate(abaci_data):
                if placed:
                    break
                working_set_i = set(ab["working_zips"])
                for j, b in enumerate(ab["bonus_zips"]):
                    existing_nz = b["zip"]
                    if existing_nz in working_set_i:
                        continue
                    in_other_working = False
                    for k, ab2 in enumerate(abaci_data):
                        if k == i:
                            continue
                        if existing_nz in ab2["working_zips"]:
                            in_other_working = True
                            break
                    if in_other_working:
                        abaci_data[i]["bonus_zips"][j] = {
                            "zip": orphan_nz, "role": "variety"
                        }
                        covered.add(orphan_nz)
                        placed = True
                        break

    # Recount after swaps
    covered = set()
    for ab in abaci_data:
        for nz in ab["working_zips"]:
            covered.add(nz)
        for b in ab["bonus_zips"]:
            covered.add(b["zip"])

    free_agents = sorted(all_numeric - covered)
    orphans_placed = initial_orphan_count - len(free_agents)
    return len(covered), orphans_placed, free_agents


# ---------------------------------------------------------------------------
# DLC Pack Builder
# ---------------------------------------------------------------------------

TYPE_NAMES = {
    "🛒": "Push", "🪡": "Pull", "🍗": "Legs", "➕": "Plus", "➖": "Ultra",
}
COLOR_NAMES = {
    "⚫": "Teaching", "🟢": "Bodyweight", "🔵": "Structured", "🟣": "Technical",
    "🔴": "Intense", "🟠": "Circuit", "🟡": "Fun", "⚪": "Mindful",
}


def build_dlc_packs(
    free_agent_zips: list[str],
    all_zips: list[dict],
) -> list[dict]:
    """Cluster free-agent zips into thematic DLC expansion packs.

    Packs are 3-12 zips grouped by Order, then sub-clustered by Axis.
    Runts (<3) merge into neighboring groups or a Mixed pack.
    """
    if not free_agent_zips:
        return []

    zip_by_num = {z["numeric_zip"]: z for z in all_zips}
    free_set = set(free_agent_zips)

    # Group by Order
    by_order: dict[str, list[str]] = defaultdict(list)
    for nz in free_agent_zips:
        z = zip_by_num[nz]
        by_order[z["order"]["emoji"]].append(nz)

    packs: list[dict] = []
    runts: list[str] = []  # zips from groups too small to form a pack
    pack_id = 1

    for oe in ORDER_EMOJIS:
        order_zips = by_order.get(oe, [])
        if not order_zips:
            continue

        if len(order_zips) < 3:
            runts.extend(order_zips)
            continue

        # Sub-cluster by Axis within this Order
        by_axis: dict[str, list[str]] = defaultdict(list)
        for nz in order_zips:
            z = zip_by_num[nz]
            by_axis[z["axis"]["emoji"]].append(nz)

        axis_groups: list[tuple[str, list[str]]] = []
        axis_runts: list[str] = []

        for ae in AXIS_EMOJIS:
            group = by_axis.get(ae, [])
            if not group:
                continue
            if len(group) < 3:
                axis_runts.extend(group)
            else:
                axis_groups.append((ae, group))

        # If axis runts exist, merge them into the largest axis group or form their own pack
        if axis_runts:
            if axis_groups:
                # Merge into largest existing group
                axis_groups.sort(key=lambda x: len(x[1]), reverse=True)
                largest_ae, largest_group = axis_groups[0]
                largest_group.extend(axis_runts)
                axis_groups[0] = (largest_ae, largest_group)
            elif len(axis_runts) >= 3:
                # All sub-groups were runts but together they form a viable pack
                axis_groups.append((None, axis_runts))
            else:
                runts.extend(axis_runts)

        # Create packs from axis groups, splitting if >12
        for ae, group in axis_groups:
            while len(group) > 12:
                chunk = group[:12]
                group = group[12:]
                packs.append(_make_dlc_pack(pack_id, oe, ae, chunk, zip_by_num))
                pack_id += 1

            if len(group) >= 3:
                packs.append(_make_dlc_pack(pack_id, oe, ae, group, zip_by_num))
                pack_id += 1
            else:
                runts.extend(group)

    # Handle all runts — merge into one or more Mixed packs
    while len(runts) >= 3:
        chunk = runts[:12]
        runts = runts[12:]
        packs.append(_make_dlc_pack(pack_id, None, None, chunk, zip_by_num))
        pack_id += 1

    # If 1-2 runts remain, append to the last pack
    if runts and packs:
        packs[-1]["zips"].extend(runts)
        packs[-1]["size"] = len(packs[-1]["zips"])
    elif runts:
        # Edge case: only 1-2 free agents total — still make a pack
        packs.append(_make_dlc_pack(pack_id, None, None, runts, zip_by_num))

    return packs


def _make_dlc_pack(
    pack_id: int,
    primary_order: str | None,
    primary_axis: str | None,
    zips: list[str],
    zip_by_num: dict[str, dict],
) -> dict:
    """Build a single DLC pack dict."""
    # Derive name
    if primary_order and primary_axis:
        name = f"{ORDER_NAMES[primary_order]} {AXIS_NAMES[primary_axis]} Pack"
        slug = f"{ORDER_NAMES[primary_order].lower().replace(' ', '-')}-{AXIS_NAMES[primary_axis].lower()}"
    elif primary_order:
        name = f"{ORDER_NAMES[primary_order]} Expansion Pack"
        slug = f"{ORDER_NAMES[primary_order].lower().replace(' ', '-')}-expansion"
    else:
        name = f"Mixed Expansion Pack"
        slug = "mixed-expansion"

    # If slug would collide, append pack_id
    slug = f"{slug}-{pack_id:02d}"

    # Derive description from zip composition
    order_counts = Counter()
    axis_counts = Counter()
    for nz in zips:
        z = zip_by_num.get(nz)
        if z:
            order_counts[z["order"]["emoji"]] += 1
            axis_counts[z["axis"]["emoji"]] += 1

    dominant_order = max(order_counts, key=order_counts.get) if order_counts else None
    dominant_axis = max(axis_counts, key=axis_counts.get) if axis_counts else None

    desc_parts = []
    if dominant_order:
        desc_parts.append(f"{dominant_order} {ORDER_NAMES.get(dominant_order, '')} dominant")
    if dominant_axis:
        desc_parts.append(f"{dominant_axis} {AXIS_NAMES.get(dominant_axis, '')} emphasis")
    description = ", ".join(desc_parts) if desc_parts else "Mixed training expansion"

    return {
        "id": f"dlc-{pack_id:02d}",
        "name": name,
        "slug": slug,
        "description": description,
        "theme": {
            "primary_order": primary_order,
            "primary_axis": primary_axis,
        },
        "zips": sorted(zips),
        "size": len(zips),
    }


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_abacus(ab: dict, all_zips: list[dict]) -> list[str]:
    """Validate one abacus. Returns list of error strings (empty = pass)."""
    errors = []
    zip_by_num = {z["numeric_zip"]: z for z in all_zips}

    # Count checks
    if len(ab["working_zips"]) != 35:
        errors.append(f"Working count: {len(ab['working_zips'])} (expected 35)")
    if len(ab["bonus_zips"]) != 13:
        errors.append(f"Bonus count: {len(ab['bonus_zips'])} (expected 13)")

    # Order distribution in working slots
    order_counts = Counter()
    type_counts = Counter()
    for nz in ab["working_zips"]:
        z = zip_by_num.get(nz)
        if z:
            order_counts[z["order"]["emoji"]] += 1
            type_counts[z["type"]["emoji"]] += 1

    for oe in ORDER_EMOJIS:
        c = order_counts.get(oe, 0)
        if c != 5:
            errors.append(f"Order {oe} count: {c} (expected 5)")

    for te in TYPE_EMOJIS:
        c = type_counts.get(te, 0)
        if c != 7:
            errors.append(f"Type {te} count: {c} (expected 7)")

    # Duplicate check within abacus
    all_in_abacus = list(ab["working_zips"]) + [b["zip"] for b in ab["bonus_zips"]]
    dupes = [nz for nz, cnt in Counter(all_in_abacus).items() if cnt > 1]
    if dupes:
        errors.append(f"Duplicate zips: {dupes}")

    return errors


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def axis_distribution(working_zips: list[str], all_zips: list[dict]) -> dict[str, float]:
    zip_by_num = {z["numeric_zip"]: z for z in all_zips}
    counts = Counter()
    for nz in working_zips:
        z = zip_by_num.get(nz)
        if z:
            counts[z["axis"]["emoji"]] += 1
    total = sum(counts.values()) or 1
    return {ae: counts.get(ae, 0) / total for ae in AXIS_EMOJIS}


def print_report(
    abaci_data: list[dict],
    all_zips: list[dict],
    coverage: dict,
    dlc_packs: list[dict] | None = None,
):
    print()
    print("PPL± Abacus Compilation")
    print("══════════════════════════════════════════════════════════════")
    print(f"35 abaci compiled — {coverage['total']} zips in catalog\n")

    all_ok = True
    for ab in abaci_data:
        errs = validate_abacus(ab, all_zips)
        status = "✅" if not errs else "❌"
        if errs:
            all_ok = False

        # Axis distribution summary
        dist = axis_distribution(ab["working_zips"], all_zips)
        dist_str = " ".join(f"{ae}{int(pct*100):>3}%" for ae, pct in dist.items() if pct > 0)

        w = len(ab["working_zips"])
        b = len(ab["bonus_zips"])
        name = ab["name"]
        print(f"  {status} {ab['id']:02d} {name:<35s} {w}W + {b}B | {dist_str}")
        for e in errs:
            print(f"       ❌ {e}")

    print()
    abaci_covered = coverage["covered"]
    print(f"Abaci coverage: {abaci_covered}/{coverage['total']} ({abaci_covered*100//coverage['total']}%)")
    if coverage.get("orphans_placed", 0) > 0:
        print(f"  ✅ {coverage['orphans_placed']} orphans resolved via bonus swap")
    free_count = coverage.get("free_agents", 0)
    if free_count > 0:
        print(f"  📦 {free_count} free-agent zips routed to DLC packs")
    print(f"Overlap: avg {coverage['avg_overlap']:.1f} abaci/zip, max {coverage['max_overlap']}")

    # Overlap histogram
    overlap = coverage.get("overlap_histogram", {})
    if overlap:
        print("\n  Overlap distribution:")
        for k in sorted(overlap.keys()):
            bar = "█" * min(overlap[k] // 10, 50)
            print(f"    {k} abaci: {overlap[k]:>5} zips {bar}")

    # DLC pack summary
    if dlc_packs:
        dlc_total = sum(p["size"] for p in dlc_packs)
        print(f"\nDLC Packs: {len(dlc_packs)} packs, {dlc_total} zips")
        for p in dlc_packs:
            print(f"  📦 {p['id']} {p['name']:<35s} {p['size']} zips")

        total_coverage = abaci_covered + dlc_total
        print(f"\nTotal coverage: {total_coverage}/{coverage['total']} "
              f"({total_coverage*100//coverage['total']}%)")

    # Show free agents by Order (zips in neither abaci nor DLC)
    all_assigned = set()
    for ab in abaci_data:
        all_assigned.update(ab["working_zips"])
        for b in ab["bonus_zips"]:
            all_assigned.add(b["zip"])
    if dlc_packs:
        for p in dlc_packs:
            all_assigned.update(p["zips"])
    all_numeric = {z["numeric_zip"] for z in all_zips}
    unassigned = sorted(all_numeric - all_assigned)
    if unassigned:
        print(f"\n⚠️  {len(unassigned)} zips unassigned (in no abacus or DLC pack):")
        by_order = defaultdict(list)
        zip_by_num = {z["numeric_zip"]: z for z in all_zips}
        for nz in unassigned:
            z = zip_by_num[nz]
            by_order[z["order"]["emoji"]].append(nz)
        for oe in ORDER_EMOJIS:
            if oe in by_order:
                print(f"    {oe} {ORDER_NAMES[oe]}: {len(by_order[oe])} zips")

    print()
    if all_ok:
        print("✅ All 35 abaci pass validation.")
    else:
        print("❌ Some abaci have validation errors.")


# ---------------------------------------------------------------------------
# Main compilation
# ---------------------------------------------------------------------------

def compile_abaci() -> tuple[list[dict], list[dict], dict]:
    """Compile all 35 abaci + DLC packs. Returns (abaci_data, dlc_packs, coverage_info)."""
    all_zips = load_zip_registry()
    assert len(all_zips) == 1680, f"Expected 1680 zips, got {len(all_zips)}"

    # Sequential assignment: working + bonus per archetype, coverage-aware
    globally_covered: set[str] = set()
    abaci_data = []
    for arch in ARCHETYPES:
        working = assign_working_slots(all_zips, arch, globally_covered)
        globally_covered.update(working)

        bonus = assign_bonus_slots(
            all_zips, arch, working, ARCHETYPES, globally_covered
        )
        for b in bonus:
            globally_covered.add(b["zip"])

        # Dominant axis = highest axis weight
        dom_axis = max(arch["axis_weights"], key=arch["axis_weights"].get)

        abaci_data.append({
            "id": arch["id"],
            "name": arch["name"],
            "slug": arch["slug"],
            "domain": arch["domain"],
            "description": arch["description"],
            "axis_bias": dom_axis,
            "working_zips": working,
            "bonus_zips": bonus,
        })

    covered, orphans_placed, free_agent_zips = coverage_sweep(all_zips, abaci_data)

    # Build DLC packs from free agents
    dlc_packs = build_dlc_packs(free_agent_zips, all_zips)

    # Compute overlap stats
    zip_abacus_count = Counter()
    for ab in abaci_data:
        for nz in ab["working_zips"]:
            zip_abacus_count[nz] += 1
        for b in ab["bonus_zips"]:
            zip_abacus_count[b["zip"]] += 1

    max_overlap = max(zip_abacus_count.values()) if zip_abacus_count else 0
    avg_overlap = sum(zip_abacus_count.values()) / len(zip_abacus_count) if zip_abacus_count else 0

    overlap_histogram = Counter(zip_abacus_count.values())

    coverage_info = {
        "total": 1680,
        "covered": covered,
        "orphans_placed": orphans_placed,
        "free_agents": len(free_agent_zips),
        "free_agent_zips": free_agent_zips,
        "dlc_packs": len(dlc_packs),
        "dlc_zips": sum(p["size"] for p in dlc_packs),
        "max_overlap": max_overlap,
        "avg_overlap": round(avg_overlap, 2),
        "overlap_histogram": dict(sorted(overlap_histogram.items())),
    }

    return abaci_data, dlc_packs, coverage_info


def write_output(abaci_data: list[dict], dlc_packs: list[dict], coverage: dict):
    output = {
        "generated": str(date.today()),
        "abaci": abaci_data,
        "dlc_packs": dlc_packs,
        "coverage": {
            k: v for k, v in coverage.items()
            if k not in ("overlap_histogram", "free_agent_zips")
        },
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"📁 Written to {OUTPUT_PATH}")


REPORT_DIR = REPO_ROOT / "reports"


def write_report(
    abaci_data: list[dict],
    dlc_packs: list[dict],
    all_zips: list[dict],
    coverage: dict,
    report_path: Path | None = None,
):
    """Write a full markdown report of the abacus sort."""
    if report_path is None:
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        report_path = REPORT_DIR / f"abacus-sort-report-{date.today()}.md"

    zip_by_num = {z["numeric_zip"]: z for z in all_zips}
    lines: list[str] = []

    def w(s: str = ""):
        lines.append(s)

    # --- Header ---
    abaci_covered = coverage["covered"]
    dlc_total = sum(p["size"] for p in dlc_packs)
    total_assigned = abaci_covered + dlc_total

    w(f"# PPL± Abacus Sort Report — {date.today()}")
    w()
    w(f"- **Total zips:** {coverage['total']}")
    w(f"- **Abaci coverage:** {abaci_covered}/{coverage['total']} "
      f"({abaci_covered*100//coverage['total']}%)")
    w(f"- **DLC packs:** {len(dlc_packs)} packs, {dlc_total} zips")
    w(f"- **Total assigned:** {total_assigned}/{coverage['total']} "
      f"({total_assigned*100//coverage['total']}%)")
    w(f"- **Orphans resolved via swap:** {coverage.get('orphans_placed', 0)}")
    w(f"- **Avg overlap:** {coverage['avg_overlap']} abaci/zip")
    w(f"- **Max overlap:** {coverage['max_overlap']}")
    w()

    # --- Abaci Summary Table ---
    w("## Abaci Summary")
    w()
    w("| # | Name | Domain | W | B | Axis Distribution |")
    w("|---|------|--------|---|---|-------------------|")
    for ab in abaci_data:
        dist = axis_distribution(ab["working_zips"], all_zips)
        dist_str = " ".join(
            f"{ae}{int(pct*100)}%" for ae, pct in dist.items() if pct > 0
        )
        w(f"| {ab['id']:02d} | {ab['name']} | {ab['domain']} | "
          f"{len(ab['working_zips'])} | {len(ab['bonus_zips'])} | {dist_str} |")
    w()

    # --- Per-Abacus Detail ---
    w("## Abacus Detail")
    w()
    for ab in abaci_data:
        w(f"### {ab['id']:02d}. {ab['name']}")
        w(f"*{ab['description']}* | Domain: {ab['domain']} | Bias: {ab['axis_bias']}")
        w()

        # Working zips
        w("**Working Slots (35):**")
        w()
        w("| # | Zip | Order | Type | Axis | Color |")
        w("|---|-----|-------|------|------|-------|")
        for i, nz in enumerate(ab["working_zips"], 1):
            z = zip_by_num.get(nz)
            if z:
                oe = z["order"]["emoji"]
                te = z["type"]["emoji"]
                ae = z["axis"]["emoji"]
                ce = z["color"]["emoji"]
                w(f"| {i} | {nz} | {oe} {ORDER_NAMES.get(oe,'')} | "
                  f"{te} {TYPE_NAMES.get(te,'')} | "
                  f"{ae} {AXIS_NAMES.get(ae,'')} | "
                  f"{ce} {COLOR_NAMES.get(ce,'')} |")
        w()

        # Bonus zips
        w("**Bonus Slots (13):**")
        w()
        w("| # | Zip | Role | Order | Type | Axis | Color |")
        w("|---|-----|------|-------|------|------|-------|")
        for i, b in enumerate(ab["bonus_zips"], 1):
            nz = b["zip"]
            z = zip_by_num.get(nz)
            if z:
                oe = z["order"]["emoji"]
                te = z["type"]["emoji"]
                ae = z["axis"]["emoji"]
                ce = z["color"]["emoji"]
                w(f"| {i} | {nz} | {b['role']} | {oe} {ORDER_NAMES.get(oe,'')} | "
                  f"{te} {TYPE_NAMES.get(te,'')} | "
                  f"{ae} {AXIS_NAMES.get(ae,'')} | "
                  f"{ce} {COLOR_NAMES.get(ce,'')} |")
        w()
        w("---")
        w()

    # --- DLC Packs ---
    if dlc_packs:
        w("## DLC Expansion Packs")
        w()
        w(f"{len(dlc_packs)} packs, {dlc_total} total zips.")
        w()
        for p in dlc_packs:
            w(f"### {p['id']}: {p['name']}")
            w(f"*{p['description']}* | {p['size']} zips")
            w()
            w("| Zip | Order | Type | Axis | Color |")
            w("|-----|-------|------|------|-------|")
            for nz in p["zips"]:
                z = zip_by_num.get(nz)
                if z:
                    oe = z["order"]["emoji"]
                    te = z["type"]["emoji"]
                    ae = z["axis"]["emoji"]
                    ce = z["color"]["emoji"]
                    w(f"| {nz} | {oe} {ORDER_NAMES.get(oe,'')} | "
                      f"{te} {TYPE_NAMES.get(te,'')} | "
                      f"{ae} {AXIS_NAMES.get(ae,'')} | "
                      f"{ce} {COLOR_NAMES.get(ce,'')} |")
            w()
            w("---")
            w()

    # --- Zip Lookup Index ---
    w("## Zip Lookup Index")
    w()
    w("Every zip code and its assignment.")
    w()
    w("| Zip | Emoji | Assignment | Slot |")
    w("|-----|-------|------------|------|")

    # Build lookup
    zip_assignment: dict[str, tuple[str, str]] = {}
    for ab in abaci_data:
        for nz in ab["working_zips"]:
            zip_assignment[nz] = (f"{ab['id']:02d} {ab['name']}", "working")
        for b in ab["bonus_zips"]:
            nz = b["zip"]
            if nz not in zip_assignment:
                zip_assignment[nz] = (f"{ab['id']:02d} {ab['name']}", f"bonus ({b['role']})")
    for p in dlc_packs:
        for nz in p["zips"]:
            if nz not in zip_assignment:
                zip_assignment[nz] = (p["name"], "dlc")

    for nz in sorted(zip_by_num.keys()):
        z = zip_by_num[nz]
        emoji_zip = (z["order"]["emoji"] + z["axis"]["emoji"]
                     + z["type"]["emoji"] + z["color"]["emoji"])
        assignment, slot = zip_assignment.get(nz, ("UNASSIGNED", "—"))
        w(f"| {nz} | {emoji_zip} | {assignment} | {slot} |")
    w()

    # --- Coverage Statistics ---
    w("## Coverage Statistics")
    w()
    overlap = coverage.get("overlap_histogram", {})
    if overlap:
        w("### Overlap Distribution")
        w()
        w("| Abaci Count | Zip Count |")
        w("|-------------|-----------|")
        for k in sorted(overlap.keys()):
            w(f"| {k} | {overlap[k]} |")
        w()

    # Free agent breakdown
    free_agent_zips = coverage.get("free_agent_zips", [])
    if free_agent_zips:
        w("### Free Agent Breakdown (before DLC clustering)")
        w()
        w("| Order | Count |")
        w("|-------|-------|")
        by_order: dict[str, int] = Counter()
        for nz in free_agent_zips:
            z = zip_by_num.get(nz)
            if z:
                by_order[z["order"]["emoji"]] += 1
        for oe in ORDER_EMOJIS:
            c = by_order.get(oe, 0)
            if c > 0:
                w(f"| {oe} {ORDER_NAMES[oe]} | {c} |")
        w()

    # Write file
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"📄 Report written to {report_path}")


def load_existing():
    if not OUTPUT_PATH.exists():
        print(f"❌ No existing registry at {OUTPUT_PATH}")
        sys.exit(1)
    data = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    return data["abaci"], data.get("dlc_packs", []), data.get("coverage", {})


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Compile 35 training abaci from the 1,680 zip registry"
    )
    parser.add_argument("--stats", action="store_true",
                        help="Print report from existing JSON (no recompile)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Compile and report but skip JSON write")
    parser.add_argument("--report", nargs="?", const="default", default=None,
                        help="Write full markdown report (optional: path)")
    args = parser.parse_args()

    all_zips = load_zip_registry()

    if args.stats:
        abaci_data, dlc_packs, coverage = load_existing()
        # Rebuild overlap histogram from data
        zip_abacus_count = Counter()
        for ab in abaci_data:
            for nz in ab["working_zips"]:
                zip_abacus_count[nz] += 1
            for b in ab["bonus_zips"]:
                zip_abacus_count[b["zip"]] += 1
        coverage["overlap_histogram"] = dict(sorted(Counter(zip_abacus_count.values()).items()))
        print_report(abaci_data, all_zips, coverage, dlc_packs)
        if args.report is not None:
            rp = None if args.report == "default" else Path(args.report)
            write_report(abaci_data, dlc_packs, all_zips, coverage, rp)
        return

    abaci_data, dlc_packs, coverage = compile_abaci()
    print_report(abaci_data, all_zips, coverage, dlc_packs)

    if args.report is not None:
        rp = None if args.report == "default" else Path(args.report)
        write_report(abaci_data, dlc_packs, all_zips, coverage, rp)

    if not args.dry_run:
        write_output(abaci_data, dlc_packs, coverage)


if __name__ == "__main__":
    main()
