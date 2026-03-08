# Ppl± Systems Language Audit

Generated: 2026-03-04
Scope: All active documents cross-referenced against `scl-deep/systems-glossary.md`
Phase: B (read-only scan → patch map)

---

## SUMMARY

- Documents scanned: 40+
- Total instances flagged: ~125
- Glossary gaps identified: 8
- Priority patches (top 5 highest-frequency informal terms):
  1. "hook runs/fires automatically" → **inserter** (CLAUDE.md, whiteboard.md, 3+ seeds)
  2. "validation script/checklist checks" → **scan cycle** of **rungs** (CLAUDE.md, middle-math)
  3. "rotation repeats/cycles" → **oscillator** (default-rotation-engine.md, rotation-engine-spec.md, operis-architecture.md)
  4. "converting zip code to workout / generating from a zip" → **resolution** (CLAUDE.md, README.md, seeds)
  5. "EMPTY stubs can't be featured / if the card is EMPTY, skip it" → **fizzle** (operis-architecture.md, CLAUDE.md, operis-prompt-pipeline.md)

---

## INSTANCES BY DOCUMENT

---

### CLAUDE.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~repo structure | "Stub. Awaiting generation." | cache miss | §4 Resolution |
| ~repo structure | "Complete. Workout generated." | cache hit | §4 Resolution |
| ~generation sequence | "Rename the stub file to the complete filename" | resolution (completing the resolution of a cache miss) | §4 Resolution |
| ~4-dial zip section | "The constraint hierarchy when dials conflict: 1. ORDER 2. COLOR..." | priority stack | §4 Resolution |
| ~exercise library section | "All exercises used must come from exercise-library.md" | belt | §2 Data Flow |
| ~infrastructure section | "PostToolUse validation hook" and "SessionStart dashboard hook" | inserter | §2 Data Flow |
| ~infrastructure section | "Auto-runs validate-card.py on the edited file" | inserter running a scan cycle | §2 Data Flow / §5 Validation |
| ~infrastructure section | "Deck identity documents" (exercise mapping cache) | recursive resolver | §4 Resolution |
| ~infrastructure section | "Codex audit agent task. The agent reads... and emits the audit report" | emit | §1 Pipeline |
| ~generation rules | Each numbered step (Parse → Derive → Select → Format → Validate) | filters connected by pipes | §2 Data Flow |
| ~generation rules | "Load all parameter ceilings and constraints" | resolution parse phase | §4 Resolution |
| ~validation checklist | "Before writing any workout to a file, verify all of the following" | scan cycle | §5 Validation |
| ~validation checklist | Each individual checkbox item | rung | §5 Validation |
| ~validation checklist | "If any check fails, revise before writing" | rung failure | §5 Validation |
| ~block rules | "Never in 🖼, 🐂, or ⚪" (Gutter restriction) | interlock (not a rung — structural prevention) | §5 Validation |
| ~common errors | "8 Colors = 8 different workouts. If two Color variants use the same primary exercise, one of them is wrong" | collision | §5 Validation |
| ~what you do not do | "validation failures that block a card from being committed" | andon | §6 Feedback |
| ~infrastructure | "audit-exercise-coverage.py — Check for duplicate primary exercises" | collision detector | §5 Validation |
| ~infrastructure | "exercise library (~2,185 exercises)" | belt | §2 Data Flow |
| ~infrastructure | "The exercise library has gaps that prevent resolution" (implied) | belt saturation | §8 Health |
| ~CLAUDE.md + scl-directory.md | "master source of truth" / "authoritative" | authoritative source on the main bus | §4 Resolution |
| ~stub template | YAML frontmatter (described without naming it) | source map | §1 Pipeline |
| ~junction block | "Include 1–3 suggested follow-up zip codes with brief rationale" | draft offering | §7 UX |
| ~order section | CNS demand ceiling per Order | energy budget | §7 UX |
| ~order section | "🖼 + 🌹 + ⚪ = the deepest recovery lane in the system" | synergy | §7 UX |
| ~order section | Hypertrophy benefits compounding over weeks (implied) | scaling | §7 UX |
| ~bottleneck | "exercise selection + validation (highest reasoning cost)" (described, not named) | bottleneck | §8 Health |
| ~numeric zip | "The emoji zip and the number zip" (two representations of same address) | aliases | §4 Resolution |
| ~deck reference | "Cosmogram → Identity → Cards → Audit → CANONICAL" dependency chain | tech tree | §8 Health |

---

### README.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~card status | "Stub file. Awaiting workout generation." | cache miss | §4 Resolution |
| ~card status | "Workout written. Pending review." | cache hit | §4 Resolution |
| ~architecture | "Each card file will be ported to an interactive HTML workout card" | transpile (.md → HTML, same abstraction level) | §1 Pipeline |

---

