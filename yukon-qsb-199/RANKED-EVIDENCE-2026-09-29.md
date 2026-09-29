# Ranked evidence — 2026-09-29 08:07 ART

Fresh public benchmark evidence:

- PR #2379 completed verified at 1,010,433,501/s versus the promoted 1,008,206,828/s. This is a positive +0.2209% result for its affine-delta / centered-divstep experiment, but it misses the 1% promotion gate.
- PR #2401 completed verified at 1,009,130,757/s, about +0.0916%. Its direct-plan / subring-4 / four-slot composition is positive but weaker.
- The earlier clean SHA-tail donor #2282 remains stronger at 1,012,807,365/s.
- PR #2406, #2403, and #2405 are currently running; no performance claim should be made before their official results land.

Current promotion floor from 1,008,206,828/s at 100 bips: 1,018,288,897/s.

The clean SHA-tail donor remains 5,481,532/s, about 0.5412%, below that floor. The standalone +0.2209% from #2379 is not enough to bridge that gap even under optimistic multiplicative composition, so SHA-tail plus that mechanism is not yet a justified evaluation target.

Decision: retain #2282 as the strongest clean donor and wait for a measured orthogonal mechanism of roughly >=0.55% before freezing a candidate. This avoids spending an official evaluation on a composition that current measurements predict will miss the gate.
