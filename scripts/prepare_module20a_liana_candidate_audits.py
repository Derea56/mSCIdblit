#!/usr/bin/env python3
"""Prepare citation-level audits for remaining-LIANA promote candidates."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "module20_db_seed"
SOURCE = WORK / "evidence_search_agents" / "liana_remaining_batch_001"
BATCH = WORK / "evidence_search_agents" / "liana_candidate_audit_001"
SIZES = [60, 60, 60, 26]
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
    candidates = []
    for path in sorted(SOURCE.glob("M20A-LIANA-REMAINING-*.report.tsv")):
        candidates.extend({
            "pair_key": row["pair_key"],
            "pair_label_canonical": row["pair_label_canonical"],
            "agent_verdict": row["verdict"],
            "source_locators": row["source_locators"],
            "species_support": row["species_support"],
            "support_kind": row["support_kind"],
            "evidence_summary": row["evidence_summary"],
            "limitations": row["limitations"],
            "search_notes": row["search_notes"],
        } for row in read(path) if row["verdict"] == "promote_candidate")
    candidates.sort(key=lambda row: row["pair_key"])
    expected = sum(SIZES)
    if len(candidates) != expected:
        raise SystemExit(f"expected {expected} candidates, found {len(candidates)}")
    manifest = []
    offset = 0
    for index, size in enumerate(SIZES, 1):
        packet_id = f"M20A-LIANA-AUDIT-{index:02d}"
        rows = candidates[offset:offset + size]
        packet = BATCH / f"{packet_id}.tsv"
        report = BATCH / f"{packet_id}.report.tsv"
        write(packet, FIELDS, rows)
        manifest.append({"packet_id": packet_id, "row_count": str(size), "first_pair_key": rows[0]["pair_key"], "last_pair_key": rows[-1]["pair_key"], "packet_path": str(packet.relative_to(ROOT)), "report_path": str(report.relative_to(ROOT)), "status": "assigned"})
        offset += size
    write(BATCH / "manifest.tsv", list(manifest[0]), manifest)
    (BATCH / "worker_contract.md").write_text(
        """# Remaining LIANA candidate citation-audit contract

Audit every proposed candidate by opening the cited primary paper(s) or exact
source. Confirm that the submitted ligand and receptor pair—not merely a
family, pathway, subunit, processed fragment, or related receptor—is actually
tested. Confirm assay type, species, receptor complex/chain notation, and
whether the result is direct binding, adhesion, receptor activation, or
receptor-dependent function.

Return exactly one row per input to the matching `.report.tsv` with header:
`pair_key\tpair_label_canonical\tfinal_verdict\tsource_locators\tspecies_support\tsupport_kind\tevidence_summary\tlimitations\taudit_notes`

Allowed final verdicts: `approve_candidate`, `retain_low`, `no_evidence`,
`reject_pair`, `needs_manual_review`. Approve only exact-pair primary evidence
with a usable citation. Retain low for real but contextual or unresolved
evidence. Use no_evidence when the cited source does not support the pair. Use
reject_pair only when the submitted relationship is wrong or not ligand–receptor.
Do not edit canonical ledgers.
""",
        encoding="utf-8",
    )
    print(f"prepared {expected} candidate audits across {len(SIZES)} packets")


if __name__ == "__main__":
    main()
