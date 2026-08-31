# Phase-2 source-locator PMID identity resolution

Only unresolved rows with exactly one explicit PMID or one stable PubMed/PMC/DOI article URL identifier in source_locator were inspected.
Each identifier had to match a titled local paper metadata record. Ambiguous keys additionally required the selected identifier to be explicit in the key.

- New rows with one explicit source-locator PMID or stable article URL inspected: 46
- New accepted exact row-level mappings: 26
- Total retained exact row-level mappings: 69
- Rejected mappings: 20

| Module | Rows |
|---|---:|
| 20B | 48 |
| 22B | 8 |
| 23B | 3 |
| 24B | 10 |

The resolver input ledger is module20_24_phase2_paper_identity_source_locator_resolutions.tsv.
