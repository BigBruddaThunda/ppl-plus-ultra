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

# --- Order×Color Intention Bank (56 unique intentions) ---

INTENTIONS = {
    # 🐂 Foundation
    ("🐂", "⚫"): "Practice the positions slowly. This is a coaching session, not a workout.",
    ("🐂", "🟢"): "Learn the pattern with your own body first. External load comes later.",
    ("🐂", "🔵"): "Follow the prescription. The numbers build the habit.",
    ("🐂", "🟣"): "Quality of position matters more than speed of completion.",
    ("🐂", "🔴"): "Sub-maximal load, high effort. Earn every rep with form.",
    ("🐂", "🟠"): "Rotate through stations at learning pace. Each one is a fresh pattern.",
    ("🐂", "🟡"): "Explore the movement. Find what feels unfamiliar and stay there.",
    ("🐂", "⚪"): "Slow the pattern down until you can feel every joint in the chain.",
    # ⛽ Strength
    ("⛽", "⚫"): "Learn where the bar sits and how it moves before adding plates.",
    ("⛽", "🟢"): "Prove the pattern holds without external load. Bodyweight is the test.",
    ("⛽", "🔵"): "Same weight, same reps, same rest. Build the base one session at a time.",
    ("⛽", "🟣"): "One clean rep at the right load is worth more than five at the wrong one.",
    ("⛽", "🔴"): "Push the ceiling. Every set should cost something real.",
    ("⛽", "🟠"): "Rotate stations. Keep the tissues trading off under heavy demand.",
    ("⛽", "🟡"): "Find a movement you have not tried at this load and own it.",
    ("⛽", "⚪"): "Four seconds down. Feel every degree of the range before you earn the drive.",
    # 🦋 Hypertrophy
    ("🦋", "⚫"): "Learn what tension feels like in the target muscle before chasing volume.",
    ("🦋", "🟢"): "Build the muscle with what you have. No equipment is not an excuse.",
    ("🦋", "🔵"): "Hit every set at the prescribed rep count. Volume is the driver.",
    ("🦋", "🟣"): "Feel the muscle work through the full range. Precision builds tissue.",
    ("🦋", "🔴"): "High volume, low rest. Chase the pump and earn the fatigue.",
    ("🦋", "🟠"): "Circuit the muscle group from every angle. Each station is a new stimulus.",
    ("🦋", "🟡"): "Try exercises you would not normally pick. Variety stimulates growth.",
    ("🦋", "⚪"): "Slow eccentrics under moderate load. Time under tension is the stimulus.",
    # 🏟 Performance
    ("🏟", "⚫"): "Rehearse the test protocol. Know the standards before test day.",
    ("🏟", "🟢"): "Test bodyweight capacity. How many, how fast, how clean.",
    ("🏟", "🔵"): "Execute the test exactly as prescribed. Record the number.",
    ("🏟", "🟣"): "One maximal attempt with perfect setup. The technique is the test.",
    ("🏟", "🔴"): "All-out effort. Leave everything on the platform.",
    ("🏟", "🟠"): "Timed circuit test. Complete as many rounds as the clock allows.",
    ("🏟", "🟡"): "Test something unconventional. Find where your capacity surprises you.",
    ("🏟", "⚪"): "Test movement quality under minimal load. Patience is the metric.",
    # 🌾 Full Body
    ("🌾", "⚫"): "Connect the chain. Coach each transition between movements.",
    ("🌾", "🟢"): "Flow through the body using only what you carry. No equipment needed.",
    ("🌾", "🔵"): "Prescribed flow. Each movement connects to the next without reset.",
    ("🌾", "🟣"): "Precision in the transitions. The connection between movements is the skill.",
    ("🌾", "🔴"): "Drive through the integrated pattern with intent. No wasted motion.",
    ("🌾", "🟠"): "Rotate through full-body stations. Every station moves a different chain.",
    ("🌾", "🟡"): "Explore compound movements that link upper and lower body.",
    ("🌾", "⚪"): "Breathe through the full chain. Each movement flows into the next.",
    # ⚖ Balance
    ("⚖", "⚫"): "Identify the weak link. Coach the correction before adding load.",
    ("⚖", "🟢"): "Find asymmetries with bodyweight. No equipment hides the gap.",
    ("⚖", "🔵"): "Prescribed accessory work. Target the specific imbalance.",
    ("⚖", "🟣"): "Precise correction. Small movements, full attention, zero momentum.",
    ("⚖", "🔴"): "Attack the weak link with volume. Fatigue exposes the gap.",
    ("⚖", "🟠"): "Rotate through corrective stations. Each one targets a different deficit.",
    ("⚖", "🟡"): "Explore movements that challenge your weakest positions.",
    ("⚖", "⚪"): "Slow down into the imbalance. Feel where the body compensates.",
    # 🖼 Restoration
    ("🖼", "⚫"): "Learn what recovery feels like. This is a teaching session for your nervous system.",
    ("🖼", "🟢"): "Restore with what your body provides. Floor work, breath, gentle movement.",
    ("🖼", "🔵"): "Follow the restoration sequence as prescribed. Each position has a purpose.",
    ("🖼", "🟣"): "Precise positioning in each restorative hold. Depth over speed.",
    ("🖼", "🔴"): "Active recovery. Move enough to flush, not enough to fatigue.",
    ("🖼", "🟠"): "Rotate through restoration stations. Each one addresses a different tissue.",
    ("🖼", "🟡"): "Explore somatic movements you would not normally try.",
    ("🖼", "⚪"): "Breathe into each position. Leave fresher than you entered.",
}

