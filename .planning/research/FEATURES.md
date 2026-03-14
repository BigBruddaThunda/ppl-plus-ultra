# Feature Research

**Domain:** Development canvas infrastructure — offline SCL parser, weight-vector-to-CSS rendering pipeline, Claude Code skills/hooks/subagents
**Researched:** 2026-03-13
**Confidence:** HIGH (project context from seeds + architecture docs), MEDIUM (competitive comparison from web research)

---

## Context

This feature research covers the **Blank Canvas Infrastructure** milestone: the `canvas/` directory system that gives Jake a local development environment for procedural rendering, parse-and-sort workflows, and canvas-driven architectural drafting. It is NOT the web app experience layer (Phase 4/5). It is the infrastructure that makes building the web app faster and more systematic.

Three subsystems in scope:

1. **Offline SCL Parser** — converts zip codes, natural language, pasted text → weight-vector-tagged SCL addresses. No AI, no network.
2. **Weight-Vector-to-CSS Pipeline** — derives 30+ CSS custom properties from 61-dimensional weight vectors. Design tokens.
3. **Canvas Development Environment** — Claude Code skills/hooks/subagents + local hot-reload canvas at localhost:3000.

---

## Feature Landscape

### Table Stakes (Users Expect These)

Features that must exist for the infrastructure to be usable. Missing these = the system can't do its job.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Emoji ↔ numeric zip conversion | Every other part of the system depends on it. Both representations must co-exist. | LOW | Pure lookup table. 4 arrays × 8 entries max. Already specced in `seeds/numeric-zip-system.md`. |
| 61-dimensional weight vector computation | The rendering pipeline, exercise selector, and progressive disclosure all consume vectors. Without this, nothing downstream works. | MEDIUM | Math is deterministic. Per-dial weights + cross-dial interactions. Specced in `middle-math/weights/`. |
| Keyword dictionary lookup (fitness terms → SCL addresses) | Parse-and-sort requires text → zip mapping. The voice parser seed already specced ~13K entries. A subset is needed for the canvas parser. | MEDIUM | Keyword dict is a JSON file. Lookup is O(1). Building the dict is the real work. |
| Heuristic exercise name detection | `exercise-library.md` is the authoritative source (~2,185 exercises). Parser must recognize these without AI. | MEDIUM | Exact-match + fuzzy string match against the exercise registry JSON. |
| CSS custom property derivation from weight vector | The rendering pipeline converts vectors → `--color-primary`, `--type-density`, `--spacing-base`, etc. This is how a workout card "looks like itself." | MEDIUM | 5 rendering dimensions specced in `middle-math/rendering/ui-weight-derivation.md`. Each is a scalar-to-token mapping. |
| Design token JSON file | All 8 Color palettes, 7 Order typographies, 6 Axis gradients, block styles need a single source of truth. | LOW | `design-tokens.json` — structured constant file. No computation. |
| Hot-reload local canvas at localhost:3000 | If you can't see the output immediately, the feedback loop is broken. Every tool in this category (v0.dev, bolt.new, Storybook) treats live preview as non-negotiable. | LOW | Vite + React. Already implied by the experience-layer-blueprint Next.js stack. |
| Canvas state persistence (local working state) | A canvas that forgets where you left off is not a daily driver. Working state in `.local/` is the minimum. | LOW | JSON write to `.local/canvas-state.json`. Git-ignored for working state. |
| Git snapshot on command | Architecture decisions need to be committed as records. Temp architect sessions need to read committed state. | LOW | Single script: `git add canvas/ && git commit -m "canvas snapshot"`. |
| Integration tests for parser accuracy | If the parser silently produces wrong zip codes, every downstream artifact is corrupted. Tests are the only guard. | MEDIUM | Unit tests: known input → expected zip. Coverage: emoji parsing, keyword matching, weight computation. |
| Parse output that surfaces confidence level | A classifier that only returns results without uncertainty is dangerous. Low-confidence classifications should be flagged, not silently emitted. | LOW | Add `confidence: 0.0–1.0` and `method: "exact" | "keyword" | "heuristic"` to parser output. |

