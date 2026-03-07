# KERNEL.md — SCL Generative Seed

This is the compressed root of the Semantic Compression Language.
It gives any AI agent enough context to understand and use the system across any project.
For project-specific rules: that project's `CLAUDE.md`.
For PPL± full specification: `scl-directory.md`.
For Graph Parti full specification: `SCL.md` at github.com/BigBruddaThunda/Graph-Parti.

---

## THE LANGUAGE

SCL — Semantic Compression Language — is an addressing system built from 61 emojis.

**Polysemic:** each emoji holds multiple valid meanings. Context determines which applies.
**Semantic:** emojis carry meaning, not decoration. They are addresses for ideas.
**Language:** grammar exists. Rules for how symbols combine into meaningful compounds.

One language. Every context — code, conversation, documentation, logging, thought.
Each project extends SCL with domain-specific vocabulary. The kernel is the mother tongue.

---

## THE ZIP CODE SYSTEM

A zip is a semantic address. Four positions. Color always terminates.

```
┌───────┬───────┬───────┬───────┐
│ Dial 1│ Dial 2│ Dial 3│ Color │
│ any   │ any   │ any   │ fixed │
└───────┴───────┴───────┴───────┘
```

Dials 1–3 can hold any emoji from any non-Color category. Color closes the thought.

**Standard 4-dial zip** (Graph Parti default): Order · Type · Modifier · Color
**District 6-dial zip** (parent containers): Order · Type · Axis · Block · Modifier · Color
**PPL± dialect zip**: Order · Axis · Type · Color (valid project override)

Project zip ordering is defined in each project's `CLAUDE.md`. The kernel defines the grammar. Projects define the dialect.

**Partial zips are valid:**

```
🟡                ← color only (status marker, bullet, state)
🐂🟡              ← order + color (phase + state)
🐂🧲🟡            ← order + type + color (phase + action + state)
🐂🧲🛒🟡          ← full zip (phase + action + direction + state)
🏛🧈🔵            ← axis + block + color (lens + container + state)
♨️🟢              ← block + color (container + state)
```

**Defaults for district headers:** 📍 for Type (locator), ➕ for Modifier (base).

---

## THE 5 CORE PRINCIPLES

1. **Emoji precedes word. Always.** `🐂 init` ← correct. `init 🐂` ← incorrect. The emoji anchors. The word contextualizes.
2. **Context determines meaning.** Same emoji, different situation = different valid meaning. There is no single correct interpretation.
3. **Grammar guides, doesn't police.** If something looks wrong by strict grammar but makes sense in context, context wins.
4. **Color terminates.** Every complete thought ends with a color. Color in zip-with-content = always last position.
5. **Partial zips are valid.** Not every zip needs all four positions. Incomplete addresses are real addresses.

---

## THE 61 SCL EMOJIS ACROSS 7 CATEGORIES

### CATEGORY 1: ORDERS (7) — Developmental Phase

Orders mark where something is in its lifecycle. Seven classical architectural phases.

| Emoji | Name | Phase | Abstract Meanings |
|-------|------|-------|-------------------|
| 🐂 | Tuscan | 1 | init, declare, define, setup, begin |
| ⛽ | Doric | 2 | validate, test, assert, check, verify |
| 🦋 | Ionic | 3 | iterate, loop, accumulate, build, grow |
| 🏟 | Corinthian | 4 | execute, run, perform, output, render |
| 🌾 | Composite | 5 | combine, merge, integrate, apply, use |
| ⚖ | Vitruvian | 6 | calibrate, adjust, balance, refactor, tune |
| 🖼 | Palladian | 7 | return, complete, finalize, view, scope |

Orders answer: **"What phase is this?"**

In conversation: "I'm still at 🐂 with this — just naming the pieces."
In code: `// 🏟 execute — run main logic`
In documentation: headers that carry phase meaning.

Projects define what each phase *means in their domain*. See Polysemic Domain Mapping below.

---

### CATEGORY 2: TYPES (12) — Action Verbs

Types are the verb. The action. What is happening.

