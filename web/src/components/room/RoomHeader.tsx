import Link from "next/link";
import type { ZipCode } from "@/types/scl";
import { getOperator } from "@/lib/scl";
import { COLOR_TOKENS, ORDER_TOKENS } from "@/lib/tokens";

interface Props {
  zip: ZipCode;
}

export function RoomHeader({ zip }: Props) {
  const operator = getOperator(zip.axis, zip.color);
  const colorToken = COLOR_TOKENS[zip.color];
  const orderToken = ORDER_TOKENS[zip.order];

  return (
    <header>
      <Link
        href="/"
        className="inline-block text-xs font-mono opacity-40 hover:opacity-70 transition-fast"
      >
        ← lobby
      </Link>

      <div className="mt-6">
        {/* Emoji zip code */}
        <p className="text-3xl tracking-wide">
          {zip.orderEmoji}{zip.axisEmoji}{zip.typeEmoji}{zip.colorEmoji}
        </p>

        {/* Operator */}
        <p className="mt-2 text-sm font-mono">
          <span className="opacity-50">±</span>
          <span className="ml-1">{operator.emoji}</span>
          <span className="ml-2 italic opacity-60">{operator.latin}</span>
        </p>

        {/* Numeric code + deck */}
        <p className="mt-1 font-mono text-xs opacity-40">
          /{zip.numeric} · Deck {String(zip.deck).padStart(2, "0")}
        </p>
      </div>

      {/* Parameter badges */}
      <div className="mt-6 flex flex-wrap gap-2">
        <Badge
          label={orderToken.scl_name}
          detail={`${orderToken.load} · ${orderToken.restPeriod} · CNS ${orderToken.cns}`}
          color="var(--ppl-primary)"
        />
        <Badge
          label={colorToken.scl_name}
          detail={`Tier ${colorToken.tier} · GOLD: ${colorToken.gold ? "Yes" : "No"}`}
          color="var(--ppl-primary)"
        />
      </div>
    </header>
  );
}

function Badge({ label, detail, color }: { label: string; detail: string; color: string }) {
  return (
    <div
      className="rounded-md border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-3 py-2"
      style={{ borderLeftColor: color, borderLeftWidth: "3px" }}
    >
      <p className="text-xs font-semibold">{label}</p>
      <p className="text-xs opacity-50">{detail}</p>
    </div>
  );
}
