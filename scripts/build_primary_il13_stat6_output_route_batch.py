#!/usr/bin/env python3
"""Build evidence-only IL-13 type-II-receptor/TYK2/STAT6 output routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


TARGETS = (
    ("M21B-E008954", "MRC1", "M21B-E008629"),
    ("M21B-E008956", "RETNLA", "M21B-E008365"),
    ("M21B-E008958", "CHIL3", "M21B-E008366"),
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(values: list[str]) -> str:
    out: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in value.split(";"):
            item = item.strip()
            if item and item not in seen:
                seen.add(item)
                out.append(item)
    return "; ".join(out)


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    sources = read_tsv(bundle / "mechanism_edge_sources.tsv")
    source_by_edge: dict[str, list[dict[str, str]]] = {}
    for source in sources:
        source_by_edge.setdefault(source["edge_id"], []).append(source)

    lr_edge = edges["M21B-E000740"]
    receptor = nodes[lr_edge["target_node_id"]]
    relay_node = next(row for row in nodes.values() if row["canonical_label"] == "TYK2")
    tf = next(row for row in nodes.values() if row["canonical_label"] == "STAT6")
    rows: list[dict[str, str]] = []
    for index, (output_edge_id, target_label, tf_target_edge_id) in enumerate(TARGETS, start=1):
        output_edge = edges[output_edge_id]
        tf_target_edge = edges[tf_target_edge_id]
        target = nodes[output_edge["target_node_id"]]
        locators = unique_join(
            [
                *(source.get("source_locator", "") for source in source_by_edge.get(lr_edge["edge_id"], [])),
                *(source.get("source_locator", "") for source in source_by_edge.get(output_edge_id, [])),
                *(source.get("source_locator", "") for source in source_by_edge.get(tf_target_edge_id, [])),
            ]
        )
        evidence_ids = unique_join(
            [
                lr_edge.get("evidence_ids", ""),
                output_edge.get("evidence_ids", ""),
                tf_target_edge.get("evidence_ids", ""),
                *(source.get("evidence_id", "") for source in source_by_edge.get(lr_edge["edge_id"], [])),
                *(source.get("evidence_id", "") for source in source_by_edge.get(output_edge_id, [])),
                *(source.get("evidence_id", "") for source in source_by_edge.get(tf_target_edge_id, [])),
                locators,
            ]
        )
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-IL13-TYK2-STAT6-{target_label}-{index:03d}",
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge",
                "intracellular_status": "source_supported",
                "ligand_node_id": lr_edge["source_node_id"],
                "ligand_label": lr_edge["source_label"],
                "ligand_receptor_edge_id": lr_edge["edge_id"],
                "receptor_node_id": lr_edge["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": relay_node["node_id"],
                "intracellular_continuation_label": relay_node["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf["node_id"],
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": tf_target_edge_id,
                "target_gene_node_id": target["node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": target["node_id"],
                "output_label": f"{target_label} expression",
                "output_form_id": "",
                "output_edge_id": output_edge_id,
                "bridge_id": "",
                "pathway_name": f"IL13-IL4RA:IL13RA1-TYK2-STAT6-{target_label}",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_chain_id": f"M21B-LITEXP-IL13-TYK2-STAT6-{target_label}-{index:03d}",
                "source_evidence_record_id": "",
                "route_linkage_status": "manual_primary_il13_stat6_output_route;graph_linked_route_source;primary_layer_linked;receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;output_edge_asserted_as_graph_edge;evidence_route_only",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": locators,
                "citation_note": "Primary IL-13 type-II-receptor, STAT6-dependent macrophage-marker, and target-gene evidence is assembled with TYK2 retained as a source-supported receptor-proximal alternative; the two relay handoffs remain unasserted.",
                "evidence_summary": f"Primary evidence supports IL-13 engagement of the IL4RA:IL13RA1 type-II receptor complex, TYK2-associated receptor-proximal signaling, STAT6 activity, and {target_label} expression. The direct IL-13 output edge and STAT6 target edge are retained as linked evidence components without asserting new intracellular graph edges.",
                "limitations": "The receptor, kinase-pathway, STAT6, and target-gene studies use complementary human and mouse macrophage or reporter systems. Preserve IL-13 receptor-chain composition, model-specific cell state, and the distinction between source-supported route composition and asserted graph connectivity; no SCI transfer, causal traversal, or database confidence score is inferred.",
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse comparator systems",
                "cell_type_context": "Human CD14-positive macrophages and mouse macrophage or promoter-reporter systems.",
                "compartment_context": "extracellular IL-13; plasma membrane receptor complex; cytoplasm; nucleus; target-gene regulatory locus",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "IL-13 stimulation; receptor or kinase-pathway perturbation; STAT6 activation or loss-of-function; target-gene RNA, promoter, and protein measurements",
                "effect_polarity": "activating",
                "source_scope": "composite_primary_evidence",
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = make_rows(args.bundle.resolve())
    args.output.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
