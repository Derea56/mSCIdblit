#!/usr/bin/env python3
"""Build primary-literature route overlays for IL-10 and TNFR-family ligands.

The overlays preserve primary-evidence route layers for mSCS plausibility
analysis. They do not create causal graph edges, confidence scores, or graph
traversal permissions for handoffs that remain unresolved.
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
            "expansion_id": "M21B-LITEXP-IL10-IL10R-JAK1TYK2-STAT3-SOCS3",
            "ligand_node_id": "NODE05283",
            "ligand_label": "IL10/interleukin-10",
            "lr_edge_id": "M21B-E000272",
            "receptor_node_id": "NODE05289",
            "receptor_label": "IL10RA:IL10RB receptor complex",
            "relay_node_id": "NODE06023",
            "relay_label": "JAK1/TYK2",
            "tf_node_id": "NODE10726",
            "tf_label": "STAT3",
            "target_node_id": "NODE10509",
            "target_label": "SOCS3 gene",
            "tf_target_edge_id": "M21B-E008279",
            "pathway_name": "IL10-IL10R-JAK1-TYK2-STAT3-SOCS3",
            "primary_locator": "PMID:7543512; PMID:11034314",
            "evidence_summary": (
                "Primary studies report IL-10-dependent phosphorylation of JAK1 and TYK2 and STAT3, followed by "
                "STAT3-associated induction of SOCS3 in human monocytes/T cells and mouse liver. The route retains "
                "the graph-linked IL10 receptor complex and the graph-linked STAT3-to-SOCS3 target relationship."
            ),
            "limitations": (
                "The cited studies use distinct human and mouse systems and do not establish one uninterrupted "
                "IL10-to-SOCS3 experiment with every receptor-to-kinase handoff. The IL10RA:IL10RB-to-JAK1/TYK2 "
                "and JAK1/TYK2-to-STAT3 transitions remain evidence-layer compositions; no causal edge or SCI "
                "transfer is inferred."
            ),
            "cell_type_context": "human monocytes and T cells; mouse liver",
            "assay_or_perturbation": "IL-10 stimulation or administration; JAK1/TYK2 and STAT phosphorylation; SOCS2/SOCS3 transcript assays; reporter inhibition by SOCS3",
            "species_context": "human; mouse",
        },
        {
            "expansion_id": "M21B-LITEXP-4-1BBL-4-1BB-TRAF2-NFKB-IL2",
            "ligand_node_id": "NODE00029",
            "ligand_label": "4-1BBL/TNFSF9",
            "lr_edge_id": "M21B-E000454",
            "receptor_node_id": "NODE00025",
            "receptor_label": "4-1BB/TNFRSF9",
            "receptor_intracellular_edge_id": "M21B-E001795",
            "relay_node_id": "NODE11375",
            "relay_label": "TRAF2",
            "tf_node_id": "NODE07984",
            "tf_label": "NF-kB",
            "target_node_id": "",
            "target_label": "",
            "pathway_name": "4-1BBL-4-1BB-TRAF2-NF-kB-IL2-output",
            "primary_locator": "PMID:9464265; PMID:9607925",
            "evidence_summary": (
                "Primary studies report 4-1BB/4-1BBL-dependent recruitment of TRAF1/2/3, TRAF2-dependent NF-kB "
                "activation, and 4-1BBL-dependent IL-2 production in T cells. The graph-linked receptor-to-TRAF2 "
                "edge is retained while IL-2 is represented as a measured functional output."
            ),
            "limitations": (
                "The receptor/NF-kB study and the TRAF2-deficient T-cell/IL-2 study are complementary rather than "
                "one uninterrupted experiment. The TRAF2-to-NF-kB and NF-kB-to-IL-2 handoffs remain unasserted "
                "route evidence; the route does not claim a direct TF-target edge or SCI transfer."
            ),
            "cell_type_context": "human 293 cells and Jurkat cells; mouse resting T cells",
            "assay_or_perturbation": "4-1BB cross-linking or soluble 4-1BBL; TRAF interaction assays; dominant-negative TRAF2/NIK; TRAF2-deficient T cells; IL-2 production",
            "species_context": "human; mouse",
        },
        {
            "expansion_id": "M21B-LITEXP-OX40L-OX40-TRAF2-NFKB-SURVIVAL",
            "ligand_node_id": "NODE08627",
            "ligand_label": "OX40L/TNFSF4",
            "lr_edge_id": "M21B-E000453",
            "receptor_node_id": "NODE08625",
            "receptor_label": "OX40/TNFRSF4",
            "receptor_intracellular_edge_id": "M21B-E001791",
            "relay_node_id": "NODE11375",
            "relay_label": "TRAF2",
            "tf_node_id": "NODE07984",
            "tf_label": "NF-kB",
            "target_node_id": "",
            "target_label": "",
            "pathway_name": "OX40L-OX40-TRAF2-PKCtheta-NF-kB-effector-T-cell-survival",
            "primary_locator": "PMID:21282629; PMCID:PMC3041086",
            "evidence_summary": (
                "A primary T-cell study reports OX40 ligation by OX40L, assembly of an OX40 signalosome containing "
                "TRAF2 and PKCtheta-associated CBM/IKK components, and strong NF-kB activity that supports effector "
                "and memory T-cell survival. The graph-linked OX40-to-TRAF2 edge is retained."
            ),
            "limitations": (
                "The primary work resolves a receptor signalosome and NF-kB-dependent survival output but not a single "
                "linear biochemical sequence or a specific terminal target gene. PKCtheta/CBM components are described "
                "in the source but are not inserted as unsupported graph nodes in this route; no SCI transfer is inferred."
            ),
            "cell_type_context": "primary mouse effector and memory T cells",
            "assay_or_perturbation": "OX40L-expressing APC stimulation; OX40 immunoprecipitation; TRAF2/CARMA1/PKCtheta perturbation; NF-kB activity; effector-cell survival",
            "species_context": "mouse",
        },
        {
            "expansion_id": "M21B-LITEXP-GITRL-GITR-JNK-AP1-TREG",
            "ligand_node_id": "NODE04126",
            "ligand_label": "GITRL/TNFSF18",
            "lr_edge_id": "M21B-E000459",
            "receptor_node_id": "NODE04125",
            "receptor_label": "GITR/TNFRSF18",
            "receptor_intracellular_edge_id": "M21B-E003835",
            "relay_node_id": "NODE11375",
            "relay_label": "TRAF2→JNK/MAPK8",
            "tf_node_id": "NODE00609",
            "tf_label": "AP-1/c-Jun",
            "target_node_id": "",
            "target_label": "",
            "pathway_name": "GITRL-GITR-JNK-cJun-NF-kB-Treg-suppression-output",
            "primary_locator": "PMID:22461627; PMID:17602748",
            "evidence_summary": (
                "Primary studies report GITR-ligand stimulation-dependent JNK activation, c-Jun and NF-kB changes, "
                "and JNK-dependent loss of regulatory T-cell suppression; a separate primary macrophage study reports "
                "ERK-dependent NF-kB nuclear translocation and inflammatory output after GITRL stimulation. The route "
                "retains the graph-linked GITR-to-TRAF2 receptor-proximal component while representing the JNK/AP-1 "
                "branch as the downstream transcriptional layer."
            ),
            "limitations": (
                "The cited studies use distinct T-regulatory-cell and macrophage systems, and the macrophage paper also "
                "examines reverse signaling through GITRL. The route therefore preserves direction and model context "
                "explicitly but does not assert a single GITRL-to-AP-1 chain, target gene, or SCI transfer."
            ),
            "cell_type_context": "mouse natural regulatory T cells; human THP-1 and primary macrophages",
            "assay_or_perturbation": "GITRL stimulation; GITR-deficient or JNK-inhibited T cells; JNK/c-Jun/NF-kB immunoblotting; macrophage ERK inhibition; cytokine and MMP9 output",
            "species_context": "mouse; human",
        },
        {
            "expansion_id": "M21B-LITEXP-RANKL-RANK-TRAF6-TAK1-NFATC1-OSTEOCLAST",
            "ligand_node_id": "NODE09623",
            "ligand_label": "RANKL/TRANCE/TNFSF11",
            "lr_edge_id": "M21B-E000462",
            "receptor_node_id": "NODE09621",
            "receptor_label": "RANK/TNFRSF11A",
            "receptor_intracellular_edge_id": "M21B-E000478",
            "relay_node_id": "NODE11385",
            "relay_label": "TRAF6→TAK1/MAP3K7",
            "tf_node_id": "NODE00609",
            "tf_label": "AP-1/c-Jun",
            "target_node_id": "",
            "target_label": "",
            "pathway_name": "RANKL-RANK-TRAF6-TAK1-MAPK-NFATC1-osteoclastogenesis",
            "primary_locator": "PMID:11809792; PMID:19112497; PMID:24558484",
            "evidence_summary": (
                "Primary studies report RANKL-dependent formation of RANK/TRAF6/TAB2/TAK1 complexes, TAK1 activation, "
                "MAPK and IKK/NF-kB signaling, and AP-1 or NFATc1-associated osteoclast differentiation and resorption "
                "outputs. The graph-linked RANK-to-TRAF6 edge is retained and NFATc1 is used as the transcriptional "
                "effector layer without inventing a direct TRAF6-to-NFATC1 edge."
            ),
            "limitations": (
                "The studies use complementary 293, RAW264.7, fibroblast, and osteoclast models and perturb different "
                "TRAF6/TAK1/MAPK/NFATC1 steps. The exact TAK1/MAPK-to-NFATC1 handoff and terminal target gene remain "
                "unasserted in this route; no causal graph edge or SCI transfer is inferred."
            ),
            "cell_type_context": "human 293 cells; mouse RAW264.7 cells, fibroblasts, and bone-marrow macrophages",
            "assay_or_perturbation": "RANKL stimulation; RANK overexpression; dominant-negative TAK1/TAB2; TRAF6-deficient rescue; NF-kB/AP-1/NFATc1 assays; osteoclastogenesis and resorption assays",
            "species_context": "human; mouse",
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
        receptor_edge_id = spec.get("receptor_intracellular_edge_id", "")
        if receptor_edge_id:
            receptor_edge = edges.get(receptor_edge_id)
            if not receptor_edge or (receptor_edge["source_node_id"], receptor_edge["target_node_id"]) != (
                spec["receptor_node_id"], spec["relay_node_id"]
            ):
                raise ValueError(f"{spec['expansion_id']}: receptor-relay edge endpoints do not match")
        tf_edge_id = spec.get("tf_target_edge_id", "")
        if tf_edge_id:
            tf_edge = edges.get(tf_edge_id)
            if not tf_edge or (tf_edge["source_node_id"], tf_edge["target_node_id"]) != (
                spec["tf_node_id"], spec["target_node_id"]
            ):
                raise ValueError(f"{spec['expansion_id']}: TF-target edge endpoints do not match")
        has_target = bool(spec.get("target_node_id"))
        missing_layers = ["intracellular_to_tf_edge"]
        if not receptor_edge_id:
            missing_layers.insert(0, "receptor_to_intracellular_edge")
        if not has_target:
            missing_layers.append("target_gene_expression")
        route_linkage = (
            "graph_linked_route_source;manual_primary_route_expansion;primary_layer_linked;"
            + ("receptor_to_intracellular_edge_asserted_as_graph_edge;" if receptor_edge_id else "receptor_to_intracellular_edge_not_asserted;")
            + "intracellular_to_tf_edge_not_asserted;"
            + ("tf_to_target_edge_asserted_as_graph_edge;" if tf_edge_id else ("tf_to_target_edge_not_asserted;" if has_target else ""))
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
                "receptor_intracellular_edge_id": receptor_edge_id,
                "intracellular_continuation_node_id": spec["relay_node_id"],
                "intracellular_continuation_label": spec["relay_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": spec["tf_node_id"],
                "transcription_factor_label": spec["tf_label"],
                "tf_target_edge_id": tf_edge_id,
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
                "evidence_ids": unique_join(
                    lr.get("evidence_ids", ""),
                    edges.get(receptor_edge_id, {}).get("evidence_ids", ""),
                    edges.get(tf_edge_id, {}).get("evidence_ids", ""),
                    spec["primary_locator"],
                ),
                "source_chain_id": spec["expansion_id"],
                "source_evidence_record_id": "",
                "route_linkage_status": route_linkage,
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
                "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular adaptor/kinase relay; nuclear transcriptional/output layer",
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
