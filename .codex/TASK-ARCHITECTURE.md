# Codex Task Architecture (CX-00A → CX-43)

This document is the Codex execution map for the current architecture campaign.
It defines the tech tree, wave plan, and context firewall for agent-safe execution.
Use glossary terms from `scl-deep/systems-glossary.md` as the authoritative source language.

## Container Index

| Container | Name | Dependency | Wave | Status | Completed In | Evidence |
|---|---|---|---|---|---|---|
| CX-00A / CX-00B | Systems Glossary + Systems Language Audit | None / CX-00A | 1 | DONE | PR #63 area · c3f6ec7 | `scl-deep/systems-glossary.md`, `scl-deep/systems-language-audit.md` |
| CX-01 | Codex Agent Configuration & Task Architecture | CX-00A | 1 | DONE | Session 037 · architecture-capstone-037 | `.codex/TASK-ARCHITECTURE.md` — governance finalized, completion summary added |
| CX-02 | Historical Events Scaffold | CX-00A | 1 | DONE | Session 028 · `047113c` | `operis-editions/historical-events/README.md` |
| CX-03 | Zip Converter Utilities | CX-00A | 1 | DONE | PR #58 · 83868b9 | `scripts/middle-math/zip_converter.py`, `scripts/middle-math/zip_registry.py`, `middle-math/zip-registry.json` |
| CX-04 | Inventory & Progress Truth Tables | CX-00A | 1 | DONE | Session 018 · `3b75660` | `scripts/progress-report.py`, `scripts/index-card-inventory.py` |
| CX-05 | Markdownlint Configuration | CX-00A | 1 | DONE | Codex run · evidence on disk | `.github/linters/.markdownlint-cli2.jsonc` |
| CX-06 | Frontmatter Schema & Validator | CX-00A | 1 | DONE | Session 030 · `0fbf244` | `scripts/check-card-schema.py`, `scripts/fixtures/schema/generated-compliant-tree.md` |
| CX-07 | CI Lint Workflow | CX-05, CX-06 | 2 | DONE | Codex run · evidence on disk | `.github/workflows/lint.yml`, `.github/workflows/pylint.yml` |
| CX-08 | SQL Schema Materialization | CX-00A | 1 | DONE | Session 025 · `b36cfff` | `middle-math/schemas/zip-metadata-schema.md` |
| CX-09 | Axis Weight Declarations | CX-00A | 2 | DONE | PR #64 · 41cc4fa | `middle-math/weights/axis-weights.md` — all 6 axes populated |
| CX-10 | Type & Color Weight Declarations | CX-00A | 2 | DONE | PR #65 · e6be726 | `middle-math/weights/type-weights.md`, `middle-math/weights/color-weights.md` |
| CX-11 | Block Weight Declarations | CX-09, CX-10 | 3 | DONE | Engine coupling session · 2026-03-05 | `middle-math/weights/block-weights.md` — 790-line working draft |
| CX-12 | Operator Weight Declarations | CX-09, CX-10 | 3 | DONE | Engine coupling session · 2026-03-05 | `middle-math/weights/operator-weights.md` — 502-line working draft |
| CX-13 | Exercise Library Parser | CX-00A | 2 | DONE | PR #61 · db7b202 | `scripts/middle-math/parse_exercise_library.py`, `middle-math/exercise-library.json` |
| CX-14 | Weight Vector Computation Engine | CX-09, CX-10, CX-11, CX-12, CX-03 | 3 | DONE | Session 034 · 2026-03-06 | `scripts/middle-math/weight_vector.py`, `middle-math/weight-vectors.json` (1,680 entries, 61 dimensions, --validate passes) |
| CX-15 | Exercise Selection Prototype | CX-13, CX-14 | 4 | DONE | Sprint 035 · claude/wave-4-sprint-035-vN8CK | `scripts/middle-math/exercise_selector.py` — GOLD gate, load ceiling, equipment tier, Type match, --validate passes 1,680 zips |
| CX-16 | Deck Identity Scaffold Generator | CX-03, CX-04 | 2 | DONE | PR #67 · 862de8d | `scripts/deck-identity-scaffold.py`, deck identity docs for Decks 10–12 |
| CX-17 | Ralph Loop Validation & Batch | CX-03 | 2 | PENDING | — | — |
| CX-18 | Design Tokens & WeightCSS Spec | CX-00A | 2 | DONE | Session 037 · architecture-capstone-037 | `middle-math/design-tokens.json`, `middle-math/weight-css-spec.md` |
| CX-19 | Agent Boundaries Document | CX-00A, CX-01 | 2 | DONE | Session 037 · architecture-capstone-037 | `.claude/AGENT-BOUNDARIES.md` — 5-agent matrix, escalation rules, Jake-reserved zones |
| CX-20 | Room Schema Extension | CX-08 | 2 | DONE | Engine coupling session · 2026-03-05 | `sql/008-room-schema-extension.sql` — 4 tables, RLS, 1,680-row population |
| CX-21 | Content Type Registry | CX-00A | 2 | DONE | Session 034 · 2026-03-06 | `middle-math/content-type-registry.json` (109 types, 6 axes, cross-floor + operator mappings) |
| CX-22 | Floor Routing Spec | CX-03, CX-20, CX-21 | 3 | DONE | Sprint 035 · claude/wave-4-sprint-035-vN8CK | `middle-math/floor-routing-spec.md` — 109 content types routed to 6 Axis floors, default landing, access gates |
| CX-23 | Navigation Graph Builder | CX-03, CX-04, CX-08 | 2 | DONE | Engine coupling session · 2026-03-05 | `scripts/build-navigation-graph.py`, `middle-math/navigation-graph.json` — 1,680 nodes × 4 edges |
| CX-24 | Bloom State Engine | CX-20, CX-03 | 3 | DONE | Sprint 035 · claude/wave-4-sprint-035-vN8CK | `scripts/middle-math/bloom_engine.py` — 6-level bloom, no streaks/decay, eudaimonic constraint, --demo and --schema flags |
| CX-25 | Vote Weight Integration | CX-20, CX-14 | 4 | DONE | Session 036 · a7c0022 | `scripts/middle-math/vote_weight_adjuster.py` — tanh signal, ±0.8 cap, --validate passes 6,720 checks |
| CX-26 | Operis Room Manifest Generator | CX-03, CX-04 | 2 | DONE | Sprint 035 · claude/wave-4-sprint-035-vN8CK | `scripts/middle-math/generate_room_manifest.py` — 13-room Sandbox from date input, --date and --week flags |
| CX-27 | Superscript/Subscript Data Model | CX-20, CX-08 | 3 | DONE | Sprint 035 · claude/wave-4-sprint-035-vN8CK | `scripts/middle-math/compute_superscript.py` — system suggestions + user overrides, --demo and --schema flags |
| CX-28 | Cosmogram Content Scaffold | CX-04 | 2 | DONE | Session 034 · 2026-03-06 | `scripts/scaffold_cosmograms.py`, `deck-cosmograms/deck-01-cosmogram.md` through `deck-42-cosmogram.md` (42 stubs) |
| CX-29 | Wilson Audio Route Scaffold | CX-22 | 4 | DONE | Session 036 · a7c0022 | `middle-math/wilson-audio-spec.md` — 3-layer keyword scoring, ~2,260 entries, Wilson voice registers by floor |
| CX-30 | Envelope Schema & Stamping Prototype | CX-08, CX-14, CX-03 | 4 | DONE | Session 036 · a7c0022 | `scripts/middle-math/envelope_stamper.py` — atomic retrieval unit, --anonymous + --full + --deck modes |
| CX-31 | Envelope Similarity Function & Retrieval Prototype | CX-30, CX-21 | 5 | DONE | Session 037 · architecture-capstone-037 | `scripts/middle-math/envelope_retrieval.py` — cosine similarity, Tier 1–4 profiles, --query/--deck/--operis/--validate/--stats, 5/5 validation checks pass |
| CX-32 | Mermaid CX Dependency Graph | None | 2 | DONE | Codex run · evidence on disk | `docs/cx-dependency-graph.md` |
| CX-33 | GitHub Pages Progress Dashboard | CX-03, CX-04 | 2 | DONE | PR #90 engine coupling session 2026-03-05 | `docs/dashboard/index.html`, `scripts/build-dashboard-data.py`, `docs/dashboard/data/progress.json` |
| CX-34 | Codespaces Dev Container | None | 1 | DONE | Codex run · evidence on disk | `.devcontainer/devcontainer.json`, `docs/codespaces-quickstart.md` |
| CX-35 | Whiteboard Negotiosum Validator | CX-03, CX-04 | 2 | DONE | Codex run · evidence on disk | `scripts/validate-negotiosum.py` |
| CX-36 | Exercise Identity Registry | CX-13 | 6 | DONE | Session 038 | `scripts/build-exercise-registry.py`, `middle-math/exercise-registry.json` (2,085 entries, EX-0001–EX-2085) |
| CX-37 | Exercise Knowledge Template + First Batch | CX-36 | 6 | DONE | Session 038 | `scripts/generate-exercise-content.py`, `exercise-content/` (197 files across push/pull/legs/plus/ultra) |
| CX-38 | Exercise Relationship Graph | CX-36 | 6 | DONE | Session 038 | `middle-math/exercise-engine/family-trees.json`, `substitution-map.json`, `sport-tags.json`, `anatomy-index.json` |
| CX-39 | External Reference Dock | CX-36 | 6 | DONE | Session 038 | `middle-math/exercise-engine/external-refs.json` (2,085 null docks), `seeds/exrx-partnership-brief.md` |
| CX-40 | Exercise Registry SQL Migration | CX-36, CX-08 | 6 | DONE | Session 038 | `sql/009-exercise-registry.sql`, `sql/010-exercise-knowledge.sql`, `sql/README.md` updated |
| CX-41 | Exercise Content Batch 2 (201–500) | CX-37 | 7 | PENDING | | |
| CX-42 | Exercise Content Batch 3 (501–1000) | CX-37 | 7 | PENDING | | |
| CX-43 | Exercise Selector V2 (registry-aware) | CX-36, CX-38, CX-15 | 7 | PENDING | | |

