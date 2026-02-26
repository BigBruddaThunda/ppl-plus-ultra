# Toggle System Specification

Four toggle types. Each sets a -8 weight on the toggled entity, excluding it from selection without deleting it.

---

## Toggle Types

### Type 1 — Exercise Toggle

Toggle a specific exercise off entirely.

```
user_exercise_toggles:
  user_id:      UUID
  toggle_type:  "exercise"
  entity_id:    "barbell-deadlift"
  active:       true
  reason:       "lower back injury" (optional)
  created_at:   TIMESTAMP
```

**Effect:** The exercise is excluded from the selection pipeline's filter step. Transfer ratios for the exercise are still available — the engine can use the user's history at this exercise to inform prescriptions at related exercises in the same family.

---

### Type 2 — Equipment Tier Toggle

Toggle all exercises at or above a specific equipment tier.

```
toggle_type:  "equipment_tier"
entity_id:    "3"              # Tier 3 = barbell, rack, bench
modifier:     "gte"            # "gte" = this tier and above, "eq" = this tier only
```

**Effect:** All exercises requiring equipment tier ≥ 3 are excluded. The system automatically routes to exercises within available tiers. Common use: hotel gym, home gym, outdoor training.

**Example:** User toggles tier 3+. The system never selects barbell exercises. Dumbbell and bodyweight alternatives surface automatically.

---

### Type 3 — Movement Pattern Toggle

Toggle all exercises in a specific movement pattern.

```
toggle_type:  "movement_pattern"
entity_id:    "overhead-press"
```

**Effect:** All exercises with `movement_pattern = "overhead-press"` are excluded. Used for temporary injury management (e.g., shoulder impingement blocks all overhead patterns).

**Scope:** Covers all exercises in the pattern across all equipment tiers and all families. More surgical than equipment toggle; more broad than exercise toggle.

---

### Type 4 — Type Toggle

Toggle all exercises in a specific SCL Type.

```
toggle_type:  "type"
entity_id:    "🍗"             # Legs
```

**Effect:** All 🍗 Legs exercises are excluded from selection. Used when a lower-body injury makes leg training completely off-limits. The engine will flag if the zip code's Type matches the toggled Type — the entire session address may be invalid.

**Note:** A Type toggle on a zip code's own Type creates a conflict. The engine surfaces this to the user: "⚠️ Your 🍗 Legs toggle is active. This zip code (⛽🏛🍗🔵) cannot be filled. Consider a different zip code or lifting the toggle."

---

## Toggle Interaction with the Weight System

Toggles are implemented as a forced -8 override applied before the weight vector computation.

```python
def apply_toggles(weight_vector, user_toggles, zip_code):
    for toggle in user_toggles:
        if toggle.toggle_type == "exercise":
            # Set weight to -8 for this exercise's axis/type affinities
            weight_vector[toggle.entity_id] = -8

        elif toggle.toggle_type == "equipment_tier":
            tier = int(toggle.entity_id)
            for exercise in get_exercises_by_tier(tier, modifier=toggle.modifier):
                weight_vector[exercise.exercise_id] = -8

        elif toggle.toggle_type == "movement_pattern":
            for exercise in get_exercises_by_pattern(toggle.entity_id):
                weight_vector[exercise.exercise_id] = -8

        elif toggle.toggle_type == "type":
            for exercise in get_exercises_by_type(toggle.entity_id):
                weight_vector[exercise.exercise_id] = -8

    return weight_vector
```

Toggles are non-destructive. The exercises remain in the library. The toggle sets their effective weight to -8 in this user's context. Lifting the toggle returns their weight to the system-computed value.

---

## Toggle Duration

Toggles can be:
- **Indefinite** (default): active until manually lifted
- **Date-limited**: set an `expires_at` timestamp
- **Session-limited**: active for N sessions only (e.g., "skip deadlifts for 2 sessions")

The toggle table supports all three with an optional `expires_at` column and an optional `session_count` column.

---

🧮
