# Systems Language Audit

## Summary

- **Total files audited:** 193
- **Total inconsistencies found:** 366
- **Files with inconsistencies:** 84

Severity rubric: **high** = glossary term exists but a completely different word is used; **medium** = close synonym; **low** = informal shorthand.

### Top 10 Most-Repeated Inconsistencies

| Rank | Found Term | Glossary Term | Severity | Count | Suggested Replacement |
|---|---|---|---|---:|---|
| 1 | `template` | Poka-yoke | low | 70 | `poka-yoke` |
| 2 | `queue` | Backpressure | medium | 55 | `backpressure` |
| 3 | `workflow` | Pipeline | high | 50 | `pipeline` |
| 4 | `checklist` | Poka-yoke | low | 33 | `poka-yoke` |
| 5 | `steps` | Filter | low | 32 | `filter` |
| 6 | `follow-up zip` | Draft offering | medium | 27 | `draft offering` |
| 7 | `process` | Pipeline | medium | 26 | `pipeline` |
| 8 | `follow-up zip code` | Draft offering | medium | 18 | `draft offering` |
| 9 | `source of truth` | Authoritative source | high | 15 | `authoritative source` |
| 10 | `lookup` | Resolution | low | 13 | `resolution` |

## AGENTS.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `AGENTS.md` | 16 | `This repository is the master source of truth for all 1,680 workouts.` | Authoritative source | `authoritative source` | high |
| `AGENTS.md` | 16 | `This repository is the master source of truth for all 1,680 workouts.` | Authoritative source | `authoritative source` | high |
| `AGENTS.md` | 221 | `\| 🚂 \| Junction \| Retention \| Bridge to next session. 1–3 follow-up zip codes with rationale. Logging sp...` | Draft offering | `draft offering` | medium |
| `AGENTS.md` | 221 | `\| 🚂 \| Junction \| Retention \| Bridge to next session. 1–3 follow-up zip codes with rationale. Logging sp...` | Draft offering | `draft offering` | medium |
| `AGENTS.md` | 262 | `5. Honor the coverage map — each card's primary exercise must match what the map specifies` | Source map | `source map` | medium |
| `AGENTS.md` | 317 | `14. 🚂 JUNCTION with logging space and next-session bridge. Include 1–3 suggested follow-up zip codes with r...` | Draft offering | `draft offering` | medium |
| `AGENTS.md` | 317 | `14. 🚂 JUNCTION with logging space and next-session bridge. Include 1–3 suggested follow-up zip codes with r...` | Draft offering | `draft offering` | medium |
| `AGENTS.md` | 317 | `14. 🚂 JUNCTION with logging space and next-session bridge. Include 1–3 suggested follow-up zip codes with r...` | Draft offering | `draft offering` | medium |
| `AGENTS.md` | 46 | `├── card-template-v2.md    — Generation template for card format` | Poka-yoke | `poka-yoke` | low |
| `AGENTS.md` | 268 | `Execute these steps in order. Do not skip steps.` | Filter | `filter` | low |
| `AGENTS.md` | 380 | `## Validation Checklist` | Poka-yoke | `poka-yoke` | low |
| `AGENTS.md` | 458 | `- Do not generate a workout without running the full validation checklist` | Poka-yoke | `poka-yoke` | low |

## CLAUDE.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `CLAUDE.md` | 28 | `This repository is the master source of truth for all 1,680 workouts.` | Authoritative source | `authoritative source` | high |
| `CLAUDE.md` | 28 | `This repository is the master source of truth for all 1,680 workouts.` | Authoritative source | `authoritative source` | high |
| `CLAUDE.md` | 709 | `These tools are available in every session. They are not optional — they are part of the workflow.` | Pipeline | `pipeline` | high |
| `CLAUDE.md` | 773 | `- **Skill** = multi-step workflow with judgment calls. Use for generation and identity building.` | Pipeline | `pipeline` | high |
| `CLAUDE.md` | 874 | `Workflow directory: `.github/workflows/`` | Pipeline | `pipeline` | high |
| `CLAUDE.md` | 414 | `\| 🚂 \| Junction \| Retention \| Bridge to next session. 1–3 follow-up zip codes with rationale. Logging sp...` | Draft offering | `draft offering` | medium |
| `CLAUDE.md` | 414 | `\| 🚂 \| Junction \| Retention \| Bridge to next session. 1–3 follow-up zip codes with rationale. Logging sp...` | Draft offering | `draft offering` | medium |
| `CLAUDE.md` | 517 | `14. 🚂 JUNCTION with logging space and next-session bridge. Include 1–3 suggested follow-up zip codes with b...` | Draft offering | `draft offering` | medium |
| `CLAUDE.md` | 517 | `14. 🚂 JUNCTION with logging space and next-session bridge. Include 1–3 suggested follow-up zip codes with b...` | Draft offering | `draft offering` | medium |
| `CLAUDE.md` | 517 | `14. 🚂 JUNCTION with logging space and next-session bridge. Include 1–3 suggested follow-up zip codes with b...` | Draft offering | `draft offering` | medium |
| `CLAUDE.md` | 909 | `**Blocked Queue (waiting on dependencies)**` | Backpressure | `backpressure` | medium |
| `CLAUDE.md` | 155 | `## CARD STUB TEMPLATE` | Poka-yoke | `poka-yoke` | low |
| `CLAUDE.md` | 201 | `3. Run the full validation checklist mentally before writing anything` | Poka-yoke | `poka-yoke` | low |
| `CLAUDE.md` | 468 | `When given a zip code, execute these steps in order. Do not skip steps.` | Filter | `filter` | low |
| `CLAUDE.md` | 580 | `## VALIDATION CHECKLIST` | Poka-yoke | `poka-yoke` | low |
| `CLAUDE.md` | 692 | `- Do not generate a workout without running the full validation checklist` | Poka-yoke | `poka-yoke` | low |
| `CLAUDE.md` | 937 | `template-based format is an evolution, not a replacement. Both formats` | Poka-yoke | `poka-yoke` | low |
| `CLAUDE.md` | 982 | `The emoji is the display layer. The number is the system layer. Both always present. Conversion is a single...` | Resolution | `resolution` | low |

## LICENSE-CONTENT.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `LICENSE-CONTENT.md` | 24 | `- Card templates and the card template V2 format` | Poka-yoke | `poka-yoke` | low |

## LICENSE-LANGUAGE.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `LICENSE-LANGUAGE.md` | — | — | — | — | No inconsistencies found |

## README.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `README.md` | 252 | `The `.md` card files are the master source of truth — the architectural` | Authoritative source | `authoritative source` | high |
| `README.md` | 252 | `The `.md` card files are the master source of truth — the architectural` | Authoritative source | `authoritative source` | high |
| `README.md` | 231 | `\| 🚂 \| Junction \| Bridge to next session. Follow-up zip suggestions. \|` | Draft offering | `draft offering` | medium |
| `README.md` | 295 | `## Goal Mapping — Quick Reference` | Source map | `source map` | medium |

## almanac-2026-zip-calendar.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `almanac-2026-zip-calendar.md` | 286 | `## Today Lookup — 2026-02-20` | Resolution | `resolution` | low |

## card-template-v2.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `card-template-v2.md` | 20 | `7. **🚂 JUNCTION** — log space (blank fields, not pre-filled) + 1–3 follow-up zips with one-line rationale` | Draft offering | `draft offering` | medium |
| `card-template-v2.md` | 1 | `# card-template-v2.md — PPL± Card Format Standard` | Poka-yoke | `poka-yoke` | low |
| `card-template-v2.md` | 3 | `This is the v2 card template. It replaces the v1 15-element required format.` | Poka-yoke | `poka-yoke` | low |
| `card-template-v2.md` | 184 | `**Reduced required elements:** 15 → 8. The seven dropped elements (sub-block zip codes, tree notation, oper...` | Poka-yoke | `poka-yoke` | low |
| `card-template-v2.md` | 186 | `**Color drives structure:** The block sequence and content depth scale to the Color's personality, not to a...` | Poka-yoke | `poka-yoke` | low |

## container-directory.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `container-directory.md` | 3 | `## Dependency Map (excerpt)` | Source map | `source map` | medium |

## exercise-library.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `exercise-library.md` | 2789 | `This repository is the master source of truth for all 1,680 workouts.` | Authoritative source | `authoritative source` | high |
| `exercise-library.md` | 2789 | `This repository is the master source of truth for all 1,680 workouts.` | Authoritative source | `authoritative source` | high |
| `exercise-library.md` | 3530 | `The .md card files are the master source of truth — the architectural` | Authoritative source | `authoritative source` | high |
| `exercise-library.md` | 3530 | `The .md card files are the master source of truth — the architectural` | Authoritative source | `authoritative source` | high |
| `exercise-library.md` | 3087 | `\| 🚂    \| Junction     \| Retention          \| Bridge to next session. 1–3 follow-up zip codes with ratio...` | Draft offering | `draft offering` | medium |
| `exercise-library.md` | 3087 | `\| 🚂    \| Junction     \| Retention          \| Bridge to next session. 1–3 follow-up zip codes with ratio...` | Draft offering | `draft offering` | medium |
| `exercise-library.md` | 3183 | `14. 🚂 JUNCTION with logging space and next-session bridge.` | Draft offering | `draft offering` | medium |
| `exercise-library.md` | 3184 | `Include 1–3 suggested follow-up zip codes with brief rationale.` | Draft offering | `draft offering` | medium |
| `exercise-library.md` | 3184 | `Include 1–3 suggested follow-up zip codes with brief rationale.` | Draft offering | `draft offering` | medium |
| `exercise-library.md` | 3513 | `\| 🚂 \| Junction \| Bridge to next session. Follow-up zip suggestions. \|` | Draft offering | `draft offering` | medium |
| `exercise-library.md` | 3564 | `Goal Mapping — Quick Reference` | Source map | `source map` | medium |
| `exercise-library.md` | 2850 | `CARD STUB TEMPLATE` | Poka-yoke | `poka-yoke` | low |
| `exercise-library.md` | 2884 | `3. Run the full validation checklist mentally before writing anything` | Poka-yoke | `poka-yoke` | low |
| `exercise-library.md` | 3135 | `When given a zip code, execute these steps in order. Do not skip steps.` | Filter | `filter` | low |
| `exercise-library.md` | 3233 | `VALIDATION CHECKLIST` | Poka-yoke | `poka-yoke` | low |
| `exercise-library.md` | 3339 | `- Do not generate a workout without running the full validation checklist` | Poka-yoke | `poka-yoke` | low |

