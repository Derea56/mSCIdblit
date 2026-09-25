#!/usr/bin/env python3
"""Build primary-literature route overlays for additional canonical ligands.

These rows are evidence-layer compositions for mSCS route plausibility.  They
retain graph-linked ligand/receptor identities and source-supported downstream
layers without asserting causal graph edges or confidence scores.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "expansion_id": "M21B-LITEXP-CXCL12-CXCR4-AKT-NFKB-SHH",
        "ligand_node_id": "NODE02639",
        "lr_edge_id": "M21B-E000158",
        "relay_node_id": "NODE08995",
        "tf_node_id": "NODE07984",
        "pathway_name": "CXCL12-CXCR4-PI3K-AKT-ERK-NF-kB-SHH",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
        "output_label": "SHH expression",
        "primary_locator": "PMID:22995914",
        "evidence_ids": "M21B-E000158;M21B-EVID-000101",
        "evidence_summary": (
            "A primary pancreatic-cancer study reports CXCL12-induced SHH up-regulation through CXCR4, "
            "with downstream Akt and ERK activation and NF-kB nuclear accumulation after I-kB-alpha "
            "phosphorylation and destabilization. The route retains PI3K-AKT1 as the graph-linked "
            "intracellular continuation and NF-kB as the transcriptional family layer."
        ),
        "limitations": (
            "The study uses pancreatic-cancer cells and establishes a functional CXCR4-to-SHH output, "
            "not an uninterrupted molecular chain for the normalized graph. Receptor-to-relay, relay-to-TF, "
            "and TF-to-output handoffs remain evidence-layer composition; no SCI transfer is inferred."
        ),
        "species_context": "human; mouse comparator",
        "cell_type_context": "human pancreatic-cancer cells and mouse pancreatic-cancer comparator cells",
        "assay_or_perturbation": "CXCL12 stimulation; CXCR4 antagonist or knockdown; Akt/ERK inhibition; NF-kB and SHH expression assays",
        "effect_polarity": "activating",
    },
    {
        "expansion_id": "M21B-LITEXP-CXCL12-CXCR4-JAK2-STAT3-survival",
        "ligand_node_id": "NODE02639",
        "lr_edge_id": "M21B-E000158",
        "relay_node_id": "NODE06026",
        "tf_node_id": "NODE10726",
        "pathway_name": "CXCL12-CXCR4-JAK2-STAT3-anti-apoptotic-output",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
        "output_label": "cisplatin-resistance and anti-apoptotic response",
        "primary_locator": "PMID:28721072",
        "evidence_ids": "M21B-E000158;M21B-EVID-000101",
        "evidence_summary": (
            "A primary human lung-cancer-cell study reports that CXCL12 stimulation through CXCR4 increases "
            "STAT3 phosphorylation through JAK2 and reduces cisplatin-induced apoptosis; CXCR4 and JAK2 "
            "antagonists suppress the response. The route maps JAK2 and STAT3 onto the existing graph layers "
            "while preserving the measured survival output."
        ),
        "limitations": (
            "The study uses A549 lung adenocarcinoma cells and measures pathway activation and apoptosis rather "
            "than a defined STAT3 target-gene promoter. The JAK2/STAT3 handoffs remain source-supported route "
            "layers rather than newly asserted graph edges or SCI-specific predictions."
        ),
        "species_context": "human",
        "cell_type_context": "human A549 lung adenocarcinoma cells",
        "assay_or_perturbation": "CXCL12 stimulation; CXCR4 antagonist AMD3100; JAK2 antagonist AG490; cisplatin; phospho-STAT3 and apoptosis assays",
        "effect_polarity": "activating",
    },
    {
        "expansion_id": "M21B-LITEXP-GAS6-AXL-PI3K-AKT-NFKB-BCL2L1",
        "ligand_node_id": "NODE03982",
        "lr_edge_id": "M21B-E000166",
        "relay_node_id": "NODE08995",
        "tf_node_id": "NODE07984",
        "pathway_name": "GAS6-AXL-PI3K-AKT-NF-kB-BCL2L1-output",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
        "output_label": "Bcl-xL/BCL2L1 survival-protein expression",
        "primary_locator": "PMID:11425860",
        "evidence_ids": "M21B-E000166;M21B-EVID-000109",
        "evidence_summary": (
            "A primary NIH 3T3 study reports that Gas6-Axl activates PI3K and Akt, induces nuclear NF-kB "
            "binding and NF-kB-responsive promoter activity, and increases Bcl-xL protein; dominant-negative "
            "Akt or I-kB inhibition blocks the response. The route preserves PI3K-AKT1 and NF-kB as the "
            "intracellular and transcriptional layers."
        ),
        "limitations": (
            "The study uses serum-starved NIH 3T3 fibroblasts and reports Bcl-xL protein rather than a "
            "promoter-resolved BCL2L1 target-gene experiment. The route is evidence-only and does not infer "
            "a universal AXL-to-NF-kB topology or SCI transfer."
        ),
        "species_context": "mouse fibroblast model",
        "cell_type_context": "NIH 3T3 fibroblasts",
        "assay_or_perturbation": "Gas6 stimulation; PI3K/Akt inhibition; dominant-negative Akt and I-kB; NF-kB DNA-binding and reporter assays; Bcl-xL protein measurement",
        "effect_polarity": "activating",
    },
    {
        "expansion_id": "M21B-LITEXP-SPP1-CD44-NFKB-IL6",
        "ligand_node_id": "NODE10627",
        "lr_edge_id": "M23B-E000265",
        "relay_node_id": "NODE07995",
        "tf_node_id": "NODE07984",
        "pathway_name": "SPP1-CD44-NF-kB-p65-IL6-output-SCI",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
        "output_label": "IL-6 protein secretion from microglia",
        "primary_locator": "PMID:40797111",
        "evidence_ids": "M23B-E000265;M21B-E010724;M21B-E010725",
        "evidence_summary": (
            "A primary mouse spinal-cord-injury study reports that recombinant SPP1 increases NF-kB/p65 "
            "phosphorylation and IL-6 protein output in BV2 microglia. The graph-linked SPP1-CD44 pair is "
            "retained as the receptor context and NF-kB/p65 phosphorylation as the measured intracellular "
            "continuation before the NF-kB transcriptional-family layer."
        ),
        "limitations": (
            "The source establishes measured p65 phosphorylation and IL-6 protein secretion, but does not "
            "isolate CD44 necessity or establish an IL6 transcript/promoter step. The route therefore remains "
            "a bounded SCI evidence route without a causal edge or confidence score."
        ),
        "species_context": "mouse",
        "cell_type_context": "BV2 mouse microglia and female C57BL/6 T10 crush spinal-cord-injury model",
        "assay_or_perturbation": "recombinant mouse SPP1; BV2 microglia; p65/phospho-p65 immunoblot; IL-6 ELISA; spinal-cord-injury tissue context",
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
                    f"manual_primary_{spec['expansion_id'].removeprefix('M21B-LITEXP-').lower()}_route;"
                    "graph_linked_route_source;primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
                    "intracellular_to_tf_edge_not_asserted;target_gene_expression_unresolved;evidence_route_only"
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
                    "Primary-evidence route overlay; supported layers are retained for mSCS plausibility, while "
                    "unresolved handoffs remain explicit and no graph edge, causal assertion, or confidence score is created."
                ),
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular signaling; nuclear or functional output context",
                "injury_context": "primary model context; SCI transfer is not inferred",
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
