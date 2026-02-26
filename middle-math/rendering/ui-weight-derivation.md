# UI Weight Derivation

Status: SEED-LEVEL — Specifies the interface between middle-math and the Phase 4/5 design system.

How the 61-weight vector for a zip code translates to visual output. The weight vector is the input. Color, typography, tone, layout density, and background treatment are the outputs.

---

## The Core Principle

The same weight vector that selects exercises also selects how the page is built. High ⛽ weight → tight, dense, purposeful. High 🖼 weight → spacious, slow, unhurried. The visual character of the room matches the character of the workout.

This is not decoration. The rendering layer reduces cognitive friction: the user who opens a 🏟 Performance card should feel the weight of the test before reading a word.

---

## Rendering Dimension 1 — Color Palette

**Input:** The primary Color emoji's weight (+8 when primary) and secondary Color affinities (from other dials).

**Output:** Dominant palette, accent palette, highlight behavior.

Each Color emoji maps to a palette family. The primary Color is at +8 — it dominates. Secondary Color weights > +3 blend in as accents.

| Color | Palette Character |
|-------|-----------------|
| ⚫ Teaching | Deep charcoal, precise contrast, coaching tones |
| 🟢 Bodyweight | Open green, outdoor light, natural palette |
| 🔵 Structured | Clean blue-grays, precision, systematic |
| 🟣 Technical | Deep violet, focused, premium — the GOLD palette |
| 🔴 Intense | High-contrast red-orange, urgency, heat |
| 🟠 Circuit | Warm amber, motion, rotation feel |
| 🟡 Fun | Warm yellow, exploration, lightness |
| ⚪ Mindful | Soft whites, minimal saturation, breath-first |

When ⛽🏛🪡🔵 is the active zip, 🔵 dominates (+8). ⛽ contributes slight cool-gray intensity (+3 to cool tones). 🏛 contributes structure (+2 to geometric precision). 🪡 contributes no palette signal (Type has no inherent color character).

**Interface output:** `{dominant: "🔵-palette", accents: ["⛽-cool-intensity"], intensity: 0.85}`

The design system maps these to specific hex values and palette tokens. The math doesn't choose the hex — it chooses the character.

---

## Rendering Dimension 2 — Typography Treatment

**Input:** Order weight (density), Color weight (tonal register), Axis weight (precision vs. feel).

**Output:** Type size hierarchy, weight, spacing, serif/sans choice.

| Order | Typography Character |
|-------|-------------------|
| 🐂 Foundation | Body-forward. Headers secondary. Learning mode = reading mode. |
| ⛽ Strength | Compact. Dense. Numbers prominent. Set tables tight. |
| 🦋 Hypertrophy | Balanced. Exercise names prominent. Cues readable. |
| 🏟 Performance | Maximal whitespace. Single number dominates. The test is the page. |
| 🌾 Full Body | Flow typography. Blocks connected visually. Movement feel. |
| ⚖ Balance | Precise. Small type for fine detail. |
| 🖼 Restoration | Open. Large leading. Long breath between elements. |

| Color | Typography Modifier |
|-------|-------------------|
| ⚫ Teaching | Serif character. Coaching voice = instructor presence. |
| 🔴 Intense | Bold condensed. Urgency. No wasted space. |
| ⚪ Mindful | Lightest weight. Maximum leading. |
| 🟣 Technical | Monospace accents for precision data. Numbers in code-style. |

**Interface output:** `{density: 0.75, leading: 1.4, header_weight: 700, body_style: "technical-sans"}`

---

## Rendering Dimension 3 — Tonal Register

**Input:** Color weight (primary tonal driver), Operator (secondary tonal inflection).

**Output:** Prose tone instruction for any AI-assisted content generation in the room.

This maps to the tonal system from `scl-deep/publication-standard.md`. The Color Context Vernacular defines 8 tonal registers — one per Color:

| Color | Tonal Register |
|-------|---------------|
| ⚫ Teaching | Order: Foundational, serious, non-negotiable |
| 🔵 Structured | Planning: Calm, methodical, systematic |
| 🟢 Bodyweight | Growth: Steady, sustainable, consistent |
| ⚪ Mindful | Eudaimonia: Honest, genuine, clear, vulnerable |
| 🔴 Intense | Passion: Urgent, intense, high-stakes, direct |
| 🟣 Technical | Magnificence: Deep, significant, precise, transformative |
| 🟡 Fun | Play: Light, curious, exploratory, optional |
| 🟠 Circuit | Connection: Warm, relational, inclusive |

When the primary Color is 🔵 Structured, any prose in the room carries the Planning register: calm, methodical, systematic.

**Interface output:** `{tonal_register: "planning", intensity: 0.8, secondary_register: null}`

---

## Rendering Dimension 4 — Layout Density

**Input:** Order weight (block count), Color weight (rest emphasis), Axis weight (visual complexity).

**Output:** Block spacing, rest indicator size, number of elements per screen view.

| Order | Layout Character |
|-------|----------------|
| 🏟 Performance | 3–4 blocks max. Maximum whitespace. Test number dominates. |
| 🐂 Foundation | 4–6 blocks. Moderate density. Cue-heavy. |
| 🦋 Hypertrophy | 6–7 blocks. Most dense layout. Volume is the point. |
| 🖼 Restoration | 4–5 blocks. Most spacious. Each block breathes. |

**Interface output:** `{blocks_per_screen: 1.5, whitespace_ratio: 0.35, rest_indicator: "prominent"}`

---

## Rendering Dimension 5 — Background Treatment

**Input:** Order weight (palette intensity), Color weight (palette saturation), Axis weight (texture).

**Output:** Background character — saturation level, texture presence, gradient direction.

Not a garish color change. A subtle shift that the user feels without analyzing.

| Order | Background Signal |
|-------|-----------------|
| ⛽ Strength | Slight cool vignette. The room has weight. |
| 🦋 Hypertrophy | Warm gradient. Blood is moving. |
| 🏟 Performance | Near-white. The test needs a clean stage. |
| 🖼 Restoration | Soft warm wash. Safety. Unhurried. |

**Interface output:** `{saturation: 0.12, texture: null, gradient_direction: "top-to-bottom", base_tone: "cool"}`

---

## Specification Interface Summary

The rendering layer receives a weight vector and outputs a rendering descriptor object:

```json
{
  "zip_code": "⛽🏛🪡🔵",
  "color_palette": {
    "dominant": "structured-blue",
    "accents": ["strength-intensity"],
    "saturation": 0.80
  },
  "typography": {
    "density": 0.80,
    "leading": 1.35,
    "header_weight": 700,
    "body_style": "technical-sans"
  },
  "tone": {
    "register": "planning",
    "intensity": 0.85
  },
  "layout": {
    "blocks_per_screen": 1.2,
    "whitespace_ratio": 0.28,
    "rest_indicator": "prominent"
  },
  "background": {
    "saturation": 0.10,
    "texture": null,
    "gradient_direction": "top-to-bottom",
    "base_tone": "cool"
  }
}
```

The design system (Phase 4/5) maps this descriptor to specific visual tokens. The middle-math produces the descriptor. The design system produces the pixels.

---

🧮
