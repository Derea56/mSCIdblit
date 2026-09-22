#!/usr/bin/env python3
"""Add conservative cross-record intracellular/TF route compositions.

The base route audit composes evidence within one downstream queue record. A
small number of exact ligand-receptor edges have separately curated
receptor-proximal intracellular evidence and TF/output evidence. This helper
composes only those records when they share the same exported ligand-receptor
edge, and retains the component provenance in the resulting evidence row.

These rows are evidence-layer route hypotheses. They do not create graph
edges, assert a direct intracellular-to-TF edge, or assign confidence.
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from collections import Counter, defaultdict
from pathlib import Path


ROUTE_FILE = "mechanism_signaling_route_evidence.tsv"
SUMMARY_FILE = "cross_record_route_linkage_summary.json"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def tokens(value: str) -> set[str]:
    return {token for token in value.split("|") if token}


def join_unique(*values: str) -> str:
    output: list[str] = []
    seen: set[str] = set()
    for value in values:
        for token in value.split(";"):
            token = token.strip()
            if token and token not in seen:
                seen.add(token)
                output.append(token)
    return ";".join(output)


def route_signature(row: dict[str, str]) -> tuple[str, str, str, str, str]:
    return (
        row.get("ligand_receptor_edge_id", ""),
        row.get("intracellular_continuation_node_id", ""),
        row.get("transcription_factor_node_id", ""),
        row.get("output_label", ""),
        row.get("target_gene_label", ""),
    )


def next_id(rows: list[dict[str, str]]) -> int:
    values = []
    for row in rows:
        value = row.get("route_evidence_id", "")
        if value.startswith("XREC:") and value[5:].isdigit():
            values.append(int(value[5:]))
    return max(values, default=0) + 1


def compose_routes(rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], dict[str, object]]:
    by_edge: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        edge_id = row.get("ligand_receptor_edge_id", "")
        if edge_id and row.get("ligand_node_id") and row.get("receptor_node_id"):
            by_edge[edge_id].append(row)

    existing_signatures = {
        route_signature(row)
        for row in rows
        if {
            "ligand",
            "receptor",
            "intracellular_continuation",
            "transcription_factor",
            "output",
        }.issubset(tokens(row.get("known_layers", "")))
    }
    candidates: list[tuple[dict[str, str], dict[str, str]]] = []
    edge_ids: set[str] = set()
    for edge_id, edge_rows in by_edge.items():
        # The intracellular row must carry an explicit receptor-proximal edge
        # and continuation node. The second row must independently carry TF
        # and output evidence for the same exact ligand-receptor edge.
        intracellular_rows = [
            row
            for row in edge_rows
            if "intracellular_continuation" in tokens(row.get("known_layers", ""))
            and row.get("receptor_intracellular_edge_id")
            and row.get("intracellular_continuation_node_id")
        ]
        tf_output_rows = [
            row
            for row in edge_rows
            if {"transcription_factor", "output"}.issubset(tokens(row.get("known_layers", "")))
            and (row.get("transcription_factor_node_id") or row.get("transcription_factor_label"))
            and (row.get("output_label") or row.get("target_gene_label"))
        ]
        if not intracellular_rows or not tf_output_rows:
            continue
        edge_candidates: set[tuple[str, str, str, str]] = set()
        for intracellular in intracellular_rows:
            for tf_output in tf_output_rows:
                shared_evidence_ids = {
                    value
                    for value in intracellular.get("evidence_ids", "").split(";")
                    if value and value in set(tf_output.get("evidence_ids", "").split(";"))
                }
                # Different queue records can be composed only when their
                # stored evidence packets retain a common evidence identifier.
                # Exact LR identity alone is not enough to merge independent
                # receptor-proximal and TF/output studies.
                if not shared_evidence_ids:
                    continue
                signature = (
                    edge_id,
                    intracellular.get("intracellular_continuation_node_id", ""),
                    tf_output.get("transcription_factor_node_id", ""),
                    tf_output.get("output_label", ""),
                )
                if signature in edge_candidates:
                    continue
                edge_candidates.add(signature)
                probe = dict(tf_output)
                probe.update(
                    {
                        "intracellular_continuation_node_id": intracellular.get("intracellular_continuation_node_id", ""),
                        "output_label": tf_output.get("output_label", ""),
                        "target_gene_label": tf_output.get("target_gene_label", ""),
                    }
                )
                if route_signature(probe) in existing_signatures:
                    continue
                candidates.append((intracellular, tf_output))
                edge_ids.add(edge_id)

    additions: list[dict[str, str]] = []
    current = next_id(rows)
    for intracellular, tf_output in candidates:
        row = dict(tf_output)
        route_id = f"XREC:{current:06d}"
        current += 1
        row.update(
            {
                "route_evidence_id": route_id,
                "route_status": "retained_evidence_route",
                "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
                "path_expression": "ligand>receptor>intracellular>TF>output",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
                "missing_layers": "target_gene_expression",
                "intracellular_status": "explicit_receptor_proximal_edge",
                "intracellular_continuation_node_id": intracellular.get("intracellular_continuation_node_id", ""),
                "intracellular_continuation_label": intracellular.get("intracellular_continuation_label", ""),
                "receptor_intracellular_edge_id": intracellular.get("receptor_intracellular_edge_id", ""),
                "intracellular_tf_edge_id": "",
                "tf_target_edge_id": "",
                "evidence_ids": join_unique(
                    intracellular.get("evidence_ids", ""),
                    tf_output.get("evidence_ids", ""),
                ),
                # The exported schema permits one queue/evidence-record
                # anchor per route row. Keep the TF/output record as the
                # primary anchor and retain the intracellular component in
                # evidence_ids plus the composite source-chain identifier.
                "source_queue_id": tf_output.get("source_queue_id", ""),
                "source_evidence_record_id": tf_output.get("source_evidence_record_id", ""),
                "source_chain_id": (
                    f"cross_record:{tf_output.get('ligand_receptor_edge_id', '')}:"
                    f"{intracellular.get('intracellular_continuation_node_id', '')}:"
                    f"{tf_output.get('transcription_factor_node_id', '')}:"
                    f"{intracellular.get('source_evidence_record_id', '')}+"
                    f"{tf_output.get('source_evidence_record_id', '')}"
                ),
                "input_evidence_type": "cross_record_exact_lr_route_composition",
                "output_evidence_type": "cross_record_tf_output_evidence",
                "route_linkage_status": (
                    "cross_record_exact_lr_pair;"
                    "shared_evidence_anchor;"
                    "receptor_proximal_and_tf_output_evidence_composed;"
                    "intracellular_to_tf_edge_not_asserted"
                ),
                "evidence_directness": "coobserved_source_claim",
                "assay_or_perturbation": join_unique(
                    intracellular.get("assay_or_perturbation", ""),
                    tf_output.get("assay_or_perturbation", ""),
                ),
            }
        )
        additions.append(row)

    summary = {
        "source_route_rows": len(rows),
        "cross_record_route_rows_added": len(additions),
        "distinct_ligand_receptor_edges_linked": len(edge_ids),
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "linkage_policy": (
            "Exact exported ligand-receptor edge plus separately curated receptor-proximal "
            "intracellular evidence and TF/output evidence with a shared evidence identifier; "
            "no intracellular-to-TF edge or causal relationship is asserted."
        ),
    }
    return additions, summary


def update_route_audit(path: Path, rows: list[dict[str, str]], additions: int) -> None:
    """Keep the route-evidence section of the inherited audit synchronized."""
    if not path.exists():
        return
    audit = json.loads(path.read_text(encoding="utf-8"))
    counts = audit.setdefault("signaling_route_evidence_counts", {})
    counts["route_evidence_record_count"] = len(rows)
    counts["route_evidence_tier_counts"] = dict(
        sorted(Counter(row.get("route_tier", "") for row in rows).items())
    )
    counts["route_evidence_unique_ligands"] = len(
        {row.get("ligand_label", "") for row in rows if row.get("ligand_label")}
    )
    counts["route_evidence_unique_target_genes"] = len(
        {
            row.get("target_gene_label", "")
            for row in rows
            if row.get("target_gene_label")
        }
    )
    counts["route_evidence_unique_transcription_factors"] = len(
        {
            row.get("transcription_factor_label", "")
            for row in rows
            if row.get("transcription_factor_label")
        }
    )
    counts["route_evidence_unique_outputs"] = len(
        {
            row.get("output_label", "") or row.get("target_gene_label", "")
            for row in rows
            if row.get("output_label") or row.get("target_gene_label")
        }
    )
    counts["route_linkage_status_counts"] = dict(
        sorted(Counter(row.get("route_linkage_status", "") for row in rows).items())
    )
    counts["coobserved_intracellular_tf_output_route_record_count"] = (
        counts.get("coobserved_intracellular_tf_output_route_record_count", 0) + additions
    )
    path.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-bundle", type=Path, required=True)
    parser.add_argument("--output-bundle", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source_bundle.resolve()
    output = args.output_bundle.resolve()
    if output.exists():
        raise FileExistsError(f"Output bundle already exists: {output}")
    shutil.copytree(source, output)

    route_path = output / ROUTE_FILE
    rows = read_tsv(route_path)
    additions, summary = compose_routes(rows)
    fields = list(rows[0])
    write_tsv(route_path, fields, rows + additions)
    update_route_audit(output / "full_signaling_chain_audit.json", rows + additions, len(additions))

    metadata_path = output / "bundle_metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["release_id"] = args.release_id
    metadata.setdefault("counts", {})["signaling_route_evidence"] = len(rows) + len(additions)
    metadata.setdefault("graph_policy", {})["cross_record_route_composition_is_evidence_layer_only"] = True
    statement = (
        "Cross-record route compositions require an exact exported ligand-receptor edge plus "
        "separately curated receptor-proximal and TF/output evidence with a shared evidence "
        "identifier; they do "
        "not create intracellular-to-TF graph edges, causal assertions, or confidence scores."
    )
    if statement not in metadata.setdefault("accuracy_contract", []):
        metadata["accuracy_contract"].append(statement)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    summary["source_bundle"] = str(source)
    summary["output_bundle"] = str(output)
    summary["release_id"] = args.release_id
    (output / SUMMARY_FILE).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