## generation-philosophy.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `generation-philosophy.md` | 97 | `🚂 Junction is 1–3 follow-up zips and a logging space.` | Draft offering | `draft offering` | medium |
| `generation-philosophy.md` | 4 | `These override any tendency toward verbosity, fake precision, or template-filling.` | Poka-yoke | `poka-yoke` | low |
| `generation-philosophy.md` | 13 | `The zip code implies a workload. Don't pad it. Don't compress it into a checklist. Let it breathe at its na...` | Poka-yoke | `poka-yoke` | low |
| `generation-philosophy.md` | 153 | `The Color isn't a modifier on a template. It IS the template. Generate the card from the Color's personalit...` | Poka-yoke | `poka-yoke` | low |

## scl-directory.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-directory.md` | 361 | `14. 🚂 JUNCTION with logging space and next-session bridge` | Draft offering | `draft offering` | medium |
| `scl-directory.md` | 485 | `- The 🚂 Junction suggested follow-up zips should account for what muscle groups come next in the rotation, ...` | Draft offering | `draft offering` | medium |
| `scl-directory.md` | 495 | `- 🚂 Junction: 1–3 follow-up zip codes with one-line rationale. Logging space.` | Draft offering | `draft offering` | medium |
| `scl-directory.md` | 495 | `- 🚂 Junction: 1–3 follow-up zip codes with one-line rationale. Logging space.` | Draft offering | `draft offering` | medium |
| `scl-directory.md` | 593 | `├─ Next session bridge: Posterior chain work today stabilizes` | Draft offering | `draft offering` | medium |
| `scl-directory.md` | 1429 | `How it differs from 🪞 Vanity: Sculpt is more structured, heavier, and process-oriented. Vanity is more outc...` | Pipeline | `pipeline` | medium |
| `scl-directory.md` | 1684 | `├─ Next session bridge: This pulling volume sets up Thursday's` | Draft offering | `draft offering` | medium |
| `scl-directory.md` | 1844 | `Goal Mapping — "I want to..."` | Source map | `source map` | medium |
| `scl-directory.md` | 305 | `When given a zip code, you execute these steps:` | Filter | `filter` | low |
| `scl-directory.md` | 406 | `VALIDATION CHECKLIST` | Poka-yoke | `poka-yoke` | low |
| `scl-directory.md` | 1586 | `Every submission must use the standard SCL workout format. This is the template:` | Poka-yoke | `poka-yoke` | low |
| `scl-directory.md` | 1758 | `All submissions must be in markdown (.md) format following the SCL template shown above.` | Poka-yoke | `poka-yoke` | low |

## systems-language-audit.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `systems-language-audit.md` | 79 | `\| ~blocked queue \| "Each deck requires: identity doc → generation → validation → review" \| tech tree \| ...` | Backpressure | `backpressure` | medium |
| `systems-language-audit.md` | 335 | `\| CLAUDE.md \| Validation checklist (agent mental check) vs scan cycle (script check) \| The VALIDATION CH...` | Pipeline | `pipeline` | medium |
| `systems-language-audit.md` | 16 | `2. "validation script/checklist checks" → **scan cycle** of **rungs** (CLAUDE.md, middle-math)` | Poka-yoke | `poka-yoke` | low |
| `systems-language-audit.md` | 42 | `\| ~validation checklist \| "Before writing any workout to a file, verify all of the following" \| scan cyc...` | Poka-yoke | `poka-yoke` | low |
| `systems-language-audit.md` | 43 | `\| ~validation checklist \| Each individual checkbox item \| rung \| §5 Validation \|` | Poka-yoke | `poka-yoke` | low |
| `systems-language-audit.md` | 44 | `\| ~validation checklist \| "If any check fails, revise before writing" \| rung failure \| §5 Validation \|` | Poka-yoke | `poka-yoke` | low |
| `systems-language-audit.md` | 52 | `\| ~stub template \| YAML frontmatter (described without naming it) \| source map \| §1 Pipeline \|` | Poka-yoke | `poka-yoke` | low |
| `systems-language-audit.md` | 82 | `\| ~validation \| Checklist items run before committing \| scan cycle / rungs \| §5 Validation \|` | Poka-yoke | `poka-yoke` | low |
| `systems-language-audit.md` | 90 | `\| ~common errors \| "Common Foundation Errors", "Common Strength Errors" sections \| implicitly a gemba ch...` | Poka-yoke | `poka-yoke` | low |
| `systems-language-audit.md` | 335 | `\| CLAUDE.md \| Validation checklist (agent mental check) vs scan cycle (script check) \| The VALIDATION CH...` | Poka-yoke | `poka-yoke` | low |
| `systems-language-audit.md` | 374 | `4. **Add: pre-flight** — the agent's mental pre-generation validation checklist (distinct from the automate...` | Poka-yoke | `poka-yoke` | low |

## whiteboard.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `whiteboard.md` | 38 | `- [x] Audit workflow docs — scripts/README.md (full audit orchestrator + checklist matrix link)` | Pipeline | `pipeline` | high |
| `whiteboard.md` | 49 | `- [x] .github/workflows/ README.md added` | Pipeline | `pipeline` | high |
| `whiteboard.md` | 62 | `Each deck is a 5-lane campaign. See `seeds/deck-campaign-workflow.md` for full spec.` | Pipeline | `pipeline` | high |
| `whiteboard.md` | 163 | `- Directory planted: .github/linters/, .github/workflows/` | Pipeline | `pipeline` | high |
| `whiteboard.md` | 165 | `- Needs: markdownlint config, frontmatter schema, CI workflow` | Pipeline | `pipeline` | high |
| `whiteboard.md` | 257 | `into existing workflow?` | Pipeline | `pipeline` | high |
| `whiteboard.md` | 270 | `- .md files are master source of truth, rendered downstream` | Authoritative source | `authoritative source` | high |
| `whiteboard.md` | 270 | `- .md files are master source of truth, rendered downstream` | Authoritative source | `authoritative source` | high |
| `whiteboard.md` | 508 | `- .github/workflows/README.md — workflows README added` | Pipeline | `pipeline` | high |
| `whiteboard.md` | 541 | `- seeds/deck-campaign-workflow.md — 5-lane campaign model planted (Cosmogram → Identity → Generation → Audi...` | Pipeline | `pipeline` | high |
| `whiteboard.md` | 73 | `Status: ⬜ Not started \| 🔄 In progress \| ✅ Complete \| ⚠️ Issues (regen queue active) \| — Not applicable` | Backpressure | `backpressure` | medium |
| `whiteboard.md` | 77 | `## Immediate Queue — Next Sessions` | Backpressure | `backpressure` | medium |
| `whiteboard.md` | 128 | `Why: ⛽🌹 Strength × Aesthetic is next in the generation queue.` | Backpressure | `backpressure` | medium |
| `whiteboard.md` | 374 | `Output: Replaced all Deck 07 🚂 Junction sections with cross-layout navigation (current zip centered, 4 type...` | Draft offering | `draft offering` | medium |
| `whiteboard.md` | 527 | `- CLAUDE.md — updated Cosmogram Layer status, Work Streams table, Blocked Queue` | Backpressure | `backpressure` | medium |
| `whiteboard.md` | 528 | `- whiteboard.md — updated Immediate Queue, Backlog, session log` | Backpressure | `backpressure` | medium |
| `whiteboard.md` | 537 | `- deck-identities/deck-07-identity.md — V2 identity doc for ⛽🏛 Strength × Basics (40 zips mapped, primary e...` | Backpressure | `backpressure` | medium |
| `whiteboard.md` | 542 | `- whiteboard.md — Deck Campaign Table added, Immediate Queue updated, Session 021 logged` | Backpressure | `backpressure` | medium |
| `whiteboard.md` | 544 | `Deck 07 regen queue (18 cards):` | Backpressure | `backpressure` | medium |
| `whiteboard.md` | 565 | `Next: Continue card generation pipeline (Deck 09 identity or Deck 07 regen queue). Daily and platform seeds...` | Backpressure | `backpressure` | medium |
| `whiteboard.md` | 619 | `- whiteboard.md — Session 029 logged, Immediate Queue updated (UPDATED)` | Backpressure | `backpressure` | medium |
| `whiteboard.md` | 637 | `- whiteboard.md — this session logged, Immediate Queue updated, Operis Build-Out backlog updated (UPDATED)` | Backpressure | `backpressure` | medium |
| `whiteboard.md` | 660 | `- whiteboard.md — this session logged; Immediate Queue and Backlog updated.` | Backpressure | `backpressure` | medium |
| `whiteboard.md` | 694 | `- whiteboard.md — This session log, queue update, backlog` | Backpressure | `backpressure` | medium |
| `whiteboard.md` | 34 | `- [x] Deck identities layer — deck-identities/ with README, template, naming-convention, deck-08-identity` | Poka-yoke | `poka-yoke` | low |
| `whiteboard.md` | 38 | `- [x] Audit workflow docs — scripts/README.md (full audit orchestrator + checklist matrix link)` | Poka-yoke | `poka-yoke` | low |
| `whiteboard.md` | 112 | `1) Add strict URL + sky-field enforcement to P1 template/checklist (Contract A gap still open).` | Poka-yoke | `poka-yoke` | low |
| `whiteboard.md` | 112 | `1) Add strict URL + sky-field enforcement to P1 template/checklist (Contract A gap still open).` | Poka-yoke | `poka-yoke` | low |
| `whiteboard.md` | 113 | `2) Add per-lane URL enforcement to P2 template/checklist (Contract B gap still open).` | Poka-yoke | `poka-yoke` | low |
| `whiteboard.md` | 113 | `2) Add per-lane URL enforcement to P2 template/checklist (Contract B gap still open).` | Poka-yoke | `poka-yoke` | low |
| `whiteboard.md` | 230 | `Next steps for middle-math:` | Filter | `filter` | low |
| `whiteboard.md` | 468 | `- deck-identities/ directory created (README, template, naming-convention, deck-08-identity)` | Poka-yoke | `poka-yoke` | low |
| `whiteboard.md` | 576 | `- middle-math/exercise-engine/ — selection algorithm (pseudocode), family trees (DRAFT, 8 families), transf...` | Poka-yoke | `poka-yoke` | low |
| `whiteboard.md` | 614 | `- seeds/operis-builder-prompt.md — Prompt 4: Builder. Takes edition → committed files. Proofing checklist (...` | Poka-yoke | `poka-yoke` | low |
| `whiteboard.md` | 733 | `session-stub template and export pipeline (Genspark-to-Obsidian Chrome` | Poka-yoke | `poka-yoke` | low |

