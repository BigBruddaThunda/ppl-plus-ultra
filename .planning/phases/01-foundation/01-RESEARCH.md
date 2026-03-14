# Phase 1: Foundation - Research

**Researched:** 2026-03-14
**Domain:** TypeScript workspace scaffold + emoji/numeric zip conversion + Claude Code path-gating infrastructure
**Confidence:** HIGH — primary sources are first-party project files (zip_converter.py, zip-registry.json, settings.json, AGENT-BOUNDARIES.md) plus verified STACK.md and ARCHITECTURE.md from project init research

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

- **Type system:** Lightweight typing — simple interfaces with runtime validation, NOT branded types
- **Const objects:** All 61 SCL emoji identity maps use const objects (Orders, Axes, Types, Colors, Operators, Blocks, System) — JSON-serializable phonebook pattern matching existing Python dicts
- **Weight vector access:** Indexed array + enum — `vec[W.STRENGTH]` reads like SCL, underlying array stays JSON-compatible with existing `weight-vectors.json`
- **One consistent pattern:** All 61 SCL emojis use ONE const object + index pattern — one phonebook, one bus, regardless of category (dials, operators, blocks, system)
- **Dual hierarchy documented separately:**
  - System hierarchy (constraint resolution): Order > Color > Axis > Type — math enforced at runtime by the resolver
  - Experience hierarchy (navigation/UX): Axis > Color > Order > Type — the elevator model; Axis = floor, Color = room
  - Both coexist. The constraint hierarchy lives exclusively in the resolver, NOT in the types.
- **Package structure:** canvas/ at repo root with its own package.json, isolated from web/, middle-math/, cards/
- **Foundation module:** TypeScript port of zip_converter.py

### Claude's Discretion

- Python vs TypeScript strategy for existing middle-math scripts (port, keep both, or vendor)
- Package boundary between canvas/ and middle-math/ compiled JSON files (import vs copy)
- AGENT-BOUNDARIES.md content and path-gating pattern for hooks
- Exact tsconfig strictness settings
- Test framework setup (Vitest confirmed from research)

### Deferred Ideas (OUT OF SCOPE)

- Experience hierarchy (Axis > Color > Order > Type) as a navigation pattern — belongs in the visual canvas layer (Session 3+), not in the foundation types
- The phonebook pattern as domain-swappable for Graph Parti — noted for extraction architecture, not Phase 1 scope
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| FOUND-01 | TypeScript type definitions for all SCL primitives (Order, Axis, Type, Color, Operator, Block) with emoji and numeric representations | The Python dict structure in zip_converter.py is the direct port template; const object + numeric enum pattern verified |
| FOUND-02 | Emoji ↔ numeric zip conversion (bidirectional, all 1,680 addresses) | zip_converter.py is a complete reference implementation; TypeScript port is a direct translation |
| FOUND-03 | Deck derivation from zip code ((order - 1) * 6 + axis) | Formula verified in zip_converter.py `zip_to_deck()` function and zip-registry.json |
| FOUND-04 | canvas/ directory scaffold with clean separation from web/, middle-math/, cards/ | web/package.json confirms existing stack; canvas/ does not yet exist; Vite scaffold approach confirmed in STACK.md |
| TEST-01 | Unit tests for zip converter (all 1,680 round-trip conversions) | zip-registry.json contains all 1,680 entries with emoji_zip + numeric_zip — can drive the full test suite directly |
</phase_requirements>

---

## Summary

Phase 1 is a port-and-scaffold phase, not a research-heavy one. The complete source of truth already exists: `scripts/middle-math/zip_converter.py` is a production-quality Python implementation with all lookup tables, bidirectional conversion, deck derivation, operator derivation, and path generation. The TypeScript port is a direct structural translation — there are no algorithmic unknowns.

The primary engineering decisions are about the shape of the type system (locked by user decisions: const objects + numeric enums, not branded types or class hierarchies) and the workspace isolation strategy (canvas/ as a standalone Vite package). Both are settled. The AGENT-BOUNDARIES.md document already exists at `.claude/AGENT-BOUNDARIES.md` and establishes the governance pattern — Phase 1 adds canvas/ specific path-gating extensions before any canvas-specific hooks fire.

