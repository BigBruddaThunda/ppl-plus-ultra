"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

interface Floor {
  emoji: string;
  latin: string;
  label: string;
  path: string; // relative to /zip/[code]
}

const FLOORS: Floor[] = [
  { emoji: "🏛", latin: "Firmitas", label: "Workout", path: "" },
  { emoji: "🔨", latin: "Utilitas", label: "Tools", path: "/tools" },
  { emoji: "🪐", latin: "Gravitas", label: "Deep", path: "/deep" },
  { emoji: "⌛", latin: "Temporitas", label: "Time", path: "/time" },
  { emoji: "🌹", latin: "Venustas", label: "Personal", path: "/personal" },
  { emoji: "🐬", latin: "Sociatas", label: "Community", path: "/community" },
];

interface FloorSelectorProps {
  zipCode: string; // numeric code e.g. "2123"
}

export function FloorSelector({ zipCode }: FloorSelectorProps) {
  const pathname = usePathname();
  const basePath = `/zip/${zipCode}`;

  return (
    <nav
      className="flex gap-1 mt-4 overflow-x-auto"
      style={{ scrollbarWidth: "none" }}
    >
      {FLOORS.map((floor) => {
        const href = `${basePath}${floor.path}`;
        // Active: exact match for root, startsWith for sub-floors
        const isActive = floor.path === ""
          ? pathname === basePath
          : pathname.startsWith(href);

        return (
          <Link
            key={floor.path}
            href={href}
            className="flex flex-col items-center px-3 py-2 rounded-lg transition-all shrink-0"
            style={{
              opacity: isActive ? 1 : 0.4,
              background: isActive ? "var(--ppl-surface)" : "transparent",
              border: isActive ? "1px solid var(--ppl-border)" : "1px solid transparent",
            }}
            title={floor.latin}
          >
            <span className="text-lg leading-none">{floor.emoji}</span>
            <span className="text-[9px] font-mono mt-0.5">{floor.latin}</span>
          </Link>
        );
      })}
    </nav>
  );
}
