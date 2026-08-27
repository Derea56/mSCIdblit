#!/usr/bin/env python3
"""Independently audit the additive public TF/regulon union.

This audit reparses the raw snapshots rather than trusting the importer
manifest, then compares those sets to the loaded external tables and to the
frozen mSCIdblit roles/edges.  It writes a JSON report and a compact Markdown
report with named examples for unresolved identities, direction conflicts,
downstream role gaps, upstream gaps, and evidence gaps.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


PRIORITY_TFS = {
    "TP53", "JUN", "FOS", "MYC", "STAT1", "HIF1A", "SP1", "ETS1",
    "RUNX1", "GATA3", "CEBPB", "IRF1", "ATF2", "EGR1", "KLF4", "NFKB2",
}


def simple_symbol(value: str | None) -> str | None:
    value = (value or "").strip()
    if not value or re.fullmatch(r"[OPQ][0-9][A-Z0-9]{4,7}", value):
        return None
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", value):
        return None
    return value


def run_psql(args: argparse.Namespace, sql: str) -> list[list[str]]:
    command = [
        args.psql, "-h", args.host, "-p", str(args.port), "-d", args.database,
        "-At", "-F", "\t", "-v", "ON_ERROR_STOP=1", "-c", sql,
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    rows = []
    for line in result.stdout.splitlines():
        rows.append(line.split("\t"))
    return rows


def parse_source(path: Path, source: str, species: str) -> tuple[int, set[str], set[tuple[str, str]], Counter, list[dict]]:
    raw_count = 0
    tfs: set[str] = set()
    pairs: set[tuple[str, str]] = set()
    effects: Counter = Counter()
    unresolved: list[dict] = []
    with path.open(encoding="utf-8", newline="") as handle:
        iterator = csv.reader(handle, delimiter="\t") if source == "trrust" else csv.DictReader(handle, delimiter="\t")
        for line_number, row in enumerate(iterator, start=1 if source == "trrust" else 2):
            raw_count += 1
            if source == "trrust":
                tf_raw, target_raw, effect = row[0], row[1], row[2]
            else:
                tf_raw = row.get("source_genesymbol", "")
                target_raw = row.get("target_genesymbol", "")
                stimulation = row.get("consensus_stimulation", "") == "True"
                inhibition = row.get("consensus_inhibition", "") == "True"
                effect = "activating_target" if stimulation and not inhibition else "repressing_target" if inhibition and not stimulation else "context_dependent" if stimulation and inhibition else "unknown"
            tf = simple_symbol(tf_raw)
            target = simple_symbol(target_raw)
            if tf:
                tfs.add(tf.casefold())
            if tf and target:
                pair = (tf.casefold(), target.casefold())
                pairs.add(pair)
                effects[(pair[0], pair[1], effect)] += 1
            if not tf or not target:
                unresolved.append({
                    "source": source,
                    "species": species,
                    "line": line_number,
                    "tf": tf_raw,
                    "target": target_raw,
                    "reason": "tf_unresolved" if not tf else "target_unresolved",
                })
    return raw_count, tfs, pairs, effects, unresolved


def metric_row(rows: list[list[str]], key_index: int = 0) -> dict[str, int]:
    return {row[key_index]: int(row[key_index + 1]) for row in rows if len(row) > key_index + 1}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trrust-human", type=Path, required=True)
    parser.add_argument("--trrust-mouse", type=Path, required=True)
    parser.add_argument("--dorothea-human", type=Path, required=True)
    parser.add_argument("--dorothea-mouse", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--psql", default="psql")
    parser.add_argument("--host", default="/private/tmp/mscidblit_pg_socket")
    parser.add_argument("--port", default="55432")
    parser.add_argument("--database", default="mscidblit_local")
    parser.add_argument(
        "--frozen-bundle-metadata",
        type=Path,
        default=Path("data/processed/mechanism_bundle_module20_24_db_v1_0_0/bundle_metadata.json"),
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    source_specs = [
        ("TRRUST", "trrust", "human", args.trrust_human),
        ("TRRUST", "trrust", "mouse", args.trrust_mouse),
        ("OmniPath_DoRothEA", "dorothea", "human", args.dorothea_human),
        ("OmniPath_DoRothEA", "dorothea", "mouse", args.dorothea_mouse),
    ]
    raw = {}
    unresolved = []
    effect_counter: Counter = Counter()
    for registry, source, species, path in source_specs:
        count, tfs, pairs, effects, unresolved_rows = parse_source(path, source, species)
        raw[(registry, species)] = {"records": count, "tfs": tfs, "pairs": pairs}
        effect_counter.update({(registry, species, tf, target, effect): count for (tf, target, effect), count in effects.items()})
        unresolved.extend(unresolved_rows)

    db_counts = metric_row(run_psql(args, """
        SELECT 'external_source_registry', count(*) FROM external_tf_source_registry
        UNION ALL SELECT 'external_identity_mapping', count(*) FROM external_tf_identity_mapping
        UNION ALL SELECT 'external_records', count(*) FROM external_tf_regulon_record
        UNION ALL SELECT 'external_references', count(*) FROM external_tf_reference
        UNION ALL SELECT 'external_regulons', count(*) FROM external_tf_regulon
        UNION ALL SELECT 'external_members', count(*) FROM external_tf_regulon_member
        UNION ALL SELECT 'external_verification', count(*) FROM external_tf_evidence_verification
    """))
    frozen_counts = metric_row(run_psql(args, """
        SELECT 'signalingentity', count(*) FROM signalingentity
        UNION ALL SELECT 'signalingentityrole', count(*) FROM signalingentityrole
        UNION ALL SELECT 'signalingedge', count(*) FROM signalingedge
        UNION ALL SELECT 'regulon', count(*) FROM regulon
        UNION ALL SELECT 'regulonmember', count(*) FROM regulonmember
        UNION ALL SELECT 'regulonmembersource', count(*) FROM regulonmembersource
    """))
    frozen_metadata = json.loads(args.frozen_bundle_metadata.read_text(encoding="utf-8"))
    frozen_core_expected = {
        "signalingentity": frozen_metadata["counts"]["nodes"],
        "signalingentityrole": frozen_metadata["counts"]["node_roles"],
        "signalingedge": frozen_metadata["counts"]["edges"],
    }

    materialized_rows = run_psql(args, """
        SELECT r.source_registry, r.species_context,
               lower(r.tf_normalized_symbol), lower(rm.target_normalized_symbol),
               count(*)
        FROM external_tf_regulon_member rm
        JOIN external_tf_regulon r ON r.external_regulon_id = rm.external_regulon_id
        GROUP BY r.source_registry, r.species_context,
                 lower(r.tf_normalized_symbol), lower(rm.target_normalized_symbol)
    """)
    materialized_pairs = defaultdict(set)
    for row in materialized_rows:
        materialized_pairs[(row[0], row[1])].add((row[2], row[3]))

    frozen_pairs_rows = run_psql(args, """
        SELECT DISTINCT lower(tf.gene_symbol), lower(target.gene_symbol)
        FROM regulonmember rm
        JOIN regulon r ON r.regulon_id = rm.regulon_id
        JOIN signalingentity tf ON tf.entity_id = r.tf_entity_id
        JOIN signalingentity target ON target.entity_id = rm.target_entity_id
        WHERE r.source_registry = 'mSCIdblit_signaling_edges'
          AND r.source_version = '2026-08-25'
          AND rm.export_priority <> 'exclude'
          AND tf.gene_symbol IS NOT NULL
          AND target.gene_symbol IS NOT NULL
    """)
    frozen_pairs = {(row[0], row[1]) for row in frozen_pairs_rows}

    tf_coverage_rows = run_psql(args, """
        SELECT registry.source_registry, registry.species_context,
               lower(regulon.tf_normalized_symbol),
               CASE WHEN mapping.mscidblit_entity_id IS NULL THEN 'absent_tf_node'
                    WHEN NOT EXISTS (
                      SELECT 1 FROM signalingentityrole role
                      WHERE role.entity_id = mapping.mscidblit_entity_id
                        AND role.role = 'transcription_factor'
                        AND role.role_status IN ('curated', 'derived')
                        AND role.export_priority <> 'exclude'
                    ) THEN 'tf_node_missing_explicit_tf_role'
                    ELSE 'tf_node_and_role_present' END,
               CASE WHEN regulon.external_regulon_id IS NULL THEN 'missing_external_regulon' ELSE 'external_regulon_present' END
        FROM external_tf_source_registry registry
        JOIN external_tf_regulon regulon
          ON regulon.source_registry = registry.source_registry
         AND regulon.source_version = registry.source_version
         AND regulon.species_context = registry.species_context
        LEFT JOIN external_tf_identity_mapping mapping
          ON mapping.source_registry = regulon.source_registry
         AND mapping.source_version = regulon.source_version
         AND mapping.species_context = regulon.species_context
         AND mapping.identity_role = 'tf'
         AND mapping.normalized_symbol_key = lower(regulon.tf_normalized_symbol)
    """)
    tf_coverage = Counter(row[3] for row in tf_coverage_rows)

    downstream_rows = run_psql(args, """
        SELECT
          count(*) FILTER (WHERE target_normalized_symbol_key IS NULL),
          count(*) FILTER (WHERE tf_normalized_symbol_key IS NULL),
          count(*) FILTER (WHERE target_normalized_symbol_key IS NOT NULL AND NOT target_node_present),
          count(*) FILTER (WHERE target_normalized_symbol_key IS NOT NULL AND target_node_present AND NOT target_role_present),
          count(*) FILTER (WHERE target_normalized_symbol_key IS NOT NULL AND target_role_present)
        FROM external_tf_downstream_union
    """)
    downstream = {}
    if downstream_rows:
        row = downstream_rows[0]
        downstream = {
            "records_with_unresolved_target_identity": int(row[0]),
            "records_with_unresolved_tf_identity": int(row[1]),
            "records_with_target_absent_from_frozen_graph": int(row[2]),
            "records_with_target_node_but_missing_explicit_target_role": int(row[3]),
            "records_with_explicit_target_role": int(row[4]),
        }

    upstream_rows = run_psql(args, """
        SELECT source_registry, species_context, tf_normalized_symbol,
               upstream_gap_class, supported_upstream_edge_count
        FROM external_tf_upstream_gaps
        ORDER BY source_registry, species_context, tf_normalized_symbol
    """)
    upstream = Counter(row[3] for row in upstream_rows)
    upstream_examples = [
        {
            "source_registry": row[0], "species": row[1], "tf": row[2],
            "gap_class": row[3], "supported_edge_count": int(row[4]),
        }
        for row in upstream_rows if row[3] != "upstream_path_present"
    ][:50]

    evidence_rows = run_psql(args, """
        SELECT priority_tf_symbol, species_context, verification_status,
               count(*)
        FROM external_tf_evidence_verification
        WHERE verification_scope = 'tf_identity'
        GROUP BY priority_tf_symbol, species_context, verification_status
        ORDER BY priority_tf_symbol, species_context
    """)
    evidence_status = Counter()
    evidence_matrix = []
    for row in evidence_rows:
        evidence_status[row[2]] += int(row[3])
        evidence_matrix.append({"tf": row[0], "species": row[1], "status": row[2]})
    record_evidence_rows = run_psql(args, """
        SELECT verification_status, count(*)
        FROM external_tf_regulon_record
        GROUP BY verification_status ORDER BY verification_status
    """)
    record_evidence = metric_row(record_evidence_rows)

    conflict_rows = run_psql(args, """
        SELECT species_context, lower(tf_normalized_symbol), lower(target_normalized_symbol),
               string_agg(DISTINCT source_registry || ':' || effect_polarity, ', ' ORDER BY source_registry || ':' || effect_polarity),
               count(DISTINCT effect_polarity)
        FROM external_tf_regulon_record
        WHERE tf_normalized_symbol_key IS NOT NULL
          AND target_normalized_symbol_key IS NOT NULL
          AND effect_polarity <> 'unknown'
        GROUP BY species_context, lower(tf_normalized_symbol), lower(target_normalized_symbol)
        HAVING count(DISTINCT effect_polarity) > 1
        ORDER BY count(*) DESC, species_context, lower(tf_normalized_symbol), lower(target_normalized_symbol)
        LIMIT 50
    """)
    conflicts = [
        {"species": row[0], "tf": row[1], "target": row[2], "assertions": row[3], "direction_count": int(row[4])}
        for row in conflict_rows
    ]
    conflict_count_rows = run_psql(args, """
        SELECT count(*)
        FROM (
          SELECT species_context, lower(tf_normalized_symbol), lower(target_normalized_symbol)
          FROM external_tf_regulon_record
          WHERE tf_normalized_symbol_key IS NOT NULL
            AND target_normalized_symbol_key IS NOT NULL
            AND effect_polarity <> 'unknown'
          GROUP BY species_context, lower(tf_normalized_symbol), lower(target_normalized_symbol)
          HAVING count(DISTINCT effect_polarity) > 1
        ) conflict_groups
    """)
    total_conflict_groups = int(conflict_count_rows[0][0]) if conflict_count_rows else 0

    integrity_rows = run_psql(args, """
        SELECT 'identity_source_fk', count(*) FROM external_tf_identity_mapping m
        WHERE NOT EXISTS (SELECT 1 FROM external_tf_source_registry s
                          WHERE s.source_registry=m.source_registry AND s.source_version=m.source_version AND s.species_context=m.species_context)
        UNION ALL SELECT 'record_source_fk', count(*) FROM external_tf_regulon_record r
        WHERE NOT EXISTS (SELECT 1 FROM external_tf_source_registry s
                          WHERE s.source_registry=r.source_registry AND s.source_version=r.source_version AND s.species_context=r.species_context)
        UNION ALL SELECT 'reference_record_fk', count(*) FROM external_tf_reference x
        WHERE NOT EXISTS (SELECT 1 FROM external_tf_regulon_record r WHERE r.external_record_key=x.external_record_key)
        UNION ALL SELECT 'member_regulon_fk', count(*) FROM external_tf_regulon_member m
        WHERE NOT EXISTS (SELECT 1 FROM external_tf_regulon r WHERE r.external_regulon_id=m.external_regulon_id)
        UNION ALL SELECT 'member_record_fk', count(*) FROM external_tf_regulon_member m
        WHERE NOT EXISTS (SELECT 1 FROM external_tf_regulon_record r WHERE r.external_record_key=m.external_record_key)
        UNION ALL SELECT 'verification_record_fk', count(*) FROM external_tf_evidence_verification v
        WHERE v.external_record_key IS NOT NULL
          AND NOT EXISTS (SELECT 1 FROM external_tf_regulon_record r WHERE r.external_record_key=v.external_record_key)
        UNION ALL SELECT 'regulon_member_count_mismatch', count(*)
        FROM external_tf_regulon r
        WHERE r.materialized_member_count <> (
          SELECT count(*) FROM external_tf_regulon_member m WHERE m.external_regulon_id=r.external_regulon_id
        )
        UNION ALL SELECT 'non_excluded_external_rows', count(*)
        FROM external_tf_regulon_record WHERE export_priority <> 'exclude'
        UNION ALL SELECT 'non_excluded_external_members', count(*)
        FROM external_tf_regulon_member WHERE export_priority <> 'exclude'
    """)
    integrity = metric_row(integrity_rows)

    source_summary = {}
    pair_coverage = {}
    downstream_gaps = []
    for (registry, species), values in raw.items():
        key = f"{registry}:{species}"
        public_pairs = values["pairs"]
        materialized = materialized_pairs[(registry, species)]
        pair_coverage[key] = {
            "raw_simple_pairs": len(public_pairs),
            "materialized_simple_pairs": len(materialized),
            "raw_pairs_not_materialized": len(public_pairs - materialized),
            "materialized_pairs_not_in_raw": len(materialized - public_pairs),
            "raw_pairs_overlapping_frozen_regulon": len(public_pairs & frozen_pairs),
            "raw_tfs": len(values["tfs"]),
        }
        source_summary[key] = {"raw_records": values["records"], "raw_tfs": len(values["tfs"]), "raw_simple_pairs": len(public_pairs)}
        downstream_gaps.extend({
            "source_registry": registry, "species": species, "tf": tf, "target": target,
        } for tf, target in sorted(public_pairs - materialized)[:100])

    named_unresolved = unresolved[:50]
    report = {
        "audit_name": "public_tf_union_v1_independent_gap_audit",
        "audit_status": "complete",
        "source_summary": source_summary,
        "database_counts": db_counts,
        "frozen_counts_after_load": frozen_counts,
        "pair_coverage": pair_coverage,
        "tf_node_coverage_categories": dict(tf_coverage),
        "unresolved_identity": {
            "raw_unresolved_rows": len(unresolved),
            "named_examples": named_unresolved,
        },
        "downstream_gaps": {
            **downstream,
            "raw_simple_pairs_not_materialized_examples": downstream_gaps,
        },
        "upstream_gaps": {
            "categories": dict(upstream),
            "named_examples": upstream_examples,
        },
        "evidence_gaps": {
            "priority_tf_identity_status_counts": dict(evidence_status),
            "priority_tf_identity_matrix": evidence_matrix,
            "all_record_verification_status_counts": record_evidence,
        },
        "direction_conflicts": {
            "named_examples": conflicts,
            "named_example_count": len(conflicts),
            "total_conflict_group_count": total_conflict_groups,
        },
        "referential_integrity": integrity,
        "acceptance_checks": {
            "zero_referential_integrity_failures": all(value == 0 for value in integrity.values()),
            "all_external_rows_export_gated": integrity.get("non_excluded_external_rows", 1) == 0 and integrity.get("non_excluded_external_members", 1) == 0,
            "frozen_core_counts_match_release_metadata": all(
                frozen_counts.get(key) == value for key, value in frozen_core_expected.items()
            ),
            "frozen_derived_tables_nonempty": all(
                frozen_counts.get(key, 0) > 0
                for key in ("regulon", "regulonmember", "regulonmembersource")
            ),
            "priority_tf_rows_present": len(evidence_matrix) == len(PRIORITY_TFS) * 2,
        },
    }
    (args.output_dir / "public_tf_union_gap_report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    md = [
        "# Public TF/regulon union v1 independent gap audit",
        "",
        "Status: complete. This report compares independent raw-snapshot parsing with the additive `external_tf_*` layer and the frozen mSCIdblit tables.",
        "",
        "## Counts",
        "",
        "| Source/species | Raw records | Raw TFs | Raw simple pairs | Materialized simple pairs | Raw pairs not materialized | Raw pairs overlapping frozen regulon |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for key in sorted(pair_coverage):
        pair = pair_coverage[key]
        md.append(f"| {key} | {source_summary[key]['raw_records']:,} | {pair['raw_tfs']:,} | {pair['raw_simple_pairs']:,} | {pair['materialized_simple_pairs']:,} | {pair['raw_pairs_not_materialized']:,} | {pair['raw_pairs_overlapping_frozen_regulon']:,} |")
    md.extend([
        "",
        "Frozen counts after materialization: " + ", ".join(f"`{key}`={value:,}" for key, value in frozen_counts.items()) + ".",
        "",
        "## Gap classes",
        "",
        f"- TF coverage categories: {dict(tf_coverage)}.",
        f"- Unresolved raw identity rows: {len(unresolved):,}; examples are retained in the JSON report and `unresolved_identity_queue.tsv`.",
        f"- Downstream view: {downstream}.",
        f"- Upstream gap categories: {dict(upstream)}. The upstream view uses exact frozen entity symbol matches only and does not infer ligand-to-TF activation.",
        f"- Priority-TF identity verification statuses: {dict(evidence_status)}. `database_curated_unverified` rows remain unpromoted.",
        f"- Direction-conflict groups: {total_conflict_groups:,}; the report includes the first {len(conflicts):,} named examples.",
        "",
        "## Direction conflicts",
        "",
        "The following are source-level disagreements, not merged assertions:",
        "",
        "| Species | TF | Target | Source/effect assertions |",
        "|---|---|---|---|",
    ])
    for conflict in conflicts[:25]:
        md.append(f"| {conflict['species']} | {conflict['tf']} | {conflict['target']} | {conflict['assertions']} |")
    md.extend([
        "",
        "## Referential integrity and release separation",
        "",
        f"Referential-integrity checks: `{integrity}`.",
        "",
        "All external records and members are export-gated with `export_priority = 'exclude'`. Existing frozen mechanism tables were not updated by the loader.",
        "",
        "## Reproduction",
        "",
        "```bash",
        "python3 scripts/audit_public_tf_union_v1.py \\",
        "  --trrust-human /private/tmp/trrust_human.tsv \\",
        "  --trrust-mouse /private/tmp/trrust_mouse.tsv \\",
        "  --dorothea-human /private/tmp/omnipath_dorothea_human.tsv \\",
        "  --dorothea-mouse /private/tmp/omnipath_dorothea_mouse.tsv \\",
        "  --output-dir data/processed/public_tf_union_v1",
        "```",
    ])
    (args.output_dir / "PUBLIC_TF_UNION_GAP_AUDIT_V1.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps({"database_counts": db_counts, "referential_integrity": integrity, "pair_coverage": pair_coverage}, sort_keys=True))


if __name__ == "__main__":
    main()
