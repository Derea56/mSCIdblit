#!/usr/bin/env python3
"""Materialize evidence-backed Module 22B TF-target promotions.

This is the write step for the normalized 22B promotion stage.  It adds or
reuses canonical TF/target entities, assigns explicit roles, creates
  evidence-backed target-gene edges, and records the same memberships in the
  Regulon layer. It consumes only rows present in the current register-backed
  stage, preserves database-curated provenance, and never infers ligand-to-TF
  activation.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STAGE = ROOT / "work/module22b_consolidation/materialization_round_register_2026_09_03"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--database-url",
        default=os.environ.get("MSCIDBLIT_DATABASE_URL") or os.environ.get("DATABASE_URL"),
        help="PostgreSQL connection URL accepted by psql -d.",
    )
    parser.add_argument("--stage-root", type=Path, default=DEFAULT_STAGE)
    parser.add_argument("--psql", default="psql")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate the stage manifest and generate SQL without connecting to PostgreSQL.",
    )
    return parser.parse_args()


def sql_literal(path: Path) -> str:
    return "'" + str(path.resolve()).replace("'", "''") + "'"


def build_sql(stage_root: Path, expected_rows: int, materialization_version: str) -> str:
    stage_path = sql_literal(stage_root / "module22b_promoted_pairs.tsv")
    pathway_name = f"Module22B-register-TF-target-evidence-{materialization_version}"
    source_registry = "module22b_register_materialization"
    source_version = materialization_version
    return f"""\
BEGIN;

CREATE TEMP TABLE stage_22b_promotions (
  materialization_id TEXT,
  module TEXT,
  species TEXT,
  tf_symbol TEXT,
  target_symbol TEXT,
  relation_type TEXT,
  effect_polarity TEXT,
  canonical_confidence_tier TEXT,
  membership_basis TEXT,
  membership_status TEXT,
  export_priority TEXT,
  evidence_status TEXT,
  support_kind TEXT,
  primary_pmids TEXT,
  corroborating_pmids TEXT,
  external_record_keys TEXT,
  source_registries TEXT,
  tf_entity_ids TEXT,
  target_entity_ids TEXT,
  tf_frozen_match_status TEXT,
  target_frozen_match_status TEXT,
  tf_role_present TEXT,
  target_role_present TEXT,
  cell_type_context TEXT,
  stimulus_context TEXT,
  limitations TEXT,
  notes TEXT,
  source_artifacts TEXT
);
\\copy stage_22b_promotions FROM {stage_path} WITH (FORMAT csv, HEADER true, DELIMITER E'\\t', QUOTE '"', ESCAPE '"', NULL '')

DO $$
DECLARE
  n INTEGER;
  bad INTEGER;
BEGIN
  SELECT count(*) INTO n FROM stage_22b_promotions;
  IF n <> {expected_rows} THEN
    RAISE EXCEPTION 'Expected {expected_rows} normalized Module 22B promotions, found %', n;
  END IF;
  SELECT count(*) INTO bad
  FROM stage_22b_promotions
  WHERE module <> '22B'
     OR relation_type <> 'regulates_target_gene'
     OR canonical_confidence_tier <> 'medium'
     OR membership_status <> 'supported'
     OR export_priority <> 'medium'
     OR btrim(species) NOT IN ('human', 'mouse')
     OR btrim(tf_symbol) = ''
     OR btrim(target_symbol) = ''
     OR (btrim(primary_pmids) = '' AND btrim(external_record_keys) = '')
     OR lower(btrim(tf_symbol)) = lower(btrim(target_symbol));
  IF bad <> 0 THEN
    RAISE EXCEPTION 'Invalid normalized 22B promotion rows: %', bad;
  END IF;
END $$;

CREATE TEMP TABLE stage_22b_endpoints (
  species TEXT NOT NULL,
  endpoint_role TEXT NOT NULL,
  symbol TEXT NOT NULL,
  PRIMARY KEY (species, endpoint_role, symbol)
) ON COMMIT DROP;

INSERT INTO stage_22b_endpoints (species, endpoint_role, symbol)
SELECT DISTINCT species, 'transcription_factor', tf_symbol
FROM stage_22b_promotions
UNION
SELECT DISTINCT species, 'target_gene', target_symbol
FROM stage_22b_promotions;

CREATE TEMP TABLE stage_22b_entity_map (
  species TEXT NOT NULL,
  endpoint_role TEXT NOT NULL,
  symbol TEXT NOT NULL,
  entity_id INTEGER NOT NULL,
  PRIMARY KEY (species, endpoint_role, symbol)
) ON COMMIT DROP;

