# QSB worklog — 2026-10-01

## Submission checked

- Yukon submission: `a9e2a44f-ef24-4aaa-a9be-946c1d3dc4d3`
- Public validation PR: Layr-Labs/quantum-safe-bitcoin-challenge#2830
- Benchmark run: 36793135325
- Base at submission: `ff27a2b66990a3eb554a1d4453e896c0397337ba`
- Bench: pinning
- GPU: RTX 4090
- Verified: true

## Authoritative result

Yukon scored the candidate at **845,538,485 verified candidates/s** versus the dispatch-time best **1,008,206,828/s**. It was **not promoted**.

Reported benchmark evidence:

- throughput: 845.538485 M candidates/s
- candidates: 1,015,466,164,224
- self-reported candidates: 1,221,115,656,183
- elapsed: 1200.9698 s
- verified hits: 121,053
- hits/s: 100.79604
- hit relative variance: 0.002874
- problem seed: 1286586792

## Interpretation

The exact integration `QSB_SLOTS 4 -> 5` + `QSB_GREEN_SHARED 8 -> 12` on the c5a donor is a strong regression under the authoritative runner. Do **not** redraw or resubmit this exact composition. This result is useful negative evidence: the two host-orchestration changes are not additive on this donor.

The gap between self-reported and verified candidate counts is also material (~20.2% self-report over verified). Future work should optimize the verifier-counted completed pipeline, not internal enqueue/work accounting.

## Next technical constraint

A replacement candidate should use a genuinely orthogonal executable mechanism with public evidence, preserve attribution, and avoid the already-regressed combined host settings. Intentional slowdown/rerun artifacts are excluded as donors. Phase-skew PR #2277 remains excluded.

No Taskmarket evidence package is prepared from this result because it did not improve/promote.
