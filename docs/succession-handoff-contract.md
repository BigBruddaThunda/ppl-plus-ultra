# Ppl± Succession Handoff Contract — Batch Deck Generation

Use this contract to hand off one deck-generation session to the next Codex agent.

## Session Header (fill before starting)

- **Branch:** `work`
- **Session link:** `<<PASTE_GITHUB_SESSION_LINK>>`
- **Deck number:** `<<01-42>>`
- **Order round:** `<<🐂|⛽|🦋|🏟|🌾|⚖|🖼>>`
- **Operator:** `Codex`
- **Timestamp (UTC):** `<<YYYY-MM-DDTHH:MM:SSZ>>`

---

## What was already completed before this handoff

- Batch tooling added:
  - `scripts/batch-generate-deck.py` (per-deck orchestrator)
  - `scripts/batch-generate-all.py` (round orchestrator)
  - `scripts/deck-identity-scaffold.py` (identity scaffolding from selector + registries)
- Deck processed in this lineage: **Deck 13 (🦋🏛)**.
- Deck 13 identity regenerated and deck cards batch-generated.
- Validation report path pattern established:
  - `reports/batch-gen/deck-XX-validation.md`

---

## Codex Contract: Batch Deck Generation — Fill All 1,680 Rooms

### Objective

Generate `GENERATED` status workout cards for every `EMPTY` stub across all 42 decks.

### Current-state framing

- Known completed decks before broad batch: 01, 07, 08, 09, 10, 11, 12.
- Decks 13–42 require identity scaffolds and generation.
- This is a first-pass fill, not canonical review.

### Phase A — Scaffold missing deck identities

Script:

```bash
python scripts/deck-identity-scaffold.py --missing
```

Or deck-specific:

```bash
python scripts/deck-identity-scaffold.py <<DECK>> --overwrite
```

Expected behavior:
1. Read `middle-math/zip-registry.json`
2. Read `middle-math/exercise-registry.json`
3. Call selector per zip (`scripts/middle-math/exercise_selector.py`)
4. Assign unique primary exercise per Type row (8 unique in each Type row)
5. Write `deck-identities/deck-XX-identity.md`

### Phase B — Generate one deck

Command:

```bash
python scripts/batch-generate-deck.py --deck <<DECK>>
```

Optional knobs:

```bash
python scripts/batch-generate-deck.py --deck <<DECK>> --dry-run
python scripts/batch-generate-deck.py --deck <<DECK>> --limit 1
python scripts/batch-generate-deck.py --deck <<DECK>> --generator-cmd "<your command>"
```

Per-card behavior contract:
1. Read stub frontmatter
2. Read deck identity zip line + primary exercise
3. Check primary exercise is in `exercise-library.md`
4. Read exercise-content file (if present)
5. Pull supplemental candidates from selector
6. Generate full workout card using SCL/AGENTS/CLAUDE constraints
7. Write content
8. Update `status: EMPTY -> GENERATED`
9. Rename file to `[zip]±[operator] [Title].md`
10. Run `scripts/validate-card.py`
11. Continue on failures; do not abort full deck
12. Log zip, title, validation status, primary exercise

### Hard constraints

```python
ORDER_CEILINGS = {
    '🐂': {'load': 65, 'reps_min': 8, 'reps_max': 15, 'difficulty': 2, 'blocks_min': 4, 'blocks_max': 6},
    '⛽': {'load_min': 75, 'load_max': 85, 'reps_min': 4, 'reps_max': 6, 'difficulty': 4, 'blocks_min': 5, 'blocks_max': 6},
    '🦋': {'load_min': 65, 'load_max': 75, 'reps_min': 8, 'reps_max': 12, 'difficulty': 3, 'blocks_min': 6, 'blocks_max': 7},
    '🏟': {'load_min': 85, 'load_max': 100, 'reps_min': 1, 'reps_max': 3, 'difficulty': 5, 'blocks_min': 3, 'blocks_max': 4},
    '🌾': {'load': 70, 'reps_min': 8, 'reps_max': 10, 'difficulty': 3, 'blocks_min': 5, 'blocks_max': 6},
    '⚖': {'load': 70, 'reps_min': 10, 'reps_max': 12, 'difficulty': 3, 'blocks_min': 5, 'blocks_max': 6},
    '🖼': {'load': 55, 'reps_min': 12, 'reps_max': 15, 'difficulty': 2, 'blocks_min': 4, 'blocks_max': 5},
}

COLOR_TIERS = {
    '⚫': (2, 3), '🟢': (0, 2), '🔵': (2, 3), '🟣': (2, 5),
    '🔴': (2, 4), '🟠': (0, 3), '🟡': (0, 5), '⚪': (0, 3),
}

GOLD_COLORS = {'🟣', '🔴'}
NO_BARBELL = {'🟢', '🟠'}
```

