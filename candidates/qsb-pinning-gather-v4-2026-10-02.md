# QSB pinning candidate — isolated QSB_GATHER_V4=1

Prepared: 2026-10-02

## Base / frontier

- Protected base observed on current Yukon submissions: `2f57d80b8877a9e63b6af220da913236886a7ce5`
- Promoted pinning source remains DPZZxlz `0fe76103`, official score **1,020,930,406 verified candidates/s**
- 100-bip promotion target: approximately **1,031,139,710/s**

## Candidate

Single existing compile-time switch in `candidates/pinning/pinning.cu`:

```diff
 #ifndef QSB_GATHER_V4
-#define QSB_GATHER_V4 0
+#define QSB_GATHER_V4 1
 #endif
```

No host scheduling, green-context geometry, verifier, benchmark, candidate enumeration, hit format, co-grinder policy, or unrelated device knob is changed.

## Why this is staged rather than submitted immediately

A fresh public-PR search on 2026-10-02 found no Yukon validation PR whose submission note names `QSB_GATHER_V4`. This makes it materially distinct from the already-scored dead ends we have retired.

However, several adjacent gather/device switches are currently being evaluated by other participants. In particular, `QSB_GATHER_EARLY=0` has already scored only 973,332,840/s and is retired. The existence of a different gather knob is not evidence that V4 is faster. Before spending a remote evaluation, inspect the exact implementation and any newly landed PRs to ensure this switch is not an alias/no-op and has not just been independently scored.

## Retired mechanisms that must not be folded into this candidate

Do not combine this experiment with: SLOTS5+GREEN_SHARED12, GREEN18, GREEN_SHARED6, GREEN_S2_LEAST, GREEN_SPLIT_FLAGS=0, FEED_BLOCK=1, half-packets, CHAIN_ALU, phase-skew, FIN_IVFOLD+FIN_RASSOC, finish instruction-cut bundles, or GATHER_EARLY=0. Those mechanisms already have negative authoritative evidence.

## Promotion discipline

This file is a staging artifact, not a performance claim. If source inspection shows `QSB_GATHER_V4=1` is executable, exact, and changes the native carrier without violating the candidate contract, prepare a one-knob submission from the current protected base. If a public evaluator scores the same hypothesis first, ingest that result and retire or promote this candidate accordingly rather than duplicating it.
