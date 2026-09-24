#!/usr/bin/env python3
"""Expand source-linked target-gene lists across the ligand route queue.

The full-sequence queue can retain an explicitly named target-gene list even
when the intracellular continuation or TF layer is unresolved.  This helper
promotes each named target into an evidence-only route for every eligible
ligand family, while preserving those unresolved layers as ``????``.  It uses
only queue records linked to a downstream curation record with a primary
source locator; graph-only route compositions are left for a separate pass.

No graph edge, causal assertion, or confidence score is created here.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import re
from pathlib import Path


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


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def target_output_label(label: str) -> str:
    return label if label.casefold().endswith((" expression", " gene")) else f"{label} expression"


def matching_edge(
    candidate_ids: str,
    fallback_id: str,
    edges: dict[str, dict[str, str]],
    source_node_id: str,
    target_node_id: str,
) -> str:
    for edge_id in split_values(candidate_ids) + ([fallback_id] if fallback_id else []):
        edge = edges.get(edge_id)
        if edge and edge["source_node_id"] == source_node_id and edge["target_node_id"] == target_node_id:
            return edge_id
    return ""


def route_shape(queue_row: dict[str, str]) -> tuple[str, str, str, str]:
    has_intracellular = bool(queue_row.get("intracellular_continuation_node_id"))
    has_tf = bool(queue_row.get("transcription_factor_node_id"))
    if has_intracellular and has_tf:
        return (
            "ligand>receptor>intracellular>TF>target_gene_expression",
            "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
            "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "",
        )
    if has_intracellular:
        return (
            "ligand>receptor>intracellular>????>target_gene_expression",
            "ligand_receptor_intracellular_target_missing_tf",
            "ligand|receptor|intracellular_continuation|target_gene_expression",
            "transcription_factor|intracellular_to_tf_edge",
        )
    if has_tf:
        return (
            "ligand>receptor>????>TF>target_gene_expression",
            "ligand_receptor_tf_target_missing_intracellular",
            "ligand|receptor|transcription_factor|target_gene_expression",
            "intracellular_continuation|intracellular_to_tf_edge",
        )
    return (
        "ligand>receptor>????>????>target_gene_expression",
        "ligand_receptor_target_missing_intracellular_and_tf",
        "ligand|receptor|target_gene_expression",
        "intracellular_continuation|transcription_factor|intracellular_to_tf_edge|tf_to_target_edge",
    )


def main() -> int:
    args = parse_args()
    bundle = args.bundle.resolve()
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    route_rows = read_tsv(bundle / "mechanism_signaling_route_evidence.tsv.gz")
    route_by_id = {row["route_evidence_id"]: row for row in route_rows}
    queue_rows = read_tsv(bundle / "mechanism_full_sequence_curation_queue.tsv.gz")
    downstream_queue = {row["queue_id"]: row for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")}
    downstream_evidence = {row["record_id"]: row for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}
    existing_expansions = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    existing_signatures = {
        (
            row.get("ligand_node_id", ""),
            row.get("receptor_node_id", ""),
            row.get("intracellular_continuation_node_id", ""),
            row.get("transcription_factor_node_id", ""),
            row.get("target_gene_node_id", ""),
            row.get("output_label", ""),
        )
        for row in existing_expansions
    }

    rows: list[dict[str, str]] = []
    generated_signatures: set[tuple[str, ...]] = set()
    skipped = {
        "missing_required_fields": 0,
        "target_label_mismatch": 0,
        "missing_direct_source_route": 0,
        "missing_primary_locator": 0,
        "already_present": 0,
    }
    for queue_row in queue_rows:
        required = (
            queue_row.get("ligand_node_id", ""),
            queue_row.get("ligand_label", ""),
            queue_row.get("receptor_node_id", ""),
            queue_row.get("receptor_label", ""),
            queue_row.get("target_gene_node_ids", ""),
            queue_row.get("target_gene_labels", ""),
            queue_row.get("stable_primary_locators", ""),
        )
        if not all(required):
            continue
        target_ids = split_values(queue_row["target_gene_node_ids"])
        target_labels = split_values(queue_row["target_gene_labels"])
        if len(target_ids) != len(target_labels):
            skipped["target_label_mismatch"] += 1
            continue

        source_routes = [
            route_by_id[route_id]
            for route_id in split_values(queue_row.get("route_evidence_ids", ""))
            if route_id in route_by_id
            and route_by_id[route_id].get("source_queue_id") in downstream_queue
            and route_by_id[route_id].get("source_evidence_record_id") in downstream_evidence
        ]
        if not source_routes:
            skipped["missing_direct_source_route"] += 1
            continue

        for target_id, target_label in zip(target_ids, target_labels):
            if target_id not in nodes:
                skipped["target_label_mismatch"] += 1
                continue
            target_route = next(
                (
                    route
                    for route in source_routes
                    if route.get("target_gene_node_id") == target_id
                    or normalize(route.get("target_gene_label", "")) == normalize(target_label)
                    or route.get("output_node_id") == target_id
                    or normalize(route.get("output_label", "")) == normalize(target_label)
                ),
                source_routes[0],
            )
            output_label = target_output_label(target_label)
            signature = (
                queue_row["ligand_node_id"],
                queue_row["receptor_node_id"],
                queue_row.get("intracellular_continuation_node_id", ""),
                queue_row.get("transcription_factor_node_id", ""),
                target_id,
                output_label,
            )
            if signature in existing_signatures or signature in generated_signatures:
                skipped["already_present"] += 1
                continue
            generated_signatures.add(signature)

            source_record = downstream_evidence[target_route["source_evidence_record_id"]]
            path_expression, route_tier, known_layers, missing_layers = route_shape(queue_row)
            lr_edge_id = matching_edge(
                queue_row.get("ligand_receptor_edge_ids", ""),
                target_route.get("ligand_receptor_edge_id", ""),
                edges,
                queue_row["ligand_node_id"],
                queue_row["receptor_node_id"],
            )
            relay_edge_id = matching_edge(
                queue_row.get("receptor_intracellular_edge_ids", ""),
                target_route.get("receptor_intracellular_edge_id", ""),
                edges,
                queue_row["receptor_node_id"],
                queue_row.get("intracellular_continuation_node_id", ""),
            )
            intracellular_tf_edge_id = matching_edge(
                queue_row.get("intracellular_tf_edge_ids", ""),
                target_route.get("intracellular_tf_edge_id", ""),
                edges,
                queue_row.get("intracellular_continuation_node_id", ""),
                queue_row.get("transcription_factor_node_id", ""),
            )
            tf_target_edge_id = matching_edge(
                queue_row.get("tf_target_edge_ids", ""),
                target_route.get("tf_target_edge_id", ""),
                edges,
                queue_row.get("transcription_factor_node_id", ""),
                target_id,
            )
            missing_edge_layers = join_unique(
                "intracellular_to_tf_edge" if queue_row.get("intracellular_continuation_node_id") and not intracellular_tf_edge_id else "",
                "tf_to_target_edge" if queue_row.get("transcription_factor_node_id") and not tf_target_edge_id else "",
            )
            linkage = join_unique(
                target_route.get("route_linkage_status", ""),
                queue_row.get("route_linkage_statuses", ""),
                "literature_expansion:source_linked_target_gene_promotion",
                "primary_layers_source_linked",
                "target_gene_named_in_full_sequence_queue",
                "receptor_to_intracellular_edge_asserted_as_graph_edge" if relay_edge_id else "receptor_to_intracellular_edge_not_asserted",
                "intracellular_to_tf_edge_asserted_as_graph_edge" if intracellular_tf_edge_id else "intracellular_to_tf_edge_not_asserted",
                "tf_to_target_edge_asserted_as_graph_edge" if tf_target_edge_id else "tf_to_target_edge_not_asserted",
                "end_to_end_chain_not_asserted_by_single_source",
                "evidence_route_only",
            )
            summary = (
                f"Source-linked target-gene route component for {queue_row['ligand_label']} > "
                f"{queue_row['receptor_label']}"
                + (f" > {queue_row['intracellular_continuation_label']}" if queue_row.get("intracellular_continuation_label") else " > ????")
                + (f" > {queue_row['transcription_factor_label']}" if queue_row.get("transcription_factor_label") else " > ????")
                + f" > {target_label}."
            )
            source_summary = source_record.get("evidence_summary", "").strip()
            if source_summary:
                summary = f"{summary} Supporting source-linked layer: {source_summary}"
            limitations = join_unique(
                source_record.get("limitations", ""),
                "The target-gene identity is promoted from an explicitly named source-linked queue component; target-specific attribution is not inferred beyond the retained primary locators.",
                "This route is composed evidence rather than a single-paper demonstration of every handoff; no new causal edge or confidence score is asserted.",
            )
            evidence_ids = join_unique(
                queue_row.get("evidence_ids", ""),
                target_route.get("evidence_ids", ""),
                target_route.get("route_evidence_id", ""),
                target_route.get("source_evidence_record_id", ""),
                queue_row.get("stable_primary_locators", ""),
            )
            rows.append(
                {
                    "expansion_id": f"M21B-LITEXP-TARGETPROMO-ALL-{len(rows) + 1:04d}",
                    "source_queue_id": target_route.get("source_queue_id", ""),
                    "route_status": "retained_evidence_route",
                    "path_expression": path_expression,
                    "route_tier": route_tier,
                    "known_layers": known_layers,
                    "missing_layers": join_unique(missing_layers, missing_edge_layers),
                    "intracellular_status": "source_supported_composed" if queue_row.get("intracellular_continuation_node_id") else "not_mapped",
                    "ligand_node_id": queue_row["ligand_node_id"],
                    "ligand_label": queue_row["ligand_label"],
                    "ligand_receptor_edge_id": lr_edge_id,
                    "receptor_node_id": queue_row["receptor_node_id"],
                    "receptor_label": queue_row["receptor_label"],
                    "receptor_intracellular_edge_id": relay_edge_id,
                    "intracellular_continuation_node_id": queue_row.get("intracellular_continuation_node_id", ""),
                    "intracellular_continuation_label": queue_row.get("intracellular_continuation_label", ""),
                    "intracellular_tf_edge_id": intracellular_tf_edge_id,
                    "transcription_factor_node_id": queue_row.get("transcription_factor_node_id", ""),
                    "transcription_factor_label": queue_row.get("transcription_factor_label", ""),
                    "tf_target_edge_id": tf_target_edge_id,
                    "target_gene_node_id": target_id,
                    "target_gene_label": target_label,
                    "target_output_form_id": "",
                    "output_node_id": target_id,
                    "output_label": output_label,
                    "output_form_id": "",
                    "bridge_id": "",
                    "pathway_name": target_route.get("pathway_name", "") or queue_row.get("pathway_names", ""),
                    "input_evidence_type": "primary_layer_evidence_route_composition",
                    "output_evidence_type": "primary_composed_target_gene_output",
                    "evidence_ids": evidence_ids,
                    "source_chain_id": f"source_linked_target_promotion:{queue_row['curation_candidate_id']}:{target_id}",
                    "source_evidence_record_id": target_route.get("source_evidence_record_id", ""),
                    "route_linkage_status": linkage,
                    "causal_status": "not_asserted",
                    "traversal_status": "evidence_route_not_causal",
                    "evidence_contract_version": "mechanism_evidence_v1",
                    "evidence_polarity": source_record.get("evidence_polarity", "supports"),
                    "negative_evidence_status": source_record.get("negative_evidence_status", "not_evaluated"),
                    "evidence_directness": "composite_primary_route",
                    "output_class": "gene_expression_or_transcription",
                    "primary_locator": join_unique(queue_row["stable_primary_locators"], source_record.get("primary_locator", "")),
                    "citation_note": f"Primary locators retained from full-sequence candidate {queue_row['curation_candidate_id']}; target-gene output {target_label} is separately addressable as evidence only.",
                    "evidence_summary": summary,
                    "limitations": limitations,
                    "curation_status": "curated_primary_route",
                    "species_context": source_record.get("species_context", ""),
                    "cell_type_context": source_record.get("cell_type_context", ""),
                    "compartment_context": source_record.get("compartment_context", ""),
                    "injury_context": source_record.get("injury_context", ""),
                    "context_scope": source_record.get("context_scope", ""),
                    "assay_or_perturbation": source_record.get("assay_or_perturbation", ""),
                    "effect_polarity": source_record.get("effect_polarity", ""),
                    "source_scope": "source_linked_composite_primary_evidence",
                }
            )

    if not rows:
        raise ValueError("No eligible source-linked target-gene routes found")
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "ligands": len({row["ligand_label"] for row in rows}), "skipped": skipped}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
