// Rotation Engine — deterministic date-to-zip formula
// Source: middle-math/rotation/rotation-engine-spec.md
// Three gears: Order by weekday, Type by rolling 5-day, Axis by month

import type { Order, Axis, Type, Color } from "@/types/scl";
import { ORDER_EMOJI, AXIS_EMOJI, TYPE_EMOJI, COLOR_EMOJI, toNumericCode, getDeckNumber } from "./scl";
import type { ZipCode } from "@/types/scl";

// ── Gear 1: Order by Day of Week ──
// Monday = 0 (JS getDay: Sun=0, Mon=1, so we remap)

const WEEKDAY_ORDERS: Order[] = [
  "restoration",   // Sunday (getDay=0)
  "foundation",    // Monday
  "strength",      // Tuesday
  "hypertrophy",   // Wednesday
  "performance",   // Thursday
  "full-body",     // Friday
  "balance",       // Saturday
];

export function getOrderForDate(date: Date): Order {
  return WEEKDAY_ORDERS[date.getDay()];
}

// ── Gear 2: Type by Rolling 5-Day from Jan 1 ──

const TYPE_CYCLE: Type[] = ["push", "pull", "legs", "plus", "ultra"];

export function getTypeForDate(date: Date): Type {
  const jan1 = new Date(date.getFullYear(), 0, 1);
  const diffMs = date.getTime() - jan1.getTime();
  const dayOfYear = Math.floor(diffMs / (1000 * 60 * 60 * 24));
  return TYPE_CYCLE[dayOfYear % 5];
}

// ── Gear 3: Axis by Month ──

const MONTHLY_AXES: Axis[] = [
  "basics",      // January
  "partner",     // February
  "functional",  // March
  "aesthetic",    // April
  "challenge",   // May
  "time",        // June
  "basics",      // July
  "partner",     // August
  "aesthetic",    // September
  "challenge",   // October
  "time",        // November
  "functional",  // December
];

const MONTHLY_OPERATORS: { emoji: string; latin: string }[] = [
  { emoji: "📍", latin: "pono" },      // January
  { emoji: "🧲", latin: "capio" },     // February
  { emoji: "🧸", latin: "fero" },      // March
  { emoji: "👀", latin: "specio" },    // April
  { emoji: "🥨", latin: "tendo" },     // May
  { emoji: "✒️", latin: "grapho" },    // June
  { emoji: "🤌", latin: "facio" },     // July
  { emoji: "🦉", latin: "logos" },     // August
  { emoji: "🦢", latin: "plico" },     // September
  { emoji: "🪵", latin: "teneo" },     // October
  { emoji: "🐋", latin: "duco" },      // November
  { emoji: "🚀", latin: "mitto" },     // December
];

export function getAxisForDate(date: Date): Axis {
  return MONTHLY_AXES[date.getMonth()];
}

export function getMonthlyOperator(date: Date): { emoji: string; latin: string } {
  return MONTHLY_OPERATORS[date.getMonth()];
}

// ── Default Color ──
// Color is user-selected. Default to structured (🔵) for display purposes.

export function getDefaultColor(): Color {
  return "structured";
}

// ── Combined: Daily Zip ──

export interface DailyZip {
  order: Order;
  axis: Axis;
  type: Type;
  color: Color;
  numeric: string;
  emoji: string;
  deck: number;
  orderEmoji: string;
  axisEmoji: string;
  typeEmoji: string;
  colorEmoji: string;
}

export function getDailyZip(date: Date, color?: Color): DailyZip {
  const order = getOrderForDate(date);
  const axis = getAxisForDate(date);
  const type = getTypeForDate(date);
  const c = color ?? getDefaultColor();

  const orderEmoji = ORDER_EMOJI[order];
  const axisEmoji = AXIS_EMOJI[axis];
  const typeEmoji = TYPE_EMOJI[type];
  const colorEmoji = COLOR_EMOJI[c];

  return {
    order,
    axis,
    type,
    color: c,
    numeric: toNumericCode(order, axis, type, c),
    emoji: `${orderEmoji}${axisEmoji}${typeEmoji}${colorEmoji}`,
    deck: getDeckNumber(order, axis),
    orderEmoji,
    axisEmoji,
    typeEmoji,
    colorEmoji,
  };
}

// ── Week Schedule ──

export interface WeekDay {
  date: Date;
  dayName: string;
  zip: DailyZip;
  isToday: boolean;
}

const DAY_NAMES = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

export function getWeekSchedule(date: Date): WeekDay[] {
  // Find Monday of this week
  const day = date.getDay();
  const mondayOffset = day === 0 ? -6 : 1 - day;
  const monday = new Date(date.getFullYear(), date.getMonth(), date.getDate() + mondayOffset);

  const today = new Date(date.getFullYear(), date.getMonth(), date.getDate());

  return Array.from({ length: 7 }, (_, i) => {
    const d = new Date(monday.getFullYear(), monday.getMonth(), monday.getDate() + i);
    return {
      date: d,
      dayName: DAY_NAMES[d.getDay()],
      zip: getDailyZip(d),
      isToday: d.getTime() === today.getTime(),
    };
  });
}

// ── Human-readable labels ──

const ORDER_NAMES: Record<Order, string> = {
  foundation: "Foundation", strength: "Strength", hypertrophy: "Hypertrophy",
  performance: "Performance", "full-body": "Full Body", balance: "Balance",
  restoration: "Restoration",
};

const AXIS_NAMES: Record<Axis, string> = {
  basics: "Basics", functional: "Functional", aesthetic: "Aesthetic",
  challenge: "Challenge", time: "Time", partner: "Partner",
};

const TYPE_NAMES: Record<Type, string> = {
  push: "Push", pull: "Pull", legs: "Legs", plus: "Plus", ultra: "Ultra",
};

const MONTH_NAMES = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December",
];

export function getOrderName(order: Order): string {
  return ORDER_NAMES[order];
}

export function getAxisName(axis: Axis): string {
  return AXIS_NAMES[axis];
}

export function getTypeName(type: Type): string {
  return TYPE_NAMES[type];
}

export function getMonthName(date: Date): string {
  return MONTH_NAMES[date.getMonth()];
}

export function formatDate(date: Date): string {
  return date.toISOString().split("T")[0];
}
