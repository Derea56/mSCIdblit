#!/usr/bin/env python3
"""Build bounded IL-21/JAK/STAT3 evidence routes from primary studies."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


TARGETS = [
    {
        "name": "IL21",
        "target_node_id": "NODE05415",
        "target_label": "IL21 gene",
        "tf_target_edge_id": "M21B-E008223",
        "locators": "PMID:18209077; PMID:17884812; PMCID:PMC2323680; PMID:11418623",
        "summary": "Primary evidence supports IL-21 receptor signaling, STAT3 activation, STAT3 recruitment to the IL21 promoter, and an IL-21 autocrine transcriptional loop.",
        "limitation": "The receptor/JAK/STAT3 and promoter-output observations are source-linked layers from human and mouse T-cell studies; the exact JAK1/JAK3-to-STAT3 molecular handoff is not asserted as a single direct graph edge, and no SCI receiver-cell transfer is inferred.",
    },
    {
        "name": "IL17A",
        "target_node_id": "NODE05331",
        "target_label": "IL17A gene",
        "tf_target_edge_id": "M21B-E008226",
        "locators": "PMID:17884812; PMCID:PMC2323680; PMID:20064451; PMCID:PMC3272079",
        "summary": "Primary evidence supports IL-21/STAT3-dependent Th17 programming, STAT3-linked IL17A output, and IL-21-induced IL-17 production.",
        "limitation": "The cited Th17 studies establish IL-21/STAT3 dependence and IL-17 output in a differentiation context; the exact JAK1/JAK3-to-STAT3 handoff and the direct STAT3-to-IL17A promoter mechanism are retained as bounded route evidence rather than asserted as one end-to-end graph edge.",
    },
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(values: list[str]) -> str:
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
    required_nodes = {"NODE05414", "NODE05419", "NODE06024", "NODE10726"}
    missing_nodes = sorted(required_nodes - nodes.keys())
    if missing_nodes:
        raise ValueError(f"IL-21 route requires missing nodes: {missing_nodes}")
    lr_edge_id = "M21B-E000248"
    relay_edge_id = "M21B-E000555"
    lr_edge = edges[lr_edge_id]
    relay_edge = edges[relay_edge_id]
    if (lr_edge["source_node_id"], lr_edge["target_node_id"]) != ("NODE05414", "NODE05419"):
        raise ValueError("Unexpected IL-21 receptor endpoints")
    if (relay_edge["source_node_id"], relay_edge["target_node_id"]) != ("NODE05419", "NODE06024"):
        raise ValueError("Unexpected IL-21 receptor/JAK endpoints")

    rows: list[dict[str, str]] = []
    for index, target in enumerate(TARGETS, start=1):
        if target["target_node_id"] not in nodes or target["tf_target_edge_id"] not in edges:
            raise ValueError(f"IL-21 route target is missing: {target}")
        tf_edge = edges[target["tf_target_edge_id"]]
        if (tf_edge["source_node_id"], tf_edge["target_node_id"]) != ("NODE10726", target["target_node_id"]):
            raise ValueError(f"Unexpected STAT3 target endpoints for {target['name']}")
        expansion_id = f"M21B-LITEXP-IL21-{index:03d}"
        evidence_ids = unique_join(
            [
                lr_edge_id,
                relay_edge_id,
                target["tf_target_edge_id"],
                "M21B-EVID-000191",
                "M21B-EVID-000498",
                "M21B-EVID-000499",
                target["locators"],
            ]
        )
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "intracellular_to_tf_edge",
                "intracellular_status": "source_supported",
                "ligand_node_id": "NODE05414",
                "ligand_label": "IL21",
                "ligand_receptor_edge_id": lr_edge_id,
                "receptor_node_id": "NODE05419",
                "receptor_label": "IL21R:IL2RG receptor complex",
                "receptor_intracellular_edge_id": relay_edge_id,
                "intracellular_continuation_node_id": "NODE06024",
                "intracellular_continuation_label": "JAK1/JAK3",
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": "NODE10726",
                "transcription_factor_label": "STAT3",
                "tf_target_edge_id": target["tf_target_edge_id"],
                "target_gene_node_id": target["target_node_id"],
                "target_gene_label": target["target_label"],
                "output_node_id": target["target_node_id"],
                "output_label": f"{target['target_label']} expression",
                "pathway_name": f"IL21-IL21R-JAK1-JAK3-STAT3-{target['name']}",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_il21_stat3_target_gene_evidence",
                "evidence_ids": evidence_ids,
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": "graph_linked_route_source;manual_primary_il21_route;receptor_proximal_and_tf_output_evidence_composed;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_graph_evidence;evidence_route_only",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": target["locators"],
                "citation_note": "Composite primary route annotation: IL-21/IL-21R:IL2RG engagement, JAK1/JAK3 receptor-proximal signaling, STAT3 activation, and target-gene output are retained as separate source-linked layers.",
                "evidence_summary": target["summary"],
                "limitations": target["limitation"],
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse as stated in primary model/assay",
                "cell_type_context": "Human peripheral or intestinal T lymphocytes and mouse CD4 T-cell/Th17 or Tfh models with IL-21 stimulation and STAT3-dependent transcriptional measurements.",
                "compartment_context": "extracellular cytokine; plasma membrane receptor complex; cytoplasm; nucleus; target-gene regulatory locus",
                "injury_context": "no SCI transfer inferred; primary lymphocyte model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "IL-21 stimulation and receptor signaling assays, STAT3 phosphorylation or inhibition/knockdown, promoter or chromatin-binding measurements, and target-gene expression/output assays.",
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
    args.output.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
