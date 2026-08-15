#!/usr/bin/env python3
"""Integrate the validated Module21A priority-6 review batches 020-021."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
PAIR = RELAY / "module21a_all_pair_relay_coverage.tsv"
TF = RELAY / "module22a_ligand_tf_handoff.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REVIEW = RELAY / "module21a_pair_relay_review_batches020_021.tsv"


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def normalize(row: dict[str, str]) -> dict[str, str]:
    layer = row.get("primary_evidence_layer") or row.get("evidence_layer", "")
    return {
        "review_id": row["review_id"],
        "source_locators": row.get("stable_citations", ""),
        "species": row.get("species", ""),
        "cell_type_model": row.get("cell_type_model", ""),
        "assay_or_perturbation": row.get("assay_perturbation", row.get("assay_or_perturbation", "")),
        "relation_type": row.get("relation_type", ""),
        "evidence_layer": layer,
        "pathway_branch": row.get("pathway_branch", ""),
        "confidence_tier": row.get("confidence", ""),
        "terminal_tf_entities": "" if row.get("terminal_TF", "") in {"", "—", "-"} else row["terminal_TF"],
        "review_status": row.get("status", ""),
        "curator_note": row.get("limitations", ""),
    }


def next_number(values: set[str], prefix: str, width: int) -> int:
    nums = []
    for value in values:
        if value.startswith(prefix):
            try:
                nums.append(int(value.rsplit("-", 1)[1]))
            except ValueError:
                pass
    return max(nums, default=0) + 1


def main() -> None:
    pair_rows = read(PAIR)
    tf_rows = read(TF)
    reuse_rows = read(REUSE)
    detail_rows = read(DETAIL)
    old_review = read(REVIEW) if REVIEW.exists() else []
    old_by_review = {r["review_id"]: r for r in old_review if r.get("review_id")}
    old_reuse_keys = {r.get("pathway_reuse_key", "") for r in old_review if r.get("pathway_reuse_key")}
    old_evidence_ids = {r.get("evidence_id", "") for r in old_review if r.get("evidence_id")}

    source_rows = []
    for filename in ("module21a_batch020_review.tsv", "module21a_batch021_review.tsv"):
        source_rows.extend(normalize(row) for row in read(RELAY / filename))
    if len(source_rows) != 50 or len({r["review_id"] for r in source_rows}) != 50:
        raise SystemExit("batches020_021 must contain 50 unique exact rows")

    pair_by_review = {r["module20a_review_id"]: r for r in pair_rows}
    tf_by_pair = {r["pair_key"]: r for r in tf_rows}
    assigned = {r["review_id"] for r in source_rows}
    missing = assigned - set(pair_by_review)
    if missing:
        raise SystemExit(f"review IDs absent from scaffold: {sorted(missing)}")

    for rid in assigned:
        row = pair_by_review[rid]
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
    existing_evidence = {r.get("evidence_id", "") for r in detail_rows}
    next_reuse = next_number(existing_reuse, "M21A-REUSE-", 4)
    next_evidence = next_number(existing_evidence, "M21A-PAIR-EVID-", 3)

    detail_fields = ["evidence_id", "pathway_reuse_key", "source_locators", "species", "cell_type_model",
                     "assay_or_perturbation", "relation_type", "evidence_layer", "pathway_branch",
                     "confidence_tier", "evidence_summary", "limitations"]
    review_fields = ["review_id", "pair_key", "pair_label_canonical", "pathway_reuse_key", "evidence_id",
                     "source_locators", "species", "cell_type_model", "assay_or_perturbation", "relation_type",
                     "evidence_layer", "pathway_branch", "confidence_tier", "terminal_tf_entities", "review_status",
                     "curator_note"]
    new_reuse = []
    final_review = []
    for source in source_rows:
        old = old_by_review.get(source["review_id"], {})
        has_reuse = source["review_status"] in {"reviewed_relay_candidate", "reviewed_function_only", "reviewed_scavenging_only"}
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

        pair = pair_by_review[source["review_id"]]
        pair["pathway_reuse_keys"] = reuse_key
        pair["module21a_edge_ids"] = "PENDING_M21A_EDGE_MATERIALIZATION" if has_reuse else ""
        pair["module21a_evidence_ids"] = evidence_id
        pair["terminal_tf_entities"] = source["terminal_tf_entities"]
        pair["module21a_status"] = source["review_status"]
        pair["module22a_status"] = "candidate_tf_handoff_pending_validation" if source["terminal_tf_entities"] else "no_terminal_tf_evidence"
        pair["search_boundary"] = "primary_review_batches020_021; exact family/chain boundary search"
        pair["curator_notes"] = source["curator_note"]

        tfrow = tf_by_pair[pair["pair_key"]]
        tfrow["pathway_reuse_keys"] = reuse_key
        tfrow["terminal_tf_entities"] = source["terminal_tf_entities"]
        tfrow["module21a_evidence_ids"] = evidence_id
        tfrow["handoff_status"] = "pending_tf_program_review" if source["terminal_tf_entities"] else "no_terminal_tf_assigned"
        tfrow["terminal_tf_status"] = "candidate_or_supported_activation" if source["terminal_tf_entities"] else "none_found"
        tfrow["search_boundary"] = "Primary downstream review batches020-021; exact family/chain boundary search."
        tfrow["limitations"] = source["curator_note"]

        if has_reuse:
            new_reuse.append({
                "pathway_reuse_key": reuse_key,
                "source_entity": source["pathway_branch"].split("-", 1)[0],
                "pathway_name": source["pathway_branch"],
                "edge_ids": "",
                "evidence_ids": evidence_id,
                "target_entities": "",
                "ligand_pair_count": "1",
                "ligand_pair_keys": pair["pair_key"],
                "terminal_tf_entities": source["terminal_tf_entities"],
                "validation_status": "reviewed_batches020_021_candidate",
                "reuse_rule": "Reuse only when exact ligand/receptor complex, isoform/chain/cofactor, species, cell/model, assay and evidence scope match.",
                "limitations": source["curator_note"],
            })

        detail_rows.append({
            "evidence_id": evidence_id,
            "pathway_reuse_key": reuse_key,
            "source_locators": source["source_locators"],
            "species": source["species"],
            "cell_type_model": source["cell_type_model"],
            "assay_or_perturbation": source["assay_or_perturbation"],
            "relation_type": source["relation_type"],
            "evidence_layer": source["evidence_layer"],
            "pathway_branch": source["pathway_branch"],
            "confidence_tier": source["confidence_tier"],
            "evidence_summary": source["pathway_branch"],
            "limitations": source["curator_note"],
        })
        final_review.append({
            "review_id": source["review_id"],
            "pair_key": pair["pair_key"],
            "pair_label_canonical": pair["pair_label_canonical"],
            "pathway_reuse_key": reuse_key,
            "evidence_id": evidence_id,
            "source_locators": source["source_locators"],
            "species": source["species"],
            "cell_type_model": source["cell_type_model"],
            "assay_or_perturbation": source["assay_or_perturbation"],
            "relation_type": source["relation_type"],
            "evidence_layer": source["evidence_layer"],
            "pathway_branch": source["pathway_branch"],
            "confidence_tier": source["confidence_tier"],
            "terminal_tf_entities": source["terminal_tf_entities"],
            "review_status": source["review_status"],
            "curator_note": source["curator_note"],
        })

    write(PAIR, list(pair_rows[0]), pair_rows)
    write(TF, list(tf_rows[0]), tf_rows)
    write(REUSE, list(reuse_rows[0]), reuse_rows + new_reuse)
    write(DETAIL, detail_fields, detail_rows)
    write(REVIEW, review_fields, final_review)
    print(f"integrated {len(final_review)} pair outcomes, {len(new_reuse)} reusable pathway candidates, and {len(final_review)} evidence records")


if __name__ == "__main__":
    main()
