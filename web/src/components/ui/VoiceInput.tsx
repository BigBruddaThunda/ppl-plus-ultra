"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { scoreInput, routeFromParse } from "@/lib/voice-parser";

export function VoiceInput() {
  const router = useRouter();
  const [query, setQuery] = useState("");
  const [result, setResult] = useState<{ label: string; confidence: number; route: string | null } | null>(null);
  const [listening, setListening] = useState(false);

  function handleParse(value: string) {
    if (!value.trim()) {
      setResult(null);
      return;
    }
    const parsed = scoreInput(value);
    const route = routeFromParse(parsed);
    setResult({ label: parsed.label, confidence: parsed.confidence, route });

    if (parsed.confidence > 0.85 && route) {
      router.push(route);
    }
  }

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (result?.route) {
      router.push(result.route);
    }
  }

  function startListening() {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const w = window as any;
    const SpeechRecognition = w.SpeechRecognition ?? w.webkitSpeechRecognition;
    if (!SpeechRecognition) return;

    const recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";

    recognition.onstart = () => setListening(true);
    recognition.onend = () => setListening(false);
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    recognition.onresult = (event: any) => {
      const transcript = event.results[0][0].transcript;
      setQuery(transcript);
      handleParse(transcript);
    };

    recognition.start();
  }

  return (
    <form onSubmit={handleSubmit} className="w-full">
      <div className="flex gap-2">
        <input
          type="text"
          value={query}
          onChange={(e) => {
            setQuery(e.target.value);
            handleParse(e.target.value);
          }}
          placeholder="heavy pull day..."
          className="flex-1 rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-4 py-2.5 text-sm outline-none focus:border-[var(--ppl-accent)]"
        />
        <button
          type="button"
          onClick={startListening}
          className={`rounded-lg border px-3 py-2.5 text-sm ${
            listening
              ? "border-red-500 bg-red-500/10 text-red-400"
              : "border-[var(--ppl-border)] opacity-50 hover:opacity-100"
          }`}
        >
          {listening ? "..." : "Mic"}
        </button>
      </div>

      {result && query && (
        <div className="mt-2 flex items-center justify-between rounded-lg border border-[var(--ppl-border)] bg-[var(--ppl-surface)] px-4 py-2">
          <div>
            <p className="text-sm font-medium">{result.label}</p>
            <p className="text-[10px] opacity-40">
              Confidence: {Math.round(result.confidence * 100)}%
            </p>
          </div>
          {result.route && (
            <button
              type="submit"
              className="rounded-lg bg-[var(--ppl-accent)] px-4 py-1.5 text-xs font-medium text-[var(--ppl-background)]"
            >
              Go
            </button>
          )}
        </div>
      )}
    </form>
  );
}
