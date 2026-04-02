# Scripts

This directory contains the stable manuscript/reproducibility wrappers for the
historical standalone Boundary repository surface.

## Stable entrypoints

- `build_current_manuscript.sh`
  - builds the current standalone manuscript to a temp output directory
- `verify_active_review_surface.sh`
  - verifies that `manuscript/current/` contains only the current `.tex` / `.pdf` pair and checks `manuscript/checksums_active_review_surface_sha256.txt`
- `verify_current_package.sh`
  - verifies the active review surface first and then checks `manuscript/checksums_current_package_sha256.txt`
- `recompute_evidence.sh`
  - recomputes the bundled gate and rep1-vs-rep3 evidence tables

Boundary is a historical/source repository surface, but the stable public
interface for the current package remains the four entrypoints above.
