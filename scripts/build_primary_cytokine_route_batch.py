#!/usr/bin/env python3
"""Build a reproducible primary-evidence cytokine route expansion batch.

The resulting rows are evidence-layer route annotations.  They deliberately
retain the receptor-to-JAK/STAT topology and the TF-to-target edge while
leaving the direct JAK-to-STAT relay unasserted when the source graph does not
contain that exact edge.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ALLOWED_SOURCE_KINDS = {
    "primary_article",
    "pubmed_pmid",
    "review_guided_primary_validation",
}

TARGETS = {
    "il2": {
        "expansion_prefix": "M21B-LITEXP-IL2",
        "queue_id": "M21B-DOWNSTREAM:00054",
        "source_evidence_record_id": "M21B-DOWNSTREAM-EVID:000105",
        "ligand_receptor_edge_id": "M21B-E000236",
        "receptor_node_id": "NODE05446",
        "receptor_intracellular_edge_id": "M21B-E000237",
        "intracellular_continuation_node_id": "NODE06024",
        "tf_node_id": "NODE10752",
        "tf_target_edges": [
            "M21B-E008250",
            "M21B-E008251",
            "M21B-E008252",
            "M21B-E008253",
            "M21B-E008257",
        ],
        "pathway": "IL2-common-gamma-JAK-STAT5",
        "context": "Human lymphocyte and cytokine-receptor reconstitution systems for the IL-2 receptor layer; target-gene studies use lymphoid, hematopoietic, or erythroid comparator systems.",
        "limitation": "The receptor-proximal source uses IL-2 receptor-complex and common-gamma-chain systems, whereas the JAK edge is exported with a receptor-complex alias; preserve that topology boundary and do not infer a single-cell full-chain assay or SCI transfer.",
    },
    "il4": {
        "expansion_prefix": "M21B-LITEXP-IL4",
        "queue_id": "M21B-DOWNSTREAM:00814",
        "source_evidence_record_id": "M21B-DOWNSTREAM-EVID:001338",
        "ligand_receptor_edge_id": "M21B-E001754",
        "receptor_node_id": "NODE05502",
        "receptor_intracellular_edge_id": "M21B-E001782",
        "intracellular_continuation_node_id": "NODE06016",
        "tf_node_id": "NODE10761",
        "tf_target_edges": [
            "M21B-E008263",
            "M21B-E008363",
            "M21B-E008364",
            "M21B-E008365",
            "M21B-E008366",
        ],
        "pathway": "IL4-type-I-receptor-JAK1-STAT6",
        "context": "Human type-I IL-4 receptor-complex reconstitution for receptor/JAK/STAT6 activation; target-gene studies use developing T-helper, macrophage, epithelial, and allergic-response systems.",
        "limitation": "The target studies establish STAT6-dependent gene regulation in bounded cell contexts; they do not demonstrate every receptor-proximal step in the same experiment or imply SCI receiver-cell transfer.",
    },
    "ifng": {
        "expansion_prefix": "M21B-LITEXP-IFNG",
        "queue_id": "M21B-DOWNSTREAM:02554",
        "source_evidence_record_id": "M21B-DOWNSTREAM-EVID:003924",
        "ligand_receptor_edge_id": "M21B-E001763",
        "receptor_node_id": "NODE05009",
        "receptor_intracellular_edge_id": "M21B-E000014",
        "intracellular_continuation_node_id": "NODE06026",
        "tf_node_id": "NODE10705",
        "tf_target_edges": [
            "M21B-E008361",
            "M21B-E008181",
            "M21B-E008259",
            "M21B-E008203",
        ],
        "pathway": "IFNG-IFNGR-JAK2-STAT1",
        "context": "Human/mouse IFNGR1/IFNGR2 receptor-reconstitution and signaling systems; target-gene studies include primary mouse microglia/macrophage and comparator cell systems.",
        "limitation": "The route combines receptor-reconstitution, JAK/STAT activation, and target-gene studies from bounded models; preserve IFN-gamma specificity and do not infer a single-cell full-chain assay or SCI transfer beyond the recorded microglia evidence.",
    },
    "il23": {
        "expansion_prefix": "M21B-LITEXP-IL23",
        "queue_id": "M21B-DOWNSTREAM:00824",
        "source_evidence_record_id": "M21B-DOWNSTREAM-EVID:001358",
        "ligand_receptor_edge_id": "M21B-E001768",
        "receptor_node_id": "NODE05307",
        "receptor_intracellular_edge_id": "M21B-E001769",
        "intracellular_continuation_node_id": "NODE06026",
        "tf_node_id": "NODE10726",
        "tf_target_edges": [
            "M21B-E008227",
            "M21B-E008229",
        ],
        "pathway": "IL23-IL12RB1-IL23R-JAK2-STAT3",
        "context": "Human/mouse IL-23 receptor-reconstitution systems for receptor/JAK/STAT activation; target-gene studies use Th17 or ILC3 lineage systems with STAT3 perturbation and locus assays.",
        "limitation": "The IL-23 receptor source supports multi-STAT activation and the target studies support STAT3 regulation of the selected genes, but the complete ligand-to-target sequence is not asserted as a single experiment and no SCI transfer is inferred.",
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def index_sources(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    result: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        result.setdefault(row["edge_id"], []).append(row)
    return result


def primary_sources(edge_id: str, sources: dict[str, list[dict[str, str]]]) -> list[dict[str, str]]:
    return [row for row in sources.get(edge_id, []) if row.get("source_kind") in ALLOWED_SOURCE_KINDS]


def join_unique(values: list[str]) -> str:
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
    queue = {row["queue_id"]: row for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")}
    records = {row["record_id"]: row for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}
    sources = index_sources(read_tsv(bundle / "mechanism_edge_sources.tsv"))

    rows: list[dict[str, str]] = []
    for route_name, spec in TARGETS.items():
        q = queue[spec["queue_id"]]
        source_record = records[spec["source_evidence_record_id"]]
        lr_edge = edges[spec["ligand_receptor_edge_id"]]
        receptor = nodes[spec["receptor_node_id"]]
        tf = nodes[spec["tf_node_id"]]
        if (lr_edge["source_node_id"], lr_edge["target_node_id"]) != (lr_edge["source_node_id"], spec["receptor_node_id"]):
            raise ValueError(f"{route_name}: ligand-receptor edge does not end at the selected receptor node")
        for target_edge_id in spec["tf_target_edges"]:
            target_edge = edges[target_edge_id]
            if target_edge["source_node_id"] != spec["tf_node_id"]:
                raise ValueError(f"{route_name}: target edge {target_edge_id} does not start at selected TF")
            target = nodes[target_edge["target_node_id"]]
            selected_edge_ids = [
                spec["ligand_receptor_edge_id"],
                spec["receptor_intracellular_edge_id"],
                target_edge_id,
            ]
            selected_sources = [source for edge_id in selected_edge_ids for source in primary_sources(edge_id, sources)]
            locators = join_unique([source.get("source_locator", "") for source in selected_sources])
            evidence_ids = join_unique(
                [
                    *selected_edge_ids,
                    *[lr_edge.get("evidence_ids", "")],
                    *[edges[spec["receptor_intracellular_edge_id"]].get("evidence_ids", "")],
                    target_edge.get("evidence_ids", ""),
                    q.get("source_evidence_ids", ""),
                    source_record.get("source_evidence_ids", ""),
                    locators,
                ]
            )
            target_sources = primary_sources(target_edge_id, sources)
            target_summary = target_sources[0].get("evidence_summary", "") if target_sources else ""
            rows.append(
                {
                    "expansion_id": f"{spec['expansion_prefix']}-{len(rows) + 1:03d}",
                    "source_queue_id": spec["queue_id"],
                    "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                    "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                    "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                    "missing_layers": "intracellular_to_tf_edge",
                    "intracellular_status": "source_supported",
                    "intracellular_tf_edge_id": "",
                    "ligand_node_id": lr_edge["source_node_id"],
                    "ligand_label": lr_edge["source_label"],
                    "ligand_receptor_edge_id": spec["ligand_receptor_edge_id"],
                    "receptor_node_id": spec["receptor_node_id"],
                    "receptor_label": receptor["canonical_label"],
                    "receptor_intracellular_edge_id": spec["receptor_intracellular_edge_id"],
                    "intracellular_continuation_node_id": spec["intracellular_continuation_node_id"],
                    "intracellular_continuation_label": edges[spec["receptor_intracellular_edge_id"]]["target_label"],
                    "transcription_factor_node_id": spec["tf_node_id"],
                    "transcription_factor_label": tf["canonical_label"],
                    "tf_target_edge_id": target_edge_id,
                    "target_gene_node_id": target["node_id"],
                    "target_gene_label": target["canonical_label"],
                    "output_node_id": target["node_id"],
                    "output_label": f"{target['canonical_label']} expression",
                    "pathway_name": f"{spec['pathway']}-{target['canonical_label']}",
                    "input_evidence_type": "primary_literature_route_expansion",
                    "output_evidence_type": "primary_target_gene_expression",
                    "evidence_ids": evidence_ids,
                    "source_evidence_record_id": spec["source_evidence_record_id"],
                    "route_linkage_status": f"manual_primary_{route_name}_route;primary_layer_linked;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;evidence_route_only",
                    "causal_status": "not_asserted",
                    "traversal_status": "evidence_route_not_causal",
                    "source_chain_id": f"{spec['expansion_prefix']}-{len(rows) + 1:03d}",
                    "route_status": "retained_evidence_route",
                    "evidence_contract_version": "mechanism_evidence_v1",
                    "evidence_polarity": "supports",
                    "negative_evidence_status": "not_evaluated",
                    "evidence_directness": "source_claim",
                    "output_class": "target_gene_expression",
                    "species_context": q.get("species_context", "as stated in primary model/assay"),
                    "cell_type_context": spec["context"],
                    "compartment_context": "extracellular ligand; plasma membrane; cytoplasm; nucleus; target-gene regulatory locus",
                    "injury_context": "no SCI transfer inferred; primary model context only",
                    "context_scope": "composite primary evidence; route layers retain source-specific models",
                    "assay_or_perturbation": f"Receptor-proximal activation and STAT/target-gene assays as recorded in the source ledger. Terminal evidence: {target_summary}",
                    "effect_polarity": "activating",
                    "source_scope": "composite_primary_evidence",
                    "primary_locator": locators,
                    "citation_note": "Composite primary route annotation assembled from independently curated ligand-receptor, receptor-proximal, and TF-target primary evidence; the direct intracellular-to-TF relay remains unasserted.",
                    "evidence_summary": f"The source ledger supports ligand activation of the recorded receptor complex, receptor-proximal JAK/STAT pathway continuation, and STAT6/STAT5/STAT1/STAT3-linked regulation of {target['canonical_label']}. {target_summary}",
                    "limitations": spec["limitation"],
                    "curation_status": "curated_primary_route",
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
