#!/usr/bin/env python3
"""Compose full routes from source-linked relay, TF, and target observations.

This pass is intentionally stricter than an unconstrained layer join.  A
relay-output route, a TF-output route, and a target-gene route must share the
same ligand/receptor pair and the same downstream source queue.  Each source
record must have a public literature locator.  The resulting row is still an
evidence-only composition: sharing a source queue does not assert that one
paper demonstrated every intracellular-to-TF or TF-to-target handoff.

No graph edge, causal assertion, or database confidence score is created.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
from collections import defaultdict
from pathlib import Path


RELAY_OUTPUT_PATH = "ligand>receptor>intracellular>????>output"
TF_OUTPUT_PATH = "ligand>receptor>????>TF>output"
TARGET_PATH = "ligand>receptor>????>????>target_gene_expression"
FULL_PATH = "ligand>receptor>intracellular>TF>target_gene_expression"
FULL_TIER = "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges"
ID_PREFIX = "M21B-LITEXP-SRCSHARED-"


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


def public_locator(value: str) -> bool:
    upper = value.upper()
    return any(token in upper for token in ("PMID:", "PMCID:", "DOI:", "HTTP://", "HTTPS://"))


def matching_edge(edge_ids: str, edges: dict[str, dict[str, str]], source: str, target: str) -> str:
    for edge_id in split_values(edge_ids):
        edge = edges.get(edge_id)
        if edge and edge.get("source_node_id") == source and edge.get("target_node_id") == target:
            return edge_id
    return ""


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
        bool(row.get("ligand_node_id"))
        and bool(row.get("receptor_node_id"))
        and "ligand" in node_roles
        and not {"receptor", "transcription_factor", "target_gene"} & node_roles
        and not any(marker in label for marker in excluded_markers)
        and label not in {"yap1", "wwtr1/taz", "ctnnb1-beta-catenin"}
    )


def route_key(row: dict[str, str]) -> tuple[str, str, str]:
    return row.get("ligand_node_id", ""), row.get("receptor_node_id", ""), row.get("source_queue_id", "")


def source_locators(
    row: dict[str, str], records: dict[str, dict[str, str]]
) -> str:
    return records.get(row.get("source_evidence_record_id", ""), {}).get("source_locator", "")


def make_row(
    partial: dict[str, str],
    relay: dict[str, str],
    tf: dict[str, str],
    source_records: dict[str, dict[str, str]],
    edges: dict[str, dict[str, str]],
    ordinal: int,
) -> dict[str, str]:
    ligand = partial["ligand_node_id"]
    receptor = partial["receptor_node_id"]
    relay_id = relay["intracellular_continuation_node_id"]
    tf_id = tf["transcription_factor_node_id"]
    target = partial["target_gene_node_id"]
    record_ids = join_unique(
        partial.get("source_evidence_record_id", ""),
        relay.get("source_evidence_record_id", ""),
        tf.get("source_evidence_record_id", ""),
    )
    records = [source_records[record_id] for record_id in split_values(record_ids) if record_id in source_records]
    locators = join_unique(*(record.get("source_locator", "") for record in records))
    lr_edge = matching_edge(partial.get("ligand_receptor_edge_id", ""), edges, ligand, receptor)
    relay_edge = matching_edge(relay.get("receptor_intracellular_edge_id", ""), edges, receptor, relay_id)
    tf_target_edge = matching_edge(partial.get("tf_target_edge_id", ""), edges, tf_id, target)
    missing_layers = join_unique(
        "receptor_to_intracellular_edge" if not relay_edge else "",
        "intracellular_to_tf_edge",
        "tf_to_target_edge" if not tf_target_edge else "",
    )
    source_summary = next((record.get("evidence_summary", "").strip() for record in records if record.get("evidence_summary", "").strip()), "")
    summary = source_summary or (
        f"Shared-source evidence composition for {partial['ligand_label']} > {partial['receptor_label']} > "
        f"{relay['intracellular_continuation_label']} > {tf['transcription_factor_label']} > {partial['target_gene_label']}."
    )
    limitations = join_unique(
        *(record.get("limitations", "") for record in records),
        "Relay, TF, and target observations share a source queue but remain a composed evidence route; the source may not demonstrate every handoff.",
        "Intracellular-to-TF and TF-to-target linkage remains unasserted unless represented by an existing graph edge.",
        "No new graph edge, causal assertion, or confidence score is created; mSCS must evaluate layer linkage and cell context.",
    )
    linkage = join_unique(
        partial.get("route_linkage_status", ""),
        relay.get("route_linkage_status", ""),
        tf.get("route_linkage_status", ""),
        "literature_expansion:source_linked_full_sequence_composition",
        f"shared_source_queue_anchor:{partial.get('source_queue_id', '')}",
        "source_linked_relay_output_component",
        "source_linked_tf_output_component",
        "source_linked_target_gene_component",
        "intracellular_to_tf_edge_not_asserted",
        "tf_to_target_edge_asserted_as_graph_edge" if tf_target_edge else "tf_to_target_edge_not_asserted",
        "receptor_to_intracellular_edge_asserted_as_graph_edge" if relay_edge else "receptor_to_intracellular_edge_not_asserted",
        "end_to_end_chain_not_asserted_by_single_source",
        "evidence_route_only",
    )
    return {
        "expansion_id": f"{ID_PREFIX}{ordinal:05d}",
        "source_queue_id": partial.get("source_queue_id", ""),
        "route_status": "retained_evidence_route",
        "path_expression": FULL_PATH,
        "route_tier": FULL_TIER,
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": missing_layers,
        "intracellular_status": "source_supported_composed",
        "ligand_node_id": ligand,
        "ligand_label": partial.get("ligand_label", ""),
        "ligand_receptor_edge_id": lr_edge,
        "receptor_node_id": receptor,
        "receptor_label": partial.get("receptor_label", ""),
        "receptor_intracellular_edge_id": relay_edge,
        "intracellular_continuation_node_id": relay_id,
        "intracellular_continuation_label": relay.get("intracellular_continuation_label", ""),
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": tf_id,
        "transcription_factor_label": tf.get("transcription_factor_label", ""),
        "tf_target_edge_id": tf_target_edge,
        "target_gene_node_id": target,
        "target_gene_label": partial.get("target_gene_label", ""),
        "target_output_form_id": partial.get("target_output_form_id", ""),
        "output_node_id": partial.get("output_node_id", "") or target,
        "output_label": partial.get("output_label", "") or partial.get("target_gene_label", ""),
        "output_form_id": partial.get("output_form_id", ""),
        "bridge_id": partial.get("bridge_id", ""),
        "pathway_name": partial.get("pathway_name", "") or relay.get("pathway_name", "") or tf.get("pathway_name", ""),
        "input_evidence_type": "primary_shared_source_route_composition",
        "output_evidence_type": "primary_composed_downstream_output",
        "evidence_ids": join_unique(
            partial.get("evidence_ids", ""), relay.get("evidence_ids", ""), tf.get("evidence_ids", ""),
            partial.get("route_evidence_id", ""), relay.get("route_evidence_id", ""), tf.get("route_evidence_id", ""),
            record_ids,
            *(record.get("source_evidence_ids", "") for record in records),
        ),
        "source_chain_id": f"source_shared_full:{partial.get('route_evidence_id', '')}:{relay.get('route_evidence_id', '')}:{tf.get('route_evidence_id', '')}",
        # Keep the schema's singular source-evidence foreign key anchored to
        # the target-gene component.  Relay/TF records remain auditable in
        # evidence_ids and in the source-chain citation note.
        "source_evidence_record_id": partial.get("source_evidence_record_id", ""),
        "route_linkage_status": linkage,
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": next((record.get("evidence_polarity", "") for record in records if record.get("evidence_polarity")), "supports"),
        "negative_evidence_status": next((record.get("negative_evidence_status", "") for record in records if record.get("negative_evidence_status")), "not_evaluated"),
        "evidence_directness": "source_linked_composite_primary_evidence",
        "output_class": "gene_expression_or_transcription",
        "primary_locator": locators,
        "citation_note": (
            f"Relay-output route {relay.get('route_evidence_id', '')}, TF-output route {tf.get('route_evidence_id', '')}, "
            f"and target-gene route {partial.get('route_evidence_id', '')} share source queue {partial.get('source_queue_id', '')}; "
            "the unresolved handoffs remain explicit."
        ),
        "evidence_summary": summary,
        "limitations": limitations,
        "curation_status": "curated_primary_route",
        "species_context": join_unique(*(record.get("species_context", "") for record in records)),
        "cell_type_context": join_unique(*(record.get("cell_type_context", "") for record in records)),
        "compartment_context": join_unique(*(record.get("compartment_context", "") for record in records)),
        "injury_context": join_unique(*(record.get("injury_context", "") for record in records)),
        "context_scope": join_unique(*(record.get("context_scope", "") for record in records)),
        "assay_or_perturbation": join_unique(*(record.get("assay_or_perturbation", "") for record in records)),
        "effect_polarity": join_unique(*(record.get("effect_polarity", "") for record in records)),
        "source_scope": "source_linked_composite_primary_evidence",
    }


def make_rows(bundle: Path) -> tuple[list[dict[str, str]], dict[str, int]]:
    expansions = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    route_rows = read_tsv(bundle / "mechanism_signaling_route_evidence.tsv.gz")
    records = {row["record_id"]: row for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    roles: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(bundle / "mechanism_node_roles.tsv"):
        roles[row["node_id"]].add(row["role"])
    existing = {
        tuple(row.get(field, "") for field in (
            "ligand_node_id", "receptor_node_id", "intracellular_continuation_node_id",
            "transcription_factor_node_id", "target_gene_node_id",
        ))
        for row in expansions
    }
    eligible = [
        row for row in route_rows
        if row.get("source_queue_id")
        and row.get("source_evidence_record_id") in records
        and public_locator(records[row["source_evidence_record_id"]].get("source_locator", ""))
        and eligible_ligand(row, roles)
        and row.get("ligand_receptor_edge_id")
    ]
    relay_by_key: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    tf_by_key: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    target_by_key: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in eligible:
        key = route_key(row)
        # A source-linked full route may expose one or more of these layers in
        # a richer path expression (for example, an existing full route).  We
        # therefore index by asserted node identity rather than requiring a
        # particular placeholder shape.  The output row still records the
        # composition and never upgrades the underlying handoffs to causal.
        if row.get("intracellular_continuation_node_id"):
            relay_by_key[key].append(row)
        if row.get("transcription_factor_node_id"):
            tf_by_key[key].append(row)
        if row.get("target_gene_node_id"):
            target_by_key[key].append(row)

    rows: list[dict[str, str]] = []
    generated: set[tuple[str, ...]] = set()
    skipped = {"no_complete_shared_source": 0, "existing_signature": 0, "duplicate_signature": 0}
    for key in sorted(set(relay_by_key) & set(tf_by_key) & set(target_by_key)):
        relays = sorted(relay_by_key[key], key=lambda row: (row.get("intracellular_continuation_node_id", ""), row.get("route_evidence_id", "")))
        tfs = sorted(tf_by_key[key], key=lambda row: (row.get("transcription_factor_node_id", ""), row.get("route_evidence_id", "")))
        targets = sorted(target_by_key[key], key=lambda row: (row.get("target_gene_node_id", ""), row.get("output_label", ""), row.get("route_evidence_id", "")))
        for relay in relays:
            for tf in tfs:
                for target in targets:
                    signature = (
                        target.get("ligand_node_id", ""), target.get("receptor_node_id", ""),
                        relay.get("intracellular_continuation_node_id", ""), tf.get("transcription_factor_node_id", ""),
                        target.get("target_gene_node_id", ""),
                    )
                    if signature in existing:
                        skipped["existing_signature"] += 1
                        continue
                    if signature in generated:
                        skipped["duplicate_signature"] += 1
                        continue
                    generated.add(signature)
                    rows.append(make_row(target, relay, tf, records, edges, len(rows) + 1))
    if not rows:
        raise ValueError("No source-linked full-sequence compositions found")
    return rows, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows, skipped = make_rows(args.bundle.resolve())
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output.resolve()),
        "rows": len(rows),
        "ligands": len({row["ligand_label"] for row in rows}),
        "skipped": skipped,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
