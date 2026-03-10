"use client";

import { useState, useCallback } from "react";
import { useRouter, usePathname } from "next/navigation";
import { AnimatePresence } from "framer-motion";
import { DialPanel } from "./DialPanel";

// Parse current zip from URL path like /zip/2123
function parseZipFromPath(pathname: string): {
  order: number;
  axis: number;
  type: number;
  color: number;
} | null {
  const match = pathname.match(/^\/zip\/(\d{4})/);
  if (!match) return null;
  const code = match[1];
  const o = parseInt(code[0]) - 1;
  const a = parseInt(code[1]) - 1;
  const t = parseInt(code[2]) - 1;
  const c = parseInt(code[3]) - 1;
  if (o < 0 || o > 6 || a < 0 || a > 5 || t < 0 || t > 4 || c < 0 || c > 7) {
    return null;
  }
  return { order: o, axis: a, type: t, color: c };
}

export function HomeButton() {
  const [open, setOpen] = useState(false);
  const router = useRouter();
  const pathname = usePathname();

  const currentZip = parseZipFromPath(pathname);

  const handleNavigate = useCallback(
    (code: string) => {
      setOpen(false);
      router.push(`/zip/${code}`);
    },
    [router]
  );

  const handleClose = useCallback(() => {
    setOpen(false);
  }, []);

  return (
    <>
      {/* Floating button */}
      <button
        onClick={() => setOpen(true)}
        className="fixed bottom-6 right-6 z-30 w-14 h-14 rounded-full bg-neutral-900 text-white text-2xl shadow-lg hover:scale-105 transition-transform flex items-center justify-center"
        aria-label="Open zip code navigator"
      >
        <span role="img" aria-hidden="true">&#x1F3E0;</span>
      </button>

      {/* Dial panel overlay */}
      <AnimatePresence>
        {open && (
          <DialPanel
            initialOrder={currentZip?.order}
            initialAxis={currentZip?.axis}
            initialType={currentZip?.type}
            initialColor={currentZip?.color}
            onNavigate={handleNavigate}
            onClose={handleClose}
          />
        )}
      </AnimatePresence>
    </>
  );
}
