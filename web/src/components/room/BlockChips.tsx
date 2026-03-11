"use client";

// BlockChips — compact block overview shown at 0.5x zoom

interface Props {
  blocks: string[];
  onSelect: (index: number) => void;
}

const BLOCK_EMOJIS: Record<string, string> = {
  "Warm-Up": "♨️",
  "Intention": "🎯",
  "Fundamentals": "🔢",
  "Bread": "🧈",
  "Butter": "🧈",
  "Bread & Butter": "🧈",
  "Bread/Butter": "🧈",
  "Circulation": "🫀",
  "Primer": "▶️",
  "Composition": "🎼",
  "Gambit": "♟️",
  "Progression": "🪜",
  "Exposure": "🌎",
  "ARAM": "🎱",
  "Gutter": "🌋",
  "Vanity": "🪞",
  "Sculpt": "🗿",
  "Craft": "🛠",
  "Supplemental": "🧩",
  "Release": "🪫",
  "Sandbox": "🏖",
  "Reformance": "🏗",
  "Imprint": "🧬",
  "Junction": "🚂",
  "SAVE": "🧮",
  "Choice": "🔠",
};

function extractBlockInfo(raw: string): { name: string; emoji: string; exerciseCount: number } {
  const lines = raw.split("\n").map((l) => l.trim()).filter(Boolean);
  let name = "Block";
  let emoji = "";

  for (const line of lines) {
    if (line.startsWith("## ")) {
      const header = line.replace(/^## /, "").replace(/^\d+\)\s*/, "");
      // Find the block name from known blocks
      for (const [key, e] of Object.entries(BLOCK_EMOJIS)) {
        if (header.includes(key)) {
          name = key;
          emoji = e;
          break;
        }
      }
      if (!emoji) {
        name = header;
      }
      break;
    }
  }

  const exerciseCount = lines.filter((l) => l.startsWith("├─")).length;

  return { name, emoji, exerciseCount };
}

export function BlockChips({ blocks, onSelect }: Props) {
  return (
    <div className="grid grid-cols-3 gap-2 sm:grid-cols-4">
      {blocks.map((block, i) => {
        const info = extractBlockInfo(block);
        return (
          <button
            key={i}
            onClick={() => onSelect(i)}
            className="rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-3 py-2.5 text-left transition-all hover:border-[var(--ppl-accent)] hover:shadow-sm"
          >
            <span className="text-lg">{info.emoji || "📦"}</span>
            <p className="mt-0.5 text-xs font-medium truncate">{info.name}</p>
            {info.exerciseCount > 0 && (
              <p className="text-[10px] opacity-40">{info.exerciseCount} exercises</p>
            )}
          </button>
        );
      })}
    </div>
  );
}
