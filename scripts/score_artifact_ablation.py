import argparse
import csv
import json
import re
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]


def load_jsonl(path):
    rows = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def extract_json(text):
    if not text:
        return None
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        parsed = json.loads(text)
        return parsed if isinstance(parsed, dict) else None
    except json.JSONDecodeError:
        pass
    start, end = text.find("{"), text.rfind("}")
    if start >= 0 and end > start:
        try:
            parsed = json.loads(text[start:end + 1])
            return parsed if isinstance(parsed, dict) else None
        except json.JSONDecodeError:
            return None
    return None


def norm(text):
    return re.sub(r"[^a-z0-9]+", " ", str(text or "").lower()).strip()


def tokens(text):
    return {t for t in norm(text).split() if len(t) > 2}


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def split_steps(value):
    if not value:
        return []
    if isinstance(value, list):
        return [str(v) for v in value if str(v).strip()]
    return [p.strip() for p in re.split(r"\s*\|\s*", str(value)) if p.strip()]


def split_paths(value):
    if not value:
        return []
    if isinstance(value, list):
        parts = value
    else:
        parts = re.split(r"\s*\|\s*", str(value))
    return [str(p).strip().strip("`'\"") for p in parts if str(p).strip()]


def pred_use_cases(parsed):
    if not isinstance(parsed, dict):
        return []
    value = parsed.get("use_cases", [])
    if not isinstance(value, list):
        return []
    out = []
    for item in value:
        if isinstance(item, dict):
            out.append(item)
    return out


def pred_actors(parsed, use_cases):
    actors = []
    if isinstance(parsed, dict) and isinstance(parsed.get("actors"), list):
        actors.extend(str(a) for a in parsed["actors"])
    actors.extend(str(uc.get("actor", "")) for uc in use_cases)
    return list(dict.fromkeys(a.strip() for a in actors if a.strip()))


def use_case_similarity(pred, gold):
    pred_text = " ".join([
        str(pred.get("name", "")),
        str(pred.get("description", "")),
        " ".join(split_steps(pred.get("main_flow", []))),
    ])
    gold_text = " ".join([
        gold["use_case_name"],
        gold["description"],
        " ".join(split_steps(gold["main_flow"])),
    ])
    name_score = jaccard(tokens(pred.get("name", "")), tokens(gold["use_case_name"]))
    text_score = jaccard(tokens(pred_text), tokens(gold_text))
    actor_bonus = 0.1 if norm(pred.get("actor", "")) == norm(gold["actor"]) else 0.0
    return max(name_score, text_score + actor_bonus)


def path_hit(pred, gold):
    pred = str(pred or "").strip().strip("`'\"").replace("\\", "/")
    gold = str(gold or "").strip().strip("`'\"").replace("\\", "/")
    if not pred or not gold:
        return False
    return pred == gold or pred.endswith("/" + gold) or gold.endswith("/" + pred) or pred in gold or gold in pred


def score_record(record, oracle):
    parsed = extract_json(record.get("stdout", ""))
    gold = oracle[record["repo"]]["use_cases"]
    use_cases = pred_use_cases(parsed)
    actors = pred_actors(parsed, use_cases)
    gold_actors = list({g["actor"] for g in gold})

    actor_hits = sum(1 for ga in gold_actors if any(norm(ga) == norm(pa) or norm(ga) in norm(pa) or norm(pa) in norm(ga) for pa in actors))
    actor_recall = actor_hits / len(gold_actors) if gold_actors else 0.0

    matches = []
    used_pred = set()
    for gi, g in enumerate(gold):
        best = (0.0, None)
        for pi, p in enumerate(use_cases):
            if pi in used_pred:
                continue
            score = use_case_similarity(p, g)
            if score > best[0]:
                best = (score, pi)
        if best[0] >= 0.28 and best[1] is not None:
            matches.append((gi, best[1], best[0]))
            used_pred.add(best[1])

    use_case_recall = len(matches) / len(gold) if gold else 0.0
    unsupported_rate = max(0, len(use_cases) - len(matches)) / len(use_cases) if use_cases else 0.0

    path_scores = []
    behavior_scores = []
    for gi, pi, _ in matches:
        g = gold[gi]
        p = use_cases[pi]
        gold_paths = split_paths(g.get("code_paths", [])) + split_paths(g.get("api_paths", [])) + split_paths(g.get("test_paths", []))
        pred_paths = split_paths(p.get("evidence_paths", []))
        if gold_paths:
            path_scores.append(sum(1 for gp in gold_paths if any(path_hit(pp, gp) for pp in pred_paths)) / len(gold_paths))
        gold_behavior = tokens(g["description"] + " " + " ".join(split_steps(g["main_flow"])))
        pred_behavior = tokens(str(p.get("description", "")) + " " + " ".join(split_steps(p.get("main_flow", []))))
        behavior_scores.append(jaccard(pred_behavior, gold_behavior))

    path_fidelity = sum(path_scores) / len(path_scores) if path_scores else 0.0
    behavior_coverage = sum(behavior_scores) / len(behavior_scores) if behavior_scores else 0.0
    parse_ok = int(parsed is not None)
    composite = 100 * (
        0.20 * actor_recall
        + 0.35 * use_case_recall
        + 0.20 * path_fidelity
        + 0.15 * behavior_coverage
        + 0.10 * (1 - unsupported_rate)
    )
    return {
        "repo": record["repo"],
        "project": record["project"],
        "condition": record["condition"],
        "model": record["model"],
        "artifact_chars": record.get("artifact_chars", ""),
        "gold_use_cases": len(gold),
        "predicted_use_cases": len(use_cases),
        "matched_use_cases": len(matches),
        "parse_ok": parse_ok,
        "actor_recall": actor_recall,
        "use_case_recall": use_case_recall,
        "path_fidelity": path_fidelity,
        "behavior_coverage": behavior_coverage,
        "unsupported_feature_rate": unsupported_rate,
        "elapsed_sec": record.get("elapsed_sec", ""),
        "composite_score": composite,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("outputs_jsonl")
    parser.add_argument("--oracle", default=str(PROJECT / "data/use_case_oracle.jsonl"))
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    oracle = {row["repo"]: row for row in load_jsonl(args.oracle)}
    rows = [score_record(record, oracle) for record in load_jsonl(args.outputs_jsonl)]
    out_path = Path(args.out) if args.out else PROJECT / "results" / (Path(args.outputs_jsonl).stem + "_metrics.csv")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()) if rows else [])
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} metric rows to {out_path}")


if __name__ == "__main__":
    main()
