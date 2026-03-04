# Systems Language Audit

## Summary

- **Total files audited:** 186
- **Total inconsistencies found:** 756
- **Files with inconsistencies:** 106

### Top 10 Repeated Inconsistencies

| Rank | Found Term Pattern | Glossary Term | Severity | Count | Suggested Replacement |
|---|---|---|---|---:|---|
| 1 | `source map` variants | Source map | low | 176 | `source map` |
| 2 | `filter` variants | Filter | low | 158 | `filter` |
| 3 | `resolution` variants | Resolution | low | 104 | `resolution` |
| 4 | `draft offering` variants | Junction / Draft offering | low | 75 | `draft offering` |
| 5 | `poka-yoke` variants | Poka-yoke | low | 56 | `poka-yoke` |
| 6 | `backpressure` variants | Backpressure | low | 47 | `backpressure` |
| 7 | `cache hit/cache miss` variants | Cache hit/miss | low | 35 | `cache hit/cache miss` |
| 8 | `pipeline` variants | Pipeline | high | 33 | `pipeline` |
| 9 | `pipeline` variants | Pipeline | medium | 33 | `pipeline` |
| 10 | `authoritative source` variants | Authoritative source | high | 15 | `authoritative source` |

Severity rubric: **high** = different system word used for a defined glossary concept; **medium** = close synonym; **low** = informal shorthand.

## .claude/agents/card-generator.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `.claude/agents/card-generator.md` | — | — | — | — | No inconsistencies found |

## .claude/agents/deck-auditor.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `.claude/agents/deck-auditor.md` | — | — | — | — | No inconsistencies found |

## .claude/agents/progress-tracker.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `.claude/agents/progress-tracker.md` | — | — | — | — | No inconsistencies found |

## .claude/skills/audit-deck.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `.claude/skills/audit-deck.md` | 9 | `## Steps` | Filter | low | `filter` |

## .claude/skills/build-deck-identity/SKILL.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `.claude/skills/build-deck-identity/SKILL.md` | 11 | `## Workflow` | Pipeline | high | `pipeline` |
| `.claude/skills/build-deck-identity/SKILL.md` | 27 | `- `deck-identities/template.md` — format structure` | Poka-yoke | low | `poka-yoke` |
| `.claude/skills/build-deck-identity/SKILL.md` | 40 | `### 4. Map 40 Zip Codes to Primary Exercises` | Source map | low | `source map` |
| `.claude/skills/build-deck-identity/SKILL.md` | 67 | `Use the template from `deck-identities/template.md`.` | Poka-yoke | low | `poka-yoke` |
| `.claude/skills/build-deck-identity/SKILL.md` | 81 | `If the deck folder doesn't exist yet (stubs only), skip this step —...` | Filter | low | `filter` |

## .claude/skills/compile-scl.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `.claude/skills/compile-scl.md` | 6 | `## Steps` | Filter | low | `filter` |
| `.claude/skills/compile-scl.md` | 15 | `## Priority Order` | Priority | low | `priority` |

