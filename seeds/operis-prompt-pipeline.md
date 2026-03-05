---
planted: 2026-03-03
status: SEED
phase-relevance: Phase 4/5 (Operis rendering), Phase 6 (automation)
depends-on:
  - seeds/operis-architecture.md
  - seeds/default-rotation-engine.md
  - seeds/operis-educational-layer.md
  - seeds/operis-color-posture.md
  - seeds/operis-sandbox-structure.md
connects-to:
  - scl-deep/publication-standard.md
  - scl-deep/vocabulary-standard.md
  - middle-math/rendering/operis-weight-derivation.md
  - middle-math/rotation/reverse-weight-resolution.md
---

# PPL± Operis — Four-Prompt Generation Pipeline

## One Sentence

The Operis is built by four prompts in sequence — Researcher, Content Architect, Editor, Builder — each with a defined input, a defined output, and a handoff contract that makes the pipeline automatable without losing editorial judgment.

## The Pipeline

```
Prompt 1 — The Researcher
    Environment: Any AI with web browsing (Genspark, ChatGPT, Claude.ai)
    Input: A date (YYYY-MM-DD)
    Output: Research brief (structured markdown)
    Does: Web research across 5 beats — historical events, astronomical data,
          agricultural observations, current events, calendar context
    Does not: Write prose, determine Color, select rooms, touch the repo
    ↓
    Handoff: Research brief document
    ↓
Prompt 2 — The Content Architect
    Environment: Any AI with web browsing
    Input: Research brief from Prompt 1 + the date
    Output: Enriched content brief (structured markdown)
    Does: Web research across 8 educational content lanes, determines Color
          of the Day, identifies Word of the Day, maps cross-domain connections,
          designates featured/secondary/tertiary lanes
    Does not: Write the edition, select rooms, touch the repo
    ↓
    Handoff: Enriched content brief document
    ↓
Prompt 3 — The Editor
    Environment: Claude Code (repo access) or temp architect with GitHub URLs
    Input: Research brief + Enriched content brief + PPL± system context
    Output: Complete Operis edition (single markdown document)
    Does: Writes the entire edition — front page card, all departments,
          room descriptions, Color-tinted prose. Selects the 5 Content Rooms
          by mapping Operis content to zip codes. Writes all 13 room
          descriptions using ExRx exercise naming.
    Does not: Search the web, determine the Color, generate workout cards
    ↓
    Handoff: Complete Operis edition document
    ↓
Prompt 4 — The Builder
    Environment: Claude Code only (requires full repo read/write access)
    Input: Complete Operis edition + full repository access
    Output: Proofed edition, generated workout cards, updated repository
    Does: Proofs the edition against vocabulary and publication standards,
          generates workout cards for any featured zip codes that are EMPTY,
          files the edition, updates whiteboard, commits and pushes
    Does not: Rewrite editorial prose, search the web, determine Color
```

Each prompt's output is the next prompt's input. The handoff documents are the contracts. No prompt reaches back into a previous prompt's work. No prompt reaches forward into a future prompt's territory.

---

## Handoff Contract A — The Research Brief (Prompt 1 → Prompt 2)

The research brief is a structured markdown document with these exact sections:

```
Operis Research Brief — [Full Date]

Edition Metadata
- Day of week
- Day of year (1–366, leap year aware)
- Season and seasonal position
- Days to next equinox/solstice
- Calendar notes (thresholds, observances)

Beat 1 — Historical Events
[5–8 events, each with: year, 3–5 sentence detail, domain tag, source URL,
body connection note]

Beat 2 — The Sky
[Sunrise, sunset, daylight hours, daily change, moon phase, illumination,
moonrise/moonset, notable astronomical events, next threshold]

Beat 3 — The Ground
[3–5 specific agricultural observations for the week and region]

Beat 4 — Current Events
[1–3 items or "No relevant current events for this date"]

Beat 5 — The Calendar
[Observances, thresholds, calendar period notes]
```

Prompt 1 checks `operis-editions/historical-events/[MM-DD].md` before doing web research for Beat 1. If the file exists, it loads those events as the starting pool and supplements with web research. If the file does not exist, it proceeds with full web research.

---

