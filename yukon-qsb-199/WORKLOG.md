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


## 2026-09-28 06:39 ART — ranked queue audit

Live promoted pinning frontier remains `1,008,206,828` verified candidates/s on source `8d07d3ebad41a017dfaa5906b164f883a9b59348`; the 1% promotion floor is `1,018,288,897`.

New official evidence:
- PR #2187 (promoted tip + QSB_PIPE_LEA + three widened root stores) completed verified but regressed to **971,145,962/s**. Do not import this four-change bundle.
- PR #2202 is queued with a more defensible composition: previously measured SHA-tail scheduling (~1,009,707,243/s on its donor run), verified host fold/slots, and symmetric IFMA square. Await its official score before considering reuse.
- PR #2201 is queued as a clean one-variable Karatsuba A/B on the promoted tip. Our local semantic identity test remains useful for correctness, but performance remains unproven until this result lands.
- PR #2204 is queued testing the previous CPU co-grinder engine plus a 48 MiB persisting table window.

Decision: do not spend a Yukon evaluation on the failed #2187 mechanism family. Prefer mechanisms with completed positive official evidence; wait for #2201/#2202/#2204 results before freezing a composition. Static analysis can continue without credentials, but an official Pepper-46 submission still requires the user's Yukon participant authorization.
