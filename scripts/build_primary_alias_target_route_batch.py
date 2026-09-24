#!/usr/bin/env python3
"""Promote source-linked ligand aliases onto existing primary target routes.

Several Module 21B records use an approved gene-symbol or receptor-complex
alias (for example ``Epo`` or ``Il21``) while the canonical route evidence is
stored under a normalized ligand label.  This pass makes those aliases
addressable as separate evidence routes.  It composes only:

* an alias ligand-receptor record that already has a primary locator and
  downstream source linkage; and
* an existing canonical ligand route with an explicit target-gene output.

Relay nodes and edges are retained only when an exact alias-receptor graph
edge or an exact alias source route supports that handoff.  Otherwise the
route keeps the TF and target output but records the intracellular layer as
unresolved.  No graph edge, causal assertion, or confidence score is created.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


ALIAS_TO_CANONICAL = {
    "Bdnf": "BDNF",
    "Epo": "EPO",
    "Growth hormone": "GH1/growth hormone (GH)",
    "Il11": "IL11",
    "Il15": "IL15",
    "Il2": "IL2",
    "Il4": "IL4",
    "Il9": "IL9",
    "Il21": "IL21",
    "Thpo": "TPO",
    "THPO/thrombopoietin (TPO)": "TPO",
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def split_values(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def join_unique(*values: str) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in split_values(value):
            if item not in seen:
                seen.add(item)
                result.append(item)
    return ";".join(result)


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def receptor_identity(value: str) -> frozenset[str]:
    """Extract receptor gene tokens while treating common label aliases alike."""

    tokens = set(re.findall(r"[a-z]+\d+[a-z0-9]*|\b[a-z]{3,}\b", value.casefold()))
    tokens -= {
        "receptor", "complex", "hexamer", "intermediate", "alpha", "beta",
        "gamma", "delta", "containing", "family", "protein", "surface",
    }
    if "trkb" in tokens:
        tokens.add("ntrk2")
        tokens.remove("trkb")
    return frozenset(tokens)


def same_receptor_family(alias_label: str, canonical_label: str) -> bool:
    alias_tokens = receptor_identity(alias_label)
    canonical_tokens = receptor_identity(canonical_label)
    return bool(alias_tokens) and alias_tokens == canonical_tokens


def matching_edge(
    edge_ids: list[str],
    edges: dict[str, dict[str, str]],
    source_node_id: str,
    target_node_id: str,
) -> str:
    for edge_id in edge_ids:
        edge = edges.get(edge_id)
        if edge and edge["source_node_id"] == source_node_id and edge["target_node_id"] == target_node_id:
            return edge_id
    return ""


def make_rows(bundle: Path) -> list[dict[str, str]]:
    expansions = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    queue_ids = {row["queue_id"] for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")}
    evidence_ids = {row["record_id"] for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}

    existing_signatures = {
        tuple(row.get(field, "") for field in (
            "ligand_node_id", "receptor_node_id", "intracellular_continuation_node_id",
            "transcription_factor_node_id", "target_gene_node_id", "output_label",
        ))
        for row in expansions
    }
    alias_rows_by_label: dict[str, list[dict[str, str]]] = {}
    for row in expansions:
        if (
            row.get("ligand_label") in ALIAS_TO_CANONICAL
            and row.get("source_queue_id") in queue_ids
            and row.get("source_evidence_record_id") in evidence_ids
            and row.get("primary_locator")
        ):
            alias_rows_by_label.setdefault(row["ligand_label"], []).append(row)

    canonical_routes = [
        row for row in expansions
        if row.get("path_expression") == "ligand>receptor>intracellular>TF>target_gene_expression"
        and row.get("target_gene_node_id")
        and row.get("transcription_factor_node_id")
        and row.get("primary_locator")
    ]

    rows: list[dict[str, str]] = []
    generated_signatures: set[tuple[str, ...]] = set()
    for alias_label, canonical_label in ALIAS_TO_CANONICAL.items():
        alias_rows = alias_rows_by_label.get(alias_label, [])
        templates = [row for row in canonical_routes if row.get("ligand_label") == canonical_label]
        for alias_row in alias_rows:
            for template in templates:
                if not same_receptor_family(alias_row["receptor_label"], template["receptor_label"]):
                    continue

                relay_node_id = template.get("intracellular_continuation_node_id", "")
                relay_label = template.get("intracellular_continuation_label", "")
                relay_edge_id = ""
                if relay_node_id:
                    relay_edge_id = matching_edge(
                        [template.get("receptor_intracellular_edge_id", "")],
                        edges,
                        alias_row["receptor_node_id"],
                        relay_node_id,
                    )
                    if not relay_edge_id:
                        relay_edge_id = matching_edge(
                            [row.get("receptor_intracellular_edge_id", "") for row in alias_rows
                             if normalize(row.get("intracellular_continuation_label", "")) == normalize(relay_label)],
                            edges,
                            alias_row["receptor_node_id"],
                            relay_node_id,
                        )
                    if not relay_edge_id:
                        relay_node_id = ""
                        relay_label = ""

                tf_node_id = template["transcription_factor_node_id"]
                target_node_id = template["target_gene_node_id"]
                tf_target_edge_id = template.get("tf_target_edge_id", "")
                tf_target_edge = edges.get(tf_target_edge_id)
                if not tf_target_edge or tf_target_edge["source_node_id"] != tf_node_id or tf_target_edge["target_node_id"] != target_node_id:
                    tf_target_edge_id = ""

                signature = (
                    alias_row["ligand_node_id"], alias_row["receptor_node_id"], relay_node_id,
                    tf_node_id, target_node_id, template["output_label"],
                )
                if signature in existing_signatures or signature in generated_signatures:
                    continue
                generated_signatures.add(signature)

                full = bool(relay_node_id)
                path_expression = (
                    "ligand>receptor>intracellular>TF>target_gene_expression"
                    if full else "ligand>receptor>????>TF>target_gene_expression"
                )
                route_tier = (
                    "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges"
                    if full else "ligand_receptor_tf_target_missing_intracellular"
                )
                known_layers = "ligand|receptor|"
                known_layers += "intracellular_continuation|" if full else ""
                known_layers += "transcription_factor|target_gene_expression"
                missing_layers = ""
                if not full:
                    missing_layers = "intracellular_continuation|intracellular_to_tf_edge"
                elif not template.get("intracellular_tf_edge_id"):
                    missing_layers = "intracellular_to_tf_edge"
                if not tf_target_edge_id:
                    missing_layers = join_unique(missing_layers, "tf_to_target_edge")

                row = dict(template)
                row.update({
                    "expansion_id": f"M21B-LITEXP-ALIAS-{normalize(alias_label).upper()}-{len(rows) + 1:04d}",
                    "source_queue_id": alias_row["source_queue_id"],
                    "ligand_node_id": alias_row["ligand_node_id"],
                    "ligand_label": alias_label,
                    "ligand_receptor_edge_id": alias_row["ligand_receptor_edge_id"],
                    "receptor_node_id": alias_row["receptor_node_id"],
                    "receptor_label": alias_row["receptor_label"],
                    "receptor_intracellular_edge_id": relay_edge_id,
                    "intracellular_continuation_node_id": relay_node_id,
                    "intracellular_continuation_label": relay_label,
                    "intracellular_tf_edge_id": "",
                    "transcription_factor_node_id": tf_node_id,
                    "transcription_factor_label": template["transcription_factor_label"],
                    "tf_target_edge_id": tf_target_edge_id,
                    "target_gene_node_id": target_node_id,
                    "target_gene_label": template["target_gene_label"],
                    "output_node_id": target_node_id,
                    "output_label": template["output_label"],
                    "path_expression": path_expression,
                    "route_tier": route_tier,
                    "known_layers": known_layers,
                    "missing_layers": missing_layers,
                    "intracellular_status": "source_supported_alias_composed" if full else "not_mapped_alias_composed",
                    "source_evidence_record_id": alias_row["source_evidence_record_id"],
                    "evidence_ids": join_unique(alias_row.get("evidence_ids", ""), template.get("evidence_ids", ""), alias_row["source_evidence_record_id"]),
                    "source_chain_id": f"alias_target_promotion:{alias_label}:{template['expansion_id']}:{target_node_id}",
                    "route_linkage_status": join_unique(
                        alias_row.get("route_linkage_status", ""),
                        template.get("route_linkage_status", ""),
                        "literature_expansion:alias_target_gene_promotion",
                        "alias_identity_supported_by_source_linked_pair",
                        "receptor_to_intracellular_edge_asserted_as_graph_edge" if relay_edge_id else "receptor_to_intracellular_edge_not_asserted",
                        "intracellular_to_tf_edge_asserted_as_graph_edge" if template.get("intracellular_tf_edge_id") else "intracellular_to_tf_edge_not_asserted",
                        "tf_to_target_edge_asserted_as_graph_edge" if tf_target_edge_id else "tf_to_target_edge_not_asserted",
                        "end_to_end_chain_not_asserted_by_single_source",
                        "evidence_route_only",
                    ),
                    "primary_locator": join_unique(alias_row["primary_locator"], template["primary_locator"]),
                    "citation_note": (
                        f"The {alias_label} ligand/receptor record is linked to the canonical {canonical_label} "
                        "target-gene route using the retained primary locators. The alias is exposed as an "
                        "evidence route; no new graph edge or causal handoff is asserted."
                    ),
                    "evidence_summary": (
                        f"Primary source-linked evidence supports the {alias_label} ligand-receptor input and "
                        f"the canonical {canonical_label} route component ending in {template['target_gene_label']}. "
                        "The alias route preserves exact graph-supported relay layers when present and retains "
                        "unresolved handoffs explicitly."
                    ),
                    "limitations": join_unique(
                        alias_row.get("limitations", ""),
                        template.get("limitations", ""),
                        "This is an alias-composed evidence route rather than a single-paper demonstration of every handoff; no causal edge or confidence score is inferred.",
                    ),
                    "output_class": "target_gene_expression",
                    "curation_status": "curated_primary_route",
                    "source_scope": "alias_composed_primary_evidence",
                })
                rows.append(row)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = make_rows(args.bundle.resolve())
    if not rows:
        raise ValueError("No eligible alias target routes found")
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output.resolve()),
        "rows": len(rows),
        "aliases": len({row["ligand_label"] for row in rows}),
        "full_routes": sum(row["path_expression"] == "ligand>receptor>intracellular>TF>target_gene_expression" for row in rows),
        "partial_routes": sum(row["path_expression"] == "ligand>receptor>????>TF>target_gene_expression" for row in rows),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
