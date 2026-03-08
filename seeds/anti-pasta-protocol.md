---
title: Anti-Pasta Protocol
status: SEED
planted: 2026-03-08
category: infrastructure
---

# Anti-Pasta Protocol

## What It Is

The Anti-Pasta is a structured architectural review document and session-init protocol. It's the project's version of a systems health check — a brief that any session (Claude Code, Codex, temp architect) can generate or consume to understand the full state of the project, surface critical questions, and prevent architectural drift.

## The Name

Anti-Pasta. Because the entire system is working toward lasagna (clean layers) and a clean bus (central authority). The Anti-Pasta is the review that prevents spaghetti code, spaghetti architecture, and spaghetti thinking. It's also just fun to say.

"What's the anti-pasta?" initiates the brief.

## Format

The Anti-Pasta is a markdown document generated per-session or on-demand. It lives at `reports/anti-pasta/YYYY-MM-DD.md` and contains 5 sections:

1. **System Snapshot** — Current phase, card count, exercise library version, abacus status, branch state, open PRs, whiteboard phase, last session summary. Pure facts. No interpretation.

2. **Architecture Health (5 Standing Questions)** — Five permanent questions that every Anti-Pasta answers. The answers update each time. The questions never change:
   - Q1: What is the current bus?
   - Q2: Where is the lasagna breaking?
   - Q3: What's the thinnest layer?
   - Q4: What would break at 10x scale?
   - Q5: What decision is Jake avoiding?

3. **Active Contracts** — Pulled from whiteboard.md. What's in progress, queued, blocked.

4. **Seeds Inventory** — All planted seeds with status. Which are approaching activation? Which are stale? Which need Jake's input?

5. **Next Session Recommendations** — Prioritized recommendation based on the answers. Not a command. Jake decides.

## Session-Init Protocol

Any Claude Code or Codex session can begin with:

> "What's the anti-pasta?"

The agent reads CLAUDE.md, whiteboard.md, and the most recent Anti-Pasta report, then generates a fresh one. The fresh report becomes the session's orientation document. Work begins from there.

## Generation Rules

- Read CLAUDE.md, whiteboard.md, and the previous Anti-Pasta report before generating
- Answer all 5 questions honestly. If a question doesn't apply, say so
- Section 1 is facts only — no interpretation, no editorializing
- Section 5 is recommendations — the agent's best judgment, not a binding contract
- The report is append-only. Never delete previous reports. Each date gets its own file
- If generating mid-session, use the current date

## Activation Status

Currently: on-demand only. Invoked by "what's the anti-pasta?" command.

Future: may become a SessionStart hook that spawns automatically, but deferred to avoid token weight and boot time costs.

## Template

See `reports/anti-pasta/TEMPLATE.md` for the reusable format.
