import argparse
import csv
import hashlib
import json
import math
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[0]
csv.field_size_limit(sys.maxsize)

CONDITIONS = [
    "readme_only",
    "file_tree_only",
    "readme_plus_tree",
    "routes_controllers",
    "models_services",
    "readme_plus_code",
    "bm25_retrieved_code",
    "random_code_same_budget",
    "full_selected_context",
    "oracle_upper_bound",
]

TEXT_EXTS = {
    ".py", ".java", ".js", ".ts", ".tsx", ".jsx", ".php", ".rb", ".go",
    ".cs", ".kt", ".scala", ".html", ".vue", ".xml", ".yml", ".yaml",
    ".json", ".md", ".txt", ".properties", ".gradle", ".toml",
}

SKIP_DIRS = {
    ".git", "node_modules", "vendor", "venv", ".venv", "__pycache__",
    "dist", "build", "target", ".next", ".idea", ".vscode", "migrations",
    "static", "media", "assets", "ss", "storage", "public", "cache",
    "logs", "lang", "fonts", "css", "js",
    "db", "database", "templates",
}


def clean_key(row):
    return {k.lstrip("\ufeff"): v for k, v in row.items()}


def split_paths(value):
    if not value:
        return []
    out = []
    for item in re.split(r"\s*\|\s*", value):
        item = item.strip()
        if item and item not in out:
            out.append(item)
    return out


def unique(items):
    return list(dict.fromkeys(item for item in items if item))


def tokens(text):
    return [t for t in re.sub(r"[^a-z0-9]+", " ", str(text or "").lower()).split() if len(t) > 2]


def clip(text, limit):
    if not isinstance(text, str):
        return ""
    text = text.strip()
    if len(text) <= limit:
        return text
    return text[:limit] + "\n...[truncated]..."


def read_text(path, limit=12000):
    try:
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            return clip(handle.read(limit + 1000), limit)
    except OSError:
        return ""


def rel_files(repo_dir, max_files=2500):
    files = []
    for dirpath, dirnames, filenames in os.walk(repo_dir):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".git")]
        base = Path(dirpath)
        for filename in filenames:
            path = base / filename
            if path.suffix.lower() not in TEXT_EXTS:
                continue
            rel = path.relative_to(repo_dir)
            files.append(rel.as_posix())
            if len(files) >= max_files:
                return sorted(files)
    return sorted(files)


def path_tree(paths, limit=220):
    tree = {}
    for path in paths:
        node = tree
        for part in path.split("/"):
            node = node.setdefault(part, {})
    lines = []

    def walk(node, prefix="", depth=0):
        if len(lines) >= limit or depth > 5:
            return
        for name in sorted(node):
            lines.append(f"{prefix}{name}")
            walk(node[name], prefix + "  ", depth + 1)

    walk(tree)
    return "\n".join(lines)


def read_readmes(repo_dir):
    readmes = []
    for path in sorted(repo_dir.glob("README*")) + sorted(repo_dir.glob("readme*")):
        if path.is_file() and path.suffix.lower() in {".md", ".txt", ""}:
            readmes.append(f"## {path.name}\n{read_text(path, 10000)}")
    return "\n\n".join(readmes)


def classify_files(paths):
    route_patterns = re.compile(r"(urls|routes|router|controller|view|views|api|endpoint)", re.I)
    model_patterns = re.compile(r"(model|models|service|services|serializer|schema|entity|repository|form|forms)", re.I)
    test_patterns = re.compile(r"(^|/)(test|tests|spec|__tests__)(/|_)|(_test|\\.test|\\.spec)", re.I)
    routes = [p for p in paths if route_patterns.search(p)]
    models = [p for p in paths if model_patterns.search(p)]
    tests = [p for p in paths if test_patterns.search(p)]
    return routes, models, tests


def path_priority(path):
    lower = path.lower()
    score = 0
    if re.search(r"(urls|routes|router|controller|view|views|api|endpoint)", lower):
        score += 60
    if re.search(r"(model|models|service|services|serializer|schema|entity|repository|form|forms)", lower):
        score += 45
    if re.search(r"(^|/)(test|tests|spec|__tests__)(/|_)|(_test|\\.test|\\.spec)", lower):
        score += 15
    if re.search(r"(student|course|class|book|library|user|admin|teacher|school|learn|lesson)", lower):
        score += 8
    return (-score, path.count("/"), len(path), path)


