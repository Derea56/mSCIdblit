#!/usr/bin/env python3
"""Materialize reviewed Module-B promotion provenance into canonical PostgreSQL.

This is the explicit write step after audit-layer staging. It updates only the
108 staged promotion candidates from the 2026-08-26 round. Canonical graph
constraints intentionally exclude self-loops; such rows remain in staging and
are reported as skipped. No Paper, Observation, or AuthorClaim foreign keys
are fabricated from register-level evidence.
"""

from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STAGE = ROOT / "work" / "module_b_consolidation" / "staging_round_2026_08_26"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--database-url",
        default=os.environ.get("MSCIDBLIT_DATABASE_URL") or os.environ.get("DATABASE_URL"),
        help="PostgreSQL connection URL accepted by psql -d.",
    )
    parser.add_argument("--stage-root", type=Path, default=DEFAULT_STAGE)
    parser.add_argument("--psql", default="psql")
    return parser.parse_args()


def sql_literal(path: Path) -> str:
    return "'" + str(path.resolve()).replace("'", "''") + "'"


def build_sql(stage_root: Path) -> str:
    candidates = stage_root / "all_promoted_edge_candidates.tsv"
    evidence = stage_root / "all_promoted_evidence_candidates.tsv"
    candidate_path = sql_literal(candidates)
    evidence_path = sql_literal(evidence)
    return f"""\
BEGIN;

CREATE TEMP TABLE stage_candidates (
  staging_candidate_id TEXT, module TEXT, b_edge_id TEXT,
  source_a_edge_id TEXT, source_entity TEXT, relation_type TEXT,
  target_entity TEXT, pathway_name TEXT, evidence_layer TEXT,
  edge_status TEXT, context_scope TEXT, cell_type_context TEXT,
  compartment_context TEXT, species_context TEXT, injury_context TEXT,
  confidence_tier TEXT, export_priority TEXT, exportable TEXT,
  linked_b_evidence_ids TEXT, promotion_primary_pmids TEXT,
  promotion_corroborating_pmids TEXT, exact_evidence_status TEXT,
  module_fit TEXT, decision TEXT, evidence_summary TEXT,
  limitations TEXT, staging_status TEXT, canonical_entity_role_gate TEXT
);
\\copy stage_candidates FROM {candidate_path} WITH (FORMAT csv, HEADER true, DELIMITER E'\\t', QUOTE '"', ESCAPE '"', NULL '')

CREATE TEMP TABLE stage_evidence (
  staging_evidence_id TEXT, module TEXT, b_evidence_id TEXT,
  b_edge_ids TEXT, source_a_evidence_id TEXT, source_kind TEXT,
  source_locator TEXT, support_kind TEXT, species_support TEXT,
  source_scope TEXT, confidence_tier TEXT, citation_note TEXT,
  evidence_summary TEXT, limitations TEXT, evidence_layer TEXT,
  exportable TEXT, promotion_specific TEXT, staging_status TEXT
);
\\copy stage_evidence FROM {evidence_path} WITH (FORMAT csv, HEADER true, DELIMITER E'\\t', QUOTE '"', ESCAPE '"', NULL '')

CREATE TEMP TABLE stage_write_candidates AS
SELECT c.*, r.edge_id AS canonical_edge_id
FROM stage_candidates AS c
JOIN SignalingEdgeRegister AS r
  ON r.register_edge_id = c.b_edge_id
JOIN SignalingEdge AS e
  ON e.edge_id = r.edge_id
WHERE e.source_entity_id <> e.target_entity_id;

DO $$
DECLARE
  candidate_count INTEGER;
  write_count INTEGER;
  self_loop_count INTEGER;
  missing_non_self_loop_count INTEGER;
  missing_promotion_evidence_count INTEGER;
BEGIN
  SELECT count(*) INTO candidate_count FROM stage_candidates;
  SELECT count(*) INTO write_count FROM stage_write_candidates;
  SELECT count(*) INTO self_loop_count
  FROM stage_candidates AS c
  WHERE lower(btrim(c.source_entity)) = lower(btrim(c.target_entity));
  SELECT count(*) INTO missing_non_self_loop_count
  FROM stage_candidates AS c
  LEFT JOIN SignalingEdgeRegister AS r ON r.register_edge_id = c.b_edge_id
  LEFT JOIN SignalingEdge AS e ON e.edge_id = r.edge_id
  WHERE lower(btrim(c.source_entity)) <> lower(btrim(c.target_entity))
    AND (r.edge_id IS NULL OR e.edge_id IS NULL);
  SELECT count(*) INTO missing_promotion_evidence_count
  FROM stage_write_candidates AS c
  WHERE NOT EXISTS (
    SELECT 1 FROM stage_evidence AS s
    WHERE s.promotion_specific = 'true'
      AND lower(btrim(s.confidence_tier)) = 'high'
      AND position(';' || s.b_edge_ids || ';' in ';' || c.b_edge_id || ';') > 0
  );
  IF candidate_count <> 108 THEN
    RAISE EXCEPTION 'Expected 108 staged candidates, found %', candidate_count;
  END IF;
  IF write_count <> 107 THEN
    RAISE EXCEPTION 'Expected 107 non-self-loop write candidates, found %', write_count;
  END IF;
  IF self_loop_count <> 1 THEN
    RAISE EXCEPTION 'Expected 1 intentional self-loop skip, found %', self_loop_count;
  END IF;
  IF missing_non_self_loop_count <> 0 THEN
    RAISE EXCEPTION 'Missing or invalid non-self-loop canonical candidates: %', missing_non_self_loop_count;
  END IF;
  IF missing_promotion_evidence_count <> 0 THEN
    RAISE EXCEPTION 'Write candidates missing high promotion evidence: %', missing_promotion_evidence_count;
  END IF;
END $$;

UPDATE SignalingEdgeRegister AS r
SET confidence_tier = 'high',
    evidence_ids = (
      SELECT string_agg(token, ';' ORDER BY token)
      FROM (
        SELECT DISTINCT btrim(token) AS token
        FROM regexp_split_to_table(
          coalesce(r.evidence_ids, '') || ';' || c.linked_b_evidence_ids, ';'
        ) AS token
        WHERE btrim(token) <> ''
      ) AS tokens
    ),
    consolidation_note = CASE
      WHEN position('High-confidence promotion materialized 2026-08-26' in coalesce(r.consolidation_note, '')) > 0
        THEN r.consolidation_note
      ELSE concat_ws(' ', NULLIF(r.consolidation_note, ''), 'High-confidence promotion materialized 2026-08-26 from audit staging.')
    END
FROM stage_write_candidates AS c
WHERE r.register_edge_id = c.b_edge_id;

INSERT INTO SignalingEdgeRegisterSource (
  edge_id, register_edge_id, register_evidence_id, module,
  support_kind, species_support, source_scope, confidence_tier,
  citation_note, notes, source_kind, source_locator,
  source_locator_status, evidence_summary, limitations,
  evidence_layer, evidence_exportable, consolidation_note
)
SELECT DISTINCT
  c.canonical_edge_id,
  c.b_edge_id,
  s.b_evidence_id,
  c.module,
  NULLIF(s.support_kind, ''),
  CASE
    WHEN lower(btrim(s.species_support)) IN ('mouse', 'human', 'both', 'mixed', 'not_applicable')
      THEN lower(btrim(s.species_support))
    WHEN lower(s.species_support) LIKE '%mouse%'
      AND lower(s.species_support) LIKE '%human%' THEN 'mixed'
    WHEN lower(s.species_support) LIKE '%mouse%' THEN 'mouse'
    WHEN lower(s.species_support) LIKE '%human%' THEN 'human'
    ELSE NULL
  END,
  CASE
    WHEN lower(btrim(s.source_scope)) IN ('direct_edge', 'pathway_membership', 'contextual_support', 'negative_evidence')
      THEN lower(btrim(s.source_scope))
    WHEN lower(s.evidence_layer) LIKE '%ligand_receptor%'
      THEN 'direct_edge'
    WHEN lower(s.evidence_layer) LIKE '%receptor_proximal%'
      OR lower(s.evidence_layer) LIKE '%pathway%' THEN 'pathway_membership'
    WHEN lower(s.evidence_layer) LIKE '%downstream%'
      OR lower(s.evidence_layer) LIKE '%contextual%' THEN 'contextual_support'
    ELSE NULL
  END,
  CASE
    WHEN lower(btrim(s.confidence_tier)) IN ('high', 'medium', 'low', 'uncertain', 'medium-high', 'medium-low', 'low-medium')
      THEN lower(btrim(s.confidence_tier))
    WHEN lower(btrim(s.confidence_tier)) LIKE 'high %' THEN 'high'
    WHEN lower(btrim(s.confidence_tier)) LIKE 'medium %' THEN 'medium'
    ELSE NULL
  END,
  NULLIF(s.citation_note, ''),
  concat_ws(
    ' ',
    'Materialized from reviewed B-module staging; no canonical Paper/Observation/AuthorClaim FK inferred.',
    CASE
      WHEN lower(btrim(s.confidence_tier)) IN ('high', 'medium', 'low', 'uncertain', 'medium-high', 'medium-low', 'low-medium')
        OR lower(btrim(s.confidence_tier)) LIKE 'high %'
        OR lower(btrim(s.confidence_tier)) LIKE 'medium %'
        OR btrim(s.confidence_tier) = ''
        THEN NULL
      ELSE 'raw_staged_confidence_tier=' || s.confidence_tier
    END
    , CASE
      WHEN lower(btrim(s.species_support)) IN ('mouse', 'human', 'both', 'mixed', 'not_applicable')
        OR btrim(s.species_support) = '' THEN NULL
      ELSE 'raw_staged_species_support=' || s.species_support
    END
    , CASE
      WHEN lower(btrim(s.source_scope)) IN ('direct_edge', 'pathway_membership', 'contextual_support', 'negative_evidence')
        OR btrim(s.source_scope) = '' THEN NULL
      ELSE 'raw_staged_source_scope=' || s.source_scope
    END
  ),
  NULLIF(s.source_kind, ''),
  NULLIF(s.source_locator, ''),
  CASE
    WHEN s.source_locator ~* '(PMID:|PMCID:|DOI:|https?://|mSCIdblit:)' THEN 'stable_or_staged'
    ELSE 'local_only_or_unresolved'
  END,
  NULLIF(s.evidence_summary, ''),
  NULLIF(s.limitations, ''),
  NULLIF(s.evidence_layer, ''),
  lower(btrim(s.exportable)) = 'true',
  'Canonical register provenance written 2026-08-26 from high-confidence promotion staging.'
FROM stage_write_candidates AS c
JOIN stage_evidence AS s
  ON position(';' || s.b_edge_ids || ';' in ';' || c.b_edge_id || ';') > 0
ON CONFLICT (edge_id, register_evidence_id) DO NOTHING;

DO $$
DECLARE
  not_high INTEGER;
  missing_sources INTEGER;
BEGIN
  SELECT count(*) INTO not_high
  FROM stage_write_candidates AS c
  JOIN SignalingEdgeRegister AS r ON r.register_edge_id = c.b_edge_id
  WHERE r.confidence_tier <> 'high';
  SELECT count(*) INTO missing_sources
  FROM stage_write_candidates AS c
  JOIN stage_evidence AS s
    ON s.promotion_specific = 'true'
   AND position(';' || s.b_edge_ids || ';' in ';' || c.b_edge_id || ';') > 0
  WHERE NOT EXISTS (
    SELECT 1 FROM SignalingEdgeRegisterSource AS rs
    WHERE rs.edge_id = c.canonical_edge_id
      AND rs.register_evidence_id = s.b_evidence_id
  );
  IF not_high <> 0 OR missing_sources <> 0 THEN
    RAISE EXCEPTION 'Canonical promotion write validation failed: not_high=%, missing_sources=%', not_high, missing_sources;
  END IF;
END $$;

SELECT 'staged_candidates' AS check_name, count(*) AS count FROM stage_candidates
UNION ALL
SELECT 'canonical_write_candidates', count(*) FROM stage_write_candidates
UNION ALL
SELECT 'intentional_self_loop_skipped', count(*)
FROM stage_candidates AS c
WHERE lower(btrim(c.source_entity)) = lower(btrim(c.target_entity));

COMMIT;
"""


def main() -> int:
    args = parse_args()
    if not args.database_url:
        raise SystemExit("Provide --database-url or set MSCIDBLIT_DATABASE_URL/DATABASE_URL.")
    for filename in ("all_promoted_edge_candidates.tsv", "all_promoted_evidence_candidates.tsv"):
        path = args.stage_root / filename
        if not path.exists():
            raise SystemExit(f"Missing staging input: {path}")
    sql = build_sql(args.stage_root)
    command = [args.psql, "-X", "-v", "ON_ERROR_STOP=1", "-d", args.database_url, "-f", "-"]
    result = subprocess.run(command, input=sql, text=True, check=False)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
