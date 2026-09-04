#!/usr/bin/env python3
"""Create a conservative disposition ledger for unlinked Module 22A candidates.

This is a local-register review. It does not claim that a candidate has no
supporting literature; it records why the current Module 22B export gate did
not produce an exact reusable high-confidence link. The blocker tags are
derived only from the candidate's recorded search boundary and limitations.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT / "work/module21_relay/module22a_ligand_tf_handoff.tsv"
LINKS = ROOT / "work/module22a_22b_promotion_audit/module22a_22b_high_confidence_links.tsv"
EVIDENCE_DETAIL = ROOT / "work/module21_relay/module21a_pair_relay_evidence_detail.tsv"
OUT_TSV = ROOT / "work/module22a_22b_promotion_audit/module22a_pending_candidate_dispositions.tsv"
OUT_MD = ROOT / "docs/MODULE22A_PENDING_CANDIDATE_DISPOSITION_2026-09-02.md"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def blocker_tags(row: dict[str, str]) -> list[str]:
    boundary = row["search_boundary"].lower()
    limitations = row["limitations"].lower()
    tags: list[str] = []

    if any(
        token in limitations
        for token in (
            "receptor complex",
            "receptor-complex",
            "receptor pair",
            "receptor-specific",
            "receptor composition",
            "heterodimer",
            "subunit",
            "standalone",
            "isolated",
            "composite",
            "biosynthetic enzyme",
            "biosynthetic",
            "enzyme that",
            "enzyme controlling",
            "flux",
            "receptor-use",
            "no direct",
        )
    ):
        tags.append("receptor_or_composite_boundary")

    if any(
        token in limitations
        for token in (
            "ligand",
            "family relay",
            "family-level",
            "exact ligand",
            "ligand-specific",
            "ligand specificity",
            "mature e2",
            "other ligand",
            "promiscuous",
        )
    ):
        tags.append("ligand_or_family_specificity_boundary")

    if any(
        token in limitations
        for token in (
            "tf identity unresolved",
            "terminal tf",
            "candidate",
            "provisional",
            "no pair-specific tf assay",
            "direct tf causality is unresolved",
            "exact target",
            "target gene",
            "target specificity",
            "no tf-target evidence",
        )
    ) or "tf target-program search remains separate" in boundary:
        tags.append("tf_or_target_assignment_unresolved")

    if any(token in limitations for token in ("program", "phenotype", "downstream")):
        tags.append("program_or_function_level_boundary")

    if any(
        token in limitations
        for token in (
            "cell context",
            "cell-specific",
            "cell type",
            "cell",
            "tissue",
            "species",
            "stage",
            "model",
            "context",
        )
    ):
        tags.append("model_or_context_boundary")

    if "exact pair/family boundary search" in boundary or "exact" in limitations:
        tags.append("exact_pair_or_family_review_required")

    if any(token in limitations for token in ("cleaved", "full-length precursor", "molecular form")):
        tags.append("molecular_form_boundary")

    if not tags:
        tags.append("no_explicit_local_blocker_tag")
    return tags


def main() -> None:
    handoffs = read_tsv(HANDOFF)
    links = read_tsv(LINKS)
    evidence_detail = {row["evidence_id"]: row for row in read_tsv(EVIDENCE_DETAIL)}
    linked = {row["handoff_id"] for row in links}
    linked_pending = {
        row["handoff_id"]
        for row in links
        if any(
            handoff["module22a_handoff_id"] == row["handoff_id"]
            and handoff["handoff_status"] == "pending_tf_program_review"
            for handoff in handoffs
        )
    }
    candidates = [
        row
        for row in handoffs
        if row["handoff_status"] == "pending_tf_program_review"
        and row["module22a_handoff_id"] not in linked
    ]
    candidates.sort(key=lambda row: row["module22a_handoff_id"])
    missing_evidence = [
        row["module21a_evidence_ids"]
        for row in candidates
        if row["module21a_evidence_ids"] not in evidence_detail
    ]
    if missing_evidence:
        raise ValueError(f"Missing local evidence packets: {missing_evidence}")

    fields = [
        "module22a_handoff_id",
        "pair_label_canonical",
        "terminal_tf_entities",
        "module21a_evidence_ids",
        "source_locators",
        "source_species",
        "source_cell_type_model",
        "source_assay_or_perturbation",
        "source_relation_type",
        "source_evidence_layer",
        "source_confidence_tier",
        "source_evidence_summary",
        "source_limitations",
        "source_review_status",
        "search_boundary",
        "limitations",
        "disposition",
        "blocker_tags",
    ]
    OUT_TSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        for row in candidates:
            tags = blocker_tags(row)
            source = evidence_detail[row["module21a_evidence_ids"]]
            writer.writerow(
                {
                    "module22a_handoff_id": row["module22a_handoff_id"],
                    "pair_label_canonical": row["pair_label_canonical"],
                    "terminal_tf_entities": row["terminal_tf_entities"],
                    "module21a_evidence_ids": row["module21a_evidence_ids"],
                    "source_locators": source["source_locators"],
                    "source_species": source["species"],
                    "source_cell_type_model": source["cell_type_model"],
                    "source_assay_or_perturbation": source["assay_or_perturbation"],
                    "source_relation_type": source["relation_type"],
                    "source_evidence_layer": source["evidence_layer"],
                    "source_confidence_tier": source["confidence_tier"],
                    "source_evidence_summary": source["evidence_summary"],
                    "source_limitations": source["limitations"],
                    "source_review_status": "mapped_to_local_primary_source_packet",
                    "search_boundary": row["search_boundary"],
                    "limitations": row["limitations"],
                    "disposition": "not_promoted_under_current_strict_gate",
                    "blocker_tags": ";".join(tags),
                }
            )

    tag_counts = Counter(tag for row in candidates for tag in blocker_tags(row))
    source_confidence_counts = Counter(
        evidence_detail[row["module21a_evidence_ids"]]["confidence_tier"].strip() or "unreported"
        for row in candidates
    )
    lines = [
        "# Module 22A Pending Candidate Disposition",
        "",
        "This ledger records the disposition of every pending Module 22A handoff",
        "that remains unlinked after the high-confidence linkage audit. It is a",
        "local-register review, not a claim that these candidates have no relevant",
        "literature. Each row preserves the source handoff's search boundary and",
        "limitation text so a future primary-source search can resume without",
        "silently broadening the evidence gate.",
        "",
        "## Review scope",
        "",
        f"- Pending handoffs before linkage: {sum(row['handoff_status'] == 'pending_tf_program_review' for row in handoffs)}",
        f"- Handoffs represented by the linkage audit: {len(linked)} ({len(linked_pending)} were pending handoffs)",
        f"- Unlinked pending handoffs reviewed here: {len(candidates)}",
        f"- Distinct local evidence packets represented: {len({row['module21a_evidence_ids'] for row in candidates})}",
        "- Evidence-packet mapping completeness: 100% (no candidate lacked a local packet)",
        "- Disposition for every row: `not_promoted_under_current_strict_gate`",
        "",
        "The strict gate requires an exact handoff-to-22B match, an exportable",
        "high-confidence 22B edge, and exportable high-confidence evidence or a",
        "reviewed primary extraction. No row below satisfied all three conditions",
        "in the current register. The tags are lexical summaries of observed local",
        "boundary/limitation text; multiple tags may apply to one row.",
        "",
        "## Blocker-tag counts",
        "",
        "| Tag | Rows |",
        "|---|---:|",
    ]
    for tag, count in sorted(tag_counts.items()):
        lines.append(f"| `{tag}` | {count} |")
    lines.extend(
        [
            "",
            "## Source-packet confidence counts",
            "",
            "These counts summarize the confidence field already recorded in the",
            "Module 21A evidence-detail register; they are not new confidence calls.",
            "",
            "| Recorded source confidence | Rows |",
            "|---|---:|",
        ]
    )
    for confidence, count in sorted(source_confidence_counts.items()):
        lines.append(f"| `{confidence}` | {count} |")
    lines.extend(
        [
            "",
            "## Candidate ledger",
            "",
            "The complete machine-readable ledger is [the TSV disposition file](../work/module22a_22b_promotion_audit/module22a_pending_candidate_dispositions.tsv). The table below lists every candidate and its local blocker tags; the TSV retains the full boundary and limitation text.",
            "",
            "| Handoff | Pair | Terminal TF field | Blocker tags |",
            "|---|---|---|---|",
        ]
    )
    for row in candidates:
        tags = "; ".join(f"`{tag}`" for tag in blocker_tags(row))
        lines.append(
            f"| {row['module22a_handoff_id']} | {row['pair_label_canonical']} | {row['terminal_tf_entities'] or '—'} | {tags} |"
        )
    OUT_MD.write_text("\n".join(lines) + "\n")
    print(f"reviewed={len(candidates)} linked_handoffs={len(linked)}")
    print("tag_counts=" + ",".join(f"{tag}:{count}" for tag, count in sorted(tag_counts.items())))


if __name__ == "__main__":
    main()
