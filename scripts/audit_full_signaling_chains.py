#!/usr/bin/env python3
"""Audit complete and incomplete ligand-to-target signaling paths.

The audit is deliberately narrower than generic graph reachability. A full
chain is one exported, evidence-gated sequence with these role-compatible
steps: ligand --binds_receptor--> receptor --(any exported relay)-->
transcription factor --(induces/represses/regulates_target_gene)--> target
gene. The intracellular continuation may be explicitly represented, summarized
by a receptor-to-TF edge, or absent from the evidence packet. The four layers
may have different pathway labels because the current
release stores receptor-proximal and target-gene evidence in separate module
pathway namespaces. Output bridges and typed-form transitions are excluded;
the graph release contract marks them as conditional or non-causal.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "data" / "processed" / "mechanism_graph_module20_24_v2026_09_01"
TARGET_RELATIONS = {"induces_target_gene", "represses_target_gene", "regulates_target_gene"}

CHAIN_FIELDS = [
    "chain_id",
    "chain_status",
    "missing_steps",
    "ligand_node_id",
    "ligand_label",
    "ligand_receptor_edge_id",
    "ligand_receptor_pathway",
    "receptor_node_id",
    "receptor_label",
    "receptor_tf_edge_id",
    "receptor_tf_pathway",
    "transcription_factor_node_id",
    "transcription_factor_label",
    "tf_target_edge_id",
    "tf_target_pathway",
    "target_gene_node_id",
    "target_gene_label",
    "target_relation",
    "module_sequence",
    "evidence_ids",
]
POSSIBLE_PATH_FIELDS = [
    "possible_path_id",
    "path_status",
    "path_expression",
    "missing_link",
    "ligand_node_id",
    "ligand_label",
    "ligand_receptor_edge_id",
    "receptor_node_id",
    "receptor_label",
    "unknown_relay_label",
    "target_gene_node_id",
    "target_gene_label",
    "target_output_form_id",
    "bridge_id",
    "pathway_name",
    "evidence_ids",
    "causal_status",
    "traversal_status",
]
ROUTE_EVIDENCE_FIELDS = [
    "route_evidence_id", "route_status", "route_tier", "path_expression",
    "known_layers", "missing_layers", "intracellular_status", "ligand_node_id", "ligand_label",
    "ligand_receptor_edge_id", "receptor_node_id", "receptor_label",
    "receptor_intracellular_edge_id", "intracellular_continuation_node_id",
    "intracellular_continuation_label", "intracellular_tf_edge_id",
    "transcription_factor_node_id", "transcription_factor_label",
    "tf_target_edge_id", "target_gene_node_id", "target_gene_label",
    "target_output_form_id", "output_node_id", "output_label", "output_form_id",
    "bridge_id", "pathway_name", "input_evidence_type",
    "output_evidence_type", "evidence_ids", "causal_status", "traversal_status",
    "source_chain_id",
]
DOWNSTREAM_CURATION_FIELDS = [
    "queue_id", "module", "edge_id", "source_node_id", "source_label",
    "target_node_id", "target_label", "graph_relation_type",
    "register_relation_type", "pathway_name", "edge_semantic_class",
    "lr_entry_assessment", "evidence_scope", "evidence_status",
    "evidence_layer", "confidence_tier", "source_locator", "citation_note",
    "evidence_summary", "limitations", "candidate_intracellular_node_id",
    "candidate_intracellular_label", "text_matched_tf_node_ids",
    "text_matched_tf_labels", "text_matched_target_gene_node_ids",
    "text_matched_target_gene_labels", "candidate_output_terms",
    "missing_layers", "curation_priority", "curation_status",
    "do_not_infer_reason",
]

RECEPTOR_LABEL_MARKERS = (
    "receptor", "gpcr", "frizzled", "integrin", "channel", "sensor",
    "tlr", "fzd", "p2x", "p2y", "pdgfr", "vegfr", "csf1r", "csf3r",
    "fgfr", "tgfbr", "bmpr", "epor", "prlr", "il17ra", "il17rc",
    "notch", "plexin", "ntrk", "egfr", "igf1r", "insr", "robo",
    "unc5", "eph", "nrp",
)
LIGAND_BINDING_MARKERS = ("bind", "engage", "agonist", "antagon", "use as")
OUTPUT_TERM_PATTERNS = {
    "reporter_readout": r"\breporter\b",
    "gene_expression_or_transcription": r"\b(?:gene|mrna|transcription|expression)\b",
    "protein_secretion_or_release": r"\b(?:secretion|secreted|release|released)\b",
    "cellular_function_assay": r"\b(?:proliferation|migration|adhesion|outgrowth|survival|invasion)\b",
    "phagocytosis_or_engulfment": r"\b(?:phagocytosis|engulfment|efferocytosis)\b",
    "phosphorylation_or_activation_readout": r"\b(?:phosphorylation|phosphorylated|activation|activated)\b",
    "translocation_or_localization_readout": r"\b(?:translocation|localization|localisation|nuclear)\b",
    "cleavage_or_processing_readout": r"\b(?:cleavage|cleaved|processing)\b",
    "second_messenger_readout": r"\b(?:camp|pip3|calcium|rac1|mapk|akt|erk)\b",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument(
        "--compare-bundle",
        type=Path,
        default=None,
        help="Optional earlier bundle used to record chain-count deltas.",
    )
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--summary", type=Path, default=None)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CHAIN_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_possible_paths(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=POSSIBLE_PATH_FIELDS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def write_route_evidence(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=ROUTE_EVIDENCE_FIELDS,
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def release_path(path: Path) -> str:
    """Return repository-relative paths when the audited bundle is in-repo."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def has_layer(value: str, token: str) -> bool:
    """Match one semicolon-delimited evidence layer without flattening it."""
    return token.casefold() in {part.strip().casefold() for part in value.split(";")}


