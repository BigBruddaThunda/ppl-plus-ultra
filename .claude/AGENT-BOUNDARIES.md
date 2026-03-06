# PPL± Agent Boundaries
**CX-19 — Formalized 2026-03-06 (Session 037)**

This document is the human-readable governance layer for the multi-agent PPL± system.
It defines which agents can read, write, or never touch which file categories.
The technical firewall lives in `.codex/TASK-ARCHITECTURE.md` (Context Firewall Rules section).

---

## Agent Roster

| Agent | Type | Model | Role |
|-------|------|-------|------|
| **Claude Code** | Primary agent | claude-sonnet-4-6 | Session orchestration, architecture decisions, file writes across repo |
| **Codex container** | Batch agent | External (OpenAI Codex) | Infrastructure-only containers (CX-series) — scripts, schemas, tooling |
| **card-generator** | Subagent | claude-opus-4-6 | Single-card generation in isolated context |
| **deck-auditor** | Subagent | claude-sonnet-4-6 | Read-only SCL compliance audit of completed decks |
| **progress-tracker** | Subagent | claude-haiku-4-5 | Lightweight repo state scan and progress reporting |

---

## Read / Write / Never-Touch Matrix

| File Category | Claude Code | Codex | card-generator | deck-auditor | progress-tracker |
|---------------|:-----------:|:-----:|:--------------:|:------------:|:----------------:|
| `CLAUDE.md` | R/W (scoped) | R | R | R | R |
| `scl-directory.md` | R | R | R | R | R |
| `exercise-library.md` | R | R (parse only) | R | R | — |
| `whiteboard.md` | R/W | R | — | — | R |
| `session-log.md` | R/W | — | — | — | — |
| `cards/**` | R/W | **Never** | W (assigned file only) | R | R (status scans) |
| `middle-math/**` | R/W | R/W | R | — | — |
| `scripts/**` | R/W | R/W | — | — | R |
| `seeds/**` | R/W | R | — | — | — |
| `scl-deep/**` | R/W | R/W (glossary + audit only) | R | — | — |
| `deck-identities/**` | R/W | R | R | R | R |
| `deck-cosmograms/**` | R/W | R/W (stubs only) | R | R | — |
| `.codex/**` | R/W | R/W | — | — | — |
| `.claude/**` | R/W | R/W | — | — | — |
| `.github/**` | R/W | R/W | — | — | — |
| `sql/**` | R/W | R/W | — | — | — |
| `html/**` | R/W | R/W | — | — | — |
| `docs/**` | R/W | R/W | — | — | R |
| `operis-editions/**` (historical-events) | R/W | R/W (scaffolds only) | — | — | — |
| `operis-editions/**` (editions) | R/W | **Never** | — | — | — |
| `reports/**` | R/W | R/W | — | R | R |
| `zip-web/**` | R/W | R | — | — | — |

**Key:**
- `R` — may read
- `R/W` — may read and write
- `—` — not applicable / agent does not touch this category
- **Never** — hard prohibition; agent must not write here under any circumstances

---

## Per-Agent Write Constraints

### Claude Code
- Full write access across repo within session scope.
- `CLAUDE.md` edits are restricted: only sections explicitly named in the active CX container's Writes list. Never freelance edits to CLAUDE.md.
- Does not push to main/master without explicit user approval.

### Codex Container
- Writes only to infrastructure paths: `middle-math/`, `scripts/`, `sql/`, `.codex/`, `.claude/`, `.github/`, `html/design-system/`, `deck-cosmograms/` (stubs), `operis-editions/historical-events/` (scaffolds), `scl-deep/systems-glossary.md`, `scl-deep/systems-language-audit.md`.
- **Never writes to `cards/`** — card content is Claude Code / card-generator territory only.
- **Never writes to `scl-directory.md`** or `exercise-library.md`.
- **Never creates or modifies SCL rules, emoji definitions, or zip codes**.
- Codex containers operate on a declared write scope. Writes outside that scope are a firewall violation.

