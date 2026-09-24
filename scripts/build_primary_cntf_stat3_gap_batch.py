#!/usr/bin/env python3
"""Build primary-literature CNTF receptor-to-STAT3 target routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "CNTF-CNTFRaGP130LIFR-JAK2-STAT3-SOCS3",
        "target_node_id": "NODE10509",
        "primary_locator": "PMID:19272793",
        "output_label": "SOCS3 gene expression",
        "pathway_name": "CNTF-CNTFRaGP130LIFR-JAK2-STAT3-SOCS3",
        "species_context": "rat",
        "cell_type_context": "neonatal rat pancreatic islets",
        "assay_or_perturbation": "CNTF stimulation; JAK2/STAT3 phosphorylation; nuclear STAT3; SOCS3 mRNA and protein; JAK and STAT3 inhibition; PI3K/MAPK inhibitor controls",
    },
    {
        "name": "CNTF-CNTFRaGP130LIFR-JAK2-STAT3-CXCL10",
        "target_node_id": "NODE02629",
        "primary_locator": "PMID:32780864",
        "output_label": "CXCL10 gene expression",
        "pathway_name": "CNTF-CNTFRaGP130LIFR-JAK2-STAT3-CXCL10",
        "species_context": "mouse",
        "cell_type_context": "primary mouse retinal Müller cells and Vldlr-null retina",
        "assay_or_perturbation": "CNTF treatment; retinal pSTAT3; STAT3-target array; primary Müller-cell qPCR; Cxcl10-conditioned-medium ELISA; retinal neovascularization models",
    },
)


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


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    lr_edge_id = "M21B-E000107"
    lr = edges[lr_edge_id]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes["NODE02288"]
    tf = nodes["NODE10722"]
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        target = nodes[spec["target_node_id"]]
        expansion_id = f"M21B-LITEXP-CNTFGAP-{index:03d}"
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": lr["source_node_id"],
                "ligand_label": ligand["canonical_label"],
                "ligand_receptor_edge_id": lr_edge_id,
                "receptor_node_id": lr["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": "NODE02288",
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": "NODE10722",
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": spec["target_node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["primary_locator"]),
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    f"manual_primary_{spec['name'].lower().replace('-', '_')}_route;graph_linked_route_source;"
                    "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
                    "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": spec["primary_locator"],
                "citation_note": (
                    f"Primary-evidence route overlay for {spec['name']}. The receptor-linked JAK/STAT3 and target-expression "
                    "layers are retained while unresolved graph handoffs remain explicit; no causal edge or confidence score is created."
                ),
                "evidence_summary": (
                    "Primary CNTF studies report activation of the CNTFRa-associated JAK/STAT3 pathway and induction of the "
                    f"{spec['output_label']} readout. The route maps those observations onto the existing CNTF receptor, JAK/STAT, "
                    "STAT3-family, and target-gene nodes."
                ),
                "limitations": (
                    "The two primary studies use different target tissues and do not establish one uninterrupted experiment for "
                    "every graph handoff. STAT3-family identity and the receptor-to-relay/TF-to-target edges remain evidence-layer "
                    "links; no SCI transfer or causal graph edge is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular CNTF; plasma-membrane CNTFR-alpha/gp130/LIFR receptor complex; intracellular JAK/STAT3 signaling; nuclear target-gene output",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "primary model-specific evidence; route layers retain source-specific systems",
                "assay_or_perturbation": spec["assay_or_perturbation"],
                "effect_polarity": "activating",
                "source_scope": "single_primary_study",
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
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
