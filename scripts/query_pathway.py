#!/usr/bin/env python3
"""Query a release database across mechanism and evidence layers.

This is a read-only retrieval utility.  It intentionally keeps three kinds of
information separate:

* canonical mechanism edges and their register/source provenance;
* external modality evidence linked to modules, pathways, entities, or edges;
* method-resource membership and public-TF staging rows.

Presence in a method resource or staging file is not converted into a
canonical mechanism claim.  The database URL is passed to ``psql`` without
being written to the result.
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STAGING_FILES = (
    ROOT / "data/processed/public_tf_union_v1/module_curation/new_tf_materialized/priority_tf_agent_decisions.tsv",
    ROOT / "data/processed/public_tf_union_v1/source_regulon_members.tsv",
)
DEFAULT_LOCAL_EVIDENCE_FILES = (
    ROOT / "data/processed/mscs_modality_evidence_import_v1/evidence_source_records.tsv",
    ROOT / "data/processed/mscs_modality_evidence_import_v1/evidence_observation_details.tsv",
)


# The marker is replaced with a SQL string literal after quote escaping.  This
# keeps apostrophes and wildcard characters literal and avoids psql variable
# substitution differences across client versions.  The release schema is
# intentionally queried using one statement.
QUERY_TERM_MARKER = "__MSCIDBLIT_QUERY_TERM__"

QUERY_SQL = r"""
WITH
matching_pathways AS MATERIALIZED (
  SELECT sp.pathway_id, sp.pathway_name, sp.pathway_class,
         sp.description, sp.source_registry, sp.notes
  FROM SignalingPathway sp
  WHERE strpos(lower(COALESCE(sp.pathway_name, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
     OR strpos(lower(COALESCE(sp.description, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
     OR strpos(lower(COALESCE(sp.notes, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
),
matching_entities AS MATERIALIZED (
  SELECT se.entity_id, se.canonical_name, se.entity_type,
         se.entity_subtype, se.gene_symbol, se.organism_scope,
         se.compartment, se.aliases, se.notes
  FROM SignalingEntity se
  WHERE strpos(lower(COALESCE(se.canonical_name, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
     OR strpos(lower(COALESCE(se.gene_symbol, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
     OR strpos(lower(COALESCE(se.aliases, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
     OR strpos(lower(COALESCE(se.notes, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
),
matching_edges AS MATERIALIZED (
  SELECT se.edge_id, se.source_entity_id, se.target_entity_id,
         se.pathway_id, src.canonical_name AS source_name,
         tgt.canonical_name AS target_name, sp.pathway_name,
         se.relation_type, se.effect_polarity, se.directionality,
         se.ligand_context, se.cell_type_context, se.compartment_context,
         se.species_context, se.injury_context, se.evidence_status,
         se.context_scope, se.export_priority, se.notes
  FROM SignalingEdge se
  JOIN SignalingEntity src ON src.entity_id = se.source_entity_id
  JOIN SignalingEntity tgt ON tgt.entity_id = se.target_entity_id
  LEFT JOIN SignalingPathway sp ON sp.pathway_id = se.pathway_id
  WHERE EXISTS (
          SELECT 1 FROM matching_entities me
          WHERE me.entity_id IN (se.source_entity_id, se.target_entity_id)
        )
     OR EXISTS (
          SELECT 1 FROM matching_pathways mp
          WHERE mp.pathway_id = se.pathway_id
        )
),
matching_communications AS MATERIALIZED (
  SELECT c.canonical_communication_id, c.species_scope,
         c.ligand_name, c.receptor_name, c.normalized_ligand_name,
         c.normalized_receptor_name, c.communication_kind,
         c.evidence_status, c.source_method_count, c.source_record_count,
         c.source_methods_json, c.normalization_notes
  FROM CanonicalCommunicationRecord c
  WHERE strpos(lower(COALESCE(c.ligand_name, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
     OR strpos(lower(COALESCE(c.receptor_name, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
     OR strpos(lower(COALESCE(c.normalized_ligand_name, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
     OR strpos(lower(COALESCE(c.normalized_receptor_name, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
     OR EXISTS (
          SELECT 1
          FROM MethodResourceRecord mrr
          JOIN MethodResourceAnnotation mra
            ON mra.method_resource_record_id = mrr.method_resource_record_id
          WHERE mrr.canonical_communication_id = c.canonical_communication_id
            AND strpos(lower(COALESCE(mra.annotation_value, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
        )
)
SELECT json_build_object(
  'pathways', COALESCE((
    SELECT json_agg(row_to_json(q) ORDER BY q.pathway_id)
    FROM (
      SELECT * FROM matching_pathways
    ) q
  ), '[]'::json),
  'entities', COALESCE((
    SELECT json_agg(row_to_json(q) ORDER BY q.entity_id)
    FROM (
      SELECT * FROM matching_entities
    ) q
  ), '[]'::json),
  'entity_roles', COALESCE((
    SELECT json_agg(row_to_json(q) ORDER BY q.entity_id, q.role)
    FROM (
      SELECT me.entity_id, me.canonical_name, r.role, r.role_status,
             r.role_source, r.role_evidence, r.source_registry,
             r.source_version, r.export_priority
      FROM matching_entities me
      JOIN SignalingEntityRole r ON r.entity_id = me.entity_id
    ) q
  ), '[]'::json),
  'pathway_members', COALESCE((
    SELECT json_agg(row_to_json(q) ORDER BY q.pathway_id, q.entity_id)
    FROM (
      SELECT mp.pathway_id, mp.pathway_name, spm.entity_id,
             se.canonical_name, se.gene_symbol, spm.member_role,
             spm.ordinal, spm.membership_status, spm.notes
      FROM matching_pathways mp
      JOIN SignalingPathwayMember spm ON spm.pathway_id = mp.pathway_id
      JOIN SignalingEntity se ON se.entity_id = spm.entity_id
    ) q
  ), '[]'::json),
  'mechanism_edges', COALESCE((
    SELECT json_agg(row_to_json(q) ORDER BY q.edge_id)
    FROM (
      SELECT * FROM matching_edges
    ) q
  ), '[]'::json),
  'mechanism_edge_sources', COALESCE((
    SELECT json_agg(row_to_json(q) ORDER BY q.edge_id, q.edge_source_id)
    FROM (
      SELECT me.edge_id, me.source_name, me.target_name, ses.edge_source_id,
             ses.support_kind, ses.species_support, ses.source_scope,
             ses.confidence_tier, ses.citation_note, ses.notes,
             ses.paper_id, p.pmid, p.doi, p.title, p.publication_year,
             ses.observation_id, ses.claim_id
      FROM matching_edges me
      JOIN SignalingEdgeSource ses ON ses.edge_id = me.edge_id
      LEFT JOIN Paper p ON p.paper_id = ses.paper_id
    ) q
  ), '[]'::json),
  'register_evidence', COALESCE((
    SELECT json_agg(row_to_json(q) ORDER BY q.edge_id, q.register_source_id)
    FROM (
      SELECT me.edge_id, me.source_name, me.target_name,
             ser.edge_register_id, ser.register_edge_id, ser.module,
             ser.source_label, ser.target_label, ser.register_relation_type,
             ser.graph_relation_type, ser.pathway_name, ser.evidence_layer,
             ser.edge_status, ser.confidence_tier, ser.evidence_ids,
             sers.register_source_id, sers.register_evidence_id,
             sers.support_kind, sers.species_support, sers.source_scope,
             sers.confidence_tier AS source_confidence_tier,
             sers.citation_note, sers.notes, sers.source_kind,
             sers.source_locator, sers.source_locator_status,
             sers.evidence_summary, sers.limitations,
             sers.evidence_layer AS source_evidence_layer,
             sers.evidence_exportable
      FROM matching_edges me
      JOIN SignalingEdgeRegister ser ON ser.edge_id = me.edge_id
      JOIN SignalingEdgeRegisterSource sers ON sers.edge_id = me.edge_id
    ) q
  ), '[]'::json),
  'linked_external_evidence', COALESCE((
    SELECT json_agg(row_to_json(q) ORDER BY q.source_record_id, q.module_evidence_link_id)
    FROM (
      SELECT mel.module_evidence_link_id, mel.source_record_id, mel.module,
             mel.link_role, mel.target_kind, mel.support_status,
             mel.evidence_grade, mel.context_level, mel.inference_role,
             mel.release_status, mel.link_basis, mel.source_field_locator,
             mel.notes, esr.source_system, esr.source_database,
             esr.source_record_type, esr.source_record_key,
             esr.source_version, esr.modality, esr.assay,
             esr.source_artifact_path, esr.source_locator, esr.source_url,
             esr.source_status, esr.provenance_note
      FROM ModuleEvidenceLink mel
      JOIN EvidenceSourceRecord esr ON esr.source_record_id = mel.source_record_id
      WHERE EXISTS (SELECT 1 FROM matching_edges me WHERE me.edge_id = mel.edge_id)
         OR EXISTS (SELECT 1 FROM matching_entities me WHERE me.entity_id = mel.entity_id)
         OR EXISTS (SELECT 1 FROM matching_pathways mp WHERE mp.pathway_id = mel.pathway_id)
         OR strpos(lower(COALESCE(esr.source_record_key, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
         OR strpos(lower(COALESCE(esr.provenance_note, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
    ) q
  ), '[]'::json),
  'modality_observations', COALESCE((
    SELECT json_agg(row_to_json(q) ORDER BY q.source_record_id, q.detail_id)
    FROM (
      SELECT eod.detail_id, eod.source_record_id, eod.source_detail_key,
             eod.reported_entity_name, eod.reported_entity_type,
             eod.measurement_kind, eod.assay, eod.protein_form,
             eod.feature_type, eod.feature_id, eod.reported_value_numeric,
             eod.reported_value_text, eod.reported_value_kind,
             eod.native_value_numeric, eod.transcribed_value_numeric,
             eod.transcribed_value_text, eod.transcribed_value_sem,
             eod.transcribed_value_sd, eod.transcribed_value_lower,
             eod.transcribed_value_upper, eod.unit,
             eod.direction_vs_control, eod.comparator, eod.sample_count,
             eod.biological_replicates, eod.technical_replicates,
             eod.timepoint_value, eod.timepoint_unit, eod.condition,
             eod.tissue_context, eod.cell_context, eod.sample_scope,
             eod.normalization, eod.negative_evidence_status,
             eod.source_evidence_label, eod.evidence_grade,
             eod.context_level, eod.measurement_status,
             eod.source_field_locator, eod.raw_observation_text,
             eod.normalization_notes, eod.native_fields_json,
             esr.source_system,
             esr.source_database, esr.source_record_type,
             esr.source_record_key, esr.source_version, esr.modality,
             esr.source_locator, esr.source_url, esr.source_status,
             esr.provenance_note
      FROM EvidenceObservationDetail eod
      JOIN EvidenceSourceRecord esr ON esr.source_record_id = eod.source_record_id
      WHERE strpos(lower(COALESCE(eod.reported_entity_name, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
         OR strpos(lower(COALESCE(eod.feature_id, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
         OR strpos(lower(COALESCE(eod.native_fields_json, '')), lower(__MSCIDBLIT_QUERY_TERM__)) > 0
    ) q
  ), '[]'::json),
  'method_communications', COALESCE((
    SELECT json_agg(row_to_json(q) ORDER BY q.canonical_communication_id)
    FROM (
      SELECT * FROM matching_communications
    ) q
  ), '[]'::json),
  'method_resource_records', COALESCE((
    SELECT json_agg(row_to_json(q) ORDER BY q.method_resource_record_id)
    FROM (
      SELECT mrr.method_resource_record_id, mrr.method_resource_id,
             mr.method_name, mr.resource_name, mr.resource_key,
             mrr.canonical_communication_id, mrr.source_record_key,
             mrr.source_record_key_kind, mrr.record_kind, mrr.native_ligand,
             mrr.native_receptor, mrr.normalized_ligand,
             mrr.normalized_receptor, mrr.original_values_json,
             mrr.normalized_values_json, mrr.transform_notes,
             mrr.evidence_status, mrr.method_score_json
      FROM MethodResourceRecord mrr
      JOIN MethodResource mr ON mr.method_resource_id = mrr.method_resource_id
      JOIN matching_communications mc
        ON mc.canonical_communication_id = mrr.canonical_communication_id
    ) q
  ), '[]'::json),
  'method_resource_annotations', COALESCE((
    SELECT json_agg(row_to_json(q) ORDER BY q.method_resource_record_id, q.annotation_kind)
    FROM (
      SELECT mrr.method_resource_record_id, mr.method_name, mr.resource_name,
             mrr.canonical_communication_id, mra.annotation_kind,
             mra.source_field_name, mra.annotation_value,
             mra.annotation_scope, mra.notes
      FROM MethodResourceRecord mrr
      JOIN MethodResource mr ON mr.method_resource_id = mrr.method_resource_id
      JOIN matching_communications mc
        ON mc.canonical_communication_id = mrr.canonical_communication_id
      JOIN MethodResourceAnnotation mra
        ON mra.method_resource_record_id = mrr.method_resource_record_id
    ) q
  ), '[]'::json)
) AS payload;
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "query",
        help="Case-insensitive literal substring, such as IL1B or IL-1.",
    )
    parser.add_argument(
        "--database-url",
        help="PostgreSQL URL accepted by psql. Defaults to MSCIDBLIT_DATABASE_URL or DATABASE_URL.",
    )
    parser.add_argument(
        "--no-local-staging",
        action="store_true",
        help="Do not scan the two explicitly supported public-TF staging files.",
    )
    parser.add_argument(
        "--no-local-evidence",
        action="store_true",
        help="Do not scan the two exact local modality-import TSV snapshots.",
    )
    parser.add_argument(
        "--max-staged-rows",
        type=int,
        default=1000,
        help="Maximum rows returned per local staging file (default: 1000).",
    )
    parser.add_argument(
        "--max-local-evidence-rows",
        type=int,
        default=5000,
        help="Maximum rows returned per local modality snapshot (default: 5000).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Write JSON to this path instead of stdout.",
    )
    return parser.parse_args()


def run_database_query(database_url: str, query_term: str) -> dict[str, Any]:
    """Run one read-only JSON query and parse its single-row response."""

    if "\x00" in query_term:
        raise ValueError("query term cannot contain a NUL byte")
    sql_literal = "'" + query_term.replace("'", "''") + "'"
    sql = QUERY_SQL.replace(QUERY_TERM_MARKER, sql_literal)
    if QUERY_TERM_MARKER in sql:
        raise RuntimeError("query SQL marker was not fully replaced")

    result = subprocess.run(
        [
            "psql",
            "-X",
            "-At",
            "-v",
            "ON_ERROR_STOP=1",
            "-d",
            database_url,
            "-c",
            sql,
        ],
        capture_output=True,
        text=True,
        check=False,
        timeout=60,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "psql query failed")
    payload = result.stdout.strip()
    if not payload:
        raise RuntimeError("psql returned no JSON payload")
    try:
        decoded = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise RuntimeError("psql returned invalid JSON") from exc
    if not isinstance(decoded, dict):
        raise RuntimeError("psql returned a JSON value other than an object")
    return decoded


def row_matches(row: dict[str, str], query_term: str) -> bool:
    needle = query_term.casefold()
    return any(needle in (value or "").casefold() for value in row.values())


def scan_local_tsv(
    query_term: str,
    max_rows: int,
    files: tuple[Path, ...],
    *,
    row_label: str,
) -> dict[str, Any]:
    """Scan known TSV snapshots without treating them as database rows."""

    if max_rows < 1:
        raise ValueError("maximum local rows must be positive")

    matches: list[dict[str, Any]] = []
    file_reports: list[dict[str, Any]] = []
    for path in files:
        report: dict[str, Any] = {
            "path": str(path),
            "exists": path.exists(),
            "matched_rows": 0,
            "returned_rows": 0,
            "truncated": False,
        }
        if not path.exists():
            file_reports.append(report)
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            for row in reader:
                if not row_matches(row, query_term):
                    continue
                report["matched_rows"] += 1
                if report["returned_rows"] >= max_rows:
                    report["truncated"] = True
                    continue
                matches.append(
                    {
                        "source_layer": row_label,
                        "source_file": str(path),
                        "row": row,
                    }
                )
                report["returned_rows"] += 1
        file_reports.append(report)

    return {"files": file_reports, "rows": matches}


def scan_local_staging(
    query_term: str,
    max_rows: int,
    files: tuple[Path, ...] = DEFAULT_STAGING_FILES,
) -> dict[str, Any]:
    """Read only known public-TF staging files and label them as noncanonical."""

    result = scan_local_tsv(query_term, max_rows, files, row_label="public_tf_staging")
    for item in result["rows"]:
        item["staging_status"] = "staged_evidence_only"
        item["canonical_mechanism_status"] = "not_materialized_by_this_query"
    result["interpretation"] = (
        "These rows are local public-TF staging/provenance records. "
        "They are not canonical mechanism edges and are not promoted by this utility."
    )
    return result


def scan_local_evidence(
    query_term: str,
    max_rows: int,
    files: tuple[Path, ...] = DEFAULT_LOCAL_EVIDENCE_FILES,
) -> dict[str, Any]:
    """Read exact local modality-import snapshots as a separate layer."""

    result = scan_local_tsv(query_term, max_rows, files, row_label="local_import_snapshot")
    result["interpretation"] = (
        "These are exact local modality-import snapshots. They are returned "
        "separately because the v1.4.0 database dump may not contain their rows; "
        "they do not become canonical mechanism edges."
    )
    return result


def add_metadata(
    payload: dict[str, Any],
    query_term: str,
    local_staging: dict[str, Any] | None,
    local_evidence: dict[str, Any] | None,
) -> dict[str, Any]:
    layer_names = (
        "pathways",
        "entities",
        "entity_roles",
        "pathway_members",
        "mechanism_edges",
        "mechanism_edge_sources",
        "register_evidence",
        "linked_external_evidence",
        "modality_observations",
        "method_communications",
        "method_resource_records",
        "method_resource_annotations",
    )
    output = {
        "query": query_term,
        "query_semantics": "case-insensitive literal substring across indexed release fields",
        "database_read_only": True,
        "database_source": "PostgreSQL release materialization supplied by --database-url",
        "layers": {name: payload.get(name, []) for name in layer_names},
        "interpretation_boundary": {
            "mechanism_edges": "canonical traversable release claims with separate edge/register provenance",
            "linked_external_evidence": "cross-cutting evidence links; inclusion does not create an edge",
            "modality_observations": "reported/transcribed external measurements; not mechanism edges",
            "local_evidence_snapshots": "exact local import snapshots; not assumed to be database materialization",
            "method_communications": "method-resource membership; not biological validation",
            "method_resource_records": "exact native resource records linked to method communications",
            "staged_public_tf": "review/staging records; not canonical mechanism claims",
        },
    }
    output["counts"] = {
        name: len(output["layers"][name]) for name in layer_names
    }
    if local_staging is not None:
        output["staged_public_tf"] = local_staging
        output["counts"]["staged_public_tf"] = len(local_staging["rows"])
    if local_evidence is not None:
        output["local_evidence_snapshots"] = local_evidence
        output["counts"]["local_evidence_snapshots"] = len(local_evidence["rows"])
    return output


def main() -> int:
    args = parse_args()
    database_url = args.database_url
    if not database_url:
        import os

        database_url = os.environ.get("MSCIDBLIT_DATABASE_URL") or os.environ.get("DATABASE_URL")
    if not database_url:
        print("Provide --database-url or set MSCIDBLIT_DATABASE_URL/DATABASE_URL.", file=sys.stderr)
        return 2
    try:
        payload = run_database_query(database_url, args.query)
        staging = None if args.no_local_staging else scan_local_staging(args.query, args.max_staged_rows)
        local_evidence = (
            None
            if args.no_local_evidence
            else scan_local_evidence(args.query, args.max_local_evidence_rows)
        )
        output = add_metadata(payload, args.query, staging, local_evidence)
    except (OSError, RuntimeError, ValueError, subprocess.TimeoutExpired) as exc:
        print(f"query failed: {exc}", file=sys.stderr)
        return 1

    serialized = json.dumps(output, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
    else:
        sys.stdout.write(serialized)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
