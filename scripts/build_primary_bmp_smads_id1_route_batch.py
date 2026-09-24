#!/usr/bin/env python3
"""Build bounded BMP-family SMAD1/5/8 -> ID1 route annotations.

The exported graph contains ligand-specific receptor records and
ligand-specific BMP/SMAD1/5/8 activation records for this small family.  It
also contains a source-linked SMAD1/5/8 -> ID1 target-gene edge.  The route
overlay composes those layers for mSCS plausibility analysis while leaving the
receptor-to-SMAD and SMAD-program-to-TF handoffs explicitly unresolved.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


TARGET_EDGE_ID = "M22B-E000346"
INTRACELLULAR_EVIDENCE_EDGE_ID = "M22B-E000347"
INTRACELLULAR_NODE_ID = "NODE10436"
TF_NODE_ID = "NODE10440"
TARGET_NODE_ID = "NODE04960"

SPECS = (
    {
        "slug": "BMP9-GDF2",
        "ligand_node_id": "NODE01319",
        "ligand_label": "BMP9/GDF2",
        "lr_edge_id": "M21B-E003256",
        "smad_edge_id": "M21B-E008864",
    },
    {
        "slug": "BMP10",
        "ligand_node_id": "NODE01291",
        "ligand_label": "Bmp10",
        "lr_edge_id": "M20B-E001803",
        "smad_edge_id": "M21B-E008862",
    },
    {
        "slug": "GDF6-BMP13",
        "ligand_node_id": "NODE04048",
        "ligand_label": "GDF6/BMP13 (CDMP-2)",
        "lr_edge_id": "M21B-E006615",
        "smad_edge_id": "M21B-E008860",
    },
    {
        "slug": "GDF7-BMP12",
        "ligand_node_id": "NODE04053",
        "ligand_label": "GDF7/BMP12",
        "lr_edge_id": "M21B-E006358",
        "smad_edge_id": "M21B-E008861",
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


def stable_locators(*rows: dict[str, str]) -> str:
    """Keep stable public identifiers; omit inherited PubMed search URLs."""
    values = []
    for row in rows:
        locator = row.get("source_locator", "")
        values.append("; ".join(item for item in locator.split(";") if "?term=" not in item))
    return unique_join(*values)


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    sources: dict[str, list[dict[str, str]]] = {}
    for row in read_tsv(bundle / "mechanism_edge_sources.tsv"):
        sources.setdefault(row["edge_id"], []).append(row)

    required_nodes = {INTRACELLULAR_NODE_ID, TF_NODE_ID, TARGET_NODE_ID}
    missing_nodes = sorted(required_nodes - nodes.keys())
    if missing_nodes:
        raise ValueError(f"BMP route requires missing nodes: {missing_nodes}")
    for spec in SPECS:
        required_edges = {spec["lr_edge_id"], spec["smad_edge_id"], TARGET_EDGE_ID, INTRACELLULAR_EVIDENCE_EDGE_ID}
        missing_edges = sorted(required_edges - edges.keys())
        if missing_edges:
            raise ValueError(f"{spec['slug']} route requires missing edges: {missing_edges}")
        lr = edges[spec["lr_edge_id"]]
        if (lr["source_node_id"], lr["target_node_id"]) != (spec["ligand_node_id"], nodes[lr["target_node_id"]]["node_id"]):
            raise ValueError(f"Unexpected ligand/receptor edge endpoints for {spec['slug']}")
        smad = edges[spec["smad_edge_id"]]
        if (smad["source_node_id"], smad["target_node_id"]) != (spec["ligand_node_id"], TF_NODE_ID):
            raise ValueError(f"Unexpected ligand/SMAD edge endpoints for {spec['slug']}")
        target = edges[TARGET_EDGE_ID]
        if (target["source_node_id"], target["target_node_id"]) != (TF_NODE_ID, TARGET_NODE_ID):
            raise ValueError("Unexpected SMAD/ID1 target edge endpoints")

    intracellular_evidence = edges[INTRACELLULAR_EVIDENCE_EDGE_ID]
    rows: list[dict[str, str]] = []
    for spec in SPECS:
        lr = edges[spec["lr_edge_id"]]
        smad = edges[spec["smad_edge_id"]]
        target = edges[TARGET_EDGE_ID]
        receptor = nodes[lr["target_node_id"]]
        locators = stable_locators(
            *sources.get(spec["lr_edge_id"], []),
            *sources.get(spec["smad_edge_id"], []),
            *sources.get(INTRACELLULAR_EVIDENCE_EDGE_ID, []),
            *sources.get(TARGET_EDGE_ID, []),
        )
        evidence_ids = unique_join(
            spec["lr_edge_id"], lr.get("evidence_ids", ""),
            spec["smad_edge_id"], smad.get("evidence_ids", ""),
            INTRACELLULAR_EVIDENCE_EDGE_ID, intracellular_evidence.get("evidence_ids", ""),
            TARGET_EDGE_ID, target.get("evidence_ids", ""),
            locators,
        )
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-{spec['slug']}-SMAD1-5-8-ID1",
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": spec["ligand_node_id"],
                "ligand_label": spec["ligand_label"],
                "ligand_receptor_edge_id": spec["lr_edge_id"],
                "receptor_node_id": receptor["node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": INTRACELLULAR_NODE_ID,
                "intracellular_continuation_label": nodes[INTRACELLULAR_NODE_ID]["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": TF_NODE_ID,
                "transcription_factor_label": nodes[TF_NODE_ID]["canonical_label"],
                "tf_target_edge_id": TARGET_EDGE_ID,
                "target_gene_node_id": TARGET_NODE_ID,
                "target_gene_label": nodes[TARGET_NODE_ID]["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": TARGET_NODE_ID,
                "output_label": "ID1 gene expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"{spec['slug']}-receptor-SMAD1-5-8-SMAD-program-ID1",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_bmp_smad_id1_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    "graph_linked_route_source;manual_primary_bmp_smads_route;"
                    "ligand_specific_receptor_evidence;ligand_specific_smad1_5_8_evidence;"
                    "shared_smads_id1_target_edge;receptor_to_intracellular_edge_not_asserted;"
                    "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_graph_evidence;"
                    "evidence_route_only"
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "gene_expression_or_transcription",
                "primary_locator": locators,
                "citation_note": "Composite primary route annotation. Ligand-specific receptor and SMAD1/5/8 activation observations are joined to the exported SMAD1/5/8-to-ID1 target-gene edge; the receptor-to-SMAD and SMAD-program-to-TF handoffs remain explicit missing-link fields.",
                "evidence_summary": f"Primary sources support {spec['ligand_label']} receptor engagement or receptor-family binding, SMAD1/5/8 pathway activation, and BMP-SMAD-associated ID1 regulation. The route makes the layered sequence available to mSCS without asserting an end-to-end causal chain.",
                "limitations": "The ligand-specific receptor and SMAD1/5/8 observations and the SMAD1/5/8-to-ID1 target record come from complementary systems and are not a single end-to-end experiment for every ligand. Preserve ligand, receptor, species, and cell-context boundaries; no SCI transfer, causal traversal, or confidence score is inferred.",
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse comparator systems as stated in primary studies",
                "cell_type_context": "Primary endothelial, osteoblast or mesenchymal, and BMP-responsive cell systems represented by the source records.",
                "compartment_context": "extracellular BMP-family ligand; plasma-membrane type-I/type-II receptor complex; cytoplasmic SMAD1/5/8 relay; nuclear SMAD-associated ID1 regulation",
                "injury_context": "no SCI transfer inferred; primary BMP signaling contexts only",
                "context_scope": "composite primary evidence; ligand-specific receptor and SMAD observations retained",
                "assay_or_perturbation": "receptor binding or reconstitution, ligand stimulation, SMAD1/5/8 phosphorylation or reporter assays, and ID1 promoter or target-gene expression assays",
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
    print(json.dumps({"output": str(args.output.resolve()), "rows": len(rows)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