| Emoji | Root | Core Meanings |
|-------|------|--------------|
| 🧲 | capio | capture, get, receive, contain, accept |
| 🐋 | duco | orchestrate, lead, conduct, produce, arrange |
| 🤌 | facio | act, make, execute, create, perform |
| 🧸 | fero | channel, carry, transfer, pass, move |
| ✒️ | grapho | write, record, inscribe, document, mark |
| 🦉 | logos | parse, reason, evaluate, calculate, interpret |
| 🚀 | mitto | dispatch, send, emit, launch, commit |
| 🦢 | plico | compress, fold, layer, nest, merge |
| 📍 | pono | set, place, position, assign, establish |
| 👀 | specio | inspect, observe, query, read, examine |
| 🥨 | tendo | span, stretch, extend, reach, push |
| 🪵 | teneo | pause, hold, retain, persist, anchor |

Types answer: **"What action is happening?"**

The Latin/Greek roots are mnemonics: *capio* = to take, *mitto* = to send, *specio* = to look.

In code: `// 🧲 capture input` `// 🚀 dispatch to API`
In conversation: "Let me 🦉 parse what you said." "Time to 🚀 dispatch."

---

### CATEGORY 3: MODIFIERS (5) — Direction and Operation

Modifiers mark which way the action flows, or what operation applies.

| Emoji | Name | Direction/Op | Abstract Meanings |
|-------|------|--------------|-------------------|
| 🛒 | Push | outward | output, emit, export, send, write |
| 🪡 | Pull | inward | input, receive, import, read, fetch |
| 🍗 | Legs | below | foundation, base, support, dependency |
| ➕ | Plus | increase | add, append, extend, include |
| ➖ | Ultra | decrease | subtract, remove, reduce, exclude |

Modifiers answer: **"Which way? What operation?"**

Used to specify direction in a zip: `🧲🪡` = capture input (pulling in). `🚀🛒` = dispatch output (pushing out).

**PPL± dialect note:** PPL± overloads these 5 emojis as Types (muscle-group domains: Push/Pull/Legs/Plus/Ultra). This is a valid polysemic project override — the 5 emojis occupy the Type position in PPL± zips rather than the Modifier position. Both are correct within their domain. See Polysemic Domain Mapping below.

---

### CATEGORY 4: AXES (6) — Dimensional Lenses

Axes mark which aspect or dimension you are examining. From Vitruvius: *firmitas, utilitas, venustas.*

| Emoji | Name | Latin Term | Question |
|-------|------|------------|----------|
| 🏛 | Firmitas | Structure | What IS it? Schema, type, model, shape. |
| 🔨 | Utilitas | Function | Does it WORK? Method, handler, utility. |
| 🌹 | Venustas | Beauty | Does it FEEL right? Style, render, display. |
| 🪐 | Gravitas | Weight | Does it MATTER? Value, priority, importance. |
| ⌛ | Temporitas | Time | WHEN? Async, delay, schedule, duration. |
| 🐬 | Sociatas | Society | WHO? Share, connect, sync, collaborate. |

Axes answer: **"Which aspect?"**

To examine something from multiple angles: 🏛 What's the structure? 🔨 Does it work? 🌹 Does it feel right?

---

### CATEGORY 5: COLORS (8) — State and Tone

Colors mark state, register, tone. **Colors always terminate.** They are the final position in any zip. A color alone is a complete statement.

| Emoji | Name | State | Abstract Meanings |
|-------|------|-------|-------------------|
| ⚪ | Eudaimonia | clear | honest, neutral, baseline, true |
| 🟡 | Play | exploring | sandbox, draft, idea, experimental |
| 🟠 | Connection | relational | collaborative, shared, warm |
| 🔴 | Passion | urgent | intense, priority, now, critical |
| ⚫ | Order | complete | done, archived, resolved, closed |
| 🟣 | Magnificence | significant | deep, breakthrough, important |
| 🔵 | Planning | structured | organized, methodical, specified |
| 🟢 | Growth | active | steady, progressing, building |

**Color as terminator:** `🐂🧲🛒🟡` = init capture output, exploring
**Color as standalone:** `🔴 This needs attention now.`
**Color as period:** End a thought stream with a color to mark its state.

---

