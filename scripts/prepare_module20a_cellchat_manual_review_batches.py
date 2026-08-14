#!/usr/bin/env python3
"""Prepare bounded re-review packets for CellChat manual/uncertain pairs."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "module20_db_seed" / "evidence_search_agents"
SOURCE = WORK / "cellchat_remaining_manual_review.tsv"
BATCH = WORK / "cellchat_manual_review_batch_001"


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
    rows = sorted(read(SOURCE), key=lambda row: row["pair_key"])
    if len(rows) != 411 or len({row["pair_key"] for row in rows}) != 411:
        raise SystemExit("expected 411 unique manual/uncertain CellChat rows")
    fields = ["review_id", "pair_key", "pair_label_canonical", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "search_notes", "manual_reason"]
    sizes = [200, 200, 11]
    manifest = []
    offset = 0
    for index, size in enumerate(sizes, 1):
        packet_id = f"M20A-CELLCHAT-MANUAL-{index:02d}"
        packet_rows = [{key: row.get(key, "") for key in fields} for row in rows[offset:offset + size]]
        packet = BATCH / f"{packet_id}.tsv"
        report = BATCH / f"{packet_id}.report.tsv"
        write(packet, fields, packet_rows)
        manifest.append({"packet_id": packet_id, "row_count": str(size), "first_pair_key": packet_rows[0]["pair_key"], "last_pair_key": packet_rows[-1]["pair_key"], "packet_path": str(packet.relative_to(ROOT)), "report_path": str(report.relative_to(ROOT)), "status": "assigned"})
        offset += size
    write(BATCH / "manifest.tsv", list(manifest[0]), manifest)
    (BATCH / "worker_contract.md").write_text(
        """# CellChat manual/uncertain re-review contract

Re-review every submitted pair from scratch, prioritizing exact primary
literature and authoritative receptor-complex sources. Search canonical names,
aliases, processed ligand forms, receptor chains/complexes, and species. Open
the cited sources rather than relying on search-result snippets. Distinguish
direct binding, receptor activation, adhesion, receptor-dependent function,
family/pathway evidence, expression-only evidence, and wrong-pair notation.

Return exactly one row per input in identical order with this header:
`review_id\tpair_key\tpair_label_canonical\tfinal_class\tsource_locators\tspecies_support\tsupport_kind\tevidence_summary\tlimitations\treview_notes`

Allowed `final_class` values: `promote_medium`, `promote_low`, `retain_manual`,
`no_evidence`, `non_ligand_receptor`. Use `promote_medium` only for direct,
replicated, exact-pair evidence sufficient to move beyond low evidence. Use
`promote_low` for a real but contextual or species/complex-limited pair. Use
`no_evidence` only when the expanded review finds no qualifying support. Use
`non_ligand_receptor` only for a wrong relationship or invalid LR notation.
Every promotion must include stable PMID, PMCID, DOI, or authoritative URL
locators and state the exact assay or functional result. Do not edit canonical
ledgers.
""",
        encoding="utf-8",
    )
    print(f"prepared {len(rows)} manual/uncertain rows across {len(sizes)} packets")


if __name__ == "__main__":
    main()