The 1,680 round-trip test (TEST-01) is straightforward: `middle-math/zip-registry.json` already contains all 1,680 entries with both `emoji_zip` and `numeric_zip` fields. The test reads the registry, converts in both directions, and asserts round-trip equality. Zero test case authorship required beyond the harness.

**Primary recommendation:** Port zip_converter.py to TypeScript first (FOUND-02 + FOUND-03), define SCL primitive types second (FOUND-01), scaffold canvas/package.json third (FOUND-04), write round-trip tests fourth (TEST-01), then document AGENT-BOUNDARIES.md canvas extensions last. Dependencies flow in this order.

---

## Standard Stack

### Core

| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| TypeScript | ^5 | All canvas/ source files | Already in web/; strict mode; the zip math is pure functions that benefit from typed array positions |
| Vite | ^8 | canvas/ dev server + build | Fastest HMR; no framework lock-in; standalone package, not a Next.js page |
| Vitest | ^4 | Unit tests for zip converter | Same config as Vite; zero extra setup for TypeScript; runs 1,680 test cases in <1s |
| Node.js built-ins | — | File I/O for reading zip-registry.json in tests | No library needed; JSON import or fs.readFileSync |

### Supporting (Phase 1 only — no parser or CSS library needed yet)

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| @vitest/coverage-v8 | ^4 | Coverage reporting | Install with Vitest; use during TEST-01 to confirm 100% branch coverage of converter |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Vitest | Jest | Jest requires Babel/ts-jest config; Vitest shares Vite config — zero setup for TypeScript; 2-4x faster |
| Vite standalone | npm init with tsc only | Vite adds HMR for Session 3+ canvas UI; no overhead in Phase 1 but avoids a config migration later |
| const objects + enums | Branded types (newtype pattern) | Branded types add zero runtime value for this domain; user decision locked: lightweight typing |

**Installation (for canvas/ workspace):**
```bash
cd canvas
npm create vite@latest . -- --template vanilla-ts
npm install
npm install -D vitest @vitest/coverage-v8
```

---

## Architecture Patterns

### Recommended Project Structure (Phase 1 scope only)

```
canvas/
├── package.json              # Standalone workspace — no web/ dependency
├── tsconfig.json             # strict: true, target: ESNext, moduleResolution: Bundler
├── vite.config.ts            # Vitest config block inline
├── src/
│   ├── types/
│   │   └── scl.ts            # All 61 SCL primitive types (FOUND-01)
│   └── parser/
│       └── zip-converter.ts  # emojiToZip(), zipToEmoji(), isValidZip(), zipToDeck() (FOUND-02, FOUND-03)
├── tests/
│   └── zip-converter.test.ts # 1,680 round-trip tests driven by zip-registry.json (TEST-01)
└── README.md
```

The `state/`, `weights/`, `rendering/`, and `components/` directories from the full architecture spec belong in later phases. Phase 1 plants only the foundation.

### Pattern 1: Phonebook Const Object

**What:** Each SCL dial category is a single const object keyed by numeric position. A reverse index (emoji → position) is derived at the same time. This mirrors the Python dict structure in zip_converter.py exactly.

**When to use:** FOUND-01 — all 61 SCL emoji type definitions.

**Example:**
```typescript
// Source: mirrors zip_converter.py ORDERS dict structure
// canvas/src/types/scl.ts

export const ORDERS = {
  1: { emoji: '🐂', name: 'Foundation', slug: 'foundation' },
  2: { emoji: '⛽', name: 'Strength',   slug: 'strength'   },
  3: { emoji: '🦋', name: 'Hypertrophy', slug: 'hypertrophy' },
  4: { emoji: '🏟', name: 'Performance', slug: 'performance' },
  5: { emoji: '🌾', name: 'Full Body',  slug: 'full-body'   },
  6: { emoji: '⚖',  name: 'Balance',   slug: 'balance'    },
  7: { emoji: '🖼',  name: 'Restoration', slug: 'restoration' },
} as const;

// Numeric enum for weight vector indexing — vec[W.STRENGTH] not vec[1]
export enum W {
  FOUNDATION  = 1,
  STRENGTH    = 2,
  HYPERTROPHY = 3,
  PERFORMANCE = 4,
  FULL_BODY   = 5,
  BALANCE     = 6,
  RESTORATION = 7,
  // ... axes, types, colors continue at offsets 8-13, 14-18, 19-26
}

// Derived reverse index — built once, used for emoji→position lookup
export const ORDER_BY_EMOJI = Object.fromEntries(
  Object.entries(ORDERS).map(([pos, { emoji }]) => [emoji, Number(pos)])
) as Record<string, number>;
```

