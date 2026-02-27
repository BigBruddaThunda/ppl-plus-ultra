---
planted: 2026-02-26
status: SEED
phase-relevance: Phase 4/5/6/7
blocks: nothing in Phase 2-3
depends-on: seeds/platform-architecture-v2.md, seeds/elevator-architecture.md, seeds/numeric-zip-system.md, middle-math/ARCHITECTURE.md
connects-to: seeds/mobile-ui-architecture.md, seeds/stripe-integration-pipeline.md, seeds/data-ethics-architecture.md, seeds/claude-code-build-sequence.md, seeds/voice-parser-architecture.md, seeds/automotive-layer-architecture.md, seeds/wilson-voice-identity.md, seeds/regional-filter-architecture.md
supersedes: nothing (first comprehensive experience layer spec)
---

# 🧮 PPL± Experience Layer Blueprint — The Complete Technical Architecture

🔵🟣 — structured + precise

## One Sentence

The PPL± experience layer is a single Next.js application that renders 1,680 distinct room experiences from one codebase, one database, and one design system — where the 4-digit numeric zip code is the universal routing key, the middle-math weight vector is the rendering instruction, and the user's subscription tier gates access through Supabase row-level security and Stripe webhook lifecycle management.

---

## The Core Premise

Every zip code is a room. Every room is a URL. Every URL is a complete experience with six floors of depth, user-specific state, and interactive space. All 1,680 rooms share one codebase, one database, one user account system, and one rendering engine. The zip code is the variable. Everything else is infrastructure.

This is not 1,680 static pages. It is one dynamic page that reconfigures completely based on the 4-digit address. The `.md` card is the architectural blueprint. The middle-math weight vector is the rendering instruction. The user context layer personalizes it. 1,680 distinct experiences from one system.

---

## Tech Stack

| Layer | Technology | Role |
|-------|-----------|------|
| Frontend | Next.js 14+ (App Router), TypeScript | File-system routing maps to zip addressing. Server + client components. |
| Styling | Tailwind CSS + PPL± design tokens | 8 Color palettes, 7 Order densities, 6 Axis typographies. CSS custom properties from weight vector. |
| Client State | Zustand | Dial positions, floor, panel state, timers. |
| Database | Supabase (PostgreSQL + Auth + Storage + Realtime) | RLS enforces tier gating. Realtime for community. Auth handles identity. |
| Hosting | Vercel | Auto-deploy from GitHub. Edge functions. ISR for room pages. |
| Payments | Stripe | Two subscription products. Customer Portal. Webhooks. |
| Realtime | Supabase Realtime | Per-zip channels for 🐬 community floor. |
| Email | Resend | Transactional only. |
| Content | MDX | Renders .md cards into React components. |
| Gesture/Animation | Framer Motion + @use-gesture/react | Dial physics, drawer slide, pinch-zoom, haptic snap. |

---

## URL Routing

```
/                              → Operis (today)
/operis/[date]                 → Specific edition
/zip/[zipcode]                 → Room entry (e.g., /zip/2123)
/zip/[zipcode]/tools           → 🔨 floor
/zip/[zipcode]/time            → ⌛ floor
/zip/[zipcode]/community       → 🐬 floor
/zip/[zipcode]/personal        → 🌹 floor
/zip/[zipcode]/deep            → 🪐 floor
/deck/[number]                 → Deck overview (1-42)
/me                            → Dashboard
/me/library                    → Saved rooms
/me/history                    → Training logs
/me/settings                   → Account, subscription, toggles, export, delete
/tools                         → 🔨 floor-level (exercise library, calculators)
/tools/exercise/[name]         → Exercise entry
/almanac                       → ⌛ floor-level (seasonal, calendar)
/learn/[topic]                 → 🪐 floor-level (educational)
/community                     → 🐬 floor-level overview
/subscribe                     → Stripe checkout
/api/stripe/webhook            → Stripe events
/api/rotation/today            → Default zip derivation
/api/zip/[zipcode]/weight      → Weight vector
/api/user/export               → Full data export (JSON)
/api/user/delete               → Account deletion cascade
/api/audio/operis/today        → Operis audio stream (car layer)
/api/audio/zip/[zipcode]/preview → Zip audio preview
```

