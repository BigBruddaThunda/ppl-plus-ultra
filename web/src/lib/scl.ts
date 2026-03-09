// SCL — Semantic Compression Language parser and lookup tables
// Maps the 61 emojis to their structured data

import type {
  Order, Axis, Type, Color,
  OrderEmoji, AxisEmoji, TypeEmoji, ColorEmoji,
  ZipCode, Polarity, OperatorDef,
} from "@/types/scl";

// ── Emoji → Key mappings ──

export const ORDER_MAP: Record<OrderEmoji, Order> = {
  "🐂": "foundation",
  "⛽": "strength",
  "🦋": "hypertrophy",
  "🏟": "performance",
  "🌾": "full-body",
  "⚖": "balance",
  "🖼": "restoration",
};

export const AXIS_MAP: Record<AxisEmoji, Axis> = {
  "🏛": "basics",
  "🔨": "functional",
  "🌹": "aesthetic",
  "🪐": "challenge",
  "⌛": "time",
  "🐬": "partner",
};

export const TYPE_MAP: Record<TypeEmoji, Type> = {
  "🛒": "push",
  "🪡": "pull",
  "🍗": "legs",
  "➕": "plus",
  "➖": "ultra",
};

export const COLOR_MAP: Record<ColorEmoji, Color> = {
  "⚫": "teaching",
  "🟢": "bodyweight",
  "🔵": "structured",
  "🟣": "technical",
  "🔴": "intense",
  "🟠": "circuit",
  "🟡": "fun",
  "⚪": "mindful",
};

// Reverse maps for emoji lookup
export const ORDER_EMOJI: Record<Order, OrderEmoji> = Object.fromEntries(
  Object.entries(ORDER_MAP).map(([k, v]) => [v, k])
) as Record<Order, OrderEmoji>;

export const AXIS_EMOJI: Record<Axis, AxisEmoji> = Object.fromEntries(
  Object.entries(AXIS_MAP).map(([k, v]) => [v, k])
) as Record<Axis, AxisEmoji>;

export const TYPE_EMOJI: Record<Type, TypeEmoji> = Object.fromEntries(
  Object.entries(TYPE_MAP).map(([k, v]) => [v, k])
) as Record<Type, TypeEmoji>;

export const COLOR_EMOJI: Record<Color, ColorEmoji> = Object.fromEntries(
  Object.entries(COLOR_MAP).map(([k, v]) => [v, k])
) as Record<Color, ColorEmoji>;

// ── Polarity ──

const PREPARATORY_COLORS: Color[] = ["teaching", "bodyweight", "mindful", "fun"];
const EXPRESSIVE_COLORS: Color[] = ["structured", "technical", "intense", "circuit"];

export function getPolarity(color: Color): Polarity {
  return PREPARATORY_COLORS.includes(color) ? "preparatory" : "expressive";
}

// ── Operator table ──

const OPERATOR_TABLE: Record<Axis, { preparatory: OperatorDef; expressive: OperatorDef }> = {
  basics:     { preparatory: { emoji: "📍", latin: "pono", meaning: "place/position" },       expressive: { emoji: "🤌", latin: "facio", meaning: "execute/perform" } },
  functional: { preparatory: { emoji: "🧸", latin: "fero", meaning: "carry/transfer" },       expressive: { emoji: "🥨", latin: "tendo", meaning: "extend/push limits" } },
  aesthetic:  { preparatory: { emoji: "👀", latin: "specio", meaning: "inspect/observe" },     expressive: { emoji: "🦢", latin: "plico", meaning: "fold/superset/layer" } },
  challenge:  { preparatory: { emoji: "🪵", latin: "teneo", meaning: "hold/anchor/persist" }, expressive: { emoji: "🚀", latin: "mitto", meaning: "dispatch/deploy/launch" } },
  time:       { preparatory: { emoji: "🐋", latin: "duco", meaning: "orchestrate/conduct" },  expressive: { emoji: "✒️", latin: "grapho", meaning: "write/prescribe/document" } },
  partner:    { preparatory: { emoji: "🧲", latin: "capio", meaning: "receive/assess" },      expressive: { emoji: "🦉", latin: "logos", meaning: "reason/analyze/interpret" } },
};

export function getOperator(axis: Axis, color: Color): OperatorDef {
  const polarity = getPolarity(color);
  return OPERATOR_TABLE[axis][polarity];
}

// ── Deck number ──