## Handoff Contract B — The Enriched Content Brief (Prompt 2 → Prompt 3)

The enriched content brief is a structured markdown document with these exact sections:

```
Operis Content Brief — [Full Date]

Color of the Day
[Color emoji] [Color name]
Posture: [One sentence — the cognitive tuning instruction]

Editorial Reasoning (for Prompt 3, not for publication)
[One paragraph — why this Color, what inputs led to it]

Edition Context
[Day of week, day of year, Order, Type, Axis, operator, Liberal Art,
default zip code, season, temporal note]

Research Brief Summary
[2–3 sentences — strongest material from the research brief]

Content Lanes
[8 lanes, each with: topic, 3–5 sentence detail, source URL,
connection to date]

Word of the Day
[Word, etymology (3–5 sentences), connection to the day]

Featured Lane
[Primary lane designation with reason]

Secondary Lanes
[Secondary and tertiary lane designations]

Connections Map
[3–5 cross-domain connections the editor can weave]

Editorial Notes for Prompt 3
[Additional observations, close-call notes, content strength signals]
```

---

## Handoff Contract C — The Operis Edition (Prompt 3 → Prompt 4)

The complete Operis edition is a single markdown document with YAML frontmatter and the full edition body. The frontmatter includes:

```yaml
title: "PPL± Operis — [Full Date]"
date: YYYY-MM-DD
color-of-day: [emoji] [Name]
posture: "[One-sentence cognitive tuning instruction]"
order: [emoji] [Architectural Name]
type: [emoji] [Name]
axis: [emoji] [Name]
operator: [emoji] [latin name]
default-zip: [4-emoji zip]
deck: [number]
liberal-art: [name]
word-of-day: "[word]"
featured-lane: [emoji] [Lane name]
sandbox-zips:
  color-siblings: [list of 8 zip codes]
  content-rooms: [list of 5 zip codes with source content tags]
word-count: [approximate]
reading-time: "[X] minutes"
status: DRAFT
```

The edition body follows the department order defined in the Department Activation Matrix below.

---

## Color Flow — Three Color Identities

The PPL± system uses 8 Color emojis (⚫🟢🔵🟣🔴🟠🟡⚪) in three distinct contexts. All three are valid simultaneously. The context determines which identity is active.

**Identity 1 — Workout Color (Position 4 of the zip code).**
Defined in CLAUDE.md. Determines equipment tier, GOLD access, and session format. A permanent property of each zip code address. ⚫ at position 4 means Teaching format with Tier 2–3 equipment and extended rest. This identity does not change.

**Identity 2 — Publication Color (Color Context Vernacular).**
Defined in `scl-deep/publication-standard.md`. Determines tonal communication register. ⚫ as publication Color means "Order: foundational, serious, non-negotiable." Used as tonal punctuation and categorical headers throughout PPL± content. This is the Color's voice.

**Identity 3 — Operis Color of the Day (Cognitive Posture).**
Defined in `seeds/operis-color-posture.md`. Determined daily by Prompt 2 based on the full content landscape. ⚫ as Color of the Day means "Think like a student." The posture sentence appears on the front page. The tonal register flows through the entire edition. This Color rotates daily. It does not override the workout Color of any zip code.

**How the three identities interact in the Operis:**
- The Color of the Day (Identity 3) determines the posture sentence on the front page and the edition's tonal register
- The featured room carries the Color of the Day as its position-4 workout Color (Identity 1) — so the cognitive posture and the workout format align at the featured room
- The other 7 Color siblings carry their own workout Colors (Identity 1) — these do not change based on the Color of the Day
- The 5 Content Rooms carry editorially selected Colors (Identity 1) based on content character
- The edition prose is tinted by the Color of the Day's publication register (Identity 2)

---

## Department Activation Matrix

This is the authoritative operational department list for the Operis. Department names and activation conditions in this document supersede the block-based department structure in `seeds/operis-architecture.md` Section "The Standing Departments." The architecture document's activation logic is the philosophical foundation. This matrix is the operational implementation.

