/**
 * card-api.ts — Vite dev server middleware that serves real card data.
 *
 * GET /api/card/:numericZip → JSON CardData from the actual .md file in cards/
 * GET /api/cards → JSON list of all available zip codes with titles
 *
 * This runs server-side in Node — has access to fs.
 */

import fs from 'node:fs';
import path from 'node:path';
import type { Connect } from 'vite';
import type { CardData, BlockData } from '../components/types.js';

// ─── SCL lookups (inline to avoid import issues in Vite middleware) ────────

const ORDERS: Record<number, { emoji: string; name: string; slug: string }> = {
  1: { emoji: '🐂', name: 'Foundation', slug: 'foundation' },
  2: { emoji: '⛽', name: 'Strength', slug: 'strength' },
  3: { emoji: '🦋', name: 'Hypertrophy', slug: 'hypertrophy' },
  4: { emoji: '🏟', name: 'Performance', slug: 'performance' },
  5: { emoji: '🌾', name: 'Full Body', slug: 'full-body' },
  6: { emoji: '⚖', name: 'Balance', slug: 'balance' },
  7: { emoji: '🖼', name: 'Restoration', slug: 'restoration' },
};

const AXES: Record<number, { emoji: string; name: string; slug: string }> = {
  1: { emoji: '🏛', name: 'Basics', slug: 'basics' },
  2: { emoji: '🔨', name: 'Functional', slug: 'functional' },
  3: { emoji: '🌹', name: 'Aesthetic', slug: 'aesthetic' },
  4: { emoji: '🪐', name: 'Challenge', slug: 'challenge' },
  5: { emoji: '⌛', name: 'Time', slug: 'time' },
  6: { emoji: '🐬', name: 'Partner', slug: 'partner' },
};

const TYPES: Record<number, { emoji: string; name: string; slug: string }> = {
  1: { emoji: '🛒', name: 'Push', slug: 'push' },
  2: { emoji: '🪡', name: 'Pull', slug: 'pull' },
  3: { emoji: '🍗', name: 'Legs', slug: 'legs' },
  4: { emoji: '➕', name: 'Plus', slug: 'plus' },
  5: { emoji: '➖', name: 'Ultra', slug: 'ultra' },
};

const COLORS: Record<number, { emoji: string; name: string; slug: string }> = {
  1: { emoji: '⚫', name: 'Teaching', slug: 'teaching' },
  2: { emoji: '🟢', name: 'Bodyweight', slug: 'bodyweight' },
  3: { emoji: '🔵', name: 'Structured', slug: 'structured' },
  4: { emoji: '🟣', name: 'Technical', slug: 'technical' },
  5: { emoji: '🔴', name: 'Intense', slug: 'intense' },
  6: { emoji: '🟠', name: 'Circuit', slug: 'circuit' },
  7: { emoji: '🟡', name: 'Fun', slug: 'fun' },
  8: { emoji: '⚪', name: 'Mindful', slug: 'mindful' },
};

const ORDER_FOLDER: Record<number, string> = {
  1: '🐂-foundation', 2: '⛽-strength', 3: '🦋-hypertrophy',
  4: '🏟-performance', 5: '🌾-full-body', 6: '⚖-balance', 7: '🖼-restoration',
};
const AXIS_FOLDER: Record<number, string> = {
  1: '🏛-basics', 2: '🔨-functional', 3: '🌹-aesthetic',
  4: '🪐-challenge', 5: '⌛-time', 6: '🐬-partner',
};
const TYPE_FOLDER: Record<number, string> = {
  1: '🛒-push', 2: '🪡-pull', 3: '🍗-legs', 4: '➕-plus', 5: '➖-ultra',
};

