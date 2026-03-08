# M9 — Operis Pipeline V4

**Status:** NOT STARTED (architecture complete, prerequisites blocked)
**SCL Zip:** 🏟 ⌛ 🔵 (Corinthian × Temporitas × Structured — executing on schedule)
**Contract:** `ppl-operis-pipeline`
**Ppl Phase:** Phase 3

---

## Scope

Activate and validate the 4-prompt Operis V4 pipeline. Produce the first fully automated Operis edition from deterministic inputs.

## Prerequisites (both required)

| Prerequisite | Status | Effort |
|-------------|--------|--------|
| Historical events database (366 files populated) | 0/366 done | ~180 hours research (incremental) |
| Cosmogram population (42 decks) | 0/42 researched | M8 completion |
| Operis V4 URL enforcement patch | Bug exists | 1 session to fix |

## The V4 Pipeline (4 prompts)

Seed documents for each prompt are in `seeds/`:

| Step | Prompt | Input | Output | Location |
|------|--------|-------|--------|----------|
| 1 | Researcher | Date input | Research Brief (Contract A) | `seeds/operis-researcher-prompt.md` |
| 2 | Content Architect | Contract A | Enriched Content Brief (Contract B) with Color of the Day | `seeds/operis-content-architect-prompt.md` |
| 3 | Editor | Contracts A + B | Full Operis edition (Contract C) — 13-room sandbox | `seeds/operis-editor-prompt.md` |
| 4 | Builder | Contract C | Proofed edition + card generation for empty zips | `seeds/operis-builder-prompt.md` |

## The 13-Room Sandbox

The Operis sandbox contains:
- 8 Color siblings (one room per Color — deterministic from zip)
- 5 Content Rooms (editorially derived from Research Brief)

## Historical Events Database

Location: `operis-editions/historical-events/[MM-DD].md`
Status: 366 stub files exist, all EMPTY
Scaffolding script: `scripts/operis/scaffold_historical_events.py`

Building incrementally: Start with the current month, then expand.

## Test Run Target

First full pipeline test on a real date. Suggested: a date with known historical significance to Ppl± (e.g., the date Deck 07 was generated).

## Verification Criteria

- [ ] Historical events database: at least 30 dates populated (one month)
- [ ] URL enforcement patch applied to Prompts 1 and 2
- [ ] One complete pipeline run (P1 → P2 → P3 → P4) on a real date
- [ ] Resulting Operis edition passes editorial checklist from `scl-deep/publication-standard.md`
- [ ] Edition committed to `operis-editions/YYYY/MM/YYYY-MM-DD.md`
- [ ] Builder step generates or validates all cited zip codes

---

*Previous milestone:* M8 (Cosmogram First Pass)
*Next milestone:* M10 (Experience Layer)