# --- Order×Color SAVE Bank (56 unique closings) ---

SAVE_MESSAGES = {
    # 🐂 Foundation
    ("🐂", "⚫"): "The positions own the session. Add complexity only when coaching cues become automatic.",
    ("🐂", "🟢"): "If the pattern held at bodyweight, it will hold under load. Graduate when ready.",
    ("🐂", "🔵"): "Log the numbers. Consistency at sub-maximal load builds the strongest base.",
    ("🐂", "🟣"): "Note which positions felt uncertain. Those are your next session's priority.",
    ("🐂", "🔴"): "Effort at low load reveals form breaks. Fix them before adding weight.",
    ("🐂", "🟠"): "Review which station felt least stable. That pattern needs more reps.",
    ("🐂", "🟡"): "What felt unfamiliar today becomes familiar next session. Return to it.",
    ("🐂", "⚪"): "Slow tempo teaches the nervous system. Carry that awareness forward.",
    # ⛽ Strength
    ("⛽", "⚫"): "Note the coaching cues that changed the movement. Build from those.",
    ("⛽", "🟢"): "Bodyweight strength is the transfer test. If it held, the gym work is real.",
    ("⛽", "🔵"): "Keep the same movement standard. Only add load if bar path stays unchanged.",
    ("⛽", "🟣"): "Log bar path quality, not just the weight. The how matters as much as the how much.",
    ("⛽", "🔴"): "Record peak effort. Recovery before next heavy session.",
    ("⛽", "🟠"): "Log station completion times. Consistency matters more than speed.",
    ("⛽", "🟡"): "Note what you tried and what surprised you. Build on it next session.",
    ("⛽", "⚪"): "Slow strength builds tendons, not just muscles. Trust the tempo.",
    # 🦋 Hypertrophy
    ("🦋", "⚫"): "Track the pump and the tension. Learning to feel the muscle is the skill.",
    ("🦋", "🟢"): "Bodyweight hypertrophy works when tempo and volume are honest. Log both.",
    ("🦋", "🔵"): "Volume drives growth; form keeps it honest. Log sets, reps, and load.",
    ("🦋", "🟣"): "Note which reps had the best mind-muscle connection. Chase that feeling.",
    ("🦋", "🔴"): "High volume earned today recovers into growth tomorrow. Eat and sleep.",
    ("🦋", "🟠"): "Circuit hypertrophy works through cumulative fatigue. Note which station failed first.",
    ("🦋", "🟡"): "New exercises recruit new motor units. Track what felt different.",
    ("🦋", "⚪"): "Slow eccentrics build tissue that fast reps miss. Trust the tempo.",
    # 🏟 Performance
    ("🏟", "⚫"): "Understand the test protocol. Next session is the real attempt.",
    ("🏟", "🟢"): "Record the bodyweight test number. That is the session.",
    ("🏟", "🔵"): "Record the number. That is the session. Come back when recovered.",
    ("🏟", "🟣"): "Log the attempt and the technique notes. Both are the data.",
    ("🏟", "🔴"): "The test is complete. Recovery is the next priority.",
    ("🏟", "🟠"): "Record rounds completed and form break point. That is the benchmark.",
    ("🏟", "🟡"): "Note what you tested and the result. New benchmarks start here.",
    ("🏟", "⚪"): "Movement quality under observation is its own test. Log what you saw.",
    # 🌾 Full Body
    ("🌾", "⚫"): "Note which transitions felt disconnected. Coach those links next session.",
    ("🌾", "🟢"): "Flow at bodyweight reveals coordination. Log the movement quality.",
    ("🌾", "🔵"): "The flow is the measure. If movements disconnected, simplify next session.",
    ("🌾", "🟣"): "Note the weakest transition. That is where the chain needs work.",
    ("🌾", "🔴"): "Integrated effort under fatigue reveals the real pattern. Log the breakdown point.",
    ("🌾", "🟠"): "Full-body circuit hits every chain. Note which station caused the most fatigue.",
    ("🌾", "🟡"): "Compound discovery teaches the body new links. Track what connected.",
    ("🌾", "⚪"): "Breathe through the chain. The flow improves as the nervous system calms.",
    # ⚖ Balance
    ("⚖", "⚫"): "The coaching eye found the weak link. Now the correction begins.",
    ("⚖", "🟢"): "Bodyweight exposed the asymmetry. Note which side lagged.",
    ("⚖", "🔵"): "The correction is the progress. Symmetry before load, always.",
    ("⚖", "🟣"): "Precision in correction builds the foundation. Note what changed.",
    ("⚖", "🔴"): "Volume on the weak side closes the gap. Log the difference between sides.",
    ("⚖", "🟠"): "Corrective circuit attacked the deficit from every angle. Note what improved.",
    ("⚖", "🟡"): "Exploring weak positions teaches the body new ranges. Track the discovery.",
    ("⚖", "⚪"): "Slow correction lets the nervous system rewrite the pattern. Trust the process.",
    # 🖼 Restoration
    ("🖼", "⚫"): "Learning to recover is a skill. Note which positions brought the most relief.",
    ("🖼", "🟢"): "Floor work and breath are always available. Use them daily.",
    ("🖼", "🔵"): "Follow the restoration protocol consistently. Recovery compounds.",
    ("🖼", "🟣"): "Precise positioning in restorative holds teaches the body to let go.",
    ("🖼", "🔴"): "Active recovery flushes fatigue. Note what felt better after moving.",
    ("🖼", "🟠"): "Each restoration station addressed a different tissue. Note what released.",
    ("🖼", "🟡"): "Somatic exploration teaches the body things the gym never will.",
    ("🖼", "⚪"): "Notice what released. Carry that awareness into the next 24 hours.",
}

