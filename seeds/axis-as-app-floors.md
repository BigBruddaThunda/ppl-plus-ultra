---
planted: 2026-02-20
status: SEED
phase-relevance: Phase 4/5 (Design System + HTML)
blocks: nothing in Phase 2-3
depends-on: scl-deep/axis-specifications.md
connects-to: seeds/zip-dial-navigation.md, seeds/art-direction.md, seeds/superposed-order-ui.md
---

# Axis-as-App-Floors — The 6 Axes as App-Level Content Spaces

## One Sentence

The 6 Axes serve dual function: inside a workout zip code they bias exercise character; outside the workout, at the app level, they are six distinct content spaces — six floors of the building — each named for the architectural principle that describes what that space IS.

## The Dual Identity

Every Axis emoji holds two roles simultaneously:

| Axis | In-Workout Role | App-Level Role |
|------|----------------|----------------|
| 🏛 Firmitas | Bilateral, barbell-first, stable classics | Front page. Navigation hub. System map. |
| 🔨 Utilitas | Unilateral, standing, athletic transfer | Tools. Calculators. Settings. Utility. |
| 🌹 Venustas | Isolation, full ROM, mind-muscle connection | Personal library. Trophy case. Private space. |
| 🪐 Gravitas | Hardest variation at any level | Challenge board. Benchmarks. Competition. |
| ⌛ Temporitas | Clock as training variable | Almanac. Calendar. Seasonal content. Schedule. |
| 🐬 Sociatas | Social training context | Community. Social layer. Discussion. Groups. |

The same workout card renders differently depending on which Axis floor is presenting it. This is not six apps — it is one building with six floors, and the workout card is the object you encounter on every floor, contextualized differently by where you're standing.

## The Six Floors — Detailed Specification

### 🏛 Firmitas — The Front Page / Navigation Hub

**Vitruvian principle:** Structural soundness. The load-bearing wall.

**What lives here:**
- The 42-deck grid as a navigable map
- The 4-dial combination lock navigator
- Quick-view zip code lookup
- Full system analytique — the architectural plate showing the entire building from above
- Today's default zip code (from the rotation engine)
- Featured workout of the day / seasonal highlight

**Relationship to workout card:** The card appears as a point on a map. One of 1,680 addresses in the grid. Thumbnail view. Structural overview. You see the card's position in the system, not its content depth.

**Firmitas is:** The lobby. The directory. The floor plan mounted on the wall when you walk in. It doesn't hold content of its own — it holds the structure that all other content hangs on.

### 🔨 Utilitas — Tools and Utility

**Vitruvian principle:** Practical function. Things that work.

**What lives here:**
- Exercise library browser (searchable, filterable by SCL attributes)
- One-rep max calculator
- Macro / nutrition calculators
- Personal zip code deck creation and deck builder
- Settings and preferences
- Account management
- Payment / subscription
- Support, bug reports, feature requests
- Help pages and documentation
- Equipment tier self-assessment

**Relationship to workout card:** The card's exercise data feeds calculators and deck builders. You see the card as raw material to manipulate — swap exercises, adjust parameters, build custom decks from existing zip code templates.

**Utilitas is:** The workshop. The toolshed. The utility room behind the beautiful facade. You go here when you need to DO something to the system rather than experience something within it.

### 🌹 Venustas — The Personal Space / Private Library

**Vitruvian principle:** Beauty and delight. The personal.

**What lives here:**
- Personal workout history
- Trophy case / accolade board (PRs, streaks, milestones)
- Saved workouts and favorites
- Personal journal / training log
- Personal notes per zip code (from previous visits)
- Hobby space / personal collection
- ± superscript/subscript data in full (your weight history, your frequency data)
- Personal version of the exercise library populated with logged data
- Venustas IS the room where the ± boxes are full because you've been here before

**Relationship to workout card:** The card appears populated with YOUR history. Your weights, your notes, your superscript/subscript boxes filled in. The card reflects you back at you. First visit: sparse. Tenth visit: rich. This is where Room Bloom (seeds/almanac-room-bloom.md) is most visible.

**Venustas is:** Your room in the building. Private. Nobody else sees it unless you invite them. The vanity mirror in the honest PPL± sense — no shame in caring about what you've built.

### 🪐 Gravitas — The Challenge Board / Competition Space

**Vitruvian principle:** Weight and seriousness. Consequence.

**What lives here:**
- Weekly challenge boards
- Benchmark tracking (the 🏟 Corinthian data surface)
- Goal setting with deadlines
- Character creator — building a training identity through tested metrics
- Live workouts / synchronous training events
- Leaderboards (opt-in, not forced)
- Testing protocols and assessment tools
- Community challenges (monthly, seasonal, annual)
- Competition brackets

