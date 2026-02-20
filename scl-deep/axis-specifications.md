---
source: Axis Specifications — Dual Layer Reference
created: 2026-02-20
status: WORKING DRAFT — dual-layer framework established, detail to be filled
integration-target: scl-directory.md (Axis section), html/design-system/axes/, html/floors/
notes: |
  This document specifies the 6 Axes across both their functional layers:
  Layer 1 (In-Workout): Exercise selection bias, ranking logic, character
  Layer 2 (App-Level): Content space, navigation floor, card presentation
  Both layers are true simultaneously. The emoji holds both.
  This replaces the previous stub file.
---

# Axis Specifications — Deep Reference

## Dual-Layer Framework

The 6 Axes operate on two layers simultaneously:

**Layer 1 — In-Workout (Exercise Character)**
Inside a zip code, the Axis biases exercise selection. It ranks exercises by character without excluding them. A 🏛 Basics workout prioritizes barbells and bilateral movement. A 🌹 Aesthetic workout prioritizes isolation and mind-muscle connection. This layer is fully operational in card generation today.

**Layer 2 — App-Level (Content Floor)**
Outside the workout, at the app level, each Axis is a distinct content space — a floor of the building. The workout card is the universal object that appears on every floor, contextualized differently by which floor presents it. This layer is architectural specification for Phase 4/5.

## The Vitruvian Origin Framework

Vitruvius wrote in *De Architectura* that good architecture requires three qualities:
- **Firmitas** — structural soundness, durability
- **Utilitas** — practical function, utility
- **Venustas** — aesthetic beauty, delight

Jake Berry identified three additional dimensions that architecture — and training — also require:
- **Gravitas** — the weight of challenge and consequence
- **Temporitas** — the dimension of time and rhythm
- **Sociatas** — the social dimension, building for and with others

Together, the 6 Axes form a complete framework for evaluating any exercise, any workout, any building, and any app experience.

## The 6 Axes — Complete Specification

### 🏛 Firmitas (Basics)

**Vitruvian principle:** Structural soundness. Durability. The load-bearing wall.

**Layer 1 — In-Workout:**
- Ranking axis (ranks exercises, does not exclude)
- Priority stack: Barbell > dumbbell. Bilateral > unilateral. Compound > isolation. Classic > novel.
- Surfaces: Time-tested fundamentals. The exercises that have anchored training for decades.
- Axis test: Would someone feel this axis without being told? Yes, if the exercises are the barbell staples.
- Operator pair: 📍 pono (preparatory — place, position) / 🤌 facio (expressive — execute, perform)

**Layer 2 — App-Level:**
- Floor identity: The front page. Navigation hub. System map. Full analytique.
- Content: 42-deck grid, 4-dial navigator, quick-view zip lookup, today's default zip, featured workout
- Card presentation: Thumbnail in grid. Position in the system. Structural overview.
- Visual character: Clean, structural, load-bearing. The lobby. Minimal ornament, maximum clarity.

**Operator pair behavior at app level:**
- 📍 pono months (January, default): Firmitas as home base feels positional, foundational, setting-up
- 🤌 facio months (June, default): Firmitas as home base feels active, executing, productive

---

### 🔨 Utilitas (Functional)

**Vitruvian principle:** Practical function. Utility. Things that work.

**Layer 1 — In-Workout:**
- Ranking axis
- Priority stack: Unilateral > bilateral. Standing > seated. Free weight > machine. Ground-based > bench-based.
- Surfaces: Athletic-transfer movements. Exercises that serve function beyond the gym.
- Axis test: Would someone feel this axis without being told? Yes, if the exercises feel athletic and practical.
- Operator pair: 🧸 fero (preparatory — carry, transfer) / 🥨 tendo (expressive — extend, push limits)

**Layer 2 — App-Level:**
- Floor identity: Tools. Calculators. Settings. Help. Utility.
- Content: Exercise library browser, 1RM calculator, macro calculator, deck builder, settings, account management, payment, support, bug reports, feature requests, help documentation
- Card presentation: Raw data. Editable parameters. Deck builder input. The card as material to work with.
- Visual character: Functional, no-nonsense. The workshop. Tools have visible affordances.

---

### 🌹 Venustas (Aesthetic)

**Vitruvian principle:** Beauty and delight. The personal.

**Layer 1 — In-Workout:**
- Ranking axis
- Priority stack: Isolation > compound. Cable/machine > barbell. Feeling > load.
- Surfaces: Mind-muscle connection. Full ROM. Feel over force.
- In 🖼 Restoration context: lens turns inward — pelvic floor, psoas, diaphragm, deep hip structures. The aesthetic lens becomes somatic.
- Operator pair: 👀 specio (preparatory — inspect, observe) / 🦢 plico (expressive — fold, layer, superset)

