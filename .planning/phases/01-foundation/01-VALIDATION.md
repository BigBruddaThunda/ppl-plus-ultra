---
phase: 1
slug: foundation
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-03-13
---

# Phase 1 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | vitest 4.x |
| **Config file** | canvas/vitest.config.ts (Wave 0 installs) |
| **Quick run command** | `cd canvas && npx vitest run --reporter=verbose` |
| **Full suite command** | `cd canvas && npx vitest run` |
| **Estimated runtime** | ~5 seconds |

---

## Sampling Rate

- **After every task commit:** Run `cd canvas && npx vitest run --reporter=verbose`
- **After every plan wave:** Run `cd canvas && npx vitest run`
- **Before `/gsd:verify-work`:** Full suite must be green
- **Max feedback latency:** 5 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 01-01-01 | 01 | 1 | FOUND-01 | structural | `test -f canvas/package.json` | ❌ W0 | ⬜ pending |
| 01-01-02 | 01 | 1 | FOUND-04 | structural | `test -d canvas/src` | ❌ W0 | ⬜ pending |
| 01-02-01 | 02 | 1 | FOUND-01 | unit | `cd canvas && npx vitest run src/types.test.ts` | ❌ W0 | ⬜ pending |
| 01-03-01 | 03 | 1 | FOUND-02 | unit | `cd canvas && npx vitest run src/zip-converter.test.ts` | ❌ W0 | ⬜ pending |
| 01-03-02 | 03 | 1 | FOUND-03 | unit | `cd canvas && npx vitest run src/zip-converter.test.ts` | ❌ W0 | ⬜ pending |
| 01-03-03 | 03 | 1 | TEST-01 | unit | `cd canvas && npx vitest run src/zip-converter.test.ts` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `canvas/package.json` — with vitest, typescript dependencies
- [ ] `canvas/tsconfig.json` — strict mode, resolveJsonModule
- [ ] `canvas/vitest.config.ts` — basic config
- [ ] `canvas/src/` — source directory structure

*If none: "Existing infrastructure covers all phase requirements."*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| AGENT-BOUNDARIES.md exists with canvas/ section | FOUND-04 | Documentation artifact | `cat .claude/AGENT-BOUNDARIES.md` and verify canvas/ path-gate pattern documented |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 5s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
