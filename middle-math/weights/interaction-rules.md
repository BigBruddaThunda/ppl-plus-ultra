# Weight Interaction Rules

When multiple dials affect the same emoji, these rules determine the result.

---

## The Constraint Hierarchy

Priority order when dials conflict:

1. **ORDER** — Hard ceiling. Order weight cannot be overridden upward by any dial below it.
2. **COLOR** — Hard filter. Color suppressions cannot be overridden upward by Axis or Type.
3. **AXIS** — Soft bias. Axis weights add to the running total.
4. **TYPE** — Soft context. Type weights add to the running total.

The constraint hierarchy here mirrors the scl-directory.md constraint hierarchy for exercise selection. The same logic that governs which exercise wins also governs how weights combine.

---

## Rule 1 — Hard Suppression Wins

If any dial with higher priority (Order or Color) declares a weight of **-6 or lower** for an emoji, that suppression holds regardless of what lower-priority dials declare.

**Example:**
- 🖼 Order declares 🌋 Gutter at -8 ("Never in 🖼")
- 🔴 Color declares 🌋 Gutter at +6 ("Gutter possible in 🔴")
- Result at 🖼🌹🛒🔴: **-8**. Order wins. Gutter never appears in Restoration.

**Example:**
- 🟠 Circuit declares barbell exercises at -8 ("No barbells in 🟠")
- 🏛 Axis declares barbell exercises at +7 (Basics prioritizes barbell)
- Result at ⛽🏛🛒🟠: **-8** for barbells. Color's hard filter holds.

---

## Rule 2 — Soft Weights Sum and Clamp

For weights above -6 from both dials (or from two dials neither of which has higher-priority hard suppression), **sum the weights and clamp to the range [-8, +8]**.

**Example:**
- ⛽ Order declares 🏛 Basics at +3
- 🔵 Color declares 🏛 Basics at +2
- Result: +3 + +2 = **+5**

**Example:**
- ⛽ Order declares 🪫 Release at +4
- 🏛 Axis declares 🪫 Release at +2
- 🪡 Type declares 🪫 Release at +2
- 🔵 Color declares 🪫 Release at +2
- Raw sum: +10 → clamped to **+8**

---

## Rule 3 — Same-Priority Conflict

Within a single zip code, each position (Order, Axis, Type, Color) appears exactly once. There are no same-priority conflicts in a valid zip code. This rule applies only in edge cases such as multi-address computation or system-level weight aggregation.

If two entities at equal priority disagree: **average and round toward zero**.

---

## Rule 4 — Temporal Layer

Date-derived weights apply as a **final ±1 adjustment** after all dial weights are resolved.

Sources of temporal weight:
- The current month's Axis operator (from rotation engine): +1 to that Axis's primary affinity emojis
- The current day-of-week Order: +1 to that Order's primary affinity emojis

**Constraint:** Temporal weights nudge but never override. They cannot push a dial-derived weight above +8 or below -8. They cannot reverse a hard suppression.

**Example:**
- Tuesday (⛽ day) temporal weight: +1 to ⛽'s affinity emojis
- March (🧸 fero / 🔨 Functional month) temporal weight: +1 to 🔨's affinity emojis
- These apply on top of the already-resolved zip code weight vector

---

## Application Order (summary)

1. Apply primary weights (+8 for each active dial's own emoji)
2. Apply each dial's affinity cascade (positive weights to other emojis)
3. Apply each dial's suppression cascade (negative weights to other emojis)
4. Resolve conflicts using hierarchy (Order > Color > Axis > Type):
   - Hard suppressions (-6 or lower from higher-priority dial) override all lower-priority weights
   - Remaining soft weights sum and clamp
5. Apply temporal ±1 nudge

The result is a 61-value weight vector. Every number is derivable from rules. No inference required.

---

🧮
