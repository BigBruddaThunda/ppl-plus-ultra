// D-Module Design System — Architectural proportions per Order
// Source: html/design-system/orders/*.css
// The D-module system derives all spacing, typography, shadows from --ppl-D (column diameter)

import type { Order, Color } from "@/types/scl";
import type { ZipCode } from "@/types/scl";
import { getZipCSSVars } from "./tokens";

export interface OrderProportions {
  /** Column diameter base unit (rem) */
  D: number;
  /** Column height ratio (7–10) */
  columnRatio: number;
  /** Gap between columns (1.5–4) */
  intercolumniation: number;
  /** Entablature to column ratio */
  entablatureRatio: number;
  /** Line weight scale factor */
  lineMultiplier: number;
  /** Shadow intensity scale factor */
  shadowDepth: number;
  /** Material hue (warm/cool neutral) */
  materialHue: number;
  /** Material saturation */
  materialSat: string;
  /** Material warmth (0–1) */
  materialWarmth: number;
  /** Body font weight */
  fontWeight: number;
  /** Display font weight */
  fontWeightDisplay: number;
  /** Letter spacing */
  letterSpacing: string;
  /** Line height */
  lineHeight: number;
  /** Spacing density multiplier */
  density: number;
  /** Classical architectural name */
  classical: string;
}

const ORDER_PROPORTIONS: Record<Order, OrderProportions> = {
  foundation: {
    D: 1, columnRatio: 7, intercolumniation: 4, entablatureRatio: 0.25,
    lineMultiplier: 0.8, shadowDepth: 0.6,
    materialHue: 35, materialSat: "12%", materialWarmth: 0.6,
    fontWeight: 400, fontWeightDisplay: 600,
    letterSpacing: "0.02em", lineHeight: 1.75, density: 1.4,
    classical: "Tuscan",
  },
  strength: {
    D: 1, columnRatio: 8, intercolumniation: 2, entablatureRatio: 0.25,
    lineMultiplier: 1.3, shadowDepth: 1.4,
    materialHue: 220, materialSat: "5%", materialWarmth: 0.3,
    fontWeight: 700, fontWeightDisplay: 900,
    letterSpacing: "0.005em", lineHeight: 1.45, density: 0.85,
    classical: "Doric",
  },
  hypertrophy: {
    D: 1, columnRatio: 9, intercolumniation: 2.25, entablatureRatio: 0.25,
    lineMultiplier: 1.0, shadowDepth: 1.0,
    materialHue: 30, materialSat: "8%", materialWarmth: 0.5,
    fontWeight: 500, fontWeightDisplay: 700,
    letterSpacing: "0.015em", lineHeight: 1.6, density: 1.0,
    classical: "Ionic",
  },
  performance: {
    D: 1.125, columnRatio: 10, intercolumniation: 1.5, entablatureRatio: 0.25,
    lineMultiplier: 1.5, shadowDepth: 1.8,
    materialHue: 0, materialSat: "0%", materialWarmth: 0.5,
    fontWeight: 800, fontWeightDisplay: 900,
    letterSpacing: "0em", lineHeight: 1.35, density: 0.7,
    classical: "Corinthian",
  },
  "full-body": {
    D: 1, columnRatio: 10, intercolumniation: 2.25, entablatureRatio: 0.25,
    lineMultiplier: 1.0, shadowDepth: 1.0,
    materialHue: 25, materialSat: "18%", materialWarmth: 0.7,
    fontWeight: 500, fontWeightDisplay: 650,
    letterSpacing: "0.01em", lineHeight: 1.65, density: 1.05,
    classical: "Composite",
  },
  balance: {
    D: 0.9375, columnRatio: 8.5, intercolumniation: 2.25, entablatureRatio: 0.235,
    lineMultiplier: 1.1, shadowDepth: 1.0,
    materialHue: 45, materialSat: "6%", materialWarmth: 0.5,
    fontWeight: 500, fontWeightDisplay: 600,
    letterSpacing: "0.02em", lineHeight: 1.6, density: 0.95,
    classical: "Vitruvian",
  },
  restoration: {
    D: 1.0625, columnRatio: 9.5, intercolumniation: 3, entablatureRatio: 0.237,
    lineMultiplier: 0.6, shadowDepth: 0.2,
    materialHue: 40, materialSat: "15%", materialWarmth: 0.8,
    fontWeight: 300, fontWeightDisplay: 400,
    letterSpacing: "0.03em", lineHeight: 1.85, density: 1.5,
    classical: "Palladian",
  },
};

export function getOrderProportions(order: Order): OrderProportions {
  return ORDER_PROPORTIONS[order];
}

/**
 * Generate the full set of CSS custom properties for a zip code.
 * Merges Color tokens (palette) + Order D-module proportions (architecture).
 */
export function getFullZipStyle(zip: ZipCode): Record<string, string> {
  const colorVars = getZipCSSVars(zip.color, zip.order);
  const p = ORDER_PROPORTIONS[zip.order];

  return {
    ...colorVars,
    // D-module architectural proportions
    "--ppl-D": `${p.D}rem`,
    "--ppl-column-ratio": String(p.columnRatio),
    "--ppl-intercolumniation": String(p.intercolumniation),
    "--ppl-entablature-ratio": String(p.entablatureRatio),
    "--ppl-line-multiplier": String(p.lineMultiplier),
    "--ppl-shadow-depth": String(p.shadowDepth),
    // Material
    "--ppl-material-hue": String(p.materialHue),
    "--ppl-material-sat": p.materialSat,
    "--ppl-material-warmth": String(p.materialWarmth),
    // Typography weights (override tokens.ts basics with D-module values)
    "--ppl-weight-font-weight": String(p.fontWeight),
    "--ppl-weight-font-weight-display": String(p.fontWeightDisplay),
    "--ppl-weight-letter-spacing": p.letterSpacing,
    "--ppl-weight-lineheight": String(p.lineHeight),
    "--ppl-weight-spacing-multiplier": String(p.density),
    "--ppl-weight-density": String(p.density),
  };
}

/**
 * Derive content max-width from Order density.
 * Foundation (spacious) gets wider, Performance (sparse) gets narrower.
 */
export function getContentMaxWidth(order: Order): string {
  const p = ORDER_PROPORTIONS[order];
  // density > 1 = spacious = wider, density < 1 = compact = narrower
  const baseWidth = 42; // rem
  const width = baseWidth * p.density;
  return `${Math.round(width * 100) / 100}rem`;
}
