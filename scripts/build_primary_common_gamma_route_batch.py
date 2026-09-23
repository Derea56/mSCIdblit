#!/usr/bin/env python3
"""Build source-linked common-gamma cytokine route annotations.

These rows are evidence-layer compositions for IL-7, IL-15, and IL-5.  They
retain parallel receptor-proximal JAK alternatives and reusable STAT5 target
evidence without creating causal graph edges or database confidence scores.
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


ROUTES = (
    {
        "name": "il7",
        "prefix": "M21B-LITEXP-IL7-CG",
        "queue_id": "M21B-DOWNSTREAM:00105",
        "source_record_id": "M21B-DOWNSTREAM-EVID:000192",
        "ligand_edge": "M21B-E000324",
        "receptor_node": "NODE05529",
        "relay_edges": ("M21B-E011504", "M21B-E011505"),
        "tf_node": "NODE10752",
        "target_edges": ("M21B-E008257", "M21B-E008253", "M21B-E008251"),
        "pathway": "IL7-IL7RA:IL2RG-JAK-STAT5",
        "context": "Human and mouse IL-7 receptor signaling systems with lymphoid target-gene comparator studies.",
        "limitation": "The receptor/JAK and STAT5-target observations come from complementary primary systems; preserve the lymphoid cell-state context, represent JAK1 and JAK3 as parallel alternatives, and do not infer SCI transfer or a single-source full chain.",
    },
    {
        "name": "il15",
        "prefix": "M21B-LITEXP-IL15-CG",
        "queue_id": "M21B-DOWNSTREAM:00815",
        "source_record_id": "M21B-DOWNSTREAM-EVID:001339",
        "ligand_edge": "M21B-E000246",
        "receptor_node": "NODE05326",
        "relay_edges": ("M21B-E011507", "M21B-E011508"),
        "tf_node": "NODE10752",
        "target_edges": ("M21B-E008257", "M21B-E008253", "M21B-E008251"),
        "pathway": "IL15-IL15RA:IL2RB:IL2RG-JAK-STAT5",
        "context": "Human and mouse IL-15 receptor or lymphoid signaling systems with shared STAT5 target-gene comparator studies.",
        "limitation": "The IL-15 receptor observations include cis/trans-presentation and shared beta/gamma-chain context, while the STAT5 target studies are independently curated; preserve those boundaries, represent JAK1 and JAK3 as parallel alternatives, and do not infer SCI transfer.",
    },
    {
        "name": "il5",
        "prefix": "M21B-LITEXP-IL5-CG",
        "queue_id": "M21B-DOWNSTREAM:02295",
        "source_record_id": "M21B-DOWNSTREAM-EVID:003662",
        "ligand_edge": "M21B-E000327",
        "receptor_node": "NODE05509",
        "relay_edges": ("M21B-E001780",),
        "tf_node": "NODE10752",
        "target_edges": ("M21B-E008257", "M21B-E008253", "M21B-E008251"),
        "pathway": "IL5-IL5RA:CSF2RB-JAK2-STAT5",
        "context": "Human and mouse IL-5 receptor and eosinophil/hematopoietic comparator systems.",
        "limitation": "The IL-5 receptor/JAK2 evidence and STAT5 target-gene evidence are complementary rather than a single-cell end-to-end experiment; preserve shared beta-chain and eosinophil/hematopoietic context and do not infer SCI transfer.",
    },
)


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
    queues = {row["queue_id"]: row for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")}
    records = {row["record_id"]: row for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}
    sources = index_sources(read_tsv(bundle / "mechanism_edge_sources.tsv"))

    rows: list[dict[str, str]] = []
    serial = 1
    for spec in ROUTES:
        queue = queues[spec["queue_id"]]
        source_record = records[spec["source_record_id"]]
        lr_edge = edges[spec["ligand_edge"]]
        receptor = nodes[spec["receptor_node"]]
        tf = nodes[spec["tf_node"]]
        if (lr_edge["source_node_id"], lr_edge["target_node_id"]) != (lr_edge["source_node_id"], spec["receptor_node"]):
            raise ValueError(f"{spec['name']}: ligand-receptor edge endpoint mismatch")
        for relay_edge_id in spec["relay_edges"]:
            relay_edge = edges[relay_edge_id]
            if relay_edge["source_node_id"] != spec["receptor_node"]:
                raise ValueError(f"{spec['name']}: relay edge does not start at receptor")
            relay = nodes[relay_edge["target_node_id"]]
            for target_edge_id in spec["target_edges"]:
                target_edge = edges[target_edge_id]
                if target_edge["source_node_id"] != spec["tf_node"]:
                    raise ValueError(f"{spec['name']}: target edge does not start at STAT5")
                target = nodes[target_edge["target_node_id"]]
                selected_edge_ids = [spec["ligand_edge"], relay_edge_id, target_edge_id]
                selected_sources = [source for edge_id in selected_edge_ids for source in primary_sources(edge_id, sources)]
                locators = join_unique(
                    [
                        *(source.get("source_locator", "") for source in selected_sources),
                        queue.get("source_locator", ""),
                        source_record.get("source_locator", ""),
                    ]
                )
                evidence_ids = join_unique(
                    [
                        *selected_edge_ids,
                        lr_edge.get("evidence_ids", ""),
                        relay_edge.get("evidence_ids", ""),
                        target_edge.get("evidence_ids", ""),
                        queue.get("source_evidence_ids", ""),
                        source_record.get("source_evidence_ids", ""),
                        locators,
                    ]
                )
                target_sources = primary_sources(target_edge_id, sources)
                target_summary = target_sources[0].get("evidence_summary", "") if target_sources else ""
                rows.append(
                    {
                        "expansion_id": f"{spec['prefix']}-{serial:03d}",
                        "source_queue_id": spec["queue_id"],
                        "route_status": "retained_evidence_route",
                        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                        "missing_layers": "intracellular_to_tf_edge",
                        "intracellular_status": "source_supported",
                        "ligand_node_id": lr_edge["source_node_id"],
                        "ligand_label": lr_edge["source_label"],
                        "ligand_receptor_edge_id": spec["ligand_edge"],
                        "receptor_node_id": spec["receptor_node"],
                        "receptor_label": receptor["canonical_label"],
                        "receptor_intracellular_edge_id": relay_edge_id,
                        "intracellular_continuation_node_id": relay_edge["target_node_id"],
                        "intracellular_continuation_label": relay["canonical_label"],
                        "transcription_factor_node_id": spec["tf_node"],
                        "transcription_factor_label": tf["canonical_label"],
                        "tf_target_edge_id": target_edge_id,
                        "target_gene_node_id": target["node_id"],
                        "target_gene_label": target["canonical_label"],
                        "target_output_form_id": "",
                        "output_node_id": target["node_id"],
                        "output_label": f"{target['canonical_label']} expression",
                        "output_form_id": "",
                        "bridge_id": "",
                        "pathway_name": f"{spec['pathway']}-{target['canonical_label']}-{relay['canonical_label']}",
                        "input_evidence_type": "primary_literature_route_expansion",
                        "output_evidence_type": "primary_target_gene_expression",
                        "evidence_ids": evidence_ids,
                        "source_chain_id": f"{spec['prefix']}-{serial:03d}",
                        "source_evidence_record_id": spec["source_record_id"],
                        "route_linkage_status": f"manual_primary_{spec['name']}_route;primary_layer_linked;parallel_receptor_relay_alternative;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;evidence_route_only",
                        "causal_status": "not_asserted",
                        "traversal_status": "evidence_route_not_causal",
                        "evidence_contract_version": "mechanism_evidence_v1",
                        "evidence_polarity": "supports",
                        "negative_evidence_status": "not_evaluated",
                        "evidence_directness": "source_claim",
                        "output_class": "target_gene_expression",
                        "primary_locator": locators,
                        "citation_note": "Composite primary route annotation assembled from independently curated ligand-receptor, receptor-proximal JAK, and STAT5-target evidence; the direct JAK-to-STAT5 relay remains unasserted.",
                        "evidence_summary": f"Primary evidence supports {lr_edge['source_label']} engagement of the recorded receptor complex, a {relay['canonical_label']} receptor-proximal continuation, and STAT5-associated regulation of {target['canonical_label']}. {target_summary}",
                        "limitations": spec["limitation"],
                        "curation_status": "curated_primary_route",
                        "species_context": queue.get("species_context", "as stated in primary model/assay"),
                        "cell_type_context": spec["context"],
                        "compartment_context": "extracellular ligand; plasma membrane receptor complex; cytoplasm; nucleus; target-gene regulatory locus",
                        "injury_context": "no SCI transfer inferred; primary model context only",
                        "context_scope": "composite primary evidence; route layers retain source-specific models",
                        "assay_or_perturbation": f"Receptor-proximal JAK/STAT activation and STAT5 target-gene assays as recorded in the source ledger. Terminal evidence: {target_summary}",
                        "effect_polarity": "activating",
                        "source_scope": "composite_primary_evidence",
                    }
                )
                serial += 1
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
