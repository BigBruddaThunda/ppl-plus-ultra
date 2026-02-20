# HTML Experience Layer

This directory will contain the rendered experience layer for PPL± workouts.

**Status: Phase 4/5 — Scaffold Only**

No functional HTML exists yet. This is the directory skeleton establishing architecture for the design system, component library, and floor-based navigation.

## Architecture

### design-system/
CSS design tokens and theme files organized by SCL category.

- **tokens/** — Core design tokens: colors (8 SCL colors with tonal + operational names), typography, spacing, elevation
- **orders/** — 7 CSS files, one per Order, controlling visual weight and ornament level (Tuscan = plain, Corinthian = ornate)
- **axes/** — 6 CSS files, one per Axis, controlling exercise character accents AND floor-level visual environment
- **types/** — 5 CSS files, one per Type, controlling muscle group visual identity
- **blocks/** — Block emoji visual identities for the 22 session containers
- **operators/** — 12 operator glyph accent styles
- **theme.css** — Master composition pulling everything together

### floors/
App-level content spaces based on the 6-Axis dual-layer architecture (see seeds/axis-as-app-floors.md).

- **firmitas/** — Front page, navigation hub, system map (the lobby)
- **utilitas/** — Tools, calculators, settings, utility (the workshop)
- **venustas/** — Personal library, trophy case, private space (your room)
- **gravitas/** — Challenge board, benchmarks, competition (the arena)
- **temporitas/** — Almanac, calendar, seasonal content (the sundial)
- **sociatas/** — Community, social layer, discussion (the agora)

### components/
Reusable HTML component templates.

- **card-shell.html** — Full-screen mobile card container (the building)
- **block-column.html** — Superposed block with bottom-up expansion
- **exercise-row.html** — Single exercise with ± superscript/subscript boxes
- **zip-header.html** — Zip code display + title + operator (the pediment)
- **junction-footer.html** — 🚂 bridge + 🧮 SAVE (the foundation)
- **toolbar-right.html** — Right-thumb structural controls (expand/collapse)
- **log-rail-left.html** — Left-thumb logging/checking (sets, weights)
- **abacus-nav.html** — 4-dial combination lock navigator

### assets/
Static assets: fonts, SVG icons from SCL emojis, textures (trace paper, watercolor, grid).

## Design Philosophy

See `seeds/art-direction.md` for the full aesthetic thesis.
See `seeds/superposed-order-ui.md` for the bottom-up interaction model.
See `seeds/exercise-superscript.md` for the ± row system.
See `seeds/axis-as-app-floors.md` for the 6-floor navigation architecture.

## Rendering Pipeline

```
.md card (master blueprint in cards/)
    ↓
HTML workout card (rendered here)
    ↓
User interactive session (log, check, track)
    ↓
User history written back to account
    ↓
Personal exercise database grows with use
```
