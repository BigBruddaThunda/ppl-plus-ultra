# Codebase Concerns

**Analysis Date:** 2026-03-07

---

## Tech Debt

**1,400 stub cards — generation pipeline is the critical path**
- Issue: 1,400 of 1,680 card files are pure stubs (`[zip]±.md` with no generated content). 262 cards are generated across 8 decks (01, 07–12). 34 decks untouched.
- Files: `cards/` — every subdirectory under ungenerated Orders/Axes
- Impact: The entire downstream application (HTML render → user session → history → preference data) is blocked on these files. A stub that stays a stub produces no user value.
- Fix approach: Systematic deck sweeps per the whiteboard Fervor section. Current pace: ~40 cards/session when focused. At 1,400 remaining, ~35 generation sessions needed. Delegate to card-generator subagent to preserve main context.

**Deck identity scaffolds: 35 of 42 are SCAFFOLD-status stubs**
- Issue: Only Decks 07–12 have complete identity documents with coverage maps and color differentiation logic. Decks 01–06 and 13–42 identities are scaffolded but contain empty coverage maps and `[Pending.]` sections.
- Files: `deck-identities/deck-13-identity.md` through `deck-identities/deck-42-identity.md` (all SCAFFOLD status)
- Impact: Generating cards without a complete identity risks duplicate primary exercises across Color variants — the most common generation error. The rule "no two Color variants use the same primary exercise" cannot be enforced without the coverage map.
- Fix approach: Build each deck identity in full before generation begins. The `/build-deck-identity` skill handles this. Blocks deck generation for all unstarted decks.

**exercise-library.md has no version number beyond v.0**
- Issue: The exercise library is documented as "v.0" with no defined version bump criteria. It is the exercise authority for all card generation. No systematic process for adding exercises, retiring bad entries, or resolving conflicts.
- Files: `exercise-library.md`, `middle-math/exercise-registry.json`
- Impact: If an exercise needs to be corrected or retired, there is no process for propagating the change to already-generated cards that used it. Version bump criteria undefined per whiteboard note.
- Fix approach: Define v.1 criteria. Minimum: named conditions that trigger a version bump. Stretch: automated cross-reference between `exercise-registry.json` and generated card content to detect cards using non-library exercises.

**`movement_pattern: core-stability` catch-all contaminates 1,256 exercises**
- Issue: The exercise registry (`middle-math/exercise-registry.json`) assigns `core-stability` as the catch-all `movement_pattern` for ~1,256 of 2,085 exercises — exercises that are actually carries, conditioning patterns, strongman movements, etc. This was a known data issue deferred from Session 038.
- Files: `middle-math/exercise-registry.json`, `exercise-content/` (all ~1,256 affected files have `movement_pattern: core-stability` in frontmatter)
- Impact: The exercise selector (`scripts/middle-math/exercise_selector.py`) applies movement pattern scoring. Contaminated patterns degrade selection quality for ➕ Plus and ➖ Ultra types especially.
- Fix approach: CX-43 Selector V2 documented an 83-entry catch-all preprocessing override. A full disambiguation pass on the 1,256 affected exercises is needed — carry, conditioning, strongman, plyometric patterns need explicit assignment.

**Stale status references in seed documents**
- Issue: 8 seed/doc files flagged in whiteboard.md (Session 036 note) carry stale card counts and status references. They have not been updated since being written.
- Files: `seeds/claude-code-build-sequence.md`, `seeds/platform-architecture-v2.md`, `seeds/operis-architecture.md`, `seeds/operis-prompt-pipeline.md`, `.codex/NEXT-ROUND-HANDOFF.md`, `AGENTS.md`, `cards/AGENTS.md`, `middle-math/ARCHITECTURE.md`
- Impact: Low for generation. High for any new contributor or agent reading these files as orientation material — they will get false context about project state.
- Fix approach: Update opportunistically when each file is next touched. Jake-blocked items (color-context-vernacular vocabulary, order-parameters vocabulary) require Jake input first.

**Archideck layer initialized on a branch, not merged**
- Issue: The entire `archideck/` directory was initialized on branch `claude/build-archideck-layer-V47rx`. The branch has not merged to main. `archideck/CONTRACTS.md` has no zip codes in the main branch yet.
- Files: `archideck/` (branch only as of 2026-03-07), `whiteboard.md` (Archideck section)
- Impact: Any generation work referencing Archideck context is operating against unmerged infrastructure. PPL± card generation continues normally on main — the risk is cross-project contamination if agents conflate branch state with main state.
- Fix approach: Define merge criteria for the Archideck branch. Test stability, then merge as additive layer. Whiteboard notes this explicitly.