def label_is_receptor_like(label: str) -> bool:
    normalized = label.casefold()
    return any(marker in normalized for marker in RECEPTOR_LABEL_MARKERS)


def classify_lr_candidate(edge: dict[str, str], roles: dict[str, set[str]]) -> tuple[str, str]:
    """Classify a role-derived LR row without rewriting the graph edge.

    The normalized graph intentionally preserves a many-to-many role layer.
    Consequently, a receptor can also appear as the source of a downstream
    edge and be re-labeled as a ligand by the legacy canonical relation. This
    classifier is conservative and exposes those topology conflicts for
    curation instead of treating every ``binds_receptor`` row as an LR input.
    """
    source = edge.get("source_label", "")
    target = edge.get("target_label", "")
    relation = edge.get("register_relation_type", "") or edge.get("relation_type", "")
    source_receptor_like = label_is_receptor_like(source) or "receptor" in roles.get(edge.get("source_node_id", ""), set())
    target_receptor_like = label_is_receptor_like(target)
    relation_lower = relation.casefold()
    binding_like = any(marker in relation_lower for marker in LIGAND_BINDING_MARKERS)
    downstream_layer = has_layer(edge.get("evidence_layer", ""), "downstream_or_functional")
    proximal_layer = has_layer(edge.get("evidence_layer", ""), "receptor_proximal_or_pathway")

    if source_receptor_like and not target_receptor_like and (downstream_layer or proximal_layer or not binding_like):
        return "receptor_proximal_or_intracellular", "not_a_direct_ligand_receptor_pair"
    if target_receptor_like and binding_like and not source_receptor_like:
        return "likely_ligand_receptor", "explicit_binding_or_activation_to_receptor_like_target"
    if binding_like and edge.get("compartment_context", "").casefold().startswith("extracellular") and not source_receptor_like:
        return "likely_ligand_receptor", "extracellular_binding_or_activation_with_nonreceptor_source_label"
    return "ambiguous_role_or_topology", "role-derived_relation_needs_manual_pair_resolution"


def matched_role_nodes(
    text: str,
    nodes: dict[str, dict[str, str]],
    roles: dict[str, set[str]],
    role: str,
) -> list[tuple[str, str]]:
    """Return exact label/gene-symbol mentions already present in the bundle."""
    normalized_text = text.casefold()
    matches: list[tuple[str, str]] = []
    aliases: list[tuple[str, str, str]] = []
    for node_id, node in nodes.items():
        if role not in roles.get(node_id, set()):
            continue
        for alias in (node.get("canonical_name", ""), node.get("canonical_label", ""), node.get("gene_symbol", "")):
            alias = alias.strip()
            if len(alias) < 4 or alias.casefold() in {"gene", "protein", "complex"}:
                continue
            aliases.append((alias.casefold(), node_id, node.get("canonical_name", alias)))
    for alias, node_id, label in sorted(set(aliases), key=lambda item: (-len(item[0]), item[0], item[1])):
        if re.search(rf"(?<![a-z0-9]){re.escape(alias)}(?![a-z0-9])", normalized_text):
            matches.append((node_id, label))
    return list(dict.fromkeys(matches))


def extract_output_terms(text: str) -> list[str]:
    normalized_text = text.casefold()
    return [name for name, pattern in OUTPUT_TERM_PATTERNS.items() if re.search(pattern, normalized_text)]


