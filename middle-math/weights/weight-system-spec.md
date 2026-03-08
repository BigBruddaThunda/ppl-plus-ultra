# Weight System Specification

Status: DRAFT

The octave weight system is the metabolic layer of Ppl±. Every SCL rule becomes a number. Every number becomes a decision.

---

## The Octave Scale

The scale runs from -8 to +8, with 0 as neutral center. The range of 17 values mirrors the octave concept from the Hero's Almanac scoring system (see `roots/octave-logic.md`), extended to a bipolar axis.

| Value | Behavioral Anchor |
|-------|------------------|
| +8 | Defining. This IS the output's character. The emoji's full identity is present. |
| +7 | Dominant. Cannot be missed. Shapes nearly every decision downstream. |
| +6 | Strong. Clearly present. Shapes most decisions. |
| +5 | Above average. Reliable influence. Shows up consistently. |
| +4 | Equal presence. Balanced. A clear contributor without dominating. |
| +3 | Contributing. Part of the texture. Noticeable to an attentive eye. |
| +2 | Noticeable if paying attention. Present in the background. |
| +1 | Background hum. Barely there but not absent. |
| 0 | Neutral. Neither sounding nor muted. |
| -1 | Slightly deprioritized. Won't lead but can follow. |
| -2 | Noticeably absent. Deprioritized in selection. |
| -3 | Actively avoided. Ranks near the bottom of any list. |
| -4 | Suppressed. Won't surface naturally. Needs explicit override to appear. |
| -5 | Excluded unless overridden. The system will not select this without instruction. |
| -6 | Contradicts the address. Appearance would undermine the zip code's integrity. |
| -7 | Violation territory. Using this at this address breaks a named SCL rule. |
| -8 | Hard exclusion. The rule says never. No override permitted. |

---

## Derivation Formula

For any given zip code (ORDER AXIS TYPE COLOR), the weight vector is computed in four steps.

### Step 1 — Primary Weights

Each of the four active dials receives +8 in its own emoji slot.

```
zip: ⛽🏛🪡🔵
→ ⛽ gets +8  (primary Order)
→ 🏛 gets +8  (primary Axis)
→ 🪡 gets +8  (primary Type)
→ 🔵 gets +8  (primary Color)
```

### Step 2 — Affinity Cascade

Each active dial declares affinities for other emojis based on the rules in `scl-directory.md`. These are positive weights: the dial is pulling those emojis toward the output.

Example (⛽ Strength affinities): ▶️ Primer +6, 🧈 Bread & Butter +8, 🏛 Basics +3, 🟣 Technical +4.

### Step 3 — Suppression Cascade

Each active dial declares suppressions for other emojis. These are negative weights: the dial is pushing those emojis away from the output.

Example (⛽ Strength suppressions): 🪞 Vanity -5, 🎱 ARAM -4, 🖼 Restoration -4, 🟠 Circuit -3.

### Step 4 — Interaction Resolution

When multiple dials have declared weights for the same emoji, apply the interaction rules in `interaction-rules.md`. The constraint hierarchy (Order > Color > Axis > Type) governs conflicts. Hard suppressions from higher-priority dials hold against lower-priority affinities. Soft weights sum and clamp to [-8, +8].

### Step 5 — Temporal Layer (optional)

Date-derived weights apply a final ±1 adjustment. The current month's Axis operator (from the rotation engine) adds +1 to that Axis's affinity emojis. The current day-of-week Order adds +1 to that Order's affinity emojis. These nudges are applied after all dial weights resolve and never override dial weights.

---

## Constraint Hierarchy for Interaction Resolution

When dials conflict:

1. **ORDER** — Hard ceiling. Order suppression at -6 or lower cannot be overridden upward by any other dial.
2. **COLOR** — Hard filter. Color suppression at -6 or lower holds against Axis and Type affinities.
3. **AXIS** — Soft bias. Axis weights add to the running total, cannot override higher-priority hard suppressions.
4. **TYPE** — Soft context. Type weights add to the running total.

---

## Worked Example: ⛽🏛🪡🔵

Zip code: ⛽ Strength + 🏛 Basics + 🪡 Pull + 🔵 Structured

**Primary weights:**
- ⛽ = +8, 🏛 = +8, 🪡 = +8, 🔵 = +8

**Selected affinity/suppression interactions (abbreviated):**

| Emoji | ⛽ declares | 🏛 declares | 🪡 declares | 🔵 declares | Net (after interaction) |
|-------|------------|------------|------------|------------|------------------------|
| ▶️ Primer | +6 | +5 | +3 | +4 | +8 (clamped) |
| 🧈 Bread & Butter | +8 | +8 | +8 | +6 | +8 (clamped) |
| 🧩 Supplemental | +3 | +4 | +3 | +3 | +8 (clamped) |
| 🪫 Release | +4 | +2 | +3 | +2 | +8 (clamped) |
| 🚂 Junction | +4 | +4 | +4 | +4 | +8 (clamped) |
| 🏛 Basics | +3 (self +8) | +8 (self) | +2 | +3 | +8 |
| 🌋 Gutter | -4 | -6 | -2 | -4 | -6 (Color hard suppression floors this) |
| 🪞 Vanity | -5 | -5 | -2 | -3 | -8 (Order + Axis suppress hard) |
| 🎱 ARAM | -4 | -4 | -2 | -3 | -8 (Order + Color push deep negative) |
| 🟢 Bodyweight | -3 | -2 | -1 | -4 | -8 (Color tier exclusion) |
| 🔴 Intense | -3 | -2 | -1 | -6 | -6 (Color hard filter) |

This is an abbreviated sample. The full vector covers all 61 emojis.

**Result:** The weight vector for ⛽🏛🪡🔵 strongly activates: ▶️ Primer, 🧈 Bread & Butter, 🧩 Supplemental, 🪫 Release, 🚂 Junction. Hard-suppresses: 🌋 Gutter, 🪞 Vanity, 🎱 ARAM, 🟢 Bodyweight, 🔴 Intense. The session structure and exercise character follow directly from these numbers.

---

## Relationship to the Almanac Octave

The Hero's Almanac v6.1 scoring system used a 1–8 scale per Dare dimension. High scores meant strong development in that dimension. Low scores indicated areas for growth. The same mathematical intuition — a single scale expressing intensity of presence — is preserved here, extended to a bipolar axis to handle both affinity and suppression.

The Almanac used the scale to score a user. The weight system uses the same scale to score a zip code. The math is the same. The subject changed.

See `roots/octave-logic.md` for the full derivation of the scale from the Almanac source.

---

🧮