### Pattern 2: Emoji Splitting for Zip Conversion

**What:** JavaScript's `[...emojiZip]` spread correctly splits emoji strings into grapheme clusters. This is the TypeScript equivalent of Python's `list(emoji_zip)` in zip_converter.py.

**When to use:** FOUND-02 — emojiToZip() function.

**Why it matters:** `emojiZip.split('')` splits on UTF-16 code units — it breaks multi-codepoint emojis. `[...emojiZip]` uses the string iterator which respects grapheme boundaries. Several SCL emojis are multi-codepoint (⚖, 🏟, ⌛, ➕, ➖, 🏛 contain variation selectors or multiple codepoints).

**Example:**
```typescript
// Source: direct port of zip_converter.py emoji_to_numeric()
// canvas/src/parser/zip-converter.ts

export function emojiToZip(emojiZip: string): string {
  const chars = [...emojiZip];  // NOT emojiZip.split('') — emoji-safe spread
  if (chars.length !== 4) {
    throw new Error(`emoji zip must contain exactly 4 emojis, got ${chars.length}`);
  }
  const order = ORDER_BY_EMOJI[chars[0]];
  const axis  = AXIS_BY_EMOJI[chars[1]];
  const type  = TYPE_BY_EMOJI[chars[2]];
  const color = COLOR_BY_EMOJI[chars[3]];
  if (!order) throw new Error(`invalid order emoji: ${chars[0]}`);
  if (!axis)  throw new Error(`invalid axis emoji: ${chars[1]}`);
  if (!type)  throw new Error(`invalid type emoji: ${chars[2]}`);
  if (!color) throw new Error(`invalid color emoji: ${chars[3]}`);
  return `${order}${axis}${type}${color}`;
}
```

### Pattern 3: Validation with Range Check

**What:** A numeric zip is valid only if: 4 digits, position 0 ∈ [1,7], position 1 ∈ [1,6], position 2 ∈ [1,5], position 3 ∈ [1,8].

**When to use:** isValidZip(), zipToEmoji() — any function receiving a numeric zip.

**Example:**
```typescript
// Source: direct port of zip_converter.py _validate_numeric_or_raise()
function validateNumericZip(numericZip: string): void {
  if (numericZip.length !== 4 || !/^\d{4}$/.test(numericZip)) {
    throw new Error('numeric zip must be exactly 4 digits');
  }
  const ranges = [[1,7],[1,6],[1,5],[1,8]] as const;
  const labels = ['order','axis','type','color'] as const;
  for (let i = 0; i < 4; i++) {
    const digit = Number(numericZip[i]);
    const [lo, hi] = ranges[i];
    if (digit < lo || digit > hi) {
      throw new Error(`${labels[i]} ${digit} out of range ${lo}-${hi}`);
    }
  }
}
```

### Pattern 4: Deck Derivation Formula

**What:** `deck = (order - 1) * 6 + axis`. This produces deck numbers 1–42. Both the Python `zip_to_deck()` and `middle-math/zip-registry.json` confirm this formula.

**When to use:** FOUND-03.

**Example:**
```typescript
// Source: zip_converter.py zip_to_deck() + verified against zip-registry.json
export function zipToDeck(zipStr: string): number {
  const numeric = /^\d{4}$/.test(zipStr) ? zipStr : emojiToZip(zipStr);
  validateNumericZip(numeric);
  const order = Number(numeric[0]);
  const axis  = Number(numeric[1]);
  return (order - 1) * 6 + axis;
}
```

