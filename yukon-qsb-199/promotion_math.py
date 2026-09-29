#!/usr/bin/env python3
"""Deterministic promotion math for Yukon QSB evidence triage.

No network access, secrets, or Yukon credentials are required.
"""
from __future__ import annotations
import argparse
import math

def promotion_floor(best: int, bips: int = 100) -> int:
    return math.ceil(best * (10_000 + bips) / 10_000)

def report(best: int, score: int, bips: int = 100) -> str:
    floor = promotion_floor(best, bips)
    delta = score - best
    pct = (delta / best) * 100
    gap = floor - score
    return (
        f"best={best}\n"
        f"promotion_floor={floor}\n"
        f"candidate={score}\n"
        f"delta={delta} ({pct:+.4f}%)\n"
        f"gap_to_floor={max(gap, 0)}\n"
        f"promotable={'yes' if score >= floor else 'no'}"
    )

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("best", type=int)
    p.add_argument("score", type=int)
    p.add_argument("--bips", type=int, default=100)
    a = p.parse_args()
    print(report(a.best, a.score, a.bips))
