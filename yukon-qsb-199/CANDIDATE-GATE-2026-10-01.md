# QSB candidate gate — 2026-10-01

Current protected pinning base: `b59a947d5c4d0ac61d2b1136ffdd7b3362010434`.
Current promoted score: 1,020,930,406 verified candidates/s. The integer-safe 100-bip target is 1,031,139,711/s.

Fresh public results exclude these as next Pepper candidates: PR #3059 FEED_BLOCK=1 scored 851,911,076; PR #3053 half-packet scored 859,254,461; PR #3088 direct TOP5 + early state discard scored 837,197,948; PR #3097 RF_NOINLINE scored 849,138,221; PR #3086 FIN_IVFOLD scored 1,008,714,192; PR #3095 PIPE_LEA + vector root stores + early discard scored 1,005,566,436. Pepper's prior SLOTS5 + GREEN_SHARED12 result remains excluded at 845,538,485.

The recurring verifier/self-report gap means selection must use official verified candidates/s rather than internal work accounting.

Next gate: inspect official results for PR #3101 (single QSB_S2_BLOCKS experiment) and PR #3105 before spending another Pepper remote evaluation. Submit only a materially distinct candidate with credible evidence on the live base; do not redraw known regressions.

No user-only action is required now.