### Pattern 5: Test Driven by zip-registry.json

**What:** `middle-math/zip-registry.json` contains all 1,680 entries with `emoji_zip` and `numeric_zip` fields pre-computed. TEST-01 imports this file and drives round-trip tests — no manual test case authorship needed.

**When to use:** zip-converter.test.ts.

**Example:**
```typescript
// canvas/tests/zip-converter.test.ts
import { describe, it, expect } from 'vitest';
import registry from '../../middle-math/zip-registry.json';
import { emojiToZip, zipToEmoji } from '../src/parser/zip-converter';

describe('zip converter — 1,680 round-trips', () => {
  for (const entry of registry) {
    it(`${entry.emoji_zip} ↔ ${entry.numeric_zip}`, () => {
      expect(emojiToZip(entry.emoji_zip)).toBe(entry.numeric_zip);
      expect(zipToEmoji(entry.numeric_zip)).toBe(entry.emoji_zip);
    });
  }
});
```

### Anti-Patterns to Avoid

- **`emojiZip.split('')` for emoji splitting:** Splits on UTF-16 code units, not grapheme clusters. Breaks multi-codepoint SCL emojis. Always use `[...emojiZip]`.
- **Branded types for ZipCode:** User decision is locked: lightweight interfaces with runtime validation. Branded types (`type ZipCode = string & { _brand: 'ZipCode' }`) add compile-time ceremony with no runtime benefit here.
- **Hierarchy logic in type definitions:** The dual hierarchy (system vs. experience) is documented in AGENT-BOUNDARIES.md and the resolver. The type const objects are pure identity maps — they contain no priority or constraint information.
- **Importing canvas/ types from web/:** canvas/ is isolated. web/ does not import from canvas/ in Phase 1. The only shared data is JSON files read from middle-math/ at build/test time.

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| 1,680 test case authorship | Manually writing 1,680 assert statements | Drive from zip-registry.json | The registry is already generated and verified; hand-authoring is error-prone and provides no additional coverage |
| Emoji string splitting | Custom grapheme parser | `[...str]` spread operator | JavaScript string iterator handles the emoji grapheme splitting correctly for all SCL emojis |
| tsconfig for strict TypeScript + Vite | Manual tsconfig research | `npm create vite@latest -- --template vanilla-ts` generates a working tsconfig.json | Vite's template includes correct `moduleResolution: Bundler` and ESNext target |

**Key insight:** The converter is a pure lookup table + validation problem. The source of truth (Python implementation + JSON registry) is complete. Phase 1 is translation, not invention.

---

## Common Pitfalls

### Pitfall 1: Emoji Splitting with split('')
**What goes wrong:** `'⛽🏛🪡🔵'.split('')` returns 8+ elements (UTF-16 code units), not 4 emojis. Conversion silently produces wrong output or throws index errors.
**Why it happens:** JavaScript strings are UTF-16; emoji characters outside the BMP use surrogate pairs. `split('')` sees each surrogate as a separate character.
**How to avoid:** Always use `[...'⛽🏛🪡🔵']` — the spread operator uses the string iterator which yields Unicode code points. Validate `chars.length === 4` after splitting.
**Warning signs:** Test fails on any emoji with a variation selector (⚖️, 🏛️) or multi-codepoint sequence.

### Pitfall 2: Importing middle-math/ JSON into canvas/ at runtime
**What goes wrong:** canvas/ src files directly `import weightVectors from '../../middle-math/weight-vectors.json'` — creating a cross-package runtime dependency that breaks if middle-math/ moves.
**Why it happens:** Relative path imports work locally but violate the package isolation principle.
**How to avoid:** For Phase 1, only tests import from middle-math/ (for the zip-registry test corpus). The canvas/src/ modules contain no middle-math/ runtime imports. If data from middle-math/ is needed in production, copy it into canvas/ at build time.
**Warning signs:** Any `../../middle-math/` import inside `canvas/src/`.

