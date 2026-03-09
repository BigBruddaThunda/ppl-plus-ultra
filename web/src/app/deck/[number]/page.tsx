// Deck view — 40 rooms in a deck (5 Types × 8 Colors)

import { notFound } from "next/navigation";
import Link from "next/link";
import {
  ORDER_EMOJI, AXIS_EMOJI, TYPE_EMOJI, COLOR_EMOJI,
  toNumericCode,
} from "@/lib/scl";
import { COLOR_TOKENS, ORDER_TOKENS } from "@/lib/tokens";
import { getOrderProportions, getFullZipStyle } from "@/lib/design-system";
import type { Metadata } from "next";
import type { Order, Axis, Type, Color } from "@/types/scl";

const ORDER_INDEX: Order[] = ["foundation", "strength", "hypertrophy", "performance", "full-body", "balance", "restoration"];
const AXIS_INDEX: Axis[] = ["basics", "functional", "aesthetic", "challenge", "time", "partner"];
const TYPE_INDEX: Type[] = ["push", "pull", "legs", "plus", "ultra"];
const COLOR_INDEX: Color[] = ["teaching", "bodyweight", "structured", "technical", "intense", "circuit", "fun", "mindful"];

function deckToOrderAxis(deck: number): { order: Order; axis: Axis } | null {
  if (deck < 1 || deck > 42) return null;
  const orderIdx = Math.floor((deck - 1) / 6);
  const axisIdx = (deck - 1) % 6;
  return { order: ORDER_INDEX[orderIdx], axis: AXIS_INDEX[axisIdx] };
}

interface Props {
  params: Promise<{ number: string }>;
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { number } = await params;
  const deckNum = parseInt(number, 10);
  const oa = deckToOrderAxis(deckNum);
  if (!oa) return { title: "Deck Not Found | Ppl±" };

  const o = ORDER_TOKENS[oa.order];
  const p = getOrderProportions(oa.order);
  return {
    title: `Deck ${String(deckNum).padStart(2, "0")} — ${o.scl_name} ${AXIS_EMOJI[oa.axis]} | Ppl±`,
    description: `${p.classical} Order. 40 rooms: 5 Types × 8 Colors.`,
  };
}

export default async function DeckPage({ params }: Props) {
  const { number } = await params;
  const deckNum = parseInt(number, 10);
  const oa = deckToOrderAxis(deckNum);
  if (!oa) notFound();

  const { order, axis } = oa;
  const oTokens = ORDER_TOKENS[order];
  const props = getOrderProportions(order);

  // Build a fake zip for the first room to get CSS vars for the page shell
  const shellZip = {
    raw: `${ORDER_EMOJI[order]}${AXIS_EMOJI[axis]}${TYPE_EMOJI["push"]}${COLOR_EMOJI["structured"]}`,
    order, axis, type: "push" as Type, color: "structured" as Color,
    orderEmoji: ORDER_EMOJI[order], axisEmoji: AXIS_EMOJI[axis],
    typeEmoji: TYPE_EMOJI["push"], colorEmoji: COLOR_EMOJI["structured"],
    deck: deckNum, numeric: toNumericCode(order, axis, "push", "structured"),
  };
  const style = getFullZipStyle(shellZip);

  return (
    <div
      className="min-h-screen bg-[var(--ppl-background)] text-[var(--ppl-text)]"
      style={style as React.CSSProperties}
    >
      <div className="mx-auto max-w-4xl px-6" style={{ paddingTop: "var(--ppl-space-2xl)", paddingBottom: "var(--ppl-space-2xl)" }}>
        {/* Header */}
        <Link href="/" className="mb-6 inline-block font-mono text-xs opacity-40 hover:opacity-70">
          ← lobby
        </Link>

        <header className="mb-8">
          <div className="flex items-baseline gap-3">
            <span className="text-4xl">{ORDER_EMOJI[order]}{AXIS_EMOJI[axis]}</span>
            <div>
              <h1 className="text-2xl" style={{ fontWeight: props.fontWeightDisplay }}>
                Deck {String(deckNum).padStart(2, "0")}
              </h1>
              <p className="text-sm opacity-60">
                {oTokens.scl_name} × {AXIS_INDEX[AXIS_INDEX.indexOf(axis)].charAt(0).toUpperCase() + axis.slice(1)} · {props.classical} Order
              </p>
            </div>
          </div>
          <p className="mt-2 font-mono text-xs opacity-40">
            {oTokens.load} · {oTokens.restPeriod} rest · CNS: {oTokens.cns}
          </p>
        </header>

        {/* 40-Room Grid: rows = Types, columns = Colors */}
        <div className="overflow-x-auto">
          <table className="w-full border-collapse">
            <thead>
              <tr>
                <th className="p-2 text-left font-mono text-xs opacity-40">Type</th>
                {COLOR_INDEX.map((color) => (
                  <th key={color} className="p-2 text-center font-mono text-xs opacity-50">
                    {COLOR_EMOJI[color]}
                    <span className="ml-1 hidden sm:inline">{COLOR_TOKENS[color].scl_name}</span>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {TYPE_INDEX.map((type) => (
                <tr key={type} className="border-t border-[var(--ppl-border)]">
                  <td className="p-2 font-mono text-sm">
                    {TYPE_EMOJI[type]} {type.charAt(0).toUpperCase() + type.slice(1)}
                  </td>
                  {COLOR_INDEX.map((color) => {
                    const numCode = toNumericCode(order, axis, type, color);
                    const emoji = `${ORDER_EMOJI[order]}${AXIS_EMOJI[axis]}${TYPE_EMOJI[type]}${COLOR_EMOJI[color]}`;
                    const cTokens = COLOR_TOKENS[color];
                    return (
                      <td key={color} className="p-1 text-center">
                        <Link
                          href={`/zip/${numCode}`}
                          className="block rounded-md border border-[var(--ppl-border)] p-2 transition-all hover:shadow-md"
                          style={{
                            backgroundColor: cTokens.background,
                            borderColor: cTokens.border,
                          }}
                        >
                          <span className="text-sm">{emoji}</span>
                          <span className="block font-mono text-[10px] opacity-40">
                            /{numCode}
                          </span>
                        </Link>
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <p className="mt-6 font-mono text-xs opacity-30 text-center">
          40 rooms · 5 Types × 8 Colors
        </p>
      </div>
    </div>
  );
}
