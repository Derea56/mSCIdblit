# Public TF union expansion v1

**Date:** 2026-08-26  
**Status:** staging/discovery only; no canonical graph or evidence promotion

## Purpose

The original public TF union used two top-level snapshot lanes: TRRUST and
OmniPath/DoRothEA. This expansion broadens the TF candidate universe without
pretending that a TF catalog, a binding profile, or an integrated gateway row
is equivalent to pair-level primary evidence.

The expansion preserves three provenance levels:

1. **Source snapshot:** the exact retrieved file, URL, retrieval date, SHA-256,
   species scope, source version, and raw record key.
2. **Reported contributor:** an underlying repository label reported inside an
   OmniPath/DoRothEA record. These links are preserved in
   `reported_contributor_links.tsv` but are explicitly marked
   `reported_by_aggregator` and `independent_snapshot=false`.
3. **Candidate identity/profile:** catalog or profile evidence that a symbol
   is a plausible TF. These records do not create TF-target edges.

## Imported and registered lanes

| Lane | Scope | Role | Evidence interpretation |
|---|---|---|---|
| TRRUST | human/mouse | source-specific TF-target snapshot | literature lead; exact pair still requires review |
| OmniPath/DoRothEA | human/mouse | integrated TF-target snapshot | integrated assertion; DoRothEA level and source labels are prioritization signals |
| Lambert HumanTFs v1.01 | human | expert-curated TF identity catalog | TF identity only |
| AnimalTFDB3 fallback snapshot | human/mouse | TF identity catalog | TF identity only; AnimalTFDB4 endpoint was unavailable during acquisition |
| JASPAR CORE 2026 vertebrates | vertebrate profile scope | experimentally derived binding profiles | binding-profile corroboration only; no direction or target claim |
| TFLink v1.0 GMT | human/mouse | integrated gateway TF summaries | TF-level discovery only in this wave; GMT lacks detailed source/assay/PMID fields per target |

## Counts

| Artifact | Count |
|---|---:|
| Source registry rows | 10 |
| Existing source-specific TF-target records retained | 45,795 |
| Reported contributor labels | 52 |
| Reported contributor links | 232,964 |
| TF identity/profile records | 54,511 |
| Lambert human TF identity rows | 1,639 |
| AnimalTFDB3 human identity rows | 1,665 |
| AnimalTFDB3 mouse identity rows | 1,636 |
| JASPAR CORE profile headers | 1,019 |
| TFLink human TF summaries | 1,605 |
| TFLink mouse TF summaries | 1,152 |
| Candidate union rows | 5,435 |
| Human candidate rows | 2,381 |
| Mouse candidate rows | 2,171 |
| Vertebrate-profile candidate rows | 883 |

The expanded candidate inventory adds 1,560 human and 1,258 mouse normalized TF
symbols beyond the current public pair-source inventory, while retaining all
previously observed human and mouse TF symbols. The exact per-source and
per-record accounting is in `tf_candidate_union.tsv` and
`tf_identity_records.tsv`.

## Provenance artifacts

- `source_registry.tsv` — source-level URL, release/version, retrieval date,
  snapshot path, SHA-256, species scope, and independence status.
- `tf_identity_records.tsv` — one row per catalog/profile/gateway identity
  observation with raw symbol, source record ID, locator, and raw hash.
- `tf_pair_records.tsv` — the existing source-specific TF-target records,
  copied with their original external record key and raw hash.
- `reported_contributor_registry.tsv` — the 52 contributor labels reported by
  OmniPath/DoRothEA, with aggregation layer and independent-snapshot status.
- `reported_contributor_links.tsv` — record-level links from each aggregated
  assertion to each reported contributor label.
- `tflink_tf_summary.tsv` — TFLink TF-level target counts; not pair-level
  evidence.
- `tf_candidate_union.tsv` — ranked-free union inventory for routing into
  later module review; every candidate retains source registry/version lists.
- `expansion_manifest.json` — counts, hashes, and policy declarations.
- `expansion_validation.json` — structural and provenance validation result.

## Validation gate

`expansion_validation.json` currently reports `status=pass` with zero issues:

- no duplicate source, identity, pair, contributor, or candidate keys;
- no missing source registry links or source locators;
- no missing contributor-to-record links;
- no aggregated contributor link incorrectly marked independent;
- all 45,795 existing public-union pair records retained with matching raw
  hashes;
- all six newly acquired raw snapshots match their recorded SHA-256 hashes;
- no candidate is marked promoted.

## Next acquisition wave

TFLink should be followed by its detailed TSV interaction export before any
TFLink pair is used for promotion, because the GMT file does not retain the
source database, experimental method, and PMID fields needed for exact
corroboration. RegNetwork and hTFtarget were checked but not imported in this
wave because their endpoints were unavailable from the current environment.
Their registry entries should be added only after a release-pinned snapshot is
successfully acquired and hashed.
