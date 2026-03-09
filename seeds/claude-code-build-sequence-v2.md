---
planted: 2026-03-09
status: SEED
phase-relevance: Phase 4/5/6/7
supersedes: seeds/claude-code-build-sequence.md
blocks: nothing in Phase 2-3
depends-on: all other experience layer seeds
connects-to: whiteboard.md
---

# Ppl± App Build Sequence V2 — Multi-Agent Workflow Contracts

🔵🔨 — structured + functional

Supersedes: `seeds/claude-code-build-sequence.md` (V1, planted 2026-02-26)

## What Changed From V1

V1 was written before the Next.js skeleton, D-module CSS design system, city compiler architecture, middle-math data layer, exercise content library, and all 1,680 cards were completed. V2 accounts for:

- **Session A is partially done.** The app lives at `/web/`, not `/ppl-plus-ultra-app/`. SCL parser, design tokens, 2 components, and 6 routes already exist.
- **The city compiler** is a new foundational session (A-1) that compiles all 1,680 zips into static JSON objects consumed by every downstream system.
- **The D-module CSS design system** (`html/design-system/`) must be integrated from Session A-prime, not bolted on later.
- **Full Operis pipeline at launch.** Not a simplified rotation engine — the real 4-prompt editorial pipeline with historical events and cosmogram context.
- **Card quality fixes** (1,636 type mismatches, 1,320 thin cards) are woven into the build as Codex background tasks in Waves 1-2.
- **Agent routing** — every session specifies its execution environment (Desktop, Web, Codex, Mobile) and parallelization opportunities.
- **Automation-first** — Jake provides env vars and config upfront via a Setup Session. Only 2 sessions (L: Community, N: Deploy) strictly require Jake at the PC.

---

## How To Use This Document

Each session is scoped to produce a working increment. "Working" means: you can run it, navigate to it, and the specified behavior is observable.

**Session pattern:**
1. Read this session's entry
2. Read any referenced seed/schema documents
3. Build only what is listed under "Build this session"
4. Do NOT build anything listed under "Not this session"
5. Confirm the test criteria pass before marking complete
6. Update whiteboard.md with results

**Agent routing key:**
- **Desktop** = Claude Code CLI on Jake's PC. For sessions requiring human judgment or interactive config.
- **Web** = Claude Code Web session. Runs autonomously while Jake is AFK.
- **Codex** = OpenAI Codex. Isolated batch tasks, content generation, data processing.
- **Mobile** = Jake on phone. Planning, review, architecture decisions.

---

## Skip List — Already Built

These items from V1's Session A are DONE. Do not rebuild:

- [x] Next.js 16.1.6 + React 19 + TypeScript + Tailwind CSS 4 initialized at `/web/`
- [x] `/app/zip/[code]/page.tsx` — accepts numeric zip, parses to emoji
- [x] `isValidZip()`, `parseNumericZip()`, `parseZipCode()` in `web/src/lib/scl.ts`
- [x] Homepage at `/` with Order picker and sample zips
- [x] 404 page for invalid zips at `/app/zip/[code]/not-found.tsx`
- [x] `RoomHeader.tsx` and `RoomShell.tsx` components
- [x] Full design tokens in `web/src/lib/tokens.ts` (8 Colors x 7 Orders → CSS vars)
- [x] Deck number derivation, GOLD gate logic, operator table in `web/src/lib/scl.ts`
- [x] Placeholder routes: `/deck/[number]`, `/operis/[date]`, `/me`
- [x] SQL migrations 001-010 written in `sql/`
- [x] All middle-math JSON data files computed (weight vectors, exercise registry, navigation graph, design tokens, abacus registry, content type registry, floor routing, Wilson audio spec)
- [x] 2,085 exercise content files in `exercise-content/`
- [x] 1,680/1,680 workout cards generated
- [x] D-module CSS design system at `html/design-system/`

---

## WAVE 0 — Foundation (Sessions 0, A', A-1)

Everything downstream depends on Wave 0. These sessions run first.

---

### Session 0 — Setup (One-Time Config)

**Goal:** Provide all secrets, env vars, and external service configs so downstream sessions can run without Jake.

**Agent:** Desktop (Jake at PC, one time only)
**Duration:** 30 minutes
**Depends on:** Nothing

**Do this session:**
1. Create Supabase project (or confirm existing). Record: Project URL, anon key, service role key
2. Run SQL migrations 001-010 against Supabase: `psql $DATABASE_URL < sql/001-*.sql` through `sql/010-*.sql`
3. Create Stripe account (or confirm existing). Create 2 products:
   - Tier 1 "Library Card" — $10/month
   - Tier 2 "Community Pass" — $25/month
   Record: Stripe secret key, publishable key, webhook signing secret, Price IDs for both tiers
4. Write `web/.env.local`:
   ```
   NEXT_PUBLIC_SUPABASE_URL=<url>
   NEXT_PUBLIC_SUPABASE_ANON_KEY=<anon>
   SUPABASE_SERVICE_ROLE_KEY=<service>
   STRIPE_SECRET_KEY=<sk_test_...>
   NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=<pk_test_...>
   STRIPE_WEBHOOK_SECRET=<whsec_...>
   STRIPE_TIER1_PRICE_ID=<price_...>
   STRIPE_TIER2_PRICE_ID=<price_...>
   ```
