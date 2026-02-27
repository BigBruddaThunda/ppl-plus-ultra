---
planted: 2026-02-26
status: SEED
phase-relevance: Phase 4/5/6/7 (all downstream systems)
blocks: nothing in Phase 2-3
depends-on: nothing (foundational notation)
connects-to: seeds/experience-layer-blueprint.md, middle-math/ARCHITECTURE.md, middle-math/schemas/zip-metadata-schema.md
---

# 🔢 The Numeric Zip System — 4 Digits, 1,680 Rooms

🔵🟣 — structured + precise

## One Sentence

Every PPL± zip code emoji has a numeric position on its dial (Order 1-7, Axis 1-6, Type 1-5, Color 1-8), making every zip code a 4-digit integer that serves as the system-layer addressing key for URLs, database primary keys, API routing, weight vector computation, and every context where emojis cannot operate.

---

## The Problem

Emojis break in URLs (percent-encoding), database indexing (collation-dependent, variable byte-width), log files, email clients, SMS, legacy browsers, accessibility screen readers, CSV exports, analytics dashboards, and any system that handles strings at the byte level. The emoji is the human display layer. It cannot be the system layer.

## The Notation

Each emoji on each dial has a fixed numeric position, starting at 1.

### Orders (Dial 1: positions 1-7)

| Position | Emoji | Name |
|----------|-------|------|
| 1 | 🐂 | Foundation |
| 2 | ⛽ | Strength |
| 3 | 🦋 | Hypertrophy |
| 4 | 🏟 | Performance |
| 5 | 🌾 | Full Body |
| 6 | ⚖ | Balance |
| 7 | 🖼 | Restoration |

### Axes (Dial 2: positions 1-6)

| Position | Emoji | Name |
|----------|-------|------|
| 1 | 🏛 | Basics / Firmitas |
| 2 | 🔨 | Functional / Utilitas |
| 3 | 🌹 | Aesthetic / Venustas |
| 4 | 🪐 | Challenge / Gravitas |
| 5 | ⌛ | Time / Temporitas |
| 6 | 🐬 | Partner / Sociatas |

### Types (Dial 3: positions 1-5)

| Position | Emoji | Name |
|----------|-------|------|
| 1 | 🛒 | Push |
| 2 | 🪡 | Pull |
| 3 | 🍗 | Legs |
| 4 | ➕ | Plus |
| 5 | ➖ | Ultra |

### Colors (Dial 4: positions 1-8)

| Position | Emoji | Name |
|----------|-------|------|
| 1 | ⚫ | Teaching |
| 2 | 🟢 | Bodyweight |
| 3 | 🔵 | Structured |
| 4 | 🟣 | Technical |
| 5 | 🔴 | Intense |
| 6 | 🟠 | Circuit |
| 7 | 🟡 | Fun |
| 8 | ⚪ | Mindful |

## The 4-Digit Zip Code

Concatenate four positions: `[Order][Axis][Type][Color]`

⛽🏛🪡🔵 → 2 1 2 3 → `2123`

Always exactly 4 digits. Leading digits never zero (Order starts at 1). Valid range: `1111` to `7658`. Not every number in range is valid — `1174` fails because Type position 7 doesn't exist (max 5).

## Validation

```typescript
export function isValidZip(zip: string): boolean {
  if (zip.length !== 4) return false;
  const [o, a, t, c] = zip.split('').map(Number);
  return o >= 1 && o <= 7 && a >= 1 && a <= 6
      && t >= 1 && t <= 5 && c >= 1 && c <= 8;
}
```

## Conversion

```typescript
const ORDERS = ['', '🐂', '⛽', '🦋', '🏟', '🌾', '⚖', '🖼'];
const AXES   = ['', '🏛', '🔨', '🌹', '🪐', '⌛', '🐬'];
const TYPES  = ['', '🛒', '🪡', '🍗', '➕', '➖'];
const COLORS = ['', '⚫', '🟢', '🔵', '🟣', '🔴', '🟠', '🟡', '⚪'];

export function zipToEmoji(zip: string): string {
  const [o, a, t, c] = zip.split('').map(Number);
  return `${ORDERS[o]}${AXES[a]}${TYPES[t]}${COLORS[c]}`;
}

export function emojiToZip(emoji: string): string {
  const chars = [...emoji];
  return `${ORDERS.indexOf(chars[0])}${AXES.indexOf(chars[1])}${TYPES.indexOf(chars[2])}${COLORS.indexOf(chars[3])}`;
}
```

## Deck Derivation

```typescript
export function zipToDeck(zip: string): number {
  const order = parseInt(zip[0]);
  const axis = parseInt(zip[1]);
  return (order - 1) * 6 + axis;
}
// '2123' → Deck 7. '2223' → Deck 8. '1111' → Deck 1. '7658' → Deck 42.
```

## URL Format

`/zip/2123` → Room ⛽🏛🪡🔵. Clean. Indexable. Bookmarkable. No percent-encoding.

## Database Primary Key

`zip_code CHAR(4)` in all tables. The emoji display is derived at the application layer. See `middle-math/schemas/zip-metadata-schema.md`.

## Weight Vector Integration

The numeric positions ARE the array indices for middle-math weight computation. Numbers in, numbers out. The emoji layer is presentation. The number layer is computation.

---

🧮
