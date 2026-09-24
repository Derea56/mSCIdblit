#!/usr/bin/env python3
"""Build primary-literature IL-18/MyD88/IFNG route overlays."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "IL18-IL18R-MYD88-NFKB-IFNG-PROTEIN",
        "output_node_id": "NODE04983",
        "output_label": "IFN-gamma protein production by IL-12-stimulated NK cells",
        "direct_output_edge_id": "M21B-E009020",
        "primary_locator": "PMID:10229825",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "intracellular_to_tf_edge|target_gene_expression",
        "output_class": "secreted_protein_or_release",
        "output_evidence_type": "primary_functional_output",
    },
    {
        "name": "IL18-IL18R-MYD88-NFKB-IFNG-TRANSCRIPTION",
        "output_node_id": "NODE05006",
        "target_gene_node_id": "NODE05006",
        "output_label": "IFNG gene transcription in IL-12-stimulated NK cells",
        "direct_output_edge_id": "M21B-E009019",
        "primary_locator": "PMID:10229825",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "intracellular_to_tf_edge|tf_to_target_edge",
        "output_class": "target_gene_expression",
        "output_evidence_type": "primary_target_gene_expression",
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
    ligand_node_id = "NODE05348"
    receptor_node_id = "NODE05357"
    lr_edge_id = "M21B-E001752"
    relay_node_id = "NODE07611"
    relay_edge_id = "M21B-E001727"
    tf_node_id = "NODE07984"
    ligand = nodes[ligand_node_id]
    receptor = nodes[receptor_node_id]
    relay = nodes[relay_node_id]
    tf = nodes[tf_node_id]
    lr = edges[lr_edge_id]
    relay_edge = edges[relay_edge_id]
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        output = nodes[spec["output_node_id"]]
        direct_output_edge = edges[spec["direct_output_edge_id"]]
        expansion_id = f"M21B-LITEXP-IL18MYD88IFNG-{index:03d}"
        target_gene_node_id = spec.get("target_gene_node_id", "")
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": spec["path_expression"],
                "route_tier": spec["route_tier"],
                "known_layers": spec["known_layers"],
                "missing_layers": spec["missing_layers"],
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": ligand_node_id,
                "ligand_label": ligand["canonical_label"],
                "ligand_receptor_edge_id": lr_edge_id,
                "receptor_node_id": receptor_node_id,
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": relay_edge_id,
                "intracellular_continuation_node_id": relay_node_id,
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf_node_id,
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": target_gene_node_id,
                "target_gene_label": nodes[target_gene_node_id]["canonical_label"] if target_gene_node_id else "",
                "target_output_form_id": "",
                "output_node_id": spec["output_node_id"],
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": spec["output_evidence_type"],
                "evidence_ids": unique_join(
                    lr.get("evidence_ids", ""), relay_edge.get("evidence_ids", ""), direct_output_edge.get("evidence_ids", ""), spec["primary_locator"]
                ),
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    f"manual_primary_{spec['name'].lower().replace('-', '_')}_route;graph_linked_route_source;"
                    "primary_layer_linked;receptor_to_intracellular_edge_supported_by_graph;"
                    "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
                    "il18_myd88_nfkb_output_retained;evidence_route_only"
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": spec["output_class"],
                "primary_locator": spec["primary_locator"],
                "citation_note": (
                    f"Primary-evidence route overlay for {spec['name']}. Existing IL-18 receptor/MyD88 graph layers and "
                    "the measured IFNG output are retained; unresolved handoffs remain explicit and no causal edge or "
                    "confidence score is created."
                ),
                "evidence_summary": (
                    "Primary IL-18 studies support IL18R1/IL18RAP-associated MyD88/NF-kB signaling and the "
                    f"{spec['output_label']} readout. The route maps those observations onto the existing IL18, IL18R1/IL18RAP, "
                    "MyD88, NF-kB and output nodes."
                ),
                "limitations": (
                    "The source system is an IL-12-stimulated NK-cell model and the cited output studies do not establish every "
                    "intracellular handoff in one experiment. Protein and transcriptional outputs remain separate, and no SCI "
                    "transfer or confidence score is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "mouse and mammalian IL-18-response systems as reported across primary studies",
                "cell_type_context": "IL-12-stimulated natural killer cells",
                "compartment_context": (
                    "extracellular IL-18; plasma-membrane IL18R1/IL18RAP; MyD88-associated intracellular signaling; "
                    "nuclear NF-kB-associated IFNG output"
                ),
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite_primary_evidence",
                "assay_or_perturbation": (
                    "IL-18 and IL-12 stimulation; IL18R/MyD88 pathway assays; NF-kB-associated signaling; IFNG transcript "
                    "and protein production assays"
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
