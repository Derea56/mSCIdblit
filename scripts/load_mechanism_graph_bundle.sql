-- Load a validated mechanism graph bundle into the normalized local database.
-- Use scripts/load_mechanism_graph_bundle.py, which substitutes the absolute
-- TSV paths before sending this template to psql. Direct psql invocation is
-- not portable because psql does not interpolate variables inside \copy paths.
-- The template expects variables pointing to absolute TSV paths, for example:
--
-- psql ... \
--   -v nodes_file=/path/mechanism_nodes.tsv \
--   -v roles_file=/path/mechanism_node_roles.tsv \
--   -v edges_file=/path/mechanism_edges.tsv \
--   -v sources_file=/path/mechanism_edge_sources.tsv \
--   -v pathways_file=/path/mechanism_pathways.tsv \
--   -f scripts/load_mechanism_graph_bundle.sql
--
-- The loader is idempotent for the register IDs and does not overwrite
-- existing SignalingEntity or SignalingEntityRole rows.

BEGIN;

CREATE TEMP TABLE stage_nodes (
  node_id TEXT NOT NULL,
  canonical_name TEXT NOT NULL,
  node_type TEXT,
  node_subtype TEXT,
  gene_symbol TEXT,
  organism_scope TEXT,
  compartment TEXT,
  notes TEXT,
  canonical_label TEXT,
  label_variants TEXT,
  modules TEXT,
  pathways TEXT,
  exportable_edge_count INTEGER
);
\copy stage_nodes FROM :nodes_file WITH (FORMAT csv, HEADER true, DELIMITER E'\t')

CREATE TEMP TABLE stage_roles (
  node_id TEXT NOT NULL,
  role TEXT NOT NULL,
  role_source TEXT NOT NULL,
  role_evidence TEXT NOT NULL
);
\copy stage_roles FROM :roles_file WITH (FORMAT csv, HEADER true, DELIMITER E'\t')

CREATE TEMP TABLE stage_pathways (
  module TEXT NOT NULL,
  pathway_name TEXT NOT NULL,
  edge_count INTEGER,
  node_count INTEGER,
  evidence_count INTEGER
);
\copy stage_pathways FROM :pathways_file WITH (FORMAT csv, HEADER true, DELIMITER E'\t')

CREATE TEMP TABLE stage_edges (
  stage_row_id BIGSERIAL,
  edge_id TEXT NOT NULL,
  source_node_id TEXT NOT NULL,
  target_node_id TEXT NOT NULL,
  pathway_label TEXT,
  relation_type TEXT NOT NULL,
  effect_polarity TEXT,
  species_context TEXT,
  cell_type_context TEXT,
  compartment_context TEXT,
  injury_context TEXT,
  evidence_status TEXT,
  context_scope TEXT,
  export_priority TEXT,
  notes TEXT,
  module TEXT NOT NULL,
  source_label TEXT NOT NULL,
  target_label TEXT NOT NULL,
  register_relation_type TEXT NOT NULL,
  pathway_name TEXT NOT NULL,
  evidence_layer TEXT NOT NULL,
  edge_status TEXT NOT NULL,
  confidence_tier TEXT,
  evidence_ids TEXT,
  evidence_count INTEGER,
  source_locator_count INTEGER,
  exportable BOOLEAN,
  consolidation_note TEXT
);
\copy stage_edges(edge_id, source_node_id, target_node_id, pathway_label, relation_type, effect_polarity, species_context, cell_type_context, compartment_context, injury_context, evidence_status, context_scope, export_priority, notes, module, source_label, target_label, register_relation_type, pathway_name, evidence_layer, edge_status, confidence_tier, evidence_ids, evidence_count, source_locator_count, exportable, consolidation_note) FROM :edges_file WITH (FORMAT csv, HEADER true, DELIMITER E'\t')

CREATE TEMP TABLE stage_sources (
  edge_source_id TEXT NOT NULL,
  edge_id TEXT NOT NULL,
  paper_id TEXT,
  observation_id TEXT,
  claim_id TEXT,
  support_kind TEXT,
  species_support TEXT,
  source_scope TEXT,
  confidence_tier TEXT,
  citation_note TEXT,
  notes TEXT,
  module TEXT NOT NULL,
  evidence_id TEXT NOT NULL,
  source_kind TEXT,
  source_locator TEXT,
  source_locator_status TEXT,
  evidence_summary TEXT,
  limitations TEXT,
  evidence_layer TEXT,
  evidence_exportable BOOLEAN,
  consolidation_note TEXT
);
\copy stage_sources FROM :sources_file WITH (FORMAT csv, HEADER true, DELIMITER E'\t')

INSERT INTO SignalingPathway (pathway_name)
SELECT DISTINCT pathway_name
FROM stage_pathways
WHERE btrim(pathway_name) <> ''
ON CONFLICT (pathway_name) DO NOTHING;

INSERT INTO SignalingEntity (
  canonical_name, entity_type, entity_subtype, gene_symbol,
  organism_scope, compartment, notes
)
SELECT DISTINCT ON (canonical_name)
  canonical_name,
  COALESCE(NULLIF(node_type, ''), 'signaling_effector'),
  NULLIF(node_subtype, ''),
  NULLIF(gene_symbol, ''),
  NULLIF(organism_scope, ''),
  NULLIF(compartment, ''),
  NULLIF(notes, '')
FROM stage_nodes
ORDER BY canonical_name, node_id
ON CONFLICT (canonical_name) DO NOTHING;

