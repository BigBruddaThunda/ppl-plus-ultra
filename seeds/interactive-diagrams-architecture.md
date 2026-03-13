# Interactive Diagrams Architecture

**Status:** SEED — planted 2026-03-12
**Author:** Jake Berry + Claude Code
**Supersedes:** Nothing. New capability layer.
**Blocks card generation:** No
**Depends on:** experience-layer-blueprint.md, art-direction-intaglio.md, elevator-architecture.md, digital-city-architecture.md, mobile-ui-architecture.md, home-screen-architecture.md

---

## What This Is

An architecture for interactive SVG/React diagram components embedded throughout the Ppl± web experience. These are not decorative illustrations. They are functional navigation tools, exercise reference surfaces, and data visualization layers — built from the JSON data that already exists in `middle-math/`.

The diagrams serve three purposes:

1. **Navigate** — Click a muscle, land in the right room. Click a building, enter the floor.
2. **Understand** — See what a weight vector looks like. See how exercises connect.
3. **Learn** — Interactive form diagrams replace text descriptions of movement.

Every diagram reads from compiled JSON. No new data pipelines required. The rendering layer interprets what the computation layer already produces.

---

## Technology

**Rendering:** React components with inline SVG. No external charting libraries for anatomy or city diagrams — hand-authored SVG paths give intaglio-grade control over line weight, hatching, and engraving texture. D3.js permitted for force-directed graphs and radial plots where manual SVG would be impractical.

**Styling:** Weight vector → CSS custom properties (per `middle-math/weight-css-spec.md`). Each diagram inherits the room's palette, typography, and D-module proportions. A diagram in a 🔵 Structured room looks different from the same diagram in a 🟡 Fun room.

**Interaction:** Hover → tooltip. Click → drill-down or navigation. Pinch-zoom on mobile (already built: `ZoomableRoom.tsx` + `@use-gesture/react`). Touch targets minimum 44px.

**Art direction:** Intaglio engraving register (per `seeds/art-direction-intaglio.md`). Line-based, not filled. Cross-hatching for shading. Guilloche borders driven by zip parameters. The diagrams look like they belong on currency, not in a SaaS dashboard.

---

## Diagram Types

### Type 1: Anatomy Explorer

**What:** Interactive human body SVG. Click a muscle group → see exercises that target it, which zip codes route there, substitution options.

**Data sources:**
- `middle-math/exercise-engine/anatomy-index.json` — muscle → exercise mapping (primary + secondary)
- `middle-math/exercise-registry.json` — 2,085 exercises with anatomy data, EX-IDs
- `middle-math/exercise-engine/family-trees.json` — progression hierarchies per movement pattern
- `middle-math/exercise-engine/substitution-map.json` — same-family, tier-up, tier-down, cross-family alternatives

**Interaction model:**
1. Full body SVG with ~40 muscle groups as clickable regions
2. Hover: muscle name + exercise count (primary/secondary)
3. Click: sidebar opens with exercise list, filterable by Type emoji (🛒🪡🍗➕➖)
4. Each exercise row shows: name, EX-ID, family, difficulty tier
5. Click exercise → substitution graph (4 axes: same-family, tier-up, tier-down, cross-family)
6. Click any exercise → navigate to a zip code that features it

**Views:**
- **Full body** — anterior + posterior toggle. All 5 Types visible.
- **Type-filtered** — 🛒 Push highlights chest/front delts/triceps. 🪡 Pull highlights lats/rear delts/biceps/traps/erectors. 🍗 Legs highlights quads/hamstrings/glutes/calves. Dimmed regions for non-targeted muscles.
- **Exercise-specific** — Single exercise selected. Primary muscles in full color. Secondary muscles in half-tone cross-hatch. Movement path arrows overlaid.

**Where it lives:**
- `/tools/anatomy` — standalone tool floor page
- Embedded in room pages as collapsible "muscle map" panel
- `/exercise/[EX-ID]` — exercise detail page (future route)

