---
planted: 2026-03-11
status: SEED
phase-relevance: Phase 5/6/7 (UX, Community, Content)
blocks: nothing currently — exploration and discovery layer
depends-on: seeds/home-screen-architecture.md, seeds/digital-city-architecture.md, seeds/elevator-architecture.md, middle-math/navigation-graph.json
connects-to: seeds/character-progression-architecture.md, seeds/life-copilot-architecture.md, seeds/operis-architecture.md, seeds/heros-almanac-v8-architecture.md
extends: seeds/digital-city-architecture.md (adds fog of war, quicksave, easter eggs, seasonal immersion, zone typology, content gating)
legacy-references: GW2 (zone discovery, dynamic events, waypoints, vistas, renown hearts), Zelda overworld map, Wikipedia hyperlinks, Spotify navigation
---

# Exploration and Immersion Architecture — The Living City

🟡🪐 — exploratory + deep

## One Sentence

The 1,680 zip codes are a living city with fog of war discovery, quicksave bookmarks at every address, seasonal tonal shifts, easter egg layers, Wikipedia-style portal rabbit holes, and zone personalities that range from bustling carnivals to quiet dead-ends — all designed to reward curiosity without punishing efficiency.

---

## Section 1 — The GW2 Zone Model Applied

Each zip code is a GW2-style zone with discoverable layers. The zone structures map directly:

| GW2 Element | Ppl± Equivalent | Implementation |
|-------------|-----------------|----------------|
| **Waypoints** | Saved/bookmarked zip codes | User's personal fast-travel network. Grows as they save rooms. Quicksave holds position within a room. |
| **Points of Interest** | Content nodes within a zip code | The tappable buildings on the central map. Each floor (6 Axes) has discoverable POIs. No gameplay gate — pure discovery markers. |
| **Vistas** | Perspective moments | High-level views that show how this zip code connects to others. The "zoom out" moment. Available when specific conditions are met (e.g., visited all 8 Colors of a Type within an Order). Reward: a panoramic view of the deck's full structure. |
| **Renown Hearts** | Completion goals per zip code | Fill a progress bar your way — log a workout, read the almanac entry, contribute to community, explore all floors. Multiple valid paths to "completing" a room. No single required path. |
| **Dynamic Events** | Operis-driven content cycles | Content publishes daily whether the user visits or not. The world is alive. Seasonal events, Operis features, community activity — things happen at zip codes whether you're watching or not. When you arrive, you see what happened. |
| **Hero Challenges** | Skill unlocks / milestone markers | Specific achievements tied to zip codes. Completing a hero challenge at a zip code permanently marks it and contributes to character progression. |

---

## Section 2 — Fog of War

### The Map Starts Dark

On first use, the central map (see `seeds/home-screen-architecture.md`) shows the current zip code and its immediate neighbors. Everything else is fog. The 1,680-room city is dark.

### How Fog Clears

- **Visiting a zip code** clears the fog for that room and reveals its immediate connections in the navigation graph (from `middle-math/navigation-graph.json`)
- **Exploring floors within a zip code** clears depth fog — the 6 Axis layers within a room
- **Operis mentions** partially clear fog for featured zip codes (you see the outline but not the detail until you visit)
- **Junction suggestions** (🚂) from completed workouts show paths to adjacent rooms, clearing fog along the connection

### Fog Persistence

Fog state is persistent per user. Once cleared, it stays cleared. The map is a permanent record of everywhere you've been. Over months, the user's map becomes a unique portrait of their journey through the city.

### Fog Statistics

- Total fog: 1,680 rooms × 6 floors = 10,080 discoverable surfaces
- Percentage complete is visible but not prominent — this is not a completion grind, it's a living record
- Deck-level fog: each deck (40 rooms) has its own completion percentage. Like GW2 zone completion.
- The fog clearing animation should feel satisfying — the map area brightens, reveals detail, shows connections

---

## Section 3 — Quicksave Bookmarks

### The Problem

Zip codes have depth. A user might be 20 pages into a seasonal almanac reading at ⛽🏛🪡🔵, or halfway through a cosmogram deep-dive at 🦋🪐🍗🟣, or in the middle of a community thread at 🐂🐬➕🟡. If they leave and come back, they shouldn't have to re-navigate to their position.

### The Solution

Every zip code holds one quicksave per user. The quicksave captures:
- Which floor (Axis) they were on
- Scroll position / page number within that floor's content
- Last interaction timestamp
- Whether they were mid-workout (paused at a specific block)

