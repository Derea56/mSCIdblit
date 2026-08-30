#!/usr/bin/env python3
"""Audit TFLink/GTRD source chains for C-tier exact-pair L0 records.

This is a provenance audit only.  It does not promote context and does not
write any canonical, module, SQLite, or release artifact.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROMOTIONS = (
    ROOT
    / "data/processed/public_tf_union_expansion_v1/"
    "comprehensive_interaction_promotion_v1/promoted_interactions.tsv"
)
DEFAULT_CONTEXT = (
    ROOT
    / "data/processed/public_tf_union_expansion_v1/"
    "comprehensive_interaction_promotion_v1/module_integration_staging_v1/"
    "context_evidence_adjudications.tsv"
)
DEFAULT_OUTPUT = (
    ROOT
    / "data/processed/public_tf_union_expansion_v1/"
    "comprehensive_interaction_promotion_v1/module_integration_staging_v1/"
    "c_tier_exact_pair_source_chain_audit.tsv"
)

FIELDS = [
    "promotion_id",
    "regulator_symbol",
    "target_symbol",
    "species_scope",
    "context_level_exact_pair",
    "source_registry",
    "source_record_id",
    "source_database",
    "detection_method",
    "pubmed_id",
    "small_scale_evidence",
    "tflink_source_url",
    "raw_snapshot_path",
    "raw_snapshot_sha256",
    "snapshot_exists",
    "snapshot_sha256_match",
    "snapshot_row_regulator_match",
    "snapshot_row_target_match",
    "snapshot_row_organism_match",
    "snapshot_row_source_match",
    "source_chain_status",
    "audit_basis",
]


def norm(value: str) -> str:
    return "".join((value or "").casefold().split())


def symbol_options(value: str) -> set[str]:
    return {
        norm(part)
        for slash_part in (value or "").split("/")
        for part in slash_part.split(";")
        if part.strip()
    }


def compound_contains(expected: str, observed: str) -> bool:
    """Return true when one observed source token is in a compound field."""
    expected_tokens = {norm(token) for token in (expected or "").split(";") if token}
    observed_tokens = {norm(token) for token in (observed or "").split(";") if token}
    return bool(expected_tokens & observed_tokens)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def snapshot_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--promotions", type=Path, default=DEFAULT_PROMOTIONS)
    parser.add_argument("--context", type=Path, default=DEFAULT_CONTEXT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    with args.promotions.open(newline="", encoding="utf-8") as handle:
        promotions = {
            row["promotion_id"]: row
            for row in csv.DictReader(handle, delimiter="\t")
            if row.get("evidence_weight_tier", "").startswith("C_")
        }
    with args.context.open(newline="", encoding="utf-8") as handle:
        context = {
            row["promotion_id"]: row
            for row in csv.DictReader(handle, delimiter="\t")
            if row.get("evidence_weight_tier", "").startswith("C_")
            and row.get("context_level_exact_pair", "").startswith("L0_")
        }

    output_rows: list[dict[str, str]] = []
    snapshot_cache: dict[Path, list[dict[str, str]]] = {}
    hash_cache: dict[Path, str] = {}

    for promotion_id in sorted(context, key=lambda value: int(value.rsplit("_", 1)[1])):
        adjudication = context[promotion_id]
        source = promotions.get(promotion_id)
        result = {field: "" for field in FIELDS}
        result.update(
            {
                "promotion_id": promotion_id,
                "regulator_symbol": adjudication.get("regulator_symbol", ""),
                "target_symbol": adjudication.get("target_symbol", ""),
                "species_scope": adjudication.get("species_scope", ""),
                "context_level_exact_pair": adjudication.get(
                    "context_level_exact_pair", ""
                ),
            }
        )

        if source is None:
            result["source_chain_status"] = "missing_promotion_source_row"
            result["audit_basis"] = "C-tier context row has no matching promotion row"
            output_rows.append(result)
            continue

        for output_field, source_field in (
            ("source_registry", "source_registry"),
            ("source_record_id", "source_record_id"),
            ("source_database", "tflink_source_database"),
            ("detection_method", "tflink_detection_method"),
            ("pubmed_id", "tflink_pubmed_id"),
            ("small_scale_evidence", "tflink_small_scale_evidence"),
            ("tflink_source_url", "tflink_source_url"),
            ("raw_snapshot_path", "tflink_raw_snapshot_path"),
            ("raw_snapshot_sha256", "tflink_raw_snapshot_sha256"),
        ):
            result[output_field] = source.get(source_field, "")

        raw_path = ROOT / source.get("tflink_raw_snapshot_path", "")
        exists = raw_path.is_file()
        result["snapshot_exists"] = str(exists).lower()
        if not exists:
            result["source_chain_status"] = "missing_raw_snapshot"
            result["audit_basis"] = "TFLink metadata is present but cited raw snapshot is missing"
            output_rows.append(result)
            continue

        if raw_path not in hash_cache:
            hash_cache[raw_path] = sha256(raw_path)
        result["snapshot_sha256_match"] = str(
            hash_cache[raw_path] == source.get("tflink_raw_snapshot_sha256", "")
        ).lower()

        if raw_path not in snapshot_cache:
            snapshot_cache[raw_path] = snapshot_rows(raw_path)
        rows = snapshot_cache[raw_path]
        tf_options = symbol_options(source.get("raw_tf_symbol", ""))
        if not tf_options:
            tf_options = symbol_options(adjudication.get("regulator_symbol", ""))
        target = norm(adjudication.get("target_symbol", ""))
        species = norm(adjudication.get("species_scope", ""))
        expected_organism = {
            "human": norm("Homo sapiens"),
            "mouse": norm("Mus musculus"),
        }.get(species, "")
        source_db = norm(source.get("tflink_source_database", ""))
        detection = norm(source.get("tflink_detection_method", ""))
        pubmed = norm(source.get("tflink_pubmed_id", ""))

        matching = [
            row
            for row in rows
            if symbol_options(row.get("Name.TF", "")) & tf_options
            and target in symbol_options(row.get("Name.Target", ""))
        ]
        result["snapshot_row_regulator_match"] = str(bool(matching)).lower()
        result["snapshot_row_target_match"] = str(bool(matching)).lower()
        result["snapshot_row_organism_match"] = str(
            any(
                expected_organism
                and norm(row.get("Organism", "")) == expected_organism
                for row in matching
            )
        ).lower()
        result["snapshot_row_source_match"] = str(
            any(
                compound_contains(source.get("tflink_source_database", ""), row.get("Source.database", ""))
                and compound_contains(source.get("tflink_detection_method", ""), row.get("Detection.method", ""))
                and compound_contains(source.get("tflink_pubmed_id", ""), row.get("PubmedID", ""))
                for row in matching
            )
        ).lower()

        checks = [
            result["snapshot_sha256_match"] == "true",
            result["snapshot_row_regulator_match"] == "true",
            result["snapshot_row_target_match"] == "true",
            result["snapshot_row_organism_match"] == "true",
            result["snapshot_row_source_match"] == "true",
        ]
        result["source_chain_status"] = (
            "verified_tflink_gtrd_snapshot_pair" if all(checks) else "source_chain_mismatch"
        )
        result["audit_basis"] = (
            "Exact C-tier pair matched to the species-specific TFLink raw snapshot; "
            "snapshot checksum and GTRD metadata were checked. This verifies provenance "
            "only and does not establish context or causality."
        )
        output_rows.append(result)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"wrote {len(output_rows)} exact-pair source-chain audits to {args.output}")


if __name__ == "__main__":
    main()
