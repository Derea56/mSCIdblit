#!/usr/bin/env python3
"""Promote target routes from same ligand-receptor route components.

This pass uses source-linked routes with known intracellular and/or TF nodes as
component templates for unresolved target-gene routes with the exact same
ligand and receptor node identities.  It is intentionally broader than a
full-output template: the component source may terminate at an output, an
unresolved endpoint, or a different target.  The resulting route is therefore
marked as composed evidence and preserves all missing handoffs explicitly.
No graph edge, causal assertion, or confidence score is created.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
from collections import defaultdict
from pathlib import Path


PARTIAL_TF_PATH = "ligand>receptor>????>TF>target_gene_expression"
PARTIAL_BOTH_PATH = "ligand>receptor>????>????>target_gene_expression"
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
    tf_template: dict[str, str] | None,
    edges: dict[str, dict[str, str]],
    downstream_evidence: dict[str, dict[str, str]],
    ordinal: int,
) -> dict[str, str]:
    ligand = partial["ligand_node_id"]
    receptor = partial["receptor_node_id"]
    relay = relay_template["intracellular_continuation_node_id"]
    tf = partial.get("transcription_factor_node_id") or (tf_template or {}).get("transcription_factor_node_id", "")
    target = partial["target_gene_node_id"]
    lr_edge = matching_edge(partial.get("ligand_receptor_edge_id", ""), edges, ligand, receptor)
    relay_edge = matching_edge(relay_template.get("receptor_intracellular_edge_id", ""), edges, receptor, relay)
    tf_edge_candidates = join_unique(
        relay_template.get("intracellular_tf_edge_id", ""),
        (tf_template or {}).get("intracellular_tf_edge_id", ""),
    )
    intracellular_tf_edge = matching_edge(tf_edge_candidates, edges, relay, tf)
    tf_target_edge = matching_edge(partial.get("tf_target_edge_id", ""), edges, tf, target)
    missing_layers = join_unique(
        "receptor_to_intracellular_edge" if not relay_edge else "",
        "intracellular_to_tf_edge" if not intracellular_tf_edge else "",
        "tf_to_target_edge" if not tf_target_edge else "",
    )
    tf_missing = not partial.get("transcription_factor_node_id")
    template_row = tf_template or relay_template
    partial_source = downstream_evidence.get(partial.get("source_evidence_record_id", ""), {})
    relay_source = downstream_evidence.get(relay_template.get("source_evidence_record_id", ""), {})
    tf_source = downstream_evidence.get((tf_template or {}).get("source_evidence_record_id", ""), {})
    linkage = join_unique(
        partial.get("route_linkage_status", ""),
        relay_template.get("route_linkage_status", ""),
        (tf_template or {}).get("route_linkage_status", ""),
        "literature_expansion:source_linked_component_promotion",
        "exact_ligand_receptor_component_templates",
        "relay_identity_supported_by_source_linked_same_lr_route",
        "tf_identity_supported_by_source_linked_same_lr_route" if tf_missing else "tf_identity_retained_from_target_route",
        "target_specific_handoff_not_asserted_by_component_templates",
        "receptor_to_intracellular_edge_asserted_as_graph_edge" if relay_edge else "receptor_to_intracellular_edge_not_asserted",
        "intracellular_to_tf_edge_asserted_as_graph_edge" if intracellular_tf_edge else "intracellular_to_tf_edge_not_asserted",
        "tf_to_target_edge_asserted_as_graph_edge" if tf_target_edge else "tf_to_target_edge_not_asserted",
        "end_to_end_chain_not_asserted_by_single_source",
        "evidence_route_only",
    )
    summary = partial_source.get("evidence_summary", "").strip() or (
        f"Source-linked target-gene route component for {partial['ligand_label']} > {partial['receptor_label']} > "
        f"{partial.get('transcription_factor_label') or '????'} > {partial['target_gene_label']}."
    )
    limitations = join_unique(
        partial_source.get("limitations", ""),
        relay_source.get("limitations", ""),
        tf_source.get("limitations", ""),
        "The relay and, when unresolved in the target route, TF identity are carried from source-linked component routes for the same ligand and receptor; those component sources may terminate at different outputs or unresolved endpoints.",
        "This is composed evidence rather than a single-paper demonstration of every handoff; no new causal edge or confidence score is asserted.",
        "The original partial target-gene route is retained separately for provenance.",
    )
    evidence_ids = join_unique(
        partial.get("evidence_ids", ""), relay_template.get("evidence_ids", ""),
        (tf_template or {}).get("evidence_ids", ""), relay_template.get("route_evidence_id", ""),
        (tf_template or {}).get("route_evidence_id", ""), relay_template.get("source_evidence_record_id", ""),
        (tf_template or {}).get("source_evidence_record_id", ""),
    )
    locators = join_unique(
        partial.get("primary_locator", ""), relay_template.get("primary_locator", ""),
        (tf_template or {}).get("primary_locator", ""),
    )
    row = dict(partial)
    row.update(
        {
            "expansion_id": f"M21B-LITEXP-COMPONENTPROMO-{ordinal:05d}",
            "route_status": "retained_evidence_route",
            "path_expression": FULL_PATH,
            "route_tier": FULL_TIER,
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": missing_layers,
            "intracellular_status": "source_supported_composed",
            "ligand_receptor_edge_id": lr_edge,
            "receptor_intracellular_edge_id": relay_edge,
            "intracellular_continuation_node_id": relay,
            "intracellular_continuation_label": relay_template["intracellular_continuation_label"],
            "intracellular_tf_edge_id": intracellular_tf_edge,
            "transcription_factor_node_id": tf,
            "transcription_factor_label": partial.get("transcription_factor_label") or template_row.get("transcription_factor_label", ""),
            "tf_target_edge_id": tf_target_edge,
            "evidence_ids": evidence_ids,
            "source_chain_id": f"component_promotion:{partial['expansion_id']}:{relay_template['expansion_id']}:{(tf_template or {}).get('expansion_id', '')}",
            "route_linkage_status": linkage,
            "primary_locator": locators,
            "citation_note": (
                f"The target-gene route is retained from {partial['expansion_id']}; component identities are carried from "
                f"{relay_template['expansion_id']}"
                + (f" and {tf_template['expansion_id']}" if tf_template else "")
                + ". No new graph edge or target-specific causal handoff is asserted."
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
        if not row.get("primary_locator"):
            continue
        key = (row.get("ligand_node_id", ""), row.get("receptor_node_id", ""))
        if row.get("intracellular_continuation_node_id") and "intracellular" in row.get("path_expression", ""):
            relay_by_lr[key].append(row)
        if row.get("transcription_factor_node_id") and "TF" in row.get("path_expression", ""):
            tf_by_lr[key].append(row)

    rows: list[dict[str, str]] = []
    generated: set[tuple[str, ...]] = set()
    skipped = {"no_relay_template": 0, "no_tf_template": 0, "duplicate_signature": 0, "missing_primary_locator": 0, "missing_source_linkage": 0}
    for partial in [row for row in expansions if row.get("path_expression") in {PARTIAL_TF_PATH, PARTIAL_BOTH_PATH}]:
        if not partial.get("primary_locator"):
            skipped["missing_primary_locator"] += 1
            continue
        if not partial.get("source_queue_id") or not partial.get("source_evidence_record_id"):
            skipped["missing_source_linkage"] += 1
            continue
        key = (partial["ligand_node_id"], partial["receptor_node_id"])
        relays = relay_by_lr.get(key, [])
        if not relays:
            skipped["no_relay_template"] += 1
            continue
        if partial["path_expression"] == PARTIAL_TF_PATH:
            templates = [(relay, None) for relay in relays]
        else:
            tfs = tf_by_lr.get(key, [])
            if not tfs:
                skipped["no_tf_template"] += 1
                continue
            templates = [(relay, tf) for relay in relays for tf in tfs]
        for relay_template, tf_template in templates:
            tf = partial.get("transcription_factor_node_id") or (tf_template or {}).get("transcription_factor_node_id", "")
            signature = (partial["ligand_node_id"], partial["receptor_node_id"], relay_template["intracellular_continuation_node_id"], tf, partial["target_gene_node_id"], partial["output_label"])
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
        raise ValueError("No source-linked component promotions found")
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "rows": len(rows), "ligands": len({row['ligand_label'] for row in rows}), "skipped": skipped}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