### Quicksave Behavior

- **Automatic.** The quicksave updates continuously as the user navigates within a zip code. No manual save action needed.
- **One per zip.** Each zip code holds one position. Returning to that zip code resumes at the saved position.
- **Overwrite on re-entry.** If you return to a zip code and navigate to a different floor, the quicksave updates. The old position is replaced.
- **Visual indicator.** Bookmarked zip codes show a small flag on the central map. Zip codes with active quicksaves (visited recently, have a position saved) show a brighter flag.
- **Quicksave list.** Accessible from the header. Shows all zip codes with active quicksaves, sorted by recency. Tap to jump back to any saved position.

### Why This Matters

The quicksave system enables **rabbit hole navigation**. A user can:
1. Start at today's Operis zip → quicksave at Operis
2. Tap a portal link in the Operis → land at a new zip → quicksave at new zip
3. Explore that zip's almanac floor → find a hyperlink to a third zip → quicksave at third zip
4. Go 20 pages deep into a cosmogram → quicksave at page 20
5. Close the app
6. Reopen → jump back to page 20 of the cosmogram
7. Or jump back to the Operis → still at where they left off there too

Each zip code is a tab that remembers its state. The user's navigation history is a web of open tabs, each holding its position.

---

## Section 4 — Portal System (Wikipedia Hyperlinks)

### Content Is Interconnected

Content within zip codes contains portal links to other zip codes — inline references that function like Wikipedia hyperlinks or academic superscript citations.

### Portal Types

**Inline zip references:**
Text mentions a related zip code. The zip code is clickable. Tapping it spins the dials to that zip and navigates there. The user's quicksave at the origin zip is preserved.

```
"The heavy pull pattern at this address connects to its
counterpart at ⛽🔨🪡🔵 [tap to visit], where the same
muscle groups are trained with a functional bias."
```

**Superscript/subscript citations:**
Deep content (cosmograms, almanac entries, educational content) uses numbered references that link to specific zip codes or external knowledge.

```
"The barbell deadlift has been a training staple since
the early 20th century¹, with its modern programming
codified in the Strength order's structured protocols²."

¹ → links to historical context at ⌛ floor of ⛽🏛🪡🔵
² → links to the cosmogram at 🪐 floor of ⛽🏛🪡🔵
```

**Block-level portals:**
Within a workout card, the 🚂 Junction block already contains suggested next zip codes. These are portals — tapping them navigates directly.

**Floor-level portals:**
Each floor within a zip code can contain cross-floor links. The 🐬 community floor might reference a discussion happening at a different zip code. The ⌛ almanac floor might link to the same date's content at a different Order.

### The Rabbit Hole

Portal links create a web of interconnected content. A user who follows their curiosity can traverse dozens of zip codes in a single session, each one holding their quicksave position. This is the **Library of Babel** principle — everything connects to everything, and the connections ARE the content.

The navigation graph (`middle-math/navigation-graph.json`, 6,720 edges) is the structural backbone. Portal links are the editorial layer on top — hand-authored connections that emerge from content meaning, not just structural adjacency.

---

## Section 5 — Zone Personality Typology

Not all zip codes are created equal. The 1,680 rooms have different densities of content, activity, and personality. This is by design.

### Zone Types

**The Metropolis**
Some zip codes are dense, active, multi-layered. They have bustling community floors, rich almanac entries, deep cosmogram content, popular workouts, and active Operis features. These are the city center zip codes — the rooms that get the most traffic because the rotation engine, Operis, and Junction system all route users there.

Examples: ⛽🏛🪡🔵 (Strength/Basics/Pull/Structured) — a barbell pulling room that everyone visits.

**The Neighborhood**
Most zip codes are neighborhoods. They have the standard features (workout, community thread, almanac entry, personal history) and a moderate level of activity. They're comfortable, familiar, lived-in. Nothing flashy. Everything works.

**The Quiet Street**
Some zip codes are sparse. A 🖼🪐➖⚪ (Restoration/Challenge/Ultra/Mindful) room might have a workout, a thin almanac entry, and an empty community floor. This is not a failure — it's architectural character. Quiet streets exist in every city. They serve people who seek them out.

**The Dead End**
Some zip codes might feel like "what's really different here?" — like 🟡 Fun vs 🟢 Bodyweight variants of the same Type. The difference might be subtle. The dead end is part of the exploration experience. Not every room is a revelation. Some rooms teach you what the differences are by making you look closely. The act of comparison IS the content.

