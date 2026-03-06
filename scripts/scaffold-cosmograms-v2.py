#!/usr/bin/env python3
"""
scripts/scaffold-cosmograms-v2.py
CX-NEW: Cosmogram v2 Scaffold — 61-Branch Architecture

Generates 42 cosmogram v2 files using the 61-branch architecture defined in
scl-deep/cosmogram-architecture.md. Each file contains all 61 SCL emoji branches
pre-populated with:
  - Affinity labels derived from deck-average weight vectors
  - Home-territory markers for the deck's own Order and Axis branches
  - Pre-computed cross-cosmogram threads (same-Order and same-Axis adjacencies)
  - Empty knowledge deposit slots ready for research population

Input sources:
  - middle-math/zip-registry.json     — deck metadata (order, axis, operators, polarity)
  - middle-math/weight-vectors.json   — 1,680 × 61 weight vectors
  - deck-cosmograms/deck-[N]-cosmogram.md — existing frontmatter to migrate

Output: deck-cosmograms/deck-[NN]-cosmogram-v2.md (42 files)

Usage:
    python scripts/scaffold-cosmograms-v2.py            # generate all 42
    python scripts/scaffold-cosmograms-v2.py --deck 8   # generate single deck
    python scripts/scaffold-cosmograms-v2.py --dry-run  # print summary, no writes
    python scripts/scaffold-cosmograms-v2.py --overwrite # overwrite existing v2 files
"""

import argparse
import json
import sys
from pathlib import Path
import yaml

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT      = Path(__file__).resolve().parent.parent
REGISTRY_PATH  = REPO_ROOT / "middle-math" / "zip-registry.json"
VECTORS_PATH   = REPO_ROOT / "middle-math" / "weight-vectors.json"
COSMOGRAM_DIR  = REPO_ROOT / "deck-cosmograms"

# ---------------------------------------------------------------------------
# 61-emoji position map (mirrors scripts/middle-math/weight_vector.py)
# ---------------------------------------------------------------------------
EMOJI_POSITIONS = {
    # Orders (7) — positions 0–6
    "🐂": 0, "⛽": 1, "🦋": 2, "🏟": 3, "🌾": 4, "⚖": 5, "🖼": 6,
    # Axes (6) — positions 7–12
    "🏛": 7, "🔨": 8, "🌹": 9, "🪐": 10, "⌛": 11, "🐬": 12,
    # Types (5) — positions 13–17
    "🛒": 13, "🪡": 14, "🍗": 15, "➕": 16, "➖": 17,
    # Colors (8) — positions 18–25
    "⚫": 18, "🟢": 19, "🔵": 20, "🟣": 21, "🔴": 22, "🟠": 23, "🟡": 24, "⚪": 25,
    # Blocks (22 + SAVE = 23) — positions 26–48
    "♨️": 26, "🎯": 27, "🔢": 28, "🧈": 29, "🫀": 30, "▶️": 31, "🎼": 32,
    "♟️": 33, "🪜": 34, "🌎": 35, "🎱": 36, "🌋": 37, "🪞": 38, "🗿": 39,
    "🛠": 40, "🧩": 41, "🪫": 42, "🏖": 43, "🏗": 44, "🧬": 45, "🚂": 46,
    "🔠": 47, "🧮": 48,
    # Operators (12) — positions 49–60
    "🧲": 49, "🐋": 50, "🤌": 51, "🧸": 52, "✒️": 53, "🦉": 54,
    "🥨": 55, "🦢": 56, "📍": 57, "👀": 58, "🪵": 59, "🚀": 60,
}