---

### Differentiators (Competitive Advantage)

These are the features that make this infrastructure specifically Ppl±, not a generic parser or design token system.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Full parse-and-sort pipeline (any pasted text → tagged, sorted by SCL layer) | Jake's daily driver workflow. Phone-accessible paste-bin that auto-classifies without manual tagging. No other tool in the fitness or training domain does this. | HIGH | Requires all three parser stages to work together: emoji detection → keyword lookup → heuristic classification → weight vector → SCL address. |
| Weight vector as rendering instruction (not just data) | The same math that selects exercises also determines how the page is built. This is the core thesis: the character of the room matches the character of the workout. No fitness app does this. Design systems usually derive tokens from brand guidelines, not from the content itself. | HIGH | Requires the full weight-to-CSS spec to be implemented and consumed by the canvas renderer. |
| `canvas-to-production.sh` migration script | Finalized canvas elements port directly into `cards/`, `html/`, etc. This closes the "prototype trap" — most canvas tools produce throwaway output. Here, canvas output IS the production artifact. | MEDIUM | Shell script: reads finalized canvas elements, copies to correct repo paths per naming convention. |
| `batch-propagate.sh` templating across N zip codes | One design decision (e.g., a block container style) propagates across hundreds of cards at once. This is how 1,680 rooms get consistent design without 1,680 manual edits. | MEDIUM | Requires the template system to be parameterized by zip code. Each propagation run takes a template + a zip list. |
| PostToolUse hook: auto-apply publication standard and art direction | Every canvas output automatically inherits the intaglio/engraving aesthetic and vocabulary standard. Zero discipline required from the author — the system enforces it. v0.dev and bolt.new have no concept of a per-project art direction constraint. | MEDIUM | Hook reads `.claude/hooks/post-tool-use.sh`. Checks output against `scl-deep/publication-standard.md` and `seeds/art-direction-intaglio.md`. |
| `canvas-renderer` subagent with fresh context | Isolated Claude Code subagent for v0-style rewrites. The main context doesn't get polluted by iterative rendering experiments. This matches the "temp architect pattern" already in use. | LOW | Subagent definition file + spawn instructions. Already described in PROJECT.md. |
| Graph Parti extraction pathway | The SCL-specific logic is isolated from the general infrastructure. Ppl± is the pilot instance. Graph Parti is the general-purpose architecture tool. The blank-canvas infrastructure has legs beyond this repo. | HIGH | Requires clean interface boundaries: SCL-specific config in one directory, general infrastructure in another. Not needed for MVP. |
| Offline-first as hard constraint (zero AI, zero network, zero cloud) | The core parser must work with no dependencies. This is a trust property: the system's foundational math cannot have a network failure mode. Tools like v0.dev and bolt.new are fundamentally cloud-dependent; this parser is not. | MEDIUM | All dictionary data lives in-repo as JSON. All computation is synchronous Python/JS. No API calls in the critical path. |

---

### Anti-Features (Commonly Requested, Often Problematic)

Features that seem like good ideas but create concrete problems for this specific system.

