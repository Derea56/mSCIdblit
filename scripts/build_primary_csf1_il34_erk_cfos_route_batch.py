#!/usr/bin/env python3
"""Build evidence-only CSF1/IL-34-CSF1R-ERK-c-FOS route annotations."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


LIGAND_RECEPTOR_EDGES = (
    ("M21B-E000722", "CSF1", "PMID:9514945; PMID:19587381; PMID:3026638"),
    ("M21B-E000723", "IL34", "PMID:33800170; PMCID:PMC7962444"),
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

    relay_edge = edges["M21B-E000113"]
    relay = nodes[relay_edge["target_node_id"]]
    tf = nodes["NODE03164"]
    target = nodes["NODE02088"]
    queue = queues["M21B-DOWNSTREAM:00001"]
    record = records["M21B-DOWNSTREAM-EVID:000003"]
    rows: list[dict[str, str]] = []

    for index, (lr_edge_id, ligand_name, output_locators) in enumerate(LIGAND_RECEPTOR_EDGES, start=1):
        lr_edge = edges[lr_edge_id]
        receptor = nodes[lr_edge["target_node_id"]]
        locators = unique_join(
            [
                output_locators,
                *(source.get("source_locator", "") for source in source_by_edge.get(lr_edge_id, [])),
                *(source.get("source_locator", "") for source in source_by_edge.get(relay_edge["edge_id"], [])),
                queue.get("source_locator", ""),
                record.get("source_locator", ""),
            ]
        )
        evidence_ids = unique_join(
            [
                lr_edge.get("evidence_ids", ""),
                relay_edge.get("evidence_ids", ""),
                queue.get("source_evidence_ids", ""),
                record.get("source_evidence_ids", ""),
            ]
        )
        expansion_id = f"M21B-LITEXP-{ligand_name}-ERK-CFOS-{index:03d}"
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": queue["queue_id"],
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported",
                "ligand_node_id": lr_edge["source_node_id"],
                "ligand_label": lr_edge["source_label"],
                "ligand_receptor_edge_id": lr_edge["edge_id"],
                "receptor_node_id": lr_edge["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": relay_edge["edge_id"],
                "intracellular_continuation_node_id": relay["node_id"],
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf["node_id"],
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": target["node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": target["node_id"],
                "output_label": "c-FOS expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"{ligand_name}-CSF1R-ERK-ELK1-cFOS",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_chain_id": expansion_id,
                "source_evidence_record_id": record["record_id"],
                "route_linkage_status": (
                    "manual_primary_csf1r_erk_cfos_route;primary_layer_linked;"
                    "parallel_receptor_proximal_alternative;intracellular_to_tf_edge_not_asserted;"
                    "tf_to_target_edge_not_asserted;evidence_route_only"
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
                    f"Primary studies support {ligand_name} engagement of CSF1R/c-Fms and c-FOS expression "
                    "in ligand-stimulated systems, while the graph-supported CSF1R-to-MEK/ERK continuation "
                    "is retained as a bounded intracellular layer. ELK1 and c-FOS are included as the "
                    "transcriptional/output interpretation without asserting either missing handoff."
                ),
                "evidence_summary": (
                    f"Primary evidence supports {ligand_name} to CSF1R/c-Fms and ligand-associated c-FOS "
                    "expression. Existing primary-supported CSF1R-to-MEK/ERK evidence supplies the "
                    "intracellular continuation; the ERK-to-ELK1 and ELK1-to-c-FOS handoffs remain explicitly "
                    "unasserted evidence-layer links."
                ),
                "limitations": (
                    "The receptor-proximal, ERK, and c-FOS studies use complementary structural, myeloid, "
                    "epithelial, and transformed-cell systems rather than one demonstrated ligand-to-target "
                    "experiment. Preserve CSF1 versus IL-34, CSF1R isoform and phosphorylation-site context, "
                    "species and cell-model limits, and the distinction between route plausibility and causal "
                    "traversal; no SCI transfer or database confidence score is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse comparator systems",
                "cell_type_context": "Myeloid progenitors/macrophages, epithelial transformation models, and ligand-stimulated c-FOS readout systems.",
                "compartment_context": "extracellular ligand; plasma membrane CSF1R/c-Fms; cytoplasmic MEK/ERK; nucleus; FOS regulatory locus",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "CSF1 or IL-34 stimulation; CSF1R engagement; ERK phosphorylation or MEK perturbation; c-FOS transcript/promoter readout",
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
