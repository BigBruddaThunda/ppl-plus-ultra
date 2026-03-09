# Guild Campaign Architecture

**Planted:** 2026-03-09
**Status:** SEED
**Depends on:** City Compiler (guild alignment), Operator Houses (12 guilds), Rotation Engine
**Blocks:** Nothing

---

## What This Is

A recurring competitive-cooperative event system built on the 12 Operator Houses (guilds). Every user belongs to a guild based on their workout history's weight vector alignment (resolved by city_compiler.py → guild alignment). Campaigns run on 35-day macro cycles tied to the rotation engine.

---

## The 12 Houses

Every user's cumulative weight vector (the centroid of all rooms they've visited, logged, and voted in) resolves to a primary guild via cosine similarity against the 12 operator profiles.

| House | Operator | Character |
|-------|----------|-----------|
| The Architects | 📍 pono | Planners, stance-setters, position-finders |
| The Receivers | 🧲 capio | Absorbers, eccentric specialists, catchers |
| The Carriers | 🧸 fero | Load-bearers, transfer agents, bridge-builders |
| The Observers | 👀 specio | Form analysts, quality inspectors, mirror-workers |
| The Extenders | 🥨 tendo | ROM pushers, limit-seekers, stretch artists |
| The Executors | 🤌 facio | Doers, concentric specialists, producers |
| The Launchers | 🚀 mitto | Explosive movers, max-effort deployers |
| The Layerers | 🦢 plico | Superset weavers, complexity folders |
| The Anchors | 🪵 teneo | Isometric holders, endurance persisters |
| The Conductors | 🐋 duco | Tempo architects, flow orchestrators |
| The Scribes | ✒️ grapho | Loggers, data documenters, PR recorders |
| The Interpreters | 🦉 logos | Analysts, movement-quality reasoners |

Guild assignment is not permanent. As a user's training evolves, their centroid shifts and their guild alignment can change. This is by design: the system reflects who you are training to become, not who you were.

---

## The 35-Day Campaign Cycle

Why 35 days: 7 Orders x 5 Types = 35 unique Order-Type combinations. One full rotation through the system.

### Campaign Structure

```
Day 1-7:    Week 1 — Scout Phase (individual quests)
Day 8-14:   Week 2 — Rally Phase (party quests unlock)
Day 15-21:  Week 3 — Siege Phase (inter-guild competition)
Day 22-28:  Week 4 — Harvest Phase (collection + scoring)
Day 29-35:  Week 5 — Festival Phase (rewards + guild standings)
```

### Quest Types

**Individual Quests (available all 35 days):**
- Visit a zip code you have never visited before
- Log a session in a zip code from a different Order than your last 3
- Complete a workout in all 5 Types within 7 days
- Log a session in a guild-hall zip code (the zip most similar to each operator)

**Party Quests (Week 2+ only, require party formation):**
- All 12 party members log sessions in the same deck within 48 hours
- Collectively visit all 8 Colors of a single Type within a week
- Complete a "Color Run" — one member per Color, all same Order and Type

**Guild Quests (Week 3+ only, guild-wide):**
- Guild members collectively visit every zip in a target deck
- Guild accumulates the most total logged sessions in a target Order
- Guild solves a riddle chain (see Easter Egg System)

---

## Scoring: The Octave System

Scores map to the 8-level octave (0-7), not arbitrary point totals.

```
Octave 0: Silent     — No participation
Octave 1: Whisper    — 1-2 quests completed
Octave 2: Murmur     — 3-5 quests completed
Octave 3: Voice      — 6-10 quests + 1 party quest
Octave 4: Call       — 11-15 quests + 2 party quests
Octave 5: Song       — 16-20 quests + guild quest participation
Octave 6: Chorus     — 21+ quests + guild quest completion
Octave 7: Anthem     — Maximum participation across all quest types
```

Individual octave feeds into guild octave (average of members). Guild octave determines campaign rewards.

---

## Rewards: Access, Not Currency

The system does not create a virtual economy. Rewards are access-based:

**Campaign Winners (top 3 guilds):**
- Unlock restricted zip codes for the next 35-day cycle
- Some zip code buildings are normally "closed" during certain periods. Winning guilds get access.
- Featured placement in Operis editions during the reward period
- Guild crest displayed on all member profiles

**Individual Rewards:**
- Bloom level boost (counts toward bloom transitions)
- Visited-zip credit for party members' logged sessions (social bloom)
- Campaign badge in workout history

**What rewards are NOT:**
- No virtual currency
- No purchasable advantages
- No pay-to-win mechanics
- No punishment for non-participation (you just don't get the bonus access)

---

## The TikTok Board (Weekly Quest Grid)

Inspired by streamer challenge boards. Each week, all party members share a 4x4 grid of mini-quests.

```
┌──────────┬──────────┬──────────┬──────────┐
│ Visit a  │ Log 3    │ Try a    │ Complete │
│ new zip  │ sessions │ new Type │ a Color  │
│          │ in 🔵    │          │ Run      │
├──────────┼──────────┼──────────┼──────────┤
│ Hit all  │ Log in   │ Visit    │ Read a   │
│ 5 Types  │ your     │ guild    │ library  │
│ this wk  │ anti-zip │ hall     │ entry    │
├──────────┼──────────┼──────────┼──────────┤
│ Log a    │ Party    │ FREE     │ Visit 3  │
│ session  │ member   │ SPACE    │ zips in  │
│ at 6am   │ co-log   │          │ same Axis│
├──────────┼──────────┼──────────┼──────────┤
│ Complete │ Log in   │ Visit    │ Earn     │
│ 🖼 rest │ all 7    │ partner  │ Octave 3 │
│ session  │ Orders   │ zip 🐬   │ this wk  │
└──────────┴──────────┴──────────┴──────────┘
```

Completing a row, column, or diagonal = bonus octave point.
Completing the full board = double bonus.

Grid is deterministically generated from the campaign date + guild hash. Every party sees a different board.

---

## Architectural Notes

- Guild alignment is computed by city_compiler.py (already built)
- Campaign cycle length (35 days) maps to the rotation engine's natural period
- Quest validation is event-sourced: every session log is an immutable event, quest completion is a projection
- No real-time multiplayer required. All interaction is asynchronous (log your session, the system checks completion)
- Party formation is handled by party-formation-engine.md (separate seed)
- Easter eggs are handled by easter-egg-system.md (separate seed)
- The octave scoring system can reuse the existing 8-level bloom architecture

---

## Open Questions

- Should guild assignment update in real-time or only at campaign boundaries?
- Should there be a "free agent" period between campaigns where users can see which guild they'd join?
- What is the minimum participation threshold for guild quest eligibility?
- How do new users (no training history) get assigned? Random? Or based on onboarding quiz?
- Should the quest grid be shared by all party members or personalized per member?

---

## Relationship to Other Seeds

- **party-formation-engine.md** — How the 12-person parties are assembled
- **easter-egg-system.md** — Hidden content scattered across zip codes
- **operis-architecture.md** — Campaign events can be featured in daily Operis
- **elevator-architecture.md** — Restricted zip access maps to the building/floor model
- **cosmogram-research-prompt.md** — Deep zip lore feeds quest narrative
