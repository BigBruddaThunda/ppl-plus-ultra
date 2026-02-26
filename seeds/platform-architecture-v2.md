---
planted: 2026-02-25
status: SEED
phase-relevance: Phase 4/5/6/7
blocks: nothing in Phase 2-3
depends-on: seeds/operis-architecture.md, seeds/elevator-architecture.md, seeds/default-rotation-engine.md
connects-to: seeds/axis-as-app-floors.md, seeds/zip-dial-navigation.md, seeds/almanac-room-bloom.md, seeds/junction-community.md
supersedes: seeds/platform-architecture-v1-archive.md (February 11, 2026)
---

# 🧮 PPL± Platform Architecture — V2

The Complete System Specification

Written: February 25, 2026
Author: Jake Berry
Status: SEED — planted, not active
Register: 🔵🟢 — structured + steady

---

## 📍 pono — POSITIONING THE PLATFORM

### What PPL± Is

PPL± is a 4-dial elevator serving 1,680 rooms across a 7-building campus, with the Operis on the piano nobile, six floors of progressive depth per room, and an automation pipeline that runs the press.

The four dials — Order (building), Axis (floor), Type (wing), Color (room) — produce a zip code. The zip code is the product. Each zip code addresses a room containing a workout, a community thread, a personal history layer, an almanac entry, and a deep-context cosmogram. The room exists at an address. The user visits the address. The system tracks the visit. Over time, the room and the user grow richer together.

### The Problem It Solves

For users: workout programming is overwhelming and inconsistent. Generic fitness apps account for neither season nor climate nor life phase. Progress tracking fragments across apps, notes, and memory. Community and accountability are absent from solo training. Quality coaching remains expensive and geographically limited.

For Jake: one-on-one training does not scale beyond hourly availability. Remote clients need structured delivery beyond text messages. Creating custom programs for each client is time-intensive. Knowledge and methodology sit uncodified in 15,000+ hours of training logs. Revenue caps at physical training hours.

### The Solution

The zip code IS the product. Each of the 1,680 addresses contains a workout that honors all four dials — the Order's load ceiling, the Axis's exercise character, the Type's muscle groups, the Color's equipment and temperament. Users live at addresses. They visit rooms. They build history. The system remembers.

The Operis delivers users to rooms each morning without requiring them to understand the addressing system. Tap a zip code on the front page. You're inside. The 61 emojis teach themselves through repeated exposure — the same way a gazette's standing departments teach themselves through daily reading.

Programs are guided tours through the zip web — sequences of addresses, with the rooms already furnished. The program is the itinerary. The rooms are the destination. The card collection (🧮 SAVE) is the user's personal library of favorite rooms.

---

## 🧲 capio — THE BUILDING MODEL

### The 4-Dial Elevator

See seeds/elevator-architecture.md for the complete specification. Summary:

Dial 1 — ORDER: Which building (7). The load ceiling, the season, the developmental phase.
Dial 2 — AXIS: Which floor (6). The exercise character AND the experience depth layer.
Dial 3 — TYPE: Which wing (5). The muscle groups, the movement domain.
Dial 4 — COLOR: Which room (8). The equipment tier, the session format, the temperament.

7 × 6 × 5 × 8 = 1,680 rooms. One elevator. Four dials.

### The Floor Stack

🔨 Utilitas — Ground floor. Tools, settings, navigation, zip directory, calculators, account.
🏛 Firmitas — Piano nobile. The Operis, the workout, the arrival experience.
⌛ Temporitas — 2nd floor. Calendar, season, training history at this address.
🐬 Sociatas — 3rd floor. Community threads, shared training, who else is here.
🌹 Venustas — 4th floor. Personal history, progress, trophies, private notes.
🪐 Gravitas — 5th floor (penthouse). Cosmogram content, deep questions, stakes.

On a phone, scrolling down moves you up through the building. Progressive disclosure IS the architecture.

### The Operis as Front Page

See seeds/operis-architecture.md for the complete specification. Summary:

The Operis lives on the 🏛 piano nobile. It is the platform's landing surface — what users see when they open PPL±. It weaves date-specific history, seasonal context, astronomical data, and 8–12 curated zip codes into a front-page experience. Tapping a zip code in the Operis takes the user into that room.

