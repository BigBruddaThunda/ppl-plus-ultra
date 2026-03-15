/**
 * WorkoutCard.tsx — Pure function rendering CardData to an HTML string
 *
 * CARD-01: renderWorkoutCard(data: CardData) → string
 *
 * This is intentionally a PURE FUNCTION, not a React component.
 * The .tsx extension honors the locked decision for "TSX production component"
 * while avoiding a React dependency in canvas/. When React is introduced
 * (Phase 4/5 web layer), this module converts to JSX cleanly.
 *
 * Card layout (three zones):
 *   Header zone  — Title, subtitle, CODE, 🎯 intention
 *   Block zone   — All workout blocks with uniform .ppl-block containers
 *   Footer zone  — 🚂 Junction + 🧮 SAVE blocks
 *
 * CSS vars are injected as inline style on .ppl-card (NOT :root).
 * All colors reference CSS custom properties — zero hardcoded color values.
 *
 * parseCardFile() uses gray-matter for frontmatter and marked for HTML.
 * Block bodies are split on ═══ (U+2550 Box Drawings Double Horizontal).
 */

import type { CardData, BlockData } from './types.js';

// ─── Block slug/role map ────────────────────────────────────────────────────

const BLOCK_ROLES: Record<string, BlockData['role']> = {
  'warm-up':      'orientation',
  'intention':    'orientation',
  'fundamentals': 'access',
  'circulation':  'access',
  'primer':       'access',
  'gambit':       'access',
  'progression':  'access',
  'bread-butter': 'transformation',
  'composition':  'transformation',
  'exposure':     'transformation',
  'aram':         'transformation',
  'gutter':       'transformation',
  'vanity':       'transformation',
  'sculpt':       'transformation',
  'craft':        'transformation',
  'supplemental': 'transformation',
  'sandbox':      'transformation',
  'reformance':   'transformation',
  'release':      'retention',
  'imprint':      'retention',
  'junction':     'retention',
  'save':         'retention',
  'choice':       'modifier',
};

/** Map block emoji to canonical slug */
const BLOCK_EMOJI_TO_SLUG: Record<string, string> = {
  '♨️': 'warm-up',
  '🎯': 'intention',
  '🔢': 'fundamentals',
  '🧈': 'bread-butter',
  '🫀': 'circulation',
  '▶️': 'primer',
  '🎼': 'composition',
  '♟️': 'gambit',
  '🪜': 'progression',
  '🌎': 'exposure',
  '🎱': 'aram',
  '🌋': 'gutter',
  '🪞': 'vanity',
  '🗿': 'sculpt',
  '🛠': 'craft',
  '🧩': 'supplemental',
  '🪫': 'release',
  '🏖': 'sandbox',
  '🏗': 'reformance',
  '🧬': 'imprint',
  '🚂': 'junction',
  '🔠': 'choice',
  '🧮': 'save',
};

// ─── HTML escaping ──────────────────────────────────────────────────────────

