#!/usr/bin/env python3
"""Build the next primary-literature route tranche for high-value ligand gaps.

These rows are evidence-layer overlays. They preserve source-supported route
layers and expose unresolved handoffs; they do not create graph edges, causal
traversal, or confidence scores.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "SPP1-ITGAVITGB3-NFkB-HIF1A-BMI1",
        "lr_edge_id": "M21B-E000174",
        "relay_node_id": "NODE07984",
        "tf_node_id": "NODE04692",
        "target_node_id": "NODE01285",
        "primary_locator": "PMID:25749383",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "BMI1/Bmi1 mRNA expression",
        "pathway_name": "SPP1-ITGAVITGB3-NFkB-HIF1A-BMI1",
        "route_linkage_status": (
            "manual_primary_spp1_itgav_itgb3_nfkb_hif1a_bmi1_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary hepatocellular-carcinoma study reports osteopontin/SPP1 signaling through integrin "
            "alphaVbeta3, NF-kB activation, increased HIF-1alpha transcription, and downstream BMI1 expression. "
            "The route retains the graph-linked receptor, relay, TF-like complex, and output nodes while keeping "
            "the intermediate handoffs unasserted."
        ),
        "limitations": (
            "The source uses a human hepatocellular-carcinoma model and cancer-stem-like phenotype assays. "
            "The HIF-1 node is represented as an HIF1A/ARNT complex and the Bmi1 output is a current graph "
            "mRNA node; no SCI transfer, causal graph edge, or confidence score is inferred."
        ),
        "species_context": "human",
        "cell_type_context": "human hepatocellular carcinoma cells and tumor stem-like fractions",
        "assay_or_perturbation": "SPP1 depletion/addition; alphaVbeta3-integrin blockade; NF-kB/HIF1A/BMI1 expression; tumorigenicity assays",
    },
    {
        "name": "LGALS3-TLR4-ERKJNK-NFkB-IL6CCL5",
        "lr_edge_id": "M21B-E000894",
        "relay_node_id": "NODE11132",
        "tf_node_id": "NODE07984",
        "target_node_id": "",
        "primary_locator": "PMID:19479862",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|target_gene_expression",
        "output_label": "IL-6 and CCL5 production/secretion",
        "pathway_name": "LGALS3-TLR4-ERKJNK-NFkB-IL6CCL5",
        "route_linkage_status": (
            "manual_primary_lgals3_tlr4_mapk_nfkb_output_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "target_gene_expression_unresolved;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary rheumatoid-arthritis synovial-fibroblast study reports extracellular galectin-3-induced "
            "p38/JNK/ERK/Akt signaling, NF-kB activation, and IL-6/CCL5 production. MAPK inhibition reduced "
            "IL-6, PI3K inhibition reduced CCL5, and NF-kB inhibition affected both outputs."
        ),
        "limitations": (
            "The source uses primary human rheumatoid-arthritis synovial fibroblasts and reports cytokine/chemokine "
            "production rather than a clean terminal target-gene node. The TLR4 assignment is graph-linked, and "
            "no causal graph edge is created."
        ),
        "species_context": "human",
        "cell_type_context": "primary human rheumatoid-arthritis synovial fibroblasts",
        "assay_or_perturbation": "galectin-3 stimulation; ERK/JNK/p38/Akt inhibitors; NF-kB assays; IL-6 and CCL5 production assays",
    },
    {
        "name": "DOPAMINE-DRD1-PKA-CREB-CFOS",
        "lr_edge_id": "M21B-E001438",
        "relay_node_id": "NODE02924",
        "tf_node_id": "NODE02446",
        "target_node_id": "NODE02087",
        "primary_locator": "PMID:7477939; PMID:9068120; PMID:7583020",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "cFos gene expression",
        "pathway_name": "DOPAMINE-DRD1-PKA-CREB-CFOS",
        "route_linkage_status": (
            "manual_primary_dopamine_drd1_pka_creb_cfos_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ),
        "evidence_summary": (
            "Primary rat striatal studies support D1-like dopamine receptor stimulation, PKA/CREB phosphorylation, "
            "and c-fos induction. A complementary study reports CREB interaction with c-fos regulatory elements, "
            "so the route retains the existing DRD1-associated relay, CREB, and cFos nodes as a composed evidence route."
        ),
        "limitations": (
            "The evidence comes from rat striatal primary cultures and rat striatum. The exact PKA/PKC branch and "
            "receptor-to-relay handoff are composed across primary studies; no causal graph edge or confidence score "
            "is inferred."
        ),
        "species_context": "rat",
        "cell_type_context": "primary rat striatal neurons and rat striatum",
        "assay_or_perturbation": "dopamine/D1 agonist; D1 antagonism; PKA/PKC inhibition; CREB phosphorylation; c-fos mRNA, promoter, and CRE-binding assays",
    },
    {
        "name": "ATP-P2X7-NFkB-output",
        "lr_edge_id": "M21B-E000171",
        "relay_node_id": "NODE08717",
        "tf_node_id": "NODE07984",
        "target_node_id": "",
        "primary_locator": "PMID:9412459",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|target_gene_expression",
        "output_label": "NF-kB p65 activation and cytokine-expression output",
        "pathway_name": "ATP-P2X7-NFkB-output",
        "route_linkage_status": (
            "manual_primary_atp_p2x7_nfkb_output_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "target_gene_expression_unresolved;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary microglial study reports extracellular ATP activating NF-kB through the P2Z/P2X7 purinergic "
            "receptor by selectively targeting NF-kB p65. The route preserves the ATP-P2X7 receptor, inflammatory "
            "relay, and NF-kB layers while leaving terminal gene output unresolved."
        ),
        "limitations": (
            "The source supports receptor-proximal NF-kB activation in microglia but does not identify a terminal "
            "target gene for this route. The graph-linked relay is retained as an evidence-layer continuation; no "
            "causal graph edge or confidence score is inferred."
        ),
        "species_context": "rat/mouse microglial model as reported by the primary study",
        "cell_type_context": "primary microglial cells",
        "assay_or_perturbation": "extracellular ATP stimulation; P2Z/P2X7 receptor activation; NF-kB p65 translocation or activation assays",
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
        relay = nodes.get(spec["relay_node_id"], {})
        tf = nodes.get(spec["tf_node_id"], {})
        target = nodes.get(spec["target_node_id"], {})
        evidence_ids = unique_join(lr.get("evidence_ids", ""), spec["primary_locator"])
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-NEXTGAP-{index:03d}",
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
                "intracellular_continuation_label": relay.get("canonical_label", ""),
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": spec["tf_node_id"],
                "transcription_factor_label": tf.get("canonical_label", ""),
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
                "evidence_ids": evidence_ids,
                "source_chain_id": f"M21B-LITEXP-NEXTGAP-{index:03d}",
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
                    f"Primary-evidence route overlay for {spec['name']}. Unresolved handoffs and graph "
                    "target limitations are retained explicitly; no graph edge, causal assertion, or "
                    "confidence score is created."
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
