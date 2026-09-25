#!/usr/bin/env python3
"""Build a primary-evidence TWSG1/BMP7/SMAD/ID1 route."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPEC = {
    "lr_edge_id": "M21B-E007043",
    "relay_node_id": "NODE01301",
    "tf_node_id": "NODE10440",
    "target_node_id": "NODE04961",
    "primary_locator": "PMID:34360647; PMCID:PMC8346149; DOI:10.3390/ijms22157882",
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


def make_row(bundle: Path) -> dict[str, str]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    lr = edges[SPEC["lr_edge_id"]]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[SPEC["relay_node_id"]]
    tf = nodes[SPEC["tf_node_id"]]
    target = nodes[SPEC["target_node_id"]]
    return {
        "expansion_id": "M21B-LITEXP-TWSG1-ID1-001",
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "intracellular_status": "source_supported_composed",
        "ligand_node_id": lr["source_node_id"],
        "ligand_label": ligand["canonical_label"],
        "ligand_receptor_edge_id": SPEC["lr_edge_id"],
        "receptor_node_id": lr["target_node_id"],
        "receptor_label": receptor["canonical_label"],
        "receptor_intracellular_edge_id": "",
        "intracellular_continuation_node_id": SPEC["relay_node_id"],
        "intracellular_continuation_label": relay["canonical_label"],
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": SPEC["tf_node_id"],
        "transcription_factor_label": tf["canonical_label"],
        "tf_target_edge_id": "",
        "target_gene_node_id": SPEC["target_node_id"],
        "target_gene_label": target["canonical_label"],
        "target_output_form_id": "",
        "output_node_id": "",
        "output_label": "ID1 mRNA expression",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": "TWSG1-BMP7-BMPR-SMAD1-5-8-ID1",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), SPEC["primary_locator"]),
        "source_chain_id": "M21B-LITEXP-TWSG1-ID1-001",
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_twsg1_bmp7_smad_id1_route;graph_linked_route_source;"
            "graph_linked_ligand_bmp_antagonist_edge;primary_layer_linked;soluble_bmp_antagonism;"
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
            "Primary-evidence route overlay for TWSG1-BMP7-BMPR-SMAD1-5-8-ID1. "
            "The source supports inhibitory BMP7-response modulation; unresolved handoffs remain explicit."
        ),
        "evidence_summary": (
            "A primary Ishikawa endometrial-cancer-cell study reports that recombinant TWSG1 "
            "suppresses BMP7-induced SMAD1/5/8 phosphorylation and ID1 mRNA expression. The route "
            "maps those observations onto the existing TWSG1-BMP7 antagonist edge, BMP receptor "
            "signaling relay, SMAD1/5/8 transcription-factor node, and ID1 target-gene node."
        ),
        "limitations": (
            "The study uses an endometrial-cancer cell model and does not establish a single direct "
            "TWSG1-to-receptor-to-SMAD-to-ID1 molecular chain. TWSG1 is represented as an extracellular "
            "BMP antagonist, so the route is inhibitory rather than productive receptor activation. "
            "No graph edge, causal traversal, or database confidence score is created."
        ),
        "curation_status": "curated_primary_route",
        "species_context": "human cell line",
        "cell_type_context": "Ishikawa endometrial-cancer cells",
        "compartment_context": "extracellular BMP antagonist; plasma-membrane receptor complex; intracellular signaling; nuclear output",
        "injury_context": "no SCI transfer inferred; primary model context only",
        "context_scope": "composite primary evidence; route layers retain source-specific models",
        "assay_or_perturbation": (
            "recombinant BMP7 and TWSG1 treatment; SMAD1/5/8 phosphorylation immunoblot; "
            "ID1 mRNA qRT-PCR"
        ),
        "effect_polarity": "inhibitory",
        "source_scope": "composite_primary_evidence",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    row = make_row(args.bundle.resolve())
    args.output.resolve().write_text(json.dumps([row], indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "rows": 1, "ligand": row["ligand_label"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
