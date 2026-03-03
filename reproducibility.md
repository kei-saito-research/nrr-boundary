# Reproducibility

## 1) Manuscript build

```bash
cd manuscript/current
tectonic -X compile nrr-boundary_manuscript_v13.tex
```

## 2) Evidence recomputation

Recompute gate and rep1-vs-rep3 evidence tables from bundled processed/raw artifacts:

```bash
python3 stats/evidence/recompute_evidence.py
```

Expected key outputs:
- `stats/evidence/gate_recheck_all.csv`
- `stats/evidence/combo_rep1_vs_rep3_direction_check.csv`
- `stats/evidence/combo_rep1_vs_rep3_direction_summary.csv`

## 3) Expected values (v13 package)

- Stage B `parse_fail_session_rate`: `0.005556`
- Combo rep1 `parse_fail_session_rate`: `0.000000`
- Combo rep3 `parse_fail_session_rate`: `0.006944`
- Rep1-to-rep3 `direction_changed_cells`: `19/216`
- Direction zero threshold: `1e-12`

## 4) Scope caveat

`stats/stageb_all/gate_recheck_final.csv` and `stats/evidence/gate_recheck_all.csv` are intentionally based on different scopes, as documented in `README.md`.
