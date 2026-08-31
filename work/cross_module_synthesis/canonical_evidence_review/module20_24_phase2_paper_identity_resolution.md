# Module 20B–24B Phase-2 paper identity resolution

This manifest bridges exact paper identifiers to Phase-2 extraction rows.
It preserves the original canonical_paper_key and does not alter evidence
grades, context levels, claims, observations, or the database schema.
Filename tokens and search-query URLs are not accepted as paper identity.
Accepted NCBI exception-ledger mappings are limited to exact single-identifier keys with one PMID and a matching PubMed record.
The derived resolved_canonical_paper_key is PMID:<id> only after an accepted single-PMID resolution; the original canonical_paper_key is preserved.

- Phase-2 extraction rows audited: 4,722
- Rows with resolved PMID: 3,705
- Rows without resolved PMID: 1,017
- Row-level unresolved exception queue: 1,017
- Deduplicated exception groups: 454
- Local artifacts parsed (only when cited by a row): 387

## Resolution status

| Status | Rows |
|---|---:|
| resolved_authoritative_local_artifact | 206 |
| resolved_authoritative_metadata_ledger | 416 |
| resolved_authoritative_ncbi_exception_ledger | 494 |
| resolved_authoritative_shared_identifier | 20 |
| resolved_authoritative_shared_identifier_ncbi | 4 |
| resolved_authoritative_shared_local_identifier | 10 |
| resolved_authoritative_source_locator | 36 |
| resolved_authoritative_source_locator_ncbi | 11 |
| resolved_authoritative_source_locator_pmid | 69 |
| resolved_authoritative_unkeyed_local_artifact | 22 |
| resolved_canonical_pmid | 2,417 |
| unresolved_ambiguous_multiple_canonical_pmids | 499 |
| unresolved_missing_canonical_identity | 456 |
| unresolved_no_authoritative_resolution | 62 |

## Unresolved policy

Rows without a single authoritative resolved PMID remain in the Phase-2 staging ledger.
Ambiguous multiple-PMID keys and local artifacts are not collapsed by guessing.
The original key and unresolved reason are retained for later adjudication.
The lossless row-level queue is module20_24_phase2_paper_identity_exceptions.tsv; its deduplicated triage index is module20_24_phase2_paper_identity_exceptions_summary.tsv.