**SCL integration:** The 5 Type emojis are the muscle group selectors. Clicking 🪡 on the anatomy chart is equivalent to filtering the exercise library by Pull. The anatomy chart IS the Type dial rendered as a body.

---

### Type 2: City Navigator

**What:** Interactive map of the Ppl± city. 7 buildings (Orders) × 6 floors (Axes) × 5 wings (Types) × 8 rooms (Colors). Click to navigate. Zoom to explore.

**Data sources:**
- `middle-math/navigation-graph.json` — 1,680 nodes, 6,720 edges, city statistics, centroid
- `middle-math/compiled/zips/[NNNN].json` — per-room data (palette, personality, connections)
- `middle-math/compiled/decks/deck-NN.json` — 42 deck aggregates with centroids
- `middle-math/compiled/abaci/abacus-NN.json` — 35 neighborhood collections

**Zoom levels (maps to existing pinch-zoom architecture):**
- **0.1x — City overview:** 7 buildings as architectural silhouettes. Each building styled per Order's D-module (Tuscan→Palladian). Color = dominant Color frequency in that Order.
- **0.25x — Building view:** One Order selected. 6 floors stacked (piano nobile arrangement from elevator-architecture). 5 wings per floor visible as structural bays.
- **0.5x — Floor view:** One Axis floor. 5 Type wings. 8 Color rooms per wing visible as a grid. Room occupancy state: lit (visited), dim (unvisited), fog (locked/undiscovered per exploration-immersion-architecture).
- **1x — Room view:** Single zip code. Full room rendering with workout card content. N/E/S/W navigation arrows to adjacent rooms. Cosine-nearest-5 shown as dotted pathways.

**Interaction model:**
1. Click building → zoom to 0.25x
2. Click floor → zoom to 0.5x
3. Click room → zoom to 1x (navigate to `/zip/[code]`)
4. Pinch/scroll to zoom freely between levels
5. Fog of war state persists (per exploration-immersion-architecture.md)

**Where it lives:**
- Home screen Zone 2 (Viewport) as default "figure-ground map" (per home-screen-architecture.md)
- `/tools/city` — standalone full-screen explorer
- `/deck/[number]` — deck view zoomed to 0.5x for that deck's 40 rooms

**Intaglio treatment:** Buildings rendered as engraved architectural elevations. Floor plans as Nolli-style figure-ground (solid = visited, void = unvisited). Room outlines as guilloche-bordered cells, border complexity driven by weight vector magnitude.

---

### Type 3: Weight Vector Radial

**What:** 61-spoke radar/polar diagram showing a zip code's weight vector. Each spoke = one SCL emoji. Length = weight magnitude. Color = positive (favor) vs negative (suppress).

**Data sources:**
- `middle-math/weight-vectors.json` — 1,680 vectors, 61 dimensions, range [-8, +8]
- `middle-math/compiled/zips/[NNNN].json` — includes `weight_vector` and `vector_magnitude`

**Interaction model:**
1. Hover spoke → emoji name, raw weight value, explanation
2. Click spoke → filter view to exercises influenced by that weight
3. Toggle: overlay a second zip's vector for comparison (alpha blend)
4. Toggle: show cosine-nearest-5 as ghost vectors behind primary
5. Animate: morph between two zip vectors to visualize the "distance"

**Variants:**
- **Full 61-spoke** — complete vector. Dense. For tools/research.
- **4-dial summary** — collapsed to 4 groups (Order/Axis/Type/Color averages). Simpler. For room page sidebar.
- **Deck centroid** — 42 deck centroids overlaid. Shows how decks cluster.

**Where it lives:**
- Room page: collapsible panel below workout content
- `/tools/vectors` — comparison tool (select two zips, overlay)
- `/deck/[number]` — deck centroid view

---

### Type 4: Exercise Progression Tree

**What:** Hierarchical tree diagram showing exercise families. Root exercise at top. Branches = progressions. Depth = difficulty tier.

