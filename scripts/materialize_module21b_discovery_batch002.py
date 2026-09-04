#!/usr/bin/env python3
"""Materialize primary-validated Module 21B discovery candidates.

This is a local audit-register write, not a PostgreSQL migration.  It accepts
only discovery rows that already carry a stable primary locator, a review
locator, a cited-primary lineage field, a primary model/assay description,
and the explicit ``validated_primary_exact_layer`` gate.  New rows retain the
discovery ID as their audit lineage, while the upstream Module 20A fields are
left empty because these candidates were discovered within Module 21B.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "work" / "module_b_consolidation" / "module21b"
DISCOVERY = MODULE_DIR / "module21b_edge_discovery_candidates.tsv"
EDGES = MODULE_DIR / "module21b_edge_register.tsv"
EVIDENCE = MODULE_DIR / "module21b_evidence_register.tsv"
BATCH = MODULE_DIR / "module21b_relay_promotion_batch002.tsv"

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
    "promotion_id", "discovery_id", "b_edge_id", "b_evidence_id",
    "previous_status", "new_status", "supported_layer", "review_locator",
    "review_cited_primary", "primary_locator", "primary_title", "decision_basis",
    "limitations_preserved", "materialization_status",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            delimiter="\t",
            extrasaction="raise",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip().lower())


def next_numeric_id(rows: list[dict[str, str]], field: str, pattern: str) -> int:
    values = []
    for row in rows:
        match = re.fullmatch(pattern, row[field].strip())
        if match:
            values.append(int(match.group(1)))
    return max(values, default=0) + 1


def species_scope(model: str) -> str:
    text = model.lower()
    labels = [
        (r"\bhuman\b", "human"), (r"\b(?:mouse|murine)\b", "mouse"),
        (r"\brat\b", "rat"), (r"\bxenopus\b", "Xenopus"),
        (r"\bzebrafish\b", "zebrafish"), (r"\bchick(?:en)?\b", "chick"),
        (r"\bporcine\b", "pig"), (r"\bpig\b", "pig"),
    ]
    found = []
    for pattern, label in labels:
        if re.search(pattern, text) and label not in found:
            found.append(label)
    return "; ".join(found) if found else "as stated in primary model/assay"


def source_scope(layer: str) -> str:
    value = layer.lower()
    if "ligand_receptor_binding_or_activation" in value:
        return "direct_edge"
    if "receptor_proximal_or_pathway" in value:
        return "pathway_membership"
    return "contextual_support"


def compartment(layer: str) -> str:
    value = layer.lower()
    if "ligand_receptor_binding_or_activation" in value:
        return "extracellular ligand to plasma-membrane receptor or receptor complex"
    if "receptor_proximal_or_pathway" in value:
        return "plasma-membrane receptor or complex to cytoplasmic signaling"
    return "receptor/pathway to cellular or functional output"


def validate_candidate(row: dict[str, str]) -> None:
    required = [
        "discovery_id", "candidate_source_entity", "relation_type", "candidate_target_entity",
        "pathway_name", "review_locator", "review_cited_primary", "review_supported_claim",
        "primary_locator", "primary_model_assay", "supported_layer", "primary_validation",
        "boundary_notes",
    ]
    missing = [field for field in required if not row.get(field, "").strip()]
    if missing:
        raise ValueError(f"{row.get('discovery_id', '<unknown>')} missing fields: {', '.join(missing)}")
    if row["primary_validation"].strip() != "validated_primary_exact_layer":
        raise ValueError(f"{row['discovery_id']} is not primary-validated")
    if not re.search(r"(?:PMID:|PMCID:|DOI:|https?://)", row["primary_locator"], re.I):
        raise ValueError(f"{row['discovery_id']} has no stable primary locator")
    if re.search(r"PMC\d+search|turn\d+|search\d+|file://", row["primary_locator"], re.I):
        raise ValueError(f"{row['discovery_id']} contains a placeholder primary locator")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--batch-output", type=Path, default=BATCH)
    parser.add_argument(
        "--promotion-id",
        default="module21b-discovery-materialization-batch002-2026-09-02",
    )
    args = parser.parse_args()

    discoveries = read_tsv(DISCOVERY)
    edges = read_tsv(EDGES)
    evidence = read_tsv(EVIDENCE)
    existing_batch = read_tsv(args.batch_output) if args.batch_output.exists() else []
    existing_triples = {
        (norm(row["source_entity"]), norm(row["relation_type"]), norm(row["target_entity"]))
        for row in edges
    }
    existing_discovery_ids = {
        row["consolidation_note"].split("discovery_id=", 1)[1].split(";", 1)[0]
        for row in edges
        if "discovery_id=" in row.get("consolidation_note", "")
    }

    candidates = []
    for row in discoveries:
        if row.get("disposition", "").strip() == "MATERIALIZED_REVIEWED_PRIMARY":
            continue
        if row.get("disposition", "").strip() != "PROMOTE_CANDIDATE":
            continue
        validate_candidate(row)
        triple = (
            norm(row["candidate_source_entity"]),
            norm(row["relation_type"]),
            norm(row["candidate_target_entity"]),
        )
        if triple in existing_triples:
            raise ValueError(f"{row['discovery_id']} overlaps an existing source/relation/target triple")
        if row["discovery_id"] in existing_discovery_ids:
            raise ValueError(f"{row['discovery_id']} already materialized")
        candidates.append((row, triple))
        existing_triples.add(triple)

    if not candidates:
        print("No unmaterialized primary-validated candidates found.")
        return 0

    edge_number = next_numeric_id(edges, "b_edge_id", r"M21B-E(\d+)")
    evidence_number = next_numeric_id(evidence, "b_evidence_id", r"M21B-EVID-(\d+)")
    promotion_id = args.promotion_id
    new_edges = []
    new_evidence = []
    batch_rows = []
    for offset, (row, _triple) in enumerate(candidates):
        edge_id = f"M21B-E{edge_number + offset:06d}"
        evidence_id = f"M21B-EVID-{evidence_number + offset:06d}"
        layer = row["supported_layer"].strip()
        species = species_scope(row["primary_model_assay"])
        lineage = f"discovery_id={row['discovery_id']}; review={row['review_locator']}; primary={row['primary_locator']}"
        note = (
            "Review-guided primary materialization; exact supported layer only. "
            f"{lineage}; no SCI or terminal-TF inference."
        )
        summary = (
            f"Primary-supported claim: {row['review_supported_claim']} "
            f"Primary model/assay: {row['primary_model_assay']}"
        )
        citation = (
            f"Review lead: {row['review_locator']}; review-cited primary: "
            f"{row['review_cited_primary']}; primary locator: {row['primary_locator']}"
        )
        new_edges.append({
            "b_edge_id": edge_id,
            "source_entity": row["candidate_source_entity"],
            "relation_type": row["relation_type"],
            "target_entity": row["candidate_target_entity"],
            "pathway_name": row["pathway_name"],
            "evidence_layer": layer,
            "source_a_edge_id": "",
            "edge_status": "validated_primary_exact_layer",
            "context_scope": "review-guided primary evidence; exact topology/layer bounded",
            "cell_type_context": row["primary_model_assay"],
            "compartment_context": compartment(layer),
            "species_context": species,
            "injury_context": "no SCI transfer inferred; primary model context only",
            "confidence_tier": "high",
            "export_priority": "medium",
            "exportable": "true",
            "consolidation_note": note,
        })
        new_evidence.append({
            "b_evidence_id": evidence_id,
            "source_a_evidence_id": "",
            "b_edge_ids": edge_id,
            "source_kind": "review_guided_primary_validation",
            "source_locator": row["primary_locator"],
            "support_kind": "primary_experiment",
            "species_support": species,
            "source_scope": source_scope(layer),
            "confidence_tier": "high",
            "citation_note": citation,
            "evidence_summary": summary,
            "limitations": row["boundary_notes"],
            "evidence_layer": layer,
            "exportable": "true",
            "consolidation_note": note,
        })
        batch_rows.append({
            "promotion_id": promotion_id,
            "discovery_id": row["discovery_id"],
            "b_edge_id": edge_id,
            "b_evidence_id": evidence_id,
            "previous_status": "PROMOTE_CANDIDATE",
            "new_status": "MATERIALIZED_REVIEWED_PRIMARY",
            "supported_layer": layer,
            "review_locator": row["review_locator"],
            "review_cited_primary": row["review_cited_primary"],
            "primary_locator": row["primary_locator"],
            "primary_title": row.get("primary_title", ""),
            "decision_basis": row["review_supported_claim"],
            "limitations_preserved": row["boundary_notes"],
            "materialization_status": "local_21B_registers_only; no_database_write",
        })

    if args.dry_run:
        print(f"would_materialize={len(candidates)} first_edge={new_edges[0]['b_edge_id']} last_edge={new_edges[-1]['b_edge_id']}")
        return 0

    edges.extend(new_edges)
    evidence.extend(new_evidence)
    write_tsv(EDGES, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE, evidence, EVIDENCE_FIELDS)
    existing_batch.extend(batch_rows)
    write_tsv(args.batch_output, existing_batch, BATCH_FIELDS)
    for row, _triple in candidates:
        row["disposition"] = "MATERIALIZED_REVIEWED_PRIMARY"
    write_tsv(DISCOVERY, discoveries, list(discoveries[0]))
    print(
        f"materialized={len(candidates)} edges={new_edges[0]['b_edge_id']}..{new_edges[-1]['b_edge_id']} "
        f"evidence={new_evidence[0]['b_evidence_id']}..{new_evidence[-1]['b_evidence_id']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
