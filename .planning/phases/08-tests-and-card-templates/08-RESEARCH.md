# Phase 8: Tests and Card Templates — Research

**Researched:** 2026-03-15
**Domain:** Vitest test authoring, HTML/TSX card rendering, intaglio CSS art direction, markdown parsing
**Confidence:** HIGH (all findings verified against existing codebase)

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**Card Template Structure**
- Zoned layout — Header zone (title with flanking emoji, subtitle, CODE line, intention), Block zone (scrollable uniform blocks with heavy border separators), Footer zone (junction + save). Each zone is a distinct visual region.
- Uniform blocks — All 22 block types use the same container treatment. The emoji header and content inside distinguish them. No visual variation by operational role.
- Bold emoji anchors — Type emoji flanking the title are large, colorized, and serve as the card's visual identity.

**Intaglio CSS Techniques**
- Full intaglio treatment — Line-work borders (fine 1-2px, possibly double/engraved-style), hatching patterns via repeating-linear-gradient for block backgrounds, guilloche pattern accents, and vignette darkening at card edges.
- Hybrid pattern system — Saturation from the weight system drives pattern DENSITY/BOLDNESS. The Color identity determines the SHAPE of the pattern (crosshatch vs parallel vs diagonal vs radial).
- SVG-based guilloche — Inline SVG or SVG background-image for guilloche patterns.

**Test Coverage**
- 10 representative zips — Start with 2123 as the anchor. Researcher picks 9 more spanning all 7 Orders.
- Multiple pipeline inputs — 3-4 different text inputs for integration tests.
- Keyword scoring tests — Known terms route to correct dimensions, collision-prone words handled correctly.

**Card Interactivity**
- Logging-ready scaffold — HTML structure complete; JavaScript logic is PLACEHOLDER/STUBBED.
- Dual format: HTML preview + TSX production component — Self-contained HTML + TSX component in canvas/components/.

### Claude's Discretion
- Which 9 additional zip codes to spot-check (must span all 7 Orders)
- Exact CSS techniques for each intaglio effect
- TSX component architecture (number of sub-components, state management for logging scaffold)
- How to parse .md workout cards into template data (markdown parsing approach)
- Test organization (one big test file vs separate files per concern)

### Deferred Ideas (OUT OF SCOPE)
- Full workout logging JavaScript (set completion, rest timers, weight/rep persistence)
- Server-side rendering of cards
- User history integration
- Dark mode card variant
- Card-to-card navigation (junction zip code links)
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| TEST-02 | Unit tests for weight vector computation (spot-check 10 representative zips across all Orders) | resolveZip() is callable synchronously; existing rendering.test.ts uses zip 2123 as anchor; 9 additional zips selected below covering all 7 Orders and edge cases |
| TEST-03 | Unit tests for keyword dictionary scoring (known terms → correct dimension routing) | scorer.test.ts already tests normalizeInput, tokenize, expandToken; new tests extend to dimension routing assertions; existing KEYWORD_MAP and DEFAULTS constants support assertions |
| TEST-05 | Integration test for full pipeline (text input → ParseResult → weight vector → CSS vars) | scoreText() → ParseResult.weightVector → weightsToCSSVars(); all three functions are already pure and synchronously importable; no async barriers |
| CARD-01 | HTML/TSX template rendering a .md workout card as an interactive web component | .md cards have YAML frontmatter + markdown body; frontmatter is machine-readable; body requires markdown parsing to extract blocks; canvas/components/ is the write target |
| CARD-02 | Template consumes CSS custom properties from weight vector (no hardcoded styles) | weightsToCSSVars() produces all 30+ CSS vars; card frontmatter zip field is the pipeline entry; HTML template injects vars inline on :root or card container |
| CARD-03 | Intaglio art direction applied via publication standard CSS (hatching, engraving aesthetic) | repeating-linear-gradient for hatching, inline SVG for guilloche, COLOR_SATURATION drives density; Color position from zip determines pattern shape |
</phase_requirements>

---

## Summary

Phase 8 is the capstone phase: it validates the entire pipeline end-to-end and produces the first visual card output. It has two independent work streams that can proceed in parallel — the test suite (TEST-02, TEST-03, TEST-05) and the card template (CARD-01, CARD-02, CARD-03).

