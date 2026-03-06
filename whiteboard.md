# Negotiosum — PPL± Active Work Board

Last updated: 2026-03-06
Phase: 2 — Workout Generation + Architecture Expansion
Cards: 222 / 1,680 (Deck 07: 40/40 ✅, Deck 08: 40/40 ✅, Deck 09: 40/40 ✅, Deck 10: 40/40 ✅, Deck 11: 40/40 ✅, Deck 12: 40/40 ✅)
Seeds: 49 | Scripts: 28
CX Containers: 44 defined, 40 complete, 4 open

For development history, see `session-log.md`.

---

## ⚫ Ordo Operis — Order of the Work

Teach, scaffold, define. Output that stands alone for any reader.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | CX-00A | Systems glossary | — | scl-deep/systems-glossary.md |
| DONE | CX-02 | Historical events scaffold (366 files) | — | scripts/operis/scaffold_historical_events.py |
| DONE | CX-05 | Markdownlint configuration | — | .github/linters/.markdownlint-cli2.jsonc |
| DONE | CX-06 | Frontmatter schema + validator | — | card-frontmatter-schema.json + validator script |
| DONE | CX-01 | Codex agent task architecture | — | Governance finalized, completion summary added. Session 037. |
| DONE | CX-19 | Agent boundaries document | — | .claude/AGENT-BOUNDARIES.md — 5-agent matrix, escalation rules, Jake zones. Session 037. |
| DONE | CX-34 | Codespaces dev container | — | .devcontainer/ + docs/codespaces-quickstart.md |
| DONE | — | Update README.md project status to 102/1,680 | — | Already updated in prior Codex runs |
| DONE | — | Update README.md repo structure (new directories, files) | — | sql/, session-log.md, docs/ added |
| DONE | CX-39 | External Reference Dock | — | Session 038: `external-refs.json` (2,085 null docks) + `seeds/exrx-partnership-brief.md` |

---

## 🟢 Natura Operis — Nature of the Work

Self-contained, zero-dependency. Runs in airplane mode.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | CX-03 | Zip converter + registry (1,680 JSON) | — | zip_converter.py, zip_registry.py, zip-registry.json |
| DONE | CX-13 | Exercise library parser (~2,185 JSON) | — | parse_exercise_library.py, exercise-library.json |
| DONE | CX-36 | Exercise Identity Registry | — | Session 038: `scripts/build-exercise-registry.py` + `middle-math/exercise-registry.json` (2,085 entries, EX-0001–EX-2085) |
| OPEN | CX-17 | Ralph Loop validation + batch orchestrator | CX-03 ✓ | validate-pod.py, ralph-batch.sh |
| OPEN | — | Deck 07 Ralph pod review (prototype approval) | — | Jake must review deck-07-pods.md before batch |

---

## 🔵 Architectura Operis — Architecture of the Work

Systematic, templated, institutional. Follow the pattern.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | CX-04 | Inventory + progress truth tables | — | inventory.py, deck-readiness.py, exercise-usage-report.py |
| DONE | CX-07 | CI lint workflow | — | .github/workflows/lint.yml |
| DONE | CX-08 | SQL schema materialization (7 migrations) | — | sql/001-007 + README — Session 033 |
| DONE | CX-16 | Deck identity scaffolds (Decks 10–12) | CX-03 ✓ | PR #67 — deck-identity-scaffold.py + 3 identity docs |
| DONE | — | Deck identity scaffolds (Decks 01–06) | CX-03 ✓ | Session 039 |
| DONE | CX-33 | GitHub Pages progress dashboard | CX-03 ✓, CX-04 ✓ | Built PR #90 (2026-03-05) — docs/dashboard/ + scripts/build-dashboard-data.py. Reconciled this session. |
| DONE | CX-40 | Exercise Registry SQL Migration | — | Session 038: `sql/009-exercise-registry.sql`, `sql/010-exercise-knowledge.sql`, `sql/README.md` updated |
| DONE | — | Deck 07 retrofit regen queue (18 cards) | — | DONE — Deck 07 debt cleared, all 40 cards meet V2 standard. |
| OPEN | — | Operis Contract A/B URL enforcement | — | P1 missing source URLs, P2 missing per-lane URLs |
| OPEN | — | Re-run Operis V4 pipeline test (2024-07-26) | Contract A/B fix | After URL/schema patching |