# ---------------------------------------------------------------------------
# 61 branches in fixed order — groups: Orders, Axes, Types, Colors, Blocks, Operators
# ---------------------------------------------------------------------------
BRANCH_ORDER = [
    # Orders (7)
    ("🐂", "Foundation",    "Order"),
    ("⛽", "Strength",      "Order"),
    ("🦋", "Hypertrophy",   "Order"),
    ("🏟", "Performance",   "Order"),
    ("🌾", "Full Body",     "Order"),
    ("⚖",  "Balance",      "Order"),
    ("🖼", "Restoration",   "Order"),
    # Axes (6)
    ("🏛", "Basics",        "Axis"),
    ("🔨", "Functional",    "Axis"),
    ("🌹", "Aesthetic",     "Axis"),
    ("🪐", "Challenge",     "Axis"),
    ("⌛", "Time",          "Axis"),
    ("🐬", "Partner",       "Axis"),
    # Types (5)
    ("🛒", "Push",          "Type"),
    ("🪡", "Pull",          "Type"),
    ("🍗", "Legs",          "Type"),
    ("➕", "Plus",          "Type"),
    ("➖", "Ultra",         "Type"),
    # Colors (8)
    ("⚫", "Teaching",      "Color"),
    ("🟢", "Bodyweight",    "Color"),
    ("🔵", "Structured",    "Color"),
    ("🟣", "Technical",     "Color"),
    ("🔴", "Intense",       "Color"),
    ("🟠", "Circuit",       "Color"),
    ("🟡", "Fun",           "Color"),
    ("⚪", "Mindful",       "Color"),
    # Blocks (23)
    ("♨️", "Warm-Up",      "Block"),
    ("🎯", "Intention",     "Block"),
    ("🔢", "Fundamentals",  "Block"),
    ("🧈", "Bread & Butter","Block"),
    ("🫀", "Circulation",   "Block"),
    ("▶️", "Primer",       "Block"),
    ("🎼", "Composition",   "Block"),
    ("♟️", "Gambit",       "Block"),
    ("🪜", "Progression",   "Block"),
    ("🌎", "Exposure",      "Block"),
    ("🎱", "ARAM",          "Block"),
    ("🌋", "Gutter",        "Block"),
    ("🪞", "Vanity",        "Block"),
    ("🗿", "Sculpt",        "Block"),
    ("🛠",  "Craft",        "Block"),
    ("🧩", "Supplemental",  "Block"),
    ("🪫", "Release",       "Block"),
    ("🏖", "Sandbox",       "Block"),
    ("🏗",  "Reformance",   "Block"),
    ("🧬", "Imprint",       "Block"),
    ("🚂", "Junction",      "Block"),
    ("🔠", "Choice",        "Block"),
    ("🧮", "SAVE",          "Block"),
    # Operators (12)
    ("📍", "pono",          "Operator"),
    ("🧲", "capio",         "Operator"),
    ("🧸", "fero",          "Operator"),
    ("👀", "specio",        "Operator"),
    ("🥨", "tendo",         "Operator"),
    ("🤌", "facio",         "Operator"),
    ("🚀", "mitto",         "Operator"),
    ("🦢", "plico",         "Operator"),
    ("🪵", "teneo",         "Operator"),
    ("🐋", "duco",          "Operator"),
    ("✒️", "grapho",        "Operator"),
    ("🦉", "logos",         "Operator"),
]

assert len(BRANCH_ORDER) == 61, f"Expected 61 branches, got {len(BRANCH_ORDER)}"

