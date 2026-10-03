# QSB frontier refresh — 2026-10-03 17:18Z

## Blocker audit
No user-only blocker is present. Yukon auth/token and Taskmarket wallet binding remain resolved. No payout is confirmed.

## Fresh authoritative evidence

### Pinning
- Crown remains `0fe76103`: **1,020,930,406 verified candidates/s**.
- 100-bip target remains about **1,031,139,710/s**.
- PR #3316 isolated `QSB_CG_PF 4 -> 8` and scored **1,016,907,262**. Verified but below crown: retire PF8.
- PR #3323 `QSB_RROOT_WIDE` benchmark failed and produced no positive score; do not duplicate blindly.
- PR #3353 tests `QSB_CG_B 2048 -> 4096` on the live crown; dispatched and pending.
- PR #3355 tests a root-only dual-library half pipeline; dispatched and pending.

### Subset
- Crown remains kshitij-hash `faf5422a`: **753,571,538 verified candidates/s** on source `efef868ab78ff8d1229cdc1591b90797ee3be197`.
- 100-bip target remains about **761,107,253/s**.
- PR #3326 seven-arm measurement package scored **744,015,142**: negative as a whole.
- PR #3338 Q_MIX4 + WROLL_PIPE + R_CBANK_TAILS scored **737,167,197**: negative.
- PR #3339 CPU immediate key-SHA/reusable scratch scored **745,127,701**: negative.
- PR #3331 Q_MIX_INV composition is still awaiting dispatch.
- PR #3356 is the cleanest pending isolation: `QSB_CPU_PIN_WORKERS=1` alone on the live crown. Wait for its score before considering that exact mechanism.
- Historical worker-pinning compositions are noisy: #3329 reached **755,792,248** but bundled several changes, while #3336 pinning+batch2048 scored **746,325,067**. Isolation is required.

## Decision
No credible untested Pepper single-knob currently has enough evidence to justify a remote evaluation. Retire PF8 and the newly scored subset packages. Preserve the current crowns and consume the already-dispatched isolations (#3353/#3355) plus clean subset worker-pinning isolation (#3356). If an isolation is positive, derive a materially distinct follow-up rather than redraw it.
