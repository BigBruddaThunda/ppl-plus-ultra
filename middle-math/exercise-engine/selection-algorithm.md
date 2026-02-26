# Exercise Selection Algorithm

Status: DRAFT

The 6-step pipeline from template role to specific exercise. Deterministic given fixed inputs. No inference required.

---

## The Pipeline

```
Role Definition
     ↓
Step 1: Read the template role
     ↓
Step 2: Read zip code constraints
     ↓
Step 3: Read user constraints
     ↓
Step 4: Query the exercise library (filter → rank → select)
     ↓
Step 5: Check user ledger for prescription data
     ↓
Step 6: Return exercise with zip-code-aware parameters
```

---

## Step 1 — Read the Template Role

A template role defines what kind of movement belongs in a given block position. It specifies:

- `movement_pattern` — e.g., "hip-hinge", "horizontal-press", "vertical-pull"
- `compound` — true/false
- `bilateral` — true/false or "preferred"
- `block_position` — which block this role fills (e.g., 🧈 Bread & Butter, 🧩 Supplemental)
- `set_count_range` — min/max sets (from Order × block role)
- `rep_range` — from Order parameters
- `intensity_ceiling` — from Order ceiling

**Example role (🧈 slot in ⛽🏛🪡🔵):**
```
role: "bread-butter-primary"
movement_pattern: "hip-hinge OR vertical-pull"
compound: true
bilateral: preferred
block_position: "🧈"
rep_range: "4-6"
intensity_ceiling: "85%"
axis_bias: "🏛"
```

---

## Step 2 — Read Zip Code Constraints

Extract constraint parameters from the four dials:

```python
def get_zip_constraints(zip_code):
    order, axis, type_, color = parse_zip(zip_code)
    return {
        "load_ceiling":      ORDER_PARAMS[order]["load_ceiling"],
        "rep_range":         ORDER_PARAMS[order]["rep_range"],
        "rest_range":        ORDER_PARAMS[order]["rest_range"],
        "difficulty_max":    ORDER_PARAMS[order]["difficulty_max"],
        "equipment_tier_max": COLOR_PARAMS[color]["tier_max"],
        "equipment_tier_min": COLOR_PARAMS[color]["tier_min"],
        "gold_unlocked":     COLOR_PARAMS[color]["gold"],
        "axis_bias":         axis,
        "type_muscles":      TYPE_PARAMS[type_]["muscles"],
        "type_patterns":     TYPE_PARAMS[type_]["patterns"],
        "weight_vector":     compute_weight_vector(zip_code),
    }
```

---

## Step 3 — Read User Constraints

```python
def get_user_constraints(user_id):
    return {
        "toggled_off_exercises":  get_exercise_toggles(user_id),
        "toggled_off_tiers":      get_tier_toggles(user_id),
        "toggled_off_patterns":   get_pattern_toggles(user_id),
        "toggled_off_types":      get_type_toggles(user_id),
        "available_equipment":    get_equipment_profile(user_id),
    }
```

---

## Step 4 — Query the Exercise Library (Filter → Rank → Select)

### 4a. Filter

```python
def filter_candidates(role, zip_constraints, user_constraints):
    candidates = query_exercise_library(
        movement_pattern = role["movement_pattern"],
        type_muscles     = zip_constraints["type_muscles"],
        equipment_tier   = range(
                             zip_constraints["equipment_tier_min"],
                             zip_constraints["equipment_tier_max"] + 1
                           ),
        gold_required    = zip_constraints["gold_unlocked"],  # if False, exclude GOLD-gated
    )

    # Apply user hard filters
    candidates = [e for e in candidates
                  if e.exercise_id not in user_constraints["toggled_off_exercises"]
                  and e.equipment_tier not in user_constraints["toggled_off_tiers"]
                  and e.movement_pattern not in user_constraints["toggled_off_patterns"]]

    return candidates
```

### 4b. Rank

```python
def rank_candidates(candidates, zip_constraints, user_id):
    weight_vector = zip_constraints["weight_vector"]
    axis_bias     = zip_constraints["axis_bias"]

    for exercise in candidates:
        # Base score: axis affinity from weight vector
        axis_score = exercise.axis_affinity.get(axis_bias, 0)

        # Order affinity
        order_score = exercise.order_affinity.get(zip_constraints["order"], 0)

        # Recency penalty: exercises logged recently at same address get slight deprioritization
        # (variety heuristic — don't repeat the same exercise every time)
        recency = get_recency_score(user_id, exercise.exercise_id, zip_constraints["zip"])

        exercise.rank_score = axis_score + order_score - recency

    return sorted(candidates, key=lambda e: e.rank_score, reverse=True)
```

### 4c. Select

```python
def select_exercise(ranked_candidates, role):
    # Select top candidate. If role requires bilateral and top is unilateral,
    # check second candidate. Apply role's compound/bilateral preference.
    for candidate in ranked_candidates:
        if satisfies_role_preference(candidate, role):
            return candidate

    # Fallback: return top candidate even if preference mismatch
    return ranked_candidates[0]
```

---

## Step 5 — Check User Ledger for Prescription

```python
def get_prescription(user_id, exercise_id, zip_code):
    profile = get_exercise_profile(user_id, exercise_id)

    if profile is None:
        # No history: return default prescription from Order parameters
        return get_default_prescription(zip_code)

    # Translate profile's known performance to this zip code's parameters
    translation_factor = compute_translation_factor(
        profile["source_zip"],   # the zip code with most logged data
        zip_code                  # the target zip code
    )

    return {
        "prescribed_load":  profile["estimated_1rm"] * zip_code["load_ceiling"] * translation_factor,
        "rep_range":        zip_code["rep_range"],
        "set_range":        derive_set_range(zip_code["order"], role["block_position"]),
        "rest":             zip_code["rest_range"],
    }
```

---

## Step 6 — Return

```python
def resolve_role(role, zip_code, user_id):
    zip_constraints  = get_zip_constraints(zip_code)
    user_constraints = get_user_constraints(user_id)

    candidates = filter_candidates(role, zip_constraints, user_constraints)

    if not candidates:
        # No valid candidates: trigger substitution pipeline
        return run_substitution(role, zip_constraints, user_constraints, user_id)

    ranked     = rank_candidates(candidates, zip_constraints, user_id)
    exercise   = select_exercise(ranked, role)
    prescription = get_prescription(user_id, exercise.exercise_id, zip_code)

    return {
        "exercise":       exercise,
        "prescription":   prescription,
        "role":           role,
        "zip_code":       zip_code,
    }
```

---

## Edge Cases

**No valid candidates after filtering:** Trigger substitution pipeline (see `substitution-rules.md`). Walk the family tree for the nearest valid substitute. If no substitute exists, flag to the user.

**User has no ledger data:** Return default prescription from Order parameters. Begin accumulating ledger data from first log.

**Exercise is GOLD-gated but Color does not unlock GOLD:** The filter in Step 4a excludes GOLD exercises when `gold_unlocked = False`. This is enforced before ranking. The engine never selects a GOLD exercise at a non-GOLD color.

**Fully-specified card (no template):** Skip Steps 1–4. The exercise is named directly. Go to Step 5 for prescription, Step 6 for return.

---

🧮