DO $$
DECLARE
  endpoint RECORD;
  resolved_id INTEGER;
  entity_type_value TEXT;
  compartment_value TEXT;
BEGIN
  FOR endpoint IN SELECT * FROM stage_22b_endpoints ORDER BY species, endpoint_role, symbol LOOP
    resolved_id := NULL;

    -- Prefer an exact canonical name, then a symbol whose organism scope is
    -- compatible or unspecified.  Existing entity type is not overwritten;
    -- the explicit role table below carries the TF/target distinction.
    SELECT entity.entity_id INTO resolved_id
    FROM SignalingEntity AS entity
    WHERE entity.canonical_name = endpoint.symbol
       OR (
         lower(coalesce(entity.gene_symbol, '')) = lower(endpoint.symbol)
         AND (
           coalesce(entity.organism_scope, '') = ''
           OR lower(entity.organism_scope) LIKE '%' || endpoint.species || '%'
         )
       )
    ORDER BY CASE WHEN entity.canonical_name = endpoint.symbol THEN 0 ELSE 1 END,
             entity.entity_id
    LIMIT 1;

    IF resolved_id IS NULL THEN
      entity_type_value := CASE
        WHEN endpoint.endpoint_role = 'transcription_factor' THEN 'transcription_factor'
        ELSE 'target_gene'
      END;
      compartment_value := CASE
        WHEN endpoint.endpoint_role = 'transcription_factor' THEN 'nucleus'
        ELSE NULL
      END;
      INSERT INTO SignalingEntity (
        canonical_name, entity_type, gene_symbol, organism_scope,
        compartment, notes
      ) VALUES (
        endpoint.symbol, entity_type_value, endpoint.symbol, endpoint.species,
        compartment_value,
        'Added for evidence-backed Module 22B public TF-target materialization; '
          || 'identity is separate from TF activation state.'
      )
      RETURNING entity_id INTO resolved_id;
    END IF;

    INSERT INTO stage_22b_entity_map (species, endpoint_role, symbol, entity_id)
    VALUES (endpoint.species, endpoint.endpoint_role, endpoint.symbol, resolved_id);
  END LOOP;
END $$;

-- The role rows are promoted from the pair-level literature review, while the
-- entity's legacy type and any pre-existing role evidence are preserved.
INSERT INTO SignalingEntityRole (
  entity_id, role, role_status, role_source, role_evidence,
  source_registry, source_version, export_priority
)
SELECT DISTINCT
  map.entity_id,
  map.endpoint_role,
  'curated',
  '{source_registry}',
  'Exact Module 22B TF-target pair identity; primary PMIDs: '
    || string_agg(DISTINCT stage.primary_pmids, '; ' ORDER BY stage.primary_pmids)
    || '. Role assignment does not assert upstream ligand activation.',
  '{source_registry}',
  '{source_version}',
  'medium'
FROM stage_22b_entity_map AS map
JOIN stage_22b_promotions AS stage
  ON (
    map.endpoint_role = 'transcription_factor'
    AND map.species = stage.species
    AND map.symbol = stage.tf_symbol
  ) OR (
    map.endpoint_role = 'target_gene'
    AND map.species = stage.species
    AND map.symbol = stage.target_symbol
  )
GROUP BY map.entity_id, map.endpoint_role
ON CONFLICT (entity_id, role) DO UPDATE SET
  role_status = CASE
    WHEN SignalingEntityRole.role_status = 'curated' THEN SignalingEntityRole.role_status
    ELSE 'curated'
  END,
  role_source = CASE
    WHEN SignalingEntityRole.export_priority = 'exclude' THEN EXCLUDED.role_source
    ELSE SignalingEntityRole.role_source
  END,
  role_evidence = CASE
    WHEN position('{source_registry}' in SignalingEntityRole.role_source) > 0
      THEN SignalingEntityRole.role_evidence
    ELSE SignalingEntityRole.role_evidence || ' Additional evidence-backed Module 22B register materialization recorded {source_version}.'
  END,
  source_registry = CASE
    WHEN SignalingEntityRole.export_priority = 'exclude' THEN EXCLUDED.source_registry
    ELSE SignalingEntityRole.source_registry
  END,
  source_version = CASE
    WHEN SignalingEntityRole.export_priority = 'exclude' THEN EXCLUDED.source_version
    ELSE SignalingEntityRole.source_version
  END,
  export_priority = CASE
    WHEN SignalingEntityRole.export_priority = 'high' THEN 'high'
    ELSE 'medium'
  END,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO SignalingPathway (
  pathway_name, pathway_class, description, source_registry, notes
)
VALUES (
  '{pathway_name}',
  'transcriptional_regulon',
  'Evidence-backed public TF-target memberships reviewed for Module 22B.',
  '{source_registry}',
  'This pathway groups reviewed TF-target edges for queryability; it does not '
    || 'infer upstream ligand-to-TF activation or claim an exhaustive regulon.'
)
ON CONFLICT (pathway_name) DO UPDATE SET
  description = EXCLUDED.description,
  notes = EXCLUDED.notes,
  updated_at = CURRENT_TIMESTAMP;

