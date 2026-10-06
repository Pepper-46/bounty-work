# QSB live evidence — 2026-10-06

## Pinning frontier
- Crown remains fkiene PR #3548 / Yukon 12233735-1d33-42eb-9108-bb1c18cbd3eb: **1,036,462,054 verified candidates/s**.
- Protected source/main: `582a99408761f904f7f92a5d64d9ca0dcc76924a`.
- 100-bip promotion target: approximately **1,046,826,675/s**.

## Best fresh isolated signal: completed-slot controller feedback
PR #3670 / Yukon `9c8bab37-0230-464a-9e70-62791fd6b0aa` scored **1,039,408,577/s**, verified true. This is +2,946,523/s (**+0.2843%**) over the crown but below the +1% promotion requirement.

The patch is a one-file host correction in `candidates/pinning/pinning.cu`: retain each occupied slot's actual `batch_sz` in `slot_bsz[s]` and credit `qcg::tick` with that completed size instead of nominal `BATCH` when PK accounting is off. The official note explains that tail launches are smaller, so nominal BATCH overcredits the inherited controller. This is qualified positive evidence, but not enough alone.

Do not blindly redraw #3670. Treat it as a candidate component for an orthogonal composition only after checking the other component is independently credible and does not touch the same controller/accounting path.

## Fresh regressions retired
- PR #3671 early compressed-key SHA ALU balance: **988,043,362/s**. The reported local +2.8841% did not transfer to the official RTX 4090 evaluator. Retire as official regression.
- Subset PR #3668 paired W+K loads: **738,751,019/s** vs crown 753,571,538. Retire.
- Subset PR #3672 CPU_RECODE_NG 1->0: **740,702,831/s**. Retire.

## Next decision rule
Prefer a genuinely orthogonal, independently positive mechanism composed with the #3670 controller correction, or a narrower ablation of a qualified positive whole package. Avoid fresh submissions that merely redraw #3670 because +0.2843% is far below the required +1% threshold. Recheck live crown before any submission.
