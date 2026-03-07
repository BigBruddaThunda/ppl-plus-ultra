#!/usr/bin/env python3
"""Batch-generate all EMPTY cards for a single deck.

This orchestrator handles deterministic file operations and validation while delegating
card prose generation to an AI command (or a local fallback template for testing).
"""

from __future__ import annotations

import argparse
import json
import re
import shlex
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ZIP_REGISTRY = ROOT / "middle-math" / "zip-registry.json"
EXERCISE_LIBRARY = ROOT / "exercise-library.md"
NAMING_CONVENTION = ROOT / "deck-identities" / "naming-convention.md"
VALIDATOR = ROOT / "scripts" / "validate-card.py"
SELECTOR = ROOT / "scripts" / "middle-math" / "exercise_selector.py"
REPORTS_DIR = ROOT / "reports" / "batch-gen"

ORDER_CEILINGS = {
    "🐂": {"load": 65, "reps_min": 8, "reps_max": 15, "difficulty": 2, "blocks_min": 4, "blocks_max": 6},
    "⛽": {"load_min": 75, "load_max": 85, "reps_min": 4, "reps_max": 6, "difficulty": 4, "blocks_min": 5, "blocks_max": 6},
    "🦋": {"load_min": 65, "load_max": 75, "reps_min": 8, "reps_max": 12, "difficulty": 3, "blocks_min": 6, "blocks_max": 7},
    "🏟": {"load_min": 85, "load_max": 100, "reps_min": 1, "reps_max": 3, "difficulty": 5, "blocks_min": 3, "blocks_max": 4},
    "🌾": {"load": 70, "reps_min": 8, "reps_max": 10, "difficulty": 3, "blocks_min": 5, "blocks_max": 6},
    "⚖": {"load": 70, "reps_min": 10, "reps_max": 12, "difficulty": 3, "blocks_min": 5, "blocks_max": 6},
    "🖼": {"load": 55, "reps_min": 12, "reps_max": 15, "difficulty": 2, "blocks_min": 4, "blocks_max": 5},
}

COLOR_TIERS = {
    "⚫": (2, 3), "🟢": (0, 2), "🔵": (2, 3), "🟣": (2, 5),
    "🔴": (2, 4), "🟠": (0, 3), "🟡": (0, 5), "⚪": (0, 3),
}

GOLD_COLORS = {"🟣", "🔴"}
NO_BARBELL = {"🟢", "🟠"}

TYPE_EMOJI = {"Push": "🛒", "Pull": "🪡", "Legs": "🍗", "Plus": "➕", "Ultra": "➖"}

# --- Order-aware generation parameters ---

ORDER_REST = {
    "🐂": {"warmup": "60s", "working": "75s", "main": "75s", "supplemental": "60s"},
    "⛽": {"warmup": "90s", "working": "120s", "main": "180s", "supplemental": "120s"},
    "🦋": {"warmup": "60s", "working": "75s", "main": "90s", "supplemental": "60s"},
    "🏟": {"warmup": "90s", "working": "120s", "main": "Full recovery", "supplemental": "N/A"},
    "🌾": {"warmup": "60s", "working": "60s", "main": "60s", "supplemental": "45s"},
    "⚖": {"warmup": "60s", "working": "75s", "main": "90s", "supplemental": "75s"},
    "🖼": {"warmup": "60s", "working": "60s", "main": "60s", "supplemental": "60s"},
}

ORDER_INTENTIONS = {
    "🐂": "Learn the pattern at sub-maximal load. Own the positions before adding weight.",
    "⛽": "Drive clean reps inside the strength ceiling and make every set repeatable.",
    "🦋": "Build tension through volume. Load serves the muscle, not the ego.",
    "🏟": "Test. Record. Leave. No junk volume after the attempt.",
    "🌾": "Flow through the full body as one integrated pattern.",
    "⚖": "Find the weak link and spend time on it. Correction is the session.",
    "🖼": "Leave fresher than you entered. Recovery is the work.",
}