def build_downstream_curation_queue(
    bundle_dir: Path,
) -> tuple[list[dict[str, object]], dict[str, object]]:
    """Index Module 21B downstream claims that lack a linked output route.

    This is a curation queue, not a causal edge or a completed signaling
    route. It retains the source evidence packet and records only exact node
    mentions or the observed assay/readout vocabulary. Unknown links remain
    explicit in ``missing_layers``.
    """
    roles: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(bundle_dir / "mechanism_node_roles.tsv"):
        roles[row["node_id"]].add(row["role"])
    nodes = {row["node_id"]: row for row in read_tsv(bundle_dir / "mechanism_nodes.tsv")}
    edges = {
        row["edge_id"]: row
        for row in read_tsv(bundle_dir / "mechanism_edges.tsv")
        if row.get("module") == "21B"
        and row.get("relation_type") == "binds_receptor"
    }
    sources_by_edge: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_tsv(bundle_dir / "mechanism_edge_sources.tsv"):
        if row.get("edge_id") in edges:
            sources_by_edge[row["edge_id"]].append(row)

    queue: list[dict[str, object]] = []
    for edge_id, edge in edges.items():
        source_rows = [row for row in sources_by_edge[edge_id] if has_layer(row.get("evidence_layer", ""), "downstream_or_functional")]
        if not source_rows:
            continue
        semantic_class, assessment = classify_lr_candidate(edge, roles)
        evidence_text = " ".join(
            value
            for source in source_rows
            for value in (source.get("evidence_summary", ""),)
            if value
        )
        tf_matches = matched_role_nodes(evidence_text, nodes, roles, "transcription_factor")
        target_matches = matched_role_nodes(evidence_text, nodes, roles, "target_gene")
        output_terms = extract_output_terms(evidence_text)
        candidate_intracellular = ""
        candidate_intracellular_label = ""
        if semantic_class == "receptor_proximal_or_intracellular":
            candidate_intracellular = edge.get("target_node_id", "")
            candidate_intracellular_label = edge.get("target_label", "")
        if semantic_class == "likely_ligand_receptor":
            missing_layers = "intracellular_continuation|transcription_factor|target_gene_expression_or_output"
            queue_type = "ligand_receptor_edge_with_unlinked_downstream_claim"
        elif semantic_class == "receptor_proximal_or_intracellular":
            missing_layers = "ligand_receptor_input_pair|transcription_factor|target_gene_expression_or_output"
            queue_type = "receptor_proximal_edge_needing_lr_pair_resolution"
        else:
            missing_layers = "ligand_receptor_pair_validation|intracellular_continuation|transcription_factor|target_gene_expression_or_output"
            queue_type = "ambiguous_edge_needing_manual_topology_review"
        direct_edge = any(row.get("source_scope") == "direct_edge" for row in source_rows)
        stable_locator = any(row.get("source_locator_status") == "stable" for row in source_rows)
        priority = "P1" if direct_edge and stable_locator and (tf_matches or target_matches or output_terms) else "P2" if direct_edge else "P3"
        source = source_rows[0]
        queue.append({
            "queue_id": "",
            "module": edge.get("module", "21B"),
            "edge_id": edge_id,
            "source_node_id": edge.get("source_node_id", ""),
            "source_label": edge.get("source_label", ""),
            "target_node_id": edge.get("target_node_id", ""),
            "target_label": edge.get("target_label", ""),
            "graph_relation_type": edge.get("relation_type", ""),
            "register_relation_type": edge.get("register_relation_type", ""),
            "pathway_name": edge.get("pathway_name", ""),
            "edge_semantic_class": queue_type,
            "lr_entry_assessment": assessment,
            "evidence_scope": ";".join(dict.fromkeys(row.get("source_scope", "") for row in source_rows if row.get("source_scope", ""))),
            "evidence_status": edge.get("evidence_status", ""),
            "evidence_layer": ";".join(dict.fromkeys(row.get("evidence_layer", "") for row in source_rows if row.get("evidence_layer", ""))),
            "confidence_tier": source.get("confidence_tier", ""),
            "source_locator": ";".join(dict.fromkeys(row.get("source_locator", "") for row in source_rows if row.get("source_locator", ""))),
            "citation_note": "; ".join(dict.fromkeys(row.get("citation_note", "") for row in source_rows if row.get("citation_note", ""))),
            "evidence_summary": " || ".join(dict.fromkeys(row.get("evidence_summary", "") for row in source_rows if row.get("evidence_summary", ""))),
            "limitations": " || ".join(dict.fromkeys(row.get("limitations", "") for row in source_rows if row.get("limitations", ""))),
            "candidate_intracellular_node_id": candidate_intracellular,
            "candidate_intracellular_label": candidate_intracellular_label,
            "text_matched_tf_node_ids": ";".join(node_id for node_id, _ in tf_matches),
            "text_matched_tf_labels": ";".join(label for _, label in tf_matches),
            "text_matched_target_gene_node_ids": ";".join(node_id for node_id, _ in target_matches),
            "text_matched_target_gene_labels": ";".join(label for _, label in target_matches),
            "candidate_output_terms": ";".join(output_terms),
            "missing_layers": missing_layers,
            "curation_priority": priority,
            "curation_status": "pending_manual_curation",
            "do_not_infer_reason": "Text-level downstream or functional evidence is retained, but missing route links are not promoted to causal graph edges.",
        })
    queue.sort(key=lambda row: (str(row["curation_priority"]), str(row["edge_id"])))
    for index, row in enumerate(queue, start=1):
        row["queue_id"] = f"M21B-DOWNSTREAM:{index:05d}"
    summary = {
        "queue_record_count": len(queue),
        "queue_semantic_class_counts": dict(Counter(str(row["edge_semantic_class"]) for row in queue)),
        "queue_priority_counts": dict(Counter(str(row["curation_priority"]) for row in queue)),
        "queue_records_with_text_matched_tf": sum(bool(row["text_matched_tf_node_ids"]) for row in queue),
        "queue_records_with_text_matched_target_gene": sum(bool(row["text_matched_target_gene_node_ids"]) for row in queue),
        "queue_records_with_output_terms": sum(bool(row["candidate_output_terms"]) for row in queue),
    }
    return queue, summary