### card-generator Subagent
- Reads: `exercise-library.md`, `scl-directory.md`, assigned deck identity doc, assigned cosmogram (if populated), `CLAUDE.md`.
- Writes: **only the single card file assigned in the generation task**. No other writes.
- If an exercise is not in `exercise-library.md`, the card-generator flags it — it does not invent exercises.
- Renames stub file to complete filename as part of the same write.
- Does not update `whiteboard.md` — Claude Code handles session log updates.

### deck-auditor Subagent
- **Read only.** No writes permitted under any circumstances.
- Tools: Read, Grep, Glob, Bash (for script execution — read-only scripts only).
- Returns structured audit report (P0 critical, P1 format, P2 suggestions) to Claude Code.
- Does not mark cards CANONICAL — that is Jake's decision after reviewing the audit report.

### progress-tracker Subagent
- **Read only.** May run `scripts/progress-report.py` and `scripts/inventory.py` via Bash.
- Returns dashboard snapshot to Claude Code. Does not write output to disk.
- Lightweight — used at session start and on-demand status checks.

---

## Escalation Rules

### card-generator escalates to Claude Code when:
- An exercise required by the zip code is not in `exercise-library.md`.
- A zip code's frontmatter has conflicting parameters (e.g., GOLD exercise in a non-GOLD color).
- The assigned stub file does not exist at the expected path.
- Validation fails after generation (PostToolUse hook reports errors).
- A parameter is ambiguous and cannot be resolved from `scl-directory.md` alone.

### deck-auditor escalates to Claude Code when:
- P0 (critical) violations are found — these block CANONICAL status.
- A card file is missing (path exists in registry but file is gone).
- The audit detects duplicate primary exercises within a deck (same exercise used as the main lift in two different Color variants of the same Type).

### Codex escalates to Claude Code (via handoff document) when:
- A CX container's dependency is not met (container status must remain PENDING, not DONE).
- A script produces unexpected output during validation.
- A write would fall outside the declared scope for the active container.
- The handoff document references outdated state in `whiteboard.md`.

### Claude Code escalates to Jake when:
- A card has been generated but its primary exercise exists in `exercise-library.md` under an ambiguous or contested classification.
- A deck audit returns P0 violations that require a judgment call (e.g., is this exercise truly within the Order ceiling?).
- A whiteboard task has been DONE for 2+ sessions but Jake hasn't reviewed it.
- A new SCL rule, emoji, or zip code variant is proposed — Jake owns the SCL spec.

---

## Jake-Reserved Zones

These files and decisions belong exclusively to Jake. Agents may read but not modify:

| Zone | Files | Reason |
|------|-------|--------|
| SCL specification | `scl-directory.md` | The law. Agents apply it; Jake writes it. |
| Exercise library | `exercise-library.md` | Exercise validity is Jake's call. |
| CANONICAL status | Any card's `status: CANONICAL` frontmatter | Only Jake marks a card canonical. |
| Billing and auth | `.env`, API keys, Stripe config | Never in repo. Jake holds credentials. |
| Deck review (pod review) | Deck 07 Ralph pod | Must see the deck before the Ralph loop runs. |
| Operator overrides | `operator:` field in any card | Jake can override the default operator. Agents honor the override. |
| New emoji or SCL categories | Any expansion of the 61-emoji set | SCL is frozen during Phase 2. |

---

## Boundary Violations — What to Do

If an agent attempts to write outside its declared scope:

1. **Stop.** Do not write.
2. **Report** the attempted write path and why it was blocked.
3. **Wait** for Claude Code or Jake to authorize the write or redirect the task.

A boundary violation that goes unreported is worse than one that is caught. The firewall only works if agents surface the conflict.

---

*Reference: `.codex/TASK-ARCHITECTURE.md` (Context Firewall Rules) · `.codex/HANDOFF-CONTRACTS.md` (agent role contracts)*
