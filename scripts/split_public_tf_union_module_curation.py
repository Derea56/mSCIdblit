#!/usr/bin/env python3
"""Split the public TF union into evidence-review lanes for Modules 20–24.

This is a file-based planning/audit step. It does not promote anything into
the frozen mechanism graph or the canonical database tables. Public TF→target
assertions belong to Module 22A/22B by default. A cited paper can create a
cross-module corroboration queue, but paper reuse is never treated as new
independent evidence automatically.
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
DEFAULT_OUTPUT = DEFAULT_INPUT / "module_curation"

PRIORITY_TFS = {
    "tp53",
    "jun",
    "fos",
    "myc",
    "stat1",
    "hif1a",
    "sp1",
    "ets1",
    "runx1",
    "gata3",
    "cebpb",
    "irf1",
    "atf2",
    "egr1",
    "klf4",
    "nfkb2",
}

PMID_RE = re.compile(r"(?<!\d)(?:PMID\s*[:]?\s*)?(\d{7,9})(?!\d)", re.I)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            delimiter="\t",
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({key: "" if value is None else value for key, value in row.items()})


def pmids(value: str) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for match in PMID_RE.finditer(value or ""):
        identifier = match.group(1)
        if identifier not in seen:
            seen.add(identifier)
            output.append(identifier)
    return output


def bool_text(value: object) -> str:
    return "true" if bool(value) else "false"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--graph-dir",
        type=Path,
        default=ROOT / "data/processed/mechanism_graph_module20_24_v2026_08_25",
    )
    args = parser.parse_args()

    records = read_tsv(args.input_dir / "source_records.tsv")
    mappings = read_tsv(args.input_dir / "frozen_entity_mapping.tsv")
    priority_evidence = read_tsv(args.input_dir / "priority_tf_evidence.tsv")
    graph_sources = read_tsv(args.graph_dir / "mechanism_edge_sources.tsv")
    graph_edges = read_tsv(args.graph_dir / "mechanism_edges.tsv")

    mapping_index: dict[tuple[str, str, str, str, str], dict[str, str]] = {}
    for row in mappings:
        key = (
            row["source_registry"],
            row["source_version"],
            row["species_context"],
            row["identity_role"],
            row["normalized_symbol_key"],
        )
        mapping_index[key] = row

    priority_by_record: dict[str, list[dict[str, str]]] = defaultdict(list)
    priority_by_tf: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in priority_evidence:
        record_key = row.get("external_record_key", "")
        if record_key and record_key != r"\N":
            priority_by_record[record_key].append(row)
        priority_by_tf[row["priority_tf_symbol"].casefold()].append(row)

    edge_by_id = {row["edge_id"]: row for row in graph_edges}
    module_by_pmid: dict[str, set[str]] = defaultdict(set)
    edge_ids_by_pmid: dict[str, set[str]] = defaultdict(set)
    source_evidence_by_pmid: dict[str, list[dict[str, str]]] = defaultdict(list)
    for source in graph_sources:
        text = " ".join(
            source.get(key, "")
            for key in (
                "source_locator",
                "citation_note",
                "evidence_summary",
                "limitations",
                "consolidation_note",
            )
        )
        source_pmids = pmids(text)
        edge_id = source.get("edge_id", "")
        edge = edge_by_id.get(edge_id, {})
        module = source.get("module") or edge.get("module") or ""
        for identifier in source_pmids:
            module_by_pmid[identifier].add(module)
            edge_ids_by_pmid[identifier].add(edge_id)
            source_evidence_by_pmid[identifier].append(source)

    public_pair_by_pmid: dict[str, set[str]] = defaultdict(set)
    public_record_by_pmid: dict[str, set[str]] = defaultdict(set)
    for row in records:
        pair_key = f"{row['species_context']}|{row['tf_normalized_symbol_key']}|{row['target_normalized_symbol_key']}"
        for identifier in pmids(row.get("reference_pmids", "")):
            public_pair_by_pmid[identifier].add(pair_key)
            public_record_by_pmid[identifier].add(row["external_record_key"])

    queue_rows: list[dict[str, object]] = []
    priority_rows: list[dict[str, object]] = []
    shared_rows: list[dict[str, object]] = []
    public_reuse_rows: list[dict[str, object]] = []
    summary: Counter[str] = Counter()
    batch_counts: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)
    batch_records: dict[tuple[str, str], set[str]] = defaultdict(set)

    for row in records:
        tf = row["tf_normalized_symbol"]
        target = row["target_normalized_symbol"]
        species = row["species_context"]
        tf_key = row["tf_normalized_symbol_key"]
        target_key = row["target_normalized_symbol_key"]
        tf_map = mapping_index.get(
            (row["source_registry"], row["source_version"], species, "tf", tf_key), {}
        )
        target_map = mapping_index.get(
            (row["source_registry"], row["source_version"], species, "target", target_key), {}
        )
        record_priority = tf_key in PRIORITY_TFS
        record_verifications = priority_by_record.get(row["external_record_key"], [])
        record_verified = any(
            item.get("verification_status") == "primary_reference_verified"
            for item in record_verifications
        )
        record_context_limited = any(
            item.get("verification_status") == "context_limited_reference"
            for item in record_verifications
        )
        record_unverified = any(
            item.get("verification_status") == "database_curated_unverified"
            for item in record_verifications
        )
        source_pmids = pmids(row.get("reference_pmids", ""))
        shared_pmids = sorted(identifier for identifier in source_pmids if module_by_pmid.get(identifier))
        reused_pmids = sorted(identifier for identifier in source_pmids if len(public_pair_by_pmid.get(identifier, set())) > 1)
        shared_modules = sorted({module for identifier in source_pmids for module in module_by_pmid.get(identifier, set()) if module})
        cross_module_shared = len(set(shared_modules) & {"20B", "21B", "23B", "24B"}) > 0
        shared_with_tf_module = "22B" in shared_modules
        if cross_module_shared or reused_pmids:
            reuse_status = "corroboration_required"
            if cross_module_shared:
                summary["cross_module_shared_paper_records"] += 1
            if reused_pmids:
                summary["public_reference_reuse_records"] += 1
        elif shared_with_tf_module:
            reuse_status = "same_module_paper_overlap_review"
            summary["same_module_shared_paper_records"] += 1
        else:
            reuse_status = "no_existing_module_paper_overlap"

        if record_priority:
            action = "priority_tf_review"
            summary["priority_tf_records"] += 1
        elif row["verification_status"] == "database_curated_unverified":
            action = "database_only_hold"
            summary["database_only_records"] += 1
        else:
            action = "source_record_review"

        if reuse_status == "corroboration_required":
            action = "shared_paper_corroboration_before_promotion"

        pair_key = f"{species}|{tf_key}|{target_key}"
        queue_row = {
            "curation_id": f"PUBTF-CUR-{len(queue_rows) + 1:06d}",
            "pair_key": pair_key,
            "external_record_key": row["external_record_key"],
            "source_registry": row["source_registry"],
            "source_version": row["source_version"],
            "species_context": species,
            "tf_symbol": tf,
            "target_symbol": target,
            "tf_entity_id": tf_map.get("mscidblit_entity_id", ""),
            "target_entity_id": target_map.get("mscidblit_entity_id", ""),
            "tf_frozen_match_status": tf_map.get("frozen_entity_match_status", ""),
            "target_frozen_match_status": target_map.get("frozen_entity_match_status", ""),
            "tf_role_present": tf_map.get("frozen_tf_role_present", "false"),
            "target_role_present": target_map.get("frozen_target_role_present", "false"),
            "effect_polarity": row["effect_polarity"],
            "relationship_class": row["relationship_class"],
            "evidence_basis": row["evidence_basis"],
            "confidence_tier": row["confidence_tier"],
            "dorothea_level": row["dorothea_level"],
            "reference_pmids": ";".join(source_pmids),
            "shared_existing_module_pmids": ";".join(shared_pmids),
            "public_reference_reuse_pmids": ";".join(reused_pmids),
            "public_reference_reuse_item_count": max(
                [len(public_pair_by_pmid.get(identifier, set())) for identifier in source_pmids] or [0]
            ),
            "existing_module_overlap": ";".join(shared_modules),
            "existing_overlap_edge_count": sum(len(edge_ids_by_pmid.get(identifier, set())) for identifier in source_pmids),
            "module_assignment": "22A/22B",
            "module_assignment_reason": "Public TF-target/regulon assertion; downstream program layer.",
            "reuse_status": reuse_status,
            "curation_action": action,
            "promotion_status": "not_promoted",
            "promotion_note": "Requires exact-pair evidence review; database presence is not sufficient.",
        }
        queue_rows.append(queue_row)
        if record_priority:
            priority_rows.append(queue_row)
            batch_key = (tf.upper(), species)
            batch_counts[batch_key]["records"] += 1
            batch_records[batch_key].add(pair_key)
            if record_verified:
                batch_counts[batch_key]["primary_verified_record_rows"] += 1
            if record_context_limited:
                batch_counts[batch_key]["context_limited_record_rows"] += 1
            if record_unverified:
                batch_counts[batch_key]["database_curated_unverified_rows"] += 1
        if reused_pmids:
            public_reuse_rows.append(
                {
                    "curation_id": queue_row["curation_id"],
                    "external_record_key": row["external_record_key"],
                    "species_context": species,
                    "tf_symbol": tf,
                    "target_symbol": target,
                    "reference_pmids": ";".join(source_pmids),
                    "public_reference_reuse_pmids": ";".join(reused_pmids),
                    "public_reference_reuse_item_count": max(
                        [len(public_pair_by_pmid.get(identifier, set())) for identifier in source_pmids] or [0]
                    ),
                    "existing_modules": ";".join(shared_modules),
                    "status": "needs_corroboration_if_cross_module_claim_is_reused" if cross_module_shared else "reference_reuse_review",
                }
            )
        if cross_module_shared:
            shared_rows.append(
                {
                    "curation_id": queue_row["curation_id"],
                    "external_record_key": row["external_record_key"],
                    "species_context": species,
                    "tf_symbol": tf,
                    "target_symbol": target,
                    "reference_pmids": ";".join(source_pmids),
                    "shared_existing_module_pmids": ";".join(shared_pmids),
                    "public_reference_reuse_pmids": ";".join(reused_pmids),
                    "public_reference_reuse_item_count": max(
                        [len(public_pair_by_pmid.get(identifier, set())) for identifier in source_pmids] or [0]
                    ),
                    "existing_modules": ";".join(shared_modules),
                    "existing_edge_ids": ";".join(sorted({edge_id for identifier in source_pmids for edge_id in edge_ids_by_pmid.get(identifier, set()) if edge_id})),
                    "public_module": "22A/22B",
                    "corroboration_requirement": "Find an independent supporting paper for at least one reused item before promoting the shared-paper claim.",
                    "status": "needs_corroboration",
                }
            )

    module_fields = list(queue_rows[0].keys()) if queue_rows else []
    write_tsv(args.output_dir / "module_curation_queue.tsv", module_fields, queue_rows)
    write_tsv(args.output_dir / "module_22_priority_tf_review_queue.tsv", module_fields, priority_rows)
    write_tsv(
        args.output_dir / "cross_module_shared_paper_corroboration.tsv",
        [
            "curation_id",
            "external_record_key",
            "species_context",
            "tf_symbol",
            "target_symbol",
            "reference_pmids",
            "shared_existing_module_pmids",
            "public_reference_reuse_pmids",
            "public_reference_reuse_item_count",
            "existing_modules",
            "existing_edge_ids",
            "public_module",
            "corroboration_requirement",
            "status",
        ],
        shared_rows,
    )
    write_tsv(
        args.output_dir / "public_reference_reuse_review.tsv",
        [
            "curation_id",
            "external_record_key",
            "species_context",
            "tf_symbol",
            "target_symbol",
            "reference_pmids",
            "public_reference_reuse_pmids",
            "public_reference_reuse_item_count",
            "existing_modules",
            "status",
        ],
        public_reuse_rows,
    )

    paper_rows = []
    for identifier in sorted(set(public_pair_by_pmid) | set(module_by_pmid)):
        public_items = sorted(public_pair_by_pmid.get(identifier, set()))
        existing_modules = sorted(module_by_pmid.get(identifier, set()))
        if len(public_items) <= 1 and not existing_modules:
            continue
        paper_rows.append(
            {
                "pmid": identifier,
                "public_unique_item_count": len(public_items),
                "public_record_count": len(public_record_by_pmid.get(identifier, set())),
                "existing_module_count": len(existing_modules),
                "existing_modules": ";".join(existing_modules),
                "public_item_keys": ";".join(public_items),
                "cross_module_overlap": bool_text(bool(set(existing_modules) & {"20B", "21B", "23B", "24B"})),
                "corroboration_status": "needs_corroboration" if len(public_items) > 1 and existing_modules else "reference_reuse_review",
            }
        )
    write_tsv(
        args.output_dir / "reference_paper_reuse_audit.tsv",
        [
            "pmid",
            "public_unique_item_count",
            "public_record_count",
            "existing_module_count",
            "existing_modules",
            "public_item_keys",
            "cross_module_overlap",
            "corroboration_status",
        ],
        paper_rows,
    )

    for module in ("20B", "21B", "23B", "24B"):
        module_rows = [row for row in shared_rows if module in str(row["existing_modules"]).split(";")]
        write_tsv(
            args.output_dir / f"module_{module.lower()}_corroboration_queue.tsv",
            [
                "curation_id",
                "external_record_key",
                "species_context",
                "tf_symbol",
                "target_symbol",
                "reference_pmids",
                "shared_existing_module_pmids",
                "public_reference_reuse_pmids",
                "public_reference_reuse_item_count",
                "existing_modules",
                "existing_edge_ids",
                "public_module",
                "corroboration_requirement",
                "status",
            ],
            module_rows,
        )

    batch_rows: list[dict[str, object]] = []
    for (tf, species), counts in sorted(batch_counts.items()):
        batch_rows.append(
            {
                "batch_id": f"M22-CUR-{len(batch_rows) + 1:03d}",
                "module": "22A/22B",
                "priority_tf": tf,
                "species_context": species,
                "record_count": counts["records"],
                "unique_pair_count": len(batch_records[(tf, species)]),
                "primary_verified_record_rows": counts["primary_verified_record_rows"],
                "context_limited_record_rows": counts["context_limited_record_rows"],
                "database_curated_unverified_rows": counts["database_curated_unverified_rows"],
                "review_order": "priority_tf_exact_pair_review",
                "promotion_gate": "primary or corroborating exact-pair evidence with species/context/assay limits recorded",
            }
        )
    write_tsv(
        args.output_dir / "module_22_priority_tf_batch_plan.tsv",
        [
            "batch_id",
            "module",
            "priority_tf",
            "species_context",
            "record_count",
            "unique_pair_count",
            "primary_verified_record_rows",
            "context_limited_record_rows",
            "database_curated_unverified_rows",
            "review_order",
            "promotion_gate",
        ],
        batch_rows,
    )

    module_queue_counts = Counter({"22A/22B": len(queue_rows)})
    for row in shared_rows:
        for module in str(row["existing_modules"]).split(";"):
            if module in {"20B", "21B", "23B", "24B"}:
                module_queue_counts[module] += 1
    manifest = {
        "status": "staged_for_curation",
        "source_records": len(records),
        "priority_tf_records": len(priority_rows),
        "cross_module_shared_paper_records": sum(
            1 for row in queue_rows if set(str(row["existing_module_overlap"]).split(";")) & {"20B", "21B", "23B", "24B"}
        ),
        "public_reference_reuse_records": len(public_reuse_rows),
        "reference_paper_reuse_audit_rows": len(paper_rows),
        "module_queue_counts": dict(sorted(module_queue_counts.items())),
        "priority_tfs": sorted(PRIORITY_TFS),
        "summary": dict(sorted(summary.items())),
        "promotion_policy": {
            "default_public_tf_route": "22A/22B",
            "cross_module_paper_reuse": "requires independent corroboration before promotion",
            "frozen_release_modified": False,
            "automatic_promotions": False,
        },
    }
    (args.output_dir / "module_curation_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
