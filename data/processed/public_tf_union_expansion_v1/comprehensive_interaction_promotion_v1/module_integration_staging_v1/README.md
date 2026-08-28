# Public TF module integration staging

This directory is an additive, review-only module staging layer generated from the comprehensive public-TF review queue and promotion overlay. It does not write canonical TF, Module 22B, SignalingEdge, Regulon, or other database rows.

All reviewed A-E rows are retained. Rows are split one-per-explicit-module assignment; multi-module assignments remain separate, and rows without an explicit module route remain in `catalog_only_evidence.tsv`. The original textual evidence tier is kept unchanged. A/B/C retain ranking aids of 3/2/1; D/E are screening-only with rank 0, `source_exportable=false`, and `module_materialization_allowed=false`. U rows are excluded. Source registry, record, review, species, effect, citation, mechanism, limitation, and raw snapshot fields are copied when present; queue-level provenance is retained for reviewed D/E rows.

See `module_integration_staging_manifest.json` for counts and the explicit no-materialization policy.
