# Paper Artifacts

This directory contains the experimental data used by the Journal of Systems and Software submission on repository artifact selection for LLM-based use-case recovery.

## Layout

- `task_manifests/`: fixed task manifests and checked use-case oracles for the main benchmark and external-domain stress test.
- `artifact_packs/main_domain/`: artifact packs for the 16 main-domain repositories and all artifact conditions.
- `artifact_packs/external_domain/`: artifact packs for the six external-domain repositories.
- `model_results/`: generated model outputs, scored metrics, aggregate summaries, paired deltas, bootstrap confidence intervals, and threshold-sensitivity outputs.
- `qualitative_annotations/rule_guided_initial_analysis/`: initial rule-guided qualitative coding tables used to define and inspect the taxonomy.
- `qualitative_annotations/independent_annotation_jsonl/`: cleaned independent annotation logs from Annotator 1, Annotator 2, and Annotator 3.
- `qualitative_annotations/independent_annotation_exports/`: completion, pairwise agreement, majority-label, and disagreement exports from the independent annotation workflow.
- `figures/`: generated figures from the experiment scripts.

## Notes

The active independent annotation set excludes an earlier pilot annotator. The paper-facing labels map the retained annotation files as follows:

- `annotator_1.jsonl`: retained annotator originally collected as annotator 11.
- `annotator_2.jsonl`: retained annotator originally collected as annotator 12.
- `annotator_3.jsonl`: retained annotator originally collected as annotator 13.

The paper reports pairwise Cohen's kappa from `qualitative_annotations/independent_annotation_exports/annotation_pairwise_agreement_paper_labels.csv` and uses majority labels from `annotation_latest_wide.csv` for the qualitative taxonomy.

The full source repositories are not vendored here. The artifact packs are the bounded evidence packs actually provided to the models, and the task manifests preserve the repository and condition identifiers needed to reproduce the reported runs.