### Pitfall 3: Operator emoji mismatch between Python and TypeScript
**What goes wrong:** The Python `OPERATOR_TABLE` in zip_converter.py uses some operator emojis that differ from the canonical CLAUDE.md operator table (🪢 vs 🦢, 🏹 vs 🚀, 🎻 vs 🐋, 🫴 vs 🧲, ✍️ vs ✒️, 🧿 vs 🦉).
**Why it happens:** zip_converter.py predates the canonical operator assignments in CLAUDE.md. The Python file is a port candidate, not an authoritative spec for operators.
**How to avoid:** Use CLAUDE.md as the operator truth source, not zip_converter.py. When porting the operator table, compare against the operator table in CLAUDE.md and use the canonical emojis.
**Warning signs:** Any `derive_operator()` output that doesn't match a row in the CLAUDE.md operator table.

### Pitfall 4: Forgetting the canvas/ path gate in hooks before adding canvas-specific hooks
**What goes wrong:** A new PostToolUse hook for canvas/ fires on writes to cards/, triggering card validation logic on TypeScript source files.
**Why it happens:** The current PostToolUse hook in `.claude/settings.json` checks for `cards/` in the path. If a canvas/ hook is added without an explicit path gate, it might trigger everywhere.
**How to avoid:** AGENT-BOUNDARIES.md must document the canvas/ path-gating pattern before any canvas-specific hook is added. The pattern: `if echo "$FILE" | grep -q '^canvas/'; then [canvas logic]; fi` mirrors the existing cards/ gate.
**Warning signs:** PostToolUse hook output appearing during card generation after canvas/ hooks are added.

### Pitfall 5: tsconfig moduleResolution incompatible with JSON imports
**What goes wrong:** `import registry from '../../middle-math/zip-registry.json'` fails at compile time with "Cannot find module" even though the file exists.
**Why it happens:** TypeScript requires `"resolveJsonModule": true` in tsconfig.json to import JSON files directly. Vite's vanilla-ts template may or may not include this.
**How to avoid:** Confirm `"resolveJsonModule": true` in canvas/tsconfig.json. Alternatively, use `fs.readFileSync` + `JSON.parse` in tests (Node.js, no tsconfig change needed).
**Warning signs:** TypeScript error TS2307 on a JSON import.

---

## Code Examples

Verified patterns derived from zip_converter.py and zip-registry.json:

### Complete OPERATOR_TABLE (canonical — from CLAUDE.md, NOT zip_converter.py)
```typescript
// Source: CLAUDE.md operator table — use this, not zip_converter.py OPERATOR_TABLE
// Note: zip_converter.py has stale operator emojis (pre-identity era)
export const OPERATOR_TABLE = {
  '🏛': { preparatory: { emoji: '📍', name: 'pono'   }, expressive: { emoji: '🤌', name: 'facio'  } },
  '🔨': { preparatory: { emoji: '🧸', name: 'fero'   }, expressive: { emoji: '🥨', name: 'tendo'  } },
  '🌹': { preparatory: { emoji: '👀', name: 'specio' }, expressive: { emoji: '🦢', name: 'plico'  } },
  '🪐': { preparatory: { emoji: '🪵', name: 'teneo'  }, expressive: { emoji: '🚀', name: 'mitto'  } },
  '⌛': { preparatory: { emoji: '🐋', name: 'duco'   }, expressive: { emoji: '✒️', name: 'grapho' } },
  '🐬': { preparatory: { emoji: '🧲', name: 'capio'  }, expressive: { emoji: '🦉', name: 'logos'  } },
} as const;

export const PREPARATORY_COLORS = new Set(['⚫', '🟢', '⚪', '🟡']);
export const EXPRESSIVE_COLORS  = new Set(['🔵', '🟣', '🔴', '🟠']);
```

### Polarity derivation (direct port of zip_converter.py derive_operator)
```typescript
// Source: zip_converter.py derive_operator() — corrected operator emojis
export function deriveOperator(emojiZip: string): { emoji: string; name: string } {
  const chars = [...emojiZip];
  if (chars.length !== 4) throw new Error('emoji zip must contain exactly 4 emojis');
  const axisEntry  = OPERATOR_TABLE[chars[1] as keyof typeof OPERATOR_TABLE];
  if (!axisEntry) throw new Error(`invalid axis emoji: ${chars[1]}`);
  const colorEmoji = chars[3];
  if (PREPARATORY_COLORS.has(colorEmoji)) return axisEntry.preparatory;
  if (EXPRESSIVE_COLORS.has(colorEmoji))  return axisEntry.expressive;
  throw new Error(`invalid color emoji: ${colorEmoji}`);
}
```

