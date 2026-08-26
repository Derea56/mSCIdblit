#!/usr/bin/env python3
"""Build an audit-only staging pack for the remaining Module-B layers.

The pack is deliberately separate from the canonical database and frozen
release. It snapshots the current B registers, extracts the new reviewed-high
promotion candidates for 20B/21B/23B/24B, and validates their evidence links.

Some current edge registers contain a solitary carriage return before a
promotion annotation in the final TSV field. The reader repairs that
formatting in the staging copy only; it does not alter the source register.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "work" / "module_b_consolidation"
PROMOTION_PATH = ROOT / "work" / "promotion_round_2026_08_26" / "high_confidence_promotion_decisions.tsv"
OUT_ROOT = SOURCE_ROOT / "staging_round_2026_08_26"
MODULES = ("20B", "21B", "23B", "24B")


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]], int]:
    """Read a TSV and repair only the known solitary-CR annotation artifact."""

    with path.open("r", newline="", encoding="utf-8", errors="replace") as handle:
        raw = handle.read()
    repaired = raw.replace("\r ", " ")
    repair_count = raw.count("\r ")
    reader = csv.reader(io.StringIO(repaired, newline=""), delimiter="\t")
    try:
        header = next(reader)
    except StopIteration:
        return [], [], repair_count
    rows: list[dict[str, str]] = []
    for line_number, values in enumerate(reader, start=2):
        if len(values) != len(header):
            raise ValueError(f"{path}: line {line_number} has {len(values)} fields; expected {len(header)}")
        rows.append(dict(zip(header, values)))
    return header, rows, repair_count


def write_tsv(path: Path, header: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=header, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in header} for row in rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def truthy(value: str) -> bool:
    return value.strip().casefold() in {"true", "1", "yes"}


def edge_tokens(value: str) -> set[str]:
    return {token.strip() for token in value.split(";") if token.strip()}


def module_dir(module: str) -> Path:
    return SOURCE_ROOT / f"module{module.lower()}"


def sql_identifier(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def write_sql_pack() -> None:
    """Write a loadable SQL script for an isolated staging schema."""

    lines = [
        "-- Module 20B/21B/23B/24B staging round 2026-08-26.",
        "-- Audit-layer only: no canonical tables or frozen releases are touched.",
        "BEGIN;",
        "CREATE SCHEMA IF NOT EXISTS module20_24b_stage_20260826;",
    ]
    for module in MODULES:
        module_key = f"module{module.lower()}"
        stage_dir = OUT_ROOT / module_key
        staged_files = {
            "edge": stage_dir / f"{module_key}_edge_register.tsv",
            "evidence": stage_dir / f"{module_key}_evidence_register.tsv",
            "boundary": stage_dir / f"{module_key}_boundary_register.tsv",
            "consolidation_matrix": stage_dir / f"{module_key}_consolidation_matrix.tsv",
        }
        for kind, path in staged_files.items():
            header, _, _ = read_tsv(path)
            table = f"module20_24b_stage_20260826.{module_key}_{kind}_staging"
            columns = ", ".join(f"{sql_identifier(field)} TEXT" for field in header)
            copy_columns = ", ".join(sql_identifier(field) for field in header)
            relative = path.relative_to(ROOT).as_posix()
            lines.extend([
                f"DROP TABLE IF EXISTS {table};",
                f"CREATE TABLE {table} ({columns});",
                f"\\copy {table} ({copy_columns}) FROM '{relative}' WITH (FORMAT csv, HEADER true, DELIMITER E'\\t', QUOTE '\"', ESCAPE '\"', NULL '');",
            ])
        candidate_path = stage_dir / f"{module_key}_promoted_edge_candidates.tsv"
        evidence_candidate_path = stage_dir / f"{module_key}_promoted_evidence_candidates.tsv"
        for suffix, path in (("promoted_edge_candidates", candidate_path), ("promoted_evidence_candidates", evidence_candidate_path)):
            header, _, _ = read_tsv(path)
            table = f"module20_24b_stage_20260826.{module_key}_{suffix}"
            columns = ", ".join(f"{sql_identifier(field)} TEXT" for field in header)
            copy_columns = ", ".join(sql_identifier(field) for field in header)
            relative = path.relative_to(ROOT).as_posix()
            lines.extend([
                f"DROP TABLE IF EXISTS {table};",
                f"CREATE TABLE {table} ({columns});",
                f"\\copy {table} ({copy_columns}) FROM '{relative}' WITH (FORMAT csv, HEADER true, DELIMITER E'\\t', QUOTE '\"', ESCAPE '\"', NULL '');",
            ])
        lines.append(
            f"DO $$ BEGIN IF (SELECT COUNT(*) FROM module20_24b_stage_20260826.{module_key}_promoted_edge_candidates) = 0 THEN RAISE EXCEPTION 'No staged candidates for {module}'; END IF; END $$;"
        )
    lines.extend([
        "COMMIT;",
        "-- Canonical materialization intentionally not included.",
    ])
    (OUT_ROOT / "module20_24b_staging_round.sql").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    promotion_header, promotions, promotion_repairs = read_tsv(PROMOTION_PATH)
    if promotion_repairs:
        raise ValueError(f"Unexpected formatting artifact in promotion file: {promotion_repairs}")

    manifest: dict[str, object] = {
        "staging_round": "2026-08-26",
        "status": "validated_audit_layer_only",
        "scope": list(MODULES),
        "canonical_database_writes": False,
        "frozen_release_modified": False,
        "source_promotion_file": str(PROMOTION_PATH.relative_to(ROOT)),
        "modules": {},
        "validation_errors": [],
    }
    all_candidate_rows: list[dict[str, str]] = []
    all_candidate_evidence: list[dict[str, str]] = []
    all_summary_rows: list[dict[str, str]] = []

    for module in MODULES:
        source = module_dir(module)
        destination = OUT_ROOT / f"module{module.lower()}"
        destination.mkdir(parents=True, exist_ok=True)
        module_errors: list[str] = []
        source_files = {
            "edge": source / f"module{module.lower()}_edge_register.tsv",
            "evidence": source / f"module{module.lower()}_evidence_register.tsv",
            "boundary": source / f"module{module.lower()}_boundary_register.tsv",
            "consolidation_matrix": source / f"module{module.lower()}_consolidation_matrix.tsv",
        }
        if (source / f"module{module.lower()}_complex_register.tsv").exists():
            source_files["complex"] = source / f"module{module.lower()}_complex_register.tsv"

        parsed: dict[str, tuple[list[str], list[dict[str, str]], int]] = {}
        repair_counts: dict[str, int] = {}
        for kind, path in source_files.items():
            header, rows, repairs = read_tsv(path)
            parsed[kind] = (header, rows, repairs)
            repair_counts[kind] = repairs
            write_tsv(destination / path.name, header, rows)

        edge_header, edge_rows, _ = parsed["edge"]
        evidence_header, evidence_rows, _ = parsed["evidence"]
        edge_by_id = {row.get("b_edge_id", ""): row for row in edge_rows}
        evidence_by_id = {row.get("b_evidence_id", ""): row for row in evidence_rows}
        if len(edge_by_id) != len(edge_rows):
            module_errors.append("duplicate or empty B edge IDs")
        if len(evidence_by_id) != len(evidence_rows):
            module_errors.append("duplicate or empty B evidence IDs")

        module_promotions = [
            row for row in promotions
            if row.get("module_route", "").strip().endswith(f"→{module}")
        ]
        candidate_header = [
            "staging_candidate_id", "module", "b_edge_id", "source_a_edge_id",
            "source_entity", "relation_type", "target_entity", "pathway_name",
            "evidence_layer", "edge_status", "context_scope", "cell_type_context",
            "compartment_context", "species_context", "injury_context",
            "confidence_tier", "export_priority", "exportable", "linked_b_evidence_ids",
            "promotion_primary_pmids", "promotion_corroborating_pmids",
            "exact_evidence_status", "module_fit", "decision", "evidence_summary",
            "limitations", "staging_status", "canonical_entity_role_gate",
        ]
        evidence_candidate_header = [
            "staging_evidence_id", "module", "b_evidence_id", "b_edge_ids",
            "source_a_evidence_id", "source_kind", "source_locator", "support_kind",
            "species_support", "source_scope", "confidence_tier", "citation_note",
            "evidence_summary", "limitations", "evidence_layer", "exportable",
            "promotion_specific", "staging_status",
        ]
        candidate_rows: list[dict[str, str]] = []
        candidate_evidence: list[dict[str, str]] = []
        promotion_evidence_ids: set[str] = set()
        for index, promotion in enumerate(module_promotions, start=1):
            edge_id = promotion.get("edge_or_pair", "").strip()
            edge = edge_by_id.get(edge_id)
            if edge is None:
                module_errors.append(f"promotion references missing edge {edge_id}")
                continue
            linked = [
                evidence for evidence in evidence_rows
                if edge_id in edge_tokens(evidence.get("b_edge_ids", ""))
            ]
            promo_linked = [
                evidence for evidence in linked
                if evidence.get("source_kind", "").strip() == "promotion_round_primary_corroboration"
            ]
            promotion_evidence_ids.update(evidence.get("b_evidence_id", "") for evidence in promo_linked)
            if not promo_linked:
                module_errors.append(f"promoted edge {edge_id} lacks promotion-specific evidence")
            if edge.get("confidence_tier", "").strip().casefold() != "high":
                module_errors.append(f"promoted edge {edge_id} is not high tier")
            if not any(evidence.get("confidence_tier", "").strip().casefold() == "high" for evidence in promo_linked):
                module_errors.append(f"promoted edge {edge_id} lacks high-tier promotion evidence")
            candidate = {
                "staging_candidate_id": f"{module}-STAGE-{index:04d}",
                "module": module,
                "b_edge_id": edge_id,
                "source_a_edge_id": edge.get("source_a_edge_id", ""),
                "source_entity": edge.get("source_entity", ""),
                "relation_type": edge.get("relation_type", ""),
                "target_entity": edge.get("target_entity", ""),
                "pathway_name": edge.get("pathway_name", ""),
                "evidence_layer": edge.get("evidence_layer", ""),
                "edge_status": edge.get("edge_status", ""),
                "context_scope": edge.get("context_scope", ""),
                "cell_type_context": edge.get("cell_type_context", ""),
                "compartment_context": edge.get("compartment_context", ""),
                "species_context": edge.get("species_context", ""),
                "injury_context": edge.get("injury_context", ""),
                "confidence_tier": edge.get("confidence_tier", "").strip(),
                "export_priority": edge.get("export_priority", ""),
                "exportable": edge.get("exportable", ""),
                "linked_b_evidence_ids": ";".join(evidence.get("b_evidence_id", "") for evidence in linked),
                "promotion_primary_pmids": promotion.get("primary_pmids", ""),
                "promotion_corroborating_pmids": promotion.get("corroborating_pmids", ""),
                "exact_evidence_status": promotion.get("exact_evidence_status", ""),
                "module_fit": promotion.get("module_fit", ""),
                "decision": promotion.get("decision", ""),
                "evidence_summary": promotion.get("evidence_summary", ""),
                "limitations": promotion.get("limitations", ""),
                "staging_status": "staged_high_confidence_pending_canonical_review",
                "canonical_entity_role_gate": "pending",
            }
            candidate_rows.append(candidate)
            for evidence in linked:
                candidate_evidence.append({
                    "staging_evidence_id": f"{module}-EVID-STAGE-{len(candidate_evidence) + 1:05d}",
                    "module": module,
                    "b_evidence_id": evidence.get("b_evidence_id", ""),
                    "b_edge_ids": evidence.get("b_edge_ids", ""),
                    "source_a_evidence_id": evidence.get("source_a_evidence_id", ""),
                    "source_kind": evidence.get("source_kind", ""),
                    "source_locator": evidence.get("source_locator", ""),
                    "support_kind": evidence.get("support_kind", ""),
                    "species_support": evidence.get("species_support", ""),
                    "source_scope": evidence.get("source_scope", ""),
                    "confidence_tier": evidence.get("confidence_tier", "").strip(),
                    "citation_note": evidence.get("citation_note", ""),
                    "evidence_summary": evidence.get("evidence_summary", ""),
                    "limitations": evidence.get("limitations", ""),
                    "evidence_layer": evidence.get("evidence_layer", ""),
                    "exportable": evidence.get("exportable", ""),
                    "promotion_specific": "true" if evidence in promo_linked else "false",
                    "staging_status": "staged_high_confidence_pending_canonical_review",
                })

        write_tsv(destination / f"module{module.lower()}_promoted_edge_candidates.tsv", candidate_header, candidate_rows)
        write_tsv(destination / f"module{module.lower()}_promoted_evidence_candidates.tsv", evidence_candidate_header, candidate_evidence)
        all_candidate_rows.extend(candidate_rows)
        all_candidate_evidence.extend(candidate_evidence)

        expected_promotion_count = len(module_promotions)
        promotion_specific_count = sum(
            1 for evidence in evidence_rows
            if evidence.get("source_kind", "").strip() == "promotion_round_primary_corroboration"
        )
        summary = {
            "module": module,
            "edge_rows": str(len(edge_rows)),
            "evidence_rows": str(len(evidence_rows)),
            "boundary_rows": str(len(parsed["boundary"][1])),
            "consolidation_matrix_rows": str(len(parsed["consolidation_matrix"][1])),
            "complex_rows": str(len(parsed.get("complex", ([], [], 0))[1])),
            "exportable_edges": str(sum(truthy(row.get("exportable", "")) for row in edge_rows)),
            "high_edges": str(sum(row.get("confidence_tier", "").strip().casefold() == "high" for row in edge_rows)),
            "promotion_decision_rows": str(expected_promotion_count),
            "promotion_specific_evidence_rows": str(promotion_specific_count),
            "candidate_evidence_rows": str(len(candidate_evidence)),
            "solitary_cr_repairs_in_source": str(sum(repair_counts.values())),
            "validation_status": "pass" if not module_errors else "fail",
            "validation_errors": " | ".join(module_errors),
        }
        all_summary_rows.append(summary)
        manifest["modules"][module] = {  # type: ignore[index]
            **summary,
            "source_register_sha256": {kind: sha256(path) for kind, path in source_files.items()},
            "staging_register_sha256": {
                kind: sha256(destination / path.name) for kind, path in source_files.items()
            },
            "promotion_evidence_ids": sorted(promotion_evidence_ids),
        }
        manifest["validation_errors"].extend(f"{module}: {error}" for error in module_errors)  # type: ignore[union-attr]

    all_candidate_header = list(all_candidate_rows[0].keys()) if all_candidate_rows else []
    all_evidence_header = list(all_candidate_evidence[0].keys()) if all_candidate_evidence else []
    write_tsv(OUT_ROOT / "all_promoted_edge_candidates.tsv", all_candidate_header, all_candidate_rows)
    write_tsv(OUT_ROOT / "all_promoted_evidence_candidates.tsv", all_evidence_header, all_candidate_evidence)
    write_tsv(OUT_ROOT / "module_summary.tsv", list(all_summary_rows[0].keys()), all_summary_rows)
    write_sql_pack()

    manifest["promoted_edge_candidate_rows"] = len(all_candidate_rows)
    manifest["promoted_evidence_candidate_rows"] = len(all_candidate_evidence)
    manifest["promotion_route_counts"] = dict(Counter(row.get("module_route", "") for row in promotions))
    manifest["new_remaining_b_promotions"] = sum(len([row for row in promotions if row.get("module_route", "").strip().endswith(f"→{module}")]) for module in MODULES)
    manifest["source_registers_normalized_only_in_staging_copy"] = True
    manifest["canonical_write_eligibility"] = "false_pending_entity_role_and_canonical_source_gate"
    manifest["status"] = "validated_audit_layer_only" if not manifest["validation_errors"] else "validation_failed"
    (OUT_ROOT / "staging_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({
        "status": manifest["status"],
        "modules": MODULES,
        "promoted_edge_candidate_rows": len(all_candidate_rows),
        "promoted_evidence_candidate_rows": len(all_candidate_evidence),
        "validation_errors": manifest["validation_errors"],
        "output": str(OUT_ROOT.relative_to(ROOT)),
    }, sort_keys=True))
    return 0 if manifest["status"] == "validated_audit_layer_only" else 1


if __name__ == "__main__":
    raise SystemExit(main())
