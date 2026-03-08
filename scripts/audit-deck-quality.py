#!/usr/bin/env python3
"""
audit-deck-quality.py — PPL± Layer 3 Quality Audit

Scores each generated card across 6 dimensions:
  1. Color Compliance    — Does the card honor Color-specific rules?
  2. Exercise-Type Accuracy — Do exercises match the Type's muscle groups?
  3. Parameter Correctness  — Do load%, reps, rest match Order ceilings?
  4. Block Sequence Validity — Does block sequence match Order×Color guidelines?
  5. Content Depth          — Is the card substantive or template-thin?
  6. Format Completeness    — All 15 required elements present?

Usage:
  python scripts/audit-deck-quality.py cards/🦋-hypertrophy/🏛-basics/  # single deck
  python scripts/audit-deck-quality.py cards/                            # all decks
  python scripts/audit-deck-quality.py cards/ --format json              # machine output
  python scripts/audit-deck-quality.py cards/ --format csv               # coverage database
  python scripts/audit-deck-quality.py cards/ --format json --out reports/audit.json

Exit 0 always (audit tool, not gate). Scores indicate quality.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

# ── SCL Constants ──────────────────────────────────────────────────────────

ORDERS = ['🐂', '⛽', '🦋', '🏟', '🌾', '⚖', '🖼']
AXES   = ['🏛', '🔨', '🌹', '🪐', '⌛', '🐬']
TYPES  = ['🛒', '🪡', '🍗', '➕', '➖']
COLORS = ['⚫', '🟢', '🔵', '🟣', '🔴', '🟠', '🟡', '⚪']

ORDER_NAMES = {'🐂': 'Foundation', '⛽': 'Strength', '🦋': 'Hypertrophy',
               '🏟': 'Performance', '🌾': 'Full Body', '⚖': 'Balance', '🖼': 'Restoration'}
AXIS_NAMES = {'🏛': 'Basics', '🔨': 'Functional', '🌹': 'Aesthetic',
              '🪐': 'Challenge', '⌛': 'Time', '🐬': 'Partner'}
TYPE_NAMES = {'🛒': 'Push', '🪡': 'Pull', '🍗': 'Legs', '➕': 'Plus', '➖': 'Ultra'}
COLOR_NAMES = {'⚫': 'Teaching', '🟢': 'Bodyweight', '🔵': 'Structured',
               '🟣': 'Technical', '🔴': 'Intense', '🟠': 'Circuit',
               '🟡': 'Fun', '⚪': 'Mindful'}

BLOCK_EMOJIS = [
    '♨️', '🎯', '🔢', '🧈', '🫀', '▶️', '🎼', '♟️', '🪜', '🌎',
    '🎱', '🌋', '🪞', '🗿', '🛠', '🧩', '🪫', '🏖', '🏗', '🧬',
    '🚂', '🔠'
]

OPERATOR_EMOJIS = ['🧲', '🐋', '🤌', '🧸', '✒️', '🦉', '🥨', '🦢', '📍', '👀', '🪵', '🚀']

# Order parameter ceilings
ORDER_PARAMS = {
    '🐂': {'load_max': 65, 'rep_min': 8, 'rep_max': 15, 'rest_min': 60, 'rest_max': 90,
            'block_min': 4, 'block_max': 6},
    '⛽': {'load_max': 85, 'rep_min': 4, 'rep_max': 6, 'rest_min': 180, 'rest_max': 240,
            'block_min': 5, 'block_max': 6},
    '🦋': {'load_max': 75, 'rep_min': 8, 'rep_max': 12, 'rest_min': 60, 'rest_max': 90,
            'block_min': 6, 'block_max': 7},
    '🏟': {'load_max': 100, 'rep_min': 1, 'rep_max': 3, 'rest_min': 300, 'rest_max': 600,
            'block_min': 3, 'block_max': 4},
    '🌾': {'load_max': 70, 'rep_min': 8, 'rep_max': 10, 'rest_min': 30, 'rest_max': 90,
            'block_min': 5, 'block_max': 6},
    '⚖': {'load_max': 70, 'rep_min': 10, 'rep_max': 12, 'rest_min': 90, 'rest_max': 90,
            'block_min': 5, 'block_max': 6},
    '🖼': {'load_max': 55, 'rep_min': 12, 'rep_max': 15, 'rest_min': 60, 'rest_max': 60,
            'block_min': 4, 'block_max': 5},
}

# Color-specific required and forbidden elements
COLOR_RULES = {
    '⚫': {'required_blocks': [], 'forbidden_equipment': [],
           'required_cues': [], 'notes': 'extended rest, coaching cues'},
    '🟢': {'required_blocks': [], 'forbidden_equipment': ['barbell'],
           'required_cues': [], 'notes': 'no gym required, tier 0-2'},
    '🔵': {'required_blocks': [], 'forbidden_equipment': [],
           'required_cues': [], 'notes': 'prescribed sets/reps/rest'},
    '🟣': {'required_blocks': [], 'forbidden_equipment': [],
           'required_cues': [], 'notes': 'fewer blocks, extended rest, quality focus'},
    '🔴': {'required_blocks': [], 'forbidden_equipment': [],
           'required_cues': [], 'notes': 'reduced rest, supersets OK, gutter permitted'},
    '🟠': {'required_blocks': ['🎱'], 'forbidden_equipment': ['barbell'],
           'required_cues': [], 'notes': 'station-based timed rotation, loop logic'},
    '🟡': {'required_blocks': ['🏖'], 'forbidden_equipment': [],
           'required_cues': [], 'notes': 'exploration, sandbox, variety'},
    '⚪': {'required_blocks': [], 'forbidden_equipment': [],
           'required_cues': ['tempo', 'eccentric', 'breath', 'slow', '4s', '4-sec', 'inhale', 'exhale'],
           'notes': 'slow tempo (4s eccentric), extended rest (2+ min), breath'},
}

# Type → exercise registry scl_types value mapping
TYPE_TO_SCL = {
    '🛒': 'Push',
    '🪡': 'Pull',
    '🍗': 'Legs',
    '➕': 'Plus',
    '➖': 'Ultra',
}

# ── Helpers ────────────────────────────────────────────────────────────────

def parse_frontmatter(content: str):
    lines = content.split('\n')
    if not lines or lines[0].strip() != '---':
        return None, content
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break
    if end_idx is None:
        return None, content
    fm = {}
    for line in lines[1:end_idx]:
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip()
    return fm, '\n'.join(lines[end_idx + 1:])


def parse_zip(zip_str: str):
    s = zip_str.strip()
    result = []
    for emoji_set in [ORDERS, AXES, TYPES, COLORS]:
        matched = False
        for emoji in emoji_set:
            if s.startswith(emoji):
                result.append(emoji)
                s = s[len(emoji):]
                matched = True
                break
        if not matched:
            return None
    return tuple(result) if not s.strip() else None


def extract_exercises(body: str) -> list[str]:
    """Extract exercise names from numbered lines: '├─ 10 🍗 Squat' or '10 🍗 Squat'"""
    exercises = []
    type_emoji_pattern = '(?:' + '|'.join(re.escape(e) for e in TYPES) + ')'
    pattern = re.compile(
        r'^\s*(?:[├│└─\-*•]+\s*)?\d+\s+' + type_emoji_pattern + r'\s+(.+?)(?:\s*\(.*\))?\s*$'
    )
    for line in body.split('\n'):
        m = pattern.match(line)
        if m:
            name = m.group(1).strip()
            name = re.sub(r'\s*\(.*?\)\s*$', '', name).strip()
            name = re.sub(r'\s+at\s+\d+(?:\.\d+)?%\s*$', '', name, flags=re.IGNORECASE).strip()
            name = re.sub(r'\s+[×x]\s+\d+\s*$', '', name).strip()
            if name and len(name) > 2:
                exercises.append(name)
    return exercises


def extract_blocks(body: str) -> list[str]:
    """Extract block emoji headers from the body."""
    blocks = []
    for line in body.split('\n'):
        stripped = line.strip()
        if not stripped.startswith('#'):
            continue
        for emoji in BLOCK_EMOJIS:
            if emoji in stripped:
                blocks.append(emoji)
                break
    return blocks


def extract_intention(body: str) -> str | None:
    """Extract the intention text from blockquote."""
    for line in body.split('\n'):
        stripped = line.strip()
        if stripped.startswith('>') and len(stripped) > 5:
            return stripped[1:].strip().strip('"').strip('"').strip('"')
    return None


def extract_set_lines(body: str) -> list[dict]:
    """
    Extract set prescription lines.
    Pattern: 'Set N: ORDER LOAD% × REPS (context)'
    """
    sets = []
    pattern = re.compile(
        r'Set\s+\d+:\s*(?:' + '|'.join(re.escape(e) for e in ORDERS) + r')\s+'
        r'(\d+(?:\.\d+)?)%\s*[×x]\s*(\d+)'
    )
    for line in body.split('\n'):
        m = pattern.search(line)
        if m:
            sets.append({
                'load': float(m.group(1)),
                'reps': int(m.group(2)),
            })
    return sets


def extract_rest_values(body: str) -> list[int]:
    """Extract rest times in seconds from 'Rest: XXs' lines."""
    rests = []
    pattern = re.compile(r'Rest:\s*(\d+)\s*s', re.IGNORECASE)
    for line in body.split('\n'):
        m = pattern.search(line)
        if m:
            rests.append(int(m.group(1)))
    return rests


def extract_cues(body: str) -> list[str]:
    """Extract parenthetical cues from exercise lines."""
    cues = []
    pattern = re.compile(r'\(([^)]{3,60})\)')
    for line in body.split('\n'):
        for m in pattern.finditer(line):
            cue = m.group(1).strip()
            # Filter out structural markers like "(Warm-Up | Push | Basics | Circuit)"
            if '|' not in cue and not cue.startswith('Set') and not re.match(r'^\d', cue):
                cues.append(cue)
    return cues


def find_barbell_refs(body: str) -> list[str]:
    """Find barbell references in exercise prescription lines."""
    found = []
    type_emoji_pattern = '(?:' + '|'.join(re.escape(e) for e in TYPES) + ')'
    pattern = re.compile(r'^\s*(?:[├│└─\-*•]+\s*)?\d+\s+' + type_emoji_pattern + r'\s+(.+)', re.MULTILINE)
    for m in pattern.finditer(body):
        if 'barbell' in m.group(1).lower():
            found.append(m.group(1).strip()[:60])
    return found


def get_primary_exercise(body: str) -> str | None:
    """Extract the first exercise from the 🧈 Bread & Butter block."""
    lines = body.split('\n')
    in_bb = False
    type_emoji_pattern = '(?:' + '|'.join(re.escape(e) for e in TYPES) + ')'
    ex_pattern = re.compile(r'^\s*(?:[├│└─\-*•]+\s*)?\d+\s+' + type_emoji_pattern + r'\s+(.+?)(?:\s*\(.*\))?\s*$')

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#') and '🧈' in stripped:
            in_bb = True
            continue
        if in_bb:
            if stripped.startswith('#') and any(e in stripped for e in BLOCK_EMOJIS if e != '🧈'):
                break
            m = ex_pattern.match(stripped)
            if m:
                name = re.sub(r'\s*\(.*?\)\s*$', '', m.group(1)).strip()
                if name and len(name) > 2:
                    return name
    # Fallback: check for 🎱 ARAM (Circuit cards)
    in_aram = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#') and '🎱' in stripped:
            in_aram = True
            continue
        if in_aram:
            if stripped.startswith('#') and any(e in stripped for e in BLOCK_EMOJIS if e != '🎱'):
                break
            m = ex_pattern.match(stripped)
            if m:
                name = re.sub(r'\s*\(.*?\)\s*$', '', m.group(1)).strip()
                if name and len(name) > 2:
                    return name
    return None


# ── Exercise Registry Loader ──────────────────────────────────────────────

_exercise_registry = None

def load_exercise_registry(repo_root: str) -> list[dict]:
    global _exercise_registry
    if _exercise_registry is not None:
        return _exercise_registry
    path = os.path.join(repo_root, 'middle-math', 'exercise-registry.json')
    if not os.path.exists(path):
        _exercise_registry = []
        return _exercise_registry
    with open(path, 'r', encoding='utf-8') as f:
        _exercise_registry = json.load(f)
    return _exercise_registry


def build_exercise_type_index(registry: list[dict]) -> dict[str, list[str]]:
    """Build exercise name (lowercase) → list of SCL type names."""
    index = {}
    for entry in registry:
        name = entry.get('canonical_name', entry.get('name', '')).lower().strip()
        scl_types = entry.get('scl_types', [])
        if name:
            index[name] = scl_types
    return index


def lookup_exercise_type(name: str, type_index: dict[str, list[str]]) -> list[str] | None:
    """
    Look up exercise SCL types. Tries exact match, then progressively
    shorter prefixes, then stripped equipment prefixes.
    """
    name_lower = name.lower().strip()

    # Exact match
    if name_lower in type_index:
        return type_index[name_lower]

    # Try without parenthetical
    clean = re.sub(r'\s*\(.*?\)\s*$', '', name_lower).strip()
    if clean in type_index:
        return type_index[clean]

    # Try first N words
    words = name_lower.split()
    for n in range(len(words), 1, -1):
        prefix = ' '.join(words[:n])
        if prefix in type_index:
            return type_index[prefix]

    # Strip equipment prefix
    equip_prefixes = ['barbell', 'dumbbell', 'kettlebell', 'cable', 'machine',
                      'band', 'resistance band', 'plate', 'trap bar', 'smith machine',
                      'ez bar', 'ez-bar', 'landmine']
    for ep in equip_prefixes:
        if name_lower.startswith(ep + ' '):
            stripped = name_lower[len(ep):].strip()
            if stripped in type_index:
                return type_index[stripped]
            # Try without parenthetical
            stripped_clean = re.sub(r'\s*\(.*?\)\s*$', '', stripped).strip()
            if stripped_clean in type_index:
                return type_index[stripped_clean]

    return None


# ── Scoring Functions ──────────────────────────────────────────────────────

def score_color_compliance(body: str, color: str, order: str, blocks: list[str]) -> tuple[int, list[str]]:
    """Score Color compliance (0-100). Returns (score, list of flags)."""
    flags = []
    rules = COLOR_RULES[color]
    score = 100
    penalty_per = 25  # Each violation costs 25 points

    # Check required blocks
    for req_block in rules['required_blocks']:
        if req_block not in blocks:
            flags.append(f"MISSING_BLOCK:{req_block}")
            score -= penalty_per

    # Check forbidden equipment
    if 'barbell' in rules['forbidden_equipment']:
        barbell_refs = find_barbell_refs(body)
        if barbell_refs:
            flags.append(f"FORBIDDEN_BARBELL:{barbell_refs[0][:40]}")
            score -= penalty_per

    # 🟠 Circuit: must have loop logic (no 🧈 — should use 🎱 instead)
    if color == '🟠':
        if '🧈' in blocks and '🎱' not in blocks:
            flags.append("CIRCUIT_NO_ARAM:has_🧈_instead_of_🎱")
            score -= penalty_per
        # Check for station/rotation language
        body_lower = body.lower()
        if not any(kw in body_lower for kw in ['station', 'rotation', 'circuit', 'loop', 'round']):
            flags.append("CIRCUIT_NO_LOOP_LANGUAGE")
            score -= 15

    # ⚪ Mindful: check for tempo/breath cues
    if color == '⚪':
        body_lower = body.lower()
        tempo_found = any(kw in body_lower for kw in rules['required_cues'])
        if not tempo_found:
            flags.append("MINDFUL_NO_TEMPO_CUES")
            score -= penalty_per
        # Check for extended rest (should be 2+ min = 120s+)
        rests = extract_rest_values(body)
        if rests and max(rests) < 120:
            flags.append("MINDFUL_REST_TOO_SHORT")
            score -= 15

    # 🔴 Intense: should have reduced rest
    if color == '🔴':
        rests = extract_rest_values(body)
        if rests and min(rests) > 90:
            flags.append("INTENSE_REST_NOT_REDUCED")
            score -= 15

    # ⚫ Teaching: should have coaching/teaching cues
    if color == '⚫':
        body_lower = body.lower()
        if not any(kw in body_lower for kw in ['coach', 'teach', 'cue', 'learn', 'practice', 'pattern']):
            flags.append("TEACHING_NO_COACHING_CUES")
            score -= 15

    # 🟣 Technical: should have quality/precision language
    if color == '🟣':
        body_lower = body.lower()
        if not any(kw in body_lower for kw in ['precision', 'quality', 'technical', 'mechanic',
                                                 'position', 'control', 'form']):
            flags.append("TECHNICAL_NO_PRECISION_LANGUAGE")
            score -= 10

    # 🟡 Fun: should have variety/exploration language
    if color == '🟡':
        body_lower = body.lower()
        if not any(kw in body_lower for kw in ['variety', 'explore', 'play', 'option', 'choose', 'sandbox']):
            flags.append("FUN_NO_VARIETY_LANGUAGE")
            score -= 10

    return max(0, score), flags


def score_exercise_type_accuracy(body: str, type_emoji: str, type_index: dict[str, list[str]]) -> tuple[int, list[str]]:
    """Score exercise-Type accuracy (0-100). Returns (score, flags)."""
    flags = []
    exercises = extract_exercises(body)
    if not exercises:
        return 50, ['NO_EXERCISES_EXTRACTED']

    expected_type = TYPE_TO_SCL.get(type_emoji, '')
    correct = 0
    checked = 0
    mismatches = []

    for ex_name in exercises:
        scl_types = lookup_exercise_type(ex_name, type_index)
        if scl_types is None:
            continue  # Can't verify — skip
        checked += 1
        if expected_type in scl_types:
            correct += 1
        else:
            mismatches.append(f"{ex_name}→{','.join(scl_types)}")

    if checked == 0:
        return 50, ['NO_EXERCISES_MATCHED_REGISTRY']

    score = int((correct / checked) * 100)
    for mm in mismatches[:5]:
        flags.append(f"TYPE_MISMATCH:{mm}")

    return score, flags


def score_parameter_correctness(body: str, order: str) -> tuple[int, list[str]]:
    """Score parameter correctness against Order ceilings (0-100)."""
    flags = []
    params = ORDER_PARAMS.get(order)
    if not params:
        return 50, ['UNKNOWN_ORDER']

    sets = extract_set_lines(body)
    if not sets:
        return 50, ['NO_SET_LINES_FOUND']

    violations = 0
    total_checks = 0

    for s in sets:
        # Load ceiling check
        total_checks += 1
        if s['load'] > params['load_max']:
            violations += 1
            flags.append(f"LOAD_OVER_CEILING:{s['load']}%>{params['load_max']}%")

        # Rep range check
        total_checks += 1
        if s['reps'] < params['rep_min'] or s['reps'] > params['rep_max']:
            violations += 1
            flags.append(f"REPS_OUT_OF_RANGE:{s['reps']}reps(expected:{params['rep_min']}-{params['rep_max']})")

    if total_checks == 0:
        return 50, ['NO_PARAMS_TO_CHECK']

    score = int(((total_checks - violations) / total_checks) * 100)
    return score, flags


def score_block_sequence(blocks: list[str], order: str, color: str) -> tuple[int, list[str]]:
    """Score block sequence validity (0-100)."""
    flags = []
    score = 100
    params = ORDER_PARAMS.get(order, {})

    # Block count check
    block_min = params.get('block_min', 3)
    block_max = params.get('block_max', 7)

    # Color modifiers
    if color == '🔴':
        block_max += 1
    elif color == '🟠':
        block_min = max(3, block_min - 2)
    elif color == '🟡':
        block_min = max(3, block_min - 1)

    block_count = len(blocks)
    if block_count < block_min or block_count > block_max:
        flags.append(f"BLOCK_COUNT:{block_count}(expected:{block_min}-{block_max})")
        score -= 25

    # Required blocks
    has_save = '🧮' in ''.join(extract_blocks_including_save(blocks))
    # 🧈 or 🎱 required
    if '🧈' not in blocks and '🎱' not in blocks:
        flags.append("MISSING_TRANSFORMATION_ANCHOR")
        score -= 25

    if '🚂' not in blocks:
        flags.append("MISSING_JUNCTION")
        score -= 25

    # 🏟 Performance should have 3-4 blocks only
    if order == '🏟' and block_count > 4:
        flags.append(f"PERFORMANCE_TOO_MANY_BLOCKS:{block_count}")
        score -= 20

    # Color-specific block expectations
    if color == '🟠' and '🎱' not in blocks:
        flags.append("CIRCUIT_MISSING_ARAM")
        score -= 25

    return max(0, score), flags


def extract_blocks_including_save(blocks: list[str]) -> list[str]:
    """Helper that includes 🧮 even though it's not in BLOCK_EMOJIS proper."""
    return blocks