---

## 🟣 Profundum Operis — The Deep Work

Precision, multi-file reasoning, cascading consequences.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | CX-09 | Axis weight declarations (6 Axes) | CX-00A ✓ | DRAFT — all 6 axes populated, PR #64 |
| DONE | CX-10 | Type + Color weight declarations (5+8) | CX-00A ✓ | DRAFT — type-weights.md + color-weights.md, PR #65 |
| DONE | CX-11 | Block weight declarations (22+SAVE) | CX-09 ✓, CX-10 ✓ | DRAFT — 790-line working draft confirmed on disk |
| DONE | CX-12 | Operator weight declarations (12) | CX-09 ✓, CX-10 ✓ | DRAFT — 502-line working draft confirmed on disk |
| DONE | CX-14 | Weight vector computation engine | CX-09–12 all ✓, CX-03 ✓ | weight_vector.py + weight-vectors.json — 1,680 vectors, 61 dims, --validate passes. Session 034. |
| DONE | CX-15 | Exercise selection prototype | CX-13 ✓, CX-14 ✓ | exercise_selector.py — GOLD gate, load ceiling, tier, --validate, --stats. Sprint 035. |
| DONE | CX-18 | Design tokens + WeightCSS spec | — | middle-math/design-tokens.json + middle-math/weight-css-spec.md. Session 037. |
| DONE | CX-20 | Room schema extension | CX-08 ✓ | sql/008-room-schema-extension.sql — 4 tables + RLS |
| DONE | CX-21 | Content type registry (109 types JSON) | CX-00A ✓ | content-type-registry.json — 109 types, 6 axes, cross-floor appearances, operator affinities. Session 034. |
| DONE | CX-22 | Floor routing spec | CX-03 ✓, CX-20 ✓, CX-21 ✓ | middle-math/floor-routing-spec.md — 109 types × 6 floors. Unblocks CX-29. Sprint 035. |
| DONE | CX-23 | Navigation graph builder (1,680 × 4 edges) | CX-03 ✓, CX-04 ✓, CX-08 ✓ | middle-math/navigation-graph.json — 6,720 edges |
| DONE | CX-24 | Bloom state engine | CX-20 ✓, CX-03 ✓ | bloom_engine.py — 6 levels, no decay, eudaimonic. Sprint 035. |
| DONE | CX-25 | Vote weight integration | CX-20 ✓, CX-14 ✓ | vote_weight_adjuster.py — tanh signal, ±0.8 cap, --validate 5/5. Session 036. |
| DONE | CX-26 | Operis room manifest generator | CX-03 ✓, CX-04 ✓ | generate_room_manifest.py — 13-room Sandbox from date. Sprint 035. |
| DONE | CX-27 | Superscript/subscript data model | CX-20 ✓, CX-08 ✓ | compute_superscript.py — system suggestions + user overrides. Sprint 035. |
| DONE | CX-28 | Cosmogram content scaffold (42 stubs) | CX-04 ✓ | scaffold_cosmograms.py + 42 stubs written. Session 034. |
| DONE | CX-29 | Wilson audio route specification | CX-22 ✓ | middle-math/wilson-audio-spec.md — 3-layer scoring, ~2,260 keywords, voice registers by floor. Session 036. |
| DONE | CX-30 | Envelope schema + stamping prototype | CX-08 ✓, CX-14 ✓, CX-03 ✓ | envelope_stamper.py — atomic retrieval unit, --anonymous + --full + --deck modes. Session 036. |
| DONE | CX-31 | Envelope similarity function + retrieval | — | envelope_retrieval.py — cosine sim, Tier 1–4 profiles, --validate 5/5. Wave 5 capstone. Session 037. |
| DONE | CX-38 | Exercise Relationship Graph | — | Session 038: `family-trees.json` (15 families/2,085 members), `substitution-map.json`, `sport-tags.json`, `anatomy-index.json` |
| DONE | CX-43 | Exercise Selector V2 (registry-aware) | CX-36 ✓, CX-38 ✓, CX-15 ✓ | Session 041: selector upgraded to registry + family diversity + substitutions (`scripts/middle-math/exercise_selector.py`) |

