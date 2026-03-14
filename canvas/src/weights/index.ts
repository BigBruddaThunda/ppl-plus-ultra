/**
 * Weight System — Barrel Export and computeRawVector()
 *
 * computeRawVector() implements Steps 1–3 of the derivation formula:
 *   Step 1: Primary weights (+8 for each active dial)
 *   Step 2: Affinity cascade (sum affinities from all 4 active dials)
 *   Step 3: Suppression cascade (sum suppressions from all 4 active dials)
 *   Clamp all positions to [-8, +8]
 *
 * Steps 4 (interaction resolution) and 5 (temporal layer) are NOT implemented here.
 * This function provides the raw summation vector for downstream consumers.
 *
 * Block and Operator tables are exported but NOT consumed by computeRawVector().
 * They are used by downstream block-selection and operator-selection systems.
 */

import { WEIGHT_VECTOR_LENGTH } from '../types/scl.js';
import { ORDERS_WEIGHTS } from './orders.js';
import { AXES_WEIGHTS } from './axes.js';
import { TYPES_WEIGHTS } from './type-weights.js';
import { COLORS_WEIGHTS } from './colors.js';
import type { WeightEntry } from './types.js';

// ---------------------------------------------------------------------------
// Re-exports
// ---------------------------------------------------------------------------

export { ORDERS_WEIGHTS } from './orders.js';
export { AXES_WEIGHTS } from './axes.js';
export { TYPES_WEIGHTS } from './type-weights.js';
export { COLORS_WEIGHTS } from './colors.js';
export { BLOCKS_WEIGHTS } from './blocks.js';
export { OPERATORS_WEIGHTS } from './operators.js';
export type { WeightScale, WeightEntry, DialWeightTable } from './types.js';

// ---------------------------------------------------------------------------
// W position offsets for each dial
// ---------------------------------------------------------------------------
// ORDER positions:  1–7   (direct, no offset)
// AXIS positions:   8–13  (axis number + 7)
// TYPE positions:   14–18 (type number + 13)
// COLOR positions:  19–26 (color number + 18)

const ORDER_OFFSET = 0;  // orderPos 1–7 → W slot 1–7
const AXIS_OFFSET  = 7;  // axisPos 1–6 → W slot 8–13
const TYPE_OFFSET  = 13; // typePos 1–5 → W slot 14–18
const COLOR_OFFSET = 18; // colorPos 1–8 → W slot 19–26

// ---------------------------------------------------------------------------
// computeRawVector
// ---------------------------------------------------------------------------

/**
 * Compute the raw weight vector for a zip code (Steps 1–3 only).
 *
 * @param orderPos  Order dial position (1–7)
 * @param axisPos   Axis dial position (1–6)
 * @param typePos   Type dial position (1–5)
 * @param colorPos  Color dial position (1–8)
 * @returns Float32Array of length 62 (slot 0 unused, slots 1–61 for W positions)
 */
export function computeRawVector(
  orderPos: number,
  axisPos:  number,
  typePos:  number,
  colorPos: number
): Float32Array {
  // Allocate: 62 slots, slot 0 unused
  const vec = new Float32Array(WEIGHT_VECTOR_LENGTH + 1);

  // Retrieve the 4 active dial entries
  const orderEntry = ORDERS_WEIGHTS[orderPos] as WeightEntry | undefined;
  const axisEntry  = AXES_WEIGHTS[axisPos]   as WeightEntry | undefined;
  const typeEntry  = TYPES_WEIGHTS[typePos]  as WeightEntry | undefined;
  const colorEntry = COLORS_WEIGHTS[colorPos] as WeightEntry | undefined;

  // ---------
  // Step 1: Primary weights — +8 at each active dial's W position
  // ---------
  if (orderEntry !== undefined) vec[orderPos + ORDER_OFFSET] = 8;
  if (axisEntry  !== undefined) vec[axisPos  + AXIS_OFFSET]  = 8;
  if (typeEntry  !== undefined) vec[typePos  + TYPE_OFFSET]  = 8;
  if (colorEntry !== undefined) vec[colorPos + COLOR_OFFSET] = 8;

  // Helper: apply one entry's affinities and suppressions to the vector
  function applyEntry(entry: WeightEntry | undefined): void {
    if (entry === undefined) return;

    // Step 2: Affinity cascade
    for (const [key, val] of Object.entries(entry.affinities)) {
      const pos = Number(key);
      if (pos >= 1 && pos <= WEIGHT_VECTOR_LENGTH && val !== undefined) {
        vec[pos] = (vec[pos] as number) + val;
      }
    }

    // Step 3: Suppression cascade
    for (const [key, val] of Object.entries(entry.suppressions)) {
      const pos = Number(key);
      if (pos >= 1 && pos <= WEIGHT_VECTOR_LENGTH && val !== undefined) {
        vec[pos] = (vec[pos] as number) + val;
      }
    }
  }

  applyEntry(orderEntry);
  applyEntry(axisEntry);
  applyEntry(typeEntry);
  applyEntry(colorEntry);

  // ---------
  // Clamp all positions to [-8, +8]
  // ---------
  for (let i = 1; i <= WEIGHT_VECTOR_LENGTH; i++) {
    vec[i] = Math.max(-8, Math.min(8, vec[i] as number));
  }

  return vec;
}