## zip-web-tasks.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web-tasks.md` | 8 | `- [ ] Define stable task-run workflow with two-file iteration rule.` | Pipeline | `pipeline` | high |

## zip-web.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web.md` | 3 | `# Zip Web Template` | Poka-yoke | `poka-yoke` | low |

## seeds/README.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/README.md` | 19 | `\| junction-community.md \| 🚂 Junction evolves into living community recommendation surface + Almanac queue...` | Backpressure | `backpressure` | medium |

## seeds/almanac-8day-rotation.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/almanac-8day-rotation.md` | 42 | `This is not mandatory ordering. A new user could begin at any point in the cycle based on registration date...` | Backpressure | `backpressure` | medium |
| `seeds/almanac-8day-rotation.md` | 97 | `## Almanac Queue Override` | Backpressure | `backpressure` | medium |
| `seeds/almanac-8day-rotation.md` | 101 | `The rotation resumes the following day from wherever it left off. The queue does not skip positions — it te...` | Backpressure | `backpressure` | medium |

## seeds/almanac-macro-operators.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/almanac-macro-operators.md` | — | — | — | — | No inconsistencies found |

## seeds/almanac-room-bloom.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/almanac-room-bloom.md` | — | — | — | — | No inconsistencies found |

## seeds/art-direction.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/art-direction.md` | — | — | — | — | No inconsistencies found |

## seeds/automotive-layer-architecture.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/automotive-layer-architecture.md` | 24 | `- Process yesterday's session (what worked, what to do next)` | Pipeline | `pipeline` | medium |
| `seeds/automotive-layer-architecture.md` | 28 | `The car is not where people log sets. It is where people prime for the session, get the Operis context, hea...` | Backpressure | `backpressure` | medium |

## seeds/axis-as-app-floors.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/axis-as-app-floors.md` | 112 | `- The Almanac itself — the user's personal workout queue and rotation` | Backpressure | `backpressure` | medium |
| `seeds/axis-as-app-floors.md` | 134 | `- Junction community voting (follow-up zip recommendations)` | Draft offering | `draft offering` | medium |
| `seeds/axis-as-app-floors.md` | 40 | `- Quick-view zip code lookup` | Resolution | `resolution` | low |

## seeds/claude-code-build-sequence.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/claude-code-build-sequence.md` | 506 | `Container block `Depends on` is the canonical source; summary tables must mirror it.` | Authoritative source | `authoritative source` | high |
| `seeds/claude-code-build-sequence.md` | 504 | `## Dependency Map` | Source map | `source map` | medium |

## seeds/codex-audit-agents-friendly-expansion.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/codex-audit-agents-friendly-expansion.md` | 100 | `- Optional CI workflow in warn-only mode.` | Pipeline | `pipeline` | high |
| `seeds/codex-audit-agents-friendly-expansion.md` | 174 | `**Goal:** single source of truth for generation status and quality state.` | Authoritative source | `authoritative source` | high |
| `seeds/codex-audit-agents-friendly-expansion.md` | 236 | `- Checklists integrated with current whiteboard workflow.` | Pipeline | `pipeline` | high |
| `seeds/codex-audit-agents-friendly-expansion.md` | 35 | `- Coverage map ensuring 8 color variants per Type do not reuse the same primary exercise.` | Source map | `source map` | medium |
| `seeds/codex-audit-agents-friendly-expansion.md` | 55 | `### A3) Retrofit Deck 07 flagged regen queue` | Backpressure | `backpressure` | medium |
| `seeds/codex-audit-agents-friendly-expansion.md` | 155 | `- Check that follow-up zips are structurally plausible.` | Draft offering | `draft offering` | medium |
| `seeds/codex-audit-agents-friendly-expansion.md` | 235 | `- Templates for "build identity", "generate batch", "audit deck", "regen queue".` | Backpressure | `backpressure` | medium |
| `seeds/codex-audit-agents-friendly-expansion.md` | 250 | `5. **Deck 07 regen queue cleanup (A3)**` | Backpressure | `backpressure` | medium |
| `seeds/codex-audit-agents-friendly-expansion.md` | 79 | `- Define canonical schema fields from current card template.` | Poka-yoke | `poka-yoke` | low |

## seeds/codex-container-directory-v3.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/codex-container-directory-v3.md` | 186 | `### CX-07: CI Lint Workflow` | Pipeline | `pipeline` | high |
| `seeds/codex-container-directory-v3.md` | 188 | `**Goal:** Create a GitHub Actions workflow that runs validation on push.` | Pipeline | `pipeline` | high |
| `seeds/codex-container-directory-v3.md` | 194 | `**Writes:** `.github/workflows/lint.yml`` | Pipeline | `pipeline` | high |
| `seeds/codex-container-directory-v3.md` | 198 | `Create `.github/workflows/lint.yml` that triggers on push to main and pull requests. Steps: (1) checkout re...` | Pipeline | `pipeline` | high |
| `seeds/codex-container-directory-v3.md` | 200 | `**Validation:** Workflow YAML is valid GitHub Actions syntax. Both script paths exist. The workflow referen...` | Pipeline | `pipeline` | high |
| `seeds/codex-container-directory-v3.md` | 202 | `**Does NOT:** Run the workflow (that happens on push). Install markdownlint as a step yet (defer to future ...` | Pipeline | `pipeline` | high |
| `seeds/codex-container-directory-v3.md` | 670 | `## DEPENDENCY MAP v3.0` | Source map | `source map` | medium |
| `seeds/codex-container-directory-v3.md` | 118 | `Create `scripts/middle-math/zip_converter.py` with functions: `emoji_to_numeric(emoji_zip: str) -> str` (e....` | Resolution | `resolution` | low |
| `seeds/codex-container-directory-v3.md` | 172 | `**Reads:** `CLAUDE.md` (card stub template, status convention), `deck-identities/template.md`` | Poka-yoke | `poka-yoke` | low |
| `seeds/codex-container-directory-v3.md` | 198 | `Create `.github/workflows/lint.yml` that triggers on push to main and pull requests. Steps: (1) checkout re...` | Filter | `filter` | low |
| `seeds/codex-container-directory-v3.md` | 232 | `**Reads:** `scl-directory.md` (Axis definitions and character), `middle-math/weights/weight-system-spec.md`...` | Poka-yoke | `poka-yoke` | low |
| `seeds/codex-container-directory-v3.md` | 250 | `**Reads:** `scl-directory.md`, `middle-math/weights/weight-system-spec.md`, `middle-math/weights/order-weig...` | Poka-yoke | `poka-yoke` | low |
| `seeds/codex-container-directory-v3.md` | 346 | `Create `scripts/middle-math/exercise_selector.py` implementing the 6-step selection pipeline from selection...` | Poka-yoke | `poka-yoke` | low |
| `seeds/codex-container-directory-v3.md` | 358 | `**Reads:** `deck-identities/template.md`, `deck-identities/deck-08-identity.md` (as example), `middle-math/...` | Poka-yoke | `poka-yoke` | low |
| `seeds/codex-container-directory-v3.md` | 586 | `**Goal:** Generate 42 cosmogram stub files and a template.` | Poka-yoke | `poka-yoke` | low |
| `seeds/codex-container-directory-v3.md` | 592 | `**Writes:** `deck-cosmograms/cosmogram-template.md`, `deck-cosmograms/deck-01-cosmogram.md` through `deck-4...` | Poka-yoke | `poka-yoke` | low |
| `seeds/codex-container-directory-v3.md` | 596 | `Create template with sections: One Sentence, Architectural Identity, Historical Roots, Cultural Context, Th...` | Poka-yoke | `poka-yoke` | low |

## seeds/content-types-architecture.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/content-types-architecture.md` | 59 | `25. The Skill Definition — one of 5 Claude Code skills. Invoke syntax, steps, output spec.` | Filter | `filter` | low |
| `seeds/content-types-architecture.md` | 67 | `33. The Deck Identity Template — the blank template for new identity documents.` | Poka-yoke | `poka-yoke` | low |
| `seeds/content-types-architecture.md` | 72 | `38. The Cosmogram Research Prompt — the research template for deck cosmogram generation.` | Poka-yoke | `poka-yoke` | low |
| `seeds/content-types-architecture.md` | 163 | `109. The Coaching Program Template — a Jake-designed program offered to Tier 2 users as a guided tour.` | Poka-yoke | `poka-yoke` | low |

