# NRR-Boundary: Same Operators, Opposite Effects by Provider and Order

NRR-Boundary is a historical/source repository for the older standalone Boundary manuscript and the reproducibility artifacts around Stage B and ordered-combination follow-up checks.
In the current cross-series execution order, this repository is not the live mainline; its evidence is carried forward as a supporting/package-first surface around `NRR-Patterns`, the current authority for integrated `paper7`.

NRR is not an anti-LLM framework.
NRR does not replace standard LLM use.
NRR optimizes when to commit and when to defer, under explicit conditions.
Series numbering policy: `paper3` is permanently skipped and never reused.

Part of the Non-Resolution Reasoning (NRR) research program.

Mainline note:
- this standalone Boundary repository is not the current editable mainline
- the current authority for this zone is the separate `NRR-Patterns` repo/worktree
- `nrr-principles` remains only as historical/source continuity for the integration history
- treat this repository as a historical/source evidence surface unless a thread explicitly reopens it

## NRR Series Hub (Start here)

For the cross-paper map and current series links, start here:
- [NRR Series Hub](https://github.com/kei-saito-research/nrr-series-hub)

## Historical standalone manuscript snapshot

- Source: `manuscript/current/nrr-boundary_manuscript_v24.tex`
- PDF: `manuscript/current/nrr-boundary_manuscript_v24.pdf`
- Active review checksum manifest: `manuscript/checksums_active_review_surface_sha256.txt`
- Current package checksum manifest: `manuscript/checksums_current_package_sha256.txt`
- `manuscript/current/` is latest-only and keeps only the active manuscript `.tex` / `.pdf` pair.
- Figures used by manuscript:
  - `manuscript/figures/stageb_provider_separated_heatmaps_v9_readable.png`
  - `manuscript/figures/fig_provider_separated_heatmaps_v9_readable.png`
  - `manuscript/figures/stageb_sign_flip_boundaries.png`
  - `manuscript/figures/fig_sign_flip_boundaries.png`

## Historical evidence bundle

- Stage B processed metrics: `stats/stageb_all/`
- Combo rep1 processed metrics: `stats/combo_rep1_all/`
- Combo rep3 processed metrics: `stats/combo_rep3_all/`
- Primary raw JSON evidence for gate parse-fail recomputation:
  - `stats/raw_stageb_all/`
  - `stats/raw_combo_rep1_all/`
  - `stats/raw_combo_rep3_all/`
- Derived evidence and recompute script: `stats/evidence/`

## Scope note (gate parse-fail)

`stats/stageb_all/gate_recheck_final.csv` includes the original run scope (`all` row based on 2025 pair-metric rows), while `stats/evidence/gate_recheck_all.csv` is recomputed from the bundled full-scope pair-metrics table in `stats/stageb_all/` (2430 rows).

## Direction rule note

Rep1-to-rep3 direction labels use `abs(improvement_mean) <= 1e-12 => zero`.
The threshold is recorded as `zero_eps_abs` in:
- `stats/evidence/combo_rep1_vs_rep3_direction_check.csv`
- `stats/evidence/combo_rep1_vs_rep3_direction_summary.csv`

## Repository structure

```text
nrr-boundary/
|-- README.md
|-- LICENSE
|-- reproducibility.md
|-- manuscript/
|   |-- checksums_active_review_surface_sha256.txt
|   |-- checksums_current_package_sha256.txt
|   |-- figures/
|   |   |-- stageb_provider_separated_heatmaps_v9_readable.png
|   |   |-- fig_provider_separated_heatmaps_v9_readable.png
|   |   |-- stageb_sign_flip_boundaries.png
|   |   `-- fig_sign_flip_boundaries.png
|   `-- current/
|       |-- nrr-boundary_manuscript_v24.tex
|       `-- nrr-boundary_manuscript_v24.pdf
|-- scripts/
|   |-- README.md
|   |-- build_current_manuscript.sh
|   |-- verify_active_review_surface.sh
|   |-- verify_current_package.sh
|   `-- recompute_evidence.sh
`-- stats/
    |-- stageb_all/
    |-- combo_rep1_all/
    |-- combo_rep3_all/
    |-- raw_stageb_all/
    |-- raw_combo_rep1_all/
    |-- raw_combo_rep3_all/
    `-- evidence/
```

## License

CC BY 4.0. See `LICENSE`.

Stable review-package entrypoints:
- `bash scripts/build_current_manuscript.sh`
- `bash scripts/verify_active_review_surface.sh`
- `bash scripts/verify_current_package.sh`
- `bash scripts/recompute_evidence.sh`
