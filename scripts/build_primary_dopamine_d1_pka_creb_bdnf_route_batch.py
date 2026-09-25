#!/usr/bin/env python3
"""Build a primary-literature dopamine/D1/PKA/CREB/BDNF route overlay."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


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
    lr_edge_id = "M21B-E001438"
    tf_target_edge_id = "M22B-E000036"
    relay_node_id = "NODE09272"
    tf_node_id = "NODE02446"
    target_node_id = "NODE01191"
    lr = edges[lr_edge_id]
    tf_target = edges[tf_target_edge_id]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[relay_node_id]
    tf = nodes[tf_node_id]
    target = nodes[target_node_id]
    expansion_id = "M21B-LITEXP-DOPAMINED1PKACREB-BDNFIV-001"
    primary_locator = "PMID:28983964; PMID:15056290; PMCID:PMC54609; PMCID:PMC7044735"
    evidence_ids = unique_join(lr.get("evidence_ids", ""), tf_target.get("evidence_ids", ""), primary_locator)
    return [
        {
            "expansion_id": expansion_id,
            "source_queue_id": "",
            "route_status": "retained_evidence_route",
            "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
            "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge",
            "intracellular_status": "source_supported_composed",
            "ligand_node_id": lr["source_node_id"],
            "ligand_label": ligand["canonical_label"],
            "ligand_receptor_edge_id": lr_edge_id,
            "receptor_node_id": lr["target_node_id"],
            "receptor_label": receptor["canonical_label"],
            "receptor_intracellular_edge_id": "",
            "intracellular_continuation_node_id": relay_node_id,
            "intracellular_continuation_label": relay["canonical_label"],
            "intracellular_tf_edge_id": "",
            "transcription_factor_node_id": tf_node_id,
            "transcription_factor_label": tf["canonical_label"],
            "tf_target_edge_id": tf_target_edge_id,
            "target_gene_node_id": target_node_id,
            "target_gene_label": target["canonical_label"],
            "target_output_form_id": "",
            "output_node_id": target_node_id,
            "output_label": "BDNF promoter IV activity and BDNF exon IV mRNA expression",
            "output_form_id": "",
            "bridge_id": "",
            "pathway_name": "dopamine-DRD1-cAMP-PKA-CREB-BDNF-promoter-IV",
            "input_evidence_type": "primary_literature_route_expansion",
            "output_evidence_type": "primary_target_gene_expression",
            "evidence_ids": evidence_ids,
            "source_chain_id": expansion_id,
            "source_evidence_record_id": "",
            "route_linkage_status": (
                "manual_primary_dopamine_d1_pka_creb_bdnf_route;graph_linked_route_source;"
                "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
                "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_graph_linked;"
                "receptor_subtype_specificity_bounded;evidence_route_only"
            ),
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": "supports",
            "negative_evidence_status": "not_evaluated",
            "evidence_directness": "composite_primary_route",
            "output_class": "target_gene_expression",
            "primary_locator": primary_locator,
            "citation_note": (
                "Primary-evidence route overlay for dopamine/D1-like receptor/cAMP-PKA-CREB-associated BDNF promoter "
                "IV activity. The astrocyte study reports receptor cross-reactivity, so D1-specific attribution remains bounded."
            ),
            "evidence_summary": (
                "Primary studies support dopamine-induced BDNF exon IV transcription and CREB-dependent promoter regulation "
                "in cortical astrocytes, D1-like receptor Gs/adenylyl-cyclase signaling, and D1/cAMP/PKA/CREB-dependent "
                "transcriptional activation in primary striatal neurons. These observations compose a dopamine-D1-like "
                "receptor-to-PKA-to-CREB-to-BDNF promoter route while retaining receptor-subtype uncertainty."
            ),
            "limitations": (
                "The astrocyte output study identifies beta-adrenergic receptors as the main mediators and D1 receptors as "
                "a contributing component; it does not establish a D1-exclusive branch. The receptor-to-PKA and PKA-to-CREB "
                "handoffs are composed across systems, and the route does not infer SCI transfer, causal traversal or a "
                "database confidence score."
            ),
            "curation_status": "curated_primary_route",
            "species_context": "rat; human",
            "cell_type_context": "Rat cortical astrocytes, primary rat striatal neurons, and cloned receptor signaling systems",
            "compartment_context": "extracellular dopamine; plasma-membrane D1-like receptor; cAMP/PKA intracellular relay; nuclear CREB-associated BDNF promoter IV output",
            "injury_context": "no SCI transfer inferred; primary neural and astrocyte model contexts only",
            "context_scope": "composite_primary_evidence",
            "assay_or_perturbation": "dopamine and D1 agonism/antagonism; cAMP measurement; PKA inhibition; CREB phosphorylation; BDNF promoter and exon-specific transcript assays",
            "effect_polarity": "activating",
            "source_scope": "composite_primary_evidence",
        }
    ]


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