# ---------------------------------------------------------------------------
# Polysemic branch descriptions — training meaning + deeper register
# Used in branch headers: "## [EMOJI] [Name] — [description]"
# ---------------------------------------------------------------------------
BRANCH_DESCRIPTIONS = {
    # Orders
    "🐂": "Foundation — naming the pieces; grammar of the discipline",
    "⛽": "Strength — what holds under pressure; logic proven by load",
    "🦋": "Hypertrophy — accumulation and growth; rhetoric that sticks",
    "🏟": "Performance — the real number; arithmetic of capacity",
    "🌾": "Full Body — integration; geometry of parts that fit",
    "⚖":  "Balance — proportion and correction; music of counterpoise",
    "🖼": "Restoration — completing the cycle; astronomy of the whole pattern",
    # Axes
    "🏛": "Basics — literal structure; what IS it, plainly and firmly",
    "🔨": "Functional — practical sense; does it work in the world",
    "🌹": "Aesthetic — allegorical sense; what lies beneath the surface",
    "🪐": "Challenge — anagogical sense; what does it ultimately point toward",
    "⌛": "Time — prophetic sense; when, for how long, in what cycle",
    "🐬": "Partner — ecclesial sense; who is involved and who benefits",
    # Types
    "🛒": "Push — output, expression, what goes outward into the world",
    "🪡": "Pull — input, reception, what is drawn inward",
    "🍗": "Legs — foundation, ground, what supports and what you stand on",
    "➕": "Plus — addition, synthesis, what is being combined or built",
    "➖": "Ultra — refinement, subtraction, transcending by removing",
    # Colors
    "⚫": "Teaching — foundational seriousness; the non-negotiable ground",
    "🟢": "Bodyweight — sustainable, organic, self-reliant; works without infrastructure",
    "🔵": "Structured — methodical, systematic, calm authority; the prescription",
    "🟣": "Technical — deep, precise, significant; fewer items, more weight per item",
    "🔴": "Intense — urgent, direct, maximum effort; demands full attention now",
    "🟠": "Circuit — warm, relational, connective; ideas rotate through people",
    "🟡": "Fun — curious, playful, exploratory; structured play within boundaries",
    "⚪": "Mindful — honest, clear, spacious; breath between thoughts",
    # Blocks
    "♨️": "Warm-Up — arrival, orientation, first contact with the subject",
    "🎯": "Intention — thesis, purpose, why this branch matters here",
    "🔢": "Fundamentals — first principles, bedrock facts, the ground truth",
    "🧈": "Bread & Butter — the core content; the main body of knowledge at this address",
    "🫀": "Circulation — how knowledge flows, distributes, reaches people",
    "▶️": "Primer — what you need before the main thing makes sense",
    "🎼": "Composition — how parts cooperate; arrangement and orchestration",
    "♟️": "Gambit — strategic sacrifice; what understanding requires giving up",
    "🪜": "Progression — the path from novice to mastery in this domain",
    "🌎": "Exposure — first encounters, expanding vocabulary, revealing gaps",
    "🎱": "ARAM — loop-based or rotation-based systems within this domain",
    "🌋": "Gutter — the edge; the extreme case, the point of no return",
    "🪞": "Vanity — surface truth, appearance, what the mirror shows honestly",
    "🗿": "Sculpt — deliberate shaping, carving, forming with intent",
    "🛠":  "Craft — skill acquisition, apprenticeship, practice traditions",
    "🧩": "Supplemental — supporting knowledge, adjacent contributions",
    "🪫": "Release — what must be dropped, discharged, let go",
    "🏖": "Sandbox — safe experimentation spaces, bounded play",
    "🏗":  "Reformance — corrective rebuilding; what was broken and rebuilt",
    "🧬": "Imprint — what persists, what gets encoded, lasting patterns",
    "🚂": "Junction — connection points; what leads to what comes next",
    "🔠": "Choice — decision points, forks, bounded autonomy",
    "🧮": "SAVE — the archive, the permanent record, what is preserved",
    # Operators
    "📍": "pono — place, position, establish; the stance before the work begins",
    "🧲": "capio — capture, receive, assess, take in; the catching phase",
    "🧸": "fero — carry, transfer, channel; moving load across contexts",
    "👀": "specio — inspect, observe, examine; watching for what the data reveals",
    "🥨": "tendo — stretch, extend, reach, push limits; lengthening toward capacity",
    "🤌": "facio — execute, make, perform, produce; the doing",
    "🚀": "mitto — dispatch, launch, commit, send forth; the decisive release",
    "🦢": "plico — fold, compress, layer, interweave; two things woven as one",
    "🪵": "teneo — hold, anchor, persist, endure; sustained tension over time",
    "🐋": "duco — orchestrate, lead, conduct, arrange; the architecture of flow",
    "✒️": "grapho — write, prescribe, document, record; making the work permanent",
    "🦉": "logos — reason, analyze, interpret, make meaning; the reflective layer",
}

