import { notFound } from "next/navigation";
import { parseNumericZip } from "@/lib/scl";
import type { Metadata } from "next";

interface Props {
  params: Promise<{ code: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) return { title: "Personal | Ppl±" };
  return { title: `Personal — ${zip.raw} | Ppl±` };
}

export default async function PersonalFloor({ params }: Props) {
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
        🌹 Venustas
      </h2>
      <p className="text-sm opacity-50 mt-2">
        Login to see your history here.
      </p>
    </section>
  );
}