### whiteboard.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~session state | "80/1,680 done. 1,600 remaining." | population (80) | §6 Feedback |
| ~session state | "Cards per session / per week" metrics | throughput | §8 Health |
| ~blocked queue | "Each deck requires: identity doc → generation → validation → review" | tech tree | §8 Health |
| ~hooks | Hook trigger descriptions without naming them | inserter | §2 Data Flow |
| ~rotation | User deviating from default rotation | branch | §3 State |
| ~validation | Checklist items run before committing | scan cycle / rungs | §5 Validation |

---

### scl-deep/order-specifications.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~common errors | "Common Foundation Errors", "Common Strength Errors" sections | implicitly a gemba checklist — reading as a user would | §6 Feedback |
| ~validation | Per-Order constraint checks described as rules | rungs | §5 Validation |

---

### scl-deep/publication-standard.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~frontmatter | YAML frontmatter described without naming it | source map | §1 Pipeline |
| ~register | Approved/banned word lists as validation | rungs (language rungs) | §5 Validation |

---

### scl-deep/vocabulary-standard.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~register | "Read the card as a user would" (implicit) | gemba | §6 Feedback |
| ~banned words | Banned word enforcement = structural prevention | poka-yoke | §5 Validation |

---

### middle-math/ARCHITECTURE.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~overview | "The exercise ledger is the raw log: one row per exercise per logged workout" | event store | §3 State |
| ~overview | "One logged set" | event | §3 State |
| ~overview | "The derived profile computed from the raw ledger" | projection | §3 State |
| ~overview | "The rotation engine" (described without naming its oscillator behavior) | oscillator | §6 Feedback |
| ~layers | "Layer 1... through Layer 7... final clamped weight" | layer system | §4 Resolution |
| ~resolution | "Converting a zip code to a complete rendered workout" | resolution | §4 Resolution |

---

### middle-math/user-context/exercise-ledger-spec.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~spec | "The ledger stores every logged set" | event store | §3 State |
| ~spec | "Each row in the ledger" | event | §3 State |
| ~spec | Append-only described without the term | event (immutable, append-only) | §3 State |
| ~user-exercise | User + exercise pair as the unit of analysis | aggregate | §3 State |

---

### middle-math/user-context/exercise-profile-spec.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~profile | "The derived profile computed from the raw ledger" | projection | §3 State |
| ~caching | "The profile is recomputed... updated after each logged session" | snapshot pattern | §3 State |
| ~prescribed vs actual | `prescribed_load_pct` and `actual_load_abs` alongside each other | setpoint and error signal | §6 Feedback |
| ~adaptation | Adjustment logic for next session based on performance gap | error signal → setpoint update | §6 Feedback |

---

### middle-math/user-context/toggle-system-spec.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~toggles | User toggles described without naming them | relics | §7 UX |
| ~persistence | "A toggle applies to all future card generation for this user" | relic (persistent passive modifier) | §7 UX |

---

### middle-math/rotation/rotation-engine-spec.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~engine | "The rotation engine" | oscillator | §6 Feedback |
| ~coprime | "The same Order × Type pairing doesn't repeat for 35 days" | oscillator period (LCM = Period-35) | §6 Feedback |
| ~3 gears | "3 gears" metaphor | oscillator (multi-period) | §6 Feedback |
| ~deviation | User not following default rotation | branch | §3 State |
| ~resume | Resuming rotation accounting for missed sessions | merge | §3 State |
| ~resume | Resuming rotation ignoring missed sessions | rebase | §3 State |

---

### middle-math/rotation/fatigue-model.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~target | Prescribed recovery targets | setpoint | §6 Feedback |
| ~actual vs prescribed | Gap between target and actual recovery | error signal | §6 Feedback |
| ~overshoot | Excessive load adjustment warning | overshoot | §6 Feedback |
| ~stable | When fatigue consistently matches targets | steady state | §6 Feedback |

---

### middle-math/rotation/reverse-weight-resolution.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~triangle | "The Temporal Triangle" (yesterday/today/tomorrow) | (glossary gap — see §Gaps) | — |
| ~yesterday | Yesterday's session informing today | event (yesterday's commit) informing today's setpoint | §3 / §6 |
| ~algorithm | Resolution adjusting by looking backward and forward | multi-pass resolution signal | §1 Pipeline |

---

### middle-math/weights/weight-system-spec.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~conflicts | "When multiple dials have opinions about the same emoji, apply the interaction rules" | priority stack | §4 Resolution |
| ~layers | Layer cascade described without naming it | layer system | §4 Resolution |

---

### middle-math/exercise-engine/selection-algorithm.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~library | Exercise library as the source pool | belt | §2 Data Flow |
| ~gaps | Library not covering a zip code constraint combination | belt saturation failure | §8 Health |
| ~narrowing | Pool narrowing as history develops | deck thinning | §7 UX |

---