The test work is additive: 8 test files already exist with 6,949 tests. New tests follow the exact same Vitest patterns already established. The weight vector tests require selecting 9 additional zips beyond the 2123 anchor, running resolveZip(), and asserting properties of the resulting CSS vars. The keyword scoring tests extend the existing scorer.test.ts file. The integration test chains scoreText() → weightsToCSSVars() in a single describe block.

The card template work is new territory. The .md card format is parseable: YAML frontmatter provides machine-readable metadata (zip, operator, order, axis, type, color, blocks), and the markdown body follows the 15-element SCL format. The template renders from the frontmatter zip (which drives CSS vars) and the parsed markdown body (which populates block content). The intaglio art direction is CSS-only: repeating-linear-gradient for hatching, SVG patterns for guilloche, opacity variation for vignette. No external CSS framework is involved.

**Primary recommendation:** Split the phase into two plans — Plan 08-01 for tests (TEST-02, TEST-03, TEST-05) and Plan 08-02 for card templates (CARD-01, CARD-02, CARD-03). Tests can ship independently and validate the pipeline before the visual layer is added.

---

## Standard Stack

### Core (already installed in canvas/)
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| vitest | ^3.0.0 | Test runner | Already configured, vite.config.ts points to tests/**/*.test.ts |
| typescript | ^5.7.0 | Type safety | noUncheckedIndexedAccess already configured |
| vite | ^6.0.0 | Build/dev server | canvas/ package.json entry point |

### Supporting (for card template parsing)
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| gray-matter | ^4.0.3 | YAML frontmatter extraction | Parsing card .md files to get zip, blocks, operator metadata |
| marked OR remark | ^12.x / ^15.x | Markdown → HTML/AST | Converting block body content to renderable HTML |

No new test libraries needed. No React needed for Phase 8 — TSX component is React but no React runtime is needed for the HTML preview file.

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| gray-matter | manual YAML parsing | gray-matter handles edge cases (multi-line strings, quoted emoji); manual parsing is fragile |
| marked | remark | remark is AST-based (better for structured extraction); marked is simpler if only HTML output is needed; either works for Phase 8 since blocks are visually rendered not further processed |

**Installation for card template plan only:**
```bash
cd canvas && npm install gray-matter marked
```

---

## Architecture Patterns

### Test File Organization

Based on the existing 8-file test structure, Phase 8 adds:

```
canvas/tests/
├── zip-converter.test.ts       # existing — 6,762 tests
├── keyword-dict.test.ts        # existing
├── weight-tables.test.ts       # existing
├── exercise-dict.test.ts       # existing
├── resolver.test.ts            # existing
├── scorer.test.ts              # existing
├── tokens.test.ts              # existing
├── rendering.test.ts           # existing — TEST-04 (done)
├── weight-vectors.test.ts      # NEW — TEST-02: 10 zip spot-checks
├── keyword-routing.test.ts     # NEW — TEST-03: keyword dimension routing
└── pipeline-integration.test.ts # NEW — TEST-05: full pipeline end-to-end
```

This keeps concerns separated. The alternative (one big Phase 8 test file) works but loses the discoverability pattern of the existing suite.

### Pattern 1: Weight Vector Spot-Check (TEST-02)

Each spot-check follows the same 3-assertion pattern: (1) dominant Order CSS var matches expected, (2) dominant Color CSS var matches expected, (3) suppressed types score near zero.

```typescript
// Source: canvas/tests/rendering.test.ts (established pattern)
describe('zip 7131 (🖼🏛🛒🔴) — Restoration/Basics/Push/Intense', () => {
  let vector: Float32Array;
  beforeAll(() => { vector = resolveZip(7, 1, 3, 5); });

  it('Order group: Restoration tokens', () => {
    const css = weightsToCSSVars(vector, tokens);
    expect(css['--ppl-weight-density']).toBe('airy');
  });

  it('Color group: Intense (passion tonal) tokens', () => {
    const css = weightsToCSSVars(vector, tokens);
    expect(css['--ppl-theme-primary']).toBe(tokens.colors.passion.primary);
  });

  it('--ppl-weight-saturation >= 0.85 (Intense Color)', () => {
    const css = weightsToCSSVars(vector, tokens);
    expect(parseFloat(css['--ppl-weight-saturation']!)).toBeGreaterThanOrEqual(0.85);
  });
});
```

### Pattern 2: Keyword Dimension Routing (TEST-03)

