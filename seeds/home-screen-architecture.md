---
planted: 2026-03-11
updated: 2026-03-12
status: SEED — WIP (active ideation)
phase-relevance: Phase 4/5/6
blocks: nothing currently — UX composition layer
depends-on: seeds/mobile-ui-architecture.md, seeds/elevator-architecture.md, seeds/digital-city-architecture.md, seeds/experience-layer-blueprint.md
connects-to: seeds/character-progression-architecture.md, seeds/exploration-immersion-architecture.md, seeds/life-copilot-architecture.md, seeds/heros-almanac-v8-architecture.md
extends: seeds/mobile-ui-architecture.md (supersedes 4-state model with 3-zone persistent HUD)
design-references: OSRS mobile portrait mode concept (reddit r/2007scape), Fallout Pip-Boy, GW2 minimap, TCG card framing, PDA interfaces
---

# The Home Screen — Architectural Composition

🟣🔵 — precise + systematic

## One Sentence

The Ppl± home screen is a persistent three-zone HUD — chat/terminal at top, framed content viewport in the middle, and the **Relevator** (split control panel: minimap joystick + stone tabula) at bottom — designed so nothing ever goes fullscreen unless deliberately entered, left hand and right hand layouts mirror, and the entire system feels like a PDA copilot crossed with a game HUD.

---

## The Three Zones (Mobile Portrait)

The composition is fixed. All three zones are always visible. Content loads INSIDE the middle zone — it never blows out to fullscreen unless a user deliberately taps into immersed mode. No jarring transitions. The HUD is always there. Like a Pip-Boy you never take off.

```
┌─────────────────────────────────┐
│  ┌─────────────────────────────┐│
│  │ ZONE 1: THE TERMINAL        ││  ← Top ~25%: Live text,
│  │ [🤌] Welcome back. ⛽ Day.  ││     chat channels, Wilson,
│  │ > Tax season in 3 weeks...  ││     context briefs, portals,
│  │ > 🐬 Chat: 4 new in Pull   ││     toggles, server browser
│  │ [☰ channels] [👥] [🔔]     ││
│  └─────────────────────────────┘│
├─────────────────────────────────┤
│  ┌─────────────────────────────┐│
│  │                             ││
│  │  ZONE 2: THE VIEWPORT       ││  ← Middle ~45%: Framed like
│  │  ╔═══════════════════════╗  ││     a TCG card. Content
│  │  ║                       ║  ││     renders here. Map, workout,
│  │  ║   [content / map /    ║  ││     almanac, community thread,
│  │  ║    media / card]      ║  ││     whatever is "on screen."
│  │  ║                       ║  ││     Scrollable inside frame.
│  │  ╚═══════════════════════╝  ││
│  │                             ││
│  └─────────────────────────────┘│
├─────────────────────────────────┤
│  ┌──────────┬──────────────────┐│
│  │          │ ┌──┬──┬──┬──┐   ││  ← Bottom ~30%: THE RELEVATOR
│  │  ◉       │ │🗡│📖│⏱│🎲│   ││     Split into two halves.
│  │ MINIMAP  │ │📋│💾│🔀│👤│   ││     Left: minimap/joystick
│  │ /JOYCON  │ │⚙│🔍│📊│🚂│   ││     Right: stone tabula
│  │          │ ├──┴──┴──┴──┤   ││     (12 tool icons)
│  │ [8 VIALS]│ │ 6 AXIS TABS │ ││     + 8 vials + 6 axis tabs
│  └──────────┴──────────────────┘│
└─────────────────────────────────┘
```

### The Handedness Mirror

The entire lower third mirrors for left-handed users. Setting in preferences.

**Right-handed (default):** Minimap/joystick on LEFT (thumb reach), tabula on RIGHT.
**Left-handed:** Minimap/joystick on RIGHT, tabula on LEFT.

The thumb that does the most work (joystick navigation, dial spinning) gets the dominant-hand side. The tabula (tap targets, less frequent) gets the off-hand side. Either layout, same functionality.

### The No-Fullscreen Rule

Nothing takes over the full screen unless the user deliberately enters immersed mode (double-tap the viewport frame, or pinch-to-expand). Every view — workout, map, chat, almanac — renders INSIDE the viewport frame while the terminal and Relevator stay visible. The user always has context. They always have controls. They never lose their place.

