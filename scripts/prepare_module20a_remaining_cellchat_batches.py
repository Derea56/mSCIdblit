#!/usr/bin/env python3
"""Prepare bounded packets for unresolved CellChat ligand-receptor pairs."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "module20_db_seed"
ROUTER = WORK / "evidence_escalation_router"
COMPARISON = ROUTER / "module20a_cellchat_liana_pair_comparison.tsv"
QUEUE = ROUTER / "module20a_external_review_queue.tsv"
LOW = ROUTER / "module20a_low_evidence_registry.tsv"
NO = ROUTER / "module20a_no_evidence_registry.tsv"
NON = ROUTER / "module20a_non_ligand_receptor_registry.tsv"
BATCH = WORK / "evidence_search_agents" / "cellchat_remaining_batch_001"
FIELDS = ["pair_key", "pair_label_canonical", "cellchat_status", "module20a_status", "review_id", "current_confidence", "prior_notes"]


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
    classified = {row["pair_key"] for path in (LOW, NO, NON) for row in read(path)}
    selected = []
    for row in comparison:
        if row["in_cellchat_full"] != "yes" or row["pair_key"] in classified:
            continue
        q = queue.get(row["pair_key"])
        if q is None or q["confidence_decision"] == "uncertain":
            selected.append({
                "pair_key": row["pair_key"],
                "pair_label_canonical": row["pair_label_canonical"],
                "cellchat_status": "cellchat_full",
                "module20a_status": row["in_module20a"],
                "review_id": q["review_id"] if q else "",
                "current_confidence": q["confidence_decision"] if q else "unreviewed",
                "prior_notes": q["curator_notes"] if q else "not_in_module20a_review_queue",
            })
    selected.sort(key=lambda row: row["pair_key"])
    sizes = [200] * (len(selected) // 200)
    if len(selected) % 200:
        sizes.append(len(selected) % 200)
    manifest = []
    offset = 0
    for index, size in enumerate(sizes, 1):
        packet_id = f"M20A-CELLCHAT-REMAINING-{index:02d}"
        rows = selected[offset:offset + size]
        packet = BATCH / f"{packet_id}.tsv"
        report = BATCH / f"{packet_id}.report.tsv"
        write(packet, FIELDS, rows)
        manifest.append({"packet_id": packet_id, "row_count": str(size), "first_pair_key": rows[0]["pair_key"], "last_pair_key": rows[-1]["pair_key"], "packet_path": str(packet.relative_to(ROOT)), "report_path": str(report.relative_to(ROOT)), "status": "assigned"})
        offset += size
    write(BATCH / "manifest.tsv", list(manifest[0]), manifest)
    (BATCH / "worker_contract.md").write_text(
        """# Remaining CellChat evidence-search contract

Search each assigned CellChat ligand–receptor pair thoroughly. Expand official
and historical gene/protein aliases, mature or processed ligand forms,
receptor subunits/holoreceptors, co-receptors, heterodimers, species names,
full-text primary papers, structural studies, receptor reconstitution,
binding, activation, adhesion, and receptor-dependent function. Follow
citation trails from relevant primary papers and reviews.

PubMed and Europe PMC are required; CellChat, LIANA, GtoPdb, ConnectomeDB,
UniProt, Reactome, reviews, and structure databases are discovery leads.
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
    print(f"prepared {len(selected)} unresolved CellChat rows across {len(sizes)} packets")


if __name__ == "__main__":
    main()