def score_content_depth(body: str, intention: str | None) -> tuple[int, list[str]]:
    """Score content depth (0-100)."""
    flags = []
    score = 100

    # Line count (non-empty lines)
    lines = [l for l in body.split('\n') if l.strip()]
    line_count = len(lines)
    if line_count < 30:
        flags.append(f"THIN_CONTENT:{line_count}_lines")
        score -= 30
    elif line_count < 50:
        flags.append(f"LIGHT_CONTENT:{line_count}_lines")
        score -= 15

    # Unique exercises
    exercises = extract_exercises(body)
    unique_exercises = len(set(e.lower() for e in exercises))
    if unique_exercises < 3:
        flags.append(f"FEW_EXERCISES:{unique_exercises}")
        score -= 20

    # Unique cues
    cues = extract_cues(body)
    unique_cues = len(set(c.lower() for c in cues))
    if unique_cues < 3:
        flags.append(f"FEW_CUES:{unique_cues}")
        score -= 15

    # Generic intention check
    if intention:
        generic_intentions = [
            'drive clean reps',
            'make every set repeatable',
            'own every rep',
            'execute with intent',
        ]
        intention_lower = intention.lower()
        for gi in generic_intentions:
            if gi in intention_lower:
                flags.append(f"GENERIC_INTENTION:{intention[:50]}")
                score -= 20
                break

    return max(0, score), flags


