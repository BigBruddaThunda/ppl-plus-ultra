# CSS Property Arbitration Spec

**Status:** COMPLETE
**Phase:** 04-design-tokens
**Blocking:** Phase 5 rendering code (weightsToCSSVars() and all deriver functions)
**Authority:** This document is the single source of truth for CSS property ownership. No property has two owners.

---

## Principle

Every CSS custom property in the Ppl± design system belongs to exactly one dial.

> If a property encodes **intensity/mood** → **Color** owns it.
> If a property encodes **rhythm/density/weight** → **Order** owns it.
> If a property encodes **direction/character/visual flow** → **Axis** owns it.
> If a property encodes **body-region/muscle-group illustration content** → **Type** owns the slot.

No property is shared. No property is derived from two dials. When Phase 5 writes
`weightsToCSSVars()`, it reads exactly one dial to produce each CSS custom property.

---

## 3+1 Ownership Model

| Dial | Domain | CSS Property Families |
|------|--------|-----------------------|
| **Order** | Structural: rhythm, density, weight | fontWeight, lineHeight, spacingMultiplier, letterSpacing, density, animationDuration, opacity (default states), gridGap/blockGap |
| **Color** | Tonal: mood, intensity, palette | primary, secondary, background, surface, text, accent, border, borderRadius, shadowDepth, saturation |
| **Axis** | Directional: character, visual flow | gradientDirection, layoutFlow, fontFamily, typographyBias |
| **Type** | Content: body-region illustration slot | illustrationSlot (declared; content deferred to Phase 5+) |

---

## Exhaustive Property Mapping Table

| CSS Custom Property Pattern | Owner Dial | Value Source | Count | Notes |
|-----------------------------|-----------|--------------|-------|-------|
| `--ppl-order-*--fontWeight` | Order | `design-tokens.json orders[name].fontWeight` | 7 | Body text weight; one per Order |
| `--ppl-order-*--fontWeightDisplay` | Order | `design-tokens.json orders[name].fontWeightDisplay` | 7 | Display/header weight; one per Order |
| `--ppl-order-*--lineHeight` | Order | `design-tokens.json orders[name].lineHeight` | 7 | Line height multiplier; one per Order |
| `--ppl-order-*--spacingMultiplier` | Order | `design-tokens.json orders[name].spacingMultiplier` | 7 | Spacing scale factor; one per Order |
| `--ppl-order-*--letterSpacing` | Order | `design-tokens.json orders[name].letterSpacing` | 7 | Letter spacing; one per Order |
| `--ppl-order-*--density` | Order | `design-tokens.json orders[name].density` | 7 | Density descriptor string (compact/spacious/airy); one per Order |
| `--ppl-order-*--animationDuration` | Order | `design-tokens.json orders[name].animationDuration` | 7 | Transition/animation duration; structural rhythm not mood |
| `--ppl-order-*--opacity` | Order | `design-tokens.json orders[name].opacity` | 7 | Default element opacity; affects information density |
| `--ppl-order-*--gridGap` | Order | `design-tokens.json orders[name].gridGap` | 7 | Grid/flex gap; spacing density is Order's structural domain |
| `--ppl-color-*--primary` | Color | `design-tokens.json colors[name].primary` | 8 | Dominant color; one per Color tonal identity |
| `--ppl-color-*--secondary` | Color | `design-tokens.json colors[name].secondary` | 8 | Supporting color; one per Color tonal identity |
| `--ppl-color-*--background` | Color | `design-tokens.json colors[name].background` | 8 | Background color; one per Color tonal identity |
| `--ppl-color-*--surface` | Color | `design-tokens.json colors[name].surface` | 8 | Surface/card color; one per Color tonal identity |
| `--ppl-color-*--text` | Color | `design-tokens.json colors[name].text` | 8 | Body text color on surface; one per Color tonal identity |
| `--ppl-color-*--accent` | Color | `design-tokens.json colors[name].accent` | 8 | Accent highlight; one per Color tonal identity |
| `--ppl-color-*--border` | Color | `design-tokens.json colors[name].border` | 8 | Border/divider color; one per Color tonal identity |
| `--ppl-color-*--borderRadius` | Color | `design-tokens.json colors[name].borderRadius` | 8 | Corner radius; roundness is a tonal quality (Order=sharp, Eudaimonia=soft) |
| `--ppl-color-*--shadowDepth` | Color | `design-tokens.json colors[name].shadowDepth` | 8 | Shadow intensity; tracks Color saturation and mood, not structure |
| `--ppl-color-*--saturation` | Color | `design-tokens.json colors[name].saturation` | 8 | Chroma/saturation level descriptor; tonal not structural |
| `--ppl-axis-*--gradientDirection` | Axis | `design-tokens.json axes[name].gradientDirection` | 6 | CSS gradient direction string; one per Axis character |
| `--ppl-axis-*--layoutFlow` | Axis | `design-tokens.json axes[name].layoutFlow` | 6 | Flex/grid flow direction; directional character of Axis |
| `--ppl-axis-*--fontFamily` | Axis | `design-tokens.json axes[name].fontFamily` | 6 | Font family (not weight); expresses Axis character (⌛→mono, 🌹→editorial, 🔨→condensed) |
| `--ppl-axis-*--typographyBias` | Axis | `design-tokens.json axes[name].typographyBias` | 6 | Typography style descriptor (classical/athletic/editorial/dramatic/precision/warm) |
| `--ppl-type-*--illustrationSlot` | Type | Deferred; content is per-exercise illustration | 5 | Slot declared; actual illustration content is Phase 5+. NOT layout or color. |

