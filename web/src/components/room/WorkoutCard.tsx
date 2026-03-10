// WorkoutCard — renders a full .md workout card as styled HTML

import type { WorkoutCard as WorkoutCardType } from "@/types/scl";
import { BlockSection } from "./BlockSection";
import { SessionSummary } from "./SessionSummary";

interface Props {
  card: WorkoutCardType;
}

/**
 * Parse the card markdown content into structured sections.
 * Cards use ═══ as block separators and ## for block headers.
 */
function parseCardSections(content: string) {
  // Split into header (before first ═══) and blocks (separated by ═══)
  const parts = content.split(/═{3,}/);

  const header = parts[0]?.trim() || "";
  const blocks = parts.slice(1).map((b) => b.trim()).filter(Boolean);

  // Parse header lines
  const headerLines = header.split("\n").map((l) => l.trim()).filter(Boolean);

  let title = "";
  let subtitle = "";
  let code = "";
  let intention = "";
  let context = "";

  for (const line of headerLines) {
    if (line.startsWith("# ")) {
      title = line.replace(/^# /, "");
    } else if (line.startsWith("## ")) {
      subtitle = line.replace(/^## /, "");
    } else if (line.startsWith("**CODE:**")) {
      code = line.replace("**CODE:**", "").trim();
    } else if (line.startsWith("> ")) {
      intention = line.replace(/^> /, "").replace(/^"/, "").replace(/"$/, "");
    } else if (line.startsWith("*") && line.endsWith("*")) {
      context = line.replace(/^\*/, "").replace(/\*$/, "");
    }
  }

  return { title, subtitle, code, intention, context, blocks };
}

export function WorkoutCard({ card }: Props) {
  const { title, subtitle, code, intention, context, blocks } = parseCardSections(card.content);
  const numericZip = card.zipCode.numeric;

  return (
    <article>
      {/* Title */}
      {title && (
        <h1
          className="text-xl font-bold"
          style={{
            fontWeight: "var(--ppl-font-weight-heading, 700)" as string,
            letterSpacing: "var(--ppl-letter-spacing, 0)",
          }}
        >
          {title}
        </h1>
      )}

      {/* Subtitle */}
      {subtitle && (
        <p className="text-sm opacity-60 mt-1">{subtitle}</p>
      )}

      {/* Code line */}
      {code && (
        <p className="font-mono text-xs opacity-40 mt-2">CODE: {code}</p>
      )}

      {/* Intention */}
      {intention && (
        <blockquote
          className="mt-4 pl-4 italic text-sm"
          style={{
            borderLeft: "3px solid var(--ppl-accent)",
            color: "var(--ppl-text)",
            opacity: 0.8,
          }}
        >
          &ldquo;{intention}&rdquo;
        </blockquote>
      )}

      {/* Context note */}
      {context && (
        <p className="text-xs italic opacity-50 mt-2">{context}</p>
      )}

      {/* Block sections */}
      <div
        className="mt-6"
        style={{
          borderTop: "2px solid var(--ppl-border)",
        }}
      >
        {blocks.map((block, i) => (
          <BlockSection
            key={i}
            raw={block}
            isLast={i === blocks.length - 1}
            zipCode={numericZip}
          />
        ))}
      </div>

      {/* Session summary (shows logged sets for today) */}
      <SessionSummary zipCode={numericZip} />
    </article>
  );
}
