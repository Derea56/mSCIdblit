#!/usr/bin/env python3
"""Build primary-literature route overlays for the next canonical ligand gaps."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


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
    specs = [
        {
            "expansion_id": "M21B-LITEXP-IL17C-IL17RE-ACT1-NFKB-NFKBIZ",
            "ligand_node_id": "NODE05336",
            "ligand_label": "IL17C",
            "lr_edge_id": "M21B-E000749",
            "receptor_node_id": "NODE05343",
            "receptor_label": "IL17RA:IL17RE receptor complex",
            "relay_node_id": "NODE00152",
            "relay_label": "ACT1/CIKS",
            "tf_node_id": "NODE07984",
            "tf_label": "NF-kB",
            "target_node_id": "NODE08048",
            "target_label": "NFKBIZ gene",
            "pathway_name": "IL17C-IL17RA-IL17RE-ACT1-NF-kB-NFKBIZ",
            "primary_locator": "PMID:21982598; PMID:23944933",
            "evidence_summary": (
                "Primary studies identify IL-17C binding to IL-17RE in an IL-17RA-containing receptor complex, "
                "require Act1 for signaling, and report induction of IκBζ/NFKBIZ or IL-17RE-dependent epithelial "
                "host-defense genes. The route retains NF-kB as the transcriptional family layer between the "
                "Act1 signalosome and NFKBIZ expression."
            ),
            "limitations": (
                "The cited studies use Th17 and airway epithelial systems and do not establish one uninterrupted "
                "IL17C-to-NFKBIZ experiment with every Act1-to-NF-kB handoff. Receptor-to-relay, relay-to-TF, and "
                "TF-to-target relationships are therefore retained as evidence-layer composition; no SCI transfer "
                "is inferred."
            ),
            "cell_type_context": "mouse Th17 cells; primary human bronchial epithelial cells",
            "assay_or_perturbation": "IL-17C stimulation; IL17RE expression or knockdown; Act1 deficiency; NFKBIZ and epithelial host-defense gene expression",
            "species_context": "human; mouse",
        },
        {
            "expansion_id": "M21B-LITEXP-CD40L-CD40-TRAF2-NFKB-IL6",
            "ligand_node_id": "NODE01898",
            "ligand_label": "CD40LG/CD154",
            "lr_edge_id": "M21B-E000679",
            "receptor_node_id": "NODE01893",
            "receptor_label": "CD40/TNFRSF5",
            "relay_node_id": "NODE11375",
            "relay_label": "TRAF2",
            "tf_node_id": "NODE07984",
            "tf_label": "NF-kB",
            "target_node_id": "NODE05233",
            "target_label": "IL-6 gene",
            "pathway_name": "CD40L-CD40-TRAF2-NF-kB-IL6",
            "primary_locator": "PMID:11886848; PMID:16260598",
            "evidence_summary": (
                "Primary dendritic-cell studies show CD40 ligation induces IL-6 transcription through CD40-tail "
                "recruitment of TRAF2 and NF-kB promoter activity. Independent loss-of-function experiments show "
                "that CD40-associated TRAF2 and TRAF6 control NF-kB and MAPK signaling in CD40-stimulated cells."
            ),
            "limitations": (
                "The literature resolves CD40-to-TRAF2 and NF-kB-dependent IL-6 transcription but does not establish "
                "a single molecular experiment spanning every receptor-to-TRAF2 handoff in the normalized graph. "
                "The route remains evidence-only and model-specific."
            ),
            "cell_type_context": "murine dendritic cells; fibroblasts and epithelial cells",
            "assay_or_perturbation": "anti-CD40 ligation; IL-6 RT-PCR and promoter assays; NF-kB or JunD inhibition; TRAF2 depletion or knockout",
            "species_context": "human; mouse",
        },
        {
            "expansion_id": "M21B-LITEXP-CD40L-CD40-TRAF2-AP1-IL6",
            "ligand_node_id": "NODE01898",
            "ligand_label": "CD40LG/CD154",
            "lr_edge_id": "M21B-E000679",
            "receptor_node_id": "NODE01893",
            "receptor_label": "CD40/TNFRSF5",
            "relay_node_id": "NODE11375",
            "relay_label": "TRAF2",
            "tf_node_id": "NODE00609",
            "tf_label": "AP-1",
            "target_node_id": "NODE05233",
            "target_label": "IL-6 gene",
            "pathway_name": "CD40L-CD40-TRAF2-AP1-IL6",
            "primary_locator": "PMID:11886848; PMID:16260598",
            "evidence_summary": (
                "The same primary CD40-ligation study identifies c-Jun, JunB, JunD, and c-Fos DNA-protein "
                "complexes as AP-1 mediators of IL-6 promoter activation, while TRAF2/TRAF6 perturbation studies "
                "resolve the proximal CD40 signaling requirement."
            ),
            "limitations": (
                "AP-1 is a family-level transcriptional component and the cited work does not resolve a single "
                "TRAF2-to-AP-1 molecular handoff in the normalized graph. The route is retained as a primary "
                "evidence composition without a confidence score or causal-edge assertion."
            ),
            "cell_type_context": "murine dendritic cells; fibroblasts and epithelial cells",
            "assay_or_perturbation": "anti-CD40 ligation; AP-1 DNA binding and IL-6 promoter assays; TRAF2 or TRAF6 perturbation",
            "species_context": "human; mouse",
        },
        {
            "expansion_id": "M21B-LITEXP-TRAIL-DR4-FADD-NFKB-output",
            "ligand_node_id": "NODE11392",
            "ligand_label": "TRAIL/TNFSF10",
            "lr_edge_id": "M21B-E000467",
            "receptor_node_id": "NODE02940",
            "receptor_label": "DR4/TNFRSF10A",
            "relay_node_id": "NODE03482",
            "relay_label": "FADD",
            "tf_node_id": "NODE07984",
            "tf_label": "NF-kB",
            "target_node_id": "",
            "target_label": "",
            "pathway_name": "TRAIL-DR4-FADD-NF-kB-death-receptor-response",
            "primary_locator": "PMID:9430227; PMID:12207174; PMID:23096115",
            "evidence_summary": (
                "Primary studies show that TRAIL ligation of DR4 recruits FADD and activates NF-kB, with the "
                "resulting transcriptional response including death-receptor amplification and altered apoptotic "
                "sensitivity. FADD and caspase-8 loss-of-function experiments support the receptor-proximal route."
            ),
            "limitations": (
                "TRAIL responses are strongly cell-context dependent and bifurcate into apoptotic and non-apoptotic "
                "branches. This route records the FADD-to-NF-kB functional branch and does not claim that every "
                "TRAIL-stimulated cell will produce the same output."
            ),
            "cell_type_context": "human epithelial and leukemia-derived cell systems",
            "assay_or_perturbation": "TRAIL stimulation; FADD or caspase-8 loss-of-function; NF-kB reporter; DR4/DR5 expression and apoptosis assays",
            "species_context": "human; mammalian cell systems",
        },
        {
            "expansion_id": "M21B-LITEXP-TRAIL-DR5-FADD-NFKB-output",
            "ligand_node_id": "NODE11392",
            "ligand_label": "TRAIL/TNFSF10",
            "lr_edge_id": "M21B-E000468",
            "receptor_node_id": "NODE02941",
            "receptor_label": "DR5/TNFRSF10B",
            "relay_node_id": "NODE03482",
            "relay_label": "FADD",
            "tf_node_id": "NODE07984",
            "tf_label": "NF-kB",
            "target_node_id": "",
            "target_label": "",
            "pathway_name": "TRAIL-DR5-FADD-NF-kB-DR5-apoptotic-response",
            "primary_locator": "PMID:9430227; PMID:12207174; PMID:23096115",
            "evidence_summary": (
                "Primary studies show that TRAIL ligation of DR5 recruits FADD and activates NF-kB, and that NF-kB "
                "activity can increase DR5 expression and amplify the apoptotic response. FADD and caspase-8 "
                "perturbations support the receptor-proximal signaling branch."
            ),
            "limitations": (
                "The terminal DR5 amplification output is represented as a functional readout rather than a target "
                "gene because the normalized graph does not contain a DR5 target-gene node for this route. The "
                "route is therefore evidence-only and cell-context bounded."
            ),
            "cell_type_context": "human epithelial and leukemia-derived cell systems",
            "assay_or_perturbation": "TRAIL stimulation; FADD or caspase-8 loss-of-function; NF-kB reporter; DR5 expression and apoptosis assays",
            "species_context": "human; mammalian cell systems",
        },
        {
            "expansion_id": "M21B-LITEXP-VEGFC-FLT4-ERK-AP1-output",
            "ligand_node_id": "NODE11739",
            "ligand_label": "VEGFC/VEGF-C",
            "lr_edge_id": "M21B-E000358",
            "receptor_node_id": "NODE03753",
            "receptor_label": "FLT4/VEGFR3",
            "relay_node_id": "NODE06776",
            "relay_label": "MAPK1/MAPK3",
            "tf_node_id": "NODE00609",
            "tf_label": "AP-1",
            "target_node_id": "",
            "target_label": "",
            "pathway_name": "VEGFC-VEGFR3-ERK-AP1-lymphatic-output",
            "primary_locator": "PMID:8617204; PMID:11532940; PMID:25281926; PMID:25524775",
            "evidence_summary": (
                "Primary studies establish VEGF-C binding and activation of VEGFR3, VEGF-C-induced ERK signaling "
                "in lymphatic endothelial cells, and ERK-dependent lymphatic endothelial growth, survival, and "
                "migration. AP-1 is retained as the MAPK-linked transcriptional family layer for plausibility analysis."
            ),
            "limitations": (
                "The cited studies resolve VEGFR3-to-ERK signaling and endothelial outputs but do not establish an "
                "uninterrupted VEGFC-to-AP-1 experiment. The relay-to-TF handoff remains explicitly unasserted."
            ),
            "cell_type_context": "human lymphatic endothelial cells; bovine capillary endothelial cells",
            "assay_or_perturbation": "VEGF-C stimulation; VEGFR3 phosphorylation; ERK/JNK/p38 phosphorylation; kinase inhibition; endothelial migration, growth, survival, and tube assays",
            "species_context": "human; bovine; mammalian cell systems",
        },
        {
            "expansion_id": "M21B-LITEXP-VEGFC-KDR-ERK-AP1-output",
            "ligand_node_id": "NODE11739",
            "ligand_label": "VEGFC/VEGF-C",
            "lr_edge_id": "M21B-E000359",
            "receptor_node_id": "NODE06102",
            "receptor_label": "KDR/VEGFR2",
            "relay_node_id": "NODE06776",
            "relay_label": "MAPK1/MAPK3",
            "tf_node_id": "NODE00609",
            "tf_label": "AP-1",
            "target_node_id": "",
            "target_label": "",
            "pathway_name": "VEGFC-VEGFR2-ERK-AP1-endothelial-output",
            "primary_locator": "PMID:8617204; PMID:9506953; PMID:11532940",
            "evidence_summary": (
                "Primary receptor studies show that VEGF-C activates KDR/VEGFR2 as well as VEGFR3, and that the "
                "VEGFR2-competent VEGF-C signal reaches ERK/MAPK and endothelial migration or permeability outputs. "
                "AP-1 is retained as the downstream MAPK-linked transcriptional family layer."
            ),
            "limitations": (
                "The cited studies do not establish one uninterrupted VEGFC-to-KDR-to-ERK-to-AP-1 experiment, and "
                "the receptor contribution varies with VEGF-C processing and receptor context. This is an "
                "evidence-layer route, not a universal causal assertion."
            ),
            "cell_type_context": "human endothelial cells; bovine capillary endothelial cells",
            "assay_or_perturbation": "VEGF-C processing and receptor-binding mutants; VEGFR2 autophosphorylation; ERK/MAPK signaling; endothelial migration and permeability assays",
            "species_context": "human; bovine; mammalian cell systems",
        },
    ]

    rows: list[dict[str, str]] = []
    for spec in specs:
        required_nodes = [
            spec["ligand_node_id"], spec["receptor_node_id"], spec["relay_node_id"], spec["tf_node_id"]
        ]
        if spec.get("target_node_id"):
            required_nodes.append(spec["target_node_id"])
        missing = [node_id for node_id in required_nodes if node_id not in nodes]
        if missing:
            raise ValueError(f"{spec['expansion_id']}: missing nodes {missing}")
        lr = edges.get(spec["lr_edge_id"])
        if not lr or (lr["source_node_id"], lr["target_node_id"]) != (
            spec["ligand_node_id"], spec["receptor_node_id"]
        ):
            raise ValueError(f"{spec['expansion_id']}: ligand-receptor edge endpoints do not match")
        has_target = bool(spec.get("target_node_id"))
        missing_layers = ["receptor_to_intracellular_edge", "intracellular_to_tf_edge"]
        if not has_target:
            missing_layers.append("target_gene_expression")
        linkage = (
            "graph_linked_route_source;manual_primary_route_expansion;primary_layer_linked;"
            "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
            + ("tf_to_target_edge_not_asserted;" if has_target else "")
            + "end_to_end_chain_not_asserted_by_single_source;evidence_route_only"
        )
        rows.append(
            {
                "expansion_id": spec["expansion_id"],
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression" if has_target else "ligand>receptor>intracellular>TF>output",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges" if has_target else "ligand_receptor_intracellular_tf_output_missing_target_gene",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression" if has_target else "ligand|receptor|intracellular_continuation|transcription_factor|output",
                "missing_layers": "|".join(missing_layers),
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": spec["ligand_node_id"],
                "ligand_label": spec["ligand_label"],
                "ligand_receptor_edge_id": spec["lr_edge_id"],
                "receptor_node_id": spec["receptor_node_id"],
                "receptor_label": spec["receptor_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": spec["relay_node_id"],
                "intracellular_continuation_label": spec["relay_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": spec["tf_node_id"],
                "transcription_factor_label": spec["tf_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": spec.get("target_node_id", ""),
                "target_gene_label": spec.get("target_label", ""),
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": spec.get("target_label", "") if has_target else spec["pathway_name"].split("-")[-1] + " functional output",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression" if has_target else "primary_composed_downstream_output",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["primary_locator"]),
                "source_chain_id": spec["expansion_id"],
                "source_evidence_record_id": "",
                "route_linkage_status": linkage,
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression" if has_target else "generic_functional_readout",
                "primary_locator": spec["primary_locator"],
                "citation_note": "Primary literature supports the listed route layers; unresolved handoffs remain explicitly bounded and no confidence score is assigned.",
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular relay; nuclear transcriptional/output layer",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence with graph-linked ligand-receptor identity",
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
