# Exercise Ledger Specification

The raw log. Every exercise in every logged workout becomes a row.

---

## Table: user_exercise_ledger

| Column | Type | Description |
|--------|------|-------------|
| `log_id` | UUID PK | Stable identifier for this log entry |
| `user_id` | UUID FK | References user table |
| `session_id` | UUID FK | Groups all entries from one workout session |
| `logged_at` | TIMESTAMP | When the entry was recorded |
| `zip_code` | TEXT | The 4-emoji address: e.g., "⛽🏛🪡🔵" |
| `exercise_id` | TEXT FK | Stable identifier: "barbell-deadlift" |
| `block` | TEXT | Which block: "🧈", "🧩", "▶️", etc. |
| `set_number` | INTEGER | 1, 2, 3... |
| `prescribed_load_pct` | NUMERIC | Prescribed as % of 1RM: 0.80 |
| `prescribed_load_abs` | NUMERIC | Prescribed absolute load in kg (or lbs if user pref) |
| `prescribed_reps` | INTEGER | Target reps |
| `actual_load_abs` | NUMERIC | What the user actually lifted |
| `actual_reps` | INTEGER | Reps completed |
| `rpe` | NUMERIC | Rate of Perceived Exertion: 1–10 (optional, user input) |
| `completed` | BOOLEAN | Did the user complete this set? |
| `notes` | TEXT | Optional free text (e.g., "knees felt off") |

---

## Session Grouping

Sessions are grouped by `session_id`. One `session_id` corresponds to one workout: one zip code, one day, one block sequence from ♨️ Warm-Up to 🧮 SAVE.

Multiple exercises within one block share the same `session_id` and `zip_code`. Multiple sets of the same exercise share the same `session_id`, `zip_code`, and `exercise_id`.

---

## The Zip Code Tag

Every ledger entry is tagged with its full zip code. This enables:

- Querying "what has this user done at this zip code?" → direct history
- Querying "what has this user done at any ⛽ address?" → Order-level history
- Querying "what has this user done with 🪡 Pull exercises?" → Type-level history
- Cross-context translation: project performance from one zip to another

---

## Load Unit Convention

Default unit: kilograms. User preference can set pounds. All internal computation uses kilograms. Display converts to user preference at render time.

For bodyweight exercises: `actual_load_abs` = bodyweight in kg. For assisted exercises: `actual_load_abs` = bodyweight minus assistance in kg.

---

## RPE Convention

RPE is optional. Users who log RPE unlock the fatigue model (see `rotation/fatigue-model.md`). Users who do not log RPE receive default prescriptions from Order parameters only.

RPE scale: 1 (minimal effort) to 10 (maximal, could not do one more rep).

---

## Minimum Viable Log

The minimum required for the profile computation:
- `exercise_id`
- `actual_load_abs`
- `actual_reps`
- `zip_code`
- `logged_at`

Everything else is optional but improves profile accuracy.

---

🧮
