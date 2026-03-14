/**
 * Exercise Dictionary Tests
 *
 * Tests for exercises.json — the ported exercise library with alias layer.
 * These tests validate the ExerciseEntry interface shape and data quality.
 */

import { describe, it, expect } from 'vitest';
import type { ExerciseEntry } from '../src/parser/types';
import exercisesRaw from '../data/exercises.json';

const exercises = exercisesRaw as ExerciseEntry[];

// Valid Type names from scl.ts
const VALID_SCL_TYPES = new Set(['Push', 'Pull', 'Legs', 'Plus', 'Ultra']);

// Sections where gold_gated exercises are permitted (per CLAUDE.md)
// J=Olympic, K=Plyometrics, Q=Strongman, plus specific entries in B, C, D
const GOLD_PERMITTED_SECTIONS = new Set(['J', 'K', 'Q', 'B', 'C', 'D']);

describe('exercises.json — count', () => {
  it('has between 2,000 and 2,200 entries', () => {
    expect(exercises.length).toBeGreaterThanOrEqual(2000);
    expect(exercises.length).toBeLessThanOrEqual(2200);
  });
});

describe('exercises.json — required fields', () => {
  it('every entry has all required fields', () => {
    const missingFields: string[] = [];
    for (const entry of exercises) {
      const required = [
        'id', 'section', 'name', 'scl_types', 'equipment_tier',
        'gold_gated', 'movement_pattern', 'muscle_groups',
        'bilateral', 'compound', 'aliases',
      ];
      for (const field of required) {
        if (!(field in entry)) {
          missingFields.push(`id=${entry.id} missing: ${field}`);
        }
      }
    }
    expect(missingFields).toHaveLength(0);
  });

  it('no entry has order_relevance field (dropped per decision)', () => {
    const withField = exercises.filter(e => 'order_relevance' in e);
    expect(withField).toHaveLength(0);
  });

  it('no entry has axis_emphasis field (dropped per decision)', () => {
    const withField = exercises.filter(e => 'axis_emphasis' in e);
    expect(withField).toHaveLength(0);
  });
});

describe('exercises.json — equipment_tier', () => {
  it('equipment_tier is always a 2-element array [min, max] where min <= max', () => {
    const invalid: string[] = [];
    for (const entry of exercises) {
      const [min, max] = entry.equipment_tier;
      if (entry.equipment_tier.length !== 2) {
        invalid.push(`id=${entry.id} tier length != 2`);
      } else if (min > max) {
        invalid.push(`id=${entry.id} min(${min}) > max(${max})`);
      }
    }
    expect(invalid).toHaveLength(0);
  });
});

describe('exercises.json — scl_types validity', () => {
  it('all scl_types values are valid Type names', () => {
    const invalid: string[] = [];
    for (const entry of exercises) {
      for (const t of entry.scl_types) {
        if (!VALID_SCL_TYPES.has(t)) {
          invalid.push(`id=${entry.id} invalid type: ${t}`);
        }
      }
    }
    expect(invalid).toHaveLength(0);
  });
});

describe('exercises.json — gold_gated constraint', () => {
  it('gold_gated exercises are only in permitted sections (J, K, Q, B, C, D)', () => {
    const violations = exercises.filter(
      e => e.gold_gated && !GOLD_PERMITTED_SECTIONS.has(e.section)
    );
    expect(violations).toHaveLength(0);
  });
});

describe('exercises.json — alias layer', () => {
  it('at least 100 entries have non-empty aliases arrays', () => {
    const withAliases = exercises.filter(e => e.aliases.length > 0);
    expect(withAliases.length).toBeGreaterThanOrEqual(100);
  });

  it('"Romanian Deadlift (RDL)" entry has alias "RDL"', () => {
    const rdl = exercises.find(e => e.name === 'Romanian Deadlift (RDL)');
    expect(rdl).toBeDefined();
    expect(rdl!.aliases).toContain('RDL');
  });

  it('"Romanian Deadlift (RDL)" entry has alias "Romanian Deadlift"', () => {
    const rdl = exercises.find(e => e.name === 'Romanian Deadlift (RDL)');
    expect(rdl).toBeDefined();
    expect(rdl!.aliases).toContain('Romanian Deadlift');
  });

  it('"Barbell Bench Press" entry has alias "bench press"', () => {
    const bench = exercises.find(e => e.name === 'Barbell Bench Press');
    expect(bench).toBeDefined();
    const aliases = bench!.aliases.map(a => a.toLowerCase());
    expect(aliases).toContain('bench press');
  });

  it('"Barbell Bench Press" entry has alias "bench"', () => {
    const bench = exercises.find(e => e.name === 'Barbell Bench Press');
    expect(bench).toBeDefined();
    const aliases = bench!.aliases.map(a => a.toLowerCase());
    expect(aliases).toContain('bench');
  });
});

describe('exercises.json — equipment tier range sanity', () => {
  // The source data uses equipment_tier as [min_possible, max_required] where max indicates
  // the heaviest equipment tier needed for the exercise. Barbell exercises (tier 3) should
  // always have equipment_tier[1] (max) >= 3 — they require at least a barbell.
  it('exercises with "barbell" in name (case-insensitive) have equipment_tier[1] >= 3', () => {
    const barbellExercises = exercises.filter(e =>
      e.name.toLowerCase().includes('barbell')
    );
    const violations = barbellExercises.filter(e => e.equipment_tier[1] < 3);
    expect(violations).toHaveLength(0);
  });
});
