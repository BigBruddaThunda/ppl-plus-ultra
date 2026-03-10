// BlockSection — renders a single workout block (♨️ Warm-Up, 🧈 Bread & Butter, etc.)

import Link from "next/link";
import { parseZipCode } from "@/lib/scl";
import { LogButton } from "./LogButton";

interface BlockSectionProps {
  raw: string; // raw markdown text for one block
  isLast?: boolean;
  zipCode?: string; // numeric zip code for logging
}

// Match emoji zip codes like ⛽🏛🪡🔵 in junction text
const ZIP_PATTERN =
  /([🐂⛽🦋🏟🌾⚖🖼][🏛🔨🌹🪐⌛🐬][🛒🪡🍗➕➖][⚫🟢🔵🟣🔴🟠🟡⚪])/gu;

function renderJunctionLinks(text: string): React.ReactNode[] {
  const parts: React.ReactNode[] = [];
  let lastIndex = 0;

  for (const match of text.matchAll(ZIP_PATTERN)) {
    const idx = match.index!;
    if (idx > lastIndex) {
      parts.push(text.slice(lastIndex, idx));
    }
    const emojiZip = match[1];
    const parsed = parseZipCode(emojiZip);
    if (parsed) {
      parts.push(
        <Link
          key={`${emojiZip}-${idx}`}
          href={`/zip/${parsed.numeric}`}
          className="underline decoration-[var(--ppl-accent)] underline-offset-2 hover:opacity-80"
        >
          {emojiZip}
        </Link>
      );
    } else {
      parts.push(emojiZip);
    }
    lastIndex = idx + match[0].length;
  }
  if (lastIndex < text.length) {
    parts.push(text.slice(lastIndex));
  }
  return parts;
}

/** Extract exercise name from a tree notation line like "├─ 5 🪡 Barbell Row (squeeze at top)" */
function extractExerciseName(line: string): string | null {
  // Match: ├─ [optional reps] [optional type emoji] ExerciseName (optional cue)
  const match = line.match(/├─\s*(?:\d+\s+)?(?:[🛒🪡🍗➕➖]\s+)?(.+?)(?:\s*\(.*\))?$/u);
  return match ? match[1].trim() : null;
}

/** Extract block name from the first ## header in the raw block */
function extractBlockName(lines: string[]): string {
  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed.startsWith("## ")) {
      return trimmed.replace(/^## /, "").replace(/^\d+\)\s*/, "");
    }
  }
  return "Unknown Block";
}

export function BlockSection({ raw, isLast, zipCode }: BlockSectionProps) {
  const lines = raw.split("\n");
  const isJunction = raw.includes("🚂 Junction");
  const isSave = raw.includes("🧮 SAVE");
  const blockName = extractBlockName(lines);

  return (
    <section
      className="py-4"
      style={{
        borderBottom: isLast
          ? "none"
          : "2px solid var(--ppl-border)",
      }}
    >
      {lines.map((line, i) => {
        const trimmed = line.trim();
        if (!trimmed) return null;

        // Block header: ## N) emoji Name or ## 🧮 SAVE
        if (trimmed.startsWith("## ")) {
          return (
            <h3
              key={i}
              className="text-base font-semibold mb-2"
              style={{
                fontWeight: "var(--ppl-font-weight-heading, 700)" as string,
                letterSpacing: "var(--ppl-letter-spacing, 0)",
              }}
            >
              {trimmed.replace(/^## /, "")}
            </h3>
          );
        }

        // Subcode line
        if (trimmed.startsWith("Subcode:")) {
          return (
            <p key={i} className="font-mono text-xs opacity-40 mb-2">
              {trimmed}
            </p>
          );
        }

        // Tree notation: exercise lines with log button
        if (trimmed.startsWith("├─") || trimmed.startsWith("│")) {
          const isExercise = trimmed.startsWith("├─");
          const exerciseName = isExercise ? extractExerciseName(trimmed) : null;

          return (
            <p
              key={i}
              className={`font-mono text-sm ${isExercise ? "mt-2" : "ml-4 opacity-70"}`}
              style={{ lineHeight: "var(--ppl-line-height, 1.6)" }}
            >
              {trimmed}
              {isExercise && exerciseName && zipCode && (
                <LogButton
                  zipCode={zipCode}
                  blockName={blockName}
                  exerciseName={exerciseName}
                />
              )}
            </p>
          );
        }

        // Rest line
        if (trimmed.startsWith("Rest:")) {
          return (
            <p key={i} className="text-xs font-mono opacity-50 mt-1 mb-2">
              {trimmed}
            </p>
          );
        }

        // Junction lines with zip links
        if (isJunction && (trimmed.startsWith("- Next") || trimmed.startsWith("Next"))) {
          return (
            <p key={i} className="text-sm mt-1">
              {renderJunctionLinks(trimmed)}
            </p>
          );
        }

        // SAVE closing principle
        if (isSave && !trimmed.startsWith("##")) {
          return (
            <p key={i} className="text-sm italic opacity-70 mt-1">
              {trimmed}
            </p>
          );
        }

        // Log/list items
        if (trimmed.startsWith("- ")) {
          return (
            <p key={i} className="text-sm ml-2 mt-1">
              {isJunction ? renderJunctionLinks(trimmed) : trimmed}
            </p>
          );
        }

        // Default: plain text
        return (
          <p key={i} className="text-sm mt-1">
            {trimmed}
          </p>
        );
      })}
    </section>
  );
}