### canvas/tsconfig.json (recommended)
```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "resolveJsonModule": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "outDir": "dist",
    "rootDir": "src"
  },
  "include": ["src", "tests"],
  "exclude": ["node_modules", "dist"]
}
```

### vite.config.ts with Vitest inline
```typescript
// canvas/vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    include: ['tests/**/*.test.ts'],
  },
});
```

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Python dict operator emojis (zip_converter.py) | Canonical CLAUDE.md operator table (🦢 not 🪢, 🚀 not 🏹, 🐋 not 🎻, 🧲 not 🫴, ✒️ not ✍️, 🦉 not 🧿) | Pre-identity era vs. current | TypeScript port must use CLAUDE.md as source, not zip_converter.py, for operator emojis |
| No canvas/ workspace | canvas/ as isolated Vite package at repo root | Phase 1 (now) | Clean separation from web/ Next.js stack; canvas deps don't pollute web/ |
| No TypeScript zip types | Const objects + numeric enum phonebook | Phase 1 (now) | `vec[W.STRENGTH]` reads like SCL; JSON-serializable; compatible with weight-vectors.json |

**Deprecated/outdated:**
- zip_converter.py operator emojis: pre-identity era assignments. The Python function `derive_operator()` logic is correct; the emoji constants in `OPERATOR_TABLE` are wrong. Port the logic, replace the constants with CLAUDE.md values.

---

## Open Questions

1. **Operator emoji discrepancy between zip_converter.py and CLAUDE.md**
   - What we know: Python OPERATOR_TABLE has 🪢/🏹/🎻/🫴/✍️/🧿; CLAUDE.md canonical table has 🦢/🚀/🐋/🧲/✒️/🦉
   - What's unclear: Whether zip-registry.json was generated with the old or new operators (needs spot-check)
   - Recommendation: Verify one zip from zip-registry.json against deriveOperator() using CLAUDE.md operators before writing tests that depend on operator derivation. Phase 1 TEST-01 only tests emoji↔numeric round-trip, not operators — so this is not a blocker for Phase 1.

