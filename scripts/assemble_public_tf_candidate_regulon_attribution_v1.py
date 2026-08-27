#!/usr/bin/env python3
"""Assemble staging-only database-attributed regulon records for new TF candidates.

This layer preserves source claims that a database associates a target set with
 a regulator, without treating that association as target-cell presence,
 upstream signaling activation, direct binding, or downstream gene activation.

TFLink is represented at source-set level because the retained GMT snapshot
has a stable source record and target count but no target-level assay, PMID, or
effect metadata. Source-specific pair records are included when they match the
current candidate role triage. All records remain candidate-only and excluded
from canonical Module 22B export.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROLE_TRIAGE = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/public_tf_role_triage.tsv"
)
DEFAULT_TFLINK = ROOT / "data/processed/public_tf_union_expansion_v1/tflink_tf_summary.tsv"
DEFAULT_PAIR_RECORDS = ROOT / "data/processed/public_tf_union_expansion_v1/tf_pair_records.tsv"
DEFAULT_RAW_DIR = ROOT / "data/raw/public_database_snapshots/tf_union_expansion_v1"
DEFAULT_OUTPUT = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1"
)


INDEX_FIELDS = [
    "regulator_key", "display_symbols", "species_scopes", "primary_role_category",
    "role_subcategory", "source_registries", "source_versions", "identity_catalogs",
    "candidate_regulon_status", "regulon_source_count", "regulon_source_registries",
    "regulon_target_count", "pair_record_count", "target_membership_scope",
    "claimed_effect", "target_cell_presence_status", "downstream_activation_status",
    "upstream_relay_status", "module_route", "module22b_eligibility",
    "evidence_readiness", "provenance_note",
]

ATTRIBUTION_FIELDS = [
    "regulator_key", "display_symbols", "species_scope", "primary_role_category",
    "role_subcategory", "source_registry", "source_version", "source_record_id",
    "raw_tf_symbol", "normalized_tf_symbol", "tf_uniprot_id", "target_membership_count",
    "membership_semantics", "claimed_effect", "candidate_regulon_status",
    "target_cell_presence_status", "downstream_activation_status", "upstream_relay_status",
    "module_route", "module22b_eligibility", "source_locator", "source_snapshot",
    "raw_record_sha256", "provenance_status", "source_notes", "reference_pmids",
    "provenance_note",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def numeric(value: str) -> int:
    try:
        return int(value or 0)
    except ValueError:
        return 0


def species_scopes(value: str) -> set[str]:
    return {item.strip() for item in (value or "").split(";") if item.strip()}


def role_route(category: str) -> tuple[str, str]:
    if category in {"catalog_concordant_tf_candidate", "dual_role_tf_chromatin_candidate"}:
        return "22B_candidate_regulon_review", "candidate_membership_export_exclude_pending_exact_evidence"
    if category in {
        "noncanonical_transcriptional_regulator",
        "provisional_nuclear_transcriptional_regulator",
    }:
        return "regulatory_machinery_candidate_program_review", "not_strict_tf_candidate_sidecar_export_exclude"
    if category == "regulon_lead_unclassified":
        return "22B_candidate_regulon_role_review", "not_ready_pending_role_and_exact_pair_review"
    if category in {
        "unresolved_identifier", "alias_or_ingestion_artifact_review", "binding_profile_only",
    }:
        return "identifier_or_profile_review", "not_ready_identity_or_profile_only"
    return "role_specific_candidate_review", "not_strict_tf_pending_role_and_functional_review"


def role_note(row: dict[str, str]) -> str:
    return (
        "Database-attributed regulon membership is retained as a candidate source claim. "
        "It does not establish target-cell presence, upstream relay activation, direct binding, "
        "or downstream gene activation; those evidence layers require separate review. "
        f"Primary role category: {row.get('primary_role_category', '')}."
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--role-triage", type=Path, default=DEFAULT_ROLE_TRIAGE)
    parser.add_argument("--tflink-summary", type=Path, default=DEFAULT_TFLINK)
    parser.add_argument("--pair-records", type=Path, default=DEFAULT_PAIR_RECORDS)
    parser.add_argument("--raw-dir", type=Path, default=DEFAULT_RAW_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    role_rows = read_tsv(args.role_triage)
    role_by_key = {row["regulator_key"]: row for row in role_rows}
    role_species_keys = {
        (species, row["regulator_key"])
        for row in role_rows
        for species in species_scopes(row.get("species_scopes", ""))
        if species in {"human", "mouse"}
    }

    tflink_rows = [
        row for row in read_tsv(args.tflink_summary)
        if (row.get("species_scope", ""), row.get("normalized_tf_symbol_key", "")) in role_species_keys
    ]
    pair_rows = [
        row for row in read_tsv(args.pair_records)
        if (row.get("species_scope", ""), row.get("normalized_tf_symbol_key", "")) in role_species_keys
    ]

    tflink_by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    pair_by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in tflink_rows:
        tflink_by_key[(row["species_scope"], row["normalized_tf_symbol_key"])].append(row)
    for row in pair_rows:
        pair_by_key[(row["species_scope"], row["normalized_tf_symbol_key"])].append(row)

    attribution_rows: list[dict[str, str]] = []
    for source_row in tflink_rows:
        key = source_row["normalized_tf_symbol_key"]
        role = role_by_key[key]
        route, eligibility = role_route(role["primary_role_category"])
        species = source_row["species_scope"]
        raw_snapshot = args.raw_dir / f"tflink_{species}_v1.0.gmt"
        source_snapshot = str(raw_snapshot.relative_to(ROOT)) if raw_snapshot.exists() else str(raw_snapshot)
        attribution_rows.append({
            "regulator_key": key,
            "display_symbols": role.get("display_symbols", ""),
            "species_scope": species,
            "primary_role_category": role.get("primary_role_category", ""),
            "role_subcategory": role.get("role_subcategory", ""),
            "source_registry": source_row.get("source_registry", "TFLink"),
            "source_version": source_row.get("source_version", ""),
            "source_record_id": source_row.get("source_record_id", ""),
            "raw_tf_symbol": source_row.get("raw_tf_symbol", ""),
            "normalized_tf_symbol": source_row.get("normalized_tf_symbol", ""),
            "tf_uniprot_id": source_row.get("tf_uniprot_id", ""),
            "target_membership_count": source_row.get("target_count", "0"),
            "membership_semantics": "aggregated_regulon_set_candidate",
            "claimed_effect": "unknown",
            "candidate_regulon_status": "database_attributed_candidate_regulon_set",
            "target_cell_presence_status": "not_assessed",
            "downstream_activation_status": "not_assessed",
            "upstream_relay_status": "not_assessed",
            "module_route": route,
            "module22b_eligibility": eligibility,
            "source_locator": source_row.get("source_locator", ""),
            "source_snapshot": source_snapshot,
            "raw_record_sha256": source_row.get("raw_record_sha256", ""),
            "provenance_status": source_row.get("provenance_status", ""),
            "source_notes": source_row.get("notes", ""),
            "reference_pmids": "",
            "provenance_note": role_note(role),
        })

    # Keep source-specific pair records separate from set-level TFLink claims.
    # This branch is currently empty for the 2,051 new candidates, but makes
    # the handoff future-proof if an exact new candidate is added to a pair
    # source in a later pinned snapshot.
    for source_row in pair_rows:
        key = source_row["normalized_tf_symbol_key"]
        role = role_by_key[key]
        route, eligibility = role_route(role["primary_role_category"])
        attribution_rows.append({
            "regulator_key": key,
            "display_symbols": role.get("display_symbols", ""),
            "species_scope": source_row.get("species_scope", ""),
            "primary_role_category": role.get("primary_role_category", ""),
            "role_subcategory": role.get("role_subcategory", ""),
            "source_registry": source_row.get("source_registry", ""),
            "source_version": source_row.get("source_version", ""),
            "source_record_id": source_row.get("source_record_id", ""),
            "raw_tf_symbol": source_row.get("raw_tf_symbol", ""),
            "normalized_tf_symbol": source_row.get("normalized_tf_symbol", ""),
            "tf_uniprot_id": "",
            "target_membership_count": "1",
            "membership_semantics": "pair_level_database_regulatory_membership_candidate",
            "claimed_effect": source_row.get("effect_polarity", "unknown"),
            "candidate_regulon_status": "database_attributed_candidate_pair_membership",
            "target_cell_presence_status": "not_assessed",
            "downstream_activation_status": "not_assessed",
            "upstream_relay_status": "not_assessed",
            "module_route": route,
            "module22b_eligibility": eligibility,
            "source_locator": source_row.get("source_locator", ""),
            "source_snapshot": "data/processed/public_tf_union_expansion_v1/tf_pair_records.tsv",
            "raw_record_sha256": source_row.get("raw_record_sha256", ""),
            "provenance_status": source_row.get("provenance_status", ""),
            "source_notes": source_row.get("limitations", ""),
            "reference_pmids": source_row.get("reference_pmids", ""),
            "provenance_note": role_note(role),
        })

    index_rows: list[dict[str, str]] = []
    for role in role_rows:
        key = role["regulator_key"]
        scopes = species_scopes(role.get("species_scopes", ""))
        source_keys = [
            source_key for source_key in tflink_by_key
            if source_key[1] == key and source_key[0] in scopes
        ]
        pair_keys = [
            source_key for source_key in pair_by_key
            if source_key[1] == key and source_key[0] in scopes
        ]
        source_registries = sorted({
            row.get("source_registry", "")
            for source_key in source_keys
            for row in tflink_by_key[source_key]
        } | {
            row.get("source_registry", "")
            for source_key in pair_keys
            for row in pair_by_key[source_key]
        } - {""})
        source_versions = sorted({
            row.get("source_version", "")
            for source_key in source_keys
            for row in tflink_by_key[source_key]
        } | {
            row.get("source_version", "")
            for source_key in pair_keys
            for row in pair_by_key[source_key]
        } - {""})
        target_count = sum(
            numeric(row.get("target_count", "0"))
            for source_key in source_keys
            for row in tflink_by_key[source_key]
        )
        pair_count = sum(len(pair_by_key[source_key]) for source_key in pair_keys)
        has_source = bool(source_keys or pair_keys)
        if has_source:
            status = "database_attributed_regulon_available"
            scope = "aggregated_set_and_or_pair_candidate"
        elif role.get("primary_role_category") == "unresolved_identifier":
            status = "blocked_identifier_mapping_before_regulon_review"
            scope = "none_mapped"
        else:
            status = "no_regulon_set_in_current_imported_sources"
            scope = "none_available_in_current_import"
        route, eligibility = role_route(role["primary_role_category"])
        index_rows.append({
            "regulator_key": key,
            "display_symbols": role.get("display_symbols", ""),
            "species_scopes": role.get("species_scopes", ""),
            "primary_role_category": role.get("primary_role_category", ""),
            "role_subcategory": role.get("role_subcategory", ""),
            "source_registries": role.get("source_registries", ""),
            "source_versions": role.get("source_versions", ""),
            "identity_catalogs": role.get("identity_catalogs", ""),
            "candidate_regulon_status": status,
            "regulon_source_count": str(len(source_keys) + len(pair_keys)),
            "regulon_source_registries": ";".join(source_registries),
            "regulon_target_count": str(target_count),
            "pair_record_count": str(pair_count),
            "target_membership_scope": scope,
            "claimed_effect": "unknown" if not pair_count else "source_specific_pair_effect_preserved",
            "target_cell_presence_status": "not_assessed",
            "downstream_activation_status": "not_assessed",
            "upstream_relay_status": "not_assessed",
            "module_route": route,
            "module22b_eligibility": eligibility,
            "evidence_readiness": (
                "candidate_regulon_set_requires_exact_pair_and_cell_context_review"
                if has_source else "no_imported_regulon_set_or_blocked_identifier"
            ),
            "provenance_note": role_note(role),
        })

    index_rows.sort(key=lambda row: (row["primary_role_category"], row["regulator_key"]))
    attribution_rows.sort(key=lambda row: (row["species_scope"], row["regulator_key"], row["source_record_id"]))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    index_path = args.output_dir / "public_tf_candidate_regulon_index.tsv"
    attribution_path = args.output_dir / "public_tf_candidate_regulon_attribution.tsv"
    write_tsv(index_path, INDEX_FIELDS, index_rows)
    write_tsv(attribution_path, ATTRIBUTION_FIELDS, attribution_rows)

    summary = {
        "status": "staging_only",
        "role_triage_rows": len(role_rows),
        "candidate_index_rows": len(index_rows),
        "attribution_rows": len(attribution_rows),
        "tflink_attribution_rows": len(tflink_rows),
        "source_pair_attribution_rows": len(pair_rows),
        "tflink_target_memberships_reported": sum(numeric(row.get("target_count", "0")) for row in tflink_rows),
        "candidate_regulon_status_counts": dict(sorted(Counter(row["candidate_regulon_status"] for row in index_rows).items())),
        "attribution_source_counts": dict(sorted(Counter(row["source_registry"] for row in attribution_rows).items())),
        "attribution_role_category_counts": dict(sorted(Counter(row["primary_role_category"] for row in attribution_rows).items())),
        "claimed_effect_counts": dict(sorted(Counter(row["claimed_effect"] for row in attribution_rows).items())),
        "target_cell_presence_status": "not_assessed_for_all_rows",
        "downstream_activation_status": "not_assessed_for_all_rows",
        "upstream_relay_status": "not_assessed_for_all_rows",
        "canonical_writes_performed": False,
        "module22b_promotions_performed": False,
        "policy": {
            "database_attribution": "preserved as candidate regulon or pair membership, source-specific and export-excluded",
            "tflink": "set-level target membership is retained by source record and raw snapshot hash; no target-level assay or PMID is inferred",
            "activation": "candidate membership does not establish target-cell presence, upstream relay activation, or downstream gene activation",
            "noncanonical": "chromatin/cofactor candidates route to a regulatory-machinery sidecar rather than strict TF role promotion",
            "species": "human and mouse remain separate",
        },
        "inputs": {
            "role_triage": str(args.role_triage.relative_to(ROOT)),
            "tflink_summary": str(args.tflink_summary.relative_to(ROOT)),
            "pair_records": str(args.pair_records.relative_to(ROOT)),
        },
        "raw_snapshots": {
            species: {
                "path": str((args.raw_dir / f"tflink_{species}_v1.0.gmt").relative_to(ROOT)),
                "sha256": sha256(args.raw_dir / f"tflink_{species}_v1.0.gmt"),
            }
            for species in ("human", "mouse")
            if (args.raw_dir / f"tflink_{species}_v1.0.gmt").exists()
        },
        "outputs": [str(index_path.relative_to(ROOT)), str(attribution_path.relative_to(ROOT))],
    }
    summary_path = args.output_dir / "public_tf_candidate_regulon_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
