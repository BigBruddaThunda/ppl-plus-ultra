# HTML Experience Layer

This directory will contain the Ppl± interactive experience layer built with Next.js.

**Status: Phase 4/5 — Blueprinted, Not Built**

No functional code exists yet. Complete technical architecture specified in `seeds/experience-layer-blueprint.md`. 20-session build plan in `seeds/claude-code-build-sequence.md`.

## Routing — Numeric Zip System

Every room URL uses the 4-digit numeric zip code: `/zip/2123` → ⛽🏛🪡🔵. The emoji is display. The number is the URL. See `seeds/numeric-zip-system.md`.

Floor-level routes for non-room content: `/tools`, `/almanac`, `/learn`, `/community`. See `seeds/voice-parser-architecture.md` for the routing architecture.

## Tech Stack

Next.js 14 (App Router) + TypeScript + Tailwind CSS + Supabase + Stripe + Zustand + Framer Motion. Full spec: `seeds/experience-layer-blueprint.md`.

## Mobile UI — 4 Interaction States

1. **Immersed** — Full-screen room, floating 🏠 button
2. **Dial Active** — 4-dial Price-is-Right lock from bottom
3. **Drawer Open** — 🔨 tool drawer with timers, nav, settings
4. **Full Tool Floor** — Axis dial on 🔨 + drawer open → full settings

Full spec: `seeds/mobile-ui-architecture.md`.

## Voice Navigation

Universal natural language parser: any speech → zip + floor + content type. Handles workouts, info queries, personal data, almanac, education, community, playlists. ~13,000 keywords, no AI model, client-side milliseconds. Wilson is the voice identity. Full spec: `seeds/voice-parser-architecture.md`, `seeds/wilson-voice-identity.md`.

## Automotive Layer

Android Auto + Apple CarPlay: Operis read aloud, voice zip navigation, curated playlists, free-tier audio funnel. Full spec: `seeds/automotive-layer-architecture.md`.

## design-system/

CSS design tokens by SCL category: 8 Color palettes, 7 Order densities, 6 Axis typographies, 5 Type identities, 22 Block visual identities, 12 Operator styles.

## floors/

6 app-level content spaces: firmitas (🏛 arrival), utilitas (🔨 tools), venustas (🌹 personal), gravitas (🪐 deep), temporitas (⌛ calendar), sociatas (🐬 community).

## components/

ZipDial, DialPanel, HomeButton, ToolDrawer, ZoomCanvas, WorkoutBlock, RoomView, ExerciseLogger, PaywallGate, OperisEdition, ZipPortal, FloorSelector, RandomGenerator, SessionSummary, ThreadList, VoiceInput, ParseResults.

## assets/

Fonts, SVG icons from SCL emojis, textures.

## Build Sequence

20 sessions in `seeds/claude-code-build-sequence.md`: A (skeleton) → B (rendering) → C (dials) → C-2 (voice parser) → D (auth) → E (onboarding) → F (Stripe) → G (logging) → H (saved rooms) → I (Operis) → J (floors) → K (zoom) → L (community) → M (data export) → N (deploy) → V-Z (automotive).

## Rendering Pipeline

```
.md card → MDX → Frontmatter → zip_metadata
→ Block decomposition → Weight vector → CSS tokens
→ React components → Interactive overlay → User context
→ Rendered room
```