# ---------------------------------------------------------------------------
# Core resonance stubs — brief framing of what each emoji means at a deck
# These are pre-populated stubs that a researcher refines. They use the deck's
# Order × Axis intersection to contextualize the emoji's polysemic meaning.
# Format: lambda(order_name, axis_name) -> string
# ---------------------------------------------------------------------------
CORE_RESONANCE_STUBS = {
    "🐂": lambda o, a: f"At the {o} × {a} intersection, 🐂 Foundation names the entry conditions — what must be established before anything more complex can hold.",
    "⛽": lambda o, a: f"At the {o} × {a} intersection, ⛽ Strength marks the moment of pressure-testing — what survives load at this address.",
    "🦋": lambda o, a: f"At the {o} × {a} intersection, 🦋 Hypertrophy tracks what accumulates — what grows when volume is applied consistently here.",
    "🏟": lambda o, a: f"At the {o} × {a} intersection, 🏟 Performance records the real number — the benchmark that cannot be argued with.",
    "🌾": lambda o, a: f"At the {o} × {a} intersection, 🌾 Full Body asks whether all the pieces have been integrated into a functioning whole.",
    "⚖":  lambda o, a: f"At the {o} × {a} intersection, ⚖ Balance identifies what is out of proportion and prescribes the correction.",
    "🖼": lambda o, a: f"At the {o} × {a} intersection, 🖼 Restoration closes the cycle — what this address looks like when the work is complete and ready to begin again.",
    "🏛": lambda o, a: f"At the {o} × {a} intersection, 🏛 Basics asks the literal question: what IS this, structurally? The answer is the foundation everything else rests on.",
    "🔨": lambda o, a: f"At the {o} × {a} intersection, 🔨 Functional asks whether it works in practice — not in theory, not on paper, but under real conditions.",
    "🌹": lambda o, a: f"At the {o} × {a} intersection, 🌹 Aesthetic reads the allegorical layer — what this address means beneath the surface of its plain function.",
    "🪐": lambda o, a: f"At the {o} × {a} intersection, 🪐 Challenge points toward the ultimate destination — the most demanding version of what this address can become.",
    "⌛": lambda o, a: f"At the {o} × {a} intersection, ⌛ Time governs the temporal dimension — the rhythm, cycle, and duration that gives this address its character.",
    "🐬": lambda o, a: f"At the {o} × {a} intersection, 🐬 Partner asks who else is present — the relational and social dimensions of knowledge at this address.",
    "🛒": lambda o, a: f"At the {o} × {a} intersection, 🛒 Push traces what goes outward — the expressive, projective, and productive forces at work here.",
    "🪡": lambda o, a: f"At the {o} × {a} intersection, 🪡 Pull traces what comes inward — the receptive, absorptive, and integrative forces at work here.",
    "🍗": lambda o, a: f"At the {o} × {a} intersection, 🍗 Legs grounds the work — what provides the base, the support, the standing place for everything else.",
    "➕": lambda o, a: f"At the {o} × {a} intersection, ➕ Plus synthesizes — what is added, combined, or built when separate elements are brought into relation.",
    "➖": lambda o, a: f"At the {o} × {a} intersection, ➖ Ultra refines — what is distilled or transcended when excess is removed and only the essential remains.",
    "⚫": lambda o, a: f"At the {o} × {a} intersection, ⚫ Teaching establishes the non-negotiable ground — the serious foundation beneath which no further simplification is permitted.",
    "🟢": lambda o, a: f"At the {o} × {a} intersection, 🟢 Bodyweight marks the self-reliant register — what this address looks like when built from resources that are always available.",
    "🔵": lambda o, a: f"At the {o} × {a} intersection, 🔵 Structured prescribes — the systematic, repeatable, trackable form of the work at this address.",
    "🟣": lambda o, a: f"At the {o} × {a} intersection, 🟣 Technical demands precision — fewer items, more weight per item, quality over quantity.",
    "🔴": lambda o, a: f"At the {o} × {a} intersection, 🔴 Intense presses for maximum output — the urgent, high-density, full-attention register of this address.",
    "🟠": lambda o, a: f"At the {o} × {a} intersection, 🟠 Circuit distributes — knowledge that rotates through people, station to station, rather than sitting still.",
    "🟡": lambda o, a: f"At the {o} × {a} intersection, 🟡 Fun opens the exploratory register — structured play, curiosity, and discovery within the address's constraints.",
    "⚪": lambda o, a: f"At the {o} × {a} intersection, ⚪ Mindful holds space — the slow, honest, spacious register where breath is allowed between thoughts.",
    "♨️": lambda o, a: f"At the {o} × {a} intersection, ♨️ Warm-Up describes the conditions of first contact — how a practitioner arrives at this address for the first time.",
    "🎯": lambda o, a: f"At the {o} × {a} intersection, 🎯 Intention frames the purpose — the one-sentence thesis for why any of this knowledge is worth holding.",
    "🔢": lambda o, a: f"At the {o} × {a} intersection, 🔢 Fundamentals names the bedrock — the irreducible principles that cannot be skipped.",
    "🧈": lambda o, a: f"At the {o} × {a} intersection, 🧈 Bread & Butter is the main thing — the core body of knowledge that most richly expresses what this address is.",
    "🫀": lambda o, a: f"At the {o} × {a} intersection, 🫀 Circulation tracks distribution — how this knowledge moves through practitioners, institutions, and generations.",
    "▶️": lambda o, a: f"At the {o} × {a} intersection, ▶️ Primer primes — what you must understand before the main thing becomes accessible.",
    "🎼": lambda o, a: f"At the {o} × {a} intersection, 🎼 Composition arranges — how the parts of this knowledge cooperate and how their arrangement creates meaning.",
    "♟️": lambda o, a: f"At the {o} × {a} intersection, ♟️ Gambit names the sacrifice — what must be given up to achieve understanding at this address.",
    "🪜": lambda o, a: f"At the {o} × {a} intersection, 🪜 Progression ladders the path — the documented sequence from first encounter to mature mastery.",
    "🌎": lambda o, a: f"At the {o} × {a} intersection, 🌎 Exposure maps the edges — first encounters with what this address reveals about adjacent territory.",
    "🎱": lambda o, a: f"At the {o} × {a} intersection, 🎱 ARAM identifies loops — the rotation systems and recursive structures native to this address.",
    "🌋": lambda o, a: f"At the {o} × {a} intersection, 🌋 Gutter marks the threshold — the extreme case, the edge of what this address can contain.",
    "🪞": lambda o, a: f"At the {o} × {a} intersection, 🪞 Vanity holds the mirror — what this address looks like to honest observation, stripped of flattery.",
    "🗿": lambda o, a: f"At the {o} × {a} intersection, 🗿 Sculpt carves — the deliberate shaping of form with intent, where subtraction creates definition.",
    "🛠":  lambda o, a: f"At the {o} × {a} intersection, 🛠 Craft maps the practice traditions — the apprenticeship pathways through which this knowledge is transmitted.",
    "🧩": lambda o, a: f"At the {o} × {a} intersection, 🧩 Supplemental gathers adjacent knowledge — what supports the main body without competing with it.",
    "🪫": lambda o, a: f"At the {o} × {a} intersection, 🪫 Release marks what must be discharged — the beliefs, habits, or frameworks that must be dropped to advance.",
    "🏖": lambda o, a: f"At the {o} × {a} intersection, 🏖 Sandbox opens the play space — bounded exploration where the rules are real but failure is reversible.",
    "🏗":  lambda o, a: f"At the {o} × {a} intersection, 🏗 Reformance documents correction — what was broken here, how it was rebuilt, what the rebuilt version looks like.",
    "🧬": lambda o, a: f"At the {o} × {a} intersection, 🧬 Imprint records what persists — the encoded patterns that outlast any single practitioner's contact with this address.",
    "🚂": lambda o, a: f"At the {o} × {a} intersection, 🚂 Junction maps the connections — the bridges from this address to adjacent decks and the rationale for each.",
    "🔠": lambda o, a: f"At the {o} × {a} intersection, 🔠 Choice marks the forks — the decision points where bounded autonomy determines which path through this knowledge a practitioner takes.",
    "🧮": lambda o, a: f"At the {o} × {a} intersection, 🧮 SAVE preserves — the permanent record of what has been learned, tested, and confirmed at this address.",
    "📍": lambda o, a: f"At the {o} × {a} intersection, 📍 pono (place) describes the setup conditions — how a practitioner positions themselves to begin work here.",
    "🧲": lambda o, a: f"At the {o} × {a} intersection, 🧲 capio (capture) governs intake — what this address draws in, what it absorbs, how it receives.",
    "🧸": lambda o, a: f"At the {o} × {a} intersection, 🧸 fero (carry) transfers — what is transported across contexts, carried from one session to the next.",
    "👀": lambda o, a: f"At the {o} × {a} intersection, 👀 specio (observe) watches — the monitoring and inspection practices native to this address.",
    "🥨": lambda o, a: f"At the {o} × {a} intersection, 🥨 tendo (extend) stretches limits — the work of reaching past the comfortable boundary at this address.",
    "🤌": lambda o, a: f"At the {o} × {a} intersection, 🤌 facio (execute) does — the concrete production and performance that constitutes doing the work here.",
    "🚀": lambda o, a: f"At the {o} × {a} intersection, 🚀 mitto (dispatch) launches — the decisive commitment and irreversible send-off that this address demands.",
    "🦢": lambda o, a: f"At the {o} × {a} intersection, 🦢 plico (fold) layers — the interweaving of elements that creates compound meaning or compound movement.",
    "🪵": lambda o, a: f"At the {o} × {a} intersection, 🪵 teneo (hold) anchors — the sustained tension and long-duration persistence that this address rewards.",
    "🐋": lambda o, a: f"At the {o} × {a} intersection, 🐋 duco (conduct) orchestrates — the session architecture and flow management that gives this address its tempo.",
    "✒️": lambda o, a: f"At the {o} × {a} intersection, ✒️ grapho (write) documents — the record-keeping and prescription practices that make work at this address repeatable.",
    "🦉": lambda o, a: f"At the {o} × {a} intersection, 🦉 logos (reason) interprets — the analytical and meaning-making layer that sits above the raw data of this address.",
}

