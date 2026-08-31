#!/usr/bin/env python3
"""Route Module 20A evidence rows into fast/medium/hard work tiers."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


OUTPUT_HEADERS = [
    "source_queue",
    "source_record_id",
    "source_database",
    "pair_label",
    "matched_families",
    "module20a_bucket",
    "species_note",
    "next_action",
    "database_evidence",
    "database_citation_status",
    "audit_status",
    "reusable_packet_status",
    "reusable_family_packets",
    "reusable_evidence_item_ids",
    "routing_tier",
    "routing_rank",
    "routing_flags",
    "routing_rationale",
    "recommended_workflow",
    "source_lookup_artifact",
]

PAIR_HEADERS = [
    "pair_label",
    "source_count",
    "source_databases",
    "best_routing_tier",
    "best_routing_rank",
    "has_audited_packet",
    "has_reusable_packet",
    "row_level_tiers",
    "row_level_record_ids",
    "routing_flags_union",
    "reusable_family_packets",
]

QUEUE_SPECS = [
    (
        "connectomedb_keep_direct_seed_review_then_primary",
        "ConnectomeDB2025",
        "work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/priority_queues/01_keep_direct_seed_review_then_primary.tsv",
        "connectome",
    ),
    (
        "connectomedb_keep_direct_seed_with_caution_review_then_primary",
        "ConnectomeDB2025",
        "work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/priority_queues/02_keep_direct_seed_with_caution_review_then_primary.tsv",
        "connectome",
    ),
    (
        "connectomedb_primary_first",
        "ConnectomeDB2025",
        "work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/priority_queues/04_primary_first.tsv",
        "connectome",
    ),
    (
        "overnight_keep_direct_seed_review_then_primary",
        "overnight_consolidated",
        "work/module20_db_seed/overnight_runs_v2/review_slices_consolidated/priority_queues/01_keep_direct_seed_review_then_primary.tsv",
        "overnight",
    ),
    (
        "overnight_keep_direct_seed_with_caution_review_then_primary",
        "overnight_consolidated",
        "work/module20_db_seed/overnight_runs_v2/review_slices_consolidated/priority_queues/02_keep_direct_seed_with_caution_review_then_primary.tsv",
        "overnight",
    ),
    (
        "overnight_primary_first",
        "overnight_consolidated",
        "work/module20_db_seed/overnight_runs_v2/review_slices_consolidated/priority_queues/04_primary_first.tsv",
        "overnight",
    ),
]

def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=root / "work" / "module20_db_seed" / "evidence_escalation_router",
        help="Destination directory for routing outputs.",
    )
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def split_terms(value: str) -> list[str]:
    return [term.strip() for term in value.split(";") if term.strip()]


def canonicalize_pair_label(value: str) -> str:
    normalized = re.sub(r"<[^>]+>", "", value or "")
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized.casefold()


def load_audited_pairs(starter_dir: Path) -> set[str]:
    audited: set[str] = set()
    for path in sorted(starter_dir.glob("*_audit.tsv")):
        for row in read_tsv(path):
            audited.add(canonicalize_pair_label(row["pair_label"]))
    return audited


def load_gtopdb_lookup(root: Path) -> dict[str, dict[str, str]]:
    path = root / "work" / "module20_db_seed" / "gtopdb_module20_priority_seeds" / "gtopdb_endogenous_module20_priority.tsv"
    lookup: dict[str, dict[str, str]] = {}
    for row in read_tsv(path):
        lookup[row["source_record_id"]] = row
    return lookup


def load_cellchat_lookup(root: Path) -> dict[str, dict[str, str]]:
    lookup: dict[str, dict[str, str]] = {}
    base = root / "work" / "module20_db_seed" / "overnight_runs_v2"
    for subdir in ["cellchat_mouse_secreted_signaling/chunks", "cellchat_mouse_ecm_receptor/chunks"]:
        for path in sorted((base / subdir).glob("chunk_*.tsv")):
            for row in read_tsv(path):
                if row["source_record_id"] not in lookup:
                    lookup[row["source_record_id"]] = {
                        **row,
                        "_source_lookup_artifact": str(path.relative_to(root)),
                    }
    return lookup


def load_reuse_registry(starter_dir: Path) -> dict[str, list[dict[str, str]]]:
    path = starter_dir / "module20a_citation_reuse_registry.tsv"
    lookup: dict[str, list[dict[str, str]]] = defaultdict(list)
    if not path.exists():
        return lookup
    for row in read_tsv(path):
        lookup[canonicalize_pair_label(row["pair_label"])].append(row)
    return lookup


def normalize_queue_row(
    row: dict[str, str],
    *,
    queue_name: str,
    source_type: str,
    root: Path,
    gtopdb_lookup: dict[str, dict[str, str]],
    cellchat_lookup: dict[str, dict[str, str]],
    audited_pairs: set[str],
    reuse_registry: dict[str, list[dict[str, str]]],
) -> dict[str, str]:
    if source_type == "connectome":
        record_id = row["interaction_id"]
        pair_label = row["lr_pair"]
        database_evidence = row.get("evidence", "")
        lookup_artifact = "work/module20_db_seed/connectomedb_mouse_priority_direct_microchunks/validated/review_slices/all_rows.tsv"
        source_database = "ConnectomeDB2025"
    else:
        record_id = row["source_record_id"]
        pair_label = row["pair_label"]
        source_database = record_id.split(":", 1)[0]
        if source_database == "GtoPdb":
            source_database = "GuideToPharmacology"
            seed_row = gtopdb_lookup.get(record_id, {})
            database_evidence = seed_row.get("interaction_pmids", "") or seed_row.get("rank_potency_pmids", "")
            lookup_artifact = "work/module20_db_seed/gtopdb_module20_priority_seeds/gtopdb_endogenous_module20_priority.tsv"
        elif source_database == "CellChat":
            seed_row = cellchat_lookup.get(record_id, {})
            database_evidence = seed_row.get("evidence", "")
            lookup_artifact = seed_row.get("_source_lookup_artifact", "work/module20_db_seed/overnight_runs_v2/cellchat_mouse_secreted_signaling/chunks/")
        else:
            database_evidence = ""
            lookup_artifact = ""

    canonical_pair = canonicalize_pair_label(pair_label)
    reuse_rows = reuse_registry.get(canonical_pair, [])

    return {
        "source_queue": queue_name,
        "source_record_id": record_id,
        "source_database": source_database,
        "pair_label": pair_label,
        "matched_families": row["matched_families"],
        "module20a_bucket": row["module20a_bucket"],
        "species_note": row["species_note"],
        "next_action": row["next_action"],
        "database_evidence": database_evidence,
        "database_citation_status": citation_status(database_evidence),
        "audit_status": "audited_packet_logged" if canonical_pair in audited_pairs else "not_yet_audited",
        "reusable_packet_status": "family_packet_available" if reuse_rows else "no_reusable_packet",
        "reusable_family_packets": ";".join(sorted({row["family_packet_id"] for row in reuse_rows})),
        "reusable_evidence_item_ids": ";".join(
            sorted(
                {
                    item_id
                    for row in reuse_rows
                    for item_id in split_terms(row["supporting_evidence_item_ids"])
                }
            )
        ),
        "source_lookup_artifact": lookup_artifact,
    }


def citation_status(value: str) -> str:
    normalized = (value or "").strip()
    if not normalized or normalized == "Direct":
        return "no_local_citation"
    if "PMID" in normalized.upper():
        return "pmid_present"
    return "non_pmid_reference_only"


def classify_row(row: dict[str, str]) -> dict[str, str]:
    pair = row["pair_label"]
    lower_pair = pair.lower()
    families = set(split_terms(row["matched_families"]))
    bucket = row["module20a_bucket"]
    species_note = row["species_note"].lower()
    flags: list[str] = []
    rationale: list[str] = []
    canonical_fast_families = {
        "chemokine_family",
        "growth_factor_family",
        "tnf_family",
        "il_family",
        "interferon_family",
        "complement_family",
        "guidance_ecm_family",
    }

    if row["audit_status"] == "audited_packet_logged":
        flags.append("already_audited")
        rationale.append("pair already has a logged evidence packet")

    if row["database_citation_status"] == "pmid_present":
        flags.append("database_pmid_present")
    elif row["database_citation_status"] == "non_pmid_reference_only":
        flags.append("database_non_pmid_reference_only")
    else:
        flags.append("no_local_database_citation")

    if row["reusable_packet_status"] == "family_packet_available":
        flags.append("reusable_family_packet_available")
        rationale.append("pair already maps to a logged reusable family packet")

    if bucket == "keep_direct_seed_with_caution":
        flags.append("caution_bucket")
        rationale.append("row is already in keep_direct_seed_with_caution")
    elif bucket == "boundary_review":
        flags.append("boundary_bucket")
        rationale.append("row is already in boundary_review")

    if "ortholog" in species_note or "human_only" in species_note:
        flags.append("species_or_orthology_caution")
        rationale.append("species note already carries orthology or non-mouse caution")

    if "ackr" in lower_pair or "ccrl" in lower_pair:
        flags.append("atypical_or_decoy_receptor")
        rationale.append("pair includes an atypical or decoy-like receptor")

    if "damp_purinergic_tlr_family" in families or re.search(r"\btlr\d", lower_pair):
        flags.append("damp_tlr_axis")
        rationale.append("DAMP/TLR-axis rows usually need bespoke mechanistic review")

    if "_" in pair or "," in pair:
        flags.append("complex_or_multicomponent_receptor")
        rationale.append("pair label suggests a receptor complex or multicomponent edge")

    if "slitrk" in lower_pair or "ptprd" in lower_pair or "ptprs" in lower_pair:
        flags.append("family_structured_synaptic_packet")
        rationale.append("current packet is likely structured at the family or synaptic-adhesion level")

    if pair.startswith("C3 ") and "Cr2" in pair:
        flags.append("complement_fragment_specificity")
        rationale.append("best direct packet is usually fragment-specific (C3d/CR2)")

    if pair.startswith("C4"):
        flags.append("complement_fragment_specificity")
        rationale.append("complement rows may require fragment-specific directness handling")

    if "soluble" in row["source_queue"].lower():
        flags.append("possible_soluble_context")

    if row["source_database"] == "ConnectomeDB2025":
        flags.append("connectome_seed_without_local_citation_packet")
        if row["database_citation_status"] == "no_local_citation":
            rationale.append("Connectome direct-seed row still lacks a local pair-linked citation packet")

    if bucket == "keep_direct_seed" and families & canonical_fast_families and "_" not in pair and "," not in pair:
        flags.append("canonical_simple_family_row")

    hard_flags = {
        "boundary_bucket",
        "atypical_or_decoy_receptor",
        "damp_tlr_axis",
        "complex_or_multicomponent_receptor",
    }
    medium_flags = {
        "caution_bucket",
        "species_or_orthology_caution",
        "family_structured_synaptic_packet",
        "complement_fragment_specificity",
        "connectome_seed_without_local_citation_packet",
    }

    if any(flag in hard_flags for flag in flags):
        tier = "hard"
        rank = "3"
        workflow = "skip default fast path; use family-aware review plus targeted primary escalation before confidence promotion"
    elif any(flag in medium_flags for flag in flags):
        tier = "medium"
        rank = "2"
        workflow = "run database-citation fast path first, then add one targeted follow-up source only if the direct packet stays ambiguous"
    else:
        tier = "fast"
        rank = "1"
        workflow = "use database-linked citation or reusable family anchor first and avoid broad bespoke searching unless directness breaks"

    if not rationale:
        rationale.append("canonical direct-seed row with no immediate red flags")

    routed = dict(row)
    routed["routing_tier"] = tier
    routed["routing_rank"] = rank
    routed["routing_flags"] = ";".join(sorted(set(flags)))
    routed["routing_rationale"] = " | ".join(rationale)
    routed["recommended_workflow"] = workflow
    return routed


def make_pair_rollup(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["pair_label"]].append(row)

    rank_order = {"fast": 1, "medium": 2, "hard": 3}
    rollup_rows: list[dict[str, str]] = []
    for pair_label, pair_rows in sorted(grouped.items()):
        best = min(pair_rows, key=lambda row: rank_order[row["routing_tier"]])
        rollup_rows.append(
            {
                "pair_label": pair_label,
                "source_count": str(len(pair_rows)),
                "source_databases": ";".join(sorted({row["source_database"] for row in pair_rows})),
                "best_routing_tier": best["routing_tier"],
                "best_routing_rank": str(rank_order[best["routing_tier"]]),
                "has_audited_packet": "yes" if any(row["audit_status"] == "audited_packet_logged" for row in pair_rows) else "no",
                "has_reusable_packet": "yes" if any(row["reusable_packet_status"] == "family_packet_available" for row in pair_rows) else "no",
                "row_level_tiers": ";".join(f"{row['source_record_id']}={row['routing_tier']}" for row in pair_rows),
                "row_level_record_ids": ";".join(row["source_record_id"] for row in pair_rows),
                "routing_flags_union": ";".join(sorted({flag for row in pair_rows for flag in split_terms(row["routing_flags"])})),
                "reusable_family_packets": ";".join(sorted({packet for row in pair_rows for packet in split_terms(row["reusable_family_packets"])})),
            }
        )
    return rollup_rows


def write_summary(path: Path, rows: list[dict[str, str]], pair_rows: list[dict[str, str]]) -> None:
    tier_counts = Counter(row["routing_tier"] for row in rows)
    source_counts = Counter(row["source_database"] for row in rows)
    bucket_counts = Counter(row["module20a_bucket"] for row in rows)
    audited_counts = Counter(row["audit_status"] for row in rows)
    reuse_counts = Counter(row["reusable_packet_status"] for row in rows)
    tier_by_source: dict[str, Counter[str]] = defaultdict(Counter)
    for row in rows:
        tier_by_source[row["source_database"]][row["routing_tier"]] += 1

    summary = {
        "row_count": len(rows),
        "pair_count": len(pair_rows),
        "tier_counts": dict(sorted(tier_counts.items())),
        "source_counts": dict(sorted(source_counts.items())),
        "bucket_counts": dict(sorted(bucket_counts.items())),
        "audit_status_counts": dict(sorted(audited_counts.items())),
        "reuse_status_counts": dict(sorted(reuse_counts.items())),
        "tier_by_source": {
            source: dict(sorted(counts.items()))
            for source, counts in sorted(tier_by_source.items())
        },
    }
    path.with_suffix(".json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    lines = [
        "# Module 20A Evidence Effort Routing Summary",
        "",
        f"- Routed rows: `{len(rows)}`",
        f"- Unique pairs: `{len(pair_rows)}`",
        "",
        "## Tier Counts",
        "",
    ]
    for key, value in sorted(tier_counts.items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Source Counts", ""])
    for key, value in sorted(source_counts.items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Audit Status", ""])
    for key, value in sorted(audited_counts.items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Reuse Status", ""])
    for key, value in sorted(reuse_counts.items()):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Tier By Source", ""])
    for source, counts in sorted(tier_by_source.items()):
        count_text = ", ".join(f"`{tier}`=`{value}`" for tier, value in sorted(counts.items()))
        lines.append(f"- `{source}`: {count_text}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    starter_dir = root / "work" / "module20_db_seed" / "evidence_escalation_starter"
    audited_pairs = load_audited_pairs(starter_dir)
    gtopdb_lookup = load_gtopdb_lookup(root)
    cellchat_lookup = load_cellchat_lookup(root)
    reuse_registry = load_reuse_registry(starter_dir)

    rows: list[dict[str, str]] = []
    for queue_name, _label, relative_path, source_type in QUEUE_SPECS:
        for row in read_tsv(root / relative_path):
            normalized = normalize_queue_row(
                row,
                queue_name=queue_name,
                source_type=source_type,
                root=root,
                gtopdb_lookup=gtopdb_lookup,
                cellchat_lookup=cellchat_lookup,
                audited_pairs=audited_pairs,
                reuse_registry=reuse_registry,
            )
            rows.append(classify_row(normalized))

    rows.sort(key=lambda row: (int(row["routing_rank"]), row["pair_label"], row["source_record_id"]))
    pair_rows = make_pair_rollup(rows)

    output_dir = args.output_dir
    write_tsv(output_dir / "module20a_evidence_effort_routing_registry.tsv", OUTPUT_HEADERS, rows)
    write_tsv(output_dir / "module20a_evidence_effort_pair_rollup.tsv", PAIR_HEADERS, pair_rows)
    for tier in ["fast", "medium", "hard"]:
        tier_rows = [row for row in rows if row["routing_tier"] == tier]
        write_tsv(output_dir / f"{tier}.tsv", OUTPUT_HEADERS, tier_rows)
    write_summary(output_dir / "summary.md", rows, pair_rows)


if __name__ == "__main__":
    main()
