/**
 * dev-app.ts — Browser entry point for the Ppl± live card renderer.
 *
 * Wires the input bar → pipeline → card render loop.
 * Runs in Vite dev server (npm run dev).
 *
 * Two render paths:
 *   1. Real card: fetches /api/card/:zip → renders actual .md workout content
 *   2. Demo card: falls back to generated demo blocks when no .md file exists
 */

import { ORDERS, AXES, TYPES, COLORS } from './types/scl.js';
import { resolveZip } from './weights/resolver.js';
import { weightsToCSSVars } from './rendering/weights-to-css-vars.js';
import { tokens } from './tokens/tokens.js';
import { scoreText } from './parser/scorer.js';
import { renderWorkoutCard } from '../components/WorkoutCard.js';
import type { CardData, BlockData } from '../components/types.js';

// ─── DOM refs ──────────────────────────────────────────────────────────────

const input = document.getElementById('zip-input') as HTMLInputElement;
const parseBar = document.getElementById('parse-bar') as HTMLDivElement;
const parseZipEl = document.getElementById('parse-zip') as HTMLSpanElement;
const parseLabelEl = document.getElementById('parse-label') as HTMLSpanElement;
const parseConfidenceEl = document.getElementById('parse-confidence') as HTMLSpanElement;
const parseDefaultedEl = document.getElementById('parse-defaulted') as HTMLSpanElement;
const cardContainer = document.getElementById('card-container') as HTMLDivElement;

// ─── Lookup helpers ────────────────────────────────────────────────────────

const ORDER_MAP = ORDERS as Record<number, { emoji: string; name: string; slug: string }>;
const AXIS_MAP = AXES as Record<number, { emoji: string; name: string; slug: string }>;
const TYPE_MAP = TYPES as Record<number, { emoji: string; name: string; slug: string }>;
const COLOR_MAP = COLORS as Record<number, { emoji: string; name: string; slug: string }>;

// ─── Parse input ───────────────────────────────────────────────────────────

interface ParsedInput {
  orderPos: number;
  axisPos: number;
  typePos: number;
  colorPos: number;
  confidence: number;
  defaultedDimensions: string[];
  method: 'numeric' | 'natural-language';
}

function parseInput(raw: string): ParsedInput | null {
  const trimmed = raw.trim();
  if (!trimmed) return null;

  // Try numeric zip first (4 digits)
  const numericMatch = /^(\d)(\d)(\d)(\d)$/.exec(trimmed);
  if (numericMatch) {
    const o = parseInt(numericMatch[1]!);
    const a = parseInt(numericMatch[2]!);
    const t = parseInt(numericMatch[3]!);
    const c = parseInt(numericMatch[4]!);
    if (o >= 1 && o <= 7 && a >= 1 && a <= 6 && t >= 1 && t <= 5 && c >= 1 && c <= 8) {
      return { orderPos: o, axisPos: a, typePos: t, colorPos: c, confidence: 1.0, defaultedDimensions: [], method: 'numeric' };
    }
  }

  // Try emoji zip (4 emoji characters)
  const chars = [...trimmed];
  if (chars.length === 4) {
    const orderEntry = Object.entries(ORDER_MAP).find(([, v]) => v.emoji === chars[0]);
    const axisEntry = Object.entries(AXIS_MAP).find(([, v]) => v.emoji === chars[1]);
    const typeEntry = Object.entries(TYPE_MAP).find(([, v]) => v.emoji === chars[2]);
    const colorEntry = Object.entries(COLOR_MAP).find(([, v]) => v.emoji === chars[3]);
    if (orderEntry && axisEntry && typeEntry && colorEntry) {
      return {
        orderPos: parseInt(orderEntry[0]), axisPos: parseInt(axisEntry[0]),
        typePos: parseInt(typeEntry[0]), colorPos: parseInt(colorEntry[0]),
        confidence: 1.0, defaultedDimensions: [], method: 'numeric'
      };
    }
  }

  // Natural language → scoreText()
  const results = scoreText(trimmed);
  if (results.length === 0) return null;

  const top = results[0]!;
  return {
    orderPos: top.orderPos,
    axisPos: top.axisPos,
    typePos: top.typePos,
    colorPos: top.colorPos,
    confidence: top.confidence,
    defaultedDimensions: top.defaulted_dimensions,
    method: 'natural-language',
  };
}

// ─── Build demo CardData (fallback when no .md file exists) ────────────────