| Feature | Why Requested | Why Problematic | Alternative |
|---------|---------------|-----------------|-------------|
| AI-assisted sorting in the parser | "Just let Claude figure out what zip code this text maps to." Feels easier than a keyword dictionary. | Violates the offline-first constraint. Network latency breaks the daily driver workflow. AI output is non-deterministic — same input can produce different zip codes across calls, corrupting the address space. The math must sort; AI creates and refines. | Build the keyword dictionary properly. 13K entries is a one-time investment. Exact matching is always deterministic. |
| Visual canvas UI (React Flow/tldraw) in the first two sessions | The spatial canvas is the most compelling part of the vision. It's natural to want to build it first. | Without the parser, design token system, and Claude Code skills/hooks as the bus, the canvas has nothing to render that means anything. The canvas is a viewport into the infrastructure. Build the infrastructure first; the canvas becomes trivial when the bus exists. Per PROJECT.md: "deferred to Session 3+ after infrastructure is solid." | Build infrastructure first (Sessions 1–2). Canvas UI becomes a thin React wrapper around a working system in Session 3. |
| Real-time sync between canvas and web app | Appealing for a "live preview" feel where changes in canvas immediately appear in the production web app. | Creates a coupling that makes both systems fragile. Canvas is a development tool, not a production rendering engine. Real-time sync adds infrastructure complexity that isn't needed while Phase 2 (card generation) is still active. | Use `canvas-to-production.sh` as the explicit, intentional migration boundary. Canvas and production are separate; the script is the gate. |
| Exhaustive keyword dictionary coverage (all 13K entries) before v1 | The voice parser architecture calls for ~13K entries. It seems like the parser is broken without them. | 13K entries is a separate project. The canvas parser needs the fitness/training subset: exercise names (~2,185 from the library), body parts (~40 muscle groups), equipment terms (~50), and Order/Type/Color/Axis name variants (~200). That's ~2,500 entries. The full 13K includes almanac, educational, and community routing terms not needed here. | Build the ~2,500 fitness-specific subset for v1. The remaining 10K+ entries are for the voice parser (Phase 4/5) and can be built incrementally. |
| Generalize for Graph Parti before Ppl± is working | Graph Parti is the universal version of this infrastructure. It's tempting to build the general version first. | Premature generalization means building for a domain that doesn't fully exist yet. Ppl± has 1,680 known zip codes, a 61-emoji vocabulary, and real content. Graph Parti has a concept. Build for the concrete case. Extract the general case when the pattern is proven. | Isolate SCL-specific logic in a `canvas/scl/` directory with clean interfaces. Don't abstract beyond that until Graph Parti development begins. |
| Canvas state as a database (user-facing persistence, multi-device) | Canvas is a development tool. Making it a database means adding auth, sync, conflict resolution, and migration paths — all before the production web app has those features. | Canvas state is working notes. Git snapshots are the committed record. | `.local/` for working state (git-ignored). `canvas/snapshots/` for committed record (git-tracked on command). That's the complete persistence model. |

---

## Feature Dependencies

```
[Emoji ↔ numeric zip conversion]
    └──required by──> [61-dimensional weight vector computation]
                          └──required by──> [CSS custom property derivation]
                          └──required by──> [Parse-and-sort pipeline]
                          └──required by──> [Progressive disclosure config]

[Keyword dictionary (fitness subset)]
    └──required by──> [Heuristic exercise name detection]
    └──required by──> [Parse-and-sort pipeline]

[Design token JSON]
    └──required by──> [CSS custom property derivation]
    └──required by──> [Hot-reload canvas at localhost:3000]

[CSS custom property derivation]
    └──required by──> [Card HTML template system]
    └──required by──> [canvas-to-production.sh]

[Claude Code skills + hooks]
    └──required by──> [PostToolUse auto-apply art direction]
    └──required by──> [canvas-renderer subagent]

[Integration tests]
    └──validates──> [Emoji ↔ numeric conversion]
    └──validates──> [Weight vector computation]
    └──validates──> [CSS derivation correctness]

[canvas-to-production.sh]
    └──requires──> [Card HTML template system]
    └──requires──> [CSS custom property derivation]

[batch-propagate.sh]
    └──requires──> [Card HTML template system]
    └──requires──> [Zip list (from existing card inventory)]
```

### Dependency Notes

- **Weight vector computation requires emoji ↔ numeric conversion:** The weight system operates on numeric positions (Order 1–7, Axis 1–6, etc.). Emoji addresses must resolve to numeric positions before weights can be computed.
- **Parse-and-sort requires both keyword dict AND weight vectors:** Keywords identify candidates. Weight vectors rank them when multiple matches exist.
- **CSS derivation requires design tokens:** The derivation produces character descriptors (`{"dominant": "structured-blue"}`). The design tokens map those to actual CSS values. Neither works without the other.
- **canvas-to-production.sh requires template system:** The script can only port finalized elements if there's a template to port them into. The template system must be built before migration can happen.
- **PostToolUse hook requires Claude Code skills infrastructure:** Hooks are registered in `.claude/`. The skills/hooks directory must be initialized first.