---

## Rendering Pipeline

```
.md card → MDX parser → Frontmatter → zip_metadata table
    ↓ Block decomposition
Weight vector (61 values) → Design tokens → CSS custom properties
    ↓ React component tree
Interactive overlay (logging, timers, swap)
    ↓ User context merge (profile + ledger + toggles)
Rendered room
```

Room pages use ISR. EMPTY rooms show construction placeholder. GENERATED rooms render full. CANONICAL rooms render with verification marker. Revalidation on card status change.

---

## Weight Vector → CSS

Color weights → UI palette. Order weights → information density. Axis weights → typography. The zip code is a complete rendering instruction, not just a workout address.

```typescript
// Weight vector shapes UI tokens, not just exercise selection
function weightsToCSSVars(weights: WeightVector): Record<string, string> {
  return {
    '--ui-saturation': `${50 + weights.color * 6}%`,
    '--ui-density': `${weights.order > 0 ? 'compact' : 'spacious'}`,
    '--ui-font-weight': `${400 + weights.axis * 50}`,
    '--ui-rest-color': colorPaletteFromWeight(weights.color),
    '--block-border-radius': `${4 + Math.abs(weights.axis) * 2}px`,
  };
}
```

---

## The Voice Layer

A universal natural language parser converts any spoken or typed input into a building address — zip code + floor + content type — by scoring against the full PPL± vocabulary (61 SCL attributes, 6 floors, 109 content types, ~2,185 exercises). Handles workouts, exercise info queries, personal progress, community browsing, almanac content, educational topics, playlists, and multi-intent input. No AI model required. ~13,000 keyword entries, runs client-side in milliseconds.

Wilson is the voice identity — the audio rendering of the publication standard. Register shifts by floor context. Not a chatbot.

See: `seeds/voice-parser-architecture.md`, `seeds/wilson-voice-identity.md`

---

## The Automotive Layer

Android Auto and Apple CarPlay: the Operis read aloud, zip code audio previews, curated playlists, voice navigation via the parser. The car is the free-tier daily touchpoint that converts through familiarity, not frustration.

See: `seeds/automotive-layer-architecture.md`

---

## The Regional Filter

User-selected region (no GPS, no tracking) adjusts seasonal content, almanac information, and Operis framing. Manual, opt-in, changeable at will.

See: `seeds/regional-filter-architecture.md`

---

## The Data Ethics Position

No analytics fingerprinting. No third-party tracking. No selling data. Full export. Full deletion. The business model is subscriptions — the user is the customer, not the product. Architecture IS the ethics.

See: `seeds/data-ethics-architecture.md`

---

## Reference Documents

| Document | What It Specifies |
|----------|-------------------|
| `seeds/numeric-zip-system.md` | 4-digit addressing standard |
| `seeds/mobile-ui-architecture.md` | 4-dial UI, tool drawer, pinch-zoom canvas |
| `seeds/data-ethics-architecture.md` | Privacy, export, deletion |
| `seeds/stripe-integration-pipeline.md` | Subscription products, checkout, webhooks |
| `seeds/claude-code-build-sequence.md` | 20-session build plan |
| `seeds/voice-parser-architecture.md` | Universal building navigation parser |
| `seeds/wilson-voice-identity.md` | Wilson: the PPL± voice |
| `seeds/automotive-layer-architecture.md` | Car audio layer |
| `seeds/regional-filter-architecture.md` | Opt-in regional content filter |
| `seeds/platform-architecture-v2.md` | Business model, UX, database schema |
| `seeds/elevator-architecture.md` | Floor stack, building model |
| `seeds/operis-architecture.md` | Publication system |
| `middle-math/ARCHITECTURE.md` | Computation engine |

---

🧮
