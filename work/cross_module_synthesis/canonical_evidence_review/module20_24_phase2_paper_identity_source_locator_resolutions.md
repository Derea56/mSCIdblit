# Phase-2 source-locator PMID identity resolution

Only unresolved rows with exactly one explicit PMID in source_locator were inspected.
Each PMID had to match a titled local paper metadata record. Ambiguous keys additionally required the locator PMID to be explicit in the key.

- Rows with one explicit source-locator PMID inspected: 44
- Accepted exact row-level mappings: 43
- Rejected mappings: 1

| Module | Rows |
|---|---:|
| 20B | 43 |

The resolver input ledger is module20_24_phase2_paper_identity_source_locator_resolutions.tsv.
