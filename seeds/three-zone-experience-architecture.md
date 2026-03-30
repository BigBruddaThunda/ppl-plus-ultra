---
planted: 2026-03-30
status: SEED
phase-relevance: Phase 4/5/6/7 (all experience layers — this is the master UI specification)
blocks: web/src/components/, web/src/app/
depends-on:
  - seeds/negentropy-thesis.md
  - seeds/architectural-reset-direction.md
  - seeds/scl-glyph-architecture.md
  - seeds/elevator-architecture.md
  - seeds/home-screen-architecture.md
  - seeds/mobile-ui-architecture.md
  - seeds/pencil-integration-architecture.md
  - seeds/art-direction-intaglio.md
  - seeds/heros-almanac-v8-architecture.md
  - seeds/life-copilot-architecture.md
  - seeds/exploration-immersion-architecture.md
  - seeds/content-types-architecture.md
  - middle-math/design-tokens.json
  - middle-math/compiled/zips/*.json
  - canvas/src/types/scl.ts
connects-to:
  - seeds/wiki-address-resolution-layer.md
  - seeds/character-progression-architecture.md
  - seeds/digital-city-architecture.md
  - seeds/city-compiler-architecture.md
  - seeds/operis-architecture.md
  - seeds/outside-system-v2-architecture.md
  - seeds/default-rotation-engine.md
  - seeds/almanac-macro-operators.md
  - seeds/guild-campaign-architecture.md
  - seeds/voice-parser-architecture.md
  - seeds/zip-dial-navigation.md
  - seeds/exercise-superscript.md
  - reports/architectural-reset-direction.md
supersedes: seeds/mobile-ui-architecture.md (absorbs and extends), seeds/home-screen-architecture.md (absorbs the three-zone model and redefines it)
---

# Three-Zone Experience Architecture — The Complete Portrait Cockpit

⚫🔵 — foundational + systematic

## One Sentence

The Ppl± experience is a full-screen portrait cockpit split into three zones — a living chat feed at top (deliberate reach), a compressed content portal in the middle (the experience itself), and the Relevator at bottom (fidget territory) — where the 12 operators are a sequential toolbar, the 4 zip dials are a universal input device, and the 6 axis tabs are floor selectors, all driven by the same negentropy engine that resolves content contextually per zip code per user state.

---

## Section 1 — The Three Zones

The phone screen is divided into three horizontal zones with distinct ergonomic intent:

```
┌─────────────────────────────────────────────┐
│                                             │
│              TOP THIRD                      │  ← Deliberate reach zone
│   The Feed. Chat, context, signals.         │     User stretches to engage.
│   Alive, scrolling, transparent.            │     Conscious choice to interact.
│                                             │
├─────────────────────────────────────────────┤
│                                             │
│              MIDDLE ZONE                    │  ← The portal
│   The Experience. Workout, content,         │     Everything happens here.
│   map, list, video, puzzle, card.           │     Compressed, complete, scrollable
│   The entire workout on one screen.         │     within but never scrolled away.
│                                             │
├═════════════════════════════════════════════╡
│  ROW 1: 12 Operators (sequential toolbar)   │
│  ROW 2: 4 Universal Dials (zip/number/rate) │  ← Fidget territory
│  ROW 3: 6 Axis Tabs (floor selectors)       │     Thumb resting zone.
│                                             │     Explore, toggle, spin, tap.
└─────────────────────────────────────────────┘
```

### Ergonomic Intent

- **Bottom third:** Where the thumb rests naturally on a phone held in one hand. All primary navigation and interaction happens here. Spinning dials, tapping operators, switching floors. This zone is designed to be fidgety — the user explores by feel.

- **Middle zone:** The content itself. The workout card, the Operis edition, the almanac page, the community thread, the map. Whatever the current zip code + floor demands. The entire workout fits here at once — the block system exists specifically to enable this compression. Users scroll within this zone but never scroll the zone away.

- **Top third:** The user must deliberately reach upward to engage. This makes social interaction, chat, community, and Wilson a conscious choice rather than an accidental tap. The top is a living feed — messages flow through it, context shifts, the room's personality expresses itself here. It is not a static header. It is a newspaper ticker, a chat log, a signals board.

---

## Section 2 — The Top Third: Living Feed

The top zone is a transparent, shifting information surface. It has layers that the user toggles between:

### Pinned Elements (always visible)

- **Status bar:** Time, current operator/date (e.g., "⛽ Mar 30 · 🧸 fero")
- **Room address:** Zip badge with emoji + numeric (⛽🏛🪡🔵 2123) plus human-readable name
- **Floor indicator:** Current axis floor with emoji and Latin name (🏛 Firmitas — Arrival Floor)

### Feed Content (toggleable via tabs)

| Tab | What It Shows | Character |
|-----|---------------|-----------|
| **Brief** | Systems brief. Workout intention. Room personality. Today's context. The default view. | Monologue from the system. |
| **Chat** | Community messages. Proximity-based channels tied to current zip. TLDR auto-bot. | Dialogue with others. |
| **Wilson** | System voice interface. Text/voice input. Responds in feed. Insights, suggestions, coaching. | Dialogue with the system. |
| **Signals** | Notifications. Incoming recommendations. Rotation engine suggestions. Guild activity. | Alerts and updates. |

### Feed Message Format

Each message in the feed is prefixed with an operator emoji that identifies the message type:

```
🐋  Session started · Bread & Butter active           (system event)
✒️  Set 1 logged: 185 lb × 5 · RPE 7                  (user action recorded)
🤌  Set 2 ready · 190 lb × 5 · rest complete           (action prompt)
🦉  Last session: 185 × 5 × 3. You're +5 lb today.    (Wilson insight)
🧲  Rotation suggests ⛽🔨🪡🟢 tomorrow                 (recommendation)
🧸  @jake shared ⛽🏛🍗🔴 · "legs were brutal"          (social)
```

The operator emoji IS the message type indicator. The system's own language serves as UI iconography. Older messages fade in opacity. The newest message is brightest. The feed scrolls upward as new events arrive.

### Design Character

The top zone should feel like:
- A newspaper ticker or RSS feed — content moves through it
- A chat interface — messages accumulate, most recent at bottom
- Transparent and layered — the content shifts, the frame stays
- Semi-monospace typography — data-forward, not decorative

---

## Section 3 — The Middle Zone: The Portal

The middle zone is the architectural card. It renders whatever the current zip code + floor + context demands.

### Content Types

The portal can display:
- A workout card (the primary use case)
- An Operis edition
- An almanac page
- A community thread
- A cosmogram deep-dive
- An exercise library entry
- A map or directory
- A video or media player
- A puzzle or interactive element
- A form or survey
- A blank canvas (hollow template mode)

The content type is determined by the zip code (which room) and the axis floor (which vertical plane). The portal renders the content inside a framed viewport. The frame never changes. The content inside it does.

### Workout Card Compression

The entire workout fits on screen at once. This is a hard constraint. The block system enables this:

- **Completed blocks** fade to ~40% opacity with a green ✓ mark
- **Active block** renders at full brightness with expanded exercise detail
- **Future blocks** render at ~35% opacity as section headers only — visible but clearly ahead
- **Block headers** are single-line: emoji + name + operator call
- **Exercise lines** use tree notation (├─ │) for visual compression
- **Toggle checkboxes** on each exercise — tap to mark set complete
- **Superscript/subscript data boxes** inline: `[190 lb]` × `[5]` RPE `[7]` — tappable fields in stone-colored recesses
- **Set progress chips** in a horizontal row: S1 ✓ (green), S2 ● (active, gold border), S3 ○ (pending, dark)
- **Rest timer** inline with the set data

The compression means a user sees the full workout arc — where they've been (faded), where they are (bright), and where they're going (dim) — without scrolling away from any zone.

### Superscript/Subscript System

Weight, rep, and RPE data are displayed in tappable inline boxes:

```
├─ [●] 5 🪡 Barbell Deadlift  (hips back, not down)
│     [190 lb] × [5]  RPE [7]
│     S1 ✓  S2 ●  S3 ○
│     Rest: 3:00
```

Each bracketed value is a tappable field. Tapping a field activates the number dial in the Relevator (see Section 5). The value updates as the user spins the dial. No keyboard popup needed. The superscript (weight) and subscript (RPE, notes) system handles all numeric data inline.

### Mid-Workout Exercise Swap

When a user taps an exercise name to swap it:
1. The exercise name highlights
2. The zip dial zone in the Relevator swaps to show alternative exercises (constraint-solver filtered)
3. The user flicks through options in the dial
4. Selecting one updates the exercise inline
5. The remaining exercises in the workout may recalculate (the cascade effect from the negentropy thesis)

---

## Section 4 — The Bottom Third: The Relevator

The Relevator is the cockpit. Three rows, always visible, always in the thumb zone.

### Row 1: The 12-Position Operator Toolbar

The 12 operators are arranged left to right in a fixed sequential order. They are NOT polarity-split by axis. They follow the natural sequence of human engagement with any task:

| Pos | Emoji | Latin | Tool Name | What It Does |
|-----|-------|-------|-----------|-------------|
| 1 | 📍 | pono | **Position** | Setup. Stance, grip, body position, starting cues. "How do I stand?" Saves current position. Drops a pin. Bookmarks. |
| 2 | 👀 | specio | **Inspect** | Form check. Video demo, key angles, common mistakes. Preview before committing. Magnify. Measure. |
| 3 | 🧲 | capio | **Receive** | Context. Why this exercise is here, what it targets, what the system recommends. Intake tray. Notifications. Envelope stamper. |
| 4 | 🐋 | duco | **Conduct** | Tempo and rhythm. Breathing cues, rest timer, session flow, EMOM/AMRAP conductor. The metronome. |
| 5 | 🤌 | facio | **Execute** | THE PRIMARY ACTION. Start the workout. Begin the set. The green light. Always highlighted. |
| 6 | ✒️ | grapho | **Write** | Log. Record weight, reps, RPE, notes. Activates number dial. Quick note. Journal. The pen. |
| 7 | 🧸 | fero | **Transfer** | Share and bridge. Share zip code, export workout, Junction suggestions, "send this to..." |
| 8 | 🦉 | logos | **Analyze** | Stats and insight. Training history, PRs, pattern recognition, personal weight vector visualization. |
| 9 | 🥨 | tendo | **Extend** | Harder. Challenge variation, deficit/pause/tempo, progression path, "show me more," deeper content. |
| 10 | 🦢 | plico | **Layer** | Overlay and combine. Split-screen two zips, compare workouts, stack content, superset logic. |
| 11 | 🪵 | teneo | **Lock** | Pin and persist. Lock a room, pin a workout, hold a weight, freeze rotation, maintain a program. |
| 12 | 🚀 | mitto | **Submit** | Finalize. Complete the session, publish a note, submit a log, commit a custom workout. The closing action. |

**The arc: Position → Inspect → Receive → Conduct → Execute → Write → Transfer → Analyze → Extend → Layer → Lock → Submit.**

This is the natural sequence of engagement with any task. It works for a barbell deadlift, an Operis edition, a cosmogram, the Hero's Almanac, or any content type the system surfaces.

### How the Operators Behave

**Static position, dynamic content.** The 12 icons never move. Their position is fixed (1-12, left to right). What changes:

1. **Lit vs dimmed.** The current context determines which operators are active. A 🖼 Restoration zip might dim 🚀 (no max attempts in recovery). A 🏟 Performance zip lights 🚀 bright. The active operator (currently engaged) gets a gold/highlighted border.

2. **Surface content.** Tapping an operator replaces the zip dial zone (Row 2) with that operator's surface — a contextual pager card. The surface content is resolved by the constraint solver based on current zip + user state + the operator's verb.

3. **Labels shift.** 🤌 reads "Start Workout" on 🏛 floor, "Begin Reading" on ⌛ floor, "Play" on 🟡 content. The verb stays the same (facio = execute), the label contextualizes.

4. **Depth grows left to right.** Positions 1-4 are setup. Position 5 is the action. Positions 6-8 are reflection. Positions 9-12 are advancement. A new user uses 📍→🤌→✒️→🚀. A power user clicks all 12.

### Operator Surface Examples (for Barbell Deadlift)

| Operator | Surface Content |
|----------|----------------|
| 📍 Position | Stance diagram. Feet hip-width. Grip outside knees. Shoulder blades over bar. |
| 👀 Inspect | Video loop of the movement. Key angle overlay. "Watch the hip hinge, not the back." |
| 🧲 Receive | "This exercise is here because your pull volume is 2 sessions behind push. The system is rebalancing." |
| 🐋 Conduct | Rest timer: 3:00 countdown. Tempo: 1-0-2-1. Breathing: brace at top, exhale at lockout. |
| 🤌 Execute | [START SET] button. Progress bar during active set. Rep counter. |
| ✒️ Write | Number dial activated. Weight input: [190] lb. Reps: [5]. RPE: [7]. Notes field. |
| 🧸 Transfer | "Next session: try 195 lb if today's RPE stays under 8." Junction: ⛽🔨🪡🔵 recommended. Share button. |
| 🦉 Analyze | History chart: last 8 sessions for this exercise. PR: 225 lb × 3. Trend: progressing (+5 lb/week). |
| 🥨 Extend | "Deficit deadlift adds 2-inch ROM. Pause deadlift adds 3s at knee. Which challenge?" |
| 🦢 Layer | Side-by-side: today's prescription vs last session's actual. Overlay: muscle activation map. |
| 🪵 Lock | "Pin 190 lb as your working weight for this exercise across all zip codes. [Lock]" |
| 🚀 Submit | "Set complete. Log submitted. Session progress: 2/3 sets done. [Next set] or [Finish block]" |

### Row 2: The Universal Dial

The 4 zip dials are not just for navigation. They are the **universal 4-value input device**. The same physical element, same thumb zone, same flick/tap behavior. The operators determine which mode the dial is in.

#### Dial Modes

| Mode | Triggered By | Dial 1 | Dial 2 | Dial 3 | Dial 4 |
|------|-------------|--------|--------|--------|--------|
| **Navigation** | Default state | Order (7) | Axis (6) | Type (5) | Color (8) |
| **Weight input** | ✒️ grapho (weight field tapped) | 0-9 hundreds | 0-9 tens | 0-9 ones | 0-9 decimal |
| **Rep input** | ✒️ grapho (rep field tapped) | — | — | 0-9 tens | 0-9 ones |
| **Timer** | 🐋 duco | Min tens | Min ones | Sec tens | Sec ones |
| **Rate workout** | 🚀 mitto (end of session) | Order fit (0-9) | Difficulty (0-9) | Enjoyment (0-9) | Recovery (0-9) |
| **Exercise swap** | Tap exercise name | Category | Family | Variation | Equipment |
| **Survey/intake** | 🧲 capio (Almanac context) | Q1 answer | Q2 answer | Q3 answer | Q4 answer |

#### Dial Mechanics

Each dial is a vertical column split into three zones:
- **Top zone** (tap = scroll backward): Shows the previous value, dimmed
- **Center zone** (active value): Large, bright, the current selection
- **Bottom zone** (tap = scroll forward): Shows the next value, dimmed
- **Flick gesture**: Thumb swipe up/down scrolls through values with snap and haptic tick
- **Wrapping**: Values wrap (7→1 for Orders, 9→0 for numbers)

The COLOR dial tints its border and center background with the active Color's hex value. When 🔵 Structured is active, the dial has a blue border and blue-tinted center.

#### The Operator-Dial Swap

When an operator is tapped:
1. The operator icon gets a highlighted border (gold or Color-tinted)
2. The dial zone (Row 2) slides/transitions to show the operator's surface instead of the 4 dials
3. The surface content is contextual to the current zip + exercise + user state
4. Tapping the same operator again returns the dials
5. Tapping a different operator swaps to that operator's surface

The transition should feel like a pager flip — the dials slide out, the surface slides in. Same physical space, different content.

#### Rating System (End of Workout)

At workout completion, 🚀 mitto triggers a 4-dial rating:
- Dial 1: How well did this Order match your energy? (0-9)
- Dial 2: How was the difficulty? (0-9)
- Dial 3: How much did you enjoy it? (0-9)
- Dial 4: How recovered do you feel? (0-9)

This produces a 4-digit score that the rebalance engine absorbs. The user is directly weighting the system's understanding of this zip code for their account. The seesaw adjusts. The next time this zip appears, its resolution reflects this feedback. **The user is tuning the negentropy engine through the same dial they use to navigate.**

### Row 3: The 6 Axis Floor Tabs

Six tabs at the bottom edge, one per axis. These are floor selectors — tapping one changes which vertical plane of content renders in the portal (middle zone) and what the feed (top zone) shows.

| Tab | Floor | What the Portal Shows | What the Feed Shows |
|-----|-------|----------------------|---------------------|
| 🏛 Basics | Piano Nobile (Arrival) | The workout card. The Operis. What IS this room. | Systems brief. Workout intention. |
| 🔨 Functional | Ground (Tools) | Settings, account, exercise library, calculators, timers. | Tool notifications. Account alerts. |
| 🌹 Aesthetic | 4th (Personal) | Training history, saved rooms, PRs, progress photos, notes. | Personal milestones. Streak alerts. |
| 🪐 Challenge | 5th (Penthouse) | Cosmogram. Deep research. Why this room matters. Stakes. | Deep questions. Philosophical prompts. |
| ⌛ Time | 2nd (Calendar) | Almanac. Seasonal content. Training calendar. Historical events. | Temporal context. Seasonal shifts. |
| 🐬 Partner | 3rd (Community) | Community threads. Forum. Shared training. Partner coordination. | Chat messages. Social activity. |

The active tab is highlighted (gold border, brighter icon). Inactive tabs are dimmed. Switching floors changes what the 12 operators show in their surfaces — the operators are tools FOR the active floor's content type.

---

## Section 5 — Accessibility and Ergonomics

### Thumb Zone Mapping

```
┌─────────────────────────────────┐
│  STRETCH ZONE (top)             │  Hard to reach. Deliberate.
│  Chat, community, Wilson.       │  Social = conscious choice.
│                                 │
├─────────────────────────────────┤
│  CONTENT ZONE (middle)          │  Reachable with stretch.
│  Tap exercises to swap.         │  Tap superscript boxes to edit.
│  Scroll within, not away.       │  Deliberate interaction.
│                                 │
├─────────────────────────────────┤
│  THUMB ZONE (bottom)            │  Natural resting position.
│  Operators: fidget, explore.    │  Where thumbs live.
│  Dials: spin, flick, tap.      │  Designed for fidgeting.
│  Axis tabs: quick floor switch. │  Maximum accessibility.
└─────────────────────────────────┘
```

### No Keyboard Popup

The universal dial eliminates the need for a keyboard popup for numeric input. Weight (0000-9999), reps (00-99), timer (00:00-99:59), and ratings (0-9 × 4) all use the same dial mechanics. The keyboard never appears unless the user enters the chat/notes text field (top zone, deliberate reach).

### No Fullscreen Takeover

Nothing goes fullscreen unless the user deliberately enters immersed mode (double-tap the portal frame or pinch-to-expand). Every view renders inside the portal while the feed and Relevator stay visible. The user always has context, always has controls, never loses their place.

---

## Section 6 — Dual Register (Light and Dark)

The cockpit has two visual registers that match the compiled zip's dual-register rendering:

### Dark Register (Cathedral)

- Stone gradient background (#0C0B09 → #141210)
- Warm gold/parchment text (#D4C8A8)
- Stone-carved borders (#2A2520)
- JetBrains Mono for data, Inter for prose
- Suggested by: evening use, high-intensity Colors (🔴🟣), Strength/Performance Orders

### Light Register (Watercolor / Golden Wool)

- Warm parchment gradient (#FAF6EE → #EDE4CE)
- Dark text on light (#3A2A0A, #4A3A1A)
- Gold metallic borders (#C8A84E, #8B6914)
- Banknote guilloche patterns in viewport backgrounds
- Suggested by: daytime use, light Colors (⚪🟢🟡), Foundation/Restoration Orders

Register selection is influenced by: time of day, active Color, Order weight, user preference. The user can always override. Both registers use the same layout, same typography hierarchy, same component structure. Only the color values change — driven by the same `weightsToCSSVars()` pipeline.

---

## Section 7 — The 61 Emojis as UI Elements

All 61 SCL emojis function as interactive UI elements throughout the three zones:

### As Buttons (Operators — Row 1)
The 12 operator emojis are tappable tool buttons. Position fixed. Content contextual.

### As Dials (Orders, Axes, Types, Colors — Row 2)
The 26 dial emojis (7+6+5+8) are the values in the navigation dials. Flick to browse, tap to select.

### As Floor Selectors (Axes — Row 3)
The 6 axis emojis are floor tabs. Tap to switch vertical plane.

### As Block Headers (Blocks — Middle Zone)
The 22 block emojis are section headers in the compressed workout card. They visually organize the content.

### As Message Type Indicators (Operators — Top Zone)
The 12 operator emojis prefix feed messages, identifying the message type (system event, user action, Wilson insight, social).

### As Data Markers (Throughout)
Order emojis appear next to set data (⛽ 80% × 5). Type emojis appear next to exercise names (🪡 Barbell Deadlift). Color emojis tint the active dial. The 61 emojis are the visual vocabulary of the entire interface.

### As System Seal (🧮 SAVE)
The session-complete seal. Appears at workout end. The closing ritual.

---

## Section 8 — State Machine

The cockpit has distinct states based on user activity:

### Idle State (Default)
- Feed shows: Systems brief
- Portal shows: Room overview (map or today's recommendation)
- Dials: Navigation mode (Order/Axis/Type/Color)
- Operators: All available, none active

### Workout Active State
- Feed shows: Session log (set completions, Wilson insights, rest timers)
- Portal shows: Compressed workout card with toggle boxes and superscript data
- Dials: Navigation mode (but swap to number input when ✒️ grapho active)
- Operators: 🤌 facio highlighted, ✒️ grapho lights up after set completion

### Logging State (✒️ Active)
- Feed shows: "WEIGHT INPUT · Barbell Deadlift · Set 2"
- Portal shows: Workout card with active field highlighted
- Dials: Number input mode (0-9 × 4)
- Operators: ✒️ grapho has gold border, others dimmed

### Rating State (🚀 End of Session)
- Feed shows: Session summary, PR alerts
- Portal shows: Completed workout with 🧮 SAVE seal
- Dials: Rating mode (0-9 × 4 for workout scoring)
- Operators: 🚀 mitto active, rating surfaces shown

### Browse State (Non-Workout)
- Feed shows: Brief or Chat or Wilson
- Portal shows: Operis, almanac, exercise library, community — whatever the current floor serves
- Dials: Navigation mode
- Operators: Context-dependent (e.g., ✒️ grapho becomes "write a note" instead of "log a set")

---

## Section 9 — How Operators Change Across 1,680 Zip Codes

The 12 operator positions are static. Their content is resolved per zip code.

### What Changes Per Zip

1. **Which operators are lit vs dimmed.** Each zip code's compiled personality includes operator weights. High-weight operators are bright. Low-weight are dimmed. The room's primary operator (from the City Compiler) is always the brightest.

2. **Surface content.** 📍 Position on a deadlift shows stance cues. 📍 Position on an Operis edition shows reading position. 📍 Position on the almanac shows seasonal position. Same tool, same position (#1), different content.

3. **Label text.** 🤌 reads "Start Workout" on workout cards, "Begin Reading" on editorial content, "Play" on media, "Start Survey" on intake forms. The verb (facio = execute) stays. The label contextualizes.

4. **Depth of content.** A zip with high 🪐 Challenge weight has a richer 🥨 tendo surface (more progression paths, more challenge variations). A zip with high 🌹 Aesthetic weight has a richer 👀 specio surface (more form detail, more video angles).

### What Changes Per User

The user's personal weight vector (from training history, Almanac, logged preferences) adjusts:
- Which operators surface the most relevant content
- What the constraint solver produces when exercises are swapped
- What 🦉 logos shows in analytics (personalized patterns)
- What 🧲 capio recommends (rotation-engine adjusted suggestions)
- What the rating dials (🚀 mitto) feed back into the system

Every interaction through the operators feeds the negentropy engine. The system absorbs the user's choices and produces more accurate, more personalized content at every position.

---

## Section 10 — Negentropy Alignment

### The Cockpit as Negentropy Interface

The three-zone layout is the negentropy engine's user interface:

- **Top zone absorbs social entropy.** Community messages, Wilson insights, system events — all incoming entropy that the feed organizes into a scrollable log with operator-typed messages.

- **Middle zone absorbs content entropy.** The portal renders whatever the current context demands. The block system compresses workouts. The superscript system handles data inline. The exercise swap system recalculates in real-time.

- **Bottom zone absorbs interaction entropy.** User taps, flicks, and spins are absorbed by the operators (contextual tools), dials (universal input), and axis tabs (floor selection). Every interaction produces data that the system metabolizes.

### The Universal Dial as Entropy Absorber

The same physical dial that navigates 1,680 rooms also inputs weight (0-9999), logs reps, sets timers, rates workouts, and answers surveys. Each mode absorbs a different kind of user entropy (location choice, performance data, temporal data, preference data) through the same interface element. The user doesn't learn new controls — the controls learn new modes.

### The Operator Sequence as Engagement Arc

Positions 1→12 map the natural arc of engagement. The system doesn't need to teach this arc — it emerges from the sequential order. A new user discovers operators one at a time, left to right. Each new operator deepens their relationship with the content. The progression IS the onboarding.

---

## Section 11 — Directional Constraint Compliance

From `seeds/architectural-reset-direction.md`, Section 5:

1. **Operates on the zip code address space?** Yes. Every element is resolved from the current zip code. The dials navigate the address space. The operators show content resolved from it. The portal renders it.

2. **Constraint hierarchy governs it?** Yes. Order > Color > Axis > Equipment governs what the operators show, what the dials offer, what the portal renders.

3. **Absorbs entropy or creates it?** Absorbs at every scale. Social entropy (feed), content entropy (portal), interaction entropy (Relevator).

4. **Same principle at different timescale?** Yes. The negentropy engine operating at the UI-interaction timescale. Same pattern as the constraint solver (in-session), rotation engine (daily), and wiki (internet-scale).

5. **Exercise library coverage?** The constraint solver runs behind every operator surface. Exercise swap pools are filtered. The library provides coverage for every operator-triggered content request.

**The 100-year question:** Would a three-zone cockpit with sequential operator tools, universal dials, and floor-based navigation still make sense if the system runs for 100 years? Yes. The layout is architecturally derived from phone ergonomics (thumb zone, stretch zone) and human engagement patterns (position→execute→reflect→advance). Neither changes with technology trends. The content changes. The architecture holds.

---

## Section 12 — Design Artifacts

### Pencil Compositions (in pencil-new.pen)

The following design iterations were built during the initial exploration:

1. **V1 — Dark Flat Sketch** — Layout proof. Basic three-zone with operators, dials, axis tabs.
2. **V2 — Stone Tabula** — Dark register. Cathedral candlelight palette. Engraved borders. Monospace data.
3. **V3 — Golden Wool White** — Light register. Warm parchment gradient. Gold metallic borders. AI-generated banknote guilloche viewport background.
4. **V4 — Active Workout State** — Mid-workout view. Chat-style feed with operator-typed messages. Compressed workout card with toggle checkboxes, superscript/subscript data boxes, set progress chips. Number-input dial mode showing weight entry (0190 = 190 lb).

### SCL-61 Icon Sheet (in pencil-new.pen)

All 61 emojis on a single dark canvas, organized by family. Colors rendered with solid design-token fills. Operators, blocks, axes, types, orders as monochrome on dark.

### Component Library (in pencil-new.pen)

61 reusable glyph components with architectural treatments per family (column capitals, building facades, anatomical engravings, ink wells, room plans, gesture engravings, institutional seal).

---

🧮
