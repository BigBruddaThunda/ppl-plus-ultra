import { notFound } from "next/navigation";
import { parseNumericZip } from "@/lib/scl";
import { RoomHeader } from "@/components/room/RoomHeader";
import { RoomShell } from "@/components/room/RoomShell";
import { FloorSelector } from "@/components/room/FloorSelector";
import { Breadcrumb } from "@/components/nav/Breadcrumb";

interface Props {
  params: Promise<{ code: string }>;
  children: React.ReactNode;
}

export default async function ZipLayout({ params, children }: Props) {
  const { code } = await params;
  const zip = parseNumericZip(code);
  if (!zip) notFound();

  return (
    <RoomShell zip={zip}>
      <Breadcrumb items={[
        { label: `Deck ${String(zip.deck).padStart(2, "0")}`, href: `/deck/${zip.deck}` },
        { label: `Room ${code}` },
      ]} />
      <RoomHeader zip={zip} />
      <FloorSelector zipCode={zip.numeric} />
      {children}
    </RoomShell>
  );
}
