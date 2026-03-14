/**
 * canvas/src/rendering/index.ts — Rendering Pipeline Public API
 *
 * Re-exports all rendering module exports.
 *
 * Phase 5 — RNDR-05, RNDR-06, RNDR-07
 */

export { COLOR_SATURATION } from './saturation-map.js';
export type { BlockContainerStyle } from './block-styles.js';
export { BLOCK_CONTAINER_STYLES } from './block-styles.js';
export {
  ORDER_W_TO_SLUG,
  AXIS_W_TO_SLUG,
  weightsToCSSVars,
} from './weights-to-css-vars.js';
