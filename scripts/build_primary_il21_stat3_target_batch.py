#!/usr/bin/env python3
"""Build primary-literature IL-21/JAK/STAT3 B-cell target routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "IL21-IL21R-JAK1JAK3-STAT3-PRDM1",
        "target_node_id": "NODE09243",
        "primary_locator": "PMID:23325890; PMID:22491065",
        "output_label": "PRDM1/Blimp-1 gene expression",
        "pathway_name": "IL21-IL21R-JAK1JAK3-STAT3-PRDM1",
        "assay_or_perturbation": "IL-21 stimulation of primary human germinal-center or CD40L-stimulated B cells; STAT3 inhibition; PRDM1/Blimp-1 RNA and protein; STAT3 loading at the PRDM1 locus",
    },
    {
        "name": "IL21-IL21R-JAK1JAK3-STAT3-XBP1",
        "target_node_id": "NODE11913",
        "primary_locator": "PMID:20048285",
        "output_label": "XBP1 gene expression",
        "pathway_name": "IL21-IL21R-JAK1JAK3-STAT3-XBP1",
        "assay_or_perturbation": "IL-21-driven differentiation of primary human B cells; STAT3 loss-of-function patient cells; XBP1 induction and immunoglobulin-secreting-cell differentiation assays",
    },
    {
        "name": "IL21-IL21R-JAK1JAK3-STAT3-IL2RA",
        "target_node_id": "NODE05444",
        "primary_locator": "PMID:24159173",
        "output_label": "IL2RA/CD25 gene expression",
        "pathway_name": "IL21-IL21R-JAK1JAK3-STAT3-IL2RA",
        "assay_or_perturbation": "IL-21 stimulation of primary human naive B cells; IL21R and STAT3 loss-of-function comparisons; STAT3 chromatin immunoprecipitation at IL2RA; IL2RA RNA and CD25 surface expression",
    },
    {
        "name": "IL21-IL21R-JAK1JAK3-STAT3-BCL6",
        "target_node_id": "NODE01168",
        "primary_locator": "PMID:20142429; PMID:20142430",
        "output_label": "BCL6 gene expression",
        "pathway_name": "IL21-IL21R-JAK1JAK3-STAT3-BCL6",
        "assay_or_perturbation": "IL-21 or IL-21R perturbation in germinal-center B-cell models; B-cell-intrinsic receptor requirement; BCL6 expression and germinal-center/plasma-cell differentiation readouts",
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
    lr_edge_id = "M21B-E000248"
    lr = edges[lr_edge_id]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes["NODE06024"]
    tf = nodes["NODE10726"]
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        target = nodes[spec["target_node_id"]]
        expansion_id = f"M21B-LITEXP-IL21GAP-{index:03d}"
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
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": "NODE06024",
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": "NODE10726",
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
                    f"Primary-evidence route overlay for {spec['name']}. IL-21 receptor/JAK/STAT3 and B-cell target-gene layers are retained "
                    "while unresolved graph handoffs remain explicit; no causal edge or confidence score is created."
                ),
                "evidence_summary": (
                    "Primary IL-21 studies support IL-21 receptor-associated JAK/STAT3 activation and the "
                    f"{spec['output_label']} readout, including STAT3-dependent, chromatin, or receptor-perturbation evidence. The route maps those "
                    "observations onto the existing IL-21 receptor, JAK1/JAK3, STAT3, and target-gene nodes."
                ),
                "limitations": (
                    "The source systems differ across primary human B cells, germinal-center models, and receptor or STAT3 perturbation systems. "
                    "Direct receptor-to-JAK, JAK-to-STAT3, and STAT3-to-target graph handoffs remain evidence-layer links; no SCI transfer "
                    "or causal graph edge is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "human and mouse cell systems",
                "cell_type_context": "primary human B-cell or mouse germinal-center B-cell systems and cytokine-receptor signaling models",
                "compartment_context": "extracellular IL-21; plasma-membrane IL-21 receptor complex; intracellular JAK1/JAK3 signaling; nuclear STAT3 target-gene output",
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
