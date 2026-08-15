#!/usr/bin/env python3
"""Integrate the priority-6 low/uncertain ECM review batches 014-015."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
PAIR = RELAY / "module21a_all_pair_relay_coverage.tsv"
TF = RELAY / "module22a_ligand_tf_handoff.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REVIEW = RELAY / "module21a_pair_relay_review_batches014_015.tsv"


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    pair_rows = read(PAIR)
    tf_rows = read(TF)
    reuse_rows = read(REUSE)
    detail_rows = read(DETAIL)
    source_rows = read(REVIEW)
    old_by_review = {r.get("review_id", ""): r for r in source_rows if r.get("review_id")}
    old_reuse_keys = {r.get("pathway_reuse_key", "") for r in source_rows if r.get("pathway_reuse_key")}
    old_evidence_ids = {r.get("evidence_id", "") for r in source_rows if r.get("evidence_id")}

    if len(source_rows) != 50 or len({r["review_id"] for r in source_rows}) != 50:
        raise SystemExit("batches014_015 must contain 50 unique exact rows after ID correction/deduplication")
    pair_by_review = {r["module20a_review_id"]: r for r in pair_rows}
    tf_by_pair = {r["pair_key"]: r for r in tf_rows}
    assigned = {r["review_id"] for r in source_rows}
    if not assigned.issubset(pair_by_review):
        raise SystemExit(f"review IDs absent from scaffold: {sorted(assigned - set(pair_by_review))}")

    for review_id in assigned:
        row = pair_by_review[review_id]
        for field in ("pathway_reuse_keys", "module21a_edge_ids", "module21a_evidence_ids", "terminal_tf_entities",
                      "module21a_status", "module22a_status", "search_boundary", "curator_notes"):
            row[field] = ""
        tfrow = tf_by_pair[row["pair_key"]]
        for field in ("pathway_reuse_keys", "terminal_tf_entities", "module21a_evidence_ids", "handoff_status",
                      "terminal_tf_status", "search_boundary", "limitations"):
            tfrow[field] = ""
    reuse_rows = [r for r in reuse_rows if r.get("pathway_reuse_key", "") not in old_reuse_keys]
    detail_rows = [r for r in detail_rows if r.get("evidence_id", "") not in old_evidence_ids]
    existing_reuse = {r.get("pathway_reuse_key", "") for r in reuse_rows}
    next_reuse = max((int(k.rsplit("-", 1)[1]) for k in existing_reuse if k.startswith("M21A-REUSE-")), default=0) + 1
    existing_evidence = {r.get("evidence_id", "") for r in detail_rows}
    next_evidence = max((int(k.rsplit("-", 1)[1]) for k in existing_evidence if k.startswith("M21A-PAIR-EVID-")), default=0) + 1

    detail_fields = ["evidence_id", "pathway_reuse_key", "source_locators", "species", "cell_type_model",
                     "assay_or_perturbation", "relation_type", "evidence_layer", "pathway_branch",
                     "confidence_tier", "evidence_summary", "limitations"]
    review_fields = ["review_id", "pair_key", "pair_label_canonical", "pathway_reuse_key", "evidence_id",
                     "source_locators", "species", "cell_type_model", "assay_or_perturbation", "relation_type",
                     "evidence_layer", "pathway_branch", "confidence_tier", "terminal_tf_entities",
                     "review_status", "curator_note"]
    new_reuse = []
    new_review = []
    for spec in source_rows:
        review_id = spec["review_id"]
        old = old_by_review.get(review_id, {})
        status = spec["review_status"]
        has_reuse = status in {"reviewed_relay_candidate", "reviewed_function_only", "reviewed_scavenging_only"}
        reuse_key = old.get("pathway_reuse_key", "") if has_reuse else ""
        if has_reuse and not reuse_key:
            while f"M21A-REUSE-{next_reuse:04d}" in existing_reuse:
                next_reuse += 1
            reuse_key = f"M21A-REUSE-{next_reuse:04d}"
            next_reuse += 1
        evidence_id = old.get("evidence_id", "")
        if not evidence_id:
            while f"M21A-PAIR-EVID-{next_evidence:03d}" in existing_evidence:
                next_evidence += 1
            evidence_id = f"M21A-PAIR-EVID-{next_evidence:03d}"
            next_evidence += 1
        existing_reuse.add(reuse_key)
        existing_evidence.add(evidence_id)
        pair = pair_by_review[review_id]
        pair["pathway_reuse_keys"] = reuse_key
        pair["module21a_edge_ids"] = "PENDING_M21A_EDGE_MATERIALIZATION" if has_reuse else ""
        pair["module21a_evidence_ids"] = evidence_id
        pair["terminal_tf_entities"] = spec.get("terminal_tf_entities", "")
        pair["module21a_status"] = status
        pair["module22a_status"] = "candidate_tf_handoff_pending_validation" if spec.get("terminal_tf_entities") else "no_terminal_tf_evidence"
        pair["search_boundary"] = "primary_review_batches014_015; chain-resolution boundary search"
        pair["curator_notes"] = spec["curator_note"]
        tfrow = tf_by_pair[pair["pair_key"]]
        tfrow["pathway_reuse_keys"] = reuse_key
        tfrow["terminal_tf_entities"] = spec.get("terminal_tf_entities", "")
        tfrow["module21a_evidence_ids"] = evidence_id
        tfrow["handoff_status"] = "pending_tf_program_review" if spec.get("terminal_tf_entities") else "no_terminal_tf_assigned"
        tfrow["terminal_tf_status"] = "candidate_or_supported_activation" if spec.get("terminal_tf_entities") else "none_found"
        tfrow["search_boundary"] = "Primary downstream review batches014-015; exact chain-resolution search boundary."
        tfrow["limitations"] = spec["curator_note"]
        if has_reuse:
            new_reuse.append({
                "pathway_reuse_key": reuse_key,
                "source_entity": spec["pathway_branch"].split("-", 1)[0],
                "pathway_name": spec["pathway_branch"],
                "edge_ids": "",
                "evidence_ids": evidence_id,
                "target_entities": "",
                "ligand_pair_count": "1",
                "ligand_pair_keys": pair["pair_key"],
                "terminal_tf_entities": spec.get("terminal_tf_entities", ""),
                "validation_status": "reviewed_batches014_015_candidate",
                "reuse_rule": "Reuse only when exact ligand/receptor complex, isoform/chain/cofactor, species, cell/model, assay and evidence scope match.",
                "limitations": spec["curator_note"],
            })
        detail_rows.append({"evidence_id": evidence_id, "pathway_reuse_key": reuse_key,
                            "source_locators": spec["source_locators"], "species": spec["species"],
                            "cell_type_model": spec["cell_type_model"], "assay_or_perturbation": spec["assay_or_perturbation"],
                            "relation_type": spec["relation_type"], "evidence_layer": spec["evidence_layer"],
                            "pathway_branch": spec["pathway_branch"], "confidence_tier": spec["confidence_tier"],
                            "evidence_summary": spec["pathway_branch"], "limitations": spec["curator_note"]})
        new_review.append({"review_id": review_id, "pair_key": pair["pair_key"],
                           "pair_label_canonical": pair["pair_label_canonical"], "pathway_reuse_key": reuse_key,
                           "evidence_id": evidence_id, "source_locators": spec["source_locators"],
                           "species": spec["species"], "cell_type_model": spec["cell_type_model"],
                           "assay_or_perturbation": spec["assay_or_perturbation"], "relation_type": spec["relation_type"],
                           "evidence_layer": spec["evidence_layer"], "pathway_branch": spec["pathway_branch"],
                           "confidence_tier": spec["confidence_tier"], "terminal_tf_entities": spec.get("terminal_tf_entities", ""),
                           "review_status": status, "curator_note": spec["curator_note"]})

    write(PAIR, list(pair_rows[0]), pair_rows)
    write(TF, list(tf_rows[0]), tf_rows)
    write(REUSE, list(reuse_rows[0]), reuse_rows + new_reuse)
    write(DETAIL, detail_fields, detail_rows)
    write(REVIEW, review_fields, new_review)
    print(f"integrated {len(new_review)} pair outcomes, {len(new_reuse)} reusable pathway candidates, and {len(new_review)} evidence records")


if __name__ == "__main__":
    main()
