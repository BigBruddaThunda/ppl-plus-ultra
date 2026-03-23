// Card Loader — reads .md card files from the cards/ directory tree
// Parses frontmatter via gray-matter and returns structured WorkoutCard
//
// On Vercel, the cards/ directory may not exist (it lives outside web/).
// In that case, all loads return null gracefully.

import type { CardFrontmatter, WorkoutCard, ZipCode } from "@/types/scl";

let matter: typeof import("gray-matter")["default"] | null = null;
let fs: typeof import("fs") | null = null;
let pathJoin: typeof import("path")["join"] | null = null;
let CARDS_ROOT = "";

// Lazy-init filesystem access — fails gracefully on Vercel
function initFs() {
  if (fs !== null) return true;
  try {
    fs = require("fs");
    pathJoin = require("path").join;
    matter = require("gray-matter");
    CARDS_ROOT = pathJoin!(process.cwd(), "..", "cards");
    return fs!.existsSync(CARDS_ROOT);
  } catch {
    return false;
  }
}

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
 * Returns null gracefully on Vercel where cards/ is not available.
 */
export function loadCard(zip: ZipCode): WorkoutCard | null {
  if (!initFs() || !fs || !pathJoin || !matter) return null;

  try {
    const orderDir = ORDER_DIRS[zip.order];
    const axisDir = AXIS_DIRS[zip.axis];
    const typeDir = TYPE_DIRS[zip.type];

    if (!orderDir || !axisDir || !typeDir) return null;

    const dirPath = pathJoin(CARDS_ROOT, orderDir, axisDir, typeDir);
    if (!fs.existsSync(dirPath)) return null;

    // Find file matching the emoji zip prefix
    const files = fs.readdirSync(dirPath);
    const match = files.find((f: string) => f.startsWith(zip.raw) && f.endsWith(".md"));
    if (!match) return null;

    const raw = fs.readFileSync(pathJoin(dirPath, match), "utf-8");
    const { data, content } = matter(raw);
    const fm = data as CardFrontmatter;

    // Don't render empty stubs
    if (fm.status === "EMPTY") return null;

    return {
      frontmatter: fm,
      content: content.trim(),
      zipCode: zip,
    };
  } catch {
    return null;
  }
}
