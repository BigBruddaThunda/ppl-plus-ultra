---
name: build-deck-identity
description: Create a deck identity document for a given deck number. Maps all 40 zip codes to primary exercises ensuring no Color overlap within Types.
disable-model-invocation: true
argument-hint: "[deck-number e.g. 09]"
allowed-tools: Read, Write, Edit, Bash, Grep, Glob
---

Build a deck identity document for Deck $ARGUMENTS.

## Workflow

### 1. Identify the Order and Axis
Use the deck reference table in CLAUDE.md:

| | 🏛 | 🔨 | 🌹 | 🪐 | ⌛ | 🐬 |
|-----|----|----|----|----|----|----|
| 🐂 | 01 | 02 | 03 | 04 | 05 | 06 |
| ⛽ | 07 | 08 | 09 | 10 | 11 | 12 |
| 🦋 | 13 | 14 | 15 | 16 | 17 | 18 |
| 🏟 | 19 | 20 | 21 | 22 | 23 | 24 |
| 🌾 | 25 | 26 | 27 | 28 | 29 | 30 |
| ⚖ | 31 | 32 | 33 | 34 | 35 | 36 |
| 🖼 | 37 | 38 | 39 | 40 | 41 | 42 |

### 2. Read Reference Documents
- `deck-identities/template.md` — format structure
- `deck-identities/naming-convention.md` — title rules
- Relevant Order and Axis sections of `scl-directory.md`
- `CLAUDE.md` — all constraint rules

### 3. Load the Exercise Library
Read sections of `exercise-library.md` relevant to all 5 Types for this Order×Axis:
- 🛒 Push → C, B, E (triceps)
- 🪡 Pull → D, B (posterior), E (biceps), G (hinges)
- 🍗 Legs → H, G, I
- ➕ Plus → F, J, K, L, Q
- ➖ Ultra → M, O, N, K

### 4. Map 40 Zip Codes to Primary Exercises
For each of the 5 Types, select 8 distinct primary exercises — one per Color:

**Colors:** ⚫ Teaching | 🟢 Bodyweight | 🔵 Structured | 🟣 Technical | 🔴 Intense | 🟠 Circuit | 🟡 Fun | ⚪ Mindful

**Rules for each selection:**
- Exercise must satisfy the Order ceiling (load, reps, difficulty)
- Exercise must match Axis selection bias
- Exercise must train the correct Type muscle groups
- Equipment must be within the Color's tier range
- GOLD exercises (Olympic, Plyometric, Strongman) only for 🔴 Intense or 🟣 Technical
- No barbells in 🟢 Bodyweight or 🟠 Circuit
- No two Colors within the same Type may share a primary exercise

**Color equipment constraints:**
- ⚫ Teaching: Tier 2–3
- 🟢 Bodyweight: Tier 0–2, no barbells
- 🔵 Structured: Tier 2–3
- 🟣 Technical: Tier 2–5, GOLD unlocked
- 🔴 Intense: Tier 2–4, GOLD unlocked
- 🟠 Circuit: Tier 0–3, no barbells
- 🟡 Fun: Tier 0–5
- ⚪ Mindful: Tier 0–3

### 5. Write the Identity Document
Write to `deck-identities/deck-$ARGUMENTS-identity.md`

Use the template from `deck-identities/template.md`.

Include for each zip code:
- Zip code
- Primary exercise
- Derived title (following naming-convention.md)
- Operator (derived from Axis × Color polarity table)
- Suggested block sequence (following Order × Color guidelines)

### 6. Verify No Conflicts
Run: `python scripts/audit-exercise-coverage.py cards/[order-folder]/[axis-folder]/`

If that path has existing generated cards, check for conflicts with already-generated primary exercises.

If the deck folder doesn't exist yet (stubs only), skip this step — the audit runs after generation.

## Quality Checks Before Finalizing
- [ ] All 40 zip codes have a primary exercise assigned
- [ ] No two Colors in the same Type share a primary exercise
- [ ] GOLD exercises only in 🔴 and 🟣
- [ ] No barbells in 🟢 or 🟠
- [ ] All exercises exist in exercise-library.md
- [ ] All titles follow naming-convention.md (no "The", no banned words)
- [ ] Operators correctly derived from Axis × Color polarity table
