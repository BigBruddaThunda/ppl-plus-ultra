# Ppl± Blank Canvas Infrastructure

## What This Is

A development infrastructure layer for Ppl± that enables procedural rendering, visual architecture drafting, and batch content generation. It consists of a full SCL parser (emoji math + keyword dictionary + heuristic text classification), Claude Code skills/hooks/subagents for canvas-driven development, a weight-vector-to-CSS rendering pipeline, and production port/batch scripts. This infrastructure powers a future visual canvas (localhost:3000) where Jake architects Ppl± interactively — and eventually becomes the foundation layer of Graph Parti, a universal architecture tool.

## Core Value

The SCL parser must deterministically convert any input — zip codes, natural language, pasted context — into weight-vector-tagged, layer-sorted SCL addresses without requiring AI. The math sorts. AI creates and refines.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Offline SCL parser that converts 61-emoji zip codes to/from 4-digit numeric addresses and computes 61-dimensional weight vectors
- [ ] Keyword dictionary (~13K entries) mapping common fitness/training terms to SCL addresses (Type, Axis, Color, Order)
- [ ] Heuristic text classifier that detects exercise names, equipment mentions, body parts and maps them to SCL dimensions
- [ ] Weight-vector-to-CSS pipeline deriving 30+ custom properties (color palette, typography, spacing, saturation, gradient direction) from weight vectors
- [ ] Design token system (design-tokens.json) encoding all 8 Color palettes, 7 Order typographies, 6 Axis gradients, and block container styles
- [ ] `/blank-canvas` Claude Code skill that initializes the canvas workspace and loads current state
- [ ] `canvas-renderer` subagent definition — fresh context for v0 rewrites, resumable for iteration
- [ ] PostToolUse hook that auto-applies publication standard and art direction (intaglio/engraving aesthetic) to canvas output
- [ ] `canvas-to-production.sh` script that ports finalized canvas elements into the real Ppl± repo structure (cards/, html/, etc.)
- [ ] `batch-propagate.sh` script that templates a design element across N zip codes at once
- [ ] Canvas state persistence: local working state (.local/) + git-committed snapshots on command
- [ ] Parse-and-sort pipeline: any pasted text auto-runs through SCL parser, tags to nearest zip code(s), places on relevant layer
- [ ] Card HTML template system for rendering .md workout cards as interactive web components
- [ ] Integration tests validating parser accuracy, weight derivation correctness, and CSS output compliance

### Out of Scope

- Visual canvas UI (React Flow/tldraw) — deferred to Session 3+ after infrastructure is solid
- Graph Parti separation from Ppl± — Ppl± is the pilot instance; Graph Parti generalizes later
- Mobile app development — web-first, mobile later
- AI-dependent sorting — the core parser must work offline with no AI/cloud dependency
- Operis generation pipeline — exists separately, does not block this work
- Card content generation (Phase 2 workout writing) — continues independently

## Context

### Existing Architecture
Ppl± has 1,680 unique workout addresses (zip codes) across 42 decks (7 Orders x 6 Axes), each with 40 cards (5 Types x 8 Colors). The SCL (Semantic Compression Language) uses 61 emojis across 7 categories. A complete middle-math layer is seeded with weight system declarations, exercise selection algorithms, and rendering derivation logic.

### Key Seeds Already Planted
- `seeds/experience-layer-blueprint.md` — master technical architecture (Next.js/Supabase/Vercel, weight-to-CSS rendering)
- `seeds/numeric-zip-system.md` — 4-digit numeric addressing standard
- `seeds/mobile-ui-architecture.md` — 4-dial UI, tool drawer, canvas interactions
- `seeds/interactive-diagrams-architecture.md` — 8 diagram types from compiled JSON
- `seeds/voice-parser-architecture.md` — 13K-entry keyword dictionary for natural language to zip routing
- `middle-math/rendering/` — CSS custom property derivation specs
- `middle-math/weights/` — weight system declarations for Orders (other categories stubbed)

### Graph Parti Connection
Graph Parti (github.com/BigBruddaThunda/graph-parti) is the universal version of this infrastructure. Ppl± is the pilot instance that proves the pattern. The blank-canvas infrastructure must be built in a way that the SCL-specific logic can eventually be swapped for any domain's addressing schema, making Graph Parti a general-purpose architecture tool.

### Claude's New Interactive Visuals (March 2026)
Anthropic shipped inline HTML+SVG+Chart.js rendering in Claude chat (March 12, 2026). This validates the procedural rendering approach — structured data → interactive visual output. The same model reasoning that generates chat visuals powers Claude Code's component generation. The blank-canvas leverages this: Claude Code writes .tsx files that Vite hot-reloads on localhost:3000.

### Daily Driver Workflow
Jake wants this as a phone-accessible paste-bin/sorter where he can load project context on the go, sorted by SCL math without needing AI. The system handles tagging automatically — no manual tagging. The parser builds and tags itself from the content.

## Constraints

- **Location**: `canvas/` at repo root — clean separation from cards/, seeds/, middle-math/
- **Offline-first**: Core parser must work with zero network, zero AI, zero cloud dependencies
- **Art direction**: All visual output must follow the intaglio/banknote engraving aesthetic (hatching, guilloche, colorized for screens)
- **Publication standard**: All text output must follow `scl-deep/vocabulary-standard.md` and `scl-deep/publication-standard.md`
- **Existing infrastructure**: Must integrate with existing scripts/, skills, hooks, and subagent definitions in .claude/
- **Session budget**: 2 sessions to build infrastructure; visual canvas layer comes in Session 3+
- **Parser accuracy**: Exercise name detection must use `exercise-library.md` as the authoritative source (~2,185 exercises)

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Infrastructure before visual canvas | Solid bus means faster canvas build later. Skills/hooks/parser are reusable regardless of canvas substrate choice | — Pending |
| canvas/ at root | Clean separation from existing dirs. Canvas is a new system, not an extension of middle-math or web/ | — Pending |
| Full parser (math + keywords + heuristics) | Parse-and-sort requires text classification. Keyword dictionary already designed in voice-parser seed. Most useful for daily driver workflow | — Pending |
| Parse-and-sort over inbox-first | Jake doesn't want to tag manually. The system should auto-sort. SCL math is deterministic enough to do this | — Pending |
| Local state + git snapshots | Working state stays fast and messy. Snapshots committed on command for architectural record and temp-architect session access | — Pending |
| Graph Parti as eventual extraction | Build Ppl±-specific now, but keep SCL-specific logic isolated so it can be swapped later | — Pending |

---
*Last updated: 2026-03-13 after initialization*
