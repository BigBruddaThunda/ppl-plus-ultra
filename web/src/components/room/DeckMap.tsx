"use client";

// DeckMap — 8×5 grid (Colors × Types) for the current deck at 0.25x zoom

import { Fragment } from "react";
import Link from "next/link";
import {
  ORDER_EMOJI, AXIS_EMOJI, TYPE_EMOJI, COLOR_EMOJI,
  toNumericCode,
} from "@/lib/scl";
import { COLOR_TOKENS } from "@/lib/tokens";
import type { Order, Axis, Type, Color } from "@/types/scl";

const TYPE_INDEX: Type[] = ["push", "pull", "legs", "plus", "ultra"];
const COLOR_INDEX: Color[] = ["teaching", "bodyweight", "structured", "technical", "intense", "circuit", "fun", "mindful"];

interface Props {
  order: Order;
  axis: Axis;
  currentCode: string; // current zip numeric code
  deckNumber: number;
}

export function DeckMap({ order, axis, currentCode, deckNumber }: Props) {
  return (
    <div>
      <div className="mb-3 flex items-baseline gap-2">
        <span className="text-2xl">{ORDER_EMOJI[order]}{AXIS_EMOJI[axis]}</span>
        <span className="text-sm font-medium opacity-70">
          Deck {String(deckNumber).padStart(2, "0")}
        </span>
        <span className="text-xs opacity-40">40 rooms</span>
      </div>

      {/* Color header row */}
      <div className="grid grid-cols-9 gap-1">
        <div className="p-1" />
        {COLOR_INDEX.map((color) => (
          <div key={color} className="p-1 text-center">
            <span className="text-xs">{COLOR_EMOJI[color]}</span>
          </div>
        ))}

        {/* Type rows */}
        {TYPE_INDEX.map((type) => (
          <Fragment key={type}>
            <div className="flex items-center p-1">
              <span className="text-sm">{TYPE_EMOJI[type]}</span>
            </div>
            {COLOR_INDEX.map((color) => {
              const code = toNumericCode(order, axis, type, color);
              const isCurrent = code === currentCode;
              const cTokens = COLOR_TOKENS[color];
              return (
                <Link
                  key={code}
                  href={`/zip/${code}`}
                  className={`rounded border p-1.5 text-center transition-all ${
                    isCurrent
                      ? "ring-2 ring-[var(--ppl-accent)] shadow-md"
                      : "opacity-60 hover:opacity-100 hover:shadow-sm"
                  }`}
                  style={{
                    backgroundColor: cTokens.background,
                    borderColor: isCurrent ? "var(--ppl-accent)" : cTokens.border,
                  }}
                >
                  <span className="text-[10px] font-mono block">{code}</span>
                </Link>
              );
            })}
          </Fragment>
        ))}
      </div>
    </div>
  );
}