ORDER_SAVE = {
    "🐂": "The pattern owns the session. Add load only when positions are automatic.",
    "⛽": "Keep the same movement standard and only add load if bar path stays unchanged.",
    "🦋": "Track the pump and the tension. Volume drives growth; form keeps it honest.",
    "🏟": "Record the number. That is the session. Come back when recovered.",
    "🌾": "The flow is the measure. If movements disconnected, simplify next session.",
    "⚖": "The correction is the progress. Symmetry before load, always.",
    "🖼": "Notice what released. Carry that awareness into the next 24 hours.",
}

ORDER_TIME = {
    "🐂": "40-50 min",
    "⛽": "50-65 min",
    "🦋": "55-70 min",
    "🏟": "25-35 min",
    "🌾": "40-55 min",
    "⚖": "40-50 min",
    "🖼": "30-40 min",
}

COLOR_CUES = {
    "⚫": "(coached, check form before adding load)",
    "🟢": "(bodyweight, no external load needed)",
    "🔵": "(prescribed, track sets and reps)",
    "🟣": "(precision, quality over volume)",
    "🔴": "(high effort, push the pace)",
    "🟠": "(station rotation, keep moving)",
    "🟡": "(explore, stay within constraints)",
    "⚪": "(4s eccentric, breath-paced)",
}


@dataclass
class StubCard:
    path: Path
    frontmatter: dict[str, str]
    body: str


@dataclass
class DeckIdentityEntry:
    zip_code: str
    description: str
    primary_exercise: str


def parse_frontmatter(raw: str) -> tuple[dict[str, str], str]:
    lines = raw.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("Missing frontmatter start delimiter")
    end = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end = idx
            break
    if end is None:
        raise ValueError("Missing frontmatter end delimiter")

    frontmatter: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        frontmatter[key.strip()] = val.strip()

    body = "\n".join(lines[end + 1 :]).strip()
    return frontmatter, body


def load_stub(path: Path) -> StubCard:
    raw = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(raw)
    return StubCard(path=path, frontmatter=fm, body=body)


def find_deck_stubs(deck: int) -> list[StubCard]:
    stubs: list[StubCard] = []
    for path in ROOT.glob("cards/**/*.md"):
        if "±.md" not in path.name:
            continue
        stub = load_stub(path)
        status = stub.frontmatter.get("status", "")
        deck_no = int(stub.frontmatter.get("deck", "-1"))
        if status == "EMPTY" and deck_no == deck:
            stubs.append(stub)
    return sorted(stubs, key=lambda s: s.frontmatter.get("zip", ""))


def parse_deck_identity(deck: int) -> dict[str, DeckIdentityEntry]:
    path = ROOT / "deck-identities" / f"deck-{deck:02d}-identity.md"
    if not path.exists():
        raise FileNotFoundError(f"Missing deck identity file: {path}")

    text = path.read_text(encoding="utf-8")
    entries: dict[str, DeckIdentityEntry] = {}
    line_re = re.compile(r"^-\s*(\S+)\s*—\s*(.+?);\s*primary exercise:\s*(.+?)\.?\s*$")
    for line in text.splitlines():
        m = line_re.match(line.strip())
        if not m:
            continue
        zip_code, desc, exercise = m.groups()
        entries[zip_code] = DeckIdentityEntry(zip_code=zip_code, description=desc.strip(), primary_exercise=exercise.strip())

    if len(entries) != 40:
        raise ValueError(f"Deck {deck:02d} identity must contain 40 zip identity lines with primary exercise; found {len(entries)}")
    return entries


def load_zip_registry() -> dict[str, Any]:
    rows = json.loads(ZIP_REGISTRY.read_text(encoding="utf-8"))
    return {row["emoji_zip"]: row for row in rows}


def exercise_in_library(exercise: str, library_text: str) -> bool:
    return exercise.lower() in library_text.lower()


def read_exercise_content(exercise: str) -> str | None:
    slug = re.sub(r"[^a-z0-9]+", "-", exercise.lower()).strip("-")
    for path in (ROOT / "exercise-content").glob("**/*.md"):
        if path.name.lower().startswith(slug):
            return path.read_text(encoding="utf-8")
    return None


