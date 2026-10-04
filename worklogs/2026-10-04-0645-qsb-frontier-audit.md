# QSB frontier audit — 2026-10-04 06:45 ART

## Live crowns

- Pinning remains `0fe76103-6afa-41fd-b727-c9b1311186d9` / PR #2908 at **1,020,930,406** verified candidates/s. Promotion threshold at 100 bips is **1,031,139,711**.
- Subset remains `faf5422a` at **753,571,538** verified candidates/s from promoted source `efef868ab78ff8d1229cdc1591b90797ee3be197`. Promotion threshold is **761,107,254**.

## Newly settled subset evidence

These exact experiments are now retired:

- PR #3373 — `QSB_SHA_UEXIT=4`: **748,017,361**, verified, not promoted.
- PR #3375 — coordinated half-sized runtime GPU batches: **743,355,669**, verified, not promoted.
- PR #3369 — WROLL + constant-bank tails composition: **746,720,603**, verified, not promoted.
- PR #3360 — related WROLL + constant-bank tails composition: **751,067,443**, verified, not promoted.
- PR #3349 — inverse Q-mix composition: **745,291,685**, verified, not promoted.
- PR #3359 — inverse Q-mix follow-up remains pending; do not duplicate before result.

## Newly settled pinning evidence

Retire these exact host-policy changes:

- PR #3418 — `QSB_FEED_BLOCK=1`: **1,016,207,492**, verified, not promoted.
- PR #3421 — `QSB_CG_RECOVER=0`: **882,307,477**, verified, not promoted.
- PR #3423 — `QSB_CG_HETERO=0`: **850,783,796**, verified, not promoted.
- PR #3416 — persist window 36 -> 40 MiB: **991,189,705**, verified, not promoted.

## Current experiments not to duplicate

At this audit the following live-base experiments are already in flight:

- PR #3427 — pinning `QSB_CG_HIGHFOLD=0`, dispatched.
- PR #3426 — pinning `QSB_CG_PF=6`, dispatched.
- PR #3424 — pinning uniform CPU backends + bounded positive-budget backoff, dispatched.
- PR #3417 — subset `QSB_TREE_UNROLL=1`, dispatched.
- PR #3420 — subset co-grinder fence + pinned workers + thermal gate, awaiting dispatch.
- PR #3422 — subset first SHA round-pair sharing experiment, awaiting dispatch.
- PR #3425 — subset WROLL/tails + worker pinning/gate composition, awaiting dispatch.
- PR #3419 — subset `QSB_SHA_ALU_RT=2`, awaiting dispatch.

## Decision

Do not spend a Pepper evaluation on any exact mechanism above while its authoritative result is pending. The current public queue is actively testing the remaining obvious single-knob host controls. Next candidate selection should wait for these near-term results and prefer a materially orthogonal mechanism rather than redraw or knob duplication.
