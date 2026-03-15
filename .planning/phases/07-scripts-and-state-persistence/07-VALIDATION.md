---
phase: 07
slug: scripts-and-state-persistence
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-03-15
---

# Phase 07 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Vitest ^3.2.4 (regression only) + bash assertions |
| **Config file** | canvas/vite.config.ts |
| **Quick run command** | `cd canvas && npm test` |
| **Full suite command** | `cd canvas && npm test` |
| **Estimated runtime** | ~3 seconds (Vitest) + ~5 seconds (bash assertions) |

Phase 7 deliverables are shell scripts and a skill. Validated by bash assertions, not Vitest. Existing tests confirm no regressions.

---

## Sampling Rate

- **After every task commit:** Run `cd canvas && npm test` (regression)
- **After every plan wave:** Run `cd canvas && npm test` + bash assertions
- **Before `/gsd:verify-work`:** Full suite green + bash assertions pass
- **Max feedback latency:** 8 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 07-01-01 | 01 | 1 | CLCD-04 | bash | canvas-to-production.sh integration test | W0 | pending |
| 07-01-01 | 01 | 1 | CLCD-05 | bash | batch-propagate.sh integration test | W0 | pending |
| 07-01-02 | 01 | 1 | CLCD-06 | bash | git check-ignore canvas/.local/ | W0 | pending |
| 07-01-02 | 01 | 1 | CLCD-06 | manual | /canvas-save skill invocation | W0 | pending |

---

## Wave 0 Requirements

- [ ] `canvas/scripts/canvas-to-production.sh` — CLCD-04
- [ ] `canvas/scripts/batch-propagate.sh` — CLCD-05
- [ ] `canvas/.local/.gitkeep` + .gitignore entry — CLCD-06
- [ ] `.claude/skills/canvas-save/SKILL.md` — CLCD-06

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| /canvas-save stages only canvas/ paths | CLCD-06 | Skill invocation requires Claude Code session | Invoke /canvas-save, check git log --name-only |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: regression tests run after each commit
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 8s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
