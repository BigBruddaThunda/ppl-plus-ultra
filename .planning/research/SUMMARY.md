# Project Research Summary

**Project:** Ppl± Blank Canvas Infrastructure
**Domain:** Offline semantic parser + weight-vector CSS rendering pipeline + Claude Code dev infrastructure
**Researched:** 2026-03-13
**Confidence:** HIGH

## Executive Summary

The Blank Canvas Infrastructure is a local development toolchain, not a user-facing application. Its job is to make building the web app faster and more systematic by giving Jake a daily-driver workspace where pasted text auto-classifies to SCL addresses, zip codes render visually as styled workout cards, and Claude Code skills/hooks/subagents provide disciplined automation. The system has three tightly-coupled subsystems — a deterministic offline parser, a weight-vector-to-CSS derivation pipeline, and a Claude Code skill/hook/subagent layer — and all three must be built before any one of them is useful. The architecture research confirms this completely: the full pipeline is a strict sequence of `string input → ParseResult → numeric zip → WeightVector → RenderDescriptor → CSS vars`, and no stage can be usefully operated without its upstream stage being complete.

The recommended approach is to build the foundation in a strict dependency order: zip conversion and type definitions first (zero dependencies), then the weight tables and keyword dictionary in parallel (both read from first-party specs), then the integration layer that wires them together, then the rendering pipeline on top of the weight engine, and finally the Claude Code infrastructure (skills, hooks, subagents) once there is something real to operate on. The visual canvas UI (React/Vite hot-reload at localhost:3000) is the last piece to add because it is a thin viewport over a working system — without the system, it has nothing meaningful to display. The stack is deliberately minimal: TypeScript 5, Vite 8, Vitest 4, style-dictionary v4, fastest-levenshtein, and fuse.js. All technologies are verified against current docs. No ML, no NLP, no runtime AI calls — the offline-first constraint is non-negotiable.

The key risks concentrate in two areas. First, the weight-vector-to-CSS arbitration layer: when a zip code carries opposing dial signals (e.g., ⛽ Strength pushing dense/compact layout against 🟡 Fun pushing warm/playful), the naive implementation applies all CSS signals additively and produces an incoherent room. The arbitration between "structural" CSS properties (owned by Order) and "tonal" CSS properties (owned by Color) must be specced before any CSS code is written — retrofitting it is rated HIGH recovery cost. Second, the Claude Code hook infrastructure: ungated PostToolUse hooks that fire on every file write in the repo create compounding execution noise, and Stop hooks using exit code 2 produce infinite loops. Both are well-documented failure modes with low recovery cost if addressed at infrastructure setup time, but they corrupt the dev environment if missed.

---

## Key Findings

### Recommended Stack

The canvas workspace lives in a `canvas/` directory with its own `package.json`, separate from `web/`. This isolates canvas tooling dependencies from the production Next.js app. The parser and CSS pipeline compile to artifacts (`exercises.json`, `design-tokens.css`, `tokens.ts`) that `web/` can eventually import — no circular dependencies.

**Core technologies:**
- TypeScript 5: Primary language for all canvas subsystems — strict types prevent errors in weight vector math (pure arithmetic on a 61-value array)
- Vite 8: Dev server for canvas; fastest HMR for hot-reload at localhost:3000; no framework lock-in; correct tool for a single-page local dev workspace (Next.js is overkill here)
- Vitest 4: Unit and integration testing; shares Vite config with zero extra setup; 2-4x faster than Jest for the test sizes involved
- style-dictionary v4: Build-time design token pipeline; `design-tokens.json` → CSS custom properties + TypeScript constants; static layer only (not runtime derivation)
- fastest-levenshtein: Myers 32-bit edit-distance algorithm for exercise name fuzzy matching (Levenshtein ≤ 2 for ~2,185 exercise names)
- fuse.js 7.1.0: Second-pass fuzzy search for multi-word alias matching where edit distance alone falls short
- Pure TypeScript `weightsToCSSVars()`: Runtime weight-to-CSS derivation is ~30 lines of arithmetic; no library needed; spec already written in `middle-math/rendering/ui-weight-derivation.md`

**What not to use:** ML/NLP libraries (the parser architecture is explicitly AI-free), CSS-in-JS runtime libraries (conflict with the CSS custom property approach), Webpack/CRA (deprecated/slow), any server-side parser endpoint (offline-first hard constraint).