5. Create `web/.env.example` (same keys, empty values) and commit it
6. Configure Supabase Auth: enable email/password, set redirect URLs
7. Register Stripe webhook endpoint (can update URL post-deploy): `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.deleted`

**Not this session:** Any code changes. This is pure config.

**Test before done:**
- `web/.env.local` exists with all 8 values populated
- `web/.env.example` committed to repo
- Supabase dashboard shows tables from migrations
- Stripe dashboard shows 2 products with prices

---

### Session A' (A-Prime) — Skeleton Completion + D-Module Integration

**Goal:** Wire the existing D-module CSS design system into the Next.js app. Complete the skeleton.

**Agent:** Web (autonomous)
**Depends on:** Nothing (existing code is sufficient)
**Parallelizable with:** Session A-1

**Build this session:**
1. Create `web/src/lib/design-system.ts`:
   - Import D-module proportions from `html/design-system/` Order CSS files (column_ratio, intercolumniation, superposition, entasis per Order)
   - Export `getOrderProportions(order: Order)` returning architectural ratios
   - Export `getFullZipStyle(zip: ZipCode)` merging Color tokens + Order proportions
2. Copy CSS custom properties from `html/design-system/theme.css` into `web/src/app/globals.css` as a foundational layer below Tailwind
3. Update `RoomShell.tsx` to apply D-module proportions (not just color tokens):
   - Column ratio → content width
   - Intercolumniation → gap spacing
   - Superposition → heading stack
4. Install missing deps: `zustand` (state), `gray-matter` (frontmatter parsing)
5. Update `/deck/[number]` route with real 40-room grid (8 Colors x 5 Types) using deck derivation from `scl.ts`
6. Ensure every route loads with correct visual proportions per Order

**Not this session:** Card rendering, auth, database, dials.

**Test before done:**
- `/zip/2123` shows ⛽ (Doric) proportions — wider columns, moderate spacing
- `/zip/1123` shows 🐂 (Tuscan) proportions — widest columns, most space
- `/zip/7658` shows 🖼 (Composite) proportions — most refined ratios
- `/deck/7` shows 40-room grid for Deck 07
- Visual difference between Orders is immediately apparent

---

### Session A-1 — City Compiler

**Goal:** Build the universal resolution engine that compiles any zip code into a complete JSON object. Both Python (batch compilation) and TypeScript (runtime resolution).

**Agent:** Web or Codex (autonomous)
**Depends on:** Nothing (reads existing middle-math JSON files)
**Parallelizable with:** Session A'

**Reference:** `seeds/city-compiler-architecture.md`

**Build this session:**
1. Create `scripts/middle-math/city_compiler.py`:
   - Reads: `weight-vectors.json`, `design-tokens.json`, `navigation-graph.json`, `abacus-registry.json`, `exercise-registry.json`, `content-type-registry.json`, `floor-routing-spec.md`
   - Input: any of emoji zip, numeric zip, deck number, abacus ID
   - Output: 7-section JSON per city compiler architecture:
     ```json
     {
       "address": { "emoji": "⛽🏛🪡🔵", "numeric": "2123", "deck": 7, ... },
       "architecture": { "order_name": "Doric", "column_ratio": 1.78, "intercolumniation": "systyle", ... },
       "palette": { "primary": "#...", "secondary": "#...", "accent": "#...", ... },
       "typography": { "heading_size": "1.5rem", "body_weight": 500, ... },
       "personality": { "operator": "🤌 facio", "polarity": "expressive", ... },
       "connections": { "neighbors": [...], "deck_siblings": [...], "abacus_slot": ... },
       "metadata": { "status": "GENERATED", "deck": 7, "weight_vector": [...] }
     }
     ```
   - Phase A scope only: `address`, `architecture`, `palette`, `typography`, `connections`, `metadata`
   - Defer Phase B (cathedral/watercolor dual palette) and Phase C (art direction layer)
2. Batch-compile all 1,680 zips: `python city_compiler.py compile-all --output middle-math/compiled/zips/`
   - One JSON file per zip: `middle-math/compiled/zips/2123.json`
3. Compile 42 deck centroids: `middle-math/compiled/decks/deck-07.json` etc.
4. Compile 35 abacus centroids: `middle-math/compiled/abaci/`
5. Create `web/src/lib/city-compiler.ts`:
   - Reads compiled JSON files at build time (via `import` or `fs.readFileSync`)
   - Exports `resolveZip(code: string): CompiledZip` — returns typed object
   - Exports `resolveDeck(number: number): CompiledDeck`
   - Exports `resolveAbacus(id: string): CompiledAbacus`
6. Add TypeScript types: `web/src/types/compiled.ts`

**Not this session:** Cathedral/watercolor dual palette (Phase B), art direction layer (Phase C), RPG archetype overlay.