const BLOCK_EMOJI_TO_SLUG: Record<string, string> = {
  '♨️': 'warm-up', '🎯': 'intention', '🔢': 'fundamentals', '🧈': 'bread-butter',
  '🫀': 'circulation', '▶️': 'primer', '🎼': 'composition', '♟️': 'gambit',
  '🪜': 'progression', '🌎': 'exposure', '🎱': 'aram', '🌋': 'gutter',
  '🪞': 'vanity', '🗿': 'sculpt', '🛠': 'craft', '🧩': 'supplemental',
  '🪫': 'release', '🏖': 'sandbox', '🏗': 'reformance', '🧬': 'imprint',
  '🚂': 'junction', '🔠': 'choice', '🧮': 'save',
};

const BLOCK_ROLES: Record<string, BlockData['role']> = {
  'warm-up': 'orientation', 'intention': 'orientation',
  'fundamentals': 'access', 'circulation': 'access', 'primer': 'access',
  'gambit': 'access', 'progression': 'access',
  'bread-butter': 'transformation', 'composition': 'transformation',
  'exposure': 'transformation', 'aram': 'transformation', 'gutter': 'transformation',
  'vanity': 'transformation', 'sculpt': 'transformation', 'craft': 'transformation',
  'supplemental': 'transformation', 'sandbox': 'transformation', 'reformance': 'transformation',
  'release': 'retention', 'imprint': 'retention', 'junction': 'retention', 'save': 'retention',
  'choice': 'modifier',
};

// ─── Card file finder ──────────────────────────────────────────────────────

const CARDS_ROOT = path.resolve(process.cwd(), '..', 'cards');

function findCardFile(numericZip: string): string | null {
  const o = parseInt(numericZip[0]!);
  const a = parseInt(numericZip[1]!);
  const t = parseInt(numericZip[2]!);

  const orderDir = ORDER_FOLDER[o];
  const axisDir = AXIS_FOLDER[a];
  const typeDir = TYPE_FOLDER[t];
  if (!orderDir || !axisDir || !typeDir) return null;

  const dir = path.join(CARDS_ROOT, orderDir, axisDir, typeDir);
  if (!fs.existsSync(dir)) return null;

  // Build the emoji zip prefix to match filenames
  const order = ORDERS[o];
  const axis = AXES[a];
  const type = TYPES[t];
  const color = COLORS[parseInt(numericZip[3]!)];
  if (!order || !axis || !type || !color) return null;

  const emojiPrefix = `${order.emoji}${axis.emoji}${type.emoji}${color.emoji}`;

  const files = fs.readdirSync(dir);
  const match = files.find(f => f.startsWith(emojiPrefix) && f.endsWith('.md'));
  return match ? path.join(dir, match) : null;
}

// ─── Card parser (server-side, uses fs) ────────────────────────────────────