**Status legend:**
- `PENDING` — not started or no merged evidence recorded yet.
- `IN_PROGRESS` — active container work in current session/branch.
- `DONE` — merged and evidenced in repository artifacts.
- `BLOCKED` — cannot proceed due to unmet dependency, missing input, or policy gate.

## Update Rule

When a container row is marked `DONE`, the row must include all of the following:
1. Session identifier from `whiteboard.md` in **Completed In** (example: `Session 028`).
2. Commit hash in **Completed In** (short hash is acceptable).
3. At least one concrete artifact path in **Evidence** proving the merged completion.

## Wave Execution Plan

- **Wave 1 — Foundation bus:** CX-00A, CX-00B, CX-01, CX-02, CX-03, CX-04, CX-05, CX-06, CX-08, CX-34
- **Wave 2 — Infrastructure expansion:** CX-07, CX-09, CX-10, CX-13, CX-16, CX-17, CX-18, CX-19, CX-20, CX-21, CX-23, CX-26, CX-28, CX-32, CX-33, CX-35
- **Wave 3 — Engine coupling:** CX-11, CX-12, CX-14, CX-22, CX-24, CX-27
- **Wave 4 — Application behaviors:** CX-15, CX-25, CX-29, CX-30
- **Wave 5 — Retrieval capstone:** CX-31
- **Wave 6 — Exercise Library Foundation:** CX-36, CX-37, CX-38, CX-39, CX-40
- **Wave 7 — Exercise Library Scale:** CX-41, CX-42, CX-43

