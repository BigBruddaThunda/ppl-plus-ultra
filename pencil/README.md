# Pencil — Ppl± Template Design Layer

This directory holds `.pen` files — Pencil.dev visual templates that Claude Code reads via MCP to generate React components.

---

## What This Directory Is

Pencil is the mold maker. The 1,680 rooms share approximately 10 template molds. Pencil designs those molds visually on an infinite canvas; Claude Code reads the structured design via MCP tools and generates pixel-perfect React/TSX code. The compiled JSON from `middle-math/compiled/` fills the mold at runtime.

Pencil is not a content tool. It does not generate workouts, write card text, or run batch operations. It designs the visual containers that content flows into.

---

## Directory Structure

```
pencil/
├── room/           — Room/card view templates (WorkoutCard, BlockSection, RoomHeader)
├── deck/           — Deck view templates (42-deck grid, 40-card detail)
├── nav/            — Navigation templates (ZipDial, Breadcrumb)
├── operis/         — Operis edition layout templates
├── onboarding/     — Onboarding flow templates
└── user/           — User profile/dashboard templates
```

---

## Naming Convention

- Filename: lowercase, hyphenated, `.pen` extension
- Examples: `room-card.pen`, `block-section.pen`, `zip-dial.pen`
- One template per file
- Keep individual `.pen` files under 15-20 screens

---

## Style Guide Configuration

Pencil's style guide must consume the Ppl± design token system:

| Token Source | What It Provides |
|-------------|-----------------|
| `middle-math/design-tokens.json` | 8 Color palettes (primary, secondary, background, surface, text, accent, border) |
| `web/src/lib/tokens.ts` | TypeScript ColorTokens and OrderTokens interfaces |
| `web/src/lib/design-system.ts` | 7 Order D-module proportions (column diameter, density, line multiplier, shadow depth) |

Components generated from `.pen` files must consume `--ppl-*` CSS custom properties only. Never hardcode hex or rgb color values.

---

## Art Direction

All templates follow the intaglio/banknote engraving aesthetic defined in `seeds/art-direction-intaglio.md`:

- Backgrounds: fine hatching patterns (CSS repeating-linear-gradient or SVG), not solid fills
- Lines: high-contrast linework, not soft gradients or blurs
- Borders: guilloche-style (complex interlocking curves or repeating geometric motifs)
- Typography: serif or monospaced typeface (never rounded sans-serif)
- No flat color fills on structural elements — texture is the default

---

## Workflow

1. Open Pencil in VS Code/Cursor (must open BEFORE starting Claude Code for MCP connection)
2. Design a template visually on the canvas
3. Save the `.pen` file to the appropriate subdirectory
4. In Claude Code: ask to generate the React component from the `.pen` template
5. Claude Code reads the canvas via Pencil MCP tools (`read_canvas`, `get_style_guide`)
6. Claude Code generates TSX to `web/src/components/` honoring art direction constraints
7. The component consumes `--ppl-*` CSS vars from `getZipCSSVars()` and `getDesignSystem()`
8. Compiled JSON from `middle-math/compiled/` populates the component at runtime

---

## What Lives Here vs. What Does Not

| Lives in `pencil/` | Does NOT live in `pencil/` |
|-------------------|--------------------------|
| `.pen` template files | Generated React/TSX code (goes to `web/src/components/`) |
| This README | Workout card content (lives in `cards/`) |
| `.gitkeep` stubs | Design tokens (lives in `middle-math/` and `web/src/lib/`) |

---

## Agent

The `pencil-designer` agent (`.claude/agents/pencil-designer.md`) reads `.pen` files and generates components. It is scoped to `web/src/components/` writes only.

The `canvas-renderer` agent (`.claude/agents/canvas-renderer.md`) is a separate agent scoped to `canvas/components/`. Do not confuse the two.

---

## Architecture Reference

Full specification: `seeds/pencil-integration-architecture.md`