**Data sources:**
- `middle-math/exercise-engine/family-trees.json` — 15 families, 2,085 members, parent-child-depth structure
- `middle-math/exercise-engine/substitution-map.json` — lateral alternatives at each tier
- `middle-math/exercise-registry.json` — EX-IDs, names, anatomy, patterns

**Interaction model:**
1. Select a family (e.g., "Horizontal Press Family")
2. Tree renders root at top, branches downward by depth
3. Hover node → exercise name, muscles, tier, transfer ratio
4. Click node → expand lateral substitutions (same-family alternatives fan out horizontally)
5. Highlight path: "You are here" marker on the user's current progression level
6. Color-code by difficulty tier (intaglio line density increases with difficulty)

**Where it lives:**
- `/tools/progressions` — standalone progression explorer
- Embedded in exercise detail pages
- Room page: "progression context" panel showing where the room's exercises sit in their family trees

---

### Type 5: Block Sequence Timeline

**What:** Horizontal timeline showing a workout's block sequence. Each block = a segment with emoji, name, duration estimate, and exercise count.

**Data sources:**
- `middle-math/compiled/zips/[NNNN].json` — `block_sequence` array, `block_count`
- Card `.md` files — actual block content (exercises, sets, reps)

**Interaction model:**
1. Timeline renders left-to-right: ♨️ → ▶️ → 🧈 → 🧩 → 🪫 → 🚂 → 🧮
2. Hover block → preview (exercise list, rep ranges)
3. Click block → scroll room page to that block section
4. Progress indicator: blocks completed in current session highlighted
5. During logging: active block pulses. Completed blocks fill with cross-hatch.

**Where it lives:**
- Room page: sticky header/footer showing workout progress
- Session summary page: completed timeline with logged data overlaid

---

### Type 6: Abacus Track Visualizer

**What:** Linear track showing a training program (abacus) as a sequence of zip codes. Current position marked. Upcoming rooms previewed.

**Data sources:**
- `middle-math/compiled/abaci/abacus-NN.json` — 35 working zips + 13 bonus per abacus
- `middle-math/compiled/zips/[NNNN].json` — per-room data for each stop

**Interaction model:**
1. Horizontal scrollable track. Each stop = one zip code rendered as a small room card.
2. Current position marked with pulsing indicator.
3. Hover stop → zip emoji, title, muscle targets, difficulty
4. Click stop → navigate to that room
5. Completed stops: filled. Upcoming: outlined. Bonus: dotted border.
6. Domain label above track (Strength / Conditioning / Mobility / etc.)

**Where it lives:**
- `/tools/programs` — browse all 35 abacus tracks
- Home screen Zone 3 (Relevator) — minimap shows current abacus position
- `/me/history` — personal abacus progress

---

### Type 7: Similarity Constellation

**What:** Force-directed graph showing zip code clusters by cosine similarity. Related zips attract. Dissimilar zips repel. Click to navigate.

**Data sources:**
- `middle-math/compiled/zips/[NNNN].json` — `cosine_nearest_5` and `cosine_farthest` per zip
- `middle-math/weight-vectors.json` — raw vectors for distance computation

**Rendering:** D3.js force-directed layout. Nodes = zips (colored by Order or Color). Edges = cosine similarity > threshold. Node size = vector magnitude.

**Interaction model:**
1. Zoom/pan through the constellation
2. Hover node → zip emoji, title, similarity to selected
3. Click node → center view, show connections, option to navigate
4. Filter: by Order, Axis, Type, Color, or Deck
5. Highlight: "your history" overlay shows visited rooms as filled nodes

**Where it lives:**
- `/tools/constellation` — full-screen explorer
- Embedded as mini-constellation (nearest-5 only) on room pages

---

### Type 8: Deck Identity Card

**What:** Visual summary card for each of 42 decks. Centroid radar, exercise coverage, block distribution, sample rooms.

**Data sources:**
- `middle-math/compiled/decks/deck-NN.json` — centroid, constituent count, Order×Axis
- Deck identity docs in `deck-identities/`
- Deck cosmograms in `deck-cosmograms/`

