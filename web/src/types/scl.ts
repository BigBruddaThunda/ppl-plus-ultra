// SCL Type Definitions — mirrors the 61-emoji system

export type Order = "foundation" | "strength" | "hypertrophy" | "performance" | "full-body" | "balance" | "restoration";
export type Axis = "basics" | "functional" | "aesthetic" | "challenge" | "time" | "partner";
export type Type = "push" | "pull" | "legs" | "plus" | "ultra";
export type Color = "teaching" | "bodyweight" | "structured" | "technical" | "intense" | "circuit" | "fun" | "mindful";

export type OrderEmoji = "🐂" | "⛽" | "🦋" | "🏟" | "🌾" | "⚖" | "🖼";
export type AxisEmoji = "🏛" | "🔨" | "🌹" | "🪐" | "⌛" | "🐬";
export type TypeEmoji = "🛒" | "🪡" | "🍗" | "➕" | "➖";
export type ColorEmoji = "⚫" | "🟢" | "🔵" | "🟣" | "🔴" | "🟠" | "🟡" | "⚪";

export interface ZipCode {
  raw: string;          // e.g. "⛽🏛🪡🔵"
  order: Order;
  axis: Axis;
  type: Type;
  color: Color;
  orderEmoji: OrderEmoji;
  axisEmoji: AxisEmoji;
  typeEmoji: TypeEmoji;
  colorEmoji: ColorEmoji;
  deck: number;         // 1–42
  numeric: string;      // 4-digit numeric code for URL routing
}

export interface CardFrontmatter {
  zip: string;
  operator: string;
  status: "EMPTY" | "GENERATED" | "CANONICAL";
  deck: number;
  order: string;
  axis: string;
  type: string;
  color: string;
  blocks: string;
}

export interface WorkoutCard {
  frontmatter: CardFrontmatter;
  content: string;
  zipCode: ZipCode;
}

export type Polarity = "preparatory" | "expressive";

export interface OperatorDef {
  emoji: string;
  latin: string;
  meaning: string;
}