# ---------------------------------------------------------------------------
# Affinity label from weight value
# ---------------------------------------------------------------------------
def affinity_label(weight: float) -> str:
    if weight >= 6:
        return "Defining characteristic — home territory at this address"
    elif weight >= 3:
        return "Strong affinity — naturally concentrates here"
    elif weight >= 1:
        return "Moderate affinity"
    elif weight == 0:
        return "Neutral presence"
    elif weight >= -3:
        return "Thin at this address — tends to concentrate elsewhere"
    else:
        return "Hard suppression — conflicts with this deck's core parameters"


# ---------------------------------------------------------------------------
# Cross-cosmogram thread generation
# Given a deck number (1–42), compute natural adjacencies
# ---------------------------------------------------------------------------
def compute_threads(deck_num: int) -> dict[str, list[tuple[int, str, str]]]:
    """
    Returns dict with keys 'same_order' and 'same_axis'.
    Each value is list of (deck_number, emoji, reason) tuples.

    Deck grid:
      Row = Order (1–7), Col = Axis (1–6)
      deck = (order - 1) * 6 + axis
      order = (deck - 1) // 6 + 1
      axis  = (deck - 1) % 6 + 1
    """
    order_num = (deck_num - 1) // 6 + 1
    axis_num  = (deck_num - 1) % 6 + 1

    order_emojis = ["🐂", "⛽", "🦋", "🏟", "🌾", "⚖", "🖼"]
    axis_emojis  = ["🏛", "🔨", "🌹", "🪐", "⌛", "🐬"]
    axis_names   = ["Basics", "Functional", "Aesthetic", "Challenge", "Time", "Partner"]

    order_emoji = order_emojis[order_num - 1]
    axis_emoji  = axis_emojis[axis_num - 1]
    axis_name   = axis_names[axis_num - 1]

    # Same-Order decks: all 6 Axis variants at this Order
    same_order = []
    for ax in range(1, 7):
        d = (order_num - 1) * 6 + ax
        if d != deck_num:
            ax_emoji = axis_emojis[ax - 1]
            ax_name  = axis_names[ax - 1]
            reason = f"{ax_emoji} {ax_name} — same {order_emoji} Order, different Axis lens"
            same_order.append((d, ax_emoji, reason))

    # Same-Axis decks: all 7 Order variants at this Axis
    same_axis = []
    for o in range(1, 8):
        d = (o - 1) * 6 + axis_num
        if d != deck_num:
            o_emoji = order_emojis[o - 1]
            reason = f"{o_emoji} {axis_emoji} — same {axis_name} Axis, different Order phase"
            same_axis.append((d, o_emoji, reason))

    return {"same_order": same_order, "same_axis": same_axis}