CREATE TEMP TABLE stage_22b_edge_map (
  materialization_id TEXT PRIMARY KEY,
  edge_id INTEGER NOT NULL,
  register_edge_id TEXT NOT NULL
) ON COMMIT DROP;

DO $$
DECLARE
  stage RECORD;
  source_id INTEGER;
  target_id INTEGER;
  pathway_id_value INTEGER;
  edge_id_value INTEGER;
  register_id_value TEXT;
  existing_register_id TEXT;
  evidence_id_list TEXT;
BEGIN
  SELECT pathway_id INTO pathway_id_value
  FROM SignalingPathway
  WHERE pathway_name = '{pathway_name}';

  FOR stage IN SELECT * FROM stage_22b_promotions ORDER BY materialization_id LOOP
    SELECT entity_id INTO source_id
    FROM stage_22b_entity_map
    WHERE species = stage.species
      AND endpoint_role = 'transcription_factor'
      AND symbol = stage.tf_symbol;
    SELECT entity_id INTO target_id
    FROM stage_22b_entity_map
    WHERE species = stage.species
      AND endpoint_role = 'target_gene'
      AND symbol = stage.target_symbol;

    IF source_id IS NULL OR target_id IS NULL THEN
      RAISE EXCEPTION 'Missing canonical endpoint for %', stage.materialization_id;
    END IF;

    SELECT register.edge_id, register.register_edge_id
      INTO edge_id_value, existing_register_id
    FROM SignalingEdgeRegister AS register
    WHERE register.register_edge_id = stage.materialization_id
    LIMIT 1;

    IF edge_id_value IS NULL THEN
      -- Reuse an existing exact canonical target-gene edge when one exists;
      -- otherwise create one.  The register table remains the provenance
      -- authority and prevents duplicate materialization on reruns.
      SELECT edge.edge_id, register.register_edge_id
        INTO edge_id_value, existing_register_id
      FROM SignalingEdge AS edge
      LEFT JOIN SignalingEdgeRegister AS register ON register.edge_id = edge.edge_id
      WHERE edge.source_entity_id = source_id
        AND edge.target_entity_id = target_id
        AND edge.relation_type = 'regulates_target_gene'
        AND (edge.species_context = stage.species OR edge.species_context IS NULL)
      ORDER BY CASE WHEN edge.pathway_id = pathway_id_value THEN 0 ELSE 1 END,
               edge.edge_id
      LIMIT 1;
    END IF;

    IF edge_id_value IS NULL THEN
      INSERT INTO SignalingEdge (
        source_entity_id, target_entity_id, pathway_id, relation_type,
        effect_polarity, directionality, cell_type_context,
        compartment_context, species_context, evidence_status,
        context_scope, export_priority, notes
      ) VALUES (
        source_id, target_id, pathway_id_value, 'regulates_target_gene',
        CASE stage.effect_polarity
          WHEN 'activating_target' THEN 'activating'
          WHEN 'repressing_target' THEN 'inhibitory'
          WHEN 'context_dependent' THEN 'context_dependent'
          ELSE 'unknown'
        END,
        'directed',
        NULLIF(stage.cell_type_context, ''),
        'nucleus',
        stage.species,
        'evidence_backed_module22b_register_materialization',
        'Module 22B TF-target membership; abstract/context limitations retained; '
          || 'no upstream ligand activation inferred.',
        'medium',
        'Materialization ' || stage.materialization_id || '; PMIDs: '
          || stage.primary_pmids || CASE WHEN stage.corroborating_pmids <> ''
             THEN '; corroborating: ' || stage.corroborating_pmids ELSE '' END
      ) RETURNING edge_id INTO edge_id_value;
    END IF;

    register_id_value := coalesce(existing_register_id, stage.materialization_id);
    SELECT string_agg(evidence_id, ';' ORDER BY evidence_id) INTO evidence_id_list
    FROM (
      SELECT register_id_value || '-P-' || btrim(pmid) AS evidence_id
      FROM regexp_split_to_table(stage.primary_pmids, ';') AS pmid
      WHERE btrim(pmid) <> ''
      UNION
      SELECT register_id_value || '-C-' || btrim(pmid) AS evidence_id
      FROM regexp_split_to_table(stage.corroborating_pmids, ';') AS pmid
      WHERE btrim(pmid) <> ''
      UNION
      SELECT register_id_value || '-X-' || btrim(record_key) AS evidence_id
      FROM regexp_split_to_table(stage.external_record_keys, ';') AS record_key
      WHERE btrim(record_key) <> ''
    ) AS evidence_ids;

    IF existing_register_id IS NULL THEN
      INSERT INTO SignalingEdgeRegister (
        edge_id, register_edge_id, module, source_label, target_label,
        register_relation_type, graph_relation_type, pathway_name,
        evidence_layer, edge_status, confidence_tier, evidence_ids,
        consolidation_note
      ) VALUES (
        edge_id_value, register_id_value, '22B', stage.tf_symbol, stage.target_symbol,
        'regulates_target_gene', 'regulates_target_gene',
        '{pathway_name}',
        'target_gene', 'supported', 'medium', evidence_id_list,
        'Evidence-backed exact-pair public TF review; canonical confidence is medium '
          || 'because abstract/context limitations remain explicit.'
      ) ON CONFLICT (register_edge_id) DO UPDATE SET
        evidence_ids = EXCLUDED.evidence_ids,
        confidence_tier = CASE
          WHEN SignalingEdgeRegister.confidence_tier = 'high' THEN 'high'
          ELSE 'medium'
        END,
        consolidation_note = EXCLUDED.consolidation_note;
    ELSE
      UPDATE SignalingEdgeRegister AS register
      SET evidence_ids = (
            SELECT string_agg(token, ';' ORDER BY token)
            FROM (
              SELECT DISTINCT btrim(token) AS token
              FROM regexp_split_to_table(
                coalesce(register.evidence_ids, '') || ';' || evidence_id_list, ';'
              ) AS token
              WHERE btrim(token) <> ''
            ) AS tokens
          ),
          consolidation_note = concat_ws(' ', register.consolidation_note,
            'Additional reviewed Module 22B register evidence materialized {source_version}.')
      WHERE register.register_edge_id = register_id_value;
    END IF;

    INSERT INTO stage_22b_edge_map (materialization_id, edge_id, register_edge_id)
    VALUES (stage.materialization_id, edge_id_value, register_id_value)
    ON CONFLICT (materialization_id) DO UPDATE SET
      edge_id = EXCLUDED.edge_id,
      register_edge_id = EXCLUDED.register_edge_id;
  END LOOP;
