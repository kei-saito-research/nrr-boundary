# Reproducibility (NRR-Boundary)

## Scope

This repository bundles the historical standalone Boundary manuscript package together with the
processed/raw evidence inputs needed to recompute the key gate and rep1-vs-rep3
evidence tables for that standalone line.
In the current cross-series execution order, this repository is a source/support surface rather than the live editable mainline; the live authority for this zone is the separate `NRR-Patterns` repo/worktree, while `nrr-principles` remains only as historical/source continuity for the integration history.

## Stable review-package commands

- Build the current manuscript to temp output:
  - `bash scripts/build_current_manuscript.sh`
  - output: `/tmp/nrr-boundary_current_build/nrr-boundary_manuscript_v24.pdf`
- Recompute the key evidence tables from bundled artifacts:
  - `bash scripts/recompute_evidence.sh`
- Verify the active review surface:
  - `bash scripts/verify_active_review_surface.sh`
- Verify the current review-package checksum manifest:
  - `bash scripts/verify_current_package.sh`

## Historical standalone package

- Main TeX: `manuscript/current/nrr-boundary_manuscript_v24.tex`
- PDF snapshot: `manuscript/current/nrr-boundary_manuscript_v24.pdf`
- Active review checksum manifest: `manuscript/checksums_active_review_surface_sha256.txt`
- Current package checksum manifest: `manuscript/checksums_current_package_sha256.txt`
- `manuscript/current/` is latest-only and contains only the active manuscript `.tex` / `.pdf` pair.
- Standalone manuscript figures:
  - `manuscript/figures/stageb_provider_separated_heatmaps_v9_readable.png`
  - `manuscript/figures/fig_provider_separated_heatmaps_v9_readable.png`
  - `manuscript/figures/stageb_sign_flip_boundaries.png`
  - `manuscript/figures/fig_sign_flip_boundaries.png`

## Checksum policy

- `manuscript/checksums_active_review_surface_sha256.txt` covers the active review
  surface and is limited to the committed current `.tex` / `.pdf` pair in
  `manuscript/current/`.
- `manuscript/checksums_current_package_sha256.txt` covers the historical standalone
  package needed to verify the current manuscript line, figure assets, and stable scripts.
- Older manuscript versions are not retained in `manuscript/current/`; version history
  is tracked through git history.

## Fixed protocol settings

- Evidence recomputation scope: gate tables and rep1-vs-rep3 direction checks
- Key recomputation outputs:
  - `stats/evidence/gate_recheck_all.csv`
  - `stats/evidence/combo_rep1_vs_rep3_direction_check.csv`
  - `stats/evidence/combo_rep1_vs_rep3_direction_summary.csv`

## Artifact map

| Artifact | Command | Output |
|---|---|---|
| Historical standalone manuscript build | `bash scripts/build_current_manuscript.sh` | `/tmp/nrr-boundary_current_build/nrr-boundary_manuscript_v24.pdf` |
| Active review surface verification | `bash scripts/verify_active_review_surface.sh` | stdout verification for `manuscript/checksums_active_review_surface_sha256.txt` plus latest-only checks on `manuscript/current/` |
| Historical standalone package checksum verification | `bash scripts/verify_current_package.sh` | stdout verification for `manuscript/checksums_current_package_sha256.txt` |
| Evidence recomputation | `bash scripts/recompute_evidence.sh` | `stats/evidence/gate_recheck_all.csv`, `stats/evidence/combo_rep1_vs_rep3_direction_check.csv`, `stats/evidence/combo_rep1_vs_rep3_direction_summary.csv` |
| Historical standalone manuscript source snapshot | N/A (tracked artifact) | `manuscript/current/nrr-boundary_manuscript_v24.tex` |

## Expected values (v23 package)

- Stage B `parse_fail_session_rate`: `0.005556`
- Combo rep1 `parse_fail_session_rate`: `0.000000`
- Combo rep3 `parse_fail_session_rate`: `0.006944`
- Rep1-to-rep3 `direction_changed_cells`: `19/216`
- Direction zero threshold: `1e-12`

## Scope caveat

`stats/stageb_all/gate_recheck_final.csv` and `stats/evidence/gate_recheck_all.csv` are intentionally based on different scopes, as documented in `README.md`.
