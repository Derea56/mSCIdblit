# Phase-2 shared DOI/PMCID identity resolution

Only unresolved rows with one shared authoritative DOI or PMCID in both canonical_paper_key and source_locator were accepted.
The shared identifier had to have one accepted exact NCBI mapping; rows with competing shared identifiers were rejected.

- Rows with shared authoritative identifier inspected: 20
- Accepted exact row-level mappings: 20
- Rejected competing mappings: 0

| Module | Rows |
|---|---:|
| 20B | 16 |
| 23B | 4 |

The resolver input ledger is module20_24_phase2_paper_identity_shared_identifier_resolutions.tsv.