# ---------------------------------------------------------------------------
# Parse existing cosmogram frontmatter to migrate metadata
# ---------------------------------------------------------------------------
def parse_existing_frontmatter(deck_num: int) -> dict:
    path = COSMOGRAM_DIR / f"deck-{deck_num:02d}-cosmogram.md"
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end == -1:
        return {}
    try:
        fm = yaml.safe_load(text[3:end])
        return fm if isinstance(fm, dict) else {}
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# Load and aggregate data
# ---------------------------------------------------------------------------
def load_registry() -> dict[int, dict]:
    """Returns dict: deck_number → representative entry (first zip in deck)."""
    with open(REGISTRY_PATH, encoding="utf-8") as f:
        entries = json.load(f)
    by_deck: dict[int, dict] = {}
    for entry in entries:
        d = entry["deck_number"]
        if d not in by_deck:
            by_deck[d] = entry
    return by_deck


def load_deck_average_vectors() -> dict[int, list[float]]:
    """Returns dict: deck_number → 61-dim average weight vector (averaged over 40 zips)."""
    with open(VECTORS_PATH, encoding="utf-8") as f:
        vectors = json.load(f)

    # Group vectors by deck
    deck_vectors: dict[int, list[list[float]]] = {}
    for zip_key, data in vectors.items():
        d = data["deck"]
        if d not in deck_vectors:
            deck_vectors[d] = []
        deck_vectors[d].append(data["vector"])

    # Average each group
    deck_avg: dict[int, list[float]] = {}
    for d, vecs in deck_vectors.items():
        n = len(vecs)
        avg = [sum(vecs[i][j] for i in range(n)) / n for j in range(61)]
        deck_avg[d] = avg

    return deck_avg


