---
planted: 2026-02-26
status: SEED
phase-relevance: Phase 4/5/6/7
blocks: nothing in Phase 2-3
depends-on: all other experience layer seeds
connects-to: whiteboard.md
---

# 🏗 Claude Code Build Sequence — 20 Sessions from Skeleton to Production

🔵🔨 — structured + functional

## How To Use This Document

This document is the execution roadmap for building the PPL± experience layer. It is written for Claude Code sessions that will execute each step.

Each session is scoped to produce a working increment. "Working" means: you can run it, navigate to it, and the specified behavior is observable. Nothing is "done" until the test section passes.

Sessions do not have to be executed in strict sequence, but the dependency chain must be honored. Dependencies are noted per session.

**Session pattern:**
1. Read this session's entry in this document
2. Read any referenced seed/schema documents
3. Build only what is listed under "Build this session"
4. Do NOT build anything listed under "Not this session"
5. Confirm the test criteria pass before marking the session complete
6. Update whiteboard.md with results

---

## LAUNCH SESSIONS (A through N)

---

### Session A — Next.js Skeleton + Zip Routing

**Goal:** A running Next.js app with proof-of-concept numeric zip routing.

**Depends on:** Nothing (Session A is the root).

**Build this session:**
1. Initialize Next.js 14 app with App Router and TypeScript in `/ppl-plus-ultra-app/` (separate from the cards repo)
2. Install: tailwindcss, zustand, @supabase/supabase-js (no auth yet)
3. Create `/app/zip/[zipcode]/page.tsx` — accepts 4-digit zip in URL
4. Implement `isValidZip()` and `zipToEmoji()` from `seeds/numeric-zip-system.md`
5. Room page renders: zip code display (numeric + emoji), placeholder card area
6. Create `/app/page.tsx` — homepage redirects to `/zip/2123` (today's placeholder)
7. Implement 404 for invalid zip codes (e.g., `/zip/9999` → not found page)

**Not this session:** Auth, database, real card content, dials, drawer, payment.

**Test before done:**
- `http://localhost:3000/zip/2123` loads and shows ⛽🏛🪡🔵
- `http://localhost:3000/zip/7658` loads and shows 🖼🐬➖⚪
- `http://localhost:3000/zip/9999` shows a 404 page
- `http://localhost:3000/` redirects to a zip page

---

### Session B — Card Rendering

**Goal:** Actual `.md` card content renders in the room.

**Depends on:** Session A.

**Build this session:**
1. Install: @next/mdx, gray-matter (or next-mdx-remote)
2. Copy all card `.md` files from `/cards/` into the app's static content directory (or reference via file path)
3. Parse frontmatter to extract zip, status, operator, deck
4. Build `WorkoutCard` React component — renders block sections with emoji headers
5. Build `BlockSection` component — renders each 🧈 🔢 ♨️ etc. block
6. Room page at `/zip/[zipcode]` now renders actual card content for GENERATED/CANONICAL cards
7. EMPTY status → show construction placeholder ("This room is being built")
8. Implement basic typographic styles in Tailwind

**Not this session:** Dials, drawer, logging, interactive elements, auth.

**Test before done:**
- `/zip/2123` renders ⛽🏛🪡🔵 card content (a Deck 07 card, if generated)
- Block sections are visually distinct
- EMPTY cards show placeholder
- Card title, subtitle, CODE line, INTENTION are all visible

---

### Session C — 4-Dial Navigation

**Goal:** The Price-is-Right dial navigator is functional.

**Depends on:** Session A.

**Build this session:**
1. Install: framer-motion, @use-gesture/react
2. Build `ZipDial` component — 4 vertical scroll columns per `seeds/mobile-ui-architecture.md`
3. Implement snap-to-position with spring physics
4. Each dial item shows emoji (large) + number (small)
5. Dials rise from bottom when 🏠 button tapped
6. [Go] button navigates to selected zip via Next.js router
7. [Cancel] / outside tap dismisses dials
8. Implement `DialPanel` wrapping component managing all 4 dials + Go/Cancel

**Not this session:** Drawer, auth, logging, haptics (add later), wrapping behavior.

**Test before done:**
- Tap 🏠 → dials appear from bottom with animation
- Scroll each dial independently
- [Go] navigates to correct zip
- [Cancel] dismisses without navigation
- Selected zip updates live as user scrolls

---

### Session C-2 — Voice Parser

**Goal:** Natural language input routes to zip + floor + content type. Client-side, no AI model.

**Depends on:** Session A, Session C (for routing).

**Build this session:**
1. Build the 3-layer keyword dictionary per `seeds/voice-parser-architecture.md`
   - Layer 1: zip keywords (all 26 dial positions × synonyms)
   - Layer 2: floor keywords (6 floors × synonyms)
   - Layer 3: content type keywords (subset for launch — top 30 types)
2. Build `scoreInput()` function — tokenize, match, score each layer
3. Build `routeFromParse()` — converts parse result to Next.js route
4. Build `VoiceInput` component — text input field + mic button (Web Speech API)
5. Wire into Tool Drawer as search input
6. Show parse results: "Routing you to: ⛽🏛🪡🔵 — Strength, Basics, Pull, Structured"
7. Navigate on confirmation (or immediately if confidence > 0.85)

**Not this session:** Full 109 content types (expand post-launch), exercise search within parser, Wilson TTS response.

**Test before done:**
- "heavy pull day" → routes to ⛽🏛🪡 + highest-confidence Color
- "bodyweight legs" → routes to a 🟢 Legs zip
- "restoration" → routes to 🖼 Order
- "exercise library" → routes to /tools
- Parse completes in < 50ms on device

---

### Session D — Auth + Profiles

**Goal:** User accounts work. Login, signup, basic profile.

**Depends on:** Session A.

**Build this session:**
1. Configure Supabase project (create if not exists), enable Auth (email/password)
2. Create `profiles` table per `middle-math/schemas/user-profile-schema.md` + Stripe columns from `seeds/stripe-integration-pipeline.md`
3. Enable RLS on profiles. Implement "users own their own row" policy
4. Build signup page (`/signup`), login page (`/login`), logout endpoint
5. Build `getAuthUser()` server helper using Supabase Auth
6. Protect `/me` route — redirect to login if unauthenticated
7. Build `/me` page (minimal: shows email, tier = 0/Free)
8. Auto-create profile row on signup via Supabase trigger

**Not this session:** Stripe, paid features, equipment toggles, email verification flow.

**Test before done:**
- Signup creates user + profile row
- Login returns to /me
- /me shows email
- Unauthenticated /me → redirect to /login
- Profile row has tier = 0 (Free) by default

---

### Session E — Onboarding

**Goal:** New user gets equipment profile and region set during onboarding.

**Depends on:** Session D.

**Build this session:**
1. Build `user_exercise_toggles` table per `middle-math/schemas/user-toggles-schema.md`
2. Build onboarding flow (`/onboarding`): 3-step modal after first signup
   - Step 1: Equipment selection (which tiers do you have access to?)
   - Step 2: Region selection (see `seeds/regional-filter-architecture.md` — 2-level picker)
   - Step 3: First zip suggestion (today's Operis recommendation)
3. Save toggles and region to database
4. Mark profile `onboarding_complete = true`
5. Redirect post-onboarding to first suggested zip
6. Add `/me/settings` page with: equipment toggles, region picker, subscription link

**Not this session:** Stripe payment, full toggle system (launch with equipment tiers only).

**Test before done:**
- New user sees onboarding after signup
- Equipment selection saves toggles to database
- Region saves to profile
- Returning user skips onboarding
- /me/settings shows toggles and region

---

### Session F — Stripe Integration

**Goal:** Subscriptions work. Free → Tier 1 → Tier 2 flow is complete.

**Depends on:** Session D.

**Build this session:**
1. Create two Stripe products per `seeds/stripe-integration-pipeline.md`
2. Build `/subscribe` page with Tier 1 and Tier 2 options
3. Build Stripe Checkout session creation endpoint (`/api/stripe/checkout`)
4. Build webhook handler (`/api/stripe/webhook`) — all events from the pipeline spec
5. Implement Customer Portal endpoint (`/api/stripe/portal`)
6. Add "Manage Subscription" link in `/me/settings`
7. Implement `PaywallGate` component — wraps Tier 1+ content, shows upgrade CTA if tier = 0
8. Add RLS policies for tier-gated tables

**Not this session:** Annual pricing, promo codes, trial periods.

**Test before done:**
- Free user sees PaywallGate on room content
- Stripe Checkout opens for Tier 1 selection
- Test webhook fires → profile tier updates to 1
- Tier 1 user accesses room content without paywall
- Customer Portal opens from /me/settings

---

### Session G — Workout Logging

**Goal:** Users can log sets during a workout session.

**Depends on:** Sessions B, D, F.

**Build this session:**
1. Create `workout_logs` table per `middle-math/schemas/user-ledger-schema.md`
2. Build logging overlay — slides up from block when user taps log button
3. Log entry: zip_code, block_name, exercise_name, sets, reps, weight, notes, date
4. Build `SessionSummary` component — appears at 🧮 SAVE block, shows session recap
5. Save session to workout_logs on SAVE
6. Show log count per zip in room header ("You've done this 3 times")
7. Build `/me/history` page — list of logged sessions, sortable by date/zip

**Not this session:** Progress graphs, PR detection, export (Session M).

**Test before done:**
- User taps log → logging overlay appears
- Fills in sets/reps/weight → saves to database
- 🧮 SAVE shows session recap
- /me/history lists logged sessions
- Room shows "You've done this N times"

---

### Session H — Saved Rooms + Personal Library

**Goal:** Users can save rooms and build a personal library.

**Depends on:** Sessions B, D, F.

**Build this session:**
1. Create `saved_workouts` table (user_id, zip_code, saved_at, notes)
2. Add "Save this room" to tool drawer — toggles saved state
3. Build `/me/library` page — grid of saved rooms with emoji, title, last-visited date
4. Add `zip_visits` table — tracks when each zip was visited (for "last visited" display)
5. Build `RandomGenerator` component — rolls a random zip from user's saved rooms

**Not this session:** Shared libraries, collaborative playlists, program sequences.

**Test before done:**
- Save button in drawer saves room
- /me/library shows saved rooms
- Unsave removes from library
- "Last visited" date shows correctly
- Random generator rolls from saved rooms

---

### Session I — Operis

**Goal:** The daily Operis edition is live.

**Depends on:** Sessions A, B, D.

**Build this session:**
1. Build `OperisEdition` component — today's zip recommendation + context paragraph
2. Implement default rotation engine (simplified): Order by weekday, Type by day-of-month
3. Build `/` homepage as Operis landing — today's edition, zip entry, deck overview
4. Build `/operis/[date]` for historical editions
5. Build Operis metadata (editorial title, intro sentence, 3-zip set for the day)
6. Store Operis editions in database (operis_editions table)

**Not this session:** Full 17-department Operis, Wilson TTS, car layer.

**Test before done:**
- / shows today's Operis
- Today's zip is valid and loads
- /operis/2026-03-01 loads historical edition
- Zip changes by day (different Order on different weekdays)

---

### Session J — Six Floors

**Goal:** All 6 Axis floors are accessible from any room.

**Depends on:** Sessions A, B.

**Build this session:**
1. Build `FloorSelector` component — 6-icon strip, navigates between floors
2. Build `/zip/[zipcode]/tools` (🔨 floor) — exercise library entry for this workout
3. Build `/zip/[zipcode]/time` (⌛ floor) — session timer, EMOM builder for relevant zips
4. Build `/zip/[zipcode]/personal` (🌹 floor) — user's history and stats at this zip (Tier 1)
5. Build `/zip/[zipcode]/deep` (🪐 floor) — educational context for this zip's training focus
6. Implement floor-aware header styling (Axis color applies to floor UI)
7. Build `/tools` top-level floor page — searchable exercise library

**Not this session:** Community floor (Session L), full educational content, almanac.

**Test before done:**
- FloorSelector visible in room
- All 5 implemented floors load
- Each floor has at least minimal content
- Floor URL structure works (/zip/2123/tools etc.)

---

### Session K — Pinch-Zoom Canvas

**Goal:** The room content area is a zoomable canvas with deck map at full zoom-out.

**Depends on:** Sessions B, C.

**Build this session:**
1. Wrap room content in a zoomable container using @use-gesture/react
2. At 0.5x: show block overview chips (compact block list)
3. At 0.25x: show deck map — 40-room grid with current zip highlighted
4. Build `DeckMap` component — 8×5 grid (8 Colors × 5 Types) for current deck
5. Tap on block chip at 0.5x → scroll back to 1x at that block
6. Tap on room in deck map → navigate to that zip
7. Show deck number and position in deck as overlay text at zoom < 1x

**Not this session:** 3D transitions, cross-deck navigation, full cosmogram layer.

**Test before done:**
- Pinch out → zoom in (content larger)
- Pinch in → zoom out to 0.5x shows block chips
- Further pinch out shows deck map
- Tap block chip → jump to block at 1x
- Tap zip in deck map → navigate to room

---

### Session L — Community Floor

**Goal:** The 🐬 Sociatas floor is live for Tier 2 users.

**Depends on:** Sessions D, F.

**Build this session:**
1. Create `community_posts` and `community_replies` tables
2. Enable Supabase Realtime on community_posts for per-zip channels
3. Build `/zip/[zipcode]/community` (🐬 floor) — thread list for this room
4. Build `ThreadList` component — shows posts + reply counts
5. Build post creation and reply UI (Tier 2 only)
6. Implement paywall for Tier 1 users viewing community (read-only preview)
7. Build `/community` top-level page — recent activity across all floors

**Not this session:** Moderation tools, reporting, DMs.

**Test before done:**
- Tier 2 user can create a post in any room
- Tier 1 user sees posts but cannot reply (upgrade CTA)
- Free user sees paywall
- Realtime: new post appears without refresh
- /community top-level shows recent activity

---

### Session M — Data Export + Deletion

**Goal:** Full GDPR-style data control is implemented.

**Depends on:** Sessions D, G, H.

**Build this session:**
1. Build `GET /api/user/export` per `seeds/data-ethics-architecture.md`
2. Build `DELETE /api/user/delete` with full cascade per data-ethics spec
3. Add "Export my data" button to `/me/settings` — downloads JSON
4. Add "Delete my account" button with confirmation flow (type "DELETE MY ACCOUNT")
5. Test deletion cancels Stripe subscription before database deletion
6. Add privacy information section to `/me/settings` explaining data model

**Not this session:** Legal privacy policy page (requires lawyer, not Claude Code).

**Test before done:**
- Export downloads valid JSON with all user data
- Deletion removes all rows from all tables
- Deletion cancels Stripe subscription
- Deleted user cannot log back in
- The "DELETE MY ACCOUNT" confirmation prevents accidental deletion

---

### Session N — Production Deployment

**Goal:** The app is live at its production domain.

**Depends on:** All previous sessions.

**Build this session:**
1. Configure Vercel project, connect GitHub repo, set all environment variables
2. Configure Supabase production project (separate from dev/staging)
3. Set Stripe to live mode, register webhook endpoint with production URL
4. Configure custom domain (DNS, SSL)
5. Run all Supabase migrations in production
6. Verify ISR revalidation works for card pages
7. Set up Vercel analytics (privacy-preserving: Vercel's own, no third-party SDKs)
8. Smoke test all critical flows in production

**Not this session:** Load testing, monitoring dashboards, error tracking integration.

**Test before done:**
- Production URL resolves and loads
- Signup → Stripe → Tier 1 access works end-to-end
- A workout can be logged
- Data export works
- No console errors on critical paths

---

## POST-LAUNCH SESSIONS (V through Z — Automotive Layer)

---

### Session V — TTS Pipeline + Wilson Voice

**Goal:** Workout content and Operis can be read aloud with Wilson's voice identity.

**Depends on:** Sessions A, I (Operis). `seeds/wilson-voice-identity.md`.

**Build this session:**
1. Select TTS provider (ElevenLabs preferred — voice cloning from Jake's recording)
2. Build SSML formatter — converts .md card blocks to SSML speech markup
3. Build Wilson response patterns for: workout intro, block transitions, SAVE closing
4. Build `/api/audio/zip/[zipcode]/preview` — 30-second preview audio
5. Build `/api/audio/operis/today` — full Operis read-aloud audio stream
6. Cache generated audio in Supabase Storage (invalidate on card update)

### Session W — Playlist Layer

**Goal:** Curated workout playlists based on Order × Color mood.

**Depends on:** Session V. `seeds/automotive-layer-architecture.md`.

**Build this session:**
1. Derive 56 mood profiles (7 Orders × 8 Colors)
2. Map moods to Spotify and Apple Music search queries or playlist IDs
3. Build `mood_playlists` table (zip_pattern, spotify_query, apple_music_query, mood_label)
4. Build `/api/playlist/[zipcode]` — returns playlist deep link for the zip's mood
5. Display playlist suggestion in Tool Drawer (🎵 Playlist for this session)

### Session X — Audio API + Android Auto

**Goal:** Android Auto integration for Operis audio and zip navigation.

**Depends on:** Sessions V, W. Android Auto developer program enrollment required.

**Build this session:**
1. Build Android Auto Media app (Kotlin/Android) using Media3 library
2. Implement MediaBrowserService exposing: Today's Operis, Saved Rooms, Deck Browse
3. Zip audio preview playback via `/api/audio/zip/[zipcode]/preview`
4. Steering wheel button mapping: next block, pause/resume
5. Voice parser via Android Auto voice input

### Session Y — Apple CarPlay

**Goal:** CarPlay integration mirrors Android Auto functionality.

**Depends on:** Session X (shared audio API). CarPlay entitlement from Apple required.

**Build this session:**
1. Build CarPlay app (Swift/iOS) using CPListTemplate
2. Implement content mirroring from Android Auto MediaBrowserService model
3. CarPlay touchscreen layout: Operis today, Saved Rooms, Browse by Order

### Session Z — Free Tier Audio Funnel

**Goal:** Free tier users experience the daily Operis audio in car without subscription.

**Depends on:** Sessions V, X, Y.

**Build this session:**
1. Make Operis audio accessible without authentication in both Auto and CarPlay apps
2. Implement conversion prompt at natural moment (end of Operis read): "Log this session with a Library Card"
3. Build attribution tracking: car → web → signup funnel (no fingerprinting — use explicit UTM param on QR code displayed in car)
4. Verify free tier audio works with no login

---

## Session Summary Table

| Session | What It Builds | Key Dependency |
|---------|---------------|----------------|
| A | Skeleton + zip routing | None |
| B | Card rendering (MDX) | A |
| C | 4-dial navigation | A |
| C-2 | Voice parser | A, C |
| D | Auth + profiles | A |
| E | Onboarding | D |
| F | Stripe + payments | D |
| G | Workout logging | B, D, F |
| H | Saved rooms | B, D, F |
| I | Operis | A, B, D |
| J | Six floors | A, B |
| K | Pinch-zoom canvas | B, C |
| L | Community floor | D, F |
| M | Data export + deletion | D, G, H |
| N | Production deployment | All |
| V | TTS + Wilson | A, I |
| W | Playlists | V |
| X | Android Auto | V, W |
| Y | Apple CarPlay | X |
| Z | Free audio funnel | V, X, Y |

---

🧮
