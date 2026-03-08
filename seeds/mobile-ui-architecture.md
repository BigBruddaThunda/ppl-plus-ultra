---
planted: 2026-02-26
status: SEED
phase-relevance: Phase 4/5
blocks: nothing in Phase 2-3
depends-on: seeds/elevator-architecture.md, seeds/numeric-zip-system.md, seeds/axis-as-app-floors.md
connects-to: seeds/experience-layer-blueprint.md, seeds/voice-parser-architecture.md
---

# 📱 Mobile UI Architecture — 4-Dial Navigation, Tool Drawer, Pinch-Zoom Canvas

🔵🔨 — structured + functional

## One Sentence

The Ppl± mobile UI is organized around four interaction states — Immersed, Dial Active, Drawer Open, Full Tool Floor — with a Price-is-Right style 4-dial lock at the bottom for room navigation, a 🔨 tool drawer for utilities, and a pinch-zoom canvas for deeper room exploration.

---

## Screen Anatomy

Phone-first layout (375px → 430px baseline). The screen is the room.

```
┌─────────────────────────┐
│  🏠  [zip emoji] [title]│  ← Floating header (fades on scroll)
│                         │
│                         │
│   ROOM CONTENT          │
│   (workout card,        │
│    floor content)       │
│                         │
│                         │
│                         │
│                         │
├─────────────────────────┤
│  [🔨 drawer handle]     │  ← Swipe up to open drawer
└─────────────────────────┘
```

When no interaction: full-screen room. The workout card or floor content fills the view. The 🏠 button floats at top-left. The drawer handle sits at the bottom edge, barely visible.

---

## Four Interaction States

### State 1: Immersed
The default state. Full-screen room content. Floating 🏠 button (top-left, 44px touch target). Minimal chrome. The room speaks.

Transitions:
- Tap 🏠 → Dial Active (dials rise from bottom)
- Swipe up from bottom edge → Drawer Open
- Pinch inward → Zoom Canvas activates

### State 2: Dial Active
Four vertical dials rise from the bottom of the screen. Each dial is a vertical carousel showing the current position ± 2 options above and below. The current selection snaps to center with a haptic tick.

```
┌─────────────────────────┐
│  Room content (dimmed)  │
│                         │
│                         │
│                         │
├─────────────────────────┤
│  ⛽  🏛  🪡  🔵        │  ← Current zip (center, full opacity)
│  🦋  🔨  🍗  🟣        │  ← One step each direction
│  🏟  🌹  ➕  🔴        │
├─────────────────────────┤
│  [Go]  [Cancel]         │
└─────────────────────────┘
```

**Price-is-Right dial mechanics:**
- Vertical scroll within each dial column
- Snap-to-position with spring physics (Framer Motion)
- Haptic feedback on each position change (vibration API where available)
- Each dial shows: number (small, gray) + emoji (large, primary)
- Wrapping behavior: Order dial wraps 7→1 and 1→7. All dials wrap.
- Touch target per item: minimum 44px height
- Dial column width: ~75px each (4 cols + gutters = ~375px)

**Number display:**
Each dial item shows the numeric position beneath the emoji.
```
  🏛
  1
```
This reinforces the numeric zip system and helps users memorize positions.

**[Go] button:** Navigates to the newly selected zip code.
**[Cancel] / tap outside:** Returns to Immersed state at current zip.

### State 3: Drawer Open
Swipe up from the drawer handle reveals the 🔨 tool drawer. The room content slides up and partially off-screen. The drawer fills the lower 60% of the screen.

```
┌─────────────────────────┐
│  Room content (top 40%) │
├─────────────────────────┤
│  🔨 TOOL DRAWER         │
│  ─────────────────────  │
│  [Always available]     │
│  ⏱ Timer               │
│  🎲 Random zip          │
│  📖 Exercise library    │
│  🗓 Zip history         │
│  ─────────────────────  │
│  [Zip-specific]         │
│  📋 Log this session    │
│  💾 Save this room      │
│  🔀 Swap an exercise    │
│  ─────────────────────  │
│  [Account]              │
│  👤 Me                  │
│  ⚙️ Settings            │
└─────────────────────────┘
```

### State 4: Full Tool Floor
When the Axis dial is on 🔨 AND the drawer is open, the tool floor expands to full-screen. This is the settings/tools environment. The room is gone from view. The drawer content becomes a full application surface.