The Operis solves the cold-start problem (no learning curve), powers the circulation system (rotates which rooms get traffic), and is automatable (four of five input layers are deterministic or static).

### Navigation: Horizontal and Vertical

Horizontal movement: room to room. Via Operis portals, Junction suggestions, zip dial, search. The zip web.
Vertical movement: floor to floor within a room. Via scrolling, floor selector. The floor stack.

Both axes are always available. Scroll deeper into this room, or navigate to a different room. The architecture supports both.

---

## 🧸 fero — THE BUSINESS MODEL

### Tier 1: The Library Card — $10/month

Target audience: general fitness users, remote clients, anyone who wants a structured daily training experience with community access.

What they receive:

PPL± Operis — every edition, every day. The full front-page experience with curated zip codes, historical context, seasonal framing, and the Wilson Note.

All 1,680 rooms — every workout at every address. Browse by dial, by deck, by Operis portal. The full library is open.

🧮 SAVE collection — build a personal library of favorite rooms. Tag them, name them, annotate them.

🎲 Random generator — draw from saved rooms. Filter by Type, by Order, by Color. The shuffle-and-draw mechanic from the card-deck metaphor.

Community access — 🐬 floor threads per zip code. Read and post. Public discussion at every address.

Basic tools — 🔨 floor: calculators (1RM, macros, volume, plates), timers (rest, EMOM, AMRAP, stopwatch), settings, profile.

Basic progress — 🌹 floor: workout logging (weights, reps, notes), trophy room (streaks, milestones), photo journal (private by default).

Calendar view — ⌛ floor: training history, seasonal position, current Order display.

Content library — 🪐 floor: Jake's long-form essays, exercise demonstrations, seasonal guides (read access).

### Tier 2: The Residency — $25–30/month

Target audience: dedicated clients who want personalized programming, direct coaching access, and guided navigation through the building.

Everything from Tier 1, plus:

Personalized programming — guided paths through the zip web. Jake reviews logs and assigns curated room sequences (programs as itineraries, with the rooms already furnished). Programs are sequences of zip code addresses with weekly structure.

Direct coaching — Jake via DM. Asynchronous (like mail, not real-time chat). Priority response within 24–48 hours. Attachment support for form videos and progress photos.

Priority on the 🌹 floor — Jake reviews progress photos and metrics. Personal feedback on what the data shows. Goal-setting with coaching input.

Custom room sequences — programs tailored to the user's goals, history, and preferences. Jake assigns; the system delivers. As automation matures, the system suggests and Jake approves.

Personalized Order progression — Jake determines when a user shifts between seasonal phases, based on their logged history and readiness signals.

### Revenue Projections

Phase 1 (Months 1–3): Early adopters.
Tier 1: 50 users × $10 = $500/month. Tier 2: 10 users × $25 = $250/month. Total: $750/month ($9,000/year).
Jake's time: ~7 hours/week (daily edition review + Tier 2 client management + forum engagement).

Phase 2 (Months 4–9): Growth.
Tier 1: 200 users × $10 = $2,000/month. Tier 2: 30 users × $25 = $750/month. Total: $2,750/month ($33,000/year).
Jake's time: ~17 hours/week (Tier 2 management becomes the time driver at 30 min/client/week).

Phase 3 (Year 2): Scale with automation.
Tier 1: 500 users × $10 = $5,000/month. Tier 2: 50 users × $25 = $1,250/month. Total: $6,250/month ($75,000/year).
Jake's time: ~14 hours/week (automation reduces per-client time despite 4× user growth).

### Platform Costs

Year 1: Hosting (Vercel) $0/month free tier. Database (Supabase) $0/month free tier. Domain $1/month. Email (Supabase basic) $0. Payment processing (Stripe) 2.9% + $0.30/transaction. Total fixed: $1/month.

At scale (200+ users): Hosting (Vercel Pro) $20/month. Database (Supabase Pro) $25/month. Email (SendGrid) $15/month. Total fixed: $60/month. Stripe fees: ~3% of revenue.

Break-even: 7 Tier 1 users covers Year 1 costs. 12 mixed-tier users covers at-scale costs.

