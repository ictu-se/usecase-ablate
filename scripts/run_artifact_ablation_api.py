import argparse
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[0]
CENTRAL_DATA = PROJECT / "data"


def load_jsonl(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def load_env(path):
    path = Path(path).expanduser()
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def task_key(record):
    return (
        record.get("repo", ""),
        record.get("condition", ""),
        record.get("model", ""),
    )


def call_chat_completion(base_url, api_key, model, prompt, timeout, max_tokens):
    started = time.time()
    endpoint = base_url.rstrip("/")
    if not endpoint.endswith("/chat/completions"):
        endpoint = endpoint + "/chat/completions"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "top_p": 0.9,
        "max_tokens": max_tokens,
        "stream": False,
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = json.loads(response.read().decode("utf-8", errors="replace"))
    choice = (data.get("choices") or [{}])[0]
    message = choice.get("message") or {}
    content = message.get("content") or message.get("reasoning_content") or ""
    usage = data.get("usage") or {}
    return {
        "returncode": 0,
        "stdout": content,
        "stderr": "",
        "elapsed_sec": round(time.time() - started, 3),
        "eval_count": usage.get("completion_tokens", ""),
        "prompt_eval_count": usage.get("prompt_tokens", ""),
    }


def render(template, task, pack):
    return (
        template
        .replace("{repo}", task["repo"])
        .replace("{project}", task["project"])
        .replace("{condition}", task["condition"])
        .replace("{artifact_pack}", pack)
    )


def safe_name(model):
    return model.replace(":", "_").replace("/", "_")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="deepseek-v4-pro")
    parser.add_argument("--provider", default="deepseek")
    parser.add_argument("--base-url", default=os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--api-key-env", default="DEEPSEEK_API_KEY")
    parser.add_argument("--env-file", default=None)
    parser.add_argument("--tasks", default=str(CENTRAL_DATA / "ablation_tasks_core6.jsonl"))
    parser.add_argument("--template", default=str(PROJECT / "prompts/artifact_ablation_prompt.md"))
    parser.add_argument("--out", default=None)
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--max-tokens", type=int, default=1500)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    if args.env_file:
        load_env(args.env_file)
    api_key = os.environ.get(args.api_key_env)
    if not api_key:
        raise SystemExit(f"Missing API key. Set {args.api_key_env} or pass --env-file.")

    safe_model = safe_name(args.model)
    out_path = Path(args.out) if args.out else PROJECT / "results_api" / f"{safe_model}_ablation_outputs.jsonl"
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
                result = call_chat_completion(args.base_url, api_key, args.model, prompt, args.timeout, args.max_tokens)
            except TimeoutError:
                result = {"returncode": -1, "stdout": "", "stderr": "timeout", "elapsed_sec": args.timeout, "eval_count": "", "prompt_eval_count": ""}
            except urllib.error.HTTPError as exc:
                body = exc.read().decode("utf-8", errors="replace")[:1000]
                result = {"returncode": -2, "stdout": "", "stderr": f"HTTP {exc.code}: {body}", "elapsed_sec": args.timeout, "eval_count": "", "prompt_eval_count": ""}
            except urllib.error.URLError as exc:
                result = {"returncode": -3, "stdout": "", "stderr": str(exc), "elapsed_sec": args.timeout, "eval_count": "", "prompt_eval_count": ""}
            record = {**task, "model": args.model, "provider": args.provider, **result}
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()
            count += 1
            print(f"{count}: {task['repo']} {task['condition']} rc={record['returncode']} elapsed={record['elapsed_sec']}", flush=True)
            if args.limit and count >= args.limit:
                break
    print(f"wrote {count} outputs to {out_path}")


if __name__ == "__main__":
    main()
