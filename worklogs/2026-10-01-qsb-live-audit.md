# QSB live audit — 2026-10-01

Current protected base: `b59a947d5c4d0ac61d2b1136ffdd7b3362010434`.
Current promoted pinning score: **1,020,930,406 verified candidates/s**; +1% target is about **1,031,139,710/s**.

## New official results

- PR #3059, `QSB_FEED_BLOCK 2 -> 1`: **851,911,076**, verifier-valid but a large regression. Retire this exact lever on the live crown.
- PR #3090, half sub-batch / 512-root path: **991,404,261**, below the crown. Do not copy this exact composition.
- PR #3097, `QSB_RF_NOINLINE=1`: **849,138,221**, large regression. Retire this exact lever.
- Pepper PR #2830 remains negative at **845,538,485**; do not repeat `SLOTS=5 + GREEN_SHARED=12` on its old donor.

## Live source observations

The promoted source already carries `GREEN=20`, `GREEN_SHARED=8`, `FEED_BLOCK=2`, `QMIX5=8`, 36 MiB persistence, `FAST_START=1`, `L2_FETCH=64`, `STREAM2=1`, `HOST_GATE=1`, `CHAIN_PIPE=1`, and `REC_MASK32=1`. These defaults are not novel candidate ideas.

The source also carries `PMIX12=65536`, `PMIX12_WARP=0`, `PMIX12_N=1`; at this very sparse mix ratio, changing only selection geometry has weak evidence for a full +1% improvement.

## Pending evidence

PR #3095/#3094/#3093 tests `PIPE_LEA=1` plus 16-byte root stores plus early finish-state discard. It was dispatched but had no official score at this audit. PR #3101 is a single-switch `S2_BLOCKS` experiment and is also dispatched with score pending.

Next Pepper remote draw should stay on the live base, be executable and verifier-safe, avoid the retired levers above, and have enough public ranked/local evidence to plausibly approach the +1% gate. Prefer an isolated mechanism over another stacked speculative composition.
