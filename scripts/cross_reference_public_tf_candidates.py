#!/usr/bin/env python3
"""Cross-reference and collapse expanded TF candidates against current sets.

The output is a staging crosswalk.  It collapses duplicate observations by
species scope plus normalized symbol, while retaining source registries,
reported contributor labels, and current canonical entity/regulon IDs. Human
and mouse rows are not merged for evidence purposes; a separate cross-species
summary is provided only as an inventory view.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import subprocess
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_expansion_v1"
DEFAULT_OUTPUT = DEFAULT_INPUT / "current_set_crosswalk_v1"
DEFAULT_DATABASE = "postgresql:///mscidblit_local?host=/private/tmp/mscidblit_pg_socket&port=55432"
DEFAULT_PSQL = "/Users/derea/Homebrew/bin/psql"

CROSSWALK_FIELDS = [
    "candidate_key", "species_scope", "tf_symbol", "tf_key", "source_registries",
    "source_versions", "reported_contributor_labels", "identity_source_count",
    "regulon_record_count", "unique_reference_pmids", "catalog_profile_count",
    "tflink_target_count", "current_sets", "current_entity_ids",
    "current_module_codes", "in_existing_public_pair_union",
    "in_canonical_tf_role_any_species", "in_canonical_tf_role_exact_species",
    "in_module_22B_exact_species", "in_current_canonical_any_species",
    "dedupe_status", "review_status", "notes",
]

CROSS_SPECIES_FIELDS = [
    "tf_key", "display_symbols", "species_scopes", "source_registries",
    "reported_contributor_labels", "human_current_sets", "mouse_current_sets",
    "vertebrate_profile_current_sets", "human_status", "mouse_status",
    "vertebrate_profile_status", "current_entity_ids", "species_scope_count",
    "current_any_species", "new_species_scopes", "dedupe_status", "notes",
]

CURRENT_SET_FIELDS = [
    "current_set", "current_id", "species_scope", "tf_symbol", "tf_key",
    "role_status", "module_code",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def run_psql(psql: str, database: str, query: str) -> list[dict[str, str]]:
    result = subprocess.run(
        [psql, "-X", "--csv", "-v", "ON_ERROR_STOP=1", "-d", database, "-c", query],
        check=True,
        capture_output=True,
        text=True,
    )
    return list(csv.DictReader(io.StringIO(result.stdout)))


def null_text(value: str | None) -> str:
    text = (value or "").strip()
    return "" if text in {r"\N", "NULL", "null"} else text


def sql_current_sets() -> str:
    # canonical_name is the fallback because several existing TF entities were
    # created before gene_symbol was populated.  This keeps their entity IDs
    # and canonical names traceable in the crosswalk instead of dropping them.
    return """
WITH canonical_tf AS (
  SELECT
    e.entity_id::text AS current_id,
    lower(NULLIF(btrim(coalesce(e.organism_scope, '')), '')) AS species_scope,
    coalesce(NULLIF(btrim(e.gene_symbol), ''), NULLIF(btrim(e.canonical_name), '')) AS tf_symbol,
    r.role_status,
    ''::text AS module_code
  FROM SignalingEntity e
  JOIN SignalingEntityRole r ON r.entity_id = e.entity_id
  WHERE r.role = 'transcription_factor'
    AND r.export_priority <> 'exclude'
),
canonical_edges AS (
  SELECT DISTINCT
    e.entity_id::text AS current_id,
    lower(NULLIF(btrim(coalesce(e.organism_scope, '')), '')) AS species_scope,
    coalesce(NULLIF(btrim(e.gene_symbol), ''), NULLIF(btrim(e.canonical_name), '')) AS tf_symbol,
    r.role_status,
    ''::text AS module_code
  FROM SignalingEntity e
  JOIN SignalingEntityRole r ON r.entity_id = e.entity_id
  JOIN SignalingEdge edge ON edge.source_entity_id = e.entity_id
  WHERE r.role = 'transcription_factor'
    AND r.export_priority <> 'exclude'
    AND edge.export_priority <> 'exclude'
),
module_22b AS (
  SELECT DISTINCT
    e.entity_id::text AS current_id,
    lower(btrim(reg.species_context)) AS species_scope,
    coalesce(NULLIF(btrim(e.gene_symbol), ''), NULLIF(btrim(e.canonical_name), '')) AS tf_symbol,
    reg.definition_status AS role_status,
    '22B'::text AS module_code
  FROM Regulon reg
  JOIN SignalingEntity e ON e.entity_id = reg.tf_entity_id
  WHERE reg.source_registry = 'public_tf_pair_review'
    AND reg.definition_status <> 'deprecated'
)
SELECT 'canonical_tf_role' AS current_set, current_id, coalesce(species_scope, 'unspecified') AS species_scope,
       tf_symbol, lower(tf_symbol) AS tf_key, role_status, module_code FROM canonical_tf
