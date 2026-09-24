#!/usr/bin/env python3
"""Build primary-literature route overlays for neurotransmitter/injury gaps."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "TNC-TLR4-MAPK-NFkB-IL6",
        "lr_edge_id": "M21B-E000269",
        "relay_node_id": "NODE11167",
        "tf_node_id": "NODE07984",
        "target_node_id": "NODE05512",
        "primary_locator": "PMID:29150600; PMID:27231521; PMID:27577261",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "IL6 gene expression",
        "pathway_name": "TNC-TLR4-MyD88-MAPK-NFkB-IL6",
        "route_linkage_status": (
            "manual_primary_tnc_tlr4_myd88_mapk_nfkb_il6_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ),
        "evidence_summary": (
            "Primary studies report that tenascin-C fibrinogen-like domains bind and activate TLR4, induce p38/JNK/NF-kB "
            "signaling and cytokine synthesis, and increase IL-6 mRNA and protein in human cardiac myofibroblasts. "
            "TLR4 neutralization attenuates the IL-6 response, supporting the receptor-to-output route."
        ),
        "limitations": (
            "The route composes macrophage TLR4 signaling and cardiac-myofibroblast IL-6 experiments across primary studies. "
            "The graph handoffs remain unasserted and the route does not infer SCI-specific transfer."
        ),
        "species_context": "human and mouse models as reported across primary studies",
        "cell_type_context": "primary human macrophages and human cardiac myofibroblasts",
        "assay_or_perturbation": "TNC/FBG stimulation; TLR4 binding and neutralization; p38/JNK/NF-kB activation; IL-6 mRNA/protein assays",
    },
    {
        "name": "NOREPINEPHRINE-ADRA1A-PKA-CREB-CFOS",
        "lr_edge_id": "M21B-E001452",
        "relay_node_id": "NODE09055",
        "tf_node_id": "NODE02446",
        "target_node_id": "NODE02087",
        "primary_locator": "PMID:8748977; PMID:9792725",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "cFos gene expression",
        "pathway_name": "NOREPINEPHRINE-ADRA1A-PKA-CREB-CFOS",
        "route_linkage_status": (
            "manual_primary_norepinephrine_adra1a_pka_creb_cfos_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ),
        "evidence_summary": (
            "Primary rat aortic-ring experiments report norepinephrine-induced c-fos mRNA through alpha-adrenoceptors, "
            "with strong alpha1-antagonist sensitivity. A complementary primary study shows alpha1-adrenergic receptor "
            "activation of PKA-dependent CREB phosphorylation and CRE-dependent transcription."
        ),
        "limitations": (
            "The c-fos and CREB experiments use different alpha-adrenergic systems and are retained as a composed route. "
            "The receptor-to-PKA and CREB-to-cFos handoffs remain evidence-only; no causal graph edge is created."
        ),
        "species_context": "rat and human alpha1-adrenergic receptor expression systems",
        "cell_type_context": "rat aortic rings and Rat1 cells expressing human alpha1-adrenergic receptor subtypes",
        "assay_or_perturbation": "norepinephrine; alpha1/alpha2/beta adrenergic antagonists; PKA inhibition; CREB phosphorylation; c-fos mRNA and CRE-reporter assays",
    },
    {
        "name": "GABA-GABAA-MAPK-CREB-BDNF",
        "lr_edge_id": "M21B-E001344",
        "relay_node_id": "NODE03908",
        "tf_node_id": "NODE02446",
        "target_node_id": "NODE01191",
        "primary_locator": "PMID:12163549",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "BDNF promoter IV/gene expression",
        "pathway_name": "GABA-GABAA-MAPK-CREB-BDNF",
        "route_linkage_status": (
            "manual_primary_gaba_gabaa_mapk_creb_bdnf_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary developing-neuron study reports GABA-A receptor-dependent MAPK activation, CREB Ser133 phosphorylation, "
            "and BDNF expression. Muscimol reproduced the response, bicuculline blocked it, and MEK inhibition attenuated "
            "CREB phosphorylation and BDNF induction."
        ),
        "limitations": (
            "The route is developmentally restricted: GABA was excitatory in the five-day cultured hypothalamic neurons but "
            "not in mature cultures. The current BDNF promoter-IV node is retained as the target representation without adding "
            "a new graph edge."
        ),
        "species_context": "rat neuronal culture model",
        "cell_type_context": "developing cultured hypothalamic neurons",
        "assay_or_perturbation": "GABA and muscimol stimulation; bicuculline blockade; MEK inhibition; MAPK and CREB phosphorylation; BDNF expression assays",
    },
    {
        "name": "ACETYLCHOLINE-CHRM1-ERK-EGR1-ACHE",
        "lr_edge_id": "M21B-E001347",
        "relay_node_id": "NODE06656",
        "tf_node_id": "NODE03137",
        "target_node_id": "",
        "primary_locator": "PMID:9789819",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|tf_to_target_edge|target_gene_node",
        "output_label": "AChE/ACHE promoter activation and transcription",
        "pathway_name": "ACETYLCHOLINE-CHRM1-ERK-EGR1-ACHE",
        "route_linkage_status": (
            "manual_primary_acetylcholine_chrm1_erk_egr1_ache_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "tf_to_target_edge_not_asserted;target_gene_node_unresolved;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary neuronal study reports muscarinic acetylcholine receptor activation through protein kinase C, rapid "
            "EGR1 induction, EGR1 binding to AChE promoter recognition sites, and activation of the human acetylcholinesterase "
            "promoter. The graph-linked M1-ERK-EGR1 relay is retained while the terminal ACHE node remains unresolved."
        ),
        "limitations": (
            "The source establishes a muscarinic/PKC/EGR1 promoter route but the exact M1-to-ERK handoff is composed from the "
            "existing graph program. EGR1 is represented by a current signaling node rather than a specialized TF node, and no "
            "new target-gene edge is asserted."
        ),
        "species_context": "human promoter and neuronal model systems",
        "cell_type_context": "neuronal cells and transfection-based promoter assays",
        "assay_or_perturbation": "muscarinic receptor stimulation; protein kinase C signaling; EGR1 expression; EGR1 DNA binding; AChE promoter reporter assays",
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
                "expansion_id": f"M21B-LITEXP-NEUROGAP-{index:03d}",
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
                "source_chain_id": f"M21B-LITEXP-NEUROGAP-{index:03d}",
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
