# PPL± Zip Web

This file is the navigational map for all 1,680 PPL± zip codes.
Each center zip is a room with 4 directional doors (N, W, S, E) to neighboring zips.

## Entry Format (strict)

Each entry uses exactly this structure:

```md
[zip]±[operator] [Title].md
N: [zip]±[operator] [Title].md
W: [zip]±[operator] [Title].md
S: [zip]±[operator] [Title].md
E: [zip]±[operator] [Title].md
```

Rules:
- One blank line between entries.
- For generated cards, use the exact filename from `cards/`.
- For ungenerated cards, use `[pending]` as the title.
- Operator is derived from Axis × Color polarity.

## Enumeration Order (for full build)

Group entries by deck in canonical Order × Axis sequence:
1. 🐂🏛  2. 🐂🔨  3. 🐂🌹  4. 🐂🪐  5. 🐂⌛  6. 🐂🐬
7. ⛽🏛  8. ⛽🔨  9. ⛽🌹 10. ⛽🪐 11. ⛽⌛ 12. ⛽🐬
13. 🦋🏛 14. 🦋🔨 15. 🦋🌹 16. 🦋🪐 17. 🦋⌛ 18. 🦋🐬
19. 🏟🏛 20. 🏟🔨 21. 🏟🌹 22. 🏟🪐 23. 🏟⌛ 24. 🏟🐬
25. 🌾🏛 26. 🌾🔨 27. 🌾🌹 28. 🌾🪐 29. 🌾⌛ 30. 🌾🐬
31. ⚖🏛 32. ⚖🔨 33. ⚖🌹 34. ⚖🪐 35. ⚖⌛ 36. ⚖🐬
37. 🖼🏛 38. 🖼🔨 39. 🖼🌹 40. 🖼🪐 41. 🖼⌛ 42. 🖼🐬

Within each deck:
- Type order: 🛒, 🪡, 🍗, ➕, ➖
- Color order: ⚫, 🟢, 🔵, 🟣, 🔴, 🟠, 🟡, ⚪

## Scaffold Checklist

- [x] Create zip-web.md with header and format explanation
- [ ] Enumerate all 1,680 zip code entries with blank N/W/S/E slots, grouped by deck
- [ ] Fill in operator emojis and Latin names for all 1,680 entries using the Axis × Color polarity table
- [ ] Fill in actual titles for all 40 Deck 07 entries from cards/⛽-strength/🏛-basics/
- [ ] Mark all non-Deck-07 entries with [pending] titles
