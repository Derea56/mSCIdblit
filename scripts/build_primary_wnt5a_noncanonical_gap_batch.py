#!/usr/bin/env python3
"""Build a primary-literature route overlay for the WNT5A noncanonical gap."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(*values: str) -> str:
    out: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in value.split(";"):
            item = item.strip()
            if item and item not in seen:
                seen.add(item)
                out.append(item)
    return "; ".join(out)


def make_row(bundle: Path) -> dict[str, str]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    lr = edges["M21B-E000472"]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes["NODE11876"]
    tf = nodes["NODE00609"]
    expansion_id = "M21B-LITEXP-WNT5AGAP-001"
    return {
        "expansion_id": expansion_id,
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|target_gene_expression",
        "intracellular_status": "source_supported_composed",
        "ligand_node_id": lr["source_node_id"],
        "ligand_label": ligand["canonical_label"],
        "ligand_receptor_edge_id": "M21B-E000472",
        "receptor_node_id": lr["target_node_id"],
        "receptor_label": receptor["canonical_label"],
        "receptor_intracellular_edge_id": "",
        "intracellular_continuation_node_id": "NODE11876",
        "intracellular_continuation_label": relay["canonical_label"],
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": "NODE00609",
        "transcription_factor_label": tf["canonical_label"],
        "tf_target_edge_id": "",
        "target_gene_node_id": "",
        "target_gene_label": "",
        "target_output_form_id": "",
        "output_node_id": "",
        "output_label": "MMP13/matrix metalloproteinase-13 expression",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": "WNT5A-ROR2-Rac-JNK-AP1-MMP13",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_functional_output",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), "PMID:20457807; PMID:22128168"),
        "source_chain_id": expansion_id,
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_wnt5a_ror2_jnk_ap1_mmp13_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "target_gene_node_unresolved;evidence_route_only"
        ),
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "output_class": "generic_functional_readout",
        "primary_locator": "PMID:20457807; PMID:22128168",
        "citation_note": (
            "Primary-evidence route overlay for WNT5A-ROR2-Rac-JNK-AP1-MMP13. The graph retains the pathway and output layers "
            "without asserting an MMP13 target-gene node or causal edge."
        ),
        "evidence_summary": (
            "Primary studies report WNT5A/ROR2/FZD7-dependent Dishevelled/Rac signaling with JNK or AP-1 reporter activation, "
            "and a separate WNT5A-ROR2 study reports AP-1 c-Jun/ATF2 recruitment to the MMP13 promoter and JNK-dependent MMP13 "
            "expression. The route preserves this convergent noncanonical evidence as a traversable functional-output route."
        ),
        "limitations": (
            "The receptor-to-JNK/AP-1 and AP-1-to-MMP13 observations come from complementary primary studies and different cell "
            "systems. The current graph has no dedicated MMP13 target-gene node, so MMP13 remains a generic output; no direct graph "
            "edge, causal assertion, or SCI transfer is inferred."
        ),
        "curation_status": "curated_primary_route",
        "species_context": "mouse and human cell systems",
        "cell_type_context": "mouse L cells and human SaOS-2 osteosarcoma cells",
        "compartment_context": "extracellular WNT5A; ROR2/FZD receptor context; cytosolic DVL/Rac/JNK relay; nuclear AP-1 promoter output",
        "injury_context": "no SCI transfer inferred; primary model context only",
        "context_scope": "composite primary evidence; route layers retain source-specific models",
        "assay_or_perturbation": "WNT5A stimulation; ROR2/FZD7 perturbation; DVL polymerization; Rac1 localization; JNK and AP-1 reporter assays; WNT5A/ROR2 depletion; AP-1 ChIP at MMP13 promoter; JNK inhibition; MMP13 qRT-PCR",
        "effect_polarity": "activating",
        "source_scope": "composite_primary_evidence",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.resolve().write_text(json.dumps([make_row(args.bundle.resolve())], indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": 1, "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