def score_format_completeness(body: str, content: str) -> tuple[int, list[str]]:
    """Score format completeness against 15 required elements (0-100)."""
    flags = []
    present = 0
    total = 15

    # 1. Title with flanking Type emojis
    first_heading = None
    for line in body.split('\n'):
        if line.strip().startswith('# '):
            first_heading = line.strip()
            break
    type_emojis_in_title = sum(1 for t in TYPES if first_heading and t in first_heading) if first_heading else 0
    if type_emojis_in_title >= 2:
        present += 1
    else:
        flags.append("MISSING:flanking_type_emojis_in_title")

    # 2. Subtitle with modality, targets, time
    has_subtitle = bool(re.search(r'##.*·.*\d+.*min', body))
    if has_subtitle:
        present += 1
    else:
        flags.append("MISSING:subtitle_with_time")

    # 3. CODE line
    if '**CODE:**' in body or '**CODE**:' in body:
        present += 1
    else:
        flags.append("MISSING:code_line")

    # 4. 🎯 INTENTION (blockquote)
    has_intention = bool(re.search(r'^>\s*.+', body, re.MULTILINE))
    if has_intention:
        present += 1
    else:
        flags.append("MISSING:intention")

    # 5. Numbered BLOCKS with emoji and ═══
    has_numbered_blocks = bool(re.search(r'##\s*\d+\)', body))
    has_separators = '═══' in body
    if has_numbered_blocks and has_separators:
        present += 1
    else:
        flags.append("MISSING:numbered_blocks_or_separators")

    # 6. Operator call inline after block header
    has_operator = any(op in body for op in OPERATOR_EMOJIS)
    if has_operator:
        present += 1
    else:
        flags.append("MISSING:operator_call")

    # 7. Sub-block zip codes
    sub_block_pattern = re.compile(r'(?:Subcode|Sub-?block):', re.IGNORECASE)
    if sub_block_pattern.search(body):
        present += 1
    else:
        flags.append("MISSING:sub_block_zip_codes")

    # 8. Tree notation (├─ and │)
    if '├─' in body and '│' in body:
        present += 1
    else:
        flags.append("MISSING:tree_notation")

    # 9. Reps before exercise name
    type_emoji_pattern = '(?:' + '|'.join(re.escape(e) for e in TYPES) + ')'
    if re.search(r'\d+\s+' + type_emoji_pattern, body):
        present += 1
    else:
        flags.append("MISSING:reps_before_exercise")

    # 10. Type emoji before exercise name
    if any(t in body for t in TYPES):
        present += 1
    else:
        flags.append("MISSING:type_emoji_before_exercise")

    # 11. Cues in parentheses
    cues = extract_cues(body)
    if len(cues) >= 1:
        present += 1
    else:
        flags.append("MISSING:cues_in_parentheses")

    # 12. Sets on individual lines with Order emoji
    set_pattern = re.compile(r'Set\s+\d+:\s*(?:' + '|'.join(re.escape(e) for e in ORDERS) + r')')
    if set_pattern.search(body):
        present += 1
    else:
        flags.append("MISSING:sets_with_order_emoji")

    # 13. Rest specified
    if re.search(r'Rest:\s*\d+', body, re.IGNORECASE):
        present += 1
    else:
        flags.append("MISSING:rest_specified")

    # 14. 🚂 JUNCTION with next-session zip codes
    if '🚂' in body and ('Next' in body or 'next' in body):
        present += 1
    else:
        flags.append("MISSING:junction_with_next")

    # 15. 🧮 SAVE with closing principle
    if '🧮' in body:
        present += 1
    else:
        flags.append("MISSING:save_block")

    score = int((present / total) * 100)
    return score, flags