---

## 👀 specio — THE USER EXPERIENCE

### The Card/Deck Metaphor — Now Mapped to Rooms

The metaphor carries forward from the Feb 11 architecture, now grounded in spatial language:

Workouts are what's on the wall in each room. The room exists at an address. The workout content fills it. The master `.md` file is the architectural drawing. The user experience is the room itself.

Programs are guided tours — curated sequences of room addresses. The program contains addresses and scheduling (which room on which day of which week). The rooms already exist. The program is the itinerary.

🧮 SAVE bookmarks a room for the user's personal collection. The user builds a personal library of favorite addresses. The collection grows with use. Room Bloom (seeds/almanac-room-bloom.md) means repeated visits enrich the experience.

🎲 Random generator draws from the user's saved collection. Filter by Type, Order, Color. Exclude rooms visited in the last N days. The shuffle-and-draw mechanic.

### The 🧮 SAVE Workflow

After completing a workout, the logging screen appears:

The user rates the session (1–5 stars), adds optional notes, and checks the 🧮 SAVE box if they want to keep this room in their collection. If saved, they can add a custom name, tags, and a note about why they're saving it. The saved room appears in their 🌹 Venustas floor collection, available for the random generator and for repeat visits.

### Programs as Zip Code Sequences

Jake creates a program as a sequence of zip code addresses with weekly structure:

Week 1: Day 1 → ⛽🏛🛒🔵, Day 2 → ⛽🏛🪡🔵, Day 3 → ⛽🏛🍗🔵, Day 4 → ⛽🔨➕🟢, Day 5 → ⛽🏛➖⚪.

The rooms already contain the workouts. The program is the route through the building. When Jake assigns a program, the user's dashboard shows today's room address and a progress bar through the sequence.

Completed programs archive to the user's history. The user can restart a completed program with a new name — same rooms, new timeline, comparable logs. The personal almanac of past performance.

### The Logging Interface — Progressive Disclosure

The workout displays in full-screen, read-only mode. The user taps "Do This Workout" and input fields appear inline — exercise by exercise, set by set. Logging happens one exercise at a time, reducing cognitive load. Each set shows the Order emoji and the prescribed parameters. The user enters their actual weight and reps.

After completing all exercises, the summary screen shows the session rating, notes field, and 🧮 SAVE option. The log writes to the user's history. The room remembers the visit.

### Onboarding Sequence

Day 1: land on the Operis. Read the front page. Tap a zip code. Do the workout. The system taught itself.
Day 5: discover floors. Scroll past the workout. See the time context (⌛), the community (🐬). Realize the room has depth.
Day 15: follow Junctions. The 🚂 at the end of a workout suggests three next rooms. Tap one. Start navigating the zip web horizontally.
Day 30: use the dial. Spin the elevator dials directly. Override the Operis's defaults. Navigate the building independently.

The onboarding curve: newspaper reader → room visitor → building explorer → self-directed navigator. No tutorial required. The architecture teaches through use.

---

## 🤌 facio — THE TECHNICAL ARCHITECTURE

### Tech Stack

Frontend: Next.js 14 (React framework), TypeScript, Tailwind CSS.
Backend: Supabase (PostgreSQL + auth + storage + realtime), Next.js API routes (serverless functions).
Hosting: Vercel (automatic deployments from GitHub), Supabase Cloud.
Payment: Stripe (subscription management).
Communication: Supabase Realtime (forum, threads), SendGrid (transactional email, future).

### Database Schema — Zip-Code-Centric

The Feb 11 schema stored workouts with emoji metadata columns. The V2 schema recognizes the zip code as the primary addressing key. The room exists at an address. The workout content fills the room.

**Core tables:**

`profiles` — extends Supabase auth.users. Fields: id (UUID, PK), full_name, bodyweight, unit_system (kg/lbs), subscription_tier (1 or 2), created_at.