## seeds/cosmogram-research-prompt.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/cosmogram-research-prompt.md` | 156 | `Named phases within a workflow. The name is fixed. The content shifts completely based on zip code context....` | Pipeline | `pipeline` | high |
| `seeds/cosmogram-research-prompt.md` | 300 | `Philosophy, Systems Thinking & Ways of Knowing. Philosophical traditions operating here. Systems thinking, ...` | Pipeline | `pipeline` | medium |
| `seeds/cosmogram-research-prompt.md` | 172 | `Fractal/Nested Structure. The 7 Orders appear at every scale. Week 1 of Doric = Tuscan-within-Doric. Week 2...` | Filter | `filter` | low |

## seeds/daily-architecture.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/daily-architecture.md` | 216 | `- How does the Daily interact with the user's Almanac queue? (Does tapping a Sandbox zip add it to queue, o...` | Backpressure | `backpressure` | medium |

## seeds/data-ethics-architecture.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/data-ethics-architecture.md` | — | — | — | — | No inconsistencies found |

## seeds/deck-campaign-workflow.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/deck-campaign-workflow.md` | 1 | `# Seed: Deck Campaign Workflow` | Pipeline | `pipeline` | high |
| `seeds/deck-campaign-workflow.md` | 104 | `Both Deck 07 and Deck 08 were generated before this workflow existed. To bring them into` | Pipeline | `pipeline` | high |
| `seeds/deck-campaign-workflow.md` | 119 | `- Campaign state view in `whiteboard.md` as the permanent source of truth` | Authoritative source | `authoritative source` | high |
| `seeds/deck-campaign-workflow.md` | 133 | `Until then, this seed informs session planning but the whiteboard remains the source of truth.` | Authoritative source | `authoritative source` | high |
| `seeds/deck-campaign-workflow.md` | 25 | `LANE B: Identity Doc     — Exercise mapping, duplicate audit, regen queue` | Backpressure | `backpressure` | medium |
| `seeds/deck-campaign-workflow.md` | 35 | `- E requires D (audit must pass before review queue opens)` | Backpressure | `backpressure` | medium |
| `seeds/deck-campaign-workflow.md` | 71 | `- ⚠️ Complete with known issues (regen queue active)` | Backpressure | `backpressure` | medium |
| `seeds/deck-campaign-workflow.md` | 92 | `The process is:` | Pipeline | `pipeline` | medium |
| `seeds/deck-campaign-workflow.md` | 112 | `Needs: full Lane C completion (regen queue), Lane D, Lane E.` | Backpressure | `backpressure` | medium |

## seeds/default-almanac-preset.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/default-almanac-preset.md` | 157 | `queue: []  (empty — no zip codes queued)` | Backpressure | `backpressure` | medium |

## seeds/default-rotation-engine.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/default-rotation-engine.md` | 118 | `The Almanac queue (seeds/almanac-8day-rotation.md) sits on TOP of the rotation engine. The engine provides ...` | Backpressure | `backpressure` | medium |

## seeds/elevator-architecture.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/elevator-architecture.md` | — | — | — | — | No inconsistencies found |

## seeds/exercise-attribute-tagging.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/exercise-attribute-tagging.md` | 39 | `~2,800 exercises × 11 attributes + flags = significant tagging effort. Could be batched by library section ...` | Pipeline | `pipeline` | medium |

## seeds/exercise-superscript.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/exercise-superscript.md` | — | — | — | — | No inconsistencies found |

## seeds/experience-layer-blueprint.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/experience-layer-blueprint.md` | — | — | — | — | No inconsistencies found |

## seeds/git-worktree-pattern.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/git-worktree-pattern.md` | — | — | — | — | No inconsistencies found |

## seeds/junction-community.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/junction-community.md` | 9 | `# 🚂 Junction — Community Layer & Almanac Queue` | Backpressure | `backpressure` | medium |
| `seeds/junction-community.md` | 18 | `Junction contains static 1–3 suggested follow-up zip codes with rationale, authored during card generation....` | Draft offering | `draft offering` | medium |
| `seeds/junction-community.md` | 18 | `Junction contains static 1–3 suggested follow-up zip codes with rationale, authored during card generation....` | Draft offering | `draft offering` | medium |
| `seeds/junction-community.md` | 21 | `Junction renders static suggestions as tappable zip code links. Selecting one queues it into the user's Alm...` | Backpressure | `backpressure` | medium |
| `seeds/junction-community.md` | 24 | `Three data sources feed the Junction: the master suggestion (architect's original, never removed), the comm...` | Draft offering | `draft offering` | medium |
| `seeds/junction-community.md` | 24 | `Three data sources feed the Junction: the master suggestion (architect's original, never removed), the comm...` | Draft offering | `draft offering` | medium |
| `seeds/junction-community.md` | 30 | `- The Almanac is a queue, not a calendar. No scheduling, no time slots. Just an ordered list of what's next.` | Backpressure | `backpressure` | medium |
| `seeds/junction-community.md` | 41 | `- Does the Almanac queue have a max depth?` | Backpressure | `backpressure` | medium |

## seeds/linters-architecture.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/linters-architecture.md` | 48 | `- `.github/workflows/lint.yml` — runs all 3 tiers on push/PR against `cards/`` | Pipeline | `pipeline` | high |
| `seeds/linters-architecture.md` | 57 | `- CI workflow (`lint.yml`) needs to be written` | Pipeline | `pipeline` | high |
| `seeds/linters-architecture.md` | 76 | `└── workflows/` | Pipeline | `pipeline` | high |

## seeds/mobile-ui-architecture.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/mobile-ui-architecture.md` | — | — | — | — | No inconsistencies found |

## seeds/numeric-zip-system.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/numeric-zip-system.md` | — | — | — | — | No inconsistencies found |

## seeds/operis-architecture.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/operis-architecture.md` | 53 | `**The generation engine.** Every edition of the Operis features 8–12 zip codes. Each featured zip code is a...` | Backpressure | `backpressure` | medium |
| `seeds/operis-architecture.md` | 388 | `⚫ The Order of the day is the law. If it is Tuesday and the Order is ⛽ Strength, the Sandbox features ⛽ zip...` | Backpressure | `backpressure` | medium |
| `seeds/operis-architecture.md` | 414 | `- How does the Operis interact with the user's Almanac queue? (Does tapping a Sandbox zip add it to queue, ...` | Backpressure | `backpressure` | medium |

## seeds/operis-builder-prompt.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/operis-builder-prompt.md` | 50 | `## Proofing Checklist` | Poka-yoke | `poka-yoke` | low |
| `seeds/operis-builder-prompt.md` | 87 | `3. Generate the card following the complete generation sequence in CLAUDE.md (Steps 1–5: parse zip, derive ...` | Filter | `filter` | low |
| `seeds/operis-builder-prompt.md` | 139 | `- Do not commit an edition with incorrect rotation engine data. If the proofing checklist reveals a discrep...` | Poka-yoke | `poka-yoke` | low |

## seeds/operis-color-posture.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/operis-color-posture.md` | 41 | `**🟢 Think like a gardener.** Today is a steady, organic day. The world is growing. The best approach is sus...` | Pipeline | `pipeline` | medium |

## seeds/operis-content-architect-prompt.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/operis-content-architect-prompt.md` | 105 | `Produce: the word, its Latin derivation path (2–3 steps), and one sentence explaining why this word fits to...` | Filter | `filter` | low |

## seeds/operis-editor-prompt.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/operis-editor-prompt.md` | — | — | — | — | No inconsistencies found |

## seeds/operis-educational-layer.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/operis-educational-layer.md` | 42 | `Domain: Financial literacy, legal basics, civic process, tax structure, insurance mechanics, contracts, cre...` | Pipeline | `pipeline` | medium |
| `seeds/operis-educational-layer.md` | 46 | `Search guidance (for Prompt 2): Tax deadlines and financial planning windows relevant to the current date. ...` | Pipeline | `pipeline` | medium |
| `seeds/operis-educational-layer.md` | 98 | `Domain: Current events that demand attention, civic engagement, voting, community organizing, emergency pre...` | Pipeline | `pipeline` | medium |
| `seeds/operis-educational-layer.md` | 102 | `Search guidance (for Prompt 2): Current events directly affecting how people live. Emergency preparedness t...` | Pipeline | `pipeline` | medium |

## seeds/operis-naming-rationale.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/operis-naming-rationale.md` | — | — | — | — | No inconsistencies found |

