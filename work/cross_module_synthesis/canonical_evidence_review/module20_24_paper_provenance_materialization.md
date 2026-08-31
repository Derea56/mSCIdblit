# Module 20B–24B paper provenance materialization

Generated SQL is limited to exact local PubMed paper records and
paper-anchored register provenance. It does not create experiment-level
or claim/observation rows.

- Unique PMID anchors in Phase-2: 1,687
- Exact local/metadata Paper records: 1,441
- Paper-anchored register-source links: 3,105
- Identity metadata conflicts retained unresolved: 1

| Module | Paper-anchored source links |
|---|---:|
| 20B | 956 |
| 21B | 77 |
| 22B | 771 |
| 23B | 1,164 |
| 24B | 137 |

Unresolved PMID anchors, DOI-only/PMCID-only cases without a resolved
Paper row, and all experiment/observation/claim routes remain in staging.
