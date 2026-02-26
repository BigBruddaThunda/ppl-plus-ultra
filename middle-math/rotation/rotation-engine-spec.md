# Rotation Engine Specification

The deterministic date-to-zip-code formula. No AI, no randomness, no user input required beyond Color preference.

Source: Formalization of `seeds/default-rotation-engine.md`.

---

## The Three Gears

### Gear 1 — Order by Day of Week (7-day fixed cycle)

| Weekday | Order |
|---------|-------|
| Monday | 🐂 Foundation |
| Tuesday | ⛽ Strength |
| Wednesday | 🦋 Hypertrophy |
| Thursday | 🏟 Performance |
| Friday | 🌾 Full Body |
| Saturday | ⚖ Balance |
| Sunday | 🖼 Restoration |

```python
ORDERS = [🐂, ⛽, 🦋, 🏟, 🌾, ⚖, 🖼]

def get_order(date):
    # Monday = 0, Sunday = 6
    weekday = date.weekday()
    return ORDERS[weekday]
```

### Gear 2 — Type by Rolling Calendar (5-day cycle from Jan 1)

The Type cycle runs continuously from January 1 of each year. It does not reset weekly. It rolls every calendar day regardless of Order.

| Sequence | Type |
|----------|------|
| 0 | 🛒 Push |
| 1 | 🪡 Pull |
| 2 | 🍗 Legs |
| 3 | ➕ Plus |
| 4 | ➖ Ultra |

```python
TYPES = [🛒, 🪡, 🍗, ➕, ➖]

def get_type(date):
    # Days since January 1 of current year (0-indexed)
    jan1 = date.replace(month=1, day=1)
    days_elapsed = (date - jan1).days
    return TYPES[days_elapsed % 5]
```

### Gear 3 — Axis by Monthly Operator (12 shifts per year)

Each month aligns to one Axis via the monthly Operator. The Operator names the monthly character; the Axis is the mechanical mapping.

| Month | Operator | Axis |
|-------|----------|------|
| January | 📍 pono | 🏛 Basics |
| February | 🧲 capio | 🐬 Partner |
| March | 🧸 fero | 🔨 Functional |
| April | 👀 specio | 🌹 Aesthetic |
| May | 🥨 tendo | 🪐 Challenge |
| June | ✒️ grapho | ⌛ Time |
| July | 🤌 facio | 🏛 Basics |
| August | 🦉 logos | 🐬 Partner |
| September | 🦢 plico | 🌹 Aesthetic |
| October | 🪵 teneo | 🪐 Challenge |
| November | 🐋 duco | ⌛ Time |
| December | 🚀 mitto | 🔨 Functional |

```python
MONTHLY_AXES = [🏛, 🐬, 🔨, 🌹, 🪐, ⌛, 🏛, 🐬, 🌹, 🪐, ⌛, 🔨]

def get_axis(date):
    month_index = date.month - 1  # 0-indexed
    return MONTHLY_AXES[month_index]
```

### Gear 4 — Color by User Choice

The Color dial is not computed by the rotation engine. The user selects from the 8 available Colors each session based on:
- Equipment access (which tiers are available today)
- Desired session format (structured, intense, mindful, circuit)
- Energy and time

The rotation engine returns a 3-dial prefix: `ORDER AXIS TYPE`. The user closes the zip code with their Color.

---

## The Full Date-to-Zip Formula

```python
def get_daily_zip(date, user_color_choice):
    order = get_order(date)
    axis  = get_axis(date)
    type_ = get_type(date)
    color = user_color_choice

    zip_code = f"{order}{axis}{type_}{color}"

    return zip_code
```

---

## The Coprime Property

5 (Types) and 7 (Orders) share no common factors. Their least common multiple = 35.

This means: the same Order × Type pairing doesn't repeat for 35 days.

Example: Tuesday ⛽ (⛽ Strength) + whatever Type the rolling calendar produces = unique combination for 35 days before that exact Order × Type pair repeats.

The Axis shifts monthly (every ~30 days), which is not coprime with 5 or 7, but operates at a different timescale (monthly) that creates sufficient variety before repetition.

**Practical result:** A user following the rotation engine gets genuine variety across the first 35 days of use without any personalization engine. The deterministic math produces variety as a side effect of the coprime relationship.

---

## Annual Periodization Embedded in the Engine

The 12 monthly Axis shifts create an implicit annual periodization:
- Jan/Jul: 🏛 Basics months (technical reset — twice per year)
- Feb/Aug: 🐬 Partner months (collaborative/spottable work)
- Mar/Dec: 🔨 Functional months (athletic transfer)
- Apr/Sep: 🌹 Aesthetic months (isolation and feel)
- May/Oct: 🪐 Challenge months (hardest variations)
- Jun/Nov: ⌛ Time months (timed work, density, EMOM)

Each dimension gets 2 months of emphasis per year. The year breathes with a rhythm the user feels without analyzing.

---

## Example Computations

**Wednesday, March 12, 2026:**
- Order: Wednesday → 🦋 Hypertrophy
- Type: Days from Jan 1 = 70 → 70 % 5 = 0 → 🛒 Push
- Axis: March → 🔨 Functional
- Color: User chooses 🔵 Structured
- Zip: 🦋🔨🛒🔵

**Tuesday, June 3, 2026:**
- Order: Tuesday → ⛽ Strength
- Type: Days from Jan 1 = 153 → 153 % 5 = 3 → ➕ Plus
- Axis: June → ⌛ Time
- Color: User chooses 🔴 Intense
- Zip: ⛽⌛➕🔴

**Sunday, January 11, 2026:**
- Order: Sunday → 🖼 Restoration
- Type: Days from Jan 1 = 10 → 10 % 5 = 0 → 🛒 Push
- Axis: January → 🏛 Basics
- Color: User chooses ⚪ Mindful
- Zip: 🖼🏛🛒⚪

---

🧮
