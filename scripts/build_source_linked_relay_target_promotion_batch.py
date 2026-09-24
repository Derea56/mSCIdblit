#!/usr/bin/env python3
"""Promote unresolved intracellular layers using existing route evidence.

Some source-linked routes already identify a ligand, receptor, TF, and target
gene but leave the intracellular continuation unresolved.  This pass exposes
those routes with relay identities that are already present in another full
route for the exact same ligand, receptor, and TF node identities.

The target-gene source linkage remains attached to the original partial route;
the relay is explicitly marked as composed evidence.  This script does not
create graph edges, causal assertions, or confidence scores.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
from pathlib import Path


PARTIAL_PATH = "ligand>receptor>????>TF>target_gene_expression"
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
        for item in split_values(value):
            if item and item not in seen:
                seen.add(item)
                result.append(item)
    return ";".join(result)


def matching_edge(
    candidate_ids: str,
    edges: dict[str, dict[str, str]],
    source_node_id: str,
    target_node_id: str,
) -> str:
    for edge_id in split_values(candidate_ids):
        edge = edges.get(edge_id)
        if edge and edge["source_node_id"] == source_node_id and edge["target_node_id"] == target_node_id:
            return edge_id
    return ""


def source_record_for(
    row: dict[str, str],
    downstream_evidence: dict[str, dict[str, str]],
) -> dict[str, str]:
    return downstream_evidence.get(row.get("source_evidence_record_id", ""), {})


def make_row(
    partial: dict[str, str],
    template: dict[str, str],
    edges: dict[str, dict[str, str]],
    downstream_evidence: dict[str, dict[str, str]],
    exact_target: bool,
    ordinal: int,
) -> dict[str, str]:
    ligand_node_id = partial["ligand_node_id"]
    receptor_node_id = partial["receptor_node_id"]
    tf_node_id = partial["transcription_factor_node_id"]
    target_node_id = partial["target_gene_node_id"]
    relay_node_id = template["intracellular_continuation_node_id"]
    relay_edge_id = matching_edge(
        template.get("receptor_intracellular_edge_id", ""),
        edges,
        receptor_node_id,
        relay_node_id,
    )
    intracellular_tf_edge_id = matching_edge(
        template.get("intracellular_tf_edge_id", ""),
        edges,
        relay_node_id,
        tf_node_id,
    )
    tf_target_edge_id = matching_edge(
        partial.get("tf_target_edge_id", ""),
        edges,
        tf_node_id,
        target_node_id,
    )
    if not tf_target_edge_id and exact_target:
        tf_target_edge_id = matching_edge(
            template.get("tf_target_edge_id", ""),
            edges,
            tf_node_id,
            target_node_id,
        )

    missing_layers = join_unique(
        "receptor_to_intracellular_edge" if not relay_edge_id else "",
        "intracellular_to_tf_edge" if not intracellular_tf_edge_id else "",
        "tf_to_target_edge" if not tf_target_edge_id else "",
    )
    relation = (
        "exact_target_partial_route_relay_promotion"
        if exact_target
        else "same_ligand_receptor_tf_partial_route_relay_promotion"
    )
    partial_source = source_record_for(partial, downstream_evidence)
    template_source = source_record_for(template, downstream_evidence)
    summary = partial_source.get("evidence_summary", "").strip() or (
        f"Source-linked route component for {partial['ligand_label']} > "
        f"{partial['receptor_label']} > ???? > {partial['transcription_factor_label']} > "
        f"{partial['target_gene_label']}."
    )
    limitations = join_unique(
        partial_source.get("limitations", ""),
        template_source.get("limitations", ""),
        "The intracellular continuation is composed from an existing full route with the same ligand, receptor, and transcription-factor node identities; the partial route's source did not itself assert that relay.",
        "This is composed evidence rather than a single-paper demonstration of every handoff; no new causal edge or confidence score is asserted.",
        "The original partial target-gene route is retained separately for provenance.",
    )
    linkage = join_unique(
        partial.get("route_linkage_status", ""),
        template.get("route_linkage_status", ""),
        "literature_expansion:source_linked_relay_target_promotion",
        relation,
        "relay_identity_supported_by_existing_full_route",
        "receptor_to_intracellular_edge_asserted_as_graph_edge" if relay_edge_id else "receptor_to_intracellular_edge_not_asserted",
        "intracellular_to_tf_edge_asserted_as_graph_edge" if intracellular_tf_edge_id else "intracellular_to_tf_edge_not_asserted",
        "tf_to_target_edge_asserted_as_graph_edge" if tf_target_edge_id else "tf_to_target_edge_not_asserted",
        "end_to_end_chain_not_asserted_by_single_source",
        "evidence_route_only",
    )
    row = dict(partial)
    row.update(
        {
            "expansion_id": f"M21B-LITEXP-RELAYPROMO-{ordinal:05d}",
            "path_expression": FULL_PATH,
            "route_tier": FULL_TIER,
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": missing_layers,
            "intracellular_status": "source_supported_composed",
            "receptor_intracellular_edge_id": relay_edge_id,
            "intracellular_continuation_node_id": relay_node_id,
            "intracellular_continuation_label": template["intracellular_continuation_label"],
            "intracellular_tf_edge_id": intracellular_tf_edge_id,
            "tf_target_edge_id": tf_target_edge_id,
            "evidence_ids": join_unique(
                partial.get("evidence_ids", ""),
                template.get("evidence_ids", ""),
                template.get("route_evidence_id", ""),
                template.get("source_evidence_record_id", ""),
            ),
            "source_chain_id": f"relay_target_promotion:{partial['expansion_id']}:{template['expansion_id']}",
            "route_linkage_status": linkage,
            "primary_locator": join_unique(partial.get("primary_locator", ""), template.get("primary_locator", "")),
            "citation_note": (
                f"The target-gene route is retained from {partial['expansion_id']}; the intracellular continuation "
                f"{template['intracellular_continuation_label']} is composed from {template['expansion_id']} with the "
                "same ligand, receptor, and TF node identities. No new graph edge or causal handoff is asserted."
            ),
            "evidence_summary": summary,
            "limitations": limitations,
            "source_scope": "source_linked_composite_primary_evidence",
        }
    )
    return row


def make_rows(bundle: Path) -> tuple[list[dict[str, str]], dict[str, int]]:
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    route_rows = read_tsv(bundle / "mechanism_signaling_route_evidence.tsv.gz")
    downstream_evidence = {
        row["record_id"]: row
        for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")
    }
    expansions = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    existing_signatures = {
        (
            row.get("ligand_node_id", ""),
            row.get("receptor_node_id", ""),
            row.get("intracellular_continuation_node_id", ""),
            row.get("transcription_factor_node_id", ""),
            row.get("target_gene_node_id", ""),
            row.get("output_label", ""),
        )
        for row in expansions
    }
    partials = [row for row in expansions if row.get("path_expression") == PARTIAL_PATH]
    full_by_key: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    for row in expansions:
        if (
            row.get("path_expression") == FULL_PATH
            and row.get("intracellular_continuation_node_id")
            and row.get("ligand_node_id")
            and row.get("receptor_node_id")
            and row.get("transcription_factor_node_id")
            and row.get("primary_locator")
        ):
            key = (
                row["ligand_node_id"],
                row["receptor_node_id"],
                row["transcription_factor_node_id"],
            )
            full_by_key.setdefault(key, []).append(row)

    rows: list[dict[str, str]] = []
    generated_signatures: set[tuple[str, ...]] = set()
    skipped = {
        "partial_without_matching_full_route": 0,
        "duplicate_signature": 0,
        "missing_primary_locator": 0,
        "missing_source_linkage": 0,
    }
    for partial in partials:
        if not partial.get("primary_locator"):
            skipped["missing_primary_locator"] += 1
            continue
        if not partial.get("source_queue_id") or not partial.get("source_evidence_record_id"):
            skipped["missing_source_linkage"] += 1
            continue
        key = (
            partial.get("ligand_node_id", ""),
            partial.get("receptor_node_id", ""),
            partial.get("transcription_factor_node_id", ""),
        )
        templates = full_by_key.get(key, [])
        if not templates:
            skipped["partial_without_matching_full_route"] += 1
            continue
        for template in templates:
            signature = (
                partial.get("ligand_node_id", ""),
                partial.get("receptor_node_id", ""),
                template.get("intracellular_continuation_node_id", ""),
                partial.get("transcription_factor_node_id", ""),
                partial.get("target_gene_node_id", ""),
                partial.get("output_label", ""),
            )
            if signature in existing_signatures or signature in generated_signatures:
                skipped["duplicate_signature"] += 1
                continue
            generated_signatures.add(signature)
            exact_target = template.get("target_gene_node_id") == partial.get("target_gene_node_id")
            rows.append(
                make_row(
                    partial,
                    template,
                    edges,
                    downstream_evidence,
                    exact_target,
                    len(rows) + 1,
                )
            )
    return rows, skipped


def main() -> int:
    args = parse_args()
    rows, skipped = make_rows(args.bundle.resolve())
    if not rows:
        raise ValueError("No source-linked relay promotions found")
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.output.resolve()),
                "rows": len(rows),
                "ligands": len({row["ligand_label"] for row in rows}),
                "exact_target_promotions": sum("exact_target_partial_route_relay_promotion" in row["route_linkage_status"] for row in rows),
                "same_lr_tf_promotions": sum("same_ligand_receptor_tf_partial_route_relay_promotion" in row["route_linkage_status"] for row in rows),
                "skipped": skipped,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
