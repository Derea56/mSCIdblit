#!/usr/bin/env python3
"""Promote unresolved target routes from source-linked output templates.

Some routes have a primary-supported target-gene output but no intracellular
or TF identity, while another primary-supported route for the same ligand and
receptor reaches a generic output through an intracellular relay and TF.  This
pass carries those identities over as composed evidence.  It never treats the
generic output route as proof of the target-specific handoff and never creates
graph edges, causal assertions, or confidence scores.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
from collections import defaultdict
from pathlib import Path


FULL_PATH = "ligand>receptor>intracellular>TF>target_gene_expression"
FULL_OUTPUT_PATH = "ligand>receptor>intracellular>TF>output"
PARTIAL_TF_PATH = "ligand>receptor>????>TF>target_gene_expression"
PARTIAL_BOTH_PATH = "ligand>receptor>????>????>target_gene_expression"
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
    template: dict[str, str],
    edges: dict[str, dict[str, str]],
    downstream_evidence: dict[str, dict[str, str]],
    ordinal: int,
) -> dict[str, str]:
    ligand = partial["ligand_node_id"]
    receptor = partial["receptor_node_id"]
    relay = template["intracellular_continuation_node_id"]
    tf = partial.get("transcription_factor_node_id") or template["transcription_factor_node_id"]
    target = partial["target_gene_node_id"]
    tf_was_missing = not partial.get("transcription_factor_node_id")
    lr_edge = matching_edge(partial.get("ligand_receptor_edge_id", ""), edges, ligand, receptor)
    relay_edge = matching_edge(template.get("receptor_intracellular_edge_id", ""), edges, receptor, relay)
    intracellular_tf_edge = matching_edge(template.get("intracellular_tf_edge_id", ""), edges, relay, tf)
    tf_target_edge = matching_edge(partial.get("tf_target_edge_id", ""), edges, tf, target)
    missing_layers = join_unique(
        "receptor_to_intracellular_edge" if not relay_edge else "",
        "intracellular_to_tf_edge" if not intracellular_tf_edge else "",
        "tf_to_target_edge" if not tf_target_edge else "",
    )
    template_kind = "exact_ligand_receptor_output_template" if tf_was_missing else "exact_ligand_receptor_tf_output_template"
    source_record = downstream_evidence.get(partial.get("source_evidence_record_id", ""), {})
    template_record = downstream_evidence.get(template.get("source_evidence_record_id", ""), {})
    linkage = join_unique(
        partial.get("route_linkage_status", ""),
        template.get("route_linkage_status", ""),
        "literature_expansion:source_linked_output_template_promotion",
        template_kind,
        "relay_identity_supported_by_existing_full_output_route",
        "tf_identity_supported_by_existing_full_output_route" if tf_was_missing else "tf_identity_retained_from_target_route",
        "target_specific_output_not_asserted_by_template",
        "receptor_to_intracellular_edge_asserted_as_graph_edge" if relay_edge else "receptor_to_intracellular_edge_not_asserted",
        "intracellular_to_tf_edge_asserted_as_graph_edge" if intracellular_tf_edge else "intracellular_to_tf_edge_not_asserted",
        "tf_to_target_edge_asserted_as_graph_edge" if tf_target_edge else "tf_to_target_edge_not_asserted",
        "end_to_end_chain_not_asserted_by_single_source",
        "evidence_route_only",
    )
    summary = source_record.get("evidence_summary", "").strip() or (
        f"Source-linked target-gene route component for {partial['ligand_label']} > {partial['receptor_label']} > "
        f"{partial.get('transcription_factor_label') or '????'} > {partial['target_gene_label']}."
    )
    limitations = join_unique(
        source_record.get("limitations", ""),
        template_record.get("limitations", ""),
        "The relay and, when unresolved in the target route, TF identity are composed from a source-linked full output route for the same ligand and receptor; the output-template source did not itself demonstrate this target-gene endpoint.",
        "This is composed evidence rather than a single-paper demonstration of every handoff; no new causal edge or confidence score is asserted.",
        "The original partial target-gene route is retained separately for provenance.",
    )
    row = dict(partial)
    row.update(
        {
            "expansion_id": f"M21B-LITEXP-OUTPROMO-{ordinal:05d}",
            "path_expression": FULL_PATH,
            "route_tier": FULL_TIER,
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": missing_layers,
            "intracellular_status": "source_supported_composed",
            "ligand_receptor_edge_id": lr_edge,
            "receptor_intracellular_edge_id": relay_edge,
            "intracellular_continuation_node_id": relay,
            "intracellular_continuation_label": template["intracellular_continuation_label"],
            "intracellular_tf_edge_id": intracellular_tf_edge,
            "transcription_factor_node_id": tf,
            "transcription_factor_label": partial.get("transcription_factor_label") or template["transcription_factor_label"],
            "tf_target_edge_id": tf_target_edge,
            "evidence_ids": join_unique(
                partial.get("evidence_ids", ""),
                template.get("evidence_ids", ""),
                template.get("route_evidence_id", ""),
                template.get("source_evidence_record_id", ""),
            ),
            "source_chain_id": f"output_template_promotion:{partial['expansion_id']}:{template['expansion_id']}",
            "route_linkage_status": linkage,
            "primary_locator": join_unique(partial.get("primary_locator", ""), template.get("primary_locator", "")),
            "citation_note": (
                f"The target-gene route is retained from {partial['expansion_id']}; relay and TF identities are "
                f"composed from the source-linked output route {template['expansion_id']}. The output-template "
                "source does not assert the target-specific endpoint, and no new graph edge is created."
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
        (
            row.get("ligand_node_id", ""), row.get("receptor_node_id", ""),
            row.get("intracellular_continuation_node_id", ""), row.get("transcription_factor_node_id", ""),
            row.get("target_gene_node_id", ""), row.get("output_label", ""),
        )
        for row in expansions
    }
    by_lrtf: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    by_lr: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in expansions:
        if (
            row.get("path_expression") == FULL_OUTPUT_PATH
            and row.get("intracellular_continuation_node_id")
            and row.get("transcription_factor_node_id")
            and row.get("primary_locator")
        ):
            by_lrtf[(row["ligand_node_id"], row["receptor_node_id"], row["transcription_factor_node_id"])].append(row)
            by_lr[(row["ligand_node_id"], row["receptor_node_id"])].append(row)

    rows: list[dict[str, str]] = []
    generated: set[tuple[str, ...]] = set()
    skipped = {"no_output_template": 0, "duplicate_signature": 0, "missing_primary_locator": 0, "missing_source_linkage": 0}
    partials = [row for row in expansions if row.get("path_expression") in {PARTIAL_TF_PATH, PARTIAL_BOTH_PATH}]
    for partial in partials:
        if not partial.get("primary_locator"):
            skipped["missing_primary_locator"] += 1
            continue
        if not partial.get("source_queue_id") or not partial.get("source_evidence_record_id"):
            skipped["missing_source_linkage"] += 1
            continue
        if partial["path_expression"] == PARTIAL_TF_PATH:
            templates = by_lrtf.get((partial["ligand_node_id"], partial["receptor_node_id"], partial["transcription_factor_node_id"]), [])
        else:
            templates = by_lr.get((partial["ligand_node_id"], partial["receptor_node_id"]), [])
        if not templates:
            skipped["no_output_template"] += 1
            continue
        for template in templates:
            tf = partial.get("transcription_factor_node_id") or template.get("transcription_factor_node_id", "")
            signature = (
                partial.get("ligand_node_id", ""), partial.get("receptor_node_id", ""),
                template.get("intracellular_continuation_node_id", ""), tf,
                partial.get("target_gene_node_id", ""), partial.get("output_label", ""),
            )
            if signature in existing_signatures or signature in generated:
                skipped["duplicate_signature"] += 1
                continue
            generated.add(signature)
            rows.append(make_row(partial, template, edges, downstream_evidence, len(rows) + 1))
    return rows, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows, skipped = make_rows(args.bundle.resolve())
    if not rows:
        raise ValueError("No source-linked output-template promotions found")
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "rows": len(rows), "ligands": len({row["ligand_label"] for row in rows}), "skipped": skipped}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
