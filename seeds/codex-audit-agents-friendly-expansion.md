# Codex Audit — Agents-Friendly Ppl± Expansion (Non-Operis Core)

Date: 2026-03-03  
Scope: High-leverage work that strengthens Daily Operis readiness without requiring web search.

---

## Why this audit exists

Daily Operis depends on upstream quality: valid cards, reliable metadata, deterministic generation contracts, and machine-checkable constraints.

If those layers are weak, Operis output becomes inconsistent even with strong prompts.

This audit defines what Codex can run now to harden the system while web-dependent Operis research remains out of scope.

---

## Operating posture (aligned with Operis rationale)

- Build deterministic inputs before expressive outputs.
- Prefer schema + validator + fixtures over ad hoc prose.
- Convert tacit rules into executable checks.
- Expand coverage in a way that preserves SCL law hierarchy (Order > Color > Axis > practical equipment).
- Keep all work additive to card-generation velocity.

---

## Workstream A — Deck expansion pipeline (highest leverage)

### A1) Build Deck 09 identity package (⛽🌹)
**Goal:** unblock 40-card generation with non-guessing seeds.

Deliverables:
- `deck-identities/deck-09-identity.md`
- Coverage map ensuring 8 color variants per Type do not reuse the same primary exercise.
- Naming pass aligned with `deck-identities/naming-convention.md`.

Codex can run:
- Gap scan versus Deck 08 patterns.
- Exercise availability verification against `exercise-library.md`.
- Preflight uniqueness check for primary exercise distribution.

### A2) Generate Deck 09 cards in controlled batches
**Goal:** progress core card inventory while maintaining strict validation.

Deliverables:
- 40 generated cards from stubs to full filenames.
- Frontmatter status update `EMPTY -> GENERATED`.

Codex can run:
- 5-card batch generation loops.
- Per-batch validation + correction before next batch.
- Commit discipline per batch for clean rollback.

### A3) Retrofit Deck 07 flagged regen queue
**Goal:** clear known quality debt before canonicalization.

Deliverables:
- Regenerated cards for REGEN-NEEDED set.
- Validation report proving hard constraints are clear.

Codex can run:
- Rule-by-rule diff against existing versions.
- Deterministic regeneration from identity mapping.
- Post-regen audit for format-15 completeness.

---

## Workstream B — Constraint automation and linting

### B1) Card schema and parser hardening
**Goal:** make card files machine-parseable for all downstream systems.

Deliverables:
- JSON schema for card structure (frontmatter + blocks + junction + save).
- Parser utility for tree notation and sub-block zip extraction.

Codex can run:
- Define canonical schema fields from current card template.
- Add fixture tests on representative cards.
- Fail fast on malformed block headers or missing required elements.

### B2) SCL rules linter (P0/P1 tiers)
**Goal:** convert AGENTS constraints into automated checks.

Deliverables:
- Linter script for hard constraints (P0) and format/tone issues (P1).
- Machine-readable output (json + human table).

Codex can run:
- Checks for load ceilings, color/equipment bans, GOLD gating, block counts, required terminal blocks.
- Circuit adjacency logic for 🟠.
- Performance block-count ceiling enforcement for 🏟.

### B3) Pre-commit/CI wiring (non-blocking first)
**Goal:** reduce regressions during high-volume generation.

Deliverables:
- Local command bundle for quick validation.
- Optional CI workflow in warn-only mode.

Codex can run:
- Create command aliases/scripts for per-card, per-folder, per-deck checks.
- Add summary reports to PR body templates.

---

## Workstream C — Middle-math readiness for deterministic selection

### C1) Complete weight declarations (remaining emoji categories)
**Goal:** normalize scoring primitives across Orders, Axes, Types, Colors, Blocks, Operators.

Deliverables:
- Filled declarations in `middle-math/` specs.
- Consistent scale and normalization notes.

Codex can run:
- Consolidation pass to unify naming and units.
- Validation script to detect missing weight nodes.

### C2) Exercise family tree expansion
**Goal:** improve substitution and transfer logic for generator + junction.

Deliverables:
- Expanded family maps for major movement patterns.
- Family metadata for equipment tier and difficulty.

Codex can run:
- Structured extraction from `exercise-library.md`.
- Build adjacency tables usable by future selector engine.

