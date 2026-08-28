# Public TF evidence collection batch_033

This is a completed bounded exact-pair review derived from database-attributed TFLink regulon sets. TFLink membership was retained as a search lead only. Every row was reviewed for the exact regulator, target, species, cell/model, assay, direction, and any upstream relay. Target-cell presence and downstream activation remain separate fields.

Batch033 contains 84 literal pairs from 25 source-set ranks because several source sets have fewer than four imported targets. One exact noncanonical candidate was staged: human COP1/RFWD2-to-MMP1, a gastric-cancer perturbation-associated downstream-expression relationship with unresolved direct ubiquitin/substrate mechanism. The other 83 rows remain database-membership-only leads. All 84 rows remain `exportable=false` and `canonical_write_performed=false`; no canonical TF, regulon, Module 22B, or other materialization write was made.

Outputs: `public_tf_evidence_collection_batch_033.tsv`, `public_tf_evidence_review_batch033_pairs.tsv`, `public_tf_evidence_review_batch033_regulator_register.tsv`, `batch_033_evidence_review_summary.json`, `batch_033_validation.json`, and `EVIDENCE_REVIEW_BATCH033.md`.