---

## 🔴 Fervor Operis — The Heat of the Work

Maximum output, full capacity. Measure throughput.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | — | First Operis edition (2026-03-02) | — | PR #27 — operis-editions/2026/03/2026-03-02.md |
| DONE | — | Deck 07 generation (40 cards) | — | 18 flagged REGEN-NEEDED |
| DONE | — | Deck 08 generation (40 cards) | — | GENERATED-V2 complete |
| DONE | — | Deck 09 generation (40 cards) | — | 102/1,680 total |
| DONE | CX-37 | Exercise Knowledge Template + First Batch | — | Session 038: `scripts/generate-exercise-content.py` + 197 files in `exercise-content/` + `exercise-content/README.md` |
| DONE | CX-41 | Exercise Content Batch 2 (201–500) | CX-37 ✓ | Session 039: `python scripts/generate-exercise-content.py --batch 500` → +298 files (495 total in `exercise-content/`) |
| DONE | CX-42 | Exercise Content Batch 3 (501–1000) | CX-37 ✓ | Session 040: `python scripts/generate-exercise-content.py --batch 1000` → +498 files (993 total in `exercise-content/`) |
| DONE | — | Exercise Content Batch 4 (1001–1500) | CX-37 ✓ | Session 042: `python scripts/generate-exercise-content.py --batch 1500` → +493 files (1,486 total in `exercise-content/`) |
| DONE | — | Exercise Content Batch 5 FINAL (1501–2085) | CX-37 ✓ | Session 045: `python scripts/generate-exercise-content.py --batch 2085` → +599 files (2,085 total in `exercise-content/`) |
| DONE | — | Deck 07 regen (18 cards) | — | DONE — Deck 07 debt cleared — all 40 cards meet V2 standard. |
| DONE | — | Deck 10 generation (40 cards) | — | ⛽🪐 Strength Challenge complete (40/40) |
| OPEN | — | Deck 11 generation (40 cards) | Deck 11 identity | ⛽⌛ Strength Time |
| DONE | — | Deck 12 generation (40 cards) | — | ⛽🐬 Strength Partner complete (40/40) |
| OPEN | — | Historical events population (366 dates) | CX-02 ✓ | Research-intensive — ~180 hours total, builds incrementally |
| OPEN | — | Remaining 37 decks (1,478 cards) | Ongoing | Foundation Order next? Jake's call |

---

## 🟠 Nuntius Operis — The Messenger of the Work

Sweep, audit, report, deliver. Touch everything, miss nothing.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | CX-00B | Systems language audit | CX-00A ✓ | scl-deep/systems-language-audit.md |
| DONE | CX-35 | Whiteboard Negotiosum validator | CX-03 ✓, CX-04 ✓ | scripts/validate-negotiosum.py |
| DONE | — | Run deck-readiness.py and commit output | — | reports/deck-readiness-2026-03-06.md committed. Session 037. |
| DONE | — | Run exercise-usage-report.py on 102 cards | — | reports/exercise-usage-2026-03-06.md committed. Session 037. |
| OPEN | — | Ralph Loop batch: populate 41 remaining deck pods | Deck 07 pod review | Blocked on Jake approval of prototype |
| OPEN | — | Exercise library version bump to v.1 | — | Version bump criteria undefined |
| OPEN | — | Whiteboard DONE-task archive pass | — | Periodic ⚪ task: trim completed rows |

---

## 🟡 Lusus Operis — The Play of the Work

Creative exploration, discovery. Surprising AND useful.

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| DONE | CX-32 | Mermaid CX dependency graph | — | docs/cx-dependency-graph.md |
| DONE | — | Systems eudaimonics seed | — | seeds/systems-eudaimonics.md |
| DONE | — | Color pipeline posture seed | — | seeds/color-pipeline-posture.md |
| DONE | — | SCL envelope architecture | — | seeds/scl-envelope-architecture.md |
| OPEN | — | First deck cosmogram (Deck 07 or 01 or 05) | — | Genspark temp architect session with web access |
| OPEN | — | Operis editorial voice prototype | — | Write one edition in full creative register |
| OPEN | — | Deck campaign naming pass (Deck 09 titles) | — | Review operator + title quality across 40 cards |
| OPEN | — | Platform architecture V3 (if V2 needs update) | — | After enough infrastructure lands |

