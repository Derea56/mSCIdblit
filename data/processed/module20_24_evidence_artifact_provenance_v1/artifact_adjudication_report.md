# Module 20B-24B artifact extraction and adjudication

This report is the artifact-to-review bridge. It does not infer new
biological claims and does not independently promote mechanism edges.
Every manifest artifact receives at least one explicit status row.

- Manifest artifacts: 2,753
- Adjudication rows: 6,666
- Artifacts represented: 2,753
- Artifacts without a conservative register crosswalk: 1,539

## Status counts

| Status | Rows |
|---|---:|
| `candidate_requires_review` | 701 |
| `linked_unresolved` | 3,320 |
| `metadata_or_search_only` | 359 |
| `negative_or_boundary_evaluated` | 2 |
| `supporting_validated_claim` | 1,104 |
| `unmapped_source_artifact` | 1,180 |

## Module routing

| Module | Rows |
|---|---:|
| `20B` | 587 |
| `21B` | 100 |
| `22B` | 2,184 |
| `23B` | 1,946 |
| `24B` | 310 |
| `UNMAPPED` | 1,539 |

## Interpretation

- `supporting_validated_claim` is the only status that may feed a later canonical evidence-source update, subject to the existing materialization validators.
- `candidate_requires_review` and `linked_unresolved` are usable review inputs but are not canonical support.
- `negative_or_boundary_evaluated` preserves evaluated non-support and must remain available for screening.
- Metadata/search/manifest artifacts are retained for provenance and search reproducibility, not treated as direct evidence.
- Exact identifiers are limited to filename/source-record metadata; article reference-list mentions are not used as paper identity.
