# Architecture Research

**Domain:** Offline semantic parser + weight-vector rendering pipeline + Claude Code dev infrastructure
**Researched:** 2026-03-13
**Confidence:** HIGH — based entirely on first-party project documents (middle-math specs, seed blueprints, working TypeScript snippets already present in seeds)

---

## Standard Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     CANVAS LAYER (canvas/)                       │
│   Dev workspace, visual scratch surface, temp architect access   │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────────┐   │
│  │  /blank-    │  │  canvas-     │  │  PostToolUse hook:    │   │
│  │  canvas     │  │  renderer    │  │  pub-standard + art   │   │
│  │  skill      │  │  subagent    │  │  direction enforcer   │   │
│  └──────┬──────┘  └──────┬───────┘  └───────────┬───────────┘   │
│         │               │                       │               │
├─────────┴───────────────┴───────────────────────┴───────────────┤
│                     PARSER LAYER (canvas/parser/)                │
│  Input: any text (emoji zip / natural language / pasted context) │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────────┐   │
│  │  Zip        │  │  Keyword     │  │  Heuristic            │   │
│  │  Converter  │  │  Dictionary  │  │  Text Classifier      │   │
│  │  (emoji↔num)│  │  (~13K terms)│  │  (exercise detect,    │   │
│  └──────┬──────┘  └──────┬───────┘  │   body part, equip)   │   │
│         │               │           └───────────┬───────────┘   │
│         └───────────────┴───────────────────────┘               │
│                         ↓ ParseResult                           │
├─────────────────────────────────────────────────────────────────┤
│                   WEIGHT ENGINE (canvas/weights/)                │
│  Input: 4-digit numeric zip  Output: 61-value weight vector      │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────────┐   │
│  │  Primary    │  │  Affinity +  │  │  Interaction          │   │
│  │  Weight     │  │  Suppression │  │  Resolution           │   │
│  │  Seeder     │  │  Cascades    │  │  (Order>Color>Axis>   │   │
│  └──────┬──────┘  └──────┬───────┘  │   Type hierarchy)     │   │
│         │               │           └───────────┬───────────┘   │
│         └───────────────┴───────────────────────┘               │
│                         ↓ WeightVector[61]                      │
├─────────────────────────────────────────────────────────────────┤
│              RENDERING PIPELINE (canvas/rendering/)              │
│  Input: WeightVector  Output: RenderDescriptor → CSS vars        │
├─────────────────────────────────────────────────────────────────┤
│  ┌────────────┐  ┌────────────┐  ┌──────────┐  ┌────────────┐   │
│  │ Palette    │  │ Typography │  │ Layout   │  │ Tonal      │   │
│  │ Deriver    │  │ Deriver    │  │ Density  │  │ Register   │   │
│  │            │  │            │  │ Deriver  │  │ Deriver    │   │
│  └──────┬─────┘  └──────┬─────┘  └────┬─────┘  └──────┬─────┘   │
│         └──────────────┴──────────────┴───────────────┘         │
│                         ↓ 30+ CSS custom properties             │
├─────────────────────────────────────────────────────────────────┤
│              DESIGN TOKEN LAYER (canvas/tokens/)                 │
│  design-tokens.json: 8 palettes, 7 densities, 6 typographies     │
│  design-tokens.css:  CSS custom properties mapped from tokens    │
└─────────────────────────────────────────────────────────────────┘
```

---

### Component Responsibilities

| Component | Responsibility | Boundary |
|-----------|---------------|----------|
| Zip Converter | Translate emoji zip ↔ 4-digit numeric. Validate dial ranges. | Stateless pure functions. No I/O. |
| Keyword Dictionary | ~13K-entry vocabulary: 26 dial positions, 6 floors, 109 content types, 2,185 exercises. Single JSON file loaded once at init. | Read-only data. No side effects. |
| Text Classifier | Tokenize input, score each token against dictionary, fuzzy-match exercise names (Levenshtein ≤ 2), return ParseResult with confidence. | Pure function. Dictionary is injected. |
| Weight Seeder | Given a numeric zip, set +8 primary weights for the 4 active dials. | Step 1 of weight derivation only. |
| Affinity/Suppression Cascades | Per-dial affinity/suppression tables encoding all SCL rules numerically. | One file per dial category (order-weights.ts, axis-weights.ts, etc.) mirroring middle-math/weights/. |
| Interaction Resolver | Apply constraint hierarchy (Order > Color > Axis > Type): hard suppressions hold, soft weights sum and clamp to [-8, +8]. | Single merge function. Input: 4 cascade arrays. Output: one vector. |
| Palette Deriver | Map Color weight → dominant palette + accent palette + saturation value. | Reads design tokens. No direct CSS output. |
| Typography Deriver | Map Order weight + Color modifier → density, leading, header weight, body style. | Reads design tokens. No direct CSS output. |
| Layout Density Deriver | Map Order weight + Color weight → blocks-per-screen, whitespace-ratio, rest-indicator prominence. | Reads design tokens. No direct CSS output. |
| Tonal Register Deriver | Map primary Color → tonal register string (from 8 Color Context Vernacular registers). | String output only. No visual tokens. |
| RenderDescriptor Assembler | Merge all 4 deriver outputs into one RenderDescriptor JSON object per the spec in `middle-math/rendering/ui-weight-derivation.md`. | Assembler only. Does not derive. |
| CSS Var Generator | Translate RenderDescriptor → 30+ CSS custom property declarations as a string/object. | Final output stage. Design token map is injected. |
| design-tokens.json | Authoritative source for all hex values, font names, spacing units, border radii. Not computed — editorially maintained. | Static data. Only humans change this. |
| `/blank-canvas` skill | Initialize canvas workspace, load current state from `.local/`, inject full project context for a dev session. | Orchestration only. Calls scripts, not parser. |
| `canvas-renderer` subagent | Isolated context worker for v0 rewrites and iteration on canvas TSX components. Receives zip + RenderDescriptor, emits component. | Read/write to `canvas/components/`. No repo-wide writes. |
| PostToolUse hook | After any write to `canvas/`, validate publication standard and art direction compliance. Auto-flag violations. | Read-only check. Never auto-corrects. |
| `canvas-to-production.sh` | Port finalized canvas elements into `cards/`, `html/`, etc. | One-way transfer. Requires explicit invocation. |
| `batch-propagate.sh` | Template a design element across N zip codes. Uses weight engine to derive per-zip RenderDescriptors. | Calls weight engine. Writes to canvas/, not production. |

---

## Recommended Project Structure

```
canvas/
├── parser/
│   ├── index.ts                # Public parser API: parse(input) → ParseResult
│   ├── zip-converter.ts        # emojiToZip(), zipToEmoji(), isValidZip(), zipToDeck()
│   ├── tokenizer.ts            # tokenize(), stem(), removeStopwords()
│   ├── fuzzy-match.ts          # levenshtein(), fuzzyMatch()
│   ├── scorer.ts               # scoreInput() — core scoring algorithm
│   ├── router.ts               # routeFromParse() — ParseResult → URL string
│   └── vocab/
│       ├── dial-keywords.json  # 26 dial positions × keywords (Orders/Axes/Types/Colors)
│       ├── floor-keywords.json # 6 floors × keywords
│       ├── content-types.json  # 109 content types × keywords
│       └── exercises.json      # 2,185 exercises + aliases + SCL metadata
│
├── weights/
│   ├── index.ts                # Public weights API: computeVector(zip) → WeightVector
│   ├── seeder.ts               # setPrimaryWeights() — step 1
│   ├── order-weights.ts        # ⛽🐂🦋🏟🌾⚖🖼 affinity/suppression tables
│   ├── axis-weights.ts         # 🏛🔨🌹🪐⌛🐬 tables
│   ├── type-weights.ts         # 🛒🪡🍗➕➖ tables
│   ├── color-weights.ts        # ⚫🟢🔵🟣🔴🟠🟡⚪ tables
│   ├── interaction-resolver.ts # merge(), clamp(), applyHierarchy()
│   └── weight-types.ts         # WeightVector, WeightMap, DialWeight types
│
├── rendering/
│   ├── index.ts                # Public rendering API: render(zip) → RenderDescriptor
│   ├── palette-deriver.ts      # colorWeightToPalette()
│   ├── typography-deriver.ts   # orderWeightToTypography()
│   ├── layout-deriver.ts       # orderColorToLayout()
│   ├── tone-deriver.ts         # colorToTonalRegister()
│   ├── assembler.ts            # buildRenderDescriptor()
│   ├── css-vars.ts             # descriptorToCSSVars() → Record<string, string>
│   └── render-types.ts         # RenderDescriptor, PaletteSpec, TypographySpec, etc.
│
├── tokens/
│   ├── design-tokens.json      # Authoritative: palettes, fonts, spacing, radii
│   └── design-tokens.css       # Generated from JSON. Do not edit directly.
│
├── components/
│   ├── CardShell.tsx           # Outer container that applies CSS vars from RenderDescriptor
│   ├── BlockRenderer.tsx       # Renders a single workout block from markdown AST
│   └── [others as built]
│
├── scripts/
│   ├── canvas-to-production.sh # Port canvas elements to production directories
│   ├── batch-propagate.sh      # Template element across N zip codes
│   └── build-exercise-vocab.ts # Parse exercise-library.md → exercises.json
│
├── state/
│   ├── canvas-state.ts         # Current working state (zip, layer, active component)
│   └── .local/                 # Git-ignored local working state snapshots
│
├── tests/
│   ├── parser.test.ts          # Parser accuracy: worked examples from voice-parser-architecture.md
│   ├── weights.test.ts         # Weight derivation: verify ⛽🏛🪡🔵 worked example
│   ├── rendering.test.ts       # CSS output: verify palette, typography, layout per Order+Color
│   └── zip-converter.test.ts   # isValidZip(), emojiToZip(), zipToEmoji(), zipToDeck()
│
└── README.md
```

### Structure Rationale

- **`parser/`:** Fully self-contained. The dictionary vocabulary files live here as JSON — not mixed with weight logic. The scoring algorithm is a pure function that can be tested in isolation with injected dictionaries.
- **`weights/`:** One file per dial category mirrors the existing `middle-math/weights/` structure. This makes porting from seed specs to implementation a direct translation. The interaction resolver is separate because it is the hardest logic and needs its own test surface.
- **`rendering/`:** Each rendering dimension (palette, typography, layout, tone) is a separate deriver file. The assembler calls all four and merges. The CSS var generator is the final output stage and only knows about RenderDescriptor + design-tokens — it does not know about zip codes or SCL rules.
- **`tokens/`:** Design tokens are editorial, not computed. They are the one place where hex values live. Everything else derives from them.
- **`state/`:** Canvas working state (which zip is active, which layer is visible, what is selected) lives here separate from the computation engine. `.local/` is git-ignored — it is the messy working surface. Committed snapshots go in `state/` directly.

---

## Architectural Patterns

### Pattern 1: Layered Derivation Pipeline

**What:** Each stage transforms a clean input type to a clean output type. No stage knows about the previous stage's internals. The full pipeline is: `string input → ParseResult → numeric zip → WeightVector → RenderDescriptor → CSS vars`.

**When to use:** Always. This is the core pipeline. Every component in the system participates in exactly one stage of this pipeline.

**Trade-offs:** Introduces more intermediate types, but makes each stage independently testable. A bug in the CSS var generator does not require debugging the weight engine.

**Example:**
```typescript
// Each stage is a pure function. No stage imports from another stage's internals.
const parsed: ParseResult = parse("heavy pull day");
const zip: string = parsed.zipCode ?? '2123';  // fallback to default
const vector: WeightVector = computeVector(zip);
const descriptor: RenderDescriptor = buildRenderDescriptor(vector);
const cssVars: Record<string, string> = descriptorToCSSVars(descriptor, tokens);
```

### Pattern 2: Injected Dictionary

**What:** The keyword dictionary is a plain JSON data structure loaded once at initialization and injected into the scorer as a function parameter. The scorer does not import the dictionary directly.

**When to use:** Parser initialization, tests. Tests can inject smaller mock dictionaries.

**Trade-offs:** Slightly more setup boilerplate, but the scorer function is pure and testable without the full 180 KB vocabulary.

**Example:**
```typescript
// In production: load once
const dict: VocabDictionary = loadDictionary();
const result = scoreInput("heavy pull day", dict);