def selector_candidates(zip_code: str, top: int = 5) -> list[str]:
    cmd = ["python", str(SELECTOR), "--zip", zip_code, "--top", str(top), "--output", "json"]
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, check=True)
    payload = extract_json_payload(result.stdout)
    data = json.loads(payload)

    names: list[str] = []
    for block in data.get("blocks", []):
        for candidate in block.get("candidates", []):
            name = candidate.get("name")
            if name and name not in names:
                names.append(name)
            if len(names) >= top:
                return names
    return names


def extract_json_payload(text: str) -> str:
    start = text.find("{")
    if start == -1:
        raise ValueError("No JSON object in selector output")
    return text[start:]


def sanitize_title(raw_title: str) -> str:
    title = raw_title.strip().strip("#").strip()
    title = re.sub(r"\s+", " ", title)
    for prefix in ("🛒", "🪡", "🍗", "➕", "➖"):
        title = title.replace(prefix, "")
    title = title.strip(" -")
    title = re.sub(r"[\\/:*?\"<>|]", "", title)
    return title[:120].strip() or "Untitled Workout"


def build_ai_prompt(context: dict[str, Any]) -> str:
    return (
        "Generate a full PPL± workout card markdown for this stub. "
        "Return only markdown content.\n\n"
        f"ZIP: {context['zip']}\n"
        f"Operator: {context['operator']}\n"
        f"Deck identity line: {context['identity_line']}\n"
        f"Primary exercise (must appear in 🧈 or 🎱): {context['primary_exercise']}\n"
        f"Supplemental candidates: {', '.join(context['supplemental'])}\n"
        f"Order constraints: {json.dumps(context['order_ceiling'], ensure_ascii=False)}\n"
        f"Color tier: {context['color_tier']}\n"
        f"GOLD allowed: {context['gold_allowed']}\n"
        f"No barbell: {context['no_barbell']}\n"
        f"Naming convention source: {NAMING_CONVENTION.as_posix()}\n"
        "Must include all 15 required format elements from AGENTS.md and end with 🧮 SAVE."
    )


def run_generator(prompt: str, generator_cmd: str | None, context: dict[str, Any]) -> str:
    if generator_cmd:
        prompt_file = REPORTS_DIR / "prompts" / f"{context['zip']}.txt"
        prompt_file.parent.mkdir(parents=True, exist_ok=True)
        prompt_file.write_text(prompt, encoding="utf-8")

        rendered = generator_cmd.format(
            prompt_file=shlex.quote(str(prompt_file)),
            zip=context["zip"],
            stub_file=shlex.quote(str(context["stub_file"])),
        )
        result = subprocess.run(rendered, cwd=ROOT, shell=True, text=True, capture_output=True)
        if result.returncode != 0:
            raise RuntimeError(f"Generator command failed for {context['zip']}: {result.stderr.strip()}")
        output = result.stdout.strip()
        if not output:
            raise RuntimeError(f"Generator command produced no output for {context['zip']}")
        return output

    return fallback_template(context)