**Interaction model:**
1. Deck card renders: name, Order+Axis emojis, centroid radar (mini), top exercises
2. Click → expand to full deck view (40 rooms as grid)
3. Toggle: cosmogram view (research/deep content layer)
4. Toggle: quality metrics (audit score, flag count)

**Where it lives:**
- `/deck/[number]` — deck landing page
- Home screen: deck of the day card
- `/tools/decks` — all 42 decks browseable

---

## Data Flow Architecture

```
┌─────────────────────────────────────────────┐
│              MIDDLE-MATH LAYER              │
│  (computed, deterministic, JSON)            │
├─────────────────────────────────────────────┤
│  weight-vectors.json      (1,680 × 61)     │
│  navigation-graph.json    (6,720 edges)     │
│  anatomy-index.json       (~40 muscles)     │
│  family-trees.json        (15 families)     │
│  substitution-map.json    (2,085 entries)   │
│  exercise-registry.json   (2,085 entries)   │
│  compiled/zips/           (1,680 files)     │
│  compiled/decks/          (42 files)        │
│  compiled/abaci/          (35 files)        │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│            DIAGRAM COMPONENT LAYER          │
│  (React + SVG, styled by weight vector)     │
├─────────────────────────────────────────────┤
│  <AnatomyExplorer />                        │
│  <CityNavigator />                          │
│  <WeightVectorRadial />                     │
│  <ProgressionTree />                        │
│  <BlockTimeline />                          │
│  <AbacusTrack />                            │
│  <SimilarityConstellation />                │
│  <DeckIdentityCard />                       │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│              INTEGRATION POINTS             │
│  (where diagrams appear in the app)         │
├─────────────────────────────────────────────┤
│  Room page (/zip/[code])                    │
│    → BlockTimeline (sticky)                 │
│    → AnatomyExplorer (collapsible)          │
│    → WeightVectorRadial (collapsible)       │
│    → ProgressionTree (per exercise)         │
│    → SimilarityConstellation (mini)         │
│                                             │
│  Home screen (Zone 2: Viewport)             │
│    → CityNavigator (default map view)       │
│    → AbacusTrack (Zone 3: Relevator mini)   │
│    → DeckIdentityCard (deck of the day)     │
│                                             │
│  Tool floor (/tools/*)                      │
│    → All diagrams as standalone pages       │
│    → Full-screen, full-interaction modes    │
│                                             │
│  Deck page (/deck/[number])                 │
│    → DeckIdentityCard (expanded)            │
│    → CityNavigator (zoomed to deck)         │
│    → WeightVectorRadial (centroid)          │
│                                             │
│  Profile (/me/*)                            │
│    → AbacusTrack (personal progress)        │
│    → SimilarityConstellation (history)      │
│    → AnatomyExplorer (muscle coverage)      │
└─────────────────────────────────────────────┘
```

---

## Prototyping Pipeline

Interactive diagrams can be prototyped in Claude.ai chat using Artifacts before being ported to the web app codebase. This matches the existing Temp Architect pattern.

**Step 1 — Claude.ai Artifact Prototype**
Open a Claude.ai chat. Paste the relevant JSON data (or a representative subset). Describe the diagram. Claude builds a React artifact with live preview. Iterate the interaction model, styling, and data binding in conversation.

**Step 2 — Export to Codebase**
Copy the artifact's React component code. Create a new component in `web/src/components/diagrams/`. Wire it to the real JSON data source (city-compiler or direct import). Apply intaglio design tokens.

**Step 3 — Integration**
Embed the component at its integration points (room page, home screen, tool floor). Connect to Zustand stores for state (selected zip, current floor, fog-of-war). Add pinch-zoom support via existing `@use-gesture/react` setup.

**Step 4 — Iterate**
Use Claude.ai for rapid visual iteration. Use Claude Code for codebase integration and data wiring. The prototype loop lives in chat. The production code lives in the repo.

---

## Priority Sequence

Build order based on data readiness and user impact:

| Priority | Diagram | Why First |
|----------|---------|-----------|
| 1 | Anatomy Explorer | Highest user value. Data 100% ready (anatomy-index + registry). Directly useful for exercise selection and learning. |
| 2 | Block Timeline | Smallest scope. Immediate UX improvement on room pages. Block sequence data already in compiled zips. |
| 3 | City Navigator | Defines the spatial metaphor. Home screen anchor. Navigation graph ready. |
| 4 | Weight Vector Radial | Research/power-user tool. Vectors computed. Good for understanding the system. |
| 5 | Progression Tree | Exercise learning tool. Family trees ready. Substitution map ready. |
| 6 | Abacus Track | Program navigation. Abacus data compiled. Needs user session state integration. |
| 7 | Deck Identity Card | Deck-level view. Centroid data ready. Cosmogram integration adds depth. |
| 8 | Similarity Constellation | Exploration tool. D3.js force layout. Most complex rendering. Last. |

---

## Art Direction Notes

All diagrams follow the intaglio engraving register:

- **Lines, not fills.** Muscles outlined, not colored solid. Cross-hatching for shading depth.
- **Guilloche borders** on diagram containers, complexity driven by the room's weight vector magnitude.
- **Engraved labels.** Small caps. Serif. Positioned with classical typographic spacing.
- **Color from the room.** Each diagram inherits the Color palette of the zip code context it renders in. Same anatomy chart, 8 different color treatments.
- **Resolution cascade.** Full detail at 1x. Simplified outlines at 0.5x. Silhouettes at 0.25x. Matches the pinch-zoom architecture already built.
- **Animation = drawing.** Diagrams animate in by drawing their lines, like a pen plotting the engraving. Not fade-in. Not scale-up. Line-by-line reveal.

---

## What This Does Not Do

- Does not replace the card `.md` format. Cards remain the source of truth.
- Does not require a new data pipeline. All data sources already exist as compiled JSON.
- Does not block card generation. This is a rendering layer, not a content layer.
- Does not require external APIs. All computation is local, all data is in-repo.
- Does not change the SCL. The diagrams read the language. They do not extend it.

---

## Relationship to Existing Seeds

| Seed | Relationship |
|------|-------------|
| `experience-layer-blueprint.md` | Diagrams are components within the experience layer |
| `art-direction-intaglio.md` | Diagrams follow the intaglio visual register |
| `elevator-architecture.md` | City Navigator implements the elevator spatial model |
| `digital-city-architecture.md` | City Navigator renders the city thesis |
| `mobile-ui-architecture.md` | Diagrams respect the 4-state interaction model and pinch-zoom |
| `home-screen-architecture.md` | City Navigator is the default Viewport content |
| `character-progression-architecture.md` | Progression Tree feeds the skill matrix visualization |
| `exploration-immersion-architecture.md` | Fog of war state affects City Navigator room visibility |
| `life-copilot-architecture.md` | Anatomy Explorer extends to health/body awareness tools |

---

## Open Questions

1. **Quiz mode on Anatomy Explorer** — Add active learning (show function, identify structure) per Anthropic's use case guide? Fits the educational floor (🏛 Basics). Needs design.
2. **SVG authoring** — Hand-draw the anatomy SVG paths for intaglio quality, or use an anatomogram library (`@ebi-gene-expression-group/anatomogram`) and style-override? Hand-drawn = beautiful, slow. Library = fast, may fight the art direction.
3. **Offline support** — Diagrams read from compiled JSON. If JSON is bundled at build time (ISR), diagrams work offline. Worth committing to?
4. **Accessibility** — SVG diagrams need ARIA labels, keyboard navigation, screen reader support. Each clickable region needs a text alternative. Design this from the start.
5. **Community floor integration** — Can users annotate diagrams? Pin a note to a muscle group? Share a marked-up anatomy chart? Ties to Session L (community) decisions.

---

61 emojis. 8 diagram types. 1,680 rooms to visualize.

Read the data. Render the room. Let the user navigate by touching the picture.

---

🧮
