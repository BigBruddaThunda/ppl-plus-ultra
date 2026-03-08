---
title: Digital City Architecture
status: SEED
planted: 2026-03-08
category: vision
depends-on: seeds/abacus-architecture.md, seeds/elevator-architecture.md, seeds/operis-architecture.md, seeds/experience-layer-blueprint.md
---

# Ppl± as a Digital Traditional City

## Thesis

Ppl± is not a workout app. It is a digital traditional city where the workout is the anchor tenant that gets people to show up daily. Everything else — the daily newspaper, the community spaces, the knowledge archives, the personal history, the seasonal rhythms — exists because people are already there, training.

The entire system is built on the same organizational principles that traditional cities use: shared language, recurring daily rhythms, neighborhoods with distinct character, civic infrastructure that serves everyone equally, and public spaces where people encounter each other through proximity rather than algorithmic curation.

## The City Map

| City Element | Ppl± Component | SCL Address |
|-------------|---------------|-------------|
| Buildings (7) | Orders | 🐂 ⛽ 🦋 🏟 🌾 ⚖ 🖼 |
| Floors (6 per building) | Axes | 🏛 🔨 🌹 🪐 ⌛ 🐬 |
| Wings (5 per floor) | Types | 🛒 🪡 🍗 ➕ ➖ |
| Rooms (8 per wing) | Colors | ⚫ 🟢 🔵 🟣 🔴 🟠 🟡 ⚪ |
| Total rooms | 1,680 | 7 × 6 × 5 × 8 |
| Total content surfaces | 10,080 | 1,680 rooms × 6 floors |

## Anchor Tenant: The Workout

The workout lives on the piano nobile — the arrival floor (🏛 Basics / Firmitas). When you enter a room, you see the workout first. It fills the screen. It is the reason you came. But scroll down and the room reveals depth: tools below, time above, community around, personal history above that, and the cosmogram penthouse at the top.

The workout is to Ppl± what the market is to the traditional piazza — the daily activity that creates foot traffic. Everything else benefits from that traffic.

## The Operis: Daily Newspaper

The Operis is the city's daily publication. It arrives every morning. It is tied to the day's Order (which building the city activates), the season (which operator governs the month), and the community's current state.

Like a local newspaper, the Operis:
- Covers what happened (training recaps, community highlights)
- Previews what's coming (tomorrow's featured rooms, upcoming seasonal shifts)
- Educates (exercise deep dives, movement science, SCL literacy)
- Connects (featured community contributions, partner highlights)

The Operis is not algorithmic content. It is editorial content published on a deterministic schedule. The same date always produces the same edition structure. The content within that structure is curated.

## Neighborhoods: The Abacus Layer

Each of the 35 training archetypes (abaci) is a neighborhood. When a user selects their abaci, they are choosing where they live. A powerlifting neighborhood has different daily rhythms, different community, different featured rooms than a yoga-and-mobility neighborhood. But they share the same buildings, the same floors, the same civic services.

See `seeds/abacus-architecture.md` for the full neighborhood model.

## Community Spaces

Community threads at specific zip codes are coffee shops. They exist because people frequent the same rooms. A community thread at ⛽🏛🪡🔵 (Strength/Basics/Pull/Structured) connects people who regularly train heavy barbell pulls in structured formats. They have something in common — the room brought them together.

This is proximity-based community, not interest-graph community. You meet people because you're both in the same room, not because an algorithm decided you're similar.

## Knowledge Archives: Cosmograms

Each of the 42 decks has a cosmogram — a deep research document that connects the deck's training identity to broader cultural, historical, and scientific context. Cosmograms are the city's museums. They're free, open, and available to anyone who enters the building.

See `deck-cosmograms/README.md` for the cosmogram system.

## The Almanac: Local History

The ⌛ Temporitas floor at each zip code shows training history, seasonal context, and temporal rhythms. At the city level, the almanac is the local history section of the library — it knows what happened on this date last year, what the season requires, and how the community's patterns have evolved.

## The 8 Colors as Cultural Protocol

The 8 SCL Colors have potential beyond the platform as a cultural communication protocol. Punctuating text messages and social media with color state markers tells people the register of what they're reading:

- ⚫ = "I'm teaching / explaining"
- 🟢 = "This is self-contained / no dependencies"
- 🔵 = "This is structured / systematic"
- 🟣 = "This requires precision / depth"
- 🔴 = "Maximum effort / high stakes"
- 🟠 = "This is a sweep / rotation / round-up"
- 🟡 = "This is playful / exploratory"
- ⚪ = "This is reflective / mindful"

This is a natural extension of how the Colors already function inside the system — they're cognitive postures, not just equipment tiers.

## The Envelope System

The envelope is condition-based postal delivery. Content at a zip code is filtered by the user's current state — their region, season, training history, equipment access, time of day, and selected abaci. The same room renders differently for different people because the envelope carries different conditions.

This is not personalization in the recommendation-engine sense. It is context-sensitivity — the room responds to who is standing in it, like a building that adjusts its lighting based on the time of day.

## MySpace Principle

Each zip code is potentially a canvas. The room's visual appearance is driven by the weight vector and CSS custom properties — but the user could mod their own rooms. Change the gradient, adjust the typography, add their own background. Like a MySpace page, but built on a coherent architectural system instead of arbitrary HTML.

Future extension: Wilson (the Ppl± voice assistant) could serve as an AI design assistant — "Wilson, make this room feel more like a garage gym" — and the system adjusts the weight vector overrides accordingly. This is RAG + design system, not template selection.

## Natural Order

The system uses the same organizational principles nature uses:
- **7 Orders** map to the 7 classical planets / 7 days of the week
- **12 Operators** map to 12 months with agricultural rationale
- **Coprime cycles** (7-day Order × 5-day Type) create 35-day super-cycles that mirror astronomical harmonics
- **Seasonal arcs** mapped to 4-month inhale → 4-month exhale → 2-month catch-breath → 2-month close
- **The liberal arts** mapped to the 7 Orders as developmental phases (Trivium for Foundation/Strength/Hypertrophy, Quadrivium for Performance/Full Body/Balance/Restoration)

The system doesn't simulate nature. It uses the same mathematical relationships nature uses because those relationships produce sustainable, non-repeating, self-organizing patterns.

## Scale

Jake builds from maximum-scale architecture backwards to MVP. The project is designed as what Ppl± should be in 100 years, deconstructed into buildable pieces. Inch by inch makes up the elephant's trunk. The architecture exists at full scale. The implementation grows into it.

---

🧮
