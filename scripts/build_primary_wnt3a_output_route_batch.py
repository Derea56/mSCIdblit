#!/usr/bin/env python3
"""Build bounded WNT3A receptor/output route annotations.

The source graph already contains the WNT3A--FZD8:LRP6 ligand/receptor edge,
WNT3A target-gene readouts, and a canonical LRP6 signalosome node.  Primary
WNT3A stimulation studies support the receptor-proximal and downstream
readouts, but the exported graph does not contain every handoff between those
layers.  These rows therefore remain evidence-only route annotations with the
missing links explicit.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


LR_EDGE_ID = "M21B-E000155"
LIGAND_ID = "NODE11857"
RECEPTOR_ID = "NODE03895"
SIGNALOSOME_ID = "NODE06555"
TARGETS = (
    ("M21B-E008927", "MYC"),
    ("M21B-E008928", "CCND1"),
    ("M21B-E008929", "CDKN1A"),
    ("M21B-E008930", "TFRC"),
    ("M21B-E008931", "PLF1"),
    ("M21B-E008932", "RAMP3"),
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def base_row() -> dict[str, str]:
    return {
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "ligand_node_id": LIGAND_ID,
        "ligand_label": "WNT3A",
        "ligand_receptor_edge_id": LR_EDGE_ID,
        "receptor_node_id": RECEPTOR_ID,
        "receptor_label": "FZD8:LRP6 receptor complex",
        "receptor_intracellular_edge_id": "",
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": "",
        "transcription_factor_label": "",
        "target_output_form_id": "",
        "output_form_id": "",
        "bridge_id": "",
        "input_evidence_type": "primary_literature_route_expansion",
        "source_evidence_record_id": "",
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "curation_status": "curated_primary_route",
        "species_context": "mouse; human receptor-reconstitution comparator where stated",
        "cell_type_context": "C57MG mammary epithelial cells and complementary WNT3A-responsive cell systems",
        "compartment_context": "extracellular WNT3A; plasma-membrane FZD8/LRP6; intracellular beta-catenin pathway; nuclear transcriptional readout",
        "injury_context": "no SCI transfer inferred; primary WNT3A signaling systems only",
        "context_scope": "composite primary evidence; receptor and downstream contexts remain bounded",
        "assay_or_perturbation": "purified or conditioned-medium WNT3A stimulation, receptor-proximal phosphorylation or stabilization readouts, reporter assays, and target-gene expression time courses",
        "effect_polarity": "activating",
        "source_scope": "composite_primary_evidence",
    }


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    required_nodes = {LIGAND_ID, RECEPTOR_ID, SIGNALOSOME_ID}
    required_nodes.update(edges[edge_id]["target_node_id"] for edge_id, _ in TARGETS)
    missing_nodes = sorted(required_nodes - nodes.keys())
    if missing_nodes:
        raise ValueError(f"WNT3A route requires missing nodes: {missing_nodes}")
    for edge_id in [LR_EDGE_ID, *(edge_id for edge_id, _ in TARGETS)]:
        if edge_id not in edges:
            raise ValueError(f"WNT3A route requires missing edge: {edge_id}")
    if (edges[LR_EDGE_ID]["source_node_id"], edges[LR_EDGE_ID]["target_node_id"]) != (LIGAND_ID, RECEPTOR_ID):
        raise ValueError("Unexpected WNT3A ligand/receptor endpoints")

    rows: list[dict[str, str]] = []
    common_linkage = (
        "graph_linked_route_source;manual_primary_wnt3a_route;"
        "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
        "tf_to_target_edge_not_asserted;evidence_route_only"
    )
    locators = "PMID:31235524; PMID:19353769; PMID:20093360"
    for edge_id, target_slug in TARGETS:
        target = nodes[edges[edge_id]["target_node_id"]]
        row = base_row()
        row.update(
            {
                "expansion_id": f"M21B-LITEXP-WNT3A-{target_slug}-OUTPUT",
                "path_expression": "ligand>receptor>????>????>target_gene_expression",
                "route_tier": "ligand_receptor_target_missing_intracellular_and_tf",
                "known_layers": "ligand|receptor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_continuation|transcription_factor|intracellular_to_tf_edge",
                "intracellular_status": "not_asserted",
                "target_gene_node_id": target["node_id"],
                "target_gene_label": target["canonical_label"],
                "output_node_id": target["node_id"],
                "output_label": f"{target_slug} gene expression",
                "output_evidence_type": "primary_wnt3a_target_gene_expression",
                "pathway_name": f"WNT3A-FZD8-LRP6-{target_slug}",
                "tf_target_edge_id": "",
                "evidence_ids": f"{LR_EDGE_ID};{edge_id};PMID:31235524;PMID:19353769;PMID:20093360",
                "route_linkage_status": common_linkage,
                "primary_locator": locators,
                "citation_note": "Composite primary route annotation. WNT3A receptor binding and WNT3A-stimulated target-gene expression are supported by complementary primary studies; receptor-to-output and transcription-factor handoffs remain unasserted.",
                "evidence_summary": f"Primary WNT3A stimulation studies report {target_slug} expression in responsive cells, while separate primary receptor-complex work supports WNT3A binding to the FZD8/LRP6 extracellular complex. This row preserves the ligand/receptor/output evidence without inferring the missing intracellular or TF layers.",
                "limitations": "The target-gene time course does not by itself establish FZD8/LRP6 mediation or direct TCF/LEF binding. Preserve the C57MG and receptor-reconstitution contexts; no SCI transfer, causal traversal, or confidence score is inferred.",
                "output_class": "gene_expression_or_transcription",
            }
        )
        rows.append(row)

    row = base_row()
    row.update(
        {
            "expansion_id": "M21B-LITEXP-WNT3A-TCF-REPORTER",
            "path_expression": "ligand>receptor>intracellular>????>output",
            "route_tier": "ligand_receptor_intracellular_output_missing_tf",
            "known_layers": "ligand|receptor|intracellular_continuation|output",
            "missing_layers": "receptor_to_intracellular_edge|transcription_factor|intracellular_to_tf_edge",
            "intracellular_status": "source_supported",
            "intracellular_continuation_node_id": SIGNALOSOME_ID,
            "intracellular_continuation_label": nodes[SIGNALOSOME_ID]["canonical_label"],
            "output_node_id": "",
            "output_label": "TCF-dependent transcriptional reporter",
            "output_evidence_type": "primary_wnt3a_tcf_reporter_readout",
            "pathway_name": "WNT3A-FZD8-LRP6-signalosome-beta-catenin-TCF-output",
            "evidence_ids": f"{LR_EDGE_ID};M21B-E000052;PMID:31235524;PMID:20093360",
            "route_linkage_status": common_linkage,
            "primary_locator": "PMID:31235524; PMID:20093360",
            "citation_note": "Primary WNT3A stimulation study measured LRP6 phosphorylation, DVL2 mobility, beta-catenin stabilization, and TCF-dependent transcription. The receptor-to-signalosome and signalosome-to-specific-TF handoffs are not exported as direct graph edges.",
            "evidence_summary": "Purified WNT3A activates receptor-proximal LRP6/DVL and beta-catenin pathway readouts together with TCF-dependent transcriptional reporter activity in engineered cell systems.",
            "limitations": "The study provides a functional TCF reporter rather than a target-gene-specific TF occupancy result. Preserve the engineered-cell and pathway-reporter context; no direct receptor-to-signalosome edge, specific TCF/LEF identity, SCI transfer, causal traversal, or confidence score is inferred.",
            "output_class": "reporter_readout",
        }
    )
    rows.append(row)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = make_rows(args.bundle.resolve())
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "rows": len(rows)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