## .claude/skills/generate-card/SKILL.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `.claude/skills/generate-card/SKILL.md` | 11 | `## Workflow` | Pipeline | high | `pipeline` |
| `.claude/skills/generate-card/SKILL.md` | 81 | `- Template: `[Primary Movement or Equipment+Exercise] — [Target Mus...` | Poka-yoke | low | `poka-yoke` |

## .claude/skills/plant-seed.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `.claude/skills/plant-seed.md` | 6 | `## Steps` | Filter | low | `filter` |
| `.claude/skills/plant-seed.md` | 9 | `2. Use this frontmatter template:` | Poka-yoke | low | `poka-yoke` |
| `.claude/skills/plant-seed.md` | 24 | `5. Update the Phase Relevance Map in `seeds/README.md` if the new s...` | Source map | low | `source map` |

## .claude/skills/progress-report/SKILL.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `.claude/skills/progress-report/SKILL.md` | — | — | — | — | No inconsistencies found |

## .claude/skills/ralph-loop.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `.claude/skills/ralph-loop.md` | — | — | — | — | No inconsistencies found |

## .claude/skills/retrofit-deck/SKILL.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `.claude/skills/retrofit-deck/SKILL.md` | 11 | `## Workflow` | Pipeline | high | `pipeline` |
| `.claude/skills/retrofit-deck/SKILL.md` | 23 | `- Template: `[Primary Movement or Equipment+Exercise] — [Target Mus...` | Poka-yoke | low | `poka-yoke` |
| `.claude/skills/retrofit-deck/SKILL.md` | 71 | `Flag any duplicate primary exercises. These require manual resolution.` | Resolution | low | `resolution` |

## .claude/skills/scaffold-html.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `.claude/skills/scaffold-html.md` | 6 | `## Steps` | Filter | low | `filter` |

## .claude/skills/validate-card.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `.claude/skills/validate-card.md` | 9 | `## Steps` | Filter | low | `filter` |

## AGENTS.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `AGENTS.md` | 16 | `This repository is the master source of truth for all 1,680 workouts.` | Authoritative source | high | `authoritative source` |
| `AGENTS.md` | 41 | `├── CLAUDE.md              — Claude Code operating instructions (al...` | Fizzle | medium | `fizzle` |
| `AGENTS.md` | 46 | `├── card-template-v2.md    — Generation template for card format` | Poka-yoke | low | `poka-yoke` |
| `AGENTS.md` | 221 | `\| 🚂 \| Junction \| Retention \| Bridge to next session. 1–3 follow...` | Junction / Draft offering | low | `draft offering` |
| `AGENTS.md` | 262 | `5. Honor the coverage map — each card's primary exercise must match...` | Source map | low | `source map` |
| `AGENTS.md` | 268 | `Execute these steps in order. Do not skip steps.` | Filter | low | `filter` |
| `AGENTS.md` | 270 | `**Step 1 — Parse the Zip Code**` | Filter | low | `filter` |
| `AGENTS.md` | 277 | `**Step 2 — Derive the Default Operator**` | Filter | low | `filter` |
| `AGENTS.md` | 282 | `**Step 3 — Derive the Block Sequence**` | Filter | low | `filter` |
| `AGENTS.md` | 286 | `**Step 4 — Select Exercises**` | Filter | low | `filter` |
| `AGENTS.md` | 295 | `**Step 5 — Format the Workout**` | Filter | low | `filter` |
| `AGENTS.md` | 317 | `14. 🚂 JUNCTION with logging space and next-session bridge. Include ...` | Junction / Draft offering | low | `draft offering` |

## CLAUDE.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `CLAUDE.md` | 28 | `This repository is the master source of truth for all 1,680 workouts.` | Authoritative source | high | `authoritative source` |
| `CLAUDE.md` | 106 | `- `operis-architecture.md` — PPL± Operis: complete specification. W...` | Multi-pass | medium | `multi-pass` |
| `CLAUDE.md` | 114 | `- `seeds/operis-sandbox-structure.md` — 13-room Sandbox: 8 determin...` | Source map | low | `source map` |
| `CLAUDE.md` | 155 | `## CARD STUB TEMPLATE` | Poka-yoke | low | `poka-yoke` |
| `CLAUDE.md` | 414 | `\| 🚂 \| Junction \| Retention \| Bridge to next session. 1–3 follow...` | Junction / Draft offering | low | `draft offering` |
| `CLAUDE.md` | 468 | `When given a zip code, execute these steps in order. Do not skip st...` | Filter | low | `filter` |
| `CLAUDE.md` | 470 | `**Step 1 — Parse the Zip Code**` | Filter | low | `filter` |
| `CLAUDE.md` | 477 | `**Step 2 — Derive the Default Operator**` | Filter | low | `filter` |
| `CLAUDE.md` | 483 | `**Step 3 — Derive the Block Sequence**` | Filter | low | `filter` |
| `CLAUDE.md` | 488 | `**Step 4 — Select Exercises**` | Filter | low | `filter` |
| `CLAUDE.md` | 497 | `**Step 5 — Format the Workout**` | Filter | low | `filter` |
| `CLAUDE.md` | 517 | `14. 🚂 JUNCTION with logging space and next-session bridge. Include ...` | Junction / Draft offering | low | `draft offering` |
| `CLAUDE.md` | 629 | `Each section declares its SCL Type mapping, Order relevance, Axis e...` | Source map | low | `source map` |
| `CLAUDE.md` | 709 | `These tools are available in every session. They are not optional —...` | Pipeline | high | `pipeline` |
| `CLAUDE.md` | 725 | `\| build-deck-identity \| Create deck identity document with exerci...` | Source map | low | `source map` |
| `CLAUDE.md` | 773 | `- **Skill** = multi-step workflow with judgment calls. Use for gene...` | Pipeline | high | `pipeline` |
| `CLAUDE.md` | 773 | `- **Skill** = multi-step workflow with judgment calls. Use for gene...` | Filter | low | `filter` |
| `CLAUDE.md` | 786 | `When describing system operations (pipelines, data flow, validation...` | Multi-pass | medium | `multi-pass` |
| `CLAUDE.md` | 794 | `- **Cache hit / miss** — Whether a zip code has generated content (...` | Cache hit/miss | low | `cache hit/cache miss` |
| `CLAUDE.md` | 799 | `- **Resolution** — Converting a zip code into a rendered workout.` | Resolution | low | `resolution` |
| `CLAUDE.md` | 845 | `4. Read the deck identity doc (if exists) — exercise mapping` | Source map | low | `source map` |
| `CLAUDE.md` | 874 | `Workflow directory: `.github/workflows/`` | Pipeline | high | `pipeline` |
| `CLAUDE.md` | 909 | `**Blocked Queue (waiting on dependencies)**` | Backpressure | low | `backpressure` |
| `CLAUDE.md` | 937 | `template-based format is an evolution, not a replacement. Both formats` | Poka-yoke | low | `poka-yoke` |
| `CLAUDE.md` | 965 | `- `middle-math/rotation/reverse-weight-resolution.md` — Temporal zi...` | Resolution | low | `resolution` |
| `CLAUDE.md` | 1030 | `- Sandbox structure planted: `seeds/operis-sandbox-structure.md` — ...` | Source map | low | `source map` |
| `CLAUDE.md` | 1032 | `- Reverse-weight resolution seeded: `middle-math/rotation/reverse-w...` | Resolution | low | `resolution` |

## LICENSE-CONTENT.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `LICENSE-CONTENT.md` | 24 | `- Card templates and the card template V2 format` | Poka-yoke | low | `poka-yoke` |

## LICENSE-LANGUAGE.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `LICENSE-LANGUAGE.md` | — | — | — | — | No inconsistencies found |

## README.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `README.md` | 168 | `├── middle-math/           — Computation engine: weights, exercise ...` | Resolution | low | `resolution` |
| `README.md` | 169 | `├── deck-identities/       — Pre-generation exercise mapping per deck` | Source map | low | `source map` |
| `README.md` | 231 | `\| 🚂 \| Junction \| Bridge to next session. Follow-up zip suggestio...` | Junction / Draft offering | low | `draft offering` |
| `README.md` | 252 | `The `.md` card files are the master source of truth — the architect...` | Authoritative source | high | `authoritative source` |
| `README.md` | 295 | `## Goal Mapping — Quick Reference` | Source map | low | `source map` |

## almanac-2026-zip-calendar.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `almanac-2026-zip-calendar.md` | — | — | — | — | No inconsistencies found |

## card-template-v2.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `card-template-v2.md` | 1 | `# card-template-v2.md — PPL± Card Format Standard` | Poka-yoke | low | `poka-yoke` |
| `card-template-v2.md` | 3 | `This is the v2 card template. It replaces the v1 15-element require...` | Poka-yoke | low | `poka-yoke` |
| `card-template-v2.md` | 184 | `**Reduced required elements:** 15 → 8. The seven dropped elements (...` | Poka-yoke | low | `poka-yoke` |
| `card-template-v2.md` | 186 | `**Color drives structure:** The block sequence and content depth sc...` | Poka-yoke | low | `poka-yoke` |

## container-directory.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `container-directory.md` | 3 | `## Dependency Map (excerpt)` | Source map | low | `source map` |

## deck-identities/README.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `deck-identities/README.md` | — | — | — | — | No inconsistencies found |

## deck-identities/deck-07-identity.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `deck-identities/deck-07-identity.md` | 15 | `## 2) Coverage Map (Type × Color)` | Source map | low | `source map` |
| `deck-identities/deck-07-identity.md` | 46 | `## 4) Content Regeneration Queue` | Backpressure | low | `backpressure` |

## deck-identities/deck-08-identity.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `deck-identities/deck-08-identity.md` | 10 | `## 2) Coverage Map (Type × Color)` | Source map | low | `source map` |
| `deck-identities/deck-08-identity.md` | 15 | `\| 🍗 \| **Rear Foot Elevated Split Squat — Leg Coaching Session**<b...` | Filter | low | `filter` |
| `deck-identities/deck-08-identity.md` | 16 | `\| ➕ \| **Suitcase Carry Basics — Core and Grip Coaching Session**<...` | Junction / Draft offering | low | `draft offering` |
| `deck-identities/deck-08-identity.md` | 52 | `- ⛽🔨🍗🟠 — Step-Up and Lunge Rotation — Quad and Glute Stations built...` | Filter | low | `filter` |
| `deck-identities/deck-08-identity.md` | 56 | `- ⛽🔨➕🟢 — Bear Crawl and Single-Leg Bridge — Core and Hip Drive, No ...` | Junction / Draft offering | low | `draft offering` |

## deck-identities/deck-08-rename-log.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `deck-identities/deck-08-rename-log.md` | 9 | `- `⛽🔨➕🟢±🧸 Barless Power — Bodyweight Carry and Core.md` → `⛽🔨➕🟢±🧸 B...` | Junction / Draft offering | low | `draft offering` |
| `deck-identities/deck-08-rename-log.md` | 23 | `- `⛽🔨🍗🟠±🥨 Leg Circuit — Functional Station Loop.md` → `⛽🔨🍗🟠±🥨 Step-...` | Filter | low | `filter` |

## deck-identities/naming-convention.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `deck-identities/naming-convention.md` | 3 | `**Template:** `[Primary Movement or Equipment+Exercise] — [Target M...` | Poka-yoke | low | `poka-yoke` |

## deck-identities/template.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `deck-identities/template.md` | 1 | `# Deck XX Identity Template` | Poka-yoke | low | `poka-yoke` |
| `deck-identities/template.md` | 6 | `## 2) Coverage Map (Type × Color)` | Source map | low | `source map` |

## exercise-library.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `exercise-library.md` | 4 | `Mapping: Each section header declares SCL Type(s), Order relevance,...` | Source map | low | `source map` |
| `exercise-library.md` | 6 | `Use these headers as the bridge between the canonical exercise list...` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 10 | `SCL Mapping: Primary ➕ Plus \| Secondary 🖼 Restoration` | Source map | low | `source map` |
| `exercise-library.md` | 54 | `25. Neck Bridge (Wrestler's Bridge)` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 66 | `SCL Mapping: Primary 🛒 Push + 🪡 Pull \| Secondary ⚖ Balance` | Source map | low | `source map` |
| `exercise-library.md` | 296 | `SCL Mapping: Primary 🛒 Push` | Source map | low | `source map` |
| `exercise-library.md` | 482 | `SCL Mapping: Primary 🪡 Pull \| Secondary ➕ Plus` | Source map | low | `source map` |
| `exercise-library.md` | 487 | `Notes: Lats, traps (upper/mid/lower), rhomboids, erectors (thoracic...` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 717 | `206. Thoracic Bridge` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 760 | `247. Back Bridge (Wrestler's Bridge)` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 849 | `SCL Mapping: Primary ⚖ Balance + 🛒 Push (triceps) + 🪡 Pull (biceps)` | Source map | low | `source map` |
| `exercise-library.md` | 854 | `Notes: Biceps = Pull type. Triceps = Push type. Forearms/wrist/grip...` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 1093 | `SCL Mapping: Primary ➕ Plus \| Secondary 🖼 Restoration` | Source map | low | `source map` |
| `exercise-library.md` | 1381 | `247. Bridge with Pelvic Floor Engagement` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 1387 | `SCL Mapping: Primary 🍗 Legs + 🪡 Pull (hip hinge) \| Secondary 🖼 Res...` | Source map | low | `source map` |
| `exercise-library.md` | 1402 | `8. Glute Bridge (Bodyweight)` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 1403 | `9. Barbell Glute Bridge` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 1404 | `10. Single-Leg Glute Bridge` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 1405 | `11. Banded Glute Bridge` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 1406 | `12. Marching Glute Bridge` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 1407 | `13. Stability Ball Glute Bridge` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 1408 | `14. Feet-Elevated Glute Bridge` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 1409 | `15. Isometric Glute Bridge Hold` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 1428 | `Gluteus Maximus - Lunges & Step-Ups` | Filter | low | `filter` |
| `exercise-library.md` | 1433 | `35. Box Step-Up` | Filter | low | `filter` |
| `exercise-library.md` | 1434 | `36. Weighted Box Step-Up` | Filter | low | `filter` |
| `exercise-library.md` | 1435 | `37. High Step-Up (Deep Glute)` | Filter | low | `filter` |
| `exercise-library.md` | 1436 | `38. Lateral Step-Up` | Filter | low | `filter` |
| `exercise-library.md` | 1437 | `39. Step-Down (Eccentric Glute)` | Filter | low | `filter` |
| `exercise-library.md` | 1548 | `134. Bridge with Pelvic Floor Engagement` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 1559 | `143. Bridge Hold (TRE Position)` | Junction / Draft offering | low | `draft offering` |
| `exercise-library.md` | 1601 | `SCL Mapping: Primary 🍗 Legs` | Source map | low | `source map` |
| `exercise-library.md` | 1603 | `Axes: All — emphasized in 🏛 Basics (barbell squat, front squat), 🔨 ...` | Filter | low | `filter` |
| `exercise-library.md` | 1688 | `Quadriceps - Step-Ups & Box Work` | Filter | low | `filter` |
| `exercise-library.md` | 1689 | `71. Box Step-Up` | Filter | low | `filter` |
| `exercise-library.md` | 1690 | `72. Weighted Box Step-Up (Dumbbells)` | Filter | low | `filter` |
| `exercise-library.md` | 1691 | `73. Barbell Box Step-Up` | Filter | low | `filter` |
| `exercise-library.md` | 1692 | `74. High Box Step-Up` | Filter | low | `filter` |
| `exercise-library.md` | 1693 | `75. Lateral Step-Up` | Filter | low | `filter` |
| `exercise-library.md` | 1694 | `76. Weighted Lateral Step-Up` | Filter | low | `filter` |
| `exercise-library.md` | — | `... 38 additional matches truncated in this report` | — | — | — |

## generation-philosophy.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `generation-philosophy.md` | 4 | `These override any tendency toward verbosity, fake precision, or te...` | Poka-yoke | low | `poka-yoke` |
| `generation-philosophy.md` | 68 | `The day-of-week Order mapping:` | Source map | low | `source map` |
| `generation-philosophy.md` | 153 | `The Color isn't a modifier on a template. It IS the template. Gener...` | Poka-yoke | low | `poka-yoke` |

## middle-math/ARCHITECTURE.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/ARCHITECTURE.md` | 21 | `Master cards define exercise roles — movement pattern, block positi...` | Poka-yoke | low | `poka-yoke` |
| `middle-math/ARCHITECTURE.md` | 27 | `See `exercise-engine/` for the selection algorithm, family trees, a...` | Poka-yoke | low | `poka-yoke` |
| `middle-math/ARCHITECTURE.md` | 47 | `A user who has squatted at ⛽🏛🍗🔵 (Strength, Basics, Legs, Structured...` | Junction / Draft offering | low | `draft offering` |
| `middle-math/ARCHITECTURE.md` | 69 | `## Section 6 — The Operis Bridge` | Junction / Draft offering | low | `draft offering` |
| `middle-math/ARCHITECTURE.md` | 111 | `Card generation (Phase 2) continues independently. Middle-math does...` | Poka-yoke | low | `poka-yoke` |

## middle-math/README.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/README.md` | 3 | `The deterministic bridge between the SCL architecture and the rende...` | Junction / Draft offering | low | `draft offering` |
| `middle-math/README.md` | 9 | `- Exercise selection resolves procedurally from templates, not AI g...` | Resolution | low | `resolution` |
| `middle-math/README.md` | 56 | `template-based format is an evolution, not a replacement. Both formats` | Poka-yoke | low | `poka-yoke` |

## middle-math/exercise-engine/README.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/exercise-engine/README.md` | 3 | `The procedural pipeline that fills template roles with specific exe...` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/README.md` | 7 | `Static card generation names specific exercises. One user, one exer...` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/README.md` | 13 | `Fully-specified workout cards (the current format — named exercises...` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/README.md` | 16 | `- Template card: engine runs the full selection pipeline and fills ...` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/README.md` | 18 | `During Phase 2 (card generation), all new cards are fully-specified...` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/README.md` | 22 | `- `selection-algorithm.md` — The 6-step query → rank → select pipel...` | Filter | low | `filter` |
| `middle-math/exercise-engine/README.md` | 26 | `- `template-spec.md` — How master cards define roles, not exercises` | Poka-yoke | low | `poka-yoke` |

## middle-math/exercise-engine/family-trees.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/exercise-engine/family-trees.md` | — | — | — | — | No inconsistencies found |

## middle-math/exercise-engine/selection-algorithm.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/exercise-engine/selection-algorithm.md` | 5 | `The 6-step pipeline from template role to specific exercise. Determ...` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 5 | `The 6-step pipeline from template role to specific exercise. Determ...` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/selection-algorithm.md` | 14 | `Step 1: Read the template role` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 14 | `Step 1: Read the template role` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/selection-algorithm.md` | 16 | `Step 2: Read zip code constraints` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 18 | `Step 3: Read user constraints` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 20 | `Step 4: Query the exercise library (filter → rank → select)` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 22 | `Step 5: Check user ledger for prescription data` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 24 | `Step 6: Return exercise with zip-code-aware parameters` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 29 | `## Step 1 — Read the Template Role` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 29 | `## Step 1 — Read the Template Role` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/selection-algorithm.md` | 31 | `A template role defines what kind of movement belongs in a given bl...` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/selection-algorithm.md` | 55 | `## Step 2 — Read Zip Code Constraints` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 79 | `## Step 3 — Read User Constraints` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 94 | `## Step 4 — Query the Exercise Library (Filter → Rank → Select)` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 152 | `# Fallback: return top candidate even if preference mismatch` | Fizzle | medium | `fizzle` |
| `middle-math/exercise-engine/selection-algorithm.md` | 158 | `## Step 5 — Check User Ledger for Prescription` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 184 | `## Step 6 — Return` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 187 | `def resolve_role(role, zip_code, user_id):` | Resolution | low | `resolution` |
| `middle-math/exercise-engine/selection-algorithm.md` | 217 | `**Exercise is GOLD-gated but Color does not unlock GOLD:** The filt...` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 219 | `**Fully-specified card (no template):** Skip Steps 1–4. The exercis...` | Filter | low | `filter` |
| `middle-math/exercise-engine/selection-algorithm.md` | 219 | `**Fully-specified card (no template):** Skip Steps 1–4. The exercis...` | Poka-yoke | low | `poka-yoke` |

## middle-math/exercise-engine/substitution-rules.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/exercise-engine/substitution-rules.md` | 9 | `### Step 1 — Walk the Family Tree` | Filter | low | `filter` |
| `middle-math/exercise-engine/substitution-rules.md` | 13 | `Priority order within the family:` | Priority | low | `priority` |
| `middle-math/exercise-engine/substitution-rules.md` | 30 | `### Step 2 — Prefer Same Axis Affinity` | Filter | low | `filter` |
| `middle-math/exercise-engine/substitution-rules.md` | 34 | `### Step 3 — Check Tier Compliance` | Filter | low | `filter` |
| `middle-math/exercise-engine/substitution-rules.md` | 38 | `### Step 4 — Fallback: Different Movement Family` | Filter | low | `filter` |
| `middle-math/exercise-engine/substitution-rules.md` | 38 | `### Step 4 — Fallback: Different Movement Family` | Fizzle | medium | `fizzle` |
| `middle-math/exercise-engine/substitution-rules.md` | 53 | `### Step 5 — Flag If No Substitute Found` | Filter | low | `filter` |
| `middle-math/exercise-engine/substitution-rules.md` | 66 | `**Equipment absence vs. toggle:** Equipment absence (user has no ba...` | Filter | low | `filter` |

## middle-math/exercise-engine/template-spec.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/exercise-engine/template-spec.md` | 1 | `# Template Specification` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/template-spec.md` | 9 | `A template role replaces a named exercise in a card with a role dec...` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/template-spec.md` | 9 | `A template role replaces a named exercise in a card with a role dec...` | Resolution | low | `resolution` |
| `middle-math/exercise-engine/template-spec.md` | 75 | `**Template card:**` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/template-spec.md` | 78 | `Role: bread-butter-primary → [engine resolves at render time]` | Resolution | low | `resolution` |
| `middle-math/exercise-engine/template-spec.md` | 91 | `No existing card needs to be converted. Template format is additive.` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/template-spec.md` | 95 | `## Worked Example: Converting a Deck 08 Card to Template Format` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/template-spec.md` | 109 | `**Template format equivalent (⛽🔨🪡🔵):**` | Poka-yoke | low | `poka-yoke` |
| `middle-math/exercise-engine/template-spec.md` | 140 | `The template version produces different exercise selections for dif...` | Poka-yoke | low | `poka-yoke` |

## middle-math/exercise-engine/transfer-ratios.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/exercise-engine/transfer-ratios.md` | — | — | — | — | No inconsistencies found |

## middle-math/rendering/README.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/rendering/README.md` | 17 | `The design system (typography choices, specific color hex values, m...` | Junction / Draft offering | low | `draft offering` |

## middle-math/rendering/operis-weight-derivation.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/rendering/operis-weight-derivation.md` | 66 | `**Logic:** Map Order weight to department count range. The existing...` | Source map | low | `source map` |
| `middle-math/rendering/operis-weight-derivation.md` | 197 | `### Resolution` | Resolution | low | `resolution` |

## middle-math/rendering/progressive-disclosure.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/rendering/progressive-disclosure.md` | 27 | `## Weight-to-Emphasis Mapping` | Source map | low | `source map` |

## middle-math/rendering/ui-weight-derivation.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/rendering/ui-weight-derivation.md` | — | — | — | — | No inconsistencies found |

## middle-math/roots/README.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/roots/README.md` | — | — | — | — | No inconsistencies found |

## middle-math/roots/almanac-archive.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/roots/almanac-archive.md` | — | — | — | — | No inconsistencies found |

## middle-math/roots/four-layers.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/roots/four-layers.md` | 9 | `These four became the four PPL± dial categories. The mapping is not...` | Source map | low | `source map` |

## middle-math/roots/octave-logic.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/roots/octave-logic.md` | — | — | — | — | No inconsistencies found |

## middle-math/roots/order-notation.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/roots/order-notation.md` | 45 | `The 7 Orders map to the 7 Liberal Arts (Trivium + Quadrivium), givi...` | Source map | low | `source map` |

## middle-math/rotation/README.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/rotation/README.md` | — | — | — | — | No inconsistencies found |

## middle-math/rotation/fatigue-model.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/rotation/fatigue-model.md` | — | — | — | — | No inconsistencies found |

## middle-math/rotation/junction-algorithm.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/rotation/junction-algorithm.md` | 3 | `The 🚂 Junction block at the end of every workout suggests 1–3 follo...` | Pipeline | high | `pipeline` |
| `middle-math/rotation/junction-algorithm.md` | 22 | `## Computation Steps` | Filter | low | `filter` |
| `middle-math/rotation/junction-algorithm.md` | 24 | `### Step 1 — Assess Session Load (Fatigue Signal)` | Filter | low | `filter` |
| `middle-math/rotation/junction-algorithm.md` | 44 | `### Step 2 — Identify Candidate Next Zip Codes` | Filter | low | `filter` |
| `middle-math/rotation/junction-algorithm.md` | 74 | `### Step 3 — Apply Fatigue Filter` | Filter | low | `filter` |
| `middle-math/rotation/junction-algorithm.md` | 103 | `### Step 4 — Generate Rationale` | Filter | low | `filter` |
| `middle-math/rotation/junction-algorithm.md` | 157 | `In the current Phase 2 card generation workflow, Junction suggestio...` | Pipeline | high | `pipeline` |
| `middle-math/rotation/junction-algorithm.md` | 157 | `In the current Phase 2 card generation workflow, Junction suggestio...` | Filter | low | `filter` |

## middle-math/rotation/reverse-weight-resolution.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/rotation/reverse-weight-resolution.md` | 2 | `title: Reverse-Weight Resolution Algorithm` | Resolution | low | `resolution` |
| `middle-math/rotation/reverse-weight-resolution.md` | 17 | `# Reverse-Weight Resolution Algorithm` | Resolution | low | `resolution` |
| `middle-math/rotation/reverse-weight-resolution.md` | 23 | `The Reverse-Weight Resolution layer triangulates today's optimal ro...` | Resolution | low | `resolution` |
| `middle-math/rotation/reverse-weight-resolution.md` | 40 | `Yesterday tells you what tissue is loaded and what CNS demand was p...` | Resolution | low | `resolution` |
| `middle-math/rotation/reverse-weight-resolution.md` | 42 | `The resolution never overrides the Order. The weekday Order is fixe...` | Resolution | low | `resolution` |
| `middle-math/rotation/reverse-weight-resolution.md` | 50 | `**Process**:` | Pipeline | medium | `pipeline` |
| `middle-math/rotation/reverse-weight-resolution.md` | 72 | `**Process**:` | Pipeline | medium | `pipeline` |
| `middle-math/rotation/reverse-weight-resolution.md` | 94 | `**Process**:` | Pipeline | medium | `pipeline` |
| `middle-math/rotation/reverse-weight-resolution.md` | 112 | `Resolution logic:` | Resolution | low | `resolution` |
| `middle-math/rotation/reverse-weight-resolution.md` | 122 | `If the rotation engine default zip scores within one standard devia...` | Resolution | low | `resolution` |
| `middle-math/rotation/reverse-weight-resolution.md` | 130 | `The reverse-weight resolution algorithm is the editorial intelligen...` | Resolution | low | `resolution` |
| `middle-math/rotation/reverse-weight-resolution.md` | 148 | `- `middle-math/rotation/rotation-engine-spec.md` — provides the def...` | Resolution | low | `resolution` |
| `middle-math/rotation/reverse-weight-resolution.md` | 163 | `resolve(date) → zip_code` | Resolution | low | `resolution` |

## middle-math/rotation/rotation-engine-spec.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/rotation/rotation-engine-spec.md` | 56 | `Each month aligns to one Axis via the monthly Operator. The Operato...` | Source map | low | `source map` |

## middle-math/schemas/README.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/schemas/README.md` | 14 | `- `zip-weight-cache-schema.md` — Optional pre-computed weight vecto...` | Cache hit/miss | low | `cache hit/cache miss` |

## middle-math/schemas/exercise-families-schema.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/schemas/exercise-families-schema.md` | — | — | — | — | No inconsistencies found |

## middle-math/schemas/exercise-library-schema.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/schemas/exercise-library-schema.md` | 18 | `-- SCL Type mapping` | Source map | low | `source map` |

## middle-math/schemas/user-ledger-schema.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/schemas/user-ledger-schema.md` | 3 | `Raw workout log. One row per exercise set per logged session. The s...` | Authoritative source | high | `authoritative source` |

## middle-math/schemas/user-profile-schema.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/schemas/user-profile-schema.md` | — | — | — | — | No inconsistencies found |

## middle-math/schemas/user-toggles-schema.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/schemas/user-toggles-schema.md` | — | — | — | — | No inconsistencies found |

## middle-math/schemas/zip-metadata-schema.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/schemas/zip-metadata-schema.md` | 229 | `- `middle-math/schemas/zip-weight-cache-schema.md` — Optional pre-c...` | Cache hit/miss | low | `cache hit/cache miss` |

## middle-math/schemas/zip-weight-cache-schema.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/schemas/zip-weight-cache-schema.md` | 1 | `# Zip Weight Cache Schema` | Cache hit/miss | low | `cache hit/cache miss` |
| `middle-math/schemas/zip-weight-cache-schema.md` | 49 | `## Cache Invalidation` | Cache hit/miss | low | `cache hit/cache miss` |
| `middle-math/schemas/zip-weight-cache-schema.md` | 51 | `When weight declaration files change (e.g., when axis-weights.md is...` | Cache hit/miss | low | `cache hit/cache miss` |
| `middle-math/schemas/zip-weight-cache-schema.md` | 76 | `This keeps the cache stable (valid for all time regardless of date)...` | Cache hit/miss | low | `cache hit/cache miss` |

## middle-math/user-context/README.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/user-context/README.md` | 7 | `1. **Exercise Ledger** — The raw log. One row per exercise per logg...` | Authoritative source | high | `authoritative source` |

## middle-math/user-context/cross-context-translation.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/user-context/cross-context-translation.md` | 5 | `The weight system provides the bridge. The difference between two z...` | Junction / Draft offering | low | `draft offering` |
| `middle-math/user-context/cross-context-translation.md` | 92 | `**Step 1 — Order ratio:**` | Filter | low | `filter` |
| `middle-math/user-context/cross-context-translation.md` | 97 | `**Step 2 — Rep adjustment:**` | Filter | low | `filter` |
| `middle-math/user-context/cross-context-translation.md` | 102 | `**Step 3 — Translation factor:**` | Filter | low | `filter` |
| `middle-math/user-context/cross-context-translation.md` | 105 | `**Step 4 — Apply to source performance:**` | Filter | low | `filter` |

## middle-math/user-context/exercise-ledger-spec.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/user-context/exercise-ledger-spec.md` | — | — | — | — | No inconsistencies found |

## middle-math/user-context/exercise-profile-spec.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/user-context/exercise-profile-spec.md` | — | — | — | — | No inconsistencies found |

## middle-math/user-context/toggle-system-spec.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/user-context/toggle-system-spec.md` | 23 | `**Effect:** The exercise is excluded from the selection pipeline's ...` | Filter | low | `filter` |

## middle-math/weights/README.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/weights/README.md` | — | — | — | — | No inconsistencies found |

## middle-math/weights/axis-weights.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/weights/axis-weights.md` | — | — | — | — | No inconsistencies found |

## middle-math/weights/block-weights.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/weights/block-weights.md` | 97 | `\| 🐂 Foundation \| +6 \| "Present in all Order block sequences." Br...` | Junction / Draft offering | low | `draft offering` |
| `middle-math/weights/block-weights.md` | 99 | `\| 🦋 Hypertrophy \| +6 \| "Always present." Logging volume and next...` | Junction / Draft offering | low | `draft offering` |
| `middle-math/weights/block-weights.md` | 101 | `\| 🌾 Full Body \| +6 \| "Always present." Bridge integration patter...` | Junction / Draft offering | low | `draft offering` |
| `middle-math/weights/block-weights.md` | 103 | `\| 🖼 Restoration \| +6 \| "Always present." Somatic session closing...` | Junction / Draft offering | low | `draft offering` |

## middle-math/weights/color-weights.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/weights/color-weights.md` | — | — | — | — | No inconsistencies found |

## middle-math/weights/interaction-rules.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/weights/interaction-rules.md` | 9 | `Priority order when dials conflict:` | Priority | low | `priority` |
| `middle-math/weights/interaction-rules.md` | 64 | `Date-derived weights apply as a **final ±1 adjustment** after all d...` | Resolution | low | `resolution` |
| `middle-math/weights/interaction-rules.md` | 75 | `- These apply on top of the already-resolved zip code weight vector` | Resolution | low | `resolution` |
| `middle-math/weights/interaction-rules.md` | 84 | `4. Resolve conflicts using hierarchy (Order > Color > Axis > Type):` | Resolution | low | `resolution` |

## middle-math/weights/operator-weights.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/weights/operator-weights.md` | 3 | `Status: WORKING DRAFT — First-pass derivation from scl-directory.md...` | Source map | low | `source map` |
| `middle-math/weights/operator-weights.md` | 381 | `\| 🚂 Junction \| +5 \| Junction block = writing the bridge to next ...` | Junction / Draft offering | low | `draft offering` |

## middle-math/weights/order-weights.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/weights/order-weights.md` | — | — | — | — | No inconsistencies found |

## middle-math/weights/type-weights.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/weights/type-weights.md` | — | — | — | — | No inconsistencies found |

## middle-math/weights/weight-system-spec.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `middle-math/weights/weight-system-spec.md` | 37 | `For any given zip code (ORDER AXIS TYPE COLOR), the weight vector i...` | Filter | low | `filter` |
| `middle-math/weights/weight-system-spec.md` | 39 | `### Step 1 — Primary Weights` | Filter | low | `filter` |
| `middle-math/weights/weight-system-spec.md` | 51 | `### Step 2 — Affinity Cascade` | Filter | low | `filter` |
| `middle-math/weights/weight-system-spec.md` | 57 | `### Step 3 — Suppression Cascade` | Filter | low | `filter` |
| `middle-math/weights/weight-system-spec.md` | 63 | `### Step 4 — Interaction Resolution` | Filter | low | `filter` |
| `middle-math/weights/weight-system-spec.md` | 63 | `### Step 4 — Interaction Resolution` | Resolution | low | `resolution` |
| `middle-math/weights/weight-system-spec.md` | 67 | `### Step 5 — Temporal Layer (optional)` | Filter | low | `filter` |
| `middle-math/weights/weight-system-spec.md` | 69 | `Date-derived weights apply a final ±1 adjustment. The current month...` | Resolution | low | `resolution` |
| `middle-math/weights/weight-system-spec.md` | 73 | `## Constraint Hierarchy for Interaction Resolution` | Resolution | low | `resolution` |

## scl-deep/README.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/README.md` | 21 | `\| operator-specifications.md \| 12 Operators semantic + monthly ca...` | Source map | low | `source map` |

## scl-deep/axis-specifications.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/axis-specifications.md` | 54 | `- Floor identity: The front page. Navigation hub. System map. Full ...` | Source map | low | `source map` |
| `scl-deep/axis-specifications.md` | 133 | `- Content: Personal workout queue, calendar views, 12-month Operato...` | Backpressure | low | `backpressure` |
| `scl-deep/axis-specifications.md` | 170 | `│   ├── firmitas/     — Front page, navigation, system map components` | Source map | low | `source map` |

## scl-deep/block-specifications.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/block-specifications.md` | 10 | `- card-template-v2.md` | Poka-yoke | low | `poka-yoke` |
| `scl-deep/block-specifications.md` | 53 | `- 🚂 Junction — always last before SAVE; the bridge forward` | Junction / Draft offering | low | `draft offering` |
| `scl-deep/block-specifications.md` | 507 | `**Role:** Bridge to next session. The transfer block. Always last b...` | Junction / Draft offering | low | `draft offering` |

## scl-deep/color-context-vernacular.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/color-context-vernacular.md` | 368 | `- "Give me space to process."` | Pipeline | medium | `pipeline` |
| `scl-deep/color-context-vernacular.md` | 392 | `\| Organization \| "Step one, step two, step three. 🔵" \|` | Filter | low | `filter` |
| `scl-deep/color-context-vernacular.md` | 521 | `\| ⚫️🟢 \| Grounded and steady \| "One step at a time. ⚫️🟢" \|` | Filter | low | `filter` |

## scl-deep/color-specifications.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/color-specifications.md` | 91 | `The four expressive poles of the Color system map to these stages w...` | Source map | low | `source map` |
| `scl-deep/color-specifications.md` | 227 | `🔵 Structured is the Planning tonal name: structured, calm, methodic...` | Filter | low | `filter` |
| `scl-deep/color-specifications.md` | 229 | `In publication: 🔵 frames structured analysis. "Step one, parse the ...` | Filter | low | `filter` |
| `scl-deep/color-specifications.md` | 440 | `🟠 carries terracotta warmth (#E07A3A range — not traffic orange, no...` | Source map | low | `source map` |
| `scl-deep/color-specifications.md` | 567 | `## Color Interaction Map` | Source map | low | `source map` |

## scl-deep/emoji-macros.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/emoji-macros.md` | 34 | `The Orders govern load, rep range, rest, and difficulty. They are t...` | Pipeline | medium | `pipeline` |
| `scl-deep/emoji-macros.md` | 34 | `The Orders govern load, rep range, rest, and difficulty. They are t...` | Source map | low | `source map` |
| `scl-deep/emoji-macros.md` | 83 | `What makes the butterfly uniquely apt for Hypertrophy is the nature...` | Pipeline | medium | `pipeline` |
| `scl-deep/emoji-macros.md` | 137 | `The scale does not prefer one side. It simply measures. And it is a...` | Filter | low | `filter` |
| `scl-deep/emoji-macros.md` | 479 | `The numbers 1-2-3: sequencing, ordering, the basic grammar of any s...` | Filter | low | `filter` |
| `scl-deep/emoji-macros.md` | 497 | `The ladder: ascending step by step. 🪜 is the loading ramp, the sequ...` | Filter | low | `filter` |
| `scl-deep/emoji-macros.md` | 533 | `The locomotive: the vehicle that runs on rails between stations. Th...` | Junction / Draft offering | low | `draft offering` |

## scl-deep/intercolumniation.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/intercolumniation.md` | — | — | — | — | No inconsistencies found |

## scl-deep/junction-web.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/junction-web.md` | 122 | `**Bridge nodes:** Balance addresses (⚖[Axis][Type][Color]) bridge c...` | Junction / Draft offering | low | `draft offering` |
| `scl-deep/junction-web.md` | 175 | `- It links forward past a required diagnostic step (e.g., linking f...` | Filter | low | `filter` |

## scl-deep/operator-specifications.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/operator-specifications.md` | 21 | `## Preamble: The ± Bridge` | Junction / Draft offering | low | `draft offering` |
| `scl-deep/operator-specifications.md` | 80 | `The 12 operators map to 12 months, creating a year-long rhythm of i...` | Source map | low | `source map` |
| `scl-deep/operator-specifications.md` | 118 | `**Agricultural resonance (January):** The farmer walks frozen field...` | Source map | low | `source map` |
| `scl-deep/operator-specifications.md` | 160 | `**As editorial verb:** *Fero* carries the argument forward — bridgi...` | Junction / Draft offering | low | `draft offering` |
| `scl-deep/operator-specifications.md` | 343 | `**Closing principle:** Every 🧮 SAVE carries a 1–2 sentence closing ...` | Junction / Draft offering | low | `draft offering` |

## scl-deep/order-etymology.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/order-etymology.md` | 10 | `architectural heritage of each Order and its mapping to training in...` | Source map | low | `source map` |
| `scl-deep/order-etymology.md` | 47 | `**Training mapping:** Foundation is the Tuscan of training. Sub-max...` | Source map | low | `source map` |
| `scl-deep/order-etymology.md` | 59 | `**Training mapping:** Strength is the Doric of training. 75–85% 1RM...` | Source map | low | `source map` |
| `scl-deep/order-etymology.md` | 71 | `**Training mapping:** Hypertrophy is the Ionic of training. 65–75% ...` | Source map | low | `source map` |
| `scl-deep/order-etymology.md` | 83 | `**Training mapping:** Performance is the Corinthian of training. 85...` | Source map | low | `source map` |
| `scl-deep/order-etymology.md` | 97 | `**Training mapping:** Full Body is the Composite of training. ~70% ...` | Source map | low | `source map` |
| `scl-deep/order-etymology.md` | 113 | `**Training mapping:** Balance is the Vitruvian of training. ~70% 1R...` | Source map | low | `source map` |
| `scl-deep/order-etymology.md` | 125 | `**Training mapping:** Restoration is the Palladian of training. ≤55...` | Source map | low | `source map` |
| `scl-deep/order-etymology.md` | 161 | `- Are there other architectural traditions worth mapping for potent...` | Source map | low | `source map` |
| `scl-deep/order-etymology.md` | 163 | `- Should the Vitruvian three principles — *firmitas, utilitas, venu...` | Source map | low | `source map` |

## scl-deep/order-specifications.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/order-specifications.md` | 84 | `The 🐂 character: the work is about building the neural map, not cha...` | Source map | low | `source map` |
| `scl-deep/order-specifications.md` | 346 | `- Each step increases load and decreases reps` | Filter | low | `filter` |
| `scl-deep/order-specifications.md` | 347 | `- Rest between steps: 2–3 minutes` | Filter | low | `filter` |
| `scl-deep/order-specifications.md` | 348 | `- Final step before test: 90%+ of test weight for 1 rep, 3+ min res...` | Filter | low | `filter` |
| `scl-deep/order-specifications.md` | 349 | `- The ramp informs the test attempt — if a step feels wrong, revise...` | Filter | low | `filter` |

## scl-deep/publication-standard.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/publication-standard.md` | 110 | `🔵 frames structured analysis. "Step one, parse the zip code. Step t...` | Filter | low | `filter` |
| `scl-deep/publication-standard.md` | 264 | `🔵 — The Structured Temperament. Methodical, calm, repeatable. This ...` | Filter | low | `filter` |
| `scl-deep/publication-standard.md` | 364 | `observe, notice, surface, name, discover, ground, anchor, carry, bu...` | Junction / Draft offering | low | `draft offering` |

## scl-deep/seasonal-density.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/seasonal-density.md` | 95 | `- **August (🦢 plico):** Fold the surplus. Volume accumulation peaks...` | Filter | low | `filter` |
| `scl-deep/seasonal-density.md` | 112 | `\| Volume relative \| Maintenance (step down from August) \| Mainte...` | Filter | low | `filter` |
| `scl-deep/seasonal-density.md` | 172 | `This produces a smooth sinusoidal density curve across the year, no...` | Filter | low | `filter` |

## scl-deep/systems-glossary.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/systems-glossary.md` | 31 | `\| Emit \| The Compiler \| The act of producing the final output ar...` | Filter | low | `filter` |
| `scl-deep/systems-glossary.md` | 31 | `\| Emit \| The Compiler \| The act of producing the final output ar...` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 33 | `\| Multi-pass \| The Compiler \| A pipeline where output from later...` | Multi-pass | medium | `multi-pass` |
| `scl-deep/systems-glossary.md` | 34 | `\| Transpile \| The Compiler \| Converting from one representation ...` | Filter | low | `filter` |
| `scl-deep/systems-glossary.md` | 35 | `\| Source map \| The Compiler \| A file that maps compiled output b...` | Source map | low | `source map` |
| `scl-deep/systems-glossary.md` | 46 | `\| Filter \| Unix / Factorio \| A single-purpose stateless transfor...` | Filter | low | `filter` |
| `scl-deep/systems-glossary.md` | 48 | `\| Tee \| Unix / Factorio \| A split that duplicates a data stream ...` | Backpressure | low | `backpressure` |
| `scl-deep/systems-glossary.md` | 50 | `\| Belt \| Unix / Factorio \| A resource stream with a maximum thro...` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 51 | `\| Backpressure \| Unix / Factorio \| When a downstream system sign...` | Pipeline | medium | `pipeline` |
| `scl-deep/systems-glossary.md` | 63 | `\| Event store \| Event Sourcing / Git \| The append-only log of al...` | Authoritative source | high | `authoritative source` |
| `scl-deep/systems-glossary.md` | 65 | `\| Snapshot \| Event Sourcing / Git \| A periodic materialization o...` | Authoritative source | high | `authoritative source` |
| `scl-deep/systems-glossary.md` | 76 | `## SECTION 4: RESOLUTION TERMS (DNS / MTG)` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 82 | `\| Resolution \| DNS / MTG \| The process of converting an address ...` | Pipeline | medium | `pipeline` |
| `scl-deep/systems-glossary.md` | 82 | `\| Resolution \| DNS / MTG \| The process of converting an address ...` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 83 | `\| Cache hit \| DNS / MTG \| When a resolved address already has st...` | Cache hit/miss | low | `cache hit/cache miss` |
| `scl-deep/systems-glossary.md` | 83 | `\| Cache hit \| DNS / MTG \| When a resolved address already has st...` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 84 | `\| Cache miss \| DNS / MTG \| When an address has no stored content...` | Cache hit/miss | low | `cache hit/cache miss` |
| `scl-deep/systems-glossary.md` | 84 | `\| Cache miss \| DNS / MTG \| When an address has no stored content...` | Backpressure | low | `backpressure` |
| `scl-deep/systems-glossary.md` | 84 | `\| Cache miss \| DNS / MTG \| When an address has no stored content...` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 85 | `\| Cache warming \| DNS / MTG \| Proactively resolving addresses be...` | Cache hit/miss | low | `cache hit/cache miss` |
| `scl-deep/systems-glossary.md` | 85 | `\| Cache warming \| DNS / MTG \| Proactively resolving addresses be...` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 87 | `\| Authoritative source \| DNS / MTG \| The origin document that ho...` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 88 | `\| Recursive resolver \| DNS / MTG \| An intermediary that checks c...` | Cache hit/miss | low | `cache hit/cache miss` |
| `scl-deep/systems-glossary.md` | 88 | `\| Recursive resolver \| DNS / MTG \| An intermediary that checks c...` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 89 | `\| Alias \| DNS / MTG \| Two names for the same address. Conversion...` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 90 | `\| Priority \| DNS / MTG \| The resolution order when multiple auth...` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 91 | `\| Layer system \| DNS / MTG \| A deterministic cascade for resolvi...` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 106 | `\| Poka-yoke \| PLC / Opus Magnum \| Mistake-proofing through struc...` | Poka-yoke | low | `poka-yoke` |
| `scl-deep/systems-glossary.md` | 152 | `\| Belt saturation \| Factorio / Kaizen \| Whether a resource strea...` | Cache hit/miss | low | `cache hit/cache miss` |
| `scl-deep/systems-glossary.md` | 152 | `\| Belt saturation \| Factorio / Kaizen \| Whether a resource strea...` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 168 | `\| Card YAML frontmatter \| Source map \| §1 Pipeline \|` | Source map | low | `source map` |
| `scl-deep/systems-glossary.md` | 170 | `\| Each card generation step \| Filter \| §2 Data Flow \|` | Filter | low | `filter` |
| `scl-deep/systems-glossary.md` | 171 | `\| YAML frontmatter struct between steps \| Pipe \| §2 Data Flow \|` | Filter | low | `filter` |
| `scl-deep/systems-glossary.md` | 172 | `\| Operis → edition + card queue \| Tee \| §2 Data Flow \|` | Backpressure | low | `backpressure` |
| `scl-deep/systems-glossary.md` | 188 | `\| Zip code → rendered workout \| Resolution \| §4 Resolution \|` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 189 | `\| GENERATED or CANONICAL card \| Cache hit \| §4 Resolution \|` | Cache hit/miss | low | `cache hit/cache miss` |
| `scl-deep/systems-glossary.md` | 189 | `\| GENERATED or CANONICAL card \| Cache hit \| §4 Resolution \|` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 190 | `\| EMPTY stub \| Cache miss \| §4 Resolution \|` | Cache hit/miss | low | `cache hit/cache miss` |
| `scl-deep/systems-glossary.md` | 190 | `\| EMPTY stub \| Cache miss \| §4 Resolution \|` | Resolution | low | `resolution` |
| `scl-deep/systems-glossary.md` | 191 | `\| Operis construction vehicle pipeline \| Cache warming \| §4 Reso...` | Cache hit/miss | low | `cache hit/cache miss` |
| `scl-deep/systems-glossary.md` | — | `... 19 additional matches truncated in this report` | — | — | — |

## scl-deep/type-specifications.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/type-specifications.md` | 249 | `- Single-leg: pistol squat, single-leg press, step-up` | Filter | low | `filter` |
| `scl-deep/type-specifications.md` | 259 | `2. Unilateral squat — Bulgarian split squat, single-leg press, pist...` | Filter | low | `filter` |
| `scl-deep/type-specifications.md` | 272 | `\| **Section G: Hips & Glutes — Squat/lunge patterns (#31–40, 180 t...` | Junction / Draft offering | low | `draft offering` |
| `scl-deep/type-specifications.md` | 282 | `\| 🔨 Functional \| Bulgarian split squat, single-leg press, step-up...` | Filter | low | `filter` |
| `scl-deep/type-specifications.md` | 291 | `- **🟢 Bodyweight (Tier 0–2):** Bodyweight squat, lunge, jump squat,...` | Junction / Draft offering | low | `draft offering` |
| `scl-deep/type-specifications.md` | 321 | `- Core stability as load transfer: transverse abdominis, obliques, ...` | Junction / Draft offering | low | `draft offering` |
| `scl-deep/type-specifications.md` | 469 | `- **🟠 Circuit (Tier 0–3):** Timed conditioning stations. No barbell...` | Filter | low | `filter` |

## scl-deep/vocabulary-standard.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-deep/vocabulary-standard.md` | 42 | `\| journey (training context) \| Spiritual-wellness register. \| "p...` | Pipeline | medium | `pipeline` |
| `scl-deep/vocabulary-standard.md` | 124 | `- bridge` | Junction / Draft offering | low | `draft offering` |

## scl-directory.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `scl-directory.md` | 280 | `🚂 JUNCTION — Pivot or transfer point. Mid-session = direction chang...` | Junction / Draft offering | low | `draft offering` |
| `scl-directory.md` | 305 | `When given a zip code, you execute these steps:` | Filter | low | `filter` |
| `scl-directory.md` | 307 | `Step 1: Parse the Zip Code` | Filter | low | `filter` |
| `scl-directory.md` | 314 | `Step 2: Derive the Default Operator` | Filter | low | `filter` |
| `scl-directory.md` | 317 | `Step 3: Derive the Block Sequence` | Filter | low | `filter` |
| `scl-directory.md` | 337 | `Step 4: Select Exercises` | Filter | low | `filter` |
| `scl-directory.md` | 345 | `Step 5: Format the Workout` | Filter | low | `filter` |
| `scl-directory.md` | 361 | `14. 🚂 JUNCTION with logging space and next-session bridge` | Junction / Draft offering | low | `draft offering` |
| `scl-directory.md` | 444 | `Day-of-week Order mapping and design implications:` | Source map | low | `source map` |
| `scl-directory.md` | 530 | `│   • 10 🍗 Glute Bridge (single leg, 5/5, pause 2 sec top)` | Junction / Draft offering | low | `draft offering` |
| `scl-directory.md` | 593 | `├─ Next session bridge: Posterior chain work today stabilizes` | Junction / Draft offering | low | `draft offering` |
| `scl-directory.md` | 670 | `Orders also carry architectural names. These aren't random — they'r...` | Source map | low | `source map` |
| `scl-directory.md` | 701 | `Polysemic behavior: 🐂 with ⚫ Teaching is pure education — coaching ...` | Filter | low | `filter` |
| `scl-directory.md` | 832 | `- 🌾🍗 = Legs-dominant integration (squat cleans, step-up to press, s...` | Filter | low | `filter` |
| `scl-directory.md` | 969 | `Movement patterns: Squat patterns (back squat, front squat, goblet ...` | Filter | low | `filter` |
| `scl-directory.md` | 1036 | `Example exercises: Split squats, Bulgarian split squats, farmer car...` | Filter | low | `filter` |
| `scl-directory.md` | 1177 | `Session character: Patient. Step-by-step. Numbered cues. Room to as...` | Filter | low | `filter` |
| `scl-directory.md` | 1429 | `How it differs from 🪞 Vanity: Sculpt is more structured, heavier, a...` | Pipeline | medium | `pipeline` |
| `scl-directory.md` | 1485 | `- End-session: Carryover. What carries into the next workout. Loggi...` | Junction / Draft offering | low | `draft offering` |
| `scl-directory.md` | 1545 | `Step 1: Pick Your Code` | Filter | low | `filter` |
| `scl-directory.md` | 1559 | `Step 2: Choose Your Blocks` | Filter | low | `filter` |
| `scl-directory.md` | 1584 | `Step 3: Write the Workout in Markdown` | Filter | low | `filter` |
| `scl-directory.md` | 1586 | `Every submission must use the standard SCL workout format. This is ...` | Poka-yoke | low | `poka-yoke` |
| `scl-directory.md` | 1606 | `│   • 10 🍗 Glute Bridge (single leg, 5/5, pause 2 sec at the top)` | Junction / Draft offering | low | `draft offering` |
| `scl-directory.md` | 1684 | `├─ Next session bridge: This pulling volume sets up Thursday's` | Junction / Draft offering | low | `draft offering` |
| `scl-directory.md` | 1705 | `Step 4: Check Your Work` | Filter | low | `filter` |
| `scl-directory.md` | 1758 | `All submissions must be in markdown (.md) format following the SCL ...` | Poka-yoke | low | `poka-yoke` |
| `scl-directory.md` | 1844 | `Goal Mapping — "I want to..."` | Source map | low | `source map` |

## seeds/README.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/README.md` | 19 | `\| junction-community.md \| 🚂 Junction evolves into living communit...` | Backpressure | low | `backpressure` |
| `seeds/README.md` | 52 | `## Phase Relevance Map` | Source map | low | `source map` |

## seeds/almanac-8day-rotation.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/almanac-8day-rotation.md` | 42 | `This is not mandatory ordering. A new user could begin at any point...` | Backpressure | low | `backpressure` |
| `seeds/almanac-8day-rotation.md` | 97 | `## Almanac Queue Override` | Backpressure | low | `backpressure` |
| `seeds/almanac-8day-rotation.md` | 101 | `The rotation resumes the following day from wherever it left off. T...` | Backpressure | low | `backpressure` |

## seeds/almanac-macro-operators.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/almanac-macro-operators.md` | 17 | `## The Monthly Mapping` | Source map | low | `source map` |
| `seeds/almanac-macro-operators.md` | 59 | `The farmer's January: Walk the fields when they're frozen. Map posi...` | Source map | low | `source map` |
| `seeds/almanac-macro-operators.md` | 86 | `The farmer's October: Final harvests. Cover crop seeding. Equipment...` | Resolution | low | `resolution` |

## seeds/almanac-room-bloom.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/almanac-room-bloom.md` | — | — | — | — | No inconsistencies found |

## seeds/art-direction.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/art-direction.md` | — | — | — | — | No inconsistencies found |

## seeds/automotive-layer-architecture.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/automotive-layer-architecture.md` | 24 | `- Process yesterday's session (what worked, what to do next)` | Pipeline | medium | `pipeline` |
| `seeds/automotive-layer-architecture.md` | 28 | `The car is not where people log sets. It is where people prime for ...` | Backpressure | low | `backpressure` |
| `seeds/automotive-layer-architecture.md` | 33 | `- The 7 Orders map cleanly to days of the week (natural spoken cont...` | Source map | low | `source map` |
| `seeds/automotive-layer-architecture.md` | 130 | `### Steering Wheel Button Mapping` | Source map | low | `source map` |
| `seeds/automotive-layer-architecture.md` | 258 | `Generated audio cached per card version (zip_code + card_status). G...` | Cache hit/miss | low | `cache hit/cache miss` |

## seeds/axis-as-app-floors.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/axis-as-app-floors.md` | 22 | `\| 🏛 Firmitas \| Bilateral, barbell-first, stable classics \| Front...` | Source map | low | `source map` |
| `seeds/axis-as-app-floors.md` | 38 | `- The 42-deck grid as a navigable map` | Source map | low | `source map` |
| `seeds/axis-as-app-floors.md` | 45 | `**Relationship to workout card:** The card appears as a point on a ...` | Source map | low | `source map` |
| `seeds/axis-as-app-floors.md` | 112 | `- The Almanac itself — the user's personal workout queue and rotation` | Backpressure | low | `backpressure` |

## seeds/claude-code-build-sequence.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/claude-code-build-sequence.md` | 16 | `This document is the execution roadmap for building the PPL± experi...` | Filter | low | `filter` |
| `seeds/claude-code-build-sequence.md` | 178 | `2. Build onboarding flow (`/onboarding`): 3-step modal after first ...` | Filter | low | `filter` |
| `seeds/claude-code-build-sequence.md` | 179 | `- Step 1: Equipment selection (which tiers do you have access to?)` | Filter | low | `filter` |
| `seeds/claude-code-build-sequence.md` | 180 | `- Step 2: Region selection (see `seeds/regional-filter-architecture...` | Filter | low | `filter` |
| `seeds/claude-code-build-sequence.md` | 181 | `- Step 3: First zip suggestion (today's Operis recommendation)` | Filter | low | `filter` |
| `seeds/claude-code-build-sequence.md` | 326 | `**Goal:** The room content area is a zoomable canvas with deck map ...` | Source map | low | `source map` |
| `seeds/claude-code-build-sequence.md` | 333 | `3. At 0.25x: show deck map — 40-room grid with current zip highlighted` | Source map | low | `source map` |
| `seeds/claude-code-build-sequence.md` | 336 | `6. Tap on room in deck map → navigate to that zip` | Source map | low | `source map` |
| `seeds/claude-code-build-sequence.md` | 344 | `- Further pinch out shows deck map` | Source map | low | `source map` |
| `seeds/claude-code-build-sequence.md` | 346 | `- Tap zip in deck map → navigate to room` | Source map | low | `source map` |
| `seeds/claude-code-build-sequence.md` | 420 | `- Production URL resolves and loads` | Resolution | low | `resolution` |
| `seeds/claude-code-build-sequence.md` | 444 | `6. Cache generated audio in Supabase Storage (invalidate on card up...` | Cache hit/miss | low | `cache hit/cache miss` |
| `seeds/claude-code-build-sequence.md` | 454 | `2. Map moods to Spotify and Apple Music search queries or playlist IDs` | Source map | low | `source map` |
| `seeds/claude-code-build-sequence.md` | 469 | `4. Steering wheel button mapping: next block, pause/resume` | Source map | low | `source map` |
| `seeds/claude-code-build-sequence.md` | 504 | `## Dependency Map` | Source map | low | `source map` |

## seeds/codex-audit-agents-friendly-expansion.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/codex-audit-agents-friendly-expansion.md` | 28 | `## Workstream A — Deck expansion pipeline (highest leverage)` | Pipeline | medium | `pipeline` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 35 | `- Coverage map ensuring 8 color variants per Type do not reuse the ...` | Source map | low | `source map` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 55 | `### A3) Retrofit Deck 07 flagged regen queue` | Backpressure | low | `backpressure` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 64 | `- Deterministic regeneration from identity mapping.` | Source map | low | `source map` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 69 | `## Workstream B — Constraint automation and linting` | Pipeline | medium | `pipeline` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 79 | `- Define canonical schema fields from current card template.` | Poka-yoke | low | `poka-yoke` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 100 | `- Optional CI workflow in warn-only mode.` | Pipeline | high | `pipeline` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 108 | `## Workstream C — Middle-math readiness for deterministic selection` | Pipeline | medium | `pipeline` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 145 | `## Workstream D — Junction intelligence and bridge quality` | Pipeline | medium | `pipeline` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 145 | `## Workstream D — Junction intelligence and bridge quality` | Junction / Draft offering | low | `draft offering` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 171 | `## Workstream E — Data and repository operations` | Pipeline | medium | `pipeline` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 174 | `**Goal:** single source of truth for generation status and quality ...` | Authoritative source | high | `authoritative source` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 207 | `## Workstream F — Agent systemization (Codex-first)` | Pipeline | medium | `pipeline` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 235 | `- Templates for "build identity", "generate batch", "audit deck", "...` | Backpressure | low | `backpressure` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 236 | `- Checklists integrated with current whiteboard workflow.` | Pipeline | high | `pipeline` |
| `seeds/codex-audit-agents-friendly-expansion.md` | 250 | `5. **Deck 07 regen queue cleanup (A3)**` | Backpressure | low | `backpressure` |

## seeds/content-types-architecture.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/content-types-architecture.md` | 33 | `4. The Deck Identity — exercise mapping and generation context per ...` | Source map | low | `source map` |
| `seeds/content-types-architecture.md` | 59 | `25. The Skill Definition — one of 5 Claude Code skills. Invoke synt...` | Filter | low | `filter` |
| `seeds/content-types-architecture.md` | 67 | `33. The Deck Identity Template — the blank template for new identit...` | Poka-yoke | low | `poka-yoke` |
| `seeds/content-types-architecture.md` | 71 | `37. The CI Workflow — GitHub Actions validation pipeline. Planned.` | Pipeline | high | `pipeline` |
| `seeds/content-types-architecture.md` | 72 | `38. The Cosmogram Research Prompt — the research template for deck ...` | Poka-yoke | low | `poka-yoke` |
| `seeds/content-types-architecture.md` | 140 | `91. The Moon Phase Display — current lunar position with zip code m...` | Source map | low | `source map` |
| `seeds/content-types-architecture.md` | 143 | `94. The Cultural Calendar Entry — a notable date with zip code mapp...` | Source map | low | `source map` |
| `seeds/content-types-architecture.md` | 163 | `109. The Coaching Program Template — a Jake-designed program offere...` | Poka-yoke | low | `poka-yoke` |
| `seeds/content-types-architecture.md` | 204 | `The 7 Orders map to 7 curriculum depth levels. Content types have a...` | Source map | low | `source map` |
| `seeds/content-types-architecture.md` | 206 | `This is the Trivium/Quadrivium mapping from the weekly editorial ca...` | Source map | low | `source map` |

## seeds/cosmogram-research-prompt.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/cosmogram-research-prompt.md` | 54 | `The Orders also map 1:1 to the 7 Liberal Arts (Trivium + Quadrivium...` | Source map | low | `source map` |
| `seeds/cosmogram-research-prompt.md` | 156 | `Named phases within a workflow. The name is fixed. The content shif...` | Pipeline | high | `pipeline` |
| `seeds/cosmogram-research-prompt.md` | 164 | `Seasonal/Calendrical. The Orders map to the annual cycle. Observati...` | Source map | low | `source map` |
| `seeds/cosmogram-research-prompt.md` | 172 | `Fractal/Nested Structure. The 7 Orders appear at every scale. Week ...` | Filter | low | `filter` |
| `seeds/cosmogram-research-prompt.md` | 296 | `Agriculture, Ecology & Seasonal Wisdom. Agricultural practices and ...` | Source map | low | `source map` |
| `seeds/cosmogram-research-prompt.md` | 300 | `Philosophy, Systems Thinking & Ways of Knowing. Philosophical tradi...` | Pipeline | medium | `pipeline` |

## seeds/daily-architecture.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/daily-architecture.md` | 70 | `Each event entry carries: the year, the event (1–2 sentences, tight...` | Source map | low | `source map` |
| `seeds/daily-architecture.md` | 98 | `Contents: next 3–7 days of notable dates (historical, astronomical,...` | Source map | low | `source map` |
| `seeds/daily-architecture.md` | 114 | `### 🚂 JUNCTION — Navigation Bridge` | Junction / Draft offering | low | `draft offering` |
| `seeds/daily-architecture.md` | 120 | `The 🚂 Junction is the recommendation engine's surface. In the Daily...` | Junction / Draft offering | low | `draft offering` |
| `seeds/daily-architecture.md` | 147 | `Inputs: historical research (encyclopedic sources, this-day-in-hist...` | Source map | low | `source map` |
| `seeds/daily-architecture.md` | 216 | `- How does the Daily interact with the user's Almanac queue? (Does ...` | Backpressure | low | `backpressure` |

## seeds/data-ethics-architecture.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/data-ethics-architecture.md` | 74 | `- Any cross-site identity resolution SDK` | Resolution | low | `resolution` |

## seeds/deck-campaign-workflow.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/deck-campaign-workflow.md` | 1 | `# Seed: Deck Campaign Workflow` | Pipeline | high | `pipeline` |
| `seeds/deck-campaign-workflow.md` | 25 | `LANE B: Identity Doc     — Exercise mapping, duplicate audit, regen...` | Backpressure | low | `backpressure` |
| `seeds/deck-campaign-workflow.md` | 25 | `LANE B: Identity Doc     — Exercise mapping, duplicate audit, regen...` | Source map | low | `source map` |
| `seeds/deck-campaign-workflow.md` | 35 | `- E requires D (audit must pass before review queue opens)` | Backpressure | low | `backpressure` |
| `seeds/deck-campaign-workflow.md` | 44 | `**Wave selection criteria (in priority order):**` | Priority | low | `priority` |
| `seeds/deck-campaign-workflow.md` | 71 | `- ⚠️ Complete with known issues (regen queue active)` | Backpressure | low | `backpressure` |
| `seeds/deck-campaign-workflow.md` | 92 | `The process is:` | Pipeline | medium | `pipeline` |
| `seeds/deck-campaign-workflow.md` | 104 | `Both Deck 07 and Deck 08 were generated before this workflow existe...` | Pipeline | high | `pipeline` |
| `seeds/deck-campaign-workflow.md` | 112 | `Needs: full Lane C completion (regen queue), Lane D, Lane E.` | Backpressure | low | `backpressure` |
| `seeds/deck-campaign-workflow.md` | 119 | `- Campaign state view in `whiteboard.md` as the permanent source of...` | Authoritative source | high | `authoritative source` |
| `seeds/deck-campaign-workflow.md` | 133 | `Until then, this seed informs session planning but the whiteboard r...` | Authoritative source | high | `authoritative source` |

## seeds/default-almanac-preset.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/default-almanac-preset.md` | 157 | `queue: []  (empty — no zip codes queued)` | Backpressure | low | `backpressure` |

## seeds/default-rotation-engine.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/default-rotation-engine.md` | 118 | `The Almanac queue (seeds/almanac-8day-rotation.md) sits on TOP of t...` | Backpressure | low | `backpressure` |

## seeds/elevator-architecture.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/elevator-architecture.md` | 73 | `The six Axes map to six floors in every building. The floor stack f...` | Source map | low | `source map` |
| `seeds/elevator-architecture.md` | 90 | `### How the Floors Map to the Scroll Experience` | Source map | low | `source map` |

## seeds/exercise-attribute-tagging.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/exercise-attribute-tagging.md` | 39 | `~2,800 exercises × 11 attributes + flags = significant tagging effo...` | Pipeline | medium | `pipeline` |

## seeds/exercise-superscript.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/exercise-superscript.md` | — | — | — | — | No inconsistencies found |

## seeds/experience-layer-blueprint.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/experience-layer-blueprint.md` | — | — | — | — | No inconsistencies found |

## seeds/git-worktree-pattern.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/git-worktree-pattern.md` | — | — | — | — | No inconsistencies found |

## seeds/junction-community.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/junction-community.md` | 9 | `# 🚂 Junction — Community Layer & Almanac Queue` | Backpressure | low | `backpressure` |
| `seeds/junction-community.md` | 21 | `Junction renders static suggestions as tappable zip code links. Sel...` | Backpressure | low | `backpressure` |
| `seeds/junction-community.md` | 30 | `- The Almanac is a queue, not a calendar. No scheduling, no time sl...` | Backpressure | low | `backpressure` |
| `seeds/junction-community.md` | 41 | `- Does the Almanac queue have a max depth?` | Backpressure | low | `backpressure` |

## seeds/linters-architecture.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/linters-architecture.md` | 48 | `- `.github/workflows/lint.yml` — runs all 3 tiers on push/PR agains...` | Pipeline | high | `pipeline` |
| `seeds/linters-architecture.md` | 57 | `- CI workflow (`lint.yml`) needs to be written` | Pipeline | high | `pipeline` |
| `seeds/linters-architecture.md` | 76 | `└── workflows/` | Pipeline | high | `pipeline` |

## seeds/mobile-ui-architecture.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/mobile-ui-architecture.md` | 66 | `│  🦋  🔨  🍗  🟣        │  ← One step each direction` | Filter | low | `filter` |
| `seeds/mobile-ui-architecture.md` | 164 | `**At 0.25x (full out):** Deck map. The current zip is highlighted i...` | Source map | low | `source map` |
| `seeds/mobile-ui-architecture.md` | 192 | `4. Pinch to zoom out → See deck map` | Source map | low | `source map` |
| `seeds/mobile-ui-architecture.md` | 216 | `Dial panel stays at bottom but uses wider column format. Drawer can...` | Source map | low | `source map` |
| `seeds/mobile-ui-architecture.md` | 221 | `**Design principle:** The mobile layout is not a simplified version...` | Fizzle | medium | `fizzle` |

## seeds/numeric-zip-system.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/numeric-zip-system.md` | 87 | `const [o, a, t, c] = zip.split('').map(Number);` | Source map | low | `source map` |
| `seeds/numeric-zip-system.md` | 102 | `const [o, a, t, c] = zip.split('').map(Number);` | Source map | low | `source map` |

## seeds/operis-architecture.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/operis-architecture.md` | 53 | `**The generation engine.** Every edition of the Operis features 8–1...` | Backpressure | low | `backpressure` |
| `seeds/operis-architecture.md` | 131 | `Editorial character: Geometry is integration — the study of how par...` | Resolution | low | `resolution` |
| `seeds/operis-architecture.md` | 182 | `\| Junction Bridge \| 🚂 \| Yes \| All Orders \|` | Junction / Draft offering | low | `draft offering` |
| `seeds/operis-architecture.md` | 200 | `## The Operis ↔ Cosmogram Feedback Loop` | Multi-pass | medium | `multi-pass` |
| `seeds/operis-architecture.md` | 208 | `**The feedback loop in practice:** The Operis editorial team (Jake,...` | Multi-pass | medium | `multi-pass` |
| `seeds/operis-architecture.md` | 210 | `The Operis does not block on cosmograms. An edition can feature any...` | Multi-pass | medium | `multi-pass` |
| `seeds/operis-architecture.md` | 257 | `## Temporal Context — Reverse-Weight Resolution` | Resolution | low | `resolution` |
| `seeds/operis-architecture.md` | 261 | `The Intention department frames today as the resolution between yes...` | Resolution | low | `resolution` |
| `seeds/operis-architecture.md` | 263 | `The featured Sandbox room is the reverse-weight resolution room — t...` | Resolution | low | `resolution` |
| `seeds/operis-architecture.md` | 265 | `The algorithm is specified in `middle-math/rotation/reverse-weight-...` | Resolution | low | `resolution` |
| `seeds/operis-architecture.md` | 273 | `**Layout**: Masthead on the left. Almanac box on the right. Content...` | Source map | low | `source map` |
| `seeds/operis-architecture.md` | 296 | `Every symbol in the almanac box is tappable in the experience layer...` | Source map | low | `source map` |
| `seeds/operis-architecture.md` | 302 | `**Symbol Map (bottom of card)**:` | Source map | low | `source map` |
| `seeds/operis-architecture.md` | 304 | `A compact legend decoding every symbol used on the front page card....` | Source map | low | `source map` |
| `seeds/operis-architecture.md` | 342 | `**Prompt 3 — The Editor.** (`seeds/operis-editor-prompt.md`) Writes...` | Source map | low | `source map` |
| `seeds/operis-architecture.md` | 388 | `⚫ The Order of the day is the law. If it is Tuesday and the Order i...` | Backpressure | low | `backpressure` |
| `seeds/operis-architecture.md` | 414 | `- How does the Operis interact with the user's Almanac queue? (Does...` | Backpressure | low | `backpressure` |
| `seeds/operis-architecture.md` | 420 | `- How does the 13-room Sandbox structure interact with the zip coun...` | Resolution | low | `resolution` |

## seeds/operis-builder-prompt.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/operis-builder-prompt.md` | 38 | `You are the Builder for the PPL± Operis. You are the last step in t...` | Filter | low | `filter` |
| `seeds/operis-builder-prompt.md` | 87 | `3. Generate the card following the complete generation sequence in ...` | Filter | low | `filter` |

## seeds/operis-color-posture.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/operis-color-posture.md` | 41 | `**🟢 Think like a gardener.** Today is a steady, organic day. The wo...` | Pipeline | medium | `pipeline` |
| `seeds/operis-color-posture.md` | 43 | `**🔵 Think like an architect.** Today rewards structure and method. ...` | Filter | low | `filter` |

## seeds/operis-content-architect-prompt.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/operis-content-architect-prompt.md` | 57 | `- Historical events have physical implication notes (you need these...` | Source map | low | `source map` |
| `seeds/operis-content-architect-prompt.md` | 69 | `3. **Monthly operator** — what is the operator's natural Color affi...` | Source map | low | `source map` |
| `seeds/operis-content-architect-prompt.md` | 105 | `Produce: the word, its Latin derivation path (2–3 steps), and one s...` | Filter | low | `filter` |
| `seeds/operis-content-architect-prompt.md` | 109 | `## Cross-Domain Connections Map` | Source map | low | `source map` |
| `seeds/operis-content-architect-prompt.md` | 120 | `## Content Room Mapping Preparation` | Source map | low | `source map` |
| `seeds/operis-content-architect-prompt.md` | 122 | `Review the historical events with physical implication notes from B...` | Source map | low | `source map` |
| `seeds/operis-content-architect-prompt.md` | 126 | `These are suggestions for Prompt 3, not prescriptions. Prompt 3 (th...` | Source map | low | `source map` |

## seeds/operis-editor-prompt.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/operis-editor-prompt.md` | 109 | `- **Masthead** — Front page card: masthead (left) with Almanac box ...` | Source map | low | `source map` |
| `seeds/operis-editor-prompt.md` | 188 | `- Do not put editorial content in zip-code titles. Titles follow Ex...` | Junction / Draft offering | low | `draft offering` |

## seeds/operis-educational-layer.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/operis-educational-layer.md` | 42 | `Domain: Financial literacy, legal basics, civic process, tax struct...` | Pipeline | medium | `pipeline` |
| `seeds/operis-educational-layer.md` | 46 | `Search guidance (for Prompt 2): Tax deadlines and financial plannin...` | Pipeline | medium | `pipeline` |
| `seeds/operis-educational-layer.md` | 68 | `Content character: This lane delivers systems knowledge in the 🔵 re...` | Filter | low | `filter` |
| `seeds/operis-educational-layer.md` | 98 | `Domain: Current events that demand attention, civic engagement, vot...` | Pipeline | medium | `pipeline` |
| `seeds/operis-educational-layer.md` | 102 | `Search guidance (for Prompt 2): Current events directly affecting h...` | Pipeline | medium | `pipeline` |
| `seeds/operis-educational-layer.md` | 112 | `Domain: Communication skills, conflict resolution, community buildi...` | Resolution | low | `resolution` |
| `seeds/operis-educational-layer.md` | 194 | `**Historical Desk (📰)** — Historical articles can pivot naturally i...` | Junction / Draft offering | low | `draft offering` |

## seeds/operis-naming-rationale.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/operis-naming-rationale.md` | — | — | — | — | No inconsistencies found |

## seeds/operis-prompt-pipeline.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/operis-prompt-pipeline.md` | 15 | `- middle-math/rotation/reverse-weight-resolution.md` | Resolution | low | `resolution` |
| `seeds/operis-prompt-pipeline.md` | 58 | `by mapping Operis content to zip codes. Writes all 13 room` | Source map | low | `source map` |
| `seeds/operis-prompt-pipeline.md` | 148 | `Connections Map` | Source map | low | `source map` |
| `seeds/operis-prompt-pipeline.md` | 229 | `\| Junction Bridge \| 🚂 \| ✓ \| ✓ \| ✓ \| ✓ \| ✓ \| ✓ \| ✓ \|` | Junction / Draft offering | low | `draft offering` |
| `seeds/operis-prompt-pipeline.md` | 267 | `Read Axis (position 2) and Color (position 4). Preparatory Colors (...` | Source map | low | `source map` |
| `seeds/operis-prompt-pipeline.md` | 294 | `**Phase C:** `seeds/operis-editor-prompt.md` runs in Claude Code, c...` | Filter | low | `filter` |
| `seeds/operis-prompt-pipeline.md` | 294 | `**Phase C:** `seeds/operis-editor-prompt.md` runs in Claude Code, c...` | Source map | low | `source map` |
| `seeds/operis-prompt-pipeline.md` | 300 | `The manual pipeline is the v1. The automation pipeline is the same ...` | Filter | low | `filter` |

## seeds/operis-researcher-prompt.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/operis-researcher-prompt.md` | 58 | `Historical events should span multiple domains: athletics and sport...` | Source map | low | `source map` |
| `seeds/operis-researcher-prompt.md` | 67 | `Fields: date, 5–8 events (year, description, domain tag, physical i...` | Junction / Draft offering | low | `draft offering` |

## seeds/operis-sandbox-structure.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/operis-sandbox-structure.md` | 9 | `- middle-math/rotation/reverse-weight-resolution.md` | Resolution | low | `resolution` |
| `seeds/operis-sandbox-structure.md` | 57 | `The principle: The Operis publishes knowledge. The 5 Content Rooms ...` | Junction / Draft offering | low | `draft offering` |
| `seeds/operis-sandbox-structure.md` | 81 | `## Content-to-Zip Mapping` | Source map | low | `source map` |
| `seeds/operis-sandbox-structure.md` | 85 | `The mapping chain:` | Source map | low | `source map` |
| `seeds/operis-sandbox-structure.md` | 96 | `**Mapping examples:**` | Source map | low | `source map` |
| `seeds/operis-sandbox-structure.md` | 98 | `Content: "1883 — Brooklyn Bridge opens. 14 years of construction. W...` | Junction / Draft offering | low | `draft offering` |
| `seeds/operis-sandbox-structure.md` | 119 | `The editor must think through the full constraint space. If a natur...` | Source map | low | `source map` |
| `seeds/operis-sandbox-structure.md` | 133 | `- ⛽🪐➕🟣±🪵 The Brooklyn Bridge Room` | Junction / Draft offering | low | `draft offering` |
| `seeds/operis-sandbox-structure.md` | 139 | `A user who discovers ⛽🪐➕🟣 six months later finds a workout called "...` | Junction / Draft offering | low | `draft offering` |
| `seeds/operis-sandbox-structure.md` | 181 | `## Relationship to Reverse-Weight Resolution` | Resolution | low | `resolution` |
| `seeds/operis-sandbox-structure.md` | 183 | `The reverse-weight resolution algorithm (`middle-math/rotation/reve...` | Resolution | low | `resolution` |
| `seeds/operis-sandbox-structure.md` | 187 | `For the 5 Content Rooms, the reverse-weight logic is secondary to t...` | Source map | low | `source map` |
| `seeds/operis-sandbox-structure.md` | 187 | `For the 5 Content Rooms, the reverse-weight logic is secondary to t...` | Resolution | low | `resolution` |
| `seeds/operis-sandbox-structure.md` | 189 | `The featured room is always the reverse-weight resolution of the Co...` | Resolution | low | `resolution` |
| `seeds/operis-sandbox-structure.md` | 206 | `## Content-to-Zip Mapping Chain` | Source map | low | `source map` |
| `seeds/operis-sandbox-structure.md` | 208 | `The mapping moves from content toward workout, not the other way:` | Source map | low | `source map` |
| `seeds/operis-sandbox-structure.md` | 220 | `Content decides Type and Axis. The Editor chooses Color. Order is f...` | Source map | low | `source map` |
| `seeds/operis-sandbox-structure.md` | 222 | `Example chain: A historical event about a 19th-century laborer carr...` | Junction / Draft offering | low | `draft offering` |
| `seeds/operis-sandbox-structure.md` | 235 | `**Incorrect:** "Bridge Builder's Hip Hinge" (editorial reference in...` | Junction / Draft offering | low | `draft offering` |
| `seeds/operis-sandbox-structure.md` | 238 | `A user finding this zip code six months from now via search, commun...` | Backpressure | low | `backpressure` |
| `seeds/operis-sandbox-structure.md` | 257 | `- How does the Content Room system interact with the user's Almanac...` | Backpressure | low | `backpressure` |

## seeds/platform-architecture-v1-archive.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/platform-architecture-v1-archive.md` | 10 | `onboarding layer. Elevator model resolved (4 dials = building/floor...` | Resolution | low | `resolution` |
| `seeds/platform-architecture-v1-archive.md` | 699 | `## The 🧮 SAVE Workflow` | Pipeline | high | `pipeline` |
| `seeds/platform-architecture-v1-archive.md` | 943 | `pool = [...new Set(pool.map(w => w.workout_id))];` | Source map | low | `source map` |
| `seeds/platform-architecture-v1-archive.md` | 1287 | `let pool = [...saved.map(s => s.workout_id), ...completed.map(c => ...` | Source map | low | `source map` |
| `seeds/platform-architecture-v1-archive.md` | 1331 | `**Jake's Workflow:**` | Pipeline | high | `pipeline` |
| `seeds/platform-architecture-v1-archive.md` | 1375 | `**Jake's Workflow:**` | Pipeline | high | `pipeline` |
| `seeds/platform-architecture-v1-archive.md` | 1425 | `**Jake's Workflow:**` | Pipeline | high | `pipeline` |
| `seeds/platform-architecture-v1-archive.md` | 1451 | `**Daily Workflows:**` | Pipeline | high | `pipeline` |
| `seeds/platform-architecture-v1-archive.md` | 1473 | `Jake checks moderation queue 1×/day (15 min)` | Backpressure | low | `backpressure` |
| `seeds/platform-architecture-v1-archive.md` | 1651 | `- Approval workflow (Jake's admin panel)` | Pipeline | high | `pipeline` |
| `seeds/platform-architecture-v1-archive.md` | 1652 | `- Continuous learning (feedback loop)` | Multi-pass | medium | `multi-pass` |
| `seeds/platform-architecture-v1-archive.md` | 1746 | `- ✅ User experience (card deck metaphor, workflows)` | Pipeline | high | `pipeline` |
| `seeds/platform-architecture-v1-archive.md` | 1751 | `**Next steps (as of February 11, 2026 — superseded by V2):**` | Filter | low | `filter` |

## seeds/platform-architecture-v2.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/platform-architecture-v2.md` | 167 | `### The 🧮 SAVE Workflow` | Pipeline | high | `pipeline` |
| `seeds/platform-architecture-v2.md` | 316 | `Exercise library expansion — adding new exercises requires coaching...` | Source map | low | `source map` |

## seeds/regional-filter-architecture.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/regional-filter-architecture.md` | 84 | `For other Level 1 regions: similar sub-region lists with 8-12 optio...` | Source map | low | `source map` |
| `seeds/regional-filter-architecture.md` | 86 | `**UI implementation:** Standard two-step select, not a map. No visu...` | Filter | low | `filter` |
| `seeds/regional-filter-architecture.md` | 86 | `**UI implementation:** Standard two-step select, not a map. No visu...` | Source map | low | `source map` |
| `seeds/regional-filter-architecture.md` | 149 | `1. Add region picker as Step 2 of onboarding (after equipment selec...` | Filter | low | `filter` |

## seeds/scl-emoji-macros-draft.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/scl-emoji-macros-draft.md` | — | — | — | — | No inconsistencies found |

## seeds/scl-envelope-architecture.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/scl-envelope-architecture.md` | 27 | `- middle-math/rotation/reverse-weight-resolution.md` | Resolution | low | `resolution` |
| `seeds/scl-envelope-architecture.md` | 171 | `The cosmogram is the editorial seed that starts this process. The a...` | Pipeline | medium | `pipeline` |
| `seeds/scl-envelope-architecture.md` | 196 | `The pin's zip code field is optional. If the user is inside a room ...` | Source map | low | `source map` |
| `seeds/scl-envelope-architecture.md` | 238 | `The Map as Envelope Visualization` | Source map | low | `source map` |
| `seeds/scl-envelope-architecture.md` | 240 | `The 🔨 Utilitas floor includes a map layer. The map is a geographic ...` | Source map | low | `source map` |
| `seeds/scl-envelope-architecture.md` | 246 | `At low zoom (state/multi-state level): the map shows condition zone...` | Source map | low | `source map` |
| `seeds/scl-envelope-architecture.md` | 248 | `The map renders in the noli plan figure-ground style described in s...` | Source map | low | `source map` |
| `seeds/scl-envelope-architecture.md` | 250 | `The map does not use GPS for tracking. It uses the user's selected ...` | Source map | low | `source map` |
| `seeds/scl-envelope-architecture.md` | 252 | `In the automotive layer (Android Auto, CarPlay), the map is the pri...` | Source map | low | `source map` |
| `seeds/scl-envelope-architecture.md` | 304 | `Phase E — Map layer. The 🔨 Utilitas floor renders pinned content on...` | Source map | low | `source map` |
| `seeds/scl-envelope-architecture.md` | 340 | `How does envelope similarity interact with the reverse-weight resol...` | Resolution | low | `resolution` |

## seeds/seasonal-content-layer.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/seasonal-content-layer.md` | 36 | `## The 12-Month Content Map` | Source map | low | `source map` |
| `seeds/seasonal-content-layer.md` | 44 | `**Agricultural practice:** Walking frozen fields, mapping soil, equ...` | Source map | low | `source map` |
| `seeds/seasonal-content-layer.md` | 51 | `- Almanac content type: goal mapping, annual training calendar, equ...` | Source map | low | `source map` |
| `seeds/seasonal-content-layer.md` | 260 | `This seasonal content map is Northern Hemisphere by default. The ag...` | Source map | low | `source map` |

## seeds/stripe-integration-pipeline.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/stripe-integration-pipeline.md` | 72 | `4. Stripe processes payment` | Pipeline | medium | `pipeline` |
| `seeds/stripe-integration-pipeline.md` | 108 | `const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);` | Pipeline | medium | `pipeline` |
| `seeds/stripe-integration-pipeline.md` | 110 | `process.env.NEXT_PUBLIC_SUPABASE_URL!,` | Pipeline | medium | `pipeline` |
| `seeds/stripe-integration-pipeline.md` | 111 | `process.env.SUPABASE_SERVICE_ROLE_KEY!` | Pipeline | medium | `pipeline` |
| `seeds/stripe-integration-pipeline.md` | 120 | `event = stripe.webhooks.constructEvent(body, sig, process.env.STRIP...` | Pipeline | medium | `pipeline` |
| `seeds/stripe-integration-pipeline.md` | 293 | `return_url: `${process.env.NEXT_PUBLIC_BASE_URL}/me/settings`,` | Pipeline | medium | `pipeline` |

## seeds/superposed-order-ui.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/superposed-order-ui.md` | — | — | — | — | No inconsistencies found |

## seeds/voice-parser-architecture.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/voice-parser-architecture.md` | 37 | `Each of the 26 SCL emoji has a set of natural language synonyms tha...` | Source map | low | `source map` |
| `seeds/voice-parser-architecture.md` | 245 | `return '/'; // fallback to Operis` | Fizzle | medium | `fizzle` |
| `seeds/voice-parser-architecture.md` | 279 | `const orderScores = dict.orders.map(o => ({` | Source map | low | `source map` |
| `seeds/voice-parser-architecture.md` | 284 | `const axisScores  = dict.axes.map(a => ({ ... }));` | Source map | low | `source map` |
| `seeds/voice-parser-architecture.md` | 285 | `const typeScores  = dict.types.map(t => ({ ... }));` | Source map | low | `source map` |
| `seeds/voice-parser-architecture.md` | 286 | `const colorScores = dict.colors.map(c => ({ ... }));` | Source map | low | `source map` |
| `seeds/voice-parser-architecture.md` | 287 | `const floorScores = dict.floors.map(f => ({ ... }));` | Source map | low | `source map` |
| `seeds/voice-parser-architecture.md` | 288 | `const typeScores3 = dict.contentTypes.map(ct => ({ ... }));` | Source map | low | `source map` |
| `seeds/voice-parser-architecture.md` | 337 | `Fallback for no Web Speech API support: text input only. The parser...` | Fizzle | medium | `fizzle` |

## seeds/wilson-voice-identity.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/wilson-voice-identity.md` | 205 | `Generated audio cached per content version. Cache key: `{content_ha...` | Cache hit/miss | low | `cache hit/cache miss` |

## seeds/zip-dial-navigation.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `seeds/zip-dial-navigation.md` | — | — | — | — | No inconsistencies found |

## systems-language-audit.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `systems-language-audit.md` | 5 | `Phase: B (read-only scan → patch map)` | Source map | low | `source map` |
| `systems-language-audit.md` | 18 | `4. "converting zip code to workout / generating from a zip" → **res...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 31 | `\| ~repo structure \| "Stub. Awaiting generation." \| cache miss \|...` | Cache hit/miss | low | `cache hit/cache miss` |
| `systems-language-audit.md` | 31 | `\| ~repo structure \| "Stub. Awaiting generation." \| cache miss \|...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 32 | `\| ~repo structure \| "Complete. Workout generated." \| cache hit \...` | Cache hit/miss | low | `cache hit/cache miss` |
| `systems-language-audit.md` | 32 | `\| ~repo structure \| "Complete. Workout generated." \| cache hit \...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 33 | `\| ~generation sequence \| "Rename the stub file to the complete fi...` | Cache hit/miss | low | `cache hit/cache miss` |
| `systems-language-audit.md` | 33 | `\| ~generation sequence \| "Rename the stub file to the complete fi...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 34 | `\| ~4-dial zip section \| "The constraint hierarchy when dials conf...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 38 | `\| ~infrastructure section \| "Deck identity documents" (exercise m...` | Cache hit/miss | low | `cache hit/cache miss` |
| `systems-language-audit.md` | 38 | `\| ~infrastructure section \| "Deck identity documents" (exercise m...` | Source map | low | `source map` |
| `systems-language-audit.md` | 38 | `\| ~infrastructure section \| "Deck identity documents" (exercise m...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 40 | `\| ~generation rules \| Each numbered step (Parse → Derive → Select...` | Filter | low | `filter` |
| `systems-language-audit.md` | 41 | `\| ~generation rules \| "Load all parameter ceilings and constraint...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 50 | `\| ~infrastructure \| "The exercise library has gaps that prevent r...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 51 | `\| ~CLAUDE.md + scl-directory.md \| "master source of truth" / "aut...` | Authoritative source | high | `authoritative source` |
| `systems-language-audit.md` | 51 | `\| ~CLAUDE.md + scl-directory.md \| "master source of truth" / "aut...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 52 | `\| ~stub template \| YAML frontmatter (described without naming it)...` | Poka-yoke | low | `poka-yoke` |
| `systems-language-audit.md` | 52 | `\| ~stub template \| YAML frontmatter (described without naming it)...` | Source map | low | `source map` |
| `systems-language-audit.md` | 58 | `\| ~numeric zip \| "The emoji zip and the number zip" (two represen...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 67 | `\| ~card status \| "Stub file. Awaiting workout generation." \| cac...` | Cache hit/miss | low | `cache hit/cache miss` |
| `systems-language-audit.md` | 67 | `\| ~card status \| "Stub file. Awaiting workout generation." \| cac...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 68 | `\| ~card status \| "Workout written. Pending review." \| cache hit ...` | Cache hit/miss | low | `cache hit/cache miss` |
| `systems-language-audit.md` | 68 | `\| ~card status \| "Workout written. Pending review." \| cache hit ...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 79 | `\| ~blocked queue \| "Each deck requires: identity doc → generation...` | Backpressure | low | `backpressure` |
| `systems-language-audit.md` | 99 | `\| ~frontmatter \| YAML frontmatter described without naming it \| ...` | Source map | low | `source map` |
| `systems-language-audit.md` | 121 | `\| ~layers \| "Layer 1... through Layer 7... final clamped weight" ...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 122 | `\| ~resolution \| "Converting a zip code to a complete rendered wor...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 181 | `### middle-math/rotation/reverse-weight-resolution.md` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 187 | `\| ~algorithm \| Resolution adjusting by looking backward and forwa...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 195 | `\| ~conflicts \| "When multiple dials have opinions about the same ...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 196 | `\| ~layers \| Layer cascade described without naming it \| layer sy...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 224 | `\| ~construction vehicle \| "The Operis as a construction vehicle" ...` | Cache hit/miss | low | `cache hit/cache miss` |
| `systems-language-audit.md` | 224 | `\| ~construction vehicle \| "The Operis as a construction vehicle" ...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 225 | `\| ~forced generation \| "Each edition forces card generation for 8...` | Cache hit/miss | low | `cache hit/cache miss` |
| `systems-language-audit.md` | 225 | `\| ~forced generation \| "Each edition forces card generation for 8...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 253 | `\| ~featured \| Cache hit/miss distinction (implicit) \| cache hit ...` | Cache hit/miss | low | `cache hit/cache miss` |
| `systems-language-audit.md` | 253 | `\| ~featured \| Cache hit/miss distinction (implicit) \| cache hit ...` | Resolution | low | `resolution` |
| `systems-language-audit.md` | 274 | `\| ~frontmatter \| YAML frontmatter carries card identity \| source...` | Source map | low | `source map` |
| `systems-language-audit.md` | 285 | `\| ~source map \| Frontmatter preserving zip in rendered output \| ...` | Source map | low | `source map` |
| `systems-language-audit.md` | — | `... 14 additional matches truncated in this report` | — | — | — |

## whiteboard.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `whiteboard.md` | 34 | `- [x] Deck identities layer — deck-identities/ with README, templat...` | Poka-yoke | low | `poka-yoke` |
| `whiteboard.md` | 48 | `- [x] .github/workflows/ README.md added` | Pipeline | high | `pipeline` |
| `whiteboard.md` | 61 | `Each deck is a 5-lane campaign. See `seeds/deck-campaign-workflow.m...` | Pipeline | high | `pipeline` |
| `whiteboard.md` | 72 | `Status: ⬜ Not started \| 🔄 In progress \| ✅ Complete \| ⚠️ Issues (...` | Backpressure | low | `backpressure` |
| `whiteboard.md` | 76 | `## Immediate Queue — Next Sessions` | Backpressure | low | `backpressure` |
| `whiteboard.md` | 78 | `Priority order. Top item is next unless Jake redirects.` | Priority | low | `priority` |
| `whiteboard.md` | 80 | `Priority order. Top item is next unless Jake redirects.` | Priority | low | `priority` |
| `whiteboard.md` | 87 | `Also updated: seeds/operis-prompt-pipeline.md (version tags, 17-dep...` | Source map | low | `source map` |
| `whiteboard.md` | 95 | `Why: Run P1→P2→P3 for a real date (suggest current date or a histor...` | Source map | low | `source map` |
| `whiteboard.md` | 100 | `Why: ⛽🌹 Strength × Aesthetic is next in the generation queue.` | Backpressure | low | `backpressure` |
| `whiteboard.md` | 135 | `- Directory planted: .github/linters/, .github/workflows/` | Pipeline | high | `pipeline` |
| `whiteboard.md` | 137 | `- Needs: markdownlint config, frontmatter schema, CI workflow` | Pipeline | high | `pipeline` |
| `whiteboard.md` | 172 | `- Sandbox structure planted: seeds/operis-sandbox-structure.md — 13...` | Source map | low | `source map` |
| `whiteboard.md` | 174 | `- Reverse-weight resolution seeded: middle-math/rotation/reverse-we...` | Resolution | low | `resolution` |
| `whiteboard.md` | 200 | `- Schemas: 7 database table definitions (exercise library enhanced,...` | Cache hit/miss | low | `cache hit/cache miss` |
| `whiteboard.md` | 202 | `Next steps for middle-math:` | Filter | low | `filter` |
| `whiteboard.md` | 229 | `into existing workflow?` | Pipeline | high | `pipeline` |
| `whiteboard.md` | 242 | `- .md files are master source of truth, rendered downstream` | Authoritative source | high | `authoritative source` |
| `whiteboard.md` | 440 | `- deck-identities/ directory created (README, template, naming-conv...` | Poka-yoke | low | `poka-yoke` |
| `whiteboard.md` | 480 | `- .github/workflows/README.md — workflows README added` | Pipeline | high | `pipeline` |
| `whiteboard.md` | 499 | `- CLAUDE.md — updated Cosmogram Layer status, Work Streams table, B...` | Backpressure | low | `backpressure` |
| `whiteboard.md` | 500 | `- whiteboard.md — updated Immediate Queue, Backlog, session log` | Backpressure | low | `backpressure` |
| `whiteboard.md` | 509 | `- deck-identities/deck-07-identity.md — V2 identity doc for ⛽🏛 Stre...` | Backpressure | low | `backpressure` |
| `whiteboard.md` | 509 | `- deck-identities/deck-07-identity.md — V2 identity doc for ⛽🏛 Stre...` | Resolution | low | `resolution` |
| `whiteboard.md` | 513 | `- seeds/deck-campaign-workflow.md — 5-lane campaign model planted (...` | Pipeline | high | `pipeline` |
| `whiteboard.md` | 514 | `- whiteboard.md — Deck Campaign Table added, Immediate Queue update...` | Backpressure | low | `backpressure` |
| `whiteboard.md` | 516 | `Deck 07 regen queue (18 cards):` | Backpressure | low | `backpressure` |
| `whiteboard.md` | 537 | `Next: Continue card generation pipeline (Deck 09 identity or Deck 0...` | Backpressure | low | `backpressure` |
| `whiteboard.md` | 548 | `- middle-math/exercise-engine/ — selection algorithm (pseudocode), ...` | Poka-yoke | low | `poka-yoke` |
| `whiteboard.md` | 565 | `- seeds/operis-architecture.md — Complete Operis specification (sup...` | Multi-pass | medium | `multi-pass` |
| `whiteboard.md` | 588 | `- seeds/operis-sandbox-structure.md — Content Room Constraint Summa...` | Source map | low | `source map` |
| `whiteboard.md` | 591 | `- whiteboard.md — Session 029 logged, Immediate Queue updated (UPDA...` | Backpressure | low | `backpressure` |
| `whiteboard.md` | 603 | `- seeds/operis-sandbox-structure.md — 13-room Sandbox: 8 determinis...` | Source map | low | `source map` |
| `whiteboard.md` | 606 | `- middle-math/rendering/operis-weight-derivation.md — Color of the ...` | Resolution | low | `resolution` |
| `whiteboard.md` | 609 | `- whiteboard.md — this session logged, Immediate Queue updated, Ope...` | Backpressure | low | `backpressure` |
| `whiteboard.md` | 613 | `- Content Rooms translate Operis editorial content into physical pr...` | Source map | low | `source map` |
| `whiteboard.md` | 626 | `- middle-math/rotation/reverse-weight-resolution.md — Temporal zip-...` | Resolution | low | `resolution` |
| `whiteboard.md` | 630 | `- CLAUDE.md — scl-deep/ directory listing updated (vocabulary-stand...` | Resolution | low | `resolution` |
| `whiteboard.md` | 631 | `- README.md — scl-deep/ listing updated to note vocabulary-standard...` | Resolution | low | `resolution` |
| `whiteboard.md` | 632 | `- whiteboard.md — this session logged; Immediate Queue and Backlog ...` | Backpressure | low | `backpressure` |
| `whiteboard.md` | — | `... 3 additional matches truncated in this report` | — | — | — |

## zip-web-tasks.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web-tasks.md` | 7 | `- [ ] Create root ZIP Web map file and establish section skeleton.` | Source map | low | `source map` |
| `zip-web-tasks.md` | 8 | `- [ ] Define stable task-run workflow with two-file iteration rule.` | Pipeline | high | `pipeline` |
| `zip-web-tasks.md` | 13 | `- [ ] Wire map entries to deck-local nodes and paths.` | Source map | low | `source map` |
| `zip-web-tasks.md` | 15 | `- [ ] Confirm deck-local links are represented consistently in map ...` | Source map | low | `source map` |
| `zip-web-tasks.md` | 27 | `- [ ] Keep validation notes concise and attached to map evolution.` | Source map | low | `source map` |
| `zip-web-tasks.md` | 31 | `- [ ] Keep map labels synchronized with canonical workout/card titles.` | Source map | low | `source map` |
| `zip-web-tasks.md` | 32 | `- [ ] Confirm naming consistency between zip codes and rendered map...` | Source map | low | `source map` |

## zip-web.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web.md` | 3 | `# Zip Web Template` | Poka-yoke | low | `poka-yoke` |

## zip-web/README.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/README.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-01-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-01-pods.md` | 61 | `\| N (Progression) \| ⛽🏛🪡🔵 \| Heavy classic pulls follow foundation...` | Filter | low | `filter` |
| `zip-web/zip-web-pods/deck-01-pods.md` | 91 | `\| N (Progression) \| ⛽🏛🪡🔴 \| High-density pulling at strength leve...` | Filter | low | `filter` |
| `zip-web/zip-web-pods/deck-01-pods.md` | 185 | `\| N (Progression) \| ⛽🏛🛒🔵 \| Heavy classic presses follow foundati...` | Filter | low | `filter` |
| `zip-web/zip-web-pods/deck-01-pods.md` | 215 | `\| N (Progression) \| ⛽🏛🛒🔴 \| High-density strength pressing follow...` | Filter | low | `filter` |
| `zip-web/zip-web-pods/deck-01-pods.md` | 433 | `\| N (Progression) \| ⛽🏛🛒🔵 \| Heavy classic presses follow foundati...` | Filter | low | `filter` |

## zip-web/zip-web-pods/deck-02-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-02-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-03-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-03-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-04-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-04-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-05-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-05-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-06-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-06-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-07-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-07-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-08-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-08-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-09-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-09-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-10-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-10-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-11-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-11-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-12-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-12-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-13-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-13-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-14-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-14-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-15-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-15-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-16-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-16-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-17-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-17-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-18-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-18-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-19-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-19-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-20-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-20-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-21-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-21-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-22-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-22-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-23-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-23-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-24-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-24-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-25-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-25-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-26-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-26-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-27-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-27-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-28-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-28-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-29-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-29-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-30-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-30-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-31-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-31-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-32-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-32-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-33-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-33-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-34-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-34-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-35-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-35-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-36-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-36-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-37-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-37-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-38-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-38-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-39-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-39-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-40-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-40-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-41-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-41-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-42-pods.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-42-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-registry.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-registry.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-rules.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-rules.md` | 3 | `This is the single source of truth for how zip-web pods are constru...` | Authoritative source | high | `authoritative source` |
| `zip-web/zip-web-rules.md` | 40 | `- N should NOT be a step backward in intensity or difficulty` | Filter | low | `filter` |
| `zip-web/zip-web-rules.md` | 299 | `b. Apply Type exclusion rule — map 4 remaining Types to N/E/S/W` | Source map | low | `source map` |

## zip-web/zip-web-signatures.md

| File Path | Line (approx) | Found Term | Glossary Term | Severity | Suggested Replacement |
|---|---:|---|---|---|---|
| `zip-web/zip-web-signatures.md` | — | — | — | — | No inconsistencies found |
