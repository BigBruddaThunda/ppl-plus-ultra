import { notFound } from "next/navigation";
import { parseNumericZip } from "@/lib/scl";
import { COLOR_TOKENS, ORDER_TOKENS } from "@/lib/tokens";
import { getOrderProportions } from "@/lib/design-system";
import { loadCard } from "@/lib/card-loader";
import { RoomHeader } from "@/components/room/RoomHeader";
import { RoomShell } from "@/components/room/RoomShell";
import { WorkoutCard } from "@/components/room/WorkoutCard";
import type { Metadata } from "next";

interface Props {
  params: Promise<{ code: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) return { title: "Room Not Found | Ppl±" };

  const c = COLOR_TOKENS[zip.color];
  const o = ORDER_TOKENS[zip.order];
  const p = getOrderProportions(zip.order);

  return {
    title: `${zip.raw} — ${o.scl_name} ${c.scl_name} | Ppl±`,
    description: `${o.scl_name} × ${c.scl_name} workout room. ${p.classical} Order. Deck ${zip.deck}.`,
  };
}

export default async function ZipPage({ params }: Props) {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) notFound();

  const card = loadCard(zip);

  return (
    <RoomShell zip={zip}>
      <RoomHeader zip={zip} />

      <section
        className="rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)]"
        style={{
          marginTop: "var(--ppl-space-lg)",
          padding: "var(--ppl-space-lg)",
          borderRadius: "var(--ppl-radius-md)",
          boxShadow: "var(--ppl-shadow-sm)",
        }}
      >
        {card ? (
          <WorkoutCard card={card} />
        ) : (
          <>
            <p className="font-mono text-sm opacity-50">
              This room is being built.
            </p>
            <p className="mt-2 font-mono text-xs opacity-30">
              status: awaiting generation
            </p>
          </>
        )}
      </section>
    </RoomShell>
  );
}
