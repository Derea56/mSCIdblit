#!/usr/bin/env python3
"""Prepare bounded packets for LIANA pairs not yet resolved in mSCIdblit."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "module20_db_seed"
ROUTER = WORK / "evidence_escalation_router"
COMPARISON = ROUTER / "module20a_cellchat_liana_pair_comparison.tsv"
QUEUE = ROUTER / "module20a_external_review_queue.tsv"
BATCH = WORK / "evidence_search_agents" / "liana_remaining_batch_001"
SIZES = [200, 200, 200, 199]
FIELDS = ["pair_key", "pair_label_canonical", "liana_status", "module20a_status", "review_id", "current_confidence", "prior_notes"]


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    comparison = read(COMPARISON)
    queue = {row["pair_key"]: row for row in read(QUEUE)}
    selected = []
    for row in comparison:
        if row["in_liana_consensus"] != "yes":
            continue
        q = queue.get(row["pair_key"])
        # Include LIANA pairs outside the queue and the queue's unresolved
        # uncertain pairs. Already searched low/no-evidence pairs are excluded.
        if q is None or q["confidence_decision"] == "uncertain":
            selected.append({
                "pair_key": row["pair_key"],
                "pair_label_canonical": row["pair_label_canonical"],
                "liana_status": "liana_consensus",
                "module20a_status": row["in_module20a"],
                "review_id": q["review_id"] if q else "",
                "current_confidence": q["confidence_decision"] if q else "unreviewed",
                "prior_notes": q["curator_notes"] if q else "not_in_module20a_review_queue",
            })
    selected.sort(key=lambda row: row["pair_key"])
    expected = sum(SIZES)
    if len(selected) != expected:
        raise SystemExit(f"expected exactly {expected} remaining LIANA rows, found {len(selected)}")
    manifest = []
    offset = 0
    for index, size in enumerate(SIZES, 1):
        packet_id = f"M20A-LIANA-REMAINING-{index:02d}"
        rows = selected[offset:offset + size]
        packet = BATCH / f"{packet_id}.tsv"
        report = BATCH / f"{packet_id}.report.tsv"
        write(packet, FIELDS, rows)
        manifest.append({"packet_id": packet_id, "row_count": str(size), "first_pair_key": rows[0]["pair_key"], "last_pair_key": rows[-1]["pair_key"], "packet_path": str(packet.relative_to(ROOT)), "report_path": str(report.relative_to(ROOT)), "status": "assigned"})
        offset += size
    write(BATCH / "manifest.tsv", list(manifest[0]), manifest)
    (BATCH / "worker_contract.md").write_text(
        """# Remaining LIANA evidence-search contract

Search each assigned LIANA ligand–receptor pair thoroughly. Expand official
and historical gene/protein aliases, mature or processed ligand forms,
receptor subunits/holoreceptors, co-receptors, heterodimers, species names,
full-text primary papers, structural studies, receptor reconstitution,
binding, activation, adhesion, and receptor-dependent function. Follow
citation trails from relevant primary papers and reviews.

PubMed and Europe PMC are required; reviews, LIANA, CellChat, GtoPdb,
ConnectomeDB, UniProt, Reactome, and structure databases are discovery leads.
Do not transfer family, expression, pathway, or database evidence to the exact
pair. Return exactly one TSV row per input to the matching `.report.tsv`:
`pair_key\tpair_label_canonical\tverdict\tsource_locators\tspecies_support\tsupport_kind\tevidence_summary\tlimitations\tsearch_notes`

Allowed verdicts: `promote_candidate`, `needs_manual_review`, `hold_low`,
`no_evidence`, `reject_pair`. Use promote_candidate only for exact submitted
pair primary evidence; no_evidence only after expanded searches; reject_pair
only for wrong/non-ligand-receptor relationships; hold_low for concrete but
unresolved evidence. Do not edit canonical ledgers.
""",
        encoding="utf-8",
    )
    print(f"prepared {expected} remaining LIANA rows across {len(SIZES)} packets")


if __name__ == "__main__":
    main()
