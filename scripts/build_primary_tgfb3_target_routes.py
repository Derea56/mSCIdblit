#!/usr/bin/env python3
"""Build primary-literature TGF-beta3 target-gene route overlays."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "TGFB3-TGFBR-SMAD23-CTGF",
        "target_node_id": "NODE02574",
        "target_label": "CTGF/CCN2",
        "output_label": "CTGF/CCN2 gene expression after TGF-beta3 stimulation",
        "pathway_name": "Tgfb3-TGFBR1/2-SMAD2/3-SMAD4-CTGF",
    },
    {
        "name": "TGFB3-TGFBR-SMAD23-SMAD7",
        "target_node_id": "NODE10475",
        "target_label": "SMAD7 gene",
        "output_label": "SMAD7 gene expression after TGF-beta3 stimulation",
        "pathway_name": "Tgfb3-TGFBR1/2-SMAD2/3-SMAD4-SMAD7",
    },
)

COMMON = {
    "ligand_node_id": "NODE11011",
    "ligand_label": "Tgfb3",
    "lr_edge_id": "M21B-E000342",
    "receptor_node_id": "NODE11016",
    "receptor_label": "TGFBR1-TGFBR2 receptor complex",
    "intracellular_node_id": "NODE10459",
    "intracellular_label": "SMAD2/3-SMAD4 heteromeric complex",
    "tf_node_id": "NODE10462",
    "tf_label": "SMAD2;SMAD3",
    "locators": "PMID:16772929; DOI:10.1097/01.prs.0000224299.16523.76",
}


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
    for spec in SPECS:
        required = [
            COMMON["ligand_node_id"], COMMON["receptor_node_id"],
            COMMON["intracellular_node_id"], COMMON["tf_node_id"],
            spec["target_node_id"],
        ]
        missing = [node_id for node_id in required if node_id not in nodes]
        if missing:
            raise ValueError(f"{spec['name']}: missing nodes {missing}")
        lr = edges.get(COMMON["lr_edge_id"])
        if not lr or (lr["source_node_id"], lr["target_node_id"]) != (
            COMMON["ligand_node_id"], COMMON["receptor_node_id"]
        ):
            raise ValueError(f"{spec['name']}: ligand-receptor edge endpoints do not match")
        expansion_id = f"M21B-LITEXP-{spec['name']}"
        rows.append({
            "expansion_id": expansion_id,
            "source_queue_id": "",
            "route_status": "retained_evidence_route",
            "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
            "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
            "intracellular_status": "source_supported_ligand_level",
            "ligand_node_id": COMMON["ligand_node_id"],
            "ligand_label": COMMON["ligand_label"],
            "ligand_receptor_edge_id": COMMON["lr_edge_id"],
            "receptor_node_id": COMMON["receptor_node_id"],
            "receptor_label": COMMON["receptor_label"],
            "receptor_intracellular_edge_id": "",
            "intracellular_continuation_node_id": COMMON["intracellular_node_id"],
            "intracellular_continuation_label": COMMON["intracellular_label"],
            "intracellular_tf_edge_id": "",
            "transcription_factor_node_id": COMMON["tf_node_id"],
            "transcription_factor_label": COMMON["tf_label"],
            "tf_target_edge_id": "",
            "target_gene_node_id": spec["target_node_id"],
            "target_gene_label": spec["target_label"],
            "output_node_id": spec["target_node_id"],
            "output_label": spec["output_label"],
            "pathway_name": spec["pathway_name"],
            "input_evidence_type": "primary_literature_route_expansion",
            "output_evidence_type": "primary_target_gene_expression",
            "evidence_ids": unique_join(lr.get("evidence_ids", ""), COMMON["locators"]),
            "source_chain_id": expansion_id,
            "source_evidence_record_id": "",
            "route_linkage_status": (
                "graph_linked_route_source;manual_primary_tgfb3_smad23_target_route;"
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
            "primary_locator": COMMON["locators"],
            "citation_note": (
                "PMID:16772929 directly reports TGF-beta3-induced CTGF, Smad3 and Smad7 expression in "
                "primary mouse fetal and adult fibroblasts; receptor and SMAD relay layers are retained "
                "from the graph-linked evidence register."
            ),
            "evidence_summary": (
                "A primary fibroblast study reports strong TGF-beta3-induced CTGF expression and increased "
                "SMAD7 expression, with the response measured across fetal and adult mouse fibroblasts. "
                "The route retains the graph-linked TGFBR1/2 receptor and SMAD2/3-SMAD4 continuation, "
                "while leaving each molecular handoff explicit rather than asserting a causal chain."
            ),
            "limitations": (
                "The primary study establishes ligand-specific target-gene responses but does not by itself "
                "resolve every receptor-to-SMAD, SMAD-complex-to-factor, or factor-to-promoter handoff in "
                "the graph. No causal traversal, graph edge, SCI transfer, or confidence score is inferred."
            ),
            "curation_status": "curated_primary_route",
            "species_context": "mouse",
            "cell_type_context": "primary fetal and adult mouse fibroblasts",
            "compartment_context": "extracellular ligand; plasma-membrane receptor; receptor-SMAD relay; nuclear transcriptional output",
            "injury_context": "no SCI transfer inferred; primary fibroblast model context only",
            "context_scope": "primary ligand-specific fibroblast evidence with graph-linked receptor and relay context",
            "assay_or_perturbation": "TGF-beta1 or TGF-beta3 stimulation; quantitative PCR for CTGF, SMAD3 and SMAD7 expression",
            "effect_polarity": "activating",
            "source_scope": "composite_primary_evidence",
        })
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