# ---------------------------------------------------------------------------
# Generate a single v2 cosmogram file content
# ---------------------------------------------------------------------------
def generate_v2_content(deck_num: int, registry: dict[int, dict],
                         deck_avg_vectors: dict[int, list[float]]) -> str:
    entry  = registry[deck_num]
    vector = deck_avg_vectors[deck_num]
    old_fm = parse_existing_frontmatter(deck_num)

    order_emoji = entry["order"]["emoji"]
    order_name  = entry["order"]["name"]
    axis_emoji  = entry["axis"]["emoji"]
    axis_name   = entry["axis"]["name"]

    # Operator pair — prep from preparatory zip, expr from expressive zip
    # The registry entry for the first zip may be prep or expr.
    # Read both from existing frontmatter if available, else derive from axis.
    prep_op = old_fm.get("operators_preparatory", "")
    expr_op = old_fm.get("operators_expressive", "")

    # If not in existing frontmatter, use the operator table
    OPERATOR_TABLE = {
        "🏛": ("📍 pono",  "🤌 facio"),
        "🔨": ("🧸 fero",  "🥨 tendo"),
        "🌹": ("👀 specio", "🦢 plico"),
        "🪐": ("🪵 teneo", "🚀 mitto"),
        "⌛": ("🐋 duco",  "✒️ grapho"),
        "🐬": ("🧲 capio", "🦉 logos"),
    }
    if not prep_op or not expr_op:
        prep_op, expr_op = OPERATOR_TABLE.get(axis_emoji, ("", ""))

    # Metadata from old frontmatter
    liberal_art   = old_fm.get("liberal_art", old_fm.get("liberal-art", ""))
    hermeneutic   = old_fm.get("hermeneutic_sense", old_fm.get("hermeneutic", ""))
    column        = old_fm.get("column", "")
    season        = old_fm.get("season", "")
    deep_question = old_fm.get("deep_question", old_fm.get("deep-question", ""))

    # Build frontmatter
    frontmatter = (
        f"---\n"
        f"deck: {deck_num:02d}\n"
        f"order: {order_emoji} {order_name}\n"
        f"axis: {axis_emoji} {axis_name}\n"
        f"operator-pair: {prep_op} / {expr_op}\n"
        f"liberal-art: \"{liberal_art}\"\n"
        f"hermeneutic: \"{hermeneutic}\"\n"
        f"column: \"{column}\"\n"
        f"season: \"{season}\"\n"
        f"deep-question: \"{deep_question}\"\n"
        f"status: STUB\n"
        f"branch-count: 0\n"
        f"last-research: null\n"
        f"---\n"
    )

    # Title and preamble
    preamble = (
        f"# Deck {deck_num:02d} Cosmogram — {order_emoji} {order_name} × {axis_emoji} {axis_name}\n"
        f"\n"
        f"> This is a v2 STUB file using the 61-branch architecture.\n"
        f"> See `scl-deep/cosmogram-architecture.md` for the architecture specification.\n"
        f"> See `seeds/cosmogram-contract-prompt-v1.md` for the research protocol.\n"
        f"> See `scl-deep/publication-standard.md` for voice and editorial standards.\n"
        f"> Generate content in a dedicated AI research session with web access.\n"
        f"\n"
        f"**Deep Question:** {deep_question}\n"
        f"**Liberal Art:** {liberal_art} | **Hermeneutic:** {hermeneutic}\n"
        f"**Season:** {season} | **Column:** {column} | **Operators:** {prep_op} / {expr_op}\n"
        f"\n"
        f"---\n"
        f"\n"
        f"## Deck Character\n"
        f"\n"
        f"*[Pre-search synthesis — Phase 1: write this from the briefing alone before any internet research.]*\n"
        f"*[What does {order_name} × {axis_name} mean as an idea space? What kinds of knowledge naturally concentrate at this address?]*\n"
    )

    # Pre-compute cross-cosmogram threads
    threads = compute_threads(deck_num)
    same_order_thread_lines = "\n".join(
        f"- → Deck {d:02d} ({reason})" for d, _, reason in threads["same_order"]
    )
    same_axis_thread_lines = "\n".join(
        f"- → Deck {d:02d} ({reason})" for d, _, reason in threads["same_axis"]
    )

    # Section headers
    sections = {
        "Order": "\n\n---\n\n## ORDERS\n\n",
        "Axis":  "\n\n---\n\n## AXES\n\n",
        "Type":  "\n\n---\n\n## TYPES\n\n",
        "Color": "\n\n---\n\n## COLORS\n\n",
        "Block": "\n\n---\n\n## BLOCKS\n\n",
        "Operator": "\n\n---\n\n## OPERATORS\n\n",
    }

    # Build branches
    branches_text = ""
    current_category = None

    for emoji, name, category in BRANCH_ORDER:
        # Section header on category change
        if category != current_category:
            branches_text += sections[category]
            current_category = category

        # Get vector index and weight
        idx    = EMOJI_POSITIONS[emoji]
        weight = vector[idx]
        label  = affinity_label(weight)

        # Home territory marker
        home_marker = ""
        if emoji == order_emoji:
            home_marker = " 🏠 HOME ORDER"
        elif emoji == axis_emoji:
            home_marker = " 🏠 HOME AXIS"

        # Branch description
        desc = BRANCH_DESCRIPTIONS.get(emoji, f"{name}")

        # Core resonance
        resonance = CORE_RESONANCE_STUBS[emoji](order_name, axis_name)

        # Thread lines — use home-territory cross-deck threads for Order/Axis branches
        if emoji == order_emoji:
            thread_section = same_order_thread_lines or "- [no adjacent decks]"
        elif emoji == axis_emoji:
            thread_section = same_axis_thread_lines or "- [no adjacent decks]"
        else:
            thread_section = "-"

        branch = (
            f"## {emoji} {desc}{home_marker}\n"
            f"\n"
            f"**Affinity:** {label} (avg weight: {weight:.2f})\n"
            f"\n"
            f"Core resonance: {resonance}\n"
            f"\n"
            f"Knowledge deposits:\n"
            f"{thread_section if emoji not in (order_emoji, axis_emoji) else '-'}\n"
            f"\n"
            f"Cross-cosmogram threads:\n"
            f"{thread_section}\n"
            f"\n"
            f"Open questions:\n"
            f"-\n"
        )
        branches_text += branch + "\n"

    # Footer
    footer = "\n---\n\n🧮\n"

    return frontmatter + "\n" + preamble + branches_text + footer


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Generate 42 cosmogram v2 files with 61-branch architecture"
    )
    parser.add_argument("--deck",      type=int, help="Generate single deck (1–42)")
    parser.add_argument("--all",       action="store_true", help="Generate all 42 decks")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing v2 files")
    parser.add_argument("--dry-run",   action="store_true", help="Print summary without writing")
    args = parser.parse_args()

    # Default: generate all if no --deck specified
    if args.deck is None:
        decks = list(range(1, 43))
    else:
        if not 1 <= args.deck <= 42:
            print(f"Error: --deck must be 1–42, got {args.deck}", file=sys.stderr)
            sys.exit(1)
        decks = [args.deck]

    print(f"Loading registry and weight vectors...")
    registry        = load_registry()
    deck_avg_vectors = load_deck_average_vectors()

    generated = 0
    skipped   = 0
    errors    = 0

    for deck_num in decks:
        out_path = COSMOGRAM_DIR / f"deck-{deck_num:02d}-cosmogram-v2.md"

        if out_path.exists() and not args.overwrite and not args.dry_run:
            print(f"  SKIP Deck {deck_num:02d} — {out_path.name} already exists (use --overwrite)")
            skipped += 1
            continue

        try:
            content = generate_v2_content(deck_num, registry, deck_avg_vectors)
        except Exception as e:
            print(f"  ERROR Deck {deck_num:02d} — {e}", file=sys.stderr)
            errors += 1
            continue

        entry = registry[deck_num]
        branch_count = content.count("\n## ")
        status_line  = f"  {'DRY-RUN' if args.dry_run else 'WRITE'} Deck {deck_num:02d} — {entry['order']['emoji']} {entry['order']['name']} × {entry['axis']['emoji']} {entry['axis']['name']} — {branch_count} branches"

        if args.dry_run:
            print(status_line)
        else:
            out_path.write_text(content, encoding="utf-8")
            print(status_line)
            generated += 1

    # Summary
    print()
    if args.dry_run:
        print(f"Dry run complete. {len(decks)} deck(s) would be generated.")
    else:
        print(f"Done. Generated: {generated}  Skipped: {skipped}  Errors: {errors}")
        print(f"Output: {COSMOGRAM_DIR}/deck-[NN]-cosmogram-v2.md")


if __name__ == "__main__":
    main()
