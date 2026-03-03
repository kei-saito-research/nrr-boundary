#!/usr/bin/env python3
import csv
import json
from pathlib import Path

ZERO_EPS_ABS = 1e-12


def read_csv(path: Path):
    with path.open('r', encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def parse_bool(v: str) -> bool:
    return str(v).strip().lower() == 'true'


def compute_gate(tag: str, pair_metrics_csv: Path, raw_all_dir: Path):
    rows = read_csv(pair_metrics_csv)
    total = len(rows)
    tau = sum(1 for r in rows if parse_bool(r['tau_trace_pass']))
    non = sum(1 for r in rows if parse_bool(r['non_effective']))

    parse_fail_turns = 0
    turns = 0
    parse_fail_sessions = 0
    sessions = 0

    for fp in sorted(raw_all_dir.glob('*.json')):
        with fp.open('r', encoding='utf-8') as f:
            data = json.load(f)
        for pair in data.get('pairs', []):
            for arm in (pair.get('arms') or {}).values():
                s_turns = ((arm.get('session_score') or {}).get('turns') or [])
                if not s_turns:
                    continue
                sessions += 1
                has_parse_fail = False
                for t in s_turns:
                    turns += 1
                    if t.get('parse_ok') is False:
                        parse_fail_turns += 1
                        has_parse_fail = True
                if has_parse_fail:
                    parse_fail_sessions += 1

    return {
        'tag': tag,
        'pair_metric_rows': total,
        'tau_trace_pass_rows': tau,
        'tau_trace_pass_rate': f"{(tau / total if total else 0.0):.6f}",
        'non_effective_rows': non,
        'non_effective_rate': f"{(non / total if total else 0.0):.6f}",
        'parse_fail_turns': parse_fail_turns,
        'turns': turns,
        'parse_fail_turn_rate': f"{(parse_fail_turns / turns if turns else 0.0):.6f}",
        'parse_fail_sessions': parse_fail_sessions,
        'sessions': sessions,
        'parse_fail_session_rate': f"{(parse_fail_sessions / sessions if sessions else 0.0):.6f}",
    }


def sign(v: float, eps: float) -> str:
    if v > eps:
        return 'positive'
    if v < -eps:
        return 'negative'
    return 'zero'


def compute_direction(rep1_csv: Path, rep3_csv: Path):
    r1 = read_csv(rep1_csv)
    r3 = read_csv(rep3_csv)

    def to_map(rows):
        out = {}
        for row in rows:
            key = (row['provider'], row['pattern'], row['metric'])
            out[key] = float(row['improvement_mean'])
        return out

    m1 = to_map(r1)
    m3 = to_map(r3)
    keys = sorted(set(m1.keys()) & set(m3.keys()))

    detail = []
    changed = 0
    for provider, pattern, metric in keys:
        v1 = m1[(provider, pattern, metric)]
        v3 = m3[(provider, pattern, metric)]
        d1 = sign(v1, ZERO_EPS_ABS)
        d3 = sign(v3, ZERO_EPS_ABS)
        ch = d1 != d3
        if ch:
            changed += 1
        detail.append({
            'provider': provider,
            'pattern': pattern,
            'metric': metric,
            'rep1_improvement_mean': f"{v1:.17g}",
            'rep3_improvement_mean': f"{v3:.17g}",
            'rep1_direction': d1,
            'rep3_direction': d3,
            'direction_changed': str(ch),
            'zero_eps_abs': f"{ZERO_EPS_ABS:.0e}",
        })

    summary = {
        'total_cells': len(detail),
        'direction_changed_cells': changed,
        'direction_change_rate': f"{(changed / len(detail) if detail else 0.0):.6f}",
        'zero_eps_abs': f"{ZERO_EPS_ABS:.0e}",
    }
    return detail, summary


def write_csv(path: Path, rows, fieldnames):
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main():
    evidence_dir = Path(__file__).resolve().parent
    stats_dir = evidence_dir.parent

    gate_rows = [
        compute_gate(
            'stageb_all',
            stats_dir / 'stageb_all' / 'mst_pair_metrics.csv',
            stats_dir / 'raw_stageb_all',
        ),
        compute_gate(
            'combo_rep1_all',
            stats_dir / 'combo_rep1_all' / 'mst_pair_metrics.csv',
            stats_dir / 'raw_combo_rep1_all',
        ),
        compute_gate(
            'combo_rep3_all',
            stats_dir / 'combo_rep3_all' / 'mst_pair_metrics.csv',
            stats_dir / 'raw_combo_rep3_all',
        ),
    ]

    gate_fields = [
        'tag', 'pair_metric_rows',
        'tau_trace_pass_rows', 'tau_trace_pass_rate',
        'non_effective_rows', 'non_effective_rate',
        'parse_fail_turns', 'turns', 'parse_fail_turn_rate',
        'parse_fail_sessions', 'sessions', 'parse_fail_session_rate',
    ]
    write_csv(evidence_dir / 'gate_recheck_all.csv', gate_rows, gate_fields)

    detail, summary = compute_direction(
        stats_dir / 'combo_rep1_all' / 'mst_provider_separated.csv',
        stats_dir / 'combo_rep3_all' / 'mst_provider_separated.csv',
    )

    detail_fields = [
        'provider', 'pattern', 'metric',
        'rep1_improvement_mean', 'rep3_improvement_mean',
        'rep1_direction', 'rep3_direction', 'direction_changed',
        'zero_eps_abs',
    ]
    write_csv(evidence_dir / 'combo_rep1_vs_rep3_direction_check.csv', detail, detail_fields)

    summary_fields = ['total_cells', 'direction_changed_cells', 'direction_change_rate', 'zero_eps_abs']
    write_csv(evidence_dir / 'combo_rep1_vs_rep3_direction_summary.csv', [summary], summary_fields)


if __name__ == '__main__':
    main()
