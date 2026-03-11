"use client";

// ZoomableRoom — wraps room content with pinch/wheel zoom
// 1x = normal room view, 0.5x = block chips, 0.25x = deck map

import { useState, useCallback, useRef, type ReactNode } from "react";
import { useGesture } from "@use-gesture/react";
import { BlockChips } from "./BlockChips";
import { DeckMap } from "./DeckMap";
import type { Order, Axis } from "@/types/scl";

type ZoomLevel = "room" | "blocks" | "deck";

interface Props {
  children: ReactNode;
  blocks: string[];
  order: Order;
  axis: Axis;
  currentCode: string;
  deckNumber: number;
}

const ZOOM_ORDER: ZoomLevel[] = ["room", "blocks", "deck"];

export function ZoomableRoom({ children, blocks, order, axis, currentCode, deckNumber }: Props) {
  const [zoom, setZoom] = useState<ZoomLevel>("room");
  const containerRef = useRef<HTMLDivElement>(null);
  const blockRefs = useRef<(HTMLElement | null)[]>([]);

  const zoomOut = useCallback(() => {
    setZoom((prev) => {
      const idx = ZOOM_ORDER.indexOf(prev);
      return idx < ZOOM_ORDER.length - 1 ? ZOOM_ORDER[idx + 1] : prev;
    });
  }, []);

  const zoomIn = useCallback(() => {
    setZoom((prev) => {
      const idx = ZOOM_ORDER.indexOf(prev);
      return idx > 0 ? ZOOM_ORDER[idx - 1] : prev;
    });
  }, []);

  // Bind pinch and wheel gestures
  useGesture(
    {
      onPinch: ({ offset: [scale], direction: [dir] }) => {
        if (dir < 0 && scale < 0.7) zoomOut();
        if (dir > 0 && scale > 1.3) zoomIn();
      },
      onWheel: ({ direction: [, dy], ctrlKey }) => {
        // Only zoom on ctrl+wheel (trackpad pinch fires as ctrl+wheel)
        if (!ctrlKey) return;
        if (dy > 0) zoomOut();
        if (dy < 0) zoomIn();
      },
    },
    {
      target: containerRef,
      eventOptions: { passive: false },
      pinch: { scaleBounds: { min: 0.2, max: 2 } },
    }
  );

  function handleBlockSelect(index: number) {
    setZoom("room");
    // Scroll to block after a tick (allows render)
    requestAnimationFrame(() => {
      const el = blockRefs.current[index];
      if (el) {
        el.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  }

  return (
    <div ref={containerRef} className="relative touch-pan-y">
      {/* Zoom indicator */}
      <div className="mb-3 flex items-center gap-1.5">
        {ZOOM_ORDER.map((level) => (
          <button
            key={level}
            onClick={() => setZoom(level)}
            className={`rounded-full px-2.5 py-0.5 text-[10px] font-medium transition-all ${
              zoom === level
                ? "bg-[var(--ppl-accent)] text-[var(--ppl-background)]"
                : "border border-[var(--ppl-border)] opacity-40 hover:opacity-70"
            }`}
          >
            {level === "room" ? "1x Room" : level === "blocks" ? "Blocks" : "Deck"}
          </button>
        ))}
        <span className="ml-auto text-[10px] opacity-30">pinch to zoom</span>
      </div>

      {/* Room view (1x) */}
      {zoom === "room" && (
        <div className="animate-in fade-in duration-200">
          {children}
        </div>
      )}

      {/* Block chips view (0.5x) */}
      {zoom === "blocks" && (
        <div className="animate-in fade-in duration-200">
          <p className="mb-3 text-xs font-medium uppercase tracking-widest opacity-50">
            Block Overview
          </p>
          <BlockChips blocks={blocks} onSelect={handleBlockSelect} />
          <p className="mt-4 text-center text-[10px] opacity-30">
            Tap a block to jump in &middot; Pinch out for deck map
          </p>
        </div>
      )}

      {/* Deck map view (0.25x) */}
      {zoom === "deck" && (
        <div className="animate-in fade-in duration-200">
          <p className="mb-3 text-xs font-medium uppercase tracking-widest opacity-50">
            Deck Map
          </p>
          <DeckMap
            order={order}
            axis={axis}
            currentCode={currentCode}
            deckNumber={deckNumber}
          />
          <p className="mt-4 text-center text-[10px] opacity-30">
            Tap a room to enter &middot; Pinch in for blocks
          </p>
        </div>
      )}
    </div>
  );
}
