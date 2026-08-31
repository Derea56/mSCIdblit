# Phase-2 authoritative identity-exception resolution

This pass evaluates only unresolved groups with exactly one PMCID or DOI in the canonical key.
NCBI is used as the authoritative source. Only exact, unique, metadata-checked mappings are accepted.
The ledger is an input to the identity resolver; it does not overwrite source extraction keys.

- Candidate identifier groups: 220
- Candidate extraction rows: 20
- Resolved authoritative mappings: 213
- Unresolved mappings: 7

## Result status

| Status | Groups |
|---|---:|
| resolved_authoritative_ncbi | 213 |
| unresolved_ncbi_nonunique_doi_match | 7 |

The resolver input ledger is module20_24_phase2_paper_identity_authoritative_resolutions.tsv.
Rows without a unique, exact NCBI mapping remain unresolved and continue in the exception queue.
