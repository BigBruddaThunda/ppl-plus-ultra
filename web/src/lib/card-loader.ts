// Card Loader — reads .md card files from the cards/ directory tree
// Parses frontmatter via gray-matter and returns structured WorkoutCard
//
// On Vercel, the cards/ directory may not exist (it lives outside web/).
// In that case, all loads return null gracefully.

import type { CardFrontmatter, WorkoutCard, ZipCode } from "@/types/scl";

// eslint-disable-next-line @typescript-eslint/no-explicit-any
let _matter: any = null;
// eslint-disable-next-line @typescript-eslint/no-explicit-any
let _fs: any = null;
// eslint-disable-next-line @typescript-eslint/no-explicit-any
let _join: any = null;
let _root = "";
let _initialized = false;
let _available = false;

// Lazy-init filesystem access — fails gracefully on Vercel
function initFs(): boolean {
  if (_initialized) return _available;
  _initialized = true;
  try {
    _fs = require("fs");
    _join = require("path").join;
    _matter = require("gray-matter");
    _root = _join(process.cwd(), "..", "cards");
    _available = _fs.existsSync(_root);
    return _available;
  } catch {
    _available = false;
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
  if (!initFs()) return null;

  try {
    const orderDir = ORDER_DIRS[zip.order];
    const axisDir = AXIS_DIRS[zip.axis];
    const typeDir = TYPE_DIRS[zip.type];

    if (!orderDir || !axisDir || !typeDir) return null;

    const dirPath = _join(_root, orderDir, axisDir, typeDir);
    if (!_fs.existsSync(dirPath)) return null;

    // Find file matching the emoji zip prefix
    const files = _fs.readdirSync(dirPath) as string[];
    const match = files.find((f: string) => f.startsWith(zip.raw) && f.endsWith(".md"));
    if (!match) return null;

    const raw = _fs.readFileSync(_join(dirPath, match), "utf-8") as string;
    const { data, content } = _matter(raw) as { data: CardFrontmatter; content: string };
    const fm = data;

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
