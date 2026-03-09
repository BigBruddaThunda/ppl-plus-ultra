---
title: Archideck Color Architecture — The D-Module Rendering System
status: SEED
planted: 2026-03-09
category: experience-layer
phase-relevance: Phase 4/5 (Design System + HTML), Phase 6 (Personalization)
blocks: nothing currently — foundational design system architecture
depends-on: middle-math/design-tokens.json, middle-math/weight-css-spec.md, seeds/elevator-architecture.md, seeds/experience-layer-blueprint.md, seeds/abacus-architecture.md, seeds/digital-city-architecture.md, scl-deep/color-context-vernacular.md, scl-deep/emoji-macros.md
connects-to: seeds/mobile-ui-architecture.md, seeds/html-rendering-pipeline.md, middle-math/rendering/ui-weight-derivation.md, middle-math/rendering/progressive-disclosure.md
supersedes: nothing (first specification — extends design-tokens.json and weight-css-spec.md)
---

# Archideck Color Architecture — The D-Module Rendering System

## Thesis

The Ppl± UI renders like a hand-drafted architectural elevation. Every proportion, spacing value, font size, border weight, shadow depth, and color temperature derives from a single base measurement — D, the column diameter — modulated by the classical order system that already names the 7 Ppl± Orders. The screen is not a web page. It is an architectural drawing where line weights communicate depth, where intercolumniation governs rhythm, where the superposition of orders creates vertical hierarchy, and where color follows the polychromy traditions of the buildings being drawn.

The 61 SCL emojis are not just workout parameters. They are a complete architectural specification. Each zip code produces a unique convergence of building, floor, wing, and room — and that convergence has a visual identity as specific as the facade of a building in a traditional city. The D-module system makes that identity calculable.

---

## Part I — The Module: D (Diameter)

### The Classical Principle

In classical architecture, the column's lower diameter is the module from which every other measurement in the building derives. Vitruvius established this in *De Architectura* (c. 15 BCE). Vignola formalized it in *Regola delli cinque ordini d'architettura* (1562). Palladio refined it in *I Quattro Libri dell'Architettura* (1570).

The principle: one measurement generates the entire building. The column diameter (D) is that measurement. The column height is a multiple of D. The entablature is a fraction of D. The intercolumniation (space between columns) is a multiple of D. The base, the capital, the pedestal, the cornice — all expressible as ratios of D.

This is not decoration. It is structural mathematics. A building whose proportions derive from a single module reads as harmonious because every part relates to every other part through a common ancestor. The eye perceives this even when the mind does not calculate it.

### D in Ppl±

In Ppl±, **D is the base font size of the room.** It is the CSS `font-size` on the room's root element. Currently this lives in `design-tokens.json` as the Order's `fontSizeBase`. Every other measurement in the room — spacing, border width, padding, margin, line height, header size, icon size, shadow offset — is a ratio of D.

```css
/* D is set by the active Order */
--ppl-D: 1rem;       /* 🐂 Foundation, 🦋 Hypertrophy, 🌾 Full Body */
--ppl-D: 1rem;       /* ⛽ Strength (same base, different ratios) */
--ppl-D: 1.125rem;   /* 🏟 Performance (enlarged — the test needs visibility) */
--ppl-D: 0.9375rem;  /* ⚖ Balance (tightened — precision requires detail) */
--ppl-D: 1.0625rem;  /* 🖼 Restoration (gentle enlargement — recovery is unhurried) */
```

One variable. Everything else is a ratio of that variable. Change D and the entire room rescales proportionally — like changing the column diameter of a building.

---

## Part II — The Seven Orders as Architectural Systems

### The Canonical Column Ratios

Vignola's five classical orders established column-height-to-diameter ratios. Ppl± extends this to 7 by adding the Vitruvian and Palladian orders — already named in the elevator architecture. Each Order is a complete proportional system.

| Ppl± Order | Classical Order | Column Height (×D) | Entablature (×D) | Character | Intercolumniation |
|------------|----------------|---------------------|-------------------|-----------|--------------------|
| 🐂 Foundation | **Tuscan** | 7D | 1.75D | Simplest. Unfluted shaft. Minimal base. Patient, unadorned. | 4D (Araeostyle — widest) |
| ⛽ Strength | **Doric** | 8D | 2D | Sturdy, powerful, no base. Triglyphs and metopes. Muscular. | 2.75D (Diastyle-Eustyle) |
| 🦋 Hypertrophy | **Ionic** | 9D | 2.25D | Voluted capitals. Scroll ornament. Moderate richness. | 2.25D (Eustyle — ideal) |
| 🏟 Performance | **Corinthian** | 10D | 2.5D | Acanthus-leaf capitals. Tallest, most ornate. Maximum expression. | 2D (Systyle — tightest classic) |
| 🌾 Full Body | **Composite** | 10D | 2.5D | Combines Ionic volutes + Corinthian leaves. Integration. | 2.25D (Eustyle) |
| ⚖ Balance | **Vitruvian** | 8.5D | 2D | Vitruvius's ideal human proportions. Bilateral symmetry. Corrective. | 2.25D (Eustyle — balanced) |
| 🖼 Restoration | **Palladian** | 9.5D | 2.25D | Palladio's villa proportions. Harmonious room ratios. Serene. | 3D (Diastyle — open, airy) |

### What the Ratios Mean for UI

The column-height-to-diameter ratio translates directly to the **typographic scale multiplier** — how large headers are relative to body text.

```css
/* Column Height Ratio → Display Font Size */
--ppl-display-ratio: 7;     /* 🐂 Tuscan: 1.75rem display (7 × 0.25rem base unit) */
--ppl-display-ratio: 8;     /* ⛽ Doric: 2rem display */
--ppl-display-ratio: 9;     /* 🦋 Ionic: 1.875rem ≈ 2.25rem (9 × 0.25) */
--ppl-display-ratio: 10;    /* 🏟 Corinthian: 2.5rem display */
--ppl-display-ratio: 10;    /* 🌾 Composite: 2.5rem display */
--ppl-display-ratio: 8.5;   /* ⚖ Vitruvian: 1.625rem display */
--ppl-display-ratio: 9.5;   /* 🖼 Palladian: 1.75rem display */
```

The entablature ratio becomes the **section header proportion** — the height of block headers (♨️ Warm-Up, 🧈 Bread & Butter, etc.) relative to body text. At 1.75D for Tuscan, the headers are modest. At 2.5D for Corinthian, the headers are commanding.

