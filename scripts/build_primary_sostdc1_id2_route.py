#!/usr/bin/env python3
"""Build a context-dependent primary-evidence SOSTDC1-to-Id2 route."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPEC = {
    "lr_edge_ids": ["M21B-E007031", "M21B-E000850"],
    "relay_node_id": "NODE01301",
    "tf_node_id": "NODE10440",
    "target_node_id": "NODE04962",
    "primary_locator": "PMID:31391487; PMCID:PMC6686024; DOI:10.1038/s41598-019-47930-x",
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(*values: str) -> str:
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
    relay = nodes[SPEC["relay_node_id"]]
    tf = nodes[SPEC["tf_node_id"]]
    target = nodes[SPEC["target_node_id"]]
    rows: list[dict[str, str]] = []
    for index, edge_id in enumerate(SPEC["lr_edge_ids"], start=1):
        lr = edges[edge_id]
        ligand = nodes[lr["source_node_id"]]
        receptor = nodes[lr["target_node_id"]]
        route_id = f"M21B-LITEXP-SOSTDC1-ID2-{index:03d}"
        rows.append(
            {
                "expansion_id": route_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": lr["source_node_id"],
                "ligand_label": ligand["canonical_label"],
                "ligand_receptor_edge_id": edge_id,
                "receptor_node_id": lr["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": relay["node_id"],
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf["node_id"],
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": target["node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": "Id2 mRNA expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"SOSTDC1-{receptor['canonical_label']}-BMPR-SMAD1-5-8-ID2",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), SPEC["primary_locator"]),
                "source_chain_id": route_id,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    "manual_primary_sostdc1_bmp_id2_route;graph_linked_route_source;"
                    "graph_linked_ligand_bmp_edge;primary_layer_linked;context_dependent_bmp_activation;"
                    "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
                    "tf_to_target_edge_not_asserted;end_to_end_chain_not_asserted_by_single_source;"
                    "evidence_route_only"
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": SPEC["primary_locator"],
                "citation_note": (
                    "Primary-evidence route overlay for the context-dependent SOSTDC1-BMP-SMAD1-5-8-Id2 "
                    "response. The source supports the observed tissue context; unresolved handoffs remain explicit."
                ),
                "evidence_summary": (
                    "A primary transgenic-rat study reports that persistent Sertoli-cell Sostdc1 expression "
                    "is associated with increased BMP4/BMP7-associated SMAD1/5/8 phosphorylation and Id2 "
                    "expression in testis. The route maps that observation onto the existing SOSTDC1-"
                    f"{receptor['canonical_label']} relation, BMP receptor relay, SMAD1/5/8 node and ID2 target-gene node."
                ),
                "limitations": (
                    "The study uses persistent transgenic expression in rat Sertoli cells and does not test a "
                    "direct SOSTDC1-BMP4/BMP7 binding or receptor-blockade mechanism in the same system. "
                    "SOSTDC1 has inhibitory as well as activating context-dependent BMP behavior, so this "
                    "route must not be generalized across tissues. No graph edge, causal traversal, or database "
                    "confidence score is created."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "rat",
                "cell_type_context": "Sertoli-cell transgenic rat testis with germ-cell output",
                "compartment_context": "Sertoli-cell extracellular or context-dependent BMP modulation; BMP receptor signaling; intracellular signaling; nuclear output",
                "injury_context": "no SCI transfer inferred; primary reproductive model context only",
                "context_scope": "primary transgenic model; context-dependent SOSTDC1/BMP response",
                "assay_or_perturbation": (
                    "Sertoli-cell Sostdc1 transgene; testicular pSMAD1/5/8 immunoblot and localization; "
                    "Bmp4, Bmp7 and Id2 qRT-PCR"
                ),
                "effect_polarity": "context_dependent",
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
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "rows": len(rows), "ligand": rows[0]["ligand_label"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
