# Ranked evidence — 2026-09-29 21:41 ART

## Live frontier
- Pinning promoted score remains **1,008,206,828/s** on current validation PRs based on `ff27a2b`.
- 100-bip promotion floor: **1,018,288,897/s**.
- Subset current best shown in current queue: **728,337,167/s**.

## New measured evidence
- PR #2483 (24-SM finish partition on a 1,011,114,699/s donor composition) is closed without promotion. Its own note estimated the composition near 1,015M/s and explicitly below the 1,018.3M floor. Do not pursue this partition as the missing gain.
- PR #2481 / `374fd563` reports deterministic GPU work around **1,005.02M/s** versus record-family **1,002.96M/s**, about **+0.21% GPU work** for the SHA-256 LEA.HI package.
- PR #2507 reports the SHA-LEA + finish-LEA composition at **1,011.93M/s official score** and deterministic GPU work **1,004.91M/s**, only about **+0.19%** over the record-family deterministic GPU work. It was rejected below the ~1,018.3M floor. This combination is therefore not sufficient.
- PR #2493's host-only radix-2^29 AVX2 co-grinder claims ~**+0.09% total score** from public same-host evidence. A fresh redraw of that host-only change is currently open as PR #2508; wait for its official result before treating it as a clean donor.

## Decision
Do **not** spend a Yukon evaluation on:
1. 24-SM finish partition,
2. SHA_LEA + FIN_LEA alone,
3. a redraw/duplicate of the currently queued host-only co-grinder.

The measured deterministic gap remains roughly 0.8% beyond the best clean GPU package. A candidate should only be frozen if a new orthogonal mechanism has ranked or tightly controlled evidence large enough that the composition can plausibly clear the 1% gate with margin.

## Next implementation target
Audit newly completed/open tickets for an orthogonal >=0.6–0.8% mechanism on the current record lineage, prioritizing:
- prepare/root arithmetic or memory-traffic reductions that do not overlap SHA_LEA,
- GPU/CPU work that is provably disjoint from the current co-grinder,
- changes with exact hit-set verification and current-base carrier evidence.

Avoid no-op draw tags and source-only redraws: they add queue load but no expected deterministic gain.
