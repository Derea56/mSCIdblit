#!/usr/bin/env python3
"""Prepare a bounded exact-pair evidence-search batch from candidate regulon sets.

The batch is a review queue only. TFLink target membership supplies exact
search pairs and prioritization metadata, not evidence. Targets already
represented in the released mechanism graph are preferred because a validated
TF-target result can later be tested for route continuity.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROLE_TRIAGE = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/public_tf_role_triage.tsv"
)
DEFAULT_TFLINK_SUMMARY = ROOT / "data/processed/public_tf_union_expansion_v1/tflink_tf_summary.tsv"
DEFAULT_RAW_DIR = ROOT / "data/raw/public_database_snapshots/tf_union_expansion_v1"
DEFAULT_MECHANISM_NODES = ROOT / "data/processed/mechanism_graph_module20_24_v2026_08_25/mechanism_nodes.tsv"
DEFAULT_OUTPUT = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_001"
)


FIELDS = [
    "batch_id", "batch_rank", "regulator_key", "display_symbols", "species_scope",
    "primary_role_category", "role_subcategory", "source_registry", "source_version",
    "source_record_id", "raw_tf_symbol", "target_symbol", "target_rank",
    "target_membership_count", "target_in_current_mechanism_graph", "target_graph_modules",
    "candidate_membership_status", "target_cell_presence_status", "downstream_activation_status",
    "upstream_relay_status", "review_status", "source_locator", "source_snapshot",
    "raw_record_sha256", "search_scope", "limitations",
]


CATEGORY_PRIORITY = {
    "catalog_concordant_tf_candidate": 0,
    "dual_role_tf_chromatin_candidate": 1,
    "noncanonical_transcriptional_regulator": 2,
    "provisional_nuclear_transcriptional_regulator": 3,
    "regulon_lead_unclassified": 4,
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def numeric(value: str) -> int:
    try:
        return int(value or 0)
    except ValueError:
        return 0


def scopes(value: str) -> set[str]:
    return {item.strip() for item in (value or "").split(";") if item.strip()}


def read_gmt(path: Path, wanted_keys: set[str] | None = None) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    with path.open(encoding="utf-8", errors="replace") as handle:
        for line in handle:
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 3:
                continue
            key = fields[0].strip().casefold()
            if wanted_keys is not None and key not in wanted_keys:
                continue
            result[key] = list(dict.fromkeys(item.strip() for item in fields[2:] if item.strip()))
    return result


def graph_targets(path: Path) -> dict[str, set[str]]:
    modules: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(path):
        symbol = (row.get("gene_symbol") or "").strip().casefold()
        if not symbol:
            continue
        modules[symbol].update(item for item in (row.get("modules") or "").split(";") if item)
    return modules


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in FIELDS} for row in rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--role-triage", type=Path, default=DEFAULT_ROLE_TRIAGE)
    parser.add_argument("--tflink-summary", type=Path, default=DEFAULT_TFLINK_SUMMARY)
    parser.add_argument("--raw-dir", type=Path, default=DEFAULT_RAW_DIR)
    parser.add_argument("--mechanism-nodes", type=Path, default=DEFAULT_MECHANISM_NODES)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--source-set-count", type=int, default=25)
    parser.add_argument("--targets-per-set", type=int, default=4)
    parser.add_argument("--source-set-offset", type=int, default=0)
    parser.add_argument("--batch-number", type=int, default=1)
    args = parser.parse_args()
    args.output_dir = args.output_dir.resolve()

    role_rows = read_tsv(args.role_triage)
    role_by_key = {row["regulator_key"]: row for row in role_rows}
    graph_by_target = graph_targets(args.mechanism_nodes)
    candidate_source_rows: list[dict[str, str]] = []
    wanted_by_species: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(args.tflink_summary):
        key = (row.get("species_scope", ""), row.get("normalized_tf_symbol_key", ""))
        role = role_by_key.get(row.get("normalized_tf_symbol_key", ""))
        if not role or key[0] not in scopes(role.get("species_scopes", "")):
            continue
        if numeric(row.get("target_count", "")) <= 0:
            continue
        if role.get("identifier_flags"):
            continue
        candidate_source_rows.append(dict(row))
        wanted_by_species[row["species_scope"]].add(row["normalized_tf_symbol_key"])

    gmt_by_species = {
        species: read_gmt(args.raw_dir / f"tflink_{species}_v1.0.gmt", wanted)
        for species, wanted in wanted_by_species.items()
    }
    source_rows: list[dict[str, str]] = []
    for row in candidate_source_rows:
        targets = gmt_by_species.get(row["species_scope"], {}).get(row["normalized_tf_symbol_key"], [])
        if not targets:
            continue
        graph_overlap = sum(target.casefold() in graph_by_target for target in targets)
        row["_targets"] = targets
        row["_graph_overlap"] = str(graph_overlap)
        source_rows.append(row)

    source_rows.sort(key=lambda row: (
        CATEGORY_PRIORITY.get(role_by_key[row["normalized_tf_symbol_key"]]["primary_role_category"], 9),
        -numeric(row.get("_graph_overlap", "0")),
        -numeric(row.get("target_count", "0")),
        row.get("species_scope", ""),
        row.get("normalized_tf_symbol_key", ""),
    ))
    selected_sources = source_rows[args.source_set_offset : args.source_set_offset + args.source_set_count]
    batch_id = f"public_tf_evidence_batch_{args.batch_number:03d}"
    batch_label = f"batch_{args.batch_number:03d}"

    output_rows: list[dict[str, str]] = []
    for batch_rank, source_row in enumerate(selected_sources, start=1):
        key = source_row["normalized_tf_symbol_key"]
        role = role_by_key[key]
        targets = source_row["_targets"]
        targets.sort(key=lambda target: (0 if target.casefold() in graph_by_target else 1, target.casefold()))
        raw_snapshot = args.raw_dir / f"tflink_{source_row['species_scope']}_v1.0.gmt"
        for target_rank, target in enumerate(targets[: args.targets_per_set], start=1):
            graph_modules = ";".join(sorted(graph_by_target.get(target.casefold(), set())))
            output_rows.append({
                "batch_id": batch_id,
                "batch_rank": str(batch_rank),
                "regulator_key": key,
                "display_symbols": role.get("display_symbols", ""),
                "species_scope": source_row.get("species_scope", ""),
                "primary_role_category": role.get("primary_role_category", ""),
                "role_subcategory": role.get("role_subcategory", ""),
                "source_registry": source_row.get("source_registry", "TFLink"),
                "source_version": source_row.get("source_version", ""),
                "source_record_id": source_row.get("source_record_id", ""),
                "raw_tf_symbol": source_row.get("raw_tf_symbol", ""),
                "target_symbol": target,
                "target_rank": str(target_rank),
                "target_membership_count": source_row.get("target_count", ""),
                "target_in_current_mechanism_graph": "yes" if target.casefold() in graph_by_target else "no",
                "target_graph_modules": graph_modules,
                "candidate_membership_status": "database_attributed_candidate_not_verified",
                "target_cell_presence_status": "not_assessed",
                "downstream_activation_status": "not_assessed",
                "upstream_relay_status": "not_assessed",
                "review_status": "queued_exact_pair_literature_review",
                "source_locator": source_row.get("source_locator", ""),
                "source_snapshot": str(raw_snapshot.relative_to(ROOT)),
                "raw_record_sha256": source_row.get("raw_record_sha256", ""),
                "search_scope": "exact regulator-target pair; species-specific; primary literature first; target-cell context separate",
                "limitations": "TFLink GMT membership is a search lead without target-level assay, effect direction, or PMID; no activation or signaling relay is inferred.",
            })

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / f"public_tf_evidence_collection_{batch_label}.tsv"
    write_tsv(output_path, output_rows)
    summary = {
        "status": "staging_only",
        "source_sets_available_after_filters": len(source_rows),
        "source_sets_selected": len(selected_sources),
        "pair_search_rows": len(output_rows),
        "unique_regulators": len({row["regulator_key"] for row in output_rows}),
        "unique_source_records": len({row["source_record_id"] for row in output_rows}),
        "role_category_counts": dict(sorted({
            category: sum(1 for row in selected_sources if role_by_key[row["normalized_tf_symbol_key"]]["primary_role_category"] == category)
            for category in {role_by_key[row["normalized_tf_symbol_key"]]["primary_role_category"] for row in selected_sources}
        }.items())),
        "target_graph_overlap_rows": sum(row["target_in_current_mechanism_graph"] == "yes" for row in output_rows),
        "target_cell_presence_status": "not_assessed_for_all_rows",
        "downstream_activation_status": "not_assessed_for_all_rows",
        "upstream_relay_status": "not_assessed_for_all_rows",
        "canonical_writes_performed": False,
        "module22b_promotions_performed": False,
        "selection_policy": "canonical and dual-role candidates first, then noncanonical/provisional candidates; source sets ranked by overlap with current mechanism gene symbols and reported target count",
        "inputs": {
            "role_triage": str(args.role_triage.relative_to(ROOT)),
            "tflink_summary": str(args.tflink_summary.relative_to(ROOT)),
            "mechanism_nodes": str(args.mechanism_nodes.relative_to(ROOT)),
        },
        "outputs": [str(output_path.relative_to(ROOT))],
    }
    summary_path = args.output_dir / f"{batch_label}_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.output_dir / "README.md").write_text(
        f"# Public TF evidence collection {batch_label}\n\n"
        "This is a bounded exact-pair literature-search queue derived from database-attributed TFLink regulon sets. "
        "TFLink membership is retained as a search lead only. Every row requires independent review of the exact regulator, target, species, cell/model, assay, direction, and any upstream relay. "
        "Target-cell presence and downstream activation remain separate fields. No canonical TF, regulon, or Module 22B evidence record is modified by this batch.\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