def snippet_block(repo_dir, paths, max_files=18, per_file=2600, total=30000):
    chunks = []
    used = 0
    for rel in paths[:max_files]:
        text = read_text(repo_dir / rel, per_file)
        if not text:
            continue
        chunk = f"### {rel}\n{text}"
        if used + len(chunk) > total:
            remaining = max(0, total - used)
            if remaining < 400:
                break
            chunk = clip(chunk, remaining)
        chunks.append(chunk)
        used += len(chunk)
        if used >= total:
            break
    return "\n\n".join(chunks)


def bm25_select(repo_dir, paths, query_text, max_files=22):
    candidates = []
    docs = []
    for rel in paths:
        text = read_text(repo_dir / rel, 2200)
        if not text:
            continue
        doc_tokens = tokens(rel.replace("/", " ") + " " + text)
        if not doc_tokens:
            continue
        candidates.append(rel)
        docs.append(doc_tokens)
    if not candidates:
        return []

    query = Counter(tokens(query_text))
    if not query:
        query = Counter(tokens("student course class book library user admin teacher school learning management"))
    df = Counter()
    for doc in docs:
        for token in set(doc):
            df[token] += 1
    avgdl = sum(len(doc) for doc in docs) / len(docs)
    n_docs = len(docs)
    k1 = 1.2
    b = 0.75
    scored = []
    for rel, doc in zip(candidates, docs):
        counts = Counter(doc)
        score = 0.0
        for token, qtf in query.items():
            if token not in counts:
                continue
            idf = math.log(1 + (n_docs - df[token] + 0.5) / (df[token] + 0.5))
            denom = counts[token] + k1 * (1 - b + b * len(doc) / avgdl)
            score += idf * ((counts[token] * (k1 + 1)) / denom) * min(qtf, 3)
        if score:
            scored.append((score, path_priority(rel), rel))
    return [rel for _, _, rel in sorted(scored, key=lambda item: (-item[0], item[1]))[:max_files]]


def deterministic_random(paths, repo, max_files=22):
    def key(path):
        return hashlib.sha256(f"{repo}:{path}".encode("utf-8")).hexdigest()
    return sorted(paths, key=key)[:max_files]


def oracle_summary(rows):
    lines = []
    for row in rows:
        lines.append({
            "actor": row["actor"],
            "use_case_name": row["use_case_name"],
            "description": row["description"],
            "main_flow": split_paths(row["main_flow"]),
            "code_paths": split_paths(row["code_paths"]),
            "api_paths": split_paths(row["api_paths"]),
            "test_paths": split_paths(row["test_paths"]),
        })
    return lines


