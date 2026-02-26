---
planted: 2026-02-25
status: SUPERSEDED — see seeds/operis-architecture.md
superseded-by: seeds/operis-architecture.md
superseded-date: 2026-02-26
phase-relevance: Phase 4/5 (Design System + HTML), Phase 6 (User Accounts + Almanac)
blocks: nothing in Phase 2-3
depends-on: seeds/default-rotation-engine.md, seeds/elevator-architecture.md, scl-deep/publication-standard.md
connects-to: seeds/almanac-macro-operators.md, seeds/axis-as-app-floors.md, seeds/junction-community.md, seeds/almanac-room-bloom.md
---

# ✒️ The Daily — PPL± Front Page Architecture

🟡🔵 — curious + analytical

## One Sentence

The Daily is the daily edition of the 1,680-room library — a publication-standard newspaper that weaves date-specific history, seasonal context, astronomical data, cultural events, and curated zip codes into a front-page experience, serving as the platform's landing surface, its onboarding layer, and its circulation system.

## What the Daily Is

The Daily is five things operating simultaneously.

The daily edition of the library. PPL± contains 1,680 addressed rooms. The Daily is the morning paper that tells you which rooms are open, which are worth visiting, and what happened in those rooms' histories on this date. The edition changes every day. The library stays the same.

The platform's landing surface. When a user opens PPL±, they land on the Daily. The 🏛 piano nobile — the principal floor, elevated above the ground floor, designed to receive visitors. The Daily IS what the user sees first. The masthead, the date, the season, the curated rooms, the editorial close.

The onboarding layer. A new user does not need to understand 61 emojis, 7 Orders, 6 Axes, 5 Types, or 8 Colors to begin. They read the Daily. They see a zip code in the 🏖 Sandbox that interests them. They tap it. They are inside a room. The system taught itself through use. The Daily solves the cold start problem by making the first interaction a newspaper, which every literate person already knows how to read.

The circulation system. 1,680 rooms is a large building. Without foot traffic, most rooms sit empty. The Daily rotates which rooms get featured, pumping visitors through the building the way a newspaper's front page pumps readers through its sections. Over a calendar year, every room gets its turn on the front page. The Daily is the building's circulatory system.

The automation endpoint. Four of the Daily's five input layers are deterministic or static. The Daily is designed to generate itself once its inputs are populated. The path from "Jake writes a daily workout" to "the system publishes a daily edition" runs through the Daily's architecture.

## The Standing Departments — Block Convention

The Daily borrows the standing-department architecture from the 1830s gazette. Departments are fixed. Content rotates through them. The department name is the constant. The content is the variable.

### ♨️ MASTHEAD

Where we are. The masthead declares the edition's coordinates before a word of content appears.