# ── Main Card Audit ────────────────────────────────────────────────────────

def audit_card(card_path: str, type_index: dict[str, list[str]]) -> dict | None:
    """Audit a single card. Returns result dict or None for stubs."""
    with open(card_path, 'r', encoding='utf-8') as f:
        content = f.read()

    fm, body = parse_frontmatter(content)
    if fm is None:
        return None

    status = fm.get('status', '').strip()
    if status == 'EMPTY':
        return None  # Skip stubs

    zip_raw = fm.get('zip', '').strip()
    if not zip_raw:
        return None

    parsed = parse_zip(zip_raw)
    if parsed is None:
        return None

    order, axis, type_emoji, color = parsed
    deck = fm.get('deck', '?')

    blocks = extract_blocks(body)
    intention = extract_intention(body)
    primary_exercise = get_primary_exercise(body)
    line_count = len([l for l in body.split('\n') if l.strip()])

    # Score each dimension
    color_score, color_flags = score_color_compliance(body, color, order, blocks)
    type_score, type_flags = score_exercise_type_accuracy(body, type_emoji, type_index)
    param_score, param_flags = score_parameter_correctness(body, order)
    block_score, block_flags = score_block_sequence(blocks, order, color)
    depth_score, depth_flags = score_content_depth(body, intention)
    format_score, format_flags = score_format_completeness(body, content)

    # Overall = weighted average
    overall = int(
        color_score * 0.20 +
        type_score * 0.20 +
        param_score * 0.20 +
        block_score * 0.15 +
        depth_score * 0.15 +
        format_score * 0.10
    )

    all_flags = color_flags + type_flags + param_flags + block_flags + depth_flags + format_flags
    missing_elements = [f for f in format_flags if f.startswith('MISSING:')]

    return {
        'file': os.path.basename(card_path),
        'path': card_path,
        'zip': zip_raw,
        'deck': deck,
        'order': order,
        'order_name': ORDER_NAMES.get(order, '?'),
        'axis': axis,
        'axis_name': AXIS_NAMES.get(axis, '?'),
        'type': type_emoji,
        'type_name': TYPE_NAMES.get(type_emoji, '?'),
        'color': color,
        'color_name': COLOR_NAMES.get(color, '?'),
        'primary_exercise': primary_exercise or '(unknown)',
        'status': status,
        'line_count': line_count,
        'intention': intention or '',
        'scores': {
            'color_compliance': color_score,
            'exercise_type': type_score,
            'parameter': param_score,
            'block_sequence': block_score,
            'content_depth': depth_score,
            'format': format_score,
            'overall': overall,
        },
        'flags': all_flags,
        'missing_elements': missing_elements,
    }


