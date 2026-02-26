# Junction Algorithm

The 🚂 Junction block at the end of every workout suggests 1–3 follow-up zip codes. In the current card generation workflow, these are hand-written by the card author. The junction algorithm computes them procedurally.

---

## Inputs

```python
junction_inputs = {
    "completed_zip":    "⛽🏛🪡🔵",         # The zip code just completed
    "completed_at":     datetime,              # Timestamp of session end
    "rpe":              8.2,                   # Session RPE (optional, user-logged)
    "volume_sets":      18,                    # Total sets completed
    "next_day_zip":     "🦋🔨🛒🔵",          # What the rotation engine produces for tomorrow
    "user_id":          uuid,                  # For ledger lookup
}
```

---

## Computation Steps

### Step 1 — Assess Session Load (Fatigue Signal)

```python
def assess_session_load(rpe, volume_sets, order):
    # Fatigue index: 0.0 (minimal) to 1.0 (maximum)
    rpe_factor    = (rpe / 10) if rpe else ORDER_DEFAULT_RPE[order] / 10
    volume_factor = min(volume_sets / ORDER_MAX_SETS[order], 1.0)
    return (rpe_factor + volume_factor) / 2
```

| Order | Default RPE | Max Sets |
|-------|------------|---------|
| 🐂 Foundation | 5.0 | 20 |
| ⛽ Strength | 7.5 | 15 |
| 🦋 Hypertrophy | 7.0 | 25 |
| 🏟 Performance | 9.0 | 8 |
| 🌾 Full Body | 6.5 | 18 |
| ⚖ Balance | 6.0 | 20 |
| 🖼 Restoration | 3.5 | 12 |

### Step 2 — Identify Candidate Next Zip Codes

Three candidate pools, one for each Junction suggestion slot:

**Slot A — Rotation-Aligned:** The rotation engine's next-day zip. Already computed.

**Slot B — Complementary Type:** The Type that most complements what was just trained.

```python
COMPLEMENTARY_TYPE = {
    🛒: 🪡,   # Push → Pull
    🪡: 🛒,   # Pull → Push
    🍗: ➕,   # Legs → Plus (core)
    ➕: ➖,   # Plus → Ultra (conditioning)
    ➖: 🍗,   # Ultra → Legs (lower body strength after conditioning)
}
next_type = COMPLEMENTARY_TYPE[parse_zip(completed_zip)[2]]
```

**Slot C — Overdue from Ledger:** The zip code with the oldest last-visited date in the user's history. Surfaces forgotten addresses.

```python
def get_overdue_zip(user_id, current_zip):
    user_history = get_user_zip_history(user_id)
    if not user_history:
        return None
    oldest = min(user_history, key=lambda z: z.last_visited)
    return oldest.zip_code if oldest.zip_code != current_zip else None
```

### Step 3 — Apply Fatigue Filter

If `fatigue_index > 0.7`, adjust all suggestions toward lower intensity:

```python
def apply_fatigue_filter(suggestions, fatigue_index):
    if fatigue_index <= 0.7:
        return suggestions  # No adjustment

    adjusted = []
    for zip_code in suggestions:
        order = parse_zip(zip_code)[0]
        if ORDER_INTENSITY_RANK[order] > 3:  # ⛽, 🏟 = intensity rank 4, 5
            # Suggest the same Axis + Type with a lower-intensity Order
            zip_code = replace_order(zip_code, 🐂)  # or 🦋 depending on context
        adjusted.append(zip_code)
    return adjusted
```

| Order | Intensity Rank |
|-------|--------------|
| 🖼 Restoration | 1 |
| 🐂 Foundation | 2 |
| ⚖ Balance | 3 |
| 🌾 Full Body | 3 |
| 🦋 Hypertrophy | 4 |
| ⛽ Strength | 4 |
| 🏟 Performance | 5 |

### Step 4 — Generate Rationale

Each suggestion gets a one-line rationale derived from the computation:

```python
def generate_rationale(suggestion_zip, slot_type, completed_zip, fatigue_index):
    if slot_type == "rotation":
        return f"Rotation engine: {get_weekday(tomorrow)} + {get_month()}"

    if slot_type == "complementary":
        source_type = parse_zip(completed_zip)[2]
        target_type = parse_zip(suggestion_zip)[2]
        return f"{source_type} done → {target_type} next balances the session pair"

    if slot_type == "overdue":
        days = get_days_since_visited(user_id, suggestion_zip)
        return f"Last visited {days} days ago — due for a return"
```

---

## Output Format

```python
junction_output = [
    {
        "zip":       "🦋🔨🛒🔵",
        "slot":      "rotation",
        "rationale": "Rotation engine: Thursday + March"
    },
    {
        "zip":       "⛽🏛🛒🔵",
        "slot":      "complementary",
        "rationale": "🪡 Pull done → 🛒 Push next balances the session pair"
    },
    {
        "zip":       "🌾🌹🍗⚪",
        "slot":      "overdue",
        "rationale": "Last visited 18 days ago — due for a return"
    }
]
```

In the card's 🚂 JUNCTION block, this renders as:
```
Next → 🦋🔨🛒🔵 — Rotation engine: Thursday + March
Next → ⛽🏛🛒🔵 — 🪡 Pull done → 🛒 Push next balances the pair
Next → 🌾🌹🍗⚪ — Last visited 18 days ago — due for a return
```

---

## Static Override (Current Card Format)

In the current Phase 2 card generation workflow, Junction suggestions are written by the card author based on judgment about logical next steps. The algorithm above describes the eventual procedural computation.

The static hand-written format:
```
Next → ⛽🔨🛒🔵 — Push day to match this Pull; keep the Functional bias
Next → ⛽🏛🪡🟣 — Same zip, Technical color: precision work on what you just pushed hard
```

This format is valid both as hand-written content and as machine-generated output from the algorithm above. The format is fixed. The generation method evolves.

---

🧮
