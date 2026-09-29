#!/usr/bin/env python3
"""Rank public Yukon pinning candidates against the live promotion gate.

Paste observed official scores into OBSERVED as they complete. The script keeps
candidate selection deterministic and prevents spending an evaluation on a
known-negative mechanism.
"""
from math import ceil

PROMOTED = 1_008_206_828
MIN_BIPS = 100

OBSERVED = {
    "promoted": PROMOTED,
    "sha_tail_pr2282": 1_012_807_365,
    "weighted_inverse_pr2281": 990_246_114,
}

PENDING = {
    "union_pr2327": "tail interleave + parity-window split + scratch vectorisation",
    "warp_bypass_pr2337": "uniform warp bypass for final sparse correction",
}

floor = ceil(PROMOTED * (10_000 + MIN_BIPS) / 10_000)
print(f"promotion_floor={floor}")
for name, score in sorted(OBSERVED.items(), key=lambda kv: kv[1], reverse=True):
    gap = floor - score
    pct = (score / PROMOTED - 1) * 100
    status = "PROMOTES" if score >= floor else "below"
    print(f"{name:28} {score:>12,}  {pct:+.4f}%  {status}; gap={gap:,}")

print("\nPending candidates:")
for name, mechanism in PENDING.items():
    print(f"- {name}: {mechanism}")
