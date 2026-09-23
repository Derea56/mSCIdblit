#!/usr/bin/env python3
"""Build source-linked IL-31 JAK1/STAT3 output route annotations."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


TARGETS = (
    ("M21B-E008321", "POMC", "M21B-E008870"),
    ("M21B-E008441", "CCL2", "M21B-E008872"),
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(values: list[str]) -> str:
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
    queues = {row["queue_id"]: row for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")}
    records = {row["record_id"]: row for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}
    sources = read_tsv(bundle / "mechanism_edge_sources.tsv")
    source_by_edge: dict[str, list[dict[str, str]]] = {}
    for source in sources:
        source_by_edge.setdefault(source["edge_id"], []).append(source)

    lr_edge = edges["M21B-E000490"]
    relay_edge = edges["M21B-E000552"]
    receptor = nodes[lr_edge["target_node_id"]]
    kinase = nodes[relay_edge["target_node_id"]]
    tf = nodes["NODE10726"]
    queue = queues["M21B-DOWNSTREAM:00175"]
    record = records["M21B-DOWNSTREAM-EVID:000297"]
    rows: list[dict[str, str]] = []
    for index, (target_edge_id, target_label, output_edge_id) in enumerate(TARGETS, start=1):
        target_edge = edges[target_edge_id]
        output_edge = edges[output_edge_id]
        target = nodes[target_edge["target_node_id"]]
        locators = unique_join(
            [
                "PMID:15184896; PMID:17379091",
                "PMID:15194700",
                "PMID:17148439",
                *(source.get("source_locator", "") for source in source_by_edge.get(relay_edge["edge_id"], [])),
                *(source.get("source_locator", "") for source in source_by_edge.get(target_edge_id, [])),
                *(source.get("source_locator", "") for source in source_by_edge.get(output_edge_id, [])),
                queue.get("source_locator", ""),
                record.get("source_locator", ""),
            ]
        )
        evidence_ids = unique_join(
            [
                "M21B-E000490; M21B-E000552; M21B-E000551",
                lr_edge.get("evidence_ids", ""),
                relay_edge.get("evidence_ids", ""),
                target_edge.get("evidence_ids", ""),
                output_edge.get("evidence_ids", ""),
                queue.get("source_evidence_ids", ""),
                record.get("source_evidence_ids", ""),
                locators,
            ]
        )
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-IL31-JAK1-STAT3-{target_label}-{index:03d}",
                "source_queue_id": "M21B-DOWNSTREAM:00175",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "intracellular_to_tf_edge",
                "intracellular_status": "source_supported",
                "ligand_node_id": lr_edge["source_node_id"],
                "ligand_label": lr_edge["source_label"],
                "ligand_receptor_edge_id": "M21B-E000490",
                "receptor_node_id": lr_edge["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "M21B-E000552",
                "intracellular_continuation_node_id": relay_edge["target_node_id"],
                "intracellular_continuation_label": kinase["canonical_label"],
                "transcription_factor_node_id": "NODE10726",
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": target_edge_id,
                "target_gene_node_id": target["node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": target["node_id"],
                "output_label": f"{target_label} expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"IL31-IL31RA:OSMRbeta-JAK1-STAT3-{target_label}",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_chain_id": f"M21B-LITEXP-IL31-JAK1-STAT3-{target_label}-{index:03d}",
                "source_evidence_record_id": "M21B-DOWNSTREAM-EVID:000297",
                "route_linkage_status": "manual_primary_il31_stat3_output_route;primary_layer_linked;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;evidence_route_only",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": locators,
                "citation_note": "Primary IL-31 receptor/JAK1/STAT3 and IL-31-induced output evidence is assembled as an evidence route; the direct JAK1-to-STAT3 handoff remains unasserted and the target-gene studies retain distinct epithelial or neuroendocrine contexts.",
                "evidence_summary": f"Primary evidence supports IL-31 engagement of the IL31RA:OSMRbeta receptor complex, JAK1 association, STAT3 activation, and {target_label} expression. The route preserves the source-specific output context without asserting causal traversal.",
                "limitations": "The receptor/JAK/STAT and output studies use complementary receptor-reconstituted, human keratinocyte, lung-epithelial, or neuroendocrine systems. Preserve OSMRbeta shared-subunit and isoform context, species/model limits, and no SCI transfer, causal traversal, or database confidence score.",
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse comparator systems",
                "cell_type_context": "Receptor-reconstituted Ba/F3 systems, human A549 lung epithelial cells, and primary human keratinocytes.",
                "compartment_context": "extracellular IL-31; plasma membrane receptor complex; cytoplasm; nucleus; target-gene regulatory locus",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "IL-31 stimulation; receptor reconstitution or receptor-site perturbation; JAK1/STAT3 activation; target-gene transcript, promoter, protein, or pathway-inhibitor assays",
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
    args.output.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
