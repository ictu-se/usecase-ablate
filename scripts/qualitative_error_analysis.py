import argparse
import csv
import importlib.util
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[0]
CENTRAL_DATA = ROOT / "datasets/03_artifact_ablation_study__data"


def load_score_module():
    path = PROJECT / "scripts/score_artifact_ablation.py"
    spec = importlib.util.spec_from_file_location("score_artifact_ablation", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


score = load_score_module()


IMPLEMENTATION_TERMS = re.compile(
    r"\b(controller|endpoint|api|repository|database|migration|schema|serializer|"
    r"middleware|route|model|entity|service|class|method|crud|http|post|get|put|delete)\b",
    re.I,
)
FRAMEWORK_TERMS = re.compile(
    r"\b(login|register|auth|password|dashboard|settings|profile|config|install|"
    r"run application|environment|cache|session|middleware)\b",
    re.I,
)
GENERIC_PATH_TERMS = re.compile(
    r"(config|migration|vendor|node_modules|middleware|auth|login|register|dashboard|settings)",
    re.I,
)


def load_jsonl(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def best_matches(use_cases, gold, threshold=0.28, actor_bonus=0.1):
    matches = {}
    used_pred = set()
    best_by_pred = {i: (0.0, None) for i in range(len(use_cases))}
    for gi, g in enumerate(gold):
        best = (0.0, None)
        for pi, p in enumerate(use_cases):
            sim = score.use_case_similarity(p, g, actor_bonus_weight=actor_bonus)
            if sim > best_by_pred[pi][0]:
                best_by_pred[pi] = (sim, gi)
            if pi in used_pred:
                continue
            if sim > best[0]:
                best = (sim, pi)
        if best[0] >= threshold and best[1] is not None:
            matches[best[1]] = (gi, best[0])
            used_pred.add(best[1])
    return matches, best_by_pred


def path_coverage(pred, gold):
    gold_paths = (
        score.split_paths(gold.get("code_paths", []))
        + score.split_paths(gold.get("api_paths", []))
        + score.split_paths(gold.get("test_paths", []))
    )
    pred_paths = score.split_paths(pred.get("evidence_paths", []))
    if not gold_paths:
        return ""
    hits = sum(1 for gp in gold_paths if any(score.path_hit(pp, gp) for pp in pred_paths))
    return hits / len(gold_paths)


def classify(record, pred, gold, match, best, gold_actors):
    text = " ".join([
        str(pred.get("actor", "")),
        str(pred.get("name", "")),
        str(pred.get("description", "")),
        " ".join(score.split_steps(pred.get("main_flow", []))),
    ])
    paths = " ".join(score.split_paths(pred.get("evidence_paths", [])))
    actor = score.norm(pred.get("actor", ""))
    actor_ok = any(actor and (actor == score.norm(a) or actor in score.norm(a) or score.norm(a) in actor) for a in gold_actors)

    if match:
        gi, sim = match
        pcov = path_coverage(pred, gold[gi])
        if pcov != "" and pcov == 0:
            return "matched_goal_missing_or_wrong_path"
        if not actor_ok:
            return "matched_goal_actor_label_drift"
        return "matched_supported_goal"

    if not actor_ok:
        return "actor_scope_error"
    if IMPLEMENTATION_TERMS.search(text):
        return "implementation_level_goal"
    if record["condition"] == "readme_only":
        return "readme_overgeneralization"
    if GENERIC_PATH_TERMS.search(paths) or FRAMEWORK_TERMS.search(text):
        return "framework_or_boilerplate_noise"
    if record["condition"] in {"random_code_same_budget", "full_selected_context", "readme_plus_code", "oracle_upper_bound"}:
        return "code_context_overgeneralization"
    if best[0] > 0.18:
        return "near_miss_or_partial_workflow"
    return "unsupported_domain_guess"


def short(value, limit=180):
    value = re.sub(r"\s+", " ", str(value or "")).strip()
    return value[: limit - 3] + "..." if len(value) > limit else value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("outputs_jsonl")
    parser.add_argument("--oracle", default=str(CENTRAL_DATA / "use_case_oracle.jsonl"))
    parser.add_argument("--out-dir", default=str(PROJECT / "analysis/qualitative_error_analysis"))
    parser.add_argument("--match-threshold", type=float, default=0.28)
    parser.add_argument("--actor-bonus", type=float, default=0.1)
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    oracle = {row["repo"]: row for row in load_jsonl(args.oracle)}

    coded = []
    for record in load_jsonl(args.outputs_jsonl):
        parsed = score.extract_json(record.get("stdout", ""))
        use_cases = score.pred_use_cases(parsed)
        gold = oracle[record["repo"]]["use_cases"]
        gold_actors = list({g["actor"] for g in gold})
        matches, best_by_pred = best_matches(use_cases, gold, args.match_threshold, args.actor_bonus)
        for idx, pred in enumerate(use_cases):
            match = matches.get(idx)
            best = best_by_pred.get(idx, (0.0, None))
            category = classify(record, pred, gold, match, best, gold_actors)
            gold_name = ""
            path_cov = ""
            if match:
                gi, _ = match
                gold_name = gold[gi]["use_case_name"]
                path_cov = path_coverage(pred, gold[gi])
            elif best[1] is not None:
                gold_name = gold[best[1]]["use_case_name"]
            coded.append({
                "repo": record["repo"],
                "condition": record["condition"],
                "model": record["model"],
                "pred_index": idx,
                "category": category,
                "actor": short(pred.get("actor", ""), 80),
                "name": short(pred.get("name", ""), 120),
                "description": short(pred.get("description", ""), 220),
                "evidence_paths": short(" | ".join(score.split_paths(pred.get("evidence_paths", []))), 220),
                "matched_gold": gold_name,
                "best_similarity": round(best[0], 4),
                "path_coverage": path_cov if path_cov == "" else round(path_cov, 4),
            })

    coding_fields = [
        "repo", "condition", "model", "pred_index", "category", "actor", "name",
        "description", "evidence_paths", "matched_gold", "best_similarity", "path_coverage",
    ]
    with (out_dir / "qualitative_error_coding.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=coding_fields)
        writer.writeheader()
        writer.writerows(coded)

    by_condition = defaultdict(Counter)
    by_category = Counter()
    for row in coded:
        by_condition[row["condition"]][row["category"]] += 1
        by_category[row["category"]] += 1

    categories = sorted(by_category)
    with (out_dir / "qualitative_error_summary_by_condition.csv").open("w", encoding="utf-8", newline="") as handle:
        summary_fields = ["condition", "n"] + categories
        writer = csv.DictWriter(handle, fieldnames=summary_fields)
        writer.writeheader()
        for condition, counts in sorted(by_condition.items()):
            total = sum(counts.values())
            row = {"condition": condition, "n": total}
            row.update({cat: counts[cat] for cat in categories})
            writer.writerow(row)

    with (out_dir / "qualitative_error_summary_by_category.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["category", "n", "percent"])
        writer.writeheader()
        total = len(coded)
        for cat, n in by_category.most_common():
            writer.writerow({"category": cat, "n": n, "percent": round(100 * n / total, 2) if total else 0})

    examples = []
    for cat in categories:
        candidates = [r for r in coded if r["category"] == cat]
        candidates.sort(key=lambda r: (r["condition"], r["repo"], r["pred_index"]))
        examples.extend(candidates[:3])
    with (out_dir / "qualitative_error_examples.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=coding_fields)
        writer.writeheader()
        writer.writerows(examples)

    print(f"coded {len(coded)} generated use cases into {out_dir}")
    print("category summary:")
    for cat, n in by_category.most_common():
        print(f"{cat}: {n}")


if __name__ == "__main__":
    main()