---

## MVP Definition

### Launch With (v1 — Sessions 1–2)

Minimum viable for the infrastructure to function as a daily driver.

- [ ] Emoji ↔ numeric zip conversion (pure lookup, ~50 lines) — foundation for everything
- [ ] 61-dimensional weight vector computation from a zip code — enables all downstream rendering
- [ ] Fitness-specific keyword dictionary (~2,500 entries: exercises, body parts, equipment, SCL names) — enables text classification
- [ ] Heuristic text classifier: input text → top-3 matching zip codes + confidence scores — the parse-and-sort core
- [ ] Design token JSON (`design-tokens.json`): 8 Color palettes, 7 Order typographies, 6 Axis gradients — single source for rendering
- [ ] CSS custom property derivation: weight vector → rendering descriptor → CSS custom properties — procedural rendering
- [ ] Hot-reload canvas at localhost:3000 (Vite + React, renders a single zip code's design tokens visually) — the feedback loop
- [ ] Canvas state persistence: `.local/canvas-state.json` (git-ignored working state) — session continuity
- [ ] `/blank-canvas` Claude Code skill — initializes workspace, loads state, runs progress dashboard
- [ ] `canvas-renderer` subagent definition — fresh context for v0-style rewrites
- [ ] PostToolUse hook: auto-apply publication standard to canvas output — art direction enforcement
- [ ] Integration tests: zip conversion, weight computation, CSS derivation — correctness guard

### Add After Validation (v1.x — Session 3)

Once the infrastructure bus is solid, the canvas UI becomes worthwhile.

- [ ] Visual canvas UI (React Flow or tldraw) — add when infrastructure is proven. Session 3+.
- [ ] `canvas-to-production.sh` — port finalized canvas elements to `cards/`, `html/`. Requires template system to exist first.
- [ ] `batch-propagate.sh` — template a design element across N zip codes. Requires canvas-to-production first.
- [ ] Git snapshot skill: commit canvas state with architecture record format — disciplined record-keeping
- [ ] Expand keyword dictionary toward full 13K entries (incrementally, starting with remaining fitness terms) — improved parse accuracy

### Future Consideration (v2+)

Defer until the infrastructure is proven and Graph Parti development begins.

- [ ] Graph Parti extraction: clean SCL-specific config into `canvas/scl/`, expose general infrastructure interface — only when the pattern is proven in Ppl±
- [ ] Card HTML template system (full interactive web components from `.md` cards) — this is Phase 4/5 scope, not canvas infrastructure
- [ ] Anatomy Explorer, City Navigator, and other interactive diagram components — Phase 4/5, use Claude.ai artifact prototyping pipeline first
- [ ] Full voice parser integration (13K-entry dictionary, natural language to zip + floor + content type) — separate Phase 4/5 system

---

## Feature Prioritization Matrix

| Feature | User Value | Implementation Cost | Priority |
|---------|------------|---------------------|----------|
| Emoji ↔ numeric zip conversion | HIGH | LOW | P1 |
| Weight vector computation | HIGH | MEDIUM | P1 |
| CSS custom property derivation | HIGH | MEDIUM | P1 |
| Design token JSON | HIGH | LOW | P1 |
| Fitness keyword dictionary (~2,500 entries) | HIGH | MEDIUM | P1 |
| Heuristic text classifier | HIGH | MEDIUM | P1 |
| Hot-reload canvas (localhost:3000) | HIGH | LOW | P1 |
| Canvas state persistence (.local/) | MEDIUM | LOW | P1 |
| `/blank-canvas` Claude Code skill | MEDIUM | LOW | P1 |
| Integration tests | HIGH | MEDIUM | P1 |
| `canvas-renderer` subagent definition | MEDIUM | LOW | P1 |
| PostToolUse art direction hook | MEDIUM | LOW | P1 |
| Visual canvas UI (React Flow/tldraw) | HIGH | HIGH | P2 |
| `canvas-to-production.sh` | HIGH | MEDIUM | P2 |
| `batch-propagate.sh` | HIGH | MEDIUM | P2 |
| Git snapshot skill | LOW | LOW | P2 |
| Full keyword dictionary (13K) | MEDIUM | HIGH | P3 |
| Graph Parti extraction | MEDIUM | HIGH | P3 |
| Card HTML template system | HIGH | HIGH | P3 |
| Interactive diagram components | HIGH | HIGH | P3 |

**Priority key:**
- P1: Must have for canvas infrastructure to function as a daily driver
- P2: Should have, unlocks the canvas UI and production migration pathway
- P3: Future consideration, Phase 4/5 or Graph Parti scope

---

## Competitor Feature Analysis

Reference tools analyzed: v0.dev, bolt.new, tldraw, React Flow, Storybook. These are the closest analogs to different subsystems of this infrastructure.

| Feature | v0.dev | bolt.new | tldraw | React Flow | Storybook | Ppl± Canvas |
|---------|--------|----------|--------|------------|-----------|-------------|
| Offline-first operation | No (cloud) | No (cloud) | Partial (SDK local) | Yes | Yes | Yes (hard constraint) |
| Domain-specific parser | No | No | No | No | No | Yes (SCL, 61-emoji + keywords) |
| Procedural CSS from structured data | No (prompt-driven) | No (prompt-driven) | No | No | Token system only | Yes (weight-vector-to-CSS) |
| Art direction enforcement | No | No | No | No | Via addon | Yes (PostToolUse hook) |
| Production migration pathway | No (throwaway) | Partial (export) | No | No | No | Yes (canvas-to-production.sh) |
| Batch templating across N artifacts | No | No | No | No | Stories as variants | Yes (batch-propagate.sh) |
| Live hot-reload preview | Yes | Yes | Yes (SDK) | Yes | Yes | Yes (Vite) |
| State persistence | Session only | Partial | Yes (file) | No | No | Yes (.local/ + git snapshots) |
| Deterministic (non-AI) classification | No | No | N/A | N/A | N/A | Yes (keyword dict + heuristics) |
| Component isolation | No | No | No | Partial | Yes | Yes (canvas-renderer subagent) |

**Key takeaway:** No existing tool combines offline-first operation, domain-specific parsing, procedural CSS derivation, and a production migration path. Each tool solves one problem well. The Ppl± canvas must solve all four because they are tightly coupled in this system.

---

## Sources

- [Compare Bolt.new vs. v0 in 2026 — SlashDot](https://slashdot.org/software/comparison/Bolt.new-vs-v0/)
- [tldraw: Infinite Canvas SDK for React](https://tldraw.dev/)
- [Node-Based UIs in React — React Flow](https://reactflow.dev)
- [Lovable vs Bolt.new vs v0: Best AI App Builder in 2026 — Particula](https://particula.tech/blog/lovable-vs-bolt-vs-v0-ai-app-builders)
- [Design Tokens That Scale in 2026 (Tailwind v4 + CSS Variables) — Mavik Labs](https://www.maviklabs.com/blog/design-tokens-tailwind-v4-2026)
- [spaCy Linguistic Features (offline NLP pipeline reference)](https://spacy.io/usage/linguistic-features)
- Project seeds: `seeds/interactive-diagrams-architecture.md`, `seeds/mobile-ui-architecture.md`, `seeds/experience-layer-blueprint.md`, `seeds/voice-parser-architecture.md`
- Project rendering specs: `middle-math/rendering/ui-weight-derivation.md`, `middle-math/rendering/progressive-disclosure.md`
- Project plan: `.planning/PROJECT.md`

---

*Feature research for: Ppl± Blank Canvas Infrastructure (offline parser + procedural rendering + Claude Code canvas environment)*
*Researched: 2026-03-13*
