#!/usr/bin/env python3
"""Compare canonical Module 22B evidence against initial TF databases.

The initial database side is the reproducible TRRUST and OmniPath/DoRothEA
snapshot represented by ``public_tf_union_v1/source_records.tsv``.  The
reasonable-confidence side is the canonical, exportable Module 22B review
layer plus the pre-existing exportable regulon memberships.  Counts are exact
case-insensitive simple-symbol pairs; composite/unresolved identifiers are
excluded rather than forced into a match.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_RECORDS = ROOT / "data/processed/public_tf_union_v1/source_records.tsv"
DEFAULT_REVIEW_STAGE = ROOT / "work/module22b_consolidation/materialization_round_2026_08_26/module22b_promoted_pairs.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/module22b_database_comparison_v1"
DEFAULT_PSQL = "/Users/derea/Homebrew/bin/psql"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--database",
        default="postgresql:///mscidblit_local?host=/private/tmp/mscidblit_pg_socket&port=55432",
    )
    parser.add_argument("--psql", default=DEFAULT_PSQL)
    parser.add_argument("--source-records", type=Path, default=DEFAULT_SOURCE_RECORDS)
    parser.add_argument("--review-stage", type=Path, default=DEFAULT_REVIEW_STAGE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def normalize(value: str | None) -> str:
    return re.sub(r"[^a-z0-9]", "", (value or "").strip().casefold())


def simple_symbol(value: str | None) -> str:
    value = (value or "").strip()
    if not value or value in {"\\N", "NA", "null"}:
        return ""
    if re.search(r"[,;+|/\\\s]", value):
        return ""
    key = normalize(value)
    return key if re.fullmatch(r"[a-z][a-z0-9]{1,15}", key) else ""


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def run_psql(psql: str, database: str, query: str) -> list[dict[str, str]]:
    result = subprocess.run(
        [psql, "-X", "--csv", "-v", "ON_ERROR_STOP=1", "-d", database, "-c", query],
        check=True,
        capture_output=True,
        text=True,
    )
    return list(csv.DictReader(io.StringIO(result.stdout)))


def pair(row: dict[str, str], tf_field: str, target_field: str) -> tuple[str, str] | None:
    tf = simple_symbol(row.get(tf_field))
    target = simple_symbol(row.get(target_field))
    return (tf, target) if tf and target else None


def metrics(ours: set[tuple[str, str]], public: set[tuple[str, str]]) -> dict[str, int | float]:
    overlap = ours & public
    return {
        "reasonable_pairs": len(ours),
        "initial_database_pairs": len(public),
        "overlap_pairs": len(overlap),
        "reasonable_only_pairs": len(ours - public),
        "initial_database_only_pairs": len(public - ours),
        "reasonable_coverage_of_initial_database": round(len(overlap) / len(public), 6) if public else 0.0,
        "initial_database_coverage_of_reasonable": round(len(overlap) / len(ours), 6) if ours else 0.0,
    }


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    source_rows = read_tsv(args.source_records)
    review_rows = read_tsv(args.review_stage)
    initial: defaultdict[tuple[str, str], set[tuple[str, str]]] = defaultdict(set)
    initial_rows: defaultdict[tuple[str, str], int] = defaultdict(int)
    for row in source_rows:
        key = (row["source_registry"], row["species_context"])
        initial_rows[key] += 1
        item = pair(row, "tf_normalized_symbol", "target_normalized_symbol")
        if item:
            initial[key].add(item)

    review_pairs_by_species: defaultdict[str, set[tuple[str, str]]] = defaultdict(set)
    review_tfs_by_species: defaultdict[str, set[str]] = defaultdict(set)
    review_registry_pairs: defaultdict[tuple[str, str], set[tuple[str, str]]] = defaultdict(set)
    for row in review_rows:
        item = pair(row, "tf_symbol", "target_symbol")
        if not item:
            continue
        species = row["species"]
        review_pairs_by_species[species].add(item)
        review_tfs_by_species[species].add(item[0])
        for registry in (token.strip() for token in row.get("source_registries", "").split(";") if token.strip()):
            review_registry_pairs[(registry, species)].add(item)

    canonical_rows = run_psql(
        args.psql,
        args.database,
        """
        SELECT
          regulon.source_registry,
          regulon.source_version,
          regulon.species_context,
          COALESCE(NULLIF(tf.gene_symbol, ''), tf.canonical_name) AS tf_symbol,
          COALESCE(NULLIF(target.gene_symbol, ''), target.canonical_name) AS target_symbol,
          regulonmember.confidence_tier,
          regulonmember.export_priority,
          regulonmember.membership_status
        FROM RegulonMember AS regulonmember
        JOIN Regulon AS regulon ON regulon.regulon_id = regulonmember.regulon_id
        JOIN SignalingEntity AS tf ON tf.entity_id = regulon.tf_entity_id
        JOIN SignalingEntity AS target ON target.entity_id = regulonmember.target_entity_id
        WHERE regulonmember.export_priority <> 'exclude'
          AND regulonmember.membership_status = 'supported'
        ORDER BY regulon.source_registry, regulon.species_context, tf_symbol, target_symbol
        """,
    )
    all_exportable: defaultdict[str, set[tuple[str, str]]] = defaultdict(set)
    all_confidence: defaultdict[str, defaultdict[str, set[tuple[str, str]]]] = defaultdict(lambda: defaultdict(set))
    for row in canonical_rows:
        item = pair(row, "tf_symbol", "target_symbol")
        if not item:
            continue
        species = row["species_context"]
        all_exportable[species].add(item)
        all_confidence[species][row["confidence_tier"]].add(item)

    reviewed_canonical_rows = run_psql(
        args.psql,
        args.database,
        """
        SELECT
          regulon.species_context,
          COALESCE(NULLIF(tf.gene_symbol, ''), tf.canonical_name) AS tf_symbol,
          COALESCE(NULLIF(target.gene_symbol, ''), target.canonical_name) AS target_symbol,
          regulonmember.confidence_tier
        FROM RegulonMember AS regulonmember
        JOIN Regulon AS regulon ON regulon.regulon_id = regulonmember.regulon_id
        JOIN SignalingEntity AS tf ON tf.entity_id = regulon.tf_entity_id
        JOIN SignalingEntity AS target ON target.entity_id = regulonmember.target_entity_id
        WHERE regulon.source_registry = 'public_tf_pair_review'
          AND regulon.source_version = '2026-08-26'
          AND regulonmember.export_priority <> 'exclude'
          AND regulonmember.membership_status = 'supported'
        ORDER BY regulon.species_context, tf_symbol, target_symbol
        """,
    )
    reviewed_canonical: defaultdict[str, set[tuple[str, str]]] = defaultdict(set)
    for row in reviewed_canonical_rows:
        item = pair(row, "tf_symbol", "target_symbol")
        if item:
            reviewed_canonical[row["species_context"]].add(item)

    by_source: dict[str, dict] = {}
    for (registry, species), public_pairs in sorted(initial.items()):
        reasonable_pairs = review_pairs_by_species[species]
        source_review_pairs = review_registry_pairs[(registry, species)]
        by_source[f"{registry}:{species}"] = {
            "initial_rows": initial_rows[(registry, species)],
            "initial_simple_pairs": len(public_pairs),
            "initial_tf_symbols": len({tf for tf, _ in public_pairs}),
            "reasonable_22b_pairs": len(reasonable_pairs),
            "reasonable_22b_tf_symbols": len(review_tfs_by_species[species]),
            "reasonable_22b_pairs_in_this_source": len(source_review_pairs),
            "reasonable_22b_pair_overlap": len(reasonable_pairs & public_pairs),
            "reasonable_22b_coverage_of_initial_pairs": round(len(reasonable_pairs & public_pairs) / len(public_pairs), 6) if public_pairs else 0.0,
            "all_exportable_canonical_pairs": len(all_exportable[species]),
            "all_exportable_canonical_tf_symbols": len({tf for tf, _ in all_exportable[species]}),
        }

    union_by_species: dict[str, dict] = {}
    for species in ("human", "mouse"):
        public_union = set().union(*(initial[(registry, species)] for registry in ("TRRUST", "OmniPath_DoRothEA")))
        union_by_species[species] = {
            "initial_database_rows": sum(initial_rows[(registry, species)] for registry in ("TRRUST", "OmniPath_DoRothEA")),
            "initial_database_simple_pairs": len(public_union),
            "initial_database_tf_symbols": len({tf for tf, _ in public_union}),
            "reasonable_22b_pairs": len(review_pairs_by_species[species]),
            "reasonable_22b_tf_symbols": len(review_tfs_by_species[species]),
            "reasonable_22b_pair_metrics": metrics(review_pairs_by_species[species], public_union),
            "all_exportable_canonical_pairs": len(all_exportable[species]),
            "all_exportable_canonical_tf_symbols": len({tf for tf, _ in all_exportable[species]}),
            "all_exportable_confidence_pairs": {tier: len(pairs) for tier, pairs in sorted(all_confidence[species].items())},
        }

    summary = {
        "analysis": {
            "comparison_unit": "case-insensitive normalized simple TF-target pairs",
            "initial_database_snapshot": str(args.source_records),
            "reasonable_confidence_definition": "canonical public_tf_pair_review memberships with supported status and medium export priority",
            "unverified_public_rows": "excluded from reasonable-confidence counts",
            "upstream_activation": "not inferred from TF-target memberships",
        },
        "reviewed_22b": {
            "canonical_pair_rows": sum(len(items) for items in reviewed_canonical.values()),
            "stage_pair_rows": len(review_rows),
            "stage_human_pairs": len(review_pairs_by_species["human"]),
            "stage_mouse_pairs": len(review_pairs_by_species["mouse"]),
            "stage_tf_species_keys": len({(row["species"], row["tf_symbol"].casefold()) for row in review_rows}),
            "stage_tf_symbol_keys": len({row["tf_symbol"].casefold() for row in review_rows}),
            "stage_pairs_with_registry_support": {
                f"{key[0]}:{key[1]}": len(value)
                for key, value in sorted(review_registry_pairs.items())
            },
        },
        "source_comparisons": by_source,
        "union_comparisons": union_by_species,
        "canonical_inventory": {
            "all_exportable_pair_rows": sum(len(items) for items in all_exportable.values()),
            "all_exportable_tf_species_pairs": len({(species, tf) for species, items in all_exportable.items() for tf, _ in items}),
            "all_exportable_tf_symbols": len({tf for items in all_exportable.values() for tf, _ in items}),
            "reviewed_22b_pairs": sum(len(items) for items in reviewed_canonical.values()),
            "preexisting_non_22b_or_other_regulon_pairs": sum(len(all_exportable[species] - reviewed_canonical[species]) for species in all_exportable),
        },
    }
    (args.output_dir / "comparison_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    lines = [
        "# Module 22B comparison with initial TF databases",
        "",
        "This comparison uses the versioned TRRUST and OmniPath/DoRothEA source-record snapshot as the initial database inventory and the canonical supported Module 22B review layer as the reasonable-confidence inventory. Counts use exact case-insensitive simple TF-target pairs; unresolved/composite identifiers are excluded.",
        "",
        "## Reasonable-confidence inventory",
        "",
        f"- Canonical reviewed 22B pairs: **{summary['reviewed_22b']['canonical_pair_rows']:,}**.",
        f"- Human reviewed pairs: **{summary['reviewed_22b']['stage_human_pairs']:,}**; mouse reviewed pairs: **{summary['reviewed_22b']['stage_mouse_pairs']:,}**.",
        f"- Species-qualified TF entries in the stage: **{summary['reviewed_22b']['stage_tf_species_keys']:,}**; normalized TF symbols: **{summary['reviewed_22b']['stage_tf_symbol_keys']:,}**.",
        f"- All exportable canonical regulon pairs after the write: **{summary['canonical_inventory']['all_exportable_pair_rows']:,}**; reviewed 22B accounts for **{summary['canonical_inventory']['reviewed_22b_pairs']:,}** of these.",
        "",
        "## Source-by-source comparison",
        "",
        "| Source | Species | Initial rows | Initial simple pairs | Initial TFs | Reasonable 22B pairs | 22B pairs in source | 22B coverage of initial pairs | All canonical pairs after write |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for key, item in sorted(by_source.items()):
        registry, species = key.split(":", 1)
        lines.append(
            f"| {registry} | {species} | {item['initial_rows']:,} | {item['initial_simple_pairs']:,} | {item['initial_tf_symbols']:,} | {item['reasonable_22b_pairs']:,} | {item['reasonable_22b_pairs_in_this_source']:,} | {item['reasonable_22b_coverage_of_initial_pairs'] * 100:.1f}% | {item['all_exportable_canonical_pairs']:,} |"
        )
    lines.extend(
        [
            "",
            "## TRRUST + OmniPath/DoRothEA union",
            "",
            "| Species | Initial union simple pairs | Initial union TFs | Reasonable 22B pairs | 22B overlap with union | 22B coverage of union | All canonical pairs after write | All canonical TFs after write |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for species, item in union_by_species.items():
        pair_metric = item["reasonable_22b_pair_metrics"]
        lines.append(
            f"| {species} | {item['initial_database_simple_pairs']:,} | {item['initial_database_tf_symbols']:,} | {item['reasonable_22b_pairs']:,} | {pair_metric['overlap_pairs']:,} | {pair_metric['reasonable_coverage_of_initial_database'] * 100:.1f}% | {item['all_exportable_canonical_pairs']:,} | {item['all_exportable_canonical_tf_symbols']:,} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "The initial databases are broad discovery resources, so their raw row counts are not directly comparable to the reviewed set. The reasonable-confidence count includes only pair-level literature promotions with a primary source; independent corroboration is preserved where available, and 22B memberships do not infer upstream ligand or receptor activation.",
            "",
            "The JSON file beside this report contains the exact denominators and pair-level counts for reruns.",
            "",
        ]
    )
    (args.output_dir / "MODULE22B_DATABASE_COMPARISON_V1.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