# Legacy accessors — kept for backward compatibility with external tools
ORDER_INTENTIONS = {k[0]: v for k, v in INTENTIONS.items() if k[1] == "🔵"}
ORDER_SAVE = {k[0]: v for k, v in SAVE_MESSAGES.items() if k[1] == "🔵"}

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


COLOR_REST_MODIFIER = {
    "⚫": 1.5,   # Teaching: +50% rest
    "⚪": 2.0,   # Mindful: double rest (minimum 120s)
    "🟣": 1.5,   # Technical: +50% rest
    "🔴": 0.5,   # Intense: halve rest
    "🟠": 0.5,   # Circuit: half rest
}

# --- Exercise registry cache ---
_EXERCISE_REGISTRY: list[dict] | None = None

def _load_registry() -> list[dict]:
    global _EXERCISE_REGISTRY
    if _EXERCISE_REGISTRY is None:
        path = ROOT / "middle-math" / "exercise-registry.json"
        _EXERCISE_REGISTRY = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    return _EXERCISE_REGISTRY

def _exercise_matches_type(name: str, expected_type: str) -> bool:
    """Check if an exercise's scl_types includes the expected Type."""
    name_lower = name.lower().strip()
    for entry in _load_registry():
        if entry.get("canonical_name", "").lower() == name_lower:
            return expected_type in entry.get("scl_types", [])
    return True  # Not found → allow (avoid false negatives)

