#!/usr/bin/env python3
"""Materialize source-linked full-intermediate route annotations from the queue.

The full-sequence queue already combines independently source-linked layers for
many routes. This helper promotes only candidates that have explicit ligand,
receptor, intracellular, TF, and downstream labels plus stable primary
locators. The result is an evidence-only composition: it does not assert that
one paper demonstrated the entire chain and it never creates graph edges.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
from pathlib import Path

try:
    from .mechanism_evidence_contract import normalize_output_class
except ImportError:  # pragma: no cover - direct script execution
    from mechanism_evidence_contract import normalize_output_class


ROUTE_FIELDS = (
    "route_evidence_id", "route_status", "route_tier", "path_expression", "known_layers",
    "missing_layers", "ligand_node_id", "ligand_label", "ligand_receptor_edge_id",
    "receptor_node_id", "receptor_label", "receptor_intracellular_edge_id",
    "intracellular_continuation_node_id", "intracellular_continuation_label",
    "intracellular_tf_edge_id", "transcription_factor_node_id", "transcription_factor_label",
    "tf_target_edge_id", "target_gene_node_id", "target_gene_label", "output_label",
    "output_node_id", "pathway_name", "evidence_ids", "source_queue_id", "source_chain_id",
    "source_evidence_record_id", "source_scope", "route_linkage_status", "causal_status",
    "traversal_status",
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=0)
    return parser.parse_args()


def split_values(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def first_valid(values: list[str], valid: set[str]) -> str:
    return next((value for value in values if value in valid), "")


def join_unique(*values: str) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in split_values(value):
            if item not in seen:
                seen.add(item)
                result.append(item)
    return ";".join(result)


def main() -> int:
    args = parse_args()
    bundle = args.bundle_dir.resolve()
    full_queue = read_tsv(bundle / "mechanism_full_sequence_curation_queue.tsv.gz")
    route_rows = read_tsv(bundle / "mechanism_signaling_route_evidence.tsv.gz")
    downstream_queue = read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")
    downstream_evidence = read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")

    route_by_id = {row["route_evidence_id"]: row for row in route_rows}
    graph_edges = {
        row["edge_id"]: row
        for row in read_tsv(bundle / "mechanism_edges.tsv")
    }
    valid_queue_ids = {row["queue_id"] for row in downstream_queue}
    evidence_by_id = {row["record_id"]: row for row in downstream_evidence}
    existing_expansions = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    existing_signatures = {
        tuple(row.get(field, "") for field in (
            "ligand_node_id", "receptor_node_id", "intracellular_continuation_node_id",
            "transcription_factor_node_id", "target_gene_node_id", "output_label",
        ))
        for row in existing_expansions
    }
    existing_full_sequence_numbers = [
        int(row["expansion_id"].rsplit("-", 1)[1])
        for row in existing_expansions
        if row.get("expansion_id", "").startswith("M21B-LITEXP-FULLSEQ-")
        and row["expansion_id"].rsplit("-", 1)[-1].isdigit()
    ]
    full_sequence_start = max(existing_full_sequence_numbers, default=0) + 1

    candidates: list[tuple[dict[str, str], dict[str, str], dict[str, str]]] = []
    skipped = {"missing_layer": 0, "missing_locator": 0, "missing_route_source": 0, "already_present": 0}
    for row in full_queue:
        if not all(
            row.get(field, "")
            for field in (
                "ligand_node_id", "ligand_label", "receptor_node_id", "receptor_label",
                "intracellular_continuation_node_id", "intracellular_continuation_label",
                "transcription_factor_node_id", "transcription_factor_label", "output_labels",
            )
        ):
            skipped["missing_layer"] += 1
            continue
        if not row.get("stable_primary_locators"):
            skipped["missing_locator"] += 1
            continue

        source_route = next(
            (
                route_by_id[route_id]
                for route_id in split_values(row.get("route_evidence_ids", ""))
                if route_id in route_by_id
                and route_by_id[route_id].get("source_queue_id") in valid_queue_ids
                and route_by_id[route_id].get("source_evidence_record_id") in evidence_by_id
            ),
            None,
        )
        if source_route is None:
            skipped["missing_route_source"] += 1
            continue
        signature = tuple(row.get(field, "") for field in (
            "ligand_node_id", "receptor_node_id", "intracellular_continuation_node_id",
            "transcription_factor_node_id", "target_gene_node_id", "output_label",
        ))
        if signature in existing_signatures:
            skipped["already_present"] += 1
            continue
        source_record = evidence_by_id[source_route["source_evidence_record_id"]]
        candidates.append((row, source_route, source_record))

    candidates.sort(key=lambda item: item[0]["curation_candidate_id"])
    if args.limit:
        candidates = candidates[: args.limit]
    if not candidates:
        raise ValueError("No eligible full-intermediate queue records found")

    rows: list[dict[str, str]] = []
    for index, (queue_row, source_route, source_record) in enumerate(candidates, start=1):
        target_gene_ids = split_values(queue_row.get("target_gene_node_ids", ""))
        target_gene_labels = split_values(queue_row.get("target_gene_labels", ""))
        has_target = bool(target_gene_ids or target_gene_labels)
        target_gene_node_id = target_gene_ids[0] if target_gene_ids else ""
        target_gene_label = target_gene_labels[0] if target_gene_labels else ""
        output_labels = split_values(queue_row.get("output_labels", ""))
        output_node_ids = split_values(queue_row.get("output_node_ids", ""))
        output_label = queue_row.get("output_label", "") or (output_labels[0] if output_labels else "")
        output_node_id = queue_row.get("output_node_id", "") or (output_node_ids[0] if output_node_ids else "")
        route_tier = (
            "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges"
            if has_target
            else "ligand_receptor_intracellular_tf_output_missing_target_gene"
        )
        path_expression = (
            "ligand>receptor>intracellular>TF>target_gene_expression"
            if has_target
            else "ligand>receptor>intracellular>TF>output"
        )
        known_layers = (
            "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression"
            if has_target
            else "ligand|receptor|intracellular_continuation|transcription_factor|output"
        )
        missing_layers = "" if has_target else "target_gene_expression"

        def matching_edge(field: str, source_node: str, target_node: str) -> str:
            if not source_node or not target_node:
                return ""
            candidates = split_values(queue_row.get(field, "")) + [source_route.get(field.replace("_ids", "_id"), "")]
            for edge_id in candidates:
                edge = graph_edges.get(edge_id)
                if edge and edge["source_node_id"] == source_node and edge["target_node_id"] == target_node:
                    return edge_id
            return ""

        edge_ids = {
            "ligand_receptor_edge_id": matching_edge(
                "ligand_receptor_edge_ids", queue_row["ligand_node_id"], queue_row["receptor_node_id"]
            ),
            "receptor_intracellular_edge_id": source_route.get("receptor_intracellular_edge_id", ""),
            "intracellular_tf_edge_id": source_route.get("intracellular_tf_edge_id", ""),
            "tf_target_edge_id": matching_edge(
                "tf_target_edge_ids", queue_row["transcription_factor_node_id"], target_gene_node_id
            ),
        }
        evidence_ids = join_unique(
            queue_row.get("evidence_ids", ""),
            source_route.get("evidence_ids", ""),
            source_route.get("source_evidence_record_id", ""),
            queue_row.get("stable_primary_locators", ""),
        )
        linkage = join_unique(
            queue_row.get("route_linkage_statuses", ""),
            "literature_expansion:full_intermediate_queue_composition",
            "primary_layers_source_linked",
            "end_to_end_chain_not_asserted_by_single_source",
        )
        summary = source_record.get("evidence_summary", "").strip()
        if not summary:
            summary = (
                f"Source-linked queue composition for {queue_row['ligand_label']} > "
                f"{queue_row['receptor_label']} > {queue_row['intracellular_continuation_label']} > "
                f"{queue_row['transcription_factor_label']} > {output_label}."
            )
        limitations = join_unique(
            source_record.get("limitations", ""),
            "This is a composed evidence route assembled from source-linked layers; no single source is asserted to demonstrate every handoff.",
            "The route remains non-causal and non-traversable; mSCS must evaluate layer linkage and cell context.",
        )
        rows.append({
            "expansion_id": f"M21B-LITEXP-FULLSEQ-{full_sequence_start + index - 1:04d}",
            "source_queue_id": source_route["source_queue_id"],
            "route_status": "retained_evidence_route",
            "path_expression": path_expression,
            "route_tier": route_tier,
            "known_layers": known_layers,
            "missing_layers": missing_layers,
            "intracellular_status": "source_supported_composed",
            "ligand_node_id": queue_row["ligand_node_id"],
            "ligand_label": queue_row["ligand_label"],
            "ligand_receptor_edge_id": edge_ids["ligand_receptor_edge_id"],
            "receptor_node_id": queue_row["receptor_node_id"],
            "receptor_label": queue_row["receptor_label"],
            "receptor_intracellular_edge_id": edge_ids["receptor_intracellular_edge_id"],
            "intracellular_continuation_node_id": queue_row["intracellular_continuation_node_id"],
            "intracellular_continuation_label": queue_row["intracellular_continuation_label"],
            "intracellular_tf_edge_id": edge_ids["intracellular_tf_edge_id"],
            "transcription_factor_node_id": queue_row["transcription_factor_node_id"],
            "transcription_factor_label": queue_row["transcription_factor_label"],
            "tf_target_edge_id": edge_ids["tf_target_edge_id"],
            "target_gene_node_id": target_gene_node_id,
            "target_gene_label": target_gene_label,
            "target_output_form_id": "",
            "output_node_id": output_node_id,
            "output_label": output_label,
            "output_form_id": "",
            "bridge_id": "",
            "pathway_name": split_values(queue_row.get("pathway_names", ""))[0] if queue_row.get("pathway_names") else "",
            "input_evidence_type": "primary_layer_evidence_route_composition",
            "output_evidence_type": "primary_composed_downstream_output",
            "evidence_ids": evidence_ids,
            "source_chain_id": f"full_sequence_queue:{queue_row['curation_candidate_id']}",
            "source_evidence_record_id": source_route["source_evidence_record_id"],
            "route_linkage_status": linkage,
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": source_record.get("evidence_polarity", "supports"),
            "negative_evidence_status": source_record.get("negative_evidence_status", "not_evaluated"),
            "evidence_directness": "composite_primary_route",
            "output_class": normalize_output_class(
                output_label=output_label,
                target_gene=target_gene_label,
            ),
            "primary_locator": queue_row["stable_primary_locators"],
            "citation_note": (
                f"Primary locators retained from full-sequence candidate {queue_row['curation_candidate_id']}; "
                "route layers remain separately source-linked."
            ),
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
            "source_scope": "composite_primary_evidence",
        })

    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "ligand_labels": len({row["ligand_label"] for row in rows}), "skipped": skipped}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