`workouts` — the rooms. Fields: id (UUID, PK), zip_code (TEXT, unique — the 4-emoji address, e.g. "⛽🏛🪡🔵"), title, markdown_content, order_emoji, axis_emoji, type_emoji, color_emoji, operator_emoji, deck_number (INTEGER), created_by (UUID, FK → auth.users), is_daily (BOOLEAN), published_date (DATE), estimated_duration (INTEGER, minutes), status (TEXT — EMPTY/GENERATED/CANONICAL), created_at. The zip_code column is the primary identity. All queries route through it.

`daily_editions` — the newspaper archive. Fields: id (UUID, PK), edition_date (DATE, unique), markdown_content (TEXT — the full rendered Daily), default_zip (TEXT — the rotation engine's derived zip for this date), featured_zips (TEXT[] — the 8–12 zips in the 🏖 Sandbox), operator_emoji, order_emoji, season_label, created_at.

`zip_visits` — room residency tracking. Fields: id (UUID, PK), user_id (UUID, FK → auth.users), zip_code (TEXT), visit_date (DATE), time_spent (INTEGER, minutes), workout_log_id (UUID, FK → workout_logs, nullable). Powers the Room Bloom concept — rooms get richer with repeated visits.

`room_threads` — per-zip-code community discussions. Fields: id (UUID, PK), zip_code (TEXT), user_id (UUID, FK → auth.users), content (TEXT), attachments (TEXT[]), created_at. The 🐬 floor of each room.

`programs` — guided tours. Fields: id (UUID, PK), title, description, duration_weeks (INTEGER), phase_emoji (TEXT — primary Order), created_by (UUID, FK → auth.users), is_template (BOOLEAN), created_at.

`program_sequence` — the itinerary. Fields: id (UUID, PK), program_id (UUID, FK → programs), zip_code (TEXT — the room address), week_number (INTEGER), day_number (INTEGER), sequence_order (INTEGER). Programs are sequences of zip codes. The rooms already contain the workouts.

`user_programs` — assigned tours. Fields: id (UUID, PK), user_id (UUID, FK → auth.users), program_id (UUID, FK → programs), assigned_date, start_date, status (active/completed/paused), current_week, current_day, nickname, rating, review, completed_at.

`workout_logs` — training history. Fields: id (UUID, PK), user_id (UUID, FK → auth.users), zip_code (TEXT), workout_id (UUID, FK → workouts, nullable), user_program_id (UUID, FK → user_programs, nullable), completed_date, exercises_logged (JSONB), overall_rating (INTEGER 1–10), notes, saved (BOOLEAN — 🧮 flag), created_at.

`saved_workouts` — personal collection. Fields: id (UUID, PK), user_id (UUID, FK → auth.users), zip_code (TEXT), workout_id (UUID, FK → workouts), saved_date, custom_name, tags (TEXT[]), notes. Unique constraint on (user_id, zip_code).

`forum_posts` — community discussion. Fields: id (UUID, PK), user_id (UUID, FK → auth.users), channel (TEXT), title, content, attachments (TEXT[]), created_at.

`forum_comments` — replies. Fields: id (UUID, PK), post_id (UUID, FK → forum_posts), user_id, content, created_at.

`direct_messages` — Tier 2 coaching channel. Fields: id (UUID, PK), sender_id, recipient_id, subject, content, attachments (TEXT[]), read (BOOLEAN), created_at.

`user_achievements` — trophy room. Fields: id (UUID, PK), user_id (UUID, FK → auth.users), achievement_type (TEXT), achieved_date, metadata (JSONB).

`progress_photos` — 🌹 floor visual tracking. Fields: id (UUID, PK), user_id (UUID, FK → auth.users), photo_url (TEXT — Supabase Storage), photo_type (front/side/back), date_taken, notes, is_public (BOOLEAN, default false).

**Key schema differences from Feb 11:**

The `workouts` table uses `zip_code` as the primary identity column, not just emoji metadata. Queries route through the zip code address.

The `program_sequence` table (replacing `program_workouts`) stores zip codes instead of workout IDs. Programs are address sequences. The rooms contain the content.

The `daily_editions` table is new — archives every Operis edition with its featured zip codes, enabling browsable history.

The `zip_visits` table is new — tracks which rooms users have visited, powering the residency concept and Room Bloom.

The `room_threads` table is new — per-zip-code community threads on the 🐬 floor.

### API Structure

Authentication via Supabase Auth (email/password signup, session management).

Core query patterns:

Fetch today's Operis edition: query `daily_editions` by date. If no pre-generated edition exists, the rotation engine derives the default zip and the system generates on the fly.

Fetch a room: query `workouts` by `zip_code`. Single room at a known address.

Fetch user's program: query `user_programs` joined to `program_sequence` joined to `workouts` (via zip_code), filtered by user_id and status='active'.

Log a workout: insert into `workout_logs` with zip_code, exercises_logged JSONB, rating, notes, saved flag. If saved=true, also insert into `saved_workouts`.

Random generator: query `saved_workouts` for user_id, apply Type/Order/Color filters, exclude recently-visited zips (via `zip_visits`), random selection from remaining pool.

Room thread: query `room_threads` by zip_code, ordered by created_at. The 🐬 floor of any room.

### Mobile-First Design Constraints

Portrait mode. Width: 375–430px. Single column. Bottom navigation for floor selection (6 floors). Minimize chrome, maximize content. Progressive disclosure as the primary UX pattern — collapse sections by default, expand on interaction.

Screenshot mode hides UI chrome for clean workout export. The workout card in screenshot mode looks like the `.md` file rendered to print — the gazette's single-column broadsheet on a phone screen.

Typography: 14px base, 18–24px headers, 1.2em emojis (larger than text, visually distinct), monospace for workout tree notation (preserves ├─ connectors).

The exercise logging interface appears inline on "Do This Workout" — set-by-set, exercise-by-exercise. Progressive disclosure applied to data entry.

---

## 🚀 mitto — THE AUTOMATION PATHWAY

### Reframing: Deterministic Pipeline + Constrained AI Generation

The Feb 11 architecture envisioned "RAG trained on Jake's logs" as the automation mechanism. The V2 architecture reframes this as a deterministic pipeline with constrained AI generation at specific stages.

**What is deterministic (runs without AI):**

The rotation engine. Order by weekday (7-day cycle). Type by rolling 5-day calendar from Jan 1. Axis by monthly operator. The math produces a daily default zip code with zero judgment required. See seeds/default-rotation-engine.md.

The exercise library. A finite validated pool of ~2,185 exercises, each mapped to SCL Types, Orders, Axes, Equipment Tiers, and GOLD gate status. The library is the constraint set. Generation selects from this pool — it does not invent.

The SCL rules. Codified in CLAUDE.md and scl-directory.md. Order ceilings, Color equipment filters, Axis biases, block sequence guidelines, the GOLD gate, the validation checklist. These rules are the generation contract.

The card generation pipeline. Scripts (validate-card.py, audit-exercise-coverage.py), skills (/generate-card, /build-deck-identity), subagents (card-generator, deck-auditor), and hooks (PostToolUse auto-validation). The infrastructure that ensures generated content honors every constraint.

**What requires AI generation (constrained):**

Card content — the workout itself. Exercise selection within the validated library, set/rep/load prescription within Order ceilings, cue writing within tonal rules, block sequencing within Order guidelines. The AI generates; the pipeline validates; Jake approves.

Operis edition assembly — weaving historical events, seasonal context, and featured zips into the front-page format. The inputs are pre-built (historical DB, cosmograms, calendar data). The assembly requires editorial judgment — which events to feature, which zips to highlight, how to frame the Wilson Note.

Program design — selecting which zip code sequence serves a user's goals. Requires coaching judgment. AI can suggest; Jake approves or modifies.

**What requires human input (irreducible):**

Cosmogram research — the deep cultural/historical/architectural context per deck. AI-assisted but human-directed.

Exercise library expansion — adding new exercises requires coaching expertise and SCL mapping.

Publication standard evolution — the voice of the institution. Jake's editorial authority.

Tier 2 coaching — personal feedback, goal adjustment, DM responses. AI can draft; Jake delivers.

### Jake's Role Shift

Phase 1–2 (manual): Jake writes daily content, manages Tier 2 clients, moderates forum. ~7–17 hours/week.

Phase 3 (assisted): AI generates Operis editions and program suggestions. Jake reviews and approves. Tier 2 management time drops as AI drafts client communications. ~14 hours/week at 500 users.

Phase 4 (automated): The system runs the press. The Operis publishes from its five input layers. Cards generate from the pipeline. Programs suggest from logged user history. Jake reviews architecture, approves new content types, writes occasional Wilson Notes, and handles escalated Tier 2 coaching. ~5 hours/week at 500 users.

The shift: from "approve AI-generated workouts" to "approve the architecture that generates them."

### Phase Timeline

Phase 1 (Months 1–3): Manual operation. Jake writes Operis editions, assigns programs, moderates forum. 50 Tier 1 + 10 Tier 2 users.

Phase 2 (Months 4–9): AI assists. Operis editions generated from populated input layers, Jake reviews before publishing. Program suggestions from logged patterns. Forum Q&A drafted by AI, moderated by Jake. 200 Tier 1 + 30 Tier 2 users.

Phase 3 (Year 2): Semi-automated. Operis editions auto-publish with Jake's weekly review. Programs auto-suggest with Jake's approval. Smart exercise substitutions for equipment constraints. 500 Tier 1 + 50 Tier 2 users.

Phase 4 (Year 2+): Full automation with oversight. The system publishes daily, generates programs, moderates community, and tracks progress. Jake reviews architecture weekly, handles Tier 2 escalations, writes long-form content. 500+ users with stable time commitment.

---

## 🪵 teneo — NON-NEGOTIABLES

### Preserved from Feb 11

User safety: emergency protocol visible, conservative recommendations, form checks flagged for human review, "stop if pain/dizziness" messaging. The system biases toward safety.

Legal compliance: Terms of Service on signup with liability waiver. Clear disclaimers (informational use, not medical advice). Jake's PT insurance covers platform usage. No medical claims, diagnosis, or treatment language.

Content quality: No auto-publishing without review in Phases 1–3. Even Phase 4 automated publishing requires validation pipeline passage. Forum moderation active. Exercise demonstrations verified for safety.

Financial integrity: transparent pricing, easy cancellation (Stripe handles), pro-rated refund policy, lifetime access to paid content.

Data ownership: users own their logs, photos, notes. Export functionality planned. Privacy controls on all shared content. No selling user data.

### Added for V2

Publication standard compliance: no motivational filler, no wellness-influencer voice, no TikTok vocabulary, no performing enthusiasm the content does not feel. Civic posture: the library is open, the shelves are addressed, the door does not close. See scl-deep/publication-standard.md.

Zip code integrity: every room at every address honors all four dials. The Order ceiling holds. The Color equipment filter holds. The Axis bias shapes exercise selection. The Type muscle groups are accurate. A room that violates its address is architecturally unsound. The validation pipeline (scripts/validate-card.py) enforces this at generation time.

The reader informs the opinion: PPL± content presents information. The reader evaluates. The publication does not tell the reader what to think — it gives them what they need to think well. Independent of party or faction. Committed to useful knowledge, honest reporting, and the cultivation of an informed public.

---

## 🚂 JUNCTION — WHAT THIS DOCUMENT UNBLOCKS

The HTML experience layer design (Phase 4/5) now has a spatial model to build from — the floor stack, the elevator, the piano nobile, the progressive-disclosure scroll architecture.

The Operis has a named place in the platform — the 🏛 piano nobile, with standing departments, a block convention, and an automation pathway.

The database schema can be prototyped — zip-code-centric tables, Operis editions archive, room visit tracking, per-zip-code community threads, programs as address sequences.

The automation pipeline has a clear dependency chain — rotation engine (math) → exercise library (pool) → SCL rules (constraints) → generation pipeline (tools) → Operis input layers (content) → publication standard (voice).

The Feb 11 "PPL± ITSELF" document is archived at seeds/platform-architecture-v1-archive.md. This document replaces it.

---

## 🧮 SAVE

Status: SEED — planted, not active.
Depends on: card generation progress (rooms need content), cosmogram population (rooms need substrate), Daily prototype refinement (front page needs testing).
Does not block: current card generation pipeline, deck identity work, cosmogram research sessions.

Published from PPL± Platform Architecture V2.
25 February 2026. Late ⛽ Doric. 🧲 capio.
