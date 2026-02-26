# Transfer Ratios

Status: DRAFT

A transfer ratio expresses how a user's known performance at one exercise predicts their likely performance at another exercise in the same movement family.

Ratio of 1.00 means perfect transfer. Ratio of 0.80 means: if you can deadlift 100kg, you can probably Romanian deadlift ~80kg.

---

## Ratio Ranges by Relationship Type

| Relationship | Ratio Range | Notes |
|-------------|-------------|-------|
| Variant (same pattern, slight modification) | 0.88–0.97 | E.g., high-bar vs. low-bar squat |
| Equipment swap (same pattern, different implement) | 0.75–0.95 | E.g., barbell → dumbbell (wider range due to stability demand) |
| Unilateral from bilateral | 0.55–0.75 | Per-side load drops significantly (stability cost) |
| Regression (easier ROM or load path) | 1.00–1.20 | You perform better on regressions |
| Progression (harder ROM, pause, deficit, bands) | 0.75–0.90 | You perform worse on progressions |
| Isolation from compound (same muscle group) | 0.40–0.65 | Compound strength does not directly transfer to isolation |
| Different equipment, same isolation pattern | 0.80–0.92 | E.g., cable curl ↔ dumbbell curl — closer transfer |

---

## Direction Matters

Transfer ratios are asymmetric.

- From barbell deadlift to dumbbell deadlift: multiply by 0.75 (perform worse)
- From dumbbell deadlift to barbell deadlift: divide by 0.75 (perform better)

When projecting from Source → Target:
```
Target_Estimated_Load = Source_Known_Load × Transfer_Ratio(Source → Target)
```

When the direction is reversed (Target → Source):
```
Source_Estimated_Load = Target_Known_Load / Transfer_Ratio(Source → Target)
```

---

## Worked Examples

**Example 1:** User has logged Barbell Bench Press at 100kg. They arrive at a zip code calling for Dumbbell Bench Press.
- Transfer ratio (bench → dumbbell bench): 0.80
- Estimated dumbbell load: 100 × 0.80 = 80kg → 40kg per dumbbell
- Return as starting prescription: "Try 38–42kg dumbbells."

**Example 2:** User has logged Dumbbell Row at 32kg (per side). They arrive at a zip code calling for Barbell Row.
- Transfer ratio (dumbbell row → barbell row): 0.85 (bilateral from unilateral, slight advantage)
- Estimated barbell load: 32 × 2 × 0.85 = ~54kg
- Return as starting prescription: "Try 50–55kg."

**Example 3:** User has logged Barbell Squat at 120kg. Zip code calls for Bulgarian Split Squat.
- Transfer ratio (squat → Bulgarian split squat, unilateral): 0.70
- Per-side load: 120 × 0.70 = 84kg → use as total (DBs in each hand = ~38–40kg per hand)
- Note: first session at new exercise — start conservative (0.90 × estimate).

---

## First-Session Conservatism

When a user has no ledger data for an exercise but transfer data exists, apply a **first-session discount of 0.85–0.90** to the estimated prescription.

Rationale: The movement is new even if it is related. Unfamiliarity costs ~10–15% of projected performance.

After the first logged session, retire the transfer estimate and use ledger data directly.

---

## Limitations

Transfer ratios are heuristics, not guarantees. Individual anatomy, training history at specific exercises, and fatigue state all affect actual transfer. The ratio provides a reasonable starting prescription — the user corrects from there. After 2–3 sessions at the new exercise, ledger data replaces the transfer estimate entirely.

---

🧮
