#!/usr/bin/env python3
"""Catalog source-linked full routes already present in route evidence.

This pass does not infer a new route and does not append another route-evidence
record. It exposes previously retained ``LITEXP`` full-route records through
``mechanism_literature_expansion.tsv`` while preserving the existing route ID,
source evidence record, primary locator, non-causal status, and route
limitations.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import shutil
from pathlib import Path


def read_tsv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-bundle", type=Path, required=True)
    parser.add_argument("--output-bundle", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    return parser.parse_args()


def is_full_route(row: dict[str, str]) -> bool:
    layers = row.get("known_layers", "")
    has_target = "target_gene_expression" in layers
    has_output = row.get("route_tier") == "ligand_receptor_intracellular_tf_output_missing_target_gene"
    return (
        row.get("route_evidence_id", "").startswith("LITEXP:")
        and "intracellular_continuation" in layers
        and "transcription_factor" in layers
        and (has_target or has_output)
        and bool(row.get("source_queue_id"))
        and bool(row.get("source_evidence_record_id"))
    )


def build_catalog_row(
    route: dict[str, str],
    source: dict[str, str],
    expansion_id: str,
) -> dict[str, str]:
    output_id = route.get("output_node_id", "") or route.get("target_gene_node_id", "")
    output_label = route.get("output_label", "") or route.get("target_gene_label", "")
    locators = source.get("source_locator", "")
    summary = (
        f"Catalogued existing source-linked full route {route['route_evidence_id']}: "
        f"{route.get('path_expression', '')}. {source.get('evidence_summary', '')}".strip()
    )
    limitations = join_unique(
        source.get("limitations", ""),
        "This catalog row reuses an existing route-evidence record; it does not add a causal edge or confidence score.",
        "The route remains a composed evidence route when its linkage status identifies unresolved handoffs.",
    )
    linkage = join_unique(
        route.get("route_linkage_status", ""),
        "literature_expansion:catalogued_existing_full_route_evidence",
        "end_to_end_chain_not_asserted_by_single_source",
    )
    return {
        "expansion_id": expansion_id,
        "source_queue_id": route.get("source_queue_id", ""),
        "route_status": route.get("route_status", "retained_evidence_route"),
        "path_expression": route.get("path_expression", ""),
        "route_tier": route.get("route_tier", ""),
        "known_layers": route.get("known_layers", ""),
        "missing_layers": route.get("missing_layers", ""),
        "intracellular_status": route.get("intracellular_status", ""),
        "ligand_node_id": route.get("ligand_node_id", ""),
        "ligand_label": route.get("ligand_label", ""),
        "ligand_receptor_edge_id": route.get("ligand_receptor_edge_id", ""),
        "receptor_node_id": route.get("receptor_node_id", ""),
        "receptor_label": route.get("receptor_label", ""),
        "receptor_intracellular_edge_id": route.get("receptor_intracellular_edge_id", ""),
        "intracellular_continuation_node_id": route.get("intracellular_continuation_node_id", ""),
        "intracellular_continuation_label": route.get("intracellular_continuation_label", ""),
        "intracellular_tf_edge_id": route.get("intracellular_tf_edge_id", ""),
        "transcription_factor_node_id": route.get("transcription_factor_node_id", ""),
        "transcription_factor_label": route.get("transcription_factor_label", ""),
        "tf_target_edge_id": route.get("tf_target_edge_id", ""),
        "target_gene_node_id": route.get("target_gene_node_id", ""),
        "target_gene_label": route.get("target_gene_label", ""),
        "target_output_form_id": "",
        "output_node_id": output_id,
        "output_label": output_label,
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": route.get("pathway_name", ""),
        "input_evidence_type": route.get("input_evidence_type", "primary_literature_route_expansion"),
        "output_evidence_type": route.get("output_evidence_type", "primary_composed_downstream_output"),
        "evidence_ids": join_unique(route.get("evidence_ids", ""), route.get("source_evidence_record_id", ""), locators),
        "source_chain_id": f"catalogued_existing_route:{route['route_evidence_id']}",
        "source_evidence_record_id": route.get("source_evidence_record_id", ""),
        "route_linkage_status": linkage,
        "causal_status": route.get("causal_status", "not_asserted"),
        "traversal_status": route.get("traversal_status", "evidence_route_not_causal"),
        "evidence_contract_version": route.get("evidence_contract_version", "mechanism_evidence_v1"),
        "evidence_polarity": route.get("evidence_polarity", "supports"),
        "negative_evidence_status": route.get("negative_evidence_status", "not_evaluated"),
        "evidence_directness": route.get("evidence_directness", "composite_primary_route"),
        "output_class": route.get("output_class", ""),
        "primary_locator": locators,
        "citation_note": source.get("citation_note", ""),
        "evidence_summary": summary,
        "limitations": limitations,
        "curation_status": "curated_primary_route",
        "species_context": route.get("species_context", source.get("species_context", "")),
        "cell_type_context": route.get("cell_type_context", source.get("cell_type_context", "")),
        "compartment_context": route.get("compartment_context", source.get("compartment_context", "")),
        "injury_context": route.get("injury_context", source.get("injury_context", "")),
        "context_scope": route.get("context_scope", source.get("context_scope", "")),
        "assay_or_perturbation": route.get("assay_or_perturbation", source.get("assay_or_perturbation", "")),
        "effect_polarity": route.get("effect_polarity", source.get("effect_polarity", "")),
        "source_scope": route.get("source_scope", "composite_primary_evidence"),
        "route_evidence_id": route["route_evidence_id"],
    }


def main() -> int:
    args = parse_args()
    source_bundle = args.source_bundle.resolve()
    output_bundle = args.output_bundle.resolve()
    if output_bundle.exists():
        raise FileExistsError(f"Output bundle already exists: {output_bundle}")
    shutil.copytree(source_bundle, output_bundle)

    routes = read_tsv(output_bundle / "mechanism_signaling_route_evidence.tsv.gz")
    expansions_path = output_bundle / "mechanism_literature_expansion.tsv"
    expansions = read_tsv(expansions_path)
    mapped_route_ids = {row.get("route_evidence_id", "") for row in expansions}
    evidence = {row["record_id"]: row for row in read_tsv(output_bundle / "mechanism_downstream_evidence_records.tsv")}

    candidates = [
        row for row in routes
        if is_full_route(row)
        and row["route_evidence_id"] not in mapped_route_ids
        and row["source_evidence_record_id"] in evidence
        and evidence[row["source_evidence_record_id"]].get("source_locator", "")
    ]
    candidates.sort(key=lambda row: row["route_evidence_id"])
    catalog_rows = [
        build_catalog_row(route, evidence[route["source_evidence_record_id"]], f"M21B-LITEXP-CATALOG-{index:04d}")
        for index, route in enumerate(candidates, start=1)
    ]
    if catalog_rows:
        fields = list(expansions[0])
        write_tsv(expansions_path, fields, expansions + catalog_rows)

    metadata_path = output_bundle / "bundle_metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["release_id"] = args.release_id
    metadata.setdefault("counts", {})["literature_expansion"] = len(expansions) + len(catalog_rows)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    summary_path = output_bundle / "mechanism_literature_expansion_summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8")) if summary_path.exists() else {}
    summary.update(
        {
            "source_bundle": str(source_bundle),
            "output_bundle": str(output_bundle),
            "release_id": args.release_id,
            "literature_expansion_rows": len(expansions) + len(catalog_rows),
            "literature_expansion_rows_added": len(catalog_rows),
            "route_evidence_rows_before": len(routes),
            "route_evidence_rows_after": len(routes),
            "catalogued_existing_route_evidence_rows": len(catalog_rows),
            "graph_edges_changed": False,
            "causal_edges_created": False,
            "confidence_scores_created": False,
        }
    )
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"rows_added": len(catalog_rows), "route_evidence_rows": len(routes), "release_id": args.release_id}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