**The Carnival**
Some zip codes act like events — time-limited content, seasonal shifts, festive elements. A 🟡 Fun variant during a seasonal event might have puzzles, challenges, games, or special content that only appears during that period. Carnivals are announced through the Operis and marked on the map.

**The Hidden Garden**
Some zip codes are easter eggs. They look ordinary from the map but contain discovery layers — hidden content, inside jokes, deeper references, cross-zip-code puzzles. These are rewards for explorers who visit every corner.

---

## Section 6 — Seasonal and Environmental Immersion

### The Space Changes

If users opt in, the entire visual environment shifts based on real-world context:

**Seasonal shifts:**
- Spring: warmer colors, growth imagery, lighter map tones
- Summer: bright, saturated, high-energy map compositions
- Autumn: amber, harvest tones, gathering/consolidation imagery
- Winter: cool, sparse, focused, minimalist map compositions

These shifts affect the central map, the vial colors (subtle tinting), and the general UI tone. They do NOT affect content or functionality — only visual atmosphere.

**Weather awareness (opt-in only):**
If the user shares location (consistent with data ethics in `seeds/data-ethics-architecture.md`), the app can reflect local weather. Rainy day? The map has a cooler tone. Sunny day? Brighter. This is atmospheric, not functional.

**Time of day shifts:**
- Morning: fresh, bright, inviting
- Afternoon: warm, productive
- Evening: cooler, winding down
- Night: dark mode, subdued, ⚪ Mindful register

### The Continuity Principle

Despite environmental shifts, the structural layout never changes. Users always know where things are. The 4 dials are always at the bottom. The 8 vials are always above them. The map is always in the center. The header is always at the top.

Immersion comes from tonal shifts, not structural changes. The city changes its lighting and seasonal decorations, not its streets.

---

## Section 7 — Content Gating by Conditions

### Not Everything Is Always Available

Some content requires conditions. This is not paywall gating — this is contextual relevance gating.

**Vial threshold gating:**
Certain content layers become available when a user's vial levels reach a threshold. Example: advanced training theory content (🟣 Precision floor) opens when the user has demonstrated enough engagement with basic content (🔵 Discipline vial above a threshold).

This is GW2 mastery: you unlock ACCESS, not POWER. The content was always there. The user earned the ability to see it.

**Temporal gating:**
Some content is time-locked. Seasonal content appears in season. Historical almanac entries unlock on their dates. The Operis publishes daily. This creates a living calendar — the city has a schedule.

**Metric gating (soft):**
Content that's "too easy" for a user at their current level doesn't disappear — it dims. Like GW2 down-scaling, the content stays relevant but the system signals "you might find more value over here." This is a suggestion, not a lock.

**Burnout protection:**
Content might lock when a user is OVER the maximum engagement threshold. If the 🔴 Output vial is overflowing and the ⚪ Recovery vial is empty, the system might suggest: "This zip code's intensity content is resting. Visit ⚪ content instead." The cup runneth over — the system helps balance it.

This is the philosophical inversion: gating protects the user from imbalance, not from content. Everything is accessible in principle. The gates are guardrails, not walls.

### Condition Communication

When content is condition-gated, the user sees:
- A subtle lock icon with a tooltip explaining the condition
- The condition expressed in plain language: "Visit 3 more 🟢 rooms to unlock this layer"
- No hidden conditions — transparency about what opens what

---

## Section 8 — Easter Eggs and Discovery Layer

### The Hidden City

Easter eggs are content, connections, or experiences that are not marked on the map and not announced in the Operis. They exist for users who explore thoroughly.

### Types of Easter Eggs

**Cross-zip puzzles:**
A sequence of zip codes, visited in a specific order, reveals a hidden message or unlocks a special view. The clues are embedded in content across multiple rooms. Like Call of Duty easter egg hunts — a community effort.

**Cosmogram deep links:**
Certain phrases or concepts in cosmogram content link to unexpected zip codes. Following these links opens content that contextualizes the cosmogram in a new way.

**Date-specific discoveries:**
On certain dates (historical significance, astronomical events, seasonal transitions), specific zip codes have additional content that only appears that day. Announced nowhere. Found by those who visit.

**Operator resonance:**
When a user's House operator matches the default operator of a zip code, subtle additional content appears — a brief note, a different map composition detail, a "this room recognizes you" moment. Not functional. Atmospheric.

