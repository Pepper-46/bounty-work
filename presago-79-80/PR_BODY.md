## Summary
- Correct `WIN_TOKENS` from 1 to **10 PULSE**, matching `const WIN_TOKENS: i128 = 10_0000000` (100,000,000 base units at 7 decimals).
- Remove retired `LOSE_TOKENS` references, since losing no longer mints consolation tokens (source comment for issue #24).
- Clarify the supply invariant and the governance checklist.

Closes #79
Closes #80

## Verification
- Checked against `prediction_market/src/lib.rs` and `pulse_token/src/lib.rs` on 2026-10-08.
- Local textual assertions and `git apply --check` passed.
- `cargo test --workspace --all-features` not run locally (source checkout and Rust dependencies unavailable); please rely on CI Tests job.

## Naming clarification
Issue #80 uses the name PRESAGO, but the current source and matrix call the reward token PULSE; this patch preserves the actual source token name rather than introducing a new mismatch.
