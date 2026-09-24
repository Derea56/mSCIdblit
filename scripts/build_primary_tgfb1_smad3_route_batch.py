#!/usr/bin/env python3
"""Build bounded TGFB1-TGFBR-SMAD3/4 target-gene evidence routes.

These rows connect existing primary-supported receptor, SMAD, and promoter
records for mSCS plausibility analysis.  They do not create causal edges or
database confidence scores, and the SMAD3-to-SMAD3/4 complex handoff remains
explicitly unresolved.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


TARGETS = (
    ("M22B-E000391", "COL1A2", "M21B-E008690"),
    ("M22B-E000392", "CTGF/CCN2", "M21B-E008688"),
    ("M22B-E000393", "JUN/c-JUN", ""),
    ("M22B-E000394", "SERPINE1/PAI-1", ""),
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(values: list[str]) -> str:
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
    sources = read_tsv(bundle / "mechanism_edge_sources.tsv")
    source_by_edge: dict[str, list[dict[str, str]]] = {}
    for source in sources:
        source_by_edge.setdefault(source["edge_id"], []).append(source)

    lr_edge = edges["M21B-E000335"]
    receptor = nodes[lr_edge["target_node_id"]]
    receptor_continuation_edge = edges["M21B-E000035"]
    intracellular = nodes[receptor_continuation_edge["target_node_id"]]
    tf_node = nodes["NODE10470"]
    rows: list[dict[str, str]] = []

    for index, (tf_target_edge_id, target_label, output_edge_id) in enumerate(TARGETS, start=1):
        tf_target_edge = edges[tf_target_edge_id]
        target = nodes[tf_target_edge["target_node_id"]]
        output_edge = edges.get(output_edge_id) if output_edge_id else None
        output_node = nodes[output_edge["target_node_id"]] if output_edge else target
        locators = unique_join(
            [
                *(source.get("source_locator", "") for source in source_by_edge.get(lr_edge["edge_id"], [])),
                *(source.get("source_locator", "") for source in source_by_edge.get(receptor_continuation_edge["edge_id"], [])),
                *(source.get("source_locator", "") for source in source_by_edge.get(tf_target_edge_id, [])),
                *(source.get("source_locator", "") for source in source_by_edge.get(output_edge_id, [])),
            ]
        )
        evidence_ids = unique_join(
            [
                lr_edge.get("evidence_ids", ""),
                receptor_continuation_edge.get("evidence_ids", ""),
                tf_target_edge.get("evidence_ids", ""),
                output_edge.get("evidence_ids", "") if output_edge else "",
                *(source.get("evidence_id", "") for source in source_by_edge.get(lr_edge["edge_id"], [])),
                *(source.get("evidence_id", "") for source in source_by_edge.get(receptor_continuation_edge["edge_id"], [])),
                *(source.get("evidence_id", "") for source in source_by_edge.get(tf_target_edge_id, [])),
                *(source.get("evidence_id", "") for source in source_by_edge.get(output_edge_id, [])),
                locators,
            ]
        )
        output_status = (
            "output_edge_asserted_as_graph_edge"
            if output_edge
            else "output_edge_not_asserted_primary_output_evidence_only"
        )
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-TGFB1-SMAD3-SMAD4-{index:03d}",
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "intracellular_to_tf_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": lr_edge["source_node_id"],
                "ligand_label": lr_edge["source_label"],
                "ligand_receptor_edge_id": lr_edge["edge_id"],
                "receptor_node_id": lr_edge["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": receptor_continuation_edge["edge_id"],
                "intracellular_continuation_node_id": intracellular["node_id"],
                "intracellular_continuation_label": intracellular["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf_node["node_id"],
                "transcription_factor_label": tf_node["canonical_label"],
                "tf_target_edge_id": tf_target_edge_id,
                "target_gene_node_id": target["node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": output_node["node_id"],
                "output_label": f"{target_label} expression",
                "output_form_id": "",
                "output_edge_id": output_edge_id,
                "bridge_id": "",
                "pathway_name": f"TGFB1-TGFBR-SMAD3-SMAD4-{target_label}",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_chain_id": f"M21B-LITEXP-TGFB1-SMAD3-SMAD4-{index:03d}",
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    "manual_primary_tgfb1_smad3_output_route;graph_linked_route_source;primary_layer_linked;"
                    "receptor_identity_alias:TGFBR1-TGFBR2 receptor complex;receptor_to_intracellular_edge_asserted_as_graph_edge;"
                    "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;"
                    f"tf_target_source_review_guided_primary_locator;{output_status};evidence_route_only"
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": locators,
                "citation_note": (
                    "Primary TGFB1 receptor, receptor-SMAD3 activation, and SMAD3/4 target-promoter evidence are "
                    "retained as a bounded route; the SMAD3-to-SMAD3/4 complex handoff remains unasserted."
                ),
                "evidence_summary": (
                    f"Primary evidence supports TGFB1 engagement of the TGFBR1:TGFBR2 receptor complex, receptor-linked "
                    f"SMAD3 signaling, SMAD3/SMAD4-associated regulation of {target_label}, and the corresponding "
                    "target-gene output. The route preserves these compatible layers without asserting a new SMAD3-to-"
                    "SMAD3/4 graph edge."
                ),
                "limitations": (
                    "The receptor, SMAD signaling, and target-promoter studies are complementary primary systems and "
                    "include fibroblast, epithelial, osteoblast, or reporter contexts. Preserve receptor-complex and "
                    "SMAD3/4 identity, target-specific cell state, and the distinction between evidence composition and "
                    "asserted graph connectivity; no SCI transfer, causal traversal, or database confidence score is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse comparator systems",
                "cell_type_context": "Human fibroblast, epithelial, osteoblast, and promoter-reporter systems represented by component evidence.",
                "compartment_context": "extracellular TGFB1; plasma-membrane TGFBR complex; cytoplasm; nucleus; target-gene regulatory locus",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "TGFB1 stimulation; receptor-SMAD phosphorylation; SMAD3/4 perturbation; promoter reporter, DNA-binding, ChIP, and target-expression assays",
                "effect_polarity": "activating",
                "source_scope": "composite_primary_and_review_guided_evidence",
            }
        )
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
