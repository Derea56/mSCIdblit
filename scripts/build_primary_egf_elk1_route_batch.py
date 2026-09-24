#!/usr/bin/env python3
"""Build a bounded EGF-EGFR-ERK-ELK1-EGR1 evidence route.

The route keeps the receptor-complex alias and the unresolved intracellular
handoff explicit.  It is evidence-layer data only: no causal graph edge or
database confidence score is created.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(values: list[str]) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in value.split(";"):
            item = item.strip()
            if item and item not in seen:
                seen.add(item)
                result.append(item)
    return "; ".join(result)


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    sources = read_tsv(bundle / "mechanism_edge_sources.tsv")
    source_by_edge: dict[str, list[dict[str, str]]] = {}
    for source in sources:
        source_by_edge.setdefault(source["edge_id"], []).append(source)

    lr_edge = edges["M21B-E000268"]
    receptor = nodes[lr_edge["target_node_id"]]
    receptor_continuation_edge = edges["M21B-E000039"]
    intracellular = nodes[receptor_continuation_edge["target_node_id"]]
    tf_target_edge = edges["M22B-E000158"]
    tf = nodes[tf_target_edge["source_node_id"]]
    target = nodes[tf_target_edge["target_node_id"]]

    locators = unique_join(
        [
            *(source.get("source_locator", "") for source in source_by_edge.get(lr_edge["edge_id"], [])),
            *(source.get("source_locator", "") for source in source_by_edge.get(receptor_continuation_edge["edge_id"], [])),
            *(source.get("source_locator", "") for source in source_by_edge.get(tf_target_edge["edge_id"], [])),
        ]
    )
    evidence_ids = unique_join(
        [
            lr_edge.get("evidence_ids", ""),
            receptor_continuation_edge.get("evidence_ids", ""),
            tf_target_edge.get("evidence_ids", ""),
            *(source.get("evidence_id", "") for source in source_by_edge.get(lr_edge["edge_id"], [])),
            *(source.get("evidence_id", "") for source in source_by_edge.get(receptor_continuation_edge["edge_id"], [])),
            *(source.get("evidence_id", "") for source in source_by_edge.get(tf_target_edge["edge_id"], [])),
            locators,
        ]
    )

    return [
        {
            "expansion_id": "M21B-LITEXP-EGF-EGFR-ELK1-EGR1-001",
            "source_queue_id": "",
            "route_status": "retained_evidence_route",
            "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
            "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": "intracellular_to_tf_edge|ligand_to_output_graph_edge",
            "intracellular_status": "source_supported_composed",
            "ligand_node_id": lr_edge["source_node_id"],
            "ligand_label": lr_edge["source_label"],
            "ligand_receptor_edge_id": lr_edge["edge_id"],
            "receptor_node_id": lr_edge["target_node_id"],
            "receptor_label": receptor["canonical_label"],
            "receptor_intracellular_edge_id": receptor_continuation_edge["edge_id"],
            "intracellular_continuation_node_id": intracellular["node_id"],
            "intracellular_continuation_label": intracellular["canonical_label"],
            "intracellular_tf_edge_id": "",
            "transcription_factor_node_id": tf["node_id"],
            "transcription_factor_label": tf["canonical_label"],
            "tf_target_edge_id": tf_target_edge["edge_id"],
            "target_gene_node_id": target["node_id"],
            "target_gene_label": target["canonical_label"],
            "target_output_form_id": "",
            "output_node_id": target["node_id"],
            "output_label": "EGR1 expression",
            "output_form_id": "",
            "output_edge_id": "",
            "bridge_id": "",
            "pathway_name": "EGF-EGFR-SHC1-GRB2-SOS1-HRAS-RAF-MEK-ERK-ELK1-EGR1",
            "input_evidence_type": "primary_literature_route_expansion",
            "output_evidence_type": "primary_target_gene_expression",
            "evidence_ids": evidence_ids,
            "source_chain_id": "M21B-LITEXP-EGF-EGFR-ELK1-EGR1-001",
            "source_evidence_record_id": "",
            "route_linkage_status": (
                "manual_primary_egf_elk1_output_route;graph_linked_route_source;primary_layer_linked;"
                "receptor_identity_alias:EGFR receptor complex;receptor_to_intracellular_edge_asserted_as_graph_edge;"
                "intracellular_chain_composed;intracellular_to_tf_edge_not_asserted;"
                "tf_to_target_edge_asserted_as_graph_edge;output_edge_not_asserted_primary_output_evidence_only;"
                "evidence_route_only"
            ),
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": "supports",
            "negative_evidence_status": "not_evaluated",
            "evidence_directness": "composite_primary_route",
            "output_class": "target_gene_expression",
            "primary_locator": locators,
            "citation_note": (
                "Primary EGF-EGFR receptor, EGFR Shc/Grb2/Sos-Ras-ERK pathway, and EGF-responsive ELK1/EGR1 promoter "
                "evidence are retained as a bounded route; the SHC1-to-ELK1 handoff remains unasserted."
            ),
            "evidence_summary": (
                "Primary evidence supports EGF binding and dimerization of EGFR, an EGFR receptor-complex-to-SHC1 "
                "and RAS/ERK signaling backbone, and EGF-dependent ELK1 occupancy and activation of the EGR1 promoter. "
                "The route records these compatible layers without asserting a new causal edge from the receptor-proximal "
                "cascade to ELK1 or a direct EGF-to-EGR1 graph edge."
            ),
            "limitations": (
                "The receptor-assembly, EGFR pathway, and ELK1/EGR1 promoter studies are complementary primary systems, "
                "with the direct target study using prostate cancer cells. Preserve receptor-complex identity, the "
                "EGF-ERK-ELK1 context, and model-specific cell state; no SCI transfer, causal traversal, or database "
                "confidence score is inferred."
            ),
            "curation_status": "curated_primary_route",
            "species_context": "human; mammalian comparator systems",
            "cell_type_context": "Human receptor and prostate-cancer-cell systems represented by the component evidence records.",
            "compartment_context": "extracellular EGF; plasma-membrane EGFR; cytoplasmic RAS/ERK cascade; nuclear EGR1 promoter",
            "injury_context": "no SCI transfer inferred; primary model context only",
            "context_scope": "composite primary evidence; route layers retain source-specific models",
            "assay_or_perturbation": "EGF stimulation; EGFR assembly and adaptor signaling; ERK-pathway inhibition; ELK1 perturbation; EGR1 promoter ChIP and reporter assays",
            "effect_polarity": "activating",
            "source_scope": "composite_primary_evidence",
        }
    ]


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