### Intercolumniation → Spacing System

The five classical intercolumniation types define column spacing. In Ppl±, intercolumniation is the **horizontal rhythm** — the space between content blocks, between exercise entries, between the tree-notation branches.

| Classical Name | Spacing (×D) | Ppl± Usage | Character |
|----------------|-------------|------------|-----------|
| **Pycnostyle** | 1.5D | 🔴 Intense, 🏟 Performance | Tightest. Dense. Urgent. |
| **Systyle** | 2D | ⛽ Strength, ⚖ Balance | Compact. Muscular spacing. |
| **Eustyle** | 2.25D | 🦋 Hypertrophy, 🌾 Full Body | Ideal. The "beautiful spacing." |
| **Diastyle** | 3D | 🖼 Restoration, ⚪ Mindful | Open. Airy. Breath between elements. |
| **Araeostyle** | 4D | 🐂 Foundation (teaching mode) | Widest. Maximum room for learning. |

```css
/* Intercolumniation applied to block spacing */
--ppl-intercolumniation: calc(var(--ppl-D) * 2.25);  /* Default: Eustyle */

/* Order overrides */
.order-foundation    { --ppl-intercolumniation: calc(var(--ppl-D) * 4); }
.order-strength      { --ppl-intercolumniation: calc(var(--ppl-D) * 2); }
.order-hypertrophy   { --ppl-intercolumniation: calc(var(--ppl-D) * 2.25); }
.order-performance   { --ppl-intercolumniation: calc(var(--ppl-D) * 1.5); }
.order-fullbody      { --ppl-intercolumniation: calc(var(--ppl-D) * 2.25); }
.order-balance       { --ppl-intercolumniation: calc(var(--ppl-D) * 2.25); }
.order-restoration   { --ppl-intercolumniation: calc(var(--ppl-D) * 3); }
```

---

## Part III — The Superposition of Orders

### The Classical Principle

In multi-story classical buildings, orders are stacked vertically — the **superposition of orders.** The Colosseum demonstrates this canonically:

- **Ground level:** Tuscan/Doric (strongest, sturdiest)
- **Second level:** Ionic (moderate)
- **Third level:** Corinthian (lightest, most ornate)
- **Attic:** Pilasters (minimal)

The principle: heavier orders support lighter orders. Structural weight decreases as you ascend. Visual ornamentation increases.

### Superposition in the Floor Stack

The Ppl± floor stack already follows the piano nobile model. Superposition adds the Order-gradient to vertical navigation:

```
🪐 Penthouse  (Gravitas)    — Corinthian: ornate, deep, richly detailed
🌹 4th Floor  (Venustas)    — Ionic: refined, graceful proportions
🐬 3rd Floor  (Sociatas)    — Composite: integrated, community warmth
⌛ 2nd Floor  (Temporitas)  — Vitruvian: precise, measured, calibrated
🏛 Piano Nobile (Firmitas)  — Doric: strong arrival, the noble floor
🔨 Ground     (Utilitas)    — Tuscan: functional, unadorned utility
```

**Implementation:** When scrolling between floors, the CSS custom properties morph. The font weight lightens as you ascend. The spacing opens. The border ornamentation increases. The floor's Axis weight modulates the Order's base proportions — and the superposition gradient provides the vertical rhythm.

```css
/* Superposition modifiers applied per floor */
.floor-ground    { --ppl-superposition: 1.0; }  /* Tuscan — heaviest */
.floor-noble     { --ppl-superposition: 0.85; } /* Doric */
.floor-second    { --ppl-superposition: 0.7; }  /* Vitruvian */
.floor-third     { --ppl-superposition: 0.55; } /* Composite */
.floor-fourth    { --ppl-superposition: 0.4; }  /* Ionic */
.floor-penthouse { --ppl-superposition: 0.25; } /* Corinthian — lightest */

/* Font weight modulated by superposition */
--ppl-floor-font-weight: calc(
  var(--ppl-weight-font-weight) * var(--ppl-superposition) +
  (1 - var(--ppl-superposition)) * 300
);
```

---

## Part IV — Line Weights as Architectural Drawing

### The Draftsman's Pen

Architectural drawings communicate depth through line weight. A heavy line means "this is cut." A medium line means "this is an edge in elevation." A light line means "this is behind the section plane." A hairline means "this is dimension or annotation."

The ISO pen standard (from the Rapidograph era) establishes a geometric progression:

| Pen | Width | Architectural Use | Ppl± UI Equivalent |
|-----|-------|-------------------|---------------------|
| 0.13mm | Hairline | Dimension lines, hatching | Grid lines, dividers |
| 0.18mm | Fine | Annotation, text leaders | Helper text, meta labels |
| 0.25mm | Light | Object edges behind cut | Secondary borders, inactive states |
| 0.35mm | Medium | Object edges in elevation | Content borders, card edges |
| 0.50mm | Bold | Section cut edges | Block separators (═══), active states |
| 0.70mm | Heavy | Primary section cuts | Headers, primary dividers |
| 1.00mm | Extra Heavy | Title block borders, site boundaries | Room boundary, Order header |

### Line Weight as CSS Border System

```css
/* Line weight tokens — all ratios of D */
--ppl-line-hairline: calc(var(--ppl-D) * 0.0625);   /* 1px at 16px base */
--ppl-line-fine:     calc(var(--ppl-D) * 0.075);     /* 1.2px */
--ppl-line-light:    calc(var(--ppl-D) * 0.09375);   /* 1.5px */
--ppl-line-medium:   calc(var(--ppl-D) * 0.125);     /* 2px */
--ppl-line-bold:     calc(var(--ppl-D) * 0.1875);    /* 3px */
--ppl-line-heavy:    calc(var(--ppl-D) * 0.25);      /* 4px */
--ppl-line-boundary: calc(var(--ppl-D) * 0.375);     /* 6px */

/* Application */
.block-separator { border-top: var(--ppl-line-bold) solid var(--ppl-theme-border); }
.exercise-row    { border-bottom: var(--ppl-line-hairline) solid var(--ppl-theme-border); }
.room-header     { border-bottom: var(--ppl-line-heavy) solid var(--ppl-theme-primary); }
.tree-branch     { border-left: var(--ppl-line-medium) solid var(--ppl-theme-accent); }
```

