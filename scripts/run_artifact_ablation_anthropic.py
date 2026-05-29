import argparse
import json
import os
import time
import urllib.error
import urllib.request
import http.client
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
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


def load_done(path):
    return {(r.get("repo", ""), r.get("condition", ""), r.get("model", "")) for r in load_jsonl(path)}


def extract_text(content_blocks):
    parts = []
    for block in content_blocks or []:
        if isinstance(block, dict) and block.get("type") == "text":
            parts.append(block.get("text", ""))
    return "\n".join(part for part in parts if part)


def call_anthropic(base_url, api_key, model, prompt, timeout, max_tokens, version):
    started = time.time()
    endpoint = base_url.rstrip("/")
    if not endpoint.endswith("/v1/messages"):
        endpoint = endpoint + "/v1/messages"
    payload = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-api-key": api_key,
            "anthropic-version": version,
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = json.loads(response.read().decode("utf-8", errors="replace"))
    usage = data.get("usage") or {}
    return {
        "returncode": 0,
        "stdout": extract_text(data.get("content")),
        "stderr": "",
        "elapsed_sec": round(time.time() - started, 3),
        "eval_count": usage.get("output_tokens", ""),
        "prompt_eval_count": usage.get("input_tokens", ""),
        "stop_reason": data.get("stop_reason", ""),
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
    parser.add_argument("--model", default="claude-sonnet-4-5")
    parser.add_argument("--provider", default="anthropic")
    parser.add_argument("--base-url", default=os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com"))
    parser.add_argument("--api-key-env", default="ANTHROPIC_API_KEY")
    parser.add_argument("--anthropic-version", default="2023-06-01")
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

    out_path = Path(args.out) if args.out else PROJECT / "results_api" / f"{safe_name(args.model)}_ablation_outputs.jsonl"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    template = Path(args.template).read_text(encoding="utf-8")
    done = load_done(out_path) if args.resume and out_path.exists() else set()

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
                result = call_anthropic(args.base_url, api_key, args.model, prompt, args.timeout, args.max_tokens, args.anthropic_version)
            except TimeoutError:
                result = {"returncode": -1, "stdout": "", "stderr": "timeout", "elapsed_sec": args.timeout, "eval_count": "", "prompt_eval_count": "", "stop_reason": ""}
            except urllib.error.HTTPError as exc:
                body = exc.read().decode("utf-8", errors="replace")[:1000]
                result = {"returncode": -2, "stdout": "", "stderr": f"HTTP {exc.code}: {body}", "elapsed_sec": args.timeout, "eval_count": "", "prompt_eval_count": "", "stop_reason": ""}
            except urllib.error.URLError as exc:
                result = {"returncode": -3, "stdout": "", "stderr": str(exc), "elapsed_sec": args.timeout, "eval_count": "", "prompt_eval_count": "", "stop_reason": ""}
            except (ConnectionResetError, http.client.HTTPException, OSError) as exc:
                result = {"returncode": -4, "stdout": "", "stderr": str(exc), "elapsed_sec": args.timeout, "eval_count": "", "prompt_eval_count": "", "stop_reason": ""}
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
