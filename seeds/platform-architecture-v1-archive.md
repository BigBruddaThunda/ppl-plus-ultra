---
status: ARCHIVED
superseded_by: seeds/platform-architecture-v2.md
original_date: 2026-02-11
archived_date: 2026-02-25
archive_reason: >
  Architecture evolved significantly between Feb 11–25. Zip code system matured from
  formatting convention to full addressing architecture. 6-Axis navigation evolved from
  tab bar to spatial floor model (piano nobile). Daily system emerged as front page and
  onboarding layer. Elevator model resolved (4 dials = building/floor/wing/room). Business
  logic, database schema thinking, UX flows, and tech stack decisions preserved in V2
  (seeds/platform-architecture-v2.md). This document retained for historical reference.
---

# 🧮 PPL± ITSELF — Platform Architecture (February 11, 2026)

> **ARCHIVED DOCUMENT**
> Superseded by `seeds/platform-architecture-v2.md` (February 25, 2026).
> Retained for historical reference only. Do not use for active planning.

---

═══════════════════════════════════════════════════════════════════════════════
🧮 PPL± ITSELF
The Complete Platform Architecture — Context Document
═══════════════════════════════════════════════════════════════════════════════
**Document Type:** System Architecture & Context Capture
**Status:** 🟡 Draft / Living Document
**Created:** February 11, 2026
**Author:** Jake Berry
**Purpose:** Complete specification of PPL± as a digital training platform
═══════════════════════════════════════════════════════════════════════════════

# 🎯 INTENTION

"PPL± is a mobile-first training platform that delivers Jake's seasonal athletic development system to clients through structured programs, daily workouts, and intelligent automation—while preserving the human craft of coaching."

═══════════════════════════════════════════════════════════════════════════════
# 🐂 FOUNDATION — What PPL± Is
═══════════════════════════════════════════════════════════════════════════════

## The Core Concept

PPL± is a digital training platform built around three interconnected systems:

1. **The Training System** — PPL± methodology (Push/Pull/Legs/Plus), Seven Orders (seasonal training phases), Eight Colors (equipment/structure approaches)
2. **The Delivery Platform** — Mobile-first web application that delivers workouts, tracks progress, manages programs, and builds community
3. **The Business Model** — Tiered subscription service that scales from mass-market daily workouts to personalized training programs

## The Problem It Solves

**For Clients:**
- Workout programming is overwhelming and inconsistent
- Generic fitness apps don't account for seasons, climate, or life phases
- Progress tracking is fragmented across apps, notes, and memory
- Community and accountability are missing from solo training
- Quality coaching is expensive and geographically limited

**For Jake:**
- One-on-one training doesn't scale beyond hourly availability
- Remote clients need structured delivery beyond text messages
- Creating custom programs for each client is time-intensive
- Knowledge and methodology aren't systematized for reuse
- Revenue is capped by physical training hours

## The Solution Architecture

PPL± solves both sides through:

**Structured Delivery:**
- Workouts formatted in PPL± Semantic Compression Language (SCL)
- Mobile-optimized for portrait mode (screenshot-friendly)
- Clear visual hierarchy using emojis as semantic anchors
- Programs structured as "card decks" (collections of workouts)

**Intelligent Scaling:**
- Daily workouts for mass market (Tier 1: $10/month)
- Personal programs for dedicated clients (Tier 2: $25/month)
- Automation pathway using RAG to reduce Jake's manual work
- Community layer for support and accountability

**Data Ownership:**
- Users build personal workout libraries via 🧮 SAVE tagging
- Programs stored as "chapters" they can return to
- Training history becomes a personal almanac
- Random workout generator pulls from their saved collection

═══════════════════════════════════════════════════════════════════════════════
# 🏛 ARCHITECTURE — The 6-Axis Navigation System
═══════════════════════════════════════════════════════════════════════════════

PPL± uses the six axes from SCL as the primary navigation structure. Each axis is a top-level section containing related features and functions.

## Visual Structure

```
Top Navigation (Mobile: Bottom Tab Bar)
├─ 🏛 Firmitas (Home/Foundation)
├─ 🔨 Utilitas (Tools/Settings)
├─ 🌹 Venustas (Progress/Vanity)
├─ 🪐 Gravitas (Content/Challenges)
├─ ⌛ Temporitas (Calendar/Time)
└─ 🐬 Sociatas (Community/Social)
```

Each axis asks a fundamental question and contains features that answer it.

---

## 🏛 FIRMITAS — What IS It? (Structure)

**Core Question:** "What is my training right now?"
**Primary Function:** Home dashboard, workout delivery, logging

### Children (Sub-Features):

**Dashboard (Landing Page)**
```
User lands here on login:
┌─────────────────────────────────────┐
│ Welcome back, Sarah                 │
│                                     │
│ 📖 CURRENT PROGRAM                  │
│ 🦋 Summer Cut 2025                  │
│ Week 3 of 8 • Day 2                 │
│                                     │
│ [View Today's Workout] →            │
│                                     │
│ Progress: ████████░░░░░░ 38%        │
│                                     │
│ Quick Stats:                        │
│ • 23-day streak 🔥                  │
│ • Last workout: 2 hours ago         │
│ • Next workout: Tomorrow 6:00 AM    │
└─────────────────────────────────────┘
QUICK ACTIONS
┌─────────────────────────────────────┐
│ 🎲 Random Workout (from saved)      │
│ 📚 My Programs (4 active)           │
│ 🧮 Saved Workouts (27 cards)        │
└─────────────────────────────────────┘
```

**Workouts (Current Assigned/Daily)**
- Mobile-optimized markdown rendering
- Full-screen portrait mode (375-430px width)
- Screenshot mode (hides UI chrome for clean export)
- SCL formatting preserved (tree connectors, emojis, structure)
- Logging interface appears on-demand (progressive disclosure)

**Logbook (Training History)**
- Past workouts (calendar view or list view)
- Weight progression charts
- Volume metrics (sets × reps × weight over time)
- Filter by Type (🛒🪡🍗➕➖) or Order (🐂⛽🦋🏟🌾⚖🖼)
- Search by exercise name

**My Programs (Chapter View)**
- Active programs (currently training)
- Completed programs (past chapters)
- Paused programs (temporarily stopped)
- Each program shows: title, duration, progress %, rating
- Tap to view full program structure (week-by-week)
- Restart completed programs with new name

**🧮 Saved Workouts (Card Collection)**
- All workouts user has tagged with 🧮 SAVE
- User can rename, tag, add notes
- Filter by Type, Order, tags, date saved
- Random workout generator pulls from this collection
- "Do This Workout" launches it immediately

