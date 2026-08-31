# Module 20B–24B Phase-2 canonical evidence materialization

This generated SQL is conservative and idempotent. It materializes
only stable-PMID rows with validated non-abstract observations and
validated claim text. Experiments are labeled source-defined evidence
units when the original experiment number was not preserved. Explicit
non-promotable claims are retained as boundary evidence and cannot
support promotion of the requested exact edge.

- Candidate extraction rows: 1,463
- Unique PMID papers used: 844
- Explicit boundary-only extraction rows: 5

| Module | Source-defined evidence units |
|---|---:|
| 20B | 668 |
| 21B | 61 |
| 22B | 506 |
| 23B | 147 |
| 24B | 81 |

Rows with abstract-only, unresolved, metadata-only, missing PMID, or
action-token claim text remain in the staging ledger. Boundary-only
rows are retained as explicit negative/context evidence (E/L0) and
are not treated as support for the requested exact edge. The generated
SQL does not invent original experiment numbers, mechanisms, or
unsupported paper metadata. On rerun, stale promotable links and edge
sources from this batch are pruned; immutable historical extraction
records are retained for audit when the database rejects their deletion.
