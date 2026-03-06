#!/usr/bin/env python3
"""
scripts/scaffold_cosmograms.py
CX-28: Cosmogram Content Scaffold

Generates 42 stub cosmogram files — one per deck — in deck-cosmograms/.
Each stub includes frontmatter derived from the deck's Order × Axis identity
and placeholder sections matching the cosmogram research prompt output format.

Usage:
    python scripts/scaffold_cosmograms.py

Output: deck-cosmograms/deck-01-cosmogram.md through deck-42-cosmogram.md
"""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR   = REPO_ROOT / "deck-cosmograms"

# ---------------------------------------------------------------------------
# SCL data
# ---------------------------------------------------------------------------

ORDERS = [
    {"emoji": "🐂", "name": "Foundation",  "liberal_art": "Grammar",    "season": "Jan–Feb", "column": "Tuscan",     "deep_question": "What are the pieces?"},
    {"emoji": "⛽", "name": "Strength",    "liberal_art": "Logic",      "season": "Feb–Apr", "column": "Doric",      "deep_question": "What's true under pressure?"},
    {"emoji": "🦋", "name": "Hypertrophy", "liberal_art": "Rhetoric",   "season": "Apr–Jun", "column": "Ionic",      "deep_question": "Can I make it stick?"},
    {"emoji": "🏟", "name": "Performance", "liberal_art": "Arithmetic", "season": "Jun–Aug", "column": "Corinthian", "deep_question": "What's my real number?"},
    {"emoji": "🌾", "name": "Full Body",   "liberal_art": "Geometry",   "season": "Aug–Oct", "column": "Composite",  "deep_question": "Does it fit my life?"},
    {"emoji": "⚖",  "name": "Balance",    "liberal_art": "Music",      "season": "Oct–Nov", "column": "Vitruvian",  "deep_question": "What's out of balance?"},
    {"emoji": "🖼", "name": "Restoration", "liberal_art": "Astronomy",  "season": "December","column": "Palladian",  "deep_question": "What's the whole pattern?"},
]

AXES = [
    {"emoji": "🏛", "name": "Basics",     "vitruvian": "Firmitas",    "hermeneutic_sense": "Literal",    "scale": "Macro",  "scale_dimension": "spatial"},
    {"emoji": "🔨", "name": "Functional", "vitruvian": "Utilitas",    "hermeneutic_sense": "Practical",  "scale": "Meso",   "scale_dimension": "spatial"},
    {"emoji": "🌹", "name": "Aesthetic",  "vitruvian": "Venustas",    "hermeneutic_sense": "Aesthetic",  "scale": "Micro",  "scale_dimension": "spatial"},
    {"emoji": "🪐", "name": "Challenge",  "vitruvian": "Gravitas",    "hermeneutic_sense": "Anagogical", "scale": "Meso",   "scale_dimension": "spatial"},
    {"emoji": "⌛", "name": "Time",       "vitruvian": "Temporitas",  "hermeneutic_sense": "Temporal",   "scale": "Mytho",  "scale_dimension": "temporal"},
    {"emoji": "🐬", "name": "Partner",    "vitruvian": "Sociatas",    "hermeneutic_sense": "Relational", "scale": "Munus",  "scale_dimension": "relational"},
]

# Operator polarity table (from scl-directory.md)
OPERATOR_TABLE = {
    "🏛": ("📍 pono",  "🤌 facio"),
    "🔨": ("🧸 fero",  "🥨 tendo"),
    "🌹": ("👀 specio","🦢 plico"),
    "🪐": ("🪵 teneo", "🚀 mitto"),
    "⌛": ("🐋 duco",  "✒️ grapho"),
    "🐬": ("🧲 capio", "🦉 logos"),
}

# ---------------------------------------------------------------------------
# Stub template
# ---------------------------------------------------------------------------

STUB_BODY = """\
# Deck {deck:02d} Cosmogram — {order_emoji} {order_name} × {axis_emoji} {axis_name}

> This is a STUB file awaiting research population.
> See `seeds/cosmogram-research-prompt.md` for the full research protocol.
> See `scl-deep/publication-standard.md` for voice and editorial standards.
> Generate content in a dedicated AI research session with web access.

---

## Deck Character

*[Pre-search synthesis: What does this deck's Order × Axis intersection mean? Synthesize from the briefing alone before any internet research.]*

Liberal Art × Hermeneutic Sense: {liberal_art} × {hermeneutic_sense}
Season × Scale: {season} × {scale} ({scale_dimension} dimension)
Vitruvian Requirement: {vitruvian}
Deep Question: "{deep_question}"

---

## Movement & Physical Culture

*[Training philosophies, historical athletes, coaches, movement traditions, sport science, cultural practices of physical practice that belong at this address.]*

---

## Architecture, Design & Built Environment

*[Architectural principles mirroring the deck's structural character. Specific buildings, structures, design movements.]*

---

## Agriculture, Ecology & Seasonal Wisdom

*[Agricultural practices mapping to this Order's phase. What grows here. The almanac tradition.]*

---

## Education, Pedagogy & Craft

*[How people learn at this intersection. Apprenticeship traditions, skill acquisition research.]*

---

## Philosophy, Psychology & Inner Life

*[Frameworks for understanding the human experience at this address. Resilience, perception, motivation, identity.]*

---

## History, Culture & Civilizational Thread

*[Historical moments, civilizations, figures that embody this intersection. Temporal depth.]*

---

## Language, Symbol & Hermeneutics

*[Words, roots, symbols, ways of reading meaning that belong here. Etymology, archetype, metaphor.]*

---

## Alchemical & Zodiacal Resonance

Alchemical operation: {alchemical_resonance}
Zodiac resonance: {zodiac_resonance}
Intercolumniation tendency: {intercolumniation}

*[Explain the resonance. How does this alchemical phase map to the Order's developmental stage?]*

---

## The Three Paths of Depth

**Daily Page (Surface):** *[One paragraph. What a first-time user encounters. Plain names, no Latin, no alchemy.]*

**Long Road (Moderate):** *[One paragraph. What surfaces on the eighth visit. Latin names, liberal arts connections.]*

**Deep Read (Complete):** *[One paragraph. The full architecture visible. All glyph meanings, cognitive functions, nested structure.]*

---

## Wilson Notes (Planned)

*[3–5 Wilson note seeds — short, wise observations that belong on the shelves of this address. Format: italicized single sentence.]*

---

## Junction Rationale

*[Why would a user journey FROM this deck TO neighboring decks? What does this deck's address naturally connect to? Reference specific zip codes where appropriate.]*

---

## Cosmogram Research Notes

*[Researcher notes: threads investigated, threads rejected, open questions, sources consulted.]*

---

🧮
"""

