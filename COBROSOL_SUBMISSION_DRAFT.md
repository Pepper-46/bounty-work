# CobroSol — Hackathon submission draft (NOT SUBMITTED)

**Project:** CobroSol — Get paid. Get proof.

**One-liner:** Solana devnet invoice requests with verifiable on-chain proof of payment, not screenshots.

**Track:** Payments / Fintech / Best Product Experience (Superteam Argentina); final category subject to platform options.

**Project code:** https://github.com/Pepper-46/bounty-work/tree/hackathon/cobrosol-20261011

**Demo URL:** NOT YET DEPLOYED. Do not enter a source code link as if it were a working deployed app.

**Demo video:** NOT YET RECORDED.

**Founder:** Account owner to authenticate and confirm legal name/residency and the role. Do not invent personal details.

## Problem

A wallet screenshot or copied transaction ID is not reliable proof that an invoice was paid. Freelancers and small businesses need a fast way to request payments with a unique reference and confirm that the right recipient, amount, and invoice were actually included in a finalized blockchain transaction.

## Solution

CobroSol creates a native SOL payment request containing a cryptographically random Solana Pay reference, a unique invoice memo, requested amount, and recipient wallet. The browser can verify the receipt against the official Solana devnet JSON-RPC using `getParsedTransaction` or search by reference through `getSignaturesForAddress`. Verification fails if the transaction was unsuccessful or any required invoice property is absent.

## Why Solana?

Fast confirmations, precise 9-decimal native SOL transfers, public transaction proofs, and standard reference accounts and memos permit non-custodial request/receipt matching. On-chain verification is the core functionality, not merely a logo or a payment button.

## Technical architecture

- Client: standalone responsive HTML, CSS, JavaScript with no build system.
- Client storage: browser localStorage; user-controlled and not relied on for final proof.
- Network: Solana **devnet only**, endpoint `https://api.devnet.solana.com`.
- Chain interaction: `getParsedTransaction` (finalized) and `getSignaturesForAddress` (finalized).
- Cryptography: `crypto.getRandomValues` for invoice IDs and 32-byte reference keys.
- Solana Pay URI fields: `amount`, `reference`, `memo`, `label`, `message`.
- Verification conditions: finalized successful transaction; expected signature; reference present in account keys; invoice memo present; native system transfer to correct recipient with lamports >= invoice amount.

## Demo plan (not yet executed)

1. Open the deployed CobroSol demo and create invoice for 0.025 *test* SOL.
2. Confirm recipient is a publicly disclosed devnet wallet and reveal the URI only after devnet warning acknowledgment.
3. Make a devnet wallet transfer that preserves the expected reference and memo.
4. Paste genuine resulting signature and verify. Save the publicly verifiable devnet signature.
5. Paste an unrelated finalized signature, demonstrating rejection rather than marking paid.

**Never use a mainnet wallet or real funds for this demo:** Solana Pay URLs cannot force wallet network selection.

## Starting point and progress log

- Project created **2026-10-11**; no verified pre-existing product, users, revenue or outside investment.
- 2026-10-11: Initial local prototype reported 15 passing unit tests with simulated transaction fixtures; not evidence of a real devnet transaction.
- 2026-10-11: First standalone GitHub demo uploaded (commit `1bdcc73984a5c450c8c5b972f395ea2d3c456bf1`).
- 2026-10-11: Documented limitations and declared AI assistance (commit `48d0bdeb208e61c2e89c6336edad48fc6b489f9a`).
- 2026-10-11: MIT license added (commit `b152a6fe5b1980adde83898256c0e664369a7b38`).

## Validation and traction

- **No independently verified end-to-end devnet payment yet.**
- **No customer interviews, usage metrics, customers, financial transactions or revenue claimed.**
- Prior unit tests were mocked, not on-chain; public demo browser flow is not independently audited.

## Roadmap

1. Deploy static demo and record real devnet verification evidence (link to Solana Explorer devnet).
2. Add a reproducible test harness and CI on the published branch.
3. Support USDC/SPL Token transfers with stricter mint/account checks.
4. Add invoices export, RPC fallback and accessibility improvements.
5. Run documented interviews with freelancers and small businesses in Argentina.

## AI / ownership disclosure

Material design, implementation, documentation and positioning were generated with OpenAI GPT-6 assistance. Human account holder must review, validate and take responsibility for any externally submitted claims and eligibility. No team members should be invented.

## Final submission prerequisites

- [ ] Confirm authentic Colosseum authenticated account, register and accept official conditions explicitly.
- [ ] Confirm Superteam Earn authenticated account and regional residency eligibility.
- [ ] Deploy and verify accessible public live demo.
- [ ] Confirm actual end-to-end Solana devnet transaction and public signature, if represented.
- [ ] Produce and upload honest demo video / pitch as required.
- [ ] Enter correct team and contact details supplied by owner.
- [ ] Submit in Colosseum AND Superteam Earn before their deadlines.
- [ ] Save both confirmation IDs / URLs; no submission may be claimed until these exist.
