#!/usr/bin/env python3
"""Contract-first audit entry point.

This script is intentionally scaffolded to lock CLI contracts for future implementation.
It exits non-zero when `--require-implementation` is provided.
"""

import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--path')
    ap.add_argument('--input')
    ap.add_argument('--zip')
    ap.add_argument('--deck')
    ap.add_argument('--fixtures')
    ap.add_argument('--require-implementation', action='store_true')
    args = ap.parse_args()

    print('Entry point defined. Implementation pending.')
    if args.require_implementation:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
