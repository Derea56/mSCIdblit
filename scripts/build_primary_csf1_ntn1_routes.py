#!/usr/bin/env python3
"""Build primary-literature CSF1 and Ntn1 intracellular route overlays."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = [
    {
        "expansion_id": "M21B-LITEXP-CSF1-CSF1R-MEK-ERK-AKT-MYELOID",
        "ligand_node_id": "NODE02503",
        "lr_edge_id": "M21B-E000120",
        "relay_node_id": "NODE06926",
        "pathway_name": "CSF1-CSF1R-PI3K-AKT-RAS-MEK-ERK-myelopoiesis",
        "primary_locator": "PMID:10958675",
        "output_label": "CSF-1-stimulated MEK/ERK and PI3K/Akt activity in myeloid progenitors",
        "evidence_ids": "M21B-E000120;M21B-EVID-000063;M21B-E000112;M21B-E000113",
        "evidence_summary": (
            "A primary myeloid-progenitor study shows that CSF-1 stimulation activates ERK through Ras and "
            "PI3-kinase-dependent mechanisms, with Akt activity used as a PI3-kinase readout. CSF-1 also activates "
            "Fyn and Lyn, and SFK inhibition prevents Akt activation in the receptor mutant model. The route retains "
            "the graph-linked CSF1-CSF1R pair and MEK/ERK intracellular continuation."
        ),
        "limitations": (
            "The study uses CSF-1R-expressing myeloid progenitor cells rather than an SCI receiver state and does "
            "not establish a transcription factor or target gene. The parallel PI3K/Akt and Ras/MEK/ERK branches are "
            "represented as one intracellular evidence route; no causal graph edge or confidence score is created."
        ),
        "species_context": "mouse myeloid progenitor cell line",
        "cell_type_context": "32D myeloid progenitors expressing wild-type or PI3K-binding-site mutant CSF-1R",
        "compartment_context": "extracellular CSF-1; cell-surface CSF-1R; PI3K/Akt, SFK, Ras, MEK/ERK intracellular activity",
        "injury_context": "myeloid comparator; SCI transfer is not inferred",
        "assay_or_perturbation": "CSF-1 stimulation; PI3K, SFK and Ras perturbation; ERK/MEK, Akt, Fyn/Lyn and Gab2 phosphorylation or kinase assays",
    },
    {
        "expansion_id": "M21B-LITEXP-NTN1-DCC-FAK-SRC-AXON-ATTRACTION-Ntn1",
        "ligand_node_id": "NODE08406",
        "lr_edge_id": "M20B-E002232",
        "relay_node_id": "NODE03489",
        "pathway_name": "Ntn1-Dcc-FAK-Src-axon-attraction",
        "primary_locator": "PMID:15494734",
        "output_label": "netrin-induced axon attraction and outgrowth",
        "evidence_ids": "M20B-E002232;M20B-EVID-002232",
        "evidence_summary": (
            "A primary neuronal study reports that netrin activates FAK and Src downstream of DCC, with DCC "
            "interactions with both kinases and inhibition of Src reducing netrin-induced axon attraction and "
            "outgrowth. The route retains the exact graph-linked Ntn1-Dcc pair and FAK/PTK2 intracellular relay."
        ),
        "limitations": (
            "The study uses neuronal axon-guidance models rather than an SCI receiver state and does not establish a "
            "transcription factor or target gene. The DCC-to-FAK/Src handoff is retained as source-supported "
            "intracellular evidence; no causal graph edge or confidence score is created."
        ),
        "species_context": "rat neuronal cultures",
        "cell_type_context": "primary neurons and neuronal axon-guidance assays",
        "compartment_context": "extracellular netrin-1; DCC receptor; FAK/Src intracellular signaling; axon-growth output",
        "injury_context": "developmental neuronal comparator; SCI transfer is not inferred",
        "assay_or_perturbation": "netrin stimulation; DCC intracellular-domain interaction assays; FAK/Src inhibition; axon attraction and outgrowth assays",
    },
    {
        "expansion_id": "M21B-LITEXP-NTN1-DCC-FAK-SRC-AXON-ATTRACTION-NTN1",
        "ligand_node_id": "NODE08407",
        "lr_edge_id": "M21B-E000191",
        "relay_node_id": "NODE03489",
        "pathway_name": "NTN1-DCC-FAK-Src-axon-attraction",
        "primary_locator": "PMID:15494734",
        "output_label": "netrin-induced axon attraction and outgrowth",
        "evidence_ids": "M21B-E000191;M21B-EVID-000134",
        "evidence_summary": (
            "A primary neuronal study reports that netrin activates FAK and Src downstream of DCC, with DCC "
            "interactions with both kinases and inhibition of Src reducing netrin-induced axon attraction and "
            "outgrowth. The route retains the exact graph-linked NTN1/netrin-1-DCC pair and FAK/PTK2 intracellular "
            "relay."
        ),
        "limitations": (
            "The study uses neuronal axon-guidance models rather than an SCI receiver state and does not establish a "
            "transcription factor or target gene. The DCC-to-FAK/Src handoff is retained as source-supported "
            "intracellular evidence; no causal graph edge or confidence score is created."
        ),
        "species_context": "rat neuronal cultures",
        "cell_type_context": "primary neurons and neuronal axon-guidance assays",
        "compartment_context": "extracellular netrin-1; DCC receptor; FAK/Src intracellular signaling; axon-growth output",
        "injury_context": "developmental neuronal comparator; SCI transfer is not inferred",
        "assay_or_perturbation": "netrin stimulation; DCC intracellular-domain interaction assays; FAK/Src inhibition; axon attraction and outgrowth assays",
    },
]


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


def make_row(bundle: Path, spec: dict[str, str]) -> dict[str, str]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    lr = edges[spec["lr_edge_id"]]
    ligand = nodes[spec["ligand_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[spec["relay_node_id"]]
    return {
        "expansion_id": spec["expansion_id"],
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>output",
        "route_tier": "ligand_receptor_intracellular_output_missing_tf",
        "known_layers": "ligand|receptor|intracellular_continuation|output",
        "missing_layers": "receptor_to_intracellular_edge|transcription_factor|target_gene_expression",
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
        "transcription_factor_node_id": "",
        "transcription_factor_label": "",
        "tf_target_edge_id": "",
        "target_gene_node_id": "",
        "target_gene_label": "",
        "target_output_form_id": "",
        "output_node_id": "",
        "output_label": spec["output_label"],
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": spec["pathway_name"],
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_functional_output",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["evidence_ids"], spec["primary_locator"]),
        "source_chain_id": spec["expansion_id"],
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_route;graph_linked_route_source;primary_layer_linked;"
            "receptor_to_intracellular_edge_not_asserted;transcription_factor_unresolved;"
            "target_gene_expression_unresolved;evidence_route_only"
        ),
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "output_class": "generic_functional_readout",
        "primary_locator": spec["primary_locator"],
        "citation_note": (
            "Primary-evidence route overlay; supported layers are retained for mSCS plausibility, while unresolved "
            "handoffs remain explicit and no graph edge, causal assertion, or confidence score is created."
        ),
        "evidence_summary": spec["evidence_summary"],
        "limitations": spec["limitations"],
        "curation_status": "curated_primary_route",
        "species_context": spec["species_context"],
        "cell_type_context": spec["cell_type_context"],
        "compartment_context": spec["compartment_context"],
        "injury_context": spec["injury_context"],
        "context_scope": "composite_primary_evidence; route layers retain source-specific models",
        "assay_or_perturbation": spec["assay_or_perturbation"],
        "effect_polarity": "activating",
        "source_scope": "composite_primary_evidence",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    bundle = args.bundle.resolve()
    rows = [make_row(bundle, spec) for spec in ROUTES]
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output.resolve())}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
