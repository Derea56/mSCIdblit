#!/usr/bin/env python3
"""Generate evidence-only literature-expansion rows from validated queue records.

This helper does not infer intracellular, TF, target-gene, or causal links. It
selects queue records that already contain a validated primary evidence layer,
an unambiguous ligand-receptor edge classification, and a non-empty output
class, then carries the queue's source-linked claim into the explicit
ligand>receptor>output evidence layer used by the release builder.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=0)
    return parser.parse_args()


def numeric_suffix(value: str) -> int:
    match = re.search(r"(\d+)$", value)
    return int(match.group(1)) if match else 0


def normalized(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


RECEPTOR_TERMS = (
    "receptor", "gpcr", "integrin", "cxcr", "ccr", "xcr", "ackr", "ntrk",
    "notch", "robo", "unc5", "plexin", "tlr", "lrp1", "cd44", "esl-1",
    "selectin", "itga", "itgb", "eph", "nrp", "frizzled", "fzd", "bmpr",
    "tgfbr", "egfr", "pdgfr", "fgfr", "igf1r", "insr", "csf1r", "il1r",
    "il6r", "il2r", "il4r", "il7r", "il9r", "il10r", "il17r", "tnfr",
    "fas", "cd40", "mcam", "neogenin", "dcc", "ptprz1", "syndecan",
)


def looks_like_receptor(label: str) -> bool:
    lowered = label.casefold()
    return any(term in lowered for term in RECEPTOR_TERMS)


def select_evidence_record(
    records_by_queue: dict[str, list[dict[str, str]]],
    queue: dict[str, str],
) -> dict[str, str]:
    records = records_by_queue.get(queue["queue_id"], [])
    if not records:
        raise ValueError(f"No downstream evidence record for {queue['queue_id']}")
    wanted = normalized(queue.get("output_class", ""))
    for record in records:
        if normalized(record.get("output_term", "")) == wanted:
            return record
    return records[0]


def main() -> int:
    args = parse_args()
    bundle = args.bundle_dir.resolve()
    queue = read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")
    evidence = read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")
    previous = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    already_curated = {row.get("source_queue_id", "") for row in previous}
    records_by_queue: dict[str, list[dict[str, str]]] = {}
    for record in evidence:
        records_by_queue.setdefault(record["source_queue_id"], []).append(record)

    candidates = []
    for row in queue:
        if row["queue_id"] in already_curated:
            continue
        if row.get("edge_semantic_class") != "ligand_receptor_edge_with_unlinked_downstream_claim":
            continue
        if row.get("lr_entry_assessment") == "not_a_direct_ligand_receptor_pair":
            continue
        if looks_like_receptor(row.get("source_label", "")):
            continue
        target_label = row.get("target_label", "").casefold()
        if any(term in target_label for term in (" receptor-associated ", " signaling branch", " pathway branch")):
            continue
        if row.get("evidence_status") != "validated_primary_exact_layer":
            continue
        if row.get("evidence_scope") != "direct_edge":
            continue
        if not row.get("output_class") or row["output_class"] == "unknown":
            continue
        if not row.get("source_locator") or not row.get("evidence_summary"):
            continue
        candidates.append(row)
    candidates.sort(key=lambda row: numeric_suffix(row["queue_id"]))
    if args.limit:
        candidates = candidates[: args.limit]
    if not candidates:
        raise ValueError("No eligible uncurated queue records found")

    next_id = max((numeric_suffix(row.get("expansion_id", "")) for row in previous), default=0) + 1
    output_rows: list[dict[str, str]] = []
    for index, row in enumerate(candidates):
        record = select_evidence_record(records_by_queue, row)
        source_record_id = record["record_id"]
        evidence_ids = [row["edge_id"], *filter(None, row.get("source_evidence_ids", "").split(";"))]
        evidence_ids.append(source_record_id)
        evidence_ids.extend(filter(None, row.get("source_locator", "").split(";")))
        limitations = row.get("limitations", "")
        unresolved = "Intracellular continuation and TF remain unresolved."
        if unresolved not in limitations:
            limitations = f"{limitations.rstrip()} {unresolved}".strip()
        output_label = f"{row['source_label']}-{row['target_label']} documented {row['output_class']}"
        output_rows.append(
            {
                "expansion_id": f"M21B-LITEXP-{next_id + index}",
                "source_queue_id": row["queue_id"],
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>output",
                "route_tier": "ligand_receptor_output_missing_intracellular_and_tf",
                "known_layers": "ligand|receptor|output",
                "missing_layers": "intracellular_continuation|transcription_factor|target_gene_expression",
                "intracellular_status": "not_mapped",
                "ligand_node_id": row["source_node_id"],
                "ligand_label": row["source_label"],
                "ligand_receptor_edge_id": row["edge_id"],
                "receptor_node_id": row["target_node_id"],
                "receptor_label": row["target_label"],
                "transcription_factor_node_id": "",
                "transcription_factor_label": "",
                "target_gene_node_id": "",
                "target_gene_label": "",
                "output_label": output_label,
                "pathway_name": row.get("pathway_name", ""),
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_ligand_receptor_and_documented_output",
                "evidence_ids": ";".join(dict.fromkeys(evidence_ids)),
                "source_chain_id": f"M21B-LITEXP-{next_id + index}",
                "source_evidence_record_id": source_record_id,
                "route_linkage_status": "literature_expansion:direct_lr_output_with_intracellular_and_tf_unresolved",
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

    args.output.resolve().write_text(json.dumps(output_rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "rows": len(output_rows), "first_queue_id": candidates[0]["queue_id"], "last_queue_id": candidates[-1]["queue_id"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