Each test asserts that scoreText() returns a primary ParseResult with the expected dimension position.

```typescript
// Source: canvas/tests/scorer.test.ts (established pattern)
describe('Keyword routing — Order dimension', () => {
  it('"heavy barbell" routes to Order 2 (Strength)', () => {
    const results = scoreText('heavy barbell');
    expect(results[0]!.orderPos).toBe(2);
  });

  it('"restorative flow" routes to Order 7 (Restoration)', () => {
    const results = scoreText('restorative flow');
    expect(results[0]!.orderPos).toBe(7);
  });
});
```

### Pattern 3: Full Pipeline Integration (TEST-05)

One describe block chains the complete pipeline without errors, asserting the output shape at each stage.

```typescript
// Source: pipeline design established in Phase 3 scorer.ts
describe('TEST-05: Full pipeline — text input to CSS vars', () => {
  it('strength query: text → ParseResult → WeightVector → CSS vars', () => {
    const results = scoreText('heavy barbell back work');
    expect(results.length).toBeGreaterThan(0);
    const primary = results[0]!;
    expect(primary.weightVector).toBeInstanceOf(Float32Array);
    const css = weightsToCSSVars(primary.weightVector, tokens);
    expect(Object.keys(css).length).toBeGreaterThanOrEqual(30);
    // All CSS var values are non-empty strings
    for (const val of Object.values(css)) {
      expect(typeof val).toBe('string');
      expect(val.length).toBeGreaterThan(0);
    }
  });
});
```

### Pattern 4: Card Template Structure (CARD-01, CARD-02, CARD-03)

```
canvas/components/
├── WorkoutCard.tsx           # TSX production component (React)
├── WorkoutCard.css           # Intaglio styles — imported by TSX
├── card-preview.html         # Self-contained HTML preview (no build step)
└── types.ts                  # CardData interface
```

The `card-preview.html` file is standalone: it loads design-tokens.css via `<link>`, inlines the CSS vars from weightsToCSSVars() output in a `<style>` block on `:root`, and contains the card HTML structure. It opens directly in a browser.

The TSX component accepts a `CardData` prop (parsed from a .md file) and renders the same structure, consuming the CSS vars injected by the parent app.

### CardData Interface

Derived from card frontmatter + parsed body:

```typescript
interface CardData {
  zip: string;          // "⛽🏛🪡🔵"
  numericZip: string;   // "2123"
  operator: string;     // "🤌 facio"
  title: string;        // "Bent-Over Barbell Row — Back Strength Log"
  subtitle: string;     // "Strength Basics — Pull focus (Structured) · 50-65 min"
  intention: string;    // "Same weight, same reps, same rest..."
  blocks: BlockData[];  // parsed block array
  cssVars: Record<string, string>; // from weightsToCSSVars()
}

interface BlockData {
  number: number;
  emoji: string;
  name: string;
  role: string;         // from BLOCK_CONTAINER_STYLES
  content: string;      // raw markdown block body
  contentHtml: string;  // parsed HTML for rendering
}
```

### Anti-Patterns to Avoid

- **Hardcoding CSS color values:** All color values must come from CSS custom properties. Never write `color: oklch(0.2 0 0)` inline.
- **Parsing blocks with regex:** The .md format uses consistent `## N) EMOJI Name` headers. Parse with a heading-split approach, not character-level regex.
- **Resolving zip inside the template:** The template receives already-resolved CSS vars. It does not import resolveZip(). The parent (preview HTML or app) resolves and injects.
- **Using JSX for the HTML preview:** The HTML preview must open in a browser without a build step. No JSX compilation in the HTML file.
- **Guilloche as raster:** SVG-based guilloche scales to any screen density. PNG/JPEG does not.

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| YAML frontmatter extraction | Custom `---` block splitter | gray-matter | Handles quoted emoji, multi-line strings, edge whitespace |
| Markdown to HTML | Character-level parser | marked or remark | Table rendering, code blocks, nested lists in block content |
| CSS var injection in HTML | `document.documentElement.style.setProperty()` in a loop | Inline `<style>:root{--var: val;}</style>` block | Works without JS for static preview; readable diff |
| Hatching patterns | CSS background-image with data URI PNG | `repeating-linear-gradient()` | Pure CSS, scales perfectly, themeable via CSS vars |

