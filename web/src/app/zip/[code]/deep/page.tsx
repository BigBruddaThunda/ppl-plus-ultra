import { notFound } from "next/navigation";
import { parseNumericZip } from "@/lib/scl";
import { existsSync, readFileSync } from "fs";
import { join } from "path";
import type { Metadata } from "next";

interface Props {
  params: Promise<{ code: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) return { title: "Deep | Ppl±" };
  return { title: `Deep — ${zip.raw} | Ppl±` };
}

export default async function DeepFloor({ params }: Props) {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) notFound();

  const deckNum = String(zip.deck).padStart(2, "0");
  const cosmogramPath = join(
    process.cwd(),
    "..",
    "deck-cosmograms",
    `deck-${deckNum}-cosmogram.md`
  );

  let excerpt: string | null = null;
  if (existsSync(cosmogramPath)) {
    const content = readFileSync(cosmogramPath, "utf-8");
    // Extract first non-frontmatter section (skip YAML front matter)
    const body = content.replace(/^---[\s\S]*?---\n/, "");
    const lines = body.split("\n").slice(0, 20);
    if (lines.some((l) => l.trim().length > 0)) {
      excerpt = lines.join("\n").trim();
    }
  }

  return (
    <section
      className="rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)]"
      style={{
        marginTop: "var(--ppl-space-lg)",
        padding: "var(--ppl-space-lg)",
        borderRadius: "var(--ppl-radius-md)",
      }}
    >
      <h2 className="text-lg font-semibold mb-1">
        🪐 Gravitas
      </h2>
      <p className="text-xs font-mono opacity-40 mb-4">
        Deck {deckNum} deep context
      </p>

      {excerpt ? (
        <div className="text-sm whitespace-pre-wrap opacity-80">
          {excerpt}
        </div>
      ) : (
        <p className="text-sm opacity-50 italic">
          Deep content for Deck {deckNum} is being researched.
        </p>
      )}
    </section>
  );
}