### CATEGORY 6: BLOCKS (22) — Process Containers

Blocks are named containers inside a workflow or session. The name is fixed. The content is context-dependent by zip code.

**Four operational functions:**
- **Orientation** — Arriving, focusing, pointing intent
- **Access/Preparation** — Priming, activating, readying
- **Transformation** — Where the core work happens
- **Retention/Transfer** — Locking in, bridging forward

| Emoji | Name | Function | Abstract Role |
|-------|------|----------|--------------|
| ♨️ | Warm-Up | Orientation/Access | Prepare, ready |
| 🎯 | Intention | Orientation | Aim, target, set goal |
| 🔢 | Fundamentals | Access | Basics, patterns, rules |
| 🫀 | Circulation | Access | Flow, pulse, cycle |
| ▶️ | Primer | Access | Activate, trigger, start |
| ♟️ | Gambit | Access | Deliberate sacrifice for positional gain |
| 🪜 | Progression | Access/Transform | Ramp, climb, advance |
| 🧈 | Bread/Butter | Transformation | The main thing. Core work. Most volume. |
| 🎼 | Composition | Transformation | Arrange, compose, orchestrate |
| 🌎 | Exposure | Transformation | Reveal, discover, surface |
| 🎱 | ARAM | Transformation | Station-based loops, rotation |
| 🌋 | Gutter | Transformation | Crucible, strip, reduce to essentials |
| 🪞 | Vanity | Transformation | Mirror, reflect, show |
| 🗿 | Sculpt | Transformation | Shape, carve, form |
| 🛠 | Craft | Transformation | Skill, practice, hone |
| 🧩 | Supplemental | Transformation | Support, assist, secondary work |
| 🏖 | Sandbox | Transformation | Constrained exploration, safe experiment |
| 🏗 | Reformance | Transformation | Correct, fix, rebuild |
| 🪫 | Release | Retention | Discharge, let go, empty |
| 🧬 | Imprint | Retention | Lock in, encode, preserve pattern |
| 🔠 | Choice | Modifier | Bounded autonomy, select from valid options |
| 🚂 | Junction | Retention | Pivot, bridge to next, log forward |

---

### CATEGORY 7: SYSTEM (1)

| Emoji | Name | Meaning |
|-------|------|---------|
| 🧮 | SAVE | Commit, log, checkpoint, preserve. Every session ends here. |

---

## POLYSEMIC DOMAIN MAPPING

The same emojis mean different things per project. This is by design — polysemy is the point.

| Category | Abstract (Kernel) | PPL± (Fitness) | Graph Parti (Canvas) |
|----------|-------------------|----------------|---------------------|
| Orders | Developmental phases (init → validate → build → execute → integrate → calibrate → complete) | Periodization protocols — intensity, volume, rest, and CNS demand per phase | Classical architectural orders (Tuscan → Palladian) |
| Types | 12 Latin action verbs (🧲🐋🤌🧸✒️🦉🚀🦢📍👀🥨🪵) | 5 muscle-group domains (Push 🛒, Pull 🪡, Legs 🍗, Plus ➕, Ultra ➖) | 12 Latin action verbs — same as kernel |
| Modifiers | 5 direction/operation emojis (🛒🪡🍗➕➖) | Promoted to Types position (dial 3) | 5 direction/operation emojis — same as kernel |
| Colors | Abstract state/tone | Equipment tier and session format — includes tier-gated content access rules | Abstract state/tone — same as kernel |
| Zip order | Order · Type · Modifier · Color | Order · Axis · Type · Color | Order · Type · Modifier · Color |

**How to read this table:** The kernel defines the abstract default. A project's `CLAUDE.md` documents its overrides. When an agent reads a PPL± zip, it applies PPL± definitions. When it reads a Graph Parti zip, it applies Graph Parti definitions. Context always determines meaning.

**The PPL± Type overload:** PPL± promotes 🛒🪡🍗➕➖ from Modifiers to Types and uses the 12 Latin verbs as post-zip Operators (a bridge mechanism unique to PPL±). This is documented in `CLAUDE.md` and `scl-directory.md`. It is not a kernel-level pattern.

