---
phase: 06
slug: claude-code-infrastructure
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-03-15
---

# Phase 06 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Vitest ^3.2.4 (existing — regression check only) |
| **Config file** | canvas/vite.config.ts |
| **Quick run command** | `cd canvas && npm test` |
| **Full suite command** | `cd canvas && npm test` |
| **Estimated runtime** | ~3 seconds |

Phase 6 deliverables are configuration files (skills, agents, hooks). They are validated by file inspection, not Vitest. Existing tests confirm no regressions.

---

## Sampling Rate

- **After every task commit:** Run `cd canvas && npm test` (regression check)
- **After every plan wave:** Run `cd canvas && npm test`
- **Before `/gsd:verify-work`:** Full suite green + manual inspection of each deliverable
- **Max feedback latency:** 3 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 06-01-01 | 01 | 1 | CLCD-01 | manual | Inspect .claude/skills/blank-canvas/SKILL.md | W0 | pending |
| 06-01-01 | 01 | 1 | CLCD-02 | manual | Inspect .claude/agents/canvas-renderer.md | W0 | pending |
| 06-01-01 | 01 | 1 | CLCD-03 | manual | Inspect .claude/settings.json hook entry | W0 | pending |

*Status: pending · green · red · flaky*

---

## Wave 0 Requirements

- [ ] `.claude/skills/blank-canvas/SKILL.md` — CLCD-01
- [ ] `.claude/agents/canvas-renderer.md` — CLCD-02
- [ ] `canvas/components/.gitkeep` — stub for canvas-renderer write target

No new test framework installs needed.

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Skill frontmatter and body correct | CLCD-01 | Config file, not code | Read SKILL.md, verify allowed-tools, description |
| Agent scope limited to canvas/components/ | CLCD-02 | Config file, not code | Read agent .md, verify scope constraint in body |
| Hook path-gates to canvas/ only | CLCD-03 | Hook behavior not testable by Vitest | Edit a canvas/ file, verify hook fires; edit a cards/ file, verify hook does NOT fire |
| Hook never uses exit code 2 | CLCD-03 | Runtime behavior | Inspect hook script, confirm all paths exit 0 |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: regression tests run after each commit
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 3s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
