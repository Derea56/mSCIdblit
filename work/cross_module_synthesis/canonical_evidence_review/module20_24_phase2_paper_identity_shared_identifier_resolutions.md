# Phase-2 shared DOI/PMCID identity resolution

Only unresolved rows with shared exact DOI/PMCID identifiers in both canonical_paper_key and source_locator were accepted.
A row was accepted either through one accepted exact NCBI mapping or when all shared identifiers mapped to one titled local paper metadata record; competing papers were rejected.

- Rows with shared authoritative identifier inspected: 256
- New accepted exact row-level mappings: 10
- Total retained exact row-level mappings: 30
- Rejected competing mappings: 246

| Module | Rows |
|---|---:|
| 20B | 20 |
| 22B | 4 |
| 23B | 6 |

The resolver input ledger is module20_24_phase2_paper_identity_shared_identifier_resolutions.tsv.
