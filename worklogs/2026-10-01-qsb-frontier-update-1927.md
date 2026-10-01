# QSB pinning frontier refresh — 2026-10-01 19:27 ART

## Live promoted frontier
- Promoted source/base: `b59a947d5c4d0ac61d2b1136ffdd7b3362010434`
- Promoted submission: `0fe76103-6afa-41fd-b727-c9b1311186d9`
- Official score: **1,020,930,406 verified candidates/s**
- 100-bip promotion target: **1,031,139,710/s** (rounded upward)

## New authoritative negative evidence
Do not spend Pepper evaluations on these isolated host levers unless materially new evidence appears:

- `QSB_FEED_BLOCK 2 -> 1`: PR #3059 scored **851,911,076/s** (-16.6% class regression).
- `QSB_GREEN_S2_LEAST 0 -> 1`: PR #3077 scored **947,644,051/s** (-7.2% vs crown).
- `QSB_GREEN 20 -> 18`: public result recorded by #3077: **935,738,577/s**.
- `QSB_GREEN_SHARED 8 -> 6`: public result recorded by #3077: **848,459,313/s**.
- `QSB_GREEN_RT_B=1`: older PR #1955 scored **895,549,927/s** on its then-current tree; not a good blind port to the current crown.
- Pepper's prior `SLOTS=5 + GREEN_SHARED=12` composition remains dead: **845,538,485/s**.

## Current experiments worth observing before duplicating
- PR #3084: `QSB_GREEN_SPLIT_FLAGS` ignore-coscheduling flag -> 0 on the current crown. Dispatched; result pending at this refresh.
- PR #3086: isolated `QSB_FIN_IVFOLD` experiment. Dispatched; result pending.
- PR #3087: subset record redraw; not a pinning mechanism candidate for Pepper.

## Decision
No new Pepper submission was fired in this refresh. The current crown has proven unusually sensitive to host scheduling/green-context changes, with several nominally small host-only toggles collapsing throughput. The next Pepper candidate should therefore avoid FEED_BLOCK, GREEN count/shared geometry, finish priority, and root-partition relocation. Prefer a narrow device-side mechanism with positive public evidence on the current lineage, or wait for #3084/#3086 authoritative results before composing anything around them.

This file is an audit checkpoint, not a performance claim.