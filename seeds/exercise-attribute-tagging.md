---
planted: 2026-02-20
status: SEED
phase-relevance: Phase 3+ (after generation, before HTML validation)
blocks: nothing in Phase 2
depends-on: scl-deep/order-parameters.md (attribute schema)
---

# Exercise Attribute Tagging

## One Sentence

Tag each of the ~2,800 exercises in exercise-library.md with the full attribute score set (D, C, A, G, SI, Ss, Sc, RD, P, KC, LAT, flags) to enable automated validation, conflict detection, and future RAG recommendations.

## The Schema (from Order Parameters v2.0)

Each exercise needs:
- **D:** Difficulty (1-5)
- **C:** CNS Demand (L/M/H)
- **A:** Axial Load (1-5)
- **G:** Grip Demand (1-5)
- **SI:** Stability Index (1-10)
- **Ss:** Shoulder Stabilizer (1-5)
- **Sc:** Core Stabilizer (1-5)
- **RD:** Recovery Demand (1-5)
- **P:** Movement Pattern (SQ/HI/HP/HPL/VP/VPL/CA/ISO/MOB/PLY/OLY)
- **KC:** Kinetic Chain (C/O/X)
- **LAT:** Laterality (B/U/X)
- **Flags:** [COMP], [SAFE], [MOD], [RISK], [GOLD], [PLYO], [OLY]

## Why This Matters

Without attribute tags, workout validation is manual and based on Claude's judgment. With tags, validation becomes mechanical — filter, sum, compare against Order thresholds, flag conflicts automatically. This is what turns workout generation from artisanal to systematic.

The 7 Conflict Detection Rules in scl-deep/order-parameters.md (axial load stacking, grip pre-fatigue, CNS accumulation, shoulder stabilizer overload, pattern redundancy, recovery demand stacking, joint-specific overload) all reference these attributes. They can't run automatically until the exercises carry scores.

## Scale

~2,800 exercises × 11 attributes + flags = significant tagging effort. Could be batched by library section (A–Q). Could be a Claude Code skill that processes one section at a time with spot-check review.

## Open Questions

- Tag inline in exercise-library.md, or create a separate structured file (JSON/YAML)?
- Batch by section or by Type routing?
- Human review needed per exercise, or can Claude tag with spot-check review?
- Should tagging begin before all 1,680 cards are generated, or after?
