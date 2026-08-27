# Public TF expansion triage v1

This is a conservative staging triage of the 2,051 normalized symbols absent from the current sets in every scope. It does not write canonical TF roles, Module 22B regulons, or evidence promotions.

`promote_identity_staging` means only that Lambert and AnimalTFDB3 independently support the TF identity. It is not a Module 22B evidence promotion. TFLink membership is a target-search lead because the retained GMT snapshot lacks target-level assays and PMIDs. JASPAR-only profiles and unresolved protein accessions are kept in the provenance inventory but excluded from automatic module promotion or gene-symbol review, respectively.

## Candidate regulon attribution

`public_tf_candidate_regulon_index.tsv` and
`public_tf_candidate_regulon_attribution.tsv` preserve database-attributed
regulon claims after role sorting. They are candidate memberships, not active
signaling routes: target-cell presence, upstream relay activation, direct
binding, and downstream gene activation remain separate evidence fields for
later review.

TFLink rows are retained at aggregated set level with the source record ID,
raw snapshot path, and record hash. The GMT target count is not converted into
pair-level evidence because the snapshot does not retain target-level assays,
effect direction, or PMID provenance. Source-specific pair records are kept
separate when they match a candidate. All rows remain export-excluded and no
canonical TF or Module 22B record is modified.

The bucket-specific TSV files are review queues generated from the full `tf_expansion_triage.tsv` ledger. Human, mouse, and vertebrate-profile evidence must remain separate during later evidence review. See `triage_validation.json` for key/provenance invariants.
