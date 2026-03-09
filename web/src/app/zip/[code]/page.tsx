import { notFound } from "next/navigation";
import { parseNumericZip } from "@/lib/scl";
import { getZipCSSVars, COLOR_TOKENS, ORDER_TOKENS } from "@/lib/tokens";
import { RoomHeader } from "@/components/room/RoomHeader";
import { RoomShell } from "@/components/room/RoomShell";
import type { Metadata } from "next";

interface Props {
  params: Promise<{ code: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) return { title: "Room Not Found | PPL±" };

  const c = COLOR_TOKENS[zip.color];
  const o = ORDER_TOKENS[zip.order];

  return {
    title: `${zip.raw} — ${o.scl_name} ${c.scl_name} | PPL±`,
    description: `${o.scl_name} × ${c.scl_name} workout room. Deck ${zip.deck}.`,
  };
}

export default async function ZipPage({ params }: Props) {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) notFound();

  const cssVars = getZipCSSVars(zip.color, zip.order);

  return (
    <div style={cssVars as React.CSSProperties}>
      <RoomShell zip={zip}>
        <RoomHeader zip={zip} />

        <section className="mt-8 rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] p-6">
          <p className="font-mono text-sm opacity-50">
            Card content will render here once the .md → MDX pipeline is connected.
          </p>
          <p className="mt-2 font-mono text-xs opacity-30">
            status: awaiting card loader
          </p>
        </section>
      </RoomShell>
    </div>
  );
}
