/**
 * derive-colors.mjs
 *
 * Derives 8 OKLCH Color palettes for the Ppl± design token system.
 * Each palette is derived from base hue parameters (H, C, L) using culori,
 * with gamut clamping to p3 display space.
 *
 * Tonal color names map to SCL Color positions:
 *   order        ⚫ Teaching     (W=19)
 *   growth       🟢 Bodyweight   (W=20)
 *   planning     🔵 Structured   (W=21)
 *   magnificence 🟣 Technical    (W=22)
 *   passion      🔴 Intense      (W=23)
 *   connection   🟠 Circuit      (W=24)
 *   play         🟡 Fun          (W=25)
 *   eudaimonia   ⚪ Mindful      (W=26)
 *
 * Usage:
 *   node canvas/scripts/derive-colors.mjs
 *   node canvas/scripts/derive-colors.mjs --stdout  (prints JSON to stdout)
 */

import { formatCss, clampChroma } from 'culori';
import { writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

// ─── Base hue parameters (H, C, L) ───────────────────────────────────────────
// Intaglio/banknote aesthetic: muted, ink-like, rich but not neon.

const COLOR_BASES = {
  order:        { h: 0,   c: 0.00, l: 0.20, emoji: '⚫', scl_name: 'Teaching',     tier: '2-3', gold: false },
  growth:       { h: 145, c: 0.12, l: 0.42, emoji: '🟢', scl_name: 'Bodyweight',   tier: '0-2', gold: false },
  planning:     { h: 230, c: 0.14, l: 0.40, emoji: '🔵', scl_name: 'Structured',   tier: '2-3', gold: false },
  magnificence: { h: 285, c: 0.18, l: 0.38, emoji: '🟣', scl_name: 'Technical',    tier: '2-5', gold: true  },
  passion:      { h: 25,  c: 0.22, l: 0.42, emoji: '🔴', scl_name: 'Intense',      tier: '2-4', gold: true  },
  connection:   { h: 45,  c: 0.18, l: 0.55, emoji: '🟠', scl_name: 'Circuit',      tier: '0-3', gold: false },
  play:         { h: 85,  c: 0.16, l: 0.72, emoji: '🟡', scl_name: 'Fun',          tier: '0-5', gold: false },
  eudaimonia:   { h: 60,  c: 0.02, l: 0.92, emoji: '⚪', scl_name: 'Mindful',      tier: '0-3', gold: false },
};

// ─── Palette derivation formulas ──────────────────────────────────────────────
// Each formula takes (L, C, H) base values and returns an oklch object.

function derivePalette(L, C, H) {
  const clamp = (obj) => clampChroma(obj, 'oklch', 'p3');
  const fmt = (obj) => formatCss(clamp(obj));

  return {
    primary:    fmt({ mode: 'oklch', l: Math.max(0, Math.min(1, L)),           c: C,        h: H }),
    secondary:  fmt({ mode: 'oklch', l: Math.max(0, Math.min(1, L + 0.10)),    c: C * 0.80, h: H }),
    background: fmt({ mode: 'oklch', l: Math.max(0, Math.min(1, 0.97)),        c: C * 0.10, h: H }),
    surface:    fmt({ mode: 'oklch', l: 1.00, c: 0, h: 0 }),
    text:       fmt({ mode: 'oklch', l: Math.max(0, Math.min(1, L - 0.14)),    c: C * 0.65, h: H }),
    accent:     fmt({ mode: 'oklch', l: Math.max(0, Math.min(1, L - 0.06)),    c: C * 0.90, h: H }),
    border:     fmt({ mode: 'oklch', l: Math.max(0, Math.min(1, 0.82)),        c: C * 0.30, h: H }),
  };
}

// ─── Derive all 8 palettes ────────────────────────────────────────────────────

export function deriveAllPalettes() {
  const result = {};

  for (const [tonalName, base] of Object.entries(COLOR_BASES)) {
    const palette = derivePalette(base.l, base.c, base.h);
    result[tonalName] = {
      emoji:      base.emoji,
      scl_name:   base.scl_name,
      tonal_name: tonalName,
      base_hue:   base.h,
      base_chroma: base.c,
      tier:       base.tier,
      gold:       base.gold,
      ...palette,
    };
  }

  return result;
}

// ─── Main ─────────────────────────────────────────────────────────────────────

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const palettes = deriveAllPalettes();
  const printOnly = process.argv.includes('--stdout');

  if (printOnly) {
    console.log(JSON.stringify(palettes, null, 2));
  } else {
    const outPath = join(__dirname, '..', 'src', 'tokens', 'design-tokens.json');

    // Read existing file if present, preserve orders and axes sections
    let existing = {};
    try {
      const { readFileSync } = await import('fs');
      existing = JSON.parse(readFileSync(outPath, 'utf8'));
    } catch {
      // No existing file — start fresh
    }

    existing.colors = palettes;

    writeFileSync(outPath, JSON.stringify(existing, null, 2) + '\n');
    console.log(`Wrote color palettes to ${outPath}`);
    console.log(`Colors derived: ${Object.keys(palettes).join(', ')}`);
  }
}
