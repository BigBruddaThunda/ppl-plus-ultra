# Cross-Context Translation

How a user's logged performance at zip code A informs a prescription at zip code B.

The weight system provides the bridge. The difference between two zip codes' weight vectors contains the mathematical signal for how difficult one is relative to the other.

---

## The Core Problem

A user logs Barbell Deadlift at ⛽🏛🪡🔵 (Strength, Basics, Pull, Structured): 120kg × 5 reps. They arrive at 🦋🔨🪡🔴 (Hypertrophy, Functional, Pull, Intense). What should they attempt?

The Order changed (⛽ → 🦋): load drops from 75–85% to 65–75%.
The Axis changed (🏛 → 🔨): bilateral preference relaxes, unilateral rises.
The Color changed (🔵 → 🔴): rep range rises, rest shortens.

These changes are encoded in the weight vectors for both zip codes. The differential produces the translation factor.

---

## Translation Factor Computation

```python
def compute_translation_factor(source_zip, target_zip):
    source_weights = compute_weight_vector(source_zip)
    target_weights = compute_weight_vector(target_zip)

    # Order weight ratio: primary driver of load change
    source_order = parse_zip(source_zip)[0]
    target_order = parse_zip(target_zip)[0]

    source_load_ceiling = ORDER_PARAMS[source_order]["load_ceiling_midpoint"]  # e.g., 0.80 for ⛽
    target_load_ceiling = ORDER_PARAMS[target_order]["load_ceiling_midpoint"]  # e.g., 0.70 for 🦋

    order_ratio = target_load_ceiling / source_load_ceiling  # 0.70 / 0.80 = 0.875

    # Color modifier: rep range change affects effective load
    source_rep_mid = ORDER_PARAMS[source_order]["rep_range_midpoint"]  # 5 for ⛽
    target_rep_mid = ORDER_PARAMS[target_order]["rep_range_midpoint"]  # 10 for 🦋

    rep_adjustment = compute_rep_adjustment(source_rep_mid, target_rep_mid)
    # Higher rep target → lower effective load (Brzycki curve adjustment)

    translation_factor = order_ratio * rep_adjustment

    return translation_factor
```

---

## Load Ceiling Midpoints by Order

| Order | Load Range | Midpoint |
|-------|-----------|---------|
| 🐂 Foundation | ≤65% | 0.62 |
| ⛽ Strength | 75–85% | 0.80 |
| 🦋 Hypertrophy | 65–75% | 0.70 |
| 🏟 Performance | 85–100%+ | 0.92 |
| 🌾 Full Body | ~70% | 0.70 |
| ⚖ Balance | ~70% | 0.70 |
| 🖼 Restoration | ≤55% | 0.52 |

---

## Rep Adjustment Table

Adjusting load based on rep range change using Epley formula approximation:

```
Load at rep range N ≈ 1RM / (1 + N / 30)
```

When rep range changes, the effective load for a given 1RM changes. The ratio of effective loads at two rep ranges = the rep adjustment factor.

| Source Reps | Target Reps | Adjustment Factor |
|------------|------------|------------------|
| 5 (⛽) | 10 (🦋) | 0.857 |
| 5 (⛽) | 3 (🏟) | 1.053 |
| 10 (🦋) | 5 (⛽) | 1.167 |
| 8 (🐂) | 10 (🦋) | 0.933 |
| 10 (🦋) | 12 (⚖) | 0.909 |

---

## Worked Example

**User:** Has logged Barbell Deadlift at ⛽🏛🪡🔵: best set = 120kg × 5.

**Source zip:** ⛽🏛🪡🔵
**Target zip:** 🦋🔨🪡🔴

**Step 1 — Order ratio:**
Source midpoint: 0.80 (⛽ Strength)
Target midpoint: 0.70 (🦋 Hypertrophy)
Order ratio: 0.70 / 0.80 = 0.875

**Step 2 — Rep adjustment:**
Source reps: 5 (⛽ midpoint)
Target reps: 10 (🦋 midpoint)
Adjustment: 0.857

**Step 3 — Translation factor:**
0.875 × 0.857 = 0.750

**Step 4 — Apply to source performance:**
120kg × 5 → estimated 1RM via Epley: 120 × (1 + 5/30) = 140kg
Target prescription: 140kg × 0.70 (🦋 midpoint) = 98kg
With rep adjustment already embedded in the order ratio: 120 × 0.750 = 90kg

**Return:** "Try 88–92kg × 10 reps. This is your first session at this address with this exercise."

**Note:** 90kg × 10 implies an estimated 1RM of 120kg, which matches the source exactly. The math is self-consistent.

---

## Axis Character Adjustment

When the Axis changes (e.g., 🏛 → 🔨), the specific exercise may also change (bilateral → unilateral preferred). In that case:

1. Compute the translation factor for the movement pattern (same as above)
2. Apply the family tree transfer ratio for the exercise change (if exercise changes)
3. Multiply: `prescription = source_load × translation_factor × transfer_ratio`

**Example:** Source = Barbell Deadlift (🏛 bias) at 120kg × 5. Target zip = 🔨 Functional → engine selects Single-Leg RDL.
- Translation factor (⛽ → 🦋): 0.750
- Transfer ratio (deadlift → single-leg RDL): 0.65
- Per-side prescription: 120 × 0.750 × 0.65 = ~59kg

The result is lower than expected — single-leg RDL is much harder per-side than bilateral deadlift. This is correct.

---

## Confidence and Decay

Translation confidence decays when:
- More than one dial changes simultaneously (compound translation, less precise)
- The exercise changes within the translation (family tree transfer adds uncertainty)
- The source zip has fewer than 3 logged sessions (thin data)

When confidence is low, the system widens the prescription range and labels it explicitly: "Estimated starting range — thin data. Log this session and the estimate will sharpen."

After 2–3 sessions at the target zip, ledger data replaces translation entirely.

---

🧮
