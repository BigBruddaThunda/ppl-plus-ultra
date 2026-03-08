---
planted: 2026-02-26
status: SEED
phase-relevance: Phase 4/5 (Design System + HTML), Phase 6 (User Accounts + Almanac)
blocks: nothing in Phase 2-3
supersedes: seeds/daily-architecture.md
depends-on: seeds/default-rotation-engine.md, seeds/elevator-architecture.md, scl-deep/publication-standard.md
connects-to:
  - seeds/almanac-macro-operators.md
  - seeds/axis-as-app-floors.md
  - seeds/content-types-architecture.md
  - seeds/operis-prompt-pipeline.md
  - seeds/operis-researcher-prompt.md
  - seeds/operis-content-architect-prompt.md
  - seeds/operis-editor-prompt.md
  - seeds/operis-builder-prompt.md
---

# ✒️ Ppl± Operis — Publication Architecture

🟡🔵 — curious + analytical

## One Sentence

Ppl± Operis is the daily editorial publication of the 1,680-room library — a gazette that weaves date-specific history, seasonal context, astronomical data, and curated zip codes into a front-page experience, serving simultaneously as the platform's landing surface, its onboarding layer, its circulation system, and its generation engine.

## The Name

Operis. Latin genitive of *opus*: "of the work." The Operis is the voice of the work — the publication that speaks from the building, not merely about it.

Phonetically in English: "off the press." The sound of the press releasing the edition.

Associative field: opera (the produced work), opus (the work itself), operate (the work in motion). The same root running through action, output, and the act of running a press.

The platform's daily publication is not "The Daily." It is the Operis — the editorial organ of the Ppl± system, published from the 🏛 piano nobile, dated and addressed, standing departments fixed, content rotating.

See `seeds/operis-naming-rationale.md` for the full etymology and naming decision.

---

## What the Operis Is

Five things operating simultaneously.

**The daily edition of the library.** Ppl± contains 1,680 addressed rooms. The Operis is the morning paper that tells you which rooms are open, which are worth visiting, and what happened in those rooms' histories on this date. The edition changes every day. The library stays the same.

**The platform's landing surface.** When a user opens Ppl±, they land on the Operis. The 🏛 piano nobile — the principal floor, elevated above the ground floor, designed to receive visitors. The Operis IS what the user sees first. The masthead, the date, the season, the curated rooms, the editorial close.

**The onboarding layer.** A new user does not need to understand 61 emojis, 7 Orders, 6 Axes, 5 Types, or 8 Colors to begin. They read the Operis. They see a zip code in the 🏖 Sandbox that interests them. They tap it. They are inside a room. The system taught itself through use. The Operis solves the cold-start problem by making the first interaction a newspaper, which every literate person already knows how to read.

**The circulation system.** 1,680 rooms is a large building. Without foot traffic, most rooms sit empty. The Operis rotates which rooms get featured, pumping visitors through the building the way a newspaper's front page pumps readers through its sections. Over a calendar year, every room gets its turn on the front page.

**The generation engine.** Every edition of the Operis features 8–12 zip codes. Each featured zip code is a room that must have content before it can receive visitors. This creates a natural generation queue: the Operis cannot feature a room whose card is EMPTY. As the Operis publishes, it forces card generation. The pipeline runs forward. See "The Construction Vehicle Pipeline" below.

---

## The Business Model Layer

The Operis is the free publication. The rooms are the paid product.

The Operis front page is publicly readable — the masthead, the historical desk, the calendar, the Wilson Note. Every user, subscriber or not, receives the editorial content of the day.

The 🏖 Sandbox zip codes are portals. Tapping one takes a user to the room's door. The door opens with a Tier 1 subscription ($10/month). The content behind the door — the workout, the community thread, the personal history layer, the cosmogram — requires the Library Card.

This is the newsstand model. The front page is visible through the glass. You pay for what's inside.

The Operis drives subscription by making the front page genuinely useful without requiring a subscription, while making the content behind each portal worth paying for. The editorial quality of the Operis is the marketing.

---

## The Weekly Editorial Cadence

The Operis follows a 7-day editorial cycle mapped to the 7 SCL Orders and the 7 Liberal Arts. Each day of the week carries a specific Order, a Liberal Art discipline, and an editorial character. This is not decorative — it determines which standing departments are active and what editorial lens is applied to the day's content.

