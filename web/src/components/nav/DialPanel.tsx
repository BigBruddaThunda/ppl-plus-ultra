"use client";

import { useState, useCallback } from "react";
import { motion } from "framer-motion";
import { ZipDial } from "./ZipDial";
import type { DialItem } from "./ZipDial";

// SCL dial data
const ORDERS: DialItem[] = [
  { emoji: "🐂", label: "Foundation", index: 0 },
  { emoji: "⛽", label: "Strength", index: 1 },
  { emoji: "🦋", label: "Hypertrophy", index: 2 },
  { emoji: "🏟", label: "Performance", index: 3 },
  { emoji: "🌾", label: "Full Body", index: 4 },
  { emoji: "⚖", label: "Balance", index: 5 },
  { emoji: "🖼", label: "Restoration", index: 6 },
];

const AXES: DialItem[] = [
  { emoji: "🏛", label: "Basics", index: 0 },
  { emoji: "🔨", label: "Functional", index: 1 },
  { emoji: "🌹", label: "Aesthetic", index: 2 },
  { emoji: "🪐", label: "Challenge", index: 3 },
  { emoji: "⌛", label: "Time", index: 4 },
  { emoji: "🐬", label: "Partner", index: 5 },
];

const TYPES: DialItem[] = [
  { emoji: "🛒", label: "Push", index: 0 },
  { emoji: "🪡", label: "Pull", index: 1 },
  { emoji: "🍗", label: "Legs", index: 2 },
  { emoji: "➕", label: "Plus", index: 3 },
  { emoji: "➖", label: "Ultra", index: 4 },
];

const COLORS: DialItem[] = [
  { emoji: "⚫", label: "Teaching", index: 0 },
  { emoji: "🟢", label: "Bodyweight", index: 1 },
  { emoji: "🔵", label: "Structured", index: 2 },
  { emoji: "🟣", label: "Technical", index: 3 },
  { emoji: "🔴", label: "Intense", index: 4 },
  { emoji: "🟠", label: "Circuit", index: 5 },
  { emoji: "🟡", label: "Fun", index: 6 },
  { emoji: "⚪", label: "Mindful", index: 7 },
];

interface DialPanelProps {
  initialOrder?: number;
  initialAxis?: number;
  initialType?: number;
  initialColor?: number;
  onNavigate: (numericCode: string) => void;
  onClose: () => void;
}

export function DialPanel({
  initialOrder = 0,
  initialAxis = 0,
  initialType = 0,
  initialColor = 0,
  onNavigate,
  onClose,
}: DialPanelProps) {
  const [order, setOrder] = useState(initialOrder);
  const [axis, setAxis] = useState(initialAxis);
  const [type, setType] = useState(initialType);
  const [color, setColor] = useState(initialColor);

  const handleGo = useCallback(() => {
    // Numeric code: 1-indexed positions
    const code = `${order + 1}${axis + 1}${type + 1}${color + 1}`;
    onNavigate(code);
  }, [order, axis, type, color, onNavigate]);

  const previewEmoji = `${ORDERS[order].emoji}${AXES[axis].emoji}${TYPES[type].emoji}${COLORS[color].emoji}`;
  const previewCode = `${order + 1}${axis + 1}${type + 1}${color + 1}`;

  return (
    <>
      {/* Backdrop */}
      <motion.div
        className="fixed inset-0 bg-black/40 z-40"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        onClick={onClose}
      />

      {/* Panel */}
      <motion.div
        className="fixed bottom-0 left-0 right-0 z-50 bg-neutral-900 text-white rounded-t-2xl"
        initial={{ y: "100%" }}
        animate={{ y: 0 }}
        exit={{ y: "100%" }}
        transition={{ type: "spring", damping: 25, stiffness: 300 }}
      >
        {/* Handle */}
        <div className="flex justify-center pt-3 pb-1">
          <div className="w-10 h-1 rounded-full bg-white/20" />
        </div>

        {/* Preview line */}
        <div className="text-center pb-2">
          <span className="text-xl tracking-wider">{previewEmoji}</span>
          <span className="text-xs font-mono opacity-40 ml-2">/{previewCode}</span>
        </div>

        {/* 4 dials */}
        <div className="flex justify-center gap-2 px-4 pb-4">
          <ZipDial label="Order" items={ORDERS} selected={order} onChange={setOrder} />
          <ZipDial label="Axis" items={AXES} selected={axis} onChange={setAxis} />
          <ZipDial label="Type" items={TYPES} selected={type} onChange={setType} />
          <ZipDial label="Color" items={COLORS} selected={color} onChange={setColor} />
        </div>

        {/* Actions */}
        <div className="flex gap-3 px-6 pb-6">
          <button
            onClick={onClose}
            className="flex-1 py-3 rounded-lg bg-white/10 text-sm font-mono hover:bg-white/15 transition-colors"
          >
            Cancel
          </button>
          <button
            onClick={handleGo}
            className="flex-1 py-3 rounded-lg bg-white text-black text-sm font-semibold hover:bg-white/90 transition-colors"
          >
            Go →
          </button>
        </div>
      </motion.div>
    </>
  );
}