### Expected Features

**Must have (table stakes) — Sessions 1–2:**
- Emoji ↔ numeric zip conversion — everything downstream depends on it
- 61-dimensional weight vector computation — enables all rendering and selection
- Fitness-specific keyword dictionary (~2,500 entries: exercises, body parts, equipment, SCL names) — enables text classification
- Heuristic text classifier returning top-3 matches with confidence scores and `defaulted_dimensions` flags
- Design token JSON (8 Color palettes, 7 Order typographies, 6 Axis gradients) — single source for all rendering values
- CSS custom property derivation (weight vector → RenderDescriptor → 30+ CSS vars) — procedural rendering
- Hot-reload canvas at localhost:3000 (Vite + React) — feedback loop
- Canvas state persistence in `.local/` (git-ignored)
- `/blank-canvas` Claude Code skill and `canvas-renderer` subagent definition
- PostToolUse hook gated to `canvas/` paths for art direction enforcement
- Integration tests for zip conversion, weight computation, CSS derivation

**Should have (competitive differentiators) — Session 3:**
- Full parse-and-sort pipeline (pasted text → tagged/sorted by SCL layer) — Jake's daily driver workflow
- Visual canvas UI (React Flow or tldraw) — viewport into the working infrastructure
- `canvas-to-production.sh` migration script — closes the prototype trap; canvas output IS the production artifact
- `batch-propagate.sh` — one design decision propagates across N zip codes without 1,680 manual edits
- Git snapshot skill — disciplined architectural record

**Defer (v2+):**
- Graph Parti extraction — generalize only after the Ppl± pattern is proven
- Card HTML template system — Phase 4/5 scope, not canvas infrastructure
- Full 13K-entry voice parser dictionary — separate system; canvas needs only the ~2,500 fitness subset
- Interactive diagram components (Anatomy Explorer, City Navigator) — Phase 4/5

**Anti-features to reject:** AI-assisted sorting in the parser (violates offline-first), real-time canvas-to-web sync (creates fragile coupling), exhaustive 13K dictionary before v1 (separate project), premature Graph Parti generalization.

### Architecture Approach

The architecture is a strict layered derivation pipeline: each stage transforms one clean type to the next, with no stage knowing about any other stage's internals. This makes each stage independently testable and means a bug in the CSS var generator does not require debugging the weight engine. The full sequence is `string → ParseResult → numeric zip → WeightVector[61] → RenderDescriptor → Record<string, string>` (CSS custom properties). The keyword dictionary is injected into the scorer as a parameter (not imported directly) so tests can use minimal mock dictionaries. The constraint hierarchy (Order > Color > Axis > Type) lives exclusively in the interaction resolver, never in individual dial tables.

**Major components:**
1. Parser layer (`canvas/parser/`) — zip converter, keyword dictionary, tokenizer, fuzzy matcher, scorer; stateless pure functions; no I/O
2. Weight engine (`canvas/weights/`) — primary seeder, per-dial affinity/suppression tables, interaction resolver; produces WeightVector[61]
3. Rendering pipeline (`canvas/rendering/`) — palette/typography/layout/tone derivers, assembler, CSS var generator; consumes WeightVector, outputs CSS custom properties
4. Design tokens (`canvas/tokens/design-tokens.json`) — authoritative hex values, font names, spacing; editorial, never computed
5. Claude Code infrastructure (`.claude/`) — `/blank-canvas` skill, `canvas-renderer` subagent, PostToolUse hook; orchestration layer, not computation

**Hard boundaries that must not be crossed:** `rendering/` does not import from `parser/`; `weights/` does not import from `rendering/`; `design-tokens.json` is not read by `weights/`; canvas components do not call `computeVector()` directly.

### Critical Pitfalls

1. **CSS arbitration missing between opposing dial signals** — Separate CSS properties into "structural" (Order owns: density, spacing, block rhythm) and "tonal" (Color owns: palette, saturation). Build this into the spec before writing any CSS derivation code. If skipped, the only fix is retrofitting the arbitration layer and regenerating all pre-computed descriptors (HIGH recovery cost).

2. **PostToolUse hooks firing on wrong paths** — Every new PostToolUse hook must include an explicit path gate (`if echo "$FILE" | grep -q 'canvas/'; then ...`). A hook with `matcher: "Edit|Write"` and no path filter runs on every file write in the repo. Document which hooks own which paths in `.claude/AGENT-BOUNDARIES.md` before adding any canvas-specific hooks.

