import argparse
import http.client
import json
import time
import urllib.error
import urllib.request
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]


def load_jsonl(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def task_key(record):
    return (
        record.get("repo", ""),
        record.get("condition", ""),
        record.get("model", ""),
    )


def call_ollama(model, prompt, timeout):
    started = time.time()
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.1, "top_p": 0.9, "num_predict": 1500},
    }
    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = json.loads(response.read().decode("utf-8", errors="replace"))
    return {
        "returncode": 0,
        "stdout": data.get("response", ""),
        "stderr": "",
        "elapsed_sec": round(time.time() - started, 3),
        "eval_count": data.get("eval_count", ""),
        "prompt_eval_count": data.get("prompt_eval_count", ""),
    }


def render(template, task, pack):
    return (
        template
        .replace("{repo}", task["repo"])
        .replace("{project}", task["project"])
        .replace("{condition}", task["condition"])
        .replace("{artifact_pack}", pack)
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--tasks", default=str(PROJECT / "data/ablation_tasks.jsonl"))
    parser.add_argument("--template", default=str(PROJECT / "prompts/artifact_ablation_prompt.md"))
    parser.add_argument("--out", default=None)
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--resume", action="store_true", help="Skip task/model rows already present in the output JSONL.")
    args = parser.parse_args()

    safe_model = args.model.replace(":", "_").replace("/", "_")
    out_path = Path(args.out) if args.out else PROJECT / "results" / f"{safe_model}_ablation_outputs.jsonl"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    template = Path(args.template).read_text(encoding="utf-8")
    done = set()
    if args.resume and out_path.exists():
        done = {task_key(record) for record in load_jsonl(out_path)}

    count = 0
    mode = "a" if args.resume else "w"
    with out_path.open(mode, encoding="utf-8", newline="\n") as out:
        for task in load_jsonl(args.tasks):
            expected_key = (task["repo"], task["condition"], args.model)
            if expected_key in done:
                print(f"skip: {task['repo']} {task['condition']} already done", flush=True)
                continue
            pack_path = Path(task["artifact_pack_path"])
            if not pack_path.is_absolute():
                pack_path = PROJECT / pack_path
            pack = pack_path.read_text(encoding="utf-8", errors="replace")
            prompt = render(template, task, pack)
            try:
                result = call_ollama(args.model, prompt, args.timeout)
            except TimeoutError:
                result = {"returncode": -1, "stdout": "", "stderr": "timeout", "elapsed_sec": args.timeout, "eval_count": "", "prompt_eval_count": ""}
            except urllib.error.URLError as exc:
                result = {"returncode": -2, "stdout": "", "stderr": str(exc), "elapsed_sec": args.timeout, "eval_count": "", "prompt_eval_count": ""}
            except http.client.RemoteDisconnected as exc:
                result = {"returncode": -3, "stdout": "", "stderr": str(exc), "elapsed_sec": args.timeout, "eval_count": "", "prompt_eval_count": ""}
            record = {**task, "model": args.model, **result}
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()
            count += 1
            print(f"{count}: {task['repo']} {task['condition']} rc={record['returncode']} elapsed={record['elapsed_sec']}", flush=True)
            if args.limit and count >= args.limit:
                break
    print(f"wrote {count} outputs to {out_path}")


if __name__ == "__main__":
    main()