END $$;

-- Make the reviewed pathway queryable.  SignalingPathwayMember has a legacy
-- unique(pathway_id, entity_id) constraint, so a dual-use entity is represented
-- there by its TF role while the many-to-many SignalingEntityRole table retains
-- both transcription_factor and target_gene roles.
INSERT INTO SignalingPathwayMember (pathway_id, entity_id, member_role, membership_status, notes)
SELECT DISTINCT
  pathway.pathway_id, map.entity_id, map.endpoint_role,
  'supported', 'Reviewed Module 22B endpoint; membership does not imply TF activation.'
FROM stage_22b_entity_map AS map
JOIN SignalingPathway AS pathway
  ON pathway.pathway_name = '{pathway_name}'
WHERE map.endpoint_role = 'transcription_factor'
ON CONFLICT (pathway_id, entity_id) DO UPDATE SET
  member_role = 'transcription_factor',
  membership_status = 'supported',
  notes = EXCLUDED.notes;

INSERT INTO SignalingPathwayMember (pathway_id, entity_id, member_role, membership_status, notes)
SELECT DISTINCT
  pathway.pathway_id, map.entity_id, map.endpoint_role,
  'supported', 'Reviewed Module 22B target endpoint; membership does not imply TF activation.'
FROM stage_22b_entity_map AS map
JOIN SignalingPathway AS pathway
  ON pathway.pathway_name = '{pathway_name}'
WHERE map.endpoint_role = 'target_gene'
ON CONFLICT DO NOTHING;

