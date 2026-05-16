# usecase-ablate

Reproduction package for the repository artifact ablation study on LLM-based use-case recovery.

The package contains the prompt, fixed 112-task manifest, scoring oracle, and scripts needed to rerun the local model matrix and regenerate aggregate tables and figures. It does not include manuscript files, generated model outputs, aggregate result CSVs, or paper figures.

## Contents

- `data/ablation_tasks.jsonl`: fixed 16 repository x 7 condition task manifest with artifact packs.
- `data/use_case_oracle.jsonl`: checked use-case oracle used by the scorer.
- `prompts/artifact_ablation_prompt.md`: JSON-output prompt template.
- `scripts/run_artifact_ablation_ollama.py`: run one Ollama model on the task manifest.
- `scripts/run_ablation_matrix.py`: run one or more models and score their outputs.
- `scripts/score_artifact_ablation.py`: compute actor recall, use-case recall, path fidelity, behavior coverage, unsupported feature rate, parse rate, runtime, and composite score.
- `scripts/summarize_ablation_results.py`: aggregate metrics, summarize model-family behavior, and regenerate summary CSVs and figures.
- `scripts/prepare_artifact_packs.py`: optional pack builder for users who have the original candidate repositories and annotation CSV.

## Environment

Install Python dependencies:

```bash
python3 -m pip install -e .
```

Install and start Ollama, then pull the models you want to run. The paper matrix used ten local models:

```bash
ollama pull qwen2.5-coder:1.5b
ollama pull qwen2.5-coder:3b
ollama pull qwen2.5-coder:7b
ollama pull qwen2.5-coder:14b
ollama pull qwen2.5:3b
ollama pull qwen2.5vl:3b
ollama pull llama3.2:3b
ollama pull llama3.2-vision:11b
ollama pull gemma3:4b
ollama pull granite3.2-vision:latest
```

## Run the Study

Run the ten-model matrix:

```bash
python3 scripts/run_ablation_matrix.py \
  --models \
  qwen2.5-coder:1.5b \
  qwen2.5-coder:3b \
  qwen2.5-coder:7b \
  qwen2.5-coder:14b \
  qwen2.5:3b \
  qwen2.5vl:3b \
  llama3.2:3b \
  llama3.2-vision:11b \
  gemma3:4b \
  granite3.2-vision:latest
```

Regenerate aggregate CSVs and figures:

```bash
python3 scripts/summarize_ablation_results.py
```

Generated outputs are written under `results/` and figures under `figures/`. The summary step also writes `ablation_summary_by_family.csv` for model-family comparison. These output directories are intentionally ignored by Git.

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
