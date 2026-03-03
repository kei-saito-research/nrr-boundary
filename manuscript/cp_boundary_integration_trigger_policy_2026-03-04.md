# cp-Boundary Integration Trigger Policy (2026-03-04 JST)

## Purpose
Preserve the current decision on when to run a unified cp + Boundary integration rerun.

## Decision (locked for now)
- Keep integration design ready, but do not execute the rerun now.
- Prioritize distribution path work first:
  - IME moderation resolution
  - Core/Phi replacement timing
  - public visibility and external feedback intake

## Why deferred
- cp and Boundary are already valid as bounded-claim papers.
- Integration rerun improves series completeness, but has lower immediate return before external feedback appears.
- A full preregistered integration cycle can block near-term priority work for multiple days.

## Trigger-to-run conditions
Run the integration rerun only when at least one trigger is true:
1. External review asks for cp-Boundary relation testing (for example: confounding vs independence).
2. Internal inconsistency appears between cp failure regions and Boundary boundary-map interpretation.
3. Series planning explicitly promotes integration evidence to "Now=1".

## Statistical stance (pre-commit)
- Confirmatory: H1-H4
- Exploratory: H5-H6
- Keep this split fixed at rerun start.
- Do not move hypotheses between confirmatory and exploratory after result inspection.

## Scope guard
- This memo does not predict or pre-commit Guarantee conclusions.
- Policy and Policy-Verification are not started yet; integration rerun is not a release gate at this time.

## Revisit rule
- Re-check this decision when one of the trigger conditions is met.
- If no trigger appears, keep rerun deferred and allocate effort to next active series tasks.
