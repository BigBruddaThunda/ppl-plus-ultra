/**
 * dev-app.ts — Browser entry point for the Ppl± live card renderer.
 *
 * Wires the input bar → pipeline → card render loop.
 * Runs in Vite dev server (npm run dev).
 *
 * Pipeline: input → scoreText()/parseZip() → resolveZip() → weightsToCSSVars() → renderWorkoutCard()
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

// ─── Operator derivation (simplified — Axis × Color polarity) ──────────────

const OPERATOR_TABLE: Record<string, Record<string, string>> = {
  // axis slug → { preparatory: op, expressive: op }
  basics:     { preparatory: '📍 pono',   expressive: '🤌 facio' },
  functional: { preparatory: '🧸 fero',   expressive: '🥨 tendo' },
  aesthetic:  { preparatory: '👀 specio',  expressive: '🦢 plico' },
  challenge:  { preparatory: '🪵 teneo',   expressive: '🚀 mitto' },
  time:       { preparatory: '🐋 duco',    expressive: '✒️ grapho' },
  partner:    { preparatory: '🧲 capio',   expressive: '🦉 logos' },
};

const PREPARATORY_COLORS = new Set(['teaching', 'bodyweight', 'mindful', 'fun']);

function deriveOperator(axisSlug: string, colorSlug: string): string {
  const row = OPERATOR_TABLE[axisSlug];
  if (!row) return '🤌 facio';
  const polarity = PREPARATORY_COLORS.has(colorSlug) ? 'preparatory' : 'expressive';
  return row[polarity] ?? '🤌 facio';
}

// ─── Build CardData from dial positions ────────────────────────────────────

function buildCardData(orderPos: number, axisPos: number, typePos: number, colorPos: number): CardData {
  const order = ORDER_MAP[orderPos] ?? ORDER_MAP[2]!;
  const axis = AXIS_MAP[axisPos] ?? AXIS_MAP[1]!;
  const type = TYPE_MAP[typePos] ?? TYPE_MAP[1]!;
  const color = COLOR_MAP[colorPos] ?? COLOR_MAP[3]!;

  const zip = `${order.emoji}${axis.emoji}${type.emoji}${color.emoji}`;
  const numericZip = `${orderPos}${axisPos}${typePos}${colorPos}`;
  const operator = deriveOperator(axis.slug, color.slug);

  // Resolve weight vector and derive CSS vars
  const vector = resolveZip(orderPos, axisPos, typePos, colorPos);
  const cssVars = weightsToCSSVars(vector, tokens);

  // Build demo blocks to show the template
  const blocks: BlockData[] = [
    {
      number: 1, emoji: '♨️', name: 'WARM-UP', slug: 'warm-up', role: 'orientation',
      content: '', contentHtml: `<p>General warm-up: 5 min light cardio → dynamic stretching → movement-specific prep.</p>`
    },
    {
      number: 2, emoji: '🎯', name: 'INTENTION', slug: 'intention', role: 'orientation',
      content: '', contentHtml: `<blockquote>"${order.name} ${type.name} work through the ${axis.name} lens, formatted ${color.name}."</blockquote>`
    },
    {
      number: 3, emoji: '🧈', name: 'BREAD & BUTTER', slug: 'bread-butter', role: 'transformation',
      content: '', contentHtml: `
        <p><strong>${type.emoji} Primary Movement</strong></p>
        <p>Set 1: ${order.emoji} Working weight × target reps</p>
        <p>Set 2: ${order.emoji} Working weight × target reps</p>
        <p>Set 3: ${order.emoji} Working weight × target reps</p>
        <p class="ppl-cue">(${axis.slug === 'basics' ? 'classic form, proven movement' : axis.slug === 'functional' ? 'stand tall, athletic stance' : axis.slug === 'aesthetic' ? 'feel the contraction, full ROM' : 'controlled execution'})</p>
      `
    },
    {
      number: 4, emoji: '🧩', name: 'SUPPLEMENTAL', slug: 'supplemental', role: 'transformation',
      content: '', contentHtml: `
        <p><strong>${type.emoji} Secondary Movement</strong></p>
        <p>3 sets × target reps</p>
        <p class="ppl-cue">(different angle from the primary)</p>
      `
    },
    {
      number: 5, emoji: '🚂', name: 'JUNCTION', slug: 'junction', role: 'retention',
      content: '', contentHtml: `
        <p><strong>Next session bridges:</strong></p>
        <p>Next → ${order.emoji}${axis.emoji}${TYPE_MAP[((typePos % 5) + 1)]?.emoji ?? '🛒'}${color.emoji} — rotate the Type dial</p>
      `
    },
    {
      number: 6, emoji: '🧮', name: 'SAVE', slug: 'save', role: 'retention',
      content: '', contentHtml: `<p>Session logged. The work speaks for itself.</p>`
    },
  ];

  return {
    zip,
    numericZip,
    operator,
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

// ─── Render ────────────────────────────────────────────────────────────────

function renderCard(parsed: ParsedInput): void {
  const { orderPos, axisPos, typePos, colorPos } = parsed;

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

  // Build and render card
  const cardData = buildCardData(orderPos, axisPos, typePos, colorPos);
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
