// City Compiler — TypeScript runtime resolver
// Reads pre-compiled JSON files from middle-math/compiled/
// For use in Server Components and build-time generation

import { readFileSync, existsSync } from "fs";
import { join } from "path";
import type { CompiledZip, CompiledDeck, CompiledAbacus } from "@/types/compiled";

// Path to compiled data (relative to project root, not web/)
const COMPILED_ROOT = join(process.cwd(), "..", "middle-math", "compiled");
const ZIPS_DIR = join(COMPILED_ROOT, "zips");
const DECKS_DIR = join(COMPILED_ROOT, "decks");
const ABACI_DIR = join(COMPILED_ROOT, "abaci");

// In-memory cache for resolved objects
const zipCache = new Map<string, CompiledZip>();
const deckCache = new Map<number, CompiledDeck>();
const abacusCache = new Map<number, CompiledAbacus>();

/**
 * Resolve a numeric zip code to its compiled object.
 * Reads from middle-math/compiled/zips/NNNN.json
 */
export function resolveZip(code: string): CompiledZip | null {
  // Validate format
  if (!/^\d{4}$/.test(code)) return null;

  const cached = zipCache.get(code);
  if (cached) return cached;

  const filePath = join(ZIPS_DIR, `${code}.json`);
  if (!existsSync(filePath)) return null;

  try {
    const raw = readFileSync(filePath, "utf-8");
    const parsed = JSON.parse(raw) as CompiledZip;
    zipCache.set(code, parsed);
    return parsed;
  } catch {
    return null;
  }
}

/**
 * Resolve a deck number (1-42) to its compiled centroid object.
 * Reads from middle-math/compiled/decks/deck-NN.json
 */
export function resolveDeck(deckNumber: number): CompiledDeck | null {
  if (deckNumber < 1 || deckNumber > 42) return null;

  const cached = deckCache.get(deckNumber);
  if (cached) return cached;

  const filePath = join(DECKS_DIR, `deck-${String(deckNumber).padStart(2, "0")}.json`);
  if (!existsSync(filePath)) return null;

  try {
    const raw = readFileSync(filePath, "utf-8");
    const parsed = JSON.parse(raw) as CompiledDeck;
    deckCache.set(deckNumber, parsed);
    return parsed;
  } catch {
    return null;
  }
}

/**
 * Resolve an abacus ID (1-35) to its compiled centroid object.
 * Reads from middle-math/compiled/abaci/abacus-NN.json
 */
export function resolveAbacus(abacusId: number): CompiledAbacus | null {
  if (abacusId < 1 || abacusId > 35) return null;

  const cached = abacusCache.get(abacusId);
  if (cached) return cached;

  const filePath = join(ABACI_DIR, `abacus-${String(abacusId).padStart(2, "0")}.json`);
  if (!existsSync(filePath)) return null;

  try {
    const raw = readFileSync(filePath, "utf-8");
    const parsed = JSON.parse(raw) as CompiledAbacus;
    abacusCache.set(abacusId, parsed);
    return parsed;
  } catch {
    return null;
  }
}

/**
 * Check if compiled data is available.
 */
export function isCompiled(): boolean {
  return existsSync(ZIPS_DIR);
}
