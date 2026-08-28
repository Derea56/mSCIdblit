# Public TF union expansion v1

This is a staging/discovery artifact. It expands TF identity and source provenance without promoting any new canonical TF-target evidence.

`tf_candidate_union.tsv` is the review inventory. `tf_identity_records.tsv` records where each TF identity/profile came from. `tf_pair_records.tsv` copies the existing source-specific pair assertions. `reported_contributor_links.tsv.gz` is the lossless compressed form of the large contributor-link table; it preserves contributor labels reported inside OmniPath/DoRothEA records and explicitly marks them as non-independent. Local builds may also materialize the uncompressed `.tsv` form. `tflink_tf_summary.tsv` records TFLink GMT TF-level counts only; it is not pair-level evidence.

The release is intentionally separate from the frozen mechanism graph and must be reviewed before any promotion.