INSERT INTO Regulon (
  tf_entity_id, regulon_name, species_context, cell_type_context,
  compartment_context, source_registry, source_version,
  definition_status, membership_semantics, notes
)
SELECT DISTINCT
  map.entity_id,
  left(stage.tf_symbol || ' evidence-backed Module 22B target set', 255),
  stage.species,
  'unspecified',
  'nucleus',
  '{source_registry}',
  '{source_version}',
  'curated',
  'target_gene_membership',
  'Reviewed public TF-target set; primary literature and corroboration are '
    || 'stored at member-source level. No upstream ligand activation inferred.'
FROM stage_22b_promotions AS stage
JOIN stage_22b_entity_map AS map
  ON map.species = stage.species
 AND map.endpoint_role = 'transcription_factor'
 AND map.symbol = stage.tf_symbol
ON CONFLICT (
  tf_entity_id, species_context, cell_type_context, compartment_context,
  source_registry, source_version
)
DO UPDATE SET
  regulon_name = EXCLUDED.regulon_name,
  definition_status = 'curated',
  notes = EXCLUDED.notes,
  updated_at = CURRENT_TIMESTAMP;

INSERT INTO RegulonMember (
  regulon_id, target_entity_id, membership_basis, regulatory_effect,
  membership_status, confidence_tier, export_priority, notes
)
SELECT
  regulon.regulon_id,
  target_map.entity_id,
  'inferred_regulatory',
  stage.effect_polarity,
  'supported',
  'medium',
  'medium',
  'Materialized ' || stage.materialization_id || '; source artifacts: '
    || stage.source_artifacts || '. Pair membership does not imply upstream TF activation.'
FROM stage_22b_promotions AS stage
JOIN stage_22b_entity_map AS tf_map
  ON tf_map.species = stage.species
 AND tf_map.endpoint_role = 'transcription_factor'
 AND tf_map.symbol = stage.tf_symbol
JOIN stage_22b_entity_map AS target_map
  ON target_map.species = stage.species
 AND target_map.endpoint_role = 'target_gene'
 AND target_map.symbol = stage.target_symbol
JOIN Regulon AS regulon
  ON regulon.tf_entity_id = tf_map.entity_id
 AND regulon.species_context = stage.species
 AND regulon.cell_type_context = 'unspecified'
 AND regulon.compartment_context = 'nucleus'
 AND regulon.source_registry = '{source_registry}'
 AND regulon.source_version = '{source_version}'
ON CONFLICT (regulon_id, target_entity_id)
DO UPDATE SET
  membership_basis = EXCLUDED.membership_basis,
  regulatory_effect = EXCLUDED.regulatory_effect,
  membership_status = 'supported',
  confidence_tier = 'medium',
  export_priority = 'medium',
  notes = EXCLUDED.notes,
  updated_at = CURRENT_TIMESTAMP;

-- Primary and corroborating PMIDs remain separate source records.  A stable
-- PubMed locator satisfies the source-anchor gate without fabricating Paper,
-- Observation, or AuthorClaim foreign keys.
INSERT INTO RegulonMemberSource (
  regulon_member_id, source_registry, source_version, external_record_id,
  source_locator, support_kind, evidence_scope, evidence_status,
  species_support, confidence_tier, citation_note, limitations
)
SELECT DISTINCT
  member.regulon_member_id,
  CASE WHEN stage.support_kind = 'database_curated' THEN 'public_tf_union_record' ELSE 'manual_pair_review' END,
  '{source_version}',
  stage.materialization_id || ':primary:' || btrim(pmid),
  'https://pubmed.ncbi.nlm.nih.gov/' || btrim(pmid) || '/',
  CASE WHEN stage.support_kind = 'database_curated' THEN 'database_curated' ELSE 'primary_experiment' END,
  'inferred_regulatory',
  'supporting',
  stage.species,
  'medium',
  CASE WHEN stage.support_kind = 'database_curated'
    THEN 'Public TF database reference PMID for Module 22B promotion ' || stage.materialization_id || '.'
    ELSE 'Primary pair-level literature source for Module 22B promotion ' || stage.materialization_id || '.'
  END,
  stage.limitations
FROM stage_22b_promotions AS stage
JOIN stage_22b_entity_map AS tf_map
  ON tf_map.species = stage.species
 AND tf_map.endpoint_role = 'transcription_factor'
 AND tf_map.symbol = stage.tf_symbol
JOIN stage_22b_entity_map AS target_map
  ON target_map.species = stage.species
 AND target_map.endpoint_role = 'target_gene'
 AND target_map.symbol = stage.target_symbol
JOIN Regulon AS regulon
  ON regulon.tf_entity_id = tf_map.entity_id
 AND regulon.species_context = stage.species
 AND regulon.source_registry = '{source_registry}'
 AND regulon.source_version = '{source_version}'
