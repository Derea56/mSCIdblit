#!/usr/bin/env python3
"""Build primary-literature IL-1beta/MyD88/NF-kB output route overlays."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "IL1B-IL1R1-MYD88-NFKB-IL6",
        "target_node_id": "NODE05511",
        "output_label": "IL6 gene expression",
        "primary_locator": "PMID:1644898",
        "direct_output_edge_id": "M21B-E008714",
    },
    {
        "name": "IL1B-IL1R1-MYD88-NFKB-CCL20",
        "target_node_id": "NODE01682",
        "output_label": "CCL20 gene expression",
        "primary_locator": "PMID:12528183; DOI:10.1002/glia.10193",
        "direct_output_edge_id": "M21B-E008717",
    },
    {
        "name": "IL1B-IL1R1-MYD88-NFKB-CXCL1",
        "target_node_id": "NODE02622",
        "output_label": "CXCL1 gene expression",
        "primary_locator": "PMID:35384588; PMCID:PMC9684245",
        "direct_output_edge_id": "M21B-E008733",
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
    lr_edge_id = "M21B-E001766"
    relay_edge_id = "M21B-E000023"
    relay_node_id = "NODE07611"
    tf_node_id = "NODE07984"
    lr = edges[lr_edge_id]
    relay_edge = edges[relay_edge_id]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[relay_node_id]
    tf = nodes[tf_node_id]
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        target = nodes[spec["target_node_id"]]
        direct_output_edge = edges[spec["direct_output_edge_id"]]
        expansion_id = f"M21B-LITEXP-IL1BMYD88NFKB-{index:03d}"
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
                "tf_target_edge_id": "",
                "target_gene_node_id": spec["target_node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": spec["target_node_id"],
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": unique_join(
                    lr.get("evidence_ids", ""), relay_edge.get("evidence_ids", ""), direct_output_edge.get("evidence_ids", ""), spec["primary_locator"]
                ),
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    f"manual_primary_{spec['name'].lower().replace('-', '_')}_route;graph_linked_route_source;"
                    "primary_layer_linked;receptor_to_intracellular_edge_supported_by_graph;"
                    "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
                    "direct_ligand_output_evidence_retained;nfkb_output_handoff_unasserted;evidence_route_only"
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
                    f"Primary-evidence route overlay for {spec['name']}. Existing IL-1 receptor/MyD88 graph layers and "
                    "direct IL-1beta output evidence are retained; the MyD88-to-NF-kB and NF-kB-to-target handoffs remain "
                    "explicit and no causal edge or confidence score is created."
                ),
                "evidence_summary": (
                    "Primary IL-1beta studies support IL1R1/IL1RAP-dependent inflammatory signaling and the "
                    f"{spec['output_label']} readout. The route maps those observations onto the existing IL1B, IL1R1/IL1RAP, "
                    "MyD88, NF-kB and target-gene nodes."
                ),
                "limitations": (
                    "The source systems and output assays differ across the primary studies. The direct IL-1beta output evidence "
                    "does not itself establish every intracellular handoff, and the current graph lacks an exact NF-kB-to-target "
                    "edge for this route. No SCI transfer or confidence score is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "human and mammalian IL-1-response systems as reported across primary studies",
                "cell_type_context": "astrocyte and inflammatory glial or epithelial model systems",
                "compartment_context": (
                    "extracellular IL-1beta; plasma-membrane IL1R1/IL1RAP; MyD88-associated intracellular signaling; "
                    "nuclear NF-kB target-gene output"
                ),
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite_primary_evidence",
                "assay_or_perturbation": (
                    "IL-1beta stimulation; IL1R1/IL1RAP or pathway perturbation; NF-kB-associated transcriptional assays; "
                    "target-gene transcript expression"
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
