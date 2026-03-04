# Codex Next-Round Handoff Brief (Session 031)

Use this as the copy/paste kickoff brief for the next Codex container run.

## 1) Assumed Done and Merged (do not redo)

- `scripts/run-full-audit.sh`
  - Final success line now branches by mode:
    - Baseline: `✅ Full audit sequence passed`
    - Strict: `✅ Full audit sequence passed (strict mode)`
- `scripts/README.md`
  - Run-full-audit section now documents the baseline vs strict success text.
- `scripts/check-card-schema.py`
  - Tree-notation validation now fails if either token is missing (`├─` OR `│`), not only when both are missing.
- Schema fixtures
  - Added fixture that has only `├─` (must fail).
  - Added fixture that has only `│` (must fail).
- Contract C parser hardening
  - Added deterministic YAML-first frontmatter parsing with constrained fallback parser for Contract C shape.
  - Enforced: reject legacy `rooms`, require `sandbox-zips`, require `sandbox-total: 13`, enforce siblings/content-room counts, and required content-room fields (`zip`, `source`, `source-beat`).
  - Preserved fail-fast `ERROR:` behavior in `main()`.
- Contract C fixtures added
  - `valid-contract-c`
  - `legacy-key-rejection`
  - `missing-sandbox-total`
  - `malformed-content-room-entry` (missing `source`)
- Canonical status allow-list alignment
  - `scripts/check-card-schema.py` and `scripts/index-card-inventory.py` now both allow:
    - `EMPTY`
    - `GENERATED`
    - `GENERATED-V2`
    - `CANONICAL`
    - `REGEN-NEEDED`
    - `GENERATED-V2-REGEN-NEEDED`
  - `scripts/README.md` updated to match these values.
  - Added regen-status schema fixture to confirm acceptance.

## 2) Current State to Assume at Session Start

- These patches are assumed merged to `main`.
- Do **not** reopen already-closed fix loops above.
- Start from container/job tracking and next-wave task orchestration.

## 3) Next Round Primary Objective

Build a reliable **container handoff + completion ledger** so each Codex run can mark jobs complete with evidence and keep queue state synchronized.

## 4) Next Round Task Pack (ordered)

### Task A — Add container completion ledger metadata

Update `.codex/TASK-ARCHITECTURE.md`:
- Extend Container Index with:
  - `Status` (`PENDING | IN_PROGRESS | DONE | BLOCKED`)
  - `Completed In` (session id)
  - `Evidence` (artifact path[s])
  - `Commit` (hash)
- Add a short legend + update rule.
- Backfill known completed containers where evidence exists.

### Task B — Enforce closure fields in handoff contract

Update `.codex/HANDOFF-CONTRACTS.md`:
- In handoff packet format, add required closure fields:
  - `Completion Status`
  - `Commit`
  - `Evidence Paths`
  - `Merged To Main`
- Add prohibition: no completion mark without commit + evidence paths.
- Add routing closure: after validator/reviewer pass, update the container row in `.codex/TASK-ARCHITECTURE.md`.

### Task C — Sync whiteboard queue with merged reality

Update `whiteboard.md`:
- In Session 030 follow-up block, move now-completed items into a “Completed since Session 030” subsection.
- Keep only actually-open follow-ups in the active queue.
- Remove queue/session duplication where possible.

### Task D — Optional lightweight automation (if time)

Add a small script in `scripts/` to check that each DONE container row has:
- a commit hash,
- at least one evidence path,
- and a valid status token.

## 5) Definition of Done for the next run

- `.codex/TASK-ARCHITECTURE.md` includes explicit completion tracking columns + legend.
- `.codex/HANDOFF-CONTRACTS.md` requires closure evidence fields.
- `whiteboard.md` queue reflects current merged state and no stale open tasks.
- If Task D is included: script runs clean on repo state.

## 6) Kickoff Prompt (copy/paste)

"Use `.codex/NEXT-ROUND-HANDOFF.md` as source of truth for this session.
Treat all listed completed items as merged.
Execute Task A, then Task B, then Task C (and Task D only if time permits).
Do not regenerate card content.
Commit once with a single focused PR for container handoff architecture updates."