function parseBlockHeader(headerLine: string): { emoji: string; name: string } {
  const cleaned = headerLine.replace(/^#+\s*/, '').replace(/^\d+\)\s*/, '').trim();
  const emojiMatch = /^(\p{Emoji_Presentation}|\p{Extended_Pictographic})\s*/u.exec(cleaned);
  if (emojiMatch) {
    const emoji = emojiMatch[1] ?? '';
    const name = cleaned.slice(emojiMatch[0].length).trim();
    return { emoji, name: name || 'Block' };
  }
  return { emoji: '▪️', name: cleaned || 'Block' };
}

function escapeHtml(str: string): string {
  return str
    .replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function markdownToHtml(md: string): string {
  // Lightweight markdown → HTML (no external dep needed for blocks)
  let html = md
    .replace(/^├─\s*(.+)$/gm, '<div class="ppl-exercise-line">$1</div>')
    .replace(/^│\s\s(.+)$/gm, '<div class="ppl-set-line">$1</div>')
    .replace(/^Rest:\s*(.+)$/gm, '<div class="ppl-rest-line">Rest: $1</div>')
    .replace(/^\*\*(.+?)\*\*/gm, '<strong>$1</strong>')
    .replace(/^>\s*"(.+)"$/gm, '<blockquote>"$1"</blockquote>')
    .replace(/^\*(.+?)\*$/gm, '<em>$1</em>')
    .replace(/^- (.+)$/gm, '<li>$1</li>')
    .replace(/^Subcode:\s*(.+)$/gm, '<div class="ppl-subcode">$1</div>');

  // Wrap consecutive <li> in <ul>
  html = html.replace(/(<li>.+<\/li>\n?)+/g, (match) => `<ul>${match}</ul>`);

  // Wrap remaining plain lines in <p>
  html = html.split('\n').map(line => {
    const trimmed = line.trim();
    if (!trimmed) return '';
    if (trimmed.startsWith('<')) return line;
    return `<p>${trimmed}</p>`;
  }).join('\n');

  return html;
}

async function parseCard(filePath: string, numericZip: string): Promise<CardData> {
  const raw = fs.readFileSync(filePath, 'utf-8');

  // Parse frontmatter manually (avoid gray-matter import issues in Vite middleware)
  const fmMatch = /^---\n([\s\S]*?)\n---\n([\s\S]*)$/.exec(raw);
  const fmBlock = fmMatch?.[1] ?? '';
  const content = fmMatch?.[2] ?? raw;

  // Extract frontmatter fields
  const fm: Record<string, string> = {};
  for (const line of fmBlock.split('\n')) {
    const colonIdx = line.indexOf(':');
    if (colonIdx > 0) {
      const key = line.slice(0, colonIdx).trim();
      const value = line.slice(colonIdx + 1).trim();
      fm[key] = value;
    }
  }

  const o = parseInt(numericZip[0]!);
  const a = parseInt(numericZip[1]!);
  const t = parseInt(numericZip[2]!);
  const c = parseInt(numericZip[3]!);

  const order = ORDERS[o]!;
  const axis = AXES[a]!;
  const type = TYPES[t]!;
  const color = COLORS[c]!;

  // Resolve weight vector → CSS vars (dynamic import from compiled source)
  let cssVars: Record<string, string> = {};
  try {
    const { resolveZip } = await import('../src/weights/resolver.js');
    const { weightsToCSSVars } = await import('../src/rendering/weights-to-css-vars.js');
    const { tokens } = await import('../src/tokens/tokens.js');
    const vector = resolveZip(o, a, t, c);
    cssVars = weightsToCSSVars(vector, tokens);
  } catch (e) {
    console.warn('Could not resolve CSS vars:', e);
  }

  // Extract title from filename
  const filename = path.basename(filePath, '.md');
  const titleMatch = /±\S+\s+(.+)$/.exec(filename);
  const title = titleMatch?.[1] ?? filename;

  // Parse blocks by splitting on ═══
  const sections = content.split('═══');
  const blocks: BlockData[] = [];
  let blockNumber = 0;

  for (const section of sections) {
    const trimmed = section.trim();
    if (!trimmed) continue;

    // Find the first heading line
    const headingMatch = /^##\s*(?:\d+\)\s*)?(.+)$/m.exec(trimmed);
    if (!headingMatch) continue;

    blockNumber++;
    const headerText = headingMatch[1]!.trim();
    const { emoji, name } = parseBlockHeader(headerText);
    const slug = BLOCK_EMOJI_TO_SLUG[emoji] ?? name.toLowerCase().replace(/[^a-z0-9]+/g, '-');
    const role = BLOCK_ROLES[slug] ?? 'transformation';

    // Get body content after heading
    const headingIdx = trimmed.indexOf(headingMatch[0]);
    const bodyStart = headingIdx + headingMatch[0].length;
    const body = trimmed.slice(bodyStart).trim();
    const contentHtml = markdownToHtml(body);

    blocks.push({ number: blockNumber, emoji, name, content: body, contentHtml, slug, role });
  }

  // Extract intention
  const intentionMatch = />\s*"([^"]+)"/.exec(content);
  const intention = intentionMatch?.[1] ?? '';

  // Build subtitle from frontmatter
  const orderLine = fm['order'] ?? '';
  const typeLine = fm['type'] ?? '';
  const colorLine = fm['color'] ?? '';

  return {
    zip: fm['zip'] ?? `${order.emoji}${axis.emoji}${type.emoji}${color.emoji}`,
    numericZip,
    operator: fm['operator'] ?? '',
    title,
    subtitle: `${order.name} · ${type.name} · ${color.name} · ~50 min`,
    intention,
    typeEmoji: type.emoji,
    blocks,
    cssVars,
    colorSlug: color.slug,
    orderSlug: order.slug,
    axisSlug: axis.slug,
  };
}

