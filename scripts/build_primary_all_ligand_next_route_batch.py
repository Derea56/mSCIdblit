#!/usr/bin/env python3
"""Build the next evidence-first route tranche for incomplete ligands.

The rows below expose primary-supported downstream layers for ligands that
already have graph-linked receptor entries.  Missing handoffs remain explicit;
these rows never create causal graph edges or database confidence scores.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "VEGFA-KDR-ERK-EGR1-tissue-factor",
        "lr_edge_id": "M21B-E000183",
        "relay_node_id": "NODE03370",
        "tf_node_id": "NODE03137",
        "target_node_id": "",
        "primary_locator": "PMID:11149911; PMID:11387210",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
        "output_label": "Tissue factor/F3 up-regulation",
        "pathway_name": "VEGFA-KDR-ERK-EGR1-tissue-factor",
        "evidence_summary": (
            "Primary endothelial-cell work reports VEGF-induced EGR-1 and tissue-factor up-regulation. "
            "A complementary KDR phosphosite study shows that VEGF-A-induced ERK1/2 activation depends "
            "on KDR Y1175. The route retains the graph-linked VEGFA-KDR input and the ERK/EGR1 layers "
            "while leaving the molecular handoffs and terminal F3 target node unresolved."
        ),
        "limitations": (
            "The supporting studies use endothelial systems and complementary perturbations rather than one "
            "single uninterrupted VEGFA-to-F3 chain. The current graph does not expose a clean F3 target-gene "
            "node for this route, so the terminal result is represented as a functional transcriptional output."
        ),
        "species_context": "human endothelial-cell systems",
        "cell_type_context": "cultured endothelial cells",
        "assay_or_perturbation": "VEGF stimulation; KDR Y1175 mutation; ERK1/2 phosphorylation; EGR1 and tissue-factor expression assays",
        "effect_polarity": "activating",
    },
    {
        "name": "HGF-MET-ERK-AP1-transcriptional-output",
        "lr_edge_id": "M21B-E000167",
        "relay_node_id": "NODE03370",
        "tf_node_id": "NODE00609",
        "target_node_id": "",
        "primary_locator": "PMID:11071904; PMID:15218027",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
        "output_label": "EBS/AP-1-dependent transcriptional response",
        "pathway_name": "HGF-MET-ERK-AP1-transcriptional-output",
        "evidence_summary": (
            "A primary Madin-Darby canine kidney-cell study reports sequential ERK activation and an "
            "EBS/AP-1-dependent transcriptional response after scatter factor/HGF stimulation. The route "
            "connects that source-supported ERK/AP-1 output to the existing mature HGF-MET receptor entry "
            "without asserting an unobserved direct graph handoff."
        ),
        "limitations": (
            "The primary study resolves an AP-1-dependent transcriptional response rather than a single named "
            "target gene, and the HGF-MET input is retained from a complementary primary receptor study. "
            "The route is evidence-only and does not infer a universal MET-to-ERK or ERK-to-AP-1 edge."
        ),
        "species_context": "canine epithelial-cell system",
        "cell_type_context": "Madin-Darby canine kidney epithelial cells",
        "assay_or_perturbation": "scatter factor/HGF stimulation; ERK and JNK time course; EBS/AP-1 reporter; MEK/MKP2 perturbation",
        "effect_polarity": "activating",
    },
    {
        "name": "WNT5B-FZD2-JNK-NFkB-IL6",
        "lr_edge_id": "M21B-E006533",
        "relay_node_id": "NODE06798",
        "tf_node_id": "NODE07984",
        "target_node_id": "NODE05510",
        "primary_locator": "PMID:27036869; DOI:10.1152/ajplung.00226.2015",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "IL6/Il6 gene expression and secretion",
        "pathway_name": "WNT5B-FZD2-TAK1-JNK-NFkB-IL6",
        "evidence_summary": (
            "Primary human lung-fibroblast work reports recombinant WNT5B responses mediated primarily by FZD2, "
            "with TAK1, JNK, p38 and IKK/NF-kB perturbation and increased IL-6 expression/secretion. The route "
            "retains the exact graph-linked WNT5B-FZD2 edge and maps the measured JNK, NF-kB and IL-6 layers."
        ),
        "limitations": (
            "The primary study supports a FZD2-associated inflammatory program but does not establish every "
            "molecular handoff as a direct graph edge or prove NF-kB occupancy at the endogenous Il6 locus. "
            "The route preserves the primary lung-fibroblast context and does not infer SCI transfer."
        ),
        "species_context": "human",
        "cell_type_context": "primary human fetal lung fibroblasts and COPD/non-COPD lung fibroblasts",
        "assay_or_perturbation": "recombinant WNT5B; FZD2 pathway perturbation; TAK1/JNK/p38/IKK inhibition; IL-6 expression and secretion assays",
        "effect_polarity": "activating",
    },
    {
        "name": "WNT5B-FZD2-JNK-NFkB-CXCL8",
        "lr_edge_id": "M21B-E006533",
        "relay_node_id": "NODE06798",
        "tf_node_id": "NODE07984",
        "target_node_id": "NODE02679",
        "primary_locator": "PMID:27036869; DOI:10.1152/ajplung.00226.2015",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "CXCL8/IL8 gene expression and secretion",
        "pathway_name": "WNT5B-FZD2-TAK1-JNK-NFkB-CXCL8",
        "evidence_summary": (
            "The same primary human lung-fibroblast study reports WNT5B-induced CXCL8/IL-8 expression and "
            "secretion with FZD2, TAK1, JNK, p38 and IKK/NF-kB pathway perturbations. This route keeps the "
            "second measured inflammatory output separate so mSCS can evaluate IL-6 and CXCL8 responses independently."
        ),
        "limitations": (
            "The source supports a pathway-level inflammatory response rather than a direct NF-kB-to-CXCL8 "
            "promoter assertion. The route is a primary evidence composition with explicit missing handoffs, "
            "not a causal graph traversal or confidence assignment."
        ),
        "species_context": "human",
        "cell_type_context": "primary human fetal lung fibroblasts and COPD/non-COPD lung fibroblasts",
        "assay_or_perturbation": "recombinant WNT5B; FZD2 pathway perturbation; TAK1/JNK/p38/IKK inhibition; CXCL8/IL-8 expression and secretion assays",
        "effect_polarity": "activating",
    },
    {
        "name": "CXCL12-CXCR4-ERK-dendritic-cell-output",
        "lr_edge_id": "M21B-E000158",
        "relay_node_id": "NODE03370",
        "tf_node_id": "",
        "target_node_id": "",
        "primary_locator": "PMID:21878648; PMID:28325822",
        "path_expression": "ligand>receptor>intracellular>output",
        "route_tier": "ligand_receptor_intracellular_output_missing_tf",
        "known_layers": "ligand|receptor|intracellular_continuation|output",
        "missing_layers": "receptor_to_intracellular_edge|transcription_factor|target_gene_expression",
        "output_label": "CXCL12/CXCR4-dependent dendritic-cell chemotaxis and survival",
        "pathway_name": "CXCL12-CXCR4-ERK-AKT-mTOR-dendritic-cell-output",
        "evidence_summary": (
            "Primary mature-dendritic-cell work reports CXCL12/CXCR4 signaling through an ERK1/2-, AKT- and "
            "mTORC1-associated signaling core that jointly controls chemotaxis and survival. The route retains "
            "the exact CXCL12-CXCR4 input while representing the measured ERK continuation as a functional-output route."
        ),
        "limitations": (
            "The primary study resolves a signaling core and cell behavior rather than a named transcription factor "
            "or target gene. CXCL12 monomer/dimer and receptor-context differences are retained through the second "
            "primary locator; no universal GPCR-to-ERK handoff or SCI receiver-cell claim is inferred."
        ),
        "species_context": "human and mammalian cell systems",
        "cell_type_context": "mature dendritic cells",
        "assay_or_perturbation": "CXCL12 stimulation; CXCR4, AKT, ERK1/2 and mTORC1 perturbation; chemotaxis and survival assays",
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
        relay = nodes.get(spec["relay_node_id"], {})
        tf = nodes.get(spec["tf_node_id"], {})
        target = nodes.get(spec["target_node_id"], {})
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-ALL-LIGAND-NEXT-{index:03d}",
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
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["primary_locator"]),
                "source_chain_id": f"M21B-LITEXP-ALL-LIGAND-NEXT-{index:03d}",
                "source_evidence_record_id": "",
                "route_linkage_status": unique_join(
                    "manual_primary_all_ligand_next_route",
                    "graph_linked_route_source",
                    "primary_layer_linked",
                    "receptor_to_intracellular_edge_not_asserted",
                    "intracellular_to_tf_edge_not_asserted" if spec["tf_node_id"] else "",
                    "tf_to_target_edge_not_asserted" if spec["target_node_id"] else "",
                    "target_gene_node_unresolved" if not spec["target_node_id"] else "",
                    "end_to_end_chain_not_asserted_by_single_source",
                    "evidence_route_only",
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression" if spec["target_node_id"] else "generic_functional_readout",
                "primary_locator": spec["primary_locator"],
                "citation_note": (
                    f"Primary-evidence route overlay for {spec['name']}. Unresolved handoffs remain explicit; "
                    "no graph edge, causal assertion, or confidence score is created."
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
    print(json.dumps({"rows": len(rows), "output": str(args.output.resolve())}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
