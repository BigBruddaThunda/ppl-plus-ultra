# Codex Task Architecture (CX-00A → CX-31)

This document is the Codex execution map for the current architecture campaign.
It defines the tech tree, wave plan, and context firewall for agent-safe execution.
Use glossary terms from `scl-deep/systems-glossary.md` as the authoritative source language.

## Container Index

| Container | Name | Dependency | Wave |
|---|---|---|---|
| CX-00A / CX-00B | Systems Glossary + Systems Language Audit | None / CX-00A | 1 |
| CX-01 | Codex Agent Configuration & Task Architecture | CX-00A | 1 |
| CX-02 | Historical Events Scaffold | CX-00A | 1 |
| CX-03 | Zip Converter Utilities | CX-00A | 1 |
| CX-04 | Inventory & Progress Truth Tables | CX-00A | 1 |
| CX-05 | Markdownlint Configuration | CX-00A | 1 |
| CX-06 | Frontmatter Schema & Validator | CX-00A | 1 |
| CX-07 | CI Lint Workflow | CX-05, CX-06 | 2 |
| CX-08 | SQL Schema Materialization | CX-00A | 1 |
| CX-09 | Axis Weight Declarations | CX-00A | 2 |
| CX-10 | Type & Color Weight Declarations | CX-00A | 2 |
| CX-11 | Block Weight Declarations | CX-09, CX-10 | 3 |
| CX-12 | Operator Weight Declarations | CX-09, CX-10 | 3 |
| CX-13 | Exercise Library Parser | CX-00A | 2 |
| CX-14 | Weight Vector Computation Engine | CX-09, CX-10, CX-11, CX-12, CX-03 | 3 |
| CX-15 | Exercise Selection Prototype | CX-13, CX-14 | 4 |
| CX-16 | Deck Identity Scaffold Generator | CX-03, CX-04 | 2 |
| CX-17 | Ralph Loop Validation & Batch | CX-03 | 2 |
| CX-18 | Design Tokens & WeightCSS Spec | CX-00A | 2 |
| CX-19 | Agent Boundaries Document | CX-00A, CX-01 | 2 |
| CX-20 | Room Schema Extension | CX-08 | 2 |
| CX-21 | Content Type Registry | CX-00A | 2 |
| CX-22 | Floor Routing Spec | CX-03, CX-20, CX-21 | 3 |
| CX-23 | Navigation Graph Builder | CX-03, CX-04, CX-08 | 2 |
| CX-24 | Bloom State Engine | CX-20, CX-03 | 3 |
| CX-25 | Vote Weight Integration | CX-20, CX-14 | 4 |
| CX-26 | Operis Room Manifest Generator | CX-03, CX-04 | 2 |
| CX-27 | Superscript/Subscript Data Model | CX-20, CX-08 | 3 |
| CX-28 | Cosmogram Content Scaffold | CX-04 | 2 |
| CX-29 | Wilson Audio Route Scaffold | CX-22 | 4 |
| CX-30 | Envelope Schema & Stamping Prototype | CX-08, CX-14, CX-03 | 4 |
| CX-31 | Envelope Similarity Function & Retrieval Prototype | CX-30, CX-21 | 5 |

## Wave Execution Plan

- **Wave 1 — Foundation bus:** CX-00A, CX-00B, CX-01, CX-02, CX-03, CX-04, CX-05, CX-06, CX-08
- **Wave 2 — Infrastructure expansion:** CX-07, CX-09, CX-10, CX-13, CX-16, CX-17, CX-18, CX-19, CX-20, CX-21, CX-23, CX-26, CX-28
- **Wave 3 — Engine coupling:** CX-11, CX-12, CX-14, CX-22, CX-24, CX-27
- **Wave 4 — Application behaviors:** CX-15, CX-25, CX-29, CX-30
- **Wave 5 — Retrieval capstone:** CX-31

## Context Firewall Rules

### Codex MAY Read
- `CLAUDE.md`, `scl-directory.md`, `whiteboard.md`, `README.md`
- `scl-deep/`, `seeds/`, `middle-math/`, `deck-identities/`, `zip-web/`, `scripts/`
- `deck-cosmograms/README.md`
- `cards/` (status scans only)
- `exercise-library.md` (parse only)

### Codex MAY Write
- `middle-math/`, `scripts/`, `sql/`, `.codex/`, `.claude/`, `.github/`
- `html/design-system/`
- `deck-cosmograms/` (stubs only)
- `operis-editions/historical-events/` (scaffolds only)
- `scl-deep/systems-glossary.md`, `scl-deep/systems-language-audit.md`

### Codex NEVER Touches
- Card content in `cards/`
- Operis editions (except historical-events scaffolds)
- `scl-directory.md`
- `exercise-library.md`
- Any file requiring live web research to populate
- SCL rule or emoji creation/modification artifacts

## Execution Notes

- Treat the architecture as a layered resolver: dependencies first, leaf tasks last.
- Keep handoffs explicit between generator, validator, explorer, and reviewer agents.
- Do not bypass interlocks: if a dependency is unmet, the container remains pending.
