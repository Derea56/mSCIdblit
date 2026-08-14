#!/usr/bin/env python3
"""Prepare an independent audit of CellChat-full non-LR classifications."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "module20_db_seed"
ROUTER = WORK / "evidence_escalation_router"
BATCH = WORK / "evidence_search_agents" / "cellchat_nonlr_audit_batch_001"


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
    comparison = {row["pair_key"] for row in read(ROUTER / "module20a_cellchat_liana_pair_comparison.tsv") if row["in_cellchat_full"] == "yes"}
    fields = ["review_id", "pair_key", "pair_label_canonical", "initial_source_locators", "initial_support_kind", "initial_evidence_summary", "initial_limitations", "initial_decision_basis"]
    rows = [{key: row.get(key, "") for key in fields} for row in read(ROUTER / "module20a_non_ligand_receptor_registry.tsv") if row["pair_key"] in comparison]
    rows.sort(key=lambda row: row["pair_key"])
    if len(rows) != 397 or len({row["pair_key"] for row in rows}) != 397:
        raise SystemExit(f"expected 397 unique CellChat-full non-LR rows, found {len(rows)}")
    sizes = [200, 197]
    manifest = []
    offset = 0
    for index, size in enumerate(sizes, 1):
        packet_id = f"M20A-CELLCHAT-NONLR-AUDIT-{index:02d}"
        packet_rows = rows[offset:offset + size]
        packet = BATCH / f"{packet_id}.tsv"
        report = BATCH / f"{packet_id}.report.tsv"
        write(packet, fields, packet_rows)
        manifest.append({"packet_id": packet_id, "row_count": str(size), "first_pair_key": packet_rows[0]["pair_key"], "last_pair_key": packet_rows[-1]["pair_key"], "packet_path": str(packet.relative_to(ROOT)), "report_path": str(report.relative_to(ROOT)), "status": "assigned"})
        offset += size
    write(BATCH / "manifest.tsv", list(manifest[0]), manifest)
    (BATCH / "worker_contract.md").write_text(
        """# CellChat non-LR audit contract

Independently audit every submitted CellChat-full pair. Determine whether the
relationship is truly invalid ligand-receptor notation, or whether it is a
valid ligand-receptor edge obscured by processed ligand biology, receptor
complexes, adhesion/co-receptor notation, isoforms, or a database naming issue.
Search PubMed, Europe PMC, and authoritative receptor/complex resources; open
the source rather than relying on snippets. Search canonical names, aliases,
processed forms, receptor chains, complexes, binding, activation, adhesion,
and receptor-dependent function.

Return exactly one row per input in identical order with header:
`review_id\tpair_key\tpair_label_canonical\tfinal_class\tsource_locators\tspecies_support\tsupport_kind\tevidence_summary\tlimitations\treview_notes`

Allowed `final_class` values: `retain_non_ligand_receptor`, `restore_low`,
`restore_medium`, `retain_manual`. Use `restore_low` only when the exact
relationship is a real but contextual/complex-limited LR edge. Use
`restore_medium` only for direct, exact-pair primary evidence. Use
`retain_manual` when the relationship may be valid but the exact entity or
complex remains unresolved. Every restoration must include stable PMID,
PMCID, DOI, or authoritative URL locators and explain the exact evidence.
Do not edit canonical ledgers.
""",
        encoding="utf-8",
    )
    print(f"prepared {len(rows)} CellChat-full non-LR audit rows across {len(sizes)} packets")


if __name__ == "__main__":
    main()