---

## THE RALPH LOOP

The Ralph Loop is the primary sorting and refinement process. Use it whenever raw context arrives as a pile and needs to become organized.

1. **Read** — Scan raw input from multiple angles. Do not filter yet. Just read.
2. **Identify** — Tag with minimal SCL. Which project? Obvious Order? Relevant emojis?
3. **Assign** — Route to correct project directory or `archideck/intake/`.
4. **Sort** — Place in the correct Color section of the Negotiosum (CONTRACTS.md).
5. **Refine** — Clean, connect, compress. Cross-check. Remove noise.
6. **Repeat** — The loop never ends. Each pass produces clearer signal.

The Ralph Loop applies to: raw ideas arriving in intake, session logs needing archiving, deck audits needing resolution, or anything that arrives as undifferentiated pile.

Leave unresolved items in 🧮 Save. Do not force a zip until the address is clear.

---

## THE 7+1 FILE STRUCTURE

Every project using SCL can organize its knowledge base into 7 Order files plus a scratchpad. This is the district file system.

| Order | File | Domain | Contains |
|-------|------|--------|----------|
| 🐂 | `🐂-tuscan.md` | Foundation | Core definitions, what things ARE, initialization |
| ⛽ | `⛽-doric.md` | Validation | Rules, constraints, what must be TRUE |
| 🦋 | `🦋-ionic.md` | Building | Features in progress, iterations, active work |
| 🏟 | `🏟-corinthian.md` | Execution | Runtime behavior, what HAPPENS, output layer |
| 🌾 | `🌾-composite.md` | Integration | Cross-system connections, collaboration flows |
| ⚖ | `⚖-vitruvian.md` | Calibration | Refinement, polish, tuning, rebalancing |
| 🖼 | `🖼-palladian.md` | Experience | What users see and feel, final presentation |
| 🧮 | `🧮-save.md` | System | Scratchpad, partial zips, unresolved items, tasks |

Projects are not required to use this structure. It is a natural expression of the 7 Orders as a filing system — intuitive, phase-aligned, and cross-project readable by any SCL-literate agent.

---

## ARCHITECTURAL PATTERNS

These patterns apply across all projects that use SCL as their operating language.

### Zip Codes as Semantic Addresses

The zip code is not a label. It is an address that encodes every relevant parameter of the content it points to. An agent reading a zip should be able to reconstruct the content constraints without reading the content itself.

- Partial zips are real addresses (incomplete, but valid)
- The same zip in two projects means different things — and that is correct
- A zip is simultaneously: location, query, tag, state, phase, and tone

### The Deck/Card/Room Metaphor

Used in PPL±; portable to any project with collections:
- **Deck** = a collection sharing two addressing dimensions
- **Card** = one zip code instantiated as a full content document
- **Room** = the user's live experience of a card (interactive, logged, personalized)

The metaphor scales: a deck is a neighborhood, a card is an address, a room is the interior.

### The Cosmogram

Every significant zip code can have a **cosmogram** — a deep identity document that goes beyond parameters to capture character, cultural context, symbolic weight, and resonance. The cosmogram is not the content. It is the identity of the address.

The cosmogram is the substrate for temporal content layers (like the PPL± Operis).

### The Operis

A temporal content layer that filters a cosmogram through current context (date, season, event, editorial angle) to produce time-stamped content at a specific address on a specific day. Projects define their own Operis cadence.

### SCL as Context Compression

SCL's core power: four characters encode a complete specification. The deeper power is fractal cross-reference — the same emoji carries meaning at every level of the system simultaneously.

🐂 is not just "Foundation." It is simultaneously:
- A developmental phase (the first of seven)
- A classical architectural order (Tuscan)
- A cognitive register (naming, not yet testing)
- A loading protocol in PPL± (≤65%, pattern learning)
- A commit marker in code (`// 🐂 init`)

One emoji. Multiple simultaneous meanings. That is the compression.

---

## NEGOTIOSUM CONTRACT SYSTEM

The Negotiosum is the active work board. It tracks all contracts across all projects. Live in `archideck/CONTRACTS.md`.