The Liberal Arts split into two tiers: the Trivium (Grammar, Logic, Rhetoric — language and thought) and the Quadrivium (Arithmetic, Geometry, Music, Astronomy — number and cosmos). Monday through Wednesday carry the Trivium. Thursday through Sunday carry the Quadrivium.

---

### Monday — 🐂 Foundation / Grammar — The Reset

Order: 🐂 Foundation. Liberal Art: Grammar (the Trivium's first discipline — the study of structure, form, the elements of language before meaning is assembled).

Editorial character: The week opens by naming its parts. Grammar is inventory — what exists, what is true, what the terms mean. The Monday Operis is a returning, a re-grounding. After Sunday's long view, Monday does not sprint. It names. It places. It confirms.

Department activation: ♨️ Masthead (always), 🎯 Intention, 🔢 Fundamentals, 🧈 Historical Desk (Grammar lens: events that named, defined, classified, or established structure), 🏖 Sandbox (foundational zip codes — 🐂 Order emphasized), 🚂 Junction.

Tonal register: ⚫🟢 — foundational, naming register. Direct without urgency. The week begins with structure.

---

### Tuesday — ⛽ Strength / Logic — The Work Day

Order: ⛽ Strength. Liberal Art: Logic (the Trivium's second discipline — the study of valid inference, argument, and the structure of reasoning).

Editorial character: Logic is demonstration — the movement from premise to conclusion, the proof of what holds. The Tuesday Operis does not describe; it argues. It selects historical events that demonstrate causal chains, turning points, decisions with consequence. The reasoning is shown, not summarized.

Department activation: ♨️ Masthead (always), 🎯 Intention, ▶️ Primer, 🧈 Historical Desk (Logic lens: events that proved a point, turned a corner, demonstrated consequence), 🧩 Supplemental, 🏖 Sandbox (⛽ Order emphasized), 🚂 Junction.

Tonal register: 🔵🟣 — structured, precise. Sentences shorter. Conclusions earned, not announced.

---

### Wednesday — 🦋 Hypertrophy / Rhetoric — The Accumulation Day

Order: 🦋 Hypertrophy. Liberal Art: Rhetoric (the Trivium's third discipline — the study of effective communication, persuasion, and the arrangement of language for an audience).

Editorial character: Rhetoric is volume with purpose — the accumulation of evidence, the layering of examples, the structure that moves the reader. The Wednesday Operis is the densest edition. More historical events. More zip codes in the Sandbox. The Wilson Note is the most fully developed. Wednesday earns its length.

Department activation: ♨️ Masthead (always), 🎯 Intention, ▶️ Primer, 🧈 Historical Desk (Rhetoric lens: events involving communication, publication, oratory, persuasion, or cultural production), 🗿 Sculpt (secondary historical material), 🪞 Vanity (appearance-driven zip codes in Sandbox), 🏖 Sandbox (🦋 Order and 🌹 Axis emphasized, maximum zip count — 10–12), 🪫 Release, 🚂 Junction.

Tonal register: 🟡🔵 — exploratory within structure. Wednesday is allowed to breathe. The only day where the editorial voice can open its register.

---

### Thursday — 🏟 Performance / Arithmetic — The Measurement Day

Order: 🏟 Performance. Liberal Art: Arithmetic (the Quadrivium's first discipline — the study of pure number, quantity, and the relationships between quantities).

Editorial character: Arithmetic is measurement — not counting for its own sake, but counting in order to know. The Thursday Operis records. It looks at the week's progress. It identifies numbers that matter: distances crossed, records broken, populations counted, years elapsed. The editorial is tighter on Thursdays. The Sandbox features fewer zip codes. Test. Record. Leave.

Department activation: ♨️ Masthead (always), 🎯 Intention, 🪜 Progression, 🧈 Historical Desk (Arithmetic lens: events involving measurement, records, mathematics, quantified firsts), 🏖 Sandbox (🏟 Order emphasized, 8 zip codes maximum), 🚂 Junction.

Tonal register: 🔵🟣 — methodical, economical. Numbers are presented without narrative inflation. The record stands or it does not.

---

### Friday — 🌾 Full Body / Geometry — The Integration Day

Order: 🌾 Full Body. Liberal Art: Geometry (the Quadrivium's second discipline — the study of space, form, proportion, and the relationships between shapes).

Editorial character: Geometry is integration — the study of how parts relate to form a whole. Friday is the week's integration day. The historical events selected show how things fit together, how patterns resolved, how separate movements became one. The Sandbox emphasizes 🌾 Full Body zip codes — workouts that flow as one unified pattern.

Department activation: ♨️ Masthead (always), 🎯 Intention, 🎼 Composition, 🧈 Historical Desk (Geometry lens: events about synthesis, architecture, integration, completed projects), 🏖 Sandbox (🌾 Order emphasized — integration, full-body, flowing), 🪫 Release, 🚂 Junction.

Tonal register: 🟢🔵 — sustainable, connected. Friday's editorial voice holds things together. No urgency. The week's work is completing itself.

---

### Saturday — ⚖ Balance / Music — The Workshop Day

Order: ⚖ Balance. Liberal Art: Music (the Quadrivium's third discipline — the study of proportion in time, ratio, harmony, the mathematics of the heard).

Editorial character: Music is proportion in motion — the relationships between notes across time that create harmony or dissonance. Saturday is the workshop. The editorial lens looks for asymmetries, corrections, overlooked patterns, and the adjustments that create coherence. The Sandbox on Saturdays features ⚖ Balance zip codes — targeted, corrective, addressing specific gaps.

Department activation: ♨️ Masthead (always), 🎯 Intention, 🏗 Reformance, 🧈 Historical Desk (Music lens: events about proportion, correction, cultural harmony, tuning — literal and figurative), 🌎 Exposure, 🏖 Sandbox (⚖ Order and ⌛ Axis emphasized), 🪫 Release, 🚂 Junction.

Tonal register: ⚪🟢 — honest, proportional. Saturday does not perform energy. It works.

---

### Sunday — 🖼 Restoration / Astronomy — The Long View

Order: 🖼 Restoration. Liberal Art: Astronomy (the Quadrivium's fourth discipline — the study of celestial bodies, cycles, and the ordering of time across large spans).

Editorial character: Astronomy is the longest perspective — the study of cycles that dwarf a human life. Sunday is the long view. The editorial reaches beyond the week, beyond the season. The historical events selected operate at the largest scale: civilizations, epochs, discoveries that changed humanity's understanding of its position. The Wilson Note is at its most reflective. The Sandbox features 🖼 Restoration zip codes — the quietest rooms in the building.

Department activation: 🎯 Intention (opens Sunday — not ♨️ Masthead first), 🪫 Release, 🧈 Historical Desk (Astronomy lens: events of long cycles, celestial discoveries, civilizational scope), 🧬 Imprint, 🏖 Sandbox (🖼 Order and ⚪ Color emphasized — minimum zip count, maximum depth), 🚂 Junction, 🧮 SAVE (extended on Sundays — the week closes here).

Tonal register: ⚪🟢 — honest, slow, spacious. Sunday's editorial voice does not rush. The long view requires patience.

---

## The Standing Departments

17 departments. Not all active in every edition. The Order of the day determines which departments run. Some departments are permanent fixtures. Others activate by Order, Axis, or editorial judgment.

| Department | Emoji | Always Present | Order Activations |
|------------|-------|---------------|-------------------|
| Masthead | ♨️ | Yes (except 🖼 Sunday) | All Orders |
| Intention | 🎯 | Yes | All Orders |
| Fundamentals | 🔢 | No | 🐂 Monday |
| Primer | ▶️ | No | ⛽ Tuesday, 🦋 Wednesday |
| Composition | 🎼 | No | 🌾 Friday |
| Reformance | 🏗 | No | ⚖ Saturday |
| Historical Desk | 📰 | Yes | All Orders (lens shifts by Liberal Art) |
| Educational Feature | 📖 | Yes | All Orders (featured lane from content brief) |
| Seasonal Desk | 🌾 | Partial | 🌾 Friday, ⚖ Saturday, 🖼 Sunday (folds into Masthead Mon–Thu) |
| Tool Floor | 🔨 | No | ⛽ Tuesday, 🦋 Wednesday, ⚖ Saturday |
| Rooms of the Day | 🏛 | Yes | All Orders (13 rooms: 8 siblings + 5 Content Rooms) |
| Sandbox Notice | 🏖 | No | 🐂 Monday |
| Wilson Note | 🌡️ | Yes | All Orders |
| Junction Bridge | 🚂 | Yes | All Orders |
| Cosmogram Reference | 🌌 | Conditional | All Orders when deck cosmogram is populated (folds otherwise) |
| Reader's Almanac | 📅 | No | 🖼 Sunday |
| Letters | ✉️ | No | Future department — not yet active |

Department names and activation conditions here match the operational matrix in `seeds/operis-prompt-pipeline.md`. If there is a discrepancy between the two documents, the pipeline document's matrix is the operational implementation; this table is the architectural source.

**Zip count by Order:**
- 🐂 Monday: 8–10 zip codes
- ⛽ Tuesday: 8 zip codes
- 🦋 Wednesday: 10–12 zip codes (maximum density)
- 🏟 Thursday: 6–8 zip codes (minimum — test, record, leave)
- 🌾 Friday: 8–10 zip codes
- ⚖ Saturday: 8 zip codes
- 🖼 Sunday: 6–8 zip codes (minimum — depth, not breadth)

---

## The Operis ↔ Cosmogram Feedback Loop

The Operis and the Cosmogram layer are in a generative relationship. They feed each other.

**Operis → Cosmogram:** When the Operis features a zip code from a deck whose cosmogram is not yet populated, the edition's Historical Desk content for that zip code is thin — the general SCL spec, no deep context. This is visible to any reader who knows the building. The thinness of the coverage is an implicit production note: this cosmogram needs to be built.

**Cosmogram → Operis:** When a cosmogram is populated for a deck, the Operis can feature that deck's zip codes with full depth — the historical events mapped to the zip, the cultural context, the architectural rationale. The Historical Desk content becomes rich. The Wilson Note can draw from the cosmogram's material.

**The feedback loop in practice:** The Operis editorial team (Jake, and eventually the automated pipeline) uses the depth of available cosmogram coverage as one signal for which zip codes to feature. Decks with populated cosmograms get richer features. This creates natural pressure to populate cosmograms for frequently featured decks.

The Operis does not block on cosmograms. An edition can feature any zip code with only SCL spec coverage. But the quality ceiling is lower without cosmogram depth. The feedback loop is an incentive, not a dependency.

---

## The Construction Vehicle Pipeline

The Operis is a generation engine disguised as a publication.

Each edition features 8–12 zip codes in the 🏖 Sandbox. Each featured zip code must have a GENERATED or CANONICAL card before the edition can go to press. If the card is EMPTY — a stub — the zip code cannot be featured. The edition must feature a different zip code.

This means: **every edition of the Operis is a generation pressure event.**

The editorial team selects 12–15 candidate zip codes for the Sandbox. They check the card status. Any EMPTY stubs must be generated before those zip codes can be featured, or the editorial team selects replacements. Over time, the Operis's editorial appetite clears the EMPTY stubs.

**Generation rate:**
- 8–12 zip codes forced per edition
- 7 editions per week
- 56–84 zip code checks per week
- Of those, some are already GENERATED (repeat features) and some are new
- Conservative estimate of new generations forced: 24–48 cards per week in active production

At 48 cards per week, the remaining 1,600 cards are complete in approximately 33 weeks of production. The Operis runs the generation pipeline as a side effect of publishing.

This is the construction vehicle model: the Operis is the truck that clears the road as it drives. The generation pipeline is not a separate operation from publishing — it IS publishing.

---

## The Five Input Layers

Carried forward from the original daily-architecture.md specification. The Operis assembles from five input layers:

**Rotation Engine Version: V1.0** — per `seeds/default-rotation-engine.md`. This version tag is embedded in all Operis prompt files and edition front-matter. When the rotation engine is updated, increment this version across all references: this document, `seeds/operis-prompt-pipeline.md`, and all four prompt seed files.

**Layer 1 — Date (Deterministic):** The rotation engine (V1.0) derives the default zip code, season, operator, and day-of-week Order from the date alone. Pure math.

**Layer 2 — Historical Events Database (Static, Built Once):** 365 files, one per calendar day. Each contains 5–15 historical events mapped to zip codes and desk assignments. Built once, reused annually.

**Layer 3 — Cosmogram Layer (Semi-Static, Built Per Deck):** Deep research substrate for featured zip codes. When the Operis features a zip from a populated-cosmogram deck, the description is rich. When the cosmogram is a stub, coverage is thin.

**Layer 4 — Forward-Looking Layer (Mixed Static/Dynamic):** Astronomical data (calculable), cultural calendar (quarterly curation), current events (optional web research).

**Layer 5 — Publication Standard (Committed):** `scl-deep/publication-standard.md`. The voice. Applied as a style guide to every sentence.

Four of five layers are deterministic or static. The Operis is designed to generate itself once inputs are populated.

---

## Temporal Context — Reverse-Weight Resolution

The rotation engine produces a default zip code for any given date. That default is the starting point, not the final answer.

The Intention department frames today as the resolution between yesterday's session and tomorrow's highest-weighted candidate. The reader does not see this framing as system logic — they see it as editorial coherence: Thursday is the day you find out what Wednesday built; today is the hinge between what was done and what is coming.

The featured Sandbox room is the reverse-weight resolution room — the zip code that maximizes preparation for tomorrow's session while minimizing conflict with yesterday's load. The selection logic runs before the edition is composed. It shapes the Sandbox from behind. It never appears in the edition text.

The algorithm is specified in `middle-math/rotation/reverse-weight-resolution.md`. Its editorial implication: the Operis is not a flat daily list of rooms. It is a triangulated response to the week's arc. Every featured room is in a specific position relative to yesterday and tomorrow. The reader feels this without being told why.

---

## Front Page Card — Broadsheet Layout

The edition opens with the Front Page Card — a screenshottable top-of-page surface containing the masthead, the almanac, and the table of contents. A screenshot of this card is a complete daily summary, self-contained and legible without prior knowledge of the system.

**Layout**: Masthead on the left. Almanac box on the right. Contents below both. Symbol map at the bottom of the card.

**Masthead (left)**:

```
PPL± Operis
[4-emoji daily zip code]
± [Day of week], [Full date]
Deck [number] · [operator emoji] [latin name] · [liberal art]
```

The liberal art maps from the weekday: Mon=Grammar, Tue=Logic, Wed=Rhetoric, Thu=Arithmetic, Fri=Geometry, Sat=Music, Sun=Astronomy.

**Almanac Box (right)**:

A dense, code-block-sized rectangle containing three bands of information separated by horizontal rules:

Band 1 — Sky: Sunrise, sunset, moon phase name, moon illumination percentage, total daylight hours, daily daylight gain or loss.

Band 2 — Season: Days to next equinox or solstice, seasonal position (e.g., "Last day of meteorological winter"), 2–3 short agricultural observations appropriate to the date and Northern Hemisphere growing cycle.

Band 3 — Navigation: Yesterday's zip code with day name. Tomorrow's zip code with day name.

Every symbol in the almanac box is tappable in the experience layer — each pops a plain-language definition on tap. The symbol map at the bottom of the card makes the screenshot self-contained: a reader who receives the image can decode every symbol without prior knowledge.

**Contents (below masthead and almanac)**:

The table of contents as navigation. Every line is a tap target in the experience layer. Format: department emoji followed by department name. For the Historical Desk, article headlines appear indented below. For the Rooms section, all zip codes are listed with their human-readable room titles, the featured room marked ★.

**Symbol Map (bottom of card)**:

A compact legend decoding every symbol used on the front page card. Two to three columns, plain language. The symbol map makes the card fully self-contained — a person who receives a screenshot can read it without prior knowledge of SCL, Orders, Axes, Types, or Colors.

---

## Depth Standard

Target length: 2,500–4,500 words per edition.

The Historical Desk carries 30–40% of total word count. It is the heart of the edition — 2–4 full articles, each 200–500 words, written as newspaper feature pieces. Each article has a headline, a lede, a body with specific dates and names and measurements, and a pivot that connects the historical material to the body's reality without announcing the connection.

Sandbox room descriptions run 80–150 words of lived-space prose. The featured room receives 150–250 words. The description must pass the lived-space test: could someone who has never heard of Ppl± read this and understand what workout they would get? If not, it contains system-speak and must be rewritten.

The Wilson Note references one concrete element from the current edition — a room, a historical fact, a seasonal observation. It is never generic. If the Wilson Note could be published in any edition on any date, it fails.

Every sentence passes the newspaper test: would a copy editor at a serious publication let this through? If a sentence would require a footnote explaining the system, it fails. If a claim about exercise or anatomy cannot be traced to exercise science, it fails. If a sentence could be deleted without the reader losing information, delete it.

---

## Age-Neutral Register

The Operis is readable by a literate teenager and a retired architect in the same edition. Both must find it worth reading. Neither must feel spoken down to or excluded.

No youth-culture signaling: no platform-native idiom, no meme register, no generational reference. No boomer nostalgia: no "back in the day," no culture-war framing, no condescension toward new practices. The register is the register of competence — factual, specific, warm, and respectful of the reader's intelligence regardless of age.

No dopamine-design cadence: no exclamation-heavy headers, no emoji-stuffed sentences, no hype rhythm. The edition reads like a broadsheet, not a push notification. An adult reading on their phone at 6am with coffee should feel like they picked up a well-edited newspaper. A teenager reading it at lunch should feel like they are being treated as intelligent.

The polarity framework (Preparatory/Expressive) is valid system architecture in the repo. It belongs in scl-deep files and weight tables. It does not belong on the Operis front page or in edition text, where it reads as infrastructure leaking onto the newspaper's front page. The reader sees rooms, days, exercises, and weather — not system metadata.

---

## The Four-Prompt Generation Pipeline

The Operis is generated by a four-prompt pipeline. Each prompt has a defined role, a defined input, a defined output, and a handoff contract. The pipeline is documented in full at `seeds/operis-prompt-pipeline.md`.

**Prompt 1 — The Researcher.** (`seeds/operis-researcher-prompt.md`) Hunts facts. Historical events, astronomical data, agricultural observations, current events, calendar context. Runs in any AI with web browsing. Outputs a structured research brief (Contract A).

**Prompt 2 — The Content Architect.** (`seeds/operis-content-architect-prompt.md`) Surveys the educational content landscape across eight lanes. Determines the Color of the Day. Runs in any AI with web browsing. Outputs an enriched content brief (Contract B).

**Prompt 3 — The Editor.** (`seeds/operis-editor-prompt.md`) Writes the edition. Receives both briefs and the Ppl± system context. Selects the 5 Content Rooms by mapping editorial content to zip codes. Produces 8 Color sibling descriptions + 5 Content Room descriptions = 13 rooms total. Runs in Claude Code or temp architect. Outputs the complete Operis edition (Contract C).

**Prompt 4 — The Builder.** (`seeds/operis-builder-prompt.md`) Proofs the edition, generates workout cards for featured zip codes, files the edition, updates the repository. Runs in Claude Code only. Outputs the proofed edition, new cards, and updated repo state.

The full prompt specifications are stored as seed files and documented in `seeds/operis-prompt-pipeline.md`. The pipeline supersedes the earlier description of the "Five Input Layers" by adding a sixth layer and formalizing the generation mechanism.

---

## Layer 6 — Educational Content Layer

The Operis is a civic education publication, not only a workout gazette. In addition to the five input layers described above, the Operis draws from an educational content layer organized as eight lanes mapped to the eight SCL Colors.

Each lane covers a domain of practical adult knowledge: institutional literacy (⚫), body and ground (🟢), digital life systems (🔵), language and ideas (🟣), civic urgency (🔴), relationships and community (🟠), skills and crafts (🟡), and the inner life (⚪). Each lane inherits its Color's tonal register from the Color Context Vernacular, unifying what is taught with how it is delivered.

The educational layer is curated by Prompt 2 and woven into the edition by Prompt 3. It does not occupy a cordoned-off section — it flows through existing departments. The full specification is at `seeds/operis-educational-layer.md`.

---

## The Color of the Day

The Color of the Day is the Operis editorial system's primary editorial judgment — a cognitive posture declaration that appears on the front page before the masthead, before the zip code, before the date.

The Color of the Day is distinct from the workout Color (position 4 of the zip code) and the publication Color (the Color Context Vernacular). It is a third identity of the same 8 emoji symbols: a daily reading of the world that tells the reader how to tune their thinking to receive the edition.

The Color of the Day is determined by Prompt 2 (the Content Architect) after seeing the full content landscape — research brief, educational content, seasonal position, monthly operator, Liberal Art, current events, temporal arc. It flows downstream to Prompt 3 as a tonal instruction that governs the edition's prose character.

The full specification is at `seeds/operis-color-posture.md`. The three Color identities are documented in `seeds/operis-prompt-pipeline.md`.

---

## The 13-Room Sandbox

The Operis Sandbox features exactly 13 workout rooms per edition: 8 Color siblings and 5 Content Rooms.

The 8 Color siblings are the daily default zip code in all 8 Color variants — deterministic, produced by the rotation engine. They represent the same workout DNA in 8 different equipment formats. One carries the Color of the Day and becomes the featured room.

The 5 Content Rooms are the Operis editorial content made physical — zip codes derived from the day's historical events, educational features, and seasonal observations. Each Content Room translates a piece of knowledge into a workout that trains the physical reality implied by that knowledge. 5 unique Types, 5 unique Axes, Colors editorially selected, titles following ExRx naming convention.

The full specification is at `seeds/operis-sandbox-structure.md`.

---

## Constraints

⚫ The Operis does not perform enthusiasm. The editorial voice follows the publication standard: direct, honest, economical. No motivational language. No "you've got this." The Operis is a gazette, not a hype machine.

⚫ The Order of the day is the law. If it is Tuesday and the Order is ⛽ Strength, the Sandbox features ⛽ zip codes at the front of the queue. The rotation engine's output governs the editorial selection. The editor can add zip codes from other Orders. The editor cannot override the rotation engine's primary assignment.

⚫ The Historical Desk is not trivia. Events are selected for their relevance to a zip code or their genuine historical weight. Events are not included because they are interesting stories. They are included because they illuminate something about the address they are mapped to.

⚫ The Wilson Note does not prescribe. It observes. It notices the season. It connects the body's experience to the date's context. It does not tell the reader what to think or feel. It reports honestly on what is true.

⚫ EMPTY cards cannot be featured. The generation pipeline must clear the stub before the Operis can use the address. There are no exceptions. A stub is not a room. A room has content.

⚫ The Operis is not a marketing channel. It does not promote the platform. It does not upsell subscriptions. It is a gazette. The quality of the content is the entire pitch.

---

## Content Type Registration

Department: ✒️ Ppl± Operis
Register: ⚫🟢 (masthead) / 🔵🟣 (historical desk) / 🟡🟠 (Sandbox) / ⚪🟢 (Wilson Note)
Frequency: Daily
Generation: Rotation engine → editorial selection → automated pipeline (target)
Address: lives on the 🏛 piano nobile
Phase relevance: Phase 4/5 (design and render), Phase 6 (user accounts and personalization)

---

## Open Questions

- Does the Operis have a URL pattern? (`pplplusultra.com/operis/2026-02-26` or `/operis/today`)
- How does the Operis interact with the user's Almanac queue? (Does tapping a Sandbox zip add it to queue, or navigate directly?)
- Should the Wilson Note carry a byline? (Jake Berry, or anonymous institutional voice?)
- How many historical events per day is the right density? (8–12 is the working range)
- Should the Operis archive be browsable? (Every past edition accessible, creating a 365-day almanac)
- When the Operis goes automated, what is Jake's editorial role? (Review before publish? Review weekly? Emergency override only?)
- Does the weekly Trivium/Quadrivium cadence appear explicitly in the Operis masthead, or is it background structure only?
- How does the 13-room Sandbox structure interact with the zip count guidelines in the Weekly Editorial Cadence section? (The cadence specifies 6–12 zips per day varying by Order. The Sandbox structure fixes at 13. Resolution: the 13-room structure supersedes the earlier variable counts.)
- Should Content Room source content tags be visible in the experience layer, or only in the edition frontmatter and archive?
- How are Content Rooms handled when the same historical event recurs the following year? (The zip code persists as a library address. The editorial framing is new each year. The card is already GENERATED from last year's edition.)

🧮
