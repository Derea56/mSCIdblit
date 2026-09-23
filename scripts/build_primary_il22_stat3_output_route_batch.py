#!/usr/bin/env python3
"""Build evidence-only IL-22 JAK1/TYK2-STAT3 output route annotations."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


TARGETS = (
    ("M21B-E008379", "MUC1", "M21B-E008656"),
    ("M21B-E008348", "LCN2", "M21B-E008658"),
)

RELAYS = ("JAK1", "TYK2")


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

    lr_edge = edges["M21B-E000448"]
    receptor = nodes[lr_edge["target_node_id"]]
    tf = nodes["NODE10726"]
    relay_nodes = {label: next(row for row in nodes.values() if row["canonical_label"] == label) for label in RELAYS}
    rows: list[dict[str, str]] = []
    index = 1
    for relay_label in RELAYS:
        relay_node = relay_nodes[relay_label]
        for target_edge_id, target_label, output_edge_id in TARGETS:
            target_edge = edges[target_edge_id]
            output_edge = edges[output_edge_id]
            target = nodes[target_edge["target_node_id"]]
            locators = unique_join(
                [
                    "PMID:12513909; PMID:12087100; PMID:20462497",
                    "PMID:12087100; PMID:15120652; PMID:32611765; PMCID:PMC7458808",
                    *(source.get("source_locator", "") for source in source_by_edge.get(lr_edge["edge_id"], [])),
                    *(source.get("source_locator", "") for source in source_by_edge.get(target_edge_id, [])),
                    *(source.get("source_locator", "") for source in source_by_edge.get(output_edge_id, [])),
                ]
            )
            evidence_ids = unique_join(
                [
                    "M21B-E000448; M21B-E000449",
                    lr_edge.get("evidence_ids", ""),
                    target_edge.get("evidence_ids", ""),
                    output_edge.get("evidence_ids", ""),
                    locators,
                ]
            )
            rows.append(
                {
                    "expansion_id": f"M21B-LITEXP-IL22-{relay_label}-STAT3-{target_label}-{index:03d}",
                    "source_queue_id": "",
                    "route_status": "retained_evidence_route",
                    "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                    "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                    "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                    "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge",
                    "intracellular_status": "source_supported",
                    "ligand_node_id": lr_edge["source_node_id"],
                    "ligand_label": lr_edge["source_label"],
                    "ligand_receptor_edge_id": "M21B-E000448",
                    "receptor_node_id": lr_edge["target_node_id"],
                    "receptor_label": receptor["canonical_label"],
                    "receptor_intracellular_edge_id": "",
                    "intracellular_continuation_node_id": relay_node["node_id"],
                    "intracellular_continuation_label": relay_label,
                    "transcription_factor_node_id": "NODE10726",
                    "transcription_factor_label": tf["canonical_label"],
                    "tf_target_edge_id": target_edge_id,
                    "target_gene_node_id": target["node_id"],
                    "target_gene_label": target["canonical_label"],
                    "target_output_form_id": "",
                    "output_node_id": target["node_id"],
                    "output_label": f"{target_label} expression",
                    "output_form_id": "",
                    "bridge_id": "",
                    "pathway_name": f"IL22-IL22RA1:IL10RB-{relay_label}-STAT3-{target_label}",
                    "input_evidence_type": "primary_literature_route_expansion",
                    "output_evidence_type": "primary_target_gene_expression",
                    "evidence_ids": evidence_ids,
                    "source_chain_id": f"M21B-LITEXP-IL22-{relay_label}-STAT3-{target_label}-{index:03d}",
                    "source_evidence_record_id": "",
                    "route_linkage_status": "manual_primary_il22_stat3_output_route;graph_linked_route_source;primary_layer_linked;parallel_receptor_proximal_alternative;receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;evidence_route_only",
                    "causal_status": "not_asserted",
                    "traversal_status": "evidence_route_not_causal",
                    "evidence_contract_version": "mechanism_evidence_v1",
                    "evidence_polarity": "supports",
                    "negative_evidence_status": "not_evaluated",
                    "evidence_directness": "composite_primary_route",
                    "output_class": "target_gene_expression",
                    "primary_locator": locators,
                    "citation_note": "Primary IL-22 receptor/STAT3 and IL-22-induced epithelial target-gene evidence is assembled with JAK1 or TYK2 as source-supported receptor-proximal alternatives; both relay handoffs remain unasserted.",
                    "evidence_summary": f"Primary evidence supports IL-22 engagement of the IL22RA1:IL10RB receptor complex, {relay_label}-associated receptor-proximal signaling, STAT3 activity, and {target_label} expression. The route complements the existing SOCS3 evidence routes without asserting new graph connectivity.",
                    "limitations": "The receptor/JAK/STAT and target-gene studies use complementary hepatoma, intestinal epithelial, macrophage, and structural systems. Preserve IL22RA1:IL10RB composition, epithelial cytokine synergy, and model limits; no SCI transfer, causal traversal, or database confidence score is inferred.",
                    "curation_status": "curated_primary_route",
                    "species_context": "human; mouse; rat comparator systems",
                    "cell_type_context": "Rat hepatoma receptor-signaling systems, human/mouse intestinal epithelial cells, and primary human macrophage comparator studies.",
                    "compartment_context": "extracellular IL-22; plasma membrane receptor complex; cytoplasm; nucleus; target-gene regulatory locus",
                    "injury_context": "no SCI transfer inferred; primary model context only",
                    "context_scope": "composite primary evidence; route layers retain source-specific models",
                    "assay_or_perturbation": "IL-22 stimulation; receptor assembly and phosphorylation; JAK/TYK2 and STAT3 activation; epithelial target-gene transcript, promoter, protein, and neutralization assays",
                    "effect_polarity": "activating",
                    "source_scope": "composite_primary_evidence",
                }
            )
            index += 1
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