def build_pack(repo_dir, repo_rows, condition):
    paths = rel_files(repo_dir)
    routes, models, tests = classify_files(paths)
    readme = read_readmes(repo_dir)
    tree = path_tree(paths)
    code_candidates = sorted(unique(routes + models), key=path_priority)
    all_code = [
        p for p in paths
        if not p.lower().endswith((".md", ".txt", ".json", ".yml", ".yaml", ".properties", ".toml"))
    ]
    heuristic_full = sorted(unique(routes + models + tests), key=path_priority)
    retrieval_query = " ".join([
        repo_dir.name.replace("__", " ").replace("-", " ").replace("_", " "),
        readme,
        "\n".join(paths[:300]),
    ])
    oracle_paths = []
    for row in repo_rows:
        oracle_paths.extend(split_paths(row["code_paths"]))
        oracle_paths.extend(split_paths(row["test_paths"]))
    oracle_paths = [p for p in unique(oracle_paths) if (repo_dir / p).exists()]

    if condition == "readme_only":
        body = f"# README\n{readme or '[no README found]'}"
    elif condition == "file_tree_only":
        body = f"# File tree\n{tree}"
    elif condition == "readme_plus_tree":
        body = f"# README\n{readme or '[no README found]'}\n\n# File tree\n{tree}"
    elif condition == "routes_controllers":
        selected = sorted(routes, key=path_priority)
        body = "# Routes/controllers\n" + snippet_block(repo_dir, selected)
    elif condition == "models_services":
        selected = sorted(models, key=path_priority)
        body = "# Models/services\n" + snippet_block(repo_dir, selected)
    elif condition == "readme_plus_code":
        selected = code_candidates
        body = f"# README\n{readme or '[no README found]'}\n\n# Code snippets\n{snippet_block(repo_dir, selected, max_files=22, total=36000)}"
    elif condition == "bm25_retrieved_code":
        selected = bm25_select(repo_dir, paths, retrieval_query, max_files=22)
        body = f"# README-derived retrieval query\n{clip(retrieval_query, 6000)}\n\n# BM25 selected code snippets\n{snippet_block(repo_dir, selected, max_files=22, total=36000)}"
    elif condition == "random_code_same_budget":
        selected = deterministic_random(all_code, repo_dir.name, max_files=22)
        body = "# Deterministic random code snippets\n" + snippet_block(repo_dir, selected, max_files=22, total=36000)
    elif condition == "full_selected_context":
        selected = heuristic_full
        body = (
            f"# README\n{readme or '[no README found]'}\n\n"
            f"# File tree\n{tree}\n\n"
            f"# Selected code and test snippets\n{snippet_block(repo_dir, selected, max_files=26, total=42000)}"
        )
    elif condition == "oracle_upper_bound":
        selected = oracle_paths + [p for p in routes + models + tests if p not in oracle_paths]
        body = (
            "# Oracle upper-bound selected context\n"
            "This condition is selected with checked trace paths and is used only as an upper-bound comparator.\n\n"
            f"# README\n{readme or '[no README found]'}\n\n"
            f"# File tree\n{tree}\n\n"
            f"# Oracle-selected code and test snippets\n{snippet_block(repo_dir, selected, max_files=26, total=42000)}"
        )
    else:
        raise ValueError(condition)
    return clip(body, 52000)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--annotations", default=str(ROOT / "datasets/11_from_source_code_to_user_goals__annotations/use_case_ground_truth_v1.csv"))
    parser.add_argument("--repos-dir", default=str(ROOT / "datasets/11_from_source_code_to_user_goals__candidate_repos"))
    parser.add_argument("--out-dir", default=str(PROJECT / "artifact_packs"))
    parser.add_argument("--tasks", default=str(PROJECT / "data/ablation_tasks.jsonl"))
    parser.add_argument("--oracle", default=str(PROJECT / "data/use_case_oracle.jsonl"))
    args = parser.parse_args()

    with Path(args.annotations).open(encoding="utf-8-sig", newline="") as handle:
        rows = [clean_key(r) for r in csv.DictReader(handle)]
    by_repo = defaultdict(list)
    for row in rows:
        if row.get("review_status") == "checked":
            by_repo[row["repository_folder"]].append(row)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    tasks = []
    oracles = []
    for repo, repo_rows in sorted(by_repo.items()):
        print(f"preparing {repo}", flush=True)
        repo_dir = Path(args.repos_dir) / repo
        if not repo_dir.exists():
            print(f"missing repo: {repo}", file=sys.stderr)
            continue
        project = repo_rows[0]["project"]
        oracles.append({
            "repo": repo,
            "project": project,
            "repository_url": repo_rows[0]["repository_url"],
            "use_cases": oracle_summary(repo_rows),
        })
        for condition in CONDITIONS:
            pack = build_pack(repo_dir, repo_rows, condition)
            pack_path = out_dir / repo / f"{condition}.md"
            pack_path.parent.mkdir(parents=True, exist_ok=True)
            pack_path.write_text(pack, encoding="utf-8")
            tasks.append({
                "repo": repo,
                "project": project,
                "condition": condition,
                "artifact_pack_path": str(pack_path.relative_to(PROJECT)),
                "artifact_chars": len(pack),
                "gold_use_cases": len(repo_rows),
            })

    task_path = Path(args.tasks)
    task_path.parent.mkdir(parents=True, exist_ok=True)
    with task_path.open("w", encoding="utf-8", newline="\n") as handle:
        for task in tasks:
            handle.write(json.dumps(task, ensure_ascii=False) + "\n")

    oracle_path = Path(args.oracle)
    with oracle_path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in oracles:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"wrote {len(tasks)} ablation tasks for {len(oracles)} repositories")
    print(f"wrote tasks to {task_path}")
    print(f"wrote oracle to {oracle_path}")


if __name__ == "__main__":
    main()
