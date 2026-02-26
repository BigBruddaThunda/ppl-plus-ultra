# Template Specification

How master cards define exercise roles instead of naming specific exercises.

---

## The Role Format

A template role replaces a named exercise in a card with a role declaration. The engine resolves the role to a specific exercise at render time.

```yaml
role:
  id: "bread-butter-primary"
  movement_pattern: "horizontal-pull"       # or pipe-separated: "hip-hinge|vertical-pull"
  compound: true
  bilateral: preferred                       # "required" | "preferred" | "either"
  block: "🧈"
  set_range: [4, 5]                         # derived from Order × block position
  rep_range: [4, 6]                         # from Order parameters
  intensity_ceiling: "85%"                  # from Order ceiling
  axis_bias: "🏛"                           # from zip code Axis
  notes: "Primary movement. Heaviest set of the session."
```

---

## Role ID Conventions

Role IDs are stable identifiers for block positions in a given zip code context:

| Role ID | Block | Position |
|---------|-------|----------|
| `warm-up-primary` | ♨️ | Primary movement in warm-up |
| `primer-activation` | ▶️ | CNS activation in primer |
| `bread-butter-primary` | 🧈 | The main lift |
| `bread-butter-secondary` | 🧈 | Second primary movement (if any) |
| `supplemental-1` | 🧩 | First supplemental movement |
| `supplemental-2` | 🧩 | Second supplemental movement |
| `sculpt-primary` | 🗿 | Hypertrophy shaping movement |
| `vanity-pump` | 🪞 | Pump/mirror work |
| `reformance-primary` | 🏗 | Corrective primary |
| `imprint-close` | 🧬 | Closing low-load neural imprint |

---

## Movement Pattern Vocabulary

Standard movement pattern IDs used across the system:

| Pattern ID | Description | Primary Type |
|------------|-------------|-------------|
| `hip-hinge` | Deadlift, RDL, good morning | 🪡 Pull |
| `vertical-pull` | Pull-up, lat pulldown | 🪡 Pull |
| `horizontal-pull` | Row, cable row | 🪡 Pull |
| `isolation-curl` | Curl variations | 🪡 Pull |
| `horizontal-press` | Bench press, push-up | 🛒 Push |
| `vertical-press` | Overhead press, landmine | 🛒 Push |
| `isolation-extension` | Tricep pushdown, skull crusher | 🛒 Push |
| `squat` | Squat variations | 🍗 Legs |
| `lunge` | Lunge, split squat | 🍗 Legs |
| `leg-isolation` | Leg curl, leg extension, calf raise | 🍗 Legs |
| `carry` | Farmer's walk, suitcase carry | ➕ Plus |
| `anti-rotation` | Pallof press, landmine rotation | ➕ Plus |
| `core-stability` | Plank, hollow hold | ➕ Plus |
| `olympic` | Clean, snatch, jerk (GOLD-gated) | ➕ Plus |
| `conditioning` | Row, run, bike (sustained) | ➖ Ultra |
| `plyometric` | Box jump, broad jump (GOLD-gated) | ➕ Plus |

---

## Backward Compatibility

Existing fully-specified cards name exercises directly. The engine handles both formats:

**Template card:**
```markdown
🧈 BREAD & BUTTER
Role: bread-butter-primary → [engine resolves at render time]
...
```

**Fully-specified card (current format):**
```markdown
🧈 BREAD & BUTTER
Set 1: ⛽ 80% × 5 🪡 Barbell Deadlift (slow off the floor)
...
```

When the engine encounters a named exercise (not a role declaration), it returns that exercise directly. Prescription is still computed from the user's ledger if available.

No existing card needs to be converted. Template format is additive.

---

## Worked Example: Converting a Deck 08 Card to Template Format

**Original (fully-specified, ⛽🔨🪡🔵):**
```markdown
🧈 BREAD & BUTTER
Set 1: ⛽ 78% × 5 🪡 Single-Leg Romanian Deadlift (slow descent, hip to heel)
Set 2: ⛽ 80% × 5 🪡 Single-Leg Romanian Deadlift (squeeze top)
Set 3: ⛽ 82% × 4 🪡 Single-Leg Romanian Deadlift (controlled, full ROM)

🧩 SUPPLEMENTAL
├─ 3 × 8 🪡 Dumbbell Row (elbow tight, full retraction)
└─ 3 × 10 🪡 Face Pull (external rotation at peak)
```

**Template format equivalent (⛽🔨🪡🔵):**
```yaml
blocks:
  bread-butter:
    role:
      id: "bread-butter-primary"
      movement_pattern: "hip-hinge"
      compound: true
      bilateral: false          # 🔨 Functional bias = unilateral preferred
      block: "🧈"
      rep_range: [4, 6]
      intensity_ceiling: "85%"
      axis_bias: "🔨"
      notes: "Unilateral hip hinge. 🔨 Functional bias."
  supplemental:
    - role:
        id: "supplemental-1"
        movement_pattern: "horizontal-pull"
        compound: true
        bilateral: false
        block: "🧩"
        rep_range: [8, 10]
    - role:
        id: "supplemental-2"
        movement_pattern: "isolation-curl|horizontal-pull"
        compound: false
        bilateral: true
        block: "🧩"
        rep_range: [10, 12]
```

The template version produces different exercise selections for different users. The fully-specified version always produces Single-Leg RDL, Dumbbell Row, Face Pull. Both are valid. The template version becomes the target for Phase 3+ cards.

---

🧮