// In tests: inject minimal fixture
const mockDict = { orders: [{position: 2, emoji: '⛽', keywords: ['heavy', 'strength']}], ... };
const result = scoreInput("heavy", mockDict);
```

### Pattern 3: Constraint Hierarchy Encoding

**What:** Each dial's weight table encodes only that dial's opinions. The interaction resolver applies the constraint hierarchy (Order > Color > Axis > Type) as a post-processing step. Hard suppressions (≤ -6) from higher-priority dials block upward revision by lower-priority affinities.

**When to use:** Weight engine. This is the only place constraint hierarchy logic lives.

**Trade-offs:** Makes individual dial tables simpler (each table only knows its own rules), but the resolver needs to know the hierarchy. Do not replicate hierarchy logic in the dial tables — it belongs in the resolver only.

**Example:**
```typescript
// order-weights.ts: declares ⛽'s opinion on 🌋 Gutter
const STRENGTH_SUPPRESSIONS: Record<string, number> = {
  '🌋': -4,  // ⛽ pushes Gutter away, but does not hard-block
  '🪞': -5,
  // ...
};

// interaction-resolver.ts: applies hierarchy AFTER all tables are merged
function applyHierarchy(votes: DialVotes, emoji: string): number {
  // Order hard suppression at -6 or lower: lock it, no override
  if (votes.order <= -6) return clamp(votes.order, -8, -6);
  // Color hard filter at -6 or lower: same rule
  if (votes.color <= -6) return clamp(votes.color, -8, -6);
  // Soft weights: sum all four, clamp to [-8, +8]
  return clamp(votes.order + votes.color + votes.axis + votes.type, -8, 8);
}
```

### Pattern 4: RenderDescriptor as Semantic Contract

**What:** The RenderDescriptor object is a semantic description ("strong blue-gray, technical-sans, dense") not pixel values ("hex #3A4A5C, 14px"). Hex values and font names live only in `design-tokens.json`. The deriver functions output semantic descriptors. The CSS var generator maps semantic → tokens → pixels.

**When to use:** The entire rendering pipeline. This is what allows design token updates without touching derivation logic.

**Trade-offs:** One extra mapping step, but changing a palette from one blue to another requires editing only `design-tokens.json`, not any TypeScript.

### Pattern 5: Claude Code Skill as Context Loader

**What:** The `/blank-canvas` skill is not an algorithm — it is a context injection sequence. It reads current canvas state, reads relevant project docs, and presents the session context to Claude so work can begin without re-reading CLAUDE.md manually.

**When to use:** Session start. Also useful mid-session after a compaction event.

**Trade-offs:** Skill files are static prompts, not compiled code. They live in `.claude/commands/` and are invoked with `/blank-canvas`. They should be readable prose, not code-heavy.

---

## Data Flow

### Primary Pipeline: Text Input to CSS Output

```
User pastes text / speaks / types zip code
    ↓