WHERE tf_symbol IS NOT NULL AND btrim(tf_symbol) <> ''
UNION ALL
SELECT 'canonical_tf_edge' AS current_set, current_id, coalesce(species_scope, 'unspecified') AS species_scope,
       tf_symbol, lower(tf_symbol) AS tf_key, role_status, module_code FROM canonical_edges
WHERE tf_symbol IS NOT NULL AND btrim(tf_symbol) <> ''
UNION ALL
SELECT 'module_22B_regulon' AS current_set, current_id, species_scope,
       tf_symbol, lower(tf_symbol) AS tf_key, role_status, module_code FROM module_22b
WHERE tf_symbol IS NOT NULL AND btrim(tf_symbol) <> ''
ORDER BY 1, 3, 5, 2;
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--database", default=DEFAULT_DATABASE)
    parser.add_argument("--psql", default=DEFAULT_PSQL)
    args = parser.parse_args()

    candidates = read_tsv(args.input_dir / "tf_candidate_union.tsv")
    identities = read_tsv(args.input_dir / "tf_identity_records.tsv")
    pair_records = read_tsv(args.input_dir / "tf_pair_records.tsv")
    contributor_links = read_tsv(args.input_dir / "reported_contributor_links.tsv")
    current_rows = run_psql(args.psql, args.database, sql_current_sets())
    for row in current_rows:
        row["species_scope"] = null_text(row.get("species_scope")) or "unspecified"
        row["tf_symbol"] = null_text(row.get("tf_symbol"))
        row["tf_key"] = null_text(row.get("tf_key")) or row["tf_symbol"].casefold()

    current_by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    current_any_by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in current_rows:
        if not row["tf_key"]:
            continue
        current_by_key[(row["species_scope"], row["tf_key"])].append(row)
        current_any_by_key[row["tf_key"]].append(row)

    public_pair_keys = {
        (row["species_scope"], row["normalized_tf_symbol_key"])
        for row in pair_records
        if row["species_scope"] in {"human", "mouse"} and row["normalized_tf_symbol_key"]
    }

    identity_by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in identities:
        if row["normalized_symbol_key"]:
            identity_by_key[(row["species_scope"], row["normalized_symbol_key"])].append(row)

    pair_records_by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in pair_records:
        if row["normalized_tf_symbol_key"]:
            pair_records_by_key[(row["species_scope"], row["normalized_tf_symbol_key"])].append(row)

    contributors_by_key: dict[tuple[str, str], set[str]] = defaultdict(set)
    pair_key_to_species_tf = {
        row["pair_record_key"]: (row["species_scope"], row["normalized_tf_symbol_key"])
        for row in pair_records
        if row["normalized_tf_symbol_key"]
    }
    for row in contributor_links:
        pair_key = pair_key_to_species_tf.get(row["external_record_key"])
        if pair_key:
            contributors_by_key[pair_key].add(row["raw_source_label"])

    crosswalk: list[dict[str, object]] = []
    for candidate in candidates:
        species = candidate["species_scope"]
        key = candidate["tf_key"]
        current_exact = current_by_key.get((species, key), [])
        current_any = current_any_by_key.get(key, [])
        current_sets = sorted({row["current_set"] for row in current_any})
        exact_sets = sorted({row["current_set"] for row in current_exact})
        entity_ids = sorted({row["current_id"] for row in current_any if row["current_id"]})
        module_codes = sorted({row["module_code"] for row in current_any if row["module_code"]})
        in_public = (species, key) in public_pair_keys
        in_role_any = "canonical_tf_role" in {row["current_set"] for row in current_any}
        in_role_exact = "canonical_tf_role" in {row["current_set"] for row in current_exact}
        in_22b_exact = "module_22B_regulon" in {row["current_set"] for row in current_exact}
        if in_public:
            status = "existing_public_pair_union"
        elif in_22b_exact or in_role_exact:
            status = "already_canonical_identity"
        elif current_any:
            status = "canonical_name_or_species_scope_match"
        else:
            status = "new_candidate"
        notes = []
        if species == "vertebrates":
            notes.append("JASPAR/profile scope is vertebrate-level; no human/mouse evidence is merged from this row.")
        if exact_sets != current_sets:
            notes.append("Current-set flags include any-species canonical matches; exact-species matches are reported separately.")
        crosswalk.append({
            "candidate_key": candidate["candidate_key"],
            "species_scope": species,
            "tf_symbol": candidate["tf_symbol"],
            "tf_key": key,
            "source_registries": candidate["source_registries"],
            "source_versions": candidate["source_versions"],
            "reported_contributor_labels": candidate["reported_contributor_labels"],
            "identity_source_count": candidate["identity_source_count"],
            "regulon_record_count": candidate["regulon_record_count"],
            "unique_reference_pmids": candidate["unique_reference_pmids"],
            "catalog_profile_count": candidate["catalog_profile_count"],
            "tflink_target_count": candidate["tflink_target_count"],
            "current_sets": ";".join(current_sets),
            "current_entity_ids": ";".join(entity_ids),
            "current_module_codes": ";".join(module_codes),
            "in_existing_public_pair_union": "true" if in_public else "false",
            "in_canonical_tf_role_any_species": "true" if in_role_any else "false",
            "in_canonical_tf_role_exact_species": "true" if in_role_exact else "false",
            "in_module_22B_exact_species": "true" if in_22b_exact else "false",
            "in_current_canonical_any_species": "true" if current_any else "false",
            "dedupe_status": status,
            "review_status": "new_candidate" if status == "new_candidate" else "cross_referenced",
            "notes": "; ".join(notes),
        })

    by_tf: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in crosswalk:
        by_tf[row["tf_key"]].append(row)
    collapsed: list[dict[str, object]] = []
    for key, rows in sorted(by_tf.items()):
        scopes = {row["species_scope"] for row in rows}
        def field_values(field: str) -> set[str]:
            return {value for row in rows for value in str(row.get(field, "")).split(";") if value}
        def current_sets_for(scope: str) -> str:
            return ";".join(sorted({value for row in rows if row["species_scope"] == scope for value in str(row["current_sets"]).split(";") if value}))
        statuses = {row["dedupe_status"] for row in rows}
        new_scopes = [scope for scope in sorted(scopes) if not any(row["species_scope"] == scope and row["dedupe_status"] != "new_candidate" for row in rows)]
        notes = []
        if len(scopes) > 1:
            notes.append("Cross-species inventory collapse only; retain species-specific evidence records separately.")
        if "vertebrates" in scopes:
            notes.append("Vertebrate JASPAR/profile scope is not treated as human/mouse evidence.")
        collapsed.append({
            "tf_key": key,
            "display_symbols": ";".join(sorted({row["tf_symbol"] for row in rows})),
            "species_scopes": ";".join(sorted(scopes)),
            "source_registries": ";".join(sorted(field_values("source_registries"))),
            "reported_contributor_labels": ";".join(sorted(field_values("reported_contributor_labels"))),
            "human_current_sets": current_sets_for("human"),
            "mouse_current_sets": current_sets_for("mouse"),
            "vertebrate_profile_current_sets": current_sets_for("vertebrates"),
            "human_status": ";".join(sorted({row["dedupe_status"] for row in rows if row["species_scope"] == "human"})),
            "mouse_status": ";".join(sorted({row["dedupe_status"] for row in rows if row["species_scope"] == "mouse"})),
            "vertebrate_profile_status": ";".join(sorted({row["dedupe_status"] for row in rows if row["species_scope"] == "vertebrates"})),
            "current_entity_ids": ";".join(sorted({value for row in rows for value in str(row["current_entity_ids"]).split(";") if value})),
            "species_scope_count": len(scopes),
            "current_any_species": "true" if any(row["in_current_canonical_any_species"] == "true" for row in rows) else "false",
            "new_species_scopes": ";".join(new_scopes),
            "dedupe_status": "existing_or_canonical" if statuses != {"new_candidate"} else "new_candidate",
            "notes": "; ".join(notes),
        })

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_tsv(args.output_dir / "current_tf_sets.tsv", CURRENT_SET_FIELDS, current_rows)
    write_tsv(args.output_dir / "tf_candidate_crosswalk.tsv", CROSSWALK_FIELDS, crosswalk)
    write_tsv(args.output_dir / "tf_cross_species_collapsed.tsv", CROSS_SPECIES_FIELDS, collapsed)

    candidate_key_list = [row["candidate_key"] for row in candidates]
    crosswalk_key_list = [row["candidate_key"] for row in crosswalk]
    validation_checks = {
        "duplicate_crosswalk_keys": len(crosswalk_key_list) - len(set(crosswalk_key_list)),
        "crosswalk_rows_missing_from_input": len(set(candidate_key_list) - set(crosswalk_key_list)),
        "crosswalk_rows_not_in_input": len(set(crosswalk_key_list) - set(candidate_key_list)),
        "duplicate_cross_species_keys": len([row["tf_key"] for row in collapsed]) - len({row["tf_key"] for row in collapsed}),
        "crosswalk_rows_without_sources": sum(not row["source_registries"] for row in crosswalk),
        "crosswalk_rows_marked_promoted": sum(row["review_status"] not in {"new_candidate", "cross_referenced"} for row in crosswalk),
    }

    counts = {
        "current_set_rows": len(current_rows),
        "crosswalk_rows": len(crosswalk),
        "cross_species_collapsed_rows": len(collapsed),
        "cross_species_unique_tf_keys": len({row["tf_key"] for row in collapsed}),
        "cross_species_existing_or_canonical_unique_tf_keys": len({
            row["tf_key"] for row in collapsed if row["dedupe_status"] != "new_candidate"
        }),
        "cross_species_new_candidate_unique_tf_keys": len({
            row["tf_key"] for row in collapsed if row["dedupe_status"] == "new_candidate"
        }),
        "human_crosswalk_rows": sum(row["species_scope"] == "human" for row in crosswalk),
        "mouse_crosswalk_rows": sum(row["species_scope"] == "mouse" for row in crosswalk),
        "vertebrate_crosswalk_rows": sum(row["species_scope"] == "vertebrates" for row in crosswalk),
        "existing_public_pair_union_rows": sum(row["in_existing_public_pair_union"] == "true" for row in crosswalk),
        "canonical_tf_role_any_species_rows": sum(row["in_canonical_tf_role_any_species"] == "true" for row in crosswalk),
        "canonical_tf_role_exact_species_rows": sum(row["in_canonical_tf_role_exact_species"] == "true" for row in crosswalk),
        "module_22B_exact_species_rows": sum(row["in_module_22B_exact_species"] == "true" for row in crosswalk),
        "new_candidate_rows": sum(row["dedupe_status"] == "new_candidate" for row in crosswalk),
        "new_candidate_unique_tf_keys": len({row["tf_key"] for row in crosswalk if row["dedupe_status"] == "new_candidate"}),
        "existing_or_canonical_rows": sum(row["dedupe_status"] != "new_candidate" for row in crosswalk),
    }
    manifest = {
        "crosswalk_name": "public_tf_union_current_set_crosswalk_v1",
        "status": "staging_inventory_only",
        "database": args.database,
        "query_definition": "Current canonical TF role, canonical TF-edge, and Module 22B public_tf_pair_review regulon sets; canonical_name is used when gene_symbol is empty.",
        "deduplication_policy": "One crosswalk row per species scope plus normalized TF symbol. Human, mouse, and vertebrate-profile scopes remain distinct for evidence; tf_cross_species_collapsed.tsv is inventory-only.",
        "counts": counts,
        "outputs": ["current_tf_sets.tsv", "tf_candidate_crosswalk.tsv", "tf_cross_species_collapsed.tsv"],
        "validation_checks": validation_checks,
        "canonical_writes": False,
    }
    (args.output_dir / "crosswalk_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    validation = {
        "status": "pass" if all(value == 0 for value in validation_checks.values()) else "fail",
        "checks": validation_checks,
        "counts": counts,
    }
    (args.output_dir / "crosswalk_validation.json").write_text(json.dumps(validation, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.output_dir / "README.md").write_text(
        "# Current TF-set crosswalk\n\n"
        "This staging crosswalk matches the expanded TF candidate inventory against the current public TF pair union, canonical TF roles, canonical TF-edge participation, and Module 22B regulons.\n\n"
        "`tf_candidate_crosswalk.tsv` has one row per species scope plus normalized TF symbol, so its row counts are not counts of distinct TFs. `tf_cross_species_collapsed.tsv` is an inventory-only collapse by normalized symbol; human and mouse evidence must remain separate. The original source-specific pair records and contributor links remain in the parent expansion directory and are not deleted or collapsed.\n\n"
        "The manifest reports both `new_candidate_rows` and `new_candidate_unique_tf_keys`. The former counts species/source-scope rows; the latter is the deduplicated symbol count. Neither is a promotion or evidence-confidence count.\n\n"
        "The cross-species manifest fields further distinguish symbols that are new in at least one scope from symbols absent from the current sets in every scope. Use `cross_species_new_candidate_unique_tf_keys` for the inventory-level expansion queue.\n\n"
        "Canonical matching uses `gene_symbol` and falls back to `canonical_name` when the current entity lacks a gene symbol. Exact-species flags and any-species flags are reported separately. No canonical database rows were written by this crosswalk.\n",
        encoding="utf-8",
    )
    print(json.dumps(counts, sort_keys=True))


if __name__ == "__main__":
    main()
