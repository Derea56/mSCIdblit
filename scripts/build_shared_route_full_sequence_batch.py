#!/usr/bin/env python3
"""Materialize full routes from exact shared route-evidence anchors.

The all-ligand queue aggregates route evidence by layer and can therefore keep
the target-gene output in one queue record while retaining the intracellular
and TF continuation in another.  This pass joins only records with the same
ligand/receptor node pair and at least one shared route-evidence identifier.
It does not infer a new graph edge or causal handoff: the resulting row is an
evidence-only composite and preserves the two source-linked layer sets.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import re
from collections import defaultdict
from pathlib import Path


FULL_PATH = "ligand>receptor>intracellular>TF>target_gene_expression"
FULL_TIER = "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges"
ID_PREFIX = "M21B-LITEXP-SHAREDROUTE-"


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
            if item and item not in seen:
                seen.add(item)
                result.append(item)
    return ";".join(result)


def next_ordinal(expansions: list[dict[str, str]]) -> int:
    values = [
        int(row["expansion_id"][len(ID_PREFIX):])
        for row in expansions
        if row.get("expansion_id", "").startswith(ID_PREFIX)
        and row["expansion_id"][len(ID_PREFIX):].isdigit()
    ]
    return max(values, default=0) + 1


def eligible_ligand(row: dict[str, str], roles: dict[str, set[str]]) -> bool:
    label = row.get("ligand_label", "").casefold()
    node_roles = roles.get(row.get("ligand_node_id", ""), set())
    excluded_markers = (
        "receptor", "site-set", " py", "itsm", "itim", "hem itam",
        "tir domain", "ralpha", "rbeta", "rgamma", "gp130", "slc6a",
    )
    return (
        bool(row.get("stable_primary_locators"))
        and bool(row.get("route_evidence_ids"))
        and "ligand" in node_roles
        and not {"receptor", "transcription_factor", "target_gene"} & node_roles
        and not any(marker in label for marker in excluded_markers)
        and label not in {"yap1", "wwtr1/taz", "ctnnb1-beta-catenin"}
    )


def matching_edge(
    edge_ids: str,
    edges: dict[str, dict[str, str]],
    source_node_id: str,
    target_node_id: str,
) -> str:
    for edge_id in split_values(edge_ids):
        edge = edges.get(edge_id)
        if edge and edge["source_node_id"] == source_node_id and edge["target_node_id"] == target_node_id:
            return edge_id
    return ""


def target_routes(
    queue_row: dict[str, str],
    routes: dict[str, dict[str, str]],
) -> list[dict[str, str]]:
    target_ids = set(split_values(queue_row.get("target_gene_node_ids", "")))
    if queue_row.get("target_gene_node_id"):
        target_ids.add(queue_row["target_gene_node_id"])
    return [
        routes[route_id]
        for route_id in split_values(queue_row.get("route_evidence_ids", ""))
        if route_id in routes
        and routes[route_id].get("target_gene_node_id") in target_ids
        and routes[route_id].get("target_gene_node_id")
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    bundle = args.bundle.resolve()

    queue = read_tsv(bundle / "mechanism_full_sequence_curation_queue.tsv.gz")
    route_rows = read_tsv(bundle / "mechanism_signaling_route_evidence.tsv.gz")
    routes = {row["route_evidence_id"]: row for row in route_rows}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    downstream_queue = {row["queue_id"] for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")}
    downstream_evidence = {
        row["record_id"]: row
        for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")
    }
    roles: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(bundle / "mechanism_node_roles.tsv"):
        roles[row["node_id"]].add(row["role"])
    expansions = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    existing_signatures = {
        tuple(row.get(field, "") for field in (
            "ligand_node_id", "receptor_node_id", "intracellular_continuation_node_id",
            "transcription_factor_node_id", "target_gene_node_id", "output_label",
        ))
        for row in expansions
    }

    by_lr: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in queue:
        if eligible_ligand(row, roles):
            by_lr[(row.get("ligand_node_id", ""), row.get("receptor_node_id", ""))].append(row)

    templates: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    targets: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for key, rows in by_lr.items():
        for row in rows:
            if row.get("intracellular_continuation_node_id") and row.get("transcription_factor_node_id"):
                templates[key].append(row)
            if row.get("target_gene_node_ids") or row.get("target_gene_node_id"):
                targets[key].append(row)

    rows: list[dict[str, str]] = []
    generated: set[tuple[str, ...]] = set()
    ordinal = next_ordinal(expansions)
    skipped = {"no_shared_route": 0, "no_target_route": 0, "existing_signature": 0}

    for key, target_rows in targets.items():
        for target_row in target_rows:
            output_routes = target_routes(target_row, routes)
            if not output_routes:
                skipped["no_target_route"] += 1
                continue
            target_route_ids = set(split_values(target_row.get("route_evidence_ids", "")))
            for template_row in templates.get(key, []):
                shared_route_ids = target_route_ids & set(split_values(template_row.get("route_evidence_ids", "")))
                if not shared_route_ids:
                    skipped["no_shared_route"] += 1
                    continue
                for output_route in output_routes:
                    relay_id = template_row["intracellular_continuation_node_id"]
                    tf_id = template_row["transcription_factor_node_id"]
                    target_id = output_route["target_gene_node_id"]
                    output_label = output_route.get("output_label", "") or output_route.get("target_gene_label", "")
                    signature = (
                        key[0], key[1], relay_id, tf_id, target_id, output_label,
                    )
                    if signature in existing_signatures or signature in generated:
                        skipped["existing_signature"] += 1
                        continue
                    generated.add(signature)
                    shared_route_id = sorted(shared_route_ids)[0]
                    shared_route = routes[shared_route_id]
                    source_queue_id = output_route.get("source_queue_id", "") or shared_route.get("source_queue_id", "")
                    source_record_id = output_route.get("source_evidence_record_id", "") or shared_route.get("source_evidence_record_id", "")
                    source_record = downstream_evidence.get(source_record_id, {})
                    graph_linked = not source_queue_id or not source_record_id
                    lr_edge_id = matching_edge(
                        join_unique(target_row.get("ligand_receptor_edge_ids", ""), output_route.get("ligand_receptor_edge_id", "")),
                        edges, key[0], key[1],
                    )
                    relay_edge_id = matching_edge(
                        join_unique(template_row.get("receptor_intracellular_edge_ids", ""), output_route.get("receptor_intracellular_edge_id", "")),
                        edges, key[1], relay_id,
                    )
                    intracellular_tf_edge_id = matching_edge(
                        join_unique(template_row.get("intracellular_tf_edge_ids", ""), output_route.get("intracellular_tf_edge_id", "")),
                        edges, relay_id, tf_id,
                    )
                    tf_target_edge_id = matching_edge(
                        join_unique(target_row.get("tf_target_edge_ids", ""), output_route.get("tf_target_edge_id", "")),
                        edges, tf_id, target_id,
                    )
                    missing_layers = join_unique(
                        "receptor_to_intracellular_edge" if not relay_edge_id else "",
                        "intracellular_to_tf_edge" if not intracellular_tf_edge_id else "",
                        "tf_to_target_edge" if not tf_target_edge_id else "",
                    )
                    linkage = join_unique(
                        target_row.get("route_linkage_statuses", ""),
                        template_row.get("route_linkage_statuses", ""),
                        output_route.get("route_linkage_status", ""),
                        shared_route.get("route_linkage_status", ""),
                        "literature_expansion:shared_route_full_sequence_composition",
                        f"shared_route_evidence_anchor:{shared_route_id}",
                        "graph_linked_route_source" if graph_linked else "",
                        "end_to_end_chain_not_asserted_by_single_source",
                        "evidence_route_only",
                    )
                    summary = source_record.get("evidence_summary", "").strip() or (
                        f"Shared-route evidence composition for {target_row['ligand_label']} > "
                        f"{target_row['receptor_label']} > {template_row['intracellular_continuation_label']} > "
                        f"{template_row['transcription_factor_label']} > {output_route.get('target_gene_label', '')}."
                    )
                    limitations = join_unique(
                        source_record.get("limitations", ""),
                        "The target-gene output and intracellular/TF continuation share an exact route-evidence anchor, but the complete handoff remains a composed evidence route rather than a single-paper causal chain.",
                        "No new graph edge, causal assertion, or confidence score is created; mSCS must evaluate layer linkage and cell context.",
                    )
                    rows.append({
                        "expansion_id": f"{ID_PREFIX}{ordinal + len(rows):05d}",
                        "source_queue_id": source_queue_id,
                        "route_status": "retained_evidence_route",
                        "path_expression": FULL_PATH,
                        "route_tier": FULL_TIER,
                        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                        "missing_layers": missing_layers,
                        "intracellular_status": "source_supported_composed",
                        "ligand_node_id": key[0],
                        "ligand_label": target_row["ligand_label"],
                        "ligand_receptor_edge_id": lr_edge_id,
                        "receptor_node_id": key[1],
                        "receptor_label": target_row["receptor_label"],
                        "receptor_intracellular_edge_id": relay_edge_id,
                        "intracellular_continuation_node_id": relay_id,
                        "intracellular_continuation_label": template_row["intracellular_continuation_label"],
                        "intracellular_tf_edge_id": intracellular_tf_edge_id,
                        "transcription_factor_node_id": tf_id,
                        "transcription_factor_label": template_row["transcription_factor_label"],
                        "tf_target_edge_id": tf_target_edge_id,
                        "target_gene_node_id": target_id,
                        "target_gene_label": output_route.get("target_gene_label", ""),
                        "target_output_form_id": output_route.get("target_output_form_id", ""),
                        "output_node_id": output_route.get("output_node_id", "") or target_id,
                        "output_label": output_label,
                        "output_form_id": output_route.get("output_form_id", ""),
                        "bridge_id": output_route.get("bridge_id", ""),
                        "pathway_name": output_route.get("pathway_name", "") or template_row.get("pathway_names", "").split(";")[0],
                        "input_evidence_type": "primary_shared_route_evidence_composition",
                        "output_evidence_type": "primary_composed_downstream_output",
                        "evidence_ids": join_unique(
                            target_row.get("evidence_ids", ""), template_row.get("evidence_ids", ""),
                            output_route.get("evidence_ids", ""), shared_route.get("evidence_ids", ""),
                            source_record.get("source_evidence_ids", ""),
                        ),
                        "source_chain_id": f"shared_route_full_sequence:{target_row['curation_candidate_id']}:{template_row['curation_candidate_id']}:{shared_route_id}",
                        "source_evidence_record_id": source_record_id,
                        "route_linkage_status": linkage,
                        "causal_status": "not_asserted",
                        "traversal_status": "evidence_route_not_causal",
                        "evidence_contract_version": "mechanism_evidence_v1",
                        "evidence_polarity": source_record.get("evidence_polarity", "supports"),
                        "negative_evidence_status": source_record.get("negative_evidence_status", "not_evaluated"),
                        "evidence_directness": "composite_primary_route",
                        "output_class": "gene_expression_or_transcription",
                        "primary_locator": join_unique(
                            target_row.get("stable_primary_locators", ""),
                            template_row.get("stable_primary_locators", ""),
                            source_record.get("source_locator", ""),
                        ),
                        "citation_note": f"Primary locators and layer evidence retained from queue candidates {target_row['curation_candidate_id']} and {template_row['curation_candidate_id']}; shared route anchor {shared_route_id} is retained for auditability.",
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
                        "source_scope": "graph_linked_composite_primary_evidence" if graph_linked else "source_linked_composite_primary_evidence",
                    })

    if not rows:
        raise ValueError("No shared-route full-sequence compositions found")
    args.output.resolve().write_text(__import__("json").dumps(rows, indent=2) + "\n", encoding="utf-8")
    print({"rows": len(rows), "ligands": len({row["ligand_label"] for row in rows}), "skipped": skipped})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
