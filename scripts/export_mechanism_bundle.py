#!/usr/bin/env python3
"""Export an mSCS-compatible mechanism bundle from the mSCIdblit database.

This script is intentionally conservative:

- it exports only graph artifacts that the simulator can consume directly
- it preserves mouse-vs-human support provenance instead of collapsing it
- it records the filter context used for the export in bundle metadata

The database remains the source of truth. The bundle is a derived snapshot.
"""

from __future__ import annotations

import argparse
import csv
from datetime import date
import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "data" / "processed" / "mechanism_bundle"
PRIORITY_RANK = {"high": 3, "medium": 2, "low": 1, "exclude": 0}


def read_project_version() -> str:
    version_path = ROOT / "VERSION"
    if not version_path.exists():
        return "0.0.0-dev"
    version = version_path.read_text().strip()
    if not version:
        raise SystemExit(f"Project version file is empty: {version_path}")
    return version


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--database-url",
        default=os.environ.get("MSCIDBLIT_DATABASE_URL") or os.environ.get("DATABASE_URL"),
        help="PostgreSQL connection URL. Defaults to MSCIDBLIT_DATABASE_URL or DATABASE_URL.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Directory for exported bundle files. Default: {DEFAULT_OUTPUT}",
    )
    parser.add_argument(
        "--species-context",
        action="append",
        default=[],
        help="Allowed SignalingEdge.species_context values. May be passed multiple times.",
    )
    parser.add_argument(
        "--species-support",
        action="append",
        default=[],
        help="Allowed SignalingEdgeSource.species_support values. May be passed multiple times.",
    )
    parser.add_argument(
        "--cell-type-context",
        action="append",
        default=[],
        help="Allowed SignalingEdge.cell_type_context values. May be passed multiple times.",
    )
    parser.add_argument(
        "--injury-context",
        action="append",
        default=[],
        help="Allowed SignalingEdge.injury_context values. May be passed multiple times.",
    )
    parser.add_argument(
        "--pathway-name",
        action="append",
        default=[],
        help="Allowed SignalingPathway.pathway_name values. May be passed multiple times.",
    )
    parser.add_argument(
        "--min-export-priority",
        choices=("high", "medium", "low"),
        default="low",
        help="Minimum SignalingEdge.export_priority to include. Default: low.",
    )
    parser.add_argument(
        "--require-sources",
        action="store_true",
        help="Drop edges that have no linked SignalingEdgeSource rows after filtering.",
    )
    parser.add_argument(
        "--bundle-name",
        default="mscs_mechanism_bundle",
        help="Metadata label for this export bundle.",
    )
    parser.add_argument(
        "--graph-version",
        default=read_project_version(),
        help="Frozen mechanism-graph version. Defaults to VERSION in the repository root.",
    )
    parser.add_argument(
        "--release-status",
        choices=("snapshot", "frozen"),
        default="snapshot",
        help="Release status recorded in metadata. Default: snapshot.",
    )
    return parser.parse_args()