JOIN RegulonMember AS member
  ON member.regulon_id = regulon.regulon_id
 AND member.target_entity_id = target_map.entity_id
CROSS JOIN LATERAL regexp_split_to_table(stage.primary_pmids, ';') AS pmid
WHERE btrim(pmid) <> ''
ON CONFLICT DO NOTHING;

INSERT INTO RegulonMemberSource (
  regulon_member_id, source_registry, source_version, external_record_id,
  source_locator, support_kind, evidence_scope, evidence_status,
  species_support, confidence_tier, citation_note, limitations
)
SELECT DISTINCT
  member.regulon_member_id,
  CASE WHEN stage.support_kind = 'database_curated' THEN 'public_tf_union_record' ELSE 'manual_pair_review' END,
  '{source_version}',
  stage.materialization_id || ':corroborating:' || btrim(pmid),
  'https://pubmed.ncbi.nlm.nih.gov/' || btrim(pmid) || '/',
  CASE WHEN stage.support_kind = 'database_curated' THEN 'database_curated' ELSE 'primary_experiment' END,
  'inferred_regulatory',
  'supporting',
  stage.species,
  'medium',
  CASE WHEN stage.support_kind = 'database_curated'
    THEN 'Additional public TF database reference PMID for Module 22B promotion ' || stage.materialization_id || '.'
    ELSE 'Independent corroborating pair-level literature source for Module 22B promotion ' || stage.materialization_id || '.'
  END,
  stage.limitations
FROM stage_22b_promotions AS stage
JOIN stage_22b_entity_map AS tf_map
  ON tf_map.species = stage.species
 AND tf_map.endpoint_role = 'transcription_factor'
 AND tf_map.symbol = stage.tf_symbol
JOIN stage_22b_entity_map AS target_map
  ON target_map.species = stage.species
 AND target_map.endpoint_role = 'target_gene'
 AND target_map.symbol = stage.target_symbol
JOIN Regulon AS regulon
  ON regulon.tf_entity_id = tf_map.entity_id
 AND regulon.species_context = stage.species
 AND regulon.source_registry = '{source_registry}'
 AND regulon.source_version = '{source_version}'
JOIN RegulonMember AS member
  ON member.regulon_id = regulon.regulon_id
 AND member.target_entity_id = target_map.entity_id
CROSS JOIN LATERAL regexp_split_to_table(stage.corroborating_pmids, ';') AS pmid
WHERE btrim(pmid) <> ''
ON CONFLICT DO NOTHING;

-- Database-curated rows may have no PMID. Preserve their signed public
-- record keys as first-class provenance instead of manufacturing a PubMed
-- locator or silently dropping the row.
INSERT INTO RegulonMemberSource (
  regulon_member_id, source_registry, source_version, external_record_id,
  source_locator, support_kind, evidence_scope, evidence_status,
  species_support, confidence_tier, citation_note, limitations
)
SELECT DISTINCT
  member.regulon_member_id,
  'public_tf_union_record',
  '{source_version}',
  stage.materialization_id || ':external:' || btrim(record_key),
  'public_record:' || btrim(record_key),
  'database_curated',
  'inferred_regulatory',
  'supporting',
  stage.species,
  'medium',
  'Signed public TF record retained for Module 22B promotion ' || stage.materialization_id || '.',
  stage.limitations
FROM stage_22b_promotions AS stage
JOIN stage_22b_entity_map AS tf_map
  ON tf_map.species = stage.species
 AND tf_map.endpoint_role = 'transcription_factor'
 AND tf_map.symbol = stage.tf_symbol
JOIN stage_22b_entity_map AS target_map
  ON target_map.species = stage.species
 AND target_map.endpoint_role = 'target_gene'
 AND target_map.symbol = stage.target_symbol
JOIN Regulon AS regulon
  ON regulon.tf_entity_id = tf_map.entity_id
 AND regulon.species_context = stage.species
 AND regulon.source_registry = '{source_registry}'
 AND regulon.source_version = '{source_version}'
JOIN RegulonMember AS member
  ON member.regulon_id = regulon.regulon_id
 AND member.target_entity_id = target_map.entity_id
CROSS JOIN LATERAL regexp_split_to_table(stage.external_record_keys, ';') AS record_key
WHERE btrim(record_key) <> ''
ON CONFLICT DO NOTHING;

