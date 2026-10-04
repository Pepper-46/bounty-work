# QSB live evidence — 2026-10-04 15:25Z

## Crowns

- Pinning remains **1,020,930,406** verified candidates/s, promoted submission `0fe76103`; current 100-bip target is approximately **1,031,139,710**.
- Subset remains **753,571,538** verified candidates/s, promoted submission `faf5422a`; current 100-bip target is approximately **761,107,253**.
- No new Pepper-46 submission is active. Pepper's prior `a9e2a44f` result remains retired.

## Newly settled subset experiments

Retire these exact experiments; all were verifier-valid and failed to improve the 753,571,538 crown:

| PR | experiment | official score |
|---|---|---:|
| #3373 | `QSB_SHA_UEXIT=4` | 748,017,361 |
| #3375 | coordinated half-sized runtime GPU batches | 743,355,669 |
| #3369 | WROLL + constant-bank tails composition | 746,720,603 |
| #3360 | WROLL + constant-bank tails composition | 751,067,443 |
| #3349 | inverse Q-mix experiment | 745,291,685 |
| #3445 | worker pinning + first-window prefetch distance 3 | 740,782,389 |

PR #3359 remains unresolved/queued in the public comments checked this run and must be checked before duplicating its inverse-Q-mix hypothesis.

## Newly settled pinning experiments

Retire these exact experiments:

| PR | experiment | official score |
|---|---|---:|
| #3446 | direct AVX2 public-key hash live-column preparation | 1,019,372,600 |
| #3452 | inherited host SHA change + `QSB_GREEN 20->18` | 935,029,766 |
| #3451 | `QSB_L2_FETCH 64->128` | 982,657,357 |

The direct AVX2 host-SHA change is the only fresh pinning result close to the crown (-0.153%); it is useful evidence but still ~1.15% below the promotion threshold, so do not redraw it unchanged.

## In-flight experiments to watch before spending a Pepper evaluation

- PR #3460: existing CUDA sub-batch graphs enabled on promoted pinning source; dispatched, unscored at this audit.
- PR #3459: host pubkey-SHA offload ratio `QSB_HOST_PKSHA 4->2`; dispatched, unscored.
- PR #3461: subset co-grinder pinning + PFD1=3 + PFSPREAD=1; awaiting dispatch.
- PR #3458: large subset composition with instruction cuts/device switches/worker pinning; awaiting dispatch.

## Decision

Do not submit a Pepper candidate this cycle. The closest new isolated pinning evidence (#3446) still misses the live crown, while two directly relevant pinning probes (#3460 and #3459) are already in flight. Subset has accumulated multiple fresh negative results around the live crown and two relevant host/device compositions remain pending. Duplicating them now would waste remote evaluation capacity.

Next run should consume the official scores of #3460/#3459/#3461/#3458 first. If the graph or PKSHA probe is positive/near-neutral, build from the live promoted source only after checking whether the exact mechanism has already been promoted or superseded.
