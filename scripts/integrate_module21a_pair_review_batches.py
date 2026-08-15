#!/usr/bin/env python3
"""Integrate one or more validated Module21A agent TSV batches.

Usage: python3 scripts/integrate_module21a_pair_review_batches.py 026 027
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def normalize(r: dict[str, str]) -> dict[str, str]:
    return {"review_id": r["review_id"], "source_locators": r.get("stable_citations", ""),
            "species": r.get("species", ""), "cell_type_model": r.get("cell_type_model", ""),
            "assay_or_perturbation": r.get("assay_perturbation") or r.get("assay_or_perturbation", ""), "relation_type": r.get("relation_type", ""),
            "evidence_layer": r.get("primary_evidence_layer") or r.get("evidence_layer", ""),
            "pathway_branch": r.get("pathway_branch", ""), "confidence_tier": r.get("confidence", ""),
            "terminal_tf_entities": "" if str(r.get("terminal_TF") or "").strip().lower() in {"", "—", "-", "none", "null"} else r["terminal_TF"],
            "review_status": r.get("status", ""), "curator_note": r.get("limitations", "")}


def next_id(values: set[str], prefix: str) -> int:
    numbers = []
    for value in values:
        if value.startswith(prefix):
            try:
                numbers.append(int(value.rsplit("-", 1)[1]))
            except ValueError:
                pass
    return max(numbers, default=0) + 1


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("batches", nargs="+", help="three-digit batch IDs, e.g. 026 027")
    args = ap.parse_args()
    tag = "_".join(args.batches)
    pair_path = RELAY / "module21a_all_pair_relay_coverage.tsv"
    tf_path = RELAY / "module22a_ligand_tf_handoff.tsv"
    reuse_path = RELAY / "module21a_pathway_reuse_registry.tsv"
    detail_path = RELAY / "module21a_pair_relay_evidence_detail.tsv"
    review_path = RELAY / f"module21a_pair_relay_review_batches{tag}.tsv"
    pairs, handoffs = read(pair_path), read(tf_path)
    reuse, detail = read(reuse_path), read(detail_path)
    old_review = read(review_path) if review_path.exists() else []
    old_by_id = {r["review_id"]: r for r in old_review if r.get("review_id")}
    old_reuse = {r["pathway_reuse_key"] for r in old_review if r.get("pathway_reuse_key")}
    old_evidence = {r["evidence_id"] for r in old_review if r.get("evidence_id")}
    source = []
    for batch in args.batches:
        source.extend(normalize(r) for r in read(RELAY / f"module21a_batch{batch}_review.tsv"))
    if not source or len({r["review_id"] for r in source}) != len(source):
        raise SystemExit("input batches must contain unique review IDs")
    pair_by_id = {r["module20a_review_id"]: r for r in pairs}
    handoff_by_pair = {r["pair_key"]: r for r in handoffs}
    assigned = {r["review_id"] for r in source}
    missing = assigned - set(pair_by_id)
    if missing:
        raise SystemExit(f"review IDs absent from scaffold: {sorted(missing)}")
    for rid in assigned:
        pair = pair_by_id[rid]
        for field in ("pathway_reuse_keys", "module21a_edge_ids", "module21a_evidence_ids", "terminal_tf_entities", "module21a_status", "module22a_status", "search_boundary", "curator_notes"):
            pair[field] = ""
        handoff = handoff_by_pair[pair["pair_key"]]
        for field in ("pathway_reuse_keys", "terminal_tf_entities", "module21a_evidence_ids", "handoff_status", "terminal_tf_status", "search_boundary", "limitations"):
            handoff[field] = ""
    reuse = [r for r in reuse if r.get("pathway_reuse_key", "") not in old_reuse]
    detail = [r for r in detail if r.get("evidence_id", "") not in old_evidence]
    used_reuse = {r.get("pathway_reuse_key", "") for r in reuse}
    used_evidence = {r.get("evidence_id", "") for r in detail}
    reuse_n, evidence_n = next_id(used_reuse, "M21A-REUSE-"), next_id(used_evidence, "M21A-PAIR-EVID-")
    detail_fields = ["evidence_id", "pathway_reuse_key", "source_locators", "species", "cell_type_model", "assay_or_perturbation", "relation_type", "evidence_layer", "pathway_branch", "confidence_tier", "evidence_summary", "limitations"]
    review_fields = ["review_id", "pair_key", "pair_label_canonical", "pathway_reuse_key", "evidence_id", "source_locators", "species", "cell_type_model", "assay_or_perturbation", "relation_type", "evidence_layer", "pathway_branch", "confidence_tier", "terminal_tf_entities", "review_status", "curator_note"]
    added_reuse, final = [], []
    for s in source:
        old = old_by_id.get(s["review_id"], {})
        promote = s["review_status"] in {"reviewed_relay_candidate", "reviewed_function_only", "reviewed_scavenging_only"}
        reuse_key = old.get("pathway_reuse_key", "") if promote else ""
        if promote and not reuse_key:
            while f"M21A-REUSE-{reuse_n:04d}" in used_reuse: reuse_n += 1
            reuse_key, reuse_n = f"M21A-REUSE-{reuse_n:04d}", reuse_n + 1
        evidence_id = old.get("evidence_id", "")
        if not evidence_id:
            while f"M21A-PAIR-EVID-{evidence_n:03d}" in used_evidence: evidence_n += 1
            evidence_id, evidence_n = f"M21A-PAIR-EVID-{evidence_n:03d}", evidence_n + 1
        used_reuse.add(reuse_key); used_evidence.add(evidence_id)
        pair = pair_by_id[s["review_id"]]
        pair.update({"pathway_reuse_keys": reuse_key, "module21a_edge_ids": "PENDING_M21A_EDGE_MATERIALIZATION" if promote else "", "module21a_evidence_ids": evidence_id, "terminal_tf_entities": s["terminal_tf_entities"], "module21a_status": s["review_status"], "module22a_status": "candidate_tf_handoff_pending_validation" if s["terminal_tf_entities"] else "no_terminal_tf_evidence", "search_boundary": f"primary_review_batches{tag}; exact pair/family boundary search", "curator_notes": s["curator_note"]})
        handoff = handoff_by_pair[pair["pair_key"]]
        handoff.update({"pathway_reuse_keys": reuse_key, "terminal_tf_entities": s["terminal_tf_entities"], "module21a_evidence_ids": evidence_id, "handoff_status": "pending_tf_program_review" if s["terminal_tf_entities"] else "no_terminal_tf_assigned", "terminal_tf_status": "candidate_or_supported_activation" if s["terminal_tf_entities"] else "none_found", "search_boundary": f"Primary downstream review batches{tag}; exact pair/family boundary search.", "limitations": s["curator_note"]})
        if promote:
            added_reuse.append({"pathway_reuse_key": reuse_key, "source_entity": s["pathway_branch"].split("-", 1)[0], "pathway_name": s["pathway_branch"], "edge_ids": "", "evidence_ids": evidence_id, "target_entities": "", "ligand_pair_count": "1", "ligand_pair_keys": pair["pair_key"], "terminal_tf_entities": s["terminal_tf_entities"], "validation_status": f"reviewed_batches{tag}_candidate", "reuse_rule": "Reuse only when exact ligand/receptor complex, isoform/chain/cofactor, species, cell/model, assay and evidence scope match.", "limitations": s["curator_note"]})
        detail.append({"evidence_id": evidence_id, "pathway_reuse_key": reuse_key, "source_locators": s["source_locators"], "species": s["species"], "cell_type_model": s["cell_type_model"], "assay_or_perturbation": s["assay_or_perturbation"], "relation_type": s["relation_type"], "evidence_layer": s["evidence_layer"], "pathway_branch": s["pathway_branch"], "confidence_tier": s["confidence_tier"], "evidence_summary": s["pathway_branch"], "limitations": s["curator_note"]})
        final.append({"review_id": s["review_id"], "pair_key": pair["pair_key"], "pair_label_canonical": pair["pair_label_canonical"], "pathway_reuse_key": reuse_key, "evidence_id": evidence_id, "source_locators": s["source_locators"], "species": s["species"], "cell_type_model": s["cell_type_model"], "assay_or_perturbation": s["assay_or_perturbation"], "relation_type": s["relation_type"], "evidence_layer": s["evidence_layer"], "pathway_branch": s["pathway_branch"], "confidence_tier": s["confidence_tier"], "terminal_tf_entities": s["terminal_tf_entities"], "review_status": s["review_status"], "curator_note": s["curator_note"]})
    write(pair_path, list(pairs[0]), pairs); write(tf_path, list(handoffs[0]), handoffs); write(reuse_path, list(reuse[0]), reuse + added_reuse); write(detail_path, detail_fields, detail); write(review_path, review_fields, final)
    print(f"integrated {len(final)} pair outcomes, {len(added_reuse)} reusable pathway candidates, and {len(final)} evidence records")


if __name__ == "__main__":
    main()
