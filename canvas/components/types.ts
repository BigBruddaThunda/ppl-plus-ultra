/**
 * types.ts — CardData and BlockData interfaces for workout card rendering
 *
 * CARD-01: Core data contracts consumed by WorkoutCard.tsx (renderWorkoutCard).
 * All color information flows through cssVars — no hardcoded colors in templates.
 */

/**
 * BlockData represents a single parsed block from a workout card file.
 * Blocks are delimited by ═══ (U+2550 Box Drawings Double Horizontal) in .md files.
 */
export interface BlockData {
  /** 1-based block number within the card */
  number: number;
  /** Block emoji identifier (e.g. "♨️", "🧈", "🚂") */
  emoji: string;
  /** Block name (e.g. "Warm-Up", "Bread & Butter", "Junction") */
  name: string;
  /** Raw markdown body content of the block */
  content: string;
  /** Parsed HTML for rendering (from marked) */
  contentHtml: string;
  /** Block slug for CSS class targeting (e.g. "warm-up", "bread-butter") */
  slug: string;
  /** Block role: orientation | access | transformation | retention | modifier */
  role: 'orientation' | 'access' | 'transformation' | 'retention' | 'modifier';
}

/**
 * CardData is the fully-resolved data contract for rendering a workout card.
 * Produced by parseCardFile() and consumed by renderWorkoutCard().
 *
 * All visual color information is contained in cssVars — no hardcoded
 * color values appear anywhere in the card template (CARD-02).
 */
export interface CardData {
  /** 4-emoji zip code address (e.g. "⛽🏛🪡🔵") */
  zip: string;
  /** 4-digit numeric zip (e.g. "2123") — system-layer key */
  numericZip: string;
  /** Operator: emoji + latin name (e.g. "🤌 facio") */
  operator: string;
  /** Workout title from filename (e.g. "Bent-Over Barbell Row — Back Strength Log") */
  title: string;
  /** Subtitle: training modality, targets, and time estimate */
  subtitle: string;
  /** 🎯 INTENTION text (quoted, one sentence) */
  intention: string;
  /** Type emoji for flanking the title (e.g. "🪡" for Pull) */
  typeEmoji: string;
  /** Parsed workout blocks */
  blocks: BlockData[];
  /**
   * CSS custom properties from weightsToCSSVars().
   * Injected as inline style on .ppl-card container element (NOT :root).
   * Keys: --ppl-theme-primary, --ppl-weight-saturation, etc.
   */
  cssVars: Record<string, string>;
  /**
   * Color slug for data-color attribute on .ppl-card.
   * Enables Color-specific CSS selectors for hatching patterns.
   * Values: "teaching" | "bodyweight" | "structured" | "technical" |
   *         "intense" | "circuit" | "fun" | "mindful"
   */
  colorSlug: string;
  /** Order name slug (e.g. "strength", "foundation") */
  orderSlug: string;
  /** Axis name slug (e.g. "basics", "functional") */
  axisSlug: string;
}