---

## Known Bugs / Data Issues

**Exercise validator does not cross-reference the exercise library**
- Symptoms: `scripts/validate-card.py` reports "No numbered exercises found to check (check manually if unexpected)" for generated cards. The CLAUDE.md mandate — "all exercises must come from exercise-library.md" — is not automatically enforced.
- Files: `scripts/validate-card.py` (lines ~40–50 exercise check section), `scripts/lint-scl-rules.py`
- Trigger: Any generated card. The validator checks structural format (blocks, zip parse, JUNCTION, SAVE) but skips exercise-library cross-reference.
- Workaround: Manual review. `scripts/audit-exercise-coverage.py` checks for duplicates within a deck but not library membership.

**Operis V4 pipeline: Contract A/B URL enforcement gaps**
- Symptoms: Prompt 1 (Researcher) missing source URLs in output. Prompt 2 (Content Architect) missing per-lane URLs in the Research Brief handoff. Contract C parser hardening is complete but depends on valid upstream contracts.
- Files: `seeds/operis-researcher-prompt.md`, `seeds/operis-content-architect-prompt.md`, `operis-editions/2026/03/2026-03-02.md` (first edition with gaps)
- Trigger: Running the V4 pipeline on any date. The pipeline test on 2024-07-26 was blocked on this fix.
- Workaround: Do not re-run the Operis pipeline until URL enforcement is patched.

**Two cosmogram files exist per deck (v1 + v2), both DRAFT**
- Symptoms: `deck-cosmograms/` contains both `deck-[N]-cosmogram.md` (v1 format, STUB status) and `deck-[N]-cosmogram-v2.md` (v2 format, DRAFT status with subject scaffolds but no web deposits). The v1 files are superseded but not removed.
- Files: `deck-cosmograms/deck-01-cosmogram.md` through `deck-42-cosmogram.md` (42 v1 files), `deck-cosmograms/deck-01-cosmogram-v2.md` through `deck-42-cosmogram-v2.md` (42 v2 files)
- Impact: Any agent reading "the cosmogram" for a deck must know to use the v2 file. The v1 files are misleading stubs. 84 files total for 42 decks.
- Fix approach: Archive or delete v1 stubs once v2 population begins. Until then, agents must explicitly reference v2 files.

---

## Missing Critical Features

**No automated exercise-library cross-reference in CI**
- Problem: Generated cards can contain exercises not in `exercise-library.md`. There is no automated gate that catches this.
- Blocks: Content accuracy guarantee. The CLAUDE.md states "content accuracy is the highest priority constraint." A hallucinated exercise propagates through `.md → HTML render → user session → user history → preference data`.
- Recommended fix: Add an exercise name extraction pass to `scripts/lint-scl-rules.py` or a new `scripts/check-exercise-library.py`. Parse exercise names from card content sections and verify each against `exercise-library.md` or `middle-math/exercise-registry.json`.

**Historical events database: 366 files, 0 populated**
- Problem: All 366 `operis-editions/historical-events/MM-DD.md` files exist as EMPTY stubs (`status: EMPTY`, `events: []`). The Operis Prompt 1 (Researcher) checks this path before web research — it always gets a cache miss.
- Blocks: Full Operis V4 pipeline automation. Each date requires hand-researched historical events. Estimated ~180 hours of research to fully populate.
- Files: `operis-editions/historical-events/01-01.md` through `12-31.md` (366 files)
- Recommended fix: Prioritize dates with active Operis editions first. Build incrementally — one month at a time is achievable per work session.

**Ralph Loop batch orchestrator not built**
- Problem: CX-17 (`validate-pod.py`, `ralph-batch.sh`) is OPEN and blocked on Jake's review of the Deck 07 pod prototype. 41 remaining zip-web pods cannot be populated without this.
- Files: None yet — `validate-pod.py` and `ralph-batch.sh` do not exist
- Blocks: Zip-web navigation layer. Users cannot browse the full address space until pods exist.
- Fix approach: Jake approves `deck-07-pods.md` prototype, then CX-17 builds the batch orchestrator.

**No CANONICAL-status cards exist**
- Problem: Zero cards have reached `status: CANONICAL`. All generated cards are `GENERATED` or `GENERATED-V2`. The CANONICAL review (Jake reads 40 cards as a user — the "Gemba test") has not happened.
- Files: All generated card files in `cards/`
- Blocks: Quality confidence. CANONICAL is the approved master version. Without it, the generation standard cannot be confirmed as correct for downstream porting.
- Fix approach: Deck 08 is the designated candidate for first CANONICAL review (whiteboard ⚪ section). Jake reviews as a user, not as an editor.

