#!/usr/bin/env python3
"""Build primary-literature route overlays for glutamatergic and DAMP gaps."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "GLUTAMATE-NMDA-ERK-CREB-CFOS",
        "lr_edge_id": "M21B-E001350",
        "relay_node_id": "NODE03370",
        "tf_node_id": "NODE02446",
        "target_node_id": "NODE02087",
        "primary_locator": "PMID:10414964; PMID:15016079",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "cFos gene expression",
        "pathway_name": "GLUTAMATE-NMDA-Ca2-ERK-CREB-CFOS",
        "route_linkage_status": (
            "manual_primary_glutamate_nmda_ca2_erk_creb_cfos_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ),
        "evidence_summary": (
            "Primary rat striatal-neuron studies report glutamate activation of ionotropic NMDA/AMPA pathways, calcium "
            "entry, ERK1/2 phosphorylation, CREB phosphorylation, and c-fos gene expression. L-type calcium-channel and "
            "MEK/ERK perturbations reduce the downstream CREB/c-fos response, supporting the retained intermediate sequence."
        ),
        "limitations": (
            "The route composes complementary receptor-to-calcium and ERK-to-CREB experiments in primary striatal cultures. "
            "Exact receptor subtype contributions and graph handoffs remain unasserted; no SCI transfer or causal graph edge is inferred."
        ),
        "species_context": "rat",
        "cell_type_context": "primary rat striatal neurons",
        "assay_or_perturbation": "glutamate/NMDA/AMPA stimulation; NMDA antagonism; L-type calcium-channel blockade; MEK/ERK inhibition; CREB phosphorylation; c-fos mRNA and reporter assays",
    },
    {
        "name": "DECORIN-TLR2-MYD88-MAPK-NFkB-INFLAMMATORY",
        "lr_edge_id": "M21B-E000869",
        "relay_node_id": "NODE11167",
        "tf_node_id": "NODE07984",
        "target_node_id": "",
        "primary_locator": "PMID:22087031",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|target_gene_expression",
        "output_label": "PDCD4, TNF-alpha, IL-12, and pro-inflammatory cytokine output",
        "pathway_name": "DECORIN-TLR2-MYD88-MAPK-NFkB-INFLAMMATORY",
        "route_linkage_status": (
            "manual_primary_decorin_tlr2_myd88_mapk_nfkb_output_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "target_gene_expression_unresolved;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary decorin study reports decorin as an endogenous TLR2/TLR4 ligand that activates NF-kB reporter activity, "
            "increases PDCD4 and pro-inflammatory TNF-alpha/IL-12 outputs in macrophages, and shifts the cytokine profile away "
            "from anti-inflammatory IL-10. The route retains the graph-linked TLR2/MyD88/MAPK/NF-kB relay and exposes the output set."
        ),
        "limitations": (
            "The source supports both TLR2 and TLR4 and does not isolate every downstream output to one receptor. The route uses "
            "the TLR2 edge and a shared MyD88/MAPK/NF-kB relay as a composed evidence route; no single terminal target-gene node is asserted."
        ),
        "species_context": "mouse and human macrophage systems",
        "cell_type_context": "mouse macrophages, human macrophage systems, and TLR reporter cells",
        "assay_or_perturbation": "decorin stimulation; TLR2/TLR4 receptor perturbation; NF-kB reporter; PDCD4, TNF-alpha, IL-12, and IL-10 assays",
    },
    {
        "name": "ATP-P2X7-NFkBAP1-IL8",
        "lr_edge_id": "M21B-E001466",
        "relay_node_id": "NODE08717",
        "tf_node_id": "NODE07984",
        "target_node_id": "",
        "primary_locator": "PMID:9412459; PMID:11404398",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|target_gene_expression",
        "output_label": "IL-8/CXCL8 mRNA and protein output",
        "pathway_name": "ATP-P2X7-NFkBAP1-IL8",
        "route_linkage_status": (
            "manual_primary_atp_p2x7_nfkb_ap1_il8_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "target_gene_node_unresolved;evidence_route_only"
        ),
        "evidence_summary": (
            "Primary studies report extracellular ATP activation of NF-kB through P2X7/P2Z receptors and ATP potentiation of "
            "NF-kB/AP-1 activity with increased IL-8 mRNA and protein in primary human astrocytes. The route retains the P2X7-NF-kB "
            "relay and preserves IL-8 as a functional output because the current graph lacks a clean CXCL8 target-gene node for this route."
        ),
        "limitations": (
            "The P2X7 microglial NF-kB study and the astrocyte IL-8 study use different inflammatory contexts and P2 receptor mixtures. "
            "The output route is therefore source-composed and non-causal, with the target-gene handoff unresolved."
        ),
        "species_context": "human astrocytes and microglial systems",
        "cell_type_context": "primary human astrocytes and microglial cells",
        "assay_or_perturbation": "extracellular ATP; P2X7/P2 receptor antagonism; NF-kB/AP-1 reporter and DNA-binding assays; IL-8 mRNA/protein assays",
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
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        lr = edges[spec["lr_edge_id"]]
        ligand = nodes[lr["source_node_id"]]
        receptor = nodes[lr["target_node_id"]]
        relay = nodes[spec["relay_node_id"]]
        tf = nodes[spec["tf_node_id"]]
        target = nodes.get(spec["target_node_id"], {})
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-GLUMATGAP-{index:03d}",
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": spec["path_expression"],
                "route_tier": spec["route_tier"],
                "known_layers": spec["known_layers"],
                "missing_layers": spec["missing_layers"],
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": lr["source_node_id"],
                "ligand_label": ligand["canonical_label"],
                "ligand_receptor_edge_id": spec["lr_edge_id"],
                "receptor_node_id": lr["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": spec["relay_node_id"],
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": spec["tf_node_id"],
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": spec["target_node_id"],
                "target_gene_label": target.get("canonical_label", ""),
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression" if spec["target_node_id"] else "primary_functional_output",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["primary_locator"]),
                "source_chain_id": f"M21B-LITEXP-GLUMATGAP-{index:03d}",
                "source_evidence_record_id": "",
                "route_linkage_status": spec["route_linkage_status"],
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression" if spec["target_node_id"] else "generic_functional_readout",
                "primary_locator": spec["primary_locator"],
                "citation_note": (
                    f"Primary-evidence route overlay for {spec['name']}. Unresolved handoffs and graph target "
                    "limitations are retained explicitly; no graph edge, causal assertion, or confidence score is created."
                ),
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular signaling; nuclear or functional output context",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": spec["assay_or_perturbation"],
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
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