const ORDER_INDEX: Order[] = ["foundation", "strength", "hypertrophy", "performance", "full-body", "balance", "restoration"];
const AXIS_INDEX: Axis[] = ["basics", "functional", "aesthetic", "challenge", "time", "partner"];

export function getDeckNumber(order: Order, axis: Axis): number {
  const row = ORDER_INDEX.indexOf(order);
  const col = AXIS_INDEX.indexOf(axis);
  return row * 6 + col + 1;
}

// ── Numeric zip code ──
// 4-digit code: [order 1-7][axis 1-6][type 1-5][color 1-8]

const TYPE_INDEX: Type[] = ["push", "pull", "legs", "plus", "ultra"];
const COLOR_INDEX: Color[] = ["teaching", "bodyweight", "structured", "technical", "intense", "circuit", "fun", "mindful"];

export function toNumericCode(order: Order, axis: Axis, type: Type, color: Color): string {
  const o = ORDER_INDEX.indexOf(order) + 1;
  const a = AXIS_INDEX.indexOf(axis) + 1;
  const t = TYPE_INDEX.indexOf(type) + 1;
  const c = COLOR_INDEX.indexOf(color) + 1;
  return `${o}${a}${t}${c}`;
}

export function fromNumericCode(code: string): { order: Order; axis: Axis; type: Type; color: Color } | null {
  if (!/^\d{4}$/.test(code)) return null;
  const o = parseInt(code[0]) - 1;
  const a = parseInt(code[1]) - 1;
  const t = parseInt(code[2]) - 1;
  const c = parseInt(code[3]) - 1;
  if (o < 0 || o > 6 || a < 0 || a > 5 || t < 0 || t > 4 || c < 0 || c > 7) return null;
  return {
    order: ORDER_INDEX[o],
    axis: AXIS_INDEX[a],
    type: TYPE_INDEX[t],
    color: COLOR_INDEX[c],
  };
}

// ── Full zip code parser ──

export function parseZipCode(raw: string): ZipCode | null {
  // Extract the 4 emojis from the raw string
  const emojis = [...raw].filter(c => c.length > 0);
  const segments: string[] = [];
  let current = "";

  for (const char of raw) {
    current += char;
    if (current in ORDER_MAP || current in AXIS_MAP || current in TYPE_MAP || current in COLOR_MAP) {
      segments.push(current);
      current = "";
    }
  }

  if (segments.length !== 4) return null;

  const orderEmoji = segments[0] as OrderEmoji;
  const axisEmoji = segments[1] as AxisEmoji;
  const typeEmoji = segments[2] as TypeEmoji;
  const colorEmoji = segments[3] as ColorEmoji;

  if (!(orderEmoji in ORDER_MAP)) return null;
  if (!(axisEmoji in AXIS_MAP)) return null;
  if (!(typeEmoji in TYPE_MAP)) return null;
  if (!(colorEmoji in COLOR_MAP)) return null;

  const order = ORDER_MAP[orderEmoji];
  const axis = AXIS_MAP[axisEmoji];
  const type = TYPE_MAP[typeEmoji];
  const color = COLOR_MAP[colorEmoji];

  return {
    raw,
    order,
    axis,
    type,
    color,
    orderEmoji,
    axisEmoji,
    typeEmoji,
    colorEmoji,
    deck: getDeckNumber(order, axis),
    numeric: toNumericCode(order, axis, type, color),
  };
}

// Parse from numeric code and return full ZipCode
export function parseNumericZip(code: string): ZipCode | null {
  const parsed = fromNumericCode(code);
  if (!parsed) return null;
  const { order, axis, type, color } = parsed;
  const raw = `${ORDER_EMOJI[order]}${AXIS_EMOJI[axis]}${TYPE_EMOJI[type]}${COLOR_EMOJI[color]}`;
  return {
    raw,
    order,
    axis,
    type,
    color,
    orderEmoji: ORDER_EMOJI[order],
    axisEmoji: AXIS_EMOJI[axis],
    typeEmoji: TYPE_EMOJI[type],
    colorEmoji: COLOR_EMOJI[color],
    deck: getDeckNumber(order, axis),
    numeric: code,
  };
}

// ── GOLD gate ──

export function isGoldAllowed(color: Color): boolean {
  return color === "intense" || color === "technical";
}

// ── Total zip count ──

export const TOTAL_ZIPS = 7 * 6 * 5 * 8; // 1,680