**Layer 2 — App-Level:**
- Floor identity: Personal library. Trophy case. Journal. Private space.
- Content: Workout history, PRs, streaks, milestones, saved workouts, personal notes per zip, journal, personal exercise library with logged data, ± superscript/subscript in full
- Card presentation: Personal history overlay. ± boxes filled. Notes from previous visits visible. Room Bloom most visible here.
- Visual character: Warm, personal, reflective. Your room. Private by default. The mirror.

---

### 🪐 Gravitas (Challenge)

**Vitruvian principle:** Weight and seriousness. Consequence.

**Layer 1 — In-Workout:**
- Ranking axis
- Priority stack: Hardest variation the person can control. Deficit, pause, tempo, bands/chains, unstable, stricter execution.
- Surfaces: The most demanding version of any movement. Scales to the individual.
- Operator pair: 🪵 teneo (preparatory — hold, anchor, persist) / 🚀 mitto (expressive — launch, deploy, send)

**Layer 2 — App-Level:**
- Floor identity: Challenge board. Benchmarks. Competition. Stakes.
- Content: Weekly challenges, benchmark tracking, goal setting, character creator, live workouts, leaderboards (opt-in), testing protocols, community challenges, competition brackets
- Card presentation: Challenge framing. Benchmark comparison. Leaderboard context. The card has stakes.
- Visual character: Heavy, serious, arena-like. You don't wander here casually. Darker palette, stronger contrast.

---

### ⌛ Temporitas (Time)

**Vitruvian principle:** Rhythm and time.

**Layer 1 — In-Workout:**
- Context axis (enables protocols, does not rank exercises)
- Enables: EMOM, AMRAP, density blocks, timed sets, time trials, TUT, steady state, zone work
- Protocol depends on Order × Color: ⌛🔴 = density/AMRAP. ⌛⚪ = meditative holds. ⌛🏟 = time trials. ⌛🔵 = EMOM.
- Operator pair: 🐋 duco (preparatory — orchestrate, conduct) / ✒️ grapho (expressive — write, document, record)

**Layer 2 — App-Level:**
- Floor identity: The Almanac. Calendar. Seasonal content. Schedule.
- Content: Personal workout queue, calendar views, 12-month Operator visualization, Farmer's Almanac content (seasonal food/lifestyle/rhythm), to-do lists, schedule keeper, training cycle planning, historical pattern visualization
- Card presentation: Calendar position. Before/after context. Seasonal tone overlay. The card lives inside time.
- Visual character: Rhythmic, flowing, clock-aware. The sundial in the courtyard. Temporal visualizations.

---

### 🐬 Sociatas (Partner)

**Vitruvian principle:** Togetherness. Society.

**Layer 1 — In-Workout:**
- Context axis (enables social exercise selection)
- Enables: Spottable, alternating, synchronized, competitive, assisted, station rotation, scalable load, teachable
- Surfaces exercises that work with another person present. Machine work deprioritized.
- Operator pair: 🧲 capio (preparatory — receive, assess, intake) / 🦉 logos (expressive — reason, analyze, interpret)

**Layer 2 — App-Level:**
- Floor identity: Community. Social layer. The public square.
- Content: Community boards per zip code, discussion threads, friend groups (dolphin pods), Junction community voting, shared challenges, training partner finder, user-submitted modifications, community seasonal content, social feed
- Card presentation: Community overlay. Other people's modifications. Votes. Discussion. The card belongs to everyone who's used it.
- Visual character: Open, communal, conversational. The agora. Activity and voices.

## Interplay Between Layers

The dual-layer system means the Axis dial in the 4-dial navigator does double duty:
- Spinning the Axis dial inside a workout changes exercise character
- Spinning the Axis dial at the app level changes which floor you're standing on

These are not separate systems. They are the same principle at different zoom levels. Firmitas is structural soundness whether you're selecting exercises or navigating the app. Venustas is beauty whether you're feeling a muscle contraction or looking at your personal trophy case. The metaphor holds all the way up and all the way down.

## HTML Architecture Implications

The `html/` directory needs expansion to account for the floor system:

```
html/
├── floors/
│   ├── firmitas/     — Front page, navigation, system map components
│   ├── utilitas/     — Tools, calculators, settings components
│   ├── venustas/     — Personal library, history, journal components
│   ├── gravitas/     — Challenge board, benchmark, competition components
│   ├── temporitas/   — Almanac, calendar, seasonal content components
│   └── sociatas/     — Community, social, discussion components
├── design-system/
│   └── axes/         — CSS per axis (now serves both workout and floor styling)
└── components/
    └── card-shell.html  — Shared card shell with per-floor presentation variants
```

## Open Questions

- Same as listed in seeds/axis-as-app-floors.md — see that file for navigation and routing questions.
- How does Layer 1 (in-workout) interact with Layer 2 (app-level) when the user is INSIDE a workout card? Does the floor context persist, or does the workout card become its own space?
- Should the Axis deep spec eventually include interaction design specifications per floor, or should that live in a separate UX document?