### Order Modulates Line Weight

Heavier Orders produce heavier line weights. The drawing reads denser.

```css
/* Line weight multiplier per Order */
.order-foundation   { --ppl-line-multiplier: 0.8; }   /* Tuscan: lighter lines */
.order-strength     { --ppl-line-multiplier: 1.3; }   /* Doric: bold, assertive */
.order-hypertrophy  { --ppl-line-multiplier: 1.0; }   /* Ionic: balanced */
.order-performance  { --ppl-line-multiplier: 1.5; }   /* Corinthian: maximum */
.order-fullbody     { --ppl-line-multiplier: 1.0; }   /* Composite: integrated */
.order-balance      { --ppl-line-multiplier: 1.1; }   /* Vitruvian: precise */
.order-restoration  { --ppl-line-multiplier: 0.6; }   /* Palladian: gossamer */
```

---

## Part V — The 61-Emoji Palette System

### From Abacus Pairings Outward

The system builds color from the inside out. Start with the Order × Axis intersection (the abacus pairing — which deck you're in). That gives you the architectural identity. Then layer Type (wing character), Color (room furnishing), Operator (action verb), and Blocks (room containers). Each layer adds or modulates the palette.

### Layer 0 — Order: The Building Material

Each Order is a building made of a specific material. The material determines the base color temperature and texture feel.

| Order | Classical Material | Base Temperature | Texture Quality | Shadow Character |
|-------|-------------------|------------------|-----------------|------------------|
| 🐂 Foundation (Tuscan) | Rough-hewn travertine | Warm neutral | Porous, matte | Soft, diffused |
| ⛽ Strength (Doric) | Pentelic marble | Cool neutral | Dense, polished | Sharp, defined |
| 🦋 Hypertrophy (Ionic) | Carrara marble | Warm white | Smooth, veined | Medium, directional |
| 🏟 Performance (Corinthian) | White marble + gilding | Bright neutral | Mirror-polished | High contrast, theatrical |
| 🌾 Full Body (Composite) | Sandstone + terracotta | Warm earth | Textured, layered | Organic, integrated |
| ⚖ Balance (Vitruvian) | Limestone | True neutral | Fine-grained | Geometrically precise |
| 🖼 Restoration (Palladian) | Stucco + fresco | Warm cream | Chalky, soft | Almost none, flat |

```css
/* Order material tones — the ambient canvas */
.order-foundation   { --ppl-material-hue: 35;  --ppl-material-sat: 12%; --ppl-material-warmth: 0.6; }
.order-strength     { --ppl-material-hue: 220; --ppl-material-sat: 5%;  --ppl-material-warmth: 0.3; }
.order-hypertrophy  { --ppl-material-hue: 30;  --ppl-material-sat: 8%;  --ppl-material-warmth: 0.5; }
.order-performance  { --ppl-material-hue: 0;   --ppl-material-sat: 0%;  --ppl-material-warmth: 0.5; }
.order-fullbody     { --ppl-material-hue: 25;  --ppl-material-sat: 18%; --ppl-material-warmth: 0.7; }
.order-balance      { --ppl-material-hue: 45;  --ppl-material-sat: 6%;  --ppl-material-warmth: 0.5; }
.order-restoration  { --ppl-material-hue: 40;  --ppl-material-sat: 15%; --ppl-material-warmth: 0.8; }
```

### Layer 1 — Axis: The Floor Atmosphere

Each Axis/floor contributes a tonal atmosphere that shifts the material base.

| Axis | Atmosphere | Shift |
|------|-----------|-------|
| 🏛 Firmitas | Grand hall, high ceiling | Brightness +10%, formality |
| 🔨 Utilitas | Workshop, utility corridor | Saturation -15%, pragmatic |
| 🌹 Venustas | Gallery, curated light | Warmth +15%, richness |
| 🪐 Gravitas | Archive, deep interior | Darkness +20%, weight |
| ⌛ Temporitas | Clock tower, fenestrated | Blue shift +10%, precision |
| 🐬 Sociatas | Piazza, open-air | Warmth +10%, openness |

```css
/* Axis atmosphere modifiers */
.axis-firmitas    { --ppl-atmos-brightness: 1.1;  --ppl-atmos-hue-shift: 0; }
.axis-utilitas    { --ppl-atmos-brightness: 0.95; --ppl-atmos-hue-shift: 0;  --ppl-atmos-sat-mult: 0.85; }
.axis-venustas    { --ppl-atmos-brightness: 1.0;  --ppl-atmos-hue-shift: 5;  --ppl-atmos-warmth: 0.15; }
.axis-gravitas    { --ppl-atmos-brightness: 0.8;  --ppl-atmos-hue-shift: 0; }
.axis-temporitas  { --ppl-atmos-brightness: 1.0;  --ppl-atmos-hue-shift: -10; }
.axis-sociatas    { --ppl-atmos-brightness: 1.05; --ppl-atmos-hue-shift: 5;  --ppl-atmos-warmth: 0.1; }
```

### Layer 2 — Color: The Room Furnishing

The 8 Colors are the room's furnishing and lighting. This is where the primary palette (from `design-tokens.json`) applies. The Color palette is absolute — it overrides the ambient canvas with its own identity. But the Order material and Axis atmosphere modulate it.

**The Color × Order saturation interaction** (already specified in weight-css-spec.md):

| Interaction | Saturation | Example |
|-------------|-----------|---------|
| 🔴 Intense + ⛽ Strength | 0.9 | Vivid, high energy, maximum contrast |
| ⚪ Mindful + 🖼 Restoration | 0.2 | Near-monochrome, calm, barely-there |
| 🟡 Fun + 🦋 Hypertrophy | 0.75 | Bright, playful, volume-is-visible |
| ⚫ Teaching + any Order | 0.05 | Desaturated, focus on content, not color |
| 🟣 Technical + 🏟 Performance | 0.85 | Deep, precise, the GOLD lane |
| 🟢 Bodyweight + 🐂 Foundation | 0.5 | Natural, steady, outdoor light |

**The palette formula:**

```
final_hue = color.primary_hue + order.material_hue_shift + axis.atmos_hue_shift
final_sat = color.saturation × order.sat_multiplier × axis.sat_multiplier
final_light = color.base_lightness × order.material_warmth × axis.brightness
```

### Layer 3 — Type: The Wing Accent

Types add a secondary accent color that highlights the active muscle group. These are not full palette overrides — they are accent touches, like the colored trim on an otherwise neutral hallway.

| Type | Accent Association | Physiological Basis |
|------|-------------------|---------------------|
| 🛒 Push | Warm red-amber | Chest, front delts — anterior chain, warm |
| 🪡 Pull | Cool blue-steel | Back, lats — posterior chain, cool |
| 🍗 Legs | Earth brown-green | Quads, glutes — ground contact, earth |
| ➕ Plus | Gold-bronze | Full body power, core — heat of effort |
| ➖ Ultra | Sky blue-silver | Cardiovascular — air, oxygen, breath |

```css
/* Type accent overlay — subtle, 10-15% influence on accent color */
--ppl-type-accent-push:  hsl(15, 60%, 50%);   /* warm amber */
--ppl-type-accent-pull:  hsl(210, 40%, 55%);   /* steel blue */
--ppl-type-accent-legs:  hsl(85, 35%, 42%);    /* earth green */
--ppl-type-accent-plus:  hsl(42, 70%, 52%);    /* bronze gold */
--ppl-type-accent-ultra: hsl(200, 50%, 60%);   /* sky silver */
```

### Layer 4 — Operator: The Action Tint

The 12 operators carry a subtle tonal inflection — a color of intent that tints the room's header and intention block (🎯).

| Operator | Tint | Rationale |
|----------|------|-----------|
| 📍 pono | Slate | Positioning: neutral, geometric |
| 🧲 capio | Copper | Receiving: warm, magnetic |
| 🧸 fero | Sienna | Carrying: earth, load-bearing |
| 👀 specio | Silver | Observing: reflective, mirror |
| 🥨 tendo | Vermillion | Extending: stretch, reach |
| 🤌 facio | Iron | Executing: dense, industrial |
| 🚀 mitto | Fire-orange | Launching: explosive, kinetic |
| 🦢 plico | Orchid | Folding: layered, complex |
| 🪵 teneo | Oak | Holding: enduring, grain |
| 🐋 duco | Deep teal | Orchestrating: ocean, depth |
| ✒️ grapho | Ink | Writing: precise, permanent |
| 🦉 logos | Ivory | Reasoning: parchment, study |

### Layer 5 — Blocks: The Room Interior

The 22 blocks + SAVE have individual color associations for their header emojis and container borders. These are not full palette overrides — they are accent markers that identify which block you're in.

**Operational function → color family:**

| Function | Blocks | Color Family |
|----------|--------|-------------|
| Orientation | ♨️ 🎯 | Warm amber (arrival, warmth) |
| Access | 🔢 🫀 ▶️ ♟️ 🪜 | Cool neutral (preparation) |
| Transformation | 🧈 🎼 🌎 🎱 🌋 🪞 🗿 🛠 🧩 🏖 🏗 | The Color's primary — this IS the workout |
| Retention | 🪫 🧬 🚂 🔠 | Muted warm (winding down) |
| System | 🧮 SAVE | Neutral (the record) |

---

## Part VI — Shadow and Light as Architectural Rendering

### Shade and Shadow in Classical Drawing

Architectural drawings follow strict conventions for shade and shadow:

- **Light source:** Upper left at 45° (the convention since Beaux-Arts tradition)
- **Shade:** The surface facing away from light (inherent darkness)
- **Shadow:** The projection of an object onto another surface (cast darkness)
- **Poché:** Solid areas filled with dark tone (walls in plan, cut sections)

### UI Shadows Follow Architectural Rules

```css
/* Shadow system — light source upper-left at 45° */
/* Shadow offset: always down-right (positive x, positive y) */
/* Shadow depth increases with elevation (floor level) */

--ppl-shadow-ground:    0px 1px 2px rgba(0,0,0, calc(0.05 * var(--ppl-weight-contrast)));
--ppl-shadow-noble:     2px 2px 4px rgba(0,0,0, calc(0.08 * var(--ppl-weight-contrast)));
--ppl-shadow-second:    3px 3px 6px rgba(0,0,0, calc(0.10 * var(--ppl-weight-contrast)));
--ppl-shadow-third:     4px 4px 8px rgba(0,0,0, calc(0.12 * var(--ppl-weight-contrast)));
--ppl-shadow-fourth:    5px 5px 10px rgba(0,0,0, calc(0.14 * var(--ppl-weight-contrast)));
--ppl-shadow-penthouse: 6px 6px 12px rgba(0,0,0, calc(0.16 * var(--ppl-weight-contrast)));
```

**Order modulates shadow depth:**

| Order | Shadow Character | Implementation |
|-------|-----------------|----------------|
| 🐂 Foundation (Tuscan) | Soft, diffused shadows. Forgiving. | Large blur radius, low opacity |
| ⛽ Strength (Doric) | Sharp, defined shadows. Assertive. | Small blur, high opacity |
| 🦋 Hypertrophy (Ionic) | Medium, directional. Sculpted. | Balanced blur and opacity |
| 🏟 Performance (Corinthian) | High contrast, theatrical. Spotlight. | Minimal blur, maximum opacity |
| 🌾 Full Body (Composite) | Organic, layered. Multiple light sources. | Dual shadow layers |
| ⚖ Balance (Vitruvian) | Geometrically precise. Even. | Equal x/y offset, clean edge |
| 🖼 Restoration (Palladian) | Almost none. Flat, fresco-like. | Near-zero opacity |

**Color modulates shadow hue:**

Shadows are not pure black. In real architecture, shadows take on the complementary color of the ambient light. In Ppl±:

```css
/* Shadow color follows the Color's complement */
.color-teaching   { --ppl-shadow-hue: 0;   --ppl-shadow-sat: 0%; }    /* Pure gray */
.color-bodyweight { --ppl-shadow-hue: 215; --ppl-shadow-sat: 10%; }   /* Blue-gray (complement of green) */
.color-structured { --ppl-shadow-hue: 30;  --ppl-shadow-sat: 8%; }    /* Warm gray (complement of blue) */
.color-technical  { --ppl-shadow-hue: 55;  --ppl-shadow-sat: 8%; }    /* Yellow-gray (complement of purple) */
.color-intense    { --ppl-shadow-hue: 180; --ppl-shadow-sat: 10%; }   /* Teal shadow (complement of red) */
.color-circuit    { --ppl-shadow-hue: 210; --ppl-shadow-sat: 8%; }    /* Blue shadow (complement of orange) */
.color-fun        { --ppl-shadow-hue: 240; --ppl-shadow-sat: 8%; }    /* Violet shadow (complement of yellow) */
.color-mindful    { --ppl-shadow-hue: 0;   --ppl-shadow-sat: 0%; }    /* No color in shadow */
```

---

## Part VII — Typography as Architectural Lettering

### Classical Lettering Standards

Architectural lettering follows rules as strict as column proportions:

- **Stroke width** is proportional to letter height
- **Letter spacing** increases with scale (display text is tracked wider)
- **Weight hierarchy** mirrors structural hierarchy: heavier for load-bearing elements
- **Baseline grid** is absolute — text aligns to an invisible ruled sheet

### The Ppl± Type System Extended

Each Order already has font parameters in `design-tokens.json`. The D-module system formalizes these as ratios:

```css
/* Typography as ratios of D */
--ppl-type-body:     calc(var(--ppl-D) * 1);       /* 1D = body text */
--ppl-type-small:    calc(var(--ppl-D) * 0.875);   /* 7/8 D = meta text */
--ppl-type-caption:  calc(var(--ppl-D) * 0.75);    /* 3/4 D = captions */
--ppl-type-h4:       calc(var(--ppl-D) * 1.125);   /* 9/8 D = sub-headers */
--ppl-type-h3:       calc(var(--ppl-D) * 1.25);    /* 5/4 D = section heads */
--ppl-type-h2:       calc(var(--ppl-D) * 1.5);     /* 3/2 D = block headers */
--ppl-type-h1:       calc(var(--ppl-D) * var(--ppl-column-ratio) * 0.2);  /* Display: Order's column ratio */
--ppl-type-display:  calc(var(--ppl-D) * var(--ppl-column-ratio) * 0.25); /* Hero: Order's column ratio */

/* Column ratio drives display scaling */
.order-foundation   { --ppl-column-ratio: 7; }   /* Tuscan: modest display */
.order-strength     { --ppl-column-ratio: 8; }   /* Doric: taller display */
.order-hypertrophy  { --ppl-column-ratio: 9; }   /* Ionic: refined display */
.order-performance  { --ppl-column-ratio: 10; }  /* Corinthian: maximum display */
.order-fullbody     { --ppl-column-ratio: 10; }  /* Composite: tall display */
.order-balance      { --ppl-column-ratio: 8.5; } /* Vitruvian: calibrated */
.order-restoration  { --ppl-column-ratio: 9.5; } /* Palladian: serene */
```

### Font Family by Axis

The Axis determines the typographic *voice* — not the size (that's the Order's job), but the character.

| Axis | Font Character | Implementation |
|------|---------------|----------------|
| 🏛 Firmitas | Geometric sans-serif. Classical. Stable. | `'Inter', system-ui` at normal tracking |
| 🔨 Utilitas | Condensed sans-serif. Utilitarian. Compact. | `'Inter Tight', system-ui` at tight tracking |
| 🌹 Venustas | Light sans-serif or transitional serif. Elegant. | `'Inter', system-ui` at weight 300, wide tracking |
| 🪐 Gravitas | Heavy sans-serif. Monumental. | `'Inter', system-ui` at weight 800, tight tracking |
| ⌛ Temporitas | Monospace accents. Tabular. Precise. | Body: `'Inter'`, numbers: `'JetBrains Mono'` |
| 🐬 Sociatas | Rounded sans-serif. Open. Warm. | `'Inter', system-ui` at generous tracking and leading |

---

## Part VIII — The Pinch-Zoom Architectural Scale

### Scale Levels as Drawing Scales

Architectural drawings exist at different scales. Each scale reveals different information:

| Drawing Scale | What You See | Ppl± Zoom Level |
|---------------|-------------|-----------------|
| 1:500 (Site plan) | Building footprints on campus | 0.1x — All 7 Order buildings visible as colored blocks |
| 1:200 (Floor plan) | Room layout within a floor | 0.25x — Deck map: 40 cards as grid |
| 1:100 (Room plan) | Furniture layout | 0.5x — Block overview: all blocks visible without scroll |
| 1:50 (Detail) | Material hatching, dimensions | 1.0x — Full card: reading and doing |
| 1:20 (Section detail) | Construction joint | 1.5x — Exercise focus: single exercise enlarged |
| 1:5 (Full detail) | Bolt holes, mortar joints | 2.0x — Log mode: set-by-set entry |

### Color Temperature Shifts with Scale

As you zoom out (lower scale numbers), the palette cools and desaturates — like viewing a city from altitude. As you zoom in, the palette warms and saturates — like entering a room.

```css
/* Zoom-level palette modifiers */
--ppl-zoom-sat-multiplier: 1.0;   /* At 1.0x: full saturation */
--ppl-zoom-warmth-shift: 0;       /* At 1.0x: no temperature shift */

/* Pinch out: cool and desaturate */
@media (zoom: 0.5) {
  :root {
    --ppl-zoom-sat-multiplier: 0.7;
    --ppl-zoom-warmth-shift: -10;
  }
}

/* Pinch in: warm and saturate */
@media (zoom: 1.5) {
  :root {
    --ppl-zoom-sat-multiplier: 1.15;
    --ppl-zoom-warmth-shift: 5;
  }
}
```

**In practice:** This uses JavaScript-driven CSS variable updates (not CSS zoom media queries, which don't exist). The pinch-zoom canvas from `seeds/mobile-ui-architecture.md` already specifies the gesture layer. This specification adds the palette response.

### The City View (0.1x scale)

At maximum zoom-out, the user sees the 7 Order buildings as architectural blocks on a campus. Each building is rendered in its material color:

```
┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
│ 🐂  │ │ ⛽  │ │ 🦋  │ │ 🏟  │ │ 🌾  │ │ ⚖  │ │ 🖼  │
│warm │ │cool │ │warm │ │white│ │earth│ │neut │ │cream│
│neut │ │neut │ │white│ │     │ │     │ │     │ │     │
└─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘
Tuscan   Doric   Ionic   Corin   Compo   Vitr    Pall
```

At this scale, the Color (room furnishing) is invisible — you see only the building material. As you pinch in, the Axis floors reveal themselves. Pinch further and the Type wings appear. Pinch to 1.0x and the Color fills the room. This is progressive disclosure expressed through architectural rendering scale.

---

## Part IX — The Ambient Temperature System

### What Changes as You Pan

The screen is a window into the architectural city. As the user scrolls or pans across zip codes, the ambient temperature of the screen shifts — not with jarring color swaps, but with the gradual modulation of a walker moving through neighborhoods.

**Temperature drivers:**

1. **Order proximity** — Moving from 🐂 Foundation to ⛽ Strength is moving from a warm travertine building to a cool marble one. The background shifts.

2. **Color proximity** — Adjacent rooms in the same wing differ only by Color. Moving from 🔵 Structured to 🔴 Intense is moving from a calm blue-lit room to a red-lit one. The transition is 250ms (from `animation.default`).

3. **Time of day (Operis cycle)** — Morning editions are cooler (🔵 Planning light). Evening is warmer (🟠 Connection light). The ambient shifts without the user choosing it.

4. **Seasonal position** — The 4-month inhale/exhale/catch-breath/close cycle from the Macro Almanac adds a global tint:
   - Jan–Apr (inhale): Cool, preparatory palette emphasis
   - May–Aug (exhale): Warm, expressive palette emphasis
   - Sep–Oct (catch-breath): Neutral, reflective
   - Nov–Dec (close): Deep, archival

```css
/* Seasonal ambient modifier */
--ppl-season-hue-shift: 0;       /* Neutral default */
--ppl-season-sat-modifier: 1.0;  /* Full sat default */
--ppl-season-temp-bias: 0;       /* No warmth bias */

/* Applied programmatically based on date */
/* January (inhale start): cool bias */
/* July (exhale peak): warm bias */
/* October (catch-breath): desaturate slightly */
```

---

## Part X — Color Theory Meets SCL Math

### The 8 Colors as a Coordinated Palette

The 8 SCL Colors are not arbitrary hex values. They form a color-theoretic system:

**Polarity (already in SCL):**
- Preparatory (inhale): ⚫ 🟢 ⚪ 🟡 — cooler, less saturated, reflective
- Expressive (exhale): 🔵 🟣 🔴 🟠 — warmer, more saturated, productive

**Color wheel positions:**

| Color | Hue (°) | Sat (%) | Light (%) | Wheel Position |
|-------|---------|---------|-----------|----------------|
| ⚫ Teaching | 0 | 0 | 10 | Achromatic (black) |
| 🟢 Bodyweight | 134 | 35 | 36 | Green (secondary) |
| 🔵 Structured | 209 | 57 | 42 | Blue (primary) |
| 🟣 Technical | 274 | 35 | 47 | Violet (tertiary) |
| 🔴 Intense | 5 | 63 | 46 | Red (primary) |
| 🟠 Circuit | 25 | 73 | 55 | Orange (secondary) |
| 🟡 Fun | 45 | 87 | 61 | Yellow (primary) |
| ⚪ Mindful | 33 | 30 | 93 | Near-white (achromatic) |

**Complementary pairs (tension pairings from Color Context Vernacular):**
- 🔴 Red ↔ 🟢 Green (Passion vs Growth) — classic complementary
- 🔵 Blue ↔ 🟠 Orange (Planning vs Connection) — classic complementary
- 🟣 Purple ↔ 🟡 Yellow (Magnificence vs Play) — classic complementary
- ⚫ Black ↔ ⚪ White (Order vs Eudaimonia) — value complementary

This is not coincidence. The 8 Colors form three complementary pairs + two achromatic poles. The color theory is built in.

### Generating Extended Palettes from Each Color

Each Color's full palette is generated systematically:

```
Base:        The primary hex value
Light 1:     Base + 20% lightness
Light 2:     Base + 40% lightness (surface/background)
Light 3:     Base + 60% lightness (lightest tint)
Dark 1:      Base - 20% lightness (accent)
Dark 2:      Base - 40% lightness (text color)
Dark 3:      Base - 60% lightness (deepest shade)
Complement:  Base + 180° hue rotation
Split-comp:  Base ± 150° hue rotation
Analogous:   Base ± 30° hue rotation
```

### WCAG Compliance Built In

The palette generation algorithm enforces WCAG AA (4.5:1 contrast) at every step:

```typescript
function ensureContrast(foreground: string, background: string, minimum: number = 4.5): string {
  const ratio = getContrastRatio(foreground, background);
  if (ratio >= minimum) return foreground;

  // Adjust lightness until contrast met
  return adjustLightnessForContrast(foreground, background, minimum);
}
```

---

## Part XI — The Vernacular Expression

### Every Zip Code Has an Architectural Identity

The convergence of all 4 dials produces a unique architectural expression — like a building in a traditional city has a specific facade that tells you what kind of building it is before you enter.

**Example: ⛽🏛🪡🔵 (Strength, Basics, Pull, Structured)**

```
Building:     ⛽ Strength (Doric) — cool neutral marble, dense, bold
Floor:        🏛 Firmitas (Piano Nobile) — grand hall, high ceiling, formal
Wing:         🪡 Pull — steel-blue accent trim
Room:         🔵 Structured (Planning) — calm blue palette, methodical
Material:     Pentelic marble with blue-gray veining
Shadow:       Sharp, warm-tinted (complement of blue)
Typography:   Geometric sans, 700 weight, tight tracking
Spacing:      Systyle (2D intercolumniation — compact)
Line weight:  Bold (1.3× multiplier)
Column ratio: 8D (Doric — strong display headers)
```

**Example: 🖼🌹➖⚪ (Restoration, Aesthetic, Ultra, Mindful)**

```
Building:     🖼 Restoration (Palladian) — warm cream stucco, chalky, soft
Floor:        🌹 Venustas (4th Floor) — gallery, curated light, warm
Wing:         ➖ Ultra — sky silver accent
Room:         ⚪ Mindful (Eudaimonia) — near-white, honest, minimal
Material:     Fresco plaster with the faintest blush
Shadow:       Almost none (Palladian: flat, fresco-like)
Typography:   Light sans, 300 weight, generous tracking and leading
Spacing:      Diastyle (3D intercolumniation — airy, breath between elements)
Line weight:  Gossamer (0.6× multiplier)
Column ratio: 9.5D (Palladian — tall, serene proportions)
```

These two rooms exist in the same system, use the same CSS template, and differ only in the weight vector that drives their CSS custom properties. The architecture produces the variety. No per-room styling.

---

## Part XII — The Emoji as Architectural Glyph

### Visual Properties of the 61 Emojis on Screen

Each of the 61 SCL emojis renders with specific colors, shapes, and visual weights on phone screens. These rendered properties are part of the palette — the emoji IS a design element.

**Order emojis as visual anchors:**

| Emoji | Dominant Rendered Colors | Visual Weight | Shape Character |
|-------|------------------------|---------------|-----------------|
| 🐂 | Brown, warm neutral | Heavy, grounded | Rounded, solid |
| ⛽ | Red, metallic gray | Medium, industrial | Geometric, mechanical |
| 🦋 | Blue, purple, iridescent | Light, ethereal | Organic, delicate wings |
| 🏟 | Green, brown, gray | Large, imposing | Rectangular, structured |
| 🌾 | Gold, brown, green | Medium, organic | Vertical lines, bundled |
| ⚖ | Gold, dark metal | Medium, precise | Bilateral symmetry |
| 🖼 | Brown, blue, warm | Light, contemplative | Rectangular frame |

**Color emojis match their palette purpose:**

The 8 Color circle emojis (⚫🟢🔵🟣🔴🟠🟡⚪) are their own design tokens. The hex values in `design-tokens.json` were derived from the rendered emoji colors. The emoji IS the swatch.

**Block emojis as iconographic system:**

Each of the 22 block emojis serves as an icon within the workout card. Their rendered visual properties — color, shape, implied motion — reinforce the block's function.

| Emoji | Rendered Character | Design Function |
|-------|-------------------|-----------------|
| ♨️ | Red, warm, rising steam | Warm-up: heat, preparation |
| 🎯 | Red/white, concentric | Intention: focus, precision |
| 🧈 | Yellow, warm, solid | Bread & Butter: nourishment, substance |
| 🚂 | Dark, mechanical, motion | Junction: movement, transition |
| 🧮 | Colorful beads on frame | SAVE: calculation, record |

---

## Part XIII — Implementation Specification

### CSS Custom Property Hierarchy

The complete variable hierarchy, in cascade order:

```css
:root {
  /* === MODULE === */
  --ppl-D: 1rem;                          /* The column diameter */
  --ppl-column-ratio: 8;                  /* Order's height-to-diameter */
  --ppl-intercolumniation: 2.25;          /* Order's column spacing (×D) */
  --ppl-superposition: 1.0;              /* Floor's structural weight */

  /* === MATERIAL (Order) === */
  --ppl-material-hue: 220;
  --ppl-material-sat: 5%;
  --ppl-material-warmth: 0.3;

  /* === ATMOSPHERE (Axis) === */
  --ppl-atmos-brightness: 1.0;
  --ppl-atmos-hue-shift: 0;
  --ppl-atmos-sat-mult: 1.0;
  --ppl-atmos-warmth: 0;

  /* === THEME (Color) === */
  --ppl-theme-primary: #2E6BA6;
  --ppl-theme-secondary: #3A7EC0;
  --ppl-theme-background: #EDF4FB;
  --ppl-theme-surface: #FFFFFF;
  --ppl-theme-text: #143050;
  --ppl-theme-accent: #1E4F7D;
  --ppl-theme-border: #B8D4EC;

  /* === LINE WEIGHT === */
  --ppl-line-multiplier: 1.0;
  --ppl-line-hairline: calc(var(--ppl-D) * 0.0625 * var(--ppl-line-multiplier));
  --ppl-line-fine:     calc(var(--ppl-D) * 0.075 * var(--ppl-line-multiplier));
  --ppl-line-light:    calc(var(--ppl-D) * 0.09375 * var(--ppl-line-multiplier));
  --ppl-line-medium:   calc(var(--ppl-D) * 0.125 * var(--ppl-line-multiplier));
  --ppl-line-bold:     calc(var(--ppl-D) * 0.1875 * var(--ppl-line-multiplier));
  --ppl-line-heavy:    calc(var(--ppl-D) * 0.25 * var(--ppl-line-multiplier));
  --ppl-line-boundary: calc(var(--ppl-D) * 0.375 * var(--ppl-line-multiplier));

  /* === TYPOGRAPHY (D-derived) === */
  --ppl-type-body:    calc(var(--ppl-D) * 1);
  --ppl-type-small:   calc(var(--ppl-D) * 0.875);
  --ppl-type-caption: calc(var(--ppl-D) * 0.75);
  --ppl-type-h4:      calc(var(--ppl-D) * 1.125);
  --ppl-type-h3:      calc(var(--ppl-D) * 1.25);
  --ppl-type-h2:      calc(var(--ppl-D) * 1.5);
  --ppl-type-h1:      calc(var(--ppl-D) * var(--ppl-column-ratio) * 0.2);
  --ppl-type-display: calc(var(--ppl-D) * var(--ppl-column-ratio) * 0.25);

  /* === SPACING (D-derived via intercolumniation) === */
  --ppl-space-xs:  calc(var(--ppl-D) * 0.25);
  --ppl-space-sm:  calc(var(--ppl-D) * 0.5);
  --ppl-space-md:  calc(var(--ppl-D) * var(--ppl-intercolumniation) * 0.5);
  --ppl-space-lg:  calc(var(--ppl-D) * var(--ppl-intercolumniation));
  --ppl-space-xl:  calc(var(--ppl-D) * var(--ppl-intercolumniation) * 1.5);
  --ppl-space-2xl: calc(var(--ppl-D) * var(--ppl-intercolumniation) * 2);

  /* === SHADOW (architectural) === */
  --ppl-shadow-hue: 30;
  --ppl-shadow-sat: 8%;
  --ppl-shadow-depth: 1.0;

  /* === ZOOM === */
  --ppl-zoom-sat-multiplier: 1.0;
  --ppl-zoom-warmth-shift: 0;

  /* === SEASON === */
  --ppl-season-hue-shift: 0;
  --ppl-season-sat-modifier: 1.0;
  --ppl-season-temp-bias: 0;
}
```

### The Rendering Function (Extended)

```typescript
interface ArchitecturalStyle {
  D: string;
  columnRatio: number;
  intercolumniation: number;
  superposition: number;
  material: { hue: number; sat: string; warmth: number };
  atmosphere: { brightness: number; hueShift: number; satMult: number };
  theme: ColorPalette;
  lineMultiplier: number;
  shadowDepth: number;
  typeAccent: string;
  operatorTint: string;
}

function resolveArchitecturalStyle(zipCode: string): ArchitecturalStyle {
  const [order, axis, type, color] = parseZip(zipCode);
  const vector = getWeightVector(zipCode);

  return {
    D: ORDER_D_VALUES[order],
    columnRatio: ORDER_COLUMN_RATIOS[order],
    intercolumniation: ORDER_INTERCOLUMNIATION[order],
    superposition: AXIS_SUPERPOSITION[axis],
    material: ORDER_MATERIALS[order],
    atmosphere: AXIS_ATMOSPHERES[axis],
    theme: COLOR_PALETTES[color],
    lineMultiplier: ORDER_LINE_MULTIPLIERS[order],
    shadowDepth: ORDER_SHADOW_DEPTHS[order],
    typeAccent: TYPE_ACCENTS[type],
    operatorTint: OPERATOR_TINTS[deriveOperator(axis, color)],
  };
}
```

---

## Part XIV — Vitruvian and Palladian: The Two Extended Orders

### 🖼 Restoration as Palladian Architecture

Andrea Palladio (1508–1580) refined the classical orders into a system of harmonic room proportions. His villas used specific room-dimension ratios:

- 1:1 (square) — most stable
- √2:1 (1.414:1) — the diagonal of a square
- 4:3 — the musical fourth
- 3:2 — the musical fifth
- 5:3 — the major sixth
- 2:1 — the octave

In the Ppl± UI, 🖼 Restoration rooms use Palladian proportions for content blocks. Block containers follow harmonic width-to-height ratios. The result is serene visual proportion — the eye rests because every rectangle relates harmonically to every other.

```css
/* Palladian harmonic ratios for block containers */
.order-restoration .block {
  aspect-ratio: 3 / 2;  /* Musical fifth — the most naturally pleasing */
}

.order-restoration .block-header {
  aspect-ratio: 4 / 3;  /* Musical fourth — stable, grounded */
}
```

### ⚖ Balance as Vitruvian Architecture

Vitruvius's *De Architectura* established three principles that map directly to the SCL Axis names:

- **Firmitas** (structural soundness) → 🏛 Basics
- **Utilitas** (functionality) → 🔨 Functional
- **Venustas** (beauty/delight) → 🌹 Aesthetic

The ⚖ Balance Order is named Vitruvian because it corrects imbalances — it is the order that asks whether the three Vitruvian principles are in equilibrium. Its UI treatment reflects this: bilateral symmetry, precise alignment, corrective detail visible.

```css
/* Vitruvian bilateral symmetry */
.order-balance .block {
  display: grid;
  grid-template-columns: 1fr 1fr;  /* Bilateral — left mirrors right */
  gap: var(--ppl-space-md);
}

.order-balance .exercise-row {
  text-align: center;  /* Centered — no asymmetric pull */
}
```

The Vitruvian Man's proportions (navel as center of a circle, extremities as corners of a square inscribed in the circle) inform the ⚖ layout's use of centered radial composition rather than the left-to-right reading order of other Orders.

---

## Part XV — The Golden Ratio as Structural Verification

### Not as Generator — as Validator

The golden ratio (φ = 1.618...) appears throughout classical architecture — not because architects designed to it, but because harmonious proportions naturally approximate it. In Ppl±, the golden ratio serves as a verification tool, not a generation tool.

**Verification checks:**

```
Column height / Entablature height ≈ φ ?
  Tuscan: 7D / 1.75D = 4.0 (no)
  Doric: 8D / 2D = 4.0 (no)
  Ionic: 9D / 2.25D = 4.0 (no — but the ratio is constant)
  Corinthian: 10D / 2.5D = 4.0 (the classical system is linear, not golden)

Content area / Sidebar ≈ φ ?
  Yes — use 1.618:1 for main-to-secondary content splits.

Block spacing / Content height ≈ φ ?
  No — let the intercolumniation system handle this.
```

The golden ratio appears in two specific places:
1. **Content area splits** (main column : secondary column = φ : 1)
2. **The Operis front page** (feature area : departments = φ : 1)

Everywhere else, the D-module system provides proportions directly.

---

## Part XVI — Open Questions

1. **Dark mode derivation:** The Palladian stucco/fresco material metaphor works beautifully in light mode. How does it translate to dark? Should 🖼 Restoration dark mode feel like a dimly lit fresco chapel rather than a standard dark theme?

2. **Emoji rendering variance:** Emojis render differently across platforms (Apple, Google, Samsung, Windows). The palette derivations from emoji appearance should use the most common rendering (Apple) as reference, with graceful degradation.

3. **Accessibility at extremes:** ⚪ Mindful rooms have near-zero saturation and near-zero shadow. Does this create sufficient visual structure for users with cognitive disabilities? The WCAG floor (4.5:1) handles contrast, but structural hierarchy may need reinforcement.

4. **Animation as architectural movement:** Should the transition between rooms animate as "walking through a corridor" (horizontal translation) or "taking the elevator" (vertical translation) or simply cross-fade? The architectural metaphor suggests corridor walks for Type changes and elevator rides for Axis changes.

5. **User customization boundary:** The MySpace principle (from digital-city-architecture.md) allows users to modify their rooms. How deep into the D-module system can user overrides reach? Can a user change their room's D? Their intercolumniation? Or only surface properties like accent color?

6. **Print rendering:** The architectural drawing metaphor translates naturally to print. Should workout cards have a "print as architectural elevation" mode that outputs them as actual architectural drawings with proper line weights and annotations?

---

## Part XVII — Relationship to Existing Specifications

This seed **extends** (does not replace) the following documents:

| Document | What This Seed Adds |
|----------|---------------------|
| `middle-math/design-tokens.json` | D-module system, column ratios, intercolumniation values, material hues, atmosphere modifiers |
| `middle-math/weight-css-spec.md` | Line weight system, shadow architecture, superposition, ambient temperature |
| `seeds/elevator-architecture.md` | Superposition of orders applied to floor stack, floor-level shadow depth |
| `seeds/experience-layer-blueprint.md` | Zoom-level palette shifts, ambient temperature system |
| `seeds/mobile-ui-architecture.md` | Pinch-zoom → architectural scale mapping |
| `scl-deep/color-context-vernacular.md` | Color wheel analysis, complementary pair identification, polarity color theory |
| `middle-math/rendering/ui-weight-derivation.md` | Material (Order), Atmosphere (Axis), Furnishing (Color) layering model |

---

🧮
