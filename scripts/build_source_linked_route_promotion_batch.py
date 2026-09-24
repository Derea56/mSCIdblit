#!/usr/bin/env python3
"""Promote directly source-linked partial routes into the evidence overlay.

This pass exposes receptor-proximal, intracellular, TF, and output evidence
that is already present in the route-evidence table but is not yet addressable
as a literature-expansion row.  It requires both downstream source pointers
and a stable public paper locator, keeps only ligand-role inputs, and
deduplicates against the existing expansion layer.  Missing handoffs remain
explicitly unresolved; no graph edge, causal assertion, or confidence score is
created.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROUTE_SHAPES = {
    "ligand>receptor>output": (
        "ligand_node_id", "receptor_node_id", "output_node_id",
    ),
    "ligand>receptor>????>????>output": (
        "ligand_node_id", "receptor_node_id", "output_node_id",
    ),
    "ligand>receptor>????>TF>output": (
        "ligand_node_id", "receptor_node_id", "transcription_factor_node_id",
        "output_node_id",
    ),
    "ligand>receptor>intracellular>????>output": (
        "ligand_node_id", "receptor_node_id", "intracellular_continuation_node_id",
        "output_node_id",
    ),
    "ligand>receptor>intracellular>TF>output": (
        "ligand_node_id", "receptor_node_id", "intracellular_continuation_node_id",
        "transcription_factor_node_id", "output_node_id",
    ),
    "ligand>receptor>????>????>target_gene_expression": (
        "ligand_node_id", "receptor_node_id", "target_gene_node_id",
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def split_values(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def join_unique(*values: str) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in split_values(value):
            if item not in seen:
                seen.add(item)
                result.append(item)
    return ";".join(result)


def join_stable_locators(*values: str) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in split_values(value):
            if not re.match(r"(?i)^(pmid:|pmcid:|doi:|https?://)", item):
                continue
            if item not in seen:
                seen.add(item)
                result.append(item)
    return "; ".join(result)


def signature(row: dict[str, str]) -> tuple[str, ...]:
    fields = ROUTE_SHAPES[row["path_expression"]]
    return tuple(row.get(field, "") for field in fields)


def matching_edge(
    edge_id: str,
    edges: dict[str, dict[str, str]],
    source_node_id: str,
    target_node_id: str,
) -> str:
    edge = edges.get(edge_id)
    if edge and (edge.get("source_node_id"), edge.get("target_node_id")) == (source_node_id, target_node_id):
        return edge_id
    return ""


def required_node_ids(route: dict[str, str]) -> list[str]:
    fields = ["ligand_node_id", "receptor_node_id"]
    path = route["path_expression"]
    if "intracellular>" in path:
        fields.append("intracellular_continuation_node_id")
    if ">TF>" in path:
        fields.append("transcription_factor_node_id")
    if "target_gene_expression" in path:
        fields.append("target_gene_node_id")
    return [route.get(field, "") for field in fields]


def make_rows(bundle: Path) -> tuple[list[dict[str, str]], dict[str, object]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    roles: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(bundle / "mechanism_node_roles.tsv"):
        roles[row["node_id"]].add(row["role"])
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    queues = {row["queue_id"]: row for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")}
    evidence = {row["record_id"]: row for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}
    routes = read_tsv(bundle / "mechanism_signaling_route_evidence.tsv.gz")
    expansions = read_tsv(bundle / "mechanism_literature_expansion.tsv")

    existing_signatures = {
        signature(row)
        for row in expansions
        if row.get("path_expression") in ROUTE_SHAPES
    }
    generated_signatures: set[tuple[str, ...]] = set()
    rows: list[dict[str, str]] = []
    skipped = Counter()
    seen_source_routes: set[str] = set()

    for route in routes:
        path = route.get("path_expression", "")
        if path not in ROUTE_SHAPES:
            continue
        if route.get("route_evidence_id", "").startswith("LITEXP:"):
            skipped["already_literature_expansion_route"] += 1
            continue
        queue_id = route.get("source_queue_id", "")
        evidence_id = route.get("source_evidence_record_id", "")
        source_record = evidence.get(evidence_id, {})
        if not queue_id or queue_id not in queues or not evidence_id or evidence_id not in evidence:
            skipped["missing_source_linkage"] += 1
            continue
        if not join_stable_locators(source_record.get("source_locator", "")):
            skipped["missing_stable_locator"] += 1
            continue
        ligand_id = route.get("ligand_node_id", "")
        if "ligand" not in roles.get(ligand_id, set()):
            skipped["ligand_role_not_asserted"] += 1
            continue
        if any(node_id not in nodes for node_id in required_node_ids(route)):
            skipped["missing_route_node"] += 1
            continue

        route_signature = signature(route)
        if route_signature in existing_signatures or route_signature in generated_signatures:
            skipped["signature_already_present"] += 1
            continue
        generated_signatures.add(route_signature)
        source_route_id = route.get("route_evidence_id", "")
        if source_route_id in seen_source_routes:
            skipped["duplicate_source_route"] += 1
            continue
        seen_source_routes.add(source_route_id)

        lr_edge_id = matching_edge(
            route.get("ligand_receptor_edge_id", ""), edges,
            route.get("ligand_node_id", ""), route.get("receptor_node_id", ""),
        )
        relay_edge_id = matching_edge(
            route.get("receptor_intracellular_edge_id", ""), edges,
            route.get("receptor_node_id", ""), route.get("intracellular_continuation_node_id", ""),
        )
        intracellular_tf_edge_id = matching_edge(
            route.get("intracellular_tf_edge_id", ""), edges,
            route.get("intracellular_continuation_node_id", ""), route.get("transcription_factor_node_id", ""),
        )
        tf_target_edge_id = matching_edge(
            route.get("tf_target_edge_id", ""), edges,
            route.get("transcription_factor_node_id", ""), route.get("target_gene_node_id", ""),
        )

        missing_edges = join_unique(
            "receptor_to_intracellular_edge" if route.get("intracellular_continuation_node_id") and not relay_edge_id else "",
            "intracellular_to_tf_edge" if route.get("transcription_factor_node_id") and route.get("intracellular_continuation_node_id") and not intracellular_tf_edge_id else "",
            "tf_to_target_edge" if route.get("target_gene_node_id") and route.get("transcription_factor_node_id") and not tf_target_edge_id else "",
        )
        linkage = join_unique(
            route.get("route_linkage_status", ""),
            "literature_expansion:source_linked_route_promotion",
            "source_queue_and_evidence_record_linked",
            "primary_locator_retained",
            "receptor_to_intracellular_edge_asserted_as_graph_edge" if relay_edge_id else "receptor_to_intracellular_edge_not_asserted",
            "intracellular_to_tf_edge_asserted_as_graph_edge" if intracellular_tf_edge_id else "intracellular_to_tf_edge_not_asserted",
            "tf_to_target_edge_asserted_as_graph_edge" if tf_target_edge_id else "tf_to_target_edge_not_asserted",
            "end_to_end_chain_not_asserted_by_single_source",
            "evidence_route_only",
        )
        summary = route.get("evidence_summary", "").strip() or source_record.get("evidence_summary", "").strip()
        if not summary:
            summary = f"Source-linked evidence route for {route.get('path_expression', '')}."
        limitations = join_unique(
            route.get("limitations", ""),
            source_record.get("limitations", ""),
            "This route preserves only the layers explicitly retained in the source-linked route record; unresolved handoffs are not inferred.",
            "This is an evidence route rather than a causal graph edge and does not create a database confidence score.",
        )
        output_class = route.get("output_class", "") or source_record.get("output_class", "")
        row = {
            "expansion_id": f"M21B-LITEXP-SOURCE-ROUTE-{len(rows) + 1:05d}",
            "source_queue_id": queue_id,
            "route_status": "retained_evidence_route",
            "path_expression": path,
            "route_tier": route.get("route_tier", ""),
            "known_layers": route.get("known_layers", ""),
            "missing_layers": join_unique(route.get("missing_layers", ""), missing_edges),
            "intracellular_status": route.get("intracellular_status", ""),
            "ligand_node_id": route.get("ligand_node_id", ""),
            "ligand_label": route.get("ligand_label", ""),
            "ligand_receptor_edge_id": lr_edge_id,
            "receptor_node_id": route.get("receptor_node_id", ""),
            "receptor_label": route.get("receptor_label", ""),
            "receptor_intracellular_edge_id": relay_edge_id,
            "intracellular_continuation_node_id": route.get("intracellular_continuation_node_id", ""),
            "intracellular_continuation_label": route.get("intracellular_continuation_label", ""),
            "intracellular_tf_edge_id": intracellular_tf_edge_id,
            "transcription_factor_node_id": route.get("transcription_factor_node_id", ""),
            "transcription_factor_label": route.get("transcription_factor_label", ""),
            "tf_target_edge_id": tf_target_edge_id,
            "target_gene_node_id": route.get("target_gene_node_id", ""),
            "target_gene_label": route.get("target_gene_label", ""),
            "target_output_form_id": route.get("target_output_form_id", ""),
            "output_node_id": route.get("output_node_id", ""),
            "output_label": route.get("output_label", ""),
            "output_form_id": route.get("output_form_id", ""),
            "bridge_id": route.get("bridge_id", ""),
            "pathway_name": route.get("pathway_name", ""),
            "input_evidence_type": route.get("input_evidence_type", "source_linked_route_evidence"),
            "output_evidence_type": route.get("output_evidence_type", "source_linked_output_evidence"),
            "evidence_ids": join_unique(route.get("evidence_ids", ""), source_record.get("source_evidence_ids", ""), evidence_id, source_route_id),
            "source_chain_id": f"source_linked_route_promotion:{source_route_id}",
            "source_evidence_record_id": evidence_id,
            "route_linkage_status": linkage,
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": route.get("evidence_polarity", source_record.get("evidence_polarity", "supports")),
            "negative_evidence_status": route.get("negative_evidence_status", source_record.get("negative_evidence_status", "not_evaluated")),
            "evidence_directness": "source_linked_route",
            "output_class": output_class,
            "primary_locator": join_stable_locators(source_record.get("source_locator", "")),
            "citation_note": source_record.get("citation_note", "") or "Primary source locator retained from the linked downstream evidence record.",
            "evidence_summary": summary,
            "limitations": limitations,
            # The importer contract uses this status for all retained
            # primary-literature evidence routes; the source-linked subtype
            # is preserved in route_linkage_status and source_scope.
            "curation_status": "curated_primary_route",
            "species_context": route.get("species_context", source_record.get("species_context", "")),
            "cell_type_context": route.get("cell_type_context", source_record.get("cell_type_context", "")),
            "compartment_context": route.get("compartment_context", source_record.get("compartment_context", "")),
            "injury_context": route.get("injury_context", source_record.get("injury_context", "")),
            "context_scope": route.get("context_scope", source_record.get("context_scope", "")),
            "assay_or_perturbation": route.get("assay_or_perturbation", source_record.get("assay_or_perturbation", "")),
            "effect_polarity": route.get("effect_polarity", source_record.get("effect_polarity", "")),
            "source_scope": "source_linked_primary_route_evidence",
            "route_evidence_id": source_route_id,
            "output_edge_id": route.get("output_edge_id", ""),
        }
        rows.append(row)

    return rows, {
        "candidate_rows_added": len(rows),
        "candidate_ligands_added": len({row["ligand_label"] for row in rows}),
        "candidate_shapes": dict(sorted(Counter(row["path_expression"] for row in rows).items())),
        "skipped": dict(sorted(skipped.items())),
    }


def main() -> int:
    args = parse_args()
    rows, summary = make_rows(args.bundle.resolve())
    if not rows:
        raise ValueError("No eligible source-linked routes found")
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), **summary}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