**Contract states:**
- `ACTIVE` — In progress this session
- `QUEUED` — Next in line, no blockers
- `PARKED` — Waiting on external dependency
- `COMPLETED` — Done, archived

**Each contract carries:**
- Scope — what this contract covers
- Current state — ACTIVE / QUEUED / PARKED / COMPLETED
- Next physical action — one sentence: what to do next
- Location — which project, which file, which branch
- Blockers — what is preventing progress (blank if none)

**Session rule:** Read `CONTRACTS.md` before any other file in a session. The switchboard tells you what is active. You work the active contract first. Do not freelance between contracts.

New contracts are added when new work is scoped. Completed contracts are archived. The Negotiosum does not carry history — only current state.

---

## AGENT SESSION START SEQUENCE

Every session, in this order:

1. Read `KERNEL.md` — the language. Ground yourself.
2. Read `archideck/CONTRACTS.md` — the switchboard. See what is active.
3. Determine which project and contract is the focus.
4. Read that project's `CLAUDE.md` — the operating rules for that domain.
5. Read that project's `whiteboard.md` — current task, session state.
6. Work the active contract.

Do not skip steps. Do not freelance. The switchboard determines the work. The CLAUDE.md determines the rules.

---

## INTAKE PROTOCOL

When raw ideas arrive — in any form, at any time — follow this protocol:

1. **Capture everything.** Do not filter. Do not discard. Fidelity first.
2. **Tag with minimal SCL.** Which project (if clear)? Obvious Order? Relevant emojis?
3. **Write to the intake directory.** Target: `archideck/intake/YYYY-MM-DD-[slug].md`
4. **Do not sort yet.** Intake stays in intake until the Ralph Loop is run.
5. **Note the intake.** Add one line to the active project's whiteboard: `intake: [slug] filed YYYY-MM-DD`.

The intake is the catch basin. The Ralph Loop is the sorter. They are separate operations.
Run intake fast. Run the Ralph Loop deliberately.

---

## BUILD PHILOSOPHY

**The bus must be clean, then spaghetti doesn't matter.**
Design the central authority (the bus) first. `KERNEL.md` is the bus for the language. Project `CLAUDE.md` files tap the bus; they do not replace it. Once the bus is clean, local variation is harmless.

**Architecture before implementation, always.**
A wrong parameter in a specification propagates through every downstream system. The cost of bad architecture compounds. The cost of slow architecture is one conversation.

**The kernel generates the system — it is the seed, not documentation of the system.**
An agent reading only `KERNEL.md` should be able to understand SCL grammar, read and write zip codes, sort context using the Ralph Loop, navigate the Archideck structure, and know where to find project-specific specs. The kernel is the beginning.

**Every project speaks SCL. Domain-specific vocabulary extends SCL, never replaces it.**
Graph Parti has districts and figures. PPL± has decks and cards. Story Engine will have acts and characters. All are extensions of the zip code grammar. None replace it.

**Parallel work across projects is the default, not the exception.**
The Archideck exists because multiple projects use the same language. The kernel enables parallel context without duplication. One agent can generate PPL± cards while another processes Graph Parti districts — both using the same SCL grammar, both reporting to the same Negotiosum.

---

## NAVIGATION POINTERS

| Need | Location |
|------|----------|
| Full project-agnostic SCL specification | `github.com/BigBruddaThunda/Graph-Parti` → `SCL.md` |
| PPL± full SCL specification (polysemic overrides, generation rules, validation) | `scl-directory.md` |
| PPL± operating instructions (generation workflow, exercise library routing, tonal rules) | `CLAUDE.md` |
| PPL± valid exercises | `exercise-library.md` |
| PPL± numeric zip aliases (emoji ↔ 4-digit address) | `seeds/numeric-zip-system.md` |
| Current project state and active tasks | that project's `whiteboard.md` |
| Cross-project contract switchboard | `archideck/CONTRACTS.md` |
| Universal agent operating instructions | `archideck/AGENT-CONTRACT.md` |
| Project index | `archideck/projects/README.md` |
| Shared cross-project tools | `shared/` |

---

61 emojis. Seven categories. One kernel. Every project extends from here.

🧮
