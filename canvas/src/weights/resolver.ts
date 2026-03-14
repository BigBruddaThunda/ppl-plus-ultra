/**
 * Weight Resolver — Interaction Resolution Layer (Step 4)
 *
 * computeRawVector() (Step 1–3) sums all dial weights but does not enforce
 * hard suppression ceilings from higher-priority dials. This module is
 * the additive post-processing layer (Step 4) that:
 *
 *   1. Reads Order's suppressions. Any position where Order's suppression <= -6
 *      is "hard suppressed" — the resolved value is pinned to that suppression
 *      floor regardless of what any other dial contributed.
 *
 *   2. Reads Color's suppressions. Same rule: any position where Color's
 *      suppression <= -6 is pinned, unless Order already pinned it harder.
 *
 *   3. All other positions (soft weights from Axis and Type, or Order/Color
 *      suppressions > -6) pass through unchanged from the raw vector.
 *
 * The constraint hierarchy enforced here:
 *   Order > Color > Axis > Type
 *
 * Axis and Type are soft — their contributions are already baked into the raw
 * sum from computeRawVector(). The resolver does NOT re-apply any affinity or
 * suppression values. It only pins hard suppression floors.
 *
 * A "hard suppression" threshold: weight <= -6 (covers both -6 and -8 values).
 */

import { WEIGHT_VECTOR_LENGTH } from '../types/scl.js';
import { ORDERS_WEIGHTS, COLORS_WEIGHTS, computeRawVector } from './index.js';

const HARD_SUPPRESSION_THRESHOLD = -6;

/**
 * Resolve a raw weight vector by enforcing the Order > Color hard suppression
 * hierarchy.
 *
 * @param rawVector  The output of computeRawVector() — Steps 1–3
 * @param orderPos   Order dial position (1–7)
 * @param axisPos    Axis dial position (1–6)   — used for future expansion
 * @param typePos    Type dial position (1–5)   — used for future expansion
 * @param colorPos   Color dial position (1–8)
 * @returns          A new Float32Array of length 62. The input is not mutated.
 */
export function resolveVector(
  rawVector: Float32Array,
  orderPos: number,
  _axisPos: number,
  _typePos: number,
  colorPos: number
): Float32Array {
  // Clone — resolver never mutates the input raw vector
  const resolved = new Float32Array(rawVector);

  const orderEntry = ORDERS_WEIGHTS[orderPos];
  const colorEntry = COLORS_WEIGHTS[colorPos];

  for (let i = 1; i <= WEIGHT_VECTOR_LENGTH; i++) {
    // --- Priority 1: Order hard suppression ---
    const orderSuppression = orderEntry?.suppressions[i];
    if (orderSuppression !== undefined && orderSuppression <= HARD_SUPPRESSION_THRESHOLD) {
      resolved[i] = orderSuppression;
      continue; // Order takes absolute priority — skip Color check
    }

    // --- Priority 2: Color hard suppression ---
    const colorSuppression = colorEntry?.suppressions[i];
    if (colorSuppression !== undefined && colorSuppression <= HARD_SUPPRESSION_THRESHOLD) {
      resolved[i] = colorSuppression;
      continue;
    }

    // --- No hard suppression: raw value passes through unchanged ---
    // (resolved[i] already holds rawVector[i] from the clone above)
  }

  return resolved;
}

/**
 * Convenience wrapper: compute raw vector then resolve in sequence.
 *
 * This is the primary entry point for callers who want a fully resolved
 * weight vector from scratch. Equivalent to:
 *   resolveVector(computeRawVector(o, a, t, c), o, a, t, c)
 *
 * @param orderPos   Order dial position (1–7)
 * @param axisPos    Axis dial position (1–6)
 * @param typePos    Type dial position (1–5)
 * @param colorPos   Color dial position (1–8)
 * @returns          Resolved Float32Array of length 62
 */
export function resolveZip(
  orderPos: number,
  axisPos: number,
  typePos: number,
  colorPos: number
): Float32Array {
  const raw = computeRawVector(orderPos, axisPos, typePos, colorPos);
  return resolveVector(raw, orderPos, axisPos, typePos, colorPos);
}
