# Reproducibility (NRR-Boundary)

## Scope

This repository bundles the historical standalone Boundary manuscript package together with the
processed/raw evidence inputs needed to recompute the key gate and rep1-vs-rep3
evidence tables for that standalone line.
In the current cross-series execution order, this repository is a source/support surface rather than the live editable mainline; the live authority for this zone is the separate `NRR-Patterns` repo/worktree, while `nrr-principles` remains only as historical/source continuity for the integration history.

## Stable review-package commands

- Build the current manuscript to temp output:
  - `bash scripts/build_current_manuscript.sh`
  - output: `/tmp/nrr-boundary_current_build/nrr-boundary_manuscript_v23.pdf`
- Recompute the key evidence tables from bundled artifacts:
  - `bash scripts/recompute_evidence.sh`
- Verify the current review-package checksum manifest:
  - `bash scripts/verify_current_package.sh`

## Historical standalone package

- Main TeX: `manuscript/current/nrr-boundary_manuscript_v23.tex`
- PDF snapshot: `manuscript/current/nrr-boundary_manuscript_v23.pdf`
- Standalone manuscript figures:
  - `manuscript/current/stageb_provider_separated_heatmaps_v9_readable.png`
  - `manuscript/current/fig_provider_separated_heatmaps_v9_readable.png`
  - `manuscript/current/stageb_sign_flip_boundaries.png`
  - `manuscript/current/fig_sign_flip_boundaries.png`
- Checksum manifest: `manuscript/current/checksums_sha256.txt`

## Checksum policy

- `manuscript/current/checksums_sha256.txt` covers the tracked files that define the
  historical standalone package kept in `manuscript/current/`.
- Coverage includes the standalone main `.tex` file, the committed `.pdf`, and
  each figure asset consumed by that manuscript from `manuscript/current/`.
- Coverage excludes `checksums_sha256.txt` itself, older manuscript versions that may
  remain in `manuscript/current/` for local working continuity, and repo-specific
  artifacts outside `manuscript/current/` unless a separate manifest is provided.

## Fixed protocol settings

- Evidence recomputation scope: gate tables and rep1-vs-rep3 direction checks
- Key recomputation outputs:
  - `stats/evidence/gate_recheck_all.csv`
  - `stats/evidence/combo_rep1_vs_rep3_direction_check.csv`
  - `stats/evidence/combo_rep1_vs_rep3_direction_summary.csv`

## Artifact map

| Artifact | Command | Output |
|---|---|---|
| Historical standalone manuscript build | `bash scripts/build_current_manuscript.sh` | `/tmp/nrr-boundary_current_build/nrr-boundary_manuscript_v23.pdf` |
| Historical standalone package checksum verification | `bash scripts/verify_current_package.sh` | stdout verification for `manuscript/current/checksums_sha256.txt` |
| Evidence recomputation | `bash scripts/recompute_evidence.sh` | `stats/evidence/gate_recheck_all.csv`, `stats/evidence/combo_rep1_vs_rep3_direction_check.csv`, `stats/evidence/combo_rep1_vs_rep3_direction_summary.csv` |
| Historical standalone manuscript source snapshot | N/A (tracked artifact) | `manuscript/current/nrr-boundary_manuscript_v23.tex` |

## Expected values (v23 package)

- Stage B `parse_fail_session_rate`: `0.005556`
- Combo rep1 `parse_fail_session_rate`: `0.000000`
- Combo rep3 `parse_fail_session_rate`: `0.006944`
- Rep1-to-rep3 `direction_changed_cells`: `19/216`
- Direction zero threshold: `1e-12`

## Scope caveat

`stats/stageb_all/gate_recheck_final.csv` and `stats/evidence/gate_recheck_all.csv` are intentionally based on different scopes, as documented in `README.md`.
