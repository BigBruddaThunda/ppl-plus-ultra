# M5 — Full Body Order Sweep

**Status:** NOT STARTED
**SCL Zip:** 🌾 🟢 (Composite × Growth — integrating, combining)
**Contract:** `ppl-workout-generation`
**Ppl Phase:** Phase 2

---

## Scope

Generate all 240 cards for the 🌾 Full Body Order (Decks 25–30).

| Deck | Axis | Cards | Status |
|------|------|-------|--------|
| 25 | 🏛 Basics | 40 | STUB |
| 26 | 🔨 Functional | 40 | STUB |
| 27 | 🌹 Aesthetic | 40 | STUB |
| 28 | 🪐 Challenge | 40 | STUB |
| 29 | ⌛ Time | 40 | STUB |
| 30 | 🐬 Partner | 40 | STUB |

**Total:** 240 cards | **Complete:** 0

## Order Parameters

- **Load:** ~70% 1RM
- **Reps:** 8–10
- **Rest:** 30–90s (format-dependent)
- **CNS:** Moderate
- **Difficulty ceiling:** 3/5
- **Block sequence:** `♨️ 🎼 🧈 🧩 🪫 🚂` (5–6 blocks)
- **Character:** Integration. Movements must flow into each other as one unified pattern.

## The Flow and Unity Test (MANDATORY for every 🌾 card)

Before writing any exercise sequence, verify both:
1. **Flow test:** Does each movement flow into the next without a reset?
2. **Unity test:** Is the result a single unified pattern, not a sequence?

**Passes:** Thruster (squat + press, one movement). Clean-and-press. Turkish get-up.
**Fails:** Squat then row as separate movements. Any exercise that requires repositioning equipment between moves.

🎼 Composition block is the primary container for 🌾. It governs the movement arrangement logic.

## Key Challenges

- 🌾 is the hardest order to get right conceptually — "full body" is not "superset"
- Every exercise selection must answer: "what does this flow into?"
- 🌹 Aesthetic + 🌾 Full Body: aesthetic lens applies to the quality of the unified movement, not isolation exercises
- 🪐 Challenge + 🌾 Full Body: harder variations of unified patterns (deficit thruster, paused clean-and-press)

## Verification Criteria

- [ ] 240 cards with `status: GENERATED`
- [ ] Every card passes the Flow test and Unity test
- [ ] 🎼 Composition block present in all cards
- [ ] No exercise appears that requires a positional reset before the next movement
- [ ] No pure isolation exercises (violates unity constraint)
- [ ] Block counts within guidelines (5–6 blocks)

---

*Previous milestone:* M4 (Performance)
*Next milestone:* M6 (Balance Order Sweep)