### middle-math/rendering/operis-weight-derivation.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~featured | "EMPTY cards cannot appear as Sandbox rooms" | fizzle | §5 Validation |
| ~color scoring | Color of the Day determination pipeline | lexer → AST chain | §1 Pipeline |

---

### seeds/operis-architecture.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~editorial | "The Operis weekly editorial cycle moving through the Order space" | glider | §6 Feedback |
| ~construction vehicle | "The Operis as a construction vehicle" | cache warming engine | §4 Resolution |
| ~forced generation | "Each edition forces card generation for 8–12 addresses" | cache warming | §4 Resolution |
| ~empty stubs | "EMPTY cards cannot be featured... edition must feature a different zip code" | fizzle | §5 Validation |
| ~throughput | "Conservative estimate: 24–48 cards per week" | throughput | §8 Health |
| ~cold start | "The Operis solves the cold-start problem" | (glossary gap — see §Gaps) | — |
| ~pipeline | "P1→P2→P3→P4 run" | single-pass | §1 Pipeline |
| ~builder | "Builder writes to repo" | emit | §1 Pipeline |

---

### seeds/operis-prompt-pipeline.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~prompt 1 | "Prompt 1 (the Researcher)" | lexer | §1 Pipeline |
| ~contract B | "Contract B" (enriched content brief) | AST | §1 Pipeline |
| ~contract C | "Contract C" (full Operis edition) | IR | §1 Pipeline |
| ~prompt 4 | "Builder writes proofed files to repo" | emit | §1 Pipeline |
| ~pipeline | "P1→P2→P3→P4 in sequence" | single-pass | §1 Pipeline |
| ~empty stubs | "If the Sandbox room is an EMPTY stub, select a replacement" | fizzle | §5 Validation |
| ~handoff | Contracts A/B/C as handoff documents | pipes (typed contracts between filters) | §2 Data Flow |

---

### seeds/operis-sandbox-structure.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~empty | "If the zip is EMPTY, skip and select next" | fizzle | §5 Validation |
| ~featured | Cache hit/miss distinction (implicit) | cache hit / cache miss | §4 Resolution |

---

### seeds/default-rotation-engine.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~rotation | "The rotation engine" | oscillator | §6 Feedback |
| ~period | "The same pairing doesn't repeat for 35 days" | Period-35 oscillator | §6 Feedback |
| ~super-cycle | "35-day super-cycle" | (see gap note — conflicts with "Period-35" naming in glossary) | — |
| ~deviation | "Does the cycle pause or keep rolling?" | branch / merge vs rebase decision | §3 State |
| ~gears | "3 gears" (Order, Type, Axis) | oscillator components | §6 Feedback |

---

### seeds/experience-layer-blueprint.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~rendering | `.md` card → HTML rendering described | transpile | §1 Pipeline |
| ~frontmatter | YAML frontmatter carries card identity | source map | §1 Pipeline |
| ~onboarding | "User taps a room and enters the experience" | embark | §7 UX |

---

### seeds/platform-architecture-v2.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~onboarding | "A new user... taps a zip code in the Operis... they are inside a room" | embark | §7 UX |
| ~rendering | `.md` → HTML card described | transpile | §1 Pipeline |
| ~source map | Frontmatter preserving zip in rendered output | source map | §1 Pipeline |

---

### seeds/operis-researcher-prompt.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~role | "Prompt 1: Researcher" role described | lexer | §1 Pipeline |
| ~output | "Structured research brief" output | AST (root = Color of the Day, branches = departments) | §1 Pipeline |

---

### seeds/operis-builder-prompt.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~role | "Builder. Proofs edition, generates cards, commits to repository" | emit stage | §1 Pipeline |
| ~empty | "Generate cards for empty zip codes" | resolve cache misses | §4 Resolution |

---

### seeds/linters-architecture.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~validation | "Three-tier validation pipeline" | three-tier scan cycle | §5 Validation |
| ~rules | Individual validation rules in each tier | rungs | §5 Validation |
| ~structural | Hard-wired format constraints | interlocks | §5 Validation |

---

### deck-cosmograms/README.md

| Approx. Line | Current Language | Glossary Term | Section |
|------|-----------------|---------------|---------|
| ~pipeline | "Cosmogram → Identity → Cards → Audit → CANONICAL" | tech tree | §8 Health |
| ~stub | Cosmogram STUB status = not yet populated | cache miss (at cosmogram level) | §4 Resolution |

---

## GLOSSARY GAPS

Concepts found in documents that have no glossary term yet:

| Document | Concept | Description | Suggested Term |
|----------|---------|-------------|----------------|
| seeds/operis-architecture.md | "Cold-start problem" | Named explicitly: Operis solves the problem of a new user having no session history to draw recommendations from | **cold start** — the state where no event store exists yet for a user-exercise aggregate |
| middle-math/rotation/reverse-weight-resolution.md | "The Temporal Triangle" | Proprietary term for the yesterday/today/tomorrow triangulation algorithm in the reverse-weight resolution | **temporal triangle** — or fold into **multi-pass** with a PPL-specific note |
| seeds/default-rotation-engine.md vs glossary | "35-day super-cycle" vs "Period-35" | Same concept named differently in two places. The rotation engine doc says "super-cycle"; the glossary says "Period-35" in the oscillator definition. This is spaghetti inside the glossary itself. | Standardize to **Period-35** (the mathematical framing); add note in glossary oscillator entry |
| CLAUDE.md | Validation checklist (agent mental check) vs scan cycle (script check) | The VALIDATION CHECKLIST section is a pre-generation agent mental check. validate-card.py is a post-generation automated check. Both are called "scan cycle" in the glossary but they're different processes. | Rename the agent mental check: **pre-flight** (pre-generation checklist run mentally by the agent); reserve **scan cycle** for the automated script run |
| CLAUDE.md | "Card status lifecycle" | EMPTY → GENERATED → CANONICAL is a state machine. The concept of a card having lifecycle states has no glossary term. | **card lifecycle** or **card status** — define as the state machine EMPTY → GENERATED → CANONICAL |
| CLAUDE.md | "Temp Ppl± Architect Pattern" | External AI does research/planning; Claude Code executes. A recurring architectural pattern with no systems term. | **read-plan-execute split** or **architect-executor pattern** — the temp architect reads and plans; Claude Code executes |
| CLAUDE.md | "Error propagation" | "A hallucinated exercise propagates: .md → HTML → user session → user history → preference data." Named as a concern, not as a systems concept. | **propagation** — the downstream contamination chain when upstream content accuracy fails |
| seeds/operis-architecture.md | "Construction vehicle" | The Operis as a mechanism that forces card generation as a side effect of editorial output. Vivid metaphor, widely used, no glossary entry. | **construction vehicle** — an editorial output pipeline whose side effect is cache warming; formalize the metaphor |

---

## PATCH PRIORITY ORDER

Recommended order for Phase C patching, by frequency and agent-read centrality:

1. **CLAUDE.md** — ~40 instances — Every agent reads this every session. Informal language here contaminates working memory for the entire session. Highest leverage patch.

2. **seeds/operis-architecture.md** — ~20 instances — Architectural source for the Operis pipeline. Frequently referenced by temp architects and the Operis builder prompts. Second highest leverage.

3. **middle-math/ARCHITECTURE.md** — ~15 instances — Read when building the procedural engine. Contains the core event store / projection / oscillator concepts described informally.

4. **seeds/operis-prompt-pipeline.md** — ~12 instances — The operational Operis pipeline spec. Prompt 1/2/3/4 described without lexer/AST/IR/emit vocabulary. Patching this aligns the pipeline spec with the systems glossary.

5. **whiteboard.md** — ~10 instances — Read at session start by every agent. Informal language here persists into the working session. High priority despite lower instance count.

6. **middle-math/user-context/** (all 3 files) — ~12 instances combined — exercise-ledger-spec.md, exercise-profile-spec.md, toggle-system-spec.md. Event store, projection, relic terminology.

7. **middle-math/rotation/** (all 4 files) — ~12 instances combined — rotation-engine-spec.md, fatigue-model.md, reverse-weight-resolution.md. Oscillator, setpoint, error signal, branch/merge/rebase.

8. **seeds/ (remaining)** — ~30 instances combined across ~15 seeds — Lower priority; seeds are read less frequently and are often in flux.

9. **README.md** — ~3 instances — Low count but high visibility. The public face of the repo.

---

## GLOSSARY ACTIONS BEFORE PHASE C

Before patching documents, update `scl-deep/systems-glossary.md` with:

1. **Add: cold start** — state where no event store exists for a user-exercise aggregate
2. **Add: temporal triangle** — the yesterday/today/tomorrow triangulation in reverse-weight resolution (or add a note in the multi-pass entry)
3. **Fix: Period-35 vs super-cycle** — standardize the oscillator entry to use "Period-35"; add a note that "35-day super-cycle" is the informal alias to be deprecated
4. **Add: pre-flight** — the agent's mental pre-generation validation checklist (distinct from the automated scan cycle)
5. **Add: card lifecycle** — the EMPTY → GENERATED → CANONICAL state machine
6. **Add: construction vehicle** — formalize the Operis-as-cache-warming-engine metaphor
7. **Add: propagation** — downstream contamination chain from upstream content accuracy failures
8. **Note on architect-executor pattern** — the temp architect / Claude Code split (may be too PPL-specific for the glossary proper; consider a note in CLAUDE.md instead)

---

*Phase C can begin after glossary gaps are resolved. Patch CLAUDE.md first.*

🧮
