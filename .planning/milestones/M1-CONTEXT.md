# M1 — Foundation Order Sweep

**Status:** IN PROGRESS (Deck 01 complete, Decks 02–06 pending)
**SCL Zip:** 🐂 🟢 (Tuscan × Growth — defining/building, self-contained)
**Contract:** `ppl-workout-generation`
**PPL Phase:** Phase 2

---

## Scope

Generate all 240 cards for the 🐂 Foundation Order (Decks 01–06).

| Deck | Axis | Cards | Status |
|------|------|-------|--------|
| 01 | 🏛 Basics | 40 | ✅ COMPLETE |
| 02 | 🔨 Functional | 40 | STUB |
| 03 | 🌹 Aesthetic | 40 | STUB |
| 04 | 🪐 Challenge | 40 | STUB |
| 05 | ⌛ Time | 40 | STUB |
| 06 | 🐬 Partner | 40 | STUB |

**Total:** 240 cards | **Complete:** 40 (16.7%)

## Order Parameters

- **Load:** ≤65% 1RM
- **Reps:** 8–15
- **Rest:** 60–90s
- **CNS:** Low
- **Difficulty ceiling:** 2/5
- **Character:** Pattern learning at sub-maximal load. The on-ramp for any skill at any level.

## Prerequisites Before Each Deck

1. Read `CLAUDE.md` + `scl-directory.md`
2. Build or verify deck identity: `deck-identities/deck-[NN]-identity.md`
3. Read deck cosmogram (v2): `deck-cosmograms/deck-[NN]-cosmogram-v2.md`
4. Confirm coverage map is populated in deck identity

## Generation Sequence

For each deck:
1. Run `/build-deck-identity [deck-number]` if identity not complete
2. Run `/generate-card` for each of 40 cards (5 Types × 8 Colors)
3. Run `bash scripts/validate-deck.sh cards/🐂-foundation/[axis-folder]/`
4. Run `python scripts/audit-exercise-coverage.py cards/🐂-foundation/[axis-folder]/`
5. Log completion in `whiteboard.md`

## Verification Criteria

- [ ] 240 cards with `status: GENERATED` or `status: CANONICAL`
- [ ] All card filenames follow `[zip]±[op] [Title].md` convention
- [ ] No duplicate primary exercises within any deck
- [ ] All exercises present in `exercise-library.md`
- [ ] Block counts within Foundation guidelines (4–6 blocks per card)
- [ ] Load stays at or below 65% in all cards

## Session Routing

Active zip: 🐂 🟢 → load `CLAUDE.md` (Foundation character) + deck identity + exercise-library sections A–Q for Foundation-relevant exercises.

---

*Next milestone:* M2 (Strength Order Sweep) — already complete ✅
