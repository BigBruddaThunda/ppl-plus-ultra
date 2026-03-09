import type { ZipCode } from "@/types/scl";

interface Props {
  zip: ZipCode;
  children: React.ReactNode;
}

export function RoomShell({ zip, children }: Props) {
  return (
    <div
      className="min-h-screen bg-[var(--ppl-background)] text-[var(--ppl-text)]"
      data-zip={zip.numeric}
      data-order={zip.order}
      data-color={zip.color}
    >
      <div className="mx-auto max-w-2xl px-6 py-10">
        {children}
      </div>
    </div>
  );
}