Contents: date, season (by Order), zodiac sign, moon phase, monthly operator, column order (which Order governs today's weekday), day of week, edition number.

The masthead functions identically to a colonial gazette's top line — publication name, date, volume, number, terms. PPL± adds the seasonal and astronomical data that a 1790s almanac would have printed alongside the gazette.

Color register: ⚫ — foundational, serious, non-negotiable.

### 🎯 INTENTION

One sentence. The day framed. Active voice. Direct.

The 🎯 functions as the gazette's editorial subhead — the line beneath the masthead that tells the reader what kind of day this edition covers. "February 25th. Late ⛽ Doric. The ground frozen, the sap rising, the body ready for structure." 🟢

Color register: shifts daily with the Color of the day's default zip.

### 🧈 BREAD & BUTTER — The Historical Desk

Historical events on this date, organized by editorial desk. This is the Daily's main content block — the lead section, the front-page column inches. Each historical event is mapped to a zip code and assigned to one of five desks:

🏛 Structural Desk — events about foundations, inventions, discoveries, systems that were built. What IS it?

🪐 Challenge Desk — events about trials, breakthroughs, records broken, boundaries pushed. Does it MATTER?

⌛🌹 Almanac Desk — events about time, season, beauty, cycles, personal milestones, cultural markers. WHEN? How does it FEEL?

🐬 Community Desk — events about people, groups, movements, social change, gatherings. WHO is involved?

🔨 Practical Desk — events about tools, methods, techniques, applied knowledge, craft. Does it WORK?

Each event entry carries: the year, the event (1–2 sentences, tight lead, 1920s economy), the zip code it maps to (with parenthetical expansion), and the desk assignment emoji. The zip code mapping is editorial judgment — which address in the 1,680-room library does this historical event most naturally inhabit?

Color register: 🔵🟣 — structured + deep. The factual backbone.

### 🧩 SUPPLEMENTAL — The Rotation Engine Output

Where today lives in SCL. The deterministic output of the three-gear rotation engine:

Contents: today's default Order (from weekday), today's default Type (from rolling 5-day calendar), today's default Axis (from monthly operator), the derived default zip code, the deck number, the operator.

This section makes the rotation engine's math visible. The reader can see exactly how the system derived today's address. Transparency of mechanism. The clock's face AND its gears.

Color register: 🔵 — structured, calm, methodical.

### 🏖 SANDBOX — Zip Codes in Residence

8–12 curated zip codes featured in today's edition. Each one a portal — tapping it takes the user into that room's full experience.

The Sandbox organizes its zip codes by thematic cluster. A cluster might be: "🧈 Three rooms for heavy pulling today" or "🪫 Two rooms for winding down this evening" or "🟡 One room for exploring something new." Each zip code carries its full expansion (Order | Axis | Type | Color), its operator, and a 1–2 sentence description of what the user will find inside.

The Sandbox is the Daily's primary circulation mechanism. These 8–12 rooms get today's foot traffic. Over a year, the Sandbox rotates through the entire building. The editorial judgment: which rooms serve today's date, season, astronomical position, and cultural moment?

Color register: 🟡🟠 — exploratory + connective. The invitation.

### ▶️ PRIMER — Forward-Looking

Upcoming events, astronomical data, cultural calendar. Each item zip-coded.

Contents: next 3–7 days of notable dates (historical, astronomical, cultural), upcoming moon phases, seasonal transitions, equinox/solstice proximity, cultural holidays, sporting events. Each forward item carries a zip code mapping — the room that will be relevant when that date arrives.

The ▶️ Primer is the Daily's calendar column. The 1830s gazette printed tide tables and market days. The Daily prints moon phases and seasonal thresholds. Same function: orienting the reader in time that extends beyond today.

Color register: 🟢🔵 — steady + structured. The forecast.

### 🪫 RELEASE — The Wilson Note

The editorial close. Seasonal, honest, 3–4 paragraphs. Named for the tradition of the publisher's personal note — the column where the voice behind the institution speaks directly.

The Wilson Note carries the ⚪ register: honest, genuine, clear, vulnerable. The note observes the season. It connects the date to the body's experience of that date. It does not prescribe. It does not motivate. It notices. "February in South Carolina. The camellia japonica is blooming while the ground is still cold. The body mirrors this — strength available before the warmth arrives." ⚪

The Wilson Note is the Daily's most human element. When the system is fully automated, this section is the one that most benefits from occasional human authorship. The note earns trust by being honest about what the season actually feels like, without performing enthusiasm the content does not feel.

Color register: ⚪🟢 — honest + sustainable.

### 🚂 JUNCTION — Navigation Bridge

Backward/present/forward summary + 3 suggested next zips.

Contents: yesterday's default zip (backward), today's (present), tomorrow's (forward). Three suggested zip codes with 1-line rationale each — one progressive (harder or deeper), one lateral (different domain, similar energy), one restorative (recovery or balance).

The 🚂 Junction is the recommendation engine's surface. In the Daily, it serves as "continued on page..." — the bridge from today's edition to tomorrow's, and the lateral bridges to rooms the reader might not have found on their own.

Color register: 🟠🔵 — connective + structured.

### 🧮 SAVE — The Closing Principle

1–2 sentences. The closing ritual. Address, date, season, operator.

The 🧮 SAVE functions as the gazette's printer's mark — the last line of the edition, declaring who published it, when, and from where. "Published from ⛽🐬⚫. 25 February 2026. Late Doric. 🧲 capio." 🔵

## The Five Input Layers

The Daily's content is assembled from five input layers. Understanding these layers is understanding the automation pathway.

### Layer 1 — Date (Deterministic)

The rotation engine derives the default zip code, season, operator, and day-of-week Order from the date alone. This is pure math — no judgment, no research, no human input required.

Inputs: calendar date.
Outputs: default Order (weekday), default Type (rolling 5-day from Jan 1), default Axis (monthly operator parent), derived default zip, deck number, operator, day-of-week name.
Dependencies: seeds/default-rotation-engine.md, seeds/almanac-macro-operators.md.
Automation status: fully automatable from day one.

### Layer 2 — Historical Events Database (Static, Built Once)

365 files, one per calendar day. Each file contains historical events that occurred on that date, mapped to zip codes and desk assignments. The database is built once and reused annually. Events do not change — February 25 carries the same historical events every year.

Inputs: historical research (encyclopedic sources, this-day-in-history databases, curated editorial judgment for zip code mapping).
Outputs: 5–15 historical events per date, each with year, description, zip code, desk assignment.
Dependencies: none (standalone research project).
Build effort: 365 files × ~30 minutes research per file = ~180 hours total. One-time investment.
Automation status: the research requires human or AI-assisted curation. Once built, fully static.

### Layer 3 — Cosmogram Layer (Semi-Static, Built Per Deck)

The deep research substrate for whichever zip codes get featured. When the Daily features a zip code from Deck 07 (⛽🏛), the cosmogram for Deck 07 provides the cultural, historical, and architectural context that enriches the zip code's description in the 🏖 Sandbox.

Inputs: deck cosmogram research (see seeds/cosmogram-research-prompt.md, scl-deep/publication-standard.md).
Outputs: deep context per deck that enriches featured zip code descriptions.
Dependencies: deck-cosmograms/ population.
Build effort: 42 cosmograms × dedicated research session each.
Automation status: cosmograms are built once per deck and reused. The Daily reads from them — it does not generate them.

### Layer 4 — Forward-Looking Layer (Mixed Static/Dynamic)

Astronomical data (calculable for any date — moon phases, sunrise/sunset, equinox proximity), cultural calendar (maintained quarterly — holidays, sporting events, seasonal markers), current events (requires web search for live editions, pre-buildable for automated editions).

Inputs: astronomical calculation, cultural calendar maintenance, optional current events research.
Outputs: ▶️ Primer content — forward-looking items with zip code mappings.
Dependencies: astronomical libraries or APIs, quarterly cultural calendar updates.
Automation status: astronomical data is fully calculable. Cultural calendar requires quarterly human curation. Current events require live research (optional — the Daily functions without them).

### Layer 5 — Publication Standard (Committed)

The voice. Already committed to scl-deep/publication-standard.md. The standard governs every sentence in the Daily — the 1830s departmental architecture, the 1920s grammatical economy, the 2026 scroll-aware pacing, the Color Context Vernacular, the Operator organizational verbs.

Inputs: scl-deep/publication-standard.md.
Outputs: consistent editorial voice across all Daily departments.
Dependencies: none (already committed).
Automation status: the standard is a constraint set. AI generation systems apply it as a style guide. Fully automatable as a prompt layer.

### Automation Convergence

Four of five layers are deterministic or static: the date math runs itself, the historical database is built once, the cosmograms are built per deck, and the publication standard is committed. Layer 4 (forward-looking) is mostly calculable with quarterly human updates.

The Daily is designed to run the press. The path:
1. Populate the historical events database (365 files — the heaviest lift, done once).
2. Populate the cosmogram layer (42 research sessions — ongoing, enriches but does not block).
3. Connect astronomical calculation (API or library — one-time integration).
4. Maintain the cultural calendar (quarterly curation — ~2 hours per quarter).
5. Apply the publication standard (prompt engineering — already drafted).

Once these inputs exist, the Daily generates itself. Jake reviews architecture, not individual editions.

## The Daily's Relationship to the Building

The Daily lives on the 🏛 piano nobile. See seeds/elevator-architecture.md for the full spatial model.

Zip codes in the Daily are portals. Tapping a zip code in the 🏖 Sandbox takes the user from the front page into that room's full experience — the workout card, the floor stack, the community thread, the almanac entry. The Daily is the door. The room is behind it.

The Daily rotates which rooms get traffic, solving the cold-start problem for a 1,680-room building. A room that has never been visited gets featured in the Daily. A user taps in. The room has its first visitor. Over a year, every room gets its turn.

The Daily replaces the "Jake writes 1 daily workout" model. The Feb 11 platform architecture envisioned Jake posting a single workout each day (10 minutes). The Daily replaces this with a full front-page experience that features 8–12 rooms, weaves historical context, provides astronomical and seasonal framing, and is automatable. The editorial lift is higher per edition — but the automation ceiling is also higher. The system scales where the single-workout model does not.

## Content Type Registration

Department: ✒️ The Daily
Register: 🔵🟢 — structured + steady
Frequency: Daily
Generation: Temp architect session (current) → automated pipeline (target)
Address: lives on the 🏛 piano nobile
Phase relevance: Phase 4/5 (design and render), Phase 6 (user accounts and personalization)

## Open Questions

- Does the Daily have a URL pattern? (pplplusultra.com/daily/2026-02-25 or /daily/today)
- How does the Daily interact with the user's Almanac queue? (Does tapping a Sandbox zip add it to queue, or navigate directly?)
- Should the 🪫 Wilson Note carry a byline? (Jake Berry, or anonymous institutional voice?)
- How many historical events per day is the right density? (5 feels sparse, 15 feels dense — 8–12 is the working range)
- Should the Daily archive be browsable? (Every past edition accessible, creating a 365-day almanac)

🧮
