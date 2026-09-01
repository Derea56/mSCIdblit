#!/usr/bin/env python3
"""Integrate the second bounded medium-to-high Module 20A LR packet."""

from __future__ import annotations

import csv
import io
import json
from datetime import UTC, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_router"
STARTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_starter"
B_DIR = ROOT / "work" / "module_b_consolidation" / "module20b"
QUEUE = ROUTER / "module20a_external_review_queue.tsv"
A_EVIDENCE = STARTER / "module20a_medium_direct_high_batch002_evidence_register.tsv"
A_DECISIONS = STARTER / "module20a_medium_direct_high_batch002_decision_register.tsv"
A_SUMMARY = STARTER / "module20a_medium_direct_high_batch002_summary.json"
B_EDGES = B_DIR / "module20b_edge_register.tsv"
B_EVIDENCE = B_DIR / "module20b_evidence_register.tsv"
B_AUDIT = B_DIR / "module20b_medium_direct_high_batch002_2026_09_01.tsv"

SELECTED = {
    "M20A-EXT-2115", "M20A-EXT-2121", "M20A-EXT-2122", "M20A-EXT-2129",
    "M20A-EXT-2134", "M20A-EXT-2137", "M20A-EXT-2138", "M20A-EXT-2139",
    "M20A-EXT-2143", "M20A-EXT-2159", "M20A-EXT-2160", "M20A-EXT-2162",
    "M20A-EXT-2185", "M20A-EXT-2186", "M20A-EXT-2188", "M20A-EXT-2189",
    "M20A-EXT-2198", "M20A-EXT-2200", "M20A-EXT-2207", "M20A-EXT-2209",
    "M20A-EXT-2215", "M20A-EXT-2216", "M20A-EXT-2228", "M20A-EXT-2238",
    "M20A-EXT-2250", "M20A-EXT-2261", "M20A-EXT-2281", "M20A-EXT-2381",
    "M20A-EXT-2418", "M20A-EXT-2437", "M20A-EXT-2444", "M20A-EXT-2447",
}

A_EVIDENCE_FIELDS = [
    "evidence_item_id", "review_id", "pair_key", "pair_label", "source_kind",
    "source_locator", "support_kind", "species_support", "source_scope",
    "confidence_tier", "citation_note", "evidence_summary", "limitations",
]
A_DECISION_FIELDS = [
    "review_id", "pair_key", "pair_label_canonical", "review_status",
    "confidence_decision", "mouse_confidence", "mouse_confidence_rank",
    "human_confidence", "human_confidence_rank", "human_evidence_present",
    "receptor_state", "receptor_role", "directness", "species_posture",
    "decision_basis", "evidence_register_ids", "next_action",
]
B_AUDIT_FIELDS = [
    "review_id", "pair_key", "pair_label_canonical", "b_edge_id",
    "b_primary_evidence_id", "a_evidence_id", "previous_edge_confidence",
    "previous_edge_exportable", "previous_frozen_evidence_confidence",
    "new_edge_confidence", "new_frozen_evidence_confidence", "decision_basis",
]

BASIS = (
    "Exact pair-specific primary direct-molecular evidence was validated at high "
    "tier in Module 20B. High applies to the ligand-receptor or explicitly "
    "preserved receptor-complex claim only; receptor topology, cofactor, isoform, "
    "ligand-form, species, assay, and non-SCI limitations remain explicit. No "
    "relay, TF/program, cellular-output, or SCI context is inferred."
)


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    old_endings: list[str] = []
    old_contents: list[str] = []
    if path.exists():
        for line in path.read_bytes().splitlines(keepends=True):
            old_endings.append("\r\n" if line.endswith(b"\r\n") else "\n")
            old_contents.append(line.rstrip(b"\r\n").decode("utf-8"))
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    generated = buffer.getvalue().splitlines()
    default_ending = old_endings[-1] if old_endings else "\n"
    with path.open("w", encoding="utf-8", newline="") as handle:
        for index, line in enumerate(generated):
            unchanged = index < len(old_contents) and line == old_contents[index]
            ending = old_endings[index] if unchanged and index < len(old_endings) else default_ending
            handle.write(line + ending)


def append_once(existing: str, note: str) -> str:
    return existing if note in existing else f"{existing} {note}".strip()


def species_confidence(species_support: str, species: str) -> tuple[str, str]:
    if species.casefold() in species_support.casefold():
        return "high", "3"
    return "uncertain", "0"


