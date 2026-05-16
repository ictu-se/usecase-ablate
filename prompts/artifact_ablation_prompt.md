You are analyzing a software repository to recover user-facing use cases from a restricted artifact pack.

Return only a JSON object with this schema:

{
  "actors": ["actor names"],
  "use_cases": [
    {
      "actor": "primary actor",
      "name": "short verb-noun use case name",
      "description": "one sentence grounded in the provided artifacts",
      "main_flow": ["3-5 concise steps"],
      "evidence_paths": ["files or API paths from the artifact pack"],
      "confidence": "high|medium|low"
    }
  ],
  "unsupported_features_avoided": ["features that might exist but are not supported by this artifact pack"],
  "artifact_limits": "one sentence about what this artifact pack cannot show"
}

Rules:
- Use only evidence present in the artifact pack.
- Prefer concrete user-visible behavior over internal implementation details.
- Do not invent screens, APIs, roles, or workflows that are not supported.
- If the artifact pack is weak, return fewer use cases with lower confidence.
- Keep at most 8 use cases.
- Keep each description and flow step short.

Repository: {repo}
Project: {project}
Condition: {condition}

Artifact pack:

{artifact_pack}
