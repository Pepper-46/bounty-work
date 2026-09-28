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


## 2026-09-28 19:31 ART — evidence update and submission target

The three queued experiments from the prior audit (#2201 Karatsuba, #2202 SHA+host+IFMA-square, #2204 old co-grinder+48MiB) were all cancelled by their submitters before producing a ranked score. They are not usable as positive performance evidence.

A materially stronger completed result is now public: PR #2282 / Yukon submission `189982bf-33ba-4478-aa6c-2e21c7349527` tested the promoted `8d07d3e` pinning tree plus **only** h0ng95's interleaved SHA-256 tail schedule. It verified successfully at **1,012,807,365/s**, versus the promoted **1,008,206,828/s** (+0.4563%). It missed the 1% promotion gate, whose floor remains **1,018,288,897/s**, by only **5,481,532/s (~0.541%)**. This is currently the cleanest positive one-variable donor found in the public ranked queue.

Decision: freeze the next Pepper-46 candidate around the exact #2282 SHA-tail donor rather than Karatsuba or the regressing host bundles. The remaining research objective is one orthogonal mechanism with credible >=0.55% upside on top of that donor. Do not import the prior split-host-fold/four-slot package: a later public combination carrying those host changes scored 951,587,955/s and is explicit negative evidence.

Submission remains blocked only at the official evaluation step by Pepper-46's Yukon participant authorization/API session. No secret should be committed or pasted into chat.