**Key insight:** The .md card format is deliberately machine-readable. The frontmatter zip field is the complete pipeline input — a single `resolveZip()` call produces the entire CSS var set. The template is thin.

---

## Common Pitfalls

### Pitfall 1: Emoji in YAML frontmatter
**What goes wrong:** YAML parsers may choke on unquoted emoji strings in frontmatter (e.g., `zip: ⛽🏛🪡🔵`). Some parsers interpret the emoji bytes incorrectly.
**Why it happens:** The .md cards were not written with programmatic parsing in mind — they were written for human readers.
**How to avoid:** gray-matter handles this gracefully. If using a raw YAML parser, quote the emoji fields. Test with a card containing all 8 Color emojis.
**Warning signs:** `zip` field coming back as `undefined` or truncated.

### Pitfall 2: Block body parsing — the === separator
**What goes wrong:** The .md block format uses `═══` (U+2550 Box Drawings Double Horizontal) as block separators, not standard `---` or `***`. String splitting on standard markdown thematic breaks fails.
**Why it happens:** SCL uses a distinct separator character so it does not conflict with YAML front matter separators.
**How to avoid:** Split block body on `/^═══$/m` (Unicode Box Drawing character U+2550). Test this explicitly against the actual card files.
**Warning signs:** All blocks merging into one block, or zero blocks parsed.

### Pitfall 3: CSS var injection scope
**What goes wrong:** CSS custom properties injected on `:root` affect the entire page. If the HTML preview contains multiple cards (future use), they all receive the same vars.
**Why it happens:** `:root` is global scope.
**How to avoid:** Inject CSS vars on the card container element (`.ppl-card`) not on `:root`. This also matches how the TSX component will work — it applies vars to its own root element via `style` prop.
**Warning signs:** Two cards on the same page showing identical color themes.

### Pitfall 4: The "10 zips" test — wrong assertion pattern
**What goes wrong:** Testing that `resolveZip(o, a, t, c)` returns a Float32Array of length 62 is not a spot-check. That is a shape test (already covered by resolver.test.ts). TEST-02 requires asserting SPECIFIC CSS values for SPECIFIC zips.
**Why it happens:** It is tempting to write a generic pass-through test.
**How to avoid:** Each of the 10 zips must have at least one assertion about a concrete CSS property value derived from the known Order or Color of that zip (e.g., zip 7xxx always gets density = 'airy', zip xx1x always gets emphasis-push near 1.0).
**Warning signs:** Tests that would pass for ANY zip, not just the specified one.

### Pitfall 5: intaglio pattern density — saturation vs. pattern
**What goes wrong:** Using `--ppl-weight-saturation` to drive BOTH pattern density AND color opacity, making low-saturation Colors (Teaching at 0.05) invisible rather than refined.
**Why it happens:** Saturation feels like an obvious proxy for "how visible should the pattern be."
**How to avoid:** Use saturation to drive gradient stop opacity in the hatching (e.g., `rgba(0,0,0, calc(var(--ppl-weight-saturation) * 0.3))`). The background remains visible — only the pattern intensity varies. Teaching gets hairline etchings; Intense gets bold crosshatch. Neither is invisible.
**Warning signs:** Teaching cards looking like blank white cards.

### Pitfall 6: TSX component requires React in canvas/
**What goes wrong:** Installing React in the canvas/ package creates a dependency that conflicts with the "clean separation from web/" principle. React is already in web/.
**Why it happens:** TSX implies React.
**How to avoid:** The TSX file uses React JSX syntax but does NOT import React from canvas/'s own node_modules. It is written for consumption by the production app (web/), which already has React. The TSX file is a source artifact — the HTML preview is the runnable artifact. canvas/ does not need React as a dependency. Consider using `.tsx` extension with a `// @ts-ignore` comment for the HTML/react-independent preview, or structure WorkoutCard as a pure function that returns a string (an HTML generator, not a React component) and use it in both the HTML and as a React component wrapper.
**Warning signs:** `npm install react react-dom` in canvas/ — stop and reconsider.

---

## Code Examples

### Hatching Pattern — Hybrid System

