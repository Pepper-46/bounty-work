# CobroSol — Get paid. Get proof.

**Crypto World's Fair 2026 / Superteam Argentina candidate | Solana devnet demonstration**

CobroSol creates non-custodial **native SOL** payment requests and checks Solana devnet for evidence of a finalized matching payment. A screenshot or arbitrary transaction hash is not evidence of receipt.

## Run

Open `index.html` locally with a simple static server:

```sh
python3 -m http.server 8080
# visit http://localhost:8080
```

No build step or API keys required. Browser internet access to the public Solana devnet RPC is necessary to verify a real transaction.

## Implemented

- Unique 32-byte cryptographically random Base58 Solana Pay reference for each request.
- Unique invoice ID incorporated into the Solana Pay memo.
- Exact SOL-to-lamports handling up to 9 decimal places.
- Solana Pay URI with recipient, amount, reference and memo.
- Local-only invoice history, no user accounts or private keys.
- Explicit devnet-wallet confirmation before displaying/copying the payment URI.
- Live Solana **devnet** JSON-RPC `getParsedTransaction` with `finalized` commitment.
- Optional finalized reference discovery via `getSignaturesForAddress`.
- Fail-closed receipt matching: signature, success, reference account, memo, native system transfer, correct recipient and amount must all match.

## How to test (test SOL only)

1. Provide a Solana public **devnet** wallet you control; never paste a private key.
2. Create an invoice for a small test amount (e.g. 0.025 SOL).
3. Confirm the payer wallet is explicitly using **devnet**, then copy the Solana Pay URI.
4. Use a devnet-capable payer wallet that preserves the reference and memo, with **test SOL only**.
5. Paste the resulting devnet transaction signature or use *Find payment by reference*.
6. Try a random unrelated signature and observe that it does not verify.

> **Critical safety note:** Solana Pay URIs do **not** enforce a devnet selection. A user could accidentally transfer real funds using a wallet on mainnet. This prototype has no production support and should **never** be used with real SOL.

## Limitations and honest evidence

- This branch is a **standalone one-file MVP**, created October 11, 2026.
- The previous local development ZIP contains a richer multi-module UI and **15 passing mocked unit tests**. Those tests are **not** a substitute for independent tests of this branch or for a real devnet end-to-end transfer.
- As of this commit, a live devnet payment with public transaction proof has **not been completed or verified**.
- No real user interviews, signed pilots, transaction counts, revenue, growth, customers, awards or formal hackathon submission are claimed.
- No actual hosting deployment is claimed by creating this GitHub source branch.
- RPC outages / CORS restrictions / indexer delays can prevent verification. Browser localStorage receipts are alterable; always revalidate the transaction on-chain.
- Native SOL only (not USDC/SPL). A valid on-chain receipt doesn't identify the person who sent it.
- Not security audited. No legal or financial product certification.

## AI assistance / eligibility disclosure

The project, UX, code and copy were developed **materially with OpenAI GPT-6 assistance** on October 11, 2026. Any human cofounder, resident-country eligibility, prior work, tests, demos, validation and external submission must be truthfully disclosed. Registration with Colosseum and separate submission to Superteam Earn **have not yet been completed**.

## Competition references

- https://superteam.ar/colosseum
- https://superteam.fun/earn/listing/colosseum-crypto-worlds-fair-hackathon-superteam-argentina-track
- https://colosseum.com/hackathon

## Ownership and license

MIT-licensed independent hackathon candidate. No third-party user data, credentials or real funds involved.