[parser/tokenizer.ts] — split, lowercase, stem, remove stopwords
    ↓ string[]
[parser/scorer.ts] — score each token against all 3 dictionary layers
    ↓ ParseResult { zipCode, floor, contentType, confidence }
[parser/zip-converter.ts] — validate zip, confirm 4-digit numeric
    ↓ string (e.g., "2123")
[weights/seeder.ts] — set +8 primary weights for 4 active dials
    ↓ partial WeightVector
[weights/order-weights.ts + axis-weights.ts + type-weights.ts + color-weights.ts]
    ↓ 4 cascade arrays
[weights/interaction-resolver.ts] — apply hierarchy, sum soft weights, clamp
    ↓ WeightVector[61]  (one value per SCL emoji)
[rendering/palette-deriver.ts + typography-deriver.ts + layout-deriver.ts + tone-deriver.ts]
    ↓ 4 partial descriptors
[rendering/assembler.ts] — merge into RenderDescriptor
    ↓ RenderDescriptor JSON
[rendering/css-vars.ts] — map through design-tokens.json
    ↓ Record<string, string>  (30+ CSS custom properties)
Applied to CSS custom properties on the root container of the workout card
```

### Parse-and-Sort Flow (Daily Driver Use Case)

```
Jake pastes text block into canvas workspace
    ↓