DO $$
DECLARE
  staged_edge RECORD;
  staged_source RECORD;
  db_edge_id INTEGER;
  db_pathway_id INTEGER;
  db_source_entity_id INTEGER;
  db_target_entity_id INTEGER;
BEGIN
  FOR staged_edge IN SELECT * FROM stage_edges ORDER BY stage_row_id LOOP
    SELECT register.edge_id
    INTO db_edge_id
    FROM SignalingEdgeRegister AS register
    WHERE register.register_edge_id = staged_edge.edge_id;

    IF db_edge_id IS NULL THEN
      SELECT pathway_id
      INTO db_pathway_id
      FROM SignalingPathway
      WHERE pathway_name = staged_edge.pathway_name;

      SELECT entity.entity_id
      INTO db_source_entity_id
      FROM stage_nodes AS node
      JOIN SignalingEntity AS entity ON entity.canonical_name = node.canonical_name
      WHERE node.node_id = staged_edge.source_node_id;

      SELECT entity.entity_id
      INTO db_target_entity_id
      FROM stage_nodes AS node
      JOIN SignalingEntity AS entity ON entity.canonical_name = node.canonical_name
      WHERE node.node_id = staged_edge.target_node_id;

      IF db_source_entity_id IS NULL OR db_target_entity_id IS NULL THEN
        RAISE EXCEPTION 'Bundle edge % references an unmapped node label', staged_edge.edge_id;
      END IF;

      INSERT INTO SignalingEdge (
        source_entity_id, target_entity_id, pathway_id, relation_type,
        effect_polarity, species_context, cell_type_context,
        compartment_context, injury_context, evidence_status,
        context_scope, export_priority, notes
      ) VALUES (
        db_source_entity_id, db_target_entity_id, db_pathway_id,
        staged_edge.relation_type,
        NULLIF(staged_edge.effect_polarity, ''),
        NULLIF(staged_edge.species_context, ''),
        NULLIF(staged_edge.cell_type_context, ''),
        NULLIF(staged_edge.compartment_context, ''),
        NULLIF(staged_edge.injury_context, ''),
        NULLIF(staged_edge.evidence_status, ''),
        NULLIF(staged_edge.context_scope, ''),
        NULLIF(staged_edge.export_priority, ''),
        NULLIF(staged_edge.notes, '')
      ) RETURNING edge_id INTO db_edge_id;

      INSERT INTO SignalingEdgeRegister (
        edge_id, register_edge_id, module, source_label, target_label,
        register_relation_type, graph_relation_type, pathway_name,
        evidence_layer, edge_status, confidence_tier, evidence_ids,
        consolidation_note
      ) VALUES (
        db_edge_id, staged_edge.edge_id, staged_edge.module,
        staged_edge.source_label, staged_edge.target_label,
        staged_edge.register_relation_type, staged_edge.relation_type,
        staged_edge.pathway_name, staged_edge.evidence_layer,
        staged_edge.edge_status, NULLIF(staged_edge.confidence_tier, ''),
        NULLIF(staged_edge.evidence_ids, ''),
        NULLIF(staged_edge.consolidation_note, '')
      );
    END IF;
  END LOOP;

  FOR staged_source IN SELECT * FROM stage_sources ORDER BY edge_source_id LOOP
    SELECT register.edge_id
    INTO db_edge_id
    FROM SignalingEdgeRegister AS register
    WHERE register.register_edge_id = staged_source.edge_id;

    IF db_edge_id IS NULL THEN
      RAISE EXCEPTION 'Bundle source % references an unmapped edge %', staged_source.edge_source_id, staged_source.edge_id;
    END IF;

    INSERT INTO SignalingEdgeRegisterSource (
      edge_id, register_edge_id, register_evidence_id, module,
      support_kind, species_support, source_scope, confidence_tier,
      citation_note, notes, source_kind, source_locator,
      source_locator_status, evidence_summary, limitations,
      evidence_layer, evidence_exportable, consolidation_note
    ) VALUES (
      db_edge_id, staged_source.edge_id, staged_source.evidence_id,
      staged_source.module, NULLIF(staged_source.support_kind, ''),
      NULLIF(staged_source.species_support, ''),
      NULLIF(staged_source.source_scope, ''),
      NULLIF(staged_source.confidence_tier, ''),
      NULLIF(staged_source.citation_note, ''),
      NULLIF(staged_source.notes, ''),
      NULLIF(staged_source.source_kind, ''),
      NULLIF(staged_source.source_locator, ''),
      NULLIF(staged_source.source_locator_status, ''),
      NULLIF(staged_source.evidence_summary, ''),
      NULLIF(staged_source.limitations, ''),
      NULLIF(staged_source.evidence_layer, ''),
      COALESCE(staged_source.evidence_exportable, FALSE),
      NULLIF(staged_source.consolidation_note, '')
    ) ON CONFLICT (edge_id, register_evidence_id) DO NOTHING;
  END LOOP;
END $$;

INSERT INTO SignalingEntityRole (
  entity_id, role, role_status, role_source, role_evidence,
  source_registry, source_version, export_priority
)
SELECT
  entity.entity_id,
  role.role,
  CASE
    WHEN role.role_source = 'curated_role_hint' THEN 'curated'
    ELSE 'derived'
  END,
  role.role_source,
  role.role_evidence,
  'mSCIdblit_module20_24',
  '2026-08-25',
  'low'
FROM stage_roles AS role
JOIN stage_nodes AS node ON node.node_id = role.node_id
JOIN SignalingEntity AS entity ON entity.canonical_name = node.canonical_name
ON CONFLICT (entity_id, role) DO NOTHING;

COMMIT;