**Completion rewards:**
Visiting all 40 rooms in a deck (all 5 Types × 8 Colors for one Order × Axis combination) unlocks a deck-level vista — a panoramic view of the deck's identity, its place in the system, its connections to other decks. Like GW2 world completion for a zone.

### Easter Egg Philosophy

Easter eggs are never essential. A user who never discovers an easter egg has a complete experience. Easter eggs reward the kind of user who reads footnotes, checks every corner, and follows their curiosity past the obvious path. They are love letters to attentive users.

Community discovery of easter eggs becomes community content. "Has anyone found the hidden connection between Deck 07 and Deck 37?" — this is the kind of discussion that builds on the 🐬 community floor.

---

## Section 9 — Healthy Engagement Patterns

### The Anti-Addiction Architecture

Ppl± is designed to promote healthy phone usage, not maximize engagement metrics.

**Time-of-day modes:**

| Mode | Trigger | Behavior |
|------|---------|----------|
| Morning | 5am–9am (configurable) | Full access. The Operis is fresh. Today's workout is featured. |
| Work/School | User-set hours | Reduced depth. Quick access to workout and tools. No rabbit hole portals. No community floor. Distraction-limited. |
| Evening | 6pm–10pm (configurable) | Full access returns. Community active. Exploration enabled. |
| Night | 10pm–5am (configurable) | ⚪ Mindful register only. Dark mode. Recovery content surfaced. Engagement depth limited. "Go to sleep." |

**Session duration awareness:**
After 45 minutes of continuous use, a subtle note: "You've been exploring for 45 minutes. The city will be here tomorrow." Not a popup. Not a gate. A note. Like a librarian mentioning the time.

**Rabbit hole breadcrumbs:**
After 5+ portal jumps in a session, the quicksave list shows a breadcrumb trail: "You started at ⛽🏛🪡🔵 → went to ⛽🔨🪡🔵 → then to 🦋🔨🪡🔵 → then to..." This helps the user see how far they've wandered and find their way back. Not limiting — orienting.

**Business hours metaphor:**
The city has business hours. Certain features operate on a schedule that mirrors real-world rhythms. The Operis publishes in the morning. Community moderation is active during the day. Evening brings reflection content. Night brings rest. The system has a circadian rhythm.

This is not engagement optimization. This is civic design. A well-designed city has hours. Shops close. Parks are lit at night. The system respects the user's time by having its own relationship to time.

---

## Section 10 — Responsive Exploration

### Mobile: Touch-First Discovery

Exploration on mobile is thumb-driven. Spin dials, tap map elements, swipe between floors, hold vials for hub access. The fog of war clears with each tap. The central map is the primary exploration surface.

### Desktop: Keyboard + Click Discovery

On desktop, the map is larger and shows more detail. Keyboard shortcuts for dial spinning (arrow keys). Click to enter rooms. Hover to preview zip code identity. The fog of war map becomes a rich, zoomable canvas.

### Cross-Device Continuity

Fog state, quicksaves, and vial levels sync across devices. Start exploring on your phone, continue on desktop. The city is the same city regardless of how you enter it.

---

## Open Questions

1. **Map generation.** How are zip code maps procedurally generated from weight vectors? Template-based? Algorithmic? Hand-authored per deck?
2. **Fog of war granularity.** Is fog binary (visited/unvisited) or gradient (partially explored)?
3. **Easter egg authoring.** Who creates easter eggs? Automated from content analysis? Hand-placed by Jake? Community-submitted?
4. **Mode customization.** How granular are the time-of-day modes? Per-hour? Per-activity? User-defined presets?
5. **Community discovery.** How are community-discovered easter eggs shared without spoiling the experience for others?
6. **Burnout protection thresholds.** What vial levels trigger protective gating? How is this communicated without feeling restrictive?
7. **Carnival scheduling.** How are carnival/event zip codes announced and managed? Operis-driven? Calendar-driven? Both?
8. **Dead end value.** How do we make "boring" zip codes feel intentional rather than forgotten? What distinguishes a deliberately quiet room from an underdeveloped one?
9. **Portal link density.** How many portal links per content surface? Too many = overwhelming. Too few = disconnected. What's the target?
10. **Down-scaling for experienced users.** How does GW2-style down-scaling work for users revisiting basic content? Does the workout change? Or just the contextual framing?

---

🧮