**Test before done:**
- `python city_compiler.py resolve 2123` prints complete JSON
- `python city_compiler.py compile-all` produces 1,680 files in `compiled/zips/`
- `resolveZip("2123")` in TypeScript returns typed `CompiledZip` object
- All 1,680 numeric zips resolve without error
- Deck 07 centroid aggregates its 40 room vectors correctly

---

### WAVE 0 Quality Gate

Before proceeding to Wave 1:
- [ ] City compiler resolves all 1,680 zips to valid JSON
- [ ] D-module proportions render visually distinct per Order
- [ ] All existing routes still work
- [ ] `web/.env.example` committed (if Session 0 done)
- [ ] No TypeScript errors

---

## WAVE 1 — Content Rendering + Card Quality (Sessions B, C, J, Q-1, Q-2)

Card content renders in rooms. Dials navigate between rooms. Quality fixes run in parallel on Codex.

---

### Session B — Card Rendering (MDX Pipeline)

**Goal:** Actual `.md` card content renders in the room.

**Agent:** Web (autonomous)
**Depends on:** Wave 0 (A' + A-1)
**Parallelizable with:** Sessions C, J, Q-1

**Build this session:**
1. Install: `next-mdx-remote` (or `@next/mdx`), `remark-gfm`
2. Create `web/src/lib/card-loader.ts`:
   - Reads `.md` card from `cards/` directory tree by zip code
   - Parses frontmatter via `gray-matter` → `CardFrontmatter`
   - Returns body as MDX-ready string
   - EMPTY status cards return null (triggers placeholder)
3. Create `WorkoutCard.tsx`:
   - Renders full card: title with flanking Type emojis, subtitle, CODE line, INTENTION
   - Parses block sections from markdown content
   - Applies D-module typography scale from compiled zip (heading sizes from column_ratio)
4. Create `BlockSection.tsx`:
   - Renders individual block with emoji header + heavy border separator
   - Handles: exercise lines (reps before name, Type emoji), cue parentheticals, set lines, rest
   - Tree notation rendering (├─ │ etc.)
5. Wire into `/zip/[code]/page.tsx`:
   - Load compiled zip from city compiler
   - Load card from card-loader
   - Render via `RoomShell` > `RoomHeader` > `WorkoutCard`
6. EMPTY cards show "This room is being built" placeholder
7. 🚂 JUNCTION renders follow-up zip codes as navigable links

**Not this session:** Dials, drawer, logging, interactive overlays, auth.

**Test before done:**
- `/zip/2123` renders actual card content with blocks, exercises, cues visible
- Block sections have distinct visual boundaries (═══ separators)
- EMPTY cards show placeholder
- 🚂 JUNCTION zip links navigate to other rooms
- Card title, subtitle, CODE, INTENTION all visible and styled per Order

---

### Session C — 4-Dial Navigation

**Goal:** The Price-is-Right dial navigator is functional.

**Agent:** Web (autonomous)
**Depends on:** Wave 0
**Parallelizable with:** Sessions B, J

**Build this session:**
1. Install: `framer-motion`, `@use-gesture/react`
2. Build `ZipDial.tsx` — 4 vertical scroll columns per `seeds/mobile-ui-architecture.md`
   - Column 1: 7 Orders
   - Column 2: 6 Axes
   - Column 3: 5 Types
   - Column 4: 8 Colors
3. Implement snap-to-position with spring physics
4. Each dial item shows: emoji (large) + numeric index (small) + name
5. Build `DialPanel.tsx` — wraps 4 dials + [Go] + [Cancel] buttons
6. Dials rise from bottom when 🏠 button tapped
7. [Go] navigates to selected zip via Next.js router
8. [Cancel] / outside tap dismisses
9. Current zip pre-selects dials when opened from a room

**Not this session:** Drawer, auth, logging, haptics, wrapping.

**Test before done:**
- Tap 🏠 → dials appear from bottom with animation
- Scroll each dial independently
- [Go] navigates to correct zip (e.g., select ⛽🏛🪡🔵 → `/zip/2123`)
- [Cancel] dismisses without navigation
- Opening dials from `/zip/2123` pre-selects ⛽🏛🪡🔵

---

### Session J — Floors + Exercise Library

**Goal:** All 6 Axis floors are accessible from any room. Exercise library is searchable.

**Agent:** Web (autonomous)
**Depends on:** Wave 0
**Parallelizable with:** Sessions B, C

**Build this session:**
1. Build `FloorSelector.tsx` — 6-icon vertical strip (🏛🔨🌹🪐⌛🐬), shows current Axis highlighted
2. Build `/zip/[code]/tools` (🔨 Utilitas floor):
   - Exercise library filtered to this workout's Type
   - Source: `exercise-registry.json` filtered by scl_type
   - Each exercise links to its `exercise-content/` file if available
3. Build `/zip/[code]/deep` (🪐 Gravitas floor):
   - Educational content placeholder
   - Show cosmogram content if deck cosmogram exists (read from `deck-cosmograms/`)
4. Build `/tools` top-level page:
   - Searchable exercise library (2,085 exercises)
   - Filter by Type, equipment tier, movement pattern
   - Exercise cards show: name, Type emoji, equipment tier, movement pattern
5. Floor-aware header styling from compiled zip's `architecture.superposition` value
6. Build `/zip/[code]/time` (⌛ Temporitas floor) — placeholder with session timer concept
7. Build `/zip/[code]/personal` (🌹 Venustas floor) — placeholder ("Login to see your history here")

**Not this session:** Community floor (Session L), full educational content, interactive timer.

**Test before done:**
- FloorSelector visible in every room
- `/zip/2123/tools` shows Pull exercises from registry
- `/tools` is searchable, returns results in < 200ms
- Floors have distinct URLs and render distinct content
- Floor-aware styling applies (heading scale from superposition)

---

### Session Q-1 — Card Quality: Type Misroutes (Codex Background)

**Goal:** Fix the 1,636 exercise-Type misroute flags identified by the quality audit.

**Agent:** Codex (batch task, runs in background)
**Depends on:** Nothing (operates on card files directly)
**Parallelizable with:** ALL Wave 1 sessions

**Build this session:**
1. Read `reports/deck-quality-audit-2026-03-08.json` for TYPE_MISMATCH flags
2. For each flagged card:
   - Identify the misrouted exercise (e.g., Kettlebell Swing in a 🛒 Push card)
   - Find a valid substitute from `middle-math/exercise-registry.json` matching the card's Type
   - Use `middle-math/exercise-engine/substitution-map.json` for family-aware substitution
   - Replace the exercise in the card file, preserving all other content
3. Run `python scripts/validate-card.py` on each modified card
4. Run `python scripts/audit-exercise-coverage.py` on each modified deck folder

**Not this session:** Content depth fixes (Q-2), card regeneration.

**Test before done:**
- TYPE_MISMATCH count drops from 1,636 to < 50
- All modified cards pass validate-card.py
- No deck has duplicate primary exercises after substitution

---

### Session Q-2 — Card Quality: Content Depth (Codex Background)

**Goal:** Regenerate the 1,320 LIGHT + 180 THIN cards with deeper content.

**Agent:** Codex (batch task, runs in background)
**Depends on:** Nothing (operates on card files directly)
**Parallelizable with:** ALL Wave 1 sessions, runs after Q-1

**Build this session:**
1. Read `reports/deck-quality-audit-2026-03-08.json` for CONTENT_DEPTH flags (LIGHT and THIN)
2. For each flagged card:
   - Read current card content
   - Read deck identity doc if exists (`deck-identities/deck-NN-identity.md`)
   - Regenerate with full SCL rules from CLAUDE.md (all 15 format elements, proper block count, exercise cues, set details)
   - Target: every card > 50 lines
3. Run validation on each regenerated card
4. Commit in deck-sized batches (40 cards per commit)

**Not this session:** New card creation, format changes.

**Test before done:**
- LIGHT + THIN count drops from 1,500 to < 100
- All regenerated cards pass validate-card.py
- Average card line count rises above 60

---

### WAVE 1 Quality Gate

Before proceeding to Wave 2:
- [ ] Card content renders in `/zip/[code]` for any GENERATED card
- [ ] Dials navigate between rooms correctly
- [ ] Exercise library searchable at `/tools`
- [ ] FloorSelector visible in rooms
- [ ] Q-1 Type misroutes < 50 remaining
- [ ] No TypeScript errors, no console errors

---

## WAVE 2 — Auth, Payments, Operis (Sessions D, F, I-full, I-data)

Infrastructure sessions. Auth and payments can overlap with Operis pipeline build.

---

### Session D — Auth + Profiles

**Goal:** User accounts work. Login, signup, basic profile.

**Agent:** Web (autonomous — env vars provided in Session 0)
**Depends on:** Session 0 (env vars)
**Parallelizable with:** Sessions I-data, I-full

**Build this session:**
1. Install: `@supabase/supabase-js`, `@supabase/ssr`
2. Create Supabase client utilities:
   - `web/src/lib/supabase/server.ts` — server-side client
   - `web/src/lib/supabase/client.ts` — client-side client
   - `web/src/lib/supabase/middleware.ts` — auth middleware
3. Build signup page (`/signup`) — email + password form
4. Build login page (`/login`) — email + password form
5. Build logout endpoint
6. Build `getAuthUser()` server helper
7. Protect `/me` route — redirect to login if unauthenticated
8. Build minimal `/me` page — shows email, tier = 0/Free
9. Auto-create profile row on signup via Supabase DB trigger (or on first login)
10. Add middleware to refresh auth token on requests

**Not this session:** Stripe, paid features, equipment toggles, email verification.

**Test before done:**
- Signup creates user + profile row in Supabase
- Login returns to /me
- /me shows email and "Free" tier
- Unauthenticated /me → redirect to /login
- Logout clears session

---

### Session F — Stripe Integration

**Goal:** Subscriptions work. Free → Tier 1 → Tier 2 flow is complete.

**Agent:** Web (autonomous — Stripe keys and Price IDs from Session 0)
**Depends on:** Session 0 (Stripe config), Session D (auth)
**Parallelizable with:** Sessions I-data, I-full (after D completes)

**Build this session:**
1. Install: `stripe`
2. Create `web/src/lib/stripe.ts` — Stripe client init
3. Build `/subscribe` page with Tier 1 ($10/mo) and Tier 2 ($25-30/mo) cards
4. Build `/api/stripe/checkout` — creates Checkout session, redirects
5. Build `/api/stripe/webhook` — handles:
   - `checkout.session.completed` → update profile tier
   - `customer.subscription.updated` → tier change
   - `customer.subscription.deleted` → tier to 0
6. Build `PaywallGate.tsx` — wraps Tier 1+ content, shows upgrade CTA if tier = 0
7. Build `/api/stripe/portal` — opens Stripe Customer Portal
8. Add "Manage Subscription" to `/me` page
9. Add RLS policies: `tier >= 1` for room content, `tier >= 2` for community

**Not this session:** Annual pricing, promo codes, trial periods.

**Test before done:**
- Free user sees PaywallGate on room content
- Stripe Checkout opens for Tier 1
- Webhook fires in test mode → profile tier updates
- Tier 1 user accesses room content without paywall
- Customer Portal opens from /me

---

### Session I-data — Operis Data Population (Codex Background)

**Goal:** Populate the historical events database and enrich cosmograms for Operis pipeline input.

**Agent:** Codex (batch task, runs in background — research-intensive)
**Depends on:** Nothing (writes to flat files)
**Parallelizable with:** ALL Wave 2 sessions

This is the long pole for full Operis. Start immediately.

**Build this session:**
1. Populate `operis-editions/historical-events/` (366 date files, MM-DD.md format):
   - Each file: 5-10 historical events for that date
   - Focus on: science, athletics, architecture, agriculture, cultural milestones
   - Format per `seeds/operis-researcher-prompt.md` Contract A requirements
   - Priority: populate March dates first (current month), then expand outward
2. Enrich 42 deck cosmograms in `deck-cosmograms/`:
   - Read existing v2 scaffold (subject stubs, no web deposits)
   - Add 3-5 research deposits per cosmogram from web sources
   - Upgrade status from DRAFT to ENRICHED
3. This is a multi-run task. Each Codex run handles 30-60 date files or 5-10 cosmograms.

**Not this session:** Operis edition generation (I-full), app integration.

**Test before done:**
- At least 31 date files populated (current month)
- At least 7 cosmograms enriched (one per Order, Decks 01/07/13/19/25/31/37)
- Historical events format matches Contract A requirements

---

### Session I-full — Full Operis Pipeline

**Goal:** The 4-prompt Operis editorial pipeline generates daily editions. Integrated into the app.

**Agent:** Web (autonomous)
**Depends on:** Session D (auth), Session I-data (historical events + cosmograms)
**Parallelizable with:** Session F (after D completes)

**Reference:** `seeds/operis-prompt-pipeline.md`, `seeds/operis-researcher-prompt.md`, `seeds/operis-content-architect-prompt.md`, `seeds/operis-editor-prompt.md`, `seeds/operis-builder-prompt.md`

**Build this session:**
1. Implement rotation engine from `middle-math/rotation/`:
   - Order by weekday (Mon=🐂, Tue=⛽, Wed=🦋, Thu=🏟, Fri=🌾, Sat=⚖, Sun=🖼)
   - Type by rolling 5-day from Jan 1
   - Axis by monthly operator mapping
   - Derive Color of the Day per `seeds/operis-color-posture.md`
2. Build `/api/operis/generate` — runs the 4-prompt pipeline:
   - P1 Researcher: reads historical events for today's date, produces Research Brief
   - P2 Content Architect: takes Research Brief, produces Enriched Content Brief with Color of the Day
   - P3 Editor: writes full Operis edition with 13-room Sandbox (8 siblings + 5 content rooms)
   - P4 Builder: proofs edition, generates cards for empty zip codes if needed
3. Build `OperisEdition.tsx` — full edition renderer:
   - Today's Order + Color identity
   - 13-room Sandbox with zip links
   - Editorial content sections
   - Navigation to historical editions
4. Build `/` homepage as Operis landing — today's edition, quick-nav to rooms
5. Build `/operis/[date]` — historical edition view
6. Create `operis_editions` table (migration 011) — store generated editions
7. Build `/api/operis/cron` — daily generation endpoint (Vercel Cron or equivalent)

**Not this session:** Wilson TTS (Session V), automotive layer.

**Test before done:**
- `/` shows today's Operis with correct Order for weekday
- 13-room Sandbox shows valid zip codes, all navigable
- `/operis/2026-03-09` loads stored edition
- Color of the Day applies to edition styling
- Different days produce different editions (Order, Type, Color shift)

---

### WAVE 2 Quality Gate

Before proceeding to Wave 3:
- [ ] Auth flow works end-to-end (signup → login → /me)
- [ ] Stripe checkout works in test mode (free → Tier 1)
- [ ] PaywallGate blocks free users from room content
- [ ] Operis generates for today and shows on homepage
- [ ] At least 31 historical events files populated (current month)
- [ ] RLS policies active on Supabase

---

## WAVE 3 — User Features (Sessions E, G, H)

Depends on auth + payments from Wave 2. All three sessions are independent and parallelizable.

---

### Session E — Onboarding

**Goal:** New user gets equipment profile and region set during onboarding.

**Agent:** Web (autonomous)
**Depends on:** Session D (auth)
**Parallelizable with:** Sessions G, H

**Build this session:**
1. Create `user_exercise_toggles` table (migration 012) per `middle-math/schemas/user-toggles-schema.md`
2. Build onboarding flow (`/onboarding`): 3-step sequence after first signup
   - Step 1: Equipment selection (which tiers do you have access to? 0-5 checkboxes)
   - Step 2: Region selection per `seeds/regional-filter-architecture.md` (2-level picker, opt-in only)
   - Step 3: First zip suggestion (today's Operis recommendation for their equipment tier)
3. Save toggles and region to database
4. Mark profile `onboarding_complete = true`
5. Redirect post-onboarding to first suggested zip
6. Build `/me/settings` page: equipment toggles, region picker, subscription link

**Not this session:** Full toggle system beyond equipment tiers.

**Test before done:**
- New user sees onboarding after signup
- Equipment selection saves toggles to database
- Region saves to profile
- Returning user skips onboarding
- /me/settings shows toggles and region

---

### Session G — Workout Logging

**Goal:** Users can log sets during a workout session.

**Agent:** Web (autonomous)
**Depends on:** Sessions B (card rendering), D (auth), F (payments)
**Parallelizable with:** Sessions E, H

**Build this session:**
1. Create `workout_logs` table (migration 013) per `middle-math/schemas/user-ledger-schema.md`
2. Build logging overlay — slides up from block when user taps log button
3. Log entry fields: zip_code, block_name, exercise_name, sets, reps, weight, notes, timestamp
4. Build `SessionSummary.tsx` — appears at 🧮 SAVE block, shows session recap
5. Save session to workout_logs on SAVE
6. Show log count per zip in room header ("You've done this 3 times")
7. Build `/me/history` — list of logged sessions, sortable by date/zip/Order

**Not this session:** Progress graphs, PR detection, export.

**Test before done:**
- User taps log → logging overlay appears on block
- Fills in sets/reps/weight → saves to database
- 🧮 SAVE shows session recap with all logged sets
- /me/history lists logged sessions
- Room header shows visit count

---

### Session H — Saved Rooms + Personal Library

**Goal:** Users can save rooms and build a personal library.

**Agent:** Web (autonomous)
**Depends on:** Sessions B (card rendering), D (auth), F (payments)
**Parallelizable with:** Sessions E, G

**Build this session:**
1. Create `saved_workouts` table (migration 014): user_id, zip_code, saved_at, notes
2. Create `zip_visits` table (migration 015): user_id, zip_code, visited_at
3. Add "Save this room" toggle in room UI
4. Build `/me/library` — grid of saved rooms with emoji, title, last-visited
5. Build `RandomGenerator.tsx` — rolls random zip from saved rooms
6. Track zip visits automatically when room loads (for "last visited" display)

**Not this session:** Shared libraries, collaborative playlists, program sequences.

**Test before done:**
- Save button saves room to database
- /me/library shows saved rooms
- Unsave removes from library
- "Last visited" date shows correctly
- Random generator rolls from saved rooms only

---

### WAVE 3 Quality Gate

Before proceeding to Wave 4:
- [ ] New user flows: signup → onboarding → first room → log a set → save room
- [ ] /me/history shows logged sessions
- [ ] /me/library shows saved rooms
- [ ] /me/settings shows equipment toggles
- [ ] Complete user journey works end-to-end without errors

---

## WAVE 4 — Polish + Advanced (Sessions C-2, K, L, M)

---

### Session C-2 — Voice Parser

**Goal:** Natural language input routes to zip + floor + content type. Client-side, no AI model.

**Agent:** Web (autonomous)
**Depends on:** Session C (dials for routing)
**Parallelizable with:** Session K

**Reference:** `seeds/voice-parser-architecture.md`, `middle-math/wilson-audio-spec.md`

**Build this session:**
1. Build 3-layer keyword dictionary from `middle-math/wilson-audio-spec.md` (~2,260 keywords already specified):
   - Layer 1: zip keywords (all 26 dial positions x synonyms)
   - Layer 2: floor keywords (6 floors x synonyms)
   - Layer 3: content type keywords (top 30 types for launch)
2. Build `scoreInput()` — tokenize input, match against layers, score
3. Build `routeFromParse()` — convert parse result to Next.js route
4. Build `VoiceInput.tsx` — text input + mic button (Web Speech API)
5. Wire into room toolbar as search input
6. Show parse result: "Routing you to: ⛽🏛🪡🔵 — Strength, Basics, Pull, Structured"
7. Navigate immediately if confidence > 0.85, else show confirmation

**Not this session:** Full 109 content types, Wilson TTS.

**Test before done:**
- "heavy pull day" → routes to ⛽🪡 + highest-confidence Color
- "bodyweight legs" → routes to a 🟢🍗 zip
- "restoration" → routes to 🖼 Order
- Parse completes in < 50ms

---

### Session K — Pinch-Zoom Canvas

**Goal:** Room content is a zoomable canvas with deck map at full zoom-out.

**Agent:** Web (autonomous)
**Depends on:** Sessions B (card rendering), C (dials)
**Parallelizable with:** Session C-2

**Build this session:**
1. Wrap room content in zoomable container via `@use-gesture/react`
2. At 1x: normal room view (current behavior)
3. At 0.5x: show block overview chips (compact block list)
4. At 0.25x: show deck map — 8x5 grid (8 Colors x 5 Types) for current deck
5. Build `DeckMap.tsx` — grid with current zip highlighted, others navigable
6. Tap block chip at 0.5x → scroll to block at 1x
7. Tap room in deck map at 0.25x → navigate to that zip

**Not this session:** 3D transitions, cross-deck navigation, full cosmogram layer.

**Test before done:**
- Pinch zoom works smoothly
- 0.5x shows block chips
- 0.25x shows deck map with 40 rooms
- Tap interactions work at each zoom level

---

### Session L — Community Floor

**Goal:** The 🐬 Sociatas floor is live for Tier 2 users.

**Agent:** Desktop (requires Supabase Realtime config + moderation policy decisions)
**Depends on:** Sessions D (auth), F (payments)
**Parallelizable with:** Session M

**Build this session:**
1. Create `community_posts` and `community_replies` tables (migration 016)
2. Enable Supabase Realtime on community tables
3. Build `/zip/[code]/community` (🐬 floor) — thread list for this room
4. Build post creation and reply UI (Tier 2 only)
5. Tier 1 sees posts read-only with upgrade CTA
6. Free sees paywall
7. Build `/community` top-level — recent activity across all rooms

**Not this session:** Moderation tools, reporting, DMs.

**Test before done:**
- Tier 2 user creates post in a room
- Tier 1 user sees posts but cannot reply
- Free user sees paywall
- Realtime: new post appears without refresh

---

### Session M — Data Export + Deletion

**Goal:** Full GDPR-style data control. Per `seeds/data-ethics-architecture.md`.

**Agent:** Web (autonomous)
**Depends on:** Sessions D, F, G, H (all user data tables exist)
**Parallelizable with:** Session L

**Build this session:**
1. Build `GET /api/user/export` — JSON download of all user data
2. Build `DELETE /api/user/delete` — cascade deletion + Stripe cancel
3. Add "Export my data" and "Delete my account" to `/me/settings`
4. Deletion requires typing "DELETE MY ACCOUNT" for confirmation
5. Deletion cancels Stripe subscription before database deletion
6. Add privacy information section explaining data model

**Not this session:** Legal privacy policy (requires lawyer).

**Test before done:**
- Export downloads valid JSON with all user data
- Deletion removes all rows, cancels Stripe
- Deleted user cannot log back in
- Confirmation prevents accidental deletion

---

### WAVE 4 Quality Gate

Before proceeding to Wave 5:
- [ ] Voice parser routes correctly for top 20 common queries
- [ ] Pinch-zoom canvas works on mobile and desktop
- [ ] Community posts visible for Tier 2 users
- [ ] Data export downloads valid JSON
- [ ] Account deletion works end-to-end

---

## WAVE 5 — Launch (Session N)

---

### Session N — Production Deployment

**Goal:** The app is live at its production domain.

**Agent:** Desktop (Jake at PC for final verification)
**Depends on:** ALL previous sessions

**Build this session:**
1. Configure Vercel project, connect GitHub repo, set all env vars
2. Configure Supabase production project (separate from dev)
3. Run all migrations (001-016) in production
4. Set Stripe to live mode, register webhook with production URL
5. Configure custom domain + SSL
6. Set up Vercel Cron for daily Operis generation
7. Verify ISR revalidation works for card pages
8. Smoke test ALL critical flows in production:
   - Signup → onboarding → first room → log a set → save room
   - Subscribe (Tier 1) → access gated content → manage subscription
   - Community post (Tier 2)
   - Data export + deletion
   - Voice parser
   - Operis loads on homepage

**Test before done:**
- Production URL resolves and loads
- Signup → Stripe → Tier 1 works end-to-end
- Operis generates daily
- No console errors on critical paths
- Mobile viewport works

---

## POST-LAUNCH — Automotive Layer (Sessions V-Z)

Sessions V through Z remain unchanged from V1. They cover:
- **V:** TTS Pipeline + Wilson Voice
- **W:** Playlist Layer (Spotify/Apple Music mood mapping)
- **X:** Android Auto integration
- **Y:** Apple CarPlay integration
- **Z:** Free Tier Audio Funnel

See `seeds/claude-code-build-sequence.md` (V1) for full specs. These sessions depend on the full launch stack.

---

## Agent Routing Matrix

| Session | Wave | Agent | Jake? | Parallel With | Produces |
|---------|------|-------|-------|---------------|----------|
| 0 | 0 | Desktop | YES (one-time) | — | Env vars, Supabase tables, Stripe products |
| A' | 0 | Web | No | A-1 | D-module integrated skeleton |
| A-1 | 0 | Web/Codex | No | A' | City compiler + 1,680 compiled JSONs |
| B | 1 | Web | No | C, J, Q-1 | Card rendering pipeline |
| C | 1 | Web | No | B, J, Q-1 | 4-dial navigation |
| J | 1 | Web | No | B, C, Q-1 | Floor system + exercise library |
| Q-1 | 1 | Codex | No | B, C, J | Type misroute fixes |
| Q-2 | 1 | Codex | No | Wave 2 (after Q-1) | Content depth fixes |
| D | 2 | Web | No | I-data, I-full | Auth + database |
| F | 2 | Web | No | I-data (after D) | Stripe payments |
| I-data | 2 | Codex | No | D, F | Historical events + cosmograms |
| I-full | 2 | Web | No | F (after D, I-data) | Full Operis pipeline |
| E | 3 | Web | No | G, H | Onboarding flow |
| G | 3 | Web | No | E, H | Workout logging |
| H | 3 | Web | No | E, G | Saved rooms |
| C-2 | 4 | Web | No | K | Voice parser |
| K | 4 | Web | No | C-2 | Pinch-zoom canvas |
| L | 4 | Desktop | YES (moderation) | M | Community floor |
| M | 4 | Web | No | L | Data export + deletion |
| N | 5 | Desktop | YES (deploy) | — | Production launch |

**Summary:** 20 sessions total. 17 autonomous (Web/Codex). 3 require Jake (0, L, N). Session 0 is a 30-minute one-time setup.

---

## Critical Path

```
Session 0 (Jake, 30 min)
    │
    ├── A' (Web)  ──┐
    │               ├── WAVE 0 GATE
    └── A-1 (Codex) ┘
            │
    ┌───────┼────────┬──────────┐
    B (Web) C (Web)  J (Web)    Q-1 (Codex)
    └───────┼────────┘          │
            │                   Q-2 (Codex) ──→
    WAVE 1 GATE
            │
    ┌───────┼──────────────┐
    D (Web) I-data (Codex) │
    │       │              │
    F (Web) I-full (Web)   │
    └───────┼──────────────┘
    WAVE 2 GATE
            │
    ┌───────┼───────┐
    E (Web) G (Web) H (Web)
    └───────┼───────┘
    WAVE 3 GATE
            │
    ┌───────┼──────────┐
    C-2     K    L (Jake)  M
    └───────┼──────────┘
    WAVE 4 GATE
            │
          N (Jake)
```

**Minimum sequential steps:** 0 → A'/A-1 → B/C/J → D → F → G/H/E → C-2/K → L → N = **8 sequential gates**

**Calendar estimate (if sessions run ~3hr each):**
- Wave 0: 1 day (A' and A-1 in parallel)
- Wave 1: 1-2 days (B, C, J in parallel; Q-1/Q-2 on Codex)
- Wave 2: 2-3 days (D then F sequential; I-data on Codex; I-full after D+I-data)
- Wave 3: 1-2 days (E, G, H all parallel)
- Wave 4: 1-2 days (C-2, K parallel; L needs Jake)
- Wave 5: 1 day (N deploy)
- **Total: ~7-12 days of active sessions**

---

## AFK Execution Strategy

**Mobile (phone):** Review plans, approve quality gates, make architecture decisions, review Operis prototypes.

**Claude Code Web (AFK):** Sessions A', B, C, J, D, F, I-full, E, G, H, C-2, K, M — run while Jake trains clients. Queue before leaving. **13 of 20 sessions** can run without Jake present.

**Codex (background):** Sessions A-1 (city compiler batch), Q-1 (type misroutes), Q-2 (content depth), I-data (historical events + cosmograms). Always running in background. **4 batch sessions.**

**Claude Code Desktop (at PC):** Session 0 (setup, 30 min), Session L (community moderation decisions), Session N (production deploy). **3 sessions.**

---

## Dependency Map (V2)

| Session | Depends On |
|---------|-----------|
| 0 | None |
| A' | None |
| A-1 | None |
| B | A', A-1 |
| C | A' |
| J | A', A-1 |
| Q-1 | None |
| Q-2 | Q-1 |
| D | 0 |
| F | 0, D |
| I-data | None |
| I-full | D, I-data |
| E | D |
| G | B, D, F |
| H | B, D, F |
| C-2 | C |
| K | B, C |
| L | D, F |
| M | D, F, G, H |
| N | ALL |

---

## Handoff Contracts

Each session produces artifacts that downstream sessions consume. These are the handoff contracts:

| From | To | Artifact | Format |
|------|----|----------|--------|
| 0 | D, F | `web/.env.local` | Env file with 8 keys |
| A' | B, J | D-module integrated RoomShell | React component with proportions |
| A-1 | B, J, I-full | `middle-math/compiled/zips/*.json` | 1,680 JSON files |
| A-1 | App (all) | `web/src/lib/city-compiler.ts` | TypeScript module |
| D | F, E, G, H, L, M | Supabase auth + profiles table | Auth helpers + middleware |
| F | G, H, L, M | Stripe integration + PaywallGate | Component + API routes |
| I-data | I-full | Historical events + enriched cosmograms | Flat files in repo |
| I-full | N | Operis generation pipeline | API route + cron |
| B | G, H, K | Card rendering components | WorkoutCard + BlockSection |
| C | C-2, K | Dial navigation | DialPanel component |

---

🧮