## Context Firewall Rules

### Codex MAY Read
- `CLAUDE.md`, `scl-directory.md`, `whiteboard.md`, `README.md`
- `scl-deep/`, `seeds/`, `middle-math/`, `deck-identities/`, `zip-web/`, `scripts/`
- `deck-cosmograms/README.md`
- `cards/` (status scans only)
- `exercise-library.md` (parse only)
- `exercise-content/` (read for batch continuation and validation)

### Codex MAY Write
- `middle-math/`, `scripts/`, `sql/`, `.codex/`, `.claude/`, `.github/`
- `html/design-system/`
- `deck-cosmograms/` (stubs only)
- `operis-editions/historical-events/` (scaffolds only)
- `scl-deep/systems-glossary.md`, `scl-deep/systems-language-audit.md`
- `exercise-content/` (knowledge files only)

### Codex NEVER Touches
- Card content in `cards/`
- Operis editions (except historical-events scaffolds)
- `scl-directory.md`
- `exercise-library.md`
- Any file requiring live web research to populate
- SCL rule or emoji creation/modification artifacts

## Dependency Readiness (current state — Session 038, 2026-03-06)

33/36 architecture containers DONE after Session 037. CX-36–40 completed in Session 038. Total: 44 defined, 38 complete, 6 open.

