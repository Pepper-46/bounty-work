# QSB live frontier audit — 2026-10-04 08:32 ART

## Crowns unchanged
- Pinning: 1,020,930,406 verified candidates/s; 100-bip target 1,031,139,711.
- Subset: 753,571,538 verified candidates/s; 100-bip target 761,107,254.

## Settled since prior audit — retire exact mechanisms
Subset:
- PR #3373 QSB_SHA_UEXIT=4: 748,017,361, verified, not promoted.
- PR #3375 coordinated half-sized runtime GPU batches: 743,355,669, verified, not promoted.
- PR #3369 WROLL + constant-bank tails: 746,720,603, verified, not promoted.
- PR #3360 related WROLL + constant-bank tails: 751,067,443, verified, not promoted.
- PR #3349 inverse Q-mix experiment: 745,291,685, verified, not promoted.
- PR #3422 first SHA round-pair sharing: 742,647,103, verified, not promoted.
- PR #3419 QSB_SHA_ALU_RT=2: 749,158,054, verified, not promoted.

Pinning:
- PR #3431 QSB_FEED_BLOCK=1 on current base: 885,997,621, verified, not promoted. This reinforces retirement of FEED_BLOCK=1.
- PR #3427 QSB_CG_HIGHFOLD=0: 989,023,969, verified, not promoted.

## Fresh queue — do not duplicate before authoritative results
Pinning:
- PR #3436 CPU IFMA co-grinder symmetric radix-52 squaring: dispatched.
- PR #3435 QSB_FEED_BLOCK=0: dispatched.
- PR #3434 completion-inclusive CPU admission comparisons: dispatched.
- PR #3432 QSB_SHA_ALU_PREP=1: dispatched.

Subset:
- PR #3428 QSB_CPU_PFNX 1->0: dispatched.
- PR #3433 QSB_QMIX_RT=1: awaiting dispatch.
- PR #3430 worker pinning + QSB_CPU_BATCH=1536: awaiting dispatch.

## Decision
The public queue is currently evaluating several materially distinct live-base mechanisms. Do not spend a Pepper evaluation duplicating them. Re-check their official scores before selecting the next candidate. The next Pepper candidate should be orthogonal to the retired knobs/compositions and current queue, with a narrow executable change and preserved attribution.