def _filter_exercises_for_type(exercises: list[str], expected_type: str) -> list[str]:
    """Remove exercises that don't match the expected Type."""
    return [e for e in exercises if _exercise_matches_type(e, expected_type)]

def _has_barbell(name: str) -> bool:
    """Check if an exercise uses a barbell."""
    name_lower = name.lower().strip()
    for entry in _load_registry():
        if entry.get("canonical_name", "").lower() == name_lower:
            equip = entry.get("equipment_primary", "").lower()
            return "barbell" in equip
    return "barbell" in name_lower  # Fallback: string check

def _filter_no_barbell(exercises: list[str]) -> list[str]:
    """Remove barbell exercises from candidate list."""
    return [e for e in exercises if not _has_barbell(e)]


def _clamp_reps(reps: int, order_e: str) -> int:
    """Clamp reps to Order's allowed range."""
    c = ORDER_CEILINGS[order_e]
    return max(c["reps_min"], min(reps, c["reps_max"]))

def _clamp_load(load: float, order_e: str) -> float:
    """Clamp load to Order's max ceiling."""
    c = ORDER_CEILINGS[order_e]
    return min(load, c.get("load_max", c.get("load", 100)))

def _apply_rest(rest_str: str, color_e: str) -> str:
    """Apply Color rest modifier to a rest string like '90s'."""
    modifier = COLOR_REST_MODIFIER.get(color_e, 1.0)
    match = re.match(r"(\d+)s?", rest_str)
    if not match:
        return rest_str
    base = int(match.group(1))
    adjusted = max(30, int(base * modifier))
    # Mindful minimum 120s
    if color_e == "⚪":
        adjusted = max(120, adjusted)
    return f"{adjusted}s"