// ─── Card index (list all available cards) ─────────────────────────────────

interface CardIndexEntry {
  numericZip: string;
  emojiZip: string;
  title: string;
  order: string;
  axis: string;
  type: string;
  color: string;
  status: string;
}

function buildCardIndex(): CardIndexEntry[] {
  const entries: CardIndexEntry[] = [];

  for (const [oStr, orderFolder] of Object.entries(ORDER_FOLDER)) {
    const o = parseInt(oStr);
    const orderDir = path.join(CARDS_ROOT, orderFolder);
    if (!fs.existsSync(orderDir)) continue;

    for (const [aStr, axisFolder] of Object.entries(AXIS_FOLDER)) {
      const a = parseInt(aStr);
      const axisDir = path.join(orderDir, axisFolder);
      if (!fs.existsSync(axisDir)) continue;

      for (const [tStr, typeFolder] of Object.entries(TYPE_FOLDER)) {
        const t = parseInt(tStr);
        const typeDir = path.join(axisDir, typeFolder);
        if (!fs.existsSync(typeDir)) continue;

        const files = fs.readdirSync(typeDir).filter(f => f.endsWith('.md'));
        for (const file of files) {
          // Determine which color this file is
          for (let c = 1; c <= 8; c++) {
            const color = COLORS[c]!;
            const order = ORDERS[o]!;
            const axis = AXES[a]!;
            const type = TYPES[t]!;
            const prefix = `${order.emoji}${axis.emoji}${type.emoji}${color.emoji}`;
            if (file.startsWith(prefix)) {
              const numericZip = `${o}${a}${t}${c}`;
              const titleMatch = /±\S+\s+(.+)\.md$/.exec(file);
              const title = titleMatch?.[1] ?? file;
              const isGenerated = file.includes('±') && !file.endsWith('±.md');
              entries.push({
                numericZip,
                emojiZip: prefix,
                title,
                order: order.name,
                axis: axis.name,
                type: type.name,
                color: color.name,
                status: isGenerated ? 'GENERATED' : 'EMPTY',
              });
              break;
            }
          }
        }
      }
    }
  }

  return entries.sort((a, b) => a.numericZip.localeCompare(b.numericZip));
}

// ─── Vite middleware ───────────────────────────────────────────────────────

export function cardApiMiddleware(): Connect.NextHandleFunction {
  let cardIndex: CardIndexEntry[] | null = null;

  return async (req, res, next) => {
    const url = req.url ?? '';

    // GET /api/cards — list all available cards
    if (url === '/api/cards') {
      if (!cardIndex) cardIndex = buildCardIndex();
      res.setHeader('Content-Type', 'application/json');
      res.end(JSON.stringify(cardIndex));
      return;
    }

    // GET /api/card/2123 — get a specific card
    const cardMatch = /^\/api\/card\/(\d{4})$/.exec(url);
    if (cardMatch) {
      const numericZip = cardMatch[1]!;
      const filePath = findCardFile(numericZip);

      if (!filePath) {
        res.statusCode = 404;
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify({ error: `No card file found for zip ${numericZip}` }));
        return;
      }

      try {
        const cardData = await parseCard(filePath, numericZip);
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify(cardData));
      } catch (e) {
        res.statusCode = 500;
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify({ error: String(e) }));
      }
      return;
    }

    next();
  };
}
