#!/usr/bin/env python3
"""Compose full intermediate routes with pairwise source-linked outputs.

This is the lower full-output tier: relay, TF, and output observations belong
to the same ligand/receptor pair, and at least one pair shares a public
literature locator.  The endpoint remains a measured output, not a named
target-gene edge, and no causal handoff is asserted.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import re
from collections import defaultdict
from pathlib import Path


FULL_OUTPUT_PATH = "ligand>receptor>intracellular>TF>output"
FULL_OUTPUT_TIER = "ligand_receptor_intracellular_tf_output_pairwise_source_overlap"
ID_PREFIX = "M21B-LITEXP-PAIRFULLOUT-"
LOCATOR_RE = re.compile(r"^(?:PMID|PMCID|DOI):")


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


def public_locators(record: dict[str, str]) -> set[str]:
    return {
        item for item in split_values(record.get("source_locator", ""))
        if LOCATOR_RE.match(item) or item.startswith(("http://", "https://"))
    }


def matching_edge(edge_ids: str, edges: dict[str, dict[str, str]], source: str, target: str) -> str:
    for edge_id in split_values(edge_ids):
        edge = edges.get(edge_id)
        if edge and edge.get("source_node_id") == source and edge.get("target_node_id") == target:
            return edge_id
    return ""


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
    )


def row_locators(row: dict[str, str], records: dict[str, dict[str, str]]) -> set[str]:
    return public_locators(records.get(row.get("source_evidence_record_id", ""), {}))


def choose_row(rows: list[dict[str, str]], preferred: set[str], records: dict[str, dict[str, str]]) -> dict[str, str]:
    return sorted(
        rows,
        key=lambda row: (
            -len(row_locators(row, records) & preferred),
            -len(row_locators(row, records)),
            row.get("route_evidence_id", ""),
        ),
    )[0]


def make_row(
    relay: dict[str, str],
    tf: dict[str, str],
    output: dict[str, str],
    pair_names: list[str],
    anchor_locators: set[str],
    records: dict[str, dict[str, str]],
    edges: dict[str, dict[str, str]],
    ordinal: int,
) -> dict[str, str]:
    ligand = output["ligand_node_id"]
    receptor = output["receptor_node_id"]
    relay_id = relay["intracellular_continuation_node_id"]
    tf_id = tf["transcription_factor_node_id"]
    components = [relay, tf, output]
    record_ids = join_unique(*(row.get("source_evidence_record_id", "") for row in components))
    source_records = [records[record_id] for record_id in split_values(record_ids) if record_id in records]
    lr_edge = matching_edge(output.get("ligand_receptor_edge_id", ""), edges, ligand, receptor)
    relay_edge = matching_edge(relay.get("receptor_intracellular_edge_id", ""), edges, receptor, relay_id)
    linkage = join_unique(
        *(row.get("route_linkage_status", "") for row in components),
        "literature_expansion:pairwise_full_output_composition",
        f"pairwise_source_overlap_count:{len(pair_names)}",
        *(f"pairwise_source_overlap:{name}" for name in pair_names),
        *(f"shared_public_locator_anchor:{locator}" for locator in sorted(anchor_locators)),
        "source_linked_relay_component",
        "source_linked_tf_component",
        "source_linked_output_component",
        "target_gene_layer_not_asserted_by_output_route",
        "receptor_to_intracellular_edge_asserted_as_graph_edge" if relay_edge else "receptor_to_intracellular_edge_not_asserted",
        "intracellular_to_tf_edge_not_asserted",
        "end_to_end_chain_not_asserted_by_single_source",
        "evidence_route_only",
    )
    summary = next((row.get("evidence_summary", "").strip() for row in source_records if row.get("evidence_summary", "").strip()), "") or (
        f"Pairwise-source-overlap full-output composition for {output['ligand_label']} > {output['receptor_label']} > "
        f"{relay['intracellular_continuation_label']} > {tf['transcription_factor_label']} > {output['output_label']}."
    )
    limitations = join_unique(
        *(row.get("limitations", "") for row in source_records),
        "Only the named component pairs share a public locator; the remaining component is independently source-linked.",
        "The endpoint is a measured output without a named target-gene edge.",
        "No new graph edge, causal assertion, or confidence score is created; mSCS must evaluate layer linkage and cell context.",
    )
    return {
        "expansion_id": f"{ID_PREFIX}{ordinal:05d}",
        "source_queue_id": output.get("source_queue_id", ""),
        "route_status": "retained_evidence_route",
        "path_expression": FULL_OUTPUT_PATH,
        "route_tier": FULL_OUTPUT_TIER,
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": join_unique("receptor_to_intracellular_edge" if not relay_edge else "", "intracellular_to_tf_edge"),
        "intracellular_status": "source_supported_pairwise_composed",
        "ligand_node_id": ligand,
        "ligand_label": output.get("ligand_label", ""),
        "ligand_receptor_edge_id": lr_edge,
        "receptor_node_id": receptor,
        "receptor_label": output.get("receptor_label", ""),
        "receptor_intracellular_edge_id": relay_edge,
        "intracellular_continuation_node_id": relay_id,
        "intracellular_continuation_label": relay.get("intracellular_continuation_label", ""),
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": tf_id,
        "transcription_factor_label": tf.get("transcription_factor_label", ""),
        "tf_target_edge_id": "",
        "target_gene_node_id": "",
        "target_gene_label": "",
        "target_output_form_id": output.get("target_output_form_id", ""),
        "output_node_id": output.get("output_node_id", ""),
        "output_label": output.get("output_label", ""),
        "output_form_id": output.get("output_form_id", ""),
        "bridge_id": output.get("bridge_id", ""),
        "pathway_name": output.get("pathway_name", "") or relay.get("pathway_name", "") or tf.get("pathway_name", ""),
        "input_evidence_type": "primary_pairwise_source_overlap_composition",
        "output_evidence_type": output.get("output_evidence_type", "primary_composed_downstream_output"),
        "evidence_ids": join_unique(
            *(row.get("evidence_ids", "") for row in components),
            *(row.get("route_evidence_id", "") for row in components),
            record_ids,
        ),
        "source_chain_id": f"pairwise_full_output:{relay.get('route_evidence_id', '')}:{tf.get('route_evidence_id', '')}:{output.get('route_evidence_id', '')}",
        "source_evidence_record_id": output.get("source_evidence_record_id", ""),
        "route_linkage_status": linkage,
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": next((row.get("evidence_polarity", "") for row in source_records if row.get("evidence_polarity")), "supports"),
        "negative_evidence_status": next((row.get("negative_evidence_status", "") for row in source_records if row.get("negative_evidence_status")), "not_evaluated"),
        "evidence_directness": "pairwise_overlap_composite_primary_evidence",
        "output_class": output.get("output_class", "generic_functional_readout"),
        "primary_locator": join_unique(*(row.get("source_locator", "") for row in source_records)),
        "citation_note": (
            f"Relay route {relay.get('route_evidence_id', '')}, TF route {tf.get('route_evidence_id', '')}, and output route "
            f"{output.get('route_evidence_id', '')} are source-linked; pairwise public-locator overlap is retained for {', '.join(pair_names)}."
        ),
        "evidence_summary": summary,
        "limitations": limitations,
        "curation_status": "curated_primary_route",
        "species_context": join_unique(*(row.get("species_context", "") for row in source_records)),
        "cell_type_context": join_unique(*(row.get("cell_type_context", "") for row in source_records)),
        "compartment_context": join_unique(*(row.get("compartment_context", "") for row in source_records)),
        "injury_context": join_unique(*(row.get("injury_context", "") for row in source_records)),
        "context_scope": join_unique(*(row.get("context_scope", "") for row in source_records)),
        "assay_or_perturbation": join_unique(*(row.get("assay_or_perturbation", "") for row in source_records)),
        "effect_polarity": join_unique(*(row.get("effect_polarity", "") for row in source_records)),
        "source_scope": "pairwise_overlap_composite_primary_evidence",
    }


def make_rows(bundle: Path) -> tuple[list[dict[str, str]], dict[str, int]]:
    routes = read_tsv(bundle / "mechanism_signaling_route_evidence.tsv.gz")
    expansions = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    records = {row["record_id"]: row for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    roles: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(bundle / "mechanism_node_roles.tsv"):
        roles[row["node_id"]].add(row["role"])
    existing = {
        tuple(row.get(field, "") for field in (
            "ligand_node_id", "receptor_node_id", "intracellular_continuation_node_id",
            "transcription_factor_node_id", "output_node_id", "output_label",
        ))
        for row in expansions
    }
    relay: dict[tuple[str, str], dict[str, list[dict[str, str]]]] = defaultdict(lambda: defaultdict(list))
    tf: dict[tuple[str, str], dict[str, list[dict[str, str]]]] = defaultdict(lambda: defaultdict(list))
    output: dict[tuple[str, str], dict[tuple[str, str], list[dict[str, str]]]] = defaultdict(lambda: defaultdict(list))
    for row in routes:
        if not row.get("source_queue_id") or row.get("source_scope") in {
            "source_linked_composite_primary_evidence",
            "pairwise_overlap_composite_primary_evidence",
        }:
            continue
        record = records.get(row.get("source_evidence_record_id", ""))
        if not record or not public_locators(record) or not eligible_ligand(row, roles):
            continue
        if not matching_edge(row.get("ligand_receptor_edge_id", ""), edges, row["ligand_node_id"], row["receptor_node_id"]):
            continue
        key = (row["ligand_node_id"], row["receptor_node_id"])
        if row.get("intracellular_continuation_node_id"):
            relay[key][row["intracellular_continuation_node_id"]].append(row)
        if row.get("transcription_factor_node_id"):
            tf[key][row["transcription_factor_node_id"]].append(row)
        if row.get("output_node_id") and row.get("output_label") and not row.get("target_gene_node_id"):
            output[key][(row.get("output_node_id", ""), row.get("output_label", ""))].append(row)
    rows: list[dict[str, str]] = []
    generated: set[tuple[str, ...]] = set()
    pair_counts = {"two_or_three_pair": 0, "one_pair": 0}
    for key in sorted(set(relay) & set(tf) & set(output)):
        for relay_id in sorted(relay[key]):
            relay_rows = relay[key][relay_id]
            relay_locs = set().union(*(row_locators(row, records) for row in relay_rows))
            for tf_id in sorted(tf[key]):
                tf_rows = tf[key][tf_id]
                tf_locs = set().union(*(row_locators(row, records) for row in tf_rows))
                pair_sets = {"relay_tf": relay_locs & tf_locs}
                for output_id in sorted(output[key]):
                    signature = (*key, relay_id, tf_id, *output_id)
                    if signature in existing or signature in generated:
                        continue
                    output_rows = output[key][output_id]
                    output_locs = set().union(*(row_locators(row, records) for row in output_rows))
                    pair_sets.update({
                        "relay_output": relay_locs & output_locs,
                        "tf_output": tf_locs & output_locs,
                    })
                    active_pairs = [name for name, locators in pair_sets.items() if locators]
                    if not active_pairs:
                        continue
                    generated.add(signature)
                    preferred_relay = set().union(*(pair_sets[name] for name in active_pairs if name.startswith("relay_")))
                    preferred_tf = set().union(*(pair_sets[name] for name in active_pairs if name.endswith("tf") or name == "tf_output"))
                    preferred_output = set().union(*(pair_sets[name] for name in active_pairs if name.endswith("output")))
                    relay_row = choose_row(relay_rows, preferred_relay, records)
                    tf_row = choose_row(tf_rows, preferred_tf, records)
                    output_row = choose_row(output_rows, preferred_output, records)
                    rows.append(make_row(relay_row, tf_row, output_row, active_pairs, set().union(*(pair_sets[name] for name in active_pairs)), records, edges, len(rows) + 1))
                    pair_counts["two_or_three_pair" if len(active_pairs) >= 2 else "one_pair"] += 1
    if not rows:
        raise ValueError("No pairwise full-output compositions found")
    return rows, pair_counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows, pair_counts = make_rows(args.bundle.resolve())
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "rows": len(rows), "ligands": len({row["ligand_label"] for row in rows}), "pair_counts": pair_counts}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
