\set ON_ERROR_STOP on
\i schema/public_tf_union_integration.sql
BEGIN;
TRUNCATE TABLE external_tf_evidence_verification, external_tf_regulon_member, external_tf_regulon, external_tf_reference, external_tf_regulon_record, external_tf_identity_mapping, external_tf_source_registry RESTART IDENTITY CASCADE;
\copy external_tf_source_registry (source_registry, source_version, species_context, retrieval_date, source_url, snapshot_path, snapshot_sha256, resource_class, upstream_version, notes) FROM 'data/processed/public_tf_union_v1/source_registry.tsv' WITH (FORMAT csv, DELIMITER E'\t', HEADER true, NULL '\N')
\copy external_tf_identity_mapping (source_registry, source_version, species_context, identity_role, source_symbol, normalized_symbol, normalized_symbol_key, identity_decision, identity_reason, mscidblit_entity_id, frozen_entity_match_status) FROM 'data/processed/public_tf_union_v1/identity_mapping.tsv' WITH (FORMAT csv, DELIMITER E'\t', HEADER true, NULL '\N')
\copy external_tf_regulon_record (external_record_key, source_registry, source_version, species_context, external_record_id, raw_record_id, raw_record_sha256, raw_payload, source_tf_symbol, source_target_symbol, tf_normalized_symbol, tf_normalized_symbol_key, target_normalized_symbol, target_normalized_symbol_key, raw_relationship_effect, effect_polarity, relationship_class, evidence_basis, confidence_tier, dorothea_level, curation_effort, external_sources, reference_text, reference_pmids, source_locator, verification_status, limitations, export_priority) FROM 'data/processed/public_tf_union_v1/source_records.tsv' WITH (FORMAT csv, DELIMITER E'\t', HEADER true, NULL '\N')
\copy external_tf_reference (external_record_key, reference_namespace, reference_id, reference_locator, reference_status) FROM 'data/processed/public_tf_union_v1/source_references.tsv' WITH (FORMAT csv, DELIMITER E'\t', HEADER true, NULL '\N')
\copy external_tf_regulon (external_regulon_id, source_registry, source_version, species_context, tf_normalized_symbol, tf_normalized_symbol_key, regulon_name, definition_status, membership_semantics, source_record_count, materialized_member_count, export_priority, limitations) FROM 'data/processed/public_tf_union_v1/source_regulons.tsv' WITH (FORMAT csv, DELIMITER E'\t', HEADER true, NULL '\N')
\copy external_tf_regulon_member (external_regulon_id, external_record_key, target_normalized_symbol, target_normalized_symbol_key, membership_basis, regulatory_effect, membership_status, confidence_tier, export_priority) FROM 'data/processed/public_tf_union_v1/source_regulon_members.tsv' WITH (FORMAT csv, DELIMITER E'\t', HEADER true, NULL '\N')
\copy external_tf_evidence_verification (verification_id, external_record_key, priority_tf_symbol, species_context, target_normalized_symbol, verification_scope, reference_pmid, reference_locator, reference_title, verification_status, evidence_class, verified_effect, cell_type_context, compartment_context, stimulus_context, confidence_tier, limitations, notes) FROM 'data/processed/public_tf_union_v1/priority_tf_evidence.tsv' WITH (FORMAT csv, DELIMITER E'\t', HEADER true, NULL '\N')

-- Resolve only unique case-insensitive exact gene_symbol matches in the frozen graph.
WITH candidates AS (
  SELECT m.mapping_id, count(e.entity_id) AS match_count, min(e.entity_id) AS entity_id
  FROM external_tf_identity_mapping m
  LEFT JOIN signalingentity e
    ON m.normalized_symbol_key IS NOT NULL
   AND lower(btrim(coalesce(e.gene_symbol, ''))) = m.normalized_symbol_key
  GROUP BY m.mapping_id
), resolved AS (
  SELECT mapping_id, match_count, entity_id FROM candidates
)
UPDATE external_tf_identity_mapping m
SET mscidblit_entity_id = CASE WHEN r.match_count = 1 THEN r.entity_id ELSE NULL END,
    frozen_entity_match_status = CASE
      WHEN m.normalized_symbol_key IS NULL THEN 'absent_from_frozen_graph'
      WHEN r.match_count = 1 THEN 'mapped_unique'
      WHEN r.match_count > 1 THEN 'ambiguous_frozen_entity'
      ELSE 'absent_from_frozen_graph' END
FROM resolved r WHERE r.mapping_id = m.mapping_id;
COMMIT;

-- The external layer is export-gated and must remain separate from the frozen bundle.
SELECT 'external_tf_union_loaded' AS check_name, count(*) AS record_count FROM external_tf_regulon_record;
SELECT 'external_tf_union_exportable_rows' AS check_name, count(*) AS issue_count FROM external_tf_regulon_record WHERE export_priority <> 'exclude';