# ── Collection & Reporting ─────────────────────────────────────────────────

def collect_cards(path: str) -> list[str]:
    """Collect all .md card files from a path."""
    cards = []
    for dirpath, _, filenames in os.walk(path):
        for fname in sorted(filenames):
            if fname.endswith('.md') and fname != 'AGENTS.md' and fname != 'README.md':
                cards.append(os.path.join(dirpath, fname))
    return cards


def format_text(results: list[dict], deck_summaries: dict) -> str:
    """Format results as human-readable text."""
    out = []
    out.append("PPL± Deck Quality Audit")
    out.append("═" * 60)
    out.append("")

    # Overall summary
    total = len(results)
    avg_overall = sum(r['scores']['overall'] for r in results) / total if total else 0
    out.append(f"Cards audited: {total}")
    out.append(f"Average overall score: {avg_overall:.0f}/100")
    out.append("")

    # Score distribution
    buckets = {'90-100': 0, '70-89': 0, '50-69': 0, '0-49': 0}
    for r in results:
        s = r['scores']['overall']
        if s >= 90: buckets['90-100'] += 1
        elif s >= 70: buckets['70-89'] += 1
        elif s >= 50: buckets['50-69'] += 1
        else: buckets['0-49'] += 1

    out.append("Score distribution:")
    for bucket, count in buckets.items():
        bar = '█' * (count * 40 // max(total, 1))
        out.append(f"  {bucket:>6}: {count:>4} {bar}")
    out.append("")

    # Dimension averages
    dims = ['color_compliance', 'exercise_type', 'parameter', 'block_sequence', 'content_depth', 'format']
    dim_labels = ['Color Compliance', 'Exercise-Type', 'Parameters', 'Block Sequence', 'Content Depth', 'Format']
    out.append("Dimension averages:")
    for dim, label in zip(dims, dim_labels):
        avg = sum(r['scores'][dim] for r in results) / total if total else 0
        out.append(f"  {label:<20}: {avg:.0f}/100")
    out.append("")

    # Per-deck summary
    if deck_summaries:
        out.append("Per-deck scores:")
        out.append(f"  {'Deck':<8} {'Cards':>5} {'Overall':>8} {'Color':>7} {'Type':>6} {'Param':>6} {'Block':>6} {'Depth':>6} {'Fmt':>5}")
        out.append("  " + "─" * 60)
        for deck_id in sorted(deck_summaries.keys()):
            ds = deck_summaries[deck_id]
            n = ds['count']
            out.append(
                f"  {deck_id:<8} {n:>5} "
                f"{ds['overall']:>7.0f} "
                f"{ds['color_compliance']:>7.0f} "
                f"{ds['exercise_type']:>6.0f} "
                f"{ds['parameter']:>6.0f} "
                f"{ds['block_sequence']:>6.0f} "
                f"{ds['content_depth']:>6.0f} "
                f"{ds['format']:>5.0f}"
            )
        out.append("")

    # Worst 20 cards
    worst = sorted(results, key=lambda r: r['scores']['overall'])[:20]
    out.append("Bottom 20 cards (rebuild priority):")
    out.append(f"  {'Score':>5} {'Zip':<12} {'Color':<12} {'Primary Exercise':<40} Flags")
    out.append("  " + "─" * 90)
    for r in worst:
        top_flags = ', '.join(r['flags'][:3]) if r['flags'] else '—'
        out.append(
            f"  {r['scores']['overall']:>5} "
            f"{r['zip']:<12} "
            f"{r['color_name']:<12} "
            f"{r['primary_exercise'][:40]:<40} "
            f"{top_flags}"
        )
    out.append("")

    # Most common flags
    flag_counts = defaultdict(int)
    for r in results:
        for f in r['flags']:
            # Normalize detailed flags to their category
            category = f.split(':')[0] if ':' in f else f
            flag_counts[category] += 1

    out.append("Most common issues:")
    for flag, count in sorted(flag_counts.items(), key=lambda x: -x[1])[:15]:
        pct = count * 100 / total if total else 0
        out.append(f"  {count:>5} ({pct:>4.0f}%) {flag}")
    out.append("")

    return '\n'.join(out)


def format_csv(results: list[dict]) -> str:
    """Format results as CSV."""
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        'zip', 'deck', 'order', 'axis', 'type', 'color',
        'primary_exercise', 'status', 'line_count',
        'color_compliance', 'exercise_type', 'parameter',
        'block_sequence', 'content_depth', 'format', 'overall',
        'missing_elements', 'flags'
    ])
    for r in results:
        writer.writerow([
            r['zip'], r['deck'], r['order_name'], r['axis_name'],
            r['type_name'], r['color_name'], r['primary_exercise'],
            r['status'], r['line_count'],
            r['scores']['color_compliance'], r['scores']['exercise_type'],
            r['scores']['parameter'], r['scores']['block_sequence'],
            r['scores']['content_depth'], r['scores']['format'],
            r['scores']['overall'],
            ';'.join(r['missing_elements']),
            ';'.join(r['flags']),
        ])
    return output.getvalue()


