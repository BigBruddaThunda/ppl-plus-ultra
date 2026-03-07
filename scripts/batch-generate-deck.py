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


def fallback_template(context: dict[str, Any]) -> str:
    zip_code = context["zip"]
    t = TYPE_EMOJI.get(context["type_name"], "🛒")
    title = f"{context['primary_exercise']} — {context['type_name']} {context['color_name']}"
    return f"""# {t} {title} {t}

## {context['order_name']} {context['axis_name']} — {context['type_name']} focus ({context['color_name']}) · 45-55 min

**CODE:** {zip_code}

> \"Drive clean reps inside the {context['order_name'].lower()} ceiling and make every set repeatable.\"

═══
## 1) ♨️ Warm-Up — {context['operator']} inline
Subcode: {zip_code} (Warm-Up | {context['type_name']} | {context['axis_name']} | {context['color_name']})
├─ 10 {t} {context['supplemental'][0] if context['supplemental'] else context['primary_exercise']} (steady tempo, easy ramp)
│  Set 1: {context['order_emoji']} 60% × 10 (pattern prep)
Rest: 75s

═══
## 2) ▶️ Primer
Subcode: {zip_code} (Primer | {context['type_name']} | {context['axis_name']} | {context['color_name']})
├─ 8 {t} {context['supplemental'][1] if len(context['supplemental']) > 1 else context['primary_exercise']} (tight setup, crisp intent)
│  Set 1: {context['order_emoji']} 65% × 8 (activation)
Rest: 90s

═══
## 3) 🧈 Bread & Butter
Subcode: {zip_code} (Bread & Butter | {context['type_name']} | {context['axis_name']} | {context['color_name']})
├─ 5 {t} {context['primary_exercise']} (clean line, own the bottom)
│  Set 1: {context['order_emoji']} 75% × 5 (build set)
│  Set 2: {context['order_emoji']} 80% × 5 (working set)
│  Set 3: {context['order_emoji']} 80% × 5 (repeat quality)
Rest: 180s

═══
## 4) 🧩 Supplemental
Subcode: {zip_code} (Supplemental | {context['type_name']} | {context['axis_name']} | {context['color_name']})
├─ 6 {t} {context['supplemental'][2] if len(context['supplemental']) > 2 else context['primary_exercise']} (full range, no drift)
│  Set 1: {context['order_emoji']} 70% × 6 (support volume)
Rest: 120s

═══
## 5) 🪫 Release
Subcode: {zip_code} (Release | {context['type_name']} | {context['axis_name']} | {context['color_name']})
├─ 12 {t} {context['supplemental'][3] if len(context['supplemental']) > 3 else context['primary_exercise']} (smooth tempo, downshift)
│  Set 1: {context['order_emoji']} 55% × 12 (tension out)
Rest: 90s

═══
## 6) 🚂 Junction
- Log: load, reps, and form break point.
- Next → {zip_code} — repeat and tighten execution under same constraints.

## 🧮 SAVE
Keep the same movement standard next session and only add load if bar path and position stay unchanged."""


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
            "operator": stub.frontmatter.get("operator", meta["operator"]["emoji"]),
            "identity_line": entry.description,
            "primary_exercise": entry.primary_exercise,
            "supplemental": supplemental,
            "order_emoji": meta["order"]["emoji"],
            "order_name": meta["order"]["name"],
            "axis_name": meta["axis"]["name"],
            "type_name": meta["type"]["name"],
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
