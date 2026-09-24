#!/usr/bin/env python3
"""Expand source-linked queue target lists into individual full-sequence routes.

The full-sequence queue can aggregate several graph-supported target outputs in
one row.  This pass promotes each explicitly named target-gene component into
its own evidence route when the ligand, receptor, intracellular continuation,
TF, target node, and primary locators are already present.  It does not infer
an intracellular-to-TF or TF-to-target causal edge.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import re
from pathlib import Path


FULL_PATH = "ligand>receptor>intracellular>TF>target_gene_expression"
FULL_TIER = "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges"


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
        for item in value.split(";"):
            item = item.strip()
            if item and item not in seen:
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
    skipped = {"missing_required_layer": 0, "target_label_mismatch": 0, "already_present": 0, "missing_route_source": 0}
    for queue_row in queue_rows:
        required = (
            queue_row.get("ligand_node_id", ""),
            queue_row.get("ligand_label", ""),
            queue_row.get("receptor_node_id", ""),
            queue_row.get("receptor_label", ""),
            queue_row.get("intracellular_continuation_node_id", ""),
            queue_row.get("intracellular_continuation_label", ""),
            queue_row.get("transcription_factor_node_id", ""),
            queue_row.get("transcription_factor_label", ""),
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

        candidate_routes = [route_by_id[route_id] for route_id in split_values(queue_row.get("route_evidence_ids", "")) if route_id in route_by_id]
        source_routes = [
            route
            for route in candidate_routes
            if (
                route.get("source_queue_id") in downstream_queue
                and route.get("source_evidence_record_id") in downstream_evidence
            )
            or "graph_supported_" in route.get("route_linkage_status", "")
        ]
        if not source_routes:
            skipped["missing_route_source"] += 1
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
                queue_row["intracellular_continuation_node_id"],
                queue_row["transcription_factor_node_id"],
                target_id,
                output_label,
            )
            if signature in existing_signatures:
                skipped["already_present"] += 1
                continue

            source_record = downstream_evidence.get(target_route.get("source_evidence_record_id", ""), {})
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
                queue_row["intracellular_continuation_node_id"],
            )
            intracellular_tf_edge_id = matching_edge(
                queue_row.get("intracellular_tf_edge_ids", ""),
                target_route.get("intracellular_tf_edge_id", ""),
                edges,
                queue_row["intracellular_continuation_node_id"],
                queue_row["transcription_factor_node_id"],
            )
            tf_target_edge_id = matching_edge(
                queue_row.get("tf_target_edge_ids", ""),
                target_route.get("tf_target_edge_id", ""),
                edges,
                queue_row["transcription_factor_node_id"],
                target_id,
            )
            graph_linked = "graph_supported_" in target_route.get("route_linkage_status", "")
            linkage = join_unique(
                target_route.get("route_linkage_status", ""),
                queue_row.get("route_linkage_statuses", ""),
                "literature_expansion:full_sequence_target_gene_promotion",
                "primary_layers_source_linked",
                "graph_linked_route_source" if graph_linked else "",
                "receptor_to_intracellular_edge_asserted_as_graph_edge" if relay_edge_id else "receptor_to_intracellular_edge_not_asserted",
                "intracellular_to_tf_edge_asserted_as_graph_edge" if intracellular_tf_edge_id else "intracellular_to_tf_edge_not_asserted",
                "tf_to_target_edge_asserted_as_graph_edge" if tf_target_edge_id else "tf_to_target_edge_not_asserted",
                "output_edge_not_asserted_primary_output_evidence_only",
                "end_to_end_chain_not_asserted_by_single_source",
                "evidence_route_only",
            )
            evidence_ids = join_unique(
                queue_row.get("evidence_ids", ""),
                target_route.get("evidence_ids", ""),
                target_route.get("route_evidence_id", ""),
                target_route.get("source_evidence_record_id", ""),
                queue_row.get("stable_primary_locators", ""),
            )
            summary = source_record.get("evidence_summary", "").strip() or (
                f"Source-linked route composition for {queue_row['ligand_label']} > "
                f"{queue_row['receptor_label']} > {queue_row['intracellular_continuation_label']} > "
                f"{queue_row['transcription_factor_label']} > {target_label}."
            )
            limitations = join_unique(
                source_record.get("limitations", ""),
                "The target-gene identity is promoted from an explicitly named source-linked output component in the full-sequence queue.",
                "The route is composed evidence rather than a single-paper demonstration of every handoff; no new causal edge or confidence score is asserted.",
            )
            rows.append(
                {
                    "expansion_id": f"M21B-LITEXP-TARGETPROMO-{len(rows) + 1:04d}",
                    "source_queue_id": target_route.get("source_queue_id", ""),
                    "route_status": "retained_evidence_route",
                    "path_expression": FULL_PATH,
                    "route_tier": FULL_TIER,
                    "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                    "missing_layers": join_unique(
                        "intracellular_to_tf_edge" if not intracellular_tf_edge_id else "",
                        "tf_to_target_edge" if not tf_target_edge_id else "",
                    ),
                    "intracellular_status": "source_supported_composed",
                    "ligand_node_id": queue_row["ligand_node_id"],
                    "ligand_label": queue_row["ligand_label"],
                    "ligand_receptor_edge_id": lr_edge_id,
                    "receptor_node_id": queue_row["receptor_node_id"],
                    "receptor_label": queue_row["receptor_label"],
                    "receptor_intracellular_edge_id": relay_edge_id,
                    "intracellular_continuation_node_id": queue_row["intracellular_continuation_node_id"],
                    "intracellular_continuation_label": queue_row["intracellular_continuation_label"],
                    "intracellular_tf_edge_id": intracellular_tf_edge_id,
                    "transcription_factor_node_id": queue_row["transcription_factor_node_id"],
                    "transcription_factor_label": queue_row["transcription_factor_label"],
                    "tf_target_edge_id": tf_target_edge_id,
                    "target_gene_node_id": target_id,
                    "target_gene_label": target_label,
                    "target_output_form_id": "",
                    "output_node_id": target_id,
                    "output_label": output_label,
                    "output_form_id": "",
                    "bridge_id": "",
                    "pathway_name": target_route.get("pathway_name", "") or queue_row.get("pathway_names", ""),
                    "input_evidence_type": "primary_graph_linked_layer_evidence_route_composition" if graph_linked else "primary_layer_evidence_route_composition",
                    "output_evidence_type": "primary_composed_target_gene_output",
                    "evidence_ids": evidence_ids,
                    "source_chain_id": f"full_sequence_target_promotion:{queue_row['curation_candidate_id']}:{target_id}",
                    "source_evidence_record_id": target_route.get("source_evidence_record_id", ""),
                    "route_linkage_status": linkage,
                    "causal_status": "not_asserted",
                    "traversal_status": "evidence_route_not_causal",
                    "evidence_contract_version": "mechanism_evidence_v1",
                    "evidence_polarity": source_record.get("evidence_polarity", "supports"),
                    "negative_evidence_status": source_record.get("negative_evidence_status", "not_evaluated"),
                    "evidence_directness": "composite_primary_route",
                    "output_class": "gene_expression_or_transcription",
                    "primary_locator": queue_row["stable_primary_locators"],
                    "citation_note": f"Primary locators retained from full-sequence candidate {queue_row['curation_candidate_id']}; target-gene output {target_label} is retained as a separately addressable evidence route.",
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
                    "source_scope": "graph_linked_composite_primary_evidence" if graph_linked else "composite_primary_evidence",
                }
            )

    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "ligands": len({row["ligand_label"] for row in rows}), "skipped": skipped}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
