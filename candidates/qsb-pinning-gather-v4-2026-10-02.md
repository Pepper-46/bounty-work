# QSB pinning candidate — QSB_GATHER_V4=1 — RETIRED BEFORE SUBMISSION

Prepared: 2026-10-02

## Status

**RETIRED / compile-time invalid. Do not submit.**

## Base / frontier

- Current protected base observed on Yukon submissions: `2f57d80b8877a9e63b6af220da913236886a7ce5`
- Promoted pinning source remains DPZZxlz `0fe76103`, official score **1,020,930,406 verified candidates/s**
- 100-bip promotion target: approximately **1,031,139,710/s**

## Candidate that was staged

The proposed isolated switch was:

```diff
 #ifndef QSB_GATHER_V4
-#define QSB_GATHER_V4 0
+#define QSB_GATHER_V4 1
 #endif
```

## Source audit result

Inspection of the exact promoted source at `b59a947d5c4d0ac61d2b1136ffdd7b3362010434` found that the switch is intentionally guarded out:

```c
#if QSB_GATHER_V4
#error "QSB_GATHER_V4: ld.global.v4.u64 is 256 bits; ptxas rejects vectors above 128 bits"
#endif
```

The dormant branches attempt `ld.global...v4.u64`, a 256-bit PTX vector load. The source itself records why this path is disabled: ptxas rejects vectors above 128 bits. Therefore `QSB_GATHER_V4=1` is not an executable optimization candidate; it is a guaranteed compile-time failure.

A fresh public-PR search found no scored Yukon submission specifically enabling this switch. That absence is now explained by the source guard and is not positive evidence.

## Decision

Do **not** spend a Yukon remote evaluation on this candidate. Retire it before submission. A future gather experiment must use legal PTX widths (for example multiple <=128-bit loads) and be a genuinely new implementation rather than merely enabling this kill switch.

## Other retired mechanisms

Do not fold in already-negative mechanisms: SLOTS5+GREEN_SHARED12, GREEN18, GREEN_SHARED6, GREEN_S2_LEAST, GREEN_SPLIT_FLAGS=0, FEED_BLOCK=1, SUB_CUT, half-packets, CHAIN_ALU, phase-skew, FIN_IVFOLD+FIN_RASSOC, finish instruction-cut bundles, or GATHER_EARLY=0.
