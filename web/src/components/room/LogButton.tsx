"use client";

import { useState } from "react";
import { LogOverlay } from "./LogOverlay";

interface LogButtonProps {
  zipCode: string;
  blockName: string;
  exerciseName: string;
}

export function LogButton({ zipCode, blockName, exerciseName }: LogButtonProps) {
  const [open, setOpen] = useState(false);
  const [logged, setLogged] = useState(false);

  return (
    <>
      <button
        onClick={() => setOpen(true)}
        className={`ml-2 inline-flex rounded px-1.5 py-0.5 text-[10px] font-medium transition-colors ${
          logged
            ? "bg-green-500/20 text-green-400"
            : "bg-[var(--ppl-border)] opacity-40 hover:opacity-70"
        }`}
      >
        {logged ? "logged" : "log"}
      </button>
      {open && (
        <LogOverlay
          zipCode={zipCode}
          blockName={blockName}
          exerciseName={exerciseName}
          onClose={() => setOpen(false)}
          onSaved={() => {
            setOpen(false);
            setLogged(true);
          }}
        />
      )}
    </>
  );
}