| Container | Status | Blocker | Notes |
|-----------|--------|---------|-------|
| CX-17 | OPEN | Jake pod review | Ralph loop tooling — Codex task, needs pod review sign-off |
| CX-36 | DONE | — | Session 038 — `middle-math/exercise-registry.json` (2,085 entries) |
| CX-37 | DONE | — | Session 038 — 197 knowledge files in `exercise-content/` |
| CX-38 | DONE | — | Session 038 — 4 relationship graph files in `middle-math/exercise-engine/` |
| CX-39 | DONE | — | Session 038 — `external-refs.json` (2,085 null docks) + ExRx brief |
| CX-40 | DONE | — | Session 038 — `sql/009-exercise-registry.sql`, `sql/010-exercise-knowledge.sql` |
| CX-41 | PENDING | CX-37 ✓ | Exercise Content Batch 2 (201–500) — CX-37 now unblocked |
| CX-42 | PENDING | CX-37 ✓ | Exercise Content Batch 3 (501–1000) — CX-37 now unblocked |
| CX-43 | PENDING | CX-36 ✓, CX-38 ✓, CX-15 ✓ | Exercise Selector V2 — all blockers cleared |
| (non-CX) Deck 07 pod review | OPEN | Jake | Jake reviews Deck 07 Ralph pod before Ralph loop can run |
| (non-CX) Operis Contract A/B URL enforcement | OPEN | manual | Manual enforcement of Contract A/B pipeline |

CX-17 remains blocked on Jake's pod review. Architecture + Exercise Library Foundation campaigns: 38/44 complete.
Wave 7 (CX-41, CX-42, CX-43) fully unblocked after Session 038.

---

## Execution Notes

- Treat the architecture as a layered resolver: dependencies first, leaf tasks last.
- Keep handoffs explicit between generator, validator, explorer, and reviewer agents.
- Do not bypass interlocks: if a dependency is unmet, the container remains pending.

---

## Container Completion Summary

All 44 containers sorted by wave and completion. 33/44 complete as of Session 037 (architecture); 8 new CX-36–43 registered Session 038.

