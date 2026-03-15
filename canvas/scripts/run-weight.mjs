/**
 * run-weight.mjs — Node ESM driver for the canvas weight engine.
 *
 * Imports the compiled weight engine and outputs CSS custom properties
 * as JSON for a given 4-digit numeric zip code.
 *
 * Usage:
 *   node canvas/scripts/run-weight.mjs <zip>
 *
 * Example:
 *   node canvas/scripts/run-weight.mjs 2123
 *
 * Output:
 *   JSON object of CSS custom property name/value pairs to stdout.
 *   e.g. { "--ppl-weight-font-weight": "800", "--ppl-theme-primary": "oklch(...)", ... }
 *
 * Exit codes:
 *   0 — Success
 *   1 — Missing argument or invalid zip format
 */

import { fileURLToPath, pathToFileURL } from 'url';
import { dirname, resolve } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Resolve dist/ relative to this script (canvas/scripts/ -> canvas/dist/src/)
const distRoot = resolve(__dirname, '../dist/src');

/**
 * toFileURL — converts an absolute path to a file:// URL string.
 * Required on Windows where dynamic import() rejects bare drive-letter paths
 * (e.g. "C:\...") — must be "file:///C:/...".
 */
function toFileURL(absPath) {
  return pathToFileURL(absPath).href;
}

// ─── Validate argument ────────────────────────────────────────────────────────

const zip = process.argv[2];

if (!zip) {
  process.stderr.write('ERROR: No zip code provided.\n');
  process.stderr.write('Usage: node canvas/scripts/run-weight.mjs <zip>\n');
  process.stderr.write('Example: node canvas/scripts/run-weight.mjs 2123\n');
  process.exit(1);
}

if (!/^\d{4}$/.test(zip)) {
  process.stderr.write(`ERROR: Invalid zip format: "${zip}". Expected 4-digit numeric zip (e.g. 2123).\n`);
  process.exit(1);
}

// ─── Parse zip into 4 dial positions ─────────────────────────────────────────

// Zip format: ORDER AXIS TYPE COLOR (each 1-digit within their valid range)
const orderPos = parseInt(zip[0], 10); // 1-7
const axisPos  = parseInt(zip[1], 10); // 1-6
const typePos  = parseInt(zip[2], 10); // 1-5
const colorPos = parseInt(zip[3], 10); // 1-8

// ─── Import compiled modules ──────────────────────────────────────────────────

const { resolveZip } = await import(
  toFileURL(resolve(distRoot, 'weights/resolver.js'))
);

const { weightsToCSSVars } = await import(
  toFileURL(resolve(distRoot, 'rendering/index.js'))
);

const { tokens } = await import(
  toFileURL(resolve(distRoot, 'tokens/tokens.js'))
);

// ─── Run weight engine ────────────────────────────────────────────────────────

const vector = resolveZip(orderPos, axisPos, typePos, colorPos);
const cssVars = weightsToCSSVars(vector, tokens);

// ─── Output JSON ──────────────────────────────────────────────────────────────

console.log(JSON.stringify(cssVars, null, 2));