---

## ⚪ Eudaimonia Operis — The Flourishing of the Work

Review, reflect, slow down. Does this serve flourishing?

| Status | ID | Task | Blocker | Note |
|--------|----|------|---------|------|
| OPEN | — | First CANONICAL review (Deck 08) | — | Jake reads 40 cards as a user. Gemba test. |
| OPEN | — | Vocabulary standard audit on Decks 07–09 | — | Check banned words in 102 generated cards |
| OPEN | — | Eudaimonics compliance review of Stripe seed | — | Does tier gating match Property 1? |
| OPEN | — | Publication standard compliance on Deck 09 | — | Voice check against scl-deep/publication-standard.md |
| OPEN | — | Whiteboard pruning session | — | Monthly: archive DONE rows, promote notes to tasks |

---

## Notes

Active observations, open questions, and emergent ideas. When a note becomes a task, move it to the appropriate Color section. When a note becomes a seed, commit it and remove from here.

- **Session 038 CLOSED (2026-03-06) — Exercise Library Expansion: Wave 6 complete (5/5).** CX-36: `middle-math/exercise-registry.json` — 2,085 exercises, globally unique EX-0001–EX-2085, 16-pattern vocabulary, anatomy inference, family linkage, axis/order affinity. CX-37: `scripts/generate-exercise-content.py` + 197 files in `exercise-content/` (push/pull/legs/plus/ultra). CX-38: 4 engine files in `middle-math/exercise-engine/` (family-trees, substitution-map, sport-tags, anatomy-index). CX-39: `external-refs.json` (2,085 null docks) + `seeds/exrx-partnership-brief.md`. CX-40: `sql/009-exercise-registry.sql` + `sql/010-exercise-knowledge.sql` + README updated. Wave 7 (CX-41, CX-42, CX-43) fully unblocked. Known data issue: `movement_pattern` catch-all assigns ~1,256 exercises to `core-stability` — carry/conditioning pattern disambiguation deferred to CX-43 Selector V2.
- **Session 039 CLOSED (2026-03-06) — Exercise Content Batch 2:** CX-41 DONE via `scripts/generate-exercise-content.py --batch 500`; +298 new files generated (202 skipped), bringing `exercise-content/` to 495 files total across push/pull/legs/plus/ultra. Spot check completed on 3 random files (464–480 words each).
- **Session 040 CLOSED (2026-03-06) — Exercise Content Batch 3:** CX-42 DONE via `scripts/generate-exercise-content.py --batch 1000`; +498 new files generated (502 skipped), bringing `exercise-content/` to 993 files total across push/pull/legs/plus/ultra. Spot check completed on 3 random files (441–478 words each).
- **Session 044 CLOSED (2026-03-06) — Deck 12 complete:** Deck identity built in `deck-identities/deck-12-identity.md`, all 40 cards generated under `cards/⛽-strength/🐬-partner/`, validators passed, and **⛽ Strength Order complete — 240/1,680 rooms filled**.
- **Session 041 CLOSED (2026-03-06) — CX-43 Selector V2 complete:** `scripts/middle-math/exercise_selector.py` upgraded to registry-aware selection (`exercise-registry.json`), octave-scale affinity scoring, family diversity enforcement (cross-block x0.3 penalty + in-block family uniqueness on output), substitution chain output (`--show-subs` via `exercise-engine/substitution-map.json`), catch-all movement_pattern preprocessing override (83 applied, logged to stderr), and V1 compatibility via `--v1`. Full sweep validation passed: 1,680/1,680 zips.
- **Deck generation priority:** Continue ⛽ Order sweep (10→11→12) or pivot to 🐂 Foundation Order (01→06)? Jake's call.
- **First CANONICAL review:** Jake has reviewed 0 decks to CANONICAL. When does this happen? Deck 08 is the candidate.
- **Exercise library versioning:** Still v.0. Version bump criteria undefined. When does v.1 trigger?
- **Cosmogram sessions:** Require Genspark (web access). Schedule independently from generation. Priority candidates: Deck 07 (cards exist), Deck 01 (system origin), Deck 05 (history seed drafted).
- **Operis V4 pipeline:** Contract A/B URL enforcement gaps remain open. Must fix before re-run. Contract C parser hardening ✅ already committed.
- **Deck 07 Deck Campaign Table:** Deck 07 ✅ 40 cards (debt cleared, identity V2 ✅). Deck 08 ✅ 40 cards (identity V2 ✅). Deck 09 ✅ 40 cards (identity ✅). Decks 10–12 ⬜.
- **Deck 05 historical research seed:** Janus (Roman time/doorways), Imbolc (Celtic purification, Feb 1–2), Lupercalia (Roman purification, Feb 15), Ishango bone (20,000 BCE timekeeping), Benedictine horarium (canonical hours as temporal grammar), seven-day week (Babylonian/planetary). Feeds cosmogram when Deck 05 gets researched.
- **Monthly operator mapping confirmed:** Jan=📍pono, Feb=🧲capio, Mar=🧸fero, Apr=👀specio, May=🥨tendo, Jun=🤌facio, Jul=🚀mitto, Aug=🦢plico, Sep=🪵teneo, Oct=🐋duco, Nov=✒️grapho, Dec=🦉logos
- **Rotation engine:** Order by weekday (7-day), Type by rolling 5-day calendar from Jan 1, Axis by monthly operator. 5 and 7 are coprime — same Order-Type pairing doesn't repeat for 35 days.
- **4-dial elevator model:** Order=building, Axis=floor, Type=wing, Color=room. 1,680 rooms. Piano nobile stack: 🔨 ground → 🏛 noble → ⌛ 2nd → 🐬 3rd → 🌹 4th → 🪐 5th. Scroll on phone is inverse of building direction. Progressive disclosure IS the architecture.
- **Sprint 035 cascade:** CX-22 (floor routing) DONE → CX-29 (Wilson audio route) NOW UNBLOCKED. CX-15 (exercise selector) DONE → CX-25 (vote weight) and CX-30 (envelope stamping) critical path clear. Next session: CX-25 or CX-30.
- **Session 037 close (2026-03-06) — Architecture Capstone:** CX-31 DONE — envelope_retrieval.py (cosine similarity engine, Tier 1–4 retrieval profiles, --query/--deck/--operis/--validate/--stats flags, 5/5 validation). CX-01 DONE — TASK-ARCHITECTURE.md governance finalized, completion summary added. CX-19 DONE — .claude/AGENT-BOUNDARIES.md (5-agent matrix, escalation rules, Jake-reserved zones). CX-18 DONE — middle-math/design-tokens.json (8 Colors × 7 Orders) + middle-math/weight-css-spec.md (61-dim vector → CSS custom properties). Audit reports committed to reports/. 33/36 containers complete. CX architecture 92% done. Only CX-17 remains (blocked on Jake pod review). Project pivots to content generation.
- **Session 036 close (2026-03-06):** CX-25 DONE — vote_weight_adjuster.py (tanh signal, ±0.8 cap, eudaimonic interlock, --validate 5/5). CX-30 DONE — envelope_stamper.py (atomic retrieval unit, --anonymous + --full + --deck modes, all layers integrated). CX-29 DONE — middle-math/wilson-audio-spec.md (3-layer keyword scoring, ~2,260 entries, Wilson registers by floor). 29/36 containers complete. CX-31 (Envelope Retrieval) now FULLY UNBLOCKED — both blockers met (CX-30 ✓, CX-21 ✓). Wave 5 capstone is next.
- **The Operis is the front door** the system was missing. Solves cold start, onboarding, room circulation. Automatable once historical DB + cosmograms + calendar data are populated.
- **Programs are guided tours** — sequences of zip code addresses, not sequences of workouts. The rooms already exist. The program is the itinerary.
- **Publication standard constraint:** No "it's not X, it's Y" framing. The publication is informational. Independent of Party or Faction. Committed to Useful Knowledge.
- **The Negotiosum structure is new** (planted 2026-03-05). First pruning pass should evaluate whether Color assignments feel right after 2 weeks of use.
- **Reconciliation session (2026-03-05):** ~25 PRs (#27–#84) merged to main between Sessions 030–033 with no session log entries. This session reconciled all container statuses, backfilled evidence in TASK-ARCHITECTURE.md, and updated the Negotiosum. Deck 09 (40 cards) was generated entirely across unlogged Codex runs.
- **Wave 3 unlock (2026-03-05):** CX-09 and CX-10 completion unlocked CX-11 (Block weights) and CX-12 (Operator weights). Both were already populated as working drafts in prior unlogged Codex runs. Engine coupling session confirmed on disk and registered as DONE. CX-14 (Weight Vector Engine) is now fully unblocked — all 5 dependencies met.
- **Stale seed audit (2026-03-05):** 8 files flagged with stale card counts or status references. Update opportunistically when each file is next touched: seeds/claude-code-build-sequence.md, seeds/platform-architecture-v2.md, seeds/operis-architecture.md, seeds/operis-prompt-pipeline.md, .codex/NEXT-ROUND-HANDOFF.md, AGENTS.md, cards/AGENTS.md, middle-math/ARCHITECTURE.md. Jake-blocked items (require Jake's input): platform-v1-archive body paste, color-context-vernacular vocabulary update, order-parameters vocabulary update.
- **Graph Parti note:** Needs scl-macro-reference.md at root — condensed emoji macros for Graph Parti context. Not blocking.
- **Color-tagging overhead:** Justified when it aids routing. Break-even at second human on project. The tags cost little now; they pay when the team grows.
- **SCL-Deep expansion complete:** emoji-macros.md, order-specifications.md, block-specifications.md, vocabulary-standard.md, publication-standard.md all committed. These are reference docs — they deepen generation quality but don't block it.
- **Middle-math status:** All 5 weight categories now DRAFT: Order ✓, Axis ✓, Type ✓, Color ✓, Block ✓, Operator ✓. Exercise family trees DRAFT (8 families). Selection algorithm spec written. CX-14 is the next step — weight vector computation engine.
- **Git-worktree pattern:** Seed planted (seeds/git-worktree-pattern.md). Adopt when parallel branch work becomes frequent enough to justify. Currently one branch at a time is sufficient.
- **Engine coupling session (2026-03-05):** CX-11 + CX-12 confirmed on disk as working drafts (790 and 502 lines) — registered as DONE. CX-20 (Room Schema Extension) written: sql/008-room-schema-extension.sql with 4 tables, RLS, indexes, 1,680-row population. CX-23 (Navigation Graph) computed: 1,680 nodes × 4 edges = 6,720 edges in middle-math/navigation-graph.json. CX-33 (Progress Dashboard) built: docs/dashboard/ with dark-theme static HTML and Python build script. 4 new containers registered (CX-32–35), 3 already done from prior Codex runs. CX-14 fully unblocked — the bus is bussing.
- **Macro system notes (planted 2026-03-05):** Color as conversational tone modifier (Phase 7+): Colors can signal intent in digital communication. "This is a 🟣 question" = I need precision. "This is a 🟡 question" = I'm exploring. Potential community floor feature. GitHub Project Board as visual Negotiosum: Create a Project board with a Color custom field, populate from whiteboard.md. Whiteboard auto-update enforcement: CX-35 partially covers this; consider adding CI check that verifies whiteboard.md was updated in any PR marking a CX container DONE.
- **Session 034 critical path advance (2026-03-06):** CX-33 reconciled (PR #90, built 2026-03-05). CX-14 DONE — weight_vector.py computes all 1,680 vectors (61 dimensions, octave scale [-8,+8]). CX-21 DONE — content-type-registry.json (109 types, 6 axes). CX-28 DONE — 42 cosmogram stubs generated. Cascade unlock: CX-15, CX-22, CX-25, CX-30 all fully unblocked. CX-15 is critical path next.
- **Wave 4 unblocked (2026-03-06):** CX-15 (Exercise Selection Prototype) — CX-13 ✓, CX-14 ✓. CX-22 (Floor Routing) — CX-03 ✓, CX-20 ✓, CX-21 ✓. CX-25 (Vote Weight Integration) — CX-20 ✓, CX-14 ✓. CX-30 (Envelope Schema) — CX-08 ✓, CX-14 ✓, CX-03 ✓.

---

🧮
