# Module 20B–24B paper provenance materialization

Generated SQL is limited to exact local PubMed paper records and
paper-anchored register provenance. It does not create experiment-level
or claim/observation rows.

- Unique PMID anchors in Phase-2: 1,519
- Exact local/metadata Paper records: 1,262
- Paper-anchored register-source links: 2,504
- Identity metadata conflicts retained unresolved: 0

| Module | Paper-anchored source links |
|---|---:|
| 20B | 861 |
| 21B | 73 |
| 22B | 754 |
| 23B | 682 |
| 24B | 134 |

Unresolved PMID anchors, DOI-only/PMCID-only cases without a resolved
Paper row, and all experiment/observation/claim routes remain in staging.
