import argparse
import csv
from collections import defaultdict
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]


def read_csv(path):
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def as_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def mean(values):
    vals = [v for v in values if v is not None]
    return sum(vals) / len(vals) if vals else None


def stdev(values):
    vals = [v for v in values if v is not None]
    if len(vals) < 2:
        return 0.0 if vals else None
    avg = sum(vals) / len(vals)
    return (sum((v - avg) ** 2 for v in vals) / (len(vals) - 1)) ** 0.5


def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with Path(path).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def model_family(model):
    if model.startswith("qwen2.5-coder"):
        return "qwen-coder"
    if model.startswith("qwen2.5vl"):
        return "qwen-vl"
    if model.startswith("qwen2.5"):
        return "qwen-text"
    if model.startswith("llama3.2-vision"):
        return "llama-vision"
    if model.startswith("llama3.2"):
        return "llama-text"
    if model.startswith("gemma"):
        return "gemma"
    if model.startswith("granite"):
        return "granite"
    return "other"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", default=str(PROJECT / "results"))
    parser.add_argument("--figures-dir", default=str(PROJECT / "figures"))
    args = parser.parse_args()
    results_dir = Path(args.results_dir)
    figures_dir = Path(args.figures_dir)

    rows = []
    for path in sorted(results_dir.glob("*_ablation_metrics.csv")):
        rows.extend(read_csv(path))

    metric_names = [
        "parse_ok",
        "actor_recall",
        "use_case_recall",
        "path_fidelity",
        "behavior_coverage",
        "unsupported_feature_rate",
        "elapsed_sec",
        "composite_score",
        "artifact_chars",
        "predicted_use_cases",
    ]

    by_condition = defaultdict(list)
    pooled_by_condition = defaultdict(list)
    by_repo_condition = defaultdict(list)
    by_model_repo_condition = defaultdict(list)
    for row in rows:
        by_condition[(row["model"], row["condition"])].append(row)
        pooled_by_condition[row["condition"]].append(row)
        by_repo_condition[(row["repo"], row["condition"])].append(row)
        by_model_repo_condition[(row["model"], row["repo"], row["condition"])].append(row)

    summary = []
    for (model, condition), group in sorted(by_condition.items()):
        out = {"model": model, "condition": condition, "rows": len(group)}
        for metric in metric_names:
            out[metric] = mean(as_float(row.get(metric)) for row in group)
        summary.append(out)

    fields = ["model", "condition", "rows"] + metric_names
    write_csv(results_dir / "ablation_summary_by_condition.csv", summary, fields)

    pooled_summary = []
    for condition, group in sorted(pooled_by_condition.items()):
        out = {"condition": condition, "rows": len(group)}
        for metric in metric_names:
            out[metric] = mean(as_float(row.get(metric)) for row in group)
        pooled_summary.append(out)
    pooled_fields = ["condition", "rows"] + metric_names
    write_csv(results_dir / "ablation_summary_pooled_by_condition.csv", pooled_summary, pooled_fields)

    repo_summary = []
    for (repo, condition), group in sorted(by_repo_condition.items()):
        out = {"repo": repo, "condition": condition, "rows": len(group)}
        for metric in metric_names:
            out[metric] = mean(as_float(row.get(metric)) for row in group)
        repo_summary.append(out)
    write_csv(results_dir / "ablation_summary_by_repo.csv", repo_summary, ["repo", "condition", "rows"] + metric_names)

    best_by_model = []
    grouped_by_model = defaultdict(list)
    for row in summary:
        grouped_by_model[row["model"]].append(row)
    for model, group in sorted(grouped_by_model.items()):
        best = max(group, key=lambda row: row["composite_score"] if row["composite_score"] is not None else -1)
        best_by_model.append({
            "model": model,
            "best_condition": best["condition"],
            "composite_score": best["composite_score"],
            "use_case_recall": best["use_case_recall"],
            "path_fidelity": best["path_fidelity"],
            "unsupported_feature_rate": best["unsupported_feature_rate"],
            "elapsed_sec": best["elapsed_sec"],
        })
    write_csv(
        results_dir / "ablation_best_per_model.csv",
        best_by_model,
        ["model", "best_condition", "composite_score", "use_case_recall", "path_fidelity", "unsupported_feature_rate", "elapsed_sec"],
    )

    by_family = defaultdict(list)
    for row in best_by_model:
        by_family[model_family(row["model"])].append(row)
    family_summary = []
    for family, group in sorted(by_family.items()):
        best = max(group, key=lambda row: row["composite_score"] if row["composite_score"] is not None else -1)
        family_summary.append({
            "family": family,
            "models": len(group),
            "mean_best_score": mean(row["composite_score"] for row in group),
            "mean_best_use_case_recall": mean(row["use_case_recall"] for row in group),
            "mean_best_path_fidelity": mean(row["path_fidelity"] for row in group),
            "mean_best_unsupported_feature_rate": mean(row["unsupported_feature_rate"] for row in group),
            "mean_best_elapsed_sec": mean(row["elapsed_sec"] for row in group),
            "best_model": best["model"],
            "best_condition": best["best_condition"],
            "best_score": best["composite_score"],
        })
    write_csv(
        results_dir / "ablation_summary_by_family.csv",
        family_summary,
        [
            "family",
            "models",
            "mean_best_score",
            "mean_best_use_case_recall",
            "mean_best_path_fidelity",
            "mean_best_unsupported_feature_rate",
            "mean_best_elapsed_sec",
            "best_model",
            "best_condition",
            "best_score",
        ],
    )

    record_lookup = {}
    for key, group in by_model_repo_condition.items():
        row = {}
        for metric in metric_names:
            row[metric] = mean(as_float(item.get(metric)) for item in group)
        record_lookup[key] = row

    comparisons = [
        ("readme_plus_code_minus_readme_only", "readme_plus_code", "readme_only"),
        ("full_minus_readme_plus_code", "full_selected_context", "readme_plus_code"),
        ("readme_plus_code_minus_file_tree", "readme_plus_code", "file_tree_only"),
        ("routes_minus_file_tree", "routes_controllers", "file_tree_only"),
        ("models_minus_file_tree", "models_services", "file_tree_only"),
    ]
    paired_rows = []
    for model in sorted({row["model"] for row in rows}):
        repos = sorted({row["repo"] for row in rows if row["model"] == model})
        for label, left, right in comparisons:
            diffs = {metric: [] for metric in ["composite_score", "use_case_recall", "path_fidelity", "unsupported_feature_rate", "elapsed_sec"]}
            for repo in repos:
                left_row = record_lookup.get((model, repo, left))
                right_row = record_lookup.get((model, repo, right))
                if not left_row or not right_row:
                    continue
                for metric in diffs:
                    lv = left_row.get(metric)
                    rv = right_row.get(metric)
                    if lv is not None and rv is not None:
                        diffs[metric].append(lv - rv)
            out = {"model": model, "comparison": label, "pairs": len(diffs["composite_score"])}
            for metric, values in diffs.items():
                out[f"{metric}_delta_mean"] = mean(values)
                out[f"{metric}_delta_sd"] = stdev(values)
            paired_rows.append(out)

    pooled_repo_condition = {}
    for (repo, condition), group in by_repo_condition.items():
        row = {}
        for metric in metric_names:
            row[metric] = mean(as_float(item.get(metric)) for item in group)
        pooled_repo_condition[(repo, condition)] = row
    for label, left, right in comparisons:
        diffs = {metric: [] for metric in ["composite_score", "use_case_recall", "path_fidelity", "unsupported_feature_rate", "elapsed_sec"]}
        repos = sorted({repo for repo, _ in pooled_repo_condition})
        for repo in repos:
            left_row = pooled_repo_condition.get((repo, left))
            right_row = pooled_repo_condition.get((repo, right))
            if not left_row or not right_row:
                continue
            for metric in diffs:
                lv = left_row.get(metric)
                rv = right_row.get(metric)
                if lv is not None and rv is not None:
                    diffs[metric].append(lv - rv)
        out = {"model": "pooled", "comparison": label, "pairs": len(diffs["composite_score"])}
        for metric, values in diffs.items():
            out[f"{metric}_delta_mean"] = mean(values)
            out[f"{metric}_delta_sd"] = stdev(values)
        paired_rows.append(out)

    paired_fields = ["model", "comparison", "pairs"]
    for metric in ["composite_score", "use_case_recall", "path_fidelity", "unsupported_feature_rate", "elapsed_sec"]:
        paired_fields.extend([f"{metric}_delta_mean", f"{metric}_delta_sd"])
    write_csv(results_dir / "ablation_paired_deltas.csv", paired_rows, paired_fields)

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib unavailable; skipped figures")
        return

    figures_dir.mkdir(parents=True, exist_ok=True)
    order = [
        "readme_only",
        "file_tree_only",
        "readme_plus_tree",
        "routes_controllers",
        "models_services",
        "readme_plus_code",
        "full_selected_context",
    ]
    compact = {
        "readme_only": "README",
        "file_tree_only": "Tree",
        "readme_plus_tree": "README+tree",
        "routes_controllers": "Routes",
        "models_services": "Models",
        "readme_plus_code": "README+code",
        "full_selected_context": "Full",
    }
    plot_rows = pooled_summary
    plot_rows = sorted(plot_rows, key=lambda r: order.index(r["condition"]))
    labels = [compact[r["condition"]] for r in plot_rows]
    scores = [r["composite_score"] for r in plot_rows]
    unsupported = [r["unsupported_feature_rate"] for r in plot_rows]

    fig, ax = plt.subplots(figsize=(8.8, 3.8))
    ax.bar(range(len(labels)), scores, color="#356f8a")
    ax.set_ylabel("Composite score")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=30, ha="right")
    ax.set_ylim(0, max(scores) * 1.18 if scores else 1)
    fig.tight_layout()
    fig.savefig(figures_dir / "fig_ablation_condition_score.pdf")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8.8, 3.8))
    ax.bar(range(len(labels)), unsupported, color="#b65f4a")
    ax.set_ylabel("Unsupported feature rate")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=30, ha="right")
    ax.set_ylim(0, min(1, max(unsupported) * 1.25) if unsupported else 1)
    fig.tight_layout()
    fig.savefig(figures_dir / "fig_ablation_unsupported_rate.pdf")
    plt.close(fig)

    if best_by_model:
        best_sorted = sorted(best_by_model, key=lambda r: r["composite_score"])
        y_labels = [r["model"].replace("qwen2.5-coder:", "qwen-coder-").replace(":latest", "") for r in best_sorted]
        y_pos = list(range(len(best_sorted)))
        fig, ax = plt.subplots(figsize=(8.8, max(3.8, len(best_sorted) * 0.38)))
        ax.barh(y_pos, [r["composite_score"] for r in best_sorted], color="#4f7d56")
        ax.set_xlabel("Best-condition composite score")
        ax.set_yticks(y_pos)
        ax.set_yticklabels(y_labels)
        fig.tight_layout()
        fig.savefig(figures_dir / "fig_ablation_best_model_score.pdf")
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(6.8, 4.2))
        ax.scatter(
            [r["elapsed_sec"] for r in best_by_model],
            [r["composite_score"] for r in best_by_model],
            color="#654ea3",
        )
        for r in best_by_model:
            label = r["model"].replace("qwen2.5-coder:", "q-coder-").replace(":latest", "")
            ax.annotate(label, (r["elapsed_sec"], r["composite_score"]), fontsize=7, xytext=(3, 3), textcoords="offset points")
        ax.set_xlabel("Mean seconds per run")
        ax.set_ylabel("Best-condition composite score")
        fig.tight_layout()
        fig.savefig(figures_dir / "fig_ablation_runtime_quality.pdf")
        plt.close(fig)

    print(f"wrote {len(summary)} condition rows, {len(best_by_model)} best-model rows, {len(family_summary)} family rows, and figures to {figures_dir}")


if __name__ == "__main__":
    main()