```css
/* Source: CSS repeating-linear-gradient technique, verified against MDN */

/* Color-specific pattern SHAPE (⚫ Teaching = parallel, 🔴 Intense = crosshatch) */
/* Density driven by --ppl-weight-saturation */

/* Teaching (⚫): fine parallel lines — barely visible */
.ppl-card[data-color="teaching"] .ppl-block {
  background-image: repeating-linear-gradient(
    45deg,
    transparent,
    transparent 4px,
    rgba(0, 0, 0, calc(var(--ppl-weight-saturation, 0.05) * 0.4)) 4px,
    rgba(0, 0, 0, calc(var(--ppl-weight-saturation, 0.05) * 0.4)) 5px
  );
}

/* Intense (🔴): bold crosshatch */
.ppl-card[data-color="intense"] .ppl-block {
  background-image:
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 3px,
      rgba(0, 0, 0, calc(var(--ppl-weight-saturation, 0.90) * 0.25)) 3px,
      rgba(0, 0, 0, calc(var(--ppl-weight-saturation, 0.90) * 0.25)) 4px
    ),
    repeating-linear-gradient(
      -45deg,
      transparent,
      transparent 3px,
      rgba(0, 0, 0, calc(var(--ppl-weight-saturation, 0.90) * 0.25)) 3px,
      rgba(0, 0, 0, calc(var(--ppl-weight-saturation, 0.90) * 0.25)) 4px
    );
}
```

### Guilloche — SVG Background

```html
<!-- Source: SVG pattern technique — inline SVG as CSS background -->
<!-- Guilloche rosette for card header accent -->
<style>
.ppl-card__header-guilloche {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80'%3E%3Ccircle cx='40' cy='40' r='35' fill='none' stroke='%23000' stroke-width='0.5' opacity='0.15'/%3E%3Ccircle cx='40' cy='40' r='25' fill='none' stroke='%23000' stroke-width='0.5' opacity='0.12'/%3E%3Ccircle cx='40' cy='40' r='15' fill='none' stroke='%23000' stroke-width='0.5' opacity='0.10'/%3E%3C/svg%3E");
  background-repeat: repeat-x;
  background-size: 80px 80px;
}
</style>
```

### Vignette Edge Darkening

```css
/* Source: CSS radial-gradient technique for vignette */
.ppl-card {
  background-image: radial-gradient(
    ellipse at center,
    transparent 60%,
    rgba(0, 0, 0, 0.08) 100%
  );
}
```

### gray-matter Frontmatter Extraction

```typescript
// Source: gray-matter npm package API
import matter from 'gray-matter';
import { readFileSync } from 'fs';

const raw = readFileSync(cardPath, 'utf-8');
const { data, content } = matter(raw);

// data.zip === "⛽🏛🪡🔵"
// data.operator === "🤌 facio"
// content === markdown body after frontmatter
```

### Block Splitting

```typescript
// Source: analysis of actual .md card files — separator is ═══ (U+2550)
const BLOCK_SEPARATOR = /^═══$/m;

function parseBlocks(content: string): string[] {
  // Remove the first line if it is the intention quote (before block 1)
  return content.split(BLOCK_SEPARATOR)
    .map(s => s.trim())
    .filter(s => s.length > 0);
}
```

### CSS Var Injection — Card Container Scope

```typescript
// Source: established pattern from weightsToCSSVars()
function buildCardStyle(cssVars: Record<string, string>): string {
  const declarations = Object.entries(cssVars)
    .map(([k, v]) => `  ${k}: ${v};`)
    .join('\n');
  return declarations;
}

// In HTML preview: set on card container element, not :root
// <div class="ppl-card" style="--ppl-weight-font-weight: 800; ...">
```

---

## 10 Representative Zips (TEST-02 Selection)

The anchor zip 2123 (⛽🏛🪡🔵) covers Order 2/Strength, Axis 1/Basics, Type 2/Pull, Color 3/Structured.

9 additional zips selected to span all 7 Orders and include edge cases:

