# QSB live evidence refresh — 2026-10-04

## Crown state

- Pinning crown remains `0fe76103` / PR #2908 at **1,020,930,406 verified candidates/s**.
- Subset crown remains kshitij-hash `faf5422a` at **753,571,538 verified candidates/s**, promoted source `efef868ab78ff8d1229cdc1591b90797ee3be197`.
- Subset 100-bip promotion target is approximately **761,107,253/s**.

## Fresh authoritative results checked

All of these ran on the live 753.57M Subset crown and are now retired as donors/levers:

- PR #3373, `QSB_SHA_UEXIT=4`: **748,017,361/s**, verified, not promoted.
- PR #3375, coordinated half-sized runtime GPU batches: **743,355,669/s**, verified, not promoted.
- PR #3369, WROLL + constant-bank tails composition: **746,720,603/s**, verified, not promoted.
- PR #3360, earlier WROLL + constant-bank tails draw: **751,067,443/s**, verified, not promoted.
- PR #3349, inverse Q-mix experiment: **745,291,685/s**, verified, not promoted.
- PR #3359, inverse Q-mix follow-up: cancelled by submitter before scoring.

These results strengthen the conclusion that the remaining easy GPU scheduling/SHA/Q-mix knobs are not additive on `faf5422a`.

## Source audit performed

I inspected the promoted `CpuGrindSubset.h` at source `efef868...`. The live co-grinder already carries a heavily tuned host path, including:

- `QSB_CPU_BATCH=1024`, `QSB_CPU_BATCH_AUTO=1`, `QSB_CPU_BATCH_SOLO=4096`
- `QSB_CPU_PFD1=8`, `QSB_CPU_PFD=3`, `QSB_CPU_PFSPREAD=3`
- `QSB_CPU_ILP2=3`, `QSB_CPU_NCH=2`
- `QSB_CPU_EPOCH_CONTIG=1`
- `QSB_CPU_ALLCPU=1`
- `QSB_CPU_BUILD_NT=0` (and the live experiment enabling it has already regressed)
- `QSB_CPU_FENCE=0`, diagnostics disabled in the effective live path.

Historical search also confirms `QSB_CPU_NCH=4` was previously evaluated on the older crown and did not establish a competitive total-rate gain, so it is not a clean high-confidence live-crown candidate.

## Decision

Do **not** spend a remote evaluation merely flipping another adjacent host constant without evidence. The live crown is now >3.4% above the previous 728.34M record and the required +1% promotion margin is substantial. The recent single-knob queue is consistently below the crown.

Next productive path: continue source-level audit for a genuinely orthogonal exact mechanism (especially work that changes verified completed coverage rather than self-reported enqueue throughput), and re-check newly scored public submissions before preparing any Pepper candidate. No user-only action is required.
