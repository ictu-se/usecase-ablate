import argparse
import csv
import json
from pathlib import Path

from score_artifact_ablation import load_jsonl, score_record


PROJECT = Path(__file__).resolve().parents[1]


def mean(values):
    vals = [v for v in values if v is not None]
    return sum(vals) / len(vals) if vals else None


def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", default=str(PROJECT / "results"))
    parser.add_argument("--oracle", default=str(PROJECT / "data/use_case_oracle.jsonl"))
    parser.add_argument("--thresholds", nargs="*", type=float, default=[0.20, 0.24, 0.28, 0.32, 0.36, 0.40])
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    results_dir = Path(args.results_dir)
    oracle = {row["repo"]: row for row in load_jsonl(args.oracle)}
    output_records = []
    for path in sorted(results_dir.glob("*_ablation_outputs.jsonl")):
        output_records.extend(load_jsonl(path))

    rows = []
    for threshold in args.thresholds:
        by_condition = {}
        for record in output_records:
            scored = score_record(record, oracle, match_threshold=threshold)
            by_condition.setdefault(scored["condition"], []).append(scored)
        for condition, group in sorted(by_condition.items()):
            rows.append({
                "match_threshold": threshold,
                "condition": condition,
                "rows": len(group),
                "parse_ok": mean(row["parse_ok"] for row in group),
                "use_case_recall": mean(row["use_case_recall"] for row in group),
                "path_fidelity": mean(row["path_fidelity"] for row in group),
                "unsupported_feature_rate": mean(row["unsupported_feature_rate"] for row in group),
                "composite_score": mean(row["composite_score"] for row in group),
            })

    out_path = Path(args.out) if args.out else results_dir / "threshold_sensitivity_by_condition.csv"
    write_csv(
        out_path,
        rows,
        ["match_threshold", "condition", "rows", "parse_ok", "use_case_recall", "path_fidelity", "unsupported_feature_rate", "composite_score"],
    )
    print(f"wrote {len(rows)} sensitivity rows to {out_path}")


if __name__ == "__main__":
    main()