INSERT INTO SignalingEdgeRegisterSource (
  edge_id, register_edge_id, register_evidence_id, module,
  support_kind, species_support, source_scope, confidence_tier,
  citation_note, notes, source_kind, source_locator,
  source_locator_status, evidence_summary, limitations,
  evidence_layer, evidence_exportable, consolidation_note
)
SELECT DISTINCT
  edge_map.edge_id,
  edge_map.register_edge_id,
  edge_map.register_edge_id || '-P-' || btrim(pmid),
  '22B',
  CASE WHEN stage.support_kind = 'database_curated' THEN 'database_curated' ELSE 'primary_experiment' END,
  stage.species,
  CASE WHEN stage.support_kind = 'database_curated' THEN 'inferred_regulatory' ELSE 'contextual_support' END,
  'medium',
  CASE WHEN stage.support_kind = 'database_curated'
    THEN 'Public TF database reference PMID ' || btrim(pmid) || ' for reviewed TF-target pair.'
    ELSE 'Primary literature PMID ' || btrim(pmid) || ' for reviewed TF-target pair.'
  END,
  'Materialized from normalized Module 22B promotion staging; no canonical '
    || 'Paper/Observation/AuthorClaim FK inferred.',
  CASE WHEN stage.support_kind = 'database_curated' THEN 'database_curated' ELSE 'primary_literature' END,
  'https://pubmed.ncbi.nlm.nih.gov/' || btrim(pmid) || '/',
  'pubmed_locator',
  'Exact pair-level primary literature support; public database membership is '
    || 'retained separately from the evidence assessment.',
  stage.limitations,
  'target_gene',
  TRUE,
  'Canonical Module 22B register TF-target evidence materialized {source_version}.'
FROM stage_22b_promotions AS stage
JOIN stage_22b_edge_map AS edge_map
  ON edge_map.materialization_id = stage.materialization_id
CROSS JOIN LATERAL regexp_split_to_table(stage.primary_pmids, ';') AS pmid
WHERE btrim(pmid) <> ''
ON CONFLICT (edge_id, register_evidence_id) DO NOTHING;

INSERT INTO SignalingEdgeRegisterSource (
  edge_id, register_edge_id, register_evidence_id, module,
  support_kind, species_support, source_scope, confidence_tier,
  citation_note, notes, source_kind, source_locator,
  source_locator_status, evidence_summary, limitations,
  evidence_layer, evidence_exportable, consolidation_note
)
SELECT DISTINCT
  edge_map.edge_id,
  edge_map.register_edge_id,
  edge_map.register_edge_id || '-C-' || btrim(pmid),
  '22B',
  CASE WHEN stage.support_kind = 'database_curated' THEN 'database_curated' ELSE 'primary_experiment' END,
  stage.species,
  CASE WHEN stage.support_kind = 'database_curated' THEN 'inferred_regulatory' ELSE 'contextual_support' END,
  'medium',
  CASE WHEN stage.support_kind = 'database_curated'
    THEN 'Additional public TF database reference PMID ' || btrim(pmid) || ' for reviewed TF-target pair.'
    ELSE 'Independent corroborating literature PMID ' || btrim(pmid) || ' for reviewed TF-target pair.'
  END,
  'Corroborating source retained separately from the primary pair source.',
  CASE WHEN stage.support_kind = 'database_curated' THEN 'database_curated' ELSE 'primary_literature' END,
  'https://pubmed.ncbi.nlm.nih.gov/' || btrim(pmid) || '/',
  'pubmed_locator',
  'Independent corroborating pair-level literature support.',
  stage.limitations,
  'target_gene',
  TRUE,
  'Canonical Module 22B register TF-target evidence materialized {source_version}.'
FROM stage_22b_promotions AS stage
JOIN stage_22b_edge_map AS edge_map
  ON edge_map.materialization_id = stage.materialization_id
CROSS JOIN LATERAL regexp_split_to_table(stage.corroborating_pmids, ';') AS pmid
WHERE btrim(pmid) <> ''
ON CONFLICT (edge_id, register_evidence_id) DO NOTHING;

INSERT INTO SignalingEdgeRegisterSource (
  edge_id, register_edge_id, register_evidence_id, module,
  support_kind, species_support, source_scope, confidence_tier,
  citation_note, notes, source_kind, source_locator,
  source_locator_status, evidence_summary, limitations,
  evidence_layer, evidence_exportable, consolidation_note
)
SELECT DISTINCT
  edge_map.edge_id,
  edge_map.register_edge_id,
  edge_map.register_edge_id || '-X-' || btrim(record_key),
  '22B',
  'database_curated',
  stage.species,
  'inferred_regulatory',
  'medium',
  'Signed public TF record ' || btrim(record_key) || ' retained for reviewed TF-target pair.',
  'Materialized from the current Module 22B register-backed stage; database support does not prove direct DNA binding.',
  'database_curated',
  'public_record:' || btrim(record_key),
  'public_record_locator',
  'Signed public TF database record supports the normalized TF-target membership.',
  stage.limitations,
  'target_gene',
  TRUE,
  'Canonical Module 22B register TF-target evidence materialized {source_version}.'
