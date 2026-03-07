#!/usr/bin/env python3
"""Run batch generation across all deck rounds."""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK_SCRIPT = ROOT / "scripts" / "batch-generate-deck.py"
REPORTS_DIR = ROOT / "reports" / "batch-gen"

ROUNDS = [
    ("🐂 Foundation", [2, 3, 4, 5, 6]),
    ("⛽ Strength", [11]),
    ("🦋 Hypertrophy", [13, 14, 15, 16, 17, 18]),
    ("🏟 Performance", [19, 20, 21, 22, 23, 24]),
    ("🌾 Full Body", [25, 26, 27, 28, 29, 30]),
    ("⚖ Balance", [31, 32, 33, 34, 35, 36]),
    ("🖼 Restoration", [37, 38, 39, 40, 41, 42]),
]


def run_all(generator_cmd: str | None, limit_per_deck: int | None, dry_run: bool) -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = REPORTS_DIR / "batch-run-progress.json"

    data: dict[str, object] = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dry_run": dry_run,
        "rounds": [],
    }

    for round_name, decks in ROUNDS:
        round_row: dict[str, object] = {"name": round_name, "decks": []}
        for deck in decks:
            cmd = ["python", str(DECK_SCRIPT), "--deck", str(deck)]
            if generator_cmd:
                cmd.extend(["--generator-cmd", generator_cmd])
            if limit_per_deck:
                cmd.extend(["--limit", str(limit_per_deck)])
            if dry_run:
                cmd.append("--dry-run")

            result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
            ok = result.returncode == 0
            round_row["decks"].append(
                {
                    "deck": deck,
                    "ok": ok,
                    "stdout": result.stdout,
                    "stderr": result.stderr,
                    "command": " ".join(cmd),
                }
            )
            status = "PASS" if ok else "FAIL"
            print(f"Deck {deck:02d}: {status}")
            if not ok:
                print(result.stderr.strip())
        data["rounds"].append(round_row)

    summary_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Run batch generation across all deck rounds.")
    parser.add_argument("--generator-cmd", help="Forwarded to batch-generate-deck.py")
    parser.add_argument("--limit-per-deck", type=int, help="Process only first N EMPTY stubs per deck")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out = run_all(args.generator_cmd, args.limit_per_deck, args.dry_run)
    print(f"Wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
