#!/usr/bin/env python3
"""Materialize source-verified general TF->target edges for Module 22B.

The source curation already contains exact primary-reference verification for
these pairs.  This batch adds the standalone TF-regulon assertion to the
Module 22B register; it does not claim that the associated ligand/receptor
route activates the TF in SCI.  Upstream route evidence remains separately
qualified on the existing signaling rows.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
SOURCE_PATH = ROOT / (
    "data/processed/public_tf_union_v1/module_curation/agent_materialized/"
    "priority_tf_agent_promoted.tsv"
)
AUDIT_PATH = ROOT / (
    "work/module22b_tf_regulon_promotion_audit/"
    "module22b_general_tf_regulon_promotion_batch001.tsv"
)
SUMMARY_PATH = ROOT / (
    "work/module22b_tf_regulon_promotion_audit/"
    "module22b_general_tf_regulon_promotion_batch001_summary.json"
)
BATCH_ID = "module22b-general-tf-regulon-promotion-batch001-2026-09-03"

EDGE_FIELDS = [
    "b_edge_id", "source_entity", "relation_type", "target_entity",
    "pathway_name", "evidence_layer", "source_a_edge_id", "edge_status",
    "context_scope", "cell_type_context", "compartment_context",
    "species_context", "injury_context", "confidence_tier", "export_priority",
    "exportable", "consolidation_note",
]
EVIDENCE_FIELDS = [
    "b_evidence_id", "source_a_evidence_id", "b_edge_ids", "source_kind",
    "source_locator", "support_kind", "species_support", "source_scope",
    "confidence_tier", "citation_note", "evidence_summary", "limitations",
    "evidence_layer", "exportable", "consolidation_note",
]
AUDIT_FIELDS = [
    "batch_id", "curation_id", "species", "tf_symbol", "target_symbol",
    "b_edge_id", "b_evidence_id", "old_edge_count", "new_edge_status",
    "new_edge_confidence", "new_evidence_confidence", "effect_polarity",
    "support_kind", "evidence_scope", "primary_pmids", "corroborating_pmids",
    "external_record_keys", "source_registries", "cell_type_context",
    "module22b_register_changed", "upstream_sci_activation_claim",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def next_numeric_id(rows: list[dict[str, str]], field: str) -> int:
    values = []
    for row in rows:
        match = re.search(r"(\d+)$", row[field])
        if match:
            values.append(int(match.group(1)))
    return max(values, default=0) + 1


def split_values(value: str) -> list[str]:
    return [item for item in (value or "").split(";") if item and item != r"\N"]


def relation_text(row: dict[str, str]) -> str:
    tf = row["tf_symbol"]
    target = row["target_symbol"]
    effect = row["effect_polarity"]
    support = row["support_kind"]
    if "cooperative" in support:
        verb = "participates in cooperative activation of"
    elif effect == "activating_target":
        verb = "activates"
    elif effect == "repressing_target":
        verb = "represses"
    else:
        verb = "regulates"
    return f"{tf} {verb} the {target} target gene in source-verified general regulatory evidence"


def main() -> int:
    edges = read_tsv(EDGE_PATH)
    evidence = read_tsv(EVIDENCE_PATH)
    source_rows = read_tsv(SOURCE_PATH)

    if not source_rows:
        raise SystemExit("no source-verified TF-regulon rows found")
    expected = {row["curation_id"] for row in source_rows}
    existing_source_ids = {row["source_a_edge_id"] for row in edges}
    overlap = expected & existing_source_ids
    if overlap:
        raise SystemExit(f"batch already partly materialized or source-id collision: {sorted(overlap)[:5]}")

    edge_number = next_numeric_id(edges, "b_edge_id")
    evidence_number = next_numeric_id(evidence, "b_evidence_id")
    audit: list[dict[str, str]] = []

    for row in source_rows:
        curation_id = row["curation_id"]
        edge_id = f"M22B-E{edge_number:06d}"
        evidence_id = f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1

        direct = "direct_binding" in row["support_kind"] or "promoter" in row["support_kind"]
        evidence_layer = "ligand_receptor_or_direct_molecular" if direct else "downstream_or_functional"
        edge_status = "reviewed_direct_target" if direct else "reviewed_regulatory_support"
        source_scope = "direct_edge" if direct else "contextual_support"
        species = row["species"]
        cell = row.get("cell_type_context") or "unspecified comparator model"
        public_refs = "; ".join(split_values(row.get("public_reference_pmids", "")))
        primary = row.get("primary_pmids", "")
        corroborating = row.get("corroborating_pmids", "")
        source_keys = row.get("external_record_keys", "")
        registries = row.get("source_registries", "")
        limitations = (row.get("limitations") or "").strip()
        if limitations:
            limitations += " "
        limitations += (
            "This is general TF-target evidence from the recorded comparator context; "
            "it does not establish that an associated ligand/receptor handoff activates "
            "the TF in SCI or in a spinal-cord cell."
        )
        citation_note = (
            f"Public-TF curation {curation_id}; registries={registries}; "
            f"external_records={source_keys}; public_reference_pmids={public_refs or 'none recorded'}"
        )
        summary = row.get("notes") or (
            f"Exact source-verified {row['tf_symbol']} to {row['target_symbol']} regulatory relationship."
        )

        edges.append({
            "b_edge_id": edge_id,
            "source_entity": row["tf_symbol"],
            "relation_type": relation_text(row),
            "target_entity": row["target_symbol"],
            "pathway_name": "target_gene",
            "evidence_layer": evidence_layer,
            "source_a_edge_id": f"PUBTF-{curation_id}",
            "edge_status": edge_status,
            "context_scope": (
                f"General TF-target claim supported in {cell}; source model is retained, "
                "but SCI/spinal-cord transfer is not asserted."
            ),
            "cell_type_context": cell,
            "compartment_context": "unspecified",
            "species_context": species,
            "injury_context": "not_assessed",
            "confidence_tier": "high",
            "export_priority": "medium",
            "exportable": "true",
            "consolidation_note": (
                f"{BATCH_ID}: high confidence for the standalone general TF-regulon claim; "
                "upstream ligand/receptor-to-TF activation in SCI remains a separate claim."
            ),
        })
        evidence.append({
            "b_evidence_id": evidence_id,
            "source_a_evidence_id": f"PUBTF-{curation_id}",
            "b_edge_ids": edge_id,
            "source_kind": "reviewed_direct_target" if direct else "reviewed_regulatory_support",
            "source_locator": "; ".join(
                value for value in (primary, corroborating)
                if value and value != r"\N"
            ) or "public source record",
            "support_kind": "primary_experiment",
            "species_support": species,
            "source_scope": source_scope,
            "confidence_tier": "high",
            "citation_note": citation_note,
            "evidence_summary": summary,
            "limitations": limitations,
            "evidence_layer": evidence_layer,
            "exportable": "true",
            "consolidation_note": (
                f"{BATCH_ID}: source-verified general TF-target evidence materialized; "
                "no upstream SCI activation inference."
            ),
        })
        audit.append({
            "batch_id": BATCH_ID,
            "curation_id": curation_id,
            "species": species,
            "tf_symbol": row["tf_symbol"],
            "target_symbol": row["target_symbol"],
            "b_edge_id": edge_id,
            "b_evidence_id": evidence_id,
            "old_edge_count": "0",
            "new_edge_status": edge_status,
            "new_edge_confidence": "high",
            "new_evidence_confidence": "high",
            "effect_polarity": row["effect_polarity"],
            "support_kind": row["support_kind"],
            "evidence_scope": row["evidence_status"],
            "primary_pmids": primary,
            "corroborating_pmids": corroborating,
            "external_record_keys": source_keys,
            "source_registries": registries,
            "cell_type_context": cell,
            "module22b_register_changed": "true",
            "upstream_sci_activation_claim": "false",
        })

    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    write_tsv(AUDIT_PATH, audit, AUDIT_FIELDS)
    counts = {
        "batch_id": BATCH_ID,
        "source_verified_rows": len(source_rows),
        "general_tf_regulon_edges_added": len(audit),
        "high_edges_after": sum(row["confidence_tier"] == "high" for row in edges),
        "exportable_edges_after": sum(row["exportable"] == "true" for row in edges),
        "target_gene_edges_after": sum(row["pathway_name"] == "target_gene" for row in edges),
        "module22b_register_changed": True,
        "canonical_sql_materialization": False,
        "upstream_sci_activation_inferred": False,
        "audit": str(AUDIT_PATH),
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(counts, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(counts, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
