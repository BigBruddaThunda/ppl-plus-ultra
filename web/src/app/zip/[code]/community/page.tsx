import { notFound } from "next/navigation";
import { parseNumericZip } from "@/lib/scl";
import type { Metadata } from "next";

interface Props {
  params: Promise<{ code: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) return { title: "Community | Ppl±" };
  return { title: `Community — ${zip.raw} | Ppl±` };
}

export default async function CommunityFloor({ params }: Props) {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) notFound();

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
        🐬 Sociatas
      </h2>
      <p className="text-sm opacity-50 mt-2">
        Community features coming in a future wave.
      </p>
    </section>
  );
}
