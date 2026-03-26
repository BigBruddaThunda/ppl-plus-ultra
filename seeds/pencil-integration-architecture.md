---
planted: 2026-03-25
status: SEED
phase-relevance: Phase 4/5 (template design), Phase 6/7 (refinement)
blocks: nothing — design tooling layer, does not block card generation or app build
depends-on:
  - seeds/art-direction-intaglio.md
  - seeds/experience-layer-blueprint.md
  - seeds/mobile-ui-architecture.md
  - web/src/lib/tokens.ts
  - web/src/lib/design-system.ts
  - middle-math/design-tokens.json
  - middle-math/weight-css-spec.md
connects-to:
  - seeds/negentropy-thesis.md
  - seeds/architectural-reset-direction.md
  - seeds/wiki-address-resolution-layer.md
  - seeds/claude-code-build-sequence-v2.md
  - .claude/agents/canvas-renderer.md
supersedes: nothing (first specification)
---

# Pencil Integration Architecture — The Template Design Layer

🔵🟣 — structured + precise

## One Sentence

Pencil is the visual template authoring layer that sits between the SCL design token system and the React component output, producing structured `.pen` files that Claude Code consumes via MCP to generate components that honor the intaglio art direction and weight-vector-driven CSS pipeline.

---

## Section 1 — What Pencil Does in the Stack

Pencil occupies a precise role: it is the mold maker.

The 1,680 rooms share approximately 10 template molds. A room card view. A block section. A deck grid. A navigation dial. An Operis edition layout. These are the containers that content flows into. The content itself — exercises, cues, sets, reps, zip code metadata — comes from compiled JSON in `middle-math/compiled/` and from the `.md` cards in `cards/`.

Pencil designs those molds visually on an infinite canvas inside VS Code or Cursor. The designs save as `.pen` files — JSON-based, version-controlled, committed alongside code. Claude Code reads the design via Pencil's MCP server and generates pixel-perfect React/TSX components.

This is the hollow template principle from the negentropy thesis (`seeds/negentropy-thesis.md`, Section 2) applied to the rendering layer. The `.pen` file defines the topology of the visual container. The compiled JSON fills it. Same room, different furniture. Same mold, 1,680 castings.

### What Pencil Is Not

Pencil is not a content tool. It does not:
- Generate workouts or card text (that is the card generation pipeline)
- Run batch operations across 1,680 rooms (that is the compilation engine)
- Write backend code, database schemas, or API endpoints
- Modify `middle-math/`, `cards/`, or `seeds/` (those are upstream of Pencil)
- Replace the weight-vector-to-CSS pipeline (it consumes the output of that pipeline)

Pencil is a design-time tool. It produces templates. The templates produce components. The components consume tokens. The tokens come from the bus.

---

## Section 2 — Token Flow

The critical data path — how design decisions flow from the SCL specification to pixels on screen:

```
middle-math/design-tokens.json          ← Source of truth (8 Color palettes, 7 Order scales)
       │
       ▼
web/src/lib/tokens.ts                   ← TypeScript interfaces (ColorTokens, OrderTokens)
web/src/lib/design-system.ts            ← D-Module proportions (OrderProportions, getDesignSystem())
       │
       ▼
getZipCSSVars(zip) → --ppl-* vars       ← CSS custom properties per room
       │
       ▼
Pencil style guide                      ← Pencil reads token values for design-time rendering
       │
       ▼
.pen file (visual template)             ← Designer creates the mold
       │
       ▼
Claude Code reads via MCP               ← read_canvas, get_style_guide tools
       │
       ▼
web/src/components/*.tsx                 ← Generated React component consuming --ppl-* vars
       │
       ▼
middle-math/compiled/*.json fills it    ← 1,680 room instances at runtime
```

### Token Bridge Table

| Ppl± Token Source | Property | Pencil Style Guide Target |
|---|---|---|
| `COLOR_TOKENS[color].primary` | 8 hex values | Primary color per Color mode |
| `COLOR_TOKENS[color].secondary` | 8 hex values | Secondary color per mode |
| `COLOR_TOKENS[color].background` | 8 hex values | Background color per mode |
| `COLOR_TOKENS[color].surface` | 8 hex values | Surface/card color per mode |
| `COLOR_TOKENS[color].text` | 8 hex values | Text color per mode |
| `COLOR_TOKENS[color].accent` | 8 hex values | Accent color per mode |
| `COLOR_TOKENS[color].border` | 8 hex values | Border color per mode |
| `ORDER_TOKENS[order].fontSizeBase` | 7 rem values | Base font size per Order |
| `ORDER_TOKENS[order].fontSizeDisplay` | 7 rem values | Display font size per Order |
| `ORDER_TOKENS[order].fontWeight` | 7 weights | Body font weight per Order |
| `ORDER_TOKENS[order].fontWeightDisplay` | 7 weights | Display font weight per Order |
| `ORDER_TOKENS[order].letterSpacing` | 7 em values | Letter spacing per Order |
| `ORDER_TOKENS[order].lineHeight` | 7 ratios | Line height per Order |
| `ORDER_PROPORTIONS[order].D` | 7 rem values | D-module base unit (column diameter) |
| `ORDER_PROPORTIONS[order].density` | 7 descriptors | Spacing density multiplier |
| `ORDER_PROPORTIONS[order].lineMultiplier` | 7 floats | Line weight scale (drives intaglio line density) |
| `ORDER_PROPORTIONS[order].shadowDepth` | 7 floats | Shadow intensity |