FROM stage_22b_promotions AS stage
JOIN stage_22b_edge_map AS edge_map
  ON edge_map.materialization_id = stage.materialization_id
CROSS JOIN LATERAL regexp_split_to_table(stage.external_record_keys, ';') AS record_key
WHERE btrim(record_key) <> ''
ON CONFLICT (edge_id, register_evidence_id) DO NOTHING;

DO $$
DECLARE
  n INTEGER;
  missing_roles INTEGER;
  missing_sources INTEGER;
BEGIN
  SELECT count(*) INTO n FROM stage_22b_edge_map;
  IF n <> {expected_rows} THEN
    RAISE EXCEPTION 'Expected {expected_rows} canonical 22B edge mappings, found %', n;
  END IF;
  SELECT count(*) INTO missing_roles
  FROM stage_22b_edge_map AS mapped
  JOIN SignalingEdge AS edge ON edge.edge_id = mapped.edge_id
  WHERE NOT EXISTS (
      SELECT 1 FROM SignalingEntityRole AS role
      WHERE role.entity_id = edge.source_entity_id
        AND role.role = 'transcription_factor'
        AND role.role_status IN ('curated', 'derived')
        AND role.export_priority <> 'exclude'
    )
    OR NOT EXISTS (
      SELECT 1 FROM SignalingEntityRole AS role
      WHERE role.entity_id = edge.target_entity_id
        AND role.role = 'target_gene'
        AND role.role_status IN ('curated', 'derived')
        AND role.export_priority <> 'exclude'
    );
  SELECT count(*) INTO missing_sources
  FROM stage_22b_edge_map AS mapped
  WHERE NOT EXISTS (
    SELECT 1 FROM SignalingEdgeRegisterSource AS source
    WHERE source.edge_id = mapped.edge_id
      AND source.evidence_exportable
      AND (
        source.source_locator LIKE 'https://pubmed.ncbi.nlm.nih.gov/%'
        OR source.source_locator LIKE 'public_record:%'
      )
  );
  IF missing_roles <> 0 OR missing_sources <> 0 THEN
    RAISE EXCEPTION '22B materialization validation failed: missing_roles=%, missing_sources=%', missing_roles, missing_sources;
  END IF;
END $$;

SELECT '22B_staged_pairs' AS metric, count(*) AS value FROM stage_22b_promotions
UNION ALL
SELECT '22B_canonical_edge_mappings', count(*) FROM stage_22b_edge_map
UNION ALL
SELECT '22B_supported_regulon_members', count(*)
FROM RegulonMember AS member
JOIN Regulon AS regulon ON regulon.regulon_id = member.regulon_id
WHERE regulon.source_registry = '{source_registry}'
  AND regulon.source_version = '{source_version}'
  AND member.membership_status = 'supported'
  AND member.export_priority = 'medium';

COMMIT;
"""


def main() -> int:
    args = parse_args()
    stage_file = args.stage_root / "module22b_promoted_pairs.tsv"
    if not stage_file.is_file():
        raise SystemExit(f"Missing staging input: {stage_file}")
    manifest_file = args.stage_root / "module22b_materialization_manifest.json"
    if not manifest_file.is_file():
        raise SystemExit(f"Missing staging manifest: {manifest_file}")
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    expected_rows = int(manifest["unique_promoted_pairs"])
    materialization_version = str(manifest["materialization_version"])
    sql = build_sql(args.stage_root, expected_rows, materialization_version)
    if args.dry_run:
        print(json.dumps({
            "stage_root": str(args.stage_root),
            "expected_rows": expected_rows,
            "materialization_version": materialization_version,
            "sql_bytes": len(sql.encode("utf-8")),
            "database_write_performed": False,
        }, indent=2))
        return 0
    if not args.database_url:
        raise SystemExit("Provide --database-url or set MSCIDBLIT_DATABASE_URL/DATABASE_URL.")
    command = [args.psql, "-X", "-v", "ON_ERROR_STOP=1", "-d", args.database_url, "-f", "-"]
    result = subprocess.run(command, input=sql, text=True, check=False)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