Coming back out of immersed mode is instant — tap the frame border or pinch-to-shrink. The HUD reappears. No loading. No transition animation. Snap.

---

## Zone 1: The Terminal (Top ~25%)

A live text interface. Part welcome screen, part chat client, part systems brief, part Wilson assistant. This is the informational layer — everything the user needs to KNOW is here. Everything they need to DO is in the Relevator below.

### What Lives in the Terminal

**Systems brief (default on open):**
- Welcome message (Wilson-voiced, time-of-day aware)
- Day context: Order of the day, operator of the month, season
- Auto-generated snapshot: weather (if opted in), upcoming calendar events, vial balance summary
- Hyperlinks in the brief text are portals — tapping a zip code reference spins the dials and loads that room in the viewport

**Community chat (toggle):**
- Proximity-based chat channels tied to zip code location
- Different rooms within a zip code may have different active chat channels
- Feels like MMO zone chat, not a rolling Twitch/IG feed
- Each channel has a TLDR auto-bot: when you enter a room or return after absence, the bot generates a brief context summary. "While you were away: 3 users discussed form on heavy pulls. User @oak shared a PR video. The Operis featured this room yesterday."
- This becomes the onboarding layer too — first-time visitors to a room get an auto-generated room tooltip from the bot

**Wilson assistant (toggle):**
- The system's voice interface. Siri of Ppl±.
- Text input or voice. Wilson responds in the terminal.
- "Wilson, what should I train today?" → Wilson recommends based on rotation + vial balance
- "Wilson, what's happening at ⛽🏛🪡🔵?" → Wilson summarizes that room's recent activity
- Wilson's responses contain portal hyperlinks — tapping them navigates

**Server browser / channel switcher:**
- Top-row buttons toggle between: Systems brief | Community chat | Wilson | Friends list | Notifications
- The active channel determines what fills the terminal text area
- Friends list shows online friends and what zip codes they're currently at
- Notification tab shows activity from saved rooms

### Terminal Design

