# Operis Weight Derivation

Status: SEED-LEVEL — Specifies the interface between the daily zip code's weight vector and Operis editorial decisions.

How the rotation engine's daily zip code shapes the Operis edition. The weight vector is the input. Content type activation, department count, tonal register, and cosmogram vocabulary are the outputs.

Source relationship: `seeds/operis-architecture.md` defines the editorial structure. This document defines the mathematical derivation that populates it.

---

## The Core Principle

The Operis is not random. Every editorial decision traces back to a weight. The day's zip code produces a weight vector. That vector shapes what the Operis editor (human or algorithm) emphasizes, de-emphasizes, and surfaces.

The editorial character of a Tuesday ⛽ Strength edition is different from a Sunday 🖼 Restoration edition — not because someone decided it would be, but because the weight vectors for those two addresses are different in computable, derivable ways.

---

## Derivation 1 — Content Type Activation

**Input:** The Axis weight for the day's zip code.

**Background:** The 109 content types (from `seeds/content-types-architecture.md`) each have an Axis home — the floor of the building where they live. The day's Axis weight determines which content types are amplified.

**Logic:**

```python
def get_active_content_types(daily_zip):
    weight_vector = compute_weight_vector(daily_zip)
    axis = parse_zip(daily_zip)[1]

    # Get all content types homed on today's Axis
    primary_types = [ct for ct in CONTENT_TYPES if ct.axis_home == axis]

    # Get content types with cross-floor appearance permissions above threshold
    secondary_types = [ct for ct in CONTENT_TYPES
                       if ct.axis_home != axis
                       and ct.cross_floor_weight.get(axis, 0) >= 3]

    return {
        "primary":   primary_types,
        "secondary": secondary_types,
        "suppressed": [ct for ct in CONTENT_TYPES
                       if weight_vector.get(ct.axis_home, 0) <= -4]
    }
```

**Example:** Daily zip = ⛽🏛🪡🔵.
- Axis = 🏛 Basics
- Primary content types: Fundamentals, Historical (Grammar lens), Technical Analysis
- Secondary: Content types with cross-floor weight to 🏛 ≥ 3 (e.g., Performance data from 🪐)
- Suppressed: Content types homed on Axes with weight ≤ -4 in this vector

---

## Derivation 2 — Department Count

**Input:** The Order weight for the day's zip code.

**Background:** The Operis weekly cadence (from `seeds/operis-architecture.md`) specifies department counts by day:
- 🐂 Foundation (Monday): Shorter edition, foundational
- 🦋 Hypertrophy (Wednesday): Longest, most dense
- 🏟 Performance (Thursday): Minimal, focused on the test
- 🖼 Restoration (Sunday): Gentle, fewer active departments

**Logic:** Map Order weight to department count range. The existing schedule in `seeds/operis-architecture.md` already encodes this — the weight derivation is the mathematical formalization of what the schedule describes in prose.

```python
ORDER_DEPARTMENT_COUNTS = {
    🐂: (5, 7),    # Monday — shorter
    ⛽: (7, 9),    # Tuesday
    🦋: (9, 12),   # Wednesday — longest
    🏟: (3, 5),    # Thursday — minimal
    🌾: (6, 8),    # Friday
    ⚖: (6, 8),    # Saturday
    🖼: (4, 6),    # Sunday — gentle
}
```

---

## Derivation 3 — Tonal Register

**Input:** The Color weight for the day's zip code.

**Background:** The Color Context Vernacular (from `scl-deep/publication-standard.md`) maps each Color to a tonal register. The day's primary Color sets the editorial voice.

**Logic:**

```python
COLOR_TONAL_REGISTER = {
    ⚫: "order",          # Foundational, serious
    🔵: "planning",       # Structured, methodical
    🟢: "growth",         # Steady, sustainable
    ⚪: "eudaimonia",     # Honest, genuine, vulnerable
    🔴: "passion",        # Urgent, intense, direct
    🟣: "magnificence",   # Deep, significant, precise
    🟡: "play",           # Light, curious, exploratory
    🟠: "connection",     # Warm, relational, inclusive
}

def get_operis_tone(daily_zip, user_color_choice):
    color = user_color_choice  # or system default if no user choice
    return COLOR_TONAL_REGISTER[color]
```

Note: The Operis is a publication, not a personal workout card. The tonal register for the edition may differ from the individual user's Color choice. The default tonal register for the Operis is derived from the rotation engine's suggested Color for the day (or a system default if no Color preference is set).

---

## Derivation 4 — Cosmogram Vocabulary

**Input:** The full 61-weight vector for the day's zip code.

**Background:** Each deck has a cosmogram — a deep research document giving the deck an identity, vocabulary, and cultural field. The deck whose weight vector most closely aligns with the day's zip code has its vocabulary active.

**Logic:**