**Relationship to workout card:** The card appears as a challenge — a benchmark to hit, a test to pass, a live session to compete in. The card has stakes. You don't wander into Gravitas casually. You go there with intent because you want to be measured.

**Gravitas is:** The arena floor. The testing ground. Where things have consequence.

### ⌛ Temporitas — The Almanac / Calendar Space

**Vitruvian principle:** Rhythm and time.

**What lives here:**
- The Almanac itself — the user's personal workout queue and rotation
- Calendar view (daily, weekly, monthly)
- The 12-month Operator calendar visualization
- Seasonal content — Farmer's Almanac layer (food, agriculture, lifestyle, rhythm)
- To-do lists and personal project manager
- Schedule keeper
- Timed seasonal content drops
- Training cycle planning (mesocycle, macrocycle views)
- Historical pattern visualization (how your training has moved through time)

**Relationship to workout card:** The card appears as today's entry in a seasonal rotation — one moment in a year-long rhythm. The card lives inside time. You see it in the context of what came before and what comes after, not as an isolated event.

**Temporitas is:** The sundial in the courtyard. The space that knows what month it is, what season it is, where you are in the cycle. It's the clock made visible.

### 🐬 Sociatas — The Community / Social Layer

**Vitruvian principle:** Togetherness. Society.

**What lives here:**
- Community boards per zip code (public record books)
- Discussion threads
- Friend groups / dolphin pods / workout crews
- Junction community voting (follow-up zip recommendations)
- Shared challenges (cross-posted from Gravitas)
- Training partner finder
- User-submitted workout modifications
- Community-contributed seasonal content
- Social feed of friend activity

**Relationship to workout card:** The card appears as a community object — what other people did with it, how they modified it, what they recommend next. The Junction block's community layer lives here in its fullest expression. The card belongs to everyone who's used it.

**Sociatas is:** The public square. The agora. Where the building's residents actually meet each other.

## Navigation Architecture

### How the Six Floors Relate to Mobile UI

The 4-dial combination lock (seeds/zip-dial-navigation.md) still works as the primary way to find a specific workout. But the Axis dial now does double duty — it selects exercise character inside a workout AND which floor of the building you're standing on when you view the results.

For mobile bottom navigation, the six floors could present as:
- 6 bottom tabs (potentially crowded but complete)
- A primary view (Firmitas as home) with the other 5 accessible via the Axis dial or a floor selector
- Firmitas as the persistent home layer with the other 5 as overlay/drawer spaces

The most architecturally honest approach: **Firmitas is always the ground floor.** You start there. The 4-dial lock lives on Firmitas. When you spin the Axis dial, you're taking an elevator to a different floor. The other three dials (Order, Type, Color) adjust what you see on that floor. Firmitas is the only floor you don't need to spin to — it's where the elevator starts.

### How the Workout Card Moves Across Floors

The workout card is the universal object. It exists once (as a master .md file). But its presentation layer shifts per floor:

| Floor | Card Presentation |
|-------|-------------------|
| 🏛 Firmitas | Thumbnail in a grid. Position in the system. |
| 🔨 Utilitas | Raw data. Editable parameters. Deck builder input. |
| 🌹 Venustas | Personal history overlay. ± boxes filled. Notes visible. |
| 🪐 Gravitas | Challenge framing. Benchmark comparison. Leaderboard context. |
| ⌛ Temporitas | Calendar position. Before/after context. Seasonal tone. |
| 🐬 Sociatas | Community overlay. Modifications. Votes. Discussion. |

## Architectural Implications

### For the HTML Directory
The `html/` scaffold needs an `html/floors/` directory or equivalent — six top-level view templates, one per Axis floor. Each floor has its own layout logic, its own content types, its own relationship to the shared component library (card-shell, exercise-row, etc.).

### For the Design System
Each floor can carry a subtle visual identity derived from its Axis. The 6 Axis CSS files in `html/design-system/axes/` now do double duty — they style both the in-workout exercise character AND the floor-level visual environment.

### For the SCL Deep Spec
`scl-deep/axis-specifications.md` now needs two sections per Axis: the in-workout behavior (exercise selection bias, ranking logic) and the app-level behavior (floor content, layout, card presentation). Both are true simultaneously. The emoji holds both.

## Open Questions

- Are all six floors always visible in navigation, or does the user unlock/discover some over time?
- Does the 4-dial Axis spin literally change the app floor, or are they separate navigation systems?
- Should some floors be visible to non-logged-in users? (Firmitas and Sociatas yes, Venustas and Temporitas require account?)
- How does the floor system relate to URL routing? (pplplusultra.com/firmitas/... vs. pplplusultra.com/🏛/...)
- Does each floor have its own visual temperature (Gravitas darker, Venustas warmer, Utilitas neutral)?
