# cards/AGENTS.md — Card Generation Context

This directory contains 1,680 workout card files organized by Order/Axis/Type.
When working in this directory, the root AGENTS.md provides the full rule set.
This file adds generation-specific reminders.

---

## Card File Status

- `status: EMPTY` — stub awaiting generation
- `status: GENERATED` — workout written, pending review
- `status: CANONICAL` — reviewed and approved by Jake Berry

---

## Generation Reminders

- Every exercise MUST exist in `exercise-library.md` (root). No exceptions.
- Order ceiling is absolute. If a dial conflict exists, Order wins.
- GOLD exercises (Olympic lifts, advanced plyometrics, spinal-loaded ballistics) require 🔴 or 🟣.
- 🟠 Circuit requires loop logic: no two adjacent stations target the same muscle group.
- 🏟 Performance: 3–4 blocks. Test, record, leave. No supplemental work.
- 🌾 Full Body: every movement must flow into the next. Apply Flow and Unity test.
- Before generating, check for a deck identity document at deck-identities/deck-[XX]-identity.md
- If it exists, read the zip identity line for this specific zip code as the generation seed
- Card titles must follow deck-identities/naming-convention.md — no vibe names, no "Protocol"
- Each Color variant of a Type must use a different primary exercise in 🧈 Bread & Butter

---

## Block Sequences by Order

```
🐂 Foundation:   4–6 blocks  ♨️ 🔢/🛠 🧈 🧩 🧬 🚂
⛽ Strength:     5–6 blocks  ♨️ ▶️ 🧈 🧩 🪫 🚂
🦋 Hypertrophy:  6–7 blocks  ♨️ ▶️ 🧈 🗿 🪞/🧩 🪫 🚂
🏟 Performance:  3–4 blocks  ♨️ 🪜 🧈 🚂
🌾 Full Body:    5–6 blocks  ♨️ 🎼 🧈 🧩 🪫 🚂
⚖ Balance:      5–6 blocks  ♨️ 🏗 🧈 🧩 🪫 🚂
🖼 Restoration:  4–5 blocks  🎯 🪫 🧈 🧬 🚂
```

---

## Color Modifiers

- ⚫ Teaching: +extended rest, +🛠 Craft emphasis
- 🟢 Bodyweight: equipment collapses to tier 0–2, no barbells
- 🔵 Structured: +🪜 Progression prominent
- 🟣 Technical: fewer blocks, extended rest, quality focus
- 🔴 Intense: 🧩 may superset, 🌋 Gutter possible
- 🟠 Circuit: 🧈/🧩/🪞 merge into 🎱 ARAM
- 🟡 Fun: +🏖 Sandbox and 🌎 Exposure permitted
- ⚪ Mindful: extended ♨️ and 🪫, slow tempo throughout

---

## Review guidelines

- Verify every exercise against `exercise-library.md`
- Verify Order ceilings, GOLD gates, Color tiers
- Verify all 15 format elements
- Verify tonal rules
- Flag P0 and P1 only
