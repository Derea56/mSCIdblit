#!/usr/bin/env python3
"""Reconcile explicit SCI context in Module 20B-24B evidence with the SCI pack.

The audit reads the canonical phase-2 extraction ledger and the existing SCI
context pack. It retains only source-derived context fields, matches exact
PMID/PMCID/DOI identifiers where present, and reports whether a module record
is already represented in the context pack or remains module-only. It does not
import observations, create graph edges, or infer proximity.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACK = ROOT / "context_packs" / "spinal_cord_injury"
DEFAULT_MODULE_LEDGER = (
    ROOT / "work/cross_module_synthesis/canonical_evidence_review/"
    "module20_24_integrated_phase2_extractions.tsv"
)
DEFAULT_SPATIAL_AUDIT = DEFAULT_PACK / "spatial_localization_audit.tsv"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.build_sci_context_pack import read_tsv

SCI_CONTEXT_FIELDS = (
    "observation_value_or_blocker",
    "observation_source_section",
    "observation_figure_or_table",
    "observation_species",
    "observation_cell_or_model",
    "observation_assay",
    "observation_perturbation",
    "claim_text_or_blocker",
    "claim_source_section",
)

SCI_INJURY = re.compile(
    r"\b(?:spinal[- ]cord injury|spinal[- ]cord[- ]injur(?:y|ed)|"
    r"spinal[- ]injur(?:y|ed)|injured spinal[- ]cord|cord injury|"
    r"SCI model|SCI tissue|contusive SCI|compression SCI|after SCI|"
    r"spinal contusion|contusion.*spinal|dorsal[- ]column lesion|"
    r"spinal lesion|hemisection|transection)\b",
    re.IGNORECASE,
)
SPINAL_CORD = re.compile(r"\bspinal[- ]cord\b", re.IGNORECASE)
EXCLUSION = re.compile(
    r"\b(?:not (?:an? )?SCI|non[- ]SCI|does not (?:use|report|establish).*?\bSCI\b|"
    r"without SCI|not a spinal[- ]cord injury model|not SCI-specific|"
    r"SCI transfer (?:was )?excluded)\b",
    re.IGNORECASE,
)

OUTPUT_FIELDS = [
    "module",
    "extraction_id",
    "b_edge_id",
    "b_evidence_id",
    "module_dependency_group",
    "canonical_paper_key",
    "module_source_locator",
    "paper_status",
    "observation_status",
    "evidence_layer",
    "confidence",
    "observation_value_or_blocker",
    "observation_source_section",
    "observation_figure_or_table",
    "observation_species",
    "observation_cell_or_model",
    "observation_assay",
    "observation_perturbation",
    "claim_text_or_blocker",
    "claim_source_section",
    "source_context_class",
    "source_context_basis_fields",
    "source_context_terms",
    "source_identifier_keys",
    "context_pack_match_status",
    "matched_context_observation_ids",
    "matched_context_ids",
    "matched_context_source_artifact_paths",
    "matched_context_source_artifact_sha256",
    "spatial_audit_match_status",
    "matched_spatial_observation_ids",
    "matched_spatial_primary_classes",
    "matched_spatial_source_artifact_paths",
    "matched_spatial_source_artifact_sha256",
    "promotion_state",
    "audit_note",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_identifier(kind: str, value: str) -> str:
    return f"{kind}:{value.strip().lower()}"


def source_identifiers(*values: str) -> set[str]:
    text = " | ".join(value or "" for value in values)
    identifiers: set[str] = set()
    identifiers.update(normalize_identifier("PMID", value) for value in re.findall(r"\bPMID\s*:?\s*(\d+)\b", text, re.IGNORECASE))
    identifiers.update(normalize_identifier("PMCID", value) for value in re.findall(r"\b(PMC\d+)\b", text, re.IGNORECASE))
    for value in re.findall(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", text, re.IGNORECASE):
        identifiers.add(normalize_identifier("DOI", value.rstrip(".,;)]")))
    return identifiers


def write_tsv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def context_class(row: dict[str, str]) -> tuple[str, list[str], list[str], str]:
    hits: list[str] = []
    basis: list[str] = []
    exclusion = False
    for field in SCI_CONTEXT_FIELDS:
        value = row.get(field, "") or ""
        if not value:
            continue
        injury_hits = SCI_INJURY.findall(value)
        cord_hits = SPINAL_CORD.findall(value)
        if injury_hits or cord_hits:
            basis.append(field)
            hits.extend(injury_hits or cord_hits)
        if EXCLUSION.search(value):
            exclusion = True
    if not hits:
        return "no_explicit_spinal_cord_context", [], [], "not_eligible"
    if exclusion:
        return "explicit_context_with_exclusion_language", sorted(set(basis)), sorted(set(hits)), "review_required"
    if any(SCI_INJURY.search(hit) for hit in hits) or SCI_INJURY.search(" ".join(hits)):
        return "explicit_sci_injury_context", sorted(set(basis)), sorted(set(hits)), "eligible"
    return "explicit_spinal_cord_context", sorted(set(basis)), sorted(set(hits)), "eligible"


def index_pack_rows(rows: list[dict[str, str]], identifier_fields: tuple[str, ...]) -> dict[str, list[dict[str, str]]]:
    index: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        for identifier in source_identifiers(*(row.get(field, "") for field in identifier_fields)):
            index[identifier].append(row)
    return index


def unique_values(rows: list[dict[str, str]], field: str) -> list[str]:
    return sorted({row.get(field, "") for row in rows if row.get(field, "")})


def build(
    pack: Path = DEFAULT_PACK,
    module_ledger: Path = DEFAULT_MODULE_LEDGER,
    spatial_audit: Path = DEFAULT_SPATIAL_AUDIT,
    output_dir: Path | None = None,
) -> dict[str, Any]:
    pack = pack.resolve()
    module_ledger = module_ledger.resolve()
    spatial_audit = spatial_audit.resolve()
    output_dir = (output_dir or pack).resolve()

    contexts = read_tsv(pack / "contexts.tsv")
    observations = read_tsv(pack / "observations.tsv")
    spatial_rows = read_tsv(spatial_audit)
    module_rows = read_tsv(module_ledger)
    context_by_id = {row["context_id"]: row for row in contexts}
    context_index = index_pack_rows(observations, ("source_locator", "source_record_key"))
    spatial_index = index_pack_rows(spatial_rows, ("source_locator", "source_record_key"))

    output_rows: list[dict[str, Any]] = []
    counts_by: dict[str, Counter[str]] = {
        "module": Counter(),
        "source_context_class": Counter(),
        "paper_status": Counter(),
        "observation_status": Counter(),
        "evidence_layer": Counter(),
        "context_pack_match_status": Counter(),
        "spatial_audit_match_status": Counter(),
        "source_context_basis_field": Counter(),
    }
    eligible_rows = 0
    skipped_no_context = 0

    for module_row in module_rows:
        classification, basis, terms, eligibility = context_class(module_row)
        if eligibility == "not_eligible":
            skipped_no_context += 1
            continue
        eligible_rows += 1
        identifiers = source_identifiers(module_row.get("canonical_paper_key", ""), module_row.get("source_locator", ""))
        matched_context = [row for identifier in identifiers for row in context_index.get(identifier, [])]
        matched_spatial = [row for identifier in identifiers for row in spatial_index.get(identifier, [])]
        matched_context = list({row["observation_id"]: row for row in matched_context}.values())
        matched_spatial = list({row["observation_id"]: row for row in matched_spatial}.values())
        context_match = "matched_exact_source_identifier" if matched_context else "no_exact_source_identifier_match"
        spatial_match = "matched_exact_source_identifier" if matched_spatial else "no_exact_source_identifier_match"
        row = {
            "module": module_row.get("module", ""),
            "extraction_id": module_row.get("extraction_id", ""),
            "b_edge_id": module_row.get("b_edge_id", ""),
            "b_evidence_id": module_row.get("b_evidence_id", ""),
            "module_dependency_group": module_row.get("b_evidence_id", "") or module_row.get("extraction_id", ""),
            "canonical_paper_key": module_row.get("canonical_paper_key", ""),
            "module_source_locator": module_row.get("source_locator", ""),
            "paper_status": module_row.get("paper_status", ""),
            "observation_status": module_row.get("observation_status", ""),
            "evidence_layer": module_row.get("evidence_layer", ""),
            "confidence": module_row.get("confidence", ""),
            **{field: module_row.get(field, "") for field in SCI_CONTEXT_FIELDS},
            "source_context_class": classification,
            "source_context_basis_fields": ";".join(basis),
            "source_context_terms": ";".join(terms),
            "source_identifier_keys": ";".join(sorted(identifiers)),
            "context_pack_match_status": context_match,
            "matched_context_observation_ids": ";".join(unique_values(matched_context, "observation_id")),
            "matched_context_ids": ";".join(unique_values(matched_context, "context_id")),
            "matched_context_source_artifact_paths": ";".join(unique_values(matched_context, "source_artifact_path")),
            "matched_context_source_artifact_sha256": ";".join(unique_values(matched_context, "source_artifact_sha256")),
            "spatial_audit_match_status": spatial_match,
            "matched_spatial_observation_ids": ";".join(unique_values(matched_spatial, "observation_id")),
            "matched_spatial_primary_classes": ";".join(unique_values(matched_spatial, "primary_spatial_class")),
            "matched_spatial_source_artifact_paths": ";".join(unique_values(matched_spatial, "source_artifact_path")),
            "matched_spatial_source_artifact_sha256": ";".join(unique_values(matched_spatial, "source_artifact_sha256")),
            "promotion_state": "audit_only_not_promoted",
            "audit_note": (
                "Source-derived module context retained for reconciliation; b_evidence_id is the dependency group. "
                "No context-pack observation, proximity relation, graph edge, or numeric weight was created."
            ),
        }
        output_rows.append(row)
        counts_by["module"][row["module"] or "unknown"] += 1
        counts_by["source_context_class"][classification] += 1
        counts_by["paper_status"][row["paper_status"] or "unknown"] += 1
        counts_by["observation_status"][row["observation_status"] or "unknown"] += 1
        counts_by["evidence_layer"][row["evidence_layer"] or "unknown"] += 1
        counts_by["context_pack_match_status"][context_match] += 1
        counts_by["spatial_audit_match_status"][spatial_match] += 1
        counts_by["source_context_basis_field"].update(basis)

    output_rows.sort(key=lambda row: (row["module"], row["b_evidence_id"], row["extraction_id"]))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_tsv = output_dir / "sci_module_spatial_reconciliation.tsv"
    output_json = output_dir / "sci_module_spatial_reconciliation.json"
    write_tsv(output_tsv, output_rows)

    input_paths = [
        module_ledger,
        pack / "contexts.tsv",
        pack / "observations.tsv",
        spatial_audit,
    ]
    input_artifacts = [
        {
            "path": str(path.relative_to(ROOT)),
            "sha256": sha256(path),
            "size_bytes": path.stat().st_size,
            "rows": len(read_tsv(path)),
        }
        for path in input_paths
    ]
    summary = {
        "audit_version": "sci_module_spatial_reconciliation_v1",
        "scope": "Canonical Module 20B-24B phase-2 extraction rows with explicit source-derived spinal-cord or SCI context; no evidence import was performed.",
        "input_artifacts": input_artifacts,
        "module_ledger_rows_scanned": len(module_rows),
        "module_rows_without_explicit_context_skipped": skipped_no_context,
        "candidate_counts": {
            "module_rows_with_explicit_context": eligible_rows,
            "source_resolved_context_rows": sum(1 for row in output_rows if row["source_context_class"] in {"explicit_sci_injury_context", "explicit_spinal_cord_context"}),
            "review_required_exclusion_rows": sum(1 for row in output_rows if row["source_context_class"] == "explicit_context_with_exclusion_language"),
            "unique_module_evidence_groups": len({row["module_dependency_group"] for row in output_rows}),
            "unique_source_identifier_keys": len({key for row in output_rows for key in row["source_identifier_keys"].split(";") if key}),
        },
        "counts_by": {key: dict(sorted(counter.items())) for key, counter in sorted(counts_by.items())},
        "reconciliation_counts": {
            "candidate_rows_matching_existing_context_pack_observations": sum(1 for row in output_rows if row["context_pack_match_status"] == "matched_exact_source_identifier"),
            "candidate_rows_matching_existing_spatial_audit_rows": sum(1 for row in output_rows if row["spatial_audit_match_status"] == "matched_exact_source_identifier"),
            "candidate_rows_module_only": sum(1 for row in output_rows if row["context_pack_match_status"] == "no_exact_source_identifier_match"),
        },
        "interpretation": {
            "source_matching": "Only exact PMID, PMCID, or DOI intersections were used; text similarity and inferred study identity were not used.",
            "dependency_policy": "Multiple extraction rows sharing b_evidence_id remain grouped and must not be double-counted as independent experiments.",
            "spatial_policy": "A module record is not treated as proximity evidence unless its source-derived fields explicitly report localization, cell assignment, co-localization, or a spatial-transcriptomic context.",
            "promotion_policy": "This audit does not modify contexts.tsv, observations.tsv, mechanism_links.tsv, context_manifest.json, or the pinned mechanism graph.",
            "next_step": "Review module-only explicit SCI rows first; promote only source-resolved, non-duplicative observations after exact study/sample/timepoint reconciliation.",
        },
        "artifacts": {"tsv": output_tsv.name, "json": output_json.name},
    }
    output_json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pack", type=Path, default=DEFAULT_PACK)
    parser.add_argument("--module-ledger", type=Path, default=DEFAULT_MODULE_LEDGER)
    parser.add_argument("--spatial-audit", type=Path, default=DEFAULT_SPATIAL_AUDIT)
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()
    summary = build(args.pack, args.module_ledger, args.spatial_audit, args.output_dir)
    print(json.dumps({"candidate_counts": summary["candidate_counts"], "counts_by": summary["counts_by"], "reconciliation_counts": summary["reconciliation_counts"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