## seeds/operis-prompt-pipeline.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/operis-prompt-pipeline.md` | 300 | `The manual pipeline is the v1. The automation pipeline is the same architecture with the human steps replac...` | Filter | `filter` | low |

## seeds/operis-researcher-prompt.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/operis-researcher-prompt.md` | — | — | — | — | No inconsistencies found |

## seeds/operis-sandbox-structure.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/operis-sandbox-structure.md` | 238 | `A user finding this zip code six months from now via search, community recommendation, or their own Almanac...` | Backpressure | `backpressure` | medium |
| `seeds/operis-sandbox-structure.md` | 257 | `- How does the Content Room system interact with the user's Almanac queue? If a user taps a Content Room fr...` | Backpressure | `backpressure` | medium |

## seeds/platform-architecture-v1-archive.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/platform-architecture-v1-archive.md` | 699 | `## The 🧮 SAVE Workflow` | Pipeline | `pipeline` | high |
| `seeds/platform-architecture-v1-archive.md` | 1331 | `**Jake's Workflow:**` | Pipeline | `pipeline` | high |
| `seeds/platform-architecture-v1-archive.md` | 1375 | `**Jake's Workflow:**` | Pipeline | `pipeline` | high |
| `seeds/platform-architecture-v1-archive.md` | 1425 | `**Jake's Workflow:**` | Pipeline | `pipeline` | high |
| `seeds/platform-architecture-v1-archive.md` | 1451 | `**Daily Workflows:**` | Pipeline | `pipeline` | high |
| `seeds/platform-architecture-v1-archive.md` | 1651 | `- Approval workflow (Jake's admin panel)` | Pipeline | `pipeline` | high |
| `seeds/platform-architecture-v1-archive.md` | 1746 | `- ✅ User experience (card deck metaphor, workflows)` | Pipeline | `pipeline` | high |
| `seeds/platform-architecture-v1-archive.md` | 1473 | `Jake checks moderation queue 1×/day (15 min)` | Backpressure | `backpressure` | medium |
| `seeds/platform-architecture-v1-archive.md` | 1751 | `**Next steps (as of February 11, 2026 — superseded by V2):**` | Filter | `filter` | low |

## seeds/platform-architecture-v2.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/platform-architecture-v2.md` | 167 | `### The 🧮 SAVE Workflow` | Pipeline | `pipeline` | high |
| `seeds/platform-architecture-v2.md` | 300 | `The SCL rules. Codified in CLAUDE.md and scl-directory.md. Order ceilings, Color equipment filters, Axis bi...` | Poka-yoke | `poka-yoke` | low |

## seeds/regional-filter-architecture.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/regional-filter-architecture.md` | — | — | — | — | No inconsistencies found |

## seeds/scl-emoji-macros-draft.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/scl-emoji-macros-draft.md` | — | — | — | — | No inconsistencies found |

## seeds/scl-envelope-architecture.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/scl-envelope-architecture.md` | 171 | `The cosmogram is the editorial seed that starts this process. The accumulated envelopes are the soil it gro...` | Pipeline | `pipeline` | medium |

## seeds/seasonal-content-layer.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/seasonal-content-layer.md` | 51 | `- Almanac content type: goal mapping, annual training calendar, equipment audit` | Source map | `source map` | medium |

## seeds/stripe-integration-pipeline.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/stripe-integration-pipeline.md` | 72 | `4. Stripe processes payment` | Pipeline | `pipeline` | medium |
| `seeds/stripe-integration-pipeline.md` | 108 | `const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);` | Pipeline | `pipeline` | medium |
| `seeds/stripe-integration-pipeline.md` | 110 | `process.env.NEXT_PUBLIC_SUPABASE_URL!,` | Pipeline | `pipeline` | medium |
| `seeds/stripe-integration-pipeline.md` | 111 | `process.env.SUPABASE_SERVICE_ROLE_KEY!` | Pipeline | `pipeline` | medium |
| `seeds/stripe-integration-pipeline.md` | 120 | `event = stripe.webhooks.constructEvent(body, sig, process.env.STRIPE_WEBHOOK_SECRET!);` | Pipeline | `pipeline` | medium |
| `seeds/stripe-integration-pipeline.md` | 293 | `return_url: `${process.env.NEXT_PUBLIC_BASE_URL}/me/settings`,` | Pipeline | `pipeline` | medium |

## seeds/superposed-order-ui.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/superposed-order-ui.md` | — | — | — | — | No inconsistencies found |

## seeds/systems-eudaimonics.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/systems-eudaimonics.md` | — | — | — | — | No inconsistencies found |

## seeds/voice-parser-architecture.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/voice-parser-architecture.md` | 88 | `\| Utilitas / Tools \| 🔨 \| tools, calculator, library, lookup, find exercise, how-to, equipment, search \|` | Resolution | `resolution` | low |

## seeds/wilson-voice-identity.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/wilson-voice-identity.md` | — | — | — | — | No inconsistencies found |

## seeds/zip-dial-navigation.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `seeds/zip-dial-navigation.md` | — | — | — | — | No inconsistencies found |

## scl-deep/README.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/README.md` | — | — | — | — | No inconsistencies found |

## scl-deep/axis-specifications.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/axis-specifications.md` | 133 | `- Content: Personal workout queue, calendar views, 12-month Operator visualization, Farmer's Almanac conten...` | Backpressure | `backpressure` | medium |
| `scl-deep/axis-specifications.md` | 55 | `- Content: 42-deck grid, 4-dial navigator, quick-view zip lookup, today's default zip, featured workout` | Resolution | `resolution` | low |

## scl-deep/block-specifications.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/block-specifications.md` | 512 | `- *Goes inside:* 1–3 suggested follow-up zip codes with rationale, logging space, notes on session performa...` | Draft offering | `draft offering` | medium |
| `scl-deep/block-specifications.md` | 512 | `- *Goes inside:* 1–3 suggested follow-up zip codes with rationale, logging space, notes on session performa...` | Draft offering | `draft offering` | medium |
| `scl-deep/block-specifications.md` | 10 | `- card-template-v2.md` | Poka-yoke | `poka-yoke` | low |

## scl-deep/color-context-vernacular.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/color-context-vernacular.md` | 368 | `- "Give me space to process."` | Pipeline | `pipeline` | medium |

## scl-deep/color-specifications.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/color-specifications.md` | 227 | `🔵 Structured is the Planning tonal name: structured, calm, methodical, processing. The person who writes in...` | Filter | `filter` | low |

## scl-deep/emoji-macros.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/emoji-macros.md` | 34 | `The Orders govern load, rep range, rest, and difficulty. They are the seven phases of a training cycle, and...` | Pipeline | `pipeline` | medium |
| `scl-deep/emoji-macros.md` | 83 | `What makes the butterfly uniquely apt for Hypertrophy is the nature of the metamorphic process: it is slow,...` | Pipeline | `pipeline` | medium |
| `scl-deep/emoji-macros.md` | 533 | `The locomotive: the vehicle that runs on rails between stations. The Junction block is the bridge — it leav...` | Draft offering | `draft offering` | medium |
| `scl-deep/emoji-macros.md` | 533 | `The locomotive: the vehicle that runs on rails between stations. The Junction block is the bridge — it leav...` | Draft offering | `draft offering` | medium |
| `scl-deep/emoji-macros.md` | 479 | `The numbers 1-2-3: sequencing, ordering, the basic grammar of any skill. Fundamentals are the numbered step...` | Filter | `filter` | low |

## scl-deep/intercolumniation.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/intercolumniation.md` | — | — | — | — | No inconsistencies found |

## scl-deep/junction-web.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/junction-web.md` | 7 | `The 🚂 Junction block at the end of every workout contains follow-up zip code` | Draft offering | `draft offering` | medium |
| `scl-deep/junction-web.md` | 7 | `The 🚂 Junction block at the end of every workout contains follow-up zip code` | Draft offering | `draft offering` | medium |
| `scl-deep/junction-web.md` | 19 | `2. Suggests 1–3 follow-up zip codes with brief rationale` | Draft offering | `draft offering` | medium |
| `scl-deep/junction-web.md` | 19 | `2. Suggests 1–3 follow-up zip codes with brief rationale` | Draft offering | `draft offering` | medium |

## scl-deep/operator-specifications.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/operator-specifications.md` | — | — | — | — | No inconsistencies found |

## scl-deep/order-etymology.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/order-etymology.md` | — | — | — | — | No inconsistencies found |

## scl-deep/order-specifications.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/order-specifications.md` | 347 | `- Rest between steps: 2–3 minutes` | Filter | `filter` | low |

## scl-deep/publication-standard.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/publication-standard.md` | — | — | — | — | No inconsistencies found |

## scl-deep/seasonal-density.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/seasonal-density.md` | — | — | — | — | No inconsistencies found |

