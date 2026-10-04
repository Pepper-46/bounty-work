# QSB live evidence refresh — 2026-10-04 12:47Z

## Crowns
- Pinning remains **1,020,930,406/s**; 100-bip target **1,031,139,711/s**.
- Subset remains **753,571,538/s**; 100-bip target **761,107,254/s**.
- No Pepper promotion or payout evidence is present.

## Newly authoritative results — retire exact mechanisms

### Pinning
- PR #3436 CPU IFMA co-grinder symmetric radix-52 squaring: **1,017,356,798/s**, verified, not promoted.
- PR #3434 completion-inclusive CPU admission comparisons: **988,808,021/s**, verified, not promoted.
- PR #3435 `QSB_FEED_BLOCK=0`: **875,767,930/s**, verified, not promoted.
- PR #3439 `QSB_CG_QUOTA_CAP=0`: **881,093,174/s**, verified, not promoted.
- PR #3432 `QSB_SHA_ALU_PREP=1`: **1,018,147,750/s**, verified, not promoted.
- PR #3426 `QSB_CG_PF=6`: **873,811,507/s**, verified, not promoted.
- PR #3424 uniform CPU backends + bounded positive-budget backoff: **1,016,503,495/s**, verified, not promoted.

The closest fresh pinning experiments remain below both the crown and the automatic-promotion target; adjacent redraws are not justified.

### Subset
- PR #3415 `QSB_CPU_PFD1 8->3`: **746,081,481/s**, verified, not promoted.
- PR #3422 first-SHA-round-pair sharing: **742,647,103/s**, verified, not promoted.
- PR #3414 WROLL/constant-tail host composition: **739,719,607/s**, verified, not promoted.
- PR #3417 `QSB_TREE_UNROLL=1`: **749,414,916/s**, verified, not promoted.
- PR #3428 `QSB_CPU_PFNX 1->0`: **741,970,509/s**, verified, not promoted.
- PR #3419 `QSB_SHA_ALU_RT=2`: **749,158,054/s**, verified, not promoted.
- PR #3420 was cancelled by submitter.

## Current queue — avoid duplication until scored
- Subset #3433: `QSB_QMIX_RT=1`, dispatched.
- Subset #3430: worker pinning + `QSB_CPU_BATCH=1536`, dispatched.
- Subset #3437: early plain-GPU-gate selection, awaiting dispatch.
- Subset #3440: `QSB_CPU_PFSPREAD 3->1`, awaiting dispatch.
- Pinning #3441: prepare SHA ALU scheduling + bounded host event queries, dispatched.
- Pinning #3442: PF-distance experiment, dispatched; isolated PF=6 already regressed in #3426.

## Decision
Do not spend a Pepper evaluation duplicating a settled negative or an in-flight experiment. Obvious host knobs are increasingly exhausted. Favor a genuinely orthogonal implementation affecting verified completed coverage rather than self-reported work. Re-check the live queue before selecting a new candidate.
