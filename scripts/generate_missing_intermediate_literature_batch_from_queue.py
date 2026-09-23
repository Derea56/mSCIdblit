#!/usr/bin/env python3
"""Promote source-linked receptor-proximal relays for routes missing an intermediate.

This is deliberately conservative. It selects only queue records with an
explicit TF and downstream layer, then inserts a receptor-proximal relay when
the current graph contains that exported edge with a stable primary locator.
The relay-to-TF handoff remains unasserted and the resulting route is evidence-
only; this helper never infers a missing edge or creates a graph edge.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
from collections import defaultdict
from pathlib import Path

try:
    from .mechanism_evidence_contract import normalize_output_class
except ImportError:  # pragma: no cover - direct script execution
    from mechanism_evidence_contract import normalize_output_class


RELAY_ALLOWLIST = {
    "JAK1", "JAK2", "JAK3", "TYK2", "JAK1/JAK3", "MYD88", "TRAF6",
    "TICAM2/TRAM", "RIPK2/RICK", "GNAI/O/Z", "GNAQ", "GNAS", "GNAI",
    "GNA12", "GNA13", "TRAF2:cIAP1/2 adaptor complex", "FCER1G/FcRgamma adaptor",
}
DISALLOWED_RELATIONS = {"binds_receptor", "induces_target_gene", "regulates_target_gene", "represses_target_gene"}


def read_tsv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", newline="", encoding="utf-8", errors="replace") as handle:
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    bundle = args.bundle_dir.resolve()
    queue = read_tsv(bundle / "mechanism_full_sequence_curation_queue.tsv.gz")
    routes = read_tsv(bundle / "mechanism_signaling_route_evidence.tsv.gz")
    downstream_queue = read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")
    downstream_evidence = read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")
    edges = read_tsv(bundle / "mechanism_edges.tsv")
    edge_sources = read_tsv(bundle / "mechanism_edge_sources.tsv")
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    role_rows = read_tsv(bundle / "mechanism_node_roles.tsv")
    roles: dict[str, set[str]] = defaultdict(set)
    for row in role_rows:
        roles[row["node_id"]].add(row["role"])

    route_by_id = {row["route_evidence_id"]: row for row in routes}
    valid_queue_ids = {row["queue_id"] for row in downstream_queue}
    evidence_by_id = {row["record_id"]: row for row in downstream_evidence}
    existing = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    existing_signatures = {
        tuple(row.get(field, "") for field in (
            "ligand_node_id", "receptor_node_id", "intracellular_continuation_node_id",
            "transcription_factor_node_id", "target_gene_node_id", "output_label",
        ))
        for row in existing
    }
    existing_relay_numbers = [
        int(row["expansion_id"].rsplit("-", 1)[1])
        for row in existing
        if row.get("expansion_id", "").startswith("M21B-LITEXP-RELAY-")
        and row["expansion_id"].rsplit("-", 1)[-1].isdigit()
    ]
    relay_start = max(existing_relay_numbers, default=0) + 1
    stable_by_edge: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in edge_sources:
        if row.get("source_locator_status") in {"stable", "stable_plus_local"} and row.get("source_locator"):
            stable_by_edge[row["edge_id"]].append(row)
    outgoing: dict[str, list[dict[str, str]]] = defaultdict(list)
    for edge in edges:
        outgoing[edge["source_node_id"]].append(edge)

    selected: list[tuple[dict[str, str], dict[str, str], dict[str, str], dict[str, str], list[dict[str, str]], bool]] = []
    selected_signatures: set[tuple[str, ...]] = set()
    for queue_row in queue:
        if queue_row.get("intracellular_continuation_label"):
            continue
        required = (
            "ligand_node_id", "ligand_label", "receptor_node_id", "receptor_label",
            "transcription_factor_node_id", "transcription_factor_label", "output_labels",
            "stable_primary_locators",
        )
        if not all(queue_row.get(field, "") for field in required):
            continue
        if "ligand" not in roles[queue_row["ligand_node_id"]] or "receptor" in roles[queue_row["ligand_node_id"]]:
            continue
        if "receptor" not in roles[queue_row["receptor_node_id"]] or "transcription_factor" in roles[queue_row["receptor_node_id"]]:
            continue
        if "transcription_factor" not in roles[queue_row["transcription_factor_node_id"]]:
            continue
        route = next(
            (
                route_by_id[route_id]
                for route_id in split_values(queue_row.get("route_evidence_ids", ""))
                if route_id in route_by_id
                and route_by_id[route_id].get("source_queue_id") in valid_queue_ids
                and route_by_id[route_id].get("source_evidence_record_id") in evidence_by_id
            ),
            None,
        )
        graph_linked = False
        if route is None:
            route = next(
                (
                    route_by_id[route_id]
                    for route_id in split_values(queue_row.get("route_evidence_ids", ""))
                    if route_id in route_by_id
                    and not route_by_id[route_id].get("source_queue_id")
                    and not route_by_id[route_id].get("source_evidence_record_id")
                    and "graph_edge_linked" in route_by_id[route_id].get("route_linkage_status", "")
                    and route_by_id[route_id].get("ligand_node_id") == queue_row["ligand_node_id"]
                    and route_by_id[route_id].get("receptor_node_id") == queue_row["receptor_node_id"]
                    and route_by_id[route_id].get("transcription_factor_node_id") == queue_row["transcription_factor_node_id"]
                ),
                None,
            )
            graph_linked = route is not None
        if route is None:
            continue
        source_record = {} if graph_linked else evidence_by_id[route["source_evidence_record_id"]]
        for edge in outgoing[queue_row["receptor_node_id"]]:
            relay_label = nodes.get(edge["target_node_id"], {}).get("canonical_label", "")
            if relay_label not in RELAY_ALLOWLIST or edge["relation_type"] in DISALLOWED_RELATIONS:
                continue
            if not stable_by_edge.get(edge["edge_id"]):
                continue
            target_ids = split_values(queue_row.get("target_gene_node_ids", ""))
            target_id = queue_row.get("target_gene_node_id", "") or (target_ids[0] if target_ids else "")
            output_label = queue_row.get("output_label", "") or (split_values(queue_row.get("output_labels", "")) or [""])[0]
            signature = (
                queue_row["ligand_node_id"], queue_row["receptor_node_id"], edge["target_node_id"],
                queue_row["transcription_factor_node_id"],
                target_id,
                output_label,
            )
            if signature in existing_signatures or signature in selected_signatures:
                continue
            selected_signatures.add(signature)
            selected.append((queue_row, route, source_record, edge, stable_by_edge[edge["edge_id"]], graph_linked))

    rows: list[dict[str, str]] = []
    for index, (queue_row, route, source_record, relay_edge, relay_sources, graph_linked) in enumerate(selected, start=1):
        target_ids = split_values(queue_row.get("target_gene_node_ids", ""))
        target_labels = split_values(queue_row.get("target_gene_labels", ""))
        target_id = queue_row.get("target_gene_node_id", "") or (target_ids[0] if target_ids else "")
        target_label = queue_row.get("target_gene_label", "") or (target_labels[0] if target_labels else "")
        output_label = queue_row.get("output_label", "") or (split_values(queue_row.get("output_labels", "")) or [""])[0]
        output_id = queue_row.get("output_node_id", "") or (split_values(queue_row.get("output_node_ids", "")) or [""])[0]
        has_target = bool(target_id or target_label)
        edge_source = relay_sources[0]
        route_tier = (
            "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges"
            if has_target else "ligand_receptor_intracellular_tf_output_missing_target_gene"
        )
        evidence_summary = join_unique(
            source_record.get("evidence_summary", ""),
            edge_source.get("evidence_summary", ""),
        )
        if not evidence_summary and graph_linked:
            evidence_summary = (
                f"Graph-linked primary-evidence composition for {queue_row['ligand_label']} > "
                f"{queue_row['receptor_label']} > {nodes[relay_edge['target_node_id']]['canonical_label']} > "
                f"{queue_row['transcription_factor_label']} > {output_label}; source locators are retained "
                "from the route queue and receptor-relay edge."
            )
        limitations = join_unique(
            source_record.get("limitations", ""),
            edge_source.get("limitations", ""),
            "Receptor-to-relay edge is source-linked; relay-to-TF handoff remains unasserted.",
            "This is a composed evidence route, not a claim that one source demonstrated every handoff.",
        )
        if graph_linked:
            limitations = join_unique(
                limitations,
                "The route is linked to graph-supported primary evidence rather than a downstream manual-evidence record; mSCS must evaluate the component linkage and context.",
            )
        rows.append({
            "expansion_id": f"M21B-LITEXP-RELAY-{relay_start + index - 1:04d}",
            "source_queue_id": route["source_queue_id"],
            "route_status": "retained_evidence_route",
            "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression" if has_target else "ligand>receptor>intracellular>TF>output",
            "route_tier": route_tier,
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression" if has_target else "ligand|receptor|intracellular_continuation|transcription_factor|output",
            "missing_layers": "" if has_target else "target_gene_expression",
            "intracellular_status": "source_supported_receptor_proximal",
            "ligand_node_id": queue_row["ligand_node_id"],
            "ligand_label": queue_row["ligand_label"],
            "ligand_receptor_edge_id": route.get("ligand_receptor_edge_id", ""),
            "receptor_node_id": queue_row["receptor_node_id"],
            "receptor_label": queue_row["receptor_label"],
            "receptor_intracellular_edge_id": relay_edge["edge_id"],
            "intracellular_continuation_node_id": relay_edge["target_node_id"],
            "intracellular_continuation_label": nodes[relay_edge["target_node_id"]]["canonical_label"],
            "intracellular_tf_edge_id": "",
            "transcription_factor_node_id": queue_row["transcription_factor_node_id"],
            "transcription_factor_label": queue_row["transcription_factor_label"],
            "tf_target_edge_id": "",
            "target_gene_node_id": target_id,
            "target_gene_label": target_label,
            "target_output_form_id": "",
            "output_node_id": output_id,
            "output_label": output_label,
            "output_form_id": "",
            "bridge_id": "",
            "pathway_name": (split_values(queue_row.get("pathway_names", "")) or [""])[0],
            "input_evidence_type": "primary_graph_linked_receptor_relay_and_downstream_evidence_composition" if graph_linked else "primary_receptor_relay_and_downstream_evidence_composition",
            "output_evidence_type": "primary_composed_downstream_output",
            "evidence_ids": join_unique(queue_row.get("evidence_ids", ""), route.get("evidence_ids", ""), route.get("source_evidence_record_id", ""), edge_source.get("evidence_id", ""), queue_row.get("stable_primary_locators", ""), edge_source.get("source_locator", "")),
            "source_chain_id": f"{'graph_linked_route' if graph_linked else 'missing_intermediate_queue'}:{queue_row['curation_candidate_id']}+{relay_edge['edge_id']}",
            "source_evidence_record_id": route.get("source_evidence_record_id", ""),
            "route_linkage_status": join_unique(queue_row.get("route_linkage_statuses", ""), "literature_expansion:source_linked_receptor_relay", "receptor_to_intracellular_edge_asserted_primary_source", "intracellular_to_tf_edge_not_asserted", "end_to_end_chain_not_asserted_by_single_source", "graph_linked_route_source" if graph_linked else ""),
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": source_record.get("evidence_polarity", "supports"),
            "negative_evidence_status": source_record.get("negative_evidence_status", "not_evaluated"),
            "evidence_directness": "composite_primary_route",
            "output_class": normalize_output_class(output_label=output_label, target_gene=target_label),
            "primary_locator": join_unique(queue_row["stable_primary_locators"], edge_source.get("source_locator", "")),
            "citation_note": f"Primary locators retained from {queue_row['curation_candidate_id']} and relay edge {relay_edge['edge_id']}; relay-to-TF remains explicitly unasserted.",
            "evidence_summary": evidence_summary,
            "limitations": limitations,
            "curation_status": "curated_primary_route",
            "species_context": source_record.get("species_context", "") or edge_source.get("species_support", ""),
            "cell_type_context": source_record.get("cell_type_context", "") or relay_edge.get("cell_type_context", ""),
            "compartment_context": source_record.get("compartment_context", "") or relay_edge.get("compartment_context", ""),
            "injury_context": source_record.get("injury_context", "") or relay_edge.get("injury_context", ""),
            "context_scope": source_record.get("context_scope", "") or relay_edge.get("context_scope", ""),
            "assay_or_perturbation": source_record.get("assay_or_perturbation", ""),
            "effect_polarity": relay_edge.get("effect_polarity", "") or source_record.get("effect_polarity", ""),
            "source_scope": "graph_linked_composite_primary_evidence" if graph_linked else "composite_primary_evidence",
        })

    if not rows:
        raise ValueError("No source-linked missing-intermediate routes found")
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "ligand_labels": len({row["ligand_label"] for row in rows})}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
