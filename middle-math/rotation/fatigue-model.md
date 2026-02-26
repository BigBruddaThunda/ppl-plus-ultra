# Fatigue Model

Status: DRAFT — Concept established, parameters to be refined.

A practical heuristic for session-to-session fatigue inference. Not a sports science model. Inputs are user-logged RPE and volume. Outputs are adjustments to next-session suggestions.

---

## Core Principle

The fatigue model does not prescribe deload weeks or override the rotation engine's zip code. It adjusts the 🚂 Junction suggestions and, optionally, the Color suggestion for tomorrow.

Heavy day today → surface lower-intensity suggestions for tomorrow.
High volume today → surface complementary (non-overlapping) Types.
No RPE logged → fall back to Order-default fatigue index.

---

## The Fatigue Index

A single value from 0.0 to 1.0 representing the estimated recovery demand of the just-completed session.

```
fatigue_index = (rpe_component + volume_component) / 2

rpe_component    = session_rpe / 10
volume_component = actual_sets / order_max_sets (capped at 1.0)
```

| Fatigue Index | Interpretation | Suggestion Adjustment |
|--------------|----------------|----------------------|
| 0.0–0.4 | Low demand | No adjustment |
| 0.4–0.7 | Moderate demand | No adjustment |
| 0.7–0.85 | High demand | Suggest lower-intensity Order for tomorrow |
| 0.85–1.0 | Very high demand | Prioritize 🖼 Restoration or ⚖ Balance suggestion |

---

## Muscle Group Overlap Heuristic

Separate from the fatigue index, the model tracks muscle group overlap between today's session and suggested next sessions.

If today's primary Type was 🪡 Pull (lats, biceps, erectors):
- Next session with 🪡 Pull → flag overlap: "🪡 Pull trained today. Consider 24–48h before returning."
- Next session with 🛒 Push → no overlap flag
- Next session with 🍗 Legs → no overlap flag

```python
TYPE_OVERLAP_PAIRS = {
    🪡: [🪡],          # Pull overlaps with Pull
    🛒: [🛒],          # Push overlaps with Push
    🍗: [🍗],          # Legs overlaps with Legs
    ➕: [➕, 🪡, 🍗],  # Plus (Olympic/core) overlaps with Pull (erectors) and Legs
    ➖: [],             # Ultra (conditioning) — minimal muscle overlap with all
}
```

The overlap flag is informational, not a hard block. The user can train the same Type two days in a row if they choose.

---

## RPE Absence

If the user does not log RPE, the model uses Order-default RPE values:

| Order | Default RPE |
|-------|------------|
| 🐂 Foundation | 5.0 |
| ⛽ Strength | 7.5 |
| 🦋 Hypertrophy | 7.0 |
| 🏟 Performance | 9.0 |
| 🌾 Full Body | 6.5 |
| ⚖ Balance | 6.0 |
| 🖼 Restoration | 3.5 |

Default RPE is a coarse estimate. Users who log RPE get more accurate fatigue inference.

---

## Future Refinement

The fatigue model is intentionally simple in this first version. Refinement paths include:

1. **Session-count trending:** If high fatigue (>0.8) appears for 3+ consecutive sessions, flag for potential deload consideration (informational only — the system never mandates).
2. **Sleep/HRV integration:** If the platform integrates wearable data, HRV and sleep quality would replace the RPE proxy with a more accurate recovery signal.
3. **Individual calibration:** Some users consistently rate RPE lower than their performance data suggests. The model could learn individual RPE bias from historical comparisons.

These are future seeds, not current requirements.

---

🧮
