# QSB frontier refresh — 2026-10-03 22:47Z

## Blocker audit
No user-only blocker is present. Yukon auth/token and Taskmarket wallet binding remain resolved. No payout is confirmed.

## Fresh authoritative subset evidence
Live crown remains kshitij-hash `faf5422a`: **753,571,538 verified candidates/s** on source `efef868ab78ff8d1229cdc1591b90797ee3be197`. The 100-bip promotion target remains about **761,107,253/s**.

New official results checked this run:
- PR #3349 inverse Q-mix composition: **745,291,685**, verified, not promoted. Retire that exact composition.
- PR #3360 WROLL + constant-bank tails composition: **751,067,443**, verified, not promoted. Close but still below crown; do not duplicate.
- PR #3369 the related WROLL + constant-bank tails package: **746,720,603**, verified, not promoted. Retire exact package.
- PR #3359 inverse Q-mix follow-up was cancelled by its submitter and has no positive score.

Still pending and therefore protected from duplication:
- PR #3373 isolated `QSB_SHA_UEXIT=4`: dispatched, official score not posted yet.
- PR #3375 coordinated half-sized runtime GPU batches: awaiting dispatch.

## Pinning
No evidence found this run that displaces the known crown `0fe76103` at **1,020,930,406/s**. Previously recorded live-base regressions remain retired.

## Decision
Do not spend a Pepper remote evaluation on WROLL/constant-bank-tail or inverse-Q-mix variants: fresh official evidence is negative. Wait for the isolated UEXIT and half-batch results before touching those mechanisms. Continue searching for a materially orthogonal live-crown mechanism; if neither pending probe is positive, favor a fresh single-knob subset experiment over stacking known-negative switches.
