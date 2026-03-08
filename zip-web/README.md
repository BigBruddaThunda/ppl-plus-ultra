# Zip-Web — Ppl± Navigation Graph

The zip-web is a relational navigation layer connecting all 1,680 Ppl± workout zip codes into a traversable graph. Every zip code is a hub. Every hub has exactly 4 outgoing directional edges (N/E/S/W). Each edge points to a zip code of a different Type. The hub plus its 4 neighbors form a **pod** — 5 workouts covering all 5 Types.

The zip-web is independent of the Almanac calendar rotation. It is a parallel navigation system.

---

## The Pod

A pod is one hub zip plus 4 directional neighbors:

```
Hub: ⛽🏛🛒🔵 — Heavy Classic Presses

N (Progression): ⛽🏛🪡🔵 — Heavy Classic Pulls
E (Balance):     ⚖🔨🍗🔵 — Single-Leg Correction Day
S (Recovery):    🖼🌹➖⚪  — Breath as Anchor
W (Exploration): 🌾⌛➕🟣  — Power Flow Precision
```

Every pod covers all 5 Types (🛒🪡🍗➕➖) across hub + 4 neighbors. A pod is a self-contained training week.

---

## The Type Exclusion Rule

This is a hard constraint. Non-negotiable.

If the hub's Type is X:
- N, E, S, W must each carry a **different** Type from the remaining 4
- All 4 non-hub Types appear **exactly once** across N/E/S/W
- The hub Type **cannot appear** in any directional slot

---

## The 4 Directional Characters

**N — Progression**
The workout that builds directly on what the hub created. It capitalizes on the neural, muscular, or metabolic state the hub zip produced. N is what a smart trainer programs next if the goal is forward momentum.

**E — Balance**
The workout that addresses what the hub neglected or exposed. If the hub was bilateral and heavy, E might be unilateral and corrective. If the hub was intense, E offers equilibrium. E brings the system back toward balance.

**S — Recovery-Aware**
The workout that respects accumulated fatigue. S assumes some depletion from the hub. It offers productive training that lets stressed systems breathe while building capacity elsewhere. S tends toward lower CNS demand and softer session formats relative to the hub.

**W — Exploration**
The least obvious connection. W opens a new training vector — a different Order-Axis combination the user wouldn't naturally gravitate toward. W is the trainer's "trust me on this one." It expands total capacity by creating novel stimulus and preventing the web from becoming predictable.

---

## How to Read a Pod Entry

```markdown
⛽🏛🛒🔵 — Heavy Classic Presses

Fatigue Signature: CNS: 4 | Tissue: Chest/FDelts/Triceps | Density: 2 | Character: Bilateral/Barbell/Stable

| Dir | Zip | Why |
|-----|-----|-----|
| N (Progression) | ⛽🏛🪡🔵 | [coaching rationale] |
| E (Balance)     | ⚖🔨🍗🔵 | [coaching rationale] |
| S (Recovery)    | 🖼🌹➖⚪  | [coaching rationale] |
| W (Exploration) | 🌾⌛➕🟣  | [coaching rationale] |

Pod Types: 🛒 (hub) + 🪡 + 🍗 + ➖ + ➕ = 🛒🪡🍗➖➕ ✓
```

---

## Relationship to the Almanac

The Almanac (seeds/default-rotation-engine.md) generates a daily default zip from three interlocking gears: Order by weekday, Type by rolling 5-day cycle, Axis by monthly operator. The zip-web is a separate navigation path — pick any zip, see 4 options, follow the web.

The two systems are parallel and compatible:
- A user following the Almanac gets a daily zip. They can check that zip's N/E/S/W for alternatives.
- A user ignoring the Almanac can enter the web at any zip and navigate by pod connections.
- The systems never conflict — both produce valid standalone workouts.

---

## File Index

```
zip-web/
├── README.md               — This file
├── zip-web-rules.md        — Complete specification for neighbor selection
├── zip-web-signatures.md   — Fatigue profiles for all 1,680 zip codes
├── zip-web-registry.md     — Index of all 1,680 zips with derived metadata
└── zip-web-pods/
    ├── deck-07-pods.md     — Prototype: 40 fully populated pods (⛽🏛 Strength × Basics)
    ├── deck-01-pods.md     — Stub awaiting Ralph Loop population
    ├── deck-02-pods.md
    ├── ...
    └── deck-42-pods.md
```

The Ralph Loop automation infrastructure for populating the remaining 41 decks lives in `scripts/ralph/`. The `/ralph` Claude Code skill is in `.claude/skills/ralph-loop.md`.

---

## Traversal

**Weekly pod rotation:**
Day 1 — Hub
Day 2 — Pick N, E, S, or W based on how you feel
Day 3 — Pick from remaining 3 directions
Day 4 — Pick from remaining 2
Day 5 — The last direction

**Infinite traversal:**
Do the hub today. Pick one direction for tomorrow. Tomorrow's zip is the new hub with its own 4 fresh directions. The graph is infinitely traversable.

**Overlap:**
Different hubs can share the same neighbor zip. If two hubs both point to the same zip at S, that zip is simply a popular recovery anchor. There is no symmetry requirement — A pointing to B does not require B to point back to A.

---

## Status

- Deck 07 (⛽🏛 Strength × Basics): **40 pods populated** — prototype quality bar
- Decks 01–06, 08–42: **Stub files only** — awaiting Ralph Loop population

Run `/ralph` to populate one deck per iteration.
