# M8 — Cosmogram First Pass

**Status:** NOT STARTED (V2 scaffolds exist, web deposits not done)
**SCL Zip:** 🐂 🌹 🟣 (Tuscan × Venustas × Technical — defining identity with precision)
**Contract:** `ppl-cosmogram-population`
**PPL Phase:** Phase 2.5

---

## Scope

Populate all 42 deck cosmograms with web-researched content. Each cosmogram is a deep identity document for one Order × Axis deck — not a workout card.

| Deck Range | Order | Count | V2 Status |
|-----------|-------|-------|-----------|
| 01–06 | 🐂 Foundation | 6 | DRAFT scaffold (no web deposits) |
| 07–12 | ⛽ Strength | 6 | DRAFT scaffold (no web deposits) |
| 13–18 | 🦋 Hypertrophy | 6 | DRAFT scaffold (no web deposits) |
| 19–24 | 🏟 Performance | 6 | DRAFT scaffold (no web deposits) |
| 25–30 | 🌾 Full Body | 6 | DRAFT scaffold (no web deposits) |
| 31–36 | ⚖ Balance | 6 | DRAFT scaffold (no web deposits) |
| 37–42 | 🖼 Restoration | 6 | DRAFT scaffold (no web deposits) |

**Total:** 42 cosmograms | **Web-researched:** 0

## What a Cosmogram Is

A cosmogram is a deep research identity document — the soul and historical context of a deck. It is NOT a workout card. It informs:
- Card generation context (which historical/cultural strands are richest for this deck)
- Operis content (featured zip descriptions, educational depth)
- Deck naming and thematic coherence

## Generation Process

**Requires external access (Genspark or Claude.ai web session):**
1. Jake opens a Genspark or Claude.ai web session with web access
2. Uses `seeds/cosmogram-research-prompt.md` as the prompt template
3. Provides the deck identity (Order × Axis combination)
4. External AI researches the full Vitruvian triad, historical figures, training philosophy
5. Output is a researched cosmogram draft
6. Jake pastes the draft into Claude Code as a handoff
7. Claude Code writes to `deck-cosmograms/deck-[NN]-cosmogram-v2.md`

## File Locations

- Research prompt: `seeds/cosmogram-research-prompt.md`
- Publication standard: `scl-deep/publication-standard.md`
- Output target: `deck-cosmograms/deck-[NN]-cosmogram-v2.md`
- V1 stubs (superseded): `deck-cosmograms/deck-[NN]-cosmogram.md`

## Dependencies

- None — cosmogram research can run in parallel with card generation
- **Blocks:** Operis pipeline (M9) — cosmograms feed featured zip descriptions in Operis editions

## Verification Criteria

- [ ] 42 V2 cosmograms with status RESEARCHED or CANONICAL (not DRAFT)
- [ ] Each cosmogram has web-deposited content (not just scaffolded sections)
- [ ] Each passes the publication standard in `scl-deep/publication-standard.md`
- [ ] V1 stubs archived or deleted (reduce confusion)

---

*Previous milestone:* M7 (Restoration)
*Next milestone:* M9 (Operis Pipeline V4)