```python
def get_active_cosmogram(daily_zip):
    daily_vector = compute_weight_vector(daily_zip)

    # Find the deck whose Order × Axis matches the day's zip most closely
    order, axis = parse_zip(daily_zip)[:2]

    # Primary: exact Order × Axis match (the deck for this combination)
    primary_deck = get_deck_by_order_axis(order, axis)

    # Secondary: highest cosine similarity to the daily weight vector
    all_deck_vectors = {deck: compute_deck_weight_vector(deck) for deck in ALL_DECKS}
    secondary_deck = max(all_deck_vectors,
                         key=lambda d: cosine_similarity(daily_vector, all_deck_vectors[d]))

    return {
        "primary":   primary_deck,
        "secondary": secondary_deck,
    }
```

The primary cosmogram's vocabulary surfaces in the edition's language and framing. The secondary cosmogram adds depth — it is the deck the day's energy most resembles even if the address doesn't match exactly.

Note: This derivation requires cosmograms to be populated. Currently, no cosmograms are populated (status: STUB across all 42 decks). This derivation activates when the first cosmogram is generated.

---

## Specification Interface Summary

The Operis weight derivation produces an editorial configuration object:

```json
{
  "daily_zip": "⛽🏛🪡🔵",
  "content_types": {
    "primary":   ["fundamentals", "historical-grammar", "technical-analysis"],
    "secondary": ["performance-data", "exercise-science"],
    "suppressed": ["somatic-movement", "partner-work"]
  },
  "department_count_range": [7, 9],
  "tonal_register": "planning",
  "cosmogram": {
    "primary":   "deck-07",
    "secondary": "deck-13"
  },
  "zip_codes": {
    "forced_minimum": 8,
    "forced_maximum": 12
  }
}
```

The Operis editor (human or algorithm) uses this configuration to build the edition. The configuration is derived. The judgment is human.

---

## Color of the Day — Weight Derivation (PLANNED)

The Color of the Day is the Operis editorial system's primary rendering decision. It is currently determined by human editorial judgment in Prompt 2 (the Content Architect). When the pipeline transitions to automated execution, the Color determination will need a scoring mechanism.

### Input Signals

Each input maps to one or more of the 8 Colors with a signal weight:

**Research brief character analysis.** Classify the dominant character of the day's historical events. Events clustering around teaching/foundations → ⚫. Events clustering around construction/engineering → 🔵. Events clustering around athletic achievement → 🔴. Events clustering around cultural production → 🟡. Events clustering around community/civic life → 🟠. Events clustering around precision/scientific discovery → 🟣. Events clustering around agriculture/organic growth → 🟢. Events with no dominant cluster or reflective character → ⚪.

**Seasonal position weights.** Derived from the annual breath rhythm in `seeds/almanac-macro-operators.md`. January–April inhale favors ⚫🟢🔵⚪. May–August exhale favors 🔴🟠🟡🟢. September–October catch-breath favors ⚪🟣⚫. November–December close favors 🟣🔵.

**Monthly operator tonal signature.** Each operator has a natural Color affinity based on its Latin semantic field. 📍 pono → ⚫ (placing, positioning). 🧲 capio → 🟠 (receiving, taking in). 🧸 fero → 🟢 (carrying, transferring organically). 👀 specio → 🟣 (inspecting, observing closely). 🥨 tendo → 🔴 (extending, pushing limits). 🤌 facio → 🔵 (executing, performing). 🚀 mitto → 🔴 (launching, maximum commitment). 🦢 plico → 🟣 (folding, layering). 🪵 teneo → ⚪ (holding, persisting). 🐋 duco → 🔵 (orchestrating). ✒️ grapho → 🔵 (documenting). 🦉 logos → 🟣 (reasoning).

**Liberal Art of the day.** Grammar → ⚫. Logic → 🟣. Rhetoric → 🟠. Arithmetic → 🔵. Geometry → 🟢. Music → 🟡. Astronomy → ⚪.

**Current events urgency level.** Scale of 0–3. 0 = no urgent events (no override). 1 = notable event (mild signal toward 🔴). 2 = significant event (strong signal toward 🔴). 3 = emergency (🔴 override, supersedes all other signals).

**Content lane strength profile.** Which lanes produced the strongest material? Each lane's strength (rated 0–3 by Prompt 2) contributes a signal toward its own Color.

**Temporal arc.** Yesterday's Color receives a negative weight (avoid repetition). The Color two days ago receives a mild negative weight. This ensures the week breathes.

### Resolution

Sum the signal weights for each of the 8 Colors. The Color with the highest aggregate weight is the recommendation. The margin between first and second place determines the confidence level:

- Margin > 3: High confidence. Color is clear.
- Margin 1–3: Moderate confidence. Color is the recommendation but the runner-up is defensible.
- Margin < 1: Close call. Either Color works. Note the close call in the editorial reasoning.

### Status

PLANNED. This scoring mechanism will be built after 30–60 manually-determined Colors provide calibration data for the signal weights. The manual determination (human editorial judgment in Prompt 2) is the v1 implementation. The scoring mechanism is the v2 implementation. Both produce the same output — a Color and an editorial reasoning paragraph.

---

🧮