## scl-deep/systems-glossary.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/systems-glossary.md` | 63 | `\| Event store \| Event Sourcing / Git \| The append-only log of all events. The source of truth for everyt...` | Authoritative source | `authoritative source` | high |
| `scl-deep/systems-glossary.md` | 65 | `\| Snapshot \| Event Sourcing / Git \| A periodic materialization of current state to avoid full event repl...` | Authoritative source | `authoritative source` | high |
| `scl-deep/systems-glossary.md` | 48 | `\| Tee \| Unix / Factorio \| A split that duplicates a data stream to two destinations without blocking eit...` | Backpressure | `backpressure` | medium |
| `scl-deep/systems-glossary.md` | 51 | `\| Backpressure \| Unix / Factorio \| When a downstream system signals upstream to slow down because it can...` | Pipeline | `pipeline` | medium |
| `scl-deep/systems-glossary.md` | 84 | `\| Cache miss \| DNS / MTG \| When an address has no stored content and requires full resolution. In PPL: a...` | Backpressure | `backpressure` | medium |
| `scl-deep/systems-glossary.md` | 172 | `\| Operis → edition + card queue \| Tee \| §2 Data Flow \|` | Backpressure | `backpressure` | medium |
| `scl-deep/systems-glossary.md` | 293 | `\| Tee \| Operis → published edition + card generation queue (same source, two streams) \|` | Backpressure | `backpressure` | medium |
| `scl-deep/systems-glossary.md` | 89 | `\| Alias \| DNS / MTG \| Two names for the same address. Conversion between aliases is a single lookup — no...` | Resolution | `resolution` | low |
| `scl-deep/systems-glossary.md` | 157 | `Complete lookup: PPL concept → systems term → definition source.` | Resolution | `resolution` | low |
| `scl-deep/systems-glossary.md` | 171 | `\| YAML frontmatter struct between steps \| Pipe \| §2 Data Flow \|` | Filter | `filter` | low |
| `scl-deep/systems-glossary.md` | 229 | `Reverse lookup: systems term → PPL implementation.` | Resolution | `resolution` | low |