**Total properties declared:** 24 patterns × dial multipliers = 59 distinct CSS custom property families (7+7+7+7+7+7+7+7 Order=56 values, 8×10 Color=80 values, 6×4 Axis=24 values, 5×1 Type=5 slots)

---

## Edge-Case Assignments with Rationale

| Property | Owner | Competing Dial | Resolution Principle |
|----------|-------|---------------|----------------------|
| `borderRadius` | **Color** | Could be Order (structural shape) | Roundness is tonal: ⚫ Order = sharp engraved corners; ⚪ Eudaimonia = soft rounded. It expresses Color character, not session rhythm. |
| `shadowDepth` | **Color** | Could be Order (structural depth) | Shadow intensity tracks Color saturation: dark/intense Colors = deeper shadows. Mood, not density. |
| `opacity` | **Order** | Could be Color (visual mood) | Opacity affects information density on screen. 🖼 Restoration uses lighter opacity elements (less information density). Structural. |
| `animationDuration` | **Order** | Could be Color (mood-based pacing) | Animation speed is structural rhythm. 🏟 Performance = instant transitions (no distraction); 🖼 Restoration = slow, deliberate. Session tempo is Order's domain. |
| `fontFamily` | **Axis** | Could be Order (weight/structure) | Font *family* (not weight) expresses Axis character: ⌛ Time → monospace numeric; 🌹 Aesthetic → editorial serif; 🔨 Functional → condensed. Directional character, not density. |
| `gridGap/blockGap` | **Order** | Could be Axis (layout direction) | Spacing gap is density. How much space between elements = Order's rhythm domain. What direction they flow = Axis. |
| `saturation` | **Color** | Could be Order (intensity level) | Saturation is the chroma level of the Color tonal identity. It describes the mood quality of the color, not structural session parameters. |

---

## W Enum → Tonal Name Bridge Table

Phase 5's `weightsToCSSVars()` uses W enum positions to identify the dominant Color.
This table is the authoritative mapping from numeric position to token key.

| W Enum Position | W Constant | SCL Color Name | Tonal Token Key | CSS Example |
|----------------|-----------|----------------|-----------------|-------------|
| 19 | `W.TEACHING` | Teaching | `order` | `--ppl-color-order--primary` |
| 20 | `W.BODYWEIGHT` | Bodyweight | `growth` | `--ppl-color-growth--primary` |
| 21 | `W.STRUCTURED` | Structured | `planning` | `--ppl-color-planning--primary` |
| 22 | `W.TECHNICAL` | Technical | `magnificence` | `--ppl-color-magnificence--primary` |
| 23 | `W.INTENSE` | Intense | `passion` | `--ppl-color-passion--primary` |
| 24 | `W.CIRCUIT` | Circuit | `connection` | `--ppl-color-connection--primary` |
| 25 | `W.FUN` | Fun | `play` | `--ppl-color-play--primary` |
| 26 | `W.MINDFUL` | Mindful | `eudaimonia` | `--ppl-color-eudaimonia--primary` |

**Index convention for Phase 5:**
- W enum is 1-indexed: positions 1–26 (W.FOUNDATION=1 through W.MINDFUL=26)
- Token access is by semantic name (`tokens.colors.passion`), NOT by numeric index
- Phase 5 must use `COLOR_W_TO_TONAL[wPosition]` to look up the token key from a W position
- Do NOT access `tokens.colors[19]` — this will be undefined. Use `tokens.colors['passion']`.

---

## Naming Convention

CSS custom properties use double-hyphen separators to encode structural grouping:

```
--ppl-[category]-[tonal-or-order-or-axis-name]--[property]
     ↑           ↑                              ↑↑
     namespace   dial value name                double hyphen = property separator
```

Examples:
- `--ppl-color-passion--primary` (Color dial, passion tonal name, primary property)
- `--ppl-order-strength--fontWeight` (Order dial, strength name, fontWeight property)
- `--ppl-axis-basics--gradientDirection` (Axis dial, basics name, gradientDirection property)
- `--ppl-type-push--illustrationSlot` (Type dial, push name, illustration slot — deferred)

The double hyphen between `[name]` and `[property]` is the structural separator.
Style-dictionary requires a custom name transform to produce this pattern.
See RESEARCH.md Pattern 3 (Custom Name Transform) for the registered transform code.

---

## Conflict Check

The following properties were evaluated for potential dual ownership and resolved:

| Property Family | Could Belong To | Assigned To | Conflict Resolved |
|-----------------|----------------|-------------|-------------------|
| `borderRadius` | Color or Order | **Color** | Yes — tonal quality wins |
| `shadowDepth` | Color or Order | **Color** | Yes — mood over structure |
| `opacity` | Order or Color | **Order** | Yes — density over mood |
| `animationDuration` | Order or Color | **Order** | Yes — rhythm over mood |
| `fontFamily` | Axis or Order | **Axis** | Yes — character over weight |
| `gridGap` | Order or Axis | **Order** | Yes — density over direction |
| `saturation` | Color or Order | **Color** | Yes — tonal not structural |

**Result: Zero properties with dual ownership.** Every CSS custom property in the system maps to exactly one dial.

---

## Phase Links

- **Produced by:** Plan 04-01 (this spec)
- **Consumed by:** Plan 04-02 (design-tokens.json shape uses owner categories) and Phase 5 (weightsToCSSVars() deriver functions)
- **Key link:** `design-tokens.json` categories (`colors`, `orders`, `axes`) map directly to the three active owner dials in this spec
- **RNDR-04 requirement:** Satisfied by this document's existence at this path

---

*CSS Property Arbitration Spec — Phase 04-design-tokens*
*Locked: 2026-03-14*
*No property has two owners.*
