---
planted: 2026-03-11
status: SEED
phase-relevance: Phase 7+ (Full Platform)
blocks: nothing currently — vision layer for long-term platform expansion
depends-on: seeds/digital-city-architecture.md, seeds/operis-architecture.md, seeds/elevator-architecture.md, seeds/data-ethics-architecture.md, seeds/character-progression-architecture.md
connects-to: seeds/home-screen-architecture.md, seeds/exploration-immersion-architecture.md, seeds/heros-almanac-v8-architecture.md, seeds/systems-eudaimonics.md, seeds/content-types-architecture.md
extends: seeds/digital-city-architecture.md (adds life domains, app integrations, copilot philosophy, grandfather's gift principle)
---

# Life Copilot Architecture — The Full Platform Vision

⚫🪐 — foundational + deep

## One Sentence

Ppl± is a daily life copilot where the workout is the anchor tenant that gets people showing up, and everything else — career guidance, financial literacy, civics, seasonal almanac, games, puzzles, community, integrations — exists because people are already there, training in the city.

---

## Section 1 — The Cathedral Thesis

Ppl± is not a workout app that added features. It is a life platform that started with workouts.

The workout is the MVP foundation — the anchor tenant in a traditional city that generates daily foot traffic. The market in the piazza. The reason people show up every morning. But a city is not a market. The market is what brings people. The city is what keeps them.

Every great platform started this way. Apple started with a computer in a garage. The computer was the anchor tenant. The ecosystem grew around it. The workout is the computer. Ppl± is the ecosystem.

### The Grandfather's Gift Principle

The app should feel like it was built by the user's grandfather — crafted with care, candid, colorful, designed to make life easier to manage. A personal living almanac that's always there, always helpful, always fair, always honest.

Not a social media dopamine trap. Not a gamified engagement machine. A genuine tool that respects the user's intelligence, time, and agency. The kind of gift someone gives when they actually care about the recipient's wellbeing.

### The 100-Year Architecture

Jake designs from the 100-year vision backwards to today's buildable pieces. The architecture exists at full scale. Implementation grows into it. Nothing is built that contradicts the full vision. Every piece laid today fits the cathedral that will stand in a century.

This is not idealism. This is architectural practice. You don't build a cathedral without blueprints. You don't draw blueprints without knowing what the cathedral serves. The vision precedes the foundation.

---

## Section 2 — Life Domains

The workout anchor opens access to broader life support. Each domain lives within the existing SCL addressing system — the 6 Axis floors and the content type registry (109 types across 6 axes, see `middle-math/content-type-registry.json`).

### Domain Mapping to Existing Architecture

| Life Domain | Primary Floor | Content Type Examples | How It Connects to Workouts |
|-------------|--------------|----------------------|----------------------------|
| **Physical Training** | 🏛 Firmitas | Workouts, exercise education, form guides | IS the anchor tenant. Direct. |
| **Career & Professional** | 🪐 Gravitas | Career guidance, mentorship content, skill development frameworks | Order progression maps to professional development stages. 🐂 Foundation = learning new skills. ⛽ Strength = building core competence. 🏟 Performance = demonstrating mastery. |
| **Financial Literacy** | ⌛ Temporitas | Budgeting frameworks, tax season guides, financial planning by life stage | Seasonal almanac calendar ties financial events to real calendar dates. Tax season content surfaces in April. Retirement planning surfaces at relevant life stages. |
| **Civic Engagement** | 🐬 Sociatas | Public information, voter guides, local resource directories, community events | Community floor naturally hosts civic discussion. Non-partisan per publication standard. |
| **Health & Wellness** | 🌹 Venustas | Nutrition, sleep, mental health resources, recovery protocols | Direct extension of the workout layer. Personal floor tracks health alongside training. |
| **Education & Learning** | 🪐 Gravitas | Course recommendations, book summaries, skill trees for learning domains | Cosmogram layer already provides deep educational content per deck. |
| **Creative Expression** | 🟡 content types | Art, music, writing, craft — creative skill development and community | 🟡 Fun / Exploration Color domain. Discovery and play are built into the system. |
| **Seasonal Living** | ⌛ Temporitas | Agricultural awareness, astronomical events, cultural calendars, holiday preparation | The 12 operators already map to 12 months with agricultural rationale. The Operis already publishes seasonal context daily. |

### The Informational Standard

All life domain content follows the publication standard (`scl-deep/publication-standard.md`):
- **NPR/PBS register.** Informational. Independent of Party or Faction. Committed to Useful Knowledge.
- **No advice, no prescription.** The system provides information and frameworks. The user makes decisions.
- **No affiliate links, no sponsored content.** The business model is subscriptions. The user is the customer, not the product.
- **Culturally inclusive.** No assumptions about the user's background, beliefs, nationality, or circumstances.
- **E for everyone.** Content passes the publication standard for all audiences.

---

## Section 3 — The Daily Copilot Experience

### What the App Knows

With user consent and engagement data, the system builds awareness of:
- Current training phase (from rotation engine + logged workouts)
- Seasonal position (date, weather if opted in, regional context)
- Personal vector state (which vials are full, which are sludgy)
- Engagement patterns (when they open the app, how long they stay, what they explore)
- Calendar context (tax season, holidays, seasonal transitions)

### What the App Surfaces

Based on awareness, the Operis and home screen surface relevant content from the content type registry:

**Morning open (commute, breakfast):**
- Today's workout (always first — anchor tenant)
- Today's Operis headline (seasonal, historical, editorial)
- 1-2 life domain nudges based on calendar: "Tax filing deadline is in 3 weeks" (April), "Daylight saving: adjust your training window" (March)

**Midday check (lunch break):**
- Quick-access workout tools if mid-session
- Community highlights from visited zip codes
- Brief educational content from cosmogram layer

**Evening return (wind-down):**
- Session summary if workout was logged
- Tomorrow's preview (what the rotation engine suggests)
- ⚪ Mindful content: recovery, reflection, breath work

**Weekly rhythm:**
- Weekly vial balance summary: "Your 🟢 Self-Reliance improved. Your ⚪ Recovery needs attention."
- Suggested zip codes that address the weakest vials
- Community highlights from the week

**Seasonal rhythm:**
- Monthly operator shift: "March is 🧸 fero — the month of carrying and transferring."
- Seasonal content relevant to the user's region (if opted in)
- Almanac entries that connect training to life context

### What the App Does NOT Do

- **Does not send push notifications for engagement.** Notifications only for time-sensitive information the user opted into (workout reminders, community replies).
- **Does not track location.** Regional content is opt-in and user-declared, not GPS-derived (per `seeds/data-ethics-architecture.md`).
- **Does not algorithmically curate a feed.** Content surfaces on a deterministic schedule (rotation engine + calendar). The same date produces the same structure. No engagement optimization.
- **Does not sell attention.** No ads. No sponsored content. No data sharing. Subscriptions are the business model.

---

## Section 4 — App Integrations and Embeds

### Widget Layer

Ppl± widgets for home screen (mobile) and desktop:
- **Today's zip** — small widget showing the rotation engine's daily recommendation. Tap to enter.
- **Vial balance** — 8 mini vials showing current balance at a glance.
- **Next workout** — countdown to next scheduled session with zip code.
- **Operis headline** — today's front page in a single line.

### Integration Points (Future)

| Integration | Direction | What It Provides |
|-------------|-----------|------------------|
| Calendar (iCal/Google) | Export | Workout schedule, Operis daily entry, seasonal markers |
| Health apps (Apple Health, Google Fit) | Import | Step counts, heart rate, sleep data → adjusts ⚪ Recovery vial |
| Music (Spotify, Apple Music) | Embed | Workout playlists tied to zip code mood. Color → playlist vibe. |
| Podcast / Audiobook | Embed | Educational content consumption during ➖ Ultra cardio sessions |
| Note-taking (Obsidian, Notion) | Export | Training logs, personal notes, cosmogram highlights |
| Weather | Import (opt-in) | Environmental context for seasonal immersion (see `seeds/exploration-immersion-architecture.md`) |

### Automotive Layer

Already seeded in `seeds/automotive-layer-architecture.md`:
- Android Auto / CarPlay support
- Operis read aloud (Wilson voice)
- Voice zip navigation
- Audio-only workout cueing for car/commute

### Games and Puzzles

The 🟡 Fun Color domain hosts interactive content:
- **Daily puzzle** — a small cognitive challenge tied to the day's Order. Logic puzzles for ⛽ Strength days. Pattern recognition for 🦋 Hypertrophy days. Memory games for 🐂 Foundation days.
- **Community challenges** — time-limited collaborative goals. "Community goal: visit 500 unique zip codes this week."
- **Cross-zip scavenger hunts** — exploration-driven games that reward visiting specific zip codes in sequence.
- **Skill mini-games** — small interactive exercises tied to the 56 skills in the character progression system. Quick, phone-friendly, 30-second interactions.

Games are never mandatory. They don't gate content. They contribute to vial levels (🟡 Exploration stat) and provide engagement variety.

---

## Section 5 — The Library

### The Always-There Resource

Ppl± is, at its core, a library. Not a library in the "content marketing" sense. A library in the civic sense — a public resource that's always available, always free (within subscription), always growing, always honest.

**Library wings (mapped to Axis floors):**

| Wing | Floor | What's On The Shelves |
|------|-------|----------------------|
| 🏛 Reference | Firmitas | Exercise library (2,085 entries), workout cards (1,680), technique guides, form references |
| 🔨 Tools | Utilitas | Calculators, timers, converters, exercise swap engine, training log, export tools |
| ⌛ Almanac | Temporitas | Seasonal calendar, historical events (366 dates), astronomical data, training periodization calendar |
| 🐬 Forum | Sociatas | Community threads per zip code, shared training logs, discussion boards |
| 🌹 Personal | Venustas | User's own training history, personal records, notes, saved rooms, vial history |
| 🪐 Archive | Gravitas | Cosmograms (42 decks), deep educational content, cross-references, the "why behind the what" |

The library is the city. The city is the library. Every zip code is a room in the library with 6 floors of depth.

### Content Pipeline

Content enters the library through:
1. **Generated workouts** — 1,680 cards, the foundation layer
2. **Operis editions** — daily editorial, growing archive
3. **Cosmograms** — deep research per deck, growing over time
4. **Community contributions** — user-generated content on community floors
5. **Almanac accretion** — historical events, seasonal content, calendar data
6. **Exercise knowledge** — 2,085 exercise content files, growing
7. **Life domain content** — the broader copilot content, growing by domain

The library never shrinks. Content accretes. The system gets richer over time. This is the civic library model — every book added makes the library more valuable for everyone.

---

## Section 6 — For Everyone

### Universal Accessibility

Ppl± is designed to work for anyone, anywhere in the world.

**Language:** English first (publication standard), with architecture designed for future localization. The SCL emoji system is language-agnostic — the 61 emojis work in any language.

**Physical accessibility:** Screen reader support. High contrast mode. Reduced motion mode. Large text mode. The HUD composition adapts to accessibility settings without losing its architectural grammar.

**Economic accessibility:** Tier 1 ($10/month) includes all core features. Free tier includes the Operis and limited room access. The subscription is the gym membership, not a paywall on each exercise.

**Cultural accessibility:** No cultural assumptions in content. No Western-centric holidays as defaults. Regional content is opt-in. The publication standard ensures respectful, inclusive framing for all topics.

**Device accessibility:** Works on any phone, tablet, or computer with a web browser. No app store lock-in. Progressive Web App (PWA) capabilities for offline access to saved rooms.

### The r/outside Principle

r/outside demonstrates that framing real life as a game makes it easier to discuss difficult things. "I got the Depression debuff" is easier to type than "I have depression." The game frame creates a safe container for sincerity.

Ppl± adopts this principle carefully:
- The character progression system provides a vocabulary for self-reflection
- Vial levels make abstract concepts (balance, neglect, growth) visible and concrete
- House identity gives users a framework for understanding their tendencies
- None of this is mandatory. Users who want a workout app get a workout app.
- Users who want a life framework find one waiting when they're ready

The framing is informational, not therapeutic. Ppl± is a library, not a clinic. It provides frameworks, not diagnoses.

---

## Section 7 — The Grandfather's Almanac

### What This Feels Like

The best way to understand the copilot experience: imagine a grandfather who is a farmer, a coach, a librarian, and a craftsman. He builds you something when you turn 18.

It's a leather-bound book that's also somehow a phone app. It has:
- A daily page with what's relevant today (the Operis)
- A workout section that knows your body (the zip code system)
- A calendar that tracks seasons, not just dates (the almanac)
- A section for each area of life where he's jotted useful frameworks (life domains)
- Pages that fill in as you use them (progressive disclosure)
- Easter eggs — little jokes, hidden connections, things he put in knowing you'd find them someday
- A character sheet that updates as you grow (the vial system)
- Space for your own notes at every page (personal floor)
- A community bulletin board at the back (community floor)
- An index that connects everything to everything (the navigation graph)

It's not flashy. It's not trying to impress. It's trying to be useful every single day for the rest of your life. And the more you use it, the more useful it becomes, because it learns your patterns and grows its content.

That's Ppl±.

---

## Section 8 — What This Is Not

- **Not a social media platform.** No feed. No likes. No follower counts. No viral mechanics. Community exists at zip code addresses, not in a timeline.
- **Not a gamification layer on top of real life.** The progression system reflects real engagement, not arbitrary points. The vials show real balance, not manufactured scores.
- **Not a replacement for professional services.** Career guidance is informational, not consulting. Financial literacy is educational, not advisory. Health content is supplemental, not medical.
- **Not a data harvesting operation.** See `seeds/data-ethics-architecture.md`. Full export. Full deletion. No tracking. No selling.
- **Not trying to maximize screen time.** The anti-addiction architecture (`seeds/exploration-immersion-architecture.md` Section 9) actively limits engagement when appropriate.
- **Not a one-shot vibe-coded app.** This is a cathedral built over decades by its architect. Every brick is placed with intention. The codebase IS the blueprints.

---

## Section 9 — The Build Path

### From Here to There

The path from today's MVP (1,680 workout cards + web app) to the full copilot platform:

**Already built:**
- 1,680 workout cards (the foundation)
- Web app scaffold (Next.js, auth, payments, logging, rooms)
- SCL addressing system (the universal routing key)
- Content type registry (109 types × 6 axes)
- Weight vector system (61 dimensions per zip code)
- Exercise library (2,085 entries)
- Rotation engine (deterministic daily suggestions)
- Navigation graph (6,720 edges connecting rooms)

**In the seeds (architecture planted, not built):**
- Character progression (this seed + heros-almanac-v8)
- Home screen composition (home-screen-architecture)
- Exploration/immersion layer (exploration-immersion-architecture)
- Operis editorial pipeline (4 prompt pipeline)
- Wilson voice identity
- Automotive layer
- Data ethics framework
- Stripe integration

**Future layers (the broader copilot):**
- Life domain content pipeline
- App integrations (health, calendar, music)
- Games and puzzles system
- Localization framework
- PWA offline capabilities
- Community moderation tooling

Each layer builds on the last. Nothing jumps ahead. The workout is the foundation. The city grows around it. The copilot emerges from the city.

---

## Open Questions

1. **Life domain content sourcing.** Who writes career guidance, financial literacy, civics content? AI-generated from prompts? Human-authored? Community-contributed? Partnership with NPR/PBS-aligned organizations?
2. **Integration API design.** How do third-party integrations authenticate and exchange data? OAuth2? Webhooks? Direct API?
3. **Localization priority.** Which languages after English? By user demand? By global fitness market size?
4. **Game design capacity.** Who designs the puzzles and mini-games? Is this a separate creative track?
5. **Content moderation at scale.** As community floors grow, what moderation model applies? Community-elected moderators? Automated flagging? Jake-reviewed? (This connects to Session L blocker.)
6. **Revenue scaling.** As life domains expand, does the pricing model change? Higher tiers? Domain-specific add-ons? Or everything stays in the base subscription?
7. **Grandfather voice.** How does the "grandfather's gift" principle translate to UI copy, onboarding language, error messages? This needs a voice and tone guide beyond the publication standard.
8. **Distraction limit configuration.** How granular? Per-mode? Per-feature? User-defined schedules? Defaults that work for most?
9. **Cross-device priority.** PWA first? Native apps eventually? Browser-only for desktop?
10. **The 100-year question.** What does Ppl± look like when Jake is no longer building it? How does the architecture ensure continuity beyond its creator?

---

🧮
