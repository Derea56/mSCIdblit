#!/usr/bin/env python3
"""Build bounded IL-24 JAK1/STAT3 target-gene evidence routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = (
    ("IL24-type-I-S100A7", "M21B-E000745", "NODE05412", "IL20RA:IL20RB receptor complex", "M21B-E008896", "NODE09973", "S100A7 gene", "S100A7"),
    ("IL24-type-II-S100A7", "M21B-E000747", "NODE05426", "IL22RA1:IL20RB receptor complex", "M21B-E008896", "NODE09973", "S100A7 gene", "S100A7"),
    ("IL24-type-I-KRT16", "M21B-E000745", "NODE05412", "IL20RA:IL20RB receptor complex", "M21B-E008897", "NODE06185", "KRT16 gene", "KRT16"),
    ("IL24-type-II-KRT16", "M21B-E000747", "NODE05426", "IL22RA1:IL20RB receptor complex", "M21B-E008897", "NODE06185", "KRT16 gene", "KRT16"),
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
        required = ["NODE05432", receptor_id, "NODE06016", "NODE10726", target_id, lr_id, output_id]
        missing = [item for item in required if item not in nodes and item not in edges]
        if missing:
            raise ValueError(f"{name}: missing graph objects {missing}")
        lr = edges[lr_id]
        if (lr["source_node_id"], lr["target_node_id"]) != ("NODE05432", receptor_id):
            raise ValueError(f"{name}: ligand-receptor endpoints do not match")
        output = edges[output_id]
        if output["source_node_id"] != "NODE05432" or output["target_node_id"] != target_id:
            raise ValueError(f"{name}: output edge does not match target")
        expansion_id = f"M21B-LITEXP-{name}-JAK1-STAT3"
        locators = "PMID:17277128; DOI:10.4049/jimmunol.178.4.2229; PMID:25168428; DOI:10.1016/j.taap.2014.08.019; PMID:38752989"
        rows.append({
            "expansion_id": expansion_id,
            "source_queue_id": "",
            "route_status": "retained_evidence_route",
            "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
            "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
            "intracellular_status": "source_supported_ligand_level",
            "ligand_node_id": "NODE05432",
            "ligand_label": "IL24",
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
            "output_label": f"{target_label} expression in reconstituted human epidermis",
            "pathway_name": f"IL24-{receptor_label.split(' receptor')[0]}-JAK1-STAT3-{target_short}",
            "input_evidence_type": "primary_literature_route_expansion",
            "output_evidence_type": "primary_target_gene_expression",
            "evidence_ids": unique_join(edges[lr_id].get("evidence_ids", ""), edges[output_id].get("evidence_ids", ""), locators),
            "source_chain_id": expansion_id,
            "source_evidence_record_id": "",
            "route_linkage_status": (
                "graph_linked_route_source;manual_primary_il24_jak1_stat3_route;"
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
            "citation_note": "Primary IL-24 receptor, JAK1/STAT3, and epidermal target-output observations are composed as an evidence route; unresolved handoffs remain explicit.",
            "evidence_summary": (
                f"Primary keratinocyte and reconstituted-epidermis studies support IL-24 receptor signaling, "
                f"JAK1-STAT3 pathway activation, STAT3 nuclear activity, and {target_label} expression. "
                "The direct IL-24-to-output record is retained as a separate supporting layer."
            ),
            "limitations": (
                "The cited studies establish complementary receptor, pathway, TF-activity, and expression layers "
                "rather than a single asserted end-to-end edge sequence. The receptor-to-JAK1, JAK1-to-STAT3, and "
                "STAT3-to-target handoffs are not created as graph edges; no SCI transfer, causal traversal, or "
                "confidence score is inferred."
            ),
            "curation_status": "curated_primary_route",
            "species_context": "human; mouse comparator in the cited IL-24/STAT3 study",
            "cell_type_context": "primary human keratinocytes and reconstituted human epidermis; source-specific context retained",
            "compartment_context": "extracellular ligand; plasma-membrane receptor complex; cytoplasmic JAK1; nuclear STAT3 and target-gene locus",
            "injury_context": "no SCI transfer inferred; primary model context only",
            "context_scope": "composite primary evidence; receptor branch and epithelial output context retained",
            "assay_or_perturbation": "IL-24 stimulation; receptor reconstitution or depletion; JAK/STAT pathway assays; STAT3 localization/binding; S100A7 or KRT16 expression assays",
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
