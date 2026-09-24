#!/usr/bin/env python3
"""Build primary-literature type-I-interferon ISGF3 target routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "IFNAB-IFNAR-JAK1-ISGF3-IFIT1",
        "target_node_id": "NODE04972",
        "target_edge_id": "M21B-E008602",
        "tf_node_id": "NODE05712",
        "output_label": "IFIT1 gene expression",
        "primary_locator": "PMID:17507495; PMID:31231385",
    },
    {
        "name": "IFNAB-IFNAR-JAK1-ISGF3-OAS1",
        "target_node_id": "NODE08452",
        "target_edge_id": "M21B-E008603",
        "tf_node_id": "NODE05712",
        "output_label": "OAS1 gene expression",
        "primary_locator": "PMID:17507495",
    },
    {
        "name": "IFNAB-IFNAR-JAK1-ISGF3-ISG15",
        "target_node_id": "NODE05709",
        "target_edge_id": "M21B-E008209",
        "tf_node_id": "NODE05712",
        "output_label": "ISG15 gene expression",
        "primary_locator": "PMID:12509459; PMID:19551150",
    },
    {
        "name": "IFNAB-IFNAR-JAK1-ISGF3-MX2",
        "target_node_id": "NODE07601",
        "target_edge_id": "M21B-E008359",
        "tf_node_id": "NODE10705",
        "output_label": "MX2 gene expression",
        "primary_locator": "PMID:31231385",
    },
    {
        "name": "IFNAB-IFNAR-JAK1-ISGF3-IRF7",
        "target_node_id": "NODE05681",
        "target_edge_id": "M21B-E008360",
        "tf_node_id": "NODE10705",
        "output_label": "IRF7 gene expression",
        "primary_locator": "PMID:31231385",
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
    lr_edge_id = "M21B-E001762"
    relay_edge_id = "M21B-E000009"
    relay_node_id = "NODE06016"
    lr = edges[lr_edge_id]
    relay_edge = edges[relay_edge_id]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[relay_node_id]
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        tf_node_id = spec["tf_node_id"]
        tf = nodes[tf_node_id]
        target = nodes[spec["target_node_id"]]
        target_edge = edges[spec["target_edge_id"]]
        expansion_id = f"M21B-LITEXP-IFNABISGF3-{index:03d}"
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
                "pathway_name": f"IFN-type-I-IFNAR-JAK1-ISGF3-{spec['output_label'].split()[0]}",
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
                    "isgf3_target_output_retained;evidence_route_only"
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
                    f"Primary-evidence route overlay for {spec['name']}. Existing type-I-interferon receptor/JAK and "
                    "ISGF3 target evidence is retained; the JAK-to-ISGF3 handoff remains explicit and no causal edge "
                    "or confidence score is created."
                ),
                "evidence_summary": (
                    "Primary interferon studies support IFNAR-associated JAK/STAT signaling and ISGF3-dependent antiviral "
                    f"transcription for the {spec['output_label']} readout. The route maps those observations onto the "
                    "existing IFN-alpha/beta, IFNAR, JAK1, ISGF3 and target-gene nodes."
                ),
                "limitations": (
                    "The source studies use different interferon preparations, cell systems and genomic assays. They support "
                    "the receptor, JAK, ISGF3 and target-output layers but do not establish a single complete molecular handoff "
                    "from IFNAR through JAK1 to ISGF3 in the same experiment. No SCI transfer or confidence score is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "human and mammalian interferon-response systems as reported across primary studies",
                "cell_type_context": "interferon-responsive human cell systems and primary model systems",
                "compartment_context": (
                    "extracellular type-I interferon; plasma-membrane IFNAR1/IFNAR2; intracellular JAK1; nuclear ISGF3 "
                    "interferon-stimulated-response-element target-gene output"
                ),
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite_primary_evidence",
                "assay_or_perturbation": (
                    "type-I-interferon stimulation; JAK/STAT perturbation; ISGF3 or STAT1/STAT2/IRF9 occupancy and/or "
                    "promoter assays; target-gene transcript expression"
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
