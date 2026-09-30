#!/usr/bin/env python3
"""Audit whether a separate SCI perturbation-evidence layer is useful.

This script reads the existing SCI context pack and writes an audit-only view.
It does not add observations, alter mechanism links, or infer causal effects.
The perturbation classes are heuristic labels used to expose curation gaps;
the exact source text, identifiers, artifact paths, checksums, and locators
remain in the output for review.
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

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.build_sci_context_pack import nonempty_context, read_tsv

PERTURBATION_FIELDS = (
    "perturbation",
    "treatment",
    "study_perturbation_status",
)
MATCH_FIELDS = (
    "species",
    "injury_model",
    "injury_level",
    "timepoint_value",
    "timepoint_unit",
    "tissue",
)

_INTERVENTION_PATTERNS = (
    ("genetic_or_cellular_perturbation", r"\b(knockout|knock-out|knockdown|knock-down|deletion|depleted|depletion|ablation|silenc|conditional knockout|transgenic|cre|flox|loxp|fl/fl)\b"),
    ("expression_or_vector_perturbation", r"\b(overexpression|over-expression|overexpressed|aav[- ]|shrna|sirna|lentiviral|adoptive transfer|transplantation)\b"),
    ("drug_or_antibody_intervention", r"\b(inhibitor|inhibition|antagonist|blockade|blocking|neutraliz|anti-[a-z0-9]|antibody treatment|drug treatment|diet)\b"),
    ("protein_or_ligand_treatment", r"\b(recombinant|infusion|treated with|treatment|therapy|rescue|agonist|administration|perturbation|manipulation|exposure)\b"),
    ("physical_or_behavioral_intervention", r"\b(photobiomodulation|electroacupuncture|exercise|rehabilitation|stimulation|conditioning)\b"),
    ("added_agent", r"(?:^|\s)\+[a-z0-9][a-z0-9-]*\b"),
)
_DESIGN_PATTERNS = (
    ("arm_comparison", r"\bversus\b|\bvs\.?\b|\bcomparison\b|\bcompared\b|\barms?\b"),
    ("genotype_or_line_comparison", r"\b(wild[- ]type|\bwt\b|mutant|knockout|knock-out|transgenic)\b"),
    ("control_or_reference_comparison", r"\b(sham|naive|uninjured|intact|vehicle|saline|control|contralateral|normal)\b"),
    ("injury_severity_comparison", r"\b(mild|moderate|severe)\b.*\b(sci|injur)|\binjury severity\b"),
)
_STATUS_PATTERNS = (
    ("injury_status", r"\b(sci|injured|injury|hemisection|contusion|transection|crush)\b"),
    ("observational_design", r"\b(observational|time course|temporal|untreated|no therapeutic|no molecular|none|series)\b"),
)
_NON_PERTURBATION_CONTEXT = re.compile(
    r"\b(perilesional|lesion[- ]?centered|spinal cord tissue|spinal-cord tissue|homogenate|white matter|microvessels?|astrocytes?|endothelial cells?|lumbar|sacral|vascular penumbra)\b",
    re.IGNORECASE,
)
_NEGATIVE_INTERVENTION = re.compile(
    r"\b(no (?:therapeutic|molecular|experimental|specific) (?:perturbation|treatment|intervention)|untreated|without treatment|no treatment)\b",
    re.IGNORECASE,
)

AUDIT_FIELDS = [
    "context_id",
    "study_id",
    "source_record_keys",
    "observation_ids",
    "modality",
    "assay",
    "dependency_group_count",
    "observation_count",
    "audit_classification",
    "classification_signals",
    "classification_basis",
    "perturbation_source_text",
    "treatment_source_text",
    "experimental_condition_source_text",
    "study_perturbation_status_source_text",
    "observation_perturbation_source_text",
    "species",
    "injury_model",
    "injury_level",
    "injury_severity",
    "timepoint_values",
    "tissue",
    "cell_type",
    "sample_scope",
    "match_fields_present",
    "match_fields_missing",
    "source_artifact_paths",
    "source_artifact_sha256s",
    "source_locators",
    "evidence_roles",
    "observation_statuses",
    "link_statuses",
    "audit_decision",
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
        writer = csv.DictWriter(handle, fieldnames=AUDIT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: "" if row.get(field) is None else row.get(field, "") for field in AUDIT_FIELDS})


def unique_values(rows: list[dict[str, str]], field: str) -> list[str]:
    return sorted({str(row.get(field, "")).strip() for row in rows if nonempty_context(row.get(field))})


def joined(values: list[str]) -> str:
    return "; ".join(values)


def classify(values: list[str]) -> dict[str, str]:
    """Return an audit-only class; no field is written back as evidence."""

    source = " | ".join(value.strip() for value in values if nonempty_context(value))
    if not source:
        return {
            "classification": "no_explicit_context",
            "signals": "",
            "basis": "No non-empty perturbation/design field was present.",
        }

    lowered = source.lower()
    signals: list[str] = []
    intervention_hits: list[str] = []
    for label, pattern in _INTERVENTION_PATTERNS:
        if re.search(pattern, lowered, flags=re.IGNORECASE):
            # A negated treatment statement is not counted as an intervention
            # unless another independent intervention signal is present.
            if label == "protein_or_ligand_treatment" and _NEGATIVE_INTERVENTION.search(lowered):
                continue
            intervention_hits.append(label)
            signals.append(label)

    design_hits: list[str] = []
    for label, pattern in _DESIGN_PATTERNS:
        if re.search(pattern, lowered, flags=re.IGNORECASE):
            design_hits.append(label)
            signals.append(label)

    status_hits: list[str] = []
    for label, pattern in _STATUS_PATTERNS:
        if re.search(pattern, lowered, flags=re.IGNORECASE):
            status_hits.append(label)
            signals.append(label)

    if intervention_hits and design_hits:
        classification = "explicit_intervention_with_comparator_design"
    elif intervention_hits:
        classification = "explicit_intervention"
    elif design_hits:
        classification = "comparator_or_injury_design"
    elif status_hits:
        classification = "injury_status_or_observational"
    elif _NON_PERTURBATION_CONTEXT.search(lowered):
        classification = "non_perturbation_context_text"
    elif lowered.strip() in {"none", "unknown", "not_reported", "observational"}:
        classification = "no_explicit_intervention"
    else:
        classification = "unclear_free_text"

    return {
        "classification": classification,
        "signals": ";".join(sorted(set(signals))),
        "basis": "Heuristic term matching over exact source-field text; review source locators before any curation use.",
    }


def link_status(link: dict[str, str] | None) -> str:
    if not link:
        return "unlinked"
    release_status = link.get("release_status", "").strip()
    if release_status == "included":
        return "linked_included"
    if release_status == "staging":
        return "linked_staging_unresolved"
    return f"linked_{release_status or 'unknown'}"


def build(pack: Path, output_dir: Path | None = None) -> dict[str, Any]:
    pack = pack.resolve()
    output_dir = output_dir or pack
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    contexts = [row for row in read_tsv(pack / "contexts.tsv") if row.get("context_kind") != "ontology_scope"]
    observations = read_tsv(pack / "observations.tsv")
    links = {row["observation_id"]: row for row in read_tsv(pack / "mechanism_links.tsv")}
    observations_by_context: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in observations:
        observations_by_context[row["context_id"]].append(row)

    context_rows: list[dict[str, Any]] = []
    context_classes: Counter[str] = Counter()
    observation_classes: Counter[str] = Counter()
    modality_by_class: dict[str, Counter[str]] = defaultdict(Counter)
    counts_by: dict[str, Counter[str]] = {
        "modality": Counter(),
        "study": Counter(),
        "injury_model": Counter(),
        "timepoint": Counter(),
        "observation_status": Counter(),
        "evidence_role": Counter(),
        "link_status": Counter(),
        "unresolved_mapping_reason": Counter(),
    }

    for context in sorted(contexts, key=lambda row: row["context_id"]):
        context_id = context["context_id"]
        context_observations = observations_by_context.get(context_id, [])
        source_values = [context.get(field, "") for field in PERTURBATION_FIELDS]
        classification = classify(source_values)
        context_classes[classification["classification"]] += 1

        for observation in context_observations:
            observation_class = classify([observation.get("perturbation", "")])
            observation_classes[observation_class["classification"]] += 1
            modality = observation.get("modality", "") or "unknown"
            modality_by_class[classification["classification"]][modality] += 1
            counts_by["modality"][modality] += 1
            counts_by["study"][context.get("study_id", "") or "unknown"] += 1
            timepoint = " ".join(value for value in (observation.get("timepoint_value", ""), observation.get("timepoint_unit", "")) if value).strip() or "unknown"
            counts_by["timepoint"][timepoint] += 1
            counts_by["observation_status"][observation.get("observation_status", "") or "unknown"] += 1
            counts_by["evidence_role"][observation.get("evidence_role", "") or "unknown"] += 1
            status = link_status(links.get(observation["observation_id"]))
            counts_by["link_status"][status] += 1
            link = links.get(observation["observation_id"])
            if status == "linked_staging_unresolved":
                counts_by["unresolved_mapping_reason"][link.get("notes", "") if link else ""] += 1

        injury_model = context.get("injury_model", "") or "unknown"
        counts_by["injury_model"][injury_model] += len(context_observations)

        match_present = [field for field in MATCH_FIELDS if nonempty_context(context.get(field))]
        match_missing = [field for field in MATCH_FIELDS if field not in match_present]
        source_record_keys = unique_values(context_observations, "source_record_key")
        observation_ids = unique_values(context_observations, "observation_id")
        artifact_paths = unique_values(context_observations, "source_artifact_path")
        artifact_hashes = unique_values(context_observations, "source_artifact_sha256")
        locators = unique_values(context_observations, "source_locator")
        link_statuses = sorted({link_status(links.get(row["observation_id"])) for row in context_observations})
        context_rows.append({
            "context_id": context_id,
            "study_id": context.get("study_id", ""),
            "source_record_keys": joined(source_record_keys),
            "observation_ids": joined(observation_ids),
            "modality": joined(unique_values(context_observations, "modality")),
            "assay": joined(unique_values(context_observations, "assay")),
            "dependency_group_count": len({row["dependency_group"] for row in context_observations if row.get("dependency_group")}),
            "observation_count": len(context_observations),
            "audit_classification": classification["classification"],
            "classification_signals": classification["signals"],
            "classification_basis": classification["basis"],
            "perturbation_source_text": context.get("perturbation", ""),
            "treatment_source_text": context.get("treatment", ""),
            "experimental_condition_source_text": context.get("experimental_condition", ""),
            "study_perturbation_status_source_text": context.get("study_perturbation_status", ""),
            "observation_perturbation_source_text": joined(unique_values(context_observations, "perturbation")),
            "species": context.get("species", ""),
            "injury_model": context.get("injury_model", ""),
            "injury_level": context.get("injury_level", ""),
            "injury_severity": context.get("injury_severity", ""),
            "timepoint_values": joined(unique_values(context_observations, "timepoint_value")),
            "tissue": context.get("tissue", ""),
            "cell_type": context.get("cell_type", ""),
            "sample_scope": context.get("sample_scope", ""),
            "match_fields_present": ";".join(match_present),
            "match_fields_missing": ";".join(match_missing),
            "source_artifact_paths": joined(artifact_paths),
            "source_artifact_sha256s": joined(artifact_hashes),
            "source_locators": joined(locators),
            "evidence_roles": joined(unique_values(context_observations, "evidence_role")),
            "observation_statuses": joined(unique_values(context_observations, "observation_status")),
            "link_statuses": ";".join(link_statuses),
            "audit_decision": "retain_existing_evidence_only",
            "audit_note": "Perturbation fields are already present; this row is not a perturbation-response observation and does not promote causality.",
        })

    for counter in counts_by.values():
        # Empty study/model values are made explicit as unknown in the report,
        # while the TSV preserves the exact empty source fields.
        if "" in counter:
            counter["unknown"] += counter.pop("")

    input_paths = [pack / "contexts.tsv", pack / "observations.tsv", pack / "mechanism_links.tsv"]
    input_artifacts = []
    for path in input_paths:
        input_artifacts.append({
            "path": str(path.relative_to(ROOT)),
            "sha256": sha256(path),
            "size_bytes": path.stat().st_size,
            "rows": len(read_tsv(path)),
        })

    intervention_classes = {
        "explicit_intervention",
        "explicit_intervention_with_comparator_design",
    }
    intervention_rows = [row for row in context_rows if row["audit_classification"] in intervention_classes]
    intervention_missing_fields = Counter(
        field
        for row in intervention_rows
        for field in row["match_fields_missing"].split(";")
        if field
    )

    output_tsv = output_dir / "perturbation_design_audit.tsv"
    output_json = output_dir / "perturbation_design_audit.json"
    write_tsv(output_tsv, context_rows)

    summary = {
        "audit_version": "sci_perturbation_design_audit_v1",
        "scope": "Existing SCI context-pack metadata only; no new evidence was imported.",
        "input_artifacts": input_artifacts,
        "pack_counts": {
            "evidence_context_profiles": len(contexts),
            "observations": len(observations),
            "mechanism_links": len(links),
            "contexts_with_perturbation_or_design_text": sum(value for key, value in context_classes.items() if key != "no_explicit_context"),
            "observations_with_perturbation_text": sum(1 for row in observations if nonempty_context(row.get("perturbation"))),
        },
        "classification_counts": {
            "contexts": dict(sorted(context_classes.items())),
            "observations": dict(sorted(observation_classes.items())),
        },
        "modality_by_context_classification": {
            key: dict(sorted(value.items())) for key, value in sorted(modality_by_class.items())
        },
        "counts_by": {key: dict(sorted(value.items())) for key, value in sorted(counts_by.items())},
        "context_match_field_coverage": {
            field: sum(1 for row in context_rows if field in row["match_fields_present"].split(";"))
            for field in MATCH_FIELDS
        },
        "intervention_context_fit": {
            "intervention_or_intervention_with_comparator_contexts": len(intervention_rows),
            "with_all_match_fields": sum(not row["match_fields_missing"] for row in intervention_rows),
            "with_missing_match_fields": sum(bool(row["match_fields_missing"]) for row in intervention_rows),
            "missing_match_fields": dict(sorted(intervention_missing_fields.items())),
            "modality": dict(sorted(Counter(
                modality
                for row in intervention_rows
                for modality in row["modality"].split("; ")
                if modality
            ).items())),
        },
        "interpretation": {
            "is_a_separate_perturbation_response_layer_needed_now": False,
            "is_normalized_perturbation_design_audit_useful": True,
            "reason": "The pack already preserves intervention and comparator metadata, but the fields mix treatment, genotype, injury status, and control design. A normalized audit is useful for condition matching; variable perturbation responses should not be generalized into mechanism support without exact study and timepoint matching.",
            "next_action": "Keep existing evidence rows unchanged. If later adding perturbation evidence, curate only source-resolved intervention/comparator observations with exact injury model, timepoint, tissue, and dependency-group provenance.",
            "heuristic_warning": "Audit classifications are not source facts, confidence scores, causal labels, graph edges, or numeric modality weights.",
        },
        "artifacts": {
            "tsv": output_tsv.name,
            "json": output_json.name,
        },
        "policy": "This audit is separate from the evidence tables and mechanism release; it does not promote observations or assign route confidence.",
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
        "evidence_context_profiles": summary["pack_counts"]["evidence_context_profiles"],
        "observations": summary["pack_counts"]["observations"],
        "context_classification_counts": summary["classification_counts"]["contexts"],
        "observation_classification_counts": summary["classification_counts"]["observations"],
        "separate_layer_needed_now": summary["interpretation"]["is_a_separate_perturbation_response_layer_needed_now"],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
