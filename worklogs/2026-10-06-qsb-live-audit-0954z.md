# QSB live audit — 2026-10-06 09:54Z

## Frontier

Pinning remains at fkiene PR #3548 / Yukon `12233735-1d33-42eb-9108-bb1c18cbd3eb`:

- protected source: `582a99408761f904f7f92a5d64d9ca0dcc76924a`
- official verified score: **1,036,462,054 candidates/s**
- 100-bip promotion target: **1,046,826,675 candidates/s**

Subset remains **753,571,538 candidates/s**; 100-bip target is **761,107,254 candidates/s**.

No Pepper-46 submission is currently queued.

## Qualified positive retained

PR #3670 / Yukon `9c8bab37-0230-464a-9e70-62791fd6b0aa` remains the cleanest isolated positive Pinning component:

- official score: **1,039,408,577**
- verified: true
- delta over crown: **+2,946,523/s (+0.2843%)**
- not promoted because the required gain is +1%

Mechanism: retain the actual launch size for an occupied asynchronous slot and credit `qcg::tick` with that completed slot's real size instead of nominal `BATCH`. This is host/controller accounting only; it does not alter the candidate function.

Important source audit: the promoted source currently retains `slot_bsz` only under `#if QSB_PK_ON`, while `QSB_HOST_PKSHA` defaults to 0, making `QSB_PK_ON=0` on the default ranked path. In that path `collect_slot` still credits `qcg::tick(..., BATCH)`. Therefore #3670 is a real default-path correction rather than a cosmetic duplicate of existing PK metadata.

## Fresh official negatives

Do not compose these with #3670:

- PR #3675 rolling compressed-key SHA schedule ALU fusion: **1,009,914,292**, regression.
- PR #3678 combined early + rolling compressed-key SHA ALU balance: **868,500,889**, strong regression.
- PR #3673 matched K8 + five-slot + one-pass input-pool selection: **879,220,449**, strong regression.
- Subset PR #3676 four-chain streaming W+K schedule: **727,801,965**, strong regression.
- Subset PR #3674 package draw: **732,389,904**, regression.

These reinforce that local/stock positive readings for the SHA ALU changes do not transfer to the authoritative runner.

## Current pending evidence worth waiting for

Subset PRs #3679, #3680 and #3681 are queued/dispatched and test materially different mechanisms. Pinning has no fresh independently-positive orthogonal component in the latest scored set that is strong enough to justify composing with #3670 yet.

## Decision

Do **not** submit a Pepper redraw of #3670 alone: +0.2843% is well below the +1% gate. Do not combine it with the newly scored SHA/K8 regressions. The next Pinning submission should pair #3670 only with a separately qualified, non-controller mechanism whose authoritative evidence survives the current runner, or use a genuinely new isolated mechanism with a plausible >0.7% residual gain.

This preserves remote evaluation budget and avoids an unsupported additive assumption.