function buildDemoCard(orderPos: number, axisPos: number, typePos: number, colorPos: number): CardData {
  const order = ORDER_MAP[orderPos] ?? ORDER_MAP[2]!;
  const axis = AXIS_MAP[axisPos] ?? AXIS_MAP[1]!;
  const type = TYPE_MAP[typePos] ?? TYPE_MAP[1]!;
  const color = COLOR_MAP[colorPos] ?? COLOR_MAP[3]!;

  const vector = resolveZip(orderPos, axisPos, typePos, colorPos);
  const cssVars = weightsToCSSVars(vector, tokens);

  const blocks: BlockData[] = [
    { number: 1, emoji: '♨️', name: 'WARM-UP', slug: 'warm-up', role: 'orientation',
      content: '', contentHtml: `<p>General warm-up: 5 min light cardio → dynamic stretching → movement-specific prep.</p>` },
    { number: 2, emoji: '🎯', name: 'INTENTION', slug: 'intention', role: 'orientation',
      content: '', contentHtml: `<blockquote>"${order.name} ${type.name.toLowerCase()} work through the ${axis.name.toLowerCase()} lens."</blockquote>` },
    { number: 3, emoji: '🧈', name: 'BREAD & BUTTER', slug: 'bread-butter', role: 'transformation',
      content: '', contentHtml: `
        <div class="ppl-exercise-line"><strong>${type.emoji} Primary Movement</strong></div>
        <div class="ppl-set-line">Set 1: ${order.emoji} Working weight × target reps</div>
        <div class="ppl-set-line">Set 2: ${order.emoji} Working weight × target reps</div>
        <div class="ppl-set-line">Set 3: ${order.emoji} Working weight × target reps</div>
        <div class="ppl-rest-line">Rest: 120s</div>` },
    { number: 4, emoji: '🧩', name: 'SUPPLEMENTAL', slug: 'supplemental', role: 'transformation',
      content: '', contentHtml: `
        <div class="ppl-exercise-line"><strong>${type.emoji} Secondary Movement</strong></div>
        <div class="ppl-set-line">3 sets × target reps</div>
        <div class="ppl-rest-line">Rest: 90s</div>` },
    { number: 5, emoji: '🚂', name: 'JUNCTION', slug: 'junction', role: 'retention',
      content: '', contentHtml: `<p>Next → rotate the Type dial</p>` },
    { number: 6, emoji: '🧮', name: 'SAVE', slug: 'save', role: 'retention',
      content: '', contentHtml: `<p>Session logged. The work speaks for itself.</p>` },
  ];

  return {
    zip: `${order.emoji}${axis.emoji}${type.emoji}${color.emoji}`,
    numericZip: `${orderPos}${axisPos}${typePos}${colorPos}`,
    operator: `${order.name} ${axis.name}`,
    title: `${order.name} ${type.name} — ${axis.name} ${color.name}`,
    subtitle: `${order.name} · ${type.name} · ${axis.name} · ${color.name} · ~45 min`,
    intention: `${order.name} ${type.name.toLowerCase()} work through the ${axis.name.toLowerCase()} lens.`,
    typeEmoji: type.emoji,
    blocks,
    cssVars,
    colorSlug: color.slug,
    orderSlug: order.slug,
    axisSlug: axis.slug,
  };
}

// ─── Render ────────────────────────────────────────────────────────────────

async function renderCard(parsed: ParsedInput): Promise<void> {
  const { orderPos, axisPos, typePos, colorPos } = parsed;
  const numericZip = `${orderPos}${axisPos}${typePos}${colorPos}`;

  const order = ORDER_MAP[orderPos] ?? ORDER_MAP[2]!;
  const axis = AXIS_MAP[axisPos] ?? AXIS_MAP[1]!;
  const type = TYPE_MAP[typePos] ?? TYPE_MAP[1]!;
  const color = COLOR_MAP[colorPos] ?? COLOR_MAP[3]!;

  // Update parse bar
  parseBar.style.display = 'flex';
  parseZipEl.textContent = `${order.emoji}${axis.emoji}${type.emoji}${color.emoji}`;
  parseLabelEl.textContent = `${order.name} · ${axis.name} · ${type.name} · ${color.name}`;
  parseConfidenceEl.textContent = parsed.method === 'numeric'
    ? 'exact match'
    : `confidence: ${(parsed.confidence * 100).toFixed(0)}%`;
  parseDefaultedEl.textContent = parsed.defaultedDimensions.length > 0
    ? `defaulted: ${parsed.defaultedDimensions.join(', ')}`
    : '';

  // Try to fetch the real card from the API
  let cardData: CardData;
  try {
    const resp = await fetch(`/api/card/${numericZip}`);
    if (resp.ok) {
      cardData = await resp.json();
      // The API returns cssVars from the server — use them directly
      parseLabelEl.textContent += ' — real card';
    } else {
      // No .md file exists — use demo card
      cardData = buildDemoCard(orderPos, axisPos, typePos, colorPos);
      parseLabelEl.textContent += ' — demo';
    }
  } catch {
    cardData = buildDemoCard(orderPos, axisPos, typePos, colorPos);
    parseLabelEl.textContent += ' — demo';
  }

  const html = renderWorkoutCard(cardData);
  cardContainer.innerHTML = html;
}

// ─── Event listeners ───────────────────────────────────────────────────────

input.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    const parsed = parseInput(input.value);
    if (parsed) {
      renderCard(parsed);
    }
  }
});

// Clickable examples
document.querySelectorAll('.ppl-empty-state__example').forEach((el) => {
  el.addEventListener('click', () => {
    const value = (el as HTMLElement).dataset.input ?? '';
    input.value = value;
    const parsed = parseInput(value);
    if (parsed) {
      renderCard(parsed);
    }
  });
});
