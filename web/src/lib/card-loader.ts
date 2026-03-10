// Card Loader — reads .md card files from the cards/ directory tree
// Parses frontmatter via gray-matter and returns structured WorkoutCard

import matter from "gray-matter";
import { readFileSync, readdirSync, existsSync } from "fs";
import { join } from "path";
import type { CardFrontmatter, WorkoutCard, ZipCode } from "@/types/scl";

const CARDS_ROOT = join(process.cwd(), "..", "cards");

const ORDER_DIRS: Record<string, string> = {
  foundation: "🐂-foundation",
  strength: "⛽-strength",
  hypertrophy: "🦋-hypertrophy",
  performance: "🏟-performance",
  "full-body": "🌾-full-body",
  balance: "⚖-balance",
  restoration: "🖼-restoration",
};

const AXIS_DIRS: Record<string, string> = {
  basics: "🏛-basics",
  functional: "🔨-functional",
  aesthetic: "🌹-aesthetic",
  challenge: "🪐-challenge",
  time: "⌛-time",
  partner: "🐬-partner",
};

const TYPE_DIRS: Record<string, string> = {
  push: "🛒-push",
  pull: "🪡-pull",
  legs: "🍗-legs",
  plus: "➕-plus",
  ultra: "➖-ultra",
};

/**
 * Load a workout card by ZipCode.
 * Returns null if the card is EMPTY, missing, or the directory doesn't exist.
 */
export function loadCard(zip: ZipCode): WorkoutCard | null {
  const orderDir = ORDER_DIRS[zip.order];
  const axisDir = AXIS_DIRS[zip.axis];
  const typeDir = TYPE_DIRS[zip.type];

  if (!orderDir || !axisDir || !typeDir) return null;

  const dirPath = join(CARDS_ROOT, orderDir, axisDir, typeDir);
  if (!existsSync(dirPath)) return null;

  // Find file matching the emoji zip prefix
  const files = readdirSync(dirPath);
  const match = files.find((f) => f.startsWith(zip.raw) && f.endsWith(".md"));
  if (!match) return null;

  const raw = readFileSync(join(dirPath, match), "utf-8");
  const { data, content } = matter(raw);
  const fm = data as CardFrontmatter;

  // Don't render empty stubs
  if (fm.status === "EMPTY") return null;

  return {
    frontmatter: fm,
    content: content.trim(),
    zipCode: zip,
  };
}