# ---------------------------------------------------------------------------
# Alchemical and zodiac mappings (placeholder — to be populated by research)
# ---------------------------------------------------------------------------

# Order-level alchemical operations (placeholder)
ORDER_ALCHEMY = {
    "🐂": "Calcination (breaking down to fundamentals)",
    "⛽": "Coagulation (hardening under pressure)",
    "🦋": "Dissolution (accumulation and softening)",
    "🏟": "Distillation (testing the purest extract)",
    "🌾": "Conjunction (integrating opposites)",
    "⚖":  "Fermentation (correcting and balancing)",
    "🖼": "Projection (transmutation and long view)",
}

# Order-level zodiac resonance (placeholder)
ORDER_ZODIAC = {
    "🐂": "Capricorn / Aquarius (winter foundation)",
    "⛽": "Aquarius / Pisces / Aries (late winter to spring surge)",
    "🦋": "Aries / Taurus / Gemini (spring accumulation)",
    "🏟": "Cancer / Leo (summer peak)",
    "🌾": "Virgo / Libra (harvest integration)",
    "⚖":  "Libra / Scorpio (autumn balance)",
    "🖼": "Sagittarius / Capricorn (solstice restoration)",
}

# Axis intercolumniation tendency (placeholder)
AXIS_INTERCOLUMNIATION = {
    "🏛": "Pycnostyle / Systyle (tight, stable, classic spacing)",
    "🔨": "Eustyle (ideal proportional spacing, most functional)",
    "🌹": "Diastyle / Araeostyle (wide, open, feeling-forward)",
    "🪐": "Pycnostyle (compressed, demanding, maximum density)",
    "⌛": "Systyle (regular rhythm, time-based cadence)",
    "🐬": "Eustyle (space for the other person)",
}

# ---------------------------------------------------------------------------
# Generator
# ---------------------------------------------------------------------------

def deck_number(order_idx: int, axis_idx: int) -> int:
    """deck = (order_position - 1) * 6 + axis_position (1-indexed)."""
    return order_idx * 6 + axis_idx + 1


def generate_stubs() -> None:
    generated = []

    for o_idx, order in enumerate(ORDERS):
        for a_idx, axis in enumerate(AXES):
            deck = deck_number(o_idx, a_idx)
            op_prep, op_expr = OPERATOR_TABLE[axis["emoji"]]

            frontmatter = f"""\
---
deck: {deck:02d}
order: {order['emoji']} {order['name']}
axis: {axis['emoji']} {axis['name']}
liberal_art: "{order['liberal_art']}"
hermeneutic_sense: "{axis['hermeneutic_sense']}"
scale: "{axis['scale']}"
scale_dimension: "{axis['scale_dimension']}"
season: "{order['season']}"
column: "{order['column']}"
vitruvian: "{axis['vitruvian']}"
alchemical_resonance: "{ORDER_ALCHEMY[order['emoji']]}"
zodiac_resonance: "{ORDER_ZODIAC[order['emoji']]}"
intercolumniation: "{AXIS_INTERCOLUMNIATION[axis['emoji']]}"
deep_question: "{order['deep_question']}"
operators_preparatory: "{op_prep}"
operators_expressive: "{op_expr}"
status: STUB
research_required: true
---
"""
            body = STUB_BODY.format(
                deck=deck,
                order_emoji=order["emoji"],
                order_name=order["name"],
                axis_emoji=axis["emoji"],
                axis_name=axis["name"],
                liberal_art=order["liberal_art"],
                hermeneutic_sense=axis["hermeneutic_sense"],
                scale=axis["scale"],
                scale_dimension=axis["scale_dimension"],
                vitruvian=axis["vitruvian"],
                deep_question=order["deep_question"],
                season=order["season"],
                alchemical_resonance=ORDER_ALCHEMY[order["emoji"]],
                zodiac_resonance=ORDER_ZODIAC[order["emoji"]],
                intercolumniation=AXIS_INTERCOLUMNIATION[axis["emoji"]],
            )

            filename = f"deck-{deck:02d}-cosmogram.md"
            out_path  = OUT_DIR / filename
            out_path.write_text(frontmatter + body, encoding="utf-8")
            generated.append(filename)

    print(f"Generated {len(generated)} cosmogram stubs in {OUT_DIR.relative_to(REPO_ROOT)}/")
    print(f"  First: {generated[0]}")
    print(f"  Last:  {generated[-1]}")


if __name__ == "__main__":
    generate_stubs()
