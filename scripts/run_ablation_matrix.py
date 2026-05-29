import argparse
import subprocess
import sys
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]

MODELS = ["qwen2.5-coder:3b"]


def safe_name(model):
    return model.replace(":", "_").replace("/", "_")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", nargs="*", default=MODELS)
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--tasks", default=str(PROJECT / "data/ablation_tasks.jsonl"))
    parser.add_argument("--oracle", default=None)
    parser.add_argument("--results-dir", default=str(PROJECT / "results"))
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    results_dir = Path(args.results_dir)
    results_dir.mkdir(parents=True, exist_ok=True)
    for model in args.models:
        out = results_dir / f"{safe_name(model)}_ablation_outputs.jsonl"
        cmd = [
            sys.executable,
            str(PROJECT / "scripts/run_artifact_ablation_ollama.py"),
            "--model", model,
            "--tasks", args.tasks,
            "--timeout", str(args.timeout),
            "--out", str(out),
        ]
        if args.limit:
            cmd.extend(["--limit", str(args.limit)])
        if args.resume:
            cmd.append("--resume")
        print("running", " ".join(cmd), flush=True)
        subprocess.run(cmd, check=True)

        metrics = results_dir / f"{safe_name(model)}_ablation_metrics.csv"
        cmd = [
            sys.executable,
            str(PROJECT / "scripts/score_artifact_ablation.py"),
            str(out),
            "--out", str(metrics),
        ]
        if args.oracle:
            cmd.extend(["--oracle", args.oracle])
        print("scoring", " ".join(cmd), flush=True)
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