2. **JSON import path from canvas/tests to middle-math/**
   - What we know: middle-math/zip-registry.json contains the full 1,680-entry test corpus; canvas/ and middle-math/ are sibling directories
   - What's unclear: Whether the Vite/Vitest config will resolve `../../middle-math/zip-registry.json` relative to the test file
   - Recommendation: Add `"resolveJsonModule": true` to tsconfig.json. If path resolution is problematic in Vitest, use `fs.readFileSync(path.resolve(__dirname, '../../middle-math/zip-registry.json'))` as fallback. This is a one-time setup concern, not an architectural question.

3. **AGENT-BOUNDARIES.md canvas/ extensions — exact path gate pattern**
   - What we know: Current PostToolUse hook uses `grep -q 'cards/'` pattern; the hook fires on all Edit/Write operations; AGENT-BOUNDARIES.md exists but does not yet mention canvas/
   - What's unclear: Whether to extend the existing AGENT-BOUNDARIES.md or create a new canvas-specific addendum
   - Recommendation: Add a `canvas/` section to the existing `.claude/AGENT-BOUNDARIES.md` file (it already covers all other path categories). The path-gate pattern for canvas-specific hooks: `if echo "$FILE" | grep -q '^canvas/'; then [canvas logic]; fi`.

---

## Validation Architecture

### Test Framework

| Property | Value |
|----------|-------|
| Framework | Vitest ^4 (to be installed — not yet present) |
| Config file | canvas/vite.config.ts (test block inline) |
| Quick run command | `cd canvas && npx vitest run tests/zip-converter.test.ts` |
| Full suite command | `cd canvas && npx vitest run` |

### Phase Requirements → Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| FOUND-01 | TypeScript types compile with strict mode | Build | `cd canvas && npx tsc --noEmit` | ❌ Wave 0 |
| FOUND-02 | All 1,680 emoji→numeric conversions correct | Unit | `cd canvas && npx vitest run tests/zip-converter.test.ts` | ❌ Wave 0 |
| FOUND-02 | All 1,680 numeric→emoji conversions correct | Unit | `cd canvas && npx vitest run tests/zip-converter.test.ts` | ❌ Wave 0 |
| FOUND-03 | Deck number correct for representative zips | Unit | `cd canvas && npx vitest run tests/zip-converter.test.ts` | ❌ Wave 0 |
| FOUND-04 | canvas/ package.json exists and installs cleanly | Build | `cd canvas && npm install` | ❌ Wave 0 |
| TEST-01 | 1,680 round-trip conversions all pass | Unit | `cd canvas && npx vitest run tests/zip-converter.test.ts` | ❌ Wave 0 |

### Sampling Rate

- **Per task commit:** `cd canvas && npx tsc --noEmit`
- **Per wave merge:** `cd canvas && npx vitest run`
- **Phase gate:** Full suite green before `/gsd:verify-work`

### Wave 0 Gaps

- [ ] `canvas/package.json` — workspace scaffold with Vite + Vitest
- [ ] `canvas/tsconfig.json` — strict mode, resolveJsonModule: true
- [ ] `canvas/vite.config.ts` — Vitest config inline
- [ ] `canvas/src/types/scl.ts` — covers FOUND-01
- [ ] `canvas/src/parser/zip-converter.ts` — covers FOUND-02, FOUND-03
- [ ] `canvas/tests/zip-converter.test.ts` — covers TEST-01
- [ ] Framework install: `cd canvas && npm install -D vitest @vitest/coverage-v8`

---

## Sources

### Primary (HIGH confidence)

- `scripts/middle-math/zip_converter.py` — complete Python reference implementation; all lookup tables, validation logic, deck derivation formula, operator derivation (direct read)
- `middle-math/zip-registry.json` — 1,680-entry registry confirming emoji_zip, numeric_zip, deck_number, operator fields (direct read)
- `.planning/research/STACK.md` — TypeScript 5, Vite 8, Vitest 4, version compatibility matrix (project research, 2026-03-13)
- `.planning/research/ARCHITECTURE.md` — full canvas/ directory structure, component boundaries, build order by phase (project research, 2026-03-13)
- `.planning/phases/01-foundation/01-CONTEXT.md` — locked decisions on type system, const objects, enum pattern, canvas/ isolation (2026-03-13)
- `CLAUDE.md` — canonical operator table (emojis), SCL primitive definitions (61 emojis), dual hierarchy documentation
- `.claude/settings.json` — existing PostToolUse hook pattern (path gate via grep -q 'cards/') for hook extension reference
- `.claude/AGENT-BOUNDARIES.md` — existing governance document to extend with canvas/ section
- `web/package.json` — confirmed existing stack versions (Next.js 16.1.6, React 19.2.3, TypeScript ^5)

### Secondary (MEDIUM confidence)

- `middle-math/design-tokens.json` — DRAFT status (confirmed by _meta.status field); all 8 Color palettes present; relevant to Phase 4+ rendering, not Phase 1

### Tertiary (LOW confidence — not applicable to Phase 1)

- None. All Phase 1 claims are directly supported by first-party files.

---

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — versions verified against STACK.md (itself verified against npm registry 2026-03-13); web/package.json confirms TypeScript ^5 already in repo
- Architecture: HIGH — directly derived from zip_converter.py (complete working implementation) and zip-registry.json (1,680 verified entries)
- Pitfalls: HIGH — emoji splitting pitfall is a known JavaScript behavior; operator mismatch is directly observable by comparing zip_converter.py to CLAUDE.md; remaining pitfalls are first-party config facts
- Test strategy: HIGH — zip-registry.json structure confirmed by direct read; Vitest round-trip pattern is standard

**Research date:** 2026-03-14
**Valid until:** 2026-04-14 (stack is stable; Vite/Vitest versions are pinned in STACK.md)
