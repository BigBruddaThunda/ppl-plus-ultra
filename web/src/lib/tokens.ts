// Design tokens — imported from middle-math/design-tokens.json
// Provides runtime access to color palettes and order typography

import type { Color, Order } from "@/types/scl";

export interface ColorTokens {
  emoji: string;
  scl_name: string;
  tonal_name: string;
  tier: string;
  gold: boolean;
  primary: string;
  secondary: string;
  background: string;
  surface: string;
  text: string;
  textOnLight: string;
  accent: string;
  border: string;
}

export interface OrderTokens {
  emoji: string;
  scl_name: string;
  load: string;
  cns: string;
  fontSizeBase: string;
  fontSizeDisplay: string;
  fontWeight: number;
  fontWeightDisplay: number;
  letterSpacing: string;
  lineHeight: number;
  density: string;
  restPeriod: string;
  uiNote: string;
}

export const COLOR_TOKENS: Record<Color, ColorTokens> = {
  teaching: {
    emoji: "⚫", scl_name: "Teaching", tonal_name: "Order",
    tier: "2-3", gold: false,
    primary: "#1A1A1A", secondary: "#2D2D2D", background: "#F8F8F8",
    surface: "#FFFFFF", text: "#F5F5F5", textOnLight: "#1A1A1A",
    accent: "#3D3D3D", border: "#E0E0E0",
  },
  bodyweight: {
    emoji: "🟢", scl_name: "Bodyweight", tonal_name: "Growth",
    tier: "0-2", gold: false,
    primary: "#3A7D44", secondary: "#4A9154", background: "#F0F7F1",
    surface: "#FFFFFF", text: "#1A3D1E", textOnLight: "#1A3D1E",
    accent: "#2A5C32", border: "#C5DEC8",
  },
  structured: {
    emoji: "🔵", scl_name: "Structured", tonal_name: "Planning",
    tier: "2-3", gold: false,
    primary: "#2E6BA6", secondary: "#3A7EC0", background: "#EDF4FB",
    surface: "#FFFFFF", text: "#143050", textOnLight: "#143050",
    accent: "#1E4F7D", border: "#B8D4EC",
  },
  technical: {
    emoji: "🟣", scl_name: "Technical", tonal_name: "Magnificence",
    tier: "2-5", gold: true,
    primary: "#7B4FA2", secondary: "#8E62B2", background: "#F3EEF8",
    surface: "#FFFFFF", text: "#3A1F50", textOnLight: "#3A1F50",
    accent: "#5E3C7D", border: "#D5C2E8",
  },
  intense: {
    emoji: "🔴", scl_name: "Intense", tonal_name: "Passion",
    tier: "2-4", gold: true,
    primary: "#C0392B", secondary: "#D44433", background: "#FDF0EE",
    surface: "#FFFFFF", text: "#5C1A13", textOnLight: "#5C1A13",
    accent: "#962D22", border: "#F0BCBA",
  },
  circuit: {
    emoji: "🟠", scl_name: "Circuit", tonal_name: "Connection",
    tier: "0-3", gold: false,
    primary: "#E07A3A", secondary: "#E88B50", background: "#FDF5EE",
    surface: "#FFFFFF", text: "#6B3418", textOnLight: "#6B3418",
    accent: "#C4612A", border: "#F0CEAD",
  },
  fun: {
    emoji: "🟡", scl_name: "Fun", tonal_name: "Play",
    tier: "0-5", gold: false,
    primary: "#F2C744", secondary: "#F5D060", background: "#FDFBEE",
    surface: "#FFFFFF", text: "#5C4A12", textOnLight: "#5C4A12",
    accent: "#D4A830", border: "#F0E3B0",
  },
  mindful: {
    emoji: "⚪", scl_name: "Mindful", tonal_name: "Eudaimonia",
    tier: "0-3", gold: false,
    primary: "#F5F0E8", secondary: "#E8E2D8", background: "#FBFAF8",
    surface: "#FFFFFF", text: "#3D3530", textOnLight: "#3D3530",
    accent: "#D4C9B8", border: "#D4C9B8",
  },
};

