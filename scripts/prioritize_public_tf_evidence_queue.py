#!/usr/bin/env python3
"""Build a reproducible, pair-level priority queue for public-TF evidence review.

The queue is a search-planning artifact only. It does not promote rows or write
canonical/module records. Historical evidence rows and source provenance are
aggregated without discarding source-level identifiers or citations.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


PAIR_FILES_GLOB = "batch_*/public_tf_evidence_review_batch*_pairs.tsv"


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip()).casefold()


def unique_values(values: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        value = (value or "").strip()
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def split_values(values: list[str]) -> list[str]:
    result: list[str] = []
    for value in values:
        result.extend(part.strip() for part in value.split(";") if part.strip())
    return unique_values(result)


def contains_any(text: str, terms: tuple[str, ...]) -> bool:
    text = norm(text)
    return any(term in text for term in terms)


DATABASE_ONLY_EVIDENCE_TERMS = (
    "database",
    "dataset",
    "profile",
    "membership",
    "target_set",
    "gtrd",
    "genome_wide_binding",
    "source_page_unavailable",
    "no_traceable",
)


def is_database_only_evidence_type(value: str) -> bool:
    return contains_any(value, DATABASE_ONLY_EVIDENCE_TERMS)


def load_promoted_tiers(path: Path) -> dict[tuple[str, str, str], set[str]]:
    if not path.exists():
        return {}
    result: dict[tuple[str, str, str], set[str]] = {}
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            key = (norm(row.get("regulator_symbol", "")), norm(row.get("target_symbol", "")), norm(row.get("species_scope", "")))
            result.setdefault(key, set()).add(row.get("evidence_weight_tier", "").strip())
    return result


def load_search_outcomes(path: Path) -> dict[tuple[str, str, str], list[dict[str, str]]]:
    if not path.exists():
        return {}
    result: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    with path.open(newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            key = (norm(row.get("regulator_symbol", "")), norm(row.get("target_symbol", "")), norm(row.get("species_scope", "")))
            result.setdefault(key, []).append(row)
    return result


def evidence_confidence_tier(
    key: tuple[str, str, str],
    rows: list[dict[str, str]],
    promoted_tiers: dict[tuple[str, str, str], set[str]],
    search_outcomes: dict[tuple[str, str, str], list[dict[str, str]]],
) -> tuple[str, str]:
    """Add an evidence tier without replacing the queue's priority tier.

    D is intentionally narrow: database/profile/membership evidence without a
    pair-specific literature or functional outcome. E marks reviewed rows that
    retain literature, functional, directional, species, identity, or other
    nonpromotable evidence. U is reserved for rows lacking a review record.
    """
    if not rows or not all(row.get("review_id", "").strip() for row in rows):
        return "U_unreviewed", "no complete pair-review record is present"

    tiers = promoted_tiers.get(key, set())
    for tier in ("A_independent_literature_corroborated", "B_independent_literature_single_source", "C_tflink_source_table_only"):
        if tier in tiers:
            return tier, "promoted overlay evidence tier"

    outcomes = search_outcomes.get(key, [])
    if outcomes:
        types = [row.get("evidence_type", "") for row in outcomes]
        if all(is_database_only_evidence_type(value) for value in types):
            return "D_database_only_no_pair_evidence", "completed search found only database/profile/membership evidence"
        return "E_reviewed_nonpromotable", "completed search recorded literature, functional, or near-match evidence but not a promotable exact edge"

    status_text = " ".join(row.get("exact_pair_status", "") for row in rows)
    citations = " ".join(
        row.get(field, "")
        for row in rows
        for field in ("primary_citation", "corroborating_citation")
    )
    if contains_any(status_text, ("no_exact_pair", "database_membership", "binding_profile", "binding_dataset", "membership_only")) and not citations.strip():
        return "D_database_only_no_pair_evidence", "no pair-specific citation or functional outcome was recorded"
    return "E_reviewed_nonpromotable", "held row has contextual, directional, species, identity, or other nonpromotable evidence"


def score_and_route(rows: list[dict[str, str]], promoted: bool, searched: bool) -> dict[str, object]:
    statuses = [row.get("exact_pair_status", "") for row in rows]
    dispositions = [row.get("disposition", "") for row in rows]
    binding = [row.get("binding_or_association_status", "") for row in rows]
    downstream = [row.get("downstream_expression_or_perturbation_status", "") for row in rows]
    exclusions = [row.get("near_match_exclusions", "") for row in rows]
    status_text = " ".join(statuses)
    all_text = " ".join(statuses + dispositions + binding + downstream + exclusions)

    if promoted:
        return {
            "priority_score": 0,
            "priority_tier": "Z_already_promoted",
            "search_lane": "promoted_followup_queue",
            "active_search_eligible": "false",
            "queue_state": "already_promoted_followup",
            "next_action": "Use the dedicated promotion follow-up queue; do not duplicate pair-level searching here.",
        }

    if searched:
        return {
            "priority_score": 0,
            "priority_tier": "Y_searched_pending_adjudication",
            "search_lane": "outcome_adjudication",
            "active_search_eligible": "false",
            "queue_state": "searched_pending_adjudication",
            "next_action": "Adjudicate the logged outcome; do not repeat the search until the review or promotion state changes.",
        }

    if contains_any(all_text, ("identity_unresolved", "unresolved identity", "identity review hold")):
        return {
            "priority_score": 0,
            "priority_tier": "D_identity_hold",
            "search_lane": "identity_resolution",
            "active_search_eligible": "false",
            "queue_state": "blocked_until_identity_resolved",
            "next_action": "Resolve the literal regulator identity from authoritative nomenclature records before searching the edge.",
        }

    if contains_any(all_text, ("reverse_direction", "cross_species", "ortholog", "paralog", "near_match", "fusion", "viral")):
        return {
            "priority_score": 8,
            "priority_tier": "D_direction_or_species_hold",
            "search_lane": "direction_species_adjudication",
            "active_search_eligible": "false",
            "queue_state": "hold_near_match",
            "next_action": "Verify direction, species, paralog, and model before considering any exact-edge search.",
        }

    score = 18
    has_functional_status = contains_any(status_text, ("functional",))
    has_direct_edge_status = contains_any(status_text, ("direct_binding", "direct_binding_reporter", "exact_locus"))
    directness_disclaimed = contains_any(
        status_text,
        ("without_direct_binding", "without_direct_occupancy", "no_direct_binding", "not_direct_binding"),
    )

    if has_functional_status:
        score = 88
        tier = "A_functional_exact_edge"
        lane = "noncanonical_mechanism_upgrade"
    elif has_direct_edge_status and not directness_disclaimed:
        score = 78
        tier = "A_direct_exact_edge"
        lane = "exact_edge_upgrade"
    elif contains_any(status_text, ("perturbation", "expression_only_exact_pair")):
        score = 64
        tier = "B_exact_edge_functional_gap"
        lane = "exact_edge_upgrade"
    elif contains_any(status_text, ("binding_profile", "occupancy", "chromatin_resource", "gtrd_promoter", "profile_membership")):
        score = 44
        tier = "C_profile_to_exact_validation"
        lane = "profile_to_exact_validation"
    elif contains_any(status_text, ("no_exact_pair", "database_membership", "membership_only", "machinery_database")):
        score = 6
        tier = "E_database_or_no_exact_pair"
        lane = "database_only_archive"
    else:
        tier = "C_bounded_review_needed"
        lane = "bounded_exact_pair_review"

    if any(norm(value) for value in binding) and contains_any(" ".join(binding), ("direct", "chip", "occupancy", "association", "binding")):
        score += 8
    if contains_any(" ".join(downstream), ("perturb", "knockdown", "knockout", "changed", "expression", "reporter", "rescue", "stability", "activation", "m6a")):
        score += 8
    if any("pubmed" in norm(value) or "pmc" in norm(value) or "doi" in norm(value) for row in rows for value in (row.get("primary_citation", ""),)):
        score += 4
    if any(row.get("corroborating_citation", "").strip() for row in rows):
        score += 6

    if tier.startswith("A"):
        next_action = "Search for an independent primary source or orthogonal assay, then reassess catalog promotion."
    elif tier.startswith("B"):
        next_action = "Search for direct locus/RNA/protein association or a regulator-specific perturbation with direction."
    elif tier.startswith("C_profile"):
        next_action = "Retrieve the source-level target-locus call and seek orthogonal validation; keep profile membership separate."
    elif tier.startswith("C"):
        next_action = "Perform one bounded exact-pair search using the literal queue symbols and record a source-backed outcome."
    else:
        next_action = "Retain provenance and do not spend manual search time unless a new primary source is identified."

    return {
        "priority_score": min(score, 100),
        "priority_tier": tier,
        "search_lane": lane,
        "active_search_eligible": "true" if tier[0] in {"A", "B", "C"} else "false",
        "queue_state": "active_search" if tier[0] in {"A", "B", "C"} else "archive_or_hold",
        "next_action": next_action,
    }


def load_promoted(path: Path) -> set[tuple[str, str, str]]:
    if not path.exists():
        return set()
    with path.open(newline="") as handle:
        return {
            (norm(row.get("regulator_symbol", "")), norm(row.get("target_symbol", "")), norm(row.get("species_scope", "")))
            for row in csv.DictReader(handle, delimiter="\t")
        }


def load_searched(path: Path) -> set[tuple[str, str, str]]:
    if not path.exists():
        return set()
    with path.open(newline="") as handle:
        return {
            (norm(row.get("regulator_symbol", "")), norm(row.get("target_symbol", "")), norm(row.get("species_scope", "")))
            for row in csv.DictReader(handle, delimiter="\t")
            if norm(row.get("search_status", "")) in {"completed", "adjudicated"}
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Defaults to the comprehensive interaction promotion directory.",
    )
    parser.add_argument("--batch-size", type=int, default=25, help="Number of active pairs copied into the next search packet.")
    args = parser.parse_args()

    repo_root = args.repo_root.resolve()
    evidence_root = repo_root / "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches"
    output_dir = args.output_dir or repo_root / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1"
    output_dir.mkdir(parents=True, exist_ok=True)

    promoted_path = output_dir / "promoted_interactions.tsv"
    promoted_keys = load_promoted(promoted_path)
    promoted_tiers = load_promoted_tiers(promoted_path)
    outcome_path = output_dir / "evidence_search_outcomes.tsv"
    searched_keys = load_searched(outcome_path)
    search_outcomes = load_search_outcomes(outcome_path)

    groups: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    input_files: list[str] = []
    row_count = 0
    for path in sorted(evidence_root.glob(PAIR_FILES_GLOB)):
        input_files.append(str(path.relative_to(repo_root)))
        with path.open(newline="") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                row_count += 1
                key = (norm(row.get("regulator_symbol", "")), norm(row.get("target_symbol", "")), norm(row.get("species_scope", "")))
                groups.setdefault(key, []).append(row)

    queue_rows: list[dict[str, str]] = []
    for key, rows in groups.items():
        first = rows[0]
        promoted = key in promoted_keys
        searched = key in searched_keys
        decision = score_and_route(rows, promoted, searched)
        evidence_tier, evidence_tier_basis = evidence_confidence_tier(key, rows, promoted_tiers, search_outcomes)
        review_status = "reviewed" if all(row.get("review_id", "").strip() for row in rows) else "unreviewed"
        citations = split_values([row.get("primary_citation", "") for row in rows] + [row.get("corroborating_citation", "") for row in rows])
        queue_rows.append(
            {
                "queue_key": "|".join(key),
                "regulator_symbol": first.get("regulator_symbol", ""),
                "target_symbol": first.get("target_symbol", ""),
                "species_scope": first.get("species_scope", ""),
                "target_graph_modules": ";".join(split_values([row.get("target_graph_modules", "") for row in rows])),
                "provenance_row_count": str(len(rows)),
                "source_registries": ";".join(split_values([row.get("source_registry", "") for row in rows])),
                "source_record_ids": ";".join(split_values([row.get("source_record_id", "") for row in rows])),
                "review_ids": ";".join(split_values([row.get("review_id", "") for row in rows])),
                "search_outcome_status": "completed_or_adjudicated" if searched else "not_yet_logged",
                "exact_pair_statuses": ";".join(unique_values([row.get("exact_pair_status", "") for row in rows])),
                "primary_and_corroborating_citations": ";".join(citations),
                "dispositions": ";".join(unique_values([row.get("disposition", "") for row in rows])),
                "review_status": review_status,
                "evidence_confidence_tier": evidence_tier,
                "evidence_tier_basis": evidence_tier_basis,
                **{k: str(v) for k, v in decision.items()},
            }
        )

    queue_rows.sort(key=lambda row: (-int(row["priority_score"]), row["priority_tier"], row["queue_key"]))
    for rank, row in enumerate(queue_rows, start=1):
        row["priority_rank"] = str(rank)

    fieldnames = [
        "priority_rank", "priority_score", "priority_tier", "search_lane", "active_search_eligible", "queue_state",
        "queue_key", "regulator_symbol", "target_symbol", "species_scope", "target_graph_modules",
        "provenance_row_count", "source_registries", "source_record_ids", "review_ids", "exact_pair_statuses",
        "primary_and_corroborating_citations", "dispositions", "review_status", "evidence_confidence_tier", "evidence_tier_basis",
        "search_outcome_status", "next_action",
    ]
    queue_path = output_dir / "evidence_priority_queue.tsv"
    with queue_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(queue_rows)

    packet_rows = [row for row in queue_rows if row["active_search_eligible"] == "true"][: args.batch_size]
    packet_path = output_dir / "evidence_search_batch_001.tsv"
    with packet_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(packet_rows)

    tier_counts = Counter(row["priority_tier"] for row in queue_rows)
    lane_counts = Counter(row["search_lane"] for row in queue_rows)
    active_rows = [row for row in queue_rows if row["active_search_eligible"] == "true"]
    summary = {
        "status": "pass",
        "input_file_count": len(input_files),
        "input_row_count": row_count,
        "unique_pair_count": len(queue_rows),
        "already_promoted_pair_count": sum(row["queue_state"] == "already_promoted_followup" for row in queue_rows),
        "searched_pending_adjudication_pair_count": sum(row["queue_state"] == "searched_pending_adjudication" for row in queue_rows),
        "active_search_pair_count": len(active_rows),
        "priority_tier_counts": dict(sorted(tier_counts.items())),
        "search_lane_counts": dict(sorted(lane_counts.items())),
        "evidence_confidence_tier_counts": dict(sorted(Counter(row["evidence_confidence_tier"] for row in queue_rows).items())),
        "review_status_counts": dict(sorted(Counter(row["review_status"] for row in queue_rows).items())),
        "top_active_pairs": [
            {key: row[key] for key in ("priority_rank", "priority_score", "regulator_symbol", "target_symbol", "species_scope", "search_lane", "next_action")}
            for row in active_rows[:25]
        ],
        "outputs": [str(queue_path.relative_to(repo_root)), str(packet_path.relative_to(repo_root)), str(outcome_path.relative_to(repo_root))],
        "policy": [
            "This queue is for search prioritization and does not promote or materialize records.",
            "Already promoted pairs are routed to the dedicated follow-up queue.",
            "Unresolved, reverse-direction, cross-species, and database-only findings remain visible but are not active manual-search priorities.",
            "All source registries, source record IDs, review IDs, statuses, citations, and module hints are retained.",
            "Completed searches are read from evidence_search_outcomes.tsv and removed from the next active packet until adjudicated.",
            "Evidence-confidence tiers are exhaustive: A/B/C are promoted tiers, D is database/profile-only without pair-specific evidence, E is reviewed but nonpromotable, and U is unreviewed.",
        ],
    }
    if not outcome_path.exists():
        outcome_path.write_text(
            "outcome_id\tqueue_key\tregulator_symbol\ttarget_symbol\tspecies_scope\tsearch_query\tsource_citations\tevidence_type\toutcome_summary\tdisposition\tsearch_status\n",
            encoding="utf-8",
        )
    summary_path = output_dir / "evidence_priority_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({**summary, "outputs": [str(queue_path), str(packet_path), str(outcome_path), str(summary_path)]}, indent=2))


if __name__ == "__main__":
    main()