### C3) Prototype executable selector
**Goal:** replace manual selection drift with deterministic candidate ranking.

Deliverables:
- `scripts/middle-math/` prototype that returns ranked candidates by zip.
- Trace output showing why each exercise was selected or rejected.

Codex can run:
- Implement constraints-first filtering then axis-weight ranking.
- Emit explainability logs for review.

---

## Workstream D — Junction intelligence and bridge quality

### D1) Junction recommendation validator
**Goal:** make "Next → [zip]" bridges coherent and auditable.

Deliverables:
- Rule set for legal next-zip transitions.
- Validator for rationale quality and progression continuity.

Codex can run:
- Check that follow-up zips are structurally plausible.
- Enforce rationale format and prevent repetitive bridges.

### D2) Rotation fatigue model prototype
**Goal:** align session bridges with recovery logic.

Deliverables:
- Basic fatigue carryover heuristic from prior session metadata.
- Suggested next-zips constrained by fatigue state.

Codex can run:
- Implement draft model from `middle-math/rotation/` seeds.
- Generate test vectors for common week patterns.

---

## Workstream E — Data and repository operations

### E1) Card inventory truth table
**Goal:** single source of truth for generation status and quality state.

Deliverables:
- Generated index (csv/json) with deck, zip, status, filename, validation state.
- Fast filters for EMPTY / GENERATED / CANONICAL / REGEN-NEEDED.

Codex can run:
- Index script over `cards/` tree.
- Delta report by commit.

### E2) Coverage audits
**Goal:** detect exercise concentration risk and variety gaps.

Deliverables:
- Primary exercise frequency report by deck/type/color.
- Redundancy alerts for same primary across color variants.

Codex can run:
- Statistical audit using existing `audit-exercise-coverage.py` direction.
- Threshold-driven alerting.

### E3) Canonicalization prep pack
**Goal:** reduce friction for Jake's review and approval.

Deliverables:
- Deck-level review packet: violations summary, fixed issues, unresolved flags.
- Candidate list for first CANONICAL deck promotion.

Codex can run:
- Aggregate linter outputs + manual notes into one review artifact.

---

## Workstream F — Agent systemization (Codex-first)

### F1) Formalize agent handoff contracts
**Goal:** prevent context loss between generator, validator, reviewer, explorer.

Deliverables:
- Contract docs specifying inputs, outputs, required checks, fail conditions.
- Shared JSON handoff examples.

Codex can run:
- Draft contracts in `.codex/agents/` companion docs.
- Add sample invocation recipes.

### F2) Prompt fixture suite
**Goal:** regression-test agent behavior against known hard cases.

Deliverables:
- Fixture set for edge zips (🟠 loop logic, 🏟 block ceiling, 🖼 somatic lens).
- Expected pass/fail outcomes.

Codex can run:
- Build fixture markdown files and expected validator outputs.
- Run periodic checks after prompt/config updates.

### F3) Session protocol templates
**Goal:** make high-throughput runs consistent.

Deliverables:
- Templates for "build identity", "generate batch", "audit deck", "regen queue".
- Checklists integrated with current whiteboard workflow.

Codex can run:
- Author templates in `seeds/` or `scripts/` docs.
- Add command snippets for one-command execution.

---

## Recommended execution order (non-web, Operis-compatible)

1. **Deck 09 identity (A1)**
2. **Deck 09 generation in batches (A2)**
3. **P0/P1 linter hardening (B2)**
4. **Inventory + coverage truth tables (E1, E2)**
5. **Deck 07 regen queue cleanup (A3)**
6. **Junction validator + fatigue prototype (D1, D2)**
7. **Agent handoff contracts + fixtures (F1, F2)**
8. **Middle-math selector prototype (C3)**

This sequence increases immediate card throughput while improving the substrate that Daily Operis will read from.

---

## Definition of done for this audit track

- Deck 09 identity exists and passes uniqueness checks.
- At least one deck generation loop runs with automated P0/P1 lint pass.
- Repository has machine-readable inventory + coverage outputs.
- Agent handoff contracts exist for the four Codex agents.
- Junction recommendations are validator-backed, not purely editorial.

When those are true, Daily Operis can later plug into stronger, cleaner, more deterministic source layers.
