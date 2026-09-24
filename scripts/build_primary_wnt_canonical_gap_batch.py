#!/usr/bin/env python3
"""Build primary-literature route overlays for canonical WNT3A gaps."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "WNT3A-FZD2-LRP6-TCF-CCND1",
        "lr_edge_id": "M21B-E006692",
        "relay_node_id": "NODE11859",
        "tf_node_id": "NODE10918",
        "target_node_id": "NODE01755",
        "primary_locator": "PMID:25605717; PMID:26798342; PMID:21975427",
        "output_label": "CCND1/cyclin D1 gene expression",
        "pathway_name": "WNT3A-FZD2-LRP6-beta-catenin-TCF-CCND1",
        "species_context": "human and mammalian cell systems",
        "cell_type_context": "FZD2-engineered 32D cells and Wnt3a-stimulated HEK293T/intestinal epithelial models",
        "assay_or_perturbation": "purified WNT3A stimulation; FZD2 receptor system; LRP6 phosphorylation; beta-catenin stabilization; TCF/LEF reporter; CCND1 expression; LRP6 or pathway perturbation",
    },
    {
        "name": "WNT3A-FZD4-LRP6-TCF-MYC",
        "lr_edge_id": "M21B-E006697",
        "relay_node_id": "NODE11859",
        "tf_node_id": "NODE10918",
        "target_node_id": "NODE07604",
        "primary_locator": "PMID:25605717; PMID:26798342; PMID:21975427",
        "output_label": "MYC/c-Myc gene expression",
        "pathway_name": "WNT3A-FZD4-LRP6-beta-catenin-TCF-MYC",
        "species_context": "human and mammalian cell systems",
        "cell_type_context": "FZD4-engineered 32D cells and Wnt3a-stimulated HEK293T/intestinal epithelial models",
        "assay_or_perturbation": "purified WNT3A stimulation; FZD4 receptor system; LRP6 phosphorylation; beta-catenin stabilization; TCF/LEF reporter; MYC expression; LRP6 or pathway perturbation",
    },
    {
        "name": "WNT3A-FZD7-LRP6-TCF-CCND1",
        "lr_edge_id": "M21B-E006693",
        "relay_node_id": "NODE11859",
        "tf_node_id": "NODE10918",
        "target_node_id": "NODE01755",
        "primary_locator": "PMID:28733458; PMID:26798342; PMID:21975427",
        "output_label": "CCND1/cyclin D1 gene expression",
        "pathway_name": "WNT3A-FZD7-LRP6-beta-catenin-TCF-CCND1",
        "species_context": "human and mammalian cell systems",
        "cell_type_context": "WNT3A-treated FZD receptor-rescue cells and Wnt3a-stimulated epithelial models",
        "assay_or_perturbation": "WNT3A stimulation; FZD7 receptor rescue/multiplex-mutant system; canonical WNT reporter; beta-catenin pathway readouts; CCND1 expression; pathway perturbation",
    },
    {
        "name": "WNT3A-FZD8LRP6-TCF-MYC",
        "lr_edge_id": "M21B-E000155",
        "relay_node_id": "NODE11860",
        "tf_node_id": "NODE10918",
        "target_node_id": "NODE07604",
        "primary_locator": "PMID:20093360; PMID:31235524; PMID:21975427",
        "output_label": "MYC/c-Myc gene expression",
        "pathway_name": "WNT3A-FZD8LRP6-beta-catenin-TCF-MYC",
        "species_context": "human and mouse molecular/cell systems",
        "cell_type_context": "purified WNT-FZD8-LRP6 complex systems, HEK293 cells, and Wnt3a-stimulated intestinal epithelial models",
        "assay_or_perturbation": "WNT3A-FZD8-LRP6 ternary-complex reconstitution; WNT3A stimulation; LRP6 phosphorylation; DVL response; beta-catenin stabilization; TCF-dependent transcription; MYC expression and LRP6 perturbation",
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
        relay = nodes[spec["relay_node_id"]]
        tf = nodes[spec["tf_node_id"]]
        target = nodes[spec["target_node_id"]]
        expansion_id = f"M21B-LITEXP-WNTGAP-{index:03d}"
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
                "target_gene_node_id": spec["target_node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["primary_locator"]),
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    f"manual_primary_{spec['name'].lower().replace('-', '_')}_route;graph_linked_route_source;"
                    "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
                    "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
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
                    f"Primary-evidence route overlay for {spec['name']}. Canonical WNT3A receptor and downstream readouts are "
                    "retained, while unresolved graph handoffs remain explicit; no graph edge or confidence score is created."
                ),
                "evidence_summary": (
                    "Primary WNT studies support WNT3A engagement of the listed Frizzled receptor context, LRP6-dependent canonical "
                    "beta-catenin/TCF signaling, and downstream MYC or CCND1 expression/readouts. The route composes receptor-selectivity, "
                    "canonical reporter, and target-expression experiments into a traversable evidence route."
                ),
                "limitations": (
                    "The cited studies do not provide one uninterrupted experiment for every listed handoff and use different cell systems. "
                    "Direct receptor-to-relay, relay-to-TCF7L2, and TCF7L2-to-target graph edges remain unasserted; mSCS should treat this "
                    "as primary-supported route evidence whose confidence depends on context and concordance."
                ),
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand; plasma-membrane Frizzled/LRP6 receptor context; cytosolic beta-catenin relay; nuclear TCF/LEF transcriptional output",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
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
