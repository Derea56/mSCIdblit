# Module 20B–24B paper provenance materialization

Generated SQL is limited to exact local PubMed paper records and
paper-anchored register provenance. It does not create experiment-level
or claim/observation rows.

- Unique PMID anchors in Phase-2: 1,722
- Exact local/metadata Paper records: 1,581
- Paper-anchored register-source links: 3,322
- Identity metadata conflicts retained unresolved: 1

| Module | Paper-anchored source links |
|---|---:|
| 20B | 1,022 |
| 21B | 79 |
| 22B | 843 |
| 23B | 1,222 |
| 24B | 156 |

Unresolved PMID anchors, DOI-only/PMCID-only cases without a resolved
Paper row, and all experiment/observation/claim routes remain in staging.
