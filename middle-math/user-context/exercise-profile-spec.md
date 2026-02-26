# Exercise Profile Specification

The derived profile computed from the raw ledger. The engine uses the profile for prescriptions — it does not query the raw ledger at render time.

---

## Table: user_exercise_profile

One row per user per exercise. Updated after each logged session containing that exercise.

| Column | Type | Description |
|--------|------|-------------|
| `profile_id` | UUID PK | |
| `user_id` | UUID FK | |
| `exercise_id` | TEXT FK | |
| `estimated_1rm` | NUMERIC | Epley-derived from best recent performance |
| `best_set` | JSONB | `{"load": 120.0, "reps": 5, "date": "2026-02-20"}` |
| `trend` | TEXT | "progressing" \| "plateau" \| "declining" |
| `session_count` | INTEGER | Total sessions logged at this exercise |
| `primary_zip` | TEXT | The zip code with most sessions logged |
| `order_history` | JSONB | `{"⛽": 8, "🦋": 3, "🐂": 1}` — sessions per Order |
| `color_history` | JSONB | `{"🔵": 6, "🟣": 3, "🔴": 2}` — sessions per Color |
| `last_logged_at` | TIMESTAMP | Date of most recent session |
| `last_logged_zip` | TEXT | Zip code of most recent session |
| `updated_at` | TIMESTAMP | When this profile row was last recomputed |

---

## Estimated 1RM Computation

Using the Epley formula as the base:

```
1RM = load × (1 + reps / 30)
```

Applied to the best set from the most recent 90-day window. If fewer than 90 days of data, use all available data.

```python
def compute_estimated_1rm(ledger_entries, exercise_id, window_days=90):
    recent = [e for e in ledger_entries
              if e.exercise_id == exercise_id
              and days_ago(e.logged_at) <= window_days
              and e.completed == True]

    if not recent:
        return None  # No data

    best = max(recent,
               key=lambda e: e.actual_load_abs * (1 + e.actual_reps / 30))

    return best.actual_load_abs * (1 + best.actual_reps / 30)
```

---

## Trend Computation

Trend is derived from the slope of estimated 1RM over the last 6 sessions at this exercise.

```python
def compute_trend(ledger_entries, exercise_id, recent_sessions=6):
    session_1rms = [compute_estimated_1rm([e], exercise_id)
                    for e in get_recent_sessions(ledger_entries, exercise_id, recent_sessions)]

    if len(session_1rms) < 3:
        return "insufficient-data"

    slope = linear_regression_slope(session_1rms)

    if slope > 0.5:    return "progressing"
    if slope < -0.5:   return "declining"
    return "plateau"
```

---

## Primary Zip

The zip code with the most logged sessions for this exercise. Used as the `source_zip` for cross-context translation (see `cross-context-translation.md`).

```python
def compute_primary_zip(ledger_entries, exercise_id):
    from collections import Counter
    zip_counts = Counter(e.zip_code for e in ledger_entries
                         if e.exercise_id == exercise_id)
    return zip_counts.most_common(1)[0][0] if zip_counts else None
```

---

## Profile Update Trigger

The profile is recomputed after each logged workout session containing the exercise. It is not a live query — it is a materialized summary that is refreshed on write.

Update trigger: `INSERT INTO user_exercise_ledger` → recompute profile rows for all `exercise_id` values in the new entries.

---

🧮
