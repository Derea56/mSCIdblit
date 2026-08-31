#!/usr/bin/env python3
"""Build the all-pair Module 21A relay inventory and Module 22A handoff.

This creates audit-layer inventories only. It does not modify Module 20A or
promote any downstream signaling claim. Existing Module 21A seed pathways are
indexed as reusable candidates, while every frozen Module 20A pair retains its
own pair-to-pathway-to-TF linkage row.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_router"
RELAY = ROOT / "work" / "module21_relay"

PAIR_QUEUE = ROUTER / "module20a_external_review_queue.tsv"
EDGE_REGISTER = RELAY / "module21a_saturation_edge_register.tsv"
EVIDENCE_REGISTER = RELAY / "module21a_evidence_layer_register.tsv"

PAIR_OUT = RELAY / "module21a_all_pair_relay_coverage.tsv"
REUSE_OUT = RELAY / "module21a_pathway_reuse_registry.tsv"
TF_OUT = RELAY / "module22a_ligand_tf_handoff.tsv"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    pairs = read_tsv(PAIR_QUEUE)
    edges = read_tsv(EDGE_REGISTER)
    layers = read_tsv(EVIDENCE_REGISTER)

    evidence_by_edge: dict[str, set[str]] = defaultdict(set)
    for row in layers:
        evidence_by_edge[row["edge_id"]].add(row["evidence_id"])

    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in edges:
        grouped[(row["source_entity"], row["pathway_name"])].append(row)

    reuse_rows = []
    reuse_by_tuple: dict[tuple[str, str], str] = {}
    for index, key in enumerate(sorted(grouped), 1):
        source_entity, pathway_name = key
        reuse_key = f"M21A-REUSE-{index:04d}"
        reuse_by_tuple[key] = reuse_key
        group = grouped[key]
        evidence_ids = sorted({eid for edge in group for eid in evidence_by_edge[edge["edge_id"]]})
        reuse_rows.append(
            {
                "pathway_reuse_key": reuse_key,
                "source_entity": source_entity,
                "pathway_name": pathway_name,
                "edge_ids": ";".join(edge["edge_id"] for edge in group),
                "evidence_ids": ";".join(evidence_ids),
                "target_entities": ";".join(sorted({edge["target_entity"] for edge in group})),
                "ligand_pair_count": "0",
                "ligand_pair_keys": "",
                "terminal_tf_entities": "",
                "validation_status": "seed_relay_only",
                "reuse_rule": "Reuse only when receptor complex, branch, species, cell/model, assay, and evidence scope match.",
                "limitations": "No Module20A pair has been assigned yet; pair linkage requires separate primary evidence review.",
            }
        )

    pair_fields = [
        "coverage_id",
        "module20a_review_id",
        "pair_key",
        "pair_label_canonical",
        "module20a_confidence",
        "module20a_review_priority",
        "module20a_evidence_register_ids",
        "pathway_reuse_keys",
        "module21a_edge_ids",
        "module21a_evidence_ids",
        "terminal_tf_entities",
        "module22a_handoff_id",
        "module21a_status",
        "module22a_status",
        "search_boundary",
        "curator_notes",
    ]
    pair_rows = []
    tf_rows = []
    for index, pair in enumerate(pairs, 1):
        coverage_id = f"M21A-PAIR-{index:06d}"
        handoff_id = f"M22A-HANDOFF-{index:06d}"
        note = "Inventory only; no downstream relay or TF endpoint inferred from Module20A LR evidence."
        pair_rows.append(
            {
                "coverage_id": coverage_id,
                "module20a_review_id": pair["review_id"],
                "pair_key": pair["pair_key"],
                "pair_label_canonical": pair["pair_label_canonical"],
                "module20a_confidence": pair["confidence_decision"],
                "module20a_review_priority": pair["review_priority"],
                "module20a_evidence_register_ids": pair["evidence_register_ids"],
                "pathway_reuse_keys": "",
                "module21a_edge_ids": "",
                "module21a_evidence_ids": "",
                "terminal_tf_entities": "",
                "module22a_handoff_id": handoff_id,
                "module21a_status": "queued",
                "module22a_status": "queued",
                "search_boundary": "not_yet_searched",
                "curator_notes": note,
            }
        )
        tf_rows.append(
            {
                "module22a_handoff_id": handoff_id,
                "coverage_id": coverage_id,
                "pair_key": pair["pair_key"],
                "pair_label_canonical": pair["pair_label_canonical"],
                "pathway_reuse_keys": "",
                "terminal_tf_entities": "",
                "module21a_evidence_ids": "",
                "tf_program_evidence_ids": "",
                "handoff_status": "queued",
                "terminal_tf_status": "not_yet_searched",
                "search_boundary": "TF endpoint search deferred until validated Module21A relay assignment.",
                "limitations": "Do not infer TF activation from ligand-receptor evidence alone.",
            }
        )

    write_tsv(PAIR_OUT, pair_fields, pair_rows)
    write_tsv(
        REUSE_OUT,
        [
            "pathway_reuse_key",
            "source_entity",
            "pathway_name",
            "edge_ids",
            "evidence_ids",
            "target_entities",
            "ligand_pair_count",
            "ligand_pair_keys",
            "terminal_tf_entities",
            "validation_status",
            "reuse_rule",
            "limitations",
        ],
        reuse_rows,
    )
    write_tsv(
        TF_OUT,
        [
            "module22a_handoff_id",
            "coverage_id",
            "pair_key",
            "pair_label_canonical",
            "pathway_reuse_keys",
            "terminal_tf_entities",
            "module21a_evidence_ids",
            "tf_program_evidence_ids",
            "handoff_status",
            "terminal_tf_status",
            "search_boundary",
            "limitations",
        ],
        tf_rows,
    )
    print(f"wrote {len(pair_rows)} pair rows, {len(reuse_rows)} reusable seed pathways, and {len(tf_rows)} TF handoff rows")


if __name__ == "__main__":
    main()