def main() -> None:
    queue_fields, queue_rows = read_tsv(QUEUE)
    queue = {row["review_id"]: row for row in queue_rows}
    if SELECTED - set(queue):
        raise SystemExit(f"selected rows missing from queue: {sorted(SELECTED - set(queue))}")
    if any(queue[aid]["confidence_decision"] != "medium" for aid in SELECTED):
        raise SystemExit("selected rows are not all still medium in the Module 20A queue")

    edge_fields, edge_rows = read_tsv(B_EDGES)
    evidence_fields, evidence_rows = read_tsv(B_EVIDENCE)
    edges = {row["source_a_edge_id"]: row for row in edge_rows}
    frozen = {
        row["source_a_evidence_id"]: row
        for row in evidence_rows
        if row["source_kind"] == "frozen_module20a_lr_release"
    }
    direct: dict[str, dict[str, str]] = {}
    for row in evidence_rows:
        aid = row["source_a_evidence_id"]
        if aid not in SELECTED:
            continue
        if (
            row["evidence_layer"] == "ligand_receptor_or_direct_molecular"
            and row["confidence_tier"].casefold() == "high"
            and row["exportable"].casefold() == "true"
            and row["b_evidence_id"].endswith("P2-DIRECT")
        ):
            if aid in direct:
                raise SystemExit(f"multiple exact direct records for {aid}; review manually")
            direct[aid] = row
    if SELECTED - set(edges) or SELECTED - set(frozen) or SELECTED - set(direct):
        raise SystemExit("selected row missing B edge, frozen evidence, or exact direct evidence")
    if any(edges[aid]["confidence_tier"] != "medium" or edges[aid]["exportable"] != "true" for aid in SELECTED):
        raise SystemExit("selected B edges are not all medium/exportable")
    if any(frozen[aid]["confidence_tier"] != "medium" for aid in SELECTED):
        raise SystemExit("selected frozen LR evidence is not all medium")

    a_evidence_rows = []
    a_decision_rows = []
    audit_rows = []
    for index, aid in enumerate(sorted(SELECTED), start=1):
        q = queue[aid]
        primary = direct[aid]
        frozen_row = frozen[aid]
        evidence_id = f"M20A-MEDHIGH002-EVID-{index:04d}"
        mouse, mouse_rank = species_confidence(primary["species_support"], "mouse")
        human, human_rank = species_confidence(primary["species_support"], "human")
        limitations = (
            f"{primary['limitations']} High is limited to the exact LR or preserved "
            "receptor-complex claim; no SCI-context or downstream relay inference is made."
        ).strip()
        a_evidence_rows.append({
            "evidence_item_id": evidence_id,
            "review_id": aid,
            "pair_key": q["pair_key"],
            "pair_label": q["pair_label_canonical"],
            "source_kind": "primary_literature_recovery",
            "source_locator": primary["source_locator"],
            "support_kind": primary["support_kind"],
            "species_support": primary["species_support"],
            "source_scope": "module20b_exact_primary_packet_reused_for_module20a_adjudication",
            "confidence_tier": "high",
            "citation_note": primary["citation_note"],
            "evidence_summary": primary["evidence_summary"],
            "limitations": limitations,
        })
        a_decision_rows.append({
            "review_id": aid,
            "pair_key": q["pair_key"],
            "pair_label_canonical": q["pair_label_canonical"],
            "review_status": "reviewed",
            "confidence_decision": "high",
            "mouse_confidence": mouse,
            "mouse_confidence_rank": mouse_rank,
            "human_confidence": human,
            "human_confidence_rank": human_rank,
            "human_evidence_present": "yes" if human == "high" else "no",
            "receptor_state": "membrane_bound_or_receptor_complex_context",
            "receptor_role": "ligand_receptor_or_receptor_complex_context",
            "directness": "exact_primary_direct_molecular_or_preserved_complex",
            "species_posture": "species_scoped_to_exact_primary_packet; no_unlisted_species_inference",
            "decision_basis": f"{BASIS} Source packet: {primary['b_evidence_id']}.",
            "evidence_register_ids": evidence_id,
            "next_action": "retain_high_ligand_receptor_evidence; preserve_complex_and_context; keep_relay_and_SCI_fields_separate",
        })
        audit_rows.append({
            "review_id": aid,
            "pair_key": q["pair_key"],
            "pair_label_canonical": q["pair_label_canonical"],
            "b_edge_id": edges[aid]["b_edge_id"],
            "b_primary_evidence_id": primary["b_evidence_id"],
            "a_evidence_id": evidence_id,
            "previous_edge_confidence": edges[aid]["confidence_tier"],
            "previous_edge_exportable": edges[aid]["exportable"],
            "previous_frozen_evidence_confidence": frozen_row["confidence_tier"],
            "new_edge_confidence": "high",
            "new_frozen_evidence_confidence": "high",
            "decision_basis": BASIS,
        })

        q["confidence_decision"] = "high"
        q["evidence_register_ids"] = ";".join(
            part for part in (q["evidence_register_ids"].strip(), evidence_id) if part
        )
        q["curator_notes"] = append_once(
            q["curator_notes"],
            "Medium-direct-high batch002: exact primary direct or explicitly preserved complex evidence adjudicated high for LR evidence only; downstream and SCI context remain separate.",
        )
        edge = edges[aid]
        edge.update({
            "confidence_tier": "high",
            "export_priority": "high",
            "exportable": "true",
            "consolidation_note": append_once(
                edge["consolidation_note"],
                "Medium-direct-high batch002: exact primary LR or preserved-complex evidence promoted; topology and context boundaries retained.",
            ),
        })
        frozen_row.update({
            "confidence_tier": "high",
            "exportable": "true",
            "consolidation_note": append_once(
                frozen_row["consolidation_note"],
                "Medium-direct-high batch002: exact primary LR or preserved-complex evidence promoted; topology and context boundaries retained.",
            ),
        })

    write_tsv(A_EVIDENCE, A_EVIDENCE_FIELDS, a_evidence_rows)
    write_tsv(A_DECISIONS, A_DECISION_FIELDS, a_decision_rows)
    write_tsv(QUEUE, queue_fields, queue_rows)
    write_tsv(B_EDGES, edge_fields, edge_rows)
    write_tsv(B_EVIDENCE, evidence_fields, evidence_rows)
    write_tsv(B_AUDIT, B_AUDIT_FIELDS, audit_rows)
    summary = {
        "generated_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "batch_id": "module20a_medium_direct_high_batch002",
        "rows_reviewed": len(SELECTED),
        "rows_promoted_to_high": len(SELECTED),
        "module20b_edges_promoted": len(SELECTED),
        "module20b_frozen_lr_evidence_promoted": len(SELECTED),
        "signaling_edges_created": 0,
        "excluded_known_provenance_collision": "M20A-EXT-2329",
        "policy": BASIS,
        "selected_review_ids": sorted(SELECTED),
    }
    A_SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
