# Ppl± Codespaces Quickstart

This quickstart is for first-time terminal users.

## 1) Open the repository
Go to `github.com/BigBruddaThunda/ppl-plus-ultra`.

## 2) Create a Codespace
Click the green **Code** button, then open the **Codespaces** tab, then click **Create codespace on main**.

## 3) Wait for setup
Wait about 60 seconds while the environment builds.

## 4) Use browser VS Code
A VS Code editor opens in your browser with a terminal at the bottom.

## 5) Run core project commands
Paste each command into the terminal and press Enter.

- `python scripts/inventory.py`
  - Expected output: a summary of card inventory counts across statuses/decks.
- `python scripts/deck-readiness.py`
  - Expected output: deck readiness and completion metrics in the terminal.
- `python scripts/middle-math/zip_converter.py --convert 2131`
  - Expected output: conversion details for zip code `2131` between numeric and emoji formats.
- `bash scripts/run-full-audit.sh cards/⛽-strength/🏛-basics`
  - Expected output: a full audit report for that deck folder, including validator/lint checks.

## Notes
- You get **60 free hours per month**.
- The Codespace auto-stops after **30 minutes of inactivity**.
- You can restart it later from the **Codespaces** tab.
- You can also open a Codespace from the GitHub mobile app (limited terminal, but functional for running scripts).
