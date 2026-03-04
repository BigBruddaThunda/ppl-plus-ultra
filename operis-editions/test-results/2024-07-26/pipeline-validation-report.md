# Operis V4 Pipeline Validation Report

## Test Metadata
- Test date executed: 2026-03-04
- Candidate publication date under test: 2024-07-26 (Friday)
- Region: Northeastern United States
- Deterministic constraints:
  1. No live web browsing during test execution
  2. Deterministic date math for rotation checks
  3. Prompt sequence limited to P1→P2→P3 contracts
- Prompt files used:
  - `seeds/operis-researcher-prompt.md` (P1)
  - `seeds/operis-content-architect-prompt.md` (P2)
  - `seeds/operis-editor-prompt.md` (P3)

## Generated Artifacts
- Contract A output: `operis-editions/test-results/2024-07-26/contract-a-research-brief.md`
- Contract B output: `operis-editions/test-results/2024-07-26/contract-b-content-brief.md`
- Contract C output: `operis-editions/test-results/2024-07-26/contract-c-operis-edition.md`

## Validation Results

### 1) Handoff Integrity Between Stages

**Result: PARTIAL PASS**

#### Contract A (P1 → P2)
- ✅ Required high-level section structure present (Edition Metadata + 5 beats).
- ❌ Failure point A1: Beat 1 event entries do not include explicit source URLs required by Contract A.
  - Exact location: `contract-a-research-brief.md`, section `Beat 1 — Historical Events`.
- ❌ Failure point A2: Beat 2 sky section does not include exact sunrise/sunset and moonrise/moonset times; uses qualitative placeholders.
  - Exact location: `contract-a-research-brief.md`, section `Beat 2 — The Sky`.

#### Contract B (P2 → P3)
- ✅ Color, posture, editorial reasoning, context, lane hierarchy, and map sections present.
- ❌ Failure point B1: Content Lanes are missing explicit per-lane source URLs required by Contract B.
  - Exact location: `contract-b-content-brief.md`, section `Content Lanes`.

#### Contract C (P3 output)
- ✅ Full edition body includes expected Friday-active departments and 13-room payload.
- ❌ Failure point C1: Frontmatter key uses `rooms:` instead of Contract C schema key `sandbox-zips:` from `seeds/operis-prompt-pipeline.md`.
  - Exact location: `contract-c-operis-edition.md`, YAML frontmatter root keys.
- ❌ Failure point C2: Missing required `sandbox-total: 13` frontmatter key from Contract C.
  - Exact location: `contract-c-operis-edition.md`, YAML frontmatter root keys.

### 2) Color Posture Coherence

**Result: PASS**
- Selected Color: 🔵 Structured.
- Posture sentence, educational feature, and room descriptions all maintain a procedural, measurable, non-hype tone aligned with Structured semantics.
- No motivational language detected; no overt tone drift into 🔴/⚪ posture.

### 3) 13-Room Sandbox Mapping Fidelity

**Result: PASS (structure), PARTIAL FAIL (schema naming)**
- ✅ Total rooms = 13 (8 siblings + 5 content rooms).
- ✅ All 13 share day Order 🌾 (Friday).
- ✅ Sibling set covers all 8 Colors for same Order×Axis×Type.
- ✅ Content rooms satisfy 5 unique Types (🛒🪡🍗➕➖ exactly once).
- ✅ Content rooms satisfy 5 unique Axes (🏛🔨🌹⌛🐬 exactly once).
- ✅ No zip duplication between siblings and content rooms.
- ❌ Contract schema mismatch remains (frontmatter naming/key requirements from Contract C not met as listed above).

### 4) Department Activation Matrix Behavior (Day-of-Week)

**Result: PASS**
- Test day = Friday → Order 🌾.
- Required Friday-active departments are present in Contract C output: Masthead, Intention, Composition, Historical Desk, Educational Feature, Seasonal Desk, Rooms of the Day, Wilson Note, Junction Bridge.
- Friday-inactive departments are correctly absent as standalone sections (Fundamentals, Primer, Reformance, Tool Floor, Sandbox Notice, Reader's Almanac, Letters).

## Follow-Up Actions
1. Patch P1 template/runbook to enforce per-event URL and exact sky-data fields before handoff.
2. Patch P2 template/runbook to enforce explicit source URL per content lane.
3. Align P3 frontmatter schema with Contract C (`sandbox-zips`, `sandbox-total`) and add a preflight key-check gate.
4. Re-run deterministic test on same date after schema corrections to verify full PASS.

## Final Status
**Overall: FAIL (contract compliance not yet full-pass).**
- Structural and mapping logic are sound.
- Contract strictness failures block production-grade automation handoff.
