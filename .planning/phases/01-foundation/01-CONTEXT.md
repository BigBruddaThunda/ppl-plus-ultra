# Phase 1: Foundation - Context

**Gathered:** 2026-03-13
**Status:** Ready for planning

<domain>
## Phase Boundary

Canvas workspace scaffold at `canvas/` with its own package.json, TypeScript type definitions for all 61 SCL primitives, bidirectional zip converter (TypeScript port of existing Python), deck derivation, and Claude Code path-gating infrastructure (AGENT-BOUNDARIES.md) before any hooks are added.

</domain>

<decisions>
## Implementation Decisions

### Type System
- Lightweight typing for zip codes — simple interfaces with runtime validation, not branded types
- Const objects for all 61 SCL emoji identity maps (Orders, Axes, Types, Colors, Operators, Blocks, System) — JSON-serializable phonebook pattern matching existing Python dicts
- Indexed array + enum for weight vectors — `vec[W.STRENGTH]` reads like SCL, underlying array stays JSON-compatible with existing `weight-vectors.json`
- All 61 SCL emojis use ONE consistent const object + index pattern — one phonebook, one bus, regardless of category (dials, operators, blocks, system)

### Dual Hierarchy
- **System hierarchy (constraint resolution):** Order > Color > Axis > Type — this is the math, enforced at runtime by the resolver. The law. Unchanged from CLAUDE.md.
- **Experience hierarchy (navigation/UX):** Axis > Color > Order > Type — how a user feels and navigates the system. The elevator model. Axis = floor, Color = room.
- Both coexist. The phonebook resolves the same address regardless of which dial the user spins first. The constraint hierarchy lives exclusively in the resolver, not in the types.

### Package Structure
- canvas/ at repo root with its own package.json, isolated from web/, middle-math/, cards/
- TypeScript port of zip_converter.py as the foundation module

### Claude's Discretion
- Python vs TypeScript strategy for existing middle-math scripts (port, keep both, or vendor)
- Package boundary between canvas/ and middle-math/ compiled JSON files (import vs copy)
- AGENT-BOUNDARIES.md content and path-gating pattern for hooks
- Exact tsconfig strictness settings
- Test framework setup (Vitest confirmed from research)

</decisions>

<specifics>
## Specific Ideas

- "Which one has the cleanest bus path for great systems architecture and potential for endless room for modded growth" — Jake wants type patterns that scale to Graph Parti and handle future domain swapping (fitness → architecture → music → anything)
- The phonebook pattern must support "octave-like growth" — each of the 61 SCL emojis gets maximum context and identity at its index position
- The system should feel like the code "speaks the language" of SCL — `vec[W.STRENGTH]` not `vec[1]`

</specifics>

<code_context>
## Existing Code Insights

### Reusable Assets
- `scripts/middle-math/zip_converter.py` — Complete Python converter with all lookup tables, validation, deck derivation, operator derivation, path generation. Direct port candidate for TypeScript foundation.
- `scripts/middle-math/weight_vector.py` — Weight vector computation in Python. Reference implementation.
- `middle-math/weight-vectors.json` — Pre-computed 61-dimensional vectors for all 1,680 zip codes. Can be imported directly.
- `middle-math/zip-registry.json` — Full registry of all zip codes with metadata.
- `middle-math/design-tokens.json` — All 8 Color palettes already defined (DRAFT status). 7 CSS properties per palette.
- `middle-math/exercise-library.json` — Parsed exercise library (~2,185 exercises).

### Established Patterns
- Python dict pattern: `{position: (emoji, name, slug)}` — the TypeScript const objects should mirror this structure
- Bidirectional lookup: emoji→position and position→emoji as separate tables (already implemented in Python)
- Polarity split: PREPARATORY_COLORS and EXPRESSIVE_COLORS sets already defined

### Integration Points
- canvas/ TypeScript will consume middle-math/ JSON files (weight-vectors.json, design-tokens.json, zip-registry.json)
- Existing Python scripts in scripts/middle-math/ remain operational — canvas/ TypeScript is a parallel implementation, not a replacement
- Claude Code hooks in .claude/ must be path-gated to avoid canvas/ hooks triggering on cards/ writes

</code_context>

<deferred>
## Deferred Ideas

- Experience hierarchy (Axis > Color > Order > Type) as a navigation pattern — belongs in the visual canvas layer (Session 3+), not in the foundation types
- The idea that the phonebook pattern should be domain-swappable for Graph Parti — noted for extraction architecture, not Phase 1 scope

</deferred>

---

*Phase: 01-foundation*
*Context gathered: 2026-03-13*