### The 56-Combination Problem

8 Colors x 7 Orders = 56 visual combinations. Pencil cannot practically maintain 56 separate style guides. The approach:

**Design at representative combinations:**
1. `⛽🔵` (Strength + Structured) — Dense, blue, high-contrast. The workhorse.
2. `🖼⚪` (Restoration + Mindful) — Airy, light, spacious. The quiet room.
3. `🏟🔴` (Performance + Intense) — Compact, red, maximum urgency. The test.
4. `🐂⚫` (Foundation + Teaching) — Clear, dark, educational. The on-ramp.
5. `🦋🟡` (Hypertrophy + Fun) — Warm, golden, exploratory. The play session.

At runtime, `getZipCSSVars()` produces the continuous interpolation from the 61-dimensional weight vector. The Pencil template handles the 5 design-time representatives; CSS custom properties handle the 56+ runtime variations.

---

## Section 3 — `.pen` File Convention

### Location

All `.pen` files live at `pencil/` in the repo root. Subdirectories mirror template categories:

```
pencil/
├── room/           — Room/card view templates
├── deck/           — Deck view templates
├── nav/            — Navigation templates
├── operis/         — Operis edition layout templates
├── onboarding/     — Onboarding flow templates
└── user/           — User profile/dashboard templates
```

### Naming

- Lowercase, hyphenated: `room-card.pen`, `block-section.pen`, `zip-dial.pen`
- One template per file
- Keep individual `.pen` files under 15-20 screens (Pencil recommendation)

### Version Control

`.pen` files are JSON-based. They commit to Git, branch with code, and appear in PRs. The same review process that governs component code governs template design. There is no separate design tool with its own version history.

---

## Section 4 — Workflow

### Prerequisites

1. Install Pencil extension in VS Code or Cursor
2. Sign up at pencil.dev for activation token
3. Claude Code subscription active (required for MCP)
4. **Launch order: open Pencil BEFORE starting Claude Code** (MCP connection requirement)

### Design Cycle

1. Open a `.pen` file in Pencil (creates one if it does not exist)
2. Design the template visually — draw, place components, set typography, apply tokens
3. Use sticky notes on canvas as AI prompts for design generation if desired
4. Save — the `.pen` file updates in the repo
5. In Claude Code: "Generate the React component from `pencil/room/room-card.pen`"
6. Claude Code calls Pencil MCP tools:
   - `read_canvas` — reads the structured layout data
   - `get_selected_frame` — reads the currently selected element
   - `get_style_guide` — reads the configured style guide tokens
7. Claude Code generates TSX to `web/src/components/[category]/[Name].tsx`
8. PostToolUse hook validates the write (art direction, token compliance)
9. Commit both the `.pen` file and the generated component together

### Iteration

Change the template in Pencil → re-run generation → the component updates. The `.pen` file is the design source of truth. The TSX is the generated output. When they diverge, regenerate from the `.pen`.

---

## Section 5 — MCP Configuration

Pencil auto-registers its MCP server when installed as a VS Code extension. No changes to `.claude/settings.json` are required.

### MCP Tools Available

| Tool | What It Does |
|------|-------------|
| `read_canvas` | Reads a `.pen` file's structured content (layout, elements, styles) |
| `get_selected_frame` | Gets the currently selected frame in the Pencil editor |
| `get_style_guide` | Reads the configured style guide (token values, color modes) |

### Compatibility

The `frontend-design@claude-plugins-official` plugin already enabled in `.claude/settings.json` is complementary — it provides general frontend design knowledge. Pencil's MCP provides project-specific design context.

### Verification

After installing Pencil:
1. Open VS Code with the extension active
2. Launch Claude Code
3. Run `/mcp` — confirm Pencil appears as connected
4. If not connected: restart VS Code, ensure Pencil opened before Claude Code

### Early Access Note

Pencil is in early access (free, March 2026). MCP tool names may change. The `pencil-designer` agent should verify available tools at session start and adapt if tool names have shifted.