def write_downstream_curation_queue(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=DOWNSTREAM_CURATION_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({key: str(value).rstrip() for key, value in row.items()} for row in rows)


def audit(bundle_dir: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    roles: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(bundle_dir / "mechanism_node_roles.tsv"):
        roles[row["node_id"]].add(row["role"])
    nodes = {row["node_id"]: row for row in read_tsv(bundle_dir / "mechanism_nodes.tsv")}
    edges = read_tsv(bundle_dir / "mechanism_edges.tsv")

    ligand_receptor = [
        row for row in edges
        if row["relation_type"] == "binds_receptor"
        and "ligand" in roles[row["source_node_id"]]
        and "receptor" in roles[row["target_node_id"]]
    ]
    receptor_tf = [
        row for row in edges
        if "receptor" in roles[row["source_node_id"]]
        and "transcription_factor" in roles[row["target_node_id"]]
    ]
    tf_target = [
        row for row in edges
        if row["relation_type"] in TARGET_RELATIONS
        and "transcription_factor" in roles[row["source_node_id"]]
        and "target_gene" in roles[row["target_node_id"]]
    ]

    receptor_tf_by_source: dict[str, list[dict[str, str]]] = defaultdict(list)
    tf_target_by_source: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in receptor_tf:
        receptor_tf_by_source[row["source_node_id"]].append(row)
    for row in tf_target:
        tf_target_by_source[row["source_node_id"]].append(row)

    ligand_receptor_by_target: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in ligand_receptor:
        ligand_receptor_by_target[row["target_node_id"]].append(row)

    # Retain evidence-backed path fragments as well as complete chains.  A
    # fragment is only emitted when an adjacent graph edge is absent; this
    # does not infer a missing mechanism or turn the fragment into a causal
    # edge.
    raw_chains: list[tuple[dict[str, str] | None, dict[str, str] | None, dict[str, str] | None]] = []
    for first in ligand_receptor:
        seconds = receptor_tf_by_source[first["target_node_id"]]
        if not seconds:
            raw_chains.append((first, None, None))
            continue
        for second in seconds:
            thirds = tf_target_by_source[second["target_node_id"]]
            if thirds:
                raw_chains.extend((first, second, third) for third in thirds)
            else:
                raw_chains.append((first, second, None))

    receptor_nodes_with_ligand = set(ligand_receptor_by_target)
    tf_nodes_with_receptor = {
        row["target_node_id"] for row in receptor_tf
    }
    for second in receptor_tf:
        if second["source_node_id"] not in receptor_nodes_with_ligand:
            thirds = tf_target_by_source[second["target_node_id"]]
            if thirds:
                raw_chains.extend((None, second, third) for third in thirds)
            else:
                raw_chains.append((None, second, None))
    for third in tf_target:
        if third["source_node_id"] not in tf_nodes_with_receptor:
            raw_chains.append((None, None, third))

    def edge_sort_key(edge: dict[str, str] | None) -> str:
        return edge["edge_id"] if edge else ""

    raw_chains = list({
        tuple(edge["edge_id"] if edge else "" for edge in chain): chain
        for chain in raw_chains
    }.values())
    raw_chains.sort(key=lambda chain: tuple(edge_sort_key(edge) for edge in chain))
    chain_rows: list[dict[str, object]] = []
    for index, (first, second, third) in enumerate(raw_chains, start=1):
        missing_steps = []
        if first is None:
            missing_steps.append("ligand_to_receptor")
        if second is None:
            missing_steps.append("receptor_to_transcription_factor")
        if third is None:
            missing_steps.append("transcription_factor_to_target_gene")
        evidence_ids = ";".join(
            dict.fromkeys(
                value
                for edge in (first, second, third)
                if edge is not None
                for value in edge.get("evidence_ids", "").split(";")
                if value
            )
        )
        first = first or {}
        second = second or {}
        third = third or {}
        chain_rows.append(
            {
                "chain_id": f"CHAIN:{index:05d}",
                "chain_status": "complete" if not missing_steps else "partial",
                "missing_steps": ";".join(missing_steps),
                "ligand_node_id": first.get("source_node_id", ""),
                "ligand_label": first.get("source_label", ""),
                "ligand_receptor_edge_id": first.get("edge_id", ""),
                "ligand_receptor_pathway": first.get("pathway_name", ""),
                "receptor_node_id": first.get("target_node_id", ""),
                "receptor_label": first.get("target_label", ""),
                "receptor_tf_edge_id": second.get("edge_id", ""),
                "receptor_tf_pathway": second.get("pathway_name", ""),
                "transcription_factor_node_id": second.get("target_node_id", ""),
                "transcription_factor_label": second.get("target_label", ""),
                "tf_target_edge_id": third.get("edge_id", ""),
                "tf_target_pathway": third.get("pathway_name", ""),
                "target_gene_node_id": third.get("target_node_id", ""),
                "target_gene_label": third.get("target_label", ""),
                "target_relation": third.get("relation_type", ""),
                "module_sequence": ">".join(
                    edge["module"] for edge in (first, second, third) if edge
                ),
                "evidence_ids": evidence_ids,
            }
        )

    complete_rows = [row for row in chain_rows if row["chain_status"] == "complete"]
    unique_node_chains = {
        (
            row["ligand_node_id"],
            row["receptor_node_id"],
            row["transcription_factor_node_id"],
            row["target_gene_node_id"],
        )
        for row in complete_rows
    }
    unique_edge_chains = {
        (row["ligand_receptor_edge_id"], row["receptor_tf_edge_id"], row["tf_target_edge_id"])
        for row in complete_rows
    }
    same_pathway = [
        row for row in complete_rows
        if row["ligand_receptor_pathway"] == row["receptor_tf_pathway"] == row["tf_target_pathway"]
    ]
    summary: dict[str, object] = {
        "bundle_dir": release_path(bundle_dir),
        "definition": {
            "step_1": "ligand-role source --binds_receptor--> receptor-role target",
            "step_2": "receptor-role source --any exported relay--> transcription_factor-role target",
            "step_3": "transcription_factor-role source --induces/represses/regulates_target_gene--> target_gene-role target",
            "pathway_label_requirement": "none; pathway labels may differ across module namespaces",
            "excluded": ["mechanism_output_bridge_candidates.tsv", "mechanism_output_bridges_validated.tsv", "mechanism_entity_transitions.tsv"],
        },
        "step_edge_counts": {
            "ligand_receptor": len(ligand_receptor),
            "receptor_transcription_factor": len(receptor_tf),
            "transcription_factor_target_gene": len(tf_target),
        },
        "full_chain_counts": {
            "edge_chain_instances": len(complete_rows),
            "unique_edge_chains": len(unique_edge_chains),
            "unique_four_node_topologies": len(unique_node_chains),
            "same_pathway_edge_chain_instances": len(same_pathway),
        },
        "partial_chain_counts": dict(Counter(
            row["missing_steps"]
            for row in chain_rows
            if row["chain_status"] == "partial"
        )),
        "retained_chain_record_count": len(chain_rows),
        "distinct_receptor_transcription_factor_pairs": len({
            (row["receptor_node_id"], row["transcription_factor_node_id"])
            for row in chain_rows
        }),
        "distinct_ligand_receptor_transcription_factor_routes": len({
            (row["ligand_node_id"], row["receptor_node_id"], row["transcription_factor_node_id"])
            for row in chain_rows
        }),
        "module_sequences": dict(Counter(row["module_sequence"] for row in complete_rows)),
        "target_relations_in_full_chains": dict(Counter(row["target_relation"] for row in complete_rows)),
    }
    return chain_rows, summary


def audit_possible_paths(bundle_dir: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    """Retain conservative ligand-to-target hypotheses with an unknown relay."""
    roles: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(bundle_dir / "mechanism_node_roles.tsv"):
        roles[row["node_id"]].add(row["role"])
    nodes = {
        row["node_id"]: row
        for row in read_tsv(bundle_dir / "mechanism_nodes.tsv")
    }
    edges = {
        row["edge_id"]: row
        for row in read_tsv(bundle_dir / "mechanism_edges.tsv")
    }
    validated_path = bundle_dir / "mechanism_output_bridges_validated.tsv"
    if not validated_path.exists():
        return [], {
            "possible_missing_relay_instances": 0,
            "unique_possible_ligand_receptor_target_paths": 0,
        }

    rows: list[dict[str, object]] = []
    for bridge in read_tsv(validated_path):
        target_forms = []
        for form_id in bridge.get("product_form_ids", "").split(";"):
            if not form_id.startswith("OUTPUT_PROTEIN:"):
                continue
            target_node_id = form_id.split(":", 1)[1]
            if "target_gene" in roles[target_node_id]:
                target_forms.append((form_id, target_node_id))
        for edge_id in bridge.get("source_edge_ids", "").split(";"):
            edge = edges.get(edge_id)
            if not edge:
                continue
            if (
                edge["relation_type"] != "binds_receptor"
                or "ligand" not in roles[edge["source_node_id"]]
                or "receptor" not in roles[edge["target_node_id"]]
            ):
                continue
            for form_id, target_node_id in target_forms:
                evidence_ids = ";".join(dict.fromkeys(
                    value
                    for value in (
                        edge.get("evidence_ids", ""),
                        bridge.get("review_evidence_ids", ""),
                    )
                    for value in value.split(";")
                    if value
                ))
                rows.append(
                    {
                        "possible_path_id": "",
                        "path_status": "possible_missing_relay",
                        "path_expression": "ligand>receptor>????>????>target_gene_expression",
                        "missing_link": "receptor_to_intracellular_continuation_and_transcription_factor",
                        "ligand_node_id": edge["source_node_id"],
                        "ligand_label": edge["source_label"],
                        "ligand_receptor_edge_id": edge_id,
                        "receptor_node_id": edge["target_node_id"],
                        "receptor_label": edge["target_label"],
                        "unknown_relay_label": "????",
                        "target_gene_node_id": target_node_id,
                        "target_gene_label": nodes[target_node_id]["canonical_name"],
                        "target_output_form_id": form_id,
                        "bridge_id": bridge["bridge_id"],
                        "pathway_name": edge["pathway_name"],
                        "evidence_ids": evidence_ids,
                        "causal_status": "not_asserted",
                        "traversal_status": "possible_path_not_traversable",
                    }
                )

    rows.sort(key=lambda row: (
        row["ligand_receptor_edge_id"],
        row["target_gene_node_id"],
        row["bridge_id"],
    ))
    for index, row in enumerate(rows, start=1):
        row["possible_path_id"] = f"POSSIBLE:{index:05d}"
    summary = {
        "possible_missing_relay_instances": len(rows),
        "unique_possible_ligand_receptor_target_paths": len({
            (
                row["ligand_receptor_edge_id"],
                row["target_gene_node_id"],
            )
            for row in rows
        }),
    }
    return rows, summary


def build_route_evidence(
    bundle_dir: Path,
    chain_rows: list[dict[str, object]],
    possible_rows: list[dict[str, object]],
) -> tuple[list[dict[str, object]], dict[str, object]]:
    """Build a reusable evidence route index without asserting causal paths."""
    roles: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(bundle_dir / "mechanism_node_roles.tsv"):
        roles[row["node_id"]].add(row["role"])
    nodes = {row["node_id"]: row for row in read_tsv(bundle_dir / "mechanism_nodes.tsv")}
    edges = read_tsv(bundle_dir / "mechanism_edges.tsv")
    edge_by_id = {row["edge_id"]: row for row in edges}
    route_rows: list[dict[str, object]] = []
    seen: set[tuple[str, ...]] = set()

    def add(key: tuple[str, ...], row: dict[str, object]) -> None:
        if key in seen:
            return
        seen.add(key)
        route_rows.append(row)

    def base_row(
        *,
        tier: str,
        expression: str,
        known_layers: str,
        missing_layers: str,
        ligand_node_id: str = "",
        ligand_label: str = "",
        ligand_receptor_edge_id: str = "",
        receptor_node_id: str = "",
        receptor_label: str = "",
        receptor_intracellular_edge_id: str = "",
        intracellular_continuation_node_id: str = "",
        intracellular_continuation_label: str = "",
        intracellular_tf_edge_id: str = "",
        transcription_factor_node_id: str = "",
        transcription_factor_label: str = "",
        tf_target_edge_id: str = "",
        target_gene_node_id: str = "",
        target_gene_label: str = "",
        target_output_form_id: str = "",
        output_node_id: str = "",
        output_label: str = "",
        output_form_id: str = "",
        bridge_id: str = "",
        pathway_name: str = "",
        input_evidence_type: str = "",
        output_evidence_type: str = "",
        evidence_ids: str = "",
        source_chain_id: str = "",
        intracellular_status: str = "not_assessed",
    ) -> dict[str, object]:
        return {
            "route_evidence_id": "",
            "route_status": "retained_evidence_route",
            "route_tier": tier,
            "path_expression": expression,
            "known_layers": known_layers,
            "missing_layers": missing_layers,
            "intracellular_status": intracellular_status,
            "ligand_node_id": ligand_node_id,
            "ligand_label": ligand_label,
            "ligand_receptor_edge_id": ligand_receptor_edge_id,
            "receptor_node_id": receptor_node_id,
            "receptor_label": receptor_label,
            "receptor_intracellular_edge_id": receptor_intracellular_edge_id,
            "intracellular_continuation_node_id": intracellular_continuation_node_id,
            "intracellular_continuation_label": intracellular_continuation_label,
            "intracellular_tf_edge_id": intracellular_tf_edge_id,
            "transcription_factor_node_id": transcription_factor_node_id,
            "transcription_factor_label": transcription_factor_label,
            "tf_target_edge_id": tf_target_edge_id,
            "target_gene_node_id": target_gene_node_id,
            "target_gene_label": target_gene_label,
            "target_output_form_id": target_output_form_id,
            "output_node_id": output_node_id,
            "output_label": output_label,
            "output_form_id": output_form_id,
            "bridge_id": bridge_id,
            "pathway_name": pathway_name,
            "input_evidence_type": input_evidence_type,
            "output_evidence_type": output_evidence_type,
            "evidence_ids": evidence_ids,
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "source_chain_id": source_chain_id,
        }

    for edge in edges:
        if (
            edge["relation_type"] != "binds_receptor"
            or "ligand" not in roles[edge["source_node_id"]]
            or "receptor" not in roles[edge["target_node_id"]]
        ):
            continue
        add(
            ("lr_entry", edge["edge_id"]),
            base_row(
                tier="ligand_receptor_entry_only",
                expression="ligand>receptor",
                known_layers="ligand|receptor",
                missing_layers="intracellular_continuation|transcription_factor|target_gene_expression",
                ligand_node_id=edge["source_node_id"],
                ligand_label=edge.get("source_label", ""),
                ligand_receptor_edge_id=edge["edge_id"],
                receptor_node_id=edge["target_node_id"],
                receptor_label=edge.get("target_label", ""),
                pathway_name=edge.get("pathway_name", ""),
                input_evidence_type="ligand_receptor_edge",
                evidence_ids=edge.get("evidence_ids", ""),
            ),
        )

    for row in chain_rows:
        first_id = str(row.get("ligand_receptor_edge_id", ""))
        second_id = str(row.get("receptor_tf_edge_id", ""))
        third_id = str(row.get("tf_target_edge_id", ""))
        if first_id and second_id and third_id:
            add(
                ("lr_tf_target", first_id, second_id, third_id),
                base_row(
                    tier="ligand_receptor_tf_target_missing_intracellular",
                    expression="ligand>receptor>????>TF>target_gene_expression",
                    known_layers="ligand|receptor|transcription_factor|target_gene",
                    missing_layers="intracellular_continuation",
                    intracellular_status="collapsed_in_receptor_tf_edge",
                    ligand_node_id=str(row["ligand_node_id"]),
                    ligand_label=str(row["ligand_label"]),
                    ligand_receptor_edge_id=first_id,
                    receptor_node_id=str(row["receptor_node_id"]),
                    receptor_label=str(row["receptor_label"]),
                    intracellular_tf_edge_id=second_id,
                    transcription_factor_node_id=str(row["transcription_factor_node_id"]),
                    transcription_factor_label=str(row["transcription_factor_label"]),
                    tf_target_edge_id=third_id,
                    target_gene_node_id=str(row["target_gene_node_id"]),
                    target_gene_label=str(row["target_gene_label"]),
                    output_node_id=str(row["target_gene_node_id"]),
                    output_label=str(row["target_gene_label"]),
                    pathway_name="|".join(
                        value for value in (
                            str(row["ligand_receptor_pathway"]),
                            str(row["receptor_tf_pathway"]),
                            str(row["tf_target_pathway"]),
                        ) if value
                    ),
                    input_evidence_type="ligand_receptor_edge",
                    output_evidence_type="tf_target_edge",
                    evidence_ids=str(row["evidence_ids"]),
                    source_chain_id=str(row["chain_id"]),
                ),
            )
        elif first_id and second_id:
            add(
                ("lr_tf", first_id, second_id),
                base_row(
                    tier="ligand_receptor_tf_missing_intracellular_and_output",
                    expression="ligand>receptor>????>TF>????",
                    known_layers="ligand|receptor|transcription_factor",
                    missing_layers="intracellular_continuation|target_gene_expression",
                    intracellular_status="collapsed_in_receptor_tf_edge",
                    ligand_node_id=str(row["ligand_node_id"]),
                    ligand_label=str(row["ligand_label"]),
                    ligand_receptor_edge_id=first_id,
                    receptor_node_id=str(row["receptor_node_id"]),
                    receptor_label=str(row["receptor_label"]),
                    intracellular_tf_edge_id=second_id,
                    transcription_factor_node_id=str(row["transcription_factor_node_id"]),
                    transcription_factor_label=str(row["transcription_factor_label"]),
                    pathway_name="|".join(
                        value for value in (
                            str(row["ligand_receptor_pathway"]),
                            str(row["receptor_tf_pathway"]),
                        ) if value
                    ),
                    input_evidence_type="ligand_receptor_edge",
                    evidence_ids=str(row["evidence_ids"]),
                    source_chain_id=str(row["chain_id"]),
                ),
            )
        elif third_id:
            third_edge = edge_by_id.get(third_id, {})
            tf_node_id = str(row.get("transcription_factor_node_id", "")) or str(third_edge.get("source_node_id", ""))
            tf_label = str(row.get("transcription_factor_label", "")) or str(third_edge.get("source_label", ""))
            target_node_id = str(row.get("target_gene_node_id", "")) or str(third_edge.get("target_node_id", ""))
            target_label = str(row.get("target_gene_label", "")) or str(third_edge.get("target_label", ""))
            add(
                ("tf_target", third_id),
                base_row(
                    tier="tf_target_output_only",
                    expression="????>TF>target_gene_expression",
                    known_layers="transcription_factor|target_gene",
                    missing_layers="ligand|receptor|intracellular_continuation",
                    intracellular_status="not_assessed",
                    intracellular_tf_edge_id=second_id,
                    transcription_factor_node_id=tf_node_id,
                    transcription_factor_label=tf_label,
                    tf_target_edge_id=third_id,
                    target_gene_node_id=target_node_id,
                    target_gene_label=target_label,
                    output_node_id=target_node_id,
                    output_label=target_label,
                    pathway_name="|".join(
                        value for value in (
                            str(row["receptor_tf_pathway"]),
                            str(row["tf_target_pathway"]),
                        ) if value
                    ),
                    output_evidence_type="tf_target_edge",
                    evidence_ids=str(row["evidence_ids"]),
                    source_chain_id=str(row["chain_id"]),
                ),
            )

    bridge_inputs: list[tuple[str, dict[str, str]]] = []
    validated_output_path = bundle_dir / "mechanism_output_bridges_validated.tsv"
    if validated_output_path.exists():
        bridge_inputs.extend(("validated_output_bridge", row) for row in read_tsv(validated_output_path))
    review_output_path = bundle_dir / "mechanism_output_bridge_candidates.tsv"
    if review_output_path.exists():
        bridge_inputs.extend(("review_output_candidate", row) for row in read_tsv(review_output_path))

    for evidence_type, bridge in bridge_inputs:
        source_edge_rows = [
            edge_by_id[edge_id]
            for edge_id in str(bridge.get("source_edge_ids", "")).split(";")
            if edge_id in edge_by_id
            and edge_by_id[edge_id]["relation_type"] == "binds_receptor"
            and "ligand" in roles[edge_by_id[edge_id]["source_node_id"]]
            and "receptor" in roles[edge_by_id[edge_id]["target_node_id"]]
        ]
        if not source_edge_rows:
            continue
        output_records: list[tuple[str, str, str]] = []
        for form_id in str(bridge.get("product_form_ids", "")).split(";"):
            if not form_id.startswith("OUTPUT_PROTEIN:"):
                continue
            output_node_id = form_id.split(":", 1)[1]
            output_records.append((form_id, output_node_id, nodes.get(output_node_id, {}).get("canonical_name", "")))
        if not output_records:
            output_label = str(bridge.get("output_label", "") or bridge.get("target_or_program_label", "")).strip()
            if output_label:
                output_records.append(("", "", output_label))
        evidence_ids = ";".join(dict.fromkeys(
            value
            for value in (
                str(bridge.get("review_evidence_ids", "")),
                str(bridge.get("review_evidence_id", "")),
                str(bridge.get("evidence_ids", "")),
            )
            for value in value.split(";")
            if value
        ))
        bridge_id = str(bridge.get("bridge_id", "") or bridge.get("candidate_id", ""))
        for edge in source_edge_rows:
            for output_form_id, output_node_id, output_label in output_records:
                is_target_gene = "target_gene" in roles[output_node_id]
                expression = (
                    "ligand>receptor>????>????>target_gene_expression"
                    if is_target_gene else "ligand>receptor>????>????>output"
                )
                add(
                    ("bridge_output", evidence_type, bridge_id, edge["edge_id"], output_form_id or output_label),
                    base_row(
                        tier="ligand_receptor_output_missing_intracellular_and_tf",
                        expression=expression,
                        known_layers="ligand|receptor|output",
                        missing_layers="intracellular_continuation|transcription_factor",
                        intracellular_status="not_mapped",
                        ligand_node_id=edge["source_node_id"],
                        ligand_label=edge.get("source_label", ""),
                        ligand_receptor_edge_id=edge["edge_id"],
                        receptor_node_id=edge["target_node_id"],
                        receptor_label=edge.get("target_label", ""),
                        target_gene_node_id=output_node_id if is_target_gene else "",
                        target_gene_label=output_label if is_target_gene else "",
                        target_output_form_id=output_form_id if is_target_gene else "",
                        output_node_id=output_node_id,
                        output_label=output_label,
                        output_form_id=output_form_id,
                        bridge_id=bridge_id,
                        pathway_name=str(bridge.get("pathway_name", "") or edge.get("pathway_name", "")),
                        input_evidence_type="ligand_receptor_edge",
                        output_evidence_type=evidence_type,
                        evidence_ids=";".join(dict.fromkeys(
                            value
                            for value in (edge.get("evidence_ids", ""), evidence_ids)
                            for value in value.split(";")
                            if value
                        )),
                        source_chain_id=bridge_id,
                    ),
                )

    route_rows.sort(key=lambda row: (
        str(row["route_tier"]),
        str(row["ligand_receptor_edge_id"]),
        str(row["intracellular_tf_edge_id"]),
        str(row["tf_target_edge_id"]),
        str(row["bridge_id"]),
    ))
    for index, row in enumerate(route_rows, start=1):
        row["route_evidence_id"] = f"ROUTE:{index:05d}"
    summary = {
        "route_evidence_record_count": len(route_rows),
        "route_evidence_tier_counts": dict(Counter(str(row["route_tier"]) for row in route_rows)),
        "route_evidence_unique_ligands": len({
            str(row["ligand_node_id"])
            for row in route_rows
            if str(row["ligand_node_id"])
        }),
        "route_evidence_unique_target_genes": len({
            str(row["target_gene_node_id"])
            for row in route_rows
            if str(row["target_gene_node_id"])
        }),
        "route_evidence_unique_outputs": len({
            (str(row["output_node_id"]), str(row["output_form_id"]), str(row["output_label"]))
            for row in route_rows
            if str(row["output_node_id"]) or str(row["output_form_id"]) or str(row["output_label"])
        }),
    }
    return route_rows, summary


def update_bundle_metadata(
    bundle_dir: Path,
    possible_path: Path,
    possible_count: int,
    route_evidence_path: Path,
    route_evidence_count: int,
    downstream_queue_path: Path,
    downstream_queue_count: int,
) -> None:
    """Register the hypothesis artifact without changing graph-edge counts."""
    metadata_path = bundle_dir / "bundle_metadata.json"
    if not metadata_path.exists():
        return
    metadata = json.loads(metadata_path.read_text())
    metadata.setdefault("files", {})["possible_signaling_paths"] = possible_path.name
    metadata.setdefault("files", {})["signaling_route_evidence"] = route_evidence_path.name
    metadata.setdefault("files", {})["downstream_curation_queue"] = downstream_queue_path.name
    metadata.setdefault("counts", {})["possible_signaling_paths"] = possible_count
    metadata.setdefault("counts", {})["signaling_route_evidence"] = route_evidence_count
    metadata.setdefault("counts", {})["downstream_curation_queue"] = downstream_queue_count
    policy = metadata.setdefault("graph_policy", {})
    policy["possible_signaling_paths_are_hypotheses_only"] = True
    policy["possible_signaling_paths_are_not_graph_edges"] = True
    policy["signaling_route_evidence_is_hypothesis_layer_only"] = True
    policy["signaling_route_evidence_is_not_graph_edges"] = True
    contract = metadata.setdefault("accuracy_contract", [])
    statement = (
        "Possible signaling paths retain validated ligand-receptor and target-output "
        "evidence with unknown relays; they are hypotheses, not causal graph edges."
    )
    if statement not in contract:
        contract.append(statement)
    route_statement = (
        "Signaling route evidence retains ligand, receptor, intracellular, TF, and output "
        "evidence at different completeness tiers for downstream plausibility scoring."
    )
    if route_statement not in contract:
        contract.append(route_statement)
    queue_statement = (
        "The Module 21B downstream curation queue retains text-level functional claims "
        "and exact node mentions for manual route-link curation; it is not a causal edge layer."
    )
    if queue_statement not in contract:
        contract.append(queue_statement)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")


def main() -> None:
    args = parse_args()
    bundle_dir = args.bundle_dir.resolve()
    output = (args.output or bundle_dir / "full_signaling_chain_audit.tsv").resolve()
    summary_path = (args.summary or bundle_dir / "full_signaling_chain_audit.json").resolve()
    possible_output = bundle_dir / "mechanism_possible_signaling_paths.tsv"
    route_evidence_output = bundle_dir / "mechanism_signaling_route_evidence.tsv"
    downstream_queue_output = bundle_dir / "mechanism_downstream_curation_queue.tsv"
    rows, summary = audit(bundle_dir)
    possible_rows, possible_summary = audit_possible_paths(bundle_dir)
    route_evidence_rows, route_evidence_summary = build_route_evidence(
        bundle_dir,
        rows,
        possible_rows,
    )
    downstream_queue_rows, downstream_queue_summary = build_downstream_curation_queue(bundle_dir)
    summary["possible_path_counts"] = possible_summary
    summary["signaling_route_evidence_counts"] = route_evidence_summary
    summary["downstream_curation_queue_counts"] = downstream_queue_summary
    if args.compare_bundle:
        _, previous = audit(args.compare_bundle.resolve())
        current_counts = summary["full_chain_counts"]
        previous_counts = previous["full_chain_counts"]
        summary["comparison"] = {
            "prior_bundle_dir": release_path(args.compare_bundle.resolve()),
            "prior_full_chain_counts": previous_counts,
            "prior_partial_chain_counts": previous["partial_chain_counts"],
            "prior_retained_chain_record_count": previous["retained_chain_record_count"],
            "delta": {
                key: current_counts[key] - previous_counts[key]
                for key in current_counts
                if key in previous_counts
            },
            "partial_delta": {
                key: summary["partial_chain_counts"].get(key, 0) - previous["partial_chain_counts"].get(key, 0)
                for key in set(summary["partial_chain_counts"]) | set(previous["partial_chain_counts"])
            },
            "retained_chain_record_delta": (
                summary["retained_chain_record_count"]
                - previous["retained_chain_record_count"]
            ),
        }
    write_tsv(output, rows)
    write_possible_paths(possible_output, possible_rows)
    write_route_evidence(route_evidence_output, route_evidence_rows)
    write_downstream_curation_queue(downstream_queue_output, downstream_queue_rows)
    update_bundle_metadata(
        bundle_dir,
        possible_output,
        len(possible_rows),
        route_evidence_output,
        len(route_evidence_rows),
        downstream_queue_output,
        len(downstream_queue_rows),
    )
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary["full_chain_counts"], sort_keys=True))


if __name__ == "__main__":
    main()
