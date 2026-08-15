#!/usr/bin/env python3
"""Integrate validated Module21A priority-7 batches 024-025."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
PAIR = RELAY / "module21a_all_pair_relay_coverage.tsv"
TF = RELAY / "module22a_ligand_tf_handoff.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REVIEW = RELAY / "module21a_pair_relay_review_batches024_025.tsv"


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
            "assay_or_perturbation": r.get("assay_perturbation", ""), "relation_type": r.get("relation_type", ""),
            "evidence_layer": r.get("primary_evidence_layer") or r.get("evidence_layer", ""),
            "pathway_branch": r.get("pathway_branch", ""), "confidence_tier": r.get("confidence", ""),
            "terminal_tf_entities": "" if r.get("terminal_TF", "") in {"", "—", "-"} else r["terminal_TF"],
            "review_status": r.get("status", ""), "curator_note": r.get("limitations", "")}


def next_id(values: set[str], prefix: str) -> int:
    nums = []
    for v in values:
        if v.startswith(prefix):
            try:
                nums.append(int(v.rsplit("-", 1)[1]))
            except ValueError:
                pass
    return max(nums, default=0) + 1


def main() -> None:
    pair_rows, tf_rows = read(PAIR), read(TF)
    reuse_rows, detail_rows = read(REUSE), read(DETAIL)
    old_review = read(REVIEW) if REVIEW.exists() else []
    old_by_id = {r["review_id"]: r for r in old_review if r.get("review_id")}
    old_reuse = {r["pathway_reuse_key"] for r in old_review if r.get("pathway_reuse_key")}
    old_evidence = {r["evidence_id"] for r in old_review if r.get("evidence_id")}
    source = []
    for name in ("module21a_batch024_review.tsv", "module21a_batch025_review.tsv"):
        source.extend(normalize(r) for r in read(RELAY / name))
    if len(source) != 50 or len({r["review_id"] for r in source}) != 50:
        raise SystemExit("batches024_025 must contain 50 unique rows")
    pair_by_id = {r["module20a_review_id"]: r for r in pair_rows}
    tf_by_pair = {r["pair_key"]: r for r in tf_rows}
    if not {r["review_id"] for r in source}.issubset(pair_by_id):
        raise SystemExit("review ID missing from pair scaffold")
    for s in source:
        p = pair_by_id[s["review_id"]]
        for field in ("pathway_reuse_keys", "module21a_edge_ids", "module21a_evidence_ids", "terminal_tf_entities", "module21a_status", "module22a_status", "search_boundary", "curator_notes"):
            p[field] = ""
        h = tf_by_pair[p["pair_key"]]
        for field in ("pathway_reuse_keys", "terminal_tf_entities", "module21a_evidence_ids", "handoff_status", "terminal_tf_status", "search_boundary", "limitations"):
            h[field] = ""
    reuse_rows = [r for r in reuse_rows if r.get("pathway_reuse_key", "") not in old_reuse]
    detail_rows = [r for r in detail_rows if r.get("evidence_id", "") not in old_evidence]
    used_reuse = {r.get("pathway_reuse_key", "") for r in reuse_rows}
    used_evidence = {r.get("evidence_id", "") for r in detail_rows}
    reuse_n, evidence_n = next_id(used_reuse, "M21A-REUSE-"), next_id(used_evidence, "M21A-PAIR-EVID-")
    detail_fields = ["evidence_id", "pathway_reuse_key", "source_locators", "species", "cell_type_model", "assay_or_perturbation", "relation_type", "evidence_layer", "pathway_branch", "confidence_tier", "evidence_summary", "limitations"]
    review_fields = ["review_id", "pair_key", "pair_label_canonical", "pathway_reuse_key", "evidence_id", "source_locators", "species", "cell_type_model", "assay_or_perturbation", "relation_type", "evidence_layer", "pathway_branch", "confidence_tier", "terminal_tf_entities", "review_status", "curator_note"]
    new_reuse, final = [], []
    for s in source:
        old = old_by_id.get(s["review_id"], {})
        promote = s["review_status"] in {"reviewed_relay_candidate", "reviewed_function_only", "reviewed_scavenging_only"}
        rk = old.get("pathway_reuse_key", "") if promote else ""
        if promote and not rk:
            while f"M21A-REUSE-{reuse_n:04d}" in used_reuse: reuse_n += 1
            rk, reuse_n = f"M21A-REUSE-{reuse_n:04d}", reuse_n + 1
        eid = old.get("evidence_id", "")
        if not eid:
            while f"M21A-PAIR-EVID-{evidence_n:03d}" in used_evidence: evidence_n += 1
            eid, evidence_n = f"M21A-PAIR-EVID-{evidence_n:03d}", evidence_n + 1
        used_reuse.add(rk); used_evidence.add(eid)
        p = pair_by_id[s["review_id"]]
        p.update({"pathway_reuse_keys": rk, "module21a_edge_ids": "PENDING_M21A_EDGE_MATERIALIZATION" if promote else "", "module21a_evidence_ids": eid,
                  "terminal_tf_entities": s["terminal_tf_entities"], "module21a_status": s["review_status"], "module22a_status": "candidate_tf_handoff_pending_validation" if s["terminal_tf_entities"] else "no_terminal_tf_evidence",
                  "search_boundary": "primary_review_batches024_025; exact family/complex boundary search", "curator_notes": s["curator_note"]})
        h = tf_by_pair[p["pair_key"]]
        h.update({"pathway_reuse_keys": rk, "terminal_tf_entities": s["terminal_tf_entities"], "module21a_evidence_ids": eid,
                  "handoff_status": "pending_tf_program_review" if s["terminal_tf_entities"] else "no_terminal_tf_assigned", "terminal_tf_status": "candidate_or_supported_activation" if s["terminal_tf_entities"] else "none_found",
                  "search_boundary": "Primary downstream review batches024-025; exact family/complex boundary search.", "limitations": s["curator_note"]})
        if promote:
            new_reuse.append({"pathway_reuse_key": rk, "source_entity": s["pathway_branch"].split("-", 1)[0], "pathway_name": s["pathway_branch"], "edge_ids": "", "evidence_ids": eid,
                              "target_entities": "", "ligand_pair_count": "1", "ligand_pair_keys": p["pair_key"], "terminal_tf_entities": s["terminal_tf_entities"], "validation_status": "reviewed_batches024_025_candidate",
                              "reuse_rule": "Reuse only when exact ligand/receptor complex, isoform/chain/cofactor, species, cell/model, assay and evidence scope match.", "limitations": s["curator_note"]})
        detail_rows.append({"evidence_id": eid, "pathway_reuse_key": rk, "source_locators": s["source_locators"], "species": s["species"], "cell_type_model": s["cell_type_model"], "assay_or_perturbation": s["assay_or_perturbation"], "relation_type": s["relation_type"], "evidence_layer": s["evidence_layer"], "pathway_branch": s["pathway_branch"], "confidence_tier": s["confidence_tier"], "evidence_summary": s["pathway_branch"], "limitations": s["curator_note"]})
        final.append({"review_id": s["review_id"], "pair_key": p["pair_key"], "pair_label_canonical": p["pair_label_canonical"], "pathway_reuse_key": rk, "evidence_id": eid, "source_locators": s["source_locators"], "species": s["species"], "cell_type_model": s["cell_type_model"], "assay_or_perturbation": s["assay_or_perturbation"], "relation_type": s["relation_type"], "evidence_layer": s["evidence_layer"], "pathway_branch": s["pathway_branch"], "confidence_tier": s["confidence_tier"], "terminal_tf_entities": s["terminal_tf_entities"], "review_status": s["review_status"], "curator_note": s["curator_note"]})
    write(PAIR, list(pair_rows[0]), pair_rows); write(TF, list(tf_rows[0]), tf_rows); write(REUSE, list(reuse_rows[0]), reuse_rows + new_reuse); write(DETAIL, detail_fields, detail_rows); write(REVIEW, review_fields, final)
    print(f"integrated {len(final)} pair outcomes, {len(new_reuse)} reusable pathway candidates, and {len(final)} evidence records")


if __name__ == "__main__": main()
