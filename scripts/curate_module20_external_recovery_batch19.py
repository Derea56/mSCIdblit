#!/usr/bin/env python3
"""Integrate the 1,000-row parallel Module 20A recovery round (0801-1800)."""

from __future__ import annotations

import csv
from pathlib import Path

from curate_module20_external_batch1 import decision, evidence, write_tsv

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_router"
STARTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_starter"
QUEUE = ROUTER / "module20a_external_review_queue.tsv"
EVIDENCE = STARTER / "module20a_external_recovery_batch19_evidence_register.tsv"
DECISIONS = STARTER / "module20a_external_recovery_batch19_decision_register.tsv"
STATUS = ROUTER / "module20a_external_review_queue_status_summary.tsv"


def expand(ranges: list[tuple[int, int]]) -> set[int]:
    return {n for start, end in ranges for n in range(start, end + 1)}


# The first worker packet had a deliberately conservative split: canonical
# database-only candidates are low, while rows without pair-specific support
# remain uncertain.  No high-confidence calls were made in this slice.
PLANCK_LOW = expand(
    [
        (811, 820), (825, 832), (837, 844), (846, 857), (892, 894),
        (914, 917), (922, 924), (927, 928), (932, 937), (947, 949),
        (966, 968), (979, 980), (1045, 1050),
    ]
)
PLANCK_LOW.update({803, 806, 808, 822, 879, 888, 897, 898, 901, 902, 905, 943, 944, 985, 993, 1021, 1022, 1043, 1044})


def range_values(ranges: list[tuple[int, int]], value: tuple[str, str, str]) -> dict[int, tuple[str, str, str]]:
    return {n: value for n in expand(ranges)}


BOYLE_OVERRIDES: dict[int, tuple[str, str, str]] = {}
BOYLE_OVERRIDES.update(range_values([(1552, 1552), (1591, 1591), (1664, 1664), (1665, 1666), (1670, 1673), (1746, 1748)], ("low", "low", "medium")))
BOYLE_OVERRIDES.update(range_values([(1577, 1577), (1621, 1621), (1667, 1667), (1669, 1669), (1674, 1675), (1678, 1678), (1680, 1681), (1754, 1755), (1757, 1760), (1766, 1768), (1777, 1779), (1780, 1783), (1785, 1788), (1789, 1796)], ("medium", "medium", "medium")))
BOYLE_OVERRIDES.update(range_values([(1572, 1572)], ("uncertain", "uncertain", "uncertain")))
BOYLE_OVERRIDES.update(range_values([(1574, 1574), (1590, 1590), (1592, 1593), (1598, 1598), (1699, 1699), (1721, 1721), (1740, 1742), (1749, 1752)], ("high", "high", "high")))
BOYLE_OVERRIDES.update({1698: ("high", "medium", "high"), 1800: ("high", "high", "medium")})
BOYLE_OVERRIDES.update(range_values([(1651, 1659), (1682, 1683), (1689, 1693)], ("low", "low", "low")))


def packet_for(n: int) -> tuple[str, str]:
    if n <= 1050:
        return "ligand_candidate", "parallel_worker_batch19_rows_0801_1050;LIANA:mouseconsensus.tsv;CellChatDB"
    if n <= 1300:
        return "chemokine_complex", "parallel_worker_batch19_rows_1051_1300;LIANA:mouseconsensus.tsv"
    if n <= 1550:
        return "liana_consensus", "parallel_worker_batch19_rows_1301_1550;LIANA:mouseconsensus.tsv"
    return "coagulation_fgf_tgfb", "parallel_worker_batch19_rows_1551_1800;LIANA:mouseconsensus.tsv;pair-specific literature citations in worker packet"


def confidence_for(n: int) -> tuple[str, str, str]:
    if n <= 1050:
        return ("low", "low", "uncertain") if n in PLANCK_LOW else ("uncertain", "uncertain", "uncertain")
    if n <= 1550:
        return ("low", "low", "uncertain")
    return BOYLE_OVERRIDES.get(n, ("low", "low", "uncertain"))


def main() -> None:
    with QUEUE.open(newline="") as handle:
        queue = list(csv.DictReader(handle, delimiter="\t"))

    evidence_rows: list[dict[str, str]] = []
    decisions: list[dict[str, str]] = []
    for row in queue:
        n = int(row["review_id"].split("-")[-1])
        if not (801 <= n <= 1800):
            continue
        # Do not overwrite an earlier targeted packet if the round is rerun.
        if not row["evidence_register_ids"].startswith("M20A-EXTC"):
            continue
        overall, mouse, human = confidence_for(n)
        packet, locator = packet_for(n)
        key = row["pair_key"]
        label = key.title()
        eid = f"M20A-EXT19-EVID-{len(decisions) + 1:04d}"
        if overall == "high":
            basis = "Parallel worker packet found pair-specific anchor evidence sufficient for a high-confidence call; retain the cited species and complex/context caveats."
        elif overall == "medium":
            basis = "Parallel worker packet found family- or pair-level support sufficient for a medium-confidence call; preserve complex, cofactor, and context caveats."
        elif overall == "low":
            basis = "Parallel worker packet retained the database candidate as biologically plausible, but did not provide enough pair-specific evidence for medium confidence."
        else:
            basis = "Parallel worker packet did not establish pair-specific support beyond a database or indirect candidate; retain uncertain pending a cleaner evidence packet."
        limitation = "This batch is a triage-level recovery pass; database consensus, expression, uptake, shared subunits, and indirect associations are not treated as direct binding evidence."
        evidence_rows.append(
            evidence(
                eid,
                row["review_id"],
                key,
                label,
                "parallel_primary_literature_triage",
                locator,
                "worker_packet_review",
                "mouse_and_human_comparator",
                "direct_edge" if overall in {"medium", "high"} else "negative_triage",
                overall,
                basis,
                basis,
                limitation,
            )
        )
        decisions.append(
            decision(
                row["review_id"],
                key,
                label,
                overall,
                mouse,
                human,
                "membrane_bound",
                "parallel_worker_review",
                "worker_packet_review",
                "conservative_species_reconciliation",
                basis,
                eid,
                "Retain assigned confidence and preserve worker-level species, complex, isoform, cofactor, and indirectness caveats.",
            )
        )

    write_tsv(EVIDENCE, evidence_rows)
    write_tsv(DECISIONS, decisions)
    updates = {row["review_id"]: row for row in decisions}
    for row in queue:
        update = updates.get(row["review_id"])
        if update:
            row["review_status"] = "reviewed"
            row["confidence_decision"] = update["confidence_decision"]
            row["evidence_register_ids"] = update["evidence_register_ids"]
            row["curator_notes"] = update["decision_basis"]

    fields = list(queue[0])
    with QUEUE.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(queue)

    grouped: dict[tuple[str, str, str], int] = {}
    rationale: dict[str, str] = {}
    for row in queue:
        key = (row["review_priority"], row["review_status"], row["confidence_decision"])
        grouped[key] = grouped.get(key, 0) + 1
        rationale[row["review_priority"]] = row["review_priority_rationale"]
    write_tsv(
        STATUS,
        [
            {
                "review_priority": priority,
                "review_priority_rationale": rationale[priority],
                "review_status": status,
                "confidence_decision": confidence,
                "pair_count": str(count),
            }
            for (priority, status, confidence), count in sorted(grouped.items(), key=lambda item: (int(item[0][0]), item[0][1], item[0][2]))
        ],
    )
    print(f"wrote {len(evidence_rows)} evidence rows and {len(decisions)} decisions")


if __name__ == "__main__":
    main()
