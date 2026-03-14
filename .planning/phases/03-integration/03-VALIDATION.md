---
phase: 03
slug: integration
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-03-14
---

# Phase 03 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Vitest ^3.2.4 (installed, 6,815 tests passing) |
| **Config file** | canvas/vite.config.ts (test.include: "tests/**/*.test.ts") |
| **Quick run command** | `cd canvas && npm test` |
| **Full suite command** | `cd canvas && npm test` |
| **Estimated runtime** | ~2 seconds |

---

## Sampling Rate

- **After every task commit:** Run `cd canvas && npm test`
- **After every plan wave:** Run `cd canvas && npm test`
- **Before `/gsd:verify-work`:** Full suite must be green
- **Max feedback latency:** 2 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 03-01-01 | 01 | 1 | WGHT-03 | unit | `cd canvas && npm test -- resolver.test.ts` | ❌ W0 | ⬜ pending |
| 03-01-01 | 01 | 1 | WGHT-04 | unit | `cd canvas && npm test -- resolver.test.ts` | ❌ W0 | ⬜ pending |
| 03-02-01 | 02 | 1 | PARS-01 | unit | `cd canvas && npm test -- scorer.test.ts` | ❌ W0 | ⬜ pending |
| 03-02-01 | 02 | 1 | PARS-06 | unit | `cd canvas && npm test -- scorer.test.ts` | ❌ W0 | ⬜ pending |
| 03-02-01 | 02 | 1 | PARS-07 | unit | `cd canvas && npm test -- scorer.test.ts` | ❌ W0 | ⬜ pending |
| 03-02-02 | 02 | 1 | PARS-08 | integration | `cd canvas && npm test -- scorer.test.ts` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `canvas/tests/resolver.test.ts` — stubs for WGHT-03, WGHT-04
- [ ] `canvas/tests/scorer.test.ts` — stubs for PARS-01, PARS-06, PARS-07, PARS-08
- [ ] Runtime dependency install: `cd canvas && npm install fastest-levenshtein fuse.js`

*Existing infrastructure covers framework and config.*

---

## Manual-Only Verifications

*All phase behaviors have automated verification.*

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 2s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