export const ORDER_TOKENS: Record<Order, OrderTokens> = {
  foundation: {
    emoji: "🐂", scl_name: "Foundation", load: "≤65%", cns: "Low",
    fontSizeBase: "1rem", fontSizeDisplay: "1.75rem",
    fontWeight: 400, fontWeightDisplay: 600,
    letterSpacing: "0.02em", lineHeight: 1.75,
    density: "spacious", restPeriod: "60-90s",
    uiNote: "Patient, deliberate. Large breathing room. Learning posture.",
  },
  strength: {
    emoji: "⛽", scl_name: "Strength", load: "75-85%", cns: "High",
    fontSizeBase: "1rem", fontSizeDisplay: "2rem",
    fontWeight: 700, fontWeightDisplay: 900,
    letterSpacing: "0.005em", lineHeight: 1.45,
    density: "compact", restPeriod: "3-4min",
    uiNote: "Heavy, focused. Dense information. High contrast. No decorative elements.",
  },
  hypertrophy: {
    emoji: "🦋", scl_name: "Hypertrophy", load: "65-75%", cns: "Moderate",
    fontSizeBase: "1rem", fontSizeDisplay: "1.875rem",
    fontWeight: 500, fontWeightDisplay: 700,
    letterSpacing: "0.015em", lineHeight: 1.6,
    density: "comfortable", restPeriod: "60-90s",
    uiNote: "Moderate density. Volume-forward. Pump-visible layout.",
  },
  performance: {
    emoji: "🏟", scl_name: "Performance", load: "85-100%+", cns: "High",
    fontSizeBase: "1.125rem", fontSizeDisplay: "2.5rem",
    fontWeight: 800, fontWeightDisplay: 900,
    letterSpacing: "0em", lineHeight: 1.35,
    density: "sparse", restPeriod: "Full",
    uiNote: "Testing environment. Maximum signal, no noise. Number forward.",
  },
  "full-body": {
    emoji: "🌾", scl_name: "Full Body", load: "~70%", cns: "Moderate",
    fontSizeBase: "1rem", fontSizeDisplay: "1.75rem",
    fontWeight: 500, fontWeightDisplay: 650,
    letterSpacing: "0.01em", lineHeight: 1.65,
    density: "flowing", restPeriod: "30-90s",
    uiNote: "Flow-forward. Movements visualized as a sequence, not a list.",
  },
  balance: {
    emoji: "⚖", scl_name: "Balance", load: "~70%", cns: "Moderate",
    fontSizeBase: "0.9375rem", fontSizeDisplay: "1.625rem",
    fontWeight: 500, fontWeightDisplay: 600,
    letterSpacing: "0.02em", lineHeight: 1.6,
    density: "precise", restPeriod: "90s",
    uiNote: "Corrective precision. Microscope on detail. Tight, deliberate layout.",
  },
  restoration: {
    emoji: "🖼", scl_name: "Restoration", load: "≤55%", cns: "Low",
    fontSizeBase: "1.0625rem", fontSizeDisplay: "1.75rem",
    fontWeight: 300, fontWeightDisplay: 400,
    letterSpacing: "0.03em", lineHeight: 1.85,
    density: "airy", restPeriod: "60s",
    uiNote: "Recovery posture. Maximum whitespace. Slow, breath-paced rhythm.",
  },
};

// Generate CSS custom properties for a given zip code's color + order
export function getZipCSSVars(color: Color, order: Order): Record<string, string> {
  const c = COLOR_TOKENS[color];
  const o = ORDER_TOKENS[order];
  return {
    "--ppl-primary": c.primary,
    "--ppl-secondary": c.secondary,
    "--ppl-background": c.background,
    "--ppl-surface": c.surface,
    "--ppl-text": c.textOnLight,
    "--ppl-accent": c.accent,
    "--ppl-border": c.border,
    "--ppl-font-size-base": o.fontSizeBase,
    "--ppl-font-size-display": o.fontSizeDisplay,
    "--ppl-font-weight": String(o.fontWeight),
    "--ppl-font-weight-display": String(o.fontWeightDisplay),
    "--ppl-letter-spacing": o.letterSpacing,
    "--ppl-line-height": String(o.lineHeight),
  };
}
