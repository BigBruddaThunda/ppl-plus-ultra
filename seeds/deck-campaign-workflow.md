# Seed: Deck Campaign Workflow

**Status:** PLANTED — not active until promoted by whiteboard.md
**Session planted:** Session 021 — 2026-02-25
**Source:** Jake's architectural direction from Session 021 handoff

---

## Problem It Solves

Deck tasks as currently tracked are scattered and don't speak to one another. A deck has a
cosmogram, an identity doc, card generation, an audit pass, and a CANONICAL review — five
distinct phases that are currently tracked as unrelated line items. This creates the illusion
of scattered work when it is actually one coordinated campaign per deck.

---

## The Deck Campaign Model

Each deck is a **campaign** — a five-lane coordinated effort that moves from research to
final approval. Lanes run in dependency order, not in parallel with each other.

```
LANE A: Cosmogram        — Deep research (Genspark / external AI)
LANE B: Identity Doc     — Exercise mapping, duplicate audit, regen queue
LANE C: Card Generation  — 40 cards generated or retrofitted using B as reference
LANE D: Audit Pass       — Scripts validate all 40 cards (validate-deck.sh + audit-exercise-coverage.py)
LANE E: CANONICAL Review — Jake reviews and approves each card to CANONICAL status
```

**Dependency chain:**
- A and B can run in parallel (B doesn't need A to start; A enriches future regen)
- C requires B (identity doc must exist before generation starts)
- D requires C (all 40 cards must be generated or retrofitted before auditing)
- E requires D (audit must pass before review queue opens)

---

## Wave Ordering

Decks are not worked sequentially (Deck 01 → 02 → 03...). They are worked in **waves** —
batches of 3–5 decks selected for thematic, architectural, or scheduling reasons.

**Wave selection criteria (in priority order):**
1. Decks that are already partially generated (avoid orphaned work)
2. Decks with strong thematic contrast (distribute across Orders and Axes)
3. Decks that share exercise vocabulary (batch cosmogram research for efficiency)
4. Decks that balance CNS demand (don't run three heavy Order decks simultaneously)

Wave ordering is determined by Jake at the start of each multi-deck sprint. The whiteboard
tracks which wave is active and what campaign phase each deck is in.

---

## Campaign State Tracking

The whiteboard's deck table should track campaign state per deck. Format:

```
| Deck | Order × Axis | Cosmogram | Identity | Cards | Audit | CANONICAL |
|------|-------------|-----------|----------|-------|-------|-----------|
| 07   | ⛽🏛         | —         | ✅ V2    | ✅ 40 | ⬜    | ⬜        |
| 08   | ⛽🔨         | —         | ✅ V2    | ✅ 40 | ⬜    | ⬜        |
| 09   | ⛽🌹         | —         | ⬜        | ⬜    | ⬜    | ⬜        |
```

**Status symbols:**
- ⬜ Not started
- 🔄 In progress
- ✅ Complete
- ⚠️ Complete with known issues (regen queue active)
- — Not applicable (e.g., no cosmogram exists yet for early decks)

---

## On the Cosmogram Lane (Lane A)

Cosmograms live at `deck-cosmograms/deck-[NUMBER]-cosmogram.md`. They are deep research
identity documents — not workout cards. They are produced in Genspark or Claude.ai external
sessions using the research prompt at `seeds/cosmogram-research-prompt.md`.

Lane A is the **slowest lane** because it depends on external session time. It should be
started first (alongside B) so it is available before card generation begins. For decks
that already have generated cards (Decks 07 and 08), Lane A can run retroactively — the
cosmogram enriches future regen work even after initial generation is complete.

---

## On the CANONICAL Lane (Lane E)

CANONICAL review is Jake's gate. Claude Code does not move cards to `status: CANONICAL`.
The process is:
1. Deck passes audit (Lane D complete, no blocking failures)
2. Jake reviews cards from the session log or directly in the repo
3. Jake approves individual cards by updating `status: GENERATED-V2` → `status: CANONICAL`
4. When all 40 cards in a deck reach CANONICAL, the deck is marked complete in the table

CANONICAL review TBD per Jake. The table column tracks progress.

---

## Retroactive Application (Decks 07 and 08)

Both Deck 07 and Deck 08 were generated before this workflow existed. To bring them into
the campaign model:

**Deck 08** — Session 020 completed Lane B (identity doc). Lane C was already done (cards
generated). Needs: Lane D (audit pass) and Lane E (CANONICAL review).

**Deck 07** — Session 021 completed Lane B (identity doc, including V2 retrofit). Cards
were renamed and flagged for regen (Lane C partial — 18 cards need full content regen).
Needs: full Lane C completion (regen queue), Lane D, Lane E.

---

## Future Tooling (Non-Blocking)

When this seed is promoted to active work, consider building:
- Campaign state view in `whiteboard.md` as the permanent source of truth
- `scripts/deck-campaign-status.py` — reads all decks and outputs campaign table
- `scripts/validate-deck.sh` already covers Lane D — no new tooling needed there
- Git worktree pattern (see `seeds/git-worktree-pattern.md`) for parallel deck campaigns

---

## Seed Promotion Criteria

Promote this seed to active when:
- More than 3 decks are in the active campaign simultaneously
- The whiteboard task list becomes too long to read at a glance
- Jake requests a campaign dashboard view

Until then, this seed informs session planning but the whiteboard remains the source of truth.

---

🧮
