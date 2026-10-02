# QSB live audit — 2026-10-02 04:31 ART

Protected base remains `b59a947d5c4d0ac61d2b1136ffdd7b3362010434`.
Promoted pinning crown remains **1,020,930,406 verified candidates/s**; the 100-bip target remains about **1,031,139,710/s**.

## Newly resolved public experiments

- PR #3059, `QSB_FEED_BLOCK 2 -> 1`: **851,911,076/s**, verifier-valid, large regression. Retire this lever on the live crown.
- PR #3095, stacked `PIPE_LEA=1` + 16-byte root stores + early finish-state discard: **1,005,566,436/s**. Valid but below the crown; do not copy the exact stack.
- PR #3101, single-switch `S2_BLOCKS` experiment: **975,754,969/s**. Valid regression; retire exact setting.
- PR #3142, `QSB_SHA_FMA_ROT`: **866,326,881/s**. Valid large regression; retire.
- PR #3053 half-size packet path remains a large regression at **859,254,461/s**.
- Pepper PR #2830 remains **845,538,485/s**; exact `SLOTS=5 + GREEN_SHARED=12` composition stays retired.

## Pending high-information draws

- PR #3147 tests a host publication-gate two-term EC operation fusion on the promoted pinning base; dispatched, no score observed at this audit.
- PR #3144 tests `QSB_SUB_CUT`; dispatched, no score observed at this audit.
- PR #3150 proposes a much larger tail-schedule transpose plus two exact cuts; awaiting dispatch.
- PR #3137 is a new subset composition; dispatched.

## Decision

Do not spend Pepper's next remote draw on FEED_BLOCK, S2_BLOCKS, SHA_FMA_ROT, the old SLOTS/GREEN_SHARED stack, or the exact #3095 stack. The frontier is mature enough that isolated host-gate changes are worth observing before another submission. A new Pepper candidate should be based on the promoted `0fe76103` source and must either (a) have fresh public ranked evidence near/above the crown, or (b) implement a genuinely orthogonal exact mechanism with a plausible >1% path. Cosmetic redraws are excluded.
