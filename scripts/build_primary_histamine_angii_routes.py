#!/usr/bin/env python3
"""Build primary-evidence routes for histamine and angiotensin-II gaps.

These records are evidence-layer overlays.  They preserve the experimentally
supported route layers while keeping graph handoffs and causal traversal
unasserted unless an existing edge already represents them.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "HISTAMINE-HRH1-PKCdelta-ERK-CREB-EGR1",
        "lr_edge_id": "M21B-E001346",
        "relay_node_id": "NODE03364",
        "tf_node_id": "NODE02446",
        "target_node_id": "NODE03139",
        "primary_locator": "PMID:18682391; PMCID:PMC2556005; DOI:10.1074/jbc.M803071200",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "EGR1 promoter/mRNA expression",
        "pathway_name": "Histamine-HRH1-PKCdelta-ERK-CREB-EGR1",
        "route_linkage_status": (
            "manual_primary_histamine_hrh1_pkcdelta_erk_creb_egr1_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary human aortic endothelial-cell study reports histamine-dependent H1R activation, "
            "PKC-delta and ERK1/2 activation, CREB involvement, and rapid EGR1 mRNA/protein induction. "
            "The route retains the current graph's H1R, ERK1/2, CREB, and EGR1 target nodes while leaving "
            "the exact graph handoffs explicit as unresolved."
        ),
        "limitations": (
            "The study uses primary human aortic endothelial cells and pharmacologic or siRNA perturbations; "
            "it does not assert every handoff as a graph edge. No causal edge or database confidence score is added."
        ),
        "species_context": "human",
        "cell_type_context": "primary human aortic endothelial cells",
        "assay_or_perturbation": "histamine stimulation; H1R antagonism; PKC-delta, ERK, p38, JNK and CREB perturbation; EGR1 mRNA/protein assays",
    },
    {
        "name": "HISTAMINE-HRH1-PKC-ERK-NFkB-IL6",
        "lr_edge_id": "M21B-E001346",
        "relay_node_id": "NODE09093",
        "tf_node_id": "NODE07984",
        "target_node_id": "NODE05511",
        "primary_locator": "PMID:15652235",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "IL6 gene expression and secretion",
        "pathway_name": "Histamine-HRH1-PKC-ERK-NFkB-IL6",
        "route_linkage_status": (
            "manual_primary_histamine_hrh1_pkc_erk_nfkb_il6_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary human keratinocyte study reports H1R-dependent histamine induction of IL6, with "
            "PKC, Raf/MEK/ERK, IKK/I-kappaB and NF-kB p65 activation and blockade by H1R or PKC inhibition. "
            "The route maps the observed PKC/ERK continuation to the existing PLCG1-PKC-ERK node and retains "
            "NF-kB and IL6 as explicit downstream evidence layers."
        ),
        "limitations": (
            "The source reports a coupled PKC/MAPK and IKK/NF-kB response in human epidermal keratinocytes, "
            "not a single isolated molecular handoff matching every graph node. The route is evidence-only."
        ),
        "species_context": "human",
        "cell_type_context": "human epidermal keratinocytes",
        "assay_or_perturbation": "histamine stimulation; H1R antagonist; PKC inhibition; ERK/IKK/NF-kB phosphorylation; IL6 expression and release assays",
    },
    {
        "name": "ANGIOTENSIN-II-AGTR1-ERK-CREB-EGR1",
        "lr_edge_id": "M21B-E001353",
        "relay_node_id": "NODE03364",
        "tf_node_id": "NODE02446",
        "target_node_id": "NODE03139",
        "primary_locator": "PMID:28105751; PMID:11502738; PMID:18272536",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "EGR1 promoter/mRNA expression",
        "pathway_name": "Angiotensin-II-AGTR1-ERK-CREB-EGR1",
        "route_linkage_status": (
            "manual_primary_angii_agtr1_erk_creb_egr1_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ),
        "evidence_summary": (
            "Primary vascular smooth-muscle studies support Ang II/AT1R-dependent EGR1 induction through "
            "ERK-linked signaling. A mechanistic study reports ERK1/2 and CREB phosphorylation, CREB "
            "silencing reducing Ang II-induced EGR1, and calcium-channel perturbation attenuating the response; "
            "additional primary work links AT1R/EGR1 activation to downstream promoter output."
        ),
        "limitations": (
            "The supporting studies use A-10 or other vascular smooth-muscle models and combine receptor, "
            "kinase, calcium, and promoter experiments across papers. The exact AT1R-to-ERK and CREB-to-EGR1 "
            "handoffs are retained as evidence layers rather than asserted graph edges."
        ),
        "species_context": "rat and mammalian vascular smooth-muscle systems",
        "cell_type_context": "vascular smooth-muscle cells",
        "assay_or_perturbation": "Ang II stimulation; AT1R antagonism; ERK/CREB phosphorylation; STIM1/Orai1, CaMKII and CREB perturbation; EGR1 expression assays",
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
        target = nodes[spec["target_node_id"]]
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-HISTAMINE-ANGII-{index:03d}",
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
                "source_chain_id": f"M21B-LITEXP-HISTAMINE-ANGII-{index:03d}",
                "source_evidence_record_id": "",
                "route_linkage_status": spec["route_linkage_status"],
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": spec["primary_locator"],
                "citation_note": (
                    f"Primary-evidence route overlay for {spec['name']}. Unresolved handoffs are retained "
                    "explicitly; no graph edge, causal assertion, or confidence score is created."
                ),
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular signaling; nuclear output context",
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