**Vocabulary standard compliance not audited on existing cards**
- Problem: `scl-deep/vocabulary-standard.md` defines banned and approved word lists. None of the 262 generated cards have been checked against it.
- Files: All generated cards in `cards/⛽-strength/`, `cards/🐂-foundation/`; `scl-deep/vocabulary-standard.md`
- Blocks: Publication standard compliance. CANONICAL review likely surfaces violations.
- Fix approach: Run the whiteboard ⚪ task: "Vocabulary standard audit on Decks 07–09."

---

## Fragile Areas

**Card generation relies on sole-operator model with no checklist enforcement**
- Files: All card generation (1,680 target files in `cards/`)
- Why fragile: The 15 required format elements and full validation checklist in CLAUDE.md are honor-system enforced during generation. The PostToolUse hook runs `validate-card.py`, but that validator checks structural presence (JUNCTION, SAVE, block count) not semantic correctness (exercise library membership, tonal rule compliance, Gold gate logic).
- Safe modification: The existing `scripts/validate-card.py` is the right foundation. Extending it with exercise library checks and tonal rule detection would harden the gate.
- Test coverage gaps: No test suite for `validate-card.py` itself. If the validator has a bug, it passes silently.

**Middle-math specs are DRAFT — not authoritative until coupled to actual rendering**
- Files: `middle-math/weights/` (all 7 weight files), `middle-math/rendering/`, `middle-math/user-context/`
- Why fragile: All weight declarations are first-draft. The weight vector engine (`scripts/middle-math/weight_vector.py`) produces 1,680 vectors but the weights themselves are educated estimates, not validated against real user behavior. Any downstream system built on these weights inherits their uncertainty.
- Safe modification: Treat middle-math outputs as provisional until user feedback loops exist. Do not hard-code middle-math values into application logic before Phase 4 data is available.
- Test coverage gaps: `weight_vector.py` has a `--validate` flag that passes structure checks, but no validation against expected output values for known zip codes.

**Cosmogram v2 content is machine-generated scaffolding, not researched**
- Files: `deck-cosmograms/deck-[01-42]-cosmogram-v2.md` (all 42 files)
- Why fragile: All 42 v2 cosmograms were generated by Codex in a single first-pass session (2026-03-07) using no web research. They contain plausible-sounding subject scaffolds that may be historically or factually imprecise. Cosmograms feed card generation context.
- Safe modification: Flag any cosmogram-sourced content in card generation. Only use cosmograms for structural guidance (which branches are richest) not factual claims until web deposits land.
- Test coverage gaps: No review of cosmogram content against external sources. `seeds/cosmogram-research-prompt.md` and `scl-deep/publication-standard.md` define the standard; no audit exists.

---

## Scaling Limits

**262/1,680 cards at current session throughput**
- Current capacity: ~40 cards per focused generation session
- Limit: 1,418 cards remain across 34 unstarted decks + partially started decks. Each card requires a full 15-element format, exercise selection, and validation pass.
- Scaling path: Delegate generation to `card-generator` subagent (Opus) to preserve main context. Batch by deck (40 cards × 34 decks = 34 sessions minimum). Deck identity must precede each deck's generation.

**exercise-content/ directory: 2,085 files with minimal quality control**
- Current capacity: 2,085 exercise content files exist. All generated in batch passes (Sessions 037–045).
- Limit: Spot checks show 441–478 words per file. Content was machine-generated at scale. No systematic review against ExRx accuracy standard in `scl-deep/vocabulary-standard.md`.
- Scaling path: Quality review is deferred to `scl-deep/publication-standard.md` compliance pass. The `external-refs.json` (2,085 null docks) in `middle-math/exercise-engine/` exists to receive ExRx partner links — 0 filled currently.

---

## Dependencies at Risk

**ExRx partnership dependency for exercise content accuracy**
- Risk: `seeds/exrx-partnership-brief.md` documents a planned ExRx partnership to provide authoritative exercise references. The `middle-math/exercise-engine/external-refs.json` file has 2,085 null entries waiting for ExRx URLs. Without this partnership, exercise content accuracy relies entirely on the generation model's training data.
- Impact: All 2,085 exercise content files in `exercise-content/` have unverified factual claims. If ExRx partnership does not materialize, an alternative authoritative source is needed.
- Migration plan: Identify fallback sources (PubMed, NSCA) and manually populate highest-priority exercise refs (the ~40 exercises that appear most frequently in generated cards).

