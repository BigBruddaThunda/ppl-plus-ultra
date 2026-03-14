/**
 * block-styles.ts — Block container style map for the 22 SCL blocks
 *
 * RNDR-06: Static mapping of all 22 block slugs to CSS container descriptors,
 * grouped by the four operational functions encoded in the BLOCKS const.
 *
 * This is a static map — it does NOT react to the weight vector. Dynamic
 * theming is handled by --ppl-theme-* CSS variables set by weightsToCSSVars().
 * Block styles describe structural/functional character, not the color theme.
 *
 * Operational functions (from BLOCKS const roles):
 *   Orientation (2):   warm-up, intention
 *   Access (5):        fundamentals, circulation, primer, gambit, progression
 *   Transformation (11): bread-butter, composition, exposure, aram, gutter,
 *                         vanity, sculpt, craft, supplemental, sandbox, reformance
 *   Retention (3):     release, imprint, junction
 *   Modifier (1):      choice
 *
 * paddingMultiplier: orientation=1.0, access=0.9, transformation=1.0,
 *                    retention=0.8, modifier=0.85
 * emphasisLevel: 'high' only for bread-butter (main work block)
 *                'medium' for intention and primary transformation blocks
 *                'low' for all access, retention, and modifier blocks
 */

import { BLOCKS } from '../types/scl.js';

// Verify the import is used (satisfies type check)
void BLOCKS;

type BlockRole = 'orientation' | 'access' | 'transformation' | 'retention' | 'modifier';

export interface BlockContainerStyle {
  role: BlockRole;
  cssClass: string;
  borderAccent: string;
  paddingMultiplier: number;
  emphasisLevel: 'low' | 'medium' | 'high';
}

/**
 * BLOCK_CONTAINER_STYLES maps every block slug (from BLOCKS const) to its
 * container style descriptor. 22 entries covering all 4 operational roles
 * plus the modifier role.
 */
export const BLOCK_CONTAINER_STYLES: Record<string, BlockContainerStyle> = {
  // ─── Orientation (2 blocks) — framing, arriving, pointing intent ──────────
  'warm-up': {
    role: 'orientation',
    cssClass: 'ppl-block--orientation',
    borderAccent: 'var(--ppl-theme-accent)',
    paddingMultiplier: 1.0,
    emphasisLevel: 'low',
  },
  'intention': {
    role: 'orientation',
    cssClass: 'ppl-block--orientation',
    borderAccent: 'var(--ppl-theme-accent)',
    paddingMultiplier: 1.0,
    emphasisLevel: 'medium',
  },

  // ─── Access (5 blocks) — mobility, activation, priming ───────────────────
  'fundamentals': {
    role: 'access',
    cssClass: 'ppl-block--access',
    borderAccent: 'var(--ppl-theme-secondary)',
    paddingMultiplier: 0.9,
    emphasisLevel: 'low',
  },
  'circulation': {
    role: 'access',
    cssClass: 'ppl-block--access',
    borderAccent: 'var(--ppl-theme-secondary)',
    paddingMultiplier: 0.9,
    emphasisLevel: 'low',
  },
  'primer': {
    role: 'access',
    cssClass: 'ppl-block--access',
    borderAccent: 'var(--ppl-theme-secondary)',
    paddingMultiplier: 0.9,
    emphasisLevel: 'low',
  },
  'gambit': {
    role: 'access',
    cssClass: 'ppl-block--access',
    borderAccent: 'var(--ppl-theme-secondary)',
    paddingMultiplier: 0.9,
    emphasisLevel: 'low',
  },
  'progression': {
    role: 'access',
    cssClass: 'ppl-block--access',
    borderAccent: 'var(--ppl-theme-secondary)',
    paddingMultiplier: 0.9,
    emphasisLevel: 'low',
  },

  // ─── Transformation (11 blocks) — where capacity is built or tested ───────
  'bread-butter': {
    role: 'transformation',
    cssClass: 'ppl-block--transformation',
    borderAccent: 'var(--ppl-theme-primary)',
    paddingMultiplier: 1.0,
    emphasisLevel: 'high',  // The main work block — highest emphasis
  },
  'composition': {
    role: 'transformation',
    cssClass: 'ppl-block--transformation',
    borderAccent: 'var(--ppl-theme-primary)',
    paddingMultiplier: 1.0,
    emphasisLevel: 'medium',
  },
  'exposure': {
    role: 'transformation',
    cssClass: 'ppl-block--transformation',
    borderAccent: 'var(--ppl-theme-primary)',
    paddingMultiplier: 1.0,
    emphasisLevel: 'medium',
  },
  'aram': {
    role: 'transformation',
    cssClass: 'ppl-block--transformation',
    borderAccent: 'var(--ppl-theme-primary)',
    paddingMultiplier: 1.0,
    emphasisLevel: 'medium',
  },
  'gutter': {
    role: 'transformation',
    cssClass: 'ppl-block--transformation',
    borderAccent: 'var(--ppl-theme-primary)',
    paddingMultiplier: 1.0,
    emphasisLevel: 'high',
  },
  'vanity': {
    role: 'transformation',
    cssClass: 'ppl-block--transformation',
    borderAccent: 'var(--ppl-theme-primary)',
    paddingMultiplier: 1.0,
    emphasisLevel: 'medium',
  },
  'sculpt': {
    role: 'transformation',
    cssClass: 'ppl-block--transformation',
    borderAccent: 'var(--ppl-theme-primary)',
    paddingMultiplier: 1.0,
    emphasisLevel: 'medium',
  },
  'craft': {
    role: 'transformation',
    cssClass: 'ppl-block--transformation',
    borderAccent: 'var(--ppl-theme-primary)',
    paddingMultiplier: 1.0,
    emphasisLevel: 'medium',
  },
  'supplemental': {
    role: 'transformation',
    cssClass: 'ppl-block--transformation',
    borderAccent: 'var(--ppl-theme-primary)',
    paddingMultiplier: 1.0,
    emphasisLevel: 'medium',
  },
  'sandbox': {
    role: 'transformation',
    cssClass: 'ppl-block--transformation',
    borderAccent: 'var(--ppl-theme-primary)',
    paddingMultiplier: 1.0,
    emphasisLevel: 'medium',
  },
  'reformance': {
    role: 'transformation',
    cssClass: 'ppl-block--transformation',
    borderAccent: 'var(--ppl-theme-primary)',
    paddingMultiplier: 1.0,
    emphasisLevel: 'medium',
  },

  // ─── Retention (3 blocks) — locking in, cooling down, bridging forward ────
  'release': {
    role: 'retention',
    cssClass: 'ppl-block--retention',
    borderAccent: 'var(--ppl-theme-border)',
    paddingMultiplier: 0.8,
    emphasisLevel: 'low',
  },
  'imprint': {
    role: 'retention',
    cssClass: 'ppl-block--retention',
    borderAccent: 'var(--ppl-theme-border)',
    paddingMultiplier: 0.8,
    emphasisLevel: 'low',
  },
  'junction': {
    role: 'retention',
    cssClass: 'ppl-block--retention',
    borderAccent: 'var(--ppl-theme-border)',
    paddingMultiplier: 0.8,
    emphasisLevel: 'low',
  },

  // ─── Modifier (1 block) — bounded autonomy modifier ───────────────────────
  'choice': {
    role: 'modifier',
    cssClass: 'ppl-block--modifier',
    borderAccent: 'var(--ppl-theme-surface)',
    paddingMultiplier: 0.85,
    emphasisLevel: 'low',
  },
} as const satisfies Record<string, BlockContainerStyle>;
