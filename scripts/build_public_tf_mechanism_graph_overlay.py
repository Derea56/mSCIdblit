#!/usr/bin/env python3
"""Add explicitly adjudicated public-TF edges to a graph release candidate.

The base graph is copied forward without modification. Only rows present in
the public-TF validated-edge layer are added as traversable edges; the full
public-TF candidate layer is copied alongside the graph as an auditable
non-traversable overlay.
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import unicodedata
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_08_26"
DEFAULT_LAYER = ROOT / "data/processed/public_tf_mechanism_layer_v2026_08_30"
DEFAULT_OUTPUT = ROOT / "data/processed/mechanism_graph_module20_24_v2026_08_30"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-dir", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--layer-dir", type=Path, default=DEFAULT_LAYER)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def node_key(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).strip().split()).casefold()


def split_semicolon(value: str) -> set[str]:
    return {x.strip() for x in value.split(";") if x.strip()}


def join_semicolon(values: set[str]) -> str:
    return ";".join(sorted(values))


def add_role(roles: list[dict[str, str]], node_id: str, role: str, evidence: str) -> None:
    if any(r["node_id"] == node_id and r["role"] == role for r in roles):
        return
    roles.append(
        {
            "node_id": node_id,
            "role": role,
            "role_source": "public_tf_validated_edge",
            "role_evidence": evidence,
        }
    )


def main() -> int:
    args = parse_args()
    base = args.base_dir.resolve()
    layer = args.layer_dir.resolve()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)

    base_metadata = json.loads((base / "bundle_metadata.json").read_text(encoding="utf-8"))
    nodes = read_tsv(base / "mechanism_nodes.tsv")
    roles = read_tsv(base / "mechanism_node_roles.tsv")
    edges = read_tsv(base / "mechanism_edges.tsv")
    sources = read_tsv(base / "mechanism_edge_sources.tsv")
    pathways = read_tsv(base / "mechanism_pathways.tsv")
    boundaries = read_tsv(base / "mechanism_boundary_summary.tsv")
    validated = read_tsv(layer / "public_tf_validated_edge_layer.tsv")
    candidates_path = layer / "public_tf_candidate_layer.tsv"
    if not validated or not candidates_path.exists():
        raise SystemExit("public-TF layer is missing validated rows or candidate layer")

    node_by_key = {node_key(row["canonical_name"]): row for row in nodes}
    role_by_node = {row["node_id"]: row for row in roles}
    max_node = max(int(row["node_id"].removeprefix("NODE")) for row in nodes)
    next_node = max_node + 1

    def resolve_or_add_node(label: str, module: str, pathway: str, edge_count: int) -> str:
        nonlocal next_node
        key = node_key(label)
        existing = node_by_key.get(key)
        if existing:
            modules = split_semicolon(existing.get("modules", ""))
            modules.add(module)
            existing["modules"] = join_semicolon(modules)
            pathways_set = split_semicolon(existing.get("pathways", ""))
            pathways_set.add(pathway)
            existing["pathways"] = join_semicolon(pathways_set)
            existing["exportable_edge_count"] = str(int(existing.get("exportable_edge_count", "0")) + edge_count)
            existing["notes"] = (
                existing.get("notes", "")
                + f"; public_tf_validated_edge_count_added={edge_count}"
            )
            return existing["node_id"]
        node_id = f"NODE{next_node:05d}"
        next_node += 1
        row = {
            "node_id": node_id,
            "canonical_name": label,
            "node_type": "transcription_factor",
            "node_subtype": "public_tf_validated_general_mechanism",
            "gene_symbol": label,
            "organism_scope": "mouse",
            "compartment": "",
            "notes": f"public-TF validated edge source; module={module}; pathway={pathway}; exportable_edge_count={edge_count}",
            "canonical_label": label,
            "label_variants": label,
            "modules": module,
            "pathways": pathway,
            "exportable_edge_count": str(edge_count),
        }
        nodes.append(row)
        node_by_key[key] = row
        return node_id

    edge_ids = {row["edge_id"] for row in edges}
    source_ids = {row["edge_source_id"] for row in sources}
    pathway_index = {(row["module"], row["pathway_name"]): row for row in pathways}
    for row in sorted(validated, key=lambda r: r["layer_record_id"]):
        edge_id = f"PTF-EDGE-{row['module']}-{row['integration_id'].split('-')[-1]}"
        source_id = f"PTF-SRC-{row['module']}-{row['integration_id'].split('-')[-1]}"
        if edge_id in edge_ids or source_id in source_ids:
            raise SystemExit(f"public-TF graph identifier already exists: {edge_id} or {source_id}")
        pathway = "public_tf_validated_target_gene_evidence"
        source_label = row["raw_tf_symbol"] or row["regulator_symbol"]
        source_node = resolve_or_add_node(source_label, row["module"], pathway, 1)
        target_node = resolve_or_add_node(row["target_symbol"], row["module"], pathway, 1)
        evidence = f"edge={edge_id}; promotion={row['promotion_id']}; decision={row['decision_id']}"
        add_role(roles, source_node, "signaling_cascade", evidence)
        add_role(roles, source_node, "transcription_factor", evidence)
        add_role(roles, target_node, "target_gene", evidence)
        citations = ";".join(
            x for x in [row.get("primary_citation", ""), row.get("corroborating_citation", "")] if x
        )
        edges.append(
            {
                "edge_id": edge_id,
                "module": row["module"],
                "source_node_id": source_node,
                "target_node_id": target_node,
                "pathway_label": pathway,
                "effect_polarity": row["validated_effect_polarity"],
                "evidence_status": "validated_general_mechanism_edge",
                "notes": row["limitations"],
                "source_label": source_label,
                "relation_type": row["validated_relation_type"],
                "register_relation_type": "public_tf_validated_target_gene",
                "target_label": row["target_symbol"],
                "pathway_name": pathway,
                "evidence_layer": "public_tf_validated_edge",
                "edge_status": "validated_general_mechanism_edge",
                "context_scope": row["context_evidence_scope"],
                "cell_type_context": "",
                "compartment_context": "",
                "species_context": row["species_scope"],
                "injury_context": "not_SCI_context",
                "confidence_tier": "high",
                "export_priority": "medium",
                "evidence_ids": row["promotion_id"],
                "evidence_count": "1",
                "source_locator_count": "1",
                "exportable": "true",
                "consolidation_note": row["validation_basis"],
            }
        )
        sources.append(
            {
                "edge_source_id": source_id,
                "edge_id": edge_id,
                "paper_id": "",
                "observation_id": "",
                "claim_id": "",
                "support_kind": "primary_experiment",
                "species_support": row["species_scope"],
                "source_scope": "direct_edge",
                "confidence_tier": "high",
                "citation_note": citations,
                "notes": row["limitations"],
                "module": row["module"],
                "evidence_id": row["promotion_id"],
                "source_kind": "public_tf_primary_literature",
                "source_locator": citations,
                "source_locator_status": "stable",
                "evidence_summary": row["validation_basis"],
                "limitations": row["limitations"],
                "evidence_layer": "public_tf_validated_edge",
                "evidence_exportable": "true",
                "consolidation_note": row["validation_basis"],
            }
        )
        pathway_row = pathway_index.get((row["module"], pathway))
        if pathway_row is None:
            pathway_row = {
                "module": row["module"],
                "pathway_name": pathway,
                "edge_count": "0",
                "node_count": "0",
                "evidence_count": "0",
            }
            pathways.append(pathway_row)
            pathway_index[(row["module"], pathway)] = pathway_row
        pathway_row["edge_count"] = str(int(pathway_row["edge_count"]) + 1)
        pathway_row["evidence_count"] = str(int(pathway_row["evidence_count"]) + 1)

    for pathway_row in pathways:
        matching_edges = [
            row for row in edges
            if row["module"] == pathway_row["module"] and row["pathway_name"] == pathway_row["pathway_name"]
        ]
        pathway_row["node_count"] = str(len({
            x for row in matching_edges for x in (row["source_node_id"], row["target_node_id"])
        }))

    edges.sort(key=lambda row: (row["module"], row["edge_id"]))
    sources.sort(key=lambda row: row["edge_source_id"])
    nodes.sort(key=lambda row: row["node_id"])
    roles.sort(key=lambda row: (row["node_id"], row["role"]))
    pathways.sort(key=lambda row: (row["module"], row["pathway_name"]))

    for name in [
        "mechanism_nodes.tsv", "mechanism_node_roles.tsv", "mechanism_edges.tsv",
        "mechanism_edge_sources.tsv", "mechanism_pathways.tsv", "mechanism_boundary_summary.tsv",
    ]:
        shutil.copy2(base / name, output / name)
    write_tsv(output / "mechanism_nodes.tsv", list(nodes[0]), nodes)
    write_tsv(output / "mechanism_node_roles.tsv", list(roles[0]), roles)
    write_tsv(output / "mechanism_edges.tsv", list(edges[0]), edges)
    write_tsv(output / "mechanism_edge_sources.tsv", list(sources[0]), sources)
    write_tsv(output / "mechanism_pathways.tsv", list(pathways[0]), pathways)

    for name in [
        "public_tf_candidate_layer.tsv",
        "public_tf_validated_edge_layer.tsv",
        "layer_metadata.json",
    ]:
        shutil.copy2(layer / name, output / name)

    metadata = dict(base_metadata)
    metadata["release_id"] = "module20_24_mechanism_graph:2026-08-30"
    metadata["generated_at"] = "2026-08-30"
    metadata["release_status"] = "candidate_register_backed_graph_with_public_tf_validated_layer"
    metadata["source_scope"] = "validated Module 20B-24B registers plus explicitly adjudicated public-TF layer"
    metadata["counts"] = dict(metadata["counts"])
    metadata["counts"].update(
        {
            "nodes": len(nodes),
            "edges": len(edges),
            "edge_sources": len(sources),
            "node_roles": len(roles),
            "nodes_with_ligand_role": len({r["node_id"] for r in roles if r["role"] == "ligand"}),
            "nodes_with_receptor_role": len({r["node_id"] for r in roles if r["role"] == "receptor"}),
            "nodes_with_transcription_factor_role": len({r["node_id"] for r in roles if r["role"] == "transcription_factor"}),
            "nodes_with_target_gene_role": len({r["node_id"] for r in roles if r["role"] == "target_gene"}),
            "pathways": len(pathways),
        }
    )
    metadata["source_locator_status_counts"] = dict(
        sorted(Counter(row["source_locator_status"] for row in sources).items())
    )
    metadata["module_counts"] = []
    for module in sorted({row["module"] for row in edges}):
        base_row = next((x for x in base_metadata["module_counts"] if x["module"] == module), None)
        module_edges = [x for x in edges if x["module"] == module]
        module_sources = [x for x in sources if x["module"] == module]
        module_paths = {x["pathway_name"] for x in module_edges}
        base_path_count = base_row["pathway_count"] if base_row else 0
        base_pathways = {
            x["pathway_name"] for x in pathways
            if x["module"] == module and not x["pathway_name"].startswith("public_tf_validated_")
        }
        metadata["module_counts"].append(
            {
                "module": module,
                "edge_count": base_row["edge_count"] if base_row else len(module_edges),
                "exportable_edge_count": len(module_edges),
                "evidence_count": (base_row["evidence_count"] if base_row else 0) + len(module_sources),
                "pathway_count": base_path_count + len(module_paths - base_pathways),
                "nonexportable_edge_count": base_row["nonexportable_edge_count"] if base_row else 0,
            }
        )
    metadata["public_tf_layer"] = {
        "candidate_rows": len(read_tsv(layer / "public_tf_candidate_layer.tsv")),
        "validated_edge_module_rows": len(validated),
        "validated_edge_unique_pairs": len({
            (x["regulator_symbol"], x["target_symbol"], x["species_scope"]) for x in validated
        }),
        "candidate_artifact": "public_tf_candidate_layer.tsv",
        "validated_artifact": "public_tf_validated_edge_layer.tsv",
        "all_other_candidate_rows_traversable": False,
    }
    metadata["files"] = dict(metadata["files"])
    metadata["files"].update(
        {
            "public_tf_candidates": "public_tf_candidate_layer.tsv",
            "public_tf_validated_edges": "public_tf_validated_edge_layer.tsv",
            "public_tf_layer_metadata": "layer_metadata.json",
        }
    )
    (output / "bundle_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output_dir": str(output), "counts": metadata["counts"], "public_tf_layer": metadata["public_tf_layer"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
