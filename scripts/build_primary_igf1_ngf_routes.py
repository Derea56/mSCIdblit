#!/usr/bin/env python3
"""Build primary-literature route overlays for IGF1 and NGF.

These are evidence-layer compositions.  They retain graph-linked ligand and
receptor identities, preserve source-supported downstream layers, and leave
cross-study handoffs explicitly unresolved rather than creating causal edges.
"""

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
            "expansion_id": "M21B-LITEXP-IGF1-IGF1R-PI3K-FOXO1-GPR17",
            "ligand_node_id": "NODE05034",
            "ligand_label": "IGF1/IGF-I",
            "lr_edge_id": "M21B-E000987",
            "receptor_node_id": "NODE05036",
            "receptor_label": "Igf1r",
            "relay_node_id": "NODE08985",
            "relay_label": "PI3K",
            "tf_node_id": "NODE03781",
            "tf_label": "FOXO1",
            "target_node_id": "NODE04387",
            "target_label": "GPR17 gene",
            "output_node_id": "NODE04387",
            "output_label": "GPR17 expression",
            "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
            "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
            "pathway_name": "IGF1-IGF1R-PI3K-AKT-FOXO1-GPR17",
            "primary_locator": "PMID:35163437",
            "evidence_summary": (
                "A primary SK-N-SH-cell study reports IGF-1-associated PI3K/Akt signaling, FoxO1 nuclear "
                "export, reduced FoxO1 occupancy at the GPR17 promoter, and reduced GPR17 expression. "
                "The route retains the graph-linked IGF1-Igf1r input and represents PI3K/Akt as the "
                "intracellular continuation."
            ),
            "limitations": (
                "The primary study uses an SK-N-SH neuronal cell model and does not establish every "
                "IGF1-Igf1r-to-PI3K/Akt handoff as a graph edge. The route composes the receptor, relay, "
                "FOXO1, and promoter observations without asserting causal traversal, SCI transfer, or a "
                "database confidence score."
            ),
            "cell_type_context": "human SK-N-SH neuroblastoma cells",
            "assay_or_perturbation": "IGF-1 stimulation; PI3K inhibition; FoxO1 knockdown or overexpression; FoxO1 chromatin immunoprecipitation at the GPR17 promoter; GPR17 expression assays",
        },
        {
            "expansion_id": "M21B-LITEXP-NGF-NTRK1-ERK-CREB-BDNF-001",
            "ligand_node_id": "NODE08052",
            "ligand_label": "NGF",
            "lr_edge_id": "M21B-E000321",
            "receptor_node_id": "NODE08423",
            "receptor_label": "NTRK1/TrkA receptor",
            "relay_node_id": "NODE03370",
            "relay_label": "ERK1/2/MAPK1/3",
            "tf_node_id": "NODE02446",
            "tf_label": "CREB",
            "target_node_id": "",
            "target_label": "",
            "output_node_id": "",
            "output_label": "BDNF mRNA and protein expression",
            "path_expression": "ligand>receptor>intracellular>TF>output",
            "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
            "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
            "pathway_name": "NGF-TrkA-ERK/p38-CREB-BDNF-output",
            "primary_locator": "PMID:9528766; PMID:9262478; PMID:9334420; PMID:15207334; PMID:22280975",
            "evidence_summary": (
                "Primary studies support NGF-TrkA signaling, ERK and p38 MAPK activation, CREB Ser133 "
                "phosphorylation, and NGF-associated BDNF mRNA/protein induction in sensory and sympathetic "
                "neuronal systems. The route retains CREB as the transcriptional layer while reporting BDNF "
                "as the measured output rather than inventing a promoter-specific target edge."
            ),
            "limitations": (
                "The supporting studies use complementary neuronal systems and do not establish one uninterrupted "
                "NGF-TrkA-to-BDNF promoter chain. The exact ERK/p38-to-CREB branch and BDNF target locus remain "
                "unresolved in this graph release; no causal graph edge, SCI transfer, or confidence score is inferred."
            ),
            "cell_type_context": "rat sympathetic neurons, dorsal-root-ganglion neurons, and cultured neuronal systems",
            "assay_or_perturbation": "NGF stimulation; TrkA kinase inhibition or dependence; ERK/p38 pathway inhibition; CREB phosphorylation; BDNF mRNA and protein assays",
        },
        {
            "expansion_id": "M21B-LITEXP-ATP-P2RY11-PKA-CREB-BDNF",
            "ligand_node_id": "NODE00998",
            "ligand_label": "ATP/adenosine triphosphate",
            "lr_edge_id": "M21B-E001467",
            "receptor_node_id": "NODE08683",
            "receptor_label": "P2RY11/P2Y11 purinergic receptor",
            "relay_node_id": "NODE09055",
            "relay_label": "PKA",
            "tf_node_id": "NODE02446",
            "tf_label": "CREB",
            "target_node_id": "NODE01191",
            "target_label": "Bdnf promoter IV",
            "tf_target_edge_id": "M22B-E000036",
            "output_node_id": "NODE01191",
            "output_label": "BDNF promoter IV activity and exon IV mRNA expression",
            "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
            "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge",
            "pathway_name": "ATP-P2Y11-PKA-CREB-BDNF-promoter-IV",
            "primary_locator": "PMID:9405388; PMID:18649393; PMID:29887330; PMCID:PMC6020856; PMID:9390517; PMCID:PMC7044735",
            "evidence_summary": (
                "Primary astrocyte studies support extracellular ATP/P2Y signaling, PKA involvement, CREB "
                "phosphorylation or dependence, and BDNF promoter IV/exon IV transcript output. The route "
                "retains the ATP-P2RY11 receptor identity and the PKA-CREB transcriptional layer while "
                "composing evidence from rat cortical and mouse hippocampal astrocyte systems."
            ),
            "limitations": (
                "The ATP-P2RY11 receptor and PKA/CREB/output observations come from complementary primary "
                "experiments, and P2Y subtype assignment is pharmacologically bounded. No single source is "
                "asserted to demonstrate every handoff, and no causal graph edge, SCI transfer, or confidence "
                "score is inferred."
            ),
            "cell_type_context": "rat cortical astrocytes, RCG-12 astrocytes, and mouse hippocampal astrocytes",
            "assay_or_perturbation": "ATP or P2Y agonist stimulation; P2Y11 antagonist; PKA inhibition; dominant-negative CREB; BDNF promoter IV reporter; BDNF exon IV and Bdnf mRNA assays",
        },
    ]

    rows: list[dict[str, str]] = []
    for spec in specs:
        required = [
            spec["ligand_node_id"], spec["receptor_node_id"], spec["relay_node_id"], spec["tf_node_id"]
        ]
        missing = [node_id for node_id in required if node_id not in nodes]
        if missing:
            raise ValueError(f"{spec['expansion_id']}: missing nodes {missing}")
        lr = edges.get(spec["lr_edge_id"])
        if not lr or (lr["source_node_id"], lr["target_node_id"]) != (
            spec["ligand_node_id"], spec["receptor_node_id"]
        ):
            raise ValueError(f"{spec['expansion_id']}: ligand-receptor edge endpoints do not match")
        rows.append(
            {
                "expansion_id": spec["expansion_id"],
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": spec["path_expression"],
                "route_tier": spec["route_tier"],
                "known_layers": spec["known_layers"],
                "missing_layers": spec["missing_layers"],
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
                "tf_target_edge_id": spec.get("tf_target_edge_id", ""),
                "target_gene_node_id": spec["target_node_id"],
                "target_gene_label": spec["target_label"],
                "target_output_form_id": "",
                "output_node_id": spec["output_node_id"],
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression" if spec["target_node_id"] else "primary_composed_downstream_output",
                "evidence_ids": unique_join(
                    lr.get("evidence_ids", ""),
                    edges.get(spec.get("tf_target_edge_id", ""), {}).get("evidence_ids", ""),
                    spec["primary_locator"],
                ),
                "source_chain_id": spec["expansion_id"],
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    "graph_linked_route_source;manual_primary_route_expansion;primary_layer_linked;"
                    "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
                    + (
                        "tf_to_target_edge_asserted_as_graph_edge;"
                        if spec.get("tf_target_edge_id")
                        else ("tf_to_target_edge_not_asserted;" if spec["target_node_id"] else "")
                    )
                    + "end_to_end_chain_not_asserted_by_single_source;evidence_route_only"
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression" if spec["target_node_id"] else "gene_expression_or_transcription",
                "primary_locator": spec["primary_locator"],
                "citation_note": "Primary literature supports the downstream signaling and expression layers; component handoffs remain explicitly bounded.",
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": "human; rat",
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular kinase relay; nuclear transcriptional/output layer",
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