## scl-deep/systems-language-audit.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/systems-language-audit.md` | 197 | `\| `whiteboard.md` \| 38 \| `- [x] Audit workflow docs — scripts/README.md (full audit orchestrator + check...` | Pipeline | `pipeline` | high |
| `scl-deep/systems-language-audit.md` | 301 | `\| `seeds/codex-container-directory-v3.md` \| 198 \| `Create `.github/workflows/lint.yml` that triggers on ...` | Pipeline | `pipeline` | high |
| `scl-deep/systems-language-audit.md` | 339 | `## seeds/deck-campaign-workflow.md` | Pipeline | `pipeline` | high |
| `scl-deep/systems-language-audit.md` | 345 | `\| `seeds/deck-campaign-workflow.md` \| 119 \| `- Campaign state view in `whiteboard.md` as the permanent s...` | Pipeline | `pipeline` | high |
| `scl-deep/systems-language-audit.md` | 346 | `\| `seeds/deck-campaign-workflow.md` \| 133 \| `Until then, this seed informs session planning but the whit...` | Pipeline | `pipeline` | high |
| `scl-deep/systems-language-audit.md` | 347 | `\| `seeds/deck-campaign-workflow.md` \| 25 \| `LANE B: Identity Doc     — Exercise mapping, duplicate audit...` | Pipeline | `pipeline` | high |
| `scl-deep/systems-language-audit.md` | 348 | `\| `seeds/deck-campaign-workflow.md` \| 35 \| `- E requires D (audit must pass before review queue opens)` ...` | Pipeline | `pipeline` | high |
| `scl-deep/systems-language-audit.md` | 349 | `\| `seeds/deck-campaign-workflow.md` \| 71 \| `- ⚠️ Complete with known issues (regen queue active)` \| Bac...` | Pipeline | `pipeline` | high |
| `scl-deep/systems-language-audit.md` | 351 | `\| `seeds/deck-campaign-workflow.md` \| 112 \| `Needs: full Lane C completion (regen queue), Lane D, Lane E...` | Pipeline | `pipeline` | high |
| `scl-deep/systems-language-audit.md` | 872 | `\| `middle-math/rotation/junction-algorithm.md` \| 157 \| `In the current Phase 2 card generation workflow,...` | Pipeline | `pipeline` | high |
| `scl-deep/systems-language-audit.md` | 695 | `\| `scl-deep/systems-language-audit.md` \| 1016 \| `\\| `seeds/deck-campaign-workflow.md` \\| 35 \\| `- E r...` | Backpressure | `backpressure` | medium |
| `scl-deep/systems-language-audit.md` | 697 | `\| `scl-deep/systems-language-audit.md` \| 1018 \| `\\| `seeds/deck-campaign-workflow.md` \\| 71 \\| `- ⚠️ ...` | Backpressure | `backpressure` | medium |
| `scl-deep/systems-language-audit.md` | 698 | `\| `scl-deep/systems-language-audit.md` \| 1021 \| `\\| `seeds/deck-campaign-workflow.md` \\| 112 \\| `Need...` | Backpressure | `backpressure` | medium |
| `scl-deep/systems-language-audit.md` | 866 | `\| `middle-math/rotation/junction-algorithm.md` \| 3 \| `The 🚂 Junction block at the end of every workout s...` | Draft offering | `draft offering` | medium |
| `scl-deep/systems-language-audit.md` | 866 | `\| `middle-math/rotation/junction-algorithm.md` \| 3 \| `The 🚂 Junction block at the end of every workout s...` | Draft offering | `draft offering` | medium |
| `scl-deep/systems-language-audit.md` | 91 | `## card-template-v2.md` | Poka-yoke | `poka-yoke` | low |
| `scl-deep/systems-language-audit.md` | 95 | `\| `card-template-v2.md` \| 20 \| `7. **🚂 JUNCTION** — log space (blank fields, not pre-filled) + 1–3 follo...` | Poka-yoke | `poka-yoke` | low |
| `scl-deep/systems-language-audit.md` | 157 | `\| `systems-language-audit.md` \| 335 \| `\\| CLAUDE.md \\| Validation checklist (agent mental check) vs sc...` | Poka-yoke | `poka-yoke` | low |
| `scl-deep/systems-language-audit.md` | 172 | `\| `whiteboard.md` \| 38 \| `- [x] Audit workflow docs — scripts/README.md (full audit orchestrator + check...` | Poka-yoke | `poka-yoke` | low |
| `scl-deep/systems-language-audit.md` | 295 | `\| `seeds/codex-container-directory-v3.md` \| 198 \| `Create `.github/workflows/lint.yml` that triggers on ...` | Filter | `filter` | low |
| `scl-deep/systems-language-audit.md` | 711 | `\| `scl-deep/systems-language-audit.md` \| 364 \| `\\| `middle-math/exercise-engine/selection-algorithm.md`...` | Poka-yoke | `poka-yoke` | low |
| `scl-deep/systems-language-audit.md` | 769 | `\| `middle-math/exercise-engine/selection-algorithm.md` \| 219 \| `**Fully-specified card (no template):** ...` | Poka-yoke | `poka-yoke` | low |
| `scl-deep/systems-language-audit.md` | 770 | `\| `middle-math/exercise-engine/selection-algorithm.md` \| 219 \| `**Fully-specified card (no template):** ...` | Filter | `filter` | low |
| `scl-deep/systems-language-audit.md` | 778 | `## middle-math/exercise-engine/template-spec.md` | Poka-yoke | `poka-yoke` | low |
| `scl-deep/systems-language-audit.md` | 1061 | `## deck-identities/template.md` | Poka-yoke | `poka-yoke` | low |
| `scl-deep/systems-language-audit.md` | 1065 | `\| `deck-identities/template.md` \| 6 \| `## 2) Coverage Map (Type × Color)` \| Source map \| `source map` ...` | Poka-yoke | `poka-yoke` | low |

## scl-deep/type-specifications.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/type-specifications.md` | — | — | — | — | No inconsistencies found |

## scl-deep/vocabulary-standard.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `scl-deep/vocabulary-standard.md` | 42 | `\| journey (training context) \| Spiritual-wellness register. \| "progression," "process," "career" \|` | Pipeline | `pipeline` | medium |

## middle-math/ARCHITECTURE.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/ARCHITECTURE.md` | 21 | `Master cards define exercise roles — movement pattern, block position, compound/isolation, bilateral/unilat...` | Poka-yoke | `poka-yoke` | low |
| `middle-math/ARCHITECTURE.md` | 27 | `See `exercise-engine/` for the selection algorithm, family trees, and template specification.` | Poka-yoke | `poka-yoke` | low |
| `middle-math/ARCHITECTURE.md` | 99 | `The emoji is the display layer. The number is the computation layer. Conversion between them is a single ar...` | Resolution | `resolution` | low |
| `middle-math/ARCHITECTURE.md` | 111 | `Card generation (Phase 2) continues independently. Middle-math does not block it. The 1,600 remaining cards...` | Poka-yoke | `poka-yoke` | low |

## middle-math/README.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/README.md` | 56 | `template-based format is an evolution, not a replacement. Both formats` | Poka-yoke | `poka-yoke` | low |

## middle-math/exercise-engine/README.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/exercise-engine/README.md` | 3 | `The procedural pipeline that fills template roles with specific exercises based on zip code constraints and...` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/README.md` | 7 | `Static card generation names specific exercises. One user, one exercise per role. The procedural engine sep...` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/README.md` | 13 | `Fully-specified workout cards (the current format — named exercises throughout) remain valid. The template ...` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/README.md` | 16 | `- Template card: engine runs the full selection pipeline and fills each role dynamically` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/README.md` | 18 | `During Phase 2 (card generation), all new cards are fully-specified. The template format will be phased in ...` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/README.md` | 26 | `- `template-spec.md` — How master cards define roles, not exercises` | Poka-yoke | `poka-yoke` | low |

## middle-math/exercise-engine/family-trees.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/exercise-engine/family-trees.md` | — | — | — | — | No inconsistencies found |

## middle-math/exercise-engine/selection-algorithm.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/exercise-engine/selection-algorithm.md` | 5 | `The 6-step pipeline from template role to specific exercise. Deterministic given fixed inputs. No inference...` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/selection-algorithm.md` | 14 | `Step 1: Read the template role` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/selection-algorithm.md` | 29 | `## Step 1 — Read the Template Role` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/selection-algorithm.md` | 31 | `A template role defines what kind of movement belongs in a given block position. It specifies:` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/selection-algorithm.md` | 219 | `**Fully-specified card (no template):** Skip Steps 1–4. The exercise is named directly. Go to Step 5 for pr...` | Filter | `filter` | low |
| `middle-math/exercise-engine/selection-algorithm.md` | 219 | `**Fully-specified card (no template):** Skip Steps 1–4. The exercise is named directly. Go to Step 5 for pr...` | Poka-yoke | `poka-yoke` | low |

## middle-math/exercise-engine/substitution-rules.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/exercise-engine/substitution-rules.md` | — | — | — | — | No inconsistencies found |

## middle-math/exercise-engine/template-spec.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/exercise-engine/template-spec.md` | 1 | `# Template Specification` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/template-spec.md` | 9 | `A template role replaces a named exercise in a card with a role declaration. The engine resolves the role t...` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/template-spec.md` | 75 | `**Template card:**` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/template-spec.md` | 91 | `No existing card needs to be converted. Template format is additive.` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/template-spec.md` | 95 | `## Worked Example: Converting a Deck 08 Card to Template Format` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/template-spec.md` | 109 | `**Template format equivalent (⛽🔨🪡🔵):**` | Poka-yoke | `poka-yoke` | low |
| `middle-math/exercise-engine/template-spec.md` | 140 | `The template version produces different exercise selections for different users. The fully-specified versio...` | Poka-yoke | `poka-yoke` | low |

## middle-math/exercise-engine/transfer-ratios.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/exercise-engine/transfer-ratios.md` | — | — | — | — | No inconsistencies found |

## middle-math/rendering/README.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/rendering/README.md` | — | — | — | — | No inconsistencies found |

## middle-math/rendering/operis-weight-derivation.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/rendering/operis-weight-derivation.md` | — | — | — | — | No inconsistencies found |

## middle-math/rendering/progressive-disclosure.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/rendering/progressive-disclosure.md` | — | — | — | — | No inconsistencies found |

## middle-math/rendering/ui-weight-derivation.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/rendering/ui-weight-derivation.md` | — | — | — | — | No inconsistencies found |

## middle-math/roots/README.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/roots/README.md` | — | — | — | — | No inconsistencies found |

## middle-math/roots/almanac-archive.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/roots/almanac-archive.md` | — | — | — | — | No inconsistencies found |

## middle-math/roots/four-layers.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/roots/four-layers.md` | — | — | — | — | No inconsistencies found |

## middle-math/roots/octave-logic.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/roots/octave-logic.md` | — | — | — | — | No inconsistencies found |

## middle-math/roots/order-notation.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/roots/order-notation.md` | — | — | — | — | No inconsistencies found |

## middle-math/rotation/README.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/rotation/README.md` | — | — | — | — | No inconsistencies found |

## middle-math/rotation/fatigue-model.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/rotation/fatigue-model.md` | — | — | — | — | No inconsistencies found |

## middle-math/rotation/junction-algorithm.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/rotation/junction-algorithm.md` | 3 | `The 🚂 Junction block at the end of every workout suggests 1–3 follow-up zip codes. In the current card gene...` | Pipeline | `pipeline` | high |
| `middle-math/rotation/junction-algorithm.md` | 157 | `In the current Phase 2 card generation workflow, Junction suggestions are written by the card author based ...` | Pipeline | `pipeline` | high |
| `middle-math/rotation/junction-algorithm.md` | 3 | `The 🚂 Junction block at the end of every workout suggests 1–3 follow-up zip codes. In the current card gene...` | Draft offering | `draft offering` | medium |
| `middle-math/rotation/junction-algorithm.md` | 3 | `The 🚂 Junction block at the end of every workout suggests 1–3 follow-up zip codes. In the current card gene...` | Draft offering | `draft offering` | medium |
| `middle-math/rotation/junction-algorithm.md` | 16 | `"user_id":          uuid,                  # For ledger lookup` | Resolution | `resolution` | low |
| `middle-math/rotation/junction-algorithm.md` | 22 | `## Computation Steps` | Filter | `filter` | low |
| `middle-math/rotation/junction-algorithm.md` | 157 | `In the current Phase 2 card generation workflow, Junction suggestions are written by the card author based ...` | Filter | `filter` | low |

## middle-math/rotation/reverse-weight-resolution.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/rotation/reverse-weight-resolution.md` | 50 | `**Process**:` | Pipeline | `pipeline` | medium |
| `middle-math/rotation/reverse-weight-resolution.md` | 72 | `**Process**:` | Pipeline | `pipeline` | medium |
| `middle-math/rotation/reverse-weight-resolution.md` | 94 | `**Process**:` | Pipeline | `pipeline` | medium |
| `middle-math/rotation/reverse-weight-resolution.md` | 150 | `- `zip-web/zip-web-signatures.md` — provides the fatigue signature lookup table for Phase 1` | Resolution | `resolution` | low |

## middle-math/rotation/rotation-engine-spec.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/rotation/rotation-engine-spec.md` | — | — | — | — | No inconsistencies found |

## middle-math/schemas/README.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/schemas/README.md` | — | — | — | — | No inconsistencies found |

## middle-math/schemas/exercise-families-schema.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/schemas/exercise-families-schema.md` | — | — | — | — | No inconsistencies found |

## middle-math/schemas/exercise-library-schema.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/schemas/exercise-library-schema.md` | — | — | — | — | No inconsistencies found |

## middle-math/schemas/user-ledger-schema.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/schemas/user-ledger-schema.md` | 3 | `Raw workout log. One row per exercise set per logged session. The source of truth for all user data.` | Authoritative source | `authoritative source` | high |

## middle-math/schemas/user-profile-schema.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/schemas/user-profile-schema.md` | — | — | — | — | No inconsistencies found |

## middle-math/schemas/user-toggles-schema.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/schemas/user-toggles-schema.md` | — | — | — | — | No inconsistencies found |

## middle-math/schemas/zip-metadata-schema.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/schemas/zip-metadata-schema.md` | — | — | — | — | No inconsistencies found |

## middle-math/schemas/zip-weight-cache-schema.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/schemas/zip-weight-cache-schema.md` | — | — | — | — | No inconsistencies found |

## middle-math/user-context/README.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/user-context/README.md` | 7 | `1. **Exercise Ledger** — The raw log. One row per exercise per logged workout. Tagged with zip code context...` | Authoritative source | `authoritative source` | high |

## middle-math/user-context/cross-context-translation.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/user-context/cross-context-translation.md` | — | — | — | — | No inconsistencies found |

## middle-math/user-context/exercise-ledger-spec.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/user-context/exercise-ledger-spec.md` | — | — | — | — | No inconsistencies found |

## middle-math/user-context/exercise-profile-spec.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/user-context/exercise-profile-spec.md` | — | — | — | — | No inconsistencies found |

## middle-math/user-context/toggle-system-spec.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/user-context/toggle-system-spec.md` | — | — | — | — | No inconsistencies found |

## middle-math/weights/README.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/weights/README.md` | — | — | — | — | No inconsistencies found |

## middle-math/weights/axis-weights.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/weights/axis-weights.md` | — | — | — | — | No inconsistencies found |

## middle-math/weights/block-weights.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/weights/block-weights.md` | 89 | `Required: Yes — always present. Must include 1–3 follow-up zip codes with rationale.` | Draft offering | `draft offering` | medium |
| `middle-math/weights/block-weights.md` | 89 | `Required: Yes — always present. Must include 1–3 follow-up zip codes with rationale.` | Draft offering | `draft offering` | medium |
| `middle-math/weights/block-weights.md` | 99 | `\| 🦋 Hypertrophy \| +6 \| "Always present." Logging volume and next-session bridge \|` | Draft offering | `draft offering` | medium |
| `middle-math/weights/block-weights.md` | 113 | `🚂 is the penultimate block in every session. 🧮 SAVE always follows. Format requires 1–3 follow-up zip codes...` | Draft offering | `draft offering` | medium |
| `middle-math/weights/block-weights.md` | 113 | `🚂 is the penultimate block in every session. 🧮 SAVE always follows. Format requires 1–3 follow-up zip codes...` | Draft offering | `draft offering` | medium |

## middle-math/weights/color-weights.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/weights/color-weights.md` | — | — | — | — | No inconsistencies found |

## middle-math/weights/interaction-rules.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/weights/interaction-rules.md` | — | — | — | — | No inconsistencies found |

## middle-math/weights/operator-weights.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/weights/operator-weights.md` | — | — | — | — | No inconsistencies found |

## middle-math/weights/order-weights.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/weights/order-weights.md` | — | — | — | — | No inconsistencies found |

## middle-math/weights/type-weights.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/weights/type-weights.md` | — | — | — | — | No inconsistencies found |

## middle-math/weights/weight-system-spec.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `middle-math/weights/weight-system-spec.md` | 37 | `For any given zip code (ORDER AXIS TYPE COLOR), the weight vector is computed in four steps.` | Filter | `filter` | low |

## deck-identities/README.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `deck-identities/README.md` | — | — | — | — | No inconsistencies found |

## deck-identities/deck-07-identity.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `deck-identities/deck-07-identity.md` | 15 | `## 2) Coverage Map (Type × Color)` | Source map | `source map` | medium |
| `deck-identities/deck-07-identity.md` | 46 | `## 4) Content Regeneration Queue` | Backpressure | `backpressure` | medium |

## deck-identities/deck-08-identity.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `deck-identities/deck-08-identity.md` | 10 | `## 2) Coverage Map (Type × Color)` | Source map | `source map` | medium |

## deck-identities/deck-08-rename-log.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `deck-identities/deck-08-rename-log.md` | — | — | — | — | No inconsistencies found |

## deck-identities/deck-09-identity.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `deck-identities/deck-09-identity.md` | 10 | `## 2) Coverage Map (Type × Color)` | Source map | `source map` | medium |

## deck-identities/naming-convention.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `deck-identities/naming-convention.md` | 3 | `**Template:** `[Primary Movement or Equipment+Exercise] — [Target Muscle/Focus, Context Modifier]`` | Poka-yoke | `poka-yoke` | low |

## deck-identities/template.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `deck-identities/template.md` | 6 | `## 2) Coverage Map (Type × Color)` | Source map | `source map` | medium |
| `deck-identities/template.md` | 1 | `# Deck XX Identity Template` | Poka-yoke | `poka-yoke` | low |

## zip-web/README.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/README.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-01-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-01-pods.md` | 61 | `\| N (Progression) \| ⛽🏛🪡🔵 \| Heavy classic pulls follow foundation pressing — the bilateral pattern is gro...` | Filter | `filter` | low |
| `zip-web/zip-web-pods/deck-01-pods.md` | 91 | `\| N (Progression) \| ⛽🏛🪡🔴 \| High-density pulling at strength level follows high-density foundation pressi...` | Filter | `filter` | low |
| `zip-web/zip-web-pods/deck-01-pods.md` | 185 | `\| N (Progression) \| ⛽🏛🛒🔵 \| Heavy classic presses follow foundation pulling — the bilateral pressing plan...` | Filter | `filter` | low |
| `zip-web/zip-web-pods/deck-01-pods.md` | 215 | `\| N (Progression) \| ⛽🏛🛒🔴 \| High-density strength pressing follows high-density foundation pulling — Orde...` | Filter | `filter` | low |
| `zip-web/zip-web-pods/deck-01-pods.md` | 433 | `\| N (Progression) \| ⛽🏛🛒🔵 \| Heavy classic presses follow foundation power — upper body strength pressing ...` | Filter | `filter` | low |

## zip-web/zip-web-pods/deck-02-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-02-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-03-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-03-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-04-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-04-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-05-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-05-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-06-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-06-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-07-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-07-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-08-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-08-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-09-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-09-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-10-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-10-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-11-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-11-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-12-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-12-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-13-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-13-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-14-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-14-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-15-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-15-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-16-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-16-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-17-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-17-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-18-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-18-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-19-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-19-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-20-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-20-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-21-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-21-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-22-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-22-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-23-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-23-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-24-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-24-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-25-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-25-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-26-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-26-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-27-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-27-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-28-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-28-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-29-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-29-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-30-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-30-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-31-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-31-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-32-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-32-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-33-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-33-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-34-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-34-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-35-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-35-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-36-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-36-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-37-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-37-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-38-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-38-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-39-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-39-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-40-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-40-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-41-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-41-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-pods/deck-42-pods.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-pods/deck-42-pods.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-registry.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-registry.md` | — | — | — | — | No inconsistencies found |

## zip-web/zip-web-rules.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-rules.md` | 3 | `This is the single source of truth for how zip-web pods are constructed. All agents (Claude Code, Codex, Ra...` | Authoritative source | `authoritative source` | high |
| `zip-web/zip-web-rules.md` | 235 | `## Pod Validation Checklist` | Poka-yoke | `poka-yoke` | low |
| `zip-web/zip-web-rules.md` | 302 | `e. Run the pod validation checklist` | Poka-yoke | `poka-yoke` | low |

## zip-web/zip-web-signatures.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `zip-web/zip-web-signatures.md` | — | — | — | — | No inconsistencies found |

## .claude/agents/card-generator.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.claude/agents/card-generator.md` | — | — | — | — | No inconsistencies found |

## .claude/agents/deck-auditor.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.claude/agents/deck-auditor.md` | 35 | `- 1–3 follow-up zip codes are suggested` | Draft offering | `draft offering` | medium |
| `.claude/agents/deck-auditor.md` | 35 | `- 1–3 follow-up zip codes are suggested` | Draft offering | `draft offering` | medium |
| `.claude/agents/deck-auditor.md` | 53 | `- Examples: Junction routing to a better follow-up zip, tonal refinement` | Draft offering | `draft offering` | medium |

## .claude/agents/progress-tracker.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.claude/agents/progress-tracker.md` | — | — | — | — | No inconsistencies found |

## .claude/skills/audit-deck.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.claude/skills/audit-deck.md` | 9 | `## Steps` | Filter | `filter` | low |

## .claude/skills/build-deck-identity/SKILL.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.claude/skills/build-deck-identity/SKILL.md` | 11 | `## Workflow` | Pipeline | `pipeline` | high |
| `.claude/skills/build-deck-identity/SKILL.md` | 27 | `- `deck-identities/template.md` — format structure` | Poka-yoke | `poka-yoke` | low |
| `.claude/skills/build-deck-identity/SKILL.md` | 67 | `Use the template from `deck-identities/template.md`.` | Poka-yoke | `poka-yoke` | low |

## .claude/skills/compile-scl.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.claude/skills/compile-scl.md` | 6 | `## Steps` | Filter | `filter` | low |

## .claude/skills/generate-card/SKILL.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.claude/skills/generate-card/SKILL.md` | 11 | `## Workflow` | Pipeline | `pipeline` | high |
| `.claude/skills/generate-card/SKILL.md` | 55 | `Run the full validation checklist from CLAUDE.md mentally before writing.` | Poka-yoke | `poka-yoke` | low |
| `.claude/skills/generate-card/SKILL.md` | 81 | `- Template: `[Primary Movement or Equipment+Exercise] — [Target Muscle/Focus, Context Modifier]`` | Poka-yoke | `poka-yoke` | low |

## .claude/skills/plant-seed.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.claude/skills/plant-seed.md` | 6 | `## Steps` | Filter | `filter` | low |
| `.claude/skills/plant-seed.md` | 9 | `2. Use this frontmatter template:` | Poka-yoke | `poka-yoke` | low |

## .claude/skills/progress-report/SKILL.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.claude/skills/progress-report/SKILL.md` | — | — | — | — | No inconsistencies found |

## .claude/skills/ralph-loop.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.claude/skills/ralph-loop.md` | 32 | `- Run the validation checklist for every pod before writing` | Poka-yoke | `poka-yoke` | low |

## .claude/skills/retrofit-deck/SKILL.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.claude/skills/retrofit-deck/SKILL.md` | 11 | `## Workflow` | Pipeline | `pipeline` | high |
| `.claude/skills/retrofit-deck/SKILL.md` | 23 | `- Template: `[Primary Movement or Equipment+Exercise] — [Target Muscle/Focus, Context Modifier]`` | Poka-yoke | `poka-yoke` | low |

## .claude/skills/scaffold-html.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.claude/skills/scaffold-html.md` | 6 | `## Steps` | Filter | `filter` | low |

## .claude/skills/validate-card.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.claude/skills/validate-card.md` | 9 | `## Steps` | Filter | `filter` | low |
| `.claude/skills/validate-card.md` | 14 | `4. Run the full validation checklist from CLAUDE.md:` | Poka-yoke | `poka-yoke` | low |

## .codex/HANDOFF-CONTRACTS.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.codex/HANDOFF-CONTRACTS.md` | 12 | `\| explorer \| Entire repository read-only for discovery, dependency lookup, and evidence gathering \| None...` | Resolution | `resolution` | low |
| `.codex/HANDOFF-CONTRACTS.md` | 20 | `- Include a validation checklist response in the handoff packet.` | Poka-yoke | `poka-yoke` | low |

## .codex/NEXT-ROUND-HANDOFF.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.codex/NEXT-ROUND-HANDOFF.md` | 95 | `"Use `.codex/NEXT-ROUND-HANDOFF.md` as source of truth for this session.` | Authoritative source | `authoritative source` | high |
| `.codex/NEXT-ROUND-HANDOFF.md` | 46 | `Build a reliable **container handoff + completion ledger** so each Codex run can mark jobs complete with ev...` | Backpressure | `backpressure` | medium |
| `.codex/NEXT-ROUND-HANDOFF.md` | 72 | `### Task C — Sync whiteboard queue with merged reality` | Backpressure | `backpressure` | medium |
| `.codex/NEXT-ROUND-HANDOFF.md` | 76 | `- Keep only actually-open follow-ups in the active queue.` | Backpressure | `backpressure` | medium |
| `.codex/NEXT-ROUND-HANDOFF.md` | 77 | `- Remove queue/session duplication where possible.` | Backpressure | `backpressure` | medium |
| `.codex/NEXT-ROUND-HANDOFF.md` | 90 | `- `whiteboard.md` queue reflects current merged state and no stale open tasks.` | Backpressure | `backpressure` | medium |

## .codex/TASK-ARCHITECTURE.md

| File Path | Line Number (approx) | Found Term | Glossary Term | Suggested Replacement | Severity |
|---|---:|---|---|---|---|
| `.codex/TASK-ARCHITECTURE.md` | 18 | `\| CX-07 \| CI Lint Workflow \| CX-05, CX-06 \| 2 \| PENDING \| — \| — \|` | Pipeline | `pipeline` | high |
