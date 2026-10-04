# QSB live evidence — 2026-10-04 18:06Z

## Crowns

- Pinning remains **1,020,930,406** verified candidates/s, promoted submission `0fe76103`; 100-bip target approximately **1,031,139,710**.
- Subset remains **753,571,538** verified candidates/s, promoted submission `faf5422a`; 100-bip target approximately **761,107,253**.
- No new Pepper-46 validation PR is active.

## Newly settled evidence

Retire these exact experiments:

| PR | track | experiment | official score |
|---|---|---|---:|
| #3460 | pinning | existing CUDA sub-batch graphs enabled on promoted source | 991,613,030 |
| #3459 | pinning | host pubkey-SHA offload ratio `QSB_HOST_PKSHA 4->2` | 1,010,851,961 |
| #3458 | subset | instruction cuts + WROLL/constant-bank tails + worker pinning composition | 741,412,826 |

All were verifier-valid and not promoted.

## Queue status

- #3461 subset: worker pinning + `QSB_CPU_PFD1=3` + `QSB_CPU_PFSPREAD=1`; dispatched, no official score at this audit.
- #3467 subset: retained own-best policy plus independent shared/L1 and normalization experiments; dispatched, no official score at this audit.
- #3471 subset: `QSB_CPU_RESERVE 2->1`; awaiting dispatch at this audit.
- #3359 inverse-Q-mix experiment was **cancelled by the submitter** and has no performance score. Do not treat it as positive evidence; exact source should still be checked before reusing the hypothesis.

## Decision

Do not spend a Pepper evaluation on the now-settled graph or PKSHA-ratio probes: both miss the crown and the promotion bar. The PKSHA ratio result is the closer of the two but is still ~0.99% below the crown and ~1.99% below the promotion target.

Subset remains the better evidence-gathering track this cycle because three directly relevant host-policy experiments are already running/queued. Consume #3461/#3467/#3471 before selecting a new single-knob host experiment so Pepper does not duplicate live work.

No payout and no user-only blocker observed in this audit.
