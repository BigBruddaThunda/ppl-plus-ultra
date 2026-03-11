"use client";

// RoomContent — client wrapper for the zoomable room experience

import { ZoomableRoom } from "./ZoomableRoom";
import { WorkoutCard } from "./WorkoutCard";
import type { WorkoutCard as WorkoutCardType, Order, Axis } from "@/types/scl";

interface Props {
  card: WorkoutCardType | null;
  order: Order;
  axis: Axis;
  numericCode: string;
  deckNumber: number;
}

function parseBlocks(content: string): string[] {
  const parts = content.split(/═{3,}/);
  return parts.slice(1).map((b) => b.trim()).filter(Boolean);
}

export function RoomContent({ card, order, axis, numericCode, deckNumber }: Props) {
  const blocks = card ? parseBlocks(card.content) : [];

  if (!card) {
    return (
      <>
        <p className="font-mono text-sm opacity-50">
          This room is being built.
        </p>
        <p className="mt-2 font-mono text-xs opacity-30">
          status: awaiting generation
        </p>
      </>
    );
  }

  return (
    <ZoomableRoom
      blocks={blocks}
      order={order}
      axis={axis}
      currentCode={numericCode}
      deckNumber={deckNumber}
    >
      <WorkoutCard card={card} />
    </ZoomableRoom>
  );
}
