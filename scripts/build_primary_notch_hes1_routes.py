#!/usr/bin/env python3
"""Build primary-evidence noncanonical-NOTCH1 routes to HES1."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = [
    {
        "name": "CCN3-NOTCH1-HES1",
        "lr_edge_id": "M21B-E006687",
        "primary_locator": "PMID:12050162; DOI:10.1074/jbc.M203727200",
        "cell_type_context": "presomitic mesoderm and C2/4 myogenic-cell systems",
        "assay_or_perturbation": (
            "CCN3/NOV-Notch1 extracellular association and domain mapping; HES1/HES5 promoter "
            "assays; CCN3 elevation in C2/4 myogenic cells; myogenic differentiation readouts"
        ),
        "evidence_summary": (
            "A primary study reports CCN3/NOV association with the extracellular EGF-like repeats of "
            "NOTCH1 and activation of HES1/HES5-associated Notch outputs in myogenic systems. The "
            "route composes that ligand-receptor/output evidence with the exported canonical NOTCH1 "
            "NICD-RBPJ-HES1 relay."
        ),
        "limitations": (
            "The primary study uses extracellular association/domain mapping and CCN3 overexpression "
            "contexts; it does not establish canonical DSL-ligand equivalence or a single direct "
            "CCN3-to-NICD-to-RBPJ-to-HES1 chain. No graph edge, causal traversal, or database "
            "confidence score is created."
        ),
    },
    {
        "name": "SERPINA4-NOTCH1-HES1",
        "lr_edge_id": "M21B-E006681",
        "primary_locator": "DOI:10.7554/eLife.99462.3; https://elifesciences.org/articles/99462",
        "cell_type_context": "primary mouse hippocampal neurons, HT22 cells and KAL-TG mouse brain",
        "assay_or_perturbation": (
            "kallistatin overexpression; NOTCH1 co-immunoprecipitation and membrane extraction; "
            "NOTCH1 or HES1 knockdown; neuronal and amyloid-beta readouts"
        ),
        "evidence_summary": (
            "A primary study reports kallistatin association with NOTCH1 in mouse hippocampal neurons "
            "and HT22 cells, with NOTCH1/HES1-dependent pathway and neuronal or amyloid-beta outputs. "
            "The route composes that ligand-receptor/target evidence with the exported canonical NOTCH1 "
            "NICD-RBPJ-HES1 relay."
        ),
        "limitations": (
            "The primary study relies on overexpression, co-immunoprecipitation or membrane extraction "
            "rather than purified binary binding and uses mouse hippocampal/Alzheimer-disease contexts. "
            "It does not establish a single direct kallistatin-to-NICD-to-RBPJ-to-HES1 chain. No graph "
            "edge, causal traversal, or database confidence score is created."
        ),
    },
]


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


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    rows: list[dict[str, str]] = []
    for spec in SPECS:
        lr = edges[spec["lr_edge_id"]]
        ligand = nodes[lr["source_node_id"]]
        receptor = nodes[lr["target_node_id"]]
        nicd = nodes["NODE08073"]
        tf = nodes["NODE09657"]
        target = nodes["NODE04668"]
        route_id = f"M21B-LITEXP-{spec['name']}-001"
        rows.append(
            {
                "expansion_id": route_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "graph_supported_canonical_notch_relay_composed",
                "ligand_node_id": lr["source_node_id"],
                "ligand_label": ligand["canonical_label"],
                "ligand_receptor_edge_id": spec["lr_edge_id"],
                "receptor_node_id": lr["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": nicd["node_id"],
                "intracellular_continuation_label": nicd["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf["node_id"],
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": target["node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": "HES1 expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["primary_locator"]),
                "source_chain_id": route_id,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    f"manual_primary_{spec['name'].lower()}_route;graph_linked_route_source;"
                    "graph_linked_ligand_notch1_edge;graph_supported_canonical_notch_relay;"
                    "primary_layer_linked;noncanonical_ligand_receptor_context;"
                    "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
                    "tf_to_target_edge_not_asserted;end_to_end_chain_not_asserted_by_single_source;"
                    "evidence_route_only"
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
                    f"Primary-evidence route overlay for {spec['name']}. "
                    "Ligand-specific evidence and canonical NOTCH relay evidence remain distinguishable."
                ),
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": "mouse and human comparator systems",
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand-receptor association; NOTCH1 proteolysis/NICD relay; nuclear RBPJ transcriptional output",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary ligand-specific evidence plus graph-supported canonical NOTCH relay",
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
    print(json.dumps({"output": str(args.output.resolve()), "rows": len(rows), "ligands": sorted({r["ligand_label"] for r in rows})}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