**Data Model (Firmitas):**
```javascript
// Workouts table
workouts {
  id, title, markdown_content,
  order_emoji, type_emoji,
  created_by, is_daily, created_at
}
// Programs table (card decks)
programs {
  id, title, description, duration_weeks,
  phase_emoji, created_by, is_template
}
// Program sequence
program_workouts {
  program_id, workout_id,
  week_number, day_number, sequence_order
}
// User's assigned programs
user_programs {
  id, user_id, program_id,
  assigned_date, start_date, status,
  current_week, current_day, nickname
}
// Workout logs
workout_logs {
  id, user_id, workout_id, completed_date,
  exercises_logged, overall_rating, notes, saved
}
// Saved workouts collection
saved_workouts {
  id, user_id, workout_id, saved_date,
  custom_name, tags, notes
}
```

---

## 🔨 UTILITAS — Does It WORK? (Function)

**Core Question:** "What tools do I need to train effectively?"
**Primary Function:** Utilities, calculators, settings, database access

### Children (Sub-Features):

**Workout Library**
- Browse all workouts (Jake's full library)
- Filter by Order (🐂⛽🦋🏟🌾⚖🖼)
- Filter by Type (🛒🪡🍗➕➖)
- Filter by Axis bias (🏛🔨🌹🪐⌛🐬)
- Filter by Color (equipment/structure)
- Search by exercise name or block type
- Preview workout before assigning
- Tier 1: View-only access
- Tier 2: Can request specific workouts

**Calculators**
- 1RM Calculator (one-rep max estimator)
- Macro Calculator (TDEE, protein/carb/fat targets)
- Volume Calculator (sets × reps × weight per session)
- Plate Calculator (what plates to load on barbell)
- Wilks Score Calculator (strength relative to bodyweight)

**Timers**
- Rest Timer (countdown between sets)
- EMOM Timer (every minute on the minute)
- AMRAP Timer (as many rounds as possible)
- Stopwatch (for timed holds, carries)
- Interval Timer (Tabata, HIIT protocols)

**Settings**
- **Profile**
  - Name, email, bodyweight
  - Training goals, experience level
  - Injury history, limitations
- **Preferences**
  - Unit system (kg/lbs, cm/inches)
  - Notification settings (workout reminders)
  - Rest timer auto-start
  - Theme (dark/light mode)
- **Subscription**
  - Current tier (Tier 1 or Tier 2)
  - Payment method
  - Billing history
  - Upgrade/downgrade options

**Exercise Database (Future Feature)**
- Video demonstrations of all exercises
- Progressions and regressions
- Common mistakes and corrections
- Equipment alternatives
- Muscle groups targeted
- Filter by equipment available

---

## 🌹 VENUSTAS — Does It FEEL Right? (Beauty/Progress)

**Core Question:** "How do I look and feel? Am I making progress?"
**Primary Function:** Visual progress tracking, achievements, vanity metrics

### Children (Sub-Features):

**Trophy Room (Achievements)**
```
Streak Badges:
├─ 🔥 7-day streak
├─ 🔥🔥 30-day streak
├─ 🔥🔥🔥 90-day streak
└─ 🔥🔥🔥🔥 365-day streak
PR Badges:
├─ 💪 First 100kg squat
├─ 🏋️ First 140kg deadlift
├─ 🦾 First bodyweight chin-up
└─ ⚡ First 60kg press
Consistency Trophies:
├─ 🏆 Completed 10 programs
├─ 🎖️ 100 workouts logged
├─ 🥇 Perfect week (7/7 days)
└─ 🌟 Training for 1 year
```

**Photo Journal (Progress Photos)**
- Upload front/side/back comparison photos
- Date-stamped and organized chronologically
- Slider view (compare any two dates)
- Private by default
- Optional sharing to 🐬 Community
- Tags for context (start of cut, end of bulk, etc.)
- Stored in Supabase Storage (1GB free tier)

**The Mirror (Vanity Metrics)**
- Bodyweight graph (over time)
- Body composition tracking (if user logs it)
- Measurements (chest, arms, waist, legs, etc.)
- Visual charts showing trends
- Goal setting (target weight, measurements)
- Progress toward goals (visual indicators)

**Social Feed (Optional Sharing)**
- Share PRs to community
- Celebrate milestones publicly
- Support/encouragement from others
- Like/comment on posts
- Privacy controls (share only what you want)

---

## 🪐 GRAVITAS — Does It MATTER? (Significance/Teaching)

**Core Question:** "Why does this training matter? What am I learning?"
**Primary Function:** Educational content, challenges, deep dives

### Children (Sub-Features):

**The Library (Jake's Long-Form Content)**
- Exercise tutorials (video + text)
- Training philosophy essays
- Seasonal training guides (how each Order works)
- "Why we train this way" explainers
- Anatomy and biomechanics primers
- Recovery and lifestyle content
- Nutrition frameworks (aligned with Orders)

**Challenges (Optional Participation)**
- 30-day squat challenge
- Weekly benchmarks (test maxes)
- Community competitions
- Leaderboards (opt-in, filterable by age/gender/weight)
- Badge rewards for completion

**Demos (Exercise Library)**
- Video demonstrations of every exercise in the system
- Common mistakes (what not to do)
- Progressions (easier variations)
- Regressions (harder variations)
- Cues that matter (Jake's coaching points)
- Equipment alternatives

**Brain Puzzles (Optional Engagement)**
- Training riddles ("What's the weak link in this squat?")
- Movement analysis challenges
- Biomechanics thought experiments
- Community discussions on technique

**Content Management:**
- Jake posts articles, videos, challenges
- Other trainers (if invited) can contribute
- Moderation layer (Jake approves all content)
- Version control (content can be updated)

---

## ⌛ TEMPORITAS — WHEN? How Long? (Time/Seasons)

**Core Question:** "Where am I in time? What phase am I in?"
**Primary Function:** Calendar, seasonal alignment, goal tracking

### Children (Sub-Features):

**Seasonal Calendar (8-Week Orders)**
```
Current Order: 🦋 IONIC (Build)
Week 3 of 8
Order Overview:
├─ Phase: Hypertrophy accumulation
├─ Climate: Late winter, moderate temps
├─ Focus: Volume, muscle growth, work capacity
├─ Nutrition: Slight surplus, high protein
└─ Next Order: 🏟 CORINTHIAN (Performance)
Historical Orders:
├─ 🐂 TUSCAN (Foundation) — Completed Jan 1-Feb 21
├─ ⛽ DORIC (Strength) — Completed Nov 1-Dec 24
└─ 🖼 PALLADIAN (Restoration) — Completed Sep 1-Oct 27
```

**Goal Tracker**
```
Active Goals:
┌─────────────────────────────────────┐
│ 🎯 Squat 150kg by June 1            │
│ Current: 135kg                      │
│ Progress: ███████████░░░ 90%        │
│ On track ✓                          │
└─────────────────────────────────────┘
┌─────────────────────────────────────┐
│ 🎯 10 strict chin-ups               │
│ Current: 7                          │
│ Progress: ███████░░░░░░░ 70%        │
│ Ahead of schedule ✓✓                │
└─────────────────────────────────────┘
```

**Training History (Calendar View)**
- Calendar overlay showing completed workouts
- Color-coded by Type (🛒🪡🍗➕➖)
- Volume metrics per week/month
- Deload weeks marked
- Injury/rest days noted
- Tap any day to see workout details

**Meal Planning (Future Feature)**
- Seasonal eating guides (aligned with Orders)
- Macro targets by training phase
- Recipe suggestions (local, seasonal foods)
- South Carolina seasonal produce calendar
- Climate-aware nutrition (hot summers, mild winters)

---

## 🐬 SOCIATAS — WHO Is Involved? (Community/Social)

**Core Question:** "Who's training with me? Who can I connect with?"
**Primary Function:** Community forum, communication, collaboration

### Children (Sub-Features):

**Community Forum (Discord-Style Channels)**
```
Channels:
├─ #daily-workout-discussion
│   └─ "Who's doing today's pull workout?"
│
├─ #form-checks
│   └─ "Can someone review my deadlift setup?" [video]
│
├─ #questions
│   └─ "How do I know if I'm ready for 🏟 Performance?"
│
├─ #wins
│   └─ "PR! 180kg deadlift × 3 🔥"
│
├─ #seasonal-chat
│   └─ "Week 3 of 🦋 Ionic hitting different"
│
├─ #general
│   └─ Open conversation, community building
│
└─ #announcements (Jake only)
    └─ New programs, features, updates
```

**Direct Messages (Tier 2 Only)**
- Message Jake directly
- Asynchronous (like email, not real-time chat)
- Attachment support (videos, photos of form)
- Priority response for Tier 2 clients
- Searchable message history
- Notification when Jake responds

**Live Workouts (Future Feature)**
- Scheduled group training sessions (virtual)
- Video chat integration (Zoom, Google Meet)
- Real-time form feedback from Jake
- Community accountability
- Recorded sessions available for replay

**Client Directory (Opt-In)**
- Find training partners near you
- Filter by location, goals, training level
- Connect for in-person training sessions
- Privacy controls (show only what you want)

**Moderation:**
- Jake is primary moderator
- Future: Trusted community members as mods
- Clear community guidelines
- Report/flag system for inappropriate content

---

═══════════════════════════════════════════════════════════════════════════════
# 🦋 BUSINESS MODEL — The Tiered System
═══════════════════════════════════════════════════════════════════════════════

## Tier 1: Daily Workout Access

**Price:** $10/month
**Target Audience:** General fitness enthusiasts, remote clients, budget-conscious users

### What They Get:

**Core Access:**
- Daily workout posted by Jake (seasonal, climate-aware)
- Access to past daily workouts (full archive)
- Basic logging (weights, reps, notes)
- Screenshot-friendly workout view

**🏛 Firmitas:**
- Dashboard (today's workout, quick stats)
- Logbook (view past workouts)
- 🧮 Saved Workouts (build personal collection)
- Random workout generator (from saved)

**🔨 Utilitas:**
- Workout library (view-only)
- Calculators (1RM, macros, volume)
- Timers (rest, EMOM, AMRAP)
- Basic settings

**🌹 Venustas:**
- Trophy room (achievements)
- Photo journal (private progress photos)
- Basic metrics (weight, measurements)

**🪐 Gravitas:**
- Content library (read-only access to Jake's essays)
- Exercise demos (video library)
- View challenges (participation requires opt-in)

**⌛ Temporitas:**
- View current Order (seasonal phase)
- Training history (calendar view)
- Basic goal tracking (self-serve)

**🐬 Sociatas:**
- Community forum (read and post)
- Public celebrations (#wins channel)
- No direct messaging to Jake

### Jake's Effort (Tier 1):

**Daily:**
- Write 1 workout (what Jake is training that day)
- Post to platform (5-10 minutes)

**Weekly:**
- Engage in forum occasionally (30-60 minutes)
- Post seasonal updates (#announcements)

**Monthly:**
- Write 1-2 long-form content pieces (essays, guides)
- Review community engagement metrics

**Automation Potential:** High
- RAG can eventually write daily workouts (Jake approves)
- Forum questions auto-answered by RAG (Jake moderates)
- Content library grows passively

---

## Tier 2: Personal Programming

**Price:** $25-30/month
**Target Audience:** Dedicated clients, those needing customization, higher engagement

### What They Get:

**Everything from Tier 1, PLUS:**

**🏛 Firmitas:**
- Personalized weekly program (based on their logs and goals)
- Custom workout adjustments (Jake reviews logs, modifies next week)
- Priority in program assignment

**🔨 Utilitas:**
- Request specific workouts from library
- Advanced settings (custom macros, detailed preferences)

**🌹 Venustas:**
- Jake reviews progress photos (optional)
- Personalized feedback on metrics
- Goal setting with Jake's input

**🪐 Gravitas:**
- Early access to new content
- Personalized challenges (Jake can create custom)

**⌛ Temporitas:**
- Personalized Order progression (Jake decides when to shift phases)
- Custom goal timelines with Jake's guidance

**🐬 Sociatas:**
- Direct messaging with Jake (asynchronous)
- Priority response time (24-48 hours)
- Future: Priority access to live workouts

### Jake's Effort (Tier 2):

**Weekly (Per Client):**
- Review workout logs (10 minutes)
- Assign next week's program (15 minutes if using templates)
- Respond to DMs (5-10 minutes)

**Monthly (Per Client):**
- Progress check-in (15 minutes)
- Program adjustment based on results
- Goal recalibration if needed

**Automation Potential:** Medium
- RAG suggests workouts based on logs (Jake approves/modifies)
- Templates reduce program creation time
- DM auto-drafts (Jake reviews before sending)

---

## Revenue Projections

### Phase 1 (Months 1-3): Early Adopters
```
Tier 1: 50 users × $10 = $500/month
Tier 2: 10 users × $25 = $250/month
Total: $750/month ($9,000/year)
Jake's time:
├─ Daily workouts: 10 min/day × 7 = 70 min/week
├─ Tier 2 management: 30 min/client × 10 = 300 min/week
├─ Forum engagement: 60 min/week
└─ Total: ~7 hours/week digital work
```

### Phase 2 (Months 4-9): Growth
```
Tier 1: 200 users × $10 = $2,000/month
Tier 2: 30 users × $25 = $750/month
Total: $2,750/month ($33,000/year)
Jake's time:
├─ Daily workouts: 10 min/day × 7 = 70 min/week
├─ Tier 2 management: 30 min/client × 30 = 900 min/week
├─ Forum moderation: 90 min/week
└─ Total: ~17 hours/week digital work
```

### Phase 3 (Year 2): Scale with Automation
```
Tier 1: 500 users × $10 = $5,000/month
Tier 2: 50 users × $25 = $1,250/month
Total: $6,250/month ($75,000/year)
Jake's time (with RAG automation):
├─ Review RAG-generated daily workouts: 5 min/day × 7 = 35 min/week
├─ Tier 2 management (RAG-assisted): 15 min/client × 50 = 750 min/week
├─ Moderate RAG forum responses: 60 min/week
└─ Total: ~14 hours/week digital work (less than Phase 2 despite 4x users)
```

---

## Platform Costs

### Year 1:
```
Hosting (Vercel): $0/month (free tier)
Database (Supabase): $0/month (free tier)
Domain: $12/year = $1/month
Email (transactional): $0/month (Supabase includes basic email)
Payment processing (Stripe): 2.9% + $0.30 per transaction
Total fixed costs: $1/month
```

### At Scale (200+ users):
```
Hosting (Vercel Pro): $20/month
Database (Supabase Pro): $25/month
Email (SendGrid): $15/month
Total fixed costs: $60/month
Stripe fees: ~3% of revenue
```

### Break-Even:
- 7 users (Tier 1) covers Year 1 costs
- 12 users (mixed tiers) covers scale costs

---

═══════════════════════════════════════════════════════════════════════════════
# 🗿 USER EXPERIENCE — The Card Deck Metaphor
═══════════════════════════════════════════════════════════════════════════════

## Core Metaphor: Workouts as Cards, Programs as Decks

**Mental Model:**
```
Workout = Card (individual training session)
Program = Deck (collection of cards in sequence)
🧮 SAVE = Add card to personal collection
Saved Library = Your card collection
Random Generator = Shuffle & draw from collection
```

This metaphor shapes the entire UX:
- Users "collect" workouts they love
- Programs are "chapters" they can return to
- History becomes an "almanac" of past training
- Variety comes from "drawing" random cards

---

## The 🧮 SAVE Workflow

### Trigger Point: After Workout Completion
```
User completes a workout → Logging screen appears:
┌─────────────────────────────────────┐
│ WORKOUT COMPLETE!                   │
│                                     │
│ 🪡 The Hinge and Pull               │
│ 85 minutes • 6 exercises            │
│                                     │
│ Rate this workout:                  │
│ ⭐ ⭐ ⭐ ⭐ ⭐                        │
│                                     │
│ Notes (optional):                   │
│ [PR on deadlifts! 180kg × 3      ]  │
│                                     │
│ ☐ 🧮 Save to my collection          │
│                                     │
│ [Submit Log]                        │
└─────────────────────────────────────┘
```

### If User Checks 🧮 SAVE:
```
┌─────────────────────────────────────┐
│ SAVE THIS WORKOUT                   │
│                                     │
│ Custom name (optional):             │
│ [My Best Pull Day Ever           ]  │
│                                     │
│ Tags (optional):                    │
│ [back] [heavy] [pr] [favorite]      │
│                                     │
│ Why you're saving it:               │
│ [Hit a huge deadlift PR today.   ]  │
│ [Form felt perfect, want to      ]  │
│ [repeat this exact workout.      ]  │
│                                     │
│ [Cancel] [Save to Collection]       │
└─────────────────────────────────────┘
```

### Result:
- Workout added to `saved_workouts` table
- Appears in 🏛 Firmitas → 🧮 Saved Workouts
- Available for Random Workout Generator
- Searchable by tags, name, date saved

---

## Program Structure: The Chapter System

### Jake Creates a Program (Admin View):
```
Program: "Summer Cut 2025"
Duration: 8 weeks
Primary Order: 🦋 Hypertrophy
Week 1: Foundation
├─ Day 1: 🛒 Push Hypertrophy
├─ Day 2: 🪡 Pull Volume
├─ Day 3: 🍗 Leg Emphasis
├─ Day 4: 🖼 Restoration
├─ Day 5: ➕ Full Body Power
└─ Days 6-7: Rest
Week 2: Build
├─ Day 1: 🛒 Push Volume
├─ Day 2: 🪡 Pull Hypertrophy
[... continues through Week 8]
```

### User Receives Program Assignment:
```
Notification:
"📖 Jake assigned you a new program: Summer Cut 2025"
Dashboard shows:
┌─────────────────────────────────────┐
│ 📖 CURRENT PROGRAM                  │
│                                     │
│ 🦋 Summer Cut 2025                  │
│ Week 1 of 8 • Day 1                 │
│                                     │
│ [View Today's Workout] →            │
│                                     │
│ [View Full Program] →               │
└─────────────────────────────────────┘
```

### User Completes Week 1:
```
Progress updates automatically:
┌─────────────────────────────────────┐
│ 🦋 Summer Cut 2025                  │
│ Week 2 of 8 • Day 1                 │
│                                     │
│ Progress: ██████░░░░░░░░ 13%        │
│                                     │
│ Week 1 complete! 5/5 workouts ✓     │
└─────────────────────────────────────┘
```

### User Completes Full Program (Week 8):
```
┌─────────────────────────────────────┐
│ 🎉 PROGRAM COMPLETE!                │
│                                     │
│ 🦋 Summer Cut 2025                  │
│ 8 weeks • 40 workouts               │
│                                     │
│ Rate this program:                  │
│ ⭐ ⭐ ⭐ ⭐ ⭐                        │
│                                     │
│ What did you think?                 │
│ [Best program I've ever done.    ]  │
│ [Saw real definition, loved the  ]  │
│ [high volume pull work.          ]  │
│                                     │
│ [Submit & Archive]                  │
└─────────────────────────────────────┘
```

Program moves to "Completed" section in My Programs.

---

## Returning to a Past Program

### User's Completed Programs:
```
═══════════════════════════════════════════════════
MY PROGRAMS → COMPLETED
═══════════════════════════════════════════════════
┌─────────────────────────────────────┐
│ 🦋 Summer Cut 2025                  │
│ 8 weeks • Completed Feb 11, 2026    │
│ ⭐⭐⭐⭐⭐ "Best program ever"        │
│                                     │
│ Results:                            │
│ • Lost 8kg                          │
│ • PRs on all major lifts            │
│ • Visible abs for first time        │
│                                     │
│ [Restart] [View Workouts] [Stats]   │
└─────────────────────────────────────┘
```

### User Taps "Restart":
```
┌─────────────────────────────────────┐
│ RESTART PROGRAM                     │
│                                     │
│ You're about to restart:            │
│ "🦋 Summer Cut 2025"                │
│                                     │
│ This will:                          │
│ • Set this as your active program   │
│ • Start you at Week 1, Day 1        │
│ • Keep your original logs           │
│                                     │
│ New name (optional):                │
│ [Summer Cut 2026                 ]  │
│                                     │
│ [Cancel] [Restart Program]          │
└─────────────────────────────────────┘
```

### Result:
- Program becomes active again
- User can compare 2025 logs vs 2026 logs
- Same workouts, new timeline
- Personal "almanac" of past performance

---

## Random Workout Generator

### User Flow:
```
User taps: 🎲 Random Workout (from saved)
┌─────────────────────────────────────┐
│ 🎲 RANDOM WORKOUT GENERATOR         │
│                                     │
│ Pull from:                          │
│ ☑ My Saved Workouts (27)            │
│ ☑ Daily Workouts I've Done (103)    │
│ ☐ All Daily Workouts (421)          │
│                                     │
│ Filter by type:                     │
│ ☑ 🛒 Push                           │
│ ☑ 🪡 Pull                           │
│ ☑ 🍗 Legs                           │
│ ☐ ➕ Plus                           │
│ ☐ ➖ Ultra                          │
│                                     │
│ Exclude workouts done in last:      │
│ [ 7 days ▼]                         │
│                                     │
│ [Generate Random Workout] 🎲        │
└─────────────────────────────────────┘
```

### After Generation:
```
┌─────────────────────────────────────┐
│ 🎲 YOUR RANDOM WORKOUT              │
│                                     │
│ 🪡 The Hinge and Pull               │
│ From: Your Saved Workouts           │
│ Last done: Jan 15, 2026 (27 days ago)│
│                                     │
│ "Heavy deadlift work + posterior    │
│  chain thickness — 75-90 min"       │
│                                     │
│ [Do This Workout] [Draw Again] 🎲   │
└─────────────────────────────────────┘
```

### Algorithm Logic:
```javascript
function generateRandomWorkout(userId, filters) {
  // 1. Get pool of eligible workouts
  let pool = [];

  if (filters.includeSaved) {
    pool.push(...getSavedWorkouts(userId));
  }

  if (filters.includeCompleted) {
    pool.push(...getCompletedWorkouts(userId));
  }

  if (filters.includeAllDaily) {
    pool.push(...getAllDailyWorkouts());
  }

  // 2. Apply type filters
  pool = pool.filter(w => filters.types.includes(w.type_emoji));

  // 3. Exclude recent workouts
  const cutoffDate = new Date();
  cutoffDate.setDate(cutoffDate.getDate() - filters.excludeDays);
  pool = pool.filter(w => w.last_done < cutoffDate || !w.last_done);

  // 4. Remove duplicates
  pool = [...new Set(pool.map(w => w.workout_id))];

  // 5. Random selection
  const randomIndex = Math.floor(Math.random() * pool.length);
  return pool[randomIndex];
}
```

---

═══════════════════════════════════════════════════════════════════════════════
# 🔨 TECHNICAL ARCHITECTURE
═══════════════════════════════════════════════════════════════════════════════

## Technology Stack

### Frontend:
- **Next.js 14** (React framework)
- **TypeScript** (type safety)
- **Tailwind CSS** (utility-first styling)
- **shadcn/ui** (component library, optional)

### Backend:
- **Supabase** (PostgreSQL database + auth + storage + realtime)
- **Next.js API Routes** (serverless functions)

### Hosting:
- **Vercel** (automatic deployments from GitHub)
- **Supabase Cloud** (database hosting)

### Payment:
- **Stripe** (subscription management)

### Communication:
- **Supabase Realtime** (forum, chat)
- **SendGrid** (transactional emails, future)

---

## Database Schema (Complete)

```sql
-- Users (handled by Supabase Auth)
-- Supabase creates auth.users automatically

-- User profiles (extends auth.users)
CREATE TABLE profiles (
  id UUID REFERENCES auth.users PRIMARY KEY,
  full_name TEXT,
  bodyweight DECIMAL,
  unit_system TEXT DEFAULT 'kg', -- 'kg' or 'lbs'
  subscription_tier INTEGER DEFAULT 1, -- 1 or 2
  created_at TIMESTAMP DEFAULT NOW()
);

-- Workouts (the cards)
CREATE TABLE workouts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title TEXT NOT NULL,
  markdown_content TEXT NOT NULL,
  order_emoji TEXT, -- 🐂⛽🦋🏟🌾⚖🖼
  type_emoji TEXT,  -- 🛒🪡🍗➕➖
  axis_emoji TEXT,  -- 🏛🔨🌹🪐⌛🐬
  color_emoji TEXT, -- ⚫🟢🔵🟣🔴🟠🟡⚪
  created_by UUID REFERENCES auth.users,
  is_daily BOOLEAN DEFAULT FALSE,
  published_date DATE,
  estimated_duration INTEGER, -- minutes
  created_at TIMESTAMP DEFAULT NOW()
);

-- Programs (the decks)
CREATE TABLE programs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title TEXT NOT NULL,
  description TEXT,
  duration_weeks INTEGER NOT NULL,
  phase_emoji TEXT, -- Primary Order
  created_by UUID REFERENCES auth.users,
  is_template BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Program workout sequence
CREATE TABLE program_workouts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  program_id UUID REFERENCES programs ON DELETE CASCADE,
  workout_id UUID REFERENCES workouts ON DELETE CASCADE,
  week_number INTEGER NOT NULL,
  day_number INTEGER NOT NULL,
  sequence_order INTEGER,
  UNIQUE(program_id, week_number, day_number)
);

-- User assigned programs (chapters)
CREATE TABLE user_programs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users ON DELETE CASCADE,
  program_id UUID REFERENCES programs,
  assigned_date DATE DEFAULT NOW(),
  start_date DATE,
  status TEXT DEFAULT 'active', -- 'active', 'completed', 'paused'
  current_week INTEGER DEFAULT 1,
  current_day INTEGER DEFAULT 1,
  nickname TEXT, -- User can rename program
  rating INTEGER, -- 1-5 stars
  review TEXT,
  completed_at TIMESTAMP
);

-- Workout logs (history)
CREATE TABLE workout_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users ON DELETE CASCADE,
  workout_id UUID REFERENCES workouts,
  user_program_id UUID REFERENCES user_programs, -- NULL if not from program
  completed_date DATE DEFAULT NOW(),
  exercises_logged JSONB, -- {exercise_name, sets: [{weight, reps}]}
  overall_rating INTEGER, -- 1-10
  notes TEXT,
  saved BOOLEAN DEFAULT FALSE, -- 🧮 SAVE flag
  created_at TIMESTAMP DEFAULT NOW()
);

-- Saved workouts (personal collection)
CREATE TABLE saved_workouts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users ON DELETE CASCADE,
  workout_id UUID REFERENCES workouts,
  saved_date DATE DEFAULT NOW(),
  custom_name TEXT,
  tags TEXT[], -- Array of tags
  notes TEXT,
  UNIQUE(user_id, workout_id)
);

-- Community forum posts
CREATE TABLE forum_posts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users,
  channel TEXT NOT NULL, -- 'daily', 'form-checks', 'wins', etc.
  title TEXT,
  content TEXT NOT NULL,
  attachments TEXT[], -- URLs to images/videos
  created_at TIMESTAMP DEFAULT NOW()
);

-- Forum comments
CREATE TABLE forum_comments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  post_id UUID REFERENCES forum_posts ON DELETE CASCADE,
  user_id UUID REFERENCES auth.users,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Direct messages (Tier 2 only)
CREATE TABLE direct_messages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  sender_id UUID REFERENCES auth.users,
  recipient_id UUID REFERENCES auth.users,
  subject TEXT,
  content TEXT NOT NULL,
  attachments TEXT[], -- URLs
  read BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Achievements/badges
CREATE TABLE user_achievements (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users ON DELETE CASCADE,
  achievement_type TEXT NOT NULL, -- 'streak_7', 'pr_100kg_squat', etc.
  achieved_date DATE DEFAULT NOW(),
  metadata JSONB -- Additional context
);

-- Progress photos
CREATE TABLE progress_photos (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users ON DELETE CASCADE,
  photo_url TEXT NOT NULL, -- Supabase Storage URL
  photo_type TEXT, -- 'front', 'side', 'back'
  date_taken DATE DEFAULT NOW(),
  notes TEXT,
  is_public BOOLEAN DEFAULT FALSE
);
```

---

## Mobile-First Design Constraints

### Screen Size:
- **Portrait mode only** (for now)
- Width: 375-430px (iPhone SE to iPhone Pro Max)
- Height: Variable (scrollable content)

### Typography:
- Base font: 14px (readable without zoom)
- Headers: 18-24px (clear hierarchy)
- Emojis: 1.2em (larger than text, visually distinct)
- Monospace for workouts: Preserves tree connectors

### Layout:
- Single column (no side-by-side content)
- Bottom tab navigation (6 axes, always visible)
- Minimal chrome (maximize content space)
- Progressive disclosure (collapse sections by default)

### Screenshot Mode:
```css
@media print, .screenshot-mode {
  /* Hide all UI chrome */
  nav, .tab-bar, .back-button, .log-button {
    display: none;
  }

  /* Clean borders for screenshot */
  .workout-container {
    border: 2px solid #000;
    padding: 1rem;
  }

  /* Ensure tree connectors render */
  .workout-content {
    font-family: 'SF Mono', Consolas, monospace;
    white-space: pre-wrap;
  }
}
```

### Logging Interface (Progressive Disclosure):

**Initial View:**
```
Workout displays in full-screen, read-only mode.
[Do This Workout]  [Screenshot] [🧮 Save]
```

**User Taps "Do This Workout":**
```
Same workout, now with input fields inline:
🧈 BREAD & BUTTER
├─ Barbell Back Squat — 4 sets:
│   Set 1: 🐂 70% × 5  [__kg] × [__reps] ✓
│   Set 2: 🐂 75% × 4  [__kg] × [__reps] ✓
│   Set 3: ⛽ 82% × 3  [__kg] × [__reps] ✓
│   Set 4: ⛽ 85% × 3  [__kg] × [__reps] ✓
[Submit & Next Exercise]
```

Logging happens exercise-by-exercise, not all at once (reduces cognitive load).

---

## API Structure

### Authentication:
```typescript
// Supabase handles auth
// Sign up
const { user, error } = await supabase.auth.signUp({
  email: 'user@example.com',
  password: 'password'
});

// Sign in
const { user, error } = await supabase.auth.signInWithPassword({
  email: 'user@example.com',
  password: 'password'
});
```

### Fetching Workouts:
```typescript
// Get today's daily workout
const { data, error } = await supabase
  .from('workouts')
  .select('*')
  .eq('is_daily', true)
  .eq('published_date', new Date().toISOString().split('T')[0])
  .single();

// Get user's assigned program
const { data, error } = await supabase
  .from('user_programs')
  .select(`
    *,
    program:programs(*),
    program_workouts(
      *,
      workout:workouts(*)
    )
  `)
  .eq('user_id', userId)
  .eq('status', 'active')
  .single();
```

### Logging a Workout:
```typescript
const { data, error } = await supabase
  .from('workout_logs')
  .insert({
    user_id: userId,
    workout_id: workoutId,
    user_program_id: userProgramId, // NULL if not from program
    completed_date: new Date().toISOString().split('T')[0],
    exercises_logged: {
      "Barbell Back Squat": {
        sets: [
          { weight: 100, reps: 5 },
          { weight: 107, reps: 4 },
          { weight: 117, reps: 3 },
          { weight: 121, reps: 3 }
        ]
      }
    },
    overall_rating: 9,
    notes: "Felt strong today, depth was good",
    saved: true // User checked 🧮 SAVE
  });
```

### Random Workout Generation:
```typescript
// Server-side function (Next.js API route)
export default async function handler(req, res) {
  const { userId, filters } = req.body;

  // Get saved workouts
  const { data: saved } = await supabase
    .from('saved_workouts')
    .select('workout_id')
    .eq('user_id', userId);

  // Get completed workouts (if opted in)
  const { data: completed } = await supabase
    .from('workout_logs')
    .select('workout_id')
    .eq('user_id', userId);

  // Combine pools
  let pool = [...saved.map(s => s.workout_id), ...completed.map(c => c.workout_id)];

  // Remove duplicates
  pool = [...new Set(pool)];

  // Fetch full workout data
  const { data: workouts } = await supabase
    .from('workouts')
    .select('*')
    .in('id', pool);

  // Apply type filters
  let filtered = workouts.filter(w =>
    filters.types.includes(w.type_emoji)
  );

  // Random selection
  const random = filtered[Math.floor(Math.random() * filtered.length)];

  res.json({ workout: random });
}
```

---

═══════════════════════════════════════════════════════════════════════════════
# 🪜 AUTOMATION PATHWAY — The RAG Integration
═══════════════════════════════════════════════════════════════════════════════

## The Goal: Jake's Time Investment Decreases as User Base Grows

**Current State (Manual):**
- 100 users = 10 hours/week
- 500 users = 50 hours/week (unsustainable)

**Future State (Automated):**
- 100 users = 10 hours/week
- 500 users = 15 hours/week (RAG handles most)
- 1000 users = 20 hours/week (still manageable)

---

## Phase 1: Manual Operation (Months 1-3)

**Jake's Workflow:**

**Daily:**
- Write 1 daily workout (what Jake is training)
- Post to platform (10 minutes)

**Weekly:**
- Review Tier 2 client logs (10 min × 10 clients = 100 min)
- Assign next week's workouts (15 min × 10 clients = 150 min)
- Respond to DMs (5 min × 10 clients = 50 min)
- Forum engagement (30 min)

**Total: ~6-8 hours/week**

---

## Phase 2: Assisted (Months 4-6)

**RAG Integration Begins:**

### RAG Training Data:
- All workouts Jake has written (SCL formatted)
- Jake's training logs (15,000+ hours documented)
- Client feedback (ratings, reviews)
- Forum Q&A (Jake's answers become training data)
- This context document (🧮 PPL± Itself)

### RAG Capabilities:

**1. Daily Workout Suggestions**
```
RAG analyzes:
├─ Current Order (🦋 Ionic, Week 3)
├─ Recent daily workouts (last 7 days)
├─ Seasonal context (late winter, moderate temps)
├─ Climate data (South Carolina weather)
└─ Training patterns (Jake's typical Week 3 Ionic work)
RAG generates:
"Suggested daily workout for Feb 12, 2026:
🪡🗿🔴 Pull Sculpt Intense
Heavy pull work + hypertrophy finish. 75 min.
Would you like to review/edit before posting?"
```

**Jake's Workflow:**
- Review RAG suggestion (2 minutes)
- Edit if needed (5 minutes)
- Approve and post (1 minute)

**Time saved: 50%** (10 min → 5 min per day)

**2. Forum Auto-Responses**
```
User asks in #questions:
"How do I know if I'm ready for 🏟 Performance phase?"
RAG drafts response:
"Great question! You're ready for 🏟 Performance when:
- You've completed at least 4 weeks of 🦋 Hypertrophy
- Your technique is consistent under fatigue
- You want to test your current maximums
Jake recommends a deload week before testing. Would you like
me to suggest a deload protocol?"
[Jake: Approve] [Edit] [Reject]
```

Jake reviews before posting (saves 80% of time writing responses).

---

## Phase 3: Semi-Automated (Months 7-12)

### RAG Expands Capabilities:

**1. Tier 2 Program Suggestions**
```
RAG analyzes Sarah's logs:
├─ Completed "Summer Cut 2025" (8 weeks)
├─ PRs on all pull exercises
├─ Saved 9 pull workouts (favorites)
├─ Ratings: ⭐⭐⭐⭐⭐ on high-volume back work
├─ Comments: "Love the deadlift variations"
└─ Goal: "Get stronger, maintain definition"
RAG suggests next program:
"🏟 Upper Body Strength Block (4 weeks)
Focus: Max strength in pull patterns
Frequency: 4×/week (Pull 2×, Push 1×, Legs 1×)
Week 1-2: Strength foundation (75-85% loads)
Week 3: Intensification (85-90% loads)
Week 4: Test week (90-100% loads)
This builds on Sarah's pull strength while maintaining
her cut physique. Approve to assign?"
[Jake: Approve] [Modify] [Create Custom Instead]
```

**Jake's Workflow:**
- Review RAG suggestion (3 minutes)
- Modify if needed (5 minutes)
- Approve and assign (1 minute)

**Time saved: 70%** (20 min → 6 min per client program)

**2. Smart Exercise Substitutions**
```
Client reports: "Gym doesn't have safety squat bar"
RAG suggests alternatives:
"Based on the workout's intent (quad emphasis, back-friendly):
1. Front Squat (same quad bias, less spinal load)
2. Goblet Squat (beginner-friendly, same pattern)
3. Leg Press (isolation, no barbell needed)
Which would you prefer? I'll adjust your program."
```

Client selects, RAG updates program automatically, Jake gets notification.

---

## Phase 4: Fully Automated (Year 2+)

### RAG Operates Autonomously (with Jake's Oversight)

**Daily Workflows:**

**1. Daily Workout Publishing (100% Automated)**
```
Every morning at 6:00 AM:
├─ RAG generates daily workout based on:
│   ├─ Current Order and week
│   ├─ Seasonal context
│   ├─ Recent workout patterns
│   └─ Climate data
├─ Formats in SCL (perfect structure)
├─ Posts to platform automatically
└─ Sends Jake notification: "Daily workout posted ✓"
Jake reviews later (5 min/day, asynchronous)
```

**2. Forum Moderation (90% Automated)**
```
User posts question → RAG responds immediately
User posts form check video → RAG tags Jake for review
User celebrates PR → RAG congratulates, suggests next challenge
Spam detected → RAG flags for moderation
Jake checks moderation queue 1×/day (15 min)
```

**3. Tier 2 Program Management (80% Automated)**
```
Weekly cycle (Sunday night):
├─ RAG reviews all Tier 2 client logs
├─ Generates next week's programs
├─ Sends drafts to Jake's admin panel
├─ Jake reviews/approves in batch (30 min for 50 clients)
└─ RAG assigns approved programs automatically
Clients wake up Monday with new week ready ✓
```

**Jake's Weekly Time Commitment at 500 Users:**
```
Daily workout review: 5 min × 7 = 35 min/week
Forum moderation: 15 min/day × 7 = 105 min/week
Tier 2 program approval: 30 min (batch review)
DM responses (flagged by RAG): 30 min/week
Content creation (essays, demos): 2 hours/week
Total: ~5 hours/week digital work
(Down from 50 hours/week without automation)
```

---

## What RAG Learns Over Time

**Training Data Sources:**

1. **Workout Library**
   - Every workout Jake writes (SCL structure)
   - Exercise selection patterns
   - Loading schemes by Order
   - Block combinations that work

2. **Client Feedback**
   - Workout ratings (⭐⭐⭐⭐⭐)
   - Saved workouts (what clients love)
   - Written reviews (qualitative data)
   - Progress metrics (what produces results)

3. **Jake's Edits**
   - When Jake modifies RAG suggestions
   - Learn from corrections
   - Pattern recognition improves

4. **Forum Interactions**
   - Common questions (build FAQ automatically)
   - Jake's answers (learn his voice)
   - Community wisdom (what resonates)

5. **Seasonal Patterns**
   - South Carolina climate data
   - Historical workout archives
   - Order progressions across years

**Result:** RAG becomes Jake's digital apprentice, trained on 15,000+ hours of expertise.

---

═══════════════════════════════════════════════════════════════════════════════
# 🚂 JUNCTION — Implementation Phases
═══════════════════════════════════════════════════════════════════════════════

## Week 1: MVP (Minimum Viable Product)

**Goal:** Usable platform for 1-5 test clients

**Features:**
- ✅ User signup/login (Supabase Auth)
- ✅ 🏛 Firmitas: Home dashboard
- ✅ Daily workout display (mobile-optimized)
- ✅ Basic logging (weights, reps, notes)
- ✅ Workout completion flow
- ✅ 🧮 SAVE functionality (basic)

**Tech:**
- Next.js project initialized
- Supabase database configured
- Mobile CSS (portrait mode, screenshot-friendly)
- Deploy to Vercel (live URL)

**Jake's Content:**
- 7 daily workouts written (Week 1 content)
- 1 test program created (4 weeks)
- Terms of service drafted

---

## Weeks 2-3: Essential Features

**Goal:** Ready for first paying clients

**Features:**
- ✅ Payment integration (Stripe subscriptions)
- ✅ Tier 1 vs Tier 2 access control
- ✅ 🔨 Utilitas: Workout library, calculators, timers
- ✅ 🐬 Sociatas: Basic forum (channels, posts, comments)
- ✅ My Programs (view assigned programs)
- ✅ Saved Workouts collection

**Tech:**
- Stripe webhook handling
- Forum realtime updates (Supabase Realtime)
- Admin panel (Jake can create/assign workouts)

**Jake's Content:**
- 14 daily workouts (2 weeks ahead)
- 2-3 program templates ready
- Forum channels configured

---

## Weeks 4-6: Growth Features

**Goal:** Scale to 20-50 users

**Features:**
- ✅ 🌹 Venustas: Progress photos, trophy room, metrics
- ✅ ⌛ Temporitas: Seasonal calendar, goal tracking
- ✅ 🐬 Sociatas: Direct messaging (Tier 2 only)
- ✅ Random workout generator
- ✅ Program restart functionality

**Tech:**
- Image upload (Supabase Storage)
- Achievement system (badge triggers)
- DM notifications
- Analytics dashboard (Jake sees user metrics)

**Jake's Content:**
- 30 daily workouts (1 month ahead)
- 5-10 program templates
- First long-form essay (🪐 Gravitas)

---

## Month 2-3: Premium Features

**Goal:** Scale to 100+ users, prepare for automation

**Features:**
- ✅ 🪐 Gravitas: Content library, exercise demos
- ✅ Admin dashboard (client management, program builder)
- ✅ Email notifications (workout reminders)
- ✅ Advanced logging (charts, progression tracking)
- ✅ Community features (leaderboards, challenges)

**Tech:**
- Video hosting (YouTube embeds or Supabase Storage)
- Email service (SendGrid integration)
- Chart rendering (Recharts library)
- Program builder GUI (drag-and-drop workouts)

**Jake's Content:**
- 60 daily workouts (2 months ahead)
- 10+ program templates (varied goals)
- Exercise demo videos (20-30 exercises)
- 3-5 long-form essays

---

## Month 4+: Automation Integration

**Goal:** RAG-assisted operation, scale to 500+ users

**Features:**
- ✅ RAG daily workout generation (Jake approves)
- ✅ RAG forum responses (Jake moderates)
- ✅ RAG program suggestions (Jake customizes)
- ✅ Smart exercise substitutions
- ✅ Predictive analytics (client progress forecasting)

**Tech:**
- RAG model trained on Jake's data
- Claude API integration (or custom model)
- Approval workflow (Jake's admin panel)
- Continuous learning (feedback loop)

**Jake's Content:**
- RAG handles daily workouts (Jake reviews)
- Focus shifts to higher-level content (essays, demos)
- Community engagement (live workouts, Q&A sessions)

---

═══════════════════════════════════════════════════════════════════════════════
# 🧬 IMPRINT — Core Principles
═══════════════════════════════════════════════════════════════════════════════

## Design Philosophy

**1. Mobile-First, Always**
- Desktop is a nice-to-have, not a requirement
- Portrait mode screenshot-friendly (workouts as image cards)
- Progressive Web App (offline capable, "add to home screen")

**2. SCL as the Semantic Foundation**
- Workouts formatted in PPL± Semantic Compression Language
- Emojis aren't decoration—they're addresses
- ZIP codes create addressable, queryable content
- Consistency enables automation (RAG can parse structure)

**3. Card Deck Metaphor**
- Workouts = Cards (collect your favorites)
- Programs = Decks (structured sequences)
- 🧮 SAVE creates personal collection
- Random generator = shuffle & draw
- History = almanac of past training

**4. Tiered Access, Not Feature Walls**
- Tier 1 gets real value (daily workouts, community, tools)
- Tier 2 gets personalization (not locked features)
- Never: "Upgrade to see this"
- Always: "Upgrade for personal coaching"

**5. Automation Serves the Coach, Not Replaces**
- RAG generates drafts, Jake approves
- AI suggests, humans decide
- Technology scales craft, doesn't dilute it
- Jake's expertise remains the product

**6. Data Ownership**
- Users own their logs, photos, notes
- Export functionality (future feature)
- Privacy controls (choose what to share)
- No selling user data, ever

**7. Community as Accountability**
- Forum before DMs (public knowledge benefits all)
- Celebrate wins loudly (#wins channel)
- Support struggles quietly (DMs, moderation)
- No toxic positivity (honest training talk)

---

## Non-Negotiables

**Legal Compliance:**
- Terms of Service on signup (liability waiver)
- Clear disclaimers (informational use, not medical)
- Jake's PT insurance covers platform usage
- No medical claims, diagnosis, or treatment

**User Safety:**
- Emergency protocol visible in app
- "Stop if pain/dizziness" messaging
- Form checks flagged for Jake's review (not AI-diagnosed)
- Conservative recommendations (RAG biases safety)

**Content Quality:**
- No auto-publishing without Jake's review (Phase 1-3)
- Even automated RAG requires approval (Phase 4)
- Forum moderation (no spam, harassment, misinformation)
- Exercise demos verified for safety

**Financial Integrity:**
- Transparent pricing (no hidden fees)
- Easy cancellation (Stripe handles)
- Refund policy (pro-rated if unused)
- Lifetime access to paid content (Jake's anti-extraction philosophy)

---

═══════════════════════════════════════════════════════════════════════════════
# 🧮 SAVE — Document Status
═══════════════════════════════════════════════════════════════════════════════

**This document captures:**
- ✅ Complete platform architecture (6-axis navigation)
- ✅ Business model (tiered subscriptions, revenue projections)
- ✅ User experience (card deck metaphor, workflows)
- ✅ Technical architecture (database, API, stack)
- ✅ Automation pathway (RAG integration phases)
- ✅ Core principles (design philosophy, non-negotiables)

**Next steps (as of February 11, 2026 — superseded by V2):**
1. Build Week 1 MVP (initialize Next.js + Supabase)
2. Write Terms of Service (legal compliance)
3. Create 7 daily workouts (content ready for launch)
4. Design mobile UI (Figma mockups or direct code)
5. Deploy to Vercel (live testing environment)

**Living document note:**
- This will evolve as platform develops
- Features may shift based on user feedback
- Technical decisions may adapt to constraints
- Core vision remains: scale Jake's coaching craft through intelligent automation

═══════════════════════════════════════════════════════════════════════════════
🧸 fero — Carry this vision into reality. The architecture stands. The path is clear.
═══════════════════════════════════════════════════════════════════════════════
🧮 PPL± ITSELF — COMPLETE
═══════════════════════════════════════════════════════════════════════════════
