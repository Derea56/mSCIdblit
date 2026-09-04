#!/usr/bin/env python3
"""Materialize validated Module 21B discovery rows into local registers."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "work/module_b_consolidation/module21b"
DISCOVERY = MODULE / "module21b_edge_discovery_candidates.tsv"
EDGES = MODULE / "module21b_edge_register.tsv"
EVIDENCE = MODULE / "module21b_evidence_register.tsv"
BATCH = MODULE / "module21b_relay_promotion_batch002.tsv"

EDGE_FIELDS = [
    "b_edge_id", "source_entity", "relation_type", "target_entity", "pathway_name",
    "evidence_layer", "source_a_edge_id", "edge_status", "context_scope",
    "cell_type_context", "compartment_context", "species_context", "injury_context",
    "confidence_tier", "export_priority", "exportable", "consolidation_note",
]
EVIDENCE_FIELDS = [
    "b_evidence_id", "source_a_evidence_id", "b_edge_ids", "source_kind",
    "source_locator", "support_kind", "species_support", "source_scope",
    "confidence_tier", "citation_note", "evidence_summary", "limitations",
    "evidence_layer", "exportable", "consolidation_note",
]
BATCH_FIELDS = [
    "promotion_id", "discovery_id", "b_edge_id", "b_evidence_id", "previous_status",
    "new_status", "supported_layer", "review_locator", "review_cited_primary",
    "primary_locator", "primary_title", "decision_basis", "limitations_preserved",
    "materialization_status",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip().lower())


def next_id(rows: list[dict[str, str]], field: str, pattern: str) -> int:
    numbers = []
    for row in rows:
        match = re.fullmatch(pattern, row.get(field, "").strip())
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def species(model: str) -> str:
    labels = [(r"\bhuman\b", "human"), (r"\b(?:mouse|murine)\b", "mouse"),
              (r"\brat\b", "rat"), (r"\bxenopus\b", "Xenopus"),
              (r"\bchick(?:en)?\b", "chick")]
    found = []
    for pattern, label in labels:
        if re.search(pattern, model.lower()) and label not in found:
            found.append(label)
    return "; ".join(found) if found else "as stated in primary model/assay"


def compartment(layer: str) -> str:
    if "ligand_receptor_binding_or_activation" in layer:
        return "extracellular ligand to plasma-membrane receptor or receptor complex"
    if "receptor_proximal_or_pathway" in layer:
        return "plasma-membrane receptor or complex to cytoplasmic signaling"
    return "receptor/pathway to cellular or functional output"


def validate(row: dict[str, str]) -> None:
    required = ["discovery_id", "candidate_source_entity", "relation_type",
                "candidate_target_entity", "pathway_name", "review_locator",
                "review_cited_primary", "review_supported_claim", "primary_locator",
                "primary_model_assay", "supported_layer", "primary_validation",
                "boundary_notes"]
    missing = [name for name in required if not row.get(name, "").strip()]
    if missing:
        raise ValueError(f"{row.get('discovery_id', '<unknown>')} missing: {', '.join(missing)}")
    if row["primary_validation"].strip() != "validated_primary_exact_layer":
        raise ValueError(f"{row['discovery_id']} is not primary validated")
    if not re.search(r"(?:PMID:|PMCID:|DOI:|https?://)", row["primary_locator"], re.I):
        raise ValueError(f"{row['discovery_id']} has no stable primary locator")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--promotion-id", default="module21b-discovery-materialization-batch002-2026-09-04-ecm-par3-001")
    args = parser.parse_args()

    discoveries = read_tsv(DISCOVERY)
    edges = read_tsv(EDGES)
    evidence = read_tsv(EVIDENCE)
    batch = read_tsv(BATCH) if BATCH.exists() else []
    triples = {(norm(r["source_entity"]), norm(r["relation_type"]), norm(r["target_entity"])) for r in edges}
    materialized = {r.get("discovery_id", "") for r in discoveries if r.get("disposition") == "MATERIALIZED_REVIEWED_PRIMARY"}
    candidates = []
    for row in discoveries:
        if row.get("disposition") != "PROMOTE_CANDIDATE":
            continue
        validate(row)
        triple = (norm(row["candidate_source_entity"]), norm(row["relation_type"]), norm(row["candidate_target_entity"]))
        if triple in triples:
            raise ValueError(f"{row['discovery_id']} overlaps an existing edge triple")
        if row["discovery_id"] in materialized:
            raise ValueError(f"{row['discovery_id']} is already materialized")
        triples.add(triple)
        candidates.append(row)
    if not candidates:
        print("No unmaterialized primary-validated candidates found.")
        return 0

    edge_start = next_id(edges, "b_edge_id", r"M21B-E(\d+)")
    evidence_start = next_id(evidence, "b_evidence_id", r"M21B-EVID-(\d+)")
    new_edges, new_evidence, new_batch = [], [], []
    for offset, row in enumerate(candidates):
        edge_id = f"M21B-E{edge_start + offset:06d}"
        evidence_id = f"M21B-EVID-{evidence_start + offset:06d}"
        layer = row["supported_layer"].strip()
        sp = species(row["primary_model_assay"])
        lineage = f"discovery_id={row['discovery_id']}; review={row['review_locator']}; primary={row['primary_locator']}"
        note = f"Review-guided primary materialization; exact supported layer only. {lineage}; no SCI or terminal-TF inference."
        citation = f"Review lead: {row['review_locator']}; review-cited primary: {row['review_cited_primary']}; primary locator: {row['primary_locator']}"
        summary = f"Primary-supported claim: {row['review_supported_claim']} Primary model/assay: {row['primary_model_assay']}"
        new_edges.append({
            "b_edge_id": edge_id, "source_entity": row["candidate_source_entity"], "relation_type": row["relation_type"],
            "target_entity": row["candidate_target_entity"], "pathway_name": row["pathway_name"], "evidence_layer": layer,
            "source_a_edge_id": "", "edge_status": "validated_primary_exact_layer",
            "context_scope": "review-guided primary evidence; exact topology/layer bounded",
            "cell_type_context": row["primary_model_assay"], "compartment_context": compartment(layer),
            "species_context": sp, "injury_context": "no SCI transfer inferred; primary model context only",
            "confidence_tier": "high", "export_priority": "medium", "exportable": "true", "consolidation_note": note,
        })
        new_evidence.append({
            "b_evidence_id": evidence_id, "source_a_evidence_id": "", "b_edge_ids": edge_id,
            "source_kind": "review_guided_primary_validation", "source_locator": row["primary_locator"],
            "support_kind": "primary_experiment", "species_support": sp,
            "source_scope": "direct_edge" if "ligand_receptor_binding_or_activation" in layer else "pathway_membership",
            "confidence_tier": "high", "citation_note": citation, "evidence_summary": summary,
            "limitations": row["boundary_notes"], "evidence_layer": layer, "exportable": "true", "consolidation_note": note,
        })
        new_batch.append({
            "promotion_id": args.promotion_id, "discovery_id": row["discovery_id"], "b_edge_id": edge_id,
            "b_evidence_id": evidence_id, "previous_status": "PROMOTE_CANDIDATE",
            "new_status": "MATERIALIZED_REVIEWED_PRIMARY", "supported_layer": layer,
            "review_locator": row["review_locator"], "review_cited_primary": row["review_cited_primary"],
            "primary_locator": row["primary_locator"], "primary_title": row.get("primary_title", ""),
            "decision_basis": row["review_supported_claim"], "limitations_preserved": row["boundary_notes"],
            "materialization_status": "local_21B_registers_only; no_database_write",
        })

    print(f"would_materialize={len(candidates)} first_edge={new_edges[0]['b_edge_id']} last_edge={new_edges[-1]['b_edge_id']}") if args.dry_run else None
    if args.dry_run:
        return 0
    edges.extend(new_edges)
    evidence.extend(new_evidence)
    batch.extend(new_batch)
    write_tsv(EDGES, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE, evidence, EVIDENCE_FIELDS)
    write_tsv(BATCH, batch, BATCH_FIELDS)
    for row in candidates:
        row["disposition"] = "MATERIALIZED_REVIEWED_PRIMARY"
    write_tsv(DISCOVERY, discoveries, list(discoveries[0]))
    print(f"materialized={len(candidates)} edges={new_edges[0]['b_edge_id']}..{new_edges[-1]['b_edge_id']} evidence={new_evidence[0]['b_evidence_id']}..{new_evidence[-1]['b_evidence_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
