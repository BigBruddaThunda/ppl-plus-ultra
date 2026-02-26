# Progressive Disclosure

Status: SEED-LEVEL — Specifies how the floor stack responds to zip code weights.

The floor stack (from `seeds/elevator-architecture.md`) is the vertical navigation model:
- 🔨 Functional — Ground floor
- 🏛 Basics — Piano nobile (noble floor)
- ⌛ Time — 2nd floor
- 🐬 Partner — 3rd floor
- 🌹 Aesthetic — 4th floor
- 🪐 Challenge — 5th floor (penthouse)

Each floor is always present. The weights modulate what the user sees first — which floor is foregrounded, which is backgrounded, and which is partially visible as an invitation to explore.

---

## The Core Principle

Progressive disclosure is not hiding content. It is emphasis. Everything is always accessible. The weights determine which floor the user lands on when they open the building, and how prominently each floor's content is presented.

A zip code with 🏛 Basics as its Axis has the piano nobile foregrounded. The user sees the most classic, fundamental content first. The 🪐 Challenge penthouse is still there — it requires a floor up.

A zip code with 🪐 Challenge as its Axis foregrounds the penthouse. The hardest variations are the default view. The fundamentals are still accessible but require a floor down.

---

## Weight-to-Emphasis Mapping

**Input:** The Axis weight vector component for each floor emoji.

**Output:** Emphasis level for each floor's content presentation.

```python
FLOOR_MAP = {
    🔨: "ground",
    🏛: "noble",
    ⌛: "second",
    🐬: "third",
    🌹: "fourth",
    🪐: "penthouse"
}

def compute_floor_emphasis(weight_vector):
    emphasis = {}
    for axis_emoji, floor_name in FLOOR_MAP.items():
        weight = weight_vector.get(axis_emoji, 0)

        if weight >= 6:
            emphasis[floor_name] = "primary"      # This floor is open on arrival
        elif weight >= 3:
            emphasis[floor_name] = "visible"       # Partially visible, easy to reach
        elif weight >= 0:
            emphasis[floor_name] = "accessible"    # Present, requires navigation
        elif weight >= -4:
            emphasis[floor_name] = "backgrounded"  # Available but not promoted
        else:
            emphasis[floor_name] = "suppressed"    # Present but requires intent

    return emphasis
```

**Example: ⛽🏛🪡🔵**
- 🏛 Basics (+8 primary) → `"primary"` — Piano nobile is the landing floor
- 🔨 Functional (+3) → `"visible"` — Ground floor accessible
- 🪐 Challenge (+4) → `"visible"` — Penthouse partially visible
- 🌹 Aesthetic (-3) → `"backgrounded"` — 4th floor not promoted
- ⌛ Time (-2) → `"backgrounded"` — 2nd floor not promoted
- 🐬 Partner (-1) → `"accessible"` — 3rd floor reachable

---

## Dual-Layer Axis Function

Each Axis serves two simultaneous functions (per `seeds/axis-as-app-floors.md`):

**Layer 1 — In-workout exercise character:** The Axis bias that shapes exercise selection within the workout.

**Layer 2 — App-level content floor:** The floor of the building that is foregrounded for discovery and navigation.

The progressive disclosure spec connects these two layers. When 🏛 Basics is the workout's Axis, it is simultaneously:
1. The exercise selection bias (barbell-first, bilateral, compound)
2. The floor that is foregrounded in the app experience for this session

The user who logs a 🏛 session is placed on the piano nobile. Their next exploration naturally starts there.

---

## Temporal Weight Effect on Disclosure

The monthly Axis operator (from the rotation engine) adds a +1 temporal nudge to the active month's Axis. This nudge slightly foregrounds that floor's content even when the day's zip code has a different primary Axis.

In March (🔨 Functional month), even a 🏛-primary workout has the 🔨 ground floor at slightly higher visibility than usual. The building knows what month it is.

---

## Design System Interface

The progressive disclosure spec outputs an emphasis configuration:

```json
{
  "daily_zip": "⛽🏛🪡🔵",
  "floor_emphasis": {
    "noble":      "primary",
    "ground":     "visible",
    "penthouse":  "visible",
    "second":     "accessible",
    "third":      "accessible",
    "fourth":     "backgrounded"
  },
  "landing_floor": "noble",
  "temporal_nudge": "ground"
}
```

The design system uses this configuration to set visual prominence: font size, contrast, scroll position on load, navigation indicator strength. The math specifies emphasis. The design system specifies the visual grammar.

---

🧮
