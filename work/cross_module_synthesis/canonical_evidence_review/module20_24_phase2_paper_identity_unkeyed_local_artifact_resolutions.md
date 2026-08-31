# Phase-2 unkeyed local-artifact identity resolution

Only unresolved missing-identity and no-authoritative-resolution rows with cited XML/HTML artifacts were inspected.
A row was accepted only when a cited artifact parsed to exactly one paper record with a PMID and title.
If a non-empty canonical key contained identifiers, the artifact record also had to carry one of those exact identifiers.
Rows were resolved individually; blank or placeholder keys were never grouped.

- Eligible unresolved rows with cited XML/HTML artifacts: 90
- Accepted exact row-level mappings: 22
- Rejected non-unique or unmatched artifact cases: 68
- Unique local artifacts parsed: 51

## Accepted rows by module

| Module | Rows |
|---|---:|
| 20B | 22 |

The resolver input ledger is module20_24_phase2_paper_identity_unkeyed_local_artifact_resolutions.tsv.
