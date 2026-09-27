# Yukon / Taskmarket 199 USDC workstream

Target Taskmarket bounty: Quantum-Safe Bitcoin: share 199 USDC for verified Yukon improvements.

## Current observed state
- Track source: Layr-Labs/quantum-safe-bitcoin-challenge
- Shared source snapshot observed: `46b24ebaa033fb69c7335794b54fd6a156359ec8`
- Pinning promoted score observed in current validation PRs: `995,329,477` verified candidates/s.
- Promotion rule: `minScoreImprovementBips = 100` (must beat the live frontier by 1%).
- Subset promoted score observed in current validation PRs: `700,953,730` verified candidates/s.
- Taskmarket reward: 199 USDC, split proportionally across eligible accepted + promoted gains.

## Strategy
Do not submit a cosmetic or identical-source redraw. Build from the strongest public near-frontier lineage and add an orthogonal mechanism only when provenance and compatibility are clear.

Promising public evidence under review:
1. PR #2064 describes a pinning base that reached 1,001,615,305 verified candidates/s, still below the 1% promotion floor, then adds a warp-local barrier mechanism.
2. PR #2079 describes a 995,834,154/s public composition plus carry-glue / ALU-pipe / L2 policy changes.
3. PR #2054 isolates narrower warp-local barriers in the fused root inverse.
4. PR #2067 explores tree_offload2, moving leaf inverses into a dense kernel.

The working hypothesis is to avoid duplicating a pending candidate and instead identify one orthogonal, not-yet-composed mechanism that can bridge the remaining gap to the promotion threshold.

## Rules we will preserve
- Only edit the selected track's `candidates/<track>/` surface.
- Preserve all third-party license notices and attribution.
- No harness/scorer/verifier modifications.
- No private key or wallet use.
- Do not claim local performance without official Yukon evidence.
- Final Taskmarket eligibility requires an accepted AND promoted Yukon candidate.

## Submission blocker
Official evaluation requires a Yukon participant session / API token obtained through Yukon using GitHub sign-in. The token must not be posted in chat or committed. Static public-source analysis can continue before that access exists.
