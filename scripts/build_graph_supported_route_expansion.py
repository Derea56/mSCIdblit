#!/usr/bin/env python3
"""Materialize conservative graph-supported evidence-route compositions.

The route table already retains direct evidence packets and conservative
cross-record compositions. This pass adds the remaining route signatures that
can be assembled from an exact ligand-receptor edge plus compatible exported
graph components. Compatibility requires a shared pathway anchor (or shared
evidence identifier); it never treats all components attached to a receptor as
a Cartesian product.

The output remains an evidence layer. It does not create graph edges, promote
an intracellular-to-TF relationship to a causal edge, or assign confidence.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path

try:
    from .route_artifacts import write_normalized_route_artifacts
except ImportError:  # pragma: no cover - direct script execution
    from route_artifacts import write_normalized_route_artifacts


ROUTE_FILE = "mechanism_signaling_route_evidence.tsv"
SUMMARY_FILE = "graph_supported_route_expansion_summary.json"
TARGET_RELATIONS = {"induces_target_gene", "represses_target_gene", "regulates_target_gene"}
GENERIC_ANCHORS = {
    "activation", "adhesion", "and", "astrocyte", "branch", "cell", "complex",
    "control", "expression", "family", "for", "from", "functional", "gene",
    "glial", "human", "inflammation", "ligand", "macrophage", "microglial",
    "mouse", "of", "or", "output", "pathway", "primary", "protein", "readout",
    "receptor", "regulation", "regulatory", "release", "response", "secretion",
    "signaling", "signalling", "surface", "the", "to", "transcription", "type",
    "via", "with",
}
OUTPUT_MARKERS = (
    " gene", " release", " secretion", " expression", " transcription", " output",
    " surface", " protein", " production", " adhesion", " readout", " phosphorylation",
    " activation",
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", newline="", encoding="utf-8", errors="replace") if path.suffix == ".gz" else opener(path, newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def tokens(value: str) -> set[str]:
    return {
        token.casefold()
        for token in re.findall(r"[A-Za-z0-9]+", value)
        if len(token) >= 3 and token.casefold() not in GENERIC_ANCHORS
    }


def anchor_roots(values: set[str]) -> set[str]:
    roots = set(values)
    for value in values:
        root = re.sub(r"\d+$", "", value)
        if len(root) >= 4:
            roots.add(root)
    return roots


def edge_anchors(edge: dict[str, str], nodes: dict[str, dict[str, str]]) -> set[str]:
    target = nodes.get(edge.get("target_node_id", ""), {})
    value = " ".join(
        edge.get(field, "")
        for field in ("pathway_label", "pathway_name")
    )
    value += " " + target.get("canonical_name", "")
    return anchor_roots(tokens(value))


def shared_anchor(*edges: dict[str, str], nodes: dict[str, dict[str, str]]) -> str:
    if not edges:
        return ""
    common: set[str] | None = None
    for edge in edges:
        values = edge_anchors(edge, nodes)
        common = values if common is None else common & values
    if not common:
        evidence_sets = [
            {value for value in edge.get("evidence_ids", "").split(";") if value}
            for edge in edges
        ]
        evidence_common = set.intersection(*evidence_sets) if evidence_sets else set()
        if evidence_common:
            return sorted(evidence_common)[0]
        return ""
    return sorted(common, key=lambda value: (len(value), value))[0]


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


def is_ligand_receptor(edge: dict[str, str], roles: dict[str, set[str]]) -> bool:
    return (
        edge.get("relation_type") == "binds_receptor"
        and "ligand" in roles[edge.get("source_node_id", "")]
        and "receptor" in roles[edge.get("target_node_id", "")]
    )


def is_output_edge(edge: dict[str, str]) -> bool:
    layer = edge.get("evidence_layer", "").casefold()
    text = " ".join(
        edge.get(field, "")
        for field in ("target_label", "pathway_label", "pathway_name", "edge_status", "evidence_layer")
    ).casefold()
    return "downstream_or_functional" in layer or any(marker in text for marker in OUTPUT_MARKERS)


def is_target_output(edge: dict[str, str], roles: dict[str, set[str]]) -> bool:
    target_label = edge.get("target_label", "").casefold()
    return (
        "target_gene" in roles[edge.get("target_node_id", "")]
        or " gene" in target_label
        or target_label.endswith("gene")
        or " expression" in target_label
        or " transcription" in target_label
    )


def output_class(label: str) -> str:
    value = label.casefold()
    if any(token in value for token in ("gene", "mrna", "transcription", "expression")):
        return "gene_expression_or_transcription"
    if any(token in value for token in ("release", "secretion", "secreted", "production")):
        return "secreted_protein_or_release"
    if any(token in value for token in ("phosphorylation", "activation", "activated")):
        return "phosphorylation_or_activation_readout"
    if any(token in value for token in ("adhesion", "migration", "survival", "proliferation")):
        return "cellular_functional_readout"
    return "generic_functional_readout"


def next_graph_id(rows: list[dict[str, str]]) -> int:
    values = []
    for row in rows:
        value = row.get("route_evidence_id", "")
        if value.startswith("GRAPHROUTE:") and value[11:].isdigit():
            values.append(int(value[11:]))
    return max(values, default=0) + 1


def build_row(
    template: dict[str, str],
    *,
    roles: dict[str, set[str]],
    tier: str,
    expression: str,
    known_layers: str,
    missing_layers: str,
    lr: dict[str, str],
    output: dict[str, str],
    anchor: str,
    relay: dict[str, str] | None = None,
    receptor_tf: dict[str, str] | None = None,
    intracellular_tf: dict[str, str] | None = None,
    tf_output: dict[str, str] | None = None,
    composition: str,
) -> dict[str, str]:
    row = {field: "" for field in template}
    target_gene = is_target_output(output, roles)
    target_id = output.get("target_node_id", "") if target_gene else ""
    target_label = output.get("target_label", "") if target_gene else ""
    tf_edge = intracellular_tf or receptor_tf or {}
    tf_output_edge = tf_output or output
    tf_id = tf_edge.get("target_node_id", "") if tf_edge else tf_output_edge.get("source_node_id", "")
    tf_label = ""
    if tf_id and tf_id == tf_output_edge.get("source_node_id", ""):
        tf_label = tf_output_edge.get("source_label", "")
    elif tf_id:
        tf_label = tf_edge.get("target_label", "")
    component_edges = [lr]
    if relay:
        component_edges.append(relay)
    if receptor_tf:
        component_edges.append(receptor_tf)
    if intracellular_tf:
        component_edges.append(intracellular_tf)
    if tf_output and tf_output is not output:
        component_edges.append(tf_output)
    component_edges.append(output)
    row.update(
        {
            "route_status": "retained_evidence_route",
            "route_tier": tier,
            "path_expression": expression,
            "known_layers": known_layers,
            "missing_layers": missing_layers,
            "intracellular_status": "explicit_receptor_proximal_edge" if relay else "not_assessed",
            "ligand_node_id": lr.get("source_node_id", ""),
            "ligand_label": lr.get("source_label", ""),
            "ligand_receptor_edge_id": lr.get("edge_id", ""),
            "receptor_node_id": lr.get("target_node_id", ""),
            "receptor_label": lr.get("target_label", ""),
            "receptor_intracellular_edge_id": relay.get("edge_id", "") if relay else "",
            "intracellular_continuation_node_id": relay.get("target_node_id", "") if relay else "",
            "intracellular_continuation_label": relay.get("target_label", "") if relay else "",
            # A direct receptor-to-TF edge is retained for a route without a
            # relay. Once a relay is present, this field is reserved for an
            # asserted relay-to-TF edge; a receptor-to-TF edge alone does not
            # prove the missing intracellular continuation.
            "intracellular_tf_edge_id": (
                intracellular_tf.get("edge_id", "")
                if intracellular_tf
                else (receptor_tf.get("edge_id", "") if receptor_tf and not relay else "")
            ),
            "transcription_factor_node_id": tf_id if tf_edge or tf_output else "",
            "transcription_factor_label": tf_label if tf_edge or tf_output else "",
            "tf_target_edge_id": tf_output.get("edge_id", "") if tf_output and tf_output.get("relation_type") in TARGET_RELATIONS else "",
            "target_gene_node_id": target_id,
            "target_gene_label": target_label,
            "output_node_id": output.get("target_node_id", ""),
            "output_label": output.get("target_label", ""),
            "pathway_name": join_unique(*(edge.get("pathway_name", "") for edge in component_edges)),
            "input_evidence_type": "graph_ligand_receptor_edge",
            "output_evidence_type": "graph_component_output_edge",
            "evidence_ids": join_unique(*(edge.get("evidence_ids", "") for edge in component_edges)),
            "route_linkage_status": (
                f"graph_supported_{composition};pathway_anchor:{anchor};evidence_route_only"
                + (";intracellular_to_tf_edge_not_asserted" if relay and not intracellular_tf else "")
            ),
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "source_chain_id": "graph_components:" + "+".join(edge.get("edge_id", "") for edge in component_edges),
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": "supports",
            "negative_evidence_status": "not_evaluated",
            "evidence_directness": "graph_component_composition",
            "output_class": output_class(output.get("target_label", "")),
            "species_context": join_unique(*(edge.get("species_context", "") for edge in component_edges)),
            "cell_type_context": join_unique(*(edge.get("cell_type_context", "") for edge in component_edges)),
            "compartment_context": join_unique(*(edge.get("compartment_context", "") for edge in component_edges)),
            "injury_context": join_unique(*(edge.get("injury_context", "") for edge in component_edges)),
            "context_scope": join_unique(*(edge.get("context_scope", "") for edge in component_edges)),
            "assay_or_perturbation": "graph component evidence; assay details retained in edge sources",
            "effect_polarity": output.get("effect_polarity", ""),
            "source_scope": join_unique(*(edge.get("evidence_layer", "") for edge in component_edges)),
        }
    )
    return row


def compose_graph_routes(rows: list[dict[str, str]], bundle: Path) -> tuple[list[dict[str, str]], dict[str, object]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    roles: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(bundle / "mechanism_node_roles.tsv"):
        roles[row["node_id"]].add(row["role"])
    edges = read_tsv(bundle / "mechanism_edges.tsv")
    edge_by_source: dict[str, list[dict[str, str]]] = defaultdict(list)
    for edge in edges:
        if edge.get("relation_type") != "binds_receptor":
            edge_by_source[edge.get("source_node_id", "")].append(edge)

    # Cache anchor extraction once. The graph is large enough that repeatedly
    # tokenizing pathway labels inside LR x relay x TF loops is material.
    anchors_by_edge = {
        edge.get("edge_id", ""): edge_anchors(edge, nodes)
        for edge in edges
    }
    evidence_by_edge = {
        edge.get("edge_id", ""): {
            value for value in edge.get("evidence_ids", "").split(";") if value
        }
        for edge in edges
    }

    def compatible_anchor(*candidate_edges: dict[str, str]) -> str:
        common: set[str] | None = None
        for edge in candidate_edges:
            values = anchors_by_edge.get(edge.get("edge_id", ""), set())
            common = values if common is None else common & values
        if common:
            return sorted(common, key=lambda value: (len(value), value))[0]
        evidence_common: set[str] | None = None
        for edge in candidate_edges:
            values = evidence_by_edge.get(edge.get("edge_id", ""), set())
            evidence_common = values if evidence_common is None else evidence_common & values
        if evidence_common:
            return sorted(evidence_common)[0]
        return ""

    def compatible_edges(
        base_edges: tuple[dict[str, str], ...],
        indexed_edges: dict[str, list[dict[str, str]]],
    ) -> list[dict[str, str]]:
        common: set[str] | None = None
        for edge in base_edges:
            values = anchors_by_edge.get(edge.get("edge_id", ""), set())
            common = values if common is None else common & values
        selected: list[dict[str, str]] = []
        seen_edge_ids: set[str] = set()
        if common:
            for anchor in common:
                for edge in indexed_edges.get(anchor, []):
                    if edge.get("edge_id", "") not in seen_edge_ids:
                        seen_edge_ids.add(edge.get("edge_id", ""))
                        selected.append(edge)
            return selected
        evidence_common: set[str] | None = None
        for edge in base_edges:
            values = evidence_by_edge.get(edge.get("edge_id", ""), set())
            evidence_common = values if evidence_common is None else evidence_common & values
        for evidence_id in evidence_common or set():
            for edge in indexed_edges.get("evidence:" + evidence_id, []):
                if edge.get("edge_id", "") not in seen_edge_ids:
                    seen_edge_ids.add(edge.get("edge_id", ""))
                    selected.append(edge)
        return selected

    lr_edges = [edge for edge in edges if is_ligand_receptor(edge, roles)]
    existing_signatures = {
        (
            row.get("ligand_receptor_edge_id", ""),
            row.get("intracellular_continuation_node_id", ""),
            row.get("transcription_factor_node_id", ""),
            row.get("target_gene_node_id", ""),
            row.get("output_node_id", ""),
            row.get("output_label", ""),
            row.get("known_layers", ""),
        )
        for row in rows
    }
    additions: list[dict[str, str]] = []
    seen: set[tuple[str, ...]] = set()
    composition_counts: Counter[str] = Counter()

    # TF candidates include existing route TF nodes and graph sources that
    # already have target-gene relations or transcription-labelled outputs.
    tf_ids = {
        row.get("transcription_factor_node_id", "")
        for row in rows
        if row.get("transcription_factor_node_id")
    }
    tf_ids.update(
        edge.get("source_node_id", "")
        for edge in edges
        if edge.get("relation_type") in TARGET_RELATIONS
    )
    tf_ids.update(
        edge.get("source_node_id", "")
        for edge in edges
        if is_output_edge(edge) and "transcription" in edge.get("pathway_label", "").casefold()
    )
    tf_output_edges = [
        edge for edge in edges
        if edge.get("source_node_id", "") in tf_ids and is_output_edge(edge)
    ]
    tf_outputs_by_anchor: dict[str, list[dict[str, str]]] = defaultdict(list)
    for edge in tf_output_edges:
        for anchor in anchors_by_edge.get(edge.get("edge_id", ""), set()):
            tf_outputs_by_anchor[anchor].append(edge)
        for evidence_id in evidence_by_edge.get(edge.get("edge_id", ""), set()):
            tf_outputs_by_anchor["evidence:" + evidence_id].append(edge)

    def add_candidate(signature: tuple[str, ...], row: dict[str, str], composition: str) -> None:
        route_signature = (
            row.get("ligand_receptor_edge_id", ""),
            row.get("intracellular_continuation_node_id", ""),
            row.get("transcription_factor_node_id", ""),
            row.get("target_gene_node_id", ""),
            row.get("output_node_id", ""),
            row.get("output_label", ""),
            row.get("known_layers", ""),
        )
        if route_signature in existing_signatures or signature in seen:
            return
        seen.add(signature)
        additions.append(row)
        composition_counts[composition] += 1

    for lr in lr_edges:
        receptor_components = edge_by_source.get(lr.get("target_node_id", ""), [])
        receptor_tf_edges = [
            edge for edge in receptor_components
            if edge.get("target_node_id") in tf_ids
        ]
        relays = [
            edge for edge in receptor_components
            if edge.get("target_node_id") not in tf_ids
            and edge.get("target_node_id") != lr.get("source_node_id")
            and edge.get("target_node_id") != lr.get("target_node_id")
        ]
        direct_outputs = [
            edge for edge in edge_by_source.get(lr.get("source_node_id", ""), [])
            if edge.get("target_node_id") != lr.get("target_node_id") and is_output_edge(edge)
        ]

        for output in direct_outputs:
            anchor = compatible_anchor(lr, output)
            if anchor:
                target = is_target_output(output, roles)
                tier = "ligand_receptor_output_missing_intracellular_and_tf"
                known = "ligand|receptor|target_gene" if target else "ligand|receptor|output"
                missing = "intracellular_continuation|transcription_factor" if target else "intracellular_continuation|transcription_factor|target_gene_expression"
                add_candidate(
                    ("lro", lr["edge_id"], output["edge_id"]),
                    build_row(rows[0], roles=roles, tier=tier, expression="ligand>receptor>????>????>target_gene_expression" if target else "ligand>receptor>output", known_layers=known, missing_layers=missing, lr=lr, output=output, anchor=anchor, composition="lr_output"),
                    "lr_output",
                )

        for receptor_tf in receptor_tf_edges:
            tf_outputs = [edge for edge in edge_by_source.get(receptor_tf.get("target_node_id", ""), []) if is_output_edge(edge)]
            for output in tf_outputs:
                anchor = compatible_anchor(lr, receptor_tf, output)
                if not anchor:
                    continue
                target = is_target_output(output, roles)
                tier = "ligand_receptor_tf_target_missing_intracellular" if target else "ligand_receptor_tf_output_missing_target_gene"
                known = "ligand|receptor|transcription_factor|target_gene" if target else "ligand|receptor|transcription_factor|output"
                missing = "intracellular_continuation" if target else "intracellular_continuation|target_gene_expression"
                add_candidate(
                    ("lrtf", lr["edge_id"], receptor_tf["edge_id"], output["edge_id"]),
                    build_row(rows[0], roles=roles, tier=tier, expression="ligand>receptor>????>TF>target_gene_expression" if target else "ligand>receptor>????>TF>output", known_layers=known, missing_layers=missing, lr=lr, output=output, anchor=anchor, receptor_tf=receptor_tf, composition="lr_receptor_tf_output"),
                    "lr_receptor_tf_output",
                )
                for relay in relays:
                    anchor = compatible_anchor(lr, relay, receptor_tf, output)
                    if not anchor:
                        continue
                    target = is_target_output(output, roles)
                    tier = "explicit_ligand_receptor_intracellular_tf_target" if target else "ligand_receptor_intracellular_tf_output_missing_target_gene"
                    known = "ligand|receptor|intracellular_continuation|transcription_factor|target_gene" if target else "ligand|receptor|intracellular_continuation|transcription_factor|output"
                    missing = "" if target else "target_gene_expression"
                    add_candidate(
                        ("lritfout", lr["edge_id"], relay["edge_id"], receptor_tf["edge_id"], output["edge_id"]),
                        build_row(rows[0], roles=roles, tier=tier, expression="ligand>receptor>intracellular>TF>target_gene_expression" if target else "ligand>receptor>intracellular>TF>output", known_layers=known, missing_layers=missing, lr=lr, output=output, anchor=anchor, relay=relay, receptor_tf=receptor_tf, composition="lr_receptor_relay_tf_output"),
                        "lr_receptor_relay_tf_output",
                    )

        for relay in relays:
            relay_tf_edges = [
                edge for edge in edge_by_source.get(relay.get("target_node_id", ""), [])
                if edge.get("target_node_id") in tf_ids
            ]
            for intracellular_tf in relay_tf_edges:
                tf_outputs = [
                    edge for edge in edge_by_source.get(intracellular_tf.get("target_node_id", ""), [])
                    if is_output_edge(edge)
                ]
                for output in tf_outputs:
                    anchor = compatible_anchor(lr, relay, intracellular_tf, output)
                    if not anchor:
                        continue
                    target = is_target_output(output, roles)
                    tier = "explicit_ligand_receptor_intracellular_tf_target" if target else "ligand_receptor_intracellular_tf_output_missing_target_gene"
                    known = "ligand|receptor|intracellular_continuation|transcription_factor|target_gene" if target else "ligand|receptor|intracellular_continuation|transcription_factor|output"
                    missing = "" if target else "target_gene_expression"
                    add_candidate(
                        ("lritf-explicit", lr["edge_id"], relay["edge_id"], intracellular_tf["edge_id"], output["edge_id"]),
                        build_row(rows[0], roles=roles, tier=tier, expression="ligand>receptor>intracellular>TF>target_gene_expression" if target else "ligand>receptor>intracellular>TF>output", known_layers=known, missing_layers=missing, lr=lr, output=output, anchor=anchor, relay=relay, intracellular_tf=intracellular_tf, composition="lr_receptor_relay_tf_output"),
                        "lr_receptor_relay_tf_output",
                    )

            for output in direct_outputs:
                anchor = compatible_anchor(lr, relay, output)
                if not anchor:
                    continue
                target = is_target_output(output, roles)
                known = "ligand|receptor|intracellular_continuation|target_gene" if target else "ligand|receptor|intracellular_continuation|output"
                missing = "transcription_factor" if target else "transcription_factor|target_gene_expression"
                add_candidate(
                    ("lriout", lr["edge_id"], relay["edge_id"], output["edge_id"]),
                    build_row(rows[0], roles=roles, tier="ligand_receptor_intracellular_output_missing_tf", expression="ligand>receptor>intracellular>????>target_gene_expression" if target else "ligand>receptor>intracellular>????>output", known_layers=known, missing_layers=missing, lr=lr, output=output, anchor=anchor, relay=relay, composition="lr_receptor_relay_output"),
                    "lr_receptor_relay_output",
                )

            direct_tf_ids = {edge.get("target_node_id", "") for edge in receptor_tf_edges}
            compatible_tf_outputs = compatible_edges((lr, relay), tf_outputs_by_anchor)
            for tf_output in compatible_tf_outputs:
                tf_id = tf_output.get("source_node_id", "")
                if tf_id in direct_tf_ids:
                    continue
                anchor = compatible_anchor(lr, relay, tf_output)
                if not anchor:
                    continue
                target = is_target_output(tf_output, roles)
                tier = "explicit_ligand_receptor_intracellular_tf_target" if target else "ligand_receptor_intracellular_tf_output_missing_target_gene"
                known = "ligand|receptor|intracellular_continuation|transcription_factor|target_gene" if target else "ligand|receptor|intracellular_continuation|transcription_factor|output"
                missing = "" if target else "target_gene_expression"
                add_candidate(
                    ("lritf", lr["edge_id"], relay["edge_id"], tf_id, tf_output["edge_id"]),
                    build_row(rows[0], roles=roles, tier=tier, expression="ligand>receptor>intracellular>TF>target_gene_expression" if target else "ligand>receptor>intracellular>TF>output", known_layers=known, missing_layers=missing, lr=lr, output=tf_output, anchor=anchor, relay=relay, composition="lr_receptor_relay_tf_output_without_direct_tf_edge"),
                    "lr_receptor_relay_tf_output_without_direct_tf_edge",
                )

    next_id = next_graph_id(rows)
    for row in additions:
        row["route_evidence_id"] = f"GRAPHROUTE:{next_id:06d}"
        next_id += 1
    summary = {
        "source_route_rows": len(rows),
        "graph_supported_route_rows_added": len(additions),
        "composition_counts": dict(sorted(composition_counts.items())),
        "distinct_ligand_receptor_edges_linked": len({row["ligand_receptor_edge_id"] for row in additions}),
        "rows_with_asserted_intracellular_to_tf_edge": sum(
            bool(row.get("receptor_intracellular_edge_id"))
            and bool(row.get("intracellular_continuation_node_id"))
            and bool(row.get("intracellular_tf_edge_id"))
            for row in additions
        ),
        "rows_with_unasserted_intracellular_to_tf_link": sum(
            "intracellular_to_tf_edge_not_asserted" in row.get("route_linkage_status", "")
            for row in additions
        ),
        "policy": "Exact exported LR edge plus graph components with a shared pathway/evidence anchor; no Cartesian product, causal edge, or confidence assertion.",
    }
    return additions, summary


def update_audit(path: Path, rows: list[dict[str, str]]) -> None:
    if not path.exists():
        return
    audit = json.loads(path.read_text(encoding="utf-8"))
    counts = audit.setdefault("signaling_route_evidence_counts", {})
    counts["route_evidence_record_count"] = len(rows)
    counts["route_evidence_tier_counts"] = dict(sorted(Counter(row.get("route_tier", "") for row in rows).items()))
    counts["route_linkage_status_counts"] = dict(sorted(Counter(row.get("route_linkage_status", "") for row in rows).items()))
    counts["route_evidence_unique_ligands"] = len({row.get("ligand_node_id", "") for row in rows if row.get("ligand_node_id")})
    counts["route_evidence_unique_target_genes"] = len({row.get("target_gene_node_id", "") for row in rows if row.get("target_gene_node_id")})
    counts["route_evidence_unique_transcription_factors"] = len({row.get("transcription_factor_node_id", "") for row in rows if row.get("transcription_factor_node_id")})
    counts["route_evidence_unique_outputs"] = len({row.get("output_node_id", "") or row.get("output_label", "") for row in rows if row.get("output_node_id") or row.get("output_label")})
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
    if not route_path.exists():
        route_path = route_path.with_suffix(route_path.suffix + ".gz")
    rows = read_tsv(route_path)
    additions, summary = compose_graph_routes(rows, output)
    fields = list(rows[0])
    all_rows = rows + additions
    uncompressed_route_path = output / ROUTE_FILE
    write_tsv(uncompressed_route_path, fields, all_rows)
    compressed_route_path = uncompressed_route_path.with_suffix(uncompressed_route_path.suffix + ".gz")
    with uncompressed_route_path.open("rb") as source, gzip.open(compressed_route_path, "wb") as target:
        target.writelines(source)
    uncompressed_route_path.unlink()
    normalized_counts = write_normalized_route_artifacts(
        output,
        all_rows,
        read_tsv(output / "mechanism_nodes.tsv"),
        read_tsv(output / "mechanism_edges.tsv"),
        read_tsv(output / "mechanism_edge_sources.tsv"),
    )
    update_audit(output / "full_signaling_chain_audit.json", all_rows)

    metadata_path = output / "bundle_metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["release_id"] = args.release_id
    metadata.setdefault("counts", {})["signaling_route_evidence"] = len(all_rows)
    metadata.setdefault("graph_policy", {})["graph_supported_route_composition_is_evidence_layer_only"] = True
    statement = (
        "Graph-supported route compositions require an exact exported ligand-receptor edge plus "
        "compatible exported graph components with a shared pathway or evidence anchor; they "
        "do not create graph edges, assert missing intracellular-to-TF edges, or assign confidence."
    )
    if statement not in metadata.setdefault("accuracy_contract", []):
        metadata["accuracy_contract"].append(statement)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    summary.update({"source_bundle": str(source), "output_bundle": str(output), "release_id": args.release_id, **normalized_counts})
    (output / SUMMARY_FILE).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