function esc(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ─── CSS vars → inline style string ────────────────────────────────────────

function cssVarsToStyle(vars: Record<string, string>): string {
  return Object.entries(vars)
    .map(([key, value]) => `${key}: ${value}`)
    .join('; ');
}

// ─── Block renderer ─────────────────────────────────────────────────────────

function renderBlock(block: BlockData): string {
  const isFooterBlock = block.slug === 'junction' || block.slug === 'save';
  const emphasisClass = block.slug === 'bread-butter' ? ' ppl-block--high-emphasis' : '';
  const footerClass = isFooterBlock ? ' ppl-block--footer' : '';

  return `
    <section class="ppl-block ppl-block--${esc(block.role)}${emphasisClass}${footerClass}" data-block="${esc(block.slug)}">
      <header class="ppl-block__header">
        <span class="ppl-block__emoji" aria-hidden="true">${esc(block.emoji)}</span>
        <h3 class="ppl-block__name">${esc(block.name)}</h3>
      </header>
      <div class="ppl-block__content">
        ${block.contentHtml}
      </div>
      ${block.slug === 'save' ? '<div class="ppl-block__save-ritual" aria-label="Session complete"></div>' : ''}
    </section>`;
}

// ─── Logging scaffold elements ───────────────────────────────────────────────

function renderLoggingScaffold(): string {
  return `
    <div class="ppl-log-scaffold" aria-label="Session logging">
      <div class="ppl-log-row">
        <label class="ppl-log-label">Weight</label>
        <input class="ppl-log-input" type="text" placeholder="kg / lb" aria-label="Weight logged" />
      </div>
      <div class="ppl-log-row">
        <label class="ppl-log-label">Reps</label>
        <input class="ppl-log-input" type="text" placeholder="reps" aria-label="Reps logged" />
      </div>
      <div class="ppl-log-row">
        <span class="ppl-timer-slot" aria-label="Rest timer">⏱ —</span>
        <label class="ppl-log-checkbox-label">
          <input class="ppl-log-checkbox" type="checkbox" aria-label="Set complete" />
          <span class="ppl-log-checkbox-text">Done</span>
        </label>
      </div>
    </div>`;
}

// ─── Main renderer ───────────────────────────────────────────────────────────

/**
 * renderWorkoutCard — pure function, CardData → HTML string.
 *
 * CSS vars are injected as inline style on .ppl-card (NOT :root).
 * The data-color attribute enables Color-specific CSS hatching patterns.
 * Zero hardcoded color values appear in the output (CARD-02).
 */
export function renderWorkoutCard(data: CardData): string {
  const styleAttr = cssVarsToStyle(data.cssVars);

  // Separate footer blocks (junction, save) from main blocks
  const mainBlocks = data.blocks.filter(b => b.slug !== 'junction' && b.slug !== 'save');
  const footerBlocks = data.blocks.filter(b => b.slug === 'junction' || b.slug === 'save');

  const mainBlocksHtml = mainBlocks.map(renderBlock).join('\n');
  const footerBlocksHtml = footerBlocks.map(renderBlock).join('\n');

  return `<article
  class="ppl-card"
  data-color="${esc(data.colorSlug)}"
  data-order="${esc(data.orderSlug)}"
  data-axis="${esc(data.axisSlug)}"
  data-zip="${esc(data.numericZip)}"
  style="${esc(styleAttr)}"
>
  <!-- ═══ HEADER ZONE ═══ -->
  <header class="ppl-card__header">
    <div class="ppl-card__header-title-row">
      <span class="ppl-card__type-emoji ppl-card__type-emoji--left" aria-hidden="true">${esc(data.typeEmoji)}</span>
      <h1 class="ppl-card__header-title">${esc(data.title)}</h1>
      <span class="ppl-card__type-emoji ppl-card__type-emoji--right" aria-hidden="true">${esc(data.typeEmoji)}</span>
    </div>
    <p class="ppl-card__subtitle">${esc(data.subtitle)}</p>
    <div class="ppl-card__meta">
      <span class="ppl-card__code" aria-label="Zip code">${esc(data.zip)}</span>
      <span class="ppl-card__operator">${esc(data.operator)}</span>
      <span class="ppl-card__numeric-zip" aria-label="Numeric zip">${esc(data.numericZip)}</span>
    </div>
    <blockquote class="ppl-card__intention" aria-label="Session intention">
      <span class="ppl-card__intention-emoji" aria-hidden="true">🎯</span>
      "${esc(data.intention)}"
    </blockquote>
  </header>

  <!-- ═══ BLOCK ZONE ═══ -->
  <div class="ppl-card__block-zone">
    ${mainBlocksHtml}
    ${renderLoggingScaffold()}
  </div>

  <!-- ═══ FOOTER ZONE ═══ -->
  <footer class="ppl-card__footer">
    ${footerBlocksHtml}
  </footer>
</article>`;
}

// ─── parseCardFile ──────────────────────────────────────────────────────────

/**
 * COLOR_POS_TO_SLUG maps Color dial position (1-8) to data-color attribute slug.
 * Position comes from SCL: ⚫=1, 🟢=2, 🔵=3, 🟣=4, 🔴=5, 🟠=6, 🟡=7, ⚪=8
 */
const COLOR_POS_TO_SLUG: Record<number, string> = {
  1: 'teaching',
  2: 'bodyweight',
  3: 'structured',
  4: 'technical',
  5: 'intense',
  6: 'circuit',
  7: 'fun',
  8: 'mindful',
};

/**
 * ORDER_POS_TO_SLUG maps Order dial position (1-7) to slug.
 */
const ORDER_POS_TO_SLUG: Record<number, string> = {
  1: 'foundation',
  2: 'strength',
  3: 'hypertrophy',
  4: 'performance',
  5: 'full-body',
  6: 'balance',
  7: 'restoration',
};

/**
 * AXIS_POS_TO_SLUG maps Axis dial position (1-6) to slug.
 */
const AXIS_POS_TO_SLUG: Record<number, string> = {
  1: 'basics',
  2: 'functional',
  3: 'aesthetic',
  4: 'challenge',
  5: 'time',
  6: 'partner',
};

/**
 * TYPE_POS_TO_EMOJI maps Type dial position (1-5) to emoji.
 */
const TYPE_POS_TO_EMOJI: Record<number, string> = {
  1: '🛒',
  2: '🪡',
  3: '🍗',
  4: '➕',
  5: '➖',
};

/**
 * NUMERIC_ZIP_DIALS: SCL emoji → numeric dial position mappings.
 */
const ORDER_EMOJI_TO_POS: Record<string, number> = {
  '🐂': 1, '⛽': 2, '🦋': 3, '🏟': 4, '🌾': 5, '⚖': 6, '🖼': 7,
};
const AXIS_EMOJI_TO_POS: Record<string, number> = {
  '🏛': 1, '🔨': 2, '🌹': 3, '🪐': 4, '⌛': 5, '🐬': 6,
};
const TYPE_EMOJI_TO_POS: Record<string, number> = {
  '🛒': 1, '🪡': 2, '🍗': 3, '➕': 4, '➖': 5,
};
const COLOR_EMOJI_TO_POS: Record<string, number> = {
  '⚫': 1, '🟢': 2, '🔵': 3, '🟣': 4, '🔴': 5, '🟠': 6, '🟡': 7, '⚪': 8,
};

/**
 * parseZipToNumeric converts "⛽🏛🪡🔵" → "2123"
 */
function parseZipToNumeric(zip: string): string {
  // Split into grapheme clusters (emoji are multi-codepoint)
  const chars = [...zip];
  if (chars.length < 4) return '0000';
  const o = ORDER_EMOJI_TO_POS[chars[0] ?? ''] ?? 0;
  const a = AXIS_EMOJI_TO_POS[chars[1] ?? ''] ?? 0;
  const t = TYPE_EMOJI_TO_POS[chars[2] ?? ''] ?? 0;
  const c = COLOR_EMOJI_TO_POS[chars[3] ?? ''] ?? 0;
  return `${o}${a}${t}${c}`;
}

/**
 * Extracts the block header emoji and name from a markdown section heading.
 * Handles formats like "## 1. ♨️ WARM-UP" or "### ♨️ Warm-Up" etc.
 */
function parseBlockHeader(headerLine: string): { emoji: string; name: string } {
  // Strip markdown heading markers and numbering
  const cleaned = headerLine.replace(/^#+\s*/, '').replace(/^\d+\.\s*/, '').trim();
  // Try to extract leading emoji
  const emojiMatch = /^(\p{Emoji_Presentation}|\p{Extended_Pictographic})\s*/u.exec(cleaned);
  if (emojiMatch) {
    const emoji = emojiMatch[1] ?? '';
    const name = cleaned.slice(emojiMatch[0].length).trim();
    return { emoji, name: name || 'Block' };
  }
  return { emoji: '▪️', name: cleaned || 'Block' };
}

/**
 * parseCardFile — reads a .md workout card file and returns CardData.
 *
 * This function uses Node.js fs (server-side only). It cannot run in
 * a browser context directly.
 *
 * @param filePath - Absolute or relative path to the .md card file
 * @returns Fully resolved CardData ready for renderWorkoutCard()
 */
export function parseCardFile(filePath: string): CardData {
  // Dynamic requires — Node.js server context only
  // eslint-disable-next-line @typescript-eslint/no-require-imports
  const fs = require('node:fs');
  // eslint-disable-next-line @typescript-eslint/no-require-imports
  const matter = require('gray-matter');
  // eslint-disable-next-line @typescript-eslint/no-require-imports
  const { marked } = require('marked');
  // eslint-disable-next-line @typescript-eslint/no-require-imports
  const path = require('node:path');

  const raw = fs.readFileSync(filePath, 'utf-8') as string;
  const parsed = matter(raw) as { data: Record<string, string>; content: string };
  const fm = parsed.data;

  // ─── Extract zip from frontmatter ────────────────────────────────────────
  const zip = (fm['zip'] as string | undefined) ?? '';
  const numericZip = parseZipToNumeric(zip);

  // Parse dial positions from numeric zip
  const orderPos = parseInt(numericZip[0] ?? '1');
  const axisPos  = parseInt(numericZip[1] ?? '1');
  const typePos  = parseInt(numericZip[2] ?? '1');
  const colorPos = parseInt(numericZip[3] ?? '3');

  const colorSlug = COLOR_POS_TO_SLUG[colorPos] ?? 'structured';
  const orderSlug = ORDER_POS_TO_SLUG[orderPos] ?? 'strength';
  const axisSlug  = AXIS_POS_TO_SLUG[axisPos] ?? 'basics';
  const typeEmoji = TYPE_POS_TO_EMOJI[typePos] ?? '🛒';

  // ─── Derive CSS vars from weight pipeline ─────────────────────────────────
  // Import resolver and weightsToCSSVars at runtime (ESM-compatible)
  // Using require with path.resolve for Windows ESM compatibility
  // eslint-disable-next-line @typescript-eslint/no-require-imports
  const resolverPath = path.resolve(__dirname, '../src/weights/resolver.js');
  // eslint-disable-next-line @typescript-eslint/no-require-imports
  const weightsPath = path.resolve(__dirname, '../src/rendering/weights-to-css-vars.js');
  // eslint-disable-next-line @typescript-eslint/no-require-imports
  const tokensPath = path.resolve(__dirname, '../src/tokens/tokens.js');

  let cssVars: Record<string, string> = {};
  try {
    // eslint-disable-next-line @typescript-eslint/no-require-imports
    const { resolveZip } = require(resolverPath) as { resolveZip: (o: number, a: number, t: number, c: number) => Float32Array };
    // eslint-disable-next-line @typescript-eslint/no-require-imports
    const { weightsToCSSVars } = require(weightsPath) as { weightsToCSSVars: (v: Float32Array, t: unknown) => Record<string, string> };
    // eslint-disable-next-line @typescript-eslint/no-require-imports
    const { tokens } = require(tokensPath) as { tokens: unknown };
    const vector = resolveZip(orderPos, axisPos, typePos, colorPos);
    cssVars = weightsToCSSVars(vector, tokens as Parameters<typeof weightsToCSSVars>[1]);
  } catch {
    // Fallback: empty cssVars — preview can still render with CSS var defaults
    cssVars = {};
  }

  // ─── Extract title from filename ─────────────────────────────────────────
  const filename = path.basename(filePath, '.md') as string;
  // Format: "⛽🏛🪡🔵±🤌 Bent-Over Barbell Row — Back Strength Log"
  // Everything after the operator emoji and space is the title
  const titleMatch = /±\S+\s+(.+)$/.exec(filename);
  const title = titleMatch ? (titleMatch[1] ?? filename) : filename;

  // ─── Extract operator from frontmatter ───────────────────────────────────
  const operator = (fm['operator'] as string | undefined) ?? '';

  // ─── Build subtitle from Order/Axis/Type/Color names ─────────────────────
  const orderLine = (fm['order'] as string | undefined) ?? '';
  const typeLine  = (fm['type'] as string | undefined) ?? '';
  const colorLine = (fm['color'] as string | undefined) ?? '';
  const orderName = orderLine.split('|')[0]?.trim().replace(/^⛽\s*/, '').replace(/^🐂\s*/, '').replace(/^🦋\s*/, '').replace(/^🏟\s*/, '').replace(/^🌾\s*/, '').replace(/^⚖\s*/, '').replace(/^🖼\s*/, '').trim() ?? orderSlug;
  const typePart  = typeLine.split('|')[0]?.trim() ?? '';
  const colorPart = colorLine.split('|')[0]?.trim() ?? '';
  const subtitle = `${orderName} · ${typePart} · ${colorPart} · ~50 min`;

  // ─── Parse block content ──────────────────────────────────────────────────
  const content = parsed.content;

  // Split on ═══ block separator (U+2550 repeated)
  // Blocks start with a heading line containing the block emoji
  const blockSections = content.split(/\n(?=#{1,3}\s)/);
  const blocks: BlockData[] = [];
  let blockNumber = 0;

  for (const section of blockSections) {
    const lines = section.split('\n');
    const headerLine = lines[0] ?? '';
    if (!headerLine.match(/^#{1,3}\s/)) continue;

    blockNumber++;
    const { emoji, name } = parseBlockHeader(headerLine);
    const bodyLines = lines.slice(1).join('\n').trim();
    const slug = BLOCK_EMOJI_TO_SLUG[emoji] ?? name.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');
    const role = BLOCK_ROLES[slug] ?? 'transformation';
    const contentHtml = marked.parse(bodyLines) as string;

    blocks.push({
      number: blockNumber,
      emoji,
      name,
      content: bodyLines,
      contentHtml,
      slug,
      role,
    });
  }

  // ─── Extract 🎯 INTENTION ─────────────────────────────────────────────────
  let intention = '';
  const intentionMatch = /"([^"]+)"/.exec(content);
  if (intentionMatch) {
    intention = intentionMatch[1] ?? '';
  }

  return {
    zip,
    numericZip,
    operator,
    title,
    subtitle,
    intention,
    typeEmoji,
    blocks,
    cssVars,
    colorSlug,
    orderSlug,
    axisSlug,
  };
}
