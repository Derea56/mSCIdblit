#!/usr/bin/env python3
"""Build reviewable Module 20B-24B audit-layer registers from frozen A layers.

The generated B layers are deliberately audit-layer outputs. They retain raw
A-layer labels, stable source identifiers, explicit boundaries, and an
exportable flag; they do not write the canonical simulator tables.
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "work" / "module_b_consolidation"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)


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
BOUNDARY_FIELDS = [
    "boundary_id", "source_a_evidence_id", "source_a_edge_ids", "boundary_type",
    "source_locator", "species_support", "source_scope", "summary", "limitations",
]
MATRIX_FIELDS = [
    "candidate_id", "source_a_status", "b_status", "layer1_status", "layer2_status",
    "layer3_status", "species_posture", "injury_context_posture", "next_gap",
]


def layer_from_label(label: str) -> str:
    value = label.lower()
    normalized = value.strip()
    if (
        "no_evidence" in value
        or "negative_evidence" in value
        or normalized in {"boundary", "search_boundary"}
    ):
        return "boundary"
    # Check downstream/function labels before pathway labels.  A-layer labels
    # such as downstream_pathway_or_cellular_function contain the word
    # "pathway", but must not be promoted to receptor-proximal relay.
    if "downstream" in value or any(token in value for token in ("function", "phenotype", "program", "output", "regulation")):
        return "downstream_or_functional"
    if any(token in value for token in ("binding", "activation", "engagement", "pharmacology")):
        return "ligand_receptor_or_direct_molecular"
    if "proximal" in value or "relay" in value or "pathway" in value:
        return "receptor_proximal_or_pathway"
    return "contextual_or_unresolved"


def support_kind(source_kind: str, source_locator: str, original: str) -> str:
    value = " ".join((source_kind, source_locator, original)).lower()
    if "no_evidence_boundary" in value or "search_boundary" in value:
        return "negative_evidence"
    if "primary" in value:
        return "primary_experiment"
    if "database" in value or "curated" in value:
        return "database_curated"
    if "review" in value:
        return "review_statement"
    return "manual_background"


def source_scope(layer: str, support: str) -> str:
    if support == "negative_evidence" or layer == "boundary":
        return "negative_evidence"
    if layer == "ligand_receptor_or_direct_molecular":
        return "direct_edge"
    if layer == "receptor_proximal_or_pathway":
        return "pathway_membership"
    return "contextual_support"


def write_module(module: str, edges: list[dict[str, str]], evidence: list[dict[str, str]],
                 matrix: list[dict[str, str]], boundaries: list[dict[str, str]],
                 complex_rows: list[dict[str, str]] | None = None) -> dict[str, int]:
    module_dir = OUT / f"module{module}b"
    module_dir.mkdir(parents=True, exist_ok=True)
    write_tsv(module_dir / f"module{module}b_edge_register.tsv", edges, EDGE_FIELDS)
    write_tsv(module_dir / f"module{module}b_evidence_register.tsv", evidence, EVIDENCE_FIELDS)
    write_tsv(module_dir / f"module{module}b_boundary_register.tsv", boundaries, BOUNDARY_FIELDS)
    write_tsv(module_dir / f"module{module}b_consolidation_matrix.tsv", matrix, MATRIX_FIELDS)
    if complex_rows is not None:
        write_tsv(
            module_dir / f"module{module}b_complex_register.tsv",
            complex_rows,
            ["complex_id", "source_review_id", "complex_coverage", "pair_label", "note"],
        )
    return {
        "edges": len(edges),
        "evidence": len(evidence),
        "boundaries": len(boundaries),
        "matrix": len(matrix),
        "exportable_edges": sum(row["exportable"] == "true" for row in edges),
    }


def build_20b() -> dict[str, int]:
    base = ROOT / "work" / "module20_db_seed" / "evidence_escalation_router"
    queue = read_tsv(base / "module20a_external_review_queue.tsv")
    ledgers = {}
    for filename, classification in (
        ("module20a_low_evidence_registry.tsv", "low_evidence"),
        ("module20a_no_evidence_registry.tsv", "no_evidence"),
        ("module20a_non_ligand_receptor_registry.tsv", "non_ligand_receptor"),
    ):
        for row in read_tsv(base / filename):
            ledgers[row["review_id"]] = classification

    edges: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    boundaries: list[dict[str, str]] = []
    matrix: list[dict[str, str]] = []
    complexes: list[dict[str, str]] = []
    for index, row in enumerate(queue, 1):
        label = row["pair_label_canonical"]
        source, target = label.rsplit(" ", 1) if " " in label else (label, "unresolved")
        classification = ledgers.get(row["review_id"], "frozen_lr_supported")
        supported = classification == "frozen_lr_supported" and row["confidence_decision"] in {"high", "medium"}
        layer = "boundary" if classification != "frozen_lr_supported" else "ligand_receptor_or_direct_molecular"
        edge_id = f"M20B-E{index:06d}"
        note = f"Frozen Module 20A classification: {classification}; source LR manifest preserved."
        edges.append({
            "b_edge_id": edge_id, "source_entity": source, "relation_type": "engages",
            "target_entity": target, "pathway_name": "module20a_frozen_ligand_receptor",
            "evidence_layer": layer, "source_a_edge_id": row["review_id"],
            "edge_status": classification, "context_scope": "Module 20A frozen LR release",
            "cell_type_context": "not_inferred_from_LR_release", "compartment_context": "not_inferred",
            "species_context": "mouse_release_scope", "injury_context": "SCI-relevant candidate universe",
            "confidence_tier": row["confidence_decision"], "export_priority": "high" if supported else "exclude",
            "exportable": "true" if supported else "false", "consolidation_note": note,
        })
        support = "database_curated" if classification == "frozen_lr_supported" else "negative_evidence"
        evidence_id = f"M20B-EVID-{index:06d}"
        evidence.append({
            "b_evidence_id": evidence_id, "source_a_evidence_id": row["review_id"],
            "b_edge_ids": edge_id, "source_kind": "frozen_module20a_lr_release",
            "source_locator": "work/module20_db_seed/evidence_escalation_router/module20a_lr_release_manifest.json",
            "support_kind": support, "species_support": "mouse", "source_scope": "direct_edge" if supported else "negative_evidence",
            "confidence_tier": row["confidence_decision"], "citation_note": row["evidence_register_ids"],
            "evidence_summary": row["curator_notes"], "limitations": row["review_priority_rationale"],
            "evidence_layer": layer, "exportable": "true" if supported else "false", "consolidation_note": note,
        })
        matrix.append({
            "candidate_id": row["review_id"], "source_a_status": row["review_status"],
            "b_status": classification, "layer1_status": layer, "layer2_status": "not_inferred",
            "layer3_status": "not_inferred", "species_posture": "mouse_release_scope",
            "injury_context_posture": "SCI-relevant candidate universe", "next_gap": row["curator_notes"],
        })
        if not supported:
            boundaries.append({
                "boundary_id": f"M20B-BOUNDARY-{index:06d}", "source_a_evidence_id": row["review_id"],
                "source_a_edge_ids": edge_id, "boundary_type": classification,
                "source_locator": "work/module20_db_seed/evidence_escalation_router/module20a_lr_release_manifest.json",
                "species_support": "mouse", "source_scope": "negative_evidence", "summary": row["curator_notes"],
                "limitations": f"Retained from frozen Module 20A classification; not exportable as a supported B-layer edge.",
            })
        coverage = row["complex_receptor_coverage"]
        if coverage not in {"", "not_assessed", "not_composite_or_not_in_gap_audit"}:
            complexes.append({
                "complex_id": f"M20B-COMPLEX-{index:06d}", "source_review_id": row["review_id"],
                "complex_coverage": coverage, "pair_label": label,
                "note": "Coverage annotation preserved; subunit membership is not inferred from the pair label.",
            })
    return write_module("20", edges, evidence, matrix, boundaries, complexes)


def build_a_register_module(module: str, edge_path: Path, evidence_path: Path,
                            matrix_path: Path | None = None,
                            layer_path: Path | None = None) -> dict[str, int]:
    a_edges = read_tsv(edge_path)
    a_evidence = read_tsv(evidence_path)
    a_matrix = read_tsv(matrix_path) if matrix_path and matrix_path.exists() else []
    edge_layer_overrides: dict[str, str] = {}
    if layer_path and layer_path.exists():
        for row in read_tsv(layer_path):
            if row.get("edge_id") and row.get("evidence_layer"):
                edge_layer_overrides[row["edge_id"]] = row["evidence_layer"]
    edge_index_by_a_id = {
        row.get("edge_id", row.get("module22a_edge_id", "")): index
        for index, row in enumerate(a_edges, 1)
    }
    evidence_to_a_edge_ids: dict[str, list[str]] = defaultdict(list)
    if module == "22":
        for row in a_edges:
            a_edge_id = row.get("module22a_edge_id", "")
            for evidence_id in row.get("module22a_evidence_ids", "").split(";"):
                if evidence_id.strip():
                    evidence_to_a_edge_ids[evidence_id.strip()].append(a_edge_id)
    evidence_by_edge: dict[str, list[str]] = defaultdict(list)
    evidence_rows: list[dict[str, str]] = []
    for index, row in enumerate(a_evidence, 1):
        source_edge_ids = [x.strip() for x in row.get("edge_id", "").split(";") if x.strip()]
        if module == "22":
            source_edge_ids = evidence_to_a_edge_ids.get(row.get("module22a_evidence_id", ""), [])
        b_ids = [f"M{module}B-E{next((i for i, e in enumerate(a_edges, 1) if e.get('edge_id') == eid), 0):06d}" for eid in source_edge_ids]
        if module == "22":
            b_ids = [f"M{module}B-E{edge_index_by_a_id[eid]:06d}" for eid in source_edge_ids if eid in edge_index_by_a_id]
        for bid in b_ids:
            if bid != f"M{module}B-E{0:06d}":
                evidence_by_edge[bid].append(f"M{module}B-EVID-{index:06d}")
        if module == "21":
            edge_layers = {
                layer_from_label(edge_layer_overrides[eid])
                for eid in source_edge_ids
                if eid in edge_layer_overrides
            }
            if len(edge_layers) == 1:
                layer = next(iter(edge_layers))
            elif len(edge_layers) > 1:
                layer = "mixed_receptor_proximal_and_downstream"
            else:
                layer = layer_from_label(row.get("evidence_layer", "") + " " + row.get("source_scope", "") + " " + row.get("relation_type", ""))
        else:
            layer = layer_from_label(row.get("evidence_layer", "") + " " + row.get("source_scope", "") + " " + row.get("relation_type", ""))
        original_support = row.get("support_kind", "") or row.get("review_status", "")
        source_kind = row.get("source_kind", "")
        source_locator = row.get("source_locator", "")
        citation_note = row.get("citation_note", "")
        species_support = row.get("species_support", "")
        source_a_evidence_id = row.get("evidence_id", "")
        if module == "22":
            # Module 22A uses a different, explicit schema. Preserve its
            # stable citation bundle and handoff ID instead of emitting blank
            # provenance fields into the B audit register.
            source_kind = source_kind or row.get("review_status", "")
            source_locator = source_locator or row.get("stable_citations", "")
            citation_note = citation_note or row.get("module22a_handoff_ids", "")
            species_support = species_support or row.get("species", "")
            source_a_evidence_id = row.get("module22a_evidence_id", "")
        support = support_kind(source_kind, source_locator, original_support)
        evidence_rows.append({
            "b_evidence_id": f"M{module}B-EVID-{index:06d}", "source_a_evidence_id": source_a_evidence_id,
            "b_edge_ids": ";".join(b_ids), "source_kind": source_kind,
            "source_locator": source_locator, "support_kind": support,
            "species_support": species_support, "source_scope": source_scope(layer, support),
            "confidence_tier": row.get("confidence_tier", ""), "citation_note": citation_note,
            "evidence_summary": row.get("evidence_summary", ""), "limitations": row.get("limitations", ""),
            "evidence_layer": layer, "exportable": "false" if support == "negative_evidence" else "true",
            "consolidation_note": "A-layer evidence retained without directness promotion.",
        })
    edges: list[dict[str, str]] = []
    for index, row in enumerate(a_edges, 1):
        b_id = f"M{module}B-E{index:06d}"
        associated_evidence = evidence_by_edge.get(b_id, [])
        evidence_exportable = {
            item["b_evidence_id"]: item["exportable"] == "true" for item in evidence_rows
        }
        supported = (
            bool(associated_evidence)
            and any(evidence_exportable.get(eid, False) for eid in associated_evidence)
            and "boundary" not in row.get("evidence_status", "").lower()
            and "no_evidence" not in row.get("review_statuses", "").lower()
        )
        edges.append({
            "b_edge_id": b_id, "source_entity": row.get("source_entity", row.get("tf_entity", "")),
            "relation_type": row.get("relation_type", "program_association"),
            "target_entity": row.get("target_entity", row.get("target_or_program", "")),
            "pathway_name": row.get("pathway_name", row.get("target_class", "")),
            "evidence_layer": layer_from_label(
                edge_layer_overrides.get(row.get("edge_id", ""), row.get("evidence_layer", ""))
                + " " + row.get("relation_type", "")
            ),
            "source_a_edge_id": row.get("edge_id", row.get("module22a_edge_id", "")),
            "edge_status": row.get("evidence_status", row.get("review_statuses", "")),
            "context_scope": row.get("context_scope", row.get("context_limitations", "")),
            "cell_type_context": row.get("cell_type_context", row.get("cell_type_model", "")),
            "compartment_context": row.get("compartment_context", ""),
            "species_context": row.get("species_context", row.get("species", "")),
            "injury_context": row.get("injury_context", ""),
            "confidence_tier": row.get("confidence_tier", row.get("confidence_values", "")),
            "export_priority": row.get("export_priority", "medium"),
            "exportable": "true" if supported else "false",
            "consolidation_note": "Direct, pathway, program, and functional layers remain distinct.",
        })
    boundaries: list[dict[str, str]] = []
    for index, row in enumerate(a_evidence, 1):
        if (
            "no_evidence" in row.get("support_kind", "")
            or "boundary" in row.get("source_kind", "").lower()
            or row.get("review_status", "") == "no_evidence_boundary"
        ):
            if module == "22":
                source_a_evidence_id = row.get("module22a_evidence_id", "")
                source_edge_ids = evidence_to_a_edge_ids.get(source_a_evidence_id, [])
                edge_ids = ";".join(
                    f"M{module}B-E{edge_index_by_a_id[x]:06d}"
                    for x in source_edge_ids if x in edge_index_by_a_id
                )
            else:
                source_a_evidence_id = row.get("evidence_id", "")
                edge_ids = ";".join(
                    f"M{module}B-E{next((i for i, e in enumerate(a_edges, 1) if e.get('edge_id') == x), 0):06d}"
                    for x in row.get("edge_id", "").split(";") if x.strip()
                )
            boundaries.append({
                "boundary_id": f"M{module}B-BOUNDARY-{index:06d}", "source_a_evidence_id": source_a_evidence_id,
                "source_a_edge_ids": edge_ids, "boundary_type": "no_evidence_boundary",
                "source_locator": row.get("source_locator", ""), "species_support": row.get("species_support", ""),
                "source_scope": "negative_evidence", "summary": row.get("evidence_summary", ""),
                "limitations": row.get("limitations", ""),
            })
    matrix: list[dict[str, str]] = []
    for row in a_matrix:
        matrix.append({
            "candidate_id": row.get("candidate_id", row.get("family_id", "")),
            "source_a_status": row.get("status", ""), "b_status": row.get("status", ""),
            "layer1_status": row.get("layer1_status", ""), "layer2_status": row.get("layer2_status", ""),
            "layer3_status": row.get("layer3_status", ""),
            "species_posture": row.get("species_posture", ""),
            "injury_context_posture": row.get("SCI_context_posture", row.get("SCI_relevance_posture", "")),
            "next_gap": row.get("next_gap", ""),
        })
    return write_module(module, edges, evidence_rows, matrix, boundaries)


def main() -> None:
    outputs = {
        "20": build_20b(),
        "21": build_a_register_module(
            "21", ROOT / "work/module21_relay/module21a_saturation_edge_register.tsv",
            ROOT / "work/module21_relay/module21a_saturation_evidence_register.tsv",
            ROOT / "work/module21_relay/module21a_saturation_matrix.tsv",
            ROOT / "work/module21_relay/module21a_evidence_layer_register.tsv",
        ),
        "22": build_a_register_module(
            "22", ROOT / "work/module22a/module22a_edge_register.tsv",
            ROOT / "work/module22a/module22a_evidence_register.tsv", None,
        ),
        "23": build_a_register_module(
            "23", ROOT / "work/module23a/module23a_edge_register.tsv",
            ROOT / "work/module23a/module23a_evidence_register.tsv",
            ROOT / "work/module23a/module23a_saturation_matrix.tsv",
        ),
        "24": build_a_register_module(
            "24", ROOT / "work/module24a/module24a_edge_register.tsv",
            ROOT / "work/module24a/module24a_evidence_register.tsv",
            ROOT / "work/module24a/module24a_saturation_matrix.tsv",
        ),
    }
    for module, counts in outputs.items():
        print(module, counts)


if __name__ == "__main__":
    main()
