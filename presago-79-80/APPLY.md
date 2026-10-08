# Presago invariants — verified replacement instructions

Target: `Presago-Labs/presago-contracts/INVARIANT_MATRIX.md` at upstream blob `09cfd815da2f02376f0acf946858abd065739d13`.

1. In the prediction_market constants table, replace `WIN_TOKENS | 1 PULSE` with `WIN_TOKENS | 10 PULSE (100,000,000 base units at 7 decimals)`.
2. Delete the obsolete `LOSE_TOKENS | 0.2 PULSE` table row.
3. In invariant #4, replace `WIN_TOKENS + LOSE_TOKENS` with `WIN_TOKENS` and describe the invariant as `PULSE supply tracks winner reward mints (no loser consolation mint)`.
4. In invariant #15, replace `WIN_TOKENS (1 PULSE)` with `WIN_TOKENS (10 PULSE = 100,000,000 base units)`.
5. In Governance Process item 4, remove `LOSE_TOKENS` from the list of constants.

Verified locally on 2026-10-08: five substitutions, no remaining `LOSE_TOKENS` references, resulting diff applies cleanly. Rust workspace tests were not run.

Source: `prediction_market/src/lib.rs` has `const WIN_TOKENS: i128 = 10_0000000;` and documents removal of loser token mints. `pulse_token/src/lib.rs` declares `PULSETokenContract`.