def quote_sql(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def make_in_clause(values: list[str]) -> str:
    return "(" + ", ".join(quote_sql(value) for value in values) + ")"


def priority_clause(min_priority: str) -> str:
    allowed = [name for name, rank in PRIORITY_RANK.items() if rank >= PRIORITY_RANK[min_priority]]
    return f"COALESCE(se.export_priority, 'low') IN {make_in_clause(allowed)}"


def edge_filters(args: argparse.Namespace) -> list[str]:
    filters = [priority_clause(args.min_export_priority)]
    if args.species_context:
        filters.append(f"COALESCE(se.species_context, '') IN {make_in_clause(args.species_context)}")
    if args.cell_type_context:
        filters.append(f"COALESCE(se.cell_type_context, '') IN {make_in_clause(args.cell_type_context)}")
    if args.injury_context:
        filters.append(f"COALESCE(se.injury_context, '') IN {make_in_clause(args.injury_context)}")
    if args.pathway_name:
        filters.append(f"COALESCE(sp.pathway_name, '') IN {make_in_clause(args.pathway_name)}")
    return filters


def source_filters(args: argparse.Namespace, alias: str = "ses") -> list[str]:
    filters: list[str] = []
    if args.species_support:
        filters.append(f"COALESCE({alias}.species_support, '') IN {make_in_clause(args.species_support)}")
    return filters


def filtered_edges_cte(args: argparse.Namespace) -> str:
    edge_where = " AND ".join(edge_filters(args))
    source_where = " AND ".join(source_filters(args)) if source_filters(args) else "TRUE"
    register_source_where = (
        " AND ".join(source_filters(args, "sers")) if source_filters(args, "sers") else "TRUE"
    )
    source_exists = ""
    if args.require_sources:
        source_exists = f"""
  AND (
    EXISTS (
      SELECT 1
      FROM SignalingEdgeSource ses
      WHERE ses.edge_id = se.edge_id
        AND {source_where}
    )
    OR EXISTS (
      SELECT 1
      FROM SignalingEdgeRegisterSource sers
      WHERE sers.edge_id = se.edge_id
        AND {register_source_where}
    )
  )"""
    return f"""
WITH filtered_edges AS (
  SELECT
    se.edge_id,
    se.source_entity_id,
    se.target_entity_id,
    sp.pathway_name,
    se.relation_type,
    se.effect_polarity,
    se.species_context,
    se.cell_type_context,
    se.compartment_context,
    se.injury_context,
    se.evidence_status,
    se.context_scope,
    se.export_priority,
    se.notes
  FROM SignalingEdge se
  LEFT JOIN SignalingPathway sp ON sp.pathway_id = se.pathway_id
  WHERE {edge_where}{source_exists}
)"""


def run_copy(database_url: str, sql: str) -> str:
    cmd = [
        "psql",
        "-X",
        "-v",
        "ON_ERROR_STOP=1",
        "-d",
        database_url,
        "-c",
        f"COPY ({sql}) TO STDOUT WITH (FORMAT CSV, HEADER TRUE, DELIMITER E'\\t')",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        raise RuntimeError("psql export failed")
    return result.stdout


def parse_tsv_string(text: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    if not lines:
        return []
    return list(csv.DictReader(lines, delimiter="\t"))


def supported_pathway_summary(edges: list[dict[str, str]], edge_sources: list[dict[str, str]]) -> list[dict[str, object]]:
    edge_ids_by_pathway: dict[str, set[str]] = {}
    for row in edges:
        pathway = row["pathway_label"].strip() or "unlabeled_pathway"
        edge_ids_by_pathway.setdefault(pathway, set()).add(row["edge_id"])

    sources_by_edge: dict[str, list[dict[str, str]]] = {}
    for row in edge_sources:
        sources_by_edge.setdefault(row["edge_id"], []).append(row)

    rows: list[dict[str, object]] = []
    for pathway, edge_ids in sorted(edge_ids_by_pathway.items()):
        species_support = sorted(
            {
                source["species_support"]
                for edge_id in edge_ids
                for source in sources_by_edge.get(edge_id, [])
                if source["species_support"]
            }
        )
        confidence_tiers = sorted(
            {
                source["confidence_tier"]
                for edge_id in edge_ids
                for source in sources_by_edge.get(edge_id, [])
                if source["confidence_tier"]
            }
        )
        rows.append(
            {
                "pathway_label": pathway,
                "edge_count": len(edge_ids),
                "species_support": species_support,
                "confidence_tiers": confidence_tiers,
            }
        )
    return rows


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)


def export_nodes(database_url: str, args: argparse.Namespace) -> list[dict[str, str]]:
    sql = f"""
{filtered_edges_cte(args)}
SELECT
  'NODE' || LPAD(se.entity_id::text, 5, '0') AS node_id,
  se.canonical_name,
  COALESCE(
    (
      SELECT ser.role
      FROM SignalingEntityRole ser
      WHERE ser.entity_id = se.entity_id
        AND ser.role IN ('ligand', 'receptor', 'transcription_factor', 'target_gene')
        AND ser.role_status IN ('curated', 'derived')
        AND ser.export_priority <> 'exclude'
      ORDER BY CASE ser.role
        WHEN 'ligand' THEN 1
        WHEN 'receptor' THEN 2
        WHEN 'transcription_factor' THEN 3
        WHEN 'target_gene' THEN 4
      END
      LIMIT 1
    ),
    CASE lower(se.entity_type)
      WHEN 'tf' THEN 'transcription_factor'
      WHEN 'ligand' THEN 'ligand'
      WHEN 'receptor' THEN 'receptor'
      WHEN 'transcription_factor' THEN 'transcription_factor'
      WHEN 'target_gene' THEN 'target_gene'
      WHEN 'signaling_effector' THEN 'signaling_effector'
      ELSE 'signaling_effector'
    END
  ) AS node_type,
  COALESCE(se.entity_subtype, '') AS node_subtype,
  COALESCE(se.gene_symbol, '') AS gene_symbol,
  COALESCE(se.organism_scope, '') AS organism_scope,
  COALESCE(se.compartment, '') AS compartment,
  COALESCE(se.notes, '') AS notes
FROM SignalingEntity se
WHERE se.entity_id IN (
  SELECT source_entity_id FROM filtered_edges
  UNION
  SELECT target_entity_id FROM filtered_edges
)
ORDER BY se.entity_id
"""
    return parse_tsv_string(run_copy(database_url, sql))


def export_node_roles(database_url: str, args: argparse.Namespace) -> list[dict[str, str]]:
    sql = f"""
{filtered_edges_cte(args)}
SELECT
  'NODE' || LPAD(ser.entity_id::text, 5, '0') AS node_id,
  ser.role,
  ser.role_source,
  ser.role_evidence
FROM SignalingEntityRole ser
WHERE ser.entity_id IN (
  SELECT source_entity_id FROM filtered_edges
  UNION
  SELECT target_entity_id FROM filtered_edges
)
  AND ser.role_status IN ('curated', 'derived')
  AND ser.export_priority <> 'exclude'
ORDER BY ser.entity_id, ser.role
"""
    return parse_tsv_string(run_copy(database_url, sql))


def export_edges(database_url: str, args: argparse.Namespace) -> list[dict[str, str]]:
    sql = f"""
{filtered_edges_cte(args)}
SELECT
  'EDGE' || LPAD(fe.edge_id::text, 5, '0') AS edge_id,
  'NODE' || LPAD(fe.source_entity_id::text, 5, '0') AS source_node_id,
  'NODE' || LPAD(fe.target_entity_id::text, 5, '0') AS target_node_id,
  COALESCE(fe.pathway_name, '') AS pathway_label,
  fe.relation_type,
  COALESCE(fe.effect_polarity, '') AS effect_polarity,
  COALESCE(fe.species_context, '') AS species_context,
  COALESCE(fe.cell_type_context, '') AS cell_type_context,
  COALESCE(fe.compartment_context, '') AS compartment_context,
  COALESCE(fe.injury_context, '') AS injury_context,
  COALESCE(fe.evidence_status, '') AS evidence_status,
  COALESCE(fe.context_scope, '') AS context_scope,
  COALESCE(fe.export_priority, '') AS export_priority,
  COALESCE(fe.notes, '') AS notes
FROM filtered_edges fe
ORDER BY fe.edge_id
"""
    return parse_tsv_string(run_copy(database_url, sql))


def export_edge_sources(database_url: str, args: argparse.Namespace) -> list[dict[str, str]]:
    source_where = " AND ".join(source_filters(args)) if source_filters(args) else "TRUE"
    register_source_where = (
        " AND ".join(source_filters(args, "sers")) if source_filters(args, "sers") else "TRUE"
    )
    sql = f"""
{filtered_edges_cte(args)}
SELECT
  'SRC' || LPAD(ses.edge_source_id::text, 5, '0') AS edge_source_id,
  'EDGE' || LPAD(ses.edge_id::text, 5, '0') AS edge_id,
  COALESCE(ses.paper_id::text, '') AS paper_id,
  COALESCE(ses.observation_id::text, '') AS observation_id,
  COALESCE(ses.claim_id::text, '') AS claim_id,
  ses.support_kind,
  COALESCE(ses.species_support, '') AS species_support,
  COALESCE(ses.source_scope, '') AS source_scope,
  COALESCE(ses.confidence_tier, '') AS confidence_tier,
  COALESCE(ses.citation_note, '') AS citation_note,
  COALESCE(ses.notes, '') AS notes
FROM SignalingEdgeSource ses
JOIN filtered_edges fe ON fe.edge_id = ses.edge_id
WHERE {source_where}
UNION ALL
SELECT
  'REGSRC' || LPAD(sers.register_source_id::text, 5, '0') AS edge_source_id,
  'EDGE' || LPAD(sers.edge_id::text, 5, '0') AS edge_id,
  '' AS paper_id,
  'REGISTER:' || sers.register_evidence_id AS observation_id,
  '' AS claim_id,
  COALESCE(sers.support_kind, 'database_curated') AS support_kind,
  COALESCE(sers.species_support, '') AS species_support,
  COALESCE(sers.source_scope, 'register_evidence') AS source_scope,
  COALESCE(sers.confidence_tier, '') AS confidence_tier,
  COALESCE(sers.citation_note, '') AS citation_note,
  concat_ws('; ',
    'register_edge_id=' || sers.register_edge_id,
    'register_evidence_id=' || sers.register_evidence_id,
    'source_kind=' || COALESCE(sers.source_kind, ''),
    'source_locator=' || COALESCE(sers.source_locator, ''),
    'source_locator_status=' || COALESCE(sers.source_locator_status, ''),
    COALESCE(sers.notes, ''),
    COALESCE(sers.limitations, '')
  ) AS notes
FROM SignalingEdgeRegisterSource sers
JOIN filtered_edges fe ON fe.edge_id = sers.edge_id
WHERE {register_source_where}
ORDER BY edge_source_id
"""
    return parse_tsv_string(run_copy(database_url, sql))


def metadata(args: argparse.Namespace, nodes: list[dict[str, str]], node_roles: list[dict[str, str]], edges: list[dict[str, str]], edge_sources: list[dict[str, str]]) -> dict[str, object]:
    pathway_rows = supported_pathway_summary(edges, edge_sources)
    release_id = f"{args.bundle_name}:v{args.graph_version}"
    return {
        "bundle_name": args.bundle_name,
        "graph_version": args.graph_version,
        "release_status": args.release_status,
        "release_id": release_id,
        "exported_at": date.today().isoformat(),
        "source_repo": "mSCIdblit",
        "target_repo": "mSCS",
        "authoritative_pathway_snapshot": True,
        "canonical_database_materialization": True,
        "role_authority": "SignalingEntityRole",
        "register_evidence_materialization": "SignalingEdgeRegisterSource",
        "replacement_policy": "Importing this bundle should replace the currently supported pathway set in mSCS.",
        "filters": {
            "species_context": args.species_context,
            "species_support": args.species_support,
            "cell_type_context": args.cell_type_context,
            "injury_context": args.injury_context,
            "pathway_name": args.pathway_name,
            "min_export_priority": args.min_export_priority,
            "require_sources": args.require_sources,
        },
        "counts": {
            "nodes": len(nodes),
            "node_roles": len(node_roles),
            "edges": len(edges),
            "edge_sources": len(edge_sources),
        },
        "files": {
            "nodes": "mechanism_nodes.tsv",
            "node_roles": "mechanism_node_roles.tsv",
            "edges": "mechanism_edges.tsv",
            "edge_sources": "mechanism_edge_sources.tsv",
        },
        "supported_pathways": pathway_rows,
    }


def main() -> None:
    args = parse_args()
    if not args.database_url:
        raise SystemExit("Provide --database-url or set MSCIDBLIT_DATABASE_URL/DATABASE_URL.")

    output_dir = args.output_dir.resolve()
    nodes = export_nodes(args.database_url, args)
    node_roles = export_node_roles(args.database_url, args)
    edges = export_edges(args.database_url, args)
    edge_sources = export_edge_sources(args.database_url, args)

    write_tsv(
        output_dir / "mechanism_nodes.tsv",
        ["node_id", "canonical_name", "node_type", "node_subtype", "gene_symbol", "organism_scope", "compartment", "notes"],
        nodes,
    )
    write_tsv(
        output_dir / "mechanism_node_roles.tsv",
        ["node_id", "role", "role_source", "role_evidence"],
        node_roles,
    )
    write_tsv(
        output_dir / "mechanism_edges.tsv",
        [
            "edge_id",
            "source_node_id",
            "target_node_id",
            "pathway_label",
            "relation_type",
            "effect_polarity",
            "species_context",
            "cell_type_context",
            "compartment_context",
            "injury_context",
            "evidence_status",
            "context_scope",
            "export_priority",
            "notes",
        ],
        edges,
    )
    write_tsv(
        output_dir / "mechanism_edge_sources.tsv",
        [
            "edge_source_id",
            "edge_id",
            "paper_id",
            "observation_id",
            "claim_id",
            "support_kind",
            "species_support",
            "source_scope",
            "confidence_tier",
            "citation_note",
            "notes",
        ],
        edge_sources,
    )
    (output_dir / "bundle_metadata.json").write_text(json.dumps(metadata(args, nodes, node_roles, edges, edge_sources), indent=2) + "\n")

    print(f"Exported mechanism bundle to {output_dir}")
    print(f"nodes={len(nodes)} node_roles={len(node_roles)} edges={len(edges)} edge_sources={len(edge_sources)}")


if __name__ == "__main__":
    main()
