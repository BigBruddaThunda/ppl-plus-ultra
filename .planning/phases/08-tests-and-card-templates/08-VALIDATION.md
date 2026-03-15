---
phase: 08
slug: tests-and-card-templates
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-03-15
---

# Phase 08 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | Vitest ^3.2.4 (installed, 6,949 tests passing) |
| **Config file** | canvas/vite.config.ts |
| **Quick run command** | `cd canvas && npm test` |
| **Full suite command** | `cd canvas && npm test` |
| **Estimated runtime** | ~4 seconds |

---

## Sampling Rate

- **After every task commit:** Run `cd canvas && npm test`
- **After every plan wave:** Run `cd canvas && npm test`
- **Before `/gsd:verify-work`:** Full suite must be green
- **Max feedback latency:** 4 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|-----------|-------------------|-------------|--------|
| 08-01-01 | 01 | 1 | TEST-02 | unit | `cd canvas && npm test` | W0 | pending |
| 08-01-01 | 01 | 1 | TEST-03 | unit | `cd canvas && npm test` | W0 | pending |
| 08-01-01 | 01 | 1 | TEST-05 | integration | `cd canvas && npm test` | W0 | pending |
| 08-02-01 | 02 | 2 | CARD-01 | smoke | `cd canvas && npm test` | W0 | pending |
| 08-02-01 | 02 | 2 | CARD-02 | lint | Visual review of output HTML | manual | pending |
| 08-02-01 | 02 | 2 | CARD-03 | visual | Open card-preview.html in browser | manual | pending |

*Status: pending · green · red · flaky*

---

## Wave 0 Requirements

- [ ] `canvas/tests/weight-vectors.test.ts` — covers TEST-02
- [ ] `canvas/tests/keyword-routing.test.ts` — covers TEST-03
- [ ] `canvas/tests/pipeline-integration.test.ts` — covers TEST-05
- [ ] gray-matter and marked install: `cd canvas && npm install gray-matter marked`

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| No hardcoded OKLCH/hex in rendered HTML | CARD-02 | Requires inspecting generated HTML for CSS var usage | Review WorkoutCard output, confirm all colors are var() references |
| Intaglio patterns visible | CARD-03 | Visual assessment | Open card-preview.html, verify hatching, guilloche, vignette present |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 4s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