- Monospace or semi-monospace font. Terminal aesthetic. Not a social feed — a command line with hyperlinks.
- **Semi-transparent overlay option:** Like OSRS mobile chat, the terminal can overlay the top of the viewport with transparency rather than being a fully opaque zone. This gives the viewport more vertical space while keeping chat visible. User toggle: opaque (full zone separation) or transparent (chat overlays viewport top). Default: semi-transparent, matching the OSRS reference.
- Text scrolls up as new content arrives. Old content scrolls off but is retrievable by scrolling back.
- Hyperlinks are colored by their destination's Color. A link to a 🔵 room is blue-tinted. A link to a 🔴 room is red-tinted. Visual wayfinding.
- The terminal never auto-plays media. Text only. Links to media open in the viewport.
- Channel tabs sit in a compact row at the very top of the screen (same position as OSRS's All/Game/Public/Private/Clan/Trade tabs). Always accessible. One tap to switch channels.

---

## Zone 2: The Viewport (Middle ~45%)

The content display. Everything visual renders here — workout cards, the figure-ground map, almanac pages, community media, exercise demonstrations, Operis editions. Framed like a TCG card with a visible border.

### The Card Frame

The viewport has a persistent border/frame around the content. This frame:
- Provides visual containment — the content has edges, it doesn't bleed into the terminal or Relevator
- Changes style subtly based on context (Order D-module proportions, Color tinting)
- Has corner indicators showing current zip code and floor
- The frame IS the room boundary. Content lives inside it. Controls live outside it.

### What Renders in the Viewport

**Default (home state):** The figure-ground map of the current zip code. The NES Zelda overworld / Nolli plan / pixel art analytique composition. Tappable buildings, fog of war, waypoint markers, paths to adjacent zips.

**Workout view:** The workout card rendered as a scrollable document inside the frame. Blocks, exercises, logging overlays — all within the viewport.

**Almanac view:** Seasonal/historical content for the current zip code's ⌛ floor. Scrollable text with portal hyperlinks.

**Community view:** Thread display for the current zip code's 🐬 floor. Posts, replies, media. Different from the terminal chat — this is threaded discussion, not live chat.

**Deep content view:** Cosmogram, educational content, exercise deep-dives. Rich text with citations and cross-references.

**Any content type from the 109-type registry** renders here. The viewport is medium-agnostic. Text, images, interactive elements, embedded widgets — all framed.

### Viewport Interaction

- **Scroll** inside the viewport = navigate within the current content
- **Tap** elements inside = interact (log a set, open a portal, expand a section)
- **Double-tap the frame** = enter immersed mode (viewport expands to fullscreen, terminal and Relevator hide)
- **Pinch-to-zoom** inside = zoom into content detail (inherited from ZoomableRoom)
- **Swipe left/right** inside = navigate between floors (6 Axis layers) at the current zip code

### The Map as Default Viewport Content

When the viewport shows the map:

**Map elements (tappable):**
- **Buildings/rooms** — solid shapes representing content zones. Tap to load that content in the viewport (the map stays accessible via back gesture).
- **Paths** — connections to adjacent zip codes (from navigation-graph.json). Visible as routes.
- **Icons** — glyphs representing content types: workout, community, almanac, deep, tools.
- **Fog of war** — unvisited areas obscured. Clears as user explores.
- **Waypoint marker** — saved/bookmarked rooms show a flag.
- **Easter egg markers** — hidden until conditions met.

Every dial spin or tap recomposes the map. The map IS the zip code rendered spatially.

### Return Visit Behavior

**The viewport remembers.** Quicksave per zip code:
- Which floor (Axis) they were on
- Scroll position within that floor
- Whether they were mid-workout (paused at a block)
- Returning to a zip code restores the viewport to its last state at that address

---

## Zone 3: The Relevator (Bottom ~30%)

The Relevator is the entire lower-third control system. The name is the thing — it's the elevator/navigator/relevance engine combined. It splits into two halves, mirrorable for handedness.

### Left Half: The Minimap & Joystick

A circular element that serves multiple functions:

**As minimap:**
- A small, zoomed-out version of the current zip code's map (or the deck-level map showing adjacent rooms)
- Shows your position in the broader zip web
- Shows nearby rooms, fog of war state, waypoint markers
- Tapping the minimap opens the full map in the viewport

**As joystick/trackpad:**
- Hold and drag in any direction = directional navigation through the zip web
- Like a virtual joycon thumbstick in touch-based games
- Drag up = navigate to the room "above" in the navigation graph
- Drag left/right = cycle through rooms in the same deck
- The viewport previews the destination as you drag (reduced opacity, like dial spin preview)
- Release = snap to the nearest room in that direction

**As zip dial launcher:**
- Tap the minimap button (not hold-drag) = the 4-dial Relevator emerges
- The dials animate up from the minimap area, overlaying the Relevator zone
- Spin or tap the dials to navigate
- Tap outside the dials = they retract back into the minimap
- The dials are a popup tool, not a permanent fixture — they appear when summoned

**The 8 Vials live here:**
- Arranged in a row beneath the minimap circle (or around its perimeter)
- Compact — small enough to fit in half the lower third
- Still tappable: single tap = toggle Color filter on the map/viewport, hold = open Color hub
- Fluid levels still animate per dial spin/tap/joystick move

### Right Half: The Stone Tabula

A grid of icon buttons — fixed positions, contextual activation. Like a carved stone tablet with tool icons that illuminate when relevant.

**~12 button positions in a grid (3×4 or 4×3):**

| Row | Slot 1 | Slot 2 | Slot 3 | Slot 4 |
|-----|--------|--------|--------|--------|
| 1 | 🏋️ Workout | 📖 Library | ⏱ Timer | 🎲 Random |
| 2 | 📋 Log | 💾 Save | 🔀 Swap | 👤 Profile |
| 3 | ⚙ Settings | 🔍 Search | 📊 Stats | 🚂 Junction |

**Contextual activation (lights on/off):**
- All 12 positions are always visible, always in the same place
- Active icons are lit (full color, tappable)
- Inactive icons are grayed out / dimmed (visible but not functional right now)
- What's active depends on context:
  - At a workout zip: 🏋️ Workout, 📋 Log, 💾 Save, 🔀 Swap, ⏱ Timer all lit
  - At a community-only room: 📖 Library, 📊 Stats, 🚂 Junction lit; 📋 Log dimmed
  - The Axis layer affects which tools are live (see below)
- Users learn the positions. "Timer is always top-right." "Log is always second row, first slot." Muscle memory.

**Tapping a tabula icon** opens that tool/feature in the viewport. The viewport content changes, the tabula stays. The terminal stays. No fullscreen.

**The 6 Axis Layer Tabs:**
- Below (or above) the 12-icon grid, a row of 6 small tabs: 🏛 🔨 🌹 🪐 ⌛ 🐬
- Each tab represents an Axis layer of the current zip code
- Tapping an Axis tab:
  - Switches the viewport to that floor's content
  - Changes which tabula icons are active (each floor has different available tools)
  - May change which Color vials are illuminated
- The active Axis tab is highlighted. Others are dimmed but always tappable.
- This IS the floor selector. You ride the elevator by tapping Axis tabs.

### Relevator Interaction Summary

```
MINIMAP HALF:                    TABULA HALF:
┌─────────────┐                  ┌─────────────────┐
│             │                  │ [🏋][📖][⏱][🎲] │
│    ◉        │  tap = zip dial  │ [📋][💾][🔀][👤] │
│  minimap    │  hold+drag = nav │ [⚙][🔍][📊][🚂] │
│             │  preview on drag │ ┌───────────────┐ │
├─────────────┤                  │ │🏛 🔨 🌹 🪐 ⌛ 🐬│ │
│⚫🟢🔵🟣🔴🟠🟡⚪│  8 vials       │ └───────────────┘ │
└─────────────┘                  └─────────────────┘
         ↕ mirrorable for handedness ↕
```

---

## The Zip Dial (Relevator Popup)

The 4-dial zip navigation is NOT always visible. It lives inside the Relevator and emerges when summoned.

### Summoning the Dials

- **Tap the minimap** = dials rise from the Relevator, overlaying the lower third
- **Voice command** = "Wilson, open the dial" (if Wilson is active)
- **Keyboard shortcut** (desktop) = spacebar or designated key

### Dial Behavior (when visible)

**Two interaction modes — Spin and Tap:**

**Spin (browse):**
- Vertical scroll within each dial column
- Snap-to with haptic tick
- Wrapping behavior: 7→1→7 for Order, etc.
- Preview: as you spin, the viewport previews the new zip code at reduced opacity

**Tap (quick-nav):**
- Tap the top half of a dial = advance one position forward
- Tap the bottom half = step one position back
- Rapid taps accumulate: tap-tap-tap on Order = advance 3 positions
- Users learn the tap counts. "3 taps on Order = ⛽ to 🌾." Muscle memory.

**Dismiss:** Tap outside the dials, swipe them down, or tap the minimap again. They retract. The Relevator returns to its default state.

### Dial Labels

Each dial position shows:
```
┌──────┐
│  ⛽  │  ← Emoji (large)
│  2   │  ← Numeric position (small)
│ STR  │  ← Short label (tiny, gray)
└──────┘
```

---

## Chat and Community Architecture (Terminal Layer)

### Proximity-Based Chat Rooms

Chat channels are tied to zip code geography. Where you are determines what chat you see. Like MMO zone chat.

**Channel hierarchy:**
- **Room chat** — the specific zip code you're at (e.g., ⛽🏛🪡🔵). Most granular. Smallest groups.
- **Wing chat** — all 8 Colors of the same Order+Axis+Type. Broader conversation about the muscle group/movement pattern.
- **Floor chat** — all rooms on the same Axis floor across the deck. Floor-level discussion (community floor is naturally the busiest).
- **Building chat** — all rooms in the same Order. Day-level conversation (everyone training in ⛽ Strength today).

Users can toggle between channel levels using the terminal's channel switcher. Default: room chat.

### The TLDR Auto-Bot

Every chat channel has an auto-generated context summary. When a user enters a room (or returns after absence), the bot provides:

- **Room tooltip** (first visit): "This is ⛽🏛🪡🔵 — Strength/Basics/Pull/Structured. Heavy barbell pulls, prescribed format. 147 users have visited. Last community activity: 2 hours ago."
- **Catch-up brief** (returning): "Since your last visit (3 days ago): 12 new messages in room chat. User @oak set a PR. The Operis featured this room yesterday. Key topic: grip width on conventional deadlifts."
- **Navigation hint** (onboarding): "Tip: Tap the 🚂 Junction icon on the tabula to see suggested next rooms."

The bot IS the tooltip system. It IS the onboarding system. It IS the "what did I miss" system. One mechanism, multiple functions.

### Wilson in the Terminal

Wilson is the system's voice. Not a chatbot — an interface assistant (see `seeds/wilson-voice-identity.md`).

Wilson responds to:
- Navigation requests: "Take me to today's workout" → dials spin, viewport loads
- Information queries: "What's my 🔴 Output score?" → Wilson reports from vial data
- Context questions: "What happened here?" → Wilson summarizes room activity
- System commands: "Open the dial" → zip dial emerges

Wilson's responses appear in the terminal as text. Portal hyperlinks in Wilson's responses are tappable. Wilson never takes over the viewport — responses stay in the terminal zone.

---

## Return Visits — The Second Open

First-time users land on:
- Terminal: Wilson welcome message + onboarding tooltips
- Viewport: The Operis (today's edition) with the rotation engine's default zip
- Relevator: All tools available, minimap showing starting position

**Second time and beyond:**
- Terminal: Systems brief (weather, calendar, vial summary) + any unread chat activity
- Viewport: Last visited zip code's last state (quicksave) OR today's rotation default (user preference)
- Relevator: Same layout, but tabula icons reflect what's active at the current zip
- Fog of war state persistent — the world remembers exploration history

**The app opens to a living state.** The terminal has new information. The viewport has your place held. The Relevator has your tools ready. Nothing is blank. Nothing requires re-navigation.

---

## Responsive Breakpoints

### Mobile Portrait (Primary — 375px–430px)

The full three-zone composition above. Handedness mirroring in Relevator. All zones visible simultaneously.

### Mobile Landscape

```
┌──────────────────────────────────────────────────────┐
│ ┌──────────┐ ┌──────────────────────┐ ┌────────────┐│
│ │          │ │                      │ │   TABULA   ││
│ │ TERMINAL │ │     VIEWPORT         │ │  [🏋][📖] ││
│ │ (compact │ │     (expanded,       │ │  [📋][💾] ││
│ │  text    │ │      primary         │ │  [⚙][🔍] ││
│ │  scroll) │ │      content)        │ │            ││
│ │          │ │                      │ │  ◉ minimap ││
│ │          │ │                      │ │  [vials]   ││
│ └──────────┘ └──────────────────────┘ └────────────┘│
└──────────────────────────────────────────────────────┘
```
- Terminal compresses to left column (text only, no toggles bar)
- Viewport expands to fill center (more content visible)
- Relevator stacks vertically on right column (tabula + minimap + vials)
- Axis tabs become a vertical strip

### Tablet (768px–1024px)

Same as mobile portrait but roomier. Terminal can show more chat history. Viewport frame has more content resolution. Tabula icons are larger with labels. Vials can show numeric values.

### Desktop (1280px+)

```
┌────────────────────────────────────────────────────────────┐
│ ┌──────────┐ ┌──────────────────────────────┐ ┌──────────┐│
│ │          │ │                              │ │          ││
│ │ TERMINAL │ │        VIEWPORT              │ │  TABULA  ││
│ │          │ │        (large format,        │ │  + AXIS  ││
│ │ full chat│ │         rich content)        │ │  + VIALS ││
│ │ history  │ │                              │ │  + MINI  ││
│ │ Wilson   │ │                              │ │          ││
│ │ friends  │ │                              │ │  [dial   ││
│ │          │ │                              │ │   below] ││
│ └──────────┘ └──────────────────────────────┘ └──────────┘│
└────────────────────────────────────────────────────────────┘
```
- Three-column layout: Terminal left, Viewport center (dominant), Relevator right
- Mouse wheel on minimap = zoom. Click = navigate. Keyboard shortcuts for dials.
- Terminal can be collapsed to give viewport more space (toggle)
- The Relevator panel is a persistent sidebar

---

## Interaction Examples

### "I just want today's workout"

1. Open app → terminal shows systems brief, viewport shows today's rotation zip map
2. Tap 🏋️ Workout on the tabula → workout card loads in viewport
3. Work through blocks, tap exercises to log (terminal stays visible with timer)
4. Finish at 🧮 SAVE → viewport returns to map, terminal shows session summary

### "I want to explore"

1. Tap minimap → zip dials emerge from Relevator
2. Spin or tap dials → viewport previews each zip code's map
3. Release on interesting room → dials retract, map loads in viewport
4. Tap a building on the map → content loads in viewport
5. Portal links in content auto-spin dials → new room loads
6. Quicksave holds position at each stop

### "What's the community talking about?"

1. Tap [🐬] in terminal channel switcher → room chat loads in terminal
2. See TLDR bot summary: "12 messages today. Key topic: grip width."
3. Read chat in terminal while viewport still shows the room's map/content
4. Tap a hyperlink someone posted in chat → viewport navigates to that content

### "I want to check my character"

1. Look at 8 vials in the Relevator → instant balance read
2. Hold a vial → that Color's hub loads in viewport
3. Terminal shows Wilson: "Your 🟢 Self-Reliance has improved 12% this week. Your ⚪ Recovery vial has been declining — consider a 🖼 Restoration room."

### "I need tools while working out"

1. Mid-workout in viewport → tap ⏱ Timer on tabula → timer panel appears in viewport (overlaid, not replacing the workout)
2. Tap 🔀 Swap → exercise substitution options appear in viewport
3. Tap 📊 Stats → personal history at this zip code appears in viewport
4. Each tool opens IN the viewport. The terminal and Relevator stay. Context is never lost.

---

## Design Principles

1. **Three zones, always visible.** Terminal for information. Viewport for content. Relevator for controls. No zone ever fully hides another unless the user deliberately enters immersed mode.

2. **No jarring transitions.** Content changes happen INSIDE the viewport frame. The frame stays. The terminal stays. The Relevator stays. The user never loses context or orientation.

3. **Handedness matters.** The Relevator mirrors for left-hand and right-hand users. The dominant thumb gets the joystick/minimap. The off-hand gets the tabula.

4. **Lights on, lights off.** Every tabula icon has a fixed position. What changes is whether it's active (lit) or inactive (dimmed). Users learn positions, not menus. The same 12 buttons are always there. Context determines which ones glow.

5. **The terminal is alive.** It's not a static header. It's a live feed of information, chat, Wilson responses, and portal hyperlinks. The terminal makes the city feel inhabited.

6. **The Relevator is the cockpit.** Minimap for spatial awareness. Joystick for directional navigation. Dials for precise addressing. Tabula for tools. Vials for stats. Axis tabs for depth layers. Everything a pilot needs, always within thumb reach.

7. **PDA copilot, not social feed.** The app is a personal device. It has tools, communication, navigation, and information — like a PDA from the early 2000s, but designed for the 2020s. It is not a timeline. It is not a feed. It is a device.

---

## Open Questions

- What is the exact 12-icon tabula layout? Which tools are universal vs. contextual? Are some positions reserved for future features?
- How does the minimap joystick interact with the navigation graph? Is movement grid-based (4 directions) or freeform (360-degree)?
- What's the minimap's zoom level? Room-level? Deck-level? Adjustable?
- How does the TLDR auto-bot generate summaries? LLM-powered? Template-based? Wilson-integrated?
- How are chat channels moderated? Per-channel moderators? Community-elected? Automated flagging?
- What's the maximum terminal text history? Infinite scroll? Rolling buffer? Archived per session?
- How does the viewport frame change with Order/Color? Subtle tinting? Border thickness? Ornamental elements?
- Should the tabula have a "favorites" or "custom" row that users can configure?
- How does the Relevator adapt when the zip dials are out? Do vials and axis tabs temporarily compress?
- What's the exact fluid redistribution algorithm? (Weight vector × personal vector → 8 Color scores → fluid allocation)
- How is the map generated from the weight vector? (Procedural? Template-based? Per deck? Per zip?)
- What is the total fluid pool size? Fixed number or percentage-based?
- How does the map composition handle 10,080 content surfaces (1,680 zips × 6 floors)?
- What triggers sludge accumulation? Time-based neglect? Active negative signals?
- How do the vials interact with the 12 Houses? Does House influence which vials are naturally fuller?
- How does proximity-based chat scale? 1,680 potential room channels — most will be empty at any given time. How does the system handle sparse channels?
- How does left/right mirroring interact with muscle memory? Does the mirror ALSO flip tabula icon positions or keep them absolute?

---

🧮
