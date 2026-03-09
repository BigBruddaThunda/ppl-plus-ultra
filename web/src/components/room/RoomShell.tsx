import type { ZipCode } from "@/types/scl";
import { getFullZipStyle, getContentMaxWidth } from "@/lib/design-system";

interface Props {
  zip: ZipCode;
  children: React.ReactNode;
}

export function RoomShell({ zip, children }: Props) {
  const style = getFullZipStyle(zip);
  const maxWidth = getContentMaxWidth(zip.order);

  return (
    <div
      className="min-h-screen bg-[var(--ppl-background)] text-[var(--ppl-text)]"
      style={style as React.CSSProperties}
      data-zip={zip.numeric}
      data-order={zip.order}
      data-color={zip.color}
    >
      <div
        className="mx-auto px-6"
        style={{
          maxWidth,
          paddingTop: "var(--ppl-space-2xl)",
          paddingBottom: "var(--ppl-space-2xl)",
        }}
      >
        {children}
      </div>
    </div>
  );
}