def _get_order_params(ctx: dict[str, Any]) -> dict[str, Any]:
    """Extract working load, reps, rest from Order ceiling."""
    c = ctx["order_ceiling"]
    load = c.get("load", (c.get("load_min", 70) + c.get("load_max", 80)) // 2)
    reps = (c["reps_min"] + c["reps_max"]) // 2
    warmup_load = max(load - 20, 40)
    warmup_reps = min(c["reps_max"], 12)
    rest = ORDER_REST[ctx["order_emoji"]]
    return {"load": load, "reps": reps, "warmup_load": warmup_load, "warmup_reps": warmup_reps, "rest": rest}


def _sub(ctx: dict[str, Any], block_name: str) -> str:
    return f"{ctx['zip']} ({block_name} | {ctx['type_name']} | {ctx['axis_name']} | {ctx['color_name']})"


def _ex(ctx: dict[str, Any], idx: int) -> str:
    """Get supplemental exercise by index, fallback to primary."""
    sups = ctx["supplemental"]
    return sups[idx] if idx < len(sups) else ctx["primary_exercise"]


def _block_warmup(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    cue = COLOR_CUES.get(ctx["color_emoji"], "(steady tempo)")
    return f"""═══
## {num}) ♨️ Warm-Up — {ctx['operator']}
Subcode: {_sub(ctx, 'Warm-Up')}
├─ {p['warmup_reps']} {t} {_ex(ctx, 0)} {cue}
│  Set 1: {ctx['order_emoji']} {p['warmup_load']}% × {p['warmup_reps']} (pattern prep)
Rest: {p['rest']['warmup']}"""


def _block_intention(ctx: dict[str, Any]) -> str:
    intention = ORDER_INTENTIONS.get(ctx["order_emoji"], "Work with purpose.")
    return f"""═══
## 1) 🎯 Intention

> \"{intention}\""""


def _block_fundamentals(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    return f"""═══
## {num}) 🔢 Fundamentals
Subcode: {_sub(ctx, 'Fundamentals')}
├─ {p['warmup_reps']} {t} {_ex(ctx, 1)} (slow, own each position)
│  Set 1: {ctx['order_emoji']} {p['warmup_load']}% × {p['warmup_reps']} (grounding)
│  Set 2: {ctx['order_emoji']} {p['warmup_load'] + 5}% × {p['warmup_reps']} (pattern lock)
Rest: {p['rest']['working']}"""


def _block_primer(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    return f"""═══
## {num}) ▶️ Primer
Subcode: {_sub(ctx, 'Primer')}
├─ {p['reps']} {t} {_ex(ctx, 1)} (tight setup, crisp intent)
│  Set 1: {ctx['order_emoji']} {p['warmup_load'] + 10}% × {p['reps']} (activation)
Rest: {p['rest']['working']}"""


def _block_progression(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    return f"""═══
## {num}) 🪜 Progression
Subcode: {_sub(ctx, 'Progression')}
├─ {p['reps']} {t} {ctx['primary_exercise']} (ramp to test weight)
│  Set 1: {ctx['order_emoji']} {p['load'] - 15}% × {p['reps'] + 1} (opener)
│  Set 2: {ctx['order_emoji']} {p['load'] - 5}% × {p['reps']} (bridge)
Rest: {p['rest']['main']}"""


def _block_composition(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    return f"""═══
## {num}) 🎼 Composition
Subcode: {_sub(ctx, 'Composition')}
├─ {p['reps']} {t} {_ex(ctx, 1)} → {ctx['primary_exercise']} (flow without reset)
│  Set 1: {ctx['order_emoji']} {p['load']}% × {p['reps']} (unified pattern)
│  Set 2: {ctx['order_emoji']} {p['load']}% × {p['reps']} (repeat flow)
Rest: {p['rest']['working']}"""


def _block_reformance(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    return f"""═══
## {num}) 🏗 Reformance
Subcode: {_sub(ctx, 'Reformance')}
├─ {p['reps']} {t} {_ex(ctx, 1)} (corrective, address the weak link)
│  Set 1: {ctx['order_emoji']} {p['warmup_load']}% × {p['reps'] + 2} (prehab)
│  Set 2: {ctx['order_emoji']} {p['warmup_load'] + 5}% × {p['reps']} (stability)
Rest: {p['rest']['working']}"""


def _block_bread_butter(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    cue = COLOR_CUES.get(ctx["color_emoji"], "(clean line, own the bottom)")
    sets = []
    order = ctx["order_emoji"]
    if ctx["order_emoji"] == "🏟":
        sets.append(f"│  Set 1: {order} {p['load']}% × {p['reps']} (test attempt)")
        sets.append(f"│  Set 2: {order} {p['load'] + 5}% × {p['reps']} (max attempt)")
    elif ctx["order_emoji"] == "🖼":
        sets.append(f"│  Set 1: {order} {p['load']}% × {p['reps']} (slow, feel each rep)")
        sets.append(f"│  Set 2: {order} {p['load']}% × {p['reps']} (same tempo, same breath)")
    else:
        sets.append(f"│  Set 1: {order} {p['load'] - 5}% × {p['reps']} (build set)")
        sets.append(f"│  Set 2: {order} {p['load']}% × {p['reps']} (working set)")
        sets.append(f"│  Set 3: {order} {p['load']}% × {p['reps']} (repeat quality)")
    return f"""═══
## {num}) 🧈 Bread & Butter
Subcode: {_sub(ctx, 'Bread & Butter')}
├─ {p['reps']} {t} {ctx['primary_exercise']} {cue}
{chr(10).join(sets)}
Rest: {p['rest']['main']}"""


def _block_sculpt(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    return f"""═══
## {num}) 🗿 Sculpt
Subcode: {_sub(ctx, 'Sculpt')}
├─ {p['reps'] + 2} {t} {_ex(ctx, 2)} (angles, tension, volume)
│  Set 1: {ctx['order_emoji']} {p['load'] - 5}% × {p['reps'] + 2} (shaping)
│  Set 2: {ctx['order_emoji']} {p['load'] - 5}% × {p['reps'] + 2} (carving)
Rest: {p['rest']['supplemental']}"""


def _block_vanity(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    return f"""═══
## {num}) 🪞 Vanity
Subcode: {_sub(ctx, 'Vanity')}
├─ {p['reps'] + 4} {t} {_ex(ctx, 3)} (pump work, mirror muscles, honest)
│  Set 1: {ctx['order_emoji']} {p['load'] - 10}% × {p['reps'] + 4} (accumulation)
│  Set 2: {ctx['order_emoji']} {p['load'] - 10}% × {p['reps'] + 4} (chase the pump)
Rest: {p['rest']['supplemental']}"""


def _block_supplemental(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    return f"""═══
## {num}) 🧩 Supplemental
Subcode: {_sub(ctx, 'Supplemental')}
├─ {p['reps'] + 2} {t} {_ex(ctx, 2)} (full range, different angle)
│  Set 1: {ctx['order_emoji']} {p['load'] - 10}% × {p['reps'] + 2} (support volume)
│  Set 2: {ctx['order_emoji']} {p['load'] - 10}% × {p['reps'] + 2} (non-redundant)
Rest: {p['rest']['supplemental']}"""


def _block_release(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    order = ctx["order_emoji"]
    if order == "🔴" or ctx["color_emoji"] == "🔴":
        cue = "(stress out, cathartic discharge)"
    elif order == "🖼" or ctx["color_emoji"] == "⚪":
        cue = "(parasympathetic, tension down)"
    else:
        cue = "(smooth tempo, downshift)"
    return f"""═══
## {num}) 🪫 Release
Subcode: {_sub(ctx, 'Release')}
├─ 12 {t} {_ex(ctx, 3)} {cue}
│  Set 1: {order} {max(p['load'] - 20, 40)}% × 12 (deload)
Rest: {p['rest']['supplemental']}"""


def _block_imprint(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    return f"""═══
## {num}) 🧬 Imprint
Subcode: {_sub(ctx, 'Imprint')}
├─ {p['reps'] + 4} {t} {_ex(ctx, 4)} (high rep, low load, neural memory)
│  Set 1: {ctx['order_emoji']} {max(p['load'] - 25, 35)}% × {p['reps'] + 4} (lock the pattern)
Rest: {p['rest']['supplemental']}"""


def _block_aram(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    """🎱 ARAM block for 🟠 Circuit — station-based loop with tissue rotation."""
    t = ctx["type_emoji"]
    sups = ctx["supplemental"]
    stations = [ctx["primary_exercise"]] + sups[:3]
    station_lines = []
    for i, ex in enumerate(stations):
        station_lines.append(f"│  Station {i + 1}: {t} {ex} × {p['reps']} {COLOR_CUES['🟠']}")
    return f"""═══
## {num}) 🎱 ARAM — Circuit Loop
Subcode: {_sub(ctx, 'ARAM')}
┌─ 3 rounds, rotate through stations. No two adjacent stations same muscle group.
{chr(10).join(station_lines)}
│  Transition: 15s between stations
│  Round rest: {p['rest']['working']}
Rest: 90s after final round"""


def _block_sandbox(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    return f"""═══
## {num}) 🏖 Sandbox
Subcode: {_sub(ctx, 'Sandbox')}
├─ {p['reps']} {t} {_ex(ctx, 4)} (explore within constraints, structured play)
│  Set 1: {ctx['order_emoji']} {p['load'] - 10}% × {p['reps']} (discovery)
Rest: {p['rest']['supplemental']}"""


def _block_junction(ctx: dict[str, Any], num: int) -> str:
    return f"""═══
## {num}) 🚂 Junction
- Log: load, reps, and form break point.
- Next → {ctx['zip']} — continue at this address.
- Next → [adjacent zip] — explore a neighboring room."""


def _block_save(ctx: dict[str, Any]) -> str:
    save_msg = ORDER_SAVE.get(ctx["order_emoji"], "Log the session and carry the standard forward.")
    return f"""
## 🧮 SAVE
{save_msg}"""


def fallback_template(context: dict[str, Any]) -> str:
    """Generate Order×Color aware workout card template."""
    zip_code = context["zip"]
    t = context.get("type_emoji", TYPE_EMOJI.get(context["type_name"], "🛒"))
    order_e = context["order_emoji"]
    color_e = context["color_emoji"]
    p = _get_order_params(context)
    time_est = ORDER_TIME.get(order_e, "45-55 min")

    title = f"{context['primary_exercise']} — {context['type_name']} {context['color_name']}"
    intention = ORDER_INTENTIONS.get(order_e, "Work with purpose.")

    header = f"""# {t} {title} {t}

## {context['order_name']} {context['axis_name']} — {context['type_name']} focus ({context['color_name']}) · {time_est}

**CODE:** {zip_code}

> \"{intention}\"
"""

    blocks: list[str] = []
    n = 1

    # --- Order-specific block assembly ---

    if order_e == "🐂":  # Foundation: 4-6 blocks
        blocks.append(_block_warmup(context, p, n)); n += 1
        blocks.append(_block_fundamentals(context, p, n)); n += 1
        blocks.append(_block_bread_butter(context, p, n)); n += 1
        if color_e not in ("🟠",):
            blocks.append(_block_supplemental(context, p, n)); n += 1
        blocks.append(_block_imprint(context, p, n)); n += 1
        blocks.append(_block_junction(context, n)); n += 1

    elif order_e == "⛽":  # Strength: 5-6 blocks
        blocks.append(_block_warmup(context, p, n)); n += 1
        blocks.append(_block_primer(context, p, n)); n += 1
        blocks.append(_block_bread_butter(context, p, n)); n += 1
        blocks.append(_block_supplemental(context, p, n)); n += 1
        blocks.append(_block_release(context, p, n)); n += 1
        blocks.append(_block_junction(context, n)); n += 1

    elif order_e == "🦋":  # Hypertrophy: 6-7 blocks
        blocks.append(_block_warmup(context, p, n)); n += 1
        blocks.append(_block_primer(context, p, n)); n += 1
        blocks.append(_block_bread_butter(context, p, n)); n += 1
        blocks.append(_block_sculpt(context, p, n)); n += 1
        if color_e == "🔴":
            blocks.append(_block_vanity(context, p, n)); n += 1
        else:
            blocks.append(_block_supplemental(context, p, n)); n += 1
        blocks.append(_block_release(context, p, n)); n += 1
        blocks.append(_block_junction(context, n)); n += 1

    elif order_e == "🏟":  # Performance: 3-4 blocks ONLY
        blocks.append(_block_warmup(context, p, n)); n += 1
        blocks.append(_block_progression(context, p, n)); n += 1
        blocks.append(_block_bread_butter(context, p, n)); n += 1
        blocks.append(_block_junction(context, n)); n += 1

    elif order_e == "🌾":  # Full Body: 5-6 blocks
        blocks.append(_block_warmup(context, p, n)); n += 1
        blocks.append(_block_composition(context, p, n)); n += 1
        blocks.append(_block_bread_butter(context, p, n)); n += 1
        blocks.append(_block_supplemental(context, p, n)); n += 1
        blocks.append(_block_release(context, p, n)); n += 1
        blocks.append(_block_junction(context, n)); n += 1

    elif order_e == "⚖":  # Balance: 5-6 blocks
        blocks.append(_block_warmup(context, p, n)); n += 1
        blocks.append(_block_reformance(context, p, n)); n += 1
        blocks.append(_block_bread_butter(context, p, n)); n += 1
        blocks.append(_block_supplemental(context, p, n)); n += 1
        blocks.append(_block_release(context, p, n)); n += 1
        blocks.append(_block_junction(context, n)); n += 1

    elif order_e == "🖼":  # Restoration: 4-5 blocks
        blocks.append(_block_intention(context))
        n = 2
        blocks.append(_block_release(context, p, n)); n += 1
        blocks.append(_block_bread_butter(context, p, n)); n += 1
        blocks.append(_block_imprint(context, p, n)); n += 1
        blocks.append(_block_junction(context, n)); n += 1

    else:  # Fallback for unknown Order
        blocks.append(_block_warmup(context, p, n)); n += 1
        blocks.append(_block_bread_butter(context, p, n)); n += 1
        blocks.append(_block_supplemental(context, p, n)); n += 1
        blocks.append(_block_junction(context, n)); n += 1

    # --- Color overrides ---
    # 🟠 Circuit: replace 🧈 Bread & Butter with 🎱 ARAM (validator requires this)
    if color_e == "🟠" and order_e != "🏟":
        new_blocks = []
        for blk in blocks:
            if "🧈 Bread & Butter" in blk:
                aram_num = int(blk.split(")")[0].split("##")[-1].strip())
                new_blocks.append(_block_aram(context, p, aram_num))
            elif "🧩 Supplemental" in blk or "🗿 Sculpt" in blk or "🪞 Vanity" in blk:
                continue  # Drop extra transformation blocks — ARAM absorbs them
            else:
                new_blocks.append(blk)
        blocks = new_blocks

    # 🟡 Fun: add Sandbox before Junction only if block count stays within Order max
    order_blocks_max = ORDER_CEILINGS[order_e].get("blocks_max", 6)
    if color_e == "🟡" and order_e not in ("🏟",) and len(blocks) < order_blocks_max:
        new_blocks = []
        for blk in blocks:
            if "🚂 Junction" in blk:
                sandbox_num = int(blk.split(")")[0].split("##")[-1].strip())
                new_blocks.append(_block_sandbox(context, p, sandbox_num))
                new_blocks.append(blk.replace(f"## {sandbox_num})", f"## {sandbox_num + 1})"))
            else:
                new_blocks.append(blk)
        blocks = new_blocks

    body = header + "\n".join(blocks) + _block_save(context)
    return body


def compose_card(frontmatter: dict[str, str], generated_body: str) -> str:
    updated = dict(frontmatter)
    updated["status"] = "GENERATED"
    fm_lines = ["---"] + [f"{k}: {v}" for k, v in updated.items()] + ["---", ""]
    return "\n".join(fm_lines) + generated_body.strip() + "\n"


def validate_card(path: Path) -> tuple[bool, str]:
    result = subprocess.run(["python", str(VALIDATOR), str(path)], cwd=ROOT, text=True, capture_output=True)
    ok = result.returncode == 0
    output = (result.stdout + "\n" + result.stderr).strip()
    return ok, output


def generate_deck(deck: int, generator_cmd: str | None, limit: int | None, dry_run: bool) -> Path:
    stubs = find_deck_stubs(deck)
    if not stubs:
        raise RuntimeError(f"No EMPTY stubs found for deck {deck:02d}")
    if limit:
        stubs = stubs[:limit]

    identity = parse_deck_identity(deck)
    registry = load_zip_registry()
    lib_text = EXERCISE_LIBRARY.read_text(encoding="utf-8")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_DIR / f"deck-{deck:02d}-validation.md"
    lines = [f"# Deck {deck:02d} Batch Generation Report", "", f"Generated: {datetime.now(timezone.utc).isoformat()}", "", "| Zip | Title | Primary Exercise | Validation | Notes |", "|---|---|---|---|---|"]

    for stub in stubs:
        zip_code = stub.frontmatter.get("zip", "")
        if zip_code not in identity:
            raise RuntimeError(f"Zip {zip_code} missing from deck identity")
        if zip_code not in registry:
            raise RuntimeError(f"Zip {zip_code} missing from zip registry")

        entry = identity[zip_code]
        if not exercise_in_library(entry.primary_exercise, lib_text):
            raise RuntimeError(f"Primary exercise '{entry.primary_exercise}' not found in exercise-library.md")

        meta = registry[zip_code]
        supplemental = selector_candidates(zip_code, top=5)
        context = {
            "zip": zip_code,
            "operator": stub.frontmatter.get("operator", meta["operator"]["emoji"] + " " + meta["operator"]["name"]),
            "identity_line": entry.description,
            "primary_exercise": entry.primary_exercise,
            "supplemental": supplemental,
            "order_emoji": meta["order"]["emoji"],
            "order_name": meta["order"]["name"],
            "axis_emoji": meta["axis"]["emoji"],
            "axis_name": meta["axis"]["name"],
            "type_emoji": TYPE_EMOJI.get(meta["type"]["name"], "🛒"),
            "type_name": meta["type"]["name"],
            "color_emoji": meta["color"]["emoji"],
            "color_name": meta["color"]["name"],
            "order_ceiling": ORDER_CEILINGS[meta["order"]["emoji"]],
            "color_tier": COLOR_TIERS[meta["color"]["emoji"]],
            "gold_allowed": meta["color"]["emoji"] in GOLD_COLORS,
            "no_barbell": meta["color"]["emoji"] in NO_BARBELL,
            "stub_file": stub.path,
            "exercise_content": read_exercise_content(entry.primary_exercise),
        }
        prompt = build_ai_prompt(context)
        generated_body = run_generator(prompt, generator_cmd, context)

        title_line = next((line for line in generated_body.splitlines() if line.strip().startswith("#")), "# Untitled Workout")
        title = sanitize_title(title_line)
        filename = f"{zip_code}±{context['operator'].split()[0]} {title}.md"
        new_path = stub.path.with_name(filename)

        notes = []
        validation = "SKIPPED"
        if dry_run:
            notes.append("dry-run")
        else:
            content = compose_card(stub.frontmatter, generated_body)
            stub.path.write_text(content, encoding="utf-8")
            stub.path.rename(new_path)
            ok, validator_output = validate_card(new_path)
            validation = "PASS" if ok else "FAIL"
            if not ok:
                notes.append(validator_output.replace("\n", " ")[:220])

        lines.append(f"| {zip_code} | {title} | {entry.primary_exercise} | {validation} | {'; '.join(notes)} |")
        print(f"[{deck:02d}] {zip_code}: {title} ({validation})")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Batch generate all EMPTY cards for one deck.")
    parser.add_argument("--deck", type=int, required=True, help="Deck number (1-42)")
    parser.add_argument(
        "--generator-cmd",
        help=(
            "Shell command that returns generated markdown on stdout. "
            "Supports placeholders: {prompt_file}, {zip}, {stub_file}."
        ),
    )
    parser.add_argument("--limit", type=int, help="Process only the first N EMPTY stubs")
    parser.add_argument("--dry-run", action="store_true", help="Do not write cards; still produce report rows")
    args = parser.parse_args()

    report = generate_deck(args.deck, args.generator_cmd, args.limit, args.dry_run)
    print(f"Wrote {report.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
