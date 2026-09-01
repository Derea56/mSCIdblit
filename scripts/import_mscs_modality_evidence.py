#!/usr/bin/env python3
"""Import exact mSCS modality observations into an mSCIdblit bridge bundle.

The importer reads the mSCS SQLite stores and emits TSV audit manifests plus
idempotent PostgreSQL SQL. It does not alter mSCS, invent identifiers, create
local Paper/Observation rows, or promote mechanism edges. External source keys
remain the mSCS keys; local detail keys are documented locators only for
derived spatial-pilot rows.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sqlite3
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MSCS_ROOT = ROOT.parent / "mSCS"
DEFAULT_OUTPUT = ROOT / "data" / "processed" / "mscs_modality_evidence_import_v1"
SPATIAL_PILOT = (
    "data/spatial/pilot_all_studies/gse269377_cluster_proxy/"
    "spatial_pair_percentages_all_samples.tsv"
)


SOURCE_FIELDS = [
    "source_system", "source_database", "source_record_type", "source_record_key",
    "source_version", "modality", "assay", "source_artifact_path",
    "source_artifact_sha256", "source_locator", "source_url", "source_status",
    "provenance_note", "source_metadata_json",
]

DETAIL_FIELDS = [
    "source_database", "source_record_type", "source_record_key", "source_version",
    "source_detail_key", "local_paper_id",
    "local_experiment_id", "local_observation_id", "local_claim_id",
    "reported_entity_name", "reported_entity_type", "measurement_kind", "assay",
    "protein_form", "feature_type", "feature_id", "reported_value_numeric",
    "reported_value_text", "reported_value_kind", "native_value_numeric",
    "transcribed_value_numeric", "transcribed_value_text", "transcribed_value_sem",
    "transcribed_value_sd", "transcribed_value_lower", "transcribed_value_upper",
    "unit", "direction_vs_control", "comparator", "sample_count",
    "biological_replicates", "technical_replicates", "timepoint_value",
    "timepoint_unit", "condition", "tissue_context", "cell_context", "sample_scope",
    "normalization", "negative_evidence_status", "source_evidence_label",
    "evidence_grade", "context_level", "measurement_status", "source_field_locator",
    "raw_observation_text", "normalization_notes", "native_fields_json",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def connect(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    return connection


def json_text(value: Any) -> str:
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return json.dumps({"raw_value": value}, ensure_ascii=False, sort_keys=True)
        return json.dumps(parsed, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def numeric_or_none(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def protein_grade(label: str | None) -> str | None:
    """Map only the explicit mSCS protein grade prefixes to ABC."""
    if not label:
        return None
    prefix = label.split("_", 1)[0]
    return prefix if prefix in {"A", "B", "C", "D", "E", "U"} else None


def row_json(row: sqlite3.Row, joined: dict[str, Any]) -> str:
    payload = {key: row[key] for key in row.keys()}
    payload.update(joined)
    return json_text(payload)


def sql(value: Any) -> str:
    if value is None or value == "":
        return "NULL"
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if isinstance(value, (int, float)):
        return str(value)
    return "'" + str(value).replace("'", "''") + "'"


def write_tsv(path: Path, fields: list[str], rows: Iterable[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: "" if row.get(field) is None else row.get(field, "") for field in fields} for row in rows)


def protein_import(mscs_root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    db_path = mscs_root / "data/flow_protein/flow_protein.sqlite"
    db_hash = sha256(db_path)
    sources: list[dict[str, Any]] = []
    details: list[dict[str, Any]] = []
    with connect(db_path) as db:
        query = """
        SELECT po.*, ec.evidence_id, ec.claim_type, ec.estimand, ec.inference_role,
               ec.missingness_status, ec.negative_evidence_status AS claim_negative_status,
               ec.evidence_status AS claim_evidence_status, ec.source_artifact_hash,
               ec.raw_fields_json, st.title AS study_title, st.doi_or_pmid,
               st.source_url AS study_source_url, st.organism, st.injury_model,
               st.acute_relevance, cp.reported_label AS population_label,
               cp.normalized_label AS population_normalized_label,
               tp.post_injury_value, tp.unit AS timepoint_unit, tp.condition,
               tp.tissue_region, src.source_location, src.source_url AS source_url,
               src.repository_accession, src.recoverability, src.source_hash
        FROM protein_observations po
        JOIN evidence_claims ec ON ec.observation_id = po.observation_id
        LEFT JOIN studies st ON st.study_id = po.study_id
        LEFT JOIN cell_populations cp ON cp.population_id = po.population_id
        LEFT JOIN study_timepoints tp ON tp.timepoint_id = po.timepoint_id
        LEFT JOIN sources src ON src.source_id = po.source_id
        ORDER BY po.observation_id
        """
        for row in db.execute(query):
            claim_status = row["claim_evidence_status"] or "candidate"
            source_key = row["observation_id"]
            source_metadata = {
                "study_id": row["study_id"], "study_title": row["study_title"],
                "doi_or_pmid": row["doi_or_pmid"], "organism": row["organism"],
                "injury_model": row["injury_model"], "acute_relevance": row["acute_relevance"],
                "population_id": row["population_id"], "population_label": row["population_label"],
                "timepoint_id": row["timepoint_id"], "post_injury_value": row["post_injury_value"],
                "timepoint_unit": row["timepoint_unit"], "condition": row["condition"],
                "tissue_region": row["tissue_region"], "evidence_id": row["evidence_id"],
                "claim_type": row["claim_type"], "estimand": row["estimand"],
                "inference_role": row["inference_role"], "missingness_status": row["missingness_status"],
                "claim_evidence_status": claim_status,
            }
            sources.append({
                "source_system": "mSCS", "source_database": "flow_protein",
                "source_record_type": "protein_observation", "source_record_key": source_key,
                "source_version": f"sha256:{db_hash}", "modality": "protein",
                "assay": row["assay"], "source_artifact_path": f"mSCS/data/flow_protein/flow_protein.sqlite",
                "source_artifact_sha256": db_hash,
                "source_locator": row["source_location"] or row["source_artifact"] or None,
                "source_url": row["source_url"] or row["study_source_url"],
                "source_status": "verified" if claim_status == "supported" else "candidate",
                "provenance_note": f"Exact mSCS flow_protein protein_observations.observation_id={source_key}; source status follows evidence_claims.evidence_status={claim_status}.",
                "source_metadata_json": json_text(source_metadata),
            })
            native_numeric = numeric_or_none(row["value"])
            transcribed_numeric = numeric_or_none(row["transcribed_value_numeric"])
            reported_numeric = native_numeric if native_numeric is not None else transcribed_numeric
            reported_kind = "source_native" if native_numeric is not None else (
                "source_transcribed" if transcribed_numeric is not None or row["transcribed_value_text"] else "unknown"
            )
            measurement_status = "reported" if native_numeric is not None else (
                "transcribed" if transcribed_numeric is not None or row["transcribed_value_text"] else (
                    "qualitative" if row["measurement_kind"] else "unknown"
                )
            )
            joined = {
                "study_title": row["study_title"], "doi_or_pmid": row["doi_or_pmid"],
                "injury_model": row["injury_model"], "population_label": row["population_label"],
                "population_normalized_label": row["population_normalized_label"],
                "timepoint_value": numeric_or_none(row["post_injury_value"]), "timepoint_unit": row["timepoint_unit"],
                "condition": row["condition"], "tissue_region": row["tissue_region"],
                "claim_evidence_status": claim_status, "claim_raw_fields_json": row["raw_fields_json"],
            }
            details.append({
                "source_database": "flow_protein", "source_record_key": source_key,
                "source_detail_key": source_key, "reported_entity_name": row["gene_symbol"] or row["protein"],
                "reported_entity_type": "protein", "measurement_kind": row["measurement_kind"],
                "assay": row["assay"], "protein_form": row["protein_form"],
                "reported_value_numeric": reported_numeric, "reported_value_text": row["transcribed_value_text"],
                "reported_value_kind": reported_kind, "native_value_numeric": native_numeric,
                "transcribed_value_numeric": transcribed_numeric, "transcribed_value_text": row["transcribed_value_text"],
                "transcribed_value_sem": numeric_or_none(row["transcribed_value_sem"]), "transcribed_value_sd": numeric_or_none(row["transcribed_value_sd"]),
                "transcribed_value_lower": numeric_or_none(row["transcribed_value_lower"]), "transcribed_value_upper": numeric_or_none(row["transcribed_value_upper"]),
                "unit": row["unit"], "direction_vs_control": row["direction_vs_control"],
                "biological_replicates": numeric_or_none(row["biological_replicates"]), "technical_replicates": numeric_or_none(row["technical_replicates"]),
                "timepoint_value": numeric_or_none(row["post_injury_value"]), "timepoint_unit": row["timepoint_unit"],
                "condition": row["condition"], "tissue_context": row["tissue_region"],
                "cell_context": row["population_label"], "sample_scope": row["sample_scope"],
                "normalization": row["normalization"], "negative_evidence_status": row["negative_evidence_status"],
                "source_evidence_label": row["evidence_grade"], "evidence_grade": protein_grade(row["evidence_grade"]),
                "measurement_status": measurement_status,
                "source_field_locator": f"flow_protein.protein_observations.observation_id={source_key}",
                "normalization_notes": row["measurement_quality"],
                "native_fields_json": row_json(row, joined),
            })
    return sources, details, {"database": "flow_protein", "database_path": "mSCS/data/flow_protein/flow_protein.sqlite", "database_sha256": db_hash, "source_count": len(sources), "detail_count": len(details)}


def epigenetic_import(mscs_root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    db_path = mscs_root / "data/epigenetic/epigenetic.sqlite"
    db_hash = sha256(db_path)
    sources: list[dict[str, Any]] = []
    details: list[dict[str, Any]] = []
    with connect(db_path) as db:
        query = """
        SELECT o.*, a.assay_name, a.epigenetic_class, a.target AS assay_target,
               a.directness, a.evidence_scope, a.evidence_level, a.source_id AS assay_source_id,
               c.condition, c.post_injury_value, c.post_injury_unit, c.tissue,
               c.tissue_region, c.cell_type, c.replicate_count,
               s.study_id, s.title AS study_title, s.pmid, s.doi, s.source_url AS study_source_url,
               s.curation_status, src.source_location, src.source_url, src.source_hash
        FROM observations o
        JOIN assays a ON a.assay_id = o.assay_id
        LEFT JOIN assay_contexts c ON c.context_id = o.context_id
        LEFT JOIN sources src ON src.source_id = o.source_id
        LEFT JOIN studies s ON s.study_id = a.study_id
        ORDER BY o.observation_id
        """
        for row in db.execute(query):
            observation_status = row["evidence_status"] or "candidate"
            source_status = "verified" if observation_status == "supported" and row["curation_status"] == "verified" else "candidate"
            source_key = row["observation_id"]
            source_metadata = {
                "study_id": row["study_id"], "study_title": row["study_title"], "pmid": row["pmid"],
                "doi": row["doi"], "curation_status": row["curation_status"], "assay_id": row["assay_id"],
                "context_id": row["context_id"], "feature_type": row["feature_type"],
                "feature_id": row["feature_id"], "evidence_status": observation_status,
            }
            sources.append({
                "source_system": "mSCS", "source_database": "epigenetic",
                "source_record_type": "epigenetic_observation", "source_record_key": source_key,
                "source_version": f"sha256:{db_hash}", "modality": "epigenomics",
                "assay": row["assay_name"], "source_artifact_path": "mSCS/data/epigenetic/epigenetic.sqlite",
                "source_artifact_sha256": db_hash,
                "source_locator": row["source_location"] or None,
                "source_url": row["source_url"] or row["study_source_url"],
                "source_status": source_status,
                "provenance_note": f"Exact mSCS epigenetic observations.observation_id={source_key}; status follows observation evidence_status={observation_status} and study curation_status={row['curation_status']}.",
                "source_metadata_json": json_text(source_metadata),
            })
            joined = {
                "study_title": row["study_title"], "pmid": row["pmid"], "doi": row["doi"],
                "curation_status": row["curation_status"], "assay_id": row["assay_id"],
                "epigenetic_class": row["epigenetic_class"], "directness": row["directness"],
                "evidence_scope": row["evidence_scope"], "evidence_level": row["evidence_level"],
                "assay_target": row["assay_target"], "context_id": row["context_id"],
                "condition": row["condition"], "post_injury_value": row["post_injury_value"],
                "post_injury_unit": row["post_injury_unit"], "tissue": row["tissue"],
                "tissue_region": row["tissue_region"], "cell_type": row["cell_type"],
                "replicate_count": row["replicate_count"],
            }
            details.append({
                "source_database": "epigenetic", "source_record_key": source_key,
                "source_detail_key": source_key, "reported_entity_name": row["gene_symbol"] or row["target"],
                "reported_entity_type": row["feature_type"], "measurement_kind": row["measurement_kind"],
                "assay": row["assay_name"], "feature_type": row["feature_type"],
                "feature_id": row["feature_id"], "reported_value_numeric": numeric_or_none(row["effect_value"]),
                "reported_value_kind": "source_native" if numeric_or_none(row["effect_value"]) is not None else "unknown",
                "unit": row["effect_unit"], "direction_vs_control": row["direction_vs_control"],
                "biological_replicates": numeric_or_none(row["replicate_count"]), "timepoint_value": numeric_or_none(row["post_injury_value"]),
                "timepoint_unit": row["post_injury_unit"], "condition": row["condition"],
                "tissue_context": row["tissue_region"] or row["tissue"], "cell_context": row["cell_type"],
                "source_evidence_label": f"{row['epigenetic_class']}:{row['directness']}:{row['evidence_level']}",
                "measurement_status": "reported" if row["effect_value"] is not None else "qualitative",
                "source_field_locator": f"epigenetic.observations.observation_id={source_key}",
                "raw_observation_text": row["notes"], "native_fields_json": row_json(row, joined),
            })
    return sources, details, {"database": "epigenetic", "database_path": "mSCS/data/epigenetic/epigenetic.sqlite", "database_sha256": db_hash, "source_count": len(sources), "detail_count": len(details)}


def spatial_import(mscs_root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    db_path = mscs_root / "data/spatial/spatial_catalog.sqlite"
    db_hash = sha256(db_path)
    sources: list[dict[str, Any]] = []
    details: list[dict[str, Any]] = []
    with connect(db_path) as db:
        rows = db.execute("SELECT * FROM datasets ORDER BY dataset_id").fetchall()
    for row in rows:
        source_key = row["dataset_id"]
        metadata = {key: row[key] for key in row.keys()}
        sources.append({
            "source_system": "mSCS", "source_database": "spatial_catalog",
            "source_record_type": "spatial_dataset", "source_record_key": source_key,
            "source_version": f"sha256:{db_hash}", "modality": "spatial_transcriptomics",
            "assay": row["assay_family"], "source_artifact_path": "mSCS/data/spatial/spatial_catalog.sqlite",
            "source_artifact_sha256": db_hash, "source_locator": row["source_manifest"],
            "source_url": None, "source_status": "candidate",
            "provenance_note": f"Exact mSCS spatial_catalog.datasets.dataset_id={source_key}; catalog/pilot source only, not route evidence.",
            "source_metadata_json": json_text(metadata),
        })
    pilot_path = mscs_root / SPATIAL_PILOT
    pilot_hash = sha256(pilot_path)
    with pilot_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for line_number, row in enumerate(reader, start=2):
            source_key = row["dataset_id"]
            focal = row["focal_cell_type"]
            partner = row["partner_cell_type"]
            detail_key = f"pilot_line:{line_number}"
            native = dict(row)
            numeric = numeric_or_none(row.get("same_spot_weighted_pct"))
            details.append({
                "source_database": "spatial_catalog", "source_record_key": source_key,
                "source_detail_key": detail_key, "reported_entity_name": f"{focal}->{partner}",
                "reported_entity_type": "provisional_spatial_cluster_pair",
                "measurement_kind": "spatial_pair_proximity_summary", "reported_value_numeric": numeric,
                "reported_value_kind": "derived_pilot_metric", "unit": "percent",
                "direction_vs_control": "not_reported", "timepoint_unit": None,
                "cell_context": f"provisional focal cluster {focal}; provisional partner cluster {partner}",
                "measurement_status": "derived_pilot",
                "source_field_locator": f"mSCS/{SPATIAL_PILOT}:line={line_number};sample_id={row['sample_id']};focal_cell_type={focal};partner_cell_type={partner}",
                "normalization_notes": "Provisional Leiden cluster labels; spatial proximity is descriptive and not a molecular interaction or causal route claim.",
                "native_fields_json": json_text(native),
            })
    return sources, details, {"database": "spatial_catalog", "database_path": "mSCS/data/spatial/spatial_catalog.sqlite", "database_sha256": db_hash, "pilot_path": f"mSCS/{SPATIAL_PILOT}", "pilot_sha256": pilot_hash, "source_count": len(sources), "detail_count": len(details), "spatial_evidence_table_rows": 0}


def source_selector(row: dict[str, Any]) -> str:
    return (
        "(SELECT source_record_id FROM EvidenceSourceRecord WHERE "
        f"source_system={sql('mSCS')} AND source_database={sql(row['source_database'])} "
        f"AND source_record_type={sql(row.get('source_record_type'))} "
        f"AND source_record_key={sql(row['source_record_key'])} "
        f"AND source_version={sql(row['source_version'])})"
    )


def detail_sql(row: dict[str, Any]) -> str:
    fields = [
        "source_record_id", "source_detail_key", "reported_entity_name", "reported_entity_type",
        "measurement_kind", "assay", "protein_form", "feature_type", "feature_id",
        "reported_value_numeric", "reported_value_text", "reported_value_kind",
        "native_value_numeric", "transcribed_value_numeric", "transcribed_value_text",
        "transcribed_value_sem", "transcribed_value_sd", "transcribed_value_lower",
        "transcribed_value_upper", "unit", "direction_vs_control", "comparator", "sample_count",
        "biological_replicates", "technical_replicates", "timepoint_value", "timepoint_unit",
        "condition", "tissue_context", "cell_context", "sample_scope", "normalization",
        "negative_evidence_status", "source_evidence_label", "evidence_grade", "context_level",
        "measurement_status", "source_field_locator", "raw_observation_text", "normalization_notes",
        "native_fields_json",
    ]
    values = [f"{source_selector(row)}" if field == "source_record_id" else sql(row.get(field)) for field in fields]
    assignments = ", ".join(f"{field}=EXCLUDED.{field}" for field in fields if field not in {"source_record_id", "source_detail_key"})
    return (
        "INSERT INTO EvidenceObservationDetail (" + ", ".join(fields) + ") SELECT "
        + ", ".join(values)
        + " ON CONFLICT (source_record_id, source_detail_key) DO UPDATE SET "
        + assignments + ";"
    )


def build(mscs_root: Path, output: Path) -> dict[str, Any]:
    protein_sources, protein_details, protein_manifest = protein_import(mscs_root)
    epi_sources, epi_details, epi_manifest = epigenetic_import(mscs_root)
    spatial_sources, spatial_details, spatial_manifest = spatial_import(mscs_root)
    sources = protein_sources + epi_sources + spatial_sources
    details = protein_details + epi_details + spatial_details
    source_type_by_database = {
        "flow_protein": "protein_observation",
        "epigenetic": "epigenetic_observation",
        "spatial_catalog": "spatial_dataset",
    }
    for row in sources:
        row["source_record_type"] = source_type_by_database[row["source_database"]]
    source_lookup = {
        (row["source_database"], row["source_record_key"]): row for row in sources
    }
    for row in details:
        source = source_lookup[(row["source_database"], row["source_record_key"])]
        row["source_record_type"] = source["source_record_type"]
        row["source_version"] = source["source_version"]
    output.mkdir(parents=True, exist_ok=True)
    write_tsv(output / "evidence_source_records.tsv", SOURCE_FIELDS, sources)
    write_tsv(output / "evidence_observation_details.tsv", DETAIL_FIELDS, details)
    sql_lines = [
        "-- Generated by scripts/import_mscs_modality_evidence.py.",
        "-- mSCS remains authoritative; these rows are a provenance-linked projection.",
        "BEGIN;", "",
    ]
    source_columns = [
        "source_system", "source_database", "source_record_type", "source_record_key",
        "source_version", "modality", "assay", "source_artifact_path", "source_artifact_sha256",
        "source_locator", "source_url", "source_status", "provenance_note", "source_metadata_json",
    ]
    for row in sources:
        values = ", ".join(sql(row.get(field)) for field in source_columns)
        updates = ", ".join(f"{field}=EXCLUDED.{field}" for field in source_columns if field not in {"source_system", "source_database", "source_record_type", "source_record_key", "source_version"})
        sql_lines.append(
            "INSERT INTO EvidenceSourceRecord (" + ", ".join(source_columns) + ") VALUES (" + values + ") "
            "ON CONFLICT (source_system, source_database, source_record_type, source_record_key, source_version) DO UPDATE SET " + updates + ";"
        )
    for row in details:
        sql_lines.append(detail_sql(row))
    sql_lines.extend(["", "COMMIT;", ""])
    (output / "mscs_modality_evidence_materialization.sql").write_text("\n".join(sql_lines), encoding="utf-8")
    manifest = {
        "import_version": "mscs_modality_evidence_import_v1",
        "source_repository": "mSCS",
        "source_root": str(mscs_root),
        "source_records": len(sources),
        "observation_details": len(details),
        "by_modality": {
            "protein": protein_manifest,
            "epigenomics": epi_manifest,
            "spatial": spatial_manifest,
        },
        "module_links_created": 0,
        "local_paper_observation_claim_anchors_created": 0,
        "canonical_edge_promotions": 0,
        "notes": [
            "Protein and epigenetic records retain exact source observation IDs.",
            "Spatial pilot metrics use source-field locators and remain derived_pilot; mSCS spatial_evidence currently has zero rows.",
            "ABC mappings are only emitted for explicit mSCS protein grade prefixes; context_level remains NULL pending explicit adjudication.",
            "No mSCS files or SQLite databases were modified by this importer.",
        ],
        "outputs": [
            "evidence_source_records.tsv",
            "evidence_observation_details.tsv",
            "mscs_modality_evidence_materialization.sql",
        ],
    }
    (output / "import_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mscs-root", type=Path, default=DEFAULT_MSCS_ROOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    manifest = build(args.mscs_root, args.output)
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