---

## Section 6 — Architectural Alignment

### Negentropy Compliance

The negentropy thesis (`seeds/negentropy-thesis.md`) says the system absorbs entropy and produces order. Pencil absorbs the entropy of "ad-hoc visual decisions made in code" and produces structured, repeatable, version-controlled template designs. The same mold produces 1,680 internally consistent rooms. Visual entropy decreases.

### Directional Constraint Compliance

From `seeds/architectural-reset-direction.md`, Section 5:

1. **Does it operate on the zip code address space?** Yes. Templates render zip-addressed rooms. The room card template is the visual instantiation of a zip code.
2. **Does the constraint hierarchy govern it?** Yes. Tokens encode Order > Color > Axis > Equipment. The CSS custom property system carries the hierarchy into every pixel.
3. **Does it absorb entropy or create it?** Absorbs. Converts "no visual design process" into structured, repeatable template authoring with version-controlled artifacts.
4. **Is it the same principle at a different timescale?** Yes. The mold/fill pattern mirrors the hollow template / furnished room distinction. Pencil operates at the design-time timescale; the weight-vector pipeline operates at the runtime timescale.
5. **Does the exercise library have coverage?** N/A. Pencil is the visual layer, not the content layer.

### The 100-Year Question

Would a visual template system for the address space still make sense if the system runs for 100 years? Yes. The molds are skeleton — they define the shape of rooms, not the content. Templates can be refreshed (new art direction, new CSS techniques) while the address space and content remain unchanged. The mold is infrastructure. The content is flesh.

### Two Rendering Pipelines

The project has two component pipelines. They do not overlap:

| Pipeline | Agent | Output Path | Technology | Purpose |
|----------|-------|-------------|-----------|---------|
| Canvas | `canvas-renderer` | `canvas/components/` | Vite, standalone HTML/TSX | Standalone rendering artifacts, weight-to-CSS bridge |
| Web (Pencil) | `pencil-designer` | `web/src/components/` | Next.js, React/TSX | Application components consumed by the web app |

The `canvas/` layer is the computational rendering engine. The `web/` layer is the user-facing application. Pencil operates on the `web/` layer only.

---

## Section 7 — Template Inventory

10 template molds, ordered by priority:

| # | Template | `.pen` Path | Maps To (Existing Component) | Priority |
|---|----------|------------|------------------------------|----------|
| 1 | Room Card View | `pencil/room/room-card.pen` | `web/src/components/room/WorkoutCard.tsx`, `RoomContent.tsx`, `RoomShell.tsx` | P0 |
| 2 | Block Section | `pencil/room/block-section.pen` | `web/src/components/room/BlockSection.tsx` | P0 |
| 3 | Room Header | `pencil/room/room-header.pen` | `web/src/components/room/RoomHeader.tsx` | P1 |
| 4 | ZipDial Navigation | `pencil/nav/zip-dial.pen` | `web/src/components/nav/ZipDial.tsx`, `DialPanel.tsx` | P1 |
| 5 | Deck Detail | `pencil/deck/deck-detail.pen` | `web/src/app/deck/[number]/page.tsx` | P1 |
| 6 | Deck Grid | `pencil/deck/deck-grid.pen` | Homepage deck overview section | P2 |
| 7 | Operis Edition | `pencil/operis/operis-edition.pen` | `web/src/app/operis/[date]/page.tsx` | P2 |
| 8 | Homepage / TodayHero | `pencil/room/today-hero.pen` | `web/src/app/page.tsx` (TodayHero section) | P2 |
| 9 | Onboarding Wizard | `pencil/onboarding/onboarding-wizard.pen` | `web/src/app/onboarding/page.tsx` | P3 |
| 10 | User Dashboard | `pencil/user/user-dashboard.pen` | `web/src/app/me/page.tsx`, `/me/library`, `/me/history` | P3 |

Templates 1-4 already have React components in `web/src/components/`. Pencil designs the visual refinement (applying intaglio art direction, D-module proportions, Color palette depth); Claude Code regenerates the component from the `.pen` canvas. Templates 5-10 have page-level implementations but may need dedicated template components extracted.

### P0 First Session Plan

When Pencil is installed, the first session should:

1. Install Pencil extension, verify MCP connection
2. Configure Pencil style guide with the 5 representative token sets (Section 2)
3. Design `pencil/room/room-card.pen` — the core experience
4. Generate the updated `WorkoutCard.tsx` from the canvas
5. Verify the component renders correctly with compiled JSON data
6. Design `pencil/room/block-section.pen` — blocks compose the room
7. Generate the updated `BlockSection.tsx`
8. Commit both `.pen` files and both generated components

This gives the visual foundation. All other templates build on the room card and block section patterns.

---

🧮
