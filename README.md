# usecase-ablate

Reproduction package for the repository artifact ablation study on LLM-based use-case recovery.

The package contains the prompt, fixed task manifests, scoring oracle, artifact packs, scripts, generated outputs, aggregate result tables, qualitative annotation exports, and paper figures needed to reproduce the Journal of Systems and Software submission.

## Contents

- `data/ablation_tasks.jsonl`: fixed 16 repository x 10 condition task manifest with artifact packs.
- `data/ablation_tasks_core6.jsonl`: smaller 16 repository x 6 condition robustness manifest for multi-family model checks.
- `data/use_case_oracle.jsonl`: checked use-case oracle used by the scorer.
- `prompts/artifact_ablation_prompt.md`: JSON-output prompt template.
- `scripts/run_artifact_ablation_ollama.py`: run one Ollama model on the task manifest.
- `scripts/run_artifact_ablation_anthropic.py`: run one Claude model through the Anthropic Messages API.
- `scripts/run_artifact_ablation_api.py`: run one OpenAI-compatible hosted API model, including DeepSeek V4 Pro.
- `scripts/run_ablation_matrix.py`: run one or more models and score their outputs.
- `scripts/score_artifact_ablation.py`: compute actor recall, use-case recall, path fidelity, behavior coverage, unsupported feature rate, parse rate, runtime, and composite score.
- `scripts/qualitative_error_analysis.py`: code generated use cases into a qualitative failure taxonomy.
- `scripts/summarize_ablation_results.py`: aggregate metrics, summarize model-family behavior, and regenerate summary CSVs and figures.
- `scripts/run_threshold_sensitivity.py`: rerun scoring across use-case matching thresholds.
- `scripts/prepare_artifact_packs.py`: optional pack builder for users who have the original candidate repositories and annotation CSV.
- `paper_artifacts/`: experimental data used in the paper, including task manifests, artifact packs, generated model outputs, scored metrics, qualitative annotation logs and exports, agreement tables, and final figures.

## Environment

Install Python dependencies:

```bash
python3 -m pip install -e .
```

Install and start Ollama, then pull the models you want to run. The upgraded journal matrix used three Qwen coder model sizes:

```bash
ollama pull qwen2.5-coder:1.5b
ollama pull qwen2.5-coder:3b
ollama pull qwen2.5-coder:7b
```

## Run the Study

Run the three-model matrix:

```bash
python3 scripts/run_ablation_matrix.py \
  --models \
  qwen2.5-coder:1.5b \
  qwen2.5-coder:3b \
  qwen2.5-coder:7b
```

Run a resumable robustness subset across additional model families:

```bash
python3 scripts/run_ablation_matrix.py \
  --tasks data/ablation_tasks_core6.jsonl \
  --results-dir results_core6 \
  --resume \
  --models \
  qwen2.5:3b \
  llama3.2:3b \
  deepseek-coder:6.7b
```

Run the hosted DeepSeek V4 Pro sanity check on the core-six task manifest:

```bash
export ANTHROPIC_API_KEY=...
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
python3 scripts/run_artifact_ablation_anthropic.py \
  --model deepseek-v4-pro \
  --provider deepseek-anthropic \
  --base-url "$ANTHROPIC_BASE_URL" \
  --tasks data/ablation_tasks_core6.jsonl \
  --out results_api/deepseek_v4_pro_anthropic_outputs.jsonl \
  --resume \
  --max-tokens 8192
python3 scripts/score_artifact_ablation.py \
  results_api/deepseek_v4_pro_anthropic_outputs.jsonl \
  --out results_api/deepseek_v4_pro_anthropic_metrics.csv
python3 scripts/qualitative_error_analysis.py \
  results_api/deepseek_v4_pro_anthropic_outputs.jsonl \
  --out-dir analysis/qualitative_error_analysis
```

Run the hosted Anthropic Claude sanity check on the core-six task manifest:

```bash
export ANTHROPIC_API_KEY=...
python3 scripts/run_artifact_ablation_anthropic.py \
  --model claude-sonnet-4-5 \
  --tasks data/ablation_tasks_core6.jsonl \
  --out results_api/claude_sonnet_4_5_ablation_outputs.jsonl \
  --resume
python3 scripts/score_artifact_ablation.py \
  results_api/claude_sonnet_4_5_ablation_outputs.jsonl \
  --out results_api/claude_sonnet_4_5_ablation_metrics.csv
```

Regenerate aggregate CSVs and figures:

```bash
python3 scripts/summarize_ablation_results.py
python3 scripts/run_threshold_sensitivity.py
```

Generated outputs are written under `results/` and figures under `figures/`. The summary step writes bootstrap confidence intervals and paired deltas. These output directories are intentionally ignored by Git.

## Optional: Rebuild Artifact Packs

If you have the original candidate repositories and annotation CSV, place them next to this repository using the layout below:

```text
JCST_SE_Research_Data/
  annotations/use_case_ground_truth_v1.csv
  candidate_repos/<repo folders>
usecase-ablate/
```

Then rebuild the fixed task files:

```bash
python3 scripts/prepare_artifact_packs.py
```
