---
planted: 2026-03-24
status: SEED
phase-relevance: Phase 3+ (can build now), Phase 4+ (deepens with app launch)
blocks: nothing — SEO layer, does not block card generation or app build
depends-on:
  - middle-math/zip-registry.json
  - middle-math/compiled/zips/*.json
  - middle-math/compiled/decks/*.json
  - middle-math/navigation-graph.json
  - middle-math/design-tokens.json
  - middle-math/compiled/abaci/*.json
  - scl-directory.md
  - seeds/negentropy-thesis.md
  - seeds/architectural-reset-direction.md
connects-to:
  - seeds/negentropy-thesis.md
  - seeds/architectural-reset-direction.md
  - seeds/numeric-zip-system.md
  - seeds/experience-layer-blueprint.md
  - seeds/elevator-architecture.md
  - seeds/digital-city-architecture.md
  - seeds/city-compiler-architecture.md
  - seeds/data-ethics-architecture.md
  - seeds/operis-architecture.md
supersedes: nothing (first specification)
---

# Wiki as Address Resolution Layer — The Hollow Template on the Open Internet

⚪🟣 — contemplative + precise

## One Sentence

The GitHub Wiki is the external address resolution layer for the 1,680-room city — planting the hollow template as indexed, findable web content so that Google becomes the decompression codec for any zip code encountered in the wild.

---

## Section 1 — What the Wiki Is in the System

The wiki is not a marketing site. It is not documentation. It is infrastructure.

The negentropy thesis (`seeds/negentropy-thesis.md`, Section 2) establishes that a zip code defines the shape of a workout before a single exercise exists in it. The address is not the content. The address is the topology — block sequence, set structure, rest architecture, constraint surface.

The wiki renders that topology as prose. Each zip code page explains what the room's shape is, what constraints govern it, what operators inhabit it, what its neighbors are, how it sits in the city. It does not contain exercises, cues, sets, reps, or any card body content. It is the hollow template expressed as web content.

This means the content boundary between wiki (free) and app (paid) is not a business decision. It is an architectural derivation:

- **Wiki shows topology** — because topology IS the address, and addresses are public by nature
- **App shows furniture** — because furniture IS the instantiation, and instantiation is the product

The boundary is structural. It falls where the system's own layers separate.

---

## Section 2 — Why the Wiki Exists: The Decoder Problem

The zip code is a communication protocol (`seeds/negentropy-thesis.md`, Section 4). Four emojis carry more workout information than a paragraph of natural language. But compression only works if both ends have the codec.

Right now, the codec lives in CLAUDE.md and scl-directory.md. These are repo-internal documents. No one outside the project can decompress a zip code.

The problem: a user encounters ⛽🏛🪡🔵 — on the app, in a text, on social media, in a forum. They Google it. Google returns nothing. The protocol is dead outside the app.

The wiki plants the decoder in Google's index. When someone searches ⛽🏛🪡🔵 or "2123 ppl workout," the wiki page IS the decompression:

> Strength order — 75-85% load, 4-6 reps, 3-4 min rest, CNS high. Basics axis — bilateral, barbell-first, time-tested classics. Pull type — lats, rear delts, biceps, traps, erectors. Structured format — prescribed sets/reps/rest, trackable, repeatable.

The wiki activates the communication protocol for the outside world. Without it, zip-as-shorthand only works between people who already use the app. With it, Google (and Gemini, which scrapes indexed sources) becomes the decompression layer for anyone who encounters a zip code anywhere.

This is not SEO strategy. This is protocol infrastructure.

---

## Section 3 — Negentropy Alignment

The negentropy thesis says: the system absorbs entropy and produces order.

Externally, the wiki absorbs the entropy of "nobody knows what Ppl± is or what these emojis mean" and produces 1,786 pages of indexed, structured, findable knowledge. It is the negentropy engine operating at the internet timescale.

Directional Constraint #3 from the architectural reset (`seeds/architectural-reset-direction.md`, Section 5): "Does it absorb entropy or create it?" The wiki absorbs external entropy (unknown system, zero search results, meaningless symbols) and produces order (rich, navigable, interlinked knowledge pages). It creates no entropy — it does not add unaddressed state, unrouted data, or ad-hoc content.

Directional Constraint #4: "Is it the same principle at a different timescale?" Yes. The constraint solver absorbs user entropy in-session and reorganizes the workout. The rotation engine absorbs user entropy daily and reorganizes tomorrow's recommendation. The wiki absorbs cultural entropy (nobody knows this system exists) and reorganizes the information landscape. Same principle — absorb disorder, produce order — operating at the internet timescale.

---

## Section 4 — What Each Wiki Page Contains

### Zip Code Pages (×1,680) — The SEO Core

Each page is assembled deterministically from compiled zip JSON + SCL constants. No AI generation. No hallucination risk. Pure data assembly.

**Content per page:**

| Section | Source | What It Shows |
|---------|--------|---------------|
| Title | zip-registry + compiled zip | `# ⛽🏛🪡🔵 — Strength · Basics · Pull · Structured` |
| Metadata | zip-registry | Numeric address (2123), deck link, polarity, GOLD eligibility |
| What This Means | SCL constants (rich text) | 4 paragraphs explaining each dial — loading protocol, exercise character, muscle groups, equipment format |
| Operator | compiled zip | Default operator with Latin etymology, guild, contextual meaning |
| Block Sequence | compiled zip | Block sequence with role explanation for each block in this context |
| Constraint Surface | SCL constants + compiled zip | Order×Axis, Order×Color, Axis×Color interaction — what the intersection does to the possibility space |
| Personality | compiled zip | House (primary/secondary/tertiary/anti operators), difficulty class, CNS demand |
| Architecture | compiled zip | Material, atmosphere, shadow character — the room's visual identity |
| City Position | compiled zip | Building, floor, wing, room — where this address sits in the city |
| Navigation | navigation-graph + compiled zip | N/E/S/W neighbors, same-deck siblings, cosine nearest-5, cross-dial tables |
| Abacus Membership | compiled zip | Training profile connections |
| Deck | compiled decks | Link to deck page with deck identity |

**Content boundary (hard rule):**

| Wiki shows (free/topology) | Wiki does NOT show (paid/furniture) |
|---|---|
| Dial meanings and loading parameters | Exercise names or selections |
| Muscle groups and movement patterns | Set/rep prescriptions |
| Block sequence and block roles | Coaching cues |
| Operator etymology and meaning | Card body content |
| Constraint surface descriptions | Workout titles |
| Personality, architecture, palette | Any generated card content |
| Navigation and city position | User-specific data |

### Reference Pages (~106)

| Page Type | Count | Content |
|-----------|-------|---------|
| Order pages | 7 | Full description, loading protocol, CNS character, all zips in this Order |
| Axis pages | 6 | Exercise character, selection bias, ranking rules, all zips in this Axis |
| Type pages | 5 | Muscle groups, movement patterns, all zips in this Type |
| Color pages | 8 | Equipment tier, format character, GOLD access, all zips in this Color |
| Operator pages | 12 | Latin etymology, training verb, contextual meaning, where this operator appears |
| Block pages | 22 | Role, function, how content shifts by Order |
| Deck pages | 42 | Deck identity, 40-cell grid, centroid, guild affinity |
| Home | 1 | System overview, navigation, stats |
| SCL Reference | 1 | Complete emoji dictionary |
| How to Read a Zip Code | 1 | Tutorial: parsing the 4-dial address |
| Master Grid | 1 | 1,680-cell browsable grid |
| Sidebar | 1 | Navigation tree |
| Footer | 1 | Standard footer |

**Total: ~1,786 pages.**

---

## Section 5 — Data Sources (All Verified Present)

| Source | Path | Records | Provides |
|--------|------|---------|----------|
| Zip Registry | `middle-math/zip-registry.json` | 1,680 | emoji/numeric zip, dials, operator, polarity, deck, GOLD |
| Compiled Zips | `middle-math/compiled/zips/{numeric}.json` | 1,680 | Architecture, palette, typography, personality, connections, blocks, weight vector |
| Compiled Decks | `middle-math/compiled/decks/deck-{nn}.json` | 42 | Deck name, centroid, guild affinity, architecture |
| Navigation Graph | `middle-math/navigation-graph.json` | 1,680 | N/E/S/W directional neighbors |
| Design Tokens | `middle-math/design-tokens.json` | 1 | Color palettes, Order typography, tiers, GOLD flags |
| Abacus Profiles | `middle-math/compiled/abaci/abacus-{nn}.json` | 35 | Training profile membership |
| Zip Converter | `scripts/middle-math/zip_converter.py` | — | Emoji↔numeric utilities (reusable) |

Every source exists. Every source is populated. The wiki generator reads JSON and assembles markdown. No AI calls. No hallucination surface.

---

## Section 6 — Rich Text Templates

The wiki's SEO value comes from ~50+ pre-written paragraphs embedded in the generation script as constants. These are the human-readable explanations of what each dial means, written in Operis publication standard tone (direct, technical, human, no motivational filler).

**Template categories:**

- 7 Order descriptions: loading protocol, CNS character, purpose, what it means for the user
- 6 Axis descriptions: exercise character, selection bias, ranking rules, what the axis feels like
- 5 Type descriptions: muscle groups, movement patterns, what the body does
- 8 Color descriptions: equipment tier, format character, GOLD access, session personality
- 12 Operator descriptions: Latin etymology, training verb, contextual meaning, guild identity
- 22 Block descriptions: role, function, how content shifts by Order context
- ~12+ dial interaction templates: what happens when Order meets Axis, Order meets Color, Axis meets Color

**Source for all templates:** `scl-directory.md` and `CLAUDE.md` (authoritative SCL spec). Templates are written once, embedded in the script, and assembled per-page. The compiled zip JSON provides the per-room specifics (personality, architecture, palette, navigation). The templates provide the universal explanations.

---

## Section 7 — Implementation Architecture

### Script: `scripts/generate-wiki.py`

```
generate-wiki.py
├── SCL_CONSTANTS              — Rich text templates for all 61 emojis
│   ├── ORDER_DESCRIPTIONS     — 7 multi-paragraph descriptions
│   ├── AXIS_DESCRIPTIONS      — 6 descriptions
│   ├── TYPE_DESCRIPTIONS      — 5 descriptions
│   ├── COLOR_DESCRIPTIONS     — 8 descriptions
│   ├── OPERATOR_DESCRIPTIONS  — 12 descriptions with Latin etymology
│   └── BLOCK_DESCRIPTIONS     — 22 block role descriptions
├── INTERACTION_TEMPLATES      — Order×Axis, Order×Color, Axis×Color prose
├── load_data()                — zip-registry, compiled zips, compiled decks, nav graph
├── generate_zip_page()        — Single zip page from compiled data
├── generate_zip_pages()       — 1,680 pages (the SEO core)
├── generate_order_pages()     — 7 Order reference pages
├── generate_axis_pages()      — 6 Axis reference pages
├── generate_type_pages()      — 5 Type reference pages
├── generate_color_pages()     — 8 Color reference pages
├── generate_operator_pages()  — 12 Operator pages
├── generate_block_pages()     — 22 Block pages
├── generate_deck_pages()      — 42 Deck pages with 40-cell grids
├── generate_reference_pages() — SCL ref, How-to-Read, Master Grid
├── generate_sidebar()         — _Sidebar.md navigation tree
├── generate_footer()          — _Footer.md
├── generate_home()            — Home.md with system overview + stats
└── main()                     — Orchestration, output dir, file counting
```

### Push helper: `scripts/push-wiki.sh`

GitHub Wiki is a separate git repo (`bigbruddathunda/ppl-plus-ultra.wiki.git`). The push helper clones the wiki repo, copies generated pages, commits, and pushes. The main repo tracks the generation script; the wiki repo tracks the generated output.

### Idempotency

The script is deterministic. Same input JSON → same output markdown. Running it twice produces identical output. This means the wiki can be regenerated at any time from the current compiled data without drift.

---

## Section 8 — What the Wiki Becomes Over Time

### Phase 3+ (now): Static topology encyclopedia

1,786 pages of room descriptions assembled from compiled data. Every zip code searchable. Every dial explained. Navigation graph as hyperlinks. The city rendered as a wiki.

### Phase 4+ (app launch): Living cross-reference

Wiki pages link to the app. App workout rooms link back to the wiki for "learn more about this address." The wiki becomes the educational substrate — free, indexed, always available — that the paid product builds on top of.

### Operis integration

The Operis features zip codes daily. The featured room's wiki page becomes the "read more" destination. The wiki provides depth without requiring Operis to re-explain the SCL every edition.

### Cosmogram layer

When deck cosmograms are populated, deck wiki pages can incorporate cosmogram context — the deep research identity that gives each deck its character. This is supplemental enrichment, not a blocker.

### Community layer

Users share zip codes. The wiki is where non-users land when they encounter a zip code. It converts curiosity into understanding. Understanding converts into app exploration. The wiki is the top of the funnel — but it is genuinely useful on its own, not a teaser.

---

## Section 9 — Directional Constraint Compliance

Every new feature must answer five questions (`seeds/architectural-reset-direction.md`, Section 5):

1. **Does it operate on the zip code address space?** Yes. Every page is a zip code or a dial reference that explains the address space.

2. **Does the constraint hierarchy govern it?** Yes. The wiki describes the constraint hierarchy — Order > Color > Axis > Equipment — as the organizing principle of every room.

3. **Does it absorb entropy or create it?** Absorbs. Converts "nobody knows what these symbols mean" into indexed, structured, navigable knowledge. Creates no unaddressed state.

4. **Is it the same principle at a different timescale?** Yes. The negentropy engine operating at the internet timescale. Same pattern as the constraint solver (in-session), rotation engine (daily), and Operis (weekly).

5. **Does the exercise library have coverage for it?** N/A — the wiki shows topology, not exercises. The content boundary prevents this question from arising.

**The 100-year question:** Would a public encyclopedia of the address space still make sense if the system runs for 100 years? Yes. Addresses are permanent. Topology is permanent. The wiki describes the skeleton, not the flesh. The skeleton does not change.

---

## Section 10 — Internal SEO: The Negentropy IDE Benefit

The wiki is not only external-facing. It functions as an internal reference layer too.

When working inside the repo — generating cards, building Operis editions, writing cosmograms, debugging the constraint solver — the wiki's rich text templates serve as a prose index of what every dial combination means. The act of writing 50+ paragraphs explaining the system to outsiders forces the system to articulate itself clearly to itself.

This is the negentropy thesis applied reflexively: the system gets more internally coherent by explaining itself externally. The wiki is not a downstream artifact. It is a coherence-producing operation.

---

🧮