| Numeric | Emoji | Order | Axis | Type | Color | Why Selected |
|---------|-------|-------|------|------|-------|-------------|
| 2123 | ⛽🏛🪡🔵 | Strength | Basics | Pull | Structured | Anchor — existing tests |
| 1213 | 🐂🔨🛒🔴 | Foundation | Functional | Push | Intense | Order 1, GOLD gate suppression (Intense on Foundation) |
| 3352 | 🦋🌹🍗🟢 | Hypertrophy | Aesthetic | Legs | Bodyweight | Order 3, no-barbell suppression |
| 4145 | 🏟🏛➕⚪ | Performance | Basics | Plus | Mindful | Order 4, few-blocks rule |
| 5241 | 🌾🔨➕⚫ | Full Body | Functional | Plus | Teaching | Order 5, flow-unity requirement |
| 6313 | ⚖🌹🛒🔴 | Balance | Aesthetic | Push | Intense | Order 6, crosshatch pattern |
| 7218 | 🖼🔨🪡⚪ | Restoration | Functional | Pull | Mindful | Order 7, somatic context |
| 2444 | ⛽🪐➕🟣 | Strength | Challenge | Plus | Technical | GOLD unlocked (Technical), challenge axis |
| 3163 | 🦋🏛🐬🔴 | Hypertrophy | Basics | Ultra | Intense | Ultra type, max saturation |
| 6526 | ⚖⌛🔨🟡 | Balance | Time | Functional | Fun | Time axis, fun/exploration pattern |

Note: zips 4145 and 6526 use 4-digit numeric but map to non-standard axes in some positions — verify with zipToEmoji() before asserting. The selection intentionally uses non-trivial zip codes that exercise known suppression paths.

---

## Intaglio Art Direction — Pattern Shape by Color

| Color | Pattern Shape | CSS Technique | Density Driver |
|-------|--------------|---------------|---------------|
| ⚫ Teaching | Fine parallel lines (45deg) | Single repeating-linear-gradient | 0.05 saturation → hairline |
| 🟢 Bodyweight | Loose parallel (natural) | Single gradient, wider spacing | 0.40 saturation → light |
| 🔵 Structured | Ruled ledger lines (horizontal) | Horizontal repeating-linear-gradient | 0.50 saturation → medium |
| 🟣 Technical | Fine crosshatch (precision grid) | Double gradient (45/-45) | 0.65 saturation → dense fine |
| 🔴 Intense | Bold crosshatch (copper plate) | Double gradient, tight spacing | 0.90 saturation → heavy |
| 🟠 Circuit | Diagonal stripes (energy) | Single gradient (60deg) | 0.70 saturation → engaged |
| 🟡 Fun | Loose diagonal (playful) | Single gradient (30deg), wider | 0.75 saturation → open |
| ⚪ Mindful | Barely-there horizontal (calm) | Horizontal gradient, very pale | 0.10 saturation → whisper |

Guilloche appears in the card header zone only — not block backgrounds. It is a static SVG pattern, not weight-driven. It uses the Color's `--ppl-theme-border` value (passed via CSS variable) for its stroke color.

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Hardcoded CSS colors | OKLCH CSS custom properties from design-tokens.css | Phase 4 (2026-03-14) | All card colors are derived from the weight pipeline |
| Generic markdown parser assumptions | U+2550 Box Drawing separator confirmed in actual .md files | Analysis for Phase 8 | Parser must split on ═══ not --- |
| React required for TSX | TSX as source artifact only; HTML preview is the runnable file | Phase 8 decision | canvas/ does not need React as a dependency |

---

## Open Questions

1. **gray-matter or manual YAML split?**
   - What we know: gray-matter handles edge cases gracefully; it is a standard Node.js package with no native dependencies
   - What's unclear: Whether Jake wants zero new dependencies in canvas/
   - Recommendation: Use gray-matter. It is small (15KB), zero native deps, well-maintained. Manual YAML splitting is brittle against the actual card files (emoji in frontmatter, multi-line values).

2. **WorkoutCard.tsx — React component or HTML generator function?**
   - What we know: canvas/ does not currently have React; web/ has React; TSX is required per CONTEXT.md
   - What's unclear: Whether the planner should install React in canvas/ or write WorkoutCard.tsx as a pure function (HTML string generator) usable in both contexts
   - Recommendation: Write WorkoutCard.tsx as a pure function that returns an HTML string: `function WorkoutCard(data: CardData): string`. This is usable in the HTML preview without React and importable into the production app as a utility. The `.tsx` extension is a signal of intent; actual JSX syntax is not required if the function returns a string. Avoids React installation in canvas/.

3. **Which 2 cards to render in the HTML preview?**
   - What we know: Anchor zip 2123 has a generated card (⛽🏛🪡🔵±🤌 Bent-Over Barbell Row)
   - What's unclear: Whether to render one card or two to show visual contrast across Colors
   - Recommendation: Render two cards: 2123 (⛽🏛🪡🔵, Structured/blue tonal) and one Intense zip (e.g., 2115 ⛽🏛🛒🔴) to demonstrate the pattern density contrast between 0.50 and 0.90 saturation. Confirms the hybrid pattern system works visually.