Transition: Dial Active (🔨 selected) + Drawer Open → Full Tool Floor.
Return: Tap back arrow or navigate to a non-🔨 zip.

---

## Tool Drawer — Contents Specification

### Always Available
| Item | Function |
|------|----------|
| ⏱ Timer | Countdown + stopwatch. Presets from current zip's rest periods. |
| 🎲 Random zip | Roll a new zip code from the current Order (keeps the day's training intent). |
| 📖 Exercise library | Full exercise search. Routes to `/tools/exercise/[name]`. |
| 🗓 Zip history | Last 10 visited rooms. Recent rooms list. |
| 🔍 Voice/text search | Open voice parser input. Any speech → zip + floor + content type. |

### Zip-Specific (appears only when inside a room)
| Item | Function |
|------|----------|
| 📋 Log this session | Open logging overlay for current zip's blocks. |
| 💾 Save this room | Add current zip to personal library. |
| 🔀 Swap an exercise | Substitution engine for one exercise in current workout. |
| 📊 My stats here | Personal history at this zip code. Volume, PRs, dates. |
| ➡️ Next sessions | 🚂 Junction suggestions for this zip. |

### Account Layer
| Item | Function |
|------|----------|
| 👤 Me | Routes to `/me` dashboard. |
| ⚙️ Settings | Routes to `/me/settings`. Subscription, toggles, export, delete. |
| 🌍 Region | Quick-change region picker. |

---

## Pinch-Zoom Canvas

The workout content area is a zoomable canvas. Default view is 1x (full card). Pinch to zoom out reveals meta-information about the room — deck position, block count, related rooms.

**At 1x (default):** Full workout card. Interactive blocks, logging, cues.

**At 0.5x (zoomed out):** Room overview. Block list as compact chips. Zip code metadata visible (deck number, operator, estimated time). Tapping a block chip scrolls back to 1x at that block.

**At 0.25x (full out):** Deck map. The current zip is highlighted in the grid of 40 rooms in its deck. Adjacent zips visible. Tap any zip to navigate. This is the visual version of the dial navigator — spatial rather than sequential.

**Use cases:**
- Quick jump to a specific block without scrolling
- See where you are in the deck
- Navigate to an adjacent room in the same deck
- Overview of session structure before starting

**Pinch-zoom widgets (appear at zoom levels < 1x):**
- Deck position indicator (e.g., "Deck 07 — Room 2123 is position 3 of 5 in Pull")
- Estimated total session time
- Primary muscles (Type emoji + name)
- Equipment summary (Color emoji + tier)

---

## Interaction Flow Examples

### "I just want to work out"
1. Open app → Operis shows today's recommended zip
2. Tap the zip → Immersed in the room
3. Work through blocks, tap to log sets
4. Finish at 🧮 SAVE

### "I want to browse rooms"
1. Tap 🏠 → Dial Active
2. Scroll dials to desired combination
3. Tap [Go] → Room loads
4. Pinch to zoom out → See deck map
5. Tap adjacent room → Navigate

### "I need a timer"
1. Swipe up from bottom → Drawer Open
2. Tap ⏱ Timer → Timer panel expands in drawer
3. Select preset from current zip's rest periods
4. Start timer, keep working

### "I want to change my equipment filter"
1. Scroll Order dial to 🔨 (Functional axis)
2. Swipe up → Drawer Open → Full Tool Floor
3. Navigate to Settings → Equipment toggles
4. Toggle equipment tiers on/off
5. Return to any zip → exercises filtered accordingly

---

## Responsive Considerations

**Phone (primary — 375px to 430px):**
Full specification above applies. All four interaction states active. Haptic feedback enabled.

**Tablet (secondary — 768px to 1024px):**
Dial panel stays at bottom but uses wider column format. Drawer can be persistent sidebar instead of overlay. Pinch-zoom canvas has more room for the deck map.

**Desktop (tertiary — 1280px+):**
Dials become a horizontal nav bar at top. Drawer becomes a right sidebar. Full keyboard navigation. The mobile metaphor is de-emphasized but the navigation structure (4 dials, 6 floors, tool layer) is unchanged. Room content uses a centered column max-width 680px.

**Design principle:** The mobile layout is not a simplified version of the desktop layout. It is the primary layout. Desktop adapts from mobile, not vice versa. The 4-dial interaction is designed for touch first. Keyboard fallback exists but is secondary.

---

🧮
