#!/usr/bin/env python3
"""Compose relay and TF identities from separate receptor-output routes.

This is the narrowest remaining exact composition for target-gene records that
lack both relay and TF identities: a source-linked relay-to-output route and a
separate source-linked TF-to-output route must exist for the same ligand and
receptor.  The two output observations do not assert a relay-to-TF handoff or
the target-specific endpoint.  No graph edge, causal assertion, or confidence
score is created.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
from collections import defaultdict
from pathlib import Path


PARTIAL_PATH = "ligand>receptor>????>????>target_gene_expression"
RELAY_OUTPUT_PATH = "ligand>receptor>intracellular>????>output"
TF_OUTPUT_PATH = "ligand>receptor>????>TF>output"
FULL_PATH = "ligand>receptor>intracellular>TF>target_gene_expression"
FULL_TIER = "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges"


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


def matching_edge(candidate_ids: str, edges: dict[str, dict[str, str]], source: str, target: str) -> str:
    for edge_id in split_values(candidate_ids):
        edge = edges.get(edge_id)
        if edge and edge["source_node_id"] == source and edge["target_node_id"] == target:
            return edge_id
    return ""


def make_row(
    partial: dict[str, str],
    relay_template: dict[str, str],
    tf_template: dict[str, str],
    edges: dict[str, dict[str, str]],
    downstream_evidence: dict[str, dict[str, str]],
    ordinal: int,
) -> dict[str, str]:
    ligand = partial["ligand_node_id"]
    receptor = partial["receptor_node_id"]
    relay = relay_template["intracellular_continuation_node_id"]
    tf = tf_template["transcription_factor_node_id"]
    target = partial["target_gene_node_id"]
    lr_edge = matching_edge(partial.get("ligand_receptor_edge_id", ""), edges, ligand, receptor)
    relay_edge = matching_edge(relay_template.get("receptor_intracellular_edge_id", ""), edges, receptor, relay)
    tf_target_edge = matching_edge(partial.get("tf_target_edge_id", ""), edges, tf, target)
    missing_layers = join_unique(
        "receptor_to_intracellular_edge" if not relay_edge else "",
        "intracellular_to_tf_edge",
        "tf_to_target_edge" if not tf_target_edge else "",
    )
    partial_source = downstream_evidence.get(partial.get("source_evidence_record_id", ""), {})
    relay_source = downstream_evidence.get(relay_template.get("source_evidence_record_id", ""), {})
    tf_source = downstream_evidence.get(tf_template.get("source_evidence_record_id", ""), {})
    linkage = join_unique(
        partial.get("route_linkage_status", ""),
        relay_template.get("route_linkage_status", ""),
        tf_template.get("route_linkage_status", ""),
        "literature_expansion:source_linked_split_output_promotion",
        "separate_relay_and_tf_output_templates",
        "relay_identity_supported_by_receptor_output_route",
        "tf_identity_supported_by_receptor_output_route",
        "target_specific_output_not_asserted_by_templates",
        "receptor_to_intracellular_edge_asserted_as_graph_edge" if relay_edge else "receptor_to_intracellular_edge_not_asserted",
        "intracellular_to_tf_edge_not_asserted",
        "tf_to_target_edge_asserted_as_graph_edge" if tf_target_edge else "tf_to_target_edge_not_asserted",
        "end_to_end_chain_not_asserted_by_single_source",
        "evidence_route_only",
    )
    summary = partial_source.get("evidence_summary", "").strip() or (
        f"Source-linked target-gene route component for {partial['ligand_label']} > {partial['receptor_label']} > ???? > ???? > {partial['target_gene_label']}."
    )
    limitations = join_unique(
        partial_source.get("limitations", ""),
        relay_source.get("limitations", ""),
        tf_source.get("limitations", ""),
        "Relay and TF identities are composed from separate source-linked output routes for the same ligand and receptor; neither output observation asserts the target-gene endpoint or the relay-to-TF handoff.",
        "This is composed evidence rather than a single-paper demonstration of every handoff; no new causal edge or confidence score is asserted.",
        "The original partial target-gene route is retained separately for provenance.",
    )
    row = dict(partial)
    row.update(
        {
            "expansion_id": f"M21B-LITEXP-SPLITPROMO-{ordinal:05d}",
            "path_expression": FULL_PATH,
            "route_tier": FULL_TIER,
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": missing_layers,
            "intracellular_status": "source_supported_composed",
            "ligand_receptor_edge_id": lr_edge,
            "receptor_intracellular_edge_id": relay_edge,
            "intracellular_continuation_node_id": relay,
            "intracellular_continuation_label": relay_template["intracellular_continuation_label"],
            "intracellular_tf_edge_id": "",
            "transcription_factor_node_id": tf,
            "transcription_factor_label": tf_template["transcription_factor_label"],
            "tf_target_edge_id": tf_target_edge,
            "evidence_ids": join_unique(
                partial.get("evidence_ids", ""), relay_template.get("evidence_ids", ""),
                tf_template.get("evidence_ids", ""), relay_template.get("route_evidence_id", ""),
                tf_template.get("route_evidence_id", ""), relay_template.get("source_evidence_record_id", ""),
                tf_template.get("source_evidence_record_id", ""),
            ),
            "source_chain_id": f"split_output_promotion:{partial['expansion_id']}:{relay_template['expansion_id']}:{tf_template['expansion_id']}",
            "route_linkage_status": linkage,
            "primary_locator": join_unique(partial.get("primary_locator", ""), relay_template.get("primary_locator", ""), tf_template.get("primary_locator", "")),
            "citation_note": (
                f"The target-gene route is retained from {partial['expansion_id']}; the relay and TF identities are "
                f"composed from separate source-linked output routes {relay_template['expansion_id']} and {tf_template['expansion_id']}. "
                "The relay-to-TF and target-specific handoffs remain unasserted."
            ),
            "evidence_summary": summary,
            "limitations": limitations,
            "source_scope": "source_linked_composite_primary_evidence",
        }
    )
    return row


def make_rows(bundle: Path) -> tuple[list[dict[str, str]], dict[str, int]]:
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    downstream_evidence = {row["record_id"]: row for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}
    expansions = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    existing_signatures = {
        (row.get("ligand_node_id", ""), row.get("receptor_node_id", ""), row.get("intracellular_continuation_node_id", ""), row.get("transcription_factor_node_id", ""), row.get("target_gene_node_id", ""), row.get("output_label", ""))
        for row in expansions
    }
    relay_by_lr: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    tf_by_lr: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in expansions:
        key = (row.get("ligand_node_id", ""), row.get("receptor_node_id", ""))
        if row.get("primary_locator") and row.get("path_expression") == RELAY_OUTPUT_PATH and row.get("intracellular_continuation_node_id"):
            relay_by_lr[key].append(row)
        if row.get("primary_locator") and row.get("path_expression") == TF_OUTPUT_PATH and row.get("transcription_factor_node_id"):
            tf_by_lr[key].append(row)
    rows: list[dict[str, str]] = []
    generated: set[tuple[str, ...]] = set()
    skipped = {"no_split_templates": 0, "duplicate_signature": 0, "missing_primary_locator": 0, "missing_source_linkage": 0}
    for partial in [row for row in expansions if row.get("path_expression") == PARTIAL_PATH]:
        if not partial.get("primary_locator"):
            skipped["missing_primary_locator"] += 1
            continue
        if not partial.get("source_queue_id") or not partial.get("source_evidence_record_id"):
            skipped["missing_source_linkage"] += 1
            continue
        key = (partial.get("ligand_node_id", ""), partial.get("receptor_node_id", ""))
        relays = relay_by_lr.get(key, [])
        tfs = tf_by_lr.get(key, [])
        if not relays or not tfs:
            skipped["no_split_templates"] += 1
            continue
        for relay_template in relays:
            for tf_template in tfs:
                signature = (partial["ligand_node_id"], partial["receptor_node_id"], relay_template["intracellular_continuation_node_id"], tf_template["transcription_factor_node_id"], partial["target_gene_node_id"], partial["output_label"])
                if signature in existing_signatures or signature in generated:
                    skipped["duplicate_signature"] += 1
                    continue
                generated.add(signature)
                rows.append(make_row(partial, relay_template, tf_template, edges, downstream_evidence, len(rows) + 1))
    return rows, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows, skipped = make_rows(args.bundle.resolve())
    if not rows:
        raise ValueError("No source-linked split-output promotions found")
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "rows": len(rows), "ligands": len({row['ligand_label'] for row in rows}), "skipped": skipped}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
