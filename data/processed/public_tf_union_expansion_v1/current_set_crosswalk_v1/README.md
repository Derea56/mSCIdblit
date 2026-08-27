# Current TF-set crosswalk

This staging crosswalk matches the expanded TF candidate inventory against the current public TF pair union, canonical TF roles, canonical TF-edge participation, and Module 22B regulons.

`tf_candidate_crosswalk.tsv` has one row per species scope plus normalized TF symbol, so its row counts are not counts of distinct TFs. `tf_cross_species_collapsed.tsv` is an inventory-only collapse by normalized symbol; human and mouse evidence must remain separate. The original source-specific pair records and contributor links remain in the parent expansion directory and are not deleted or collapsed.

The manifest reports both `new_candidate_rows` and `new_candidate_unique_tf_keys`. The former counts species/source-scope rows; the latter is the deduplicated symbol count. Neither is a promotion or evidence-confidence count.

The cross-species manifest fields further distinguish symbols that are new in at least one scope from symbols absent from the current sets in every scope. Use `cross_species_new_candidate_unique_tf_keys` for the inventory-level expansion queue.

Canonical matching uses `gene_symbol` and falls back to `canonical_name` when the current entity lacks a gene symbol. Exact-species flags and any-species flags are reported separately. No canonical database rows were written by this crosswalk.
