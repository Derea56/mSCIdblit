#!/usr/bin/env python3
"""Prepare audits for CellChat candidates added by the final search wave."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "module20_db_seed"
SOURCE = WORK / "evidence_search_agents" / "cellchat_remaining_batch_001"
DONE = WORK / "evidence_search_agents" / "cellchat_candidate_audit_001"
BATCH = WORK / "evidence_search_agents" / "cellchat_candidate_audit_002"
FIELDS = ["pair_key", "pair_label_canonical", "agent_verdict", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "search_notes"]


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
    done = set()
    for path in DONE.glob("M20A-CELLCHAT-AUDIT-*.report.tsv"):
        done.update(row["pair_key"] for row in read(path))
    candidates = []
    for path in sorted(SOURCE.glob("M20A-CELLCHAT-REMAINING-*.report.tsv")):
        for row in read(path):
            if row["verdict"] == "promote_candidate" and row["pair_key"] not in done:
                candidates.append({
                    "pair_key": row["pair_key"], "pair_label_canonical": row["pair_label_canonical"], "agent_verdict": row["verdict"],
                    "source_locators": row["source_locators"], "species_support": row["species_support"], "support_kind": row["support_kind"],
                    "evidence_summary": row["evidence_summary"], "limitations": row["limitations"], "search_notes": row["search_notes"],
                })
    candidates.sort(key=lambda row: row["pair_key"])
    if len(candidates) != 126:
        raise SystemExit(f"expected 126 missing candidates, found {len(candidates)}")
    sizes = [60, 60, 6]
    manifest = []
    offset = 0
    for index, size in enumerate(sizes, 1):
        packet_id = f"M20A-CELLCHAT-MISSING-AUDIT-{index:02d}"
        rows = candidates[offset:offset + size]
        packet = BATCH / f"{packet_id}.tsv"
        report = BATCH / f"{packet_id}.report.tsv"
        write(packet, FIELDS, rows)
        manifest.append({"packet_id": packet_id, "row_count": str(size), "first_pair_key": rows[0]["pair_key"], "last_pair_key": rows[-1]["pair_key"], "packet_path": str(packet.relative_to(ROOT)), "report_path": str(report.relative_to(ROOT)), "status": "assigned"})
        offset += size
    write(BATCH / "manifest.tsv", list(manifest[0]), manifest)
    (BATCH / "worker_contract.md").write_text(
        """# CellChat missing-candidate citation-audit contract

Audit every candidate by opening the cited primary source(s). Confirm exact
ligand-receptor identity, assay, species, receptor complex/chain, and whether
the result is binding, adhesion, receptor activation, or receptor-dependent
function rather than family/pathway/expression-only evidence.

Return exactly one row per input in identical order with header:
`pair_key\tpair_label_canonical\tfinal_verdict\tsource_locators\tspecies_support\tsupport_kind\tevidence_summary\tlimitations\taudit_notes`

Allowed final verdicts: `approve_candidate`, `retain_low`, `no_evidence`,
`reject_pair`, `needs_manual_review`. Do not edit canonical ledgers.
""",
        encoding="utf-8",
    )
    print(f"prepared {len(candidates)} missing candidate audits across {len(sizes)} packets")


if __name__ == "__main__":
    main()
