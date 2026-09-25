#!/usr/bin/env python3
"""Build primary-literature route overlays for CX3CL1 and FN1."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "expansion_id": "M21B-LITEXP-CX3CL1-CX3CR1-RAFMEKERK-NFKB-MMP3",
        "ligand_node_id": "NODE02606",
        "lr_edge_id": "M21B-E000256",
        "relay_node_id": "NODE09609",
        "tf_node_id": "NODE07984",
        "target_gene_node_id": "NODE07457",
        "pathway_name": "CX3CL1-CX3CR1-c-Raf-MEK-ERK-NF-kB-MMP3",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "MMP-3/MMP3 production",
        "primary_locator": "PMID:29268768",
        "evidence_ids": "M21B-E000256;M21B-EVID-000199",
        "evidence_summary": (
            "A primary osteoarthritis-synovial-fibroblast study reports that CX3CL1 signals through CX3CR1 "
            "and the c-Raf/MEK/ERK pathway to activate NF-kB, with p65 promoter occupancy and increased MMP3 "
            "transcript and MMP-3 production. Inhibiting CX3CR1, c-Raf, MEK, or ERK attenuated the response. "
            "The route retains the graph-linked CX3CL1-CX3CR1 pair, the RAF-MEK-ERK relay, NF-kB, and the "
            "existing MMP3 gene node."
        ),
        "limitations": (
            "The study uses osteoarthritis synovial fibroblasts rather than an SCI model. The normalized graph "
            "does not assert each c-Raf-to-MEK, MEK-to-ERK, ERK-to-NF-kB, or NF-kB-to-MMP3 edge; those handoffs "
            "remain evidence-layer composition and no confidence score is assigned."
        ),
        "species_context": "human",
        "cell_type_context": "human osteoarthritis synovial fibroblasts",
        "assay_or_perturbation": "CX3CL1 stimulation; CX3CR1 siRNA; c-Raf, MEK, and ERK inhibitors or mutants; NF-kB luciferase, p65 phosphorylation/ChIP, MMP3 qPCR, and MMP-3 ELISA assays",
        "effect_polarity": "activating",
    },
    {
        "expansion_id": "M23B-LITEXP-FN1-ITGA5ITGB1-ILK-PI3KAPKT-AP1",
        "ligand_node_id": "NODE03756",
        "lr_edge_id": "M23B-E000143",
        "relay_node_id": "NODE05960",
        "tf_node_id": "NODE00609",
        "pathway_name": "FN1-ITGA5-ITGB1-ILK-PI3K-AKT-AP1",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
        "output_label": "AP-1 transcriptional reporter activity",
        "primary_locator": "PMID:10523630",
        "evidence_ids": "M23B-E000143;M23B-EVID-000211",
        "evidence_summary": (
            "A primary cell-adhesion study reports that fibronectin interaction stimulates integrin-linked "
            "kinase, activates protein kinase B and inhibits GSK-3 through a PI3K-dependent branch, and induces "
            "AP-1 reporter activity. The route retains the graph-linked FN1-ITGA5:ITGB1 pair, the existing "
            "ITGB1-ILK signaling component, and AP-1 as the transcriptional readout layer."
        ),
        "limitations": (
            "The study measures matrix adhesion and AP-1 reporter activity in HEK-293 cells rather than a "
            "secreted-ligand or SCI context. The receptor-to-ILK and ILK-to-AP-1 handoffs remain evidence-layer "
            "composition; the route does not assert a target gene or a universal FN1 topology."
        ),
        "species_context": "human",
        "cell_type_context": "human HEK-293 cells with fibronectin-adhesion systems",
        "assay_or_perturbation": "fibronectin adhesion; ILK and GSK-3 manipulation; PI3K inhibition; AP-1 luciferase reporter assay",
        "effect_polarity": "activating",
    },
)


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
    rows: list[dict[str, str]] = []
    for spec in SPECS:
        lr = edges[spec["lr_edge_id"]]
        ligand = nodes[spec["ligand_node_id"]]
        receptor = nodes[lr["target_node_id"]]
        relay = nodes[spec["relay_node_id"]]
        tf = nodes[spec["tf_node_id"]]
        target_gene_id = spec.get("target_gene_node_id", "")
        target_gene = nodes[target_gene_id] if target_gene_id else {}
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
                "target_gene_node_id": target_gene_id,
                "target_gene_label": target_gene.get("canonical_label", ""),
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression" if target_gene_id else "primary_functional_output",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["evidence_ids"], spec["primary_locator"]),
                "source_chain_id": spec["expansion_id"],
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    f"manual_primary_{spec['expansion_id'].removeprefix('M21B-LITEXP-').removeprefix('M23B-LITEXP-').lower()}_route;"
                    "graph_linked_route_source;primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
                    "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
                    "target_gene_expression_unresolved;evidence_route_only"
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression" if target_gene_id else "reporter_readout",
                "primary_locator": spec["primary_locator"],
                "citation_note": (
                    "Primary-evidence route overlay; supported layers are retained for mSCS plausibility, while "
                    "unresolved handoffs remain explicit and no graph edge, causal assertion, or confidence score is created."
                ),
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular or matrix ligand; cell-surface receptor; intracellular signaling; nuclear or functional output context",
                "injury_context": "primary model context; SCI transfer is not inferred",
                "context_scope": "composite_primary_evidence; route layers retain source-specific models",
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
