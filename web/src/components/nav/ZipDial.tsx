"use client";

import { useRef, useCallback } from "react";

export interface DialItem {
  emoji: string;
  label: string;
  index: number;
}

interface ZipDialProps {
  label: string;
  items: DialItem[];
  selected: number;
  onChange: (index: number) => void;
}

const ITEM_HEIGHT = 52; // px per dial position

export function ZipDial({ label, items, selected, onChange }: ZipDialProps) {
  const scrollRef = useRef<HTMLDivElement>(null);

  const handleClick = useCallback(
    (index: number) => {
      onChange(index);
    },
    [onChange]
  );

  return (
    <div className="flex flex-col items-center" style={{ minWidth: 72 }}>
      <p className="text-[10px] font-mono uppercase tracking-wider opacity-40 mb-2">
        {label}
      </p>
      <div
        ref={scrollRef}
        className="flex flex-col items-center gap-0 overflow-y-auto"
        style={{
          height: ITEM_HEIGHT * 3,
          scrollSnapType: "y mandatory",
          scrollbarWidth: "none",
        }}
      >
        {items.map((item) => {
          const isSelected = item.index === selected;
          return (
            <button
              key={item.index}
              onClick={() => handleClick(item.index)}
              className="flex flex-col items-center justify-center shrink-0 transition-all"
              style={{
                height: ITEM_HEIGHT,
                width: "100%",
                scrollSnapAlign: "center",
                opacity: isSelected ? 1 : 0.3,
                transform: isSelected ? "scale(1.15)" : "scale(0.9)",
              }}
            >
              <span className="text-2xl leading-none">{item.emoji}</span>
              <span className="text-[9px] font-mono mt-0.5 opacity-70 truncate max-w-[64px]">
                {item.label}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
}
