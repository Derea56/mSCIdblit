#!/usr/bin/env python3
"""Materialize the completed agent TF curation into an evidence ledger.

This writes only review/staging artifacts.  It never inserts into the local
database and never changes the frozen Module 20–24 graph.  Public TF-target
assertions are routed to 22B unless a lane explicitly supplies a different
promoted module with the same pair-level evidence; cross-module observations
are retained in a separate review queue.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_v1"
DEFAULT_MERGED = DEFAULT_INPUT / "module_curation/agent_merged/priority_tf_agent_merged.tsv"
DEFAULT_BOUNDARY = DEFAULT_INPUT / "module_curation/agent_merged/priority_tf_agent_boundary_audit.tsv"
DEFAULT_OUTPUT = DEFAULT_INPUT / "module_curation/agent_materialized"

PMID_RE = re.compile(r"(?<!\d)(?:PMID\s*[:]?\s*)?(\d{7,9})(?!\d)", re.I)
NO_CROSS_MODULE = {
    "",
    "none",
    "not_applicable",
    "no_overlap_with_modules_20_21_23_24",
    "no_modules_20_21_23_24_overlap",
    "no_verified_cross_module_claim",
    "not_claimed",
}
TF_ALIASES = {
    ("mouse", "tp53"): {"tp53", "trp53"},
    ("mouse", "trp53"): {"tp53", "trp53"},
}
PRIORITY_TF_LABELS = {
    "tp53": "TP53", "trp53": "TP53", "jun": "JUN", "fos": "FOS", "myc": "MYC",
    "stat1": "STAT1", "hif1a": "HIF1A", "sp1": "SP1", "ets1": "ETS1", "runx1": "RUNX1",
    "gata3": "GATA3", "cebpb": "CEBPB", "irf1": "IRF1", "atf2": "ATF2", "egr1": "EGR1",
    "klf4": "KLF4", "nfkb2": "NFKB2",
}

LEDGER_FIELDS = [
    "curation_id", "pair_key", "module", "species", "tf_symbol", "target_symbol",
    "decision", "module_assignment", "evidence_status", "support_kind",
    "effect_polarity", "primary_pmids", "corroborating_pmids",
    "external_record_keys", "source_registries", "public_reference_pmids",
    "public_effect_polarities", "public_verification_statuses", "tf_entity_ids",
    "target_entity_ids", "tf_frozen_match_status", "target_frozen_match_status",
    "tf_role_present", "target_role_present", "cell_type_context", "stimulus_context",
    "shared_paper_status", "cross_module_status", "limitations", "notes",
    "graph_materialization_status",
]

SOURCE_LINK_FIELDS = [
    "curation_id", "pair_key", "link_type", "source_registry", "source_version",
    "species", "tf_symbol", "target_symbol", "external_record_key", "source_pmid",
    "source_locator", "source_locator_status", "source_kind", "support_kind",
    "evidence_scope", "citation_note", "limitations",
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
            writer.writerow({field: "" if row.get(field) is None else row.get(field, "") for field in fields})


def values(value: str) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for item in re.split(r"[;,]", value or ""):
        item = item.strip()
        if not item or item in {r"\N", "NA", "null"} or item in seen:
            continue
        seen.add(item)
        output.append(item)
    return output


def join_unique(items: list[str]) -> str:
    return ";".join(values(";".join(items)))


def pair_key(species: str, tf: str, target: str) -> str:
    return f"{species}|{tf}|{target}"


def actual_cross_module(value: str) -> bool:
    return (value or "").strip().casefold() not in NO_CROSS_MODULE


def source_tf_keys(species: str, tf: str) -> set[str]:
    return TF_ALIASES.get((species.casefold(), tf.casefold()), {tf.casefold()})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--merged", type=Path, default=DEFAULT_MERGED)
    parser.add_argument("--boundary", type=Path, default=DEFAULT_BOUNDARY)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    rows = read_tsv(args.merged)
    boundary_rows = read_tsv(args.boundary) if args.boundary.is_file() else []
    source_rows = read_tsv(args.input_dir / "source_records.tsv")
    mapping_rows = read_tsv(args.input_dir / "frozen_entity_mapping.tsv")

    source_by_pair: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for source in source_rows:
        source_by_pair[(
            source["species_context"].casefold(),
            source["tf_normalized_symbol"].casefold(),
            source["target_normalized_symbol"].casefold(),
        )].append(source)

    mapping_by_key: dict[tuple[str, str, str, str, str], list[dict[str, str]]] = defaultdict(list)
    for mapping in mapping_rows:
        mapping_by_key[(
            mapping["source_registry"], mapping["source_version"],
            mapping["species_context"].casefold(), mapping["identity_role"],
            mapping["normalized_symbol_key"].casefold(),
        )].append(mapping)

    decisions: list[dict[str, str]] = []
    promoted: list[dict[str, str]] = []
    holds: list[dict[str, str]] = []
    module_review: list[dict[str, str]] = []
    source_links: list[dict[str, str]] = []
    errors: list[str] = []

    for index, row in enumerate(rows, start=1):
        species = row["species"].strip().lower()
        tf = row["tf_symbol"].strip()
        target = row["target_symbol"].strip()
        key = pair_key(species, tf, target)
        promotion = row["decision"].startswith("promote_to_")
        cross_module = actual_cross_module(row.get("cross_module_status", ""))
        if promotion and not row["primary_pmids"].strip():
            errors.append(f"{key}: promoted row lacks primary PMID")
        if promotion and cross_module and not row["corroborating_pmids"].strip():
            errors.append(f"{key}: cross-module promotion lacks corroborating PMID")

        pair_rows: list[dict[str, str]] = []
        tf_keys = source_tf_keys(species, tf)
        for tf_key in tf_keys:
            pair_rows.extend(source_by_pair.get((species, tf_key, target.casefold()), []))
        pair_rows = list({source["external_record_key"]: source for source in pair_rows}.values())

        external_keys = join_unique([row.get("external_record_keys", "")] + [source["external_record_key"] for source in pair_rows])
        registries = join_unique([source["source_registry"] for source in pair_rows])
        public_pmids = join_unique([source.get("reference_pmids", "") for source in pair_rows])
        public_effects = join_unique([source.get("effect_polarity", "") for source in pair_rows])
        public_statuses = join_unique([source.get("verification_status", "") for source in pair_rows])

        tf_maps: list[dict[str, str]] = []
        target_maps: list[dict[str, str]] = []
        for source in pair_rows:
            tf_maps.extend(mapping_by_key[(
                source["source_registry"], source["source_version"], species, "tf",
                source["tf_normalized_symbol_key"].casefold(),
            )])
            target_maps.extend(mapping_by_key[(
                source["source_registry"], source["source_version"], species, "target",
                source["target_normalized_symbol_key"].casefold(),
            )])

        tf_entity_ids = join_unique([item.get("mscidblit_entity_id", "") for item in tf_maps])
        target_entity_ids = join_unique([item.get("mscidblit_entity_id", "") for item in target_maps])
        tf_match = join_unique([item.get("frozen_entity_match_status", "") for item in tf_maps])
        target_match = join_unique([item.get("frozen_entity_match_status", "") for item in target_maps])
        tf_role = "true" if any(item.get("frozen_tf_role_present") == "t" for item in tf_maps) else "false"
        target_role = "true" if any(item.get("frozen_target_role_present") == "t" for item in target_maps) else "false"
        module = row["decision"].removeprefix("promote_to_") if promotion else "22B"
        graph_status = "blocked;no_matching_public_record" if not pair_rows else "staged_evidence_only;canonical_entity_role_gate_pending" if promotion else "review_ledger_only"
        record = {
            "curation_id": f"PUBTF-AGENT-{index:05d}",
            "pair_key": key,
            "module": module,
            "species": species,
            "tf_symbol": tf,
            "target_symbol": target,
            "decision": row["decision"],
            "module_assignment": row["module_assignment"],
            "evidence_status": row["evidence_status"],
            "support_kind": row["support_kind"],
            "effect_polarity": row["effect_polarity"],
            "primary_pmids": row["primary_pmids"],
            "corroborating_pmids": row["corroborating_pmids"],
            "external_record_keys": external_keys,
            "source_registries": registries,
            "public_reference_pmids": public_pmids,
            "public_effect_polarities": public_effects,
            "public_verification_statuses": public_statuses,
            "tf_entity_ids": tf_entity_ids,
            "target_entity_ids": target_entity_ids,
            "tf_frozen_match_status": tf_match,
            "target_frozen_match_status": target_match,
            "tf_role_present": tf_role,
            "target_role_present": target_role,
            "cell_type_context": row["cell_type_context"],
            "stimulus_context": row["stimulus_context"],
            "shared_paper_status": row["shared_paper_status"],
            "cross_module_status": row["cross_module_status"],
            "limitations": row["limitations"],
            "notes": row["notes"],
            "graph_materialization_status": graph_status,
        }
        decisions.append(record)
        if promotion:
            promoted.append(record)
        else:
            holds.append(record)
        if cross_module:
            module_review.append(record)

        for source in pair_rows:
            source_links.append({
                "curation_id": record["curation_id"], "pair_key": key,
                "link_type": "public_record_provenance",
                "source_registry": source["source_registry"], "source_version": source["source_version"],
                "species": source["species_context"], "tf_symbol": source["tf_normalized_symbol"],
                "target_symbol": source["target_normalized_symbol"],
                "external_record_key": source["external_record_key"],
                "source_pmid": source.get("reference_pmids", ""),
                "source_locator": source.get("source_locator", ""),
                "source_locator_status": "public_record_locator", "source_kind": "public_tf_union_record",
                "support_kind": source.get("evidence_basis", "database_curated"),
                "evidence_scope": "public_record_reference_lead",
                "citation_note": "Public record retained as provenance lead; not treated as proof without pair-level literature adjudication.",
                "limitations": source.get("limitations", ""),
            })
        for link_type, pmid_value, support_kind, note in (
            ("verified_primary", row["primary_pmids"], "primary_experiment", "Exact-pair primary source selected during agent evidence review."),
            ("corroborating_primary", row["corroborating_pmids"], "primary_experiment", "Independent corroborating primary source; kept separate from the primary source."),
        ):
            for pmid in values(pmid_value):
                source_links.append({
                    "curation_id": record["curation_id"], "pair_key": key, "link_type": link_type,
                    "source_registry": "manual_pair_review", "source_version": "agent_lanes_v1",
                    "species": species, "tf_symbol": tf, "target_symbol": target,
                    "external_record_key": external_keys, "source_pmid": pmid,
                    "source_locator": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                    "source_locator_status": "pubmed_locator", "source_kind": "primary_literature",
                    "support_kind": support_kind, "evidence_scope": row["support_kind"],
                    "citation_note": note, "limitations": row["limitations"],
                })

    coverage: dict[str, set[str]] = defaultdict(set)
    for item in decisions:
        coverage[PRIORITY_TF_LABELS.get(item["tf_symbol"].casefold(), item["tf_symbol"].upper())].add(item["species"])

    manifest = {
        "status": "pass" if not errors else "fail",
        "decision_rows": len(decisions),
        "promoted_rows": len(promoted),
        "held_rows": len(holds),
        "module_specific_review_rows": len(module_review),
        "boundary_audit_rows": len(boundary_rows),
        "source_link_rows": len(source_links),
        "decision_counts": dict(Counter(row["decision"] for row in decisions)),
        "promotion_module_counts": dict(Counter(row["module"] for row in promoted)),
        "tf_species_coverage": {tf: sorted(species) for tf, species in sorted(coverage.items())},
        "errors": errors,
        "canonical_database_writes": False,
        "frozen_release_modified": False,
        "policy": {
            "public_tf_default_module": "22B",
            "cross_module_evidence": "retained in module_specific_review_queue.tsv; no citation-overlap-only promotion",
            "independent_corroboration": "required for promoted rows with actual cross-module relevance",
        },
    }
    if not errors:
        write_tsv(args.output_dir / "priority_tf_agent_decisions.tsv", LEDGER_FIELDS, decisions)
        write_tsv(args.output_dir / "priority_tf_agent_promoted.tsv", LEDGER_FIELDS, promoted)
        write_tsv(args.output_dir / "priority_tf_agent_hold_queue.tsv", LEDGER_FIELDS, holds)
        write_tsv(args.output_dir / "module_specific_review_queue.tsv", LEDGER_FIELDS, module_review)
        write_tsv(args.output_dir / "boundary_audit_queue.tsv", LEDGER_FIELDS, boundary_rows)
        write_tsv(args.output_dir / "priority_tf_agent_source_links.tsv", SOURCE_LINK_FIELDS, source_links)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "priority_tf_agent_materialization_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
