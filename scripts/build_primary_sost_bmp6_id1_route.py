#!/usr/bin/env python3
"""Build a composite primary-evidence SOST/BMP6/SMAD/ID1 route."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPEC = {
    "lr_edge_id": "M21B-E000852",
    "relay_node_id": "NODE01301",
    "tf_node_id": "NODE10440",
    "target_node_id": "NODE04961",
    "primary_locator": (
        "PMID:14633986; PMID:15877825; PMCID:PMC1134658"
    ),
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
        "expansion_id": "M21B-LITEXP-SOST-BMP6-ID1-001",
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
        "pathway_name": "SOST-BMP6-BMPR-SMAD1-5-8-ID1",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), SPEC["primary_locator"]),
        "source_chain_id": "M21B-LITEXP-SOST-BMP6-ID1-001",
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_sost_bmp6_id1_route;graph_linked_route_source;"
            "graph_linked_ligand_bmp_antagonist_edge;primary_layer_linked;"
            "cross_record_primary_route_composition;source_overlap_bmp6_smad;"
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
            "Composite primary-evidence route overlay for SOST-BMP6-BMPR-SMAD1-5-8-ID1. "
            "The BMP6-to-ID1 continuation and SOST inhibition are supported by separate primary studies."
        ),
        "evidence_summary": (
            "A primary sclerostin study reports inhibition of BMP6-induced SMAD phosphorylation, and a "
            "separate primary human B-cell study reports that BMP6 induces SMAD1/5/8 phosphorylation "
            "followed by Id1 mRNA and protein upregulation. The route composes these observations with "
            "the existing SOST-BMP6 antagonist edge and the exported BMP-SMAD relay."
        ),
        "limitations": (
            "The SOST inhibition study and the BMP6-to-Id1 study use different cell systems and do not "
            "demonstrate one end-to-end SOST-to-Id1 experiment. The route is therefore evidence-layer "
            "composition only; receptor-to-relay, relay-to-TF and TF-to-target handoffs remain unresolved. "
            "No graph edge, causal traversal, or database confidence score is created."
        ),
        "curation_status": "curated_primary_route",
        "species_context": "mouse and human",
        "cell_type_context": "primary osteoblast-lineage systems and human peripheral B cells",
        "compartment_context": "extracellular BMP antagonist; plasma-membrane receptor complex; intracellular signaling; nuclear output",
        "injury_context": "no SCI transfer inferred; primary model contexts only",
        "context_scope": "composite primary evidence across distinct cell systems",
        "assay_or_perturbation": (
            "recombinant sclerostin/BMP6 signaling assays; pSMAD1/5/8 measurement; recombinant BMP6 "
            "treatment of human B cells; Id1 qRT-PCR and immunoblot"
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
