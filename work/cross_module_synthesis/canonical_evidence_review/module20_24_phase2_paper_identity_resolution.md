# Module 20B–24B Phase-2 paper identity resolution

This manifest bridges exact paper identifiers to Phase-2 extraction rows.
It preserves the original canonical_paper_key and does not alter evidence
grades, context levels, claims, observations, or the database schema.
Filename tokens and search-query URLs are not accepted as paper identity.

- Phase-2 extraction rows audited: 4,722
- Rows with resolved PMID: 3,058
- Rows without resolved PMID: 1,664
- Local artifacts parsed (only when cited by a row): 530

## Resolution status

| Status | Rows |
|---|---:|
| resolved_authoritative_local_artifact | 184 |
| resolved_authoritative_metadata_ledger | 416 |
| resolved_authoritative_source_locator | 41 |
| resolved_canonical_pmid | 2,417 |
| unresolved_ambiguous_multiple_canonical_pmids | 585 |
| unresolved_missing_canonical_identity | 519 |
| unresolved_no_authoritative_resolution | 560 |

## Unresolved policy

Rows without a single authoritative resolved PMID remain in the Phase-2 staging ledger.
Ambiguous multiple-PMID keys and local artifacts are not collapsed by guessing.
The original key and unresolved reason are retained for later adjudication.
