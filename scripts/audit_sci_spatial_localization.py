#!/usr/bin/env python3
"""Audit extractable spatial/localization information in the SCI context pack.

This is a read-only audit of existing observations. It classifies source
records into extractable information types without creating relation records,
image-derived measurements, graph edges, or proximity confidence.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACK = ROOT / "context_packs" / "spinal_cord_injury"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.build_sci_context_pack import nonempty_context, read_tsv

IF_IHC_ASSAY = re.compile(
    r"immunofluorescence|immunohistochemistry|immunocytochemistry|multilabel immunostain",
    re.IGNORECASE,
)
SPATIAL_TRANSCRIPTOMICS_ASSAY = re.compile(
    r"spatial transcript|visium|spatial gene expression|spatial sequencing",
    re.IGNORECASE,
)
SAME_CELL = re.compile(
    r"colocal|co-local|double[- ]positive|double[- ]immuno|co[- ]label|co-labeled|cell-marker",
    re.IGNORECASE,
)
CELL_ASSIGNMENT = re.compile(
    r"cell[- ]type|cell assignment|cell-associated|cell-specific|positive (?:cells?|neurons?|astrocytes?|microglia|macrophages?)|cell localization|cell identity|cell population",
    re.IGNORECASE,
)
SUBCELLULAR = re.compile(
    r"nuclear|nucleus|cytoplasm|cytoplasmic|membrane|lysosom|junctional|synaptic|perivascular",
    re.IGNORECASE,
)
REGIONAL = re.compile(
    r"lesion|epicenter|perilesional|perilesion|lesion[- ]border|rostral|caudal|gray matter|white matter|dorsal|ventral|central|margin|region|lamina|spinal cord layer|injury site",
    re.IGNORECASE,
)
STRUCTURAL = re.compile(
    r"density|area|fiber|puncta|gap|vessel|microvessel|coverage|immunoreactive density|optical density|integrated density|cells/mm|per mm",
    re.IGNORECASE,
)

OUTPUT_FIELDS = [
    "observation_id",
    "context_id",
    "study_id",
    "modality",
    "assay",
    "primary_spatial_class",
    "secondary_spatial_classes",
    "extractable_information",
    "relation_directness",
    "promotion_state",
    "measured_entity_name",
    "measurement_kind",
    "value_numeric",
    "value_text",
    "value_kind",
    "unit",
    "comparator",
    "cell_type",
    "sample_id",
    "species",
    "injury_model",
    "injury_level",
    "timepoint_value",
    "timepoint_unit",
    "tissue",
    "injury_distance",
    "injury_distance_unit",
    "sample_scope",
    "dependency_group",
    "observation_status",
    "evidence_role",
    "link_status",
    "source_record_key",
    "source_artifact_path",
    "source_artifact_sha256",
    "source_locator",
    "provenance_note",
    "audit_note",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_tsv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def combined_text(row: dict[str, str]) -> str:
    return " ".join(
        row.get(field, "")
        for field in (
            "assay", "measurement_kind", "measured_entity_name", "value_text",
            "cell_type", "provenance_note", "source_locator",
        )
    )


def assay_family(row: dict[str, str]) -> str | None:
    assay = row.get("assay", "")
    if IF_IHC_ASSAY.search(assay):
        return "if_ihc"
    if row.get("modality") == "transcriptomics" and SPATIAL_TRANSCRIPTOMICS_ASSAY.search(combined_text(row)):
        return "spatial_transcriptomics"
    return None


def link_status(link: dict[str, str] | None) -> str:
    if not link:
        return "unlinked"
    release_status = link.get("release_status", "").strip()
    if release_status == "included":
        return "linked_included"
    if release_status == "staging":
        return "linked_staging_unresolved"
    return f"linked_{release_status or 'unknown'}"


def classify(row: dict[str, str]) -> tuple[str, list[str], str, str]:
    text = combined_text(row)
    flags: list[str] = []
    if SAME_CELL.search(text):
        flags.append("same_cell_colocalization")
    if CELL_ASSIGNMENT.search(text):
        flags.append("cell_type_assignment")
    if SUBCELLULAR.search(text):
        flags.append("subcellular_localization")
    if REGIONAL.search(text) or nonempty_context(row.get("tissue")):
        flags.append("regional_localization")
    if STRUCTURAL.search(text):
        flags.append("structural_density_or_area")

    family = assay_family(row)
    if family == "spatial_transcriptomics":
        return (
            "spatial_transcriptomic_dataset_context",
            sorted(set(flags)),
            "dataset_context_only_pending_coordinate_validation",
            "Source record identifies an SCI-related spatial-transcriptomic dataset; no spot-level relation is imported here.",
        )
    if not flags:
        return (
            "ordinary_protein_observation",
            [],
            "retain_as_protein_observation",
            "IF/IHC assay is present but no explicit localization, cell-assignment, structural, or co-localization claim was detected.",
        )
    primary = flags[0]
    if primary == "same_cell_colocalization":
        directness = "source_reported_same_cell_or_double_label"
        decision = "candidate_for_relation_curation"
    elif primary == "cell_type_assignment":
        directness = "source_reported_cell_or_population_assignment"
        decision = "candidate_for_spatial_context_curation"
    else:
        directness = "source_reported_localization_or_structure"
        decision = "candidate_for_spatial_context_curation"
    return primary, sorted(set(flags[1:])), decision, directness


def build(pack: Path = DEFAULT_PACK, output_dir: Path | None = None) -> dict[str, Any]:
    pack = pack.resolve()
    output_dir = (output_dir or pack).resolve()
    contexts_path = pack / "contexts.tsv"
    observations_path = pack / "observations.tsv"
    links_path = pack / "mechanism_links.tsv"
    contexts = {row["context_id"]: row for row in read_tsv(contexts_path)}
    observations = read_tsv(observations_path)
    links = {row["observation_id"]: row for row in read_tsv(links_path)}

    rows: list[dict[str, Any]] = []
    class_counts: Counter[str] = Counter()
    secondary_class_counts: Counter[str] = Counter()
    assay_counts: Counter[str] = Counter()
    modality_counts: Counter[str] = Counter()
    value_state_counts: Counter[str] = Counter()
    counts_by: dict[str, Counter[str]] = {
        "study": Counter(),
        "injury_model": Counter(),
        "timepoint": Counter(),
        "perturbation": Counter(),
        "observation_status": Counter(),
        "evidence_role": Counter(),
        "link_status": Counter(),
        "unresolved_mapping_reason": Counter(),
    }

    for observation in observations:
        family = assay_family(observation)
        if family is None:
            continue
        context = contexts.get(observation["context_id"], {})
        primary, secondary, decision, directness_or_note = classify(observation)
        link = links.get(observation["observation_id"], {})
        row_link_status = link_status(link or None)
        if nonempty_context(observation.get("value_numeric")):
            value_state = "numeric_value_present"
        elif observation.get("value_text") and observation.get("value_kind") not in {"unreported", "unknown"}:
            value_state = "qualitative_or_reported_text_present"
        else:
            value_state = "not_measured_or_not_reported"
        timepoint = " ".join(
            value for value in (observation.get("timepoint_value", ""), observation.get("timepoint_unit", ""))
            if value
        ).strip() or "unknown"
        row = {
            "observation_id": observation["observation_id"],
            "context_id": observation["context_id"],
            "study_id": context.get("study_id", "") or "unknown",
            "modality": observation.get("modality", ""),
            "assay": observation.get("assay", ""),
            "primary_spatial_class": primary,
            "secondary_spatial_classes": ";".join(secondary),
            "extractable_information": (
                "source-reported same-cell/co-localization candidate" if primary == "same_cell_colocalization"
                else "source-reported cell, region, or structural localization candidate" if primary != "spatial_transcriptomic_dataset_context"
                else "SCI-related spatial-transcriptomic dataset context; coordinate-level extraction not yet performed"
            ),
            "relation_directness": directness_or_note if primary != "spatial_transcriptomic_dataset_context" else "dataset_context_only",
            "promotion_state": "audit_only_not_promoted",
            "measured_entity_name": observation.get("measured_entity_name", ""),
            "measurement_kind": observation.get("measurement_kind", ""),
            "value_numeric": observation.get("value_numeric", ""),
            "value_text": observation.get("value_text", ""),
            "value_kind": observation.get("value_kind", ""),
            "unit": observation.get("unit", ""),
            "comparator": observation.get("comparator", ""),
            "cell_type": observation.get("cell_type", "") or context.get("cell_type", ""),
            "sample_id": observation.get("sample_id", "") or context.get("sample_id", ""),
            "species": context.get("species", ""),
            "injury_model": context.get("injury_model", ""),
            "injury_level": context.get("injury_level", ""),
            "timepoint_value": observation.get("timepoint_value", "") or context.get("timepoint_value", ""),
            "timepoint_unit": observation.get("timepoint_unit", "") or context.get("timepoint_unit", ""),
            "tissue": context.get("tissue", ""),
            "injury_distance": context.get("injury_distance", ""),
            "injury_distance_unit": context.get("injury_distance_unit", ""),
            "sample_scope": context.get("sample_scope", ""),
            "dependency_group": observation.get("dependency_group", ""),
            "observation_status": observation.get("observation_status", ""),
            "evidence_role": observation.get("evidence_role", ""),
            "link_status": row_link_status,
            "source_record_key": observation.get("source_record_key", ""),
            "source_artifact_path": observation.get("source_artifact_path", ""),
            "source_artifact_sha256": observation.get("source_artifact_sha256", ""),
            "source_locator": observation.get("source_locator", ""),
            "provenance_note": observation.get("provenance_note", ""),
            "audit_note": directness_or_note if primary != "spatial_transcriptomic_dataset_context" else "No spot, coordinate, or neighborhood metric was imported.",
        }
        rows.append(row)
        class_counts[primary] += 1
        secondary_class_counts.update(secondary)
        assay_counts[observation.get("assay", "") or "unknown"] += 1
        modality_counts[observation.get("modality", "") or "unknown"] += 1
        value_state_counts[value_state] += 1
        counts_by["study"][row["study_id"]] += 1
        counts_by["injury_model"][context.get("injury_model", "") or "unknown"] += 1
        counts_by["timepoint"][timepoint] += 1
        counts_by["perturbation"][observation.get("perturbation", "") or context.get("perturbation", "") or "unknown"] += 1
        counts_by["observation_status"][row["observation_status"] or "unknown"] += 1
        counts_by["evidence_role"][row["evidence_role"] or "unknown"] += 1
        counts_by["link_status"][row_link_status] += 1
        if row_link_status == "linked_staging_unresolved":
            counts_by["unresolved_mapping_reason"][link.get("notes", "") or "unknown"] += 1

    rows.sort(key=lambda row: row["observation_id"])
    output_dir.mkdir(parents=True, exist_ok=True)
    output_tsv = output_dir / "spatial_localization_audit.tsv"
    output_json = output_dir / "spatial_localization_audit.json"
    write_tsv(output_tsv, rows)

    input_paths = [contexts_path, observations_path, links_path]
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
        "audit_version": "sci_spatial_localization_audit_v1",
        "scope": "Existing SCI context-pack observations only; no image or spot re-analysis was performed.",
        "input_artifacts": input_artifacts,
        "candidate_counts": {
            "if_ihc_or_immunostain_observations": sum(1 for row in rows if row["primary_spatial_class"] != "spatial_transcriptomic_dataset_context"),
            "spatial_transcriptomic_dataset_contexts": sum(1 for row in rows if row["primary_spatial_class"] == "spatial_transcriptomic_dataset_context"),
            "all_candidates": len(rows),
        },
        "class_counts": dict(sorted(class_counts.items())),
        "secondary_class_counts": dict(sorted(secondary_class_counts.items())),
        "assay_counts": dict(sorted(assay_counts.items())),
        "modality_counts": dict(sorted(modality_counts.items())),
        "value_state_counts": dict(sorted(value_state_counts.items())),
        "counts_by": {key: dict(sorted(value.items())) for key, value in sorted(counts_by.items())},
        "interpretation": {
            "highest_value_initial_layer": "source-reported IF/IHC same-cell co-localization and cell-type assignment",
            "spatial_transcriptomics_status": "Current SCI records are dataset-context annotations; spot-level or coordinate-level proximity remains unimported.",
            "image_reanalysis_status": "No raw-image segmentation, pixel colocalization, or distance calculation was performed.",
            "promotion_policy": "This audit does not create relation observations, graph edges, route confidence, or numeric modality weights.",
            "next_step": "Review same_cell_colocalization candidates first, then separate cell assignment, regional localization, and structural-density records before any relation-table promotion.",
        },
        "artifacts": {
            "tsv": output_tsv.name,
            "json": output_json.name,
        },
    }
    output_json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pack", type=Path, default=DEFAULT_PACK)
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()
    summary = build(args.pack, args.output_dir)
    print(json.dumps({
        "candidate_counts": summary["candidate_counts"],
        "class_counts": summary["class_counts"],
        "value_state_counts": summary["value_state_counts"],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