| Department | Emoji | 🐂 Mon | ⛽ Tue | 🦋 Wed | 🏟 Thu | 🌾 Fri | ⚖ Sat | 🖼 Sun |
|---|---|---|---|---|---|---|---|---|
| Front Page Card | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Intention | 🎯 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Historical Desk | 📰 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Educational Feature | 📖 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Seasonal Desk | 🌾 | fold | fold | fold | fold | ✓ | ✓ | ✓ |
| Rooms of the Day | 🏛 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Composition | 🎼 | — | — | — | — | ✓ | — | — |
| Tool Floor | 🔨 | — | ✓ | ✓ | — | — | ✓ | — |
| Sandbox Notice | 🏖 | ✓ | — | — | — | — | — | — |
| Word of the Day | 📖 | call | call | call | call | call | call | call |
| Wilson Note | 🌡️ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Junction | 🚂 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| SAVE | 🧮 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

"fold" = Seasonal Desk content folds into the Almanac Box on the Front Page Card.
"call" = Word of the Day appears on the front page always; earns a standalone body paragraph at the editor's discretion when the etymology is particularly rich.

---

## Rotation Engine Reference — V1.0

Version tag: **Rotation Engine V1.0** — per `seeds/default-rotation-engine.md`

This reference is embedded in Prompts 2 and 3. When the rotation engine is updated, this version tag identifies which prompts need updating.

**Gear 1 — Order (weekday, fixed):**
Mon=🐂 Tuscan. Tue=⛽ Doric. Wed=🦋 Ionic. Thu=🏟 Corinthian. Fri=🌾 Composite. Sat=⚖ Vitruvian. Sun=🖼 Palladian.

**Gear 2 — Type (rolling 5-day cycle from Jan 1):**
(Day-of-year minus 1) modulo 5. 0=🛒Push, 1=🪡Pull, 2=🍗Legs, 3=➕Plus, 4=➖Ultra.

**Gear 3 — Axis (monthly operator parent):**
Jan=🏛. Feb=🐬. Mar=🔨. Apr=🌹. May=🔨. Jun=🏛. Jul=🪐. Aug=🌹. Sep=🪐. Oct=⌛. Nov=⌛. Dec=🐬.

**Monthly Operator:**
Jan=📍pono. Feb=🧲capio. Mar=🧸fero. Apr=👀specio. May=🥨tendo. Jun=🤌facio. Jul=🚀mitto. Aug=🦢plico. Sep=🪵teneo. Oct=🐋duco. Nov=✒️grapho. Dec=🦉logos.

**Liberal Art (weekday):**
Mon=Grammar. Tue=Logic. Wed=Rhetoric. Thu=Arithmetic. Fri=Geometry. Sat=Music. Sun=Astronomy.

**Deck Formula:**
(order_position - 1) × 6 + axis_position
Order positions: 🐂=1, ⛽=2, 🦋=3, 🏟=4, 🌾=5, ⚖=6, 🖼=7
Axis positions: 🏛=1, 🔨=2, 🌹=3, 🪐=4, ⌛=5, 🐬=6

**Operator Derivation:**
Read Axis (position 2) and Color (position 4). Preparatory Colors (⚫🟢⚪🟡) → first operator. Expressive Colors (🔵🟣🔴🟠) → second operator. See CLAUDE.md Default Operator Table for the full mapping.

---

## Future State — Automation

The pipeline is designed for eventual automation as a daily cron job:

**Phase A:** Prompt 1 runs automatically for the current date. Checks the historical events database first, supplements with web research as needed. Outputs the research brief.

**Phase B:** Prompt 2 runs automatically, consuming the research brief. The Color of the Day determination uses a scoring mechanism (see `middle-math/rendering/operis-weight-derivation.md`) to produce a recommendation. Outputs the enriched content brief.

**Phase C:** Prompt 3 runs in Claude Code, consuming both briefs. Writes the edition. The 8 Color siblings are fully deterministic. The 5 Content Rooms require editorial mapping (content → zip code) — this is the step that may retain human oversight longest.

**Phase D:** Prompt 4 runs in Claude Code, consuming the edition. Proofs, generates cards, files, commits.

Jake reviews the build report each morning and promotes cards to CANONICAL on a weekly review cycle.

The manual pipeline is the v1. The automation pipeline is the same architecture with the human steps replaced by scheduled execution and scoring mechanisms. Every architectural decision in this document is made with both modes in mind.

🧮