### Phase C — Round orchestration

Command:

```bash
python scripts/batch-generate-all.py
```

Round order:
1. 🐂 Foundation: 02, 03, 04, 05, 06
2. ⛽ Strength: 11
3. 🦋 Hypertrophy: 13, 14, 15, 16, 17, 18
4. 🏟 Performance: 19, 20, 21, 22, 23, 24
5. 🌾 Full Body: 25, 26, 27, 28, 29, 30
6. ⚖ Balance: 31, 32, 33, 34, 35, 36
7. 🖼 Restoration: 37, 38, 39, 40, 41, 42

Commit convention (one commit per deck generation):

```text
gen(deck-XX): batch generate 40 cards ORDER [Name]
```

### Phase D — Post-batch audit

```bash
python scripts/progress-report.py
bash scripts/validate-deck.sh cards/
python scripts/audit-exercise-coverage.py cards/
```

Write summary to:

- `reports/batch-gen-summary.md`

Must include:
- Total cards generated
- Validation pass/fail per deck
- Coverage stats
- Duplicate primary-exercise flags
- Priority regen queue

---

## Per-session task execution checklist

- [ ] Read `whiteboard.md`
- [ ] Read `AGENTS.md`
- [ ] Ensure deck identity is present/updated
- [ ] Run per-deck generation
- [ ] Run deck validation (`bash scripts/validate-deck.sh ...`)
- [ ] Commit deck outputs
- [ ] Record session link in stamp table

---

## 42 Deck Session Stamp Table

| Deck | Session Link | Branch | Status |
|---|---|---|---|
| 01 |  | work | done (historical) |
| 02 |  | work | pending |
| 03 |  | work | pending |
| 04 |  | work | pending |
| 05 |  | work | pending |
| 06 |  | work | pending |
| 07 |  | work | done (historical) |
| 08 |  | work | done (historical) |
| 09 |  | work | done (historical) |
| 10 |  | work | done (historical) |
| 11 |  | work | done (historical) |
| 12 |  | work | done (historical) |
| 13 |  | work | done in this tooling lineage |
| 14 |  | work | pending |
| 15 |  | work | pending |
| 16 |  | work | pending |
| 17 |  | work | pending |
| 18 |  | work | pending |
| 19 |  | work | pending |
| 20 |  | work | pending |
| 21 |  | work | pending |
| 22 |  | work | pending |
| 23 |  | work | pending |
| 24 |  | work | pending |
| 25 |  | work | pending |
| 26 |  | work | pending |
| 27 |  | work | pending |
| 28 |  | work | pending |
| 29 |  | work | pending |
| 30 |  | work | pending |
| 31 |  | work | pending |
| 32 |  | work | pending |
| 33 |  | work | pending |
| 34 |  | work | pending |
| 35 |  | work | pending |
| 36 |  | work | pending |
| 37 |  | work | pending |
| 38 |  | work | pending |
| 39 |  | work | pending |
| 40 |  | work | pending |
| 41 |  | work | pending |
| 42 |  | work | pending |

---

## Ready-to-paste prompt packet for each deck chat

```text
Codex Task: Deck <<XX>> batch generation (PPL±)

1) Read whiteboard.md and AGENTS.md first.
2) Run: python scripts/deck-identity-scaffold.py <<XX>> --overwrite
3) Run: python scripts/batch-generate-deck.py --deck <<XX>>
4) Run: bash scripts/validate-deck.sh "cards/<<order-folder>>/<<axis-folder>>"
5) Commit with: gen(deck-<<XX>>): batch generate 40 cards ORDER <<OrderName>>
6) Report pass/fail counts and include reports/batch-gen/deck-<<XX>>-validation.md summary.
7) Update docs/succession-handoff-contract.md stamp table row for deck <<XX>> with session link.

Non-negotiable constraints:
- Respect AGENTS.md SCL rules and 15 required format elements.
- Keep Order ceilings and Color equipment gates.
- GOLD only in 🟣/🔴.
- No barbell in 🟢/🟠.
- Use 🎱 ARAM for 🟠 circuit structure.
- Do not stop the full deck batch on one card failure; log failure and continue.
```