---

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | Vitest 3.x |
| Config file | canvas/vite.config.ts (test.include: "tests/**/*.test.ts") |
| Quick run command | `cd canvas && npm test` |
| Full suite command | `cd canvas && npm test` (all 8+ files run together) |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| TEST-02 | 10 zip spot-checks: resolveZip() → weightsToCSSVars() → expected CSS values | unit | `cd canvas && npm test -- weight-vectors` | ❌ Wave 0 |
| TEST-03 | Keyword terms route to expected dimension positions via scoreText() | unit | `cd canvas && npm test -- keyword-routing` | ❌ Wave 0 |
| TEST-05 | Full pipeline: scoreText() → ParseResult → weightsToCSSVars() → 30+ CSS vars | integration | `cd canvas && npm test -- pipeline-integration` | ❌ Wave 0 |
| CARD-01 | WorkoutCard renders .md card without throwing | smoke | `cd canvas && npm test -- card-template` (if test added) | ❌ Wave 0 |
| CARD-02 | Rendered output contains no hardcoded OKLCH/hex values | lint | Visual review of WorkoutCard output HTML | manual |
| CARD-03 | Intaglio patterns visible in HTML preview | visual | Open card-preview.html in browser | manual |

### Sampling Rate
- **Per task commit:** `cd canvas && npm test`
- **Per wave merge:** `cd canvas && npm test` (full suite — currently runs in ~3s for 6,949 tests)
- **Phase gate:** Full suite green before `/gsd:verify-work`

### Wave 0 Gaps
- [ ] `canvas/tests/weight-vectors.test.ts` — covers TEST-02 (10 zip spot-checks)
- [ ] `canvas/tests/keyword-routing.test.ts` — covers TEST-03 (keyword dimension routing)
- [ ] `canvas/tests/pipeline-integration.test.ts` — covers TEST-05 (full pipeline)
- [ ] `canvas/components/types.ts` — CardData and BlockData interfaces
- [ ] gray-matter install: `cd canvas && npm install gray-matter marked`

*(All three test files are NEW files; no existing file modifications needed for Wave 0.)*

---

## Sources

### Primary (HIGH confidence)
- `canvas/tests/rendering.test.ts` — established test pattern for this codebase
- `canvas/src/rendering/weights-to-css-vars.ts` — all 30 CSS var names and derivation logic verified
- `canvas/src/rendering/saturation-map.ts` — COLOR_SATURATION values for all 8 Colors
- `canvas/src/rendering/block-styles.ts` — 22-block BLOCK_CONTAINER_STYLES map
- `canvas/src/weights/resolver.ts` — resolveZip() API signature
- `canvas/src/parser/scorer.ts` — scoreText() API signature and pipeline stages
- `cards/⛽-strength/🏛-basics/🪡-pull/⛽🏛🪡🔵±🤌 Bent-Over Barbell Row — Back Strength Log.md` — actual .md card format confirmed (YAML frontmatter + ═══ separator)
- `canvas/package.json` — no React, no markdown parser currently installed

### Secondary (MEDIUM confidence)
- gray-matter npm package — standard frontmatter parser, verified against Node.js ecosystem patterns
- CSS `repeating-linear-gradient()` — MDN-documented, widely supported, confirmed for SVG-free hatching
- Inline SVG as CSS `background-image` data URI — standard technique, supported in all modern browsers

### Tertiary (LOW confidence)
- Specific guilloche SVG path complexity — LOW. The exact SVG path data for guilloche rosettes requires visual iteration. The technique (SVG as background-image) is HIGH confidence; the exact aesthetic requires live review.

---

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — all libraries already in canvas/ or are standard npm packages
- Architecture: HIGH — derived from actual codebase inspection, not assumptions
- Test patterns: HIGH — copied from existing test files
- CSS intaglio techniques: MEDIUM — CSS techniques are standard; specific visual output requires browser iteration
- Markdown parsing: HIGH — .md format confirmed from actual card files

**Research date:** 2026-03-15
**Valid until:** 2026-04-15 (stable stack — no fast-moving dependencies)
