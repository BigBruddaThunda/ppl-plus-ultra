# Phase 2: Core Data - Context

**Gathered:** 2026-03-14
**Status:** Ready for planning

<domain>
## Phase Boundary

Four dial weight tables (Order, Axis, Type, Color) plus Block and Operator weight tables — all 6 categories as typed TypeScript modules in canvas/. A fitness keyword dictionary (~2,500 terms) as JSON with TypeScript types. An exercise dictionary ported from existing JSON with fuzzy-matchable alias layer. A computeRawVector(zip) function that sums raw weights into a 61-dimensional array (steps 1-3 of the weight derivation formula). The interaction resolver (step 4, constraint hierarchy) is Phase 3 — NOT this phase.

</domain>

<decisions>
## Implementation Decisions

### Weight Table Authoring
- **Re-derive all weights from scratch** using CLAUDE.md and scl-directory.md as canonical sources. Do NOT port existing DRAFT markdown tables from middle-math/weights/. Fresh derivation ensures no drift from stale drafts.
- **All 6 categories**: Order (7), Axis (6), Type (5), Color (8), Block (22), Operator (12). The weight vector is 61-dimensional across ALL emojis — all categories must be populated.
- **Cross-talk scope: let the researcher decide.** Analyze scl-directory.md rules to determine which intra-category relationships (e.g., Order↔Order) actually exist in the spec vs. cross-category only. Don't pre-commit to a pattern.
- **Coarse scale: use even values + key thresholds** (0, ±2, ±4, ±6, ±8). The mid-range distinctions (+1 vs +2) are noise for exercise selection. Author at coarse granularity from the start.
- **Citation: cite hard rules, estimate soft ones.** Hard suppressions (-6 to -8) and strong affinities (+6 to +8) MUST cite a specific rule from CLAUDE.md or scl-directory.md. Mid-range values (-4 to +4) can be estimated from character descriptions.
- **Phase 2 includes basic summation**: computeRawVector(zip) sums all four dials' affinity and suppression weights into a 61-dimensional array. This is steps 1-3 of weight-system-spec.md (Primary, Affinity Cascade, Suppression Cascade). Step 4 (Interaction Resolution with constraint hierarchy) is Phase 3.
- **Ignore existing weight-vectors.json.** The pre-computed vectors in middle-math/ were derived from DRAFT weights we're replacing. Fresh derivation means fresh validation — no anchoring to potentially wrong values.

### Exercise Dictionary
- **Port existing exercise-library.json** shape (id, section, name, scl_types, equipment_tier, gold_gated, movement_pattern, muscle_groups, bilateral, compound) into TypeScript.
- **Auto-derive search tokens from exercise names** (split into searchable fragments) PLUS a **manual alias layer** for common gym slang (~100-200 high-value entries seeded now). Abbreviations (RDL, OHP, SLDL) and tribal knowledge aliases ('skullcrusher' → 'Lying Triceps Extension').
- **Exercise relevance derived from weight tables, not scored individually.** Drop the order_relevance and axis_emphasis fields (they list ALL values and carry no signal). An exercise's Type + equipment tier + movement pattern filters it through the zip code's weight vector. The dictionary is clean metadata; the weight system does the work.

### Keyword Dictionary
- **Hybrid source: first-party + seed supplement.** Mine CLAUDE.md, scl-directory.md, and exercise-library.md for fitness vocabulary first (authoritative). Supplement with voice-parser-architecture seed entries that aren't already covered.
- **Collision handling: split into compound forms.** Ambiguous single words ('press') are avoided in favor of compound keywords ('bench press', 'overhead press') that have precise dimension affinity. If a single word is ambiguous, only include it as part of longer phrases.
- **JSON file + TypeScript types.** dial-keywords.json as data, imported and validated against a TypeScript interface at build time. Same pattern as exercise-library.json.

### Claude's Discretion
- TypeScript module shape for weight tables (const objects vs. JSON + types — pick whichever matches the phonebook pattern from Phase 1)
- Exact number of alias entries to seed (target ~100-200, researcher determines the high-value set)
- How to structure the keyword mining pipeline (which sources read in what order)
- Test strategy for weight tables and keyword dictionary

</decisions>

<specifics>
## Specific Ideas

- The exercise dictionary should NOT duplicate what the weight tables already express — clean metadata only, let the weight system rank
- Compound keywords preferred over ambiguous singles — "the longer the match, the more precise the score"
- Coarse scale is a feature, not a limitation — reduces false precision in a system that will be refined iteratively

</specifics>

<code_context>
## Existing Code Insights

### Reusable Assets
- `canvas/src/types/scl.ts` — All 61 SCL primitives as const objects with SclEntry interface. The phonebook pattern. Weight tables must align with these positions.
- `canvas/src/parser/zip-converter.ts` — Bidirectional zip converter. computeRawVector() will consume the same zip codes this converter handles.
- `middle-math/exercise-library.json` — ~2,185 exercises already parsed. Port to TypeScript, don't re-parse.
- `middle-math/weights/*.md` — DRAFT weight declarations (reference only, NOT to be ported). Useful for understanding what rules were considered.
- `middle-math/weight-system-spec.md` — The derivation formula (4 steps). Steps 1-3 are Phase 2 scope.
- `seeds/voice-parser-architecture.md` — ~13K keyword entries (v2 scope). Supplement source for the ~2,500 Phase 2 dictionary.

### Established Patterns
- Const object phonebook: `ORDERS[2]` → `{ emoji: '⛽', name: 'Strength', slug: 'strength' }`. Weight tables should follow same keying.
- W enum for vector indexing: `vec[W.STRENGTH]` — weight vector slots indexed by semantic name
- JSON data + TypeScript types pattern (exercise-library.json model)

### Integration Points
- Weight tables must produce entries keyed to the same position numbers used in scl.ts (ORDERS[1-7], AXES[1-6], TYPES[1-5], COLORS[1-8])
- computeRawVector() output must be a 61-element array indexed by the W enum from Phase 1
- Exercise dictionary TypeScript types must be importable by the Phase 3 text scorer

</code_context>

<deferred>
## Deferred Ideas

- Per-exercise affinity scoring (individual exercise × Order/Axis scores) — too much authoring for Phase 2, may never be needed if weight tables do the job
- Full 13K keyword dictionary from voice-parser-architecture — v2 scope (XPRS-01)
- Context-aware keyword scoring using user history — v2 scope (XPRS-03)
- Intra-category cross-talk that goes beyond what scl-directory.md rules support — don't invent relationships the spec doesn't describe

</deferred>

---

*Phase: 02-core-data*
*Context gathered: 2026-03-14*
