# QSB frontier refresh — 2026-10-03

## Live state checked

### Pinning
- Promoted crown remains `0fe76103`: **1,020,930,406 verified candidates/s**.
- Protected repository base observed on current submissions: `efef868ab78ff8d1229cdc1591b90797ee3be197`; promoted pinning source remains `b59a947d5c4d0ac61d2b1136ffdd7b3362010434`.
- 100-bip promotion target remains about **1,031,139,710/s**.
- New negative/near-control evidence:
  - PR #3327 optional generator precomputation on joint host gate: **1,019,597,584**, not promoted.
  - PR #3325 finish-state discard + host digest reuse composition: **991,044,387**, not promoted.
  - PR #3329 GREEN 20->18 redraw/composition: **854,574,203**, confirming GREEN18 remains retired.
- Interesting pending single-knob experiments worth observing before duplicating:
  - PR #3316: `QSB_CG_PF 4 -> 8` host co-grinder prefetch distance.
  - PR #3323: `QSB_RROOT_WIDE 0 -> 1` register-root experiment.
- Do not submit a Pepper duplicate until those exact hypotheses have authoritative scores.

### Subset
- The prior 736,585,478 crown is stale.
- Current promoted crown observed in fresh submissions is kshitij-hash `faf5422a`: **753,571,538 verified candidates/s**.
- Current 100-bip target is about **761,107,253/s**.
- PR #3315 scored **754,592,867**: improves the crown numerically but is only ~0.136% higher, so it did not clear the 1% promotion gate.
- PR #3319 (WROLL_PIPE + R_CBANK_TAILS etc.) scored **745,130,449**, not promoted.
- PR #3326 is a seven-arm measurement run probing Q layouts / CODE_ROLL and is more valuable to wait for than blindly duplicating a switch.
- PR #3331 tests a new Q_MIX_INV composition on the live subset crown; pending.

## Decision

Do not spend a Pepper remote evaluation on any already-scored dead mechanism or duplicate a currently pending single-knob experiment. The subset frontier moved materially (+2.3% from 736.59M to 753.57M), so all staged subset work based on the old crown must be rebased/re-audited before submission. Highest-value next step is to consume the pending measurement results (#3326/#3331) and isolate any positive arm that can plausibly exceed 761.11M; otherwise continue searching for an orthogonal host-only subset improvement.

No user-only blocker exists. No payout is confirmed.