PostToolUse hook triggers on canvas/state/ write
[parser/scorer.ts] — auto-classify pasted content
    ↓ ParseResult[]  (may produce multiple matches)
[canvas/state/canvas-state.ts] — tag content with zip + floor + content type
    ↓ sorted, tagged content entries
Canvas layer displays content organized by SCL address
```

### Claude Code Skill Invocation Flow

```
/blank-canvas invoked
    ↓
[.claude/commands/blank-canvas.md] — skill definition reads:
    - canvas/state/canvas-state.ts (current session state)
    - .planning/PROJECT.md (milestone context)
    - CLAUDE.md (project rules)
    - whiteboard.md (current tasks)
    ↓
Claude Code session initialized with full context
    ↓
Dev work begins → writes to canvas/components/
    ↓
PostToolUse hook fires → publication standard check
    ↓
canvas-renderer subagent available for isolated component iteration
```

### Design Token Update Flow

```
Jake edits design-tokens.json (palette change, font update)
    ↓
[scripts/build-tokens.ts] — regenerates design-tokens.css
    ↓
All CSS var outputs automatically reflect new tokens
(No TypeScript changes required — derivation logic unchanged)
```

---

## Component Boundaries (What Talks to What)

| From | To | Interface | Notes |
|------|----|-----------|-------|
| parser/scorer.ts | vocab/*.json | Import at init, inject as parameter | Dictionary is data, not behavior |
| parser/router.ts | None outside parser/ | Returns URL strings | Routing decisions stay inside parser boundary |
| weights/interaction-resolver.ts | weights/*-weights.ts | Calls each table's cascade function | Resolver owns hierarchy; tables own their own rules only |
| rendering/assembler.ts | rendering/*-deriver.ts | Calls each deriver with the weight vector | Assembler knows about all 4 derivers |
| rendering/css-vars.ts | tokens/design-tokens.json | Reads token map | CSS vars generator is the only component that reads tokens |
| canvas/components/*.tsx | rendering/css-vars.ts | Consumes CSS custom properties via className | Components do not call the weight engine directly |
| /blank-canvas skill | canvas/state/ | File reads | Skill is a static prompt, not TypeScript |
| canvas-renderer subagent | canvas/components/ | Read/write | Bounded to components only |
| PostToolUse hook | parser/scorer.ts + scl-deep/publication-standard.md | Invokes scorer for validation | Hook reads, never writes |
| batch-propagate.sh | weights/index.ts | Calls computeVector() for each zip | Shell script calling compiled TypeScript via ts-node |
| canvas-to-production.sh | cards/, html/ | File copy only | No parsing or weight computation |

**Hard boundaries (never cross):**
- `rendering/` does not import from `parser/` — the rendering layer does not know how a zip code was derived
- `weights/` does not import from `rendering/` — weight computation does not know about visual output
- `design-tokens.json` is not imported by `weights/` — weights are semantic, tokens are visual
- `canvas/components/` do not call `computeVector()` directly — they receive CSS vars already applied to the container

---

## Build Order (Phase Dependencies)

### Phase 1 — Foundation (must be complete before anything else)

1. `canvas/parser/zip-converter.ts` — Emoji/numeric conversion and validation. Zero dependencies. This is the universal addressing key the whole system references.
2. `canvas/tokens/design-tokens.json` — Palette and typography tokens. Editorial work. No code dependencies.
3. `canvas/weights/weight-types.ts` — TypeScript type definitions for WeightVector, DialWeight, WeightMap. All other weight files import these.

### Phase 2 — Core Engine (parallel once Phase 1 is done)

4. `canvas/weights/order-weights.ts` through `color-weights.ts` — Four files, independently portable from `middle-math/weights/` seed specs. Can be written in parallel.
5. `canvas/parser/vocab/dial-keywords.json` — Portable from `seeds/voice-parser-architecture.md`. Can be written in parallel with weight tables.
6. `canvas/parser/vocab/exercises.json` — Built by `canvas/scripts/build-exercise-vocab.ts` parsing `exercise-library.md`. Depends on the exercise library format but not on the weight engine.

### Phase 3 — Integration Layer (requires Phase 2)

7. `canvas/weights/interaction-resolver.ts` — Requires all four dial weight files to exist and their types to be defined.
8. `canvas/weights/index.ts` — Public API over the resolver. One-liner: `export const computeVector = (zip) => resolver.resolve(seedWeights(zip), ...cascades)`.
9. `canvas/parser/tokenizer.ts` + `fuzzy-match.ts` — Pure utilities with no external dependencies. Can go in Phase 2 but not blocking.
10. `canvas/parser/scorer.ts` — Requires tokenizer, fuzzy-match, and vocab JSON files.

### Phase 4 — Rendering Pipeline (requires Phase 3 weight engine)

11. `canvas/rendering/render-types.ts` — Type definitions for RenderDescriptor, PaletteSpec, etc.
12. `canvas/rendering/palette-deriver.ts`, `typography-deriver.ts`, `layout-deriver.ts`, `tone-deriver.ts` — Each deriver takes `WeightVector`, returns partial descriptor. Can be written in parallel once render-types.ts exists.
13. `canvas/rendering/assembler.ts` — Merges the 4 deriving outputs.
14. `canvas/rendering/css-vars.ts` — Final stage. Requires assembler and design-tokens.json.

### Phase 5 — Claude Code Infrastructure (requires Phase 3 parser + Phase 4 rendering)

15. `.claude/commands/blank-canvas.md` — Skill definition. Prose document. Can be drafted early, finalized after canvas/ structure is stable.
16. `canvas-renderer` subagent definition — Requires knowing what canvas/components/ look like.
17. PostToolUse hook — Requires parser to exist (calls scorer for validation).
18. `canvas-to-production.sh` and `batch-propagate.sh` — Require the full pipeline to be working.

### Phase 6 — Tests and Card Templates (requires all prior phases)

19. `canvas/tests/*.test.ts` — Integration tests against all worked examples in project seeds.
20. `canvas/components/CardShell.tsx`, `BlockRenderer.tsx` — HTML rendering of .md cards. Depends on CSS vars working.

---

## Anti-Patterns

### Anti-Pattern 1: Bypassing the Pipeline with Direct Design Token Reads

**What people do:** Components import `design-tokens.json` directly and pull hex values, skipping the weight vector and rendering pipeline entirely.

**Why it's wrong:** A component that hard-codes a color token has no connection to the zip code's character. All 1,680 rooms look the same. The core premise — "the zip code is a complete rendering instruction" — collapses.

**Do this instead:** Components consume CSS custom properties (`var(--ui-saturation)`, `var(--ui-palette-dominant)`) applied by `css-vars.ts` to the root container. Components never import design-tokens.json directly.

### Anti-Pattern 2: Putting Hierarchy Logic in Dial Weight Tables

**What people do:** The `order-weights.ts` file checks the Color weight before declaring its own suppression value.

**Why it's wrong:** Dial tables should be pure declarations of a single dial's opinions. Cross-dial logic belongs only in `interaction-resolver.ts`. Tables that check other tables create circular imports and make each table harder to reason about in isolation.

**Do this instead:** Each dial table returns its own opinions, unconditioned by other dials. The resolver applies hierarchy after collecting all four tables' outputs.

### Anti-Pattern 3: Making the Parser AI-Dependent

**What people do:** When a low-confidence parse occurs, call an LLM to interpret the ambiguous input.

**Why it's wrong:** The offline-first constraint is non-negotiable (`.planning/PROJECT.md`). The parser must work with zero network and zero AI dependency. An AI-dependent fallback creates a hard dependency that breaks the daily driver use case.

**Do this instead:** Low-confidence parses surface a disambiguation UI — offer the top 2-3 scored interpretations as explicit choices. Wilson reads back the parse result. The user confirms. No AI call.

### Anti-Pattern 4: Writing Canvas Components to Production Directories Directly

**What people do:** The `canvas-renderer` subagent writes finalized components directly to `web/src/components/`.

**Why it's wrong:** Canvas is a scratch surface. Production directories have different conventions, validation gates, and deployment implications. Direct writes bypass the `canvas-to-production.sh` intentional porting step.

**Do this instead:** `canvas-renderer` writes only to `canvas/components/`. When Jake decides an element is finalized, he runs `canvas-to-production.sh` to port it. The gate is intentional.

### Anti-Pattern 5: Treating the Exercise Vocab JSON as a Weight File

**What people do:** `exercises.json` declares SCL weights for each exercise (e.g., "Romanian Deadlift has axis_weight of +6 for 🔨 Functional").

**Why it's wrong:** Exercise weights are derived by the weight engine from the zip code, not stored per-exercise. Storing pre-computed weights per exercise creates a second weight system that diverges from the canonical computation.

**Do this instead:** `exercises.json` stores SCL metadata (type, axis_affinity, section, is_gold) used by the parser for routing. The weight engine derives exercise rankings at query time from the zip code's vector, not from a pre-scored list.

---

## Integration Points

### Internal Boundaries

| Boundary | Communication | Notes |
|----------|---------------|-------|
| parser/ ↔ weights/ | ParseResult.zipCode (string) | Parser outputs a zip string. Weight engine takes a zip string. The only coupling is the 4-digit numeric format. |
| weights/ ↔ rendering/ | WeightVector (typed array of 61 values) | Strong typed interface. The rendering layer consumes only this — not the intermediate cascade arrays. |
| rendering/ ↔ components/ | CSS custom properties on container element | Loose coupling. Components use `var()` references. |
| canvas/ ↔ middle-math/ | Source specification, not code import | Canvas TypeScript implements what middle-math/ seeds specify. Canvas does not import from middle-math/ at runtime. |
| canvas/ ↔ .claude/ | Skill definition files, hook definitions | Static prose/config. No code import. |
| canvas/ ↔ exercise-library.md | Build step only (build-exercise-vocab.ts) | At build time, parse the library into exercises.json. At runtime, only the JSON is used. |

### Claude Code Infrastructure Integration

| Component | Integration Pattern | Notes |
|-----------|--------------------|-|
| `/blank-canvas` skill | `.claude/commands/blank-canvas.md` — prose that reads canvas/state/ files | Skills are markdown documents, not TypeScript. They inject context into a Claude Code session. |
| `canvas-renderer` subagent | `.claude/agents/canvas-renderer.md` — scoped context definition | Subagent definition constrains writes to `canvas/components/` only. Receives zip + RenderDescriptor as input context. |
| PostToolUse hook | `.claude/hooks/post-tool-use.js` — triggers validate-card.py and pub-standard check on writes to canvas/ | Non-blocking check. Flags violations to the session output. Does not halt writes. |
| `batch-propagate.sh` | Shell script invoking `ts-node canvas/weights/index.ts` per zip | Requires `ts-node` available in the project. |

---

## Scaling Considerations

This is a local development infrastructure tool first, not a user-facing service. Scaling concerns are minimal until the canvas becomes a production rendering engine in Phase 4/5.

| Scale | Architecture Adjustments |
|-------|--------------------------|
| 1 developer (current) | Single-process Node. All computation synchronous. Simple enough. |
| Canvas becomes web service | Weight computation is stateless and fast (~1ms per zip). No caching required. Render on request. |
| 1,680 zips pre-rendered | `batch-propagate.sh` generates all 1,680 RenderDescriptors and corresponding CSS files at build time. Serves static files. No runtime weight computation needed. |
| Multi-user platform (Phase 4/5) | Weight computation moves to `/api/zip/[zipcode]/weight` (already specified in experience-layer-blueprint.md). Canvas parser becomes the voice parser client-side library. No architectural changes to the canvas layer itself. |

### Scaling Priorities

1. **First bottleneck:** Dictionary load time if exercises.json grows beyond 500 KB. Fix: compress at build time, lazy-load exercise section separately from dial keywords.
2. **Second bottleneck:** Batch-propagation runtime across 1,680 zips. Fix: parallelize with `Promise.all()` — weight computation is stateless and embarrassingly parallel.

---

## Sources

All findings are HIGH confidence, derived from first-party project documents:

- `middle-math/ARCHITECTURE.md` — Weight system architecture, rendering pipeline specification, numeric zip layer
- `middle-math/weights/weight-system-spec.md` — Octave scale, derivation formula, constraint hierarchy, worked example
- `middle-math/rendering/ui-weight-derivation.md` — 5 rendering dimensions, RenderDescriptor interface, specification contract
- `seeds/voice-parser-architecture.md` — Dictionary structure, scoring algorithm, ParseResult interface, exercise vocab format, fuzzy matching, size analysis
- `seeds/numeric-zip-system.md` — 4-digit notation, conversion TypeScript, validation logic, deck derivation
- `seeds/experience-layer-blueprint.md` — Tech stack, rendering pipeline diagram, weight-to-CSS interface
- `.planning/PROJECT.md` — Component list, canvas/ directory decision, Graph Parti abstraction boundary, offline-first constraint

---

*Architecture research for: Offline SCL parser + weight-vector rendering pipeline + Claude Code dev infrastructure (Ppl± Blank Canvas)*
*Researched: 2026-03-13*