3. **Stop hook infinite loop via exit code 2** — Stop hooks must use exit code 0 or 1 only, and use `async: true` for any blocking operations. Exit code 2 from a Stop hook blocks Claude from stopping, which triggers another stop attempt, which triggers the hook again (documented GitHub issue #10205). Address at Phase 1 infrastructure build.

4. **Keyword token collision between dial dimensions** — "Heavy" scores for both Order (⛽ Strength) and Color (🟣 Technical). Build a `dimension_affinity_score` per keyword that biases tokens toward their primary dimension, and add a conflict-resolution pass after per-dimension scoring. Must be designed before the dictionary reaches full scale — retrofitting onto 13K entries is painful.

5. **Parser defaults silently overriding user intent** — When a dial dimension scores zero, the parser defaults (e.g., 🏛 Basics for Axis). The `ParseResult` interface must include `defaulted_dimensions: string[]` from day one so the routing layer can replace defaults with user-preference data. Retrofitting this is a breaking API change.

---

## Implications for Roadmap

Based on the dependency graph in ARCHITECTURE.md and the pitfall-to-phase mapping in PITFALLS.md, the build order is fully deterministic. Every phase is blocked by its predecessor; there is no parallel starting path.

### Phase 1: Foundation and Infrastructure Setup

**Rationale:** Zero-dependency pieces that every other phase requires. The zip converter is the universal addressing key. The TypeScript type definitions are the interface contracts. The Claude Code infrastructure setup (skill/hook templates, AGENT-BOUNDARIES.md, path gating patterns) must be locked before any hooks are added — the pitfall research shows that getting hooks wrong early is expensive.

**Delivers:** `zip-converter.ts`, `weight-types.ts`, `design-tokens.json` (initial palette draft), `.claude/` directory structure with path-gating patterns documented, `AGENT-BOUNDARIES.md`.

**Addresses:** Table stakes — emoji ↔ numeric zip conversion (P1), design token JSON (P1), `/blank-canvas` skill skeleton.

**Avoids:** PostToolUse hook path gating pitfall (Pitfall 2), Stop hook infinite loop (Pitfall 3), skill auto-activation collision (Pitfall 8). All three require decisions made at setup time, not patchable later.

### Phase 2: Core Engine (Weight Tables + Keyword Dictionary)

**Rationale:** The four dial weight tables and the fitness keyword dictionary are independently derivable from first-party specs (`middle-math/weights/` and `seeds/voice-parser-architecture.md`). They have no cross-dependency on each other, so they can be built in parallel within the session. But they both require Phase 1 types to exist.

**Delivers:** `order-weights.ts`, `axis-weights.ts`, `type-weights.ts`, `color-weights.ts`, `vocab/dial-keywords.json`, `vocab/exercises.json` (built from `exercise-library.md` by `build-exercise-vocab.ts`).

**Uses:** TypeScript 5, fastest-levenshtein, fuse.js (for exercises.json alias matching).

**Avoids:** Parser dictionary structure pitfall — design the indexed lookup structure before the dictionary reaches scale. Mark collision-prone keywords with `dimension_affinity_score` during initial construction (Pitfalls 1 and 4).

### Phase 3: Integration Layer (Resolver + Scorer)

**Rationale:** The interaction resolver requires all four dial weight files. The text scorer requires the tokenizer, fuzzy matcher, and vocab JSON files. This phase wires the Phase 2 components into operational units with public APIs.

**Delivers:** `weights/interaction-resolver.ts`, `weights/index.ts` (public API), `parser/tokenizer.ts`, `parser/fuzzy-match.ts`, `parser/scorer.ts`, `parser/index.ts` (public parser API). `ParseResult` interface includes `defaulted_dimensions` array from the start (Pitfall 5 prevention).

**Implements:** Constraint hierarchy encoding pattern (Order > Color > Axis > Type lives only in the resolver, never in dial tables).

**Avoids:** Parser defaults silently overriding user intent (Pitfall 5). Hierarchy logic bleeding into dial tables (Architecture Anti-Pattern 2).

### Phase 4: Rendering Pipeline

**Rationale:** Requires Phase 3 weight engine to produce WeightVector. This is where the CSS arbitration decision must be made before any code is written. The spec must separate structural CSS properties (Order-owned) from tonal CSS properties (Color-owned) before the deriver files are implemented.

**Delivers:** `rendering/render-types.ts`, `palette-deriver.ts`, `typography-deriver.ts`, `layout-deriver.ts`, `tone-deriver.ts`, `assembler.ts`, `css-vars.ts`. `design-tokens.json` finalized with semantic token names (not primitive hex values).

**Uses:** style-dictionary v4 for static token build (`design-tokens.json` → `design-tokens.css` + `tokens.ts`).

**Avoids:** CSS incoherence from opposing dial signals (Pitfall 4 — the highest recovery cost pitfall). Bypassing the pipeline with direct design token reads (Architecture Anti-Pattern 1). Storing primitive tokens instead of semantic tokens ("looks done but isn't" checklist item).

### Phase 5: Claude Code Infrastructure

**Rationale:** Skills, hooks, and subagents are only valuable once there is a working system to operate on. The `canvas-renderer` subagent needs to know what `canvas/components/` look like. The PostToolUse hook calls the parser for validation — the parser must exist first.

**Delivers:** `/blank-canvas` skill (finalized), `canvas-renderer` subagent (scoped to `canvas/components/` only), PostToolUse art direction enforcement hook (path-gated to `canvas/`), `canvas-to-production.sh` skeleton.

**Implements:** Pattern 5 (Claude Code skill as context loader). "Flush before delegate" rule enforced in AGENT-BOUNDARIES.md. Subagent exclusion list for card-generation skill.

**Avoids:** Subagent producing stale outputs (Pitfall 7), wrong skill auto-activating (Pitfall 8), MDX emoji parsing break in canvas components (Pitfall 6 — use `u` flag on all content regexes).

### Phase 6: Tests, Hot-Reload Canvas, and Card Templates

**Rationale:** Integration tests validate the full pipeline end-to-end using worked examples from project seeds. The hot-reload canvas is the thin React wrapper that makes the working system visible. Card templates are the final deliverable that bridges canvas infrastructure to production content.

**Delivers:** `canvas/tests/*.test.ts` (zip converter, weight derivation, CSS output, parser accuracy), Vite + React hot-reload canvas at localhost:3000 (`CardShell.tsx`, `BlockRenderer.tsx`), `batch-propagate.sh`.

**Uses:** Vitest 4, React 19, Vite 8.

**Avoids:** `canvas-renderer` subagent writing directly to production directories (Architecture Anti-Pattern 4). Inline style application instead of `:root` CSS custom property block (performance trap). Accidentally committing `.local/` working state (checklist item).

---

### Phase Ordering Rationale

- **Phases 1-3 are hard-blocked in sequence:** zip converter → type definitions → weight tables → resolver. No shortcut.
- **Phase 4 is sequenced after Phase 3** because CSS derivation requires a working WeightVector. The CSS arbitration spec decision (structural vs. tonal CSS) must happen at Phase 4 entry, not at Phase 5 patching time.
- **Phase 5 is sequenced after Phase 3 and 4** because the PostToolUse hook calls the parser, and the subagent operates on components that require the rendering pipeline.
- **Phase 6 last** because integration tests validate the completed system, and the canvas UI is a viewport into a working system — adding it before the system works produces an empty shell.
- **The visual canvas UI is deferred to Phase 6** because FEATURES.md explicitly flags it as P2 and the architecture confirms it is a thin wrapper. Building it in Phase 2 (a common mistake) produces a tool with nothing to display.

### Research Flags

Phases needing no deeper research during planning (well-documented patterns with first-party specs):
- **Phase 1:** Zip converter and TypeScript types are pure lookup tables. Claude Code hook/skill format is fully documented.
- **Phase 2:** Weight tables are a direct port from `middle-math/weights/` seed specs. Exercise vocab is a direct parse of `exercise-library.md`.
- **Phase 5:** Claude Code skills/hooks/subagents are fully documented with official sources. All format fields verified.

Phases that may need targeted research during planning:
- **Phase 3 (Interaction Resolver):** The constraint hierarchy encoding (Order > Color > Axis > Type with hard suppression at -6) is well-specced, but the interaction between soft-weight summing and hard-block thresholds needs a worked validation test against all 1,680 zip codes before the resolver is considered correct.
- **Phase 4 (Rendering Pipeline):** The arbitration boundary between structural (Order) and tonal (Color) CSS properties has been identified as a pitfall but the full property-to-owner mapping has not been written. This mapping must be produced at Phase 4 entry as a specification step before implementation.

---

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | All versions verified against official npm registry and official docs. Existing `web/package.json` versions confirmed by direct file read. No speculative version pins. |
| Features | HIGH (project context) / MEDIUM (competitive comparison) | P1 features derived directly from first-party project seeds and architecture docs. Competitive comparison (v0.dev, bolt.new, tldraw) from web research; findings are directional, not authoritative. |
| Architecture | HIGH | Based entirely on first-party project documents: middle-math specs, seed blueprints, working TypeScript snippets already present in seeds. Component responsibilities and boundaries are fully specified. |
| Pitfalls | HIGH (hooks/subagents), MEDIUM (parser/CSS patterns) | Hook lifecycle behavior verified against official Claude Code docs and GitHub issues. Parser dimension collision and CSS arbitration pitfalls derived from analogous documented patterns in intent classification and CSS token systems; not Ppl±-specific empirical evidence. |

**Overall confidence:** HIGH

### Gaps to Address

- **CSS arbitration property map:** The spec distinguishes structural (Order) vs. tonal (Color) CSS ownership but the specific property-to-owner table has not been written. Must be produced as a deliverable at Phase 4 entry before any deriver code is written.
- **Weight vector worked validation:** The interaction resolver spec includes one worked example (⛽🏛🪡🔵 = 2123). A validation pass across all 1,680 zip codes is needed to confirm no edge case produces an incoherent vector. This is a Phase 3 exit criterion, not a blocker.
- **Keyword collision map:** The pitfall research identifies the collision problem and the solution approach (`dimension_affinity_score`) but the actual list of collision-prone keywords has not been audited. Should be a Phase 2 deliverable alongside the initial dictionary construction.
- **`canvas/` directory creation:** Research confirms the directory structure and `package.json` separation, but the actual `canvas/` workspace has not yet been initialized in the repo. Phase 1 begins with that initialization.

---

## Sources

### Primary (HIGH confidence)
- Official Claude Code Skills docs (code.claude.com/docs/en/skills) — skills format, frontmatter fields
- Official Claude Code Hooks docs (code.claude.com/docs/en/hooks-guide) — hook lifecycle, event types, exit codes
- GitHub issue #10205 (anthropics/claude-code) — Stop hook infinite loop failure mode
- GitHub issue #19009 (anthropics/claude-code) — PostToolUse exit code 2 behavior confirmation
- Vitest 4.1.0 (vitest.dev) — version confirmed
- style-dictionary v4 migration (styledictionary.com) — v4 async API confirmed
- fuse.js 7.1.0 (npmjs.com/package/fuse.js) — version confirmed
- fastest-levenshtein (npmjs.com/package/fastest-levenshtein) — Myers algorithm, TypeScript support confirmed
- Vite 8.0.0 (npmjs.com/package/vite) — current version confirmed
- `web/package.json` — existing stack versions confirmed by direct file read
- `middle-math/ARCHITECTURE.md` — weight system architecture
- `middle-math/weights/weight-system-spec.md` — octave scale, derivation formula, constraint hierarchy
- `middle-math/rendering/ui-weight-derivation.md` — 5 rendering dimensions, RenderDescriptor spec
- `seeds/voice-parser-architecture.md` — dictionary structure, scoring algorithm, ParseResult interface
- `seeds/numeric-zip-system.md` — 4-digit notation, conversion TypeScript, validation logic
- `seeds/experience-layer-blueprint.md` — tech stack, rendering pipeline diagram
- `.planning/PROJECT.md` — component list, canvas/ directory decision, offline-first constraint

### Secondary (MEDIUM confidence)
- disler/claude-code-hooks-mastery (GitHub) — hook patterns, `stop_hook_active` loop prevention
- CSS Variables Guide: Design Tokens (frontendtools.tech) — semantic vs. primitive token distinction
- Intent Classification pitfalls (labelyourdata.com) — taxonomy size, dimension collision handling
- react-markdown emoji handling (GitHub issue #61) — emoji in markdown headings edge cases
- Parse Markdown Frontmatter in MDX (dev.to) — gray-matter + MDX frontmatter separation
- Competitor feature analysis: v0.dev, bolt.new, tldraw, React Flow, Storybook

---

*Research completed: 2026-03-13*
*Ready for roadmap: yes*