def format_json(results: list[dict], deck_summaries: dict) -> str:
    """Format results as JSON."""
    total = len(results)
    avg_overall = sum(r['scores']['overall'] for r in results) / total if total else 0
    output = {
        'audit_date': __import__('datetime').date.today().isoformat(),
        'total_cards': total,
        'average_overall': round(avg_overall, 1),
        'deck_summaries': deck_summaries,
        'cards': results,
    }
    return json.dumps(output, ensure_ascii=False, indent=2)


def compute_deck_summaries(results: list[dict]) -> dict:
    """Compute per-deck average scores."""
    by_deck = defaultdict(list)
    for r in results:
        by_deck[r['deck']].append(r)

    summaries = {}
    dims = ['color_compliance', 'exercise_type', 'parameter', 'block_sequence', 'content_depth', 'format', 'overall']
    for deck_id, cards in by_deck.items():
        n = len(cards)
        summary = {'count': n}
        for dim in dims:
            summary[dim] = sum(c['scores'][dim] for c in cards) / n
        summaries[deck_id] = summary
    return summaries


# ── CLI ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='PPL± Layer 3 Quality Audit')
    parser.add_argument('path', help='Card file or deck directory to audit')
    parser.add_argument('--format', choices=['text', 'json', 'csv'], default='text',
                        help='Output format (default: text)')
    parser.add_argument('--out', help='Write output to file instead of stdout')
    args = parser.parse_args()

    # Determine repo root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)

    # Load exercise registry for Type accuracy checking
    registry = load_exercise_registry(repo_root)
    type_index = build_exercise_type_index(registry)
    if not type_index:
        print("⚠️  exercise-registry.json not found — Type accuracy scoring will be limited", file=sys.stderr)

    # Collect cards
    target = args.path
    if os.path.isfile(target):
        card_paths = [target]
    elif os.path.isdir(target):
        card_paths = collect_cards(target)
    else:
        print(f"❌ Path not found: {target}", file=sys.stderr)
        sys.exit(1)

    if not card_paths:
        print("No .md card files found.", file=sys.stderr)
        sys.exit(0)

    # Audit each card
    results = []
    for cp in card_paths:
        result = audit_card(cp, type_index)
        if result is not None:
            results.append(result)

    if not results:
        print("No generated cards found (all stubs?).", file=sys.stderr)
        sys.exit(0)

    # Compute deck summaries
    deck_summaries = compute_deck_summaries(results)

    # Format output
    if args.format == 'csv':
        output = format_csv(results)
    elif args.format == 'json':
        output = format_json(results, deck_summaries)
    else:
        output = format_text(results, deck_summaries)

    # Write output
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Audit written to {args.out}", file=sys.stderr)
    else:
        print(output)


if __name__ == '__main__':
    main()