**Operis pipeline blocked on two research-intensive prerequisites**
- Risk: Both blocking prerequisites for Operis automation are research-intensive human tasks: (1) historical events database — 366 dates, ~180 hours; (2) cosmogram population — 42 decks, each requiring Genspark web-access sessions.
- Impact: The Operis pipeline cannot automate without these. The front door of the application remains manual.
- Migration plan: Build incrementally. Populate historical events for the current month first. Schedule dedicated cosmogram sessions using `seeds/cosmogram-contract-prompt-v1.md`.

---

## Test Coverage Gaps

**`scripts/validate-card.py` — no test suite**
- What's not tested: The validator itself has no test cases. A regression in the validator could silently pass malformed cards.
- Files: `scripts/validate-card.py`, `scripts/check-card-schema.py`, `scripts/lint-scl-rules.py`
- Risk: If the PostToolUse hook auto-validates every card write and the validator has a bug, every generated card could pass incorrectly.
- Priority: High. The validator is the primary quality gate.

**Exercise library membership check — completely absent from CI**
- What's not tested: No automated check verifies that exercises named in card bodies exist in `exercise-library.md` or `middle-math/exercise-registry.json`.
- Files: All 262 generated cards; `exercise-library.md`; `middle-math/exercise-registry.json`
- Risk: Hallucinated exercises propagate downstream without detection.
- Priority: High. Explicitly called out in CLAUDE.md as highest priority constraint.

**Color differentiation — no automated duplicate-primary-exercise check across decks**
- What's not tested: `scripts/audit-exercise-coverage.py` checks for duplicates within a single deck. No tool checks that the same primary exercise isn't used in the same Type across two Color variants in the same deck. No cross-deck duplicate check exists.
- Files: `scripts/audit-exercise-coverage.py`; all generated card files
- Risk: The rule "8 Colors = 8 different workouts" can be violated silently. Two Color variants using the same primary exercise is called out as the most common generation error in CLAUDE.md.
- Priority: Medium. The audit script exists but has narrower scope than needed.

**Middle-math weight vectors — no regression tests**
- What's not tested: `scripts/middle-math/weight_vector.py --validate` checks structure (1,680 vectors generated, dimensions match) but not expected values. There are no golden-output tests.
- Files: `scripts/middle-math/weight_vector.py`; `middle-math/weight-vectors.json`
- Risk: Changes to any of the 7 weight declaration files silently shift all 1,680 weight vectors without detection.
- Priority: Low for current Phase 2 work. High before Phase 4 when weight vectors drive rendering.

---

## SCL Zip Index

Each concern mapped to its closest SCL address for location in the navigation graph.

| Concern | Zip | Location |
|---------|-----|----------|
| 1,400 stub cards | 🦋 🤌 🟢 | Ionic (build) + facio + Growth — active generation domain |
| Deck identity gaps (35/42 stubs) | 🐂 🏛 ⚫ | Tuscan (define) + Firmitas + Teaching — setup phase |
| Exercise library versioning | 🐂 🏛 ⚪ | Tuscan (define) + Firmitas + Mindful — authority/review |
| `core-stability` contamination | ⛽ 🏛 🟠 | Doric (validate) + Firmitas + Circuit — sweep/audit |
| Stale seed status references | 🖼 🏛 ⚪ | Palladian (restore) + Firmitas + Mindful — pruning |
| Archideck on unmerged branch | 🌾 🏛 🔵 | Composite (integrate) + Firmitas + Structured — merge task |
| No exercise library cross-ref in CI | ⛽ 🏛 🟠 | Doric (validate) + Firmitas + Circuit — audit gap |
| Historical events DB (0/366) | 🏟 ⌛ 🟣 | Corinthian (execute) + Temporitas + Technical — research intensive |
| Ralph Loop batch orchestrator | 🌾 🔨 🔵 | Composite (integrate) + Utilitas + Structured — build |
| No CANONICAL cards | ⚪ | Mindful color — review posture only |
| Vocabulary standard audit | ⚪ | Mindful color — review posture only |
| Validate-card.py has no tests | ⛽ 🏛 🟠 | Doric (validate) + Firmitas + Circuit — gap |
| Middle-math weights are DRAFT | ⚖ 🏛 🟣 | Vitruvian (calibrate) + Firmitas + Technical — precision work |
| Cosmogram content unverified | 🐂 🌹 🟣 | Tuscan (define) + Venustas + Technical — research needed |
| ExRx partnership dependency | 🌾 🐬 🟡 | Composite (combine) + Sociatas (partner) + Fun (exploratory) |

*Concerns audit: 2026-03-07*