| Container | Name | Wave | Status | Session Completed |
|-----------|------|------|--------|-------------------|
| CX-00A | Systems Glossary | 1 | DONE | Session 028 (PR #63) |
| CX-00B | Systems Language Audit | 1 | DONE | Session 028 (PR #63) |
| CX-01 | Codex Agent Configuration & Task Architecture | 1 | DONE | Session 037 |
| CX-02 | Historical Events Scaffold | 1 | DONE | Session 028 |
| CX-03 | Zip Converter Utilities | 1 | DONE | PR #58 |
| CX-04 | Inventory & Progress Truth Tables | 1 | DONE | Session 018 |
| CX-05 | Markdownlint Configuration | 1 | DONE | Codex run |
| CX-06 | Frontmatter Schema & Validator | 1 | DONE | Session 030 |
| CX-08 | SQL Schema Materialization | 1 | DONE | Session 025 |
| CX-34 | Codespaces Dev Container | 1 | DONE | Codex run |
| CX-07 | CI Lint Workflow | 2 | DONE | Codex run |
| CX-09 | Axis Weight Declarations | 2 | DONE | PR #64 |
| CX-10 | Type & Color Weight Declarations | 2 | DONE | PR #65 |
| CX-13 | Exercise Library Parser | 2 | DONE | PR #61 |
| CX-16 | Deck Identity Scaffold Generator | 2 | DONE | PR #67 |
| CX-17 | Ralph Loop Validation & Batch | 2 | PENDING | — |
| CX-18 | Design Tokens & WeightCSS Spec | 2 | DONE | Session 037 |
| CX-19 | Agent Boundaries Document | 2 | DONE | Session 037 |
| CX-20 | Room Schema Extension | 2 | DONE | Session 034 (engine coupling) |
| CX-21 | Content Type Registry | 2 | DONE | Session 034 |
| CX-23 | Navigation Graph Builder | 2 | DONE | Session 034 (engine coupling) |
| CX-26 | Operis Room Manifest Generator | 2 | DONE | Sprint 035 |
| CX-28 | Cosmogram Content Scaffold | 2 | DONE | Session 034 |
| CX-32 | Mermaid CX Dependency Graph | 2 | DONE | Codex run |
| CX-33 | GitHub Pages Progress Dashboard | 2 | DONE | PR #90 / Session 034 |
| CX-35 | Whiteboard Negotiosum Validator | 2 | DONE | Codex run |
| CX-11 | Block Weight Declarations | 3 | DONE | Session 034 (engine coupling) |
| CX-12 | Operator Weight Declarations | 3 | DONE | Session 034 (engine coupling) |
| CX-14 | Weight Vector Computation Engine | 3 | DONE | Session 034 |
| CX-22 | Floor Routing Spec | 3 | DONE | Sprint 035 |
| CX-24 | Bloom State Engine | 3 | DONE | Sprint 035 |
| CX-27 | Superscript/Subscript Data Model | 3 | DONE | Sprint 035 |
| CX-15 | Exercise Selection Prototype | 4 | DONE | Sprint 035 |
| CX-25 | Vote Weight Integration | 4 | DONE | Session 036 |
| CX-29 | Wilson Audio Route Scaffold | 4 | DONE | Session 036 |
| CX-30 | Envelope Schema & Stamping Prototype | 4 | DONE | Session 036 |
| CX-31 | Envelope Similarity & Retrieval | 5 | DONE | Session 037 |

| CX-36 | Exercise Identity Registry | 6 | DONE | Session 038 |
| CX-37 | Exercise Knowledge Template + First Batch | 6 | DONE | Session 038 |
| CX-38 | Exercise Relationship Graph | 6 | DONE | Session 038 |
| CX-39 | External Reference Dock | 6 | DONE | Session 038 |
| CX-40 | Exercise Registry SQL Migration | 6 | DONE | Session 038 |
| CX-41 | Exercise Content Batch 2 (201–500) | 7 | PENDING | — |
| CX-42 | Exercise Content Batch 3 (501–1000) | 7 | PENDING | — |
| CX-43 | Exercise Selector V2 (registry-aware) | 7 | PENDING | — |

Wave completion: Wave 1 (9/10) · Wave 2 (14/16) · Wave 3 (6/6) · Wave 4 (4/4) · Wave 5 (1/1) · Wave 6 (5/5) · Wave 7 (0/3)
CX-17 remains blocked on Jake pod review. Wave 6 complete (Session 038). Wave 7 fully unblocked.
