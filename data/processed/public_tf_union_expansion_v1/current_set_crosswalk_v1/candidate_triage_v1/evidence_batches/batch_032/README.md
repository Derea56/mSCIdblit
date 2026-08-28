# Public TF evidence collection batch_032

This is a completed bounded exact-pair review derived from database-attributed TFLink regulon sets. TFLink membership was retained as a search lead only. Every row was reviewed for the exact regulator, target, species, cell/model, assay, direction, and any upstream relay. Target-cell presence and downstream activation remain separate fields.

Batch032 staged five exact noncanonical functional candidates: human MRTFA-to-COL1A1, MRTFA-to-MYL9, MRTFA-to-MMP9, mouse Mrtfa-to-Id3, and human SRPK2-to-ACSS2. One Mrtfa-to-Tagln binding/cofactor near-match and two MRTFA directionality/interaction near-matches were retained separately. The other 92 rows remain database-membership-only leads. All 100 rows remain `exportable=false` and `canonical_write_performed=false`; no canonical TF, regulon, Module 22B, or other materialization write was made.

Outputs: `public_tf_evidence_review_batch032_pairs.tsv`, `public_tf_evidence_review_batch032_regulator_register.tsv`, `batch_032_evidence_review_summary.json`, `batch_032_validation.json`, and `EVIDENCE_REVIEW_BATCH032.md`.
