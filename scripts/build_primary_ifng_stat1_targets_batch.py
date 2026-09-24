#!/usr/bin/env python3
"""Build primary-literature IFN-gamma/IFNGR/JAK1/STAT1 target routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "IFNG-IFNGR-JAK1-STAT1-IRF1",
        "target_node_id": "NODE05660",
        "target_edge_id": "M21B-E008259",
        "output_label": "IRF1 gene expression",
        "primary_locator": "PMID:19929594; PMID:7645205",
    },
    {
        "name": "IFNG-IFNGR-JAK1-STAT1-GBP2",
        "target_node_id": "NODE04004",
        "target_edge_id": "M21B-E008203",
        "output_label": "GBP2 gene expression",
        "primary_locator": "PMID:17293456; PMCID:PMC1815270",
    },
    {
        "name": "IFNG-IFNGR-JAK1-STAT1-CXCL9",
        "target_node_id": "NODE02696",
        "target_edge_id": "M21B-E008361",
        "output_label": "CXCL9 gene expression",
        "primary_locator": "PMID:20585034; PMCID:PMC2925661",
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
    lr_edge_id = "M21B-E001763"
    relay_edge_id = "M21B-E000013"
    relay_node_id = "NODE06016"
    tf_node_id = "NODE10705"
    lr = edges[lr_edge_id]
    relay_edge = edges[relay_edge_id]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[relay_node_id]
    tf = nodes[tf_node_id]
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        target = nodes[spec["target_node_id"]]
        target_edge = edges[spec["target_edge_id"]]
        expansion_id = f"M21B-LITEXP-IFNGSTAT1-{index:03d}"
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": lr["source_node_id"],
                "ligand_label": ligand["canonical_label"],
                "ligand_receptor_edge_id": lr_edge_id,
                "receptor_node_id": lr["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": relay_edge_id,
                "intracellular_continuation_node_id": relay_node_id,
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf_node_id,
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": spec["target_edge_id"],
                "target_gene_node_id": spec["target_node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": spec["target_node_id"],
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"IFN-type-II-IFNGR-JAK1-STAT1-{spec['output_label'].split()[0]}",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": unique_join(
                    lr.get("evidence_ids", ""), relay_edge.get("evidence_ids", ""), target_edge.get("evidence_ids", ""), spec["primary_locator"]
                ),
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    f"manual_primary_{spec['name'].lower().replace('-', '_')}_route;graph_linked_route_source;"
                    "primary_layer_linked;receptor_to_intracellular_edge_supported_by_graph;"
                    "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_supported_by_target_evidence;"
                    "type_ii_ifn_stat1_target_output_retained;evidence_route_only"
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": spec["primary_locator"],
                "citation_note": (
                    f"Primary-evidence route overlay for {spec['name']}. Existing IFNGR/JAK and STAT1 target evidence "
                    "is retained; the JAK1-to-STAT1 handoff remains explicit and no causal edge or confidence score is created."
                ),
                "evidence_summary": (
                    "Primary IFN-gamma studies support IFNGR-associated JAK/STAT1 signaling and the "
                    f"{spec['output_label']} readout. The route maps those observations onto the existing IFN-gamma, IFNGR, "
                    "JAK1, STAT1 and target-gene nodes."
                ),
                "limitations": (
                    "The source studies use different cell systems and genomic or transcript assays. They support the receptor, "
                    "JAK1, STAT1 and target-output layers but do not establish a single complete molecular handoff from IFNGR "
                    "through JAK1 to STAT1 in the same experiment. No SCI transfer or confidence score is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "human and mammalian IFN-gamma-response systems as reported across primary studies",
                "cell_type_context": "IFN-gamma-responsive immune and glial model systems",
                "compartment_context": (
                    "extracellular IFN-gamma; plasma-membrane IFNGR1/IFNGR2; intracellular JAK1; nuclear STAT1 target-gene output"
                ),
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite_primary_evidence",
                "assay_or_perturbation": (
                    "IFN-gamma stimulation; JAK/STAT perturbation; STAT1 occupancy or promoter assays; target-gene transcript expression"
                ),
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
