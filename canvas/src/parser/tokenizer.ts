/**
 * Tokenizer — Input normalization and tokenization for the SCL parser
 *
 * Produces unigrams and adjacent bigrams from natural language input.
 * This is the first stage of the scoreText() pipeline.
 *
 * normalizeInput(): lowercase, strip punctuation (preserve hyphens inside words),
 *                   unicode NFD normalization with combining mark removal
 * tokenize(): split normalized input into unigrams + adjacent bigrams
 */

/**
 * Normalize a raw input string for keyword lookup.
 *
 * - Lowercase
 * - NFD unicode normalization, stripping combining marks (accents, diacritics)
 * - Strip punctuation, except hyphens that appear between word characters
 * - Collapse multiple spaces to single space
 * - Trim leading/trailing whitespace
 *
 * @param input  Raw user input string
 * @returns      Normalized string safe for keyword matching
 */
export function normalizeInput(input: string): string {
  if (!input) return '';

  // NFD normalize then strip combining marks (unicode category M)
  let s = input.normalize('NFD').replace(/[\u0300-\u036f]/g, '');

  // Lowercase
  s = s.toLowerCase();

  // Strip punctuation but preserve hyphens between word chars
  // Replace any punctuation that is NOT a hyphen between word chars
  s = s.replace(/[^\w\s-]/g, ' ');

  // Replace hyphens that are NOT between word chars with space
  // (e.g., leading/trailing hyphens, but keep "bench-press")
  s = s.replace(/(?<!\w)-|-(?!\w)/g, ' ');

  // Collapse multiple spaces to single
  s = s.replace(/\s+/g, ' ').trim();

  return s;
}

/**
 * Tokenize a normalized string into unigrams and adjacent bigrams.
 *
 * Input should be the output of normalizeInput().
 * Returns an array of all unique tokens: individual words plus all
 * adjacent 2-word combinations.
 *
 * Example: "heavy barbell back" → ["heavy", "barbell", "back",
 *                                   "heavy barbell", "barbell back"]
 *
 * @param normalized  Output of normalizeInput()
 * @returns           Array of unigram and bigram tokens (no dedup needed — lookup is a dict hit)
 */
export function tokenize(normalized: string): string[] {
  if (!normalized) return [];

  const words = normalized.split(/\s+/).filter(w => w.length > 0);
  if (words.length === 0) return [];

  const tokens: string[] = [...words];

  // Adjacent bigrams
  for (let i = 0; i < words.length - 1; i++) {
    tokens.push(`${words[i]} ${words[i + 1]}`);
  }

  return tokens;
}
