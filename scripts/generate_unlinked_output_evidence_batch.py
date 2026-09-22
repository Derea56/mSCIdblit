#!/usr/bin/env python3
"""Materialize source-linked output observations without assigning topology."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def suffix(value: str) -> int:
    match = re.search(r"(\d+)$", value)
    return int(match.group(1)) if match else 0


def normalized(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    bundle = args.bundle_dir.resolve()

    queue = read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")
    evidence = read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")
    prior: list[dict[str, str]] = []
    for path in sorted(bundle.parent.glob("mechanism_graph_module20_24_v2026_09_21_literature_expansion*/mechanism_literature_expansion.tsv")):
        prior.extend(read_tsv(path))
    already_curated = {row.get("source_queue_id", "") for row in prior}
    records_by_queue: dict[str, list[dict[str, str]]] = {}
    for record in evidence:
        records_by_queue.setdefault(record["source_queue_id"], []).append(record)

    eligible_semantics = {
        "ambiguous_edge_needing_manual_topology_review",
        "receptor_proximal_edge_needing_lr_pair_resolution",
    }
    candidates = [
        row for row in queue
        if row["queue_id"] not in already_curated
        and row.get("edge_semantic_class") in eligible_semantics
        and row.get("evidence_status") == "validated_primary_exact_layer"
        and row.get("evidence_scope") == "direct_edge"
        and row.get("output_class") not in {"", "unknown"}
        and row.get("source_locator")
        and row.get("evidence_summary")
    ]
    candidates.sort(key=lambda row: suffix(row["queue_id"]))
    if not candidates:
        raise ValueError("No eligible unlinked output records found")

    def evidence_record(row: dict[str, str]) -> dict[str, str]:
        records = records_by_queue.get(row["queue_id"], [])
        if not records:
            raise ValueError(f"No downstream evidence record for {row['queue_id']}")
        wanted = normalized(row.get("output_class", ""))
        for record in records:
            if normalized(record.get("output_term", "")) == wanted:
                return record
        return records[0]

    next_id = max((suffix(row.get("expansion_id", "")) for row in prior), default=0) + 1
    output: list[dict[str, str]] = []
    for index, row in enumerate(candidates):
        record = evidence_record(row)
        record_id = record["record_id"]
        evidence_ids = [row["edge_id"], *filter(None, row.get("source_evidence_ids", "").split(";")), record_id]
        evidence_ids.extend(filter(None, row.get("source_locator", "").split(";")))
        limitations = row.get("limitations", "").rstrip()
        topology_boundary = "Ligand-receptor topology remains unresolved; output evidence is retained without assigning source or target roles."
        if topology_boundary not in limitations:
            limitations = f"{limitations} {topology_boundary}".strip()
        expansion = f"M21B-LITEXP-{next_id + index}"
        output.append(
            {
                "expansion_id": expansion,
                "source_queue_id": row["queue_id"],
                "route_status": "retained_evidence_route",
                "path_expression": "????>????>????>????>output",
                "route_tier": "downstream_output_annotation_unlinked_topology",
                "known_layers": "output",
                "missing_layers": "ligand_receptor_pair|receptor|intracellular_continuation|transcription_factor",
                "intracellular_status": "not_mapped",
                "ligand_node_id": "",
                "ligand_label": "",
                "ligand_receptor_edge_id": "",
                "receptor_node_id": "",
                "receptor_label": "",
                "transcription_factor_node_id": "",
                "transcription_factor_label": "",
                "target_gene_node_id": "",
                "target_gene_label": "",
                "output_label": f"{row['source_label']}-{row['target_label']} documented {row['output_class']}",
                "pathway_name": row.get("pathway_name", ""),
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_documented_output_unlinked_topology",
                "evidence_ids": ";".join(dict.fromkeys(evidence_ids)),
                "source_chain_id": expansion,
                "source_evidence_record_id": record_id,
                "route_linkage_status": "literature_expansion:output_supported_topology_unresolved",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": row.get("evidence_polarity", "supports"),
                "negative_evidence_status": row.get("negative_evidence_status", "not_evaluated"),
                "evidence_directness": row.get("evidence_directness", "source_claim"),
                "output_class": row["output_class"],
                "primary_locator": row["source_locator"],
                "citation_note": row.get("citation_note", ""),
                "evidence_summary": row["evidence_summary"],
                "limitations": limitations,
                "curation_status": "curated_primary_route",
                "species_context": row.get("species_context", ""),
                "cell_type_context": row.get("cell_type_context", ""),
                "assay_or_perturbation": row.get("assay_or_perturbation", ""),
                "effect_polarity": row.get("effect_polarity", ""),
                "source_scope": row.get("source_scope", "direct_edge"),
            }
        )

    args.output.resolve().write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "rows": len(output), "first_queue_id": candidates[0]["queue_id"], "last_queue_id": candidates[-1]["queue_id"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
