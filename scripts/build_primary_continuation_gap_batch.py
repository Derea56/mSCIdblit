#!/usr/bin/env python3
"""Build another primary-literature evidence-route tranche.

The rows preserve supported layers for mSCS route plausibility. They do not
create graph edges, causal traversal, or confidence scores.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "GDNF-GFRA1RET-RASERK-CREB-CFOS",
        "lr_edge_id": "M21B-E000322",
        "relay_node_id": "NODE04069",
        "tf_node_id": "NODE02446",
        "target_node_id": "NODE02087",
        "primary_locator": "PMID:17962702",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "cFos gene expression",
        "pathway_name": "GDNF-GFRA1RET-RASERK-CREB-CFOS",
        "route_linkage_status": (
            "manual_primary_gdnf_gfra1_ret_ras_erk_creb_cfos_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary mouse spermatogonial-stem-cell study reports GDNF-induced RET phosphorylation, Shc/Grb2 "
            "association, Ras and ERK1/2 activation, CREB-family phosphorylation, and c-fos transcription. "
            "The route maps those source-supported layers onto the existing GDNF-GFRA1/RET, ERK-CREB, CREB, and cFos nodes."
        ),
        "limitations": (
            "The source uses a mouse spermatogonial stem-cell line and the exact receptor-proximal and ERK-to-CREB "
            "handoffs are retained as evidence-layer links rather than new graph edges. No SCI transfer or confidence "
            "score is inferred."
        ),
        "species_context": "mouse",
        "cell_type_context": "mouse C18-4 spermatogonial stem-cell line",
        "assay_or_perturbation": "GDNF stimulation; RET phosphorylation; Shc/Grb2 association; Ras and ERK1/2 activation; MEK inhibition; CREB-family phosphorylation; c-fos transcription",
        "effect_polarity": "activating",
    },
    {
        "name": "FGF2-FGFR1-ERK-JUND-UPA",
        "lr_edge_id": "M21B-E000203",
        "relay_node_id": "NODE06926",
        "tf_node_id": "NODE06059",
        "target_node_id": "",
        "primary_locator": "PMID:8547215",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|target_gene_expression",
        "output_label": "uPA/PLAU gene activation",
        "pathway_name": "FGF2-FGFR1-RASRAFMEKERK-JUND-UPA",
        "route_linkage_status": (
            "manual_primary_fgf2_fgfr1_ras_raf_mek_erk_jund_upa_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "target_gene_node_unresolved;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary NIH 3T3 fibroblast study reports FGF2-induced uPA transcription through a Ras/Raf-1/MEK/ERK-2/JunD "
            "pathway and a PEA3/AP-1 promoter element. The route preserves the FGF2-FGFR1 edge, MEK/ERK relay, JunD TF, "
            "and uPA transcriptional output while leaving the terminal graph target unresolved."
        ),
        "limitations": (
            "The study uses NIH 3T3 fibroblasts and the current graph does not expose a clean PLAU target-gene node for "
            "this route. The FGF2-FGFR1 edge is structural in the graph, so downstream linkage remains evidence-only."
        ),
        "species_context": "mouse fibroblast model",
        "cell_type_context": "NIH 3T3 fibroblasts",
        "assay_or_perturbation": "FGF2 stimulation; Ras/Raf/MEK/ERK activity assays; dominant-negative signaling constructs; uPA promoter reporter; JunD/AP-1 promoter analysis",
        "effect_polarity": "activating",
    },
    {
        "name": "SFTPD-TLR4MD2-PI3KAKTNFkB-inflammatory-output",
        "lr_edge_id": "M21B-E000701",
        "relay_node_id": "NODE10270",
        "tf_node_id": "NODE07984",
        "target_node_id": "",
        "primary_locator": "PMID:18990700",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|target_gene_expression",
        "output_label": "NF-kB attenuation and TNF-alpha/cytokine secretion",
        "pathway_name": "SFTPD-TLR4MD2-PI3KAKTNFkB-inflammatory-output",
        "route_linkage_status": (
            "manual_primary_sftpd_tlr4_md2_pi3k_akt_nfkb_output_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "target_gene_expression_unresolved;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary alveolar-macrophage and TLR4/MD-2-transfected-cell study reports SP-D binding TLR4/MD-2 and "
            "down-regulating LPS-elicited NF-kB activation and TNF-alpha secretion. The route retains the existing "
            "SFTPD-TLR4/MD-2 antagonism relay and NF-kB layer with inhibitory polarity."
        ),
        "limitations": (
            "The source studies SP-D modulation of LPS responses rather than an isolated terminal gene target. The route "
            "is inhibitory and output-level; it does not infer a specific TNF target-gene node or causal graph edge."
        ),
        "species_context": "human and rodent alveolar-macrophage systems",
        "cell_type_context": "alveolar macrophages and TLR4/MD-2-transfected HEK293 cells",
        "assay_or_perturbation": "SP-D binding to TLR4/MD-2; LPS stimulation; NF-kB activation; TNF-alpha secretion; receptor-transfected-cell assays",
        "effect_polarity": "inhibitory",
    },
    {
        "name": "ANGPTL2-ITGA5ITGB1-MAPKAKTNFkB-inflammatory-output",
        "lr_edge_id": "M21B-E000645",
        "relay_node_id": "NODE06768",
        "tf_node_id": "NODE07984",
        "target_node_id": "",
        "primary_locator": "PMID:31581797",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|target_gene_expression",
        "output_label": "IL-1beta, TNF-alpha, COX-2, ADAMTS-5, MMP-3, and MMP-13 gene expression",
        "pathway_name": "ANGPTL2-ITGA5ITGB1-MAPKAKTNFkB-inflammatory-output",
        "route_linkage_status": (
            "manual_primary_angptl2_itga5_itgb1_mapk_akt_nfkb_output_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "target_gene_node_unresolved;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary chondrocyte study reports ANGPTL2-induced integrin alpha5beta1-dependent phosphorylation of "
            "MAPKs, Akt, and NF-kB together with increased IL-1beta, TNF-alpha, COX-2, ADAMTS-5, MMP-3, and MMP-13 gene "
            "expression. The route retains the existing integrin and MAPK/Akt/NF-kB relay as a functional-output route."
        ),
        "limitations": (
            "The source uses ATDC5 chondrocyte cells and the graph lacks one clean terminal node for the multi-gene "
            "output set. The route is evidence-only and does not infer a direct TF-to-target edge or SCI transfer."
        ),
        "species_context": "mouse chondrocyte model",
        "cell_type_context": "ATDC5 chondrocyte cells",
        "assay_or_perturbation": "recombinant ANGPTL2; alpha5beta1-integrin blockade; MAPK/Akt/NF-kB phosphorylation; inflammatory-gene RT-qPCR",
        "effect_polarity": "activating",
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
                "expansion_id": f"M21B-LITEXP-CONTGAP-{index:03d}",
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
                "output_evidence_type": "primary_functional_output",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["primary_locator"]),
                "source_chain_id": f"M21B-LITEXP-CONTGAP-{index:03d}",
                "source_evidence_record_id": "",
                "route_linkage_status": spec["route_linkage_status"],
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "generic_functional_readout",
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
                "effect_polarity": spec["effect_polarity"],
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
