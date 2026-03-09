# Party Formation Engine

**Planted:** 2026-03-09
**Status:** SEED
**Depends on:** Guild Campaign Architecture, City Compiler (guild alignment), Rotation Engine
**Blocks:** Nothing

---

## What This Is

A weekly party formation system that assembles 12-person groups from across the guild network. One member from each of the 12 Houses. Total strangers in a random party for one week. The formation is deterministic (same inputs = same output), but the inputs rotate weekly so parties are always fresh.

---

## Formation Rules

### The 12-Seat Rule

Every party has exactly 12 seats — one per House. This guarantees:
- Maximum diversity of training styles within every party
- No guild can dominate a party
- Every member encounters someone whose training philosophy is their opposite

### Seat Assignment

```
Seat 1:  📍 The Architects
Seat 2:  🧲 The Receivers
Seat 3:  🧸 The Carriers
Seat 4:  👀 The Observers
Seat 5:  🥨 The Extenders
Seat 6:  🤌 The Executors
Seat 7:  🚀 The Launchers
Seat 8:  🦢 The Layerers
Seat 9:  🪵 The Anchors
Seat 10: 🐋 The Conductors
Seat 11: ✒️ The Scribes
Seat 12: 🦉 The Interpreters
```

### Selection Algorithm

```
1. Input: week_start_date, all active users with guild assignment
2. For each guild, sort eligible members by:
   a. Bloom level (prefer higher — more engaged)
   b. Recency of last session (prefer recent — active users)
   c. Party history (prefer users not recently in a party together)
3. Deterministic shuffle using hash(week_start_date + guild_id) as seed
4. Sequential assignment: take first available from each guild bucket
5. Overflow: if a guild has fewer available members than needed parties,
   some parties get a "wild card" seat — filled by secondary guild alignment
6. Output: list of 12-person party assignments for the week
```

The algorithm is deterministic: same week + same user pool = same parties. But the weekly rotation means no two consecutive weeks produce the same parties.

### Eligibility

A user is eligible for party formation if:
- They have logged at least 1 session in the past 14 days (active)
- They have a resolved guild alignment (requires at least 3 logged sessions total)
- They have not opted out of party formation for this week

Users who are inactive or new get a "solo quest" track instead — they can still participate in individual quests but are not assigned to a party.

---

## Party Lifecycle

```
Sunday 00:00 UTC  — Party formation runs. Members notified.
Monday            — Party quest board unlocked. Members can see each other's profiles.
Monday-Saturday   — Quest window. All party and individual quests active.
Sunday 23:59 UTC  — Week ends. Party dissolved. Scores tallied.
```

### What Party Members Can See About Each Other

- Display name (not real name unless opted in)
- Guild alignment (primary house)
- Current bloom level (0-5)
- Most-visited Order and Type (general training character)
- Campaign octave progress

### What They Cannot See

- Specific workout logs
- Weight/load data
- Personal notes
- Real identity
- Location

Privacy is structural, not a setting. The system architecturally cannot expose what it does not collect.

---

## Party Communication

Parties do NOT get a chat system. No messaging. No DMs.

Instead, communication is through action:
- Members can see when another member completes a quest (event notification)
- Members can "signal" a zip code — marking it as a suggestion for the party (one signal per day)
- Members can "salute" another member's completed quest (one-tap acknowledgment, no text)

This is deliberate. The party is a cooperation structure, not a social network. Strangers cooperate through shared objectives and parallel action, not conversation.

---

## Rotational Friend Circles (Pod Extension)

Over time, the system tracks which party members you've been grouped with and how often your quests overlapped. After 3+ co-assignments, the system may suggest a "pod" — a persistent small group (3-5 people) that persists across campaigns.

Pods are opt-in. They provide:
- Persistent party quest bonus when multiple pod members are in the same weekly party
- Shared campaign history
- A small, stable social anchor within the larger rotating party system

Pods form organically from repeated party assignment, not from user search or friend requests.

---

## Wild Card Seats and Asymmetric Parties

When a guild has fewer active members than needed:

**Wild Card Rule:** The empty seat is filled by a member whose secondary guild alignment matches the empty House. Their primary guild already has a seat filled, but their secondary alignment places them in the unfilled seat.

This means some users may occupy a seat that is their secondary (not primary) alignment. This is by design — it introduces slight unpredictability and rewards well-rounded training.

If even secondary alignment cannot fill a seat, the party runs with 11 members. The missing seat's quest slot becomes a "ghost quest" — any member can claim it for bonus credit.

---

## Relationship to Scoring

Party quest completion feeds into the octave scoring system (see guild-campaign-architecture.md):
- Individual quest completion: +1 toward personal octave
- Party quest completion: +1 toward personal octave AND +0.5 toward guild octave
- Full quest board (TikTok board): +2 toward personal octave
- Party-wide coordination (all 12 complete same quest): +1 toward guild octave

---

## Open Questions

- Should party formation happen weekly or at campaign boundaries (every 35 days)?
- Should users be able to "re-roll" their party once per campaign (at a cost of 1 octave point)?
- Should there be a "rivals" mechanic where two parties are paired for head-to-head comparison?
- What is the minimum active user count for party formation to activate? (12? 24? 120?)
- Should pods have a maximum size to prevent clique formation?

---

## Architectural Notes

- Party formation is a pure function: f(date, user_pool) → party_assignments
- No state mutation. The assignment is computed fresh each week from current data.
- Party data is ephemeral — stored for campaign scoring, archived after 35-day cycle
- Guild alignment is read from city_compiler.py's resolve function
- The deterministic shuffle ensures reproducibility for debugging and auditing
- No real-time infrastructure needed. Everything is batch-computed at week boundary.
