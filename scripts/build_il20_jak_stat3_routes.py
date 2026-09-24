#!/usr/bin/env python3
"""Build bounded IL-20 JAK1/STAT3 target-gene evidence routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = (
    ("IL20-type-I-CCL2", "M21B-E000744", "NODE05412", "IL20RA:IL20RB receptor complex", "M21B-E008892", "NODE01663", "CCL2 gene", "CCL2"),
    ("IL20-type-II-CCL2", "M21B-E000746", "NODE05426", "IL22RA1:IL20RB receptor complex", "M21B-E008892", "NODE01663", "CCL2 gene", "CCL2"),
    ("IL20-type-I-HGF", "M21B-E000744", "NODE05412", "IL20RA:IL20RB receptor complex", "M21B-E008893", "NODE04681", "HGF gene", "HGF"),
    ("IL20-type-II-HGF", "M21B-E000746", "NODE05426", "IL22RA1:IL20RB receptor complex", "M21B-E008893", "NODE04681", "HGF gene", "HGF"),
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


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    rows: list[dict[str, str]] = []
    for name, lr_id, receptor_id, receptor_label, output_id, target_id, target_label, target_short in ROUTES:
        required = ["NODE05410", receptor_id, "NODE06016", "NODE10726", target_id, lr_id, output_id]
        missing = [item for item in required if item not in nodes and item not in edges]
        if missing:
            raise ValueError(f"{name}: missing graph objects {missing}")
        lr = edges[lr_id]
        if (lr["source_node_id"], lr["target_node_id"]) != ("NODE05410", receptor_id):
            raise ValueError(f"{name}: ligand-receptor endpoints do not match")
        output = edges[output_id]
        if output["source_node_id"] != "NODE05410":
            raise ValueError(f"{name}: output edge does not start at IL20")
        expansion_id = f"M21B-LITEXP-{name}-JAK1-STAT3"
        locators = "PMID:12351624; PMID:17083366; PMID:22802649; PMID:35486004; PMCID:PMC9321592; DOI:10.1096/fj.202101800R; PMID:37884352"
        rows.append({
            "expansion_id": expansion_id,
            "source_queue_id": "",
            "route_status": "retained_evidence_route",
            "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
            "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
            "intracellular_status": "source_supported_ligand_level",
            "ligand_node_id": "NODE05410",
            "ligand_label": "IL20",
            "ligand_receptor_edge_id": lr_id,
            "receptor_node_id": receptor_id,
            "receptor_label": receptor_label,
            "receptor_intracellular_edge_id": "",
            "intracellular_continuation_node_id": "NODE06016",
            "intracellular_continuation_label": "JAK1",
            "intracellular_tf_edge_id": "",
            "transcription_factor_node_id": "NODE10726",
            "transcription_factor_label": "STAT3",
            "tf_target_edge_id": "",
            "target_gene_node_id": target_id,
            "target_gene_label": target_label,
            "output_node_id": target_id,
            "output_label": f"{target_label} expression in primary human keratinocytes",
            "pathway_name": f"IL20-{receptor_label.split(' receptor')[0]}-JAK1-STAT3-{target_short}",
            "input_evidence_type": "primary_literature_route_expansion",
            "output_evidence_type": "primary_target_gene_expression",
            "evidence_ids": unique_join(edges[lr_id].get("evidence_ids", ""), edges[output_id].get("evidence_ids", ""), locators),
            "source_chain_id": expansion_id,
            "source_evidence_record_id": "",
            "route_linkage_status": (
                "graph_linked_route_source;manual_primary_il20_jak1_stat3_route;"
                "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
                "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
                "direct_ligand_output_retained_as_supporting_evidence;evidence_route_only"
            ),
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": "supports",
            "negative_evidence_status": "not_evaluated",
            "evidence_directness": "composite_primary_route",
            "output_class": "target_gene_expression",
            "primary_locator": locators,
            "citation_note": "Primary IL-20 receptor, STAT3 pathway, and epithelial target-output observations are composed as an evidence route; unresolved handoffs remain explicit.",
            "evidence_summary": (
                f"Primary receptor-transfection, epithelial, and intestinal studies support IL-20 signaling through "
                f"the {receptor_label}, JAK/STAT3 pathway activity, and {target_label} output. The direct IL-20 "
                "output record is retained as a separate supporting layer."
            ),
            "limitations": (
                "The cited studies establish complementary receptor, pathway, TF-activity, and expression layers "
                "rather than a single asserted end-to-end edge sequence. The receptor-to-JAK1, JAK1-to-STAT3, and "
                "STAT3-to-target handoffs are not created as graph edges; receptor branch and cell-context effects "
                "remain source-specific. No SCI transfer, causal traversal, or confidence score is inferred."
            ),
            "curation_status": "curated_primary_route",
            "species_context": "human; mouse comparator as stated in the cited IL-20/STAT3 study",
            "cell_type_context": "primary human keratinocytes and intestinal epithelial systems; source-specific context retained",
            "compartment_context": "extracellular ligand; plasma-membrane receptor complex; cytoplasmic JAK1; nuclear STAT3 and target-gene locus",
            "injury_context": "no SCI transfer inferred; primary model context only",
            "context_scope": "composite primary evidence; receptor branch and epithelial output context retained",
            "assay_or_perturbation": "IL-20 stimulation; receptor reconstitution or deletion; JAK/STAT pathway assays; STAT3 activation; CCL2 or HGF expression assays",
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
    args.output.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