def _get_order_params(ctx: dict[str, Any]) -> dict[str, Any]:
    """Extract working load, reps, rest from Order ceiling with Color modifications."""
    c = ctx["order_ceiling"]
    load = c.get("load", (c.get("load_min", 70) + c.get("load_max", 80)) // 2)
    reps = (c["reps_min"] + c["reps_max"]) // 2
    warmup_load = max(load - 20, 40)
    warmup_reps = min(c["reps_max"], 12)
    color_e = ctx.get("color_emoji", "🔵")
    base_rest = ORDER_REST[ctx["order_emoji"]]
    rest = {k: _apply_rest(v, color_e) for k, v in base_rest.items()}
    return {"load": load, "reps": reps, "warmup_load": warmup_load, "warmup_reps": warmup_reps, "rest": rest}


def _sub(ctx: dict[str, Any], block_name: str) -> str:
    return f"{ctx['zip']} ({block_name} | {ctx['type_name']} | {ctx['axis_name']} | {ctx['color_name']})"


def _ex(ctx: dict[str, Any], idx: int) -> str:
    """Get supplemental exercise by index, fallback to primary."""
    sups = ctx["supplemental"]
    return sups[idx] if idx < len(sups) else ctx["primary_exercise"]


def _warmup_exercise(ctx: dict[str, Any]) -> str:
    """Get warm-up exercise, respecting barbell restrictions."""
    ex = _ex(ctx, 0)
    if ctx.get("no_barbell") and _has_barbell(ex):
        # Try other supplementals
        for i in range(1, 5):
            alt = _ex(ctx, i)
            if not _has_barbell(alt):
                return alt
        return ctx["primary_exercise"]  # fallback (should already be filtered)
    return ex


def _block_warmup(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    cue = COLOR_CUES.get(ctx["color_emoji"], "(steady tempo)")
    exercise = _warmup_exercise(ctx)
    return f"""═══
## {num}) ♨️ Warm-Up — {ctx['operator']}
Subcode: {_sub(ctx, 'Warm-Up')}
├─ {p['warmup_reps']} {t} {exercise} {cue}
│  Set 1: {ctx['order_emoji']} {p['warmup_load']}% × {p['warmup_reps']} (pattern prep)
Rest: {p['rest']['warmup']}"""


def _block_intention(ctx: dict[str, Any]) -> str:
    key = (ctx["order_emoji"], ctx["color_emoji"])
    intention = INTENTIONS.get(key, INTENTIONS.get((ctx["order_emoji"], "🔵"), "Work with purpose."))
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
    opener_reps = _clamp_reps(p['reps'] + 1, ctx["order_emoji"])
    return f"""═══
## {num}) 🪜 Progression
Subcode: {_sub(ctx, 'Progression')}
├─ {p['reps']} {t} {ctx['primary_exercise']} (ramp to test weight)
│  Set 1: {ctx['order_emoji']} {p['load'] - 15}% × {opener_reps} (opener)
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
    reps = _clamp_reps(p['reps'] + 2, ctx["order_emoji"])
    return f"""═══
## {num}) 🏗 Reformance
Subcode: {_sub(ctx, 'Reformance')}
├─ {p['reps']} {t} {_ex(ctx, 1)} (corrective, address the weak link)
│  Set 1: {ctx['order_emoji']} {p['warmup_load']}% × {reps} (prehab)
│  Set 2: {ctx['order_emoji']} {p['warmup_load'] + 5}% × {p['reps']} (stability)
Rest: {p['rest']['working']}"""


def _block_bread_butter(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    cue = COLOR_CUES.get(ctx["color_emoji"], "(clean line, own the bottom)")
    sets = []
    order = ctx["order_emoji"]
    if ctx["order_emoji"] == "🏟":
        max_load = int(_clamp_load(p['load'] + 5, ctx["order_emoji"]))
        sets.append(f"│  Set 1: {order} {p['load']}% × {p['reps']} (test attempt)")
        sets.append(f"│  Set 2: {order} {max_load}% × {p['reps']} (max attempt)")
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
    reps = _clamp_reps(p['reps'] + 2, ctx["order_emoji"])
    load = _clamp_load(p['load'] - 5, ctx["order_emoji"])
    return f"""═══
## {num}) 🗿 Sculpt
Subcode: {_sub(ctx, 'Sculpt')}
├─ {reps} {t} {_ex(ctx, 2)} (angles, tension, volume)
│  Set 1: {ctx['order_emoji']} {load}% × {reps} (shaping)
│  Set 2: {ctx['order_emoji']} {load}% × {reps} (carving)
Rest: {p['rest']['supplemental']}"""


def _block_vanity(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    reps = _clamp_reps(p['reps'] + 4, ctx["order_emoji"])
    load = _clamp_load(max(p['load'] - 10, 40), ctx["order_emoji"])
    return f"""═══
## {num}) 🪞 Vanity
Subcode: {_sub(ctx, 'Vanity')}
├─ {reps} {t} {_ex(ctx, 3)} (pump work, mirror muscles, honest)
│  Set 1: {ctx['order_emoji']} {load}% × {reps} (accumulation)
│  Set 2: {ctx['order_emoji']} {load}% × {reps} (chase the pump)
Rest: {p['rest']['supplemental']}"""


def _block_supplemental(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    reps = _clamp_reps(p['reps'] + 2, ctx["order_emoji"])
    load = _clamp_load(max(p['load'] - 10, 40), ctx["order_emoji"])
    return f"""═══
## {num}) 🧩 Supplemental
Subcode: {_sub(ctx, 'Supplemental')}
├─ {reps} {t} {_ex(ctx, 2)} (full range, different angle)
│  Set 1: {ctx['order_emoji']} {load}% × {reps} (support volume)
│  Set 2: {ctx['order_emoji']} {load}% × {reps} (non-redundant)
Rest: {p['rest']['supplemental']}"""


def _block_release(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    order = ctx["order_emoji"]
    color = ctx["color_emoji"]
    if color == "🔴":
        cue = "(stress out, cathartic discharge)"
    elif color == "⚪" or order == "🖼":
        cue = "(parasympathetic, tension down, 4s eccentric)"
    else:
        cue = "(smooth tempo, downshift)"
    reps = _clamp_reps(12, order)
    load = _clamp_load(max(p['load'] - 20, 40), order)
    return f"""═══
## {num}) 🪫 Release
Subcode: {_sub(ctx, 'Release')}
├─ {reps} {t} {_ex(ctx, 3)} {cue}
│  Set 1: {order} {load}% × {reps} (deload)
Rest: {p['rest']['supplemental']}"""


def _block_imprint(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    t = ctx["type_emoji"]
    reps = _clamp_reps(p['reps'] + 4, ctx["order_emoji"])
    load = _clamp_load(max(p['load'] - 25, 35), ctx["order_emoji"])
    return f"""═══
## {num}) 🧬 Imprint
Subcode: {_sub(ctx, 'Imprint')}
├─ {reps} {t} {_ex(ctx, 4)} (high rep, low load, neural memory)
│  Set 1: {ctx['order_emoji']} {load}% × {reps} (lock the pattern)
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
    reps = _clamp_reps(p['reps'], ctx["order_emoji"])
    load = _clamp_load(max(p['load'] - 10, 40), ctx["order_emoji"])
    return f"""═══
## {num}) 🏖 Sandbox
Subcode: {_sub(ctx, 'Sandbox')}
├─ {reps} {t} {_ex(ctx, 4)} (explore within constraints, choose your variation)
│  Option A: {ctx['order_emoji']} {load}% × {reps} (play with grip, stance, or tempo)
│  Option B: {ctx['order_emoji']} {load}% × {reps} (try a variation you have not used before)
Rest: {p['rest']['supplemental']}"""


def _block_craft(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    """🛠 Craft block for ⚫ Teaching — skill acquisition with coaching cues."""
    t = ctx["type_emoji"]
    reps = _clamp_reps(p['reps'], ctx["order_emoji"])
    return f"""═══
## {num}) 🛠 Craft
Subcode: {_sub(ctx, 'Craft')}
├─ {reps} {t} {_ex(ctx, 1)} (coach: check grip width, elbow angle, foot pressure)
│  Set 1: {ctx['order_emoji']} {p['warmup_load']}% × {reps} (practice the pattern, not the load)
│  Set 2: {ctx['order_emoji']} {p['warmup_load'] + 5}% × {reps} (same cues, slightly heavier)
Rest: {p['rest']['working']}"""


def _block_gutter(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    """🌋 Gutter block for 🔴 Intense — all-out effort."""
    t = ctx["type_emoji"]
    reps = _clamp_reps(p['reps'] + 4, ctx["order_emoji"])
    load = _clamp_load(max(p['load'] - 15, 40), ctx["order_emoji"])
    return f"""═══
## {num}) 🌋 Gutter
Subcode: {_sub(ctx, 'Gutter')}
├─ {reps} {t} {_ex(ctx, 3)} (all-out, leave nothing in reserve)
│  Set 1: {ctx['order_emoji']} {load}% × {reps} (push to form break)
│  Set 2: {ctx['order_emoji']} {load}% × AMRAP (final effort)
Rest: 45s"""


def _block_exposure(ctx: dict[str, Any], p: dict[str, Any], num: int) -> str:
    """🌎 Exposure block for 🟡 Fun — reveal weaknesses, expand vocabulary."""
    t = ctx["type_emoji"]
    reps = _clamp_reps(p['reps'], ctx["order_emoji"])
    load = _clamp_load(max(p['load'] - 15, 40), ctx["order_emoji"])
    return f"""═══
## {num}) 🌎 Exposure
Subcode: {_sub(ctx, 'Exposure')}
├─ {reps} {t} {_ex(ctx, 3)} (try the unfamiliar version, explore the range)
│  Set 1: {ctx['order_emoji']} {load}% × {reps} (discovery set)
Rest: {p['rest']['supplemental']}"""


def _block_junction(ctx: dict[str, Any], num: int) -> str:
    return f"""═══
## {num}) 🚂 Junction
- Log: load, reps, and form break point.
- Next → {ctx['zip']} — continue at this address.
- Next → [adjacent zip] — explore a neighboring room."""


def _block_save(ctx: dict[str, Any]) -> str:
    key = (ctx["order_emoji"], ctx["color_emoji"])
    save_msg = SAVE_MESSAGES.get(key, SAVE_MESSAGES.get((ctx["order_emoji"], "🔵"), "Log the session and carry the standard forward."))
    return f"""
## 🧮 SAVE
{save_msg}"""


def _default_blocks(ctx: dict[str, Any], p: dict[str, Any], order_e: str) -> list[str]:
    """Build the default Order-specific block sequence."""
    blocks: list[str] = []
    n = 1
    if order_e == "🐂":
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_fundamentals(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_supplemental(ctx, p, n)); n += 1
        blocks.append(_block_imprint(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    elif order_e == "⛽":
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_primer(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_supplemental(ctx, p, n)); n += 1
        blocks.append(_block_release(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    elif order_e == "🦋":
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_primer(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_sculpt(ctx, p, n)); n += 1
        blocks.append(_block_supplemental(ctx, p, n)); n += 1
        blocks.append(_block_release(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    elif order_e == "🏟":
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_progression(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    elif order_e == "🌾":
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_composition(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_supplemental(ctx, p, n)); n += 1
        blocks.append(_block_release(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    elif order_e == "⚖":
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_reformance(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_supplemental(ctx, p, n)); n += 1
        blocks.append(_block_release(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    elif order_e == "🖼":
        blocks.append(_block_intention(ctx)); n = 2
        blocks.append(_block_release(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_imprint(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    else:
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_supplemental(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    return blocks


def _circuit_blocks(ctx: dict[str, Any], p: dict[str, Any], order_e: str) -> list[str]:
    """🟠 Circuit: ARAM replaces 🧈. No barbells. Station rotation."""
    blocks: list[str] = []
    n = 1
    if order_e == "🏟":
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_aram(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    elif order_e == "🖼":
        blocks.append(_block_intention(ctx)); n = 2
        blocks.append(_block_aram(ctx, p, n)); n += 1
        blocks.append(_block_release(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    else:
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_aram(ctx, p, n)); n += 1
        blocks.append(_block_release(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    return blocks


def _fun_blocks(ctx: dict[str, Any], p: dict[str, Any], order_e: str) -> list[str]:
    """🟡 Fun: Always includes 🏖 Sandbox + 🌎 Exposure where possible."""
    blocks: list[str] = []
    n = 1
    if order_e == "🏟":
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_sandbox(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    elif order_e == "🖼":
        blocks.append(_block_intention(ctx)); n = 2
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_sandbox(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    else:
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_exposure(ctx, p, n)); n += 1
        blocks.append(_block_sandbox(ctx, p, n)); n += 1
        blocks.append(_block_release(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    return blocks


def _mindful_blocks(ctx: dict[str, Any], p: dict[str, Any], order_e: str) -> list[str]:
    """⚪ Mindful: Extended warm-up/release. 4s eccentric. 120s+ rest. Breathing cues."""
    blocks: list[str] = []
    n = 1
    if order_e == "🏟":
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    elif order_e == "🖼":
        blocks.append(_block_intention(ctx)); n = 2
        blocks.append(_block_release(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_imprint(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    else:
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_supplemental(ctx, p, n)); n += 1
        blocks.append(_block_release(ctx, p, n)); n += 1
        blocks.append(_block_imprint(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    return blocks


def _teaching_blocks(ctx: dict[str, Any], p: dict[str, Any], order_e: str) -> list[str]:
    """⚫ Teaching: +🛠 Craft block. Coaching cues. Extended rest."""
    blocks: list[str] = []
    n = 1
    if order_e == "🏟":
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_craft(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    elif order_e == "🖼":
        blocks.append(_block_intention(ctx)); n = 2
        blocks.append(_block_craft(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    else:
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_craft(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_supplemental(ctx, p, n)); n += 1
        blocks.append(_block_imprint(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    return blocks


def _bodyweight_blocks(ctx: dict[str, Any], p: dict[str, Any], order_e: str) -> list[str]:
    """🟢 Bodyweight: Standard Order sequence. No barbells, no machines."""
    return _default_blocks(ctx, p, order_e)


def _intense_blocks(ctx: dict[str, Any], p: dict[str, Any], order_e: str) -> list[str]:
    """🔴 Intense: Reduced rest. +🌋 Gutter (not in 🖼/🐂). Supersets in 🧩."""
    blocks: list[str] = []
    n = 1
    if order_e == "🏟":
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_progression(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    elif order_e == "🖼":
        blocks.append(_block_intention(ctx)); n = 2
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_release(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    elif order_e in ("🐂",):  # No gutter in Foundation
        return _default_blocks(ctx, p, order_e)
    else:
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_primer(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_supplemental(ctx, p, n)); n += 1
        blocks.append(_block_gutter(ctx, p, n)); n += 1
        blocks.append(_block_release(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    return blocks


def _technical_blocks(ctx: dict[str, Any], p: dict[str, Any], order_e: str) -> list[str]:
    """🟣 Technical: Fewer blocks (minimum for Order). Extended rest. Quality over volume."""
    blocks: list[str] = []
    n = 1
    min_blocks = ORDER_CEILINGS.get(order_e, {}).get("blocks_min", 4)
    if order_e == "🏟":
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_progression(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    elif order_e == "🖼":
        blocks.append(_block_intention(ctx)); n = 2
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_imprint(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    else:
        blocks.append(_block_warmup(ctx, p, n)); n += 1
        blocks.append(_block_primer(ctx, p, n)); n += 1
        blocks.append(_block_bread_butter(ctx, p, n)); n += 1
        blocks.append(_block_supplemental(ctx, p, n)); n += 1
        blocks.append(_block_release(ctx, p, n)); n += 1
        blocks.append(_block_junction(ctx, n))
    # Ensure we meet minimum block count for the Order
    # (Technical aims for min, not max — quality over volume)
    return blocks


def _structured_blocks(ctx: dict[str, Any], p: dict[str, Any], order_e: str) -> list[str]:
    """🔵 Structured: Default Order sequence + 🪜 Progression prominent."""
    blocks = _default_blocks(ctx, p, order_e)
    # Add Progression before 🧈 if not already present (for non-🏟 Orders)
    if order_e not in ("🏟", "🖼") and not any("🪜 Progression" in b for b in blocks):
        new_blocks = []
        for blk in blocks:
            if "🧈 Bread & Butter" in blk:
                prog_num = int(blk.split(")")[0].split("##")[-1].strip())
                new_blocks.append(_block_progression(ctx, p, prog_num))
                # Renumber remaining blocks
                new_blocks.append(blk.replace(f"## {prog_num})", f"## {prog_num + 1})"))
            else:
                new_blocks.append(blk)
        # Only use if within block count limits
        max_blocks = ORDER_CEILINGS[order_e].get("blocks_max", 7)
        if len(new_blocks) <= max_blocks:
            blocks = new_blocks
    return blocks


def fallback_template(context: dict[str, Any]) -> str:
    """Generate Order×Color aware workout card template with Color-first dispatch."""
    zip_code = context["zip"]
    t = context.get("type_emoji", TYPE_EMOJI.get(context["type_name"], "🛒"))
    order_e = context["order_emoji"]
    color_e = context["color_emoji"]
    p = _get_order_params(context)
    time_est = ORDER_TIME.get(order_e, "45-55 min")

    title = f"{context['primary_exercise']} — {context['type_name']} {context['color_name']}"
    key = (order_e, color_e)
    intention = INTENTIONS.get(key, INTENTIONS.get((order_e, "🔵"), "Work with purpose."))

    header = f"""# {t} {title} {t}

## {context['order_name']} {context['axis_name']} — {context['type_name']} focus ({context['color_name']}) · {time_est}

**CODE:** {zip_code}

> \"{intention}\"
"""

    # --- Color-first block dispatch ---
    if color_e == "🟠":
        blocks = _circuit_blocks(context, p, order_e)
    elif color_e == "🟡":
        blocks = _fun_blocks(context, p, order_e)
    elif color_e == "⚪":
        blocks = _mindful_blocks(context, p, order_e)
    elif color_e == "⚫":
        blocks = _teaching_blocks(context, p, order_e)
    elif color_e == "🟢":
        blocks = _bodyweight_blocks(context, p, order_e)
    elif color_e == "🔴":
        blocks = _intense_blocks(context, p, order_e)
    elif color_e == "🟣":
        blocks = _technical_blocks(context, p, order_e)
    else:
        blocks = _structured_blocks(context, p, order_e)

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
        # Filter supplemental exercises for Type accuracy
        type_name = meta["type"]["name"]
        supplemental = _filter_exercises_for_type(supplemental, type_name)
        # Filter out barbells for 🟢 and 🟠
        if meta["color"]["emoji"] in NO_BARBELL:
            supplemental = _filter_no_barbell(supplemental)
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
