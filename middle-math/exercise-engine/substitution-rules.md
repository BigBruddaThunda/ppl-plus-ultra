# Substitution Rules

When a selected exercise is unavailable (toggled off, equipment absent, or no valid candidates after filtering), the engine runs the substitution pipeline.

---

## Substitution Pipeline

### Step 1 — Walk the Family Tree

Find the toggled/unavailable exercise in its movement family. Walk up to the parent, then search sibling branches for a valid substitute.

Priority order within the family:
1. Same tier, same bilateral/unilateral character
2. Same tier, different bilateral/unilateral character (note the shift)
3. Adjacent tier up (if available)
4. Adjacent tier down (if available)

```python
def walk_family_tree(exercise, zip_constraints, user_constraints):
    family = get_family(exercise.family_id)
    siblings = get_siblings(exercise, family)
    valid = [s for s in siblings
             if s.equipment_tier in zip_constraints["tier_range"]
             and s.exercise_id not in user_constraints["toggled_off"]
             and s.movement_pattern == exercise.movement_pattern]
    return valid
```

### Step 2 — Prefer Same Axis Affinity

Among valid family members, prefer the one with the highest axis affinity score for the zip code's Axis.

### Step 3 — Check Tier Compliance

The substitute must be within the Color's equipment tier range. Never go above the Color's tier ceiling. Going below is acceptable (using lower-tier equipment than maximum allowed).

### Step 4 — Fallback: Different Movement Family

If no valid substitute exists within the family, query the exercise library for the nearest valid exercise at the same Type (muscle group) with a different movement pattern.

```python
def find_cross_family_substitute(role, zip_constraints, user_constraints):
    # Query same Type, same block position, different movement pattern
    candidates = filter_candidates(
        role=modify_role(role, movement_pattern="any"),
        zip_constraints=zip_constraints,
        user_constraints=user_constraints
    )
    return rank_candidates(candidates, zip_constraints, user_id)[0]
```

### Step 5 — Flag If No Substitute Found

If no valid substitute exists anywhere in the Type for the given constraints, flag to the user:

```
⚠️ No valid exercise found for [role] at [zip_code] with current settings.
   Suggested action: Review equipment toggles or Color selection.
```

---

## Cascade Notes

**Equipment absence vs. toggle:** Equipment absence (user has no barbell) is treated as a hard -8 suppression on all barbell exercises. Toggle-off is the same. Both are handled identically in the filter step — the distinction is only for the user-facing explanation.

**GOLD gate:** Never substitute a GOLD exercise at a non-GOLD Color. The substitution pipeline respects the GOLD gate as a hard constraint.

**Transfer ratios on substitutes:** When a substitute is returned, attach a transfer ratio note to the prescription: "Estimated load based on [original exercise] history × [ratio]." After the user logs the substitute, that data enters the ledger for the substitute's own profile.

---

🧮
