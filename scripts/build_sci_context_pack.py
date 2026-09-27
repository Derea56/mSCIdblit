#!/usr/bin/env python3
"""Build the populated spinal-cord-injury context evidence overlay.

The builder reads the current mSCS protein-state support view, curated mSCS
epigenetic SQLite store, mSCS spatial-transcriptomic catalog, and two explicit
SCI qRT-PCR records from the pinned mechanism-release evidence table. It writes
only the file-based context pack; it does not modify mSCS or the neutral Module
20B-24B mechanism bundle.

Observations retain source observation identifiers, source artifact hashes,
study/sample context, and dependency groups.  Exact mechanism-node matches
are included as observation links.  Rows without an exact mapping receive a
staging link to the stable module boundary ``21B`` with an explicit unresolved
reason; that link is not a graph edge and does not promote a route.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MSCS_ROOT = ROOT.parent / "mSCS"
DEFAULT_PACK = ROOT / "context_packs" / "spinal_cord_injury"
DEFAULT_BUNDLE = ROOT / "data" / "processed" / "mechanism_graph_module20_24_v2026_09_25_literature_expansion627"
RELEASE_ID = "module20_24_mechanism_graph:2026-09-25-literature-expansion-627"
RELEASE_TAG = "mSCIdblit-v1.9.386"
CONTEXT_PACK_VERSION = "0.5.27"
DEFAULT_CURATION_OVERRIDES = DEFAULT_PACK / "protein_context_curation_overrides.tsv"

SCI_SPATIAL_TRANSCRIPTOMIC_DATASETS = {
    "MSCIDATA000008",  # GSE195783: explicit T10 hemisection SCI time course
    "MSCIDATA000011",  # GSE234774: explicit spinal-cord-injury atlas
    "MSCIDATA000016",  # GSE268779: explicit injury-site spatial atlas
    "MSCIDATA000019",  # GSE305911 mouse SCI organoid-transplant tissue
    "MSCIDATA000027",  # GSE298545: explicit acute SCI dataset
    "MSCIDATA000029",  # GSE184369: paralysis/SCI EES rehabilitation dataset
    "MSCIDATA000038",  # GSE190910: explicit SCI/sham/solu-medrol sections
    "MSCIDATA000043",  # GSE256397: explicit mouse SCI time/space atlas
    "MSCIDATA000199",  # GSE312910: lesion-remote spinal-cord repair context
}
EXTERNAL_TRANSCRIPTOMIC_RECORDS = {
    "M21B-DOWNSTREAM-EVID:004631",
    "M21B-DOWNSTREAM-EVID:004632",
}

METABOLOMICS_TRANSCRIPTION_ARTIFACTS = {
    "FLOW_SCI_222__OBS222_6W_ATP_MS": "data/flow_protein/transcriptions/batch_2026-08-20_study222_atp_ms_not_reported.tsv",
    "FLOW_SCI_240__FLOW_SCI_240_OBS1": "data/flow_protein/transcriptions/batch_2026-08-21_study240_lipid_mediators.tsv",
    "FLOW_SCI_240__FLOW_SCI_240_OBS2": "data/flow_protein/transcriptions/batch_2026-08-21_study240_lipid_mediators.tsv",
    "FLOW_SCI_241__FLOW_SCI_241_OBS3": "data/flow_protein/transcriptions/batch_2026-08-20_direct_text_numeric_222_241_243_424.tsv",
    "FLOW_SCI_241__FLOW_SCI_241_OBS4": "data/flow_protein/transcriptions/batch_2026-08-20_direct_text_numeric_222_241_243_424.tsv",
}

CURATION_OVERRIDE_FIELDS = {
    "injury_model", "injury_level", "injury_severity", "sex",
    "perturbation_status", "condition", "sample_scope",
    "timepoint_value", "timepoint_unit", "sample_count",
}

CONTEXT_FIELDS = [
    "context_id", "context_name", "context_kind", "disease_context",
    "anatomical_context", "species", "injury_model", "injury_level",
    "injury_severity", "sex",
    "timepoint_value", "timepoint_unit", "perturbation", "treatment",
    "experimental_condition", "study_perturbation_status", "injury_distance",
    "injury_distance_unit", "sample_scope", "sample_count", "cell_type",
    "sample_id", "study_id", "tissue", "context_status",
    "provenance_note",
]
OBSERVATION_FIELDS = [
    "observation_id", "context_id", "source_system", "source_database",
    "source_record_type", "source_record_key", "source_version", "modality",
    "assay", "measurement_kind", "measured_entity_name", "measured_entity_type",
    "feature_id", "value_numeric", "value_text", "value_kind", "unit",
    "direction_vs_control", "comparator", "biological_replicates",
    "timepoint_value", "timepoint_unit", "perturbation", "cell_type",
    "sample_id", "observation_status", "evidence_role", "dependency_group",
    "source_artifact_path", "source_artifact_sha256", "source_locator",
    "provenance_note",
]
LINK_FIELDS = [
    "link_id", "observation_id", "mechanism_release_id", "mechanism_target_kind",
    "mechanism_target_key", "mechanism_route_id", "route_stage", "link_role",
    "context_match", "support_status", "release_status", "link_basis",
    "source_field_locator", "notes",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_curation_overrides(path: Path) -> dict[tuple[str, str], dict[str, str]]:
    rows = read_tsv(path)
    required = {
        "curation_id", "study_id", "timepoint_id", "source_locator", "source_url",
        "curation_note", "curation_status",
    } | CURATION_OVERRIDE_FIELDS
    if rows and not required.issubset(rows[0]):
        missing = sorted(required - set(rows[0]))
        raise ValueError(f"curation override file is missing fields: {', '.join(missing)}")
    overrides: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows:
        if row.get("curation_status") != "applied":
            continue
        key = (row.get("study_id", ""), row.get("timepoint_id", ""))
        if not key[0]:
            raise ValueError("curation override rows require study_id")
        if key in overrides:
            raise ValueError(f"duplicate applied curation override key: {key}")
        if not row.get("source_locator") or not row.get("source_url"):
            raise ValueError(f"curation override {row.get('curation_id')} lacks exact source provenance")
        overrides[key] = row
    return overrides


def apply_curation_override(row: dict[str, Any], overrides: dict[tuple[str, str], dict[str, str]]) -> dict[str, Any]:
    """Apply only explicitly curated study/timepoint fields and retain provenance."""
    merged = dict(row)
    study_id = str(row.get("study_id") or "")
    timepoint_id = str(row.get("timepoint_id") or "")
    override = overrides.get((study_id, timepoint_id)) or overrides.get((study_id, ""))
    if not override:
        return merged
    for field in CURATION_OVERRIDE_FIELDS:
        value = override.get(field, "")
        if value:
            if field == "perturbation_status":
                merged["perturbation_status"] = value
            elif field == "condition":
                merged["condition"] = value
            elif field == "timepoint_value":
                merged["post_injury_value"] = value
            else:
                merged[field] = value
    merged["_context_curation"] = {
        "curation_id": override["curation_id"],
        "source_locator": override["source_locator"],
        "source_url": override["source_url"],
        "curation_note": override["curation_note"],
    }
    return merged


def curation_provenance(row: dict[str, Any]) -> dict[str, Any] | None:
    value = row.get("_context_curation")
    return value if isinstance(value, dict) else None


def write_tsv(path: Path, fields: list[str], rows: Iterable[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: "" if row.get(field) is None else row.get(field, "") for field in fields})


def json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def normalized(value: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", "", (value or "").lower())


def number(value: Any) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def display_number(value: Any) -> str:
    parsed = number(value)
    if parsed is None:
        return ""
    return str(int(parsed)) if parsed.is_integer() else str(parsed)


def timepoint_number(value: Any) -> float | None:
    parsed = number(value)
    return None if parsed is None or parsed < 0 else parsed


def display_timepoint(value: Any) -> str:
    rendered = display_number(timepoint_number(value))
    if rendered:
        return rendered
    if value not in (None, ""):
        return str(value).strip()
    return ""


def timepoint_label(value: Any, unit: Any) -> str:
    rendered = display_timepoint(value)
    unit_text = str(unit or "").strip()
    if rendered:
        return f"{rendered} {unit_text}".strip()
    return f"unknown ({unit_text})" if unit_text else "unknown"


def nonempty_context(value: Any) -> bool:
    return value is not None and str(value).strip().lower() not in {"", "unknown", "not_reported"}


def valid_timepoint(value: Any) -> bool:
    parsed = timepoint_number(value)
    return parsed is not None


def protein_value(row: dict[str, Any]) -> float | None:
    return number(row.get("transcribed_value_numeric")) if row.get("transcribed_value_numeric") not in (None, "") else number(row.get("value"))


def protein_has_measurement(row: dict[str, Any]) -> bool:
    return (
        protein_value(row) is not None
        or nonempty_context(row.get("transcribed_value_text"))
        or row.get("direction_vs_control") not in (None, "", "unknown", "not_reported")
    )


def metabolomics_candidate_kind(row: dict[str, Any]) -> str:
    """Classify explicit metabolite-oriented records without broad text matching."""
    assay = (row.get("assay") or "").lower()
    form = (row.get("protein_form") or "").lower()
    measurement = (row.get("measurement_kind") or "").lower()
    entity = (row.get("protein") or "").lower()
    if "mature lipid mediator" in form and assay in {"elisa", "lc-ms/ms", "lc-ms", "mass_spectrometry"}:
        return "lipid_mediator_assay"
    if assay == "elisa" and "lipid-mediator" in measurement:
        return "lipid_mediator_assay"
    if any(token in assay for token in ("metabolomics", "lc-ms", "mass spectrometry", "mass_spectrometry")):
        if any(token in f"{form} {measurement}" for token in ("metabolite", "atp", "lipid mediator")):
            return "mass_spectrometry_metabolite"
    if entity == "anandamide" and "mature lipid mediator" in form:
        return "queued_lipid_mediator_assay"
    if "atp" in entity and any(token in f"{form} {measurement}" for token in ("atp", "metabolite")):
        return "non_metabolomics_metabolite_readout"
    return ""


def is_metabolomics_import_candidate(row: dict[str, Any]) -> bool:
    """Return true only for directly measured metabolite/lipid assays."""
    kind = metabolomics_candidate_kind(row)
    if kind not in {"lipid_mediator_assay", "mass_spectrometry_metabolite"}:
        return False
    if not nonempty_context(row.get("injury_model")):
        return False
    if row.get("extraction_status") not in {
        "figure_table_transcribed", "source_data_transcribed", "primary_source_checked_not_reported",
        "text_extracted",
    }:
        return False
    return row.get("transcription_status") not in {"ambiguous"}


def protein_form_requires_state_review(row: dict[str, Any]) -> bool:
    """Return true for explicitly phospho/active or mixed-state records.

    Do not use substring matching for ``active``: ``C-reactive`` is a normal
    protein name, not an active-form measurement.  Total-protein records that
    merely say that phosphorylation was not resolved remain eligible.
    """
    form = (row.get("protein_form") or "").lower()
    measurement = (row.get("measurement_kind") or "").lower()
    if "total and phospho" in measurement or "total and phospho" in form:
        return True
    # A total-protein assay may explicitly state that a phospho-form was not
    # resolved.  That is still a total-protein observation, not a phospho
    # observation (for example, total MLKL with phospho-MLKL unresolved).
    total_protein = form.startswith("total ")
    if re.search(r"\bphospho(?:[-\s]|$)", form):
        return not total_protein
    if re.search(r"\bphosphorylated\b", form):
        return not total_protein
    if re.search(r"\bphosphorylation[- ]state-specific\b", form):
        return True
    if re.search(r"\bactive(?:[\s\-/]|$)", form):
        return True
    return False


def is_protein_expression_candidate(row: dict[str, Any], selected_ids: set[str]) -> bool:
    if row["observation_id"] in selected_ids:
        return False
    if is_metabolomics_import_candidate(row):
        return False
    if not nonempty_context(row.get("injury_model")):
        return False
    if row.get("extraction_status") not in {"figure_table_transcribed", "source_data_transcribed"}:
        return False
    if "inferred" in (row.get("timepoint_id") or "").lower():
        return False
    if not protein_has_measurement(row):
        return False
    assay = (row.get("assay") or "").lower()
    form = (row.get("protein_form") or "").lower()
    measurement = (row.get("measurement_kind") or "").lower()
    if "ambiguous:" in assay or "reporter" in assay or "reporter" in form:
        return False
    if protein_form_requires_state_review(row):
        return False
    if any(token in assay for token in ("emsa", "enzyme activity", "lipid assay", "zymography")):
        return False
    if "association" in measurement or "complex" in measurement:
        return False
    return any(
        token in assay
        for token in (
            "immunofluorescence", "immunohistochemistry", "immunocytochemistry",
            "western", "elisa", "flow_cytometry", "multiplex", "electrochemiluminescence",
            "mass_spectrometry", "gel_electrophoresis",
            "intracellular_flow", "protein_array", "antibody array", "proteomics", "lc-ms",
        )
    )


def stable_id(prefix: str, *values: Any) -> str:
    raw = "|".join("" if value is None else str(value) for value in values)
    digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]
    return f"{prefix}:{digest}"


def source_locator(*parts: str | None) -> str:
    return ";".join(part for part in parts if part)


def load_nodes(bundle: Path) -> dict[str, list[dict[str, str]]]:
    index: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in read_tsv(bundle / "mechanism_nodes.tsv"):
        keys = {normalized(row.get("gene_symbol")), normalized(row.get("canonical_name"))}
        keys.update(normalized(item) for item in (row.get("label_variants") or "").split(";"))
        for key in {key for key in keys if key}:
            index[key].append(row)
    return index


def exact_node(node_index: dict[str, list[dict[str, str]]], gene_symbol: str | None, entity: str | None) -> tuple[dict[str, str] | None, str]:
    gene_reason = ""
    if gene_symbol:
        matches = node_index.get(normalized(gene_symbol), [])
        unique = {row["node_id"]: row for row in matches}
        canonical = [
            row for row in unique.values()
            if normalized(row.get("canonical_name")) == normalized(gene_symbol)
        ]
        if len(canonical) == 1:
            return canonical[0], "exact canonical mechanism node name matches gene_symbol"
        if len(unique) > 1:
            gene_reason = f"ambiguous gene_symbol match ({len(unique)} stable nodes)"
        if len(unique) == 1:
            return next(iter(unique.values())), "exact gene_symbol match"
    for value, label in ((entity, "canonical entity label"),):
        matches = node_index.get(normalized(value), []) if value else []
        unique = {row["node_id"]: row for row in matches}
        if len(unique) == 1:
            return next(iter(unique.values())), f"exact {label} match"
        if len(unique) > 1:
            return None, f"ambiguous {label} match ({len(unique)} stable nodes)"
    return None, gene_reason or "no exact stable mechanism-node match"


def protein_context_rows(db_path: Path, selected_ids: set[str], artifact_hash: str, curation_overrides: dict[tuple[str, str], dict[str, str]]) -> tuple[list[dict[str, str]], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    contexts: dict[str, dict[str, str]] = {}
    context_meta: dict[str, dict[str, Any]] = {}
    observations: dict[str, dict[str, Any]] = {}
    query = """
        SELECT po.*, st.title AS study_title, st.doi_or_pmid, st.source_url AS study_source_url,
               st.organism, st.injury_model, st.injury_severity, st.injury_level, st.sex,
               st.perturbation_status,
               cp.reported_label AS population_label, cp.normalized_label AS population_normalized_label,
               tp.post_injury_value, tp.unit AS timepoint_unit, tp.condition,
               tp.tissue_region, tp.injury_distance, tp.injury_distance_unit, tp.sample_count,
               src.source_location, src.source_url, src.repository_accession
        FROM protein_observations po
        JOIN studies st ON st.study_id = po.study_id
        JOIN cell_populations cp ON cp.population_id = po.population_id
        JOIN study_timepoints tp ON tp.timepoint_id = po.timepoint_id
        LEFT JOIN sources src ON src.source_id = po.source_id
        WHERE po.observation_id = ?
    """
    phospho_path = DEFAULT_MSCS_ROOT / "data/derived/phosphorylation_support_observations.tsv"
    for selected in read_tsv(phospho_path):
        observation_id = selected["observation_id"]
        if observation_id not in selected_ids:
            continue
        with sqlite3.connect(db_path) as db:
            db.row_factory = sqlite3.Row
            row = db.execute(query, (observation_id,)).fetchone()
        if row is None:
            raise ValueError(f"selected mSCS protein observation is absent from canonical store: {observation_id}")
        row = apply_curation_override(dict(row), curation_overrides)
        context_id = stable_id("sci:protein", row["study_id"], row["timepoint_id"], row["population_id"])
        population = row["population_label"] or row["population_normalized_label"] or ""
        perturbation = row["condition"] or ""
        treatment = row["perturbation_status"] or ""
        contexts.setdefault(context_id, {
            "context_id": context_id,
            "context_name": f"{row['study_id']} protein context at {timepoint_label(row['post_injury_value'], row['timepoint_unit'])}",
            "context_kind": "sample_context",
            "disease_context": "spinal_cord_injury",
            "anatomical_context": "spinal_cord",
            "species": row["organism"] or "",
            "injury_model": row["injury_model"] or "",
            "injury_level": row["injury_level"] or "",
            "injury_severity": row.get("injury_severity") or "",
            "sex": row.get("sex") or "",
            "timepoint_value": display_timepoint(row["post_injury_value"]),
            "timepoint_unit": row["timepoint_unit"] or "",
            "perturbation": perturbation,
            "treatment": treatment,
            "experimental_condition": row["condition"] or "",
            "study_perturbation_status": row["perturbation_status"] or "",
            "injury_distance": display_number(row.get("injury_distance")),
            "injury_distance_unit": row.get("injury_distance_unit") or "",
            "sample_scope": row.get("sample_scope") or "",
            "sample_count": row.get("sample_count"),
            "cell_type": population,
            "sample_id": "", "study_id": row["study_id"],
            "tissue": row["tissue_region"] or "",
            "context_status": "defined",
            "provenance_note": source_locator(
                "mSCS/data/flow_protein/flow_protein.sqlite",
                f"studies.study_id={row['study_id']}",
                f"study_timepoints.timepoint_id={row['timepoint_id']}",
                f"cell_populations.population_id={row['population_id']}",
                f"study_title={row['study_title']}",
                f"context_curation={json_text(curation_provenance(row))}" if curation_provenance(row) else None,
            ),
        })
        context_meta.setdefault(context_id, {
            "study_id": row["study_id"], "study_title": row["study_title"],
            "doi_or_pmid": row["doi_or_pmid"], "source_url": row["study_source_url"],
            "organism": row["organism"], "injury_model": row["injury_model"],
            "injury_level": row["injury_level"], "timepoint_id": row["timepoint_id"],
            "population_id": row["population_id"], "condition": row["condition"],
            "injury_severity": row["injury_severity"], "sex": row["sex"],
            "injury_distance": row["injury_distance"], "injury_distance_unit": row["injury_distance_unit"],
            "sample_scope": row["sample_scope"], "sample_count": row["sample_count"],
            "tissue_region": row["tissue_region"], "source_location": row["source_location"],
        })
        numeric = number(selected.get("value"))
        direction = selected.get("direction_vs_control") or "not_reported"
        extraction = selected.get("extraction_status") or "unknown"
        if numeric is not None:
            value_kind = "numeric"
        elif direction not in {"", "unknown", "not_reported"}:
            value_kind = "qualitative"
        else:
            value_kind = "unreported"
        if "ambiguous" in extraction or "inaccessible" in extraction:
            status = "unknown"
        elif numeric is not None and "digit" in extraction:
            status = "digitized"
        elif numeric is not None:
            status = "transcribed"
        else:
            status = "reported"
        source_loc = source_locator(
            f"flow_protein.protein_observations.observation_id={observation_id}",
            row["source_location"],
            f"selected_view_line_observation_id={observation_id}",
        )
        observations[observation_id] = {
            "observation_id": observation_id, "context_id": context_id,
            "source_system": "mSCS", "source_database": "flow_protein",
            "source_record_type": "protein_observation", "source_record_key": observation_id,
            "source_version": f"sha256:{artifact_hash}", "modality": "protein",
            "assay": selected.get("assay"), "measurement_kind": selected.get("measurement_kind"),
            "measured_entity_name": selected.get("protein") or selected.get("gene_symbol"),
            "measured_entity_type": "phosphorylated_protein" if selected.get("state_class") == "phosphorylation_specific" else "protein_state",
            "feature_id": selected.get("gene_symbol") or selected.get("protein"),
            "value_numeric": numeric, "value_text": "" if numeric is not None else direction,
            "value_kind": value_kind, "unit": selected.get("unit"),
            "direction_vs_control": direction, "comparator": "reference_control" if direction == "reference_control" else "",
            "biological_replicates": number(selected.get("biological_replicates")),
            "timepoint_value": timepoint_number(row["post_injury_value"]), "timepoint_unit": row["timepoint_unit"],
            "perturbation": perturbation, "cell_type": population, "sample_id": "",
            "observation_status": status, "evidence_role": "dataset_observation",
            "dependency_group": f"mSCS:flow_protein:{row['study_id']}:{row['timepoint_id']}:{row['population_id']}",
            "source_artifact_path": "mSCS/data/flow_protein/flow_protein.sqlite",
            "source_artifact_sha256": artifact_hash, "source_locator": source_loc,
            "provenance_note": json_text({
                "canonical_source": "mSCS/data/flow_protein/flow_protein.sqlite",
                "canonical_observation_id": observation_id,
                "selection_view": "mSCS/data/derived/phosphorylation_support_observations.tsv",
                "selection_state_class": selected.get("state_class"),
                "support_tier": selected.get("support_tier"),
                "evidence_grade": selected.get("evidence_grade"),
                "extraction_status": extraction,
                "primary_source_url": selected.get("primary_source_url"),
                "source_location": selected.get("source_location"),
                "notes": selected.get("notes"),
                **({"context_curation": curation_provenance(row)} if curation_provenance(row) else {}),
            }),
            "_gene_symbol": selected.get("gene_symbol"),
            "_entity": selected.get("protein") or selected.get("gene_symbol"),
            "_context_meta": context_meta[context_id],
            "_context_curation": curation_provenance(row),
            "_study_key": row["study_id"],
            "_injury_model": row["injury_model"] or "unknown",
            "_timepoint_key": timepoint_label(row["post_injury_value"], row["timepoint_unit"]),
            "_evidence_label": selected.get("evidence_grade") or "unknown",
        }
    return list(contexts.values()), context_meta, observations


def protein_expression_rows(db_path: Path, selected_ids: set[str], artifact_hash: str, curation_overrides: dict[tuple[str, str], dict[str, str]]) -> tuple[list[dict[str, str]], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    """Select directly measured, source-extracted non-phosphorylated protein records."""
    contexts: dict[str, dict[str, str]] = {}
    context_meta: dict[str, dict[str, Any]] = {}
    observations: dict[str, dict[str, Any]] = {}
    query = """
        SELECT po.*, st.title AS study_title, st.doi_or_pmid, st.source_url AS study_source_url,
               st.organism, st.injury_model, st.injury_severity, st.injury_level, st.sex,
               st.perturbation_status,
               cp.reported_label AS population_label, cp.normalized_label AS population_normalized_label,
               tp.post_injury_value, tp.unit AS timepoint_unit, tp.condition,
               tp.tissue_region, tp.injury_distance, tp.injury_distance_unit, tp.sample_count,
               src.source_location, src.source_url, src.repository_accession,
               ec.evidence_status, ec.evidence_id
        FROM protein_observations po
        JOIN studies st ON st.study_id = po.study_id
        JOIN cell_populations cp ON cp.population_id = po.population_id
        JOIN study_timepoints tp ON tp.timepoint_id = po.timepoint_id
        LEFT JOIN sources src ON src.source_id = po.source_id
        LEFT JOIN evidence_claims ec ON ec.observation_id = po.observation_id
        ORDER BY po.observation_id
    """
    with sqlite3.connect(db_path) as db:
        db.row_factory = sqlite3.Row
        rows = [dict(row) for row in db.execute(query)]
    for row in rows:
        row = apply_curation_override(row, curation_overrides)
        if not is_protein_expression_candidate(row, selected_ids):
            continue
        observation_id = row["observation_id"]
        context_id = stable_id("sci:protein", row["study_id"], row["timepoint_id"], row["population_id"])
        population = row["population_label"] or row["population_normalized_label"] or ""
        perturbation = row["condition"] or ""
        treatment = row["perturbation_status"] or ""
        contexts.setdefault(context_id, {
            "context_id": context_id,
            "context_name": f"{row['study_id']} protein context at {timepoint_label(row['post_injury_value'], row['timepoint_unit'])}",
            "context_kind": "sample_context", "disease_context": "spinal_cord_injury",
            "anatomical_context": "spinal_cord", "species": row["organism"] or "",
            "injury_model": row["injury_model"] or "", "injury_level": row["injury_level"] or "",
            "injury_severity": row.get("injury_severity") or "", "sex": row.get("sex") or "",
            "timepoint_value": display_timepoint(row["post_injury_value"]),
            "timepoint_unit": row["timepoint_unit"] or "", "perturbation": perturbation,
            "treatment": treatment, "experimental_condition": row["condition"] or "",
            "study_perturbation_status": row["perturbation_status"] or "",
            "injury_distance": display_number(row.get("injury_distance")),
            "injury_distance_unit": row.get("injury_distance_unit") or "",
            "sample_scope": row.get("sample_scope") or "", "sample_count": row.get("sample_count"),
            "cell_type": population, "sample_id": "", "study_id": row["study_id"],
            "tissue": row["tissue_region"] or "", "context_status": "defined",
            "provenance_note": source_locator(
                "mSCS/data/flow_protein/flow_protein.sqlite",
                f"studies.study_id={row['study_id']}",
                f"study_timepoints.timepoint_id={row['timepoint_id']}",
                f"cell_populations.population_id={row['population_id']}",
                f"study_title={row['study_title']}",
                f"context_curation={json_text(curation_provenance(row))}" if curation_provenance(row) else None,
            ),
        })
        context_meta.setdefault(context_id, {
            "study_id": row["study_id"], "study_title": row["study_title"],
            "doi_or_pmid": row["doi_or_pmid"], "source_url": row["study_source_url"],
            "organism": row["organism"], "injury_model": row["injury_model"],
            "injury_level": row["injury_level"], "injury_severity": row["injury_severity"],
            "sex": row["sex"], "timepoint_id": row["timepoint_id"],
            "population_id": row["population_id"], "condition": row["condition"],
            "perturbation_status": row["perturbation_status"],
            "tissue_region": row["tissue_region"], "injury_distance": row["injury_distance"],
            "injury_distance_unit": row["injury_distance_unit"], "sample_scope": row["sample_scope"],
            "sample_count": row["sample_count"], "source_location": row["source_location"],
        })
        numeric = protein_value(row)
        direction = row.get("direction_vs_control") or "not_reported"
        value_text = row.get("transcribed_value_text") or ("" if numeric is not None else direction)
        value_kind = "numeric" if numeric is not None else ("qualitative" if value_text not in {"", "unknown", "not_reported"} else "unreported")
        source_loc = source_locator(
            f"flow_protein.protein_observations.observation_id={observation_id}",
            row.get("source_location"),
        )
        observations[observation_id] = {
            "observation_id": observation_id, "context_id": context_id,
            "source_system": "mSCS", "source_database": "flow_protein",
            "source_record_type": "protein_observation", "source_record_key": observation_id,
            "source_version": f"sha256:{artifact_hash}", "modality": "protein",
            "assay": row.get("assay"), "measurement_kind": row.get("measurement_kind"),
            "measured_entity_name": row.get("protein") or row.get("gene_symbol"),
            "measured_entity_type": "protein_expression", "feature_id": row.get("gene_symbol") or row.get("protein"),
            "value_numeric": numeric, "value_text": value_text, "value_kind": value_kind,
            "unit": row.get("unit"), "direction_vs_control": direction,
            "comparator": "reference_control" if direction == "reference_control" else "",
            "biological_replicates": row.get("biological_replicates"),
            "timepoint_value": timepoint_number(row["post_injury_value"]), "timepoint_unit": row["timepoint_unit"],
            "perturbation": perturbation, "cell_type": population, "sample_id": "",
            "observation_status": "transcribed", "evidence_role": "dataset_observation",
            "dependency_group": f"mSCS:flow_protein:{row['study_id']}:{row['timepoint_id']}:{row['population_id']}",
            "source_artifact_path": "mSCS/data/flow_protein/flow_protein.sqlite",
            "source_artifact_sha256": artifact_hash, "source_locator": source_loc,
            "provenance_note": json_text({
                "canonical_source": "mSCS/data/flow_protein/flow_protein.sqlite",
                "canonical_observation_id": observation_id,
                "selection_rule": "direct protein assay; explicit SCI injury model; source-extracted measurement; non-phosphorylated/non-active form",
                "study_id": row.get("study_id"), "timepoint_id": row.get("timepoint_id"),
                "population_id": row.get("population_id"), "protein_form": row.get("protein_form"),
                "protein_resolution": row.get("protein_resolution"), "sample_scope": row.get("sample_scope"),
                "evidence_grade": row.get("evidence_grade"), "measurement_quality": row.get("measurement_quality"),
                "extraction_status": row.get("extraction_status"), "evidence_status": row.get("evidence_status"),
                "evidence_id": row.get("evidence_id"), "negative_evidence_status": row.get("negative_evidence_status"),
                "source_location": row.get("source_location"), "source_repository_accession": row.get("repository_accession"),
                "study_condition": row.get("condition"), "study_perturbation_status": row.get("perturbation_status"),
                **({"context_curation": curation_provenance(row)} if curation_provenance(row) else {}),
            }),
            "_gene_symbol": row.get("gene_symbol"), "_entity": row.get("protein") or row.get("gene_symbol"),
            "_context_meta": context_meta[context_id], "_context_curation": curation_provenance(row), "_study_key": row["study_id"],
            "_injury_model": row["injury_model"] or "unknown",
            "_timepoint_key": timepoint_label(row["post_injury_value"], row["timepoint_unit"]),
            "_evidence_label": row.get("evidence_grade") or "unknown",
        }
    return list(contexts.values()), context_meta, observations


def metabolomics_rows(
    db_path: Path,
    artifact_hash: str,
    curation_overrides: dict[tuple[str, str], dict[str, str]],
    mscs_root: Path,
) -> tuple[list[dict[str, str]], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    """Import explicit SCI metabolite assays from the mSCS canonical store."""
    contexts: dict[str, dict[str, str]] = {}
    context_meta: dict[str, dict[str, Any]] = {}
    observations: dict[str, dict[str, Any]] = {}
    query = """
        SELECT po.*, st.title AS study_title, st.doi_or_pmid, st.source_url AS study_source_url,
               st.organism, st.injury_model, st.injury_severity, st.injury_level, st.sex,
               st.perturbation_status,
               cp.reported_label AS population_label, cp.normalized_label AS population_normalized_label,
               tp.post_injury_value, tp.unit AS timepoint_unit, tp.condition,
               tp.tissue_region, tp.injury_distance, tp.injury_distance_unit, tp.sample_count,
               src.source_id AS canonical_source_id, src.source_location, src.source_url, src.repository_accession
        FROM protein_observations po
        JOIN studies st ON st.study_id = po.study_id
        JOIN cell_populations cp ON cp.population_id = po.population_id
        JOIN study_timepoints tp ON tp.timepoint_id = po.timepoint_id
        LEFT JOIN sources src ON src.source_id = po.source_id
        ORDER BY po.observation_id
    """
    with sqlite3.connect(db_path) as db:
        db.row_factory = sqlite3.Row
        rows = [dict(row) for row in db.execute(query)]

    for raw_row in rows:
        if not is_metabolomics_import_candidate(raw_row):
            continue
        row = apply_curation_override(raw_row, curation_overrides)
        observation_id = row["observation_id"]
        relative_transcription_path = METABOLOMICS_TRANSCRIPTION_ARTIFACTS.get(observation_id)
        if not relative_transcription_path:
            raise ValueError(f"metabolomics observation lacks a curated transcription artifact mapping: {observation_id}")
        transcription_path = mscs_root / relative_transcription_path
        if not transcription_path.exists():
            raise FileNotFoundError(transcription_path)
        transcription_hash = sha256(transcription_path)
        context_id = stable_id("sci:metabolomics", row["study_id"], row["timepoint_id"], row["population_id"])
        population = row["population_label"] or row["population_normalized_label"] or ""
        perturbation = row["condition"] or ""
        treatment = row["perturbation_status"] or ""
        contexts.setdefault(context_id, {
            "context_id": context_id,
            "context_name": f"{row['study_id']} metabolomics context at {timepoint_label(row['post_injury_value'], row['timepoint_unit'])}",
            "context_kind": "sample_context", "disease_context": "spinal_cord_injury",
            "anatomical_context": "spinal_cord", "species": row["organism"] or "",
            "injury_model": row["injury_model"] or "", "injury_level": row["injury_level"] or "",
            "injury_severity": row.get("injury_severity") or "", "sex": row.get("sex") or "",
            "timepoint_value": display_timepoint(row["post_injury_value"]),
            "timepoint_unit": row["timepoint_unit"] or "", "perturbation": perturbation,
            "treatment": treatment, "experimental_condition": row["condition"] or "",
            "study_perturbation_status": row["perturbation_status"] or "",
            "injury_distance": display_number(row.get("injury_distance")),
            "injury_distance_unit": row.get("injury_distance_unit") or "",
            "sample_scope": row.get("sample_scope") or "", "sample_count": row.get("sample_count"),
            "cell_type": "", "sample_id": "", "study_id": row["study_id"],
            "tissue": row["tissue_region"] or "", "context_status": "defined",
            "provenance_note": source_locator(
                "mSCS/data/flow_protein/flow_protein.sqlite",
                f"studies.study_id={row['study_id']}",
                f"study_timepoints.timepoint_id={row['timepoint_id']}",
                f"cell_populations.population_id={row['population_id']}",
                f"sources.source_id={row.get('canonical_source_id')}",
                f"transcription_artifact=mSCS/{relative_transcription_path}",
                f"transcription_sha256={transcription_hash}",
                f"study_title={row['study_title']}",
                f"context_curation={json_text(curation_provenance(row))}" if curation_provenance(row) else None,
            ),
        })
        context_meta.setdefault(context_id, {
            "study_id": row["study_id"], "study_title": row["study_title"],
            "doi_or_pmid": row["doi_or_pmid"], "source_url": row["study_source_url"],
            "organism": row["organism"], "injury_model": row["injury_model"],
            "injury_level": row["injury_level"], "timepoint_id": row["timepoint_id"],
            "population_id": row["population_id"], "condition": row["condition"],
            "injury_severity": row["injury_severity"], "sex": row["sex"],
            "injury_distance": row["injury_distance"], "injury_distance_unit": row["injury_distance_unit"],
            "sample_scope": row["sample_scope"], "sample_count": row["sample_count"],
            "tissue_region": row["tissue_region"], "source_location": row["source_location"],
        })
        numeric = protein_value(row)
        direction = row.get("direction_vs_control") or "not_reported"
        value_text = row.get("transcribed_value_text") or ("" if numeric is not None else direction)
        extraction = row.get("extraction_status") or "unknown"
        value_kind = "numeric" if numeric is not None else (
            "qualitative" if value_text not in {"", "unknown", "not_reported"} else "unreported"
        )
        if numeric is not None and "digit" in extraction:
            status = "digitized"
        elif numeric is not None:
            status = "transcribed"
        elif direction not in {"", "unknown", "not_reported"}:
            status = "reported"
        else:
            status = "not_measured"
        source_loc = source_locator(
            f"flow_protein.protein_observations.observation_id={observation_id}",
            f"sources.source_id={row.get('canonical_source_id')}",
            row.get("source_location"),
            f"transcription_artifact=mSCS/{relative_transcription_path}",
        )
        measured_entity = row.get("protein") or ""
        measured_type = "lipid_mediator" if "lipid" in (row.get("protein_form") or "").lower() else "metabolite"
        observations[observation_id] = {
            "observation_id": observation_id, "context_id": context_id,
            "source_system": "mSCS", "source_database": "flow_protein",
            "source_record_type": "metabolomics_observation", "source_record_key": observation_id,
            "source_version": f"sha256:{artifact_hash}", "modality": "metabolomics",
            "assay": row.get("assay"), "measurement_kind": row.get("measurement_kind"),
            "measured_entity_name": measured_entity, "measured_entity_type": measured_type,
            "feature_id": measured_entity, "value_numeric": numeric, "value_text": value_text,
            "value_kind": value_kind, "unit": row.get("unit"),
            "direction_vs_control": direction,
            "comparator": "reference_control" if direction == "reference_control" else "",
            "biological_replicates": row.get("biological_replicates"),
            "timepoint_value": timepoint_number(row["post_injury_value"]), "timepoint_unit": row["timepoint_unit"],
            "perturbation": perturbation, "cell_type": "", "sample_id": "",
            "observation_status": status, "evidence_role": "dataset_observation",
            "dependency_group": f"mSCS:flow_metabolomics:{row['study_id']}:{row['timepoint_id']}:{row['population_id']}",
            "source_artifact_path": "mSCS/data/flow_protein/flow_protein.sqlite",
            "source_artifact_sha256": artifact_hash, "source_locator": source_loc,
            "provenance_note": json_text({
                "canonical_source": "mSCS/data/flow_protein/flow_protein.sqlite",
                "canonical_observation_id": observation_id,
                "canonical_source_id": row.get("canonical_source_id"),
                "transcription_source_artifact": f"mSCS/{relative_transcription_path}",
                "transcription_source_sha256": transcription_hash,
                "selection_rule": "explicit SCI metabolite/lipid-mediator assay; direct source-extracted or explicitly reported direction; no protein relabeling",
                "study_id": row.get("study_id"), "timepoint_id": row.get("timepoint_id"),
                "population_id": row.get("population_id"), "protein_form": row.get("protein_form"),
                "protein_resolution": row.get("protein_resolution"), "sample_scope": row.get("sample_scope"),
                "evidence_grade": row.get("evidence_grade"), "measurement_quality": row.get("measurement_quality"),
                "extraction_status": extraction, "negative_evidence_status": row.get("negative_evidence_status"),
                "source_location": row.get("source_location"), "source_repository_accession": row.get("repository_accession"),
                "study_condition": row.get("condition"), "study_perturbation_status": row.get("perturbation_status"),
                **({"context_curation": curation_provenance(row)} if curation_provenance(row) else {}),
            }),
            "_gene_symbol": None, "_entity": measured_entity,
            "_context_meta": context_meta[context_id], "_context_curation": curation_provenance(row),
            "_study_key": row["study_id"], "_injury_model": row["injury_model"] or "unknown",
            "_timepoint_key": timepoint_label(row["post_injury_value"], row["timepoint_unit"]),
            "_evidence_label": row.get("evidence_grade") or "unknown",
        }
    return list(contexts.values()), context_meta, observations


def epigenetic_rows(db_path: Path, artifact_hash: str) -> tuple[list[dict[str, str]], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    contexts: dict[str, dict[str, str]] = {}
    context_meta: dict[str, dict[str, Any]] = {}
    observations: dict[str, dict[str, Any]] = {}
    def add_context(row: dict[str, Any]) -> str:
        context_key = row.get("context_id") or row.get("assay_id")
        context_id = stable_id("sci:epigenetic", row["study_id"], context_key)
        if context_id in contexts:
            return context_id
        context_cell = row.get("cell_type") or ""
        sample_scope = row.get("sorting_or_enrichment") or row.get("sample_unit") or ""
        contexts[context_id] = {
            "context_id": context_id,
            "context_name": f"{row['study_id']} epigenetic context at {timepoint_label(row.get('post_injury_value'), row.get('post_injury_unit'))}",
            "context_kind": "sample_context" if sample_scope or context_cell else "study_context",
            "disease_context": "spinal_cord_injury", "anatomical_context": "spinal_cord",
            "species": row.get("species") or "", "injury_model": row.get("injury_model") or "",
            "injury_level": row.get("injury_level") or "",
            "injury_severity": row.get("injury_severity") or "", "sex": row.get("sex") or "",
            "timepoint_value": display_timepoint(row.get("post_injury_value")),
            "timepoint_unit": row.get("post_injury_unit") or "",
            "perturbation": row.get("condition") or "", "treatment": "",
            "experimental_condition": row.get("condition") or "",
            "study_perturbation_status": row.get("condition") or "",
            "injury_distance": "", "injury_distance_unit": "",
            "sample_scope": sample_scope, "sample_count": row.get("replicate_count"),
            "cell_type": context_cell, "sample_id": "",
            "study_id": row["study_id"], "tissue": row.get("tissue_region") or row.get("tissue") or "",
            "context_status": "defined",
            "provenance_note": source_locator(
                "mSCS/data/epigenetic/epigenetic.sqlite",
                f"studies.study_id={row['study_id']}",
                f"assays.assay_id={row['assay_id']}",
                f"assay_contexts.context_id={context_key}",
                f"study_title={row.get('study_title')}",
                f"source_url={row.get('source_url')}",
            ),
        }
        context_meta[context_id] = {
            "study_id": row["study_id"], "study_title": row.get("study_title"),
            "species": row.get("species"), "injury_model": row.get("injury_model"),
            "injury_level": row.get("injury_level"), "injury_severity": row.get("injury_severity"),
            "sex": row.get("sex"), "timepoint_id": context_key,
            "condition": row.get("condition"), "source_location": row.get("source_location"),
            "source_url": row.get("source_url"),
        }
        return context_id

    context_query = """
        SELECT c.*, a.assay_name,
               s.study_id, s.title AS study_title, s.species, s.injury_model,
               s.injury_level, s.injury_severity, s.sex, s.curation_status,
               src.source_location, src.source_url
        FROM assay_contexts c
        JOIN assays a ON a.assay_id = c.assay_id
        JOIN studies s ON s.study_id = a.study_id
        LEFT JOIN sources src ON src.source_id = a.source_id
        ORDER BY c.context_id
    """
    with sqlite3.connect(db_path) as db:
        db.row_factory = sqlite3.Row
        for row in db.execute(context_query):
            add_context(dict(row))

    query = """
        SELECT o.*, a.assay_name, a.epigenetic_class, a.target AS assay_target,
               a.directness, a.evidence_scope, a.evidence_level,
               c.condition, c.post_injury_value, c.post_injury_unit, c.tissue,
               c.tissue_region, c.cell_type, c.sorting_or_enrichment,
               c.replicate_count, c.sample_unit,
               s.study_id, s.title AS study_title, s.species, s.injury_model,
               s.injury_level, s.injury_severity, s.sex, s.pmid, s.doi, s.curation_status,
               src.source_location, src.source_url
        FROM observations o
        JOIN assays a ON a.assay_id = o.assay_id
        LEFT JOIN assay_contexts c ON c.context_id = o.context_id
        LEFT JOIN studies s ON s.study_id = a.study_id
        LEFT JOIN sources src ON src.source_id = o.source_id
        ORDER BY o.observation_id
    """
    with sqlite3.connect(db_path) as db:
        db.row_factory = sqlite3.Row
        rows = [dict(row) for row in db.execute(query)]
    for row in rows:
        context_id = add_context(row)
        context_cell = row.get("cell_type") or ""
        numeric = number(row.get("effect_value"))
        direction = row.get("direction_vs_control") or "not_reported"
        value_kind = "numeric" if numeric is not None else ("qualitative" if direction not in {"", "not_reported"} else "unreported")
        feature_name = row.get("gene_symbol") or row.get("target") or row.get("feature_id") or row.get("feature_type")
        source_loc = source_locator(
            f"epigenetic.observations.observation_id={row['observation_id']}",
            row.get("source_location"),
        )
        observations[row["observation_id"]] = {
            "observation_id": row["observation_id"], "context_id": context_id,
            "source_system": "mSCS", "source_database": "epigenetic",
            "source_record_type": "epigenetic_observation", "source_record_key": row["observation_id"],
            "source_version": f"sha256:{artifact_hash}", "modality": "epigenomics",
            "assay": row.get("assay_name"), "measurement_kind": row.get("measurement_kind"),
            "measured_entity_name": feature_name, "measured_entity_type": row.get("feature_type"),
            "feature_id": row.get("feature_id"), "value_numeric": numeric,
            "value_text": "" if numeric is not None else direction, "value_kind": value_kind,
            "unit": row.get("effect_unit"), "direction_vs_control": direction,
            "comparator": "", "biological_replicates": number(row.get("replicate_count")),
            "timepoint_value": timepoint_number(row.get("post_injury_value")), "timepoint_unit": row.get("post_injury_unit"),
            "perturbation": row.get("condition"), "cell_type": context_cell, "sample_id": "",
            "observation_status": "reported", "evidence_role": "dataset_observation",
            "dependency_group": f"mSCS:epigenetic:{row['study_id']}:{row['assay_id']}:{row['context_id']}",
            "source_artifact_path": "mSCS/data/epigenetic/epigenetic.sqlite",
            "source_artifact_sha256": artifact_hash, "source_locator": source_loc,
            "provenance_note": json_text({
                "study_id": row["study_id"], "study_title": row["study_title"],
                "observation_id": row["observation_id"], "assay_id": row["assay_id"],
                "epigenetic_class": row.get("epigenetic_class"), "directness": row.get("directness"),
                "evidence_scope": row.get("evidence_scope"), "evidence_level": row.get("evidence_level"),
                "evidence_status": row.get("evidence_status"), "curation_status": row.get("curation_status"),
                "pmid": row.get("pmid"), "doi": row.get("doi"),
                "source_location": row.get("source_location"), "source_url": row.get("source_url"),
                "notes": row.get("notes"),
            }),
            "_gene_symbol": row.get("gene_symbol"), "_entity": feature_name,
            "_context_meta": context_meta[context_id], "_study_key": row["study_id"],
            "_injury_model": row.get("injury_model") or "unknown",
            "_timepoint_key": timepoint_label(row.get("post_injury_value"), row.get("post_injury_unit")),
            "_evidence_label": f"{row.get('epigenetic_class')}:{row.get('directness')}:{row.get('evidence_level')}",
        }
    binary_query = """
        SELECT b.*, a.assay_name, a.epigenetic_class, a.directness,
               a.evidence_scope, a.evidence_level,
               c.condition, c.post_injury_value, c.post_injury_unit, c.tissue,
               c.tissue_region, c.cell_type, c.sorting_or_enrichment,
               c.replicate_count, c.sample_unit,
               s.study_id, s.title AS study_title, s.species, s.injury_model,
               s.injury_level, s.injury_severity, s.sex, s.pmid, s.doi,
               s.curation_status, src.source_location, src.source_url
        FROM binary_feature_status b
        JOIN assays a ON a.assay_id = b.assay_id
        LEFT JOIN assay_contexts c ON c.context_id = b.context_id
        JOIN studies s ON s.study_id = a.study_id
        LEFT JOIN sources src ON src.source_id = a.source_id
        ORDER BY b.binary_id
    """
    with sqlite3.connect(db_path) as db:
        db.row_factory = sqlite3.Row
        binary_rows = [dict(row) for row in db.execute(binary_query)]
    status_map = {
        "present": "observed", "absent": "negative",
        "not_assayed": "not_measured", "unavailable": "not_measured",
        "insufficient_coverage": "unknown", "not_evaluable": "unknown",
    }
    for row in binary_rows:
        context_id = add_context(row)
        observation_id = f"EPIGENETIC_BINARY:{row['binary_id']}"
        numeric = number(row.get("quantitative_value"))
        detection_status = row.get("detection_status") or "unknown"
        source_artifact = row.get("source_artifact") or ""
        source_artifact_path = f"mSCS/{source_artifact}" if source_artifact else "mSCS/data/epigenetic/epigenetic.sqlite"
        source_artifact_hash = row.get("source_artifact_hash") or artifact_hash
        feature_name = row.get("target") or row.get("feature_id") or row.get("feature_type")
        source_loc = source_locator(
            f"epigenetic.binary_feature_status.binary_id={row['binary_id']}",
            f"feature_type={row.get('feature_type')}",
            f"feature_id={row.get('feature_id')}",
            row.get("source_location"),
            f"source_url={row.get('source_url')}",
        )
        observations[observation_id] = {
            "observation_id": observation_id, "context_id": context_id,
            "source_system": "mSCS", "source_database": "epigenetic",
            "source_record_type": "epigenetic_binary_feature", "source_record_key": row["binary_id"],
            "source_version": f"sha256:{artifact_hash}", "modality": "epigenomics",
            "assay": row.get("assay_name"), "measurement_kind": "binary feature status",
            "measured_entity_name": feature_name, "measured_entity_type": row.get("feature_type"),
            "feature_id": row.get("feature_id"), "value_numeric": numeric,
            "value_text": "" if numeric is not None else detection_status,
            "value_kind": "numeric" if numeric is not None else "qualitative",
            "unit": row.get("quantitative_unit"), "direction_vs_control": "not_reported",
            "comparator": "", "biological_replicates": number(row.get("replicate_count")),
            "timepoint_value": timepoint_number(row.get("post_injury_value")),
            "timepoint_unit": row.get("post_injury_unit"), "perturbation": row.get("condition"),
            "cell_type": row.get("cell_type") or "", "sample_id": "",
            "observation_status": status_map.get(detection_status, "unknown"),
            "evidence_role": "dataset_observation",
            "dependency_group": f"mSCS:epigenetic:{row['study_id']}:{row['assay_id']}:{row.get('context_id') or row['assay_id']}",
            "source_artifact_path": source_artifact_path,
            "source_artifact_sha256": source_artifact_hash, "source_locator": source_loc,
            "provenance_note": json_text({
                "study_id": row["study_id"], "study_title": row.get("study_title"),
                "binary_id": row["binary_id"], "assay_id": row["assay_id"],
                "epigenetic_class": row.get("epigenetic_class"), "directness": row.get("directness"),
                "evidence_scope": row.get("evidence_scope"), "evidence_level": row.get("evidence_level"),
                "detection_status": detection_status, "availability_observed": row.get("availability_observed"),
                "analysis_version": row.get("analysis_version"),
                "source_artifact": source_artifact, "source_artifact_hash": source_artifact_hash,
                "source_location": row.get("source_location"), "source_url": row.get("source_url"),
                "notes": row.get("notes"),
            }),
            "_gene_symbol": row.get("target"), "_entity": feature_name,
            "_context_meta": context_meta[context_id], "_study_key": row["study_id"],
            "_injury_model": row.get("injury_model") or "unknown",
            "_timepoint_key": timepoint_label(row.get("post_injury_value"), row.get("post_injury_unit")),
            "_evidence_label": f"{row.get('epigenetic_class')}:{row.get('directness')}:{row.get('evidence_level')}",
        }
    return list(contexts.values()), context_meta, observations


def transcriptomic_timepoints(dataset_id: str, curator_notes: str, capture: dict[str, Any] | None) -> list[tuple[float, str]]:
    """Return only timepoints explicitly retained by the spatial catalog."""
    if capture and capture.get("timepoint"):
        match = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*(dpi|hpi)\s*", str(capture["timepoint"]))
        if match:
            return [(float(match.group(1)), match.group(2))]
    explicit = {
        "MSCIDATA000043": [(0.0, "hpi"), (3.0, "hpi"), (24.0, "hpi"), (72.0, "hpi")],
        "MSCIDATA000027": [(3.0, "dpi")],
        "MSCIDATA000019": [(7.0, "weeks_after_transplantation")],
    }
    return explicit.get(dataset_id, [])


def transcriptomic_context_fields(dataset_id: str, dataset: dict[str, Any], protocols: list[dict[str, Any]]) -> dict[str, str]:
    """Map catalog text to context fields without treating catalog annotations as measurements."""
    metadata = json.loads(dataset["dataset_metadata_json"] or "{}")
    notes = metadata.get("curator_notes") or ""
    protocol_text = " | ".join(
        str(item.get("dissociation_method_reported") or item.get("notes") or "")
        for item in protocols
        if item.get("dissociation_method_reported") or item.get("notes")
    )
    fields = {
        "species": dataset.get("organism") or "",
        "injury_model": "",
        "injury_level": "",
        "injury_severity": "",
        "sex": "",
        "perturbation": "",
        "treatment": "",
        "experimental_condition": notes,
        "study_perturbation_status": "",
        "sample_scope": notes,
        "sample_count": "",
        "cell_type": "",
        "tissue": dataset.get("tissue") or "",
    }
    if dataset_id == "MSCIDATA000008":
        fields.update({"injury_model": "right lateral hemisection", "injury_level": "T10"})
    elif dataset_id == "MSCIDATA000011":
        fields.update({
            "injury_model": "spinal cord injury",
            "injury_level": "mid-thoracic (GEO label); lumbar (protocol text)",
            "sample_count": "72",
            "experimental_condition": "lesion-epicenter sections; serial sampling through the dorsoventral axis",
        })
    elif dataset_id == "MSCIDATA000016":
        fields.update({"injury_model": "spinal cord injury", "sample_count": "7"})
    elif dataset_id == "MSCIDATA000019":
        fields.update({
            "injury_model": "complete spinal cord transection",
            "injury_level": "T9",
            "sex": "female",
            "treatment": "enTsOrg or sOrg transplantation",
            "sample_count": "2",
            "experimental_condition": "mouse spinal cord spatial transcriptomics at 7 weeks after enTsOrg or sOrg transplantation",
        })
    elif dataset_id == "MSCIDATA000027":
        fields.update({"injury_model": "acute spinal cord injury", "sample_count": "4"})
    elif dataset_id == "MSCIDATA000029":
        fields.update({
            "injury_model": "paralysis/spinal cord injury rehabilitation context",
            "treatment": "EES rehabilitation",
            "sample_count": "16",
            "experimental_condition": "SCI->EES::walking labels are present in the deposited spot-level metadata",
        })
    elif dataset_id == "MSCIDATA000038":
        fields.update({
            "injury_model": "spinal cord injury",
            "experimental_condition": "SCI/sham/solu-medrol spinal cord sections",
            "study_perturbation_status": "SCI/sham/solu-medrol",
        })
    elif dataset_id == "MSCIDATA000043":
        fields.update({
            "injury_model": "mouse spinal cord injury",
            "experimental_condition": "rostral/caudal distances; 0, 3, 24, and 72 hpi",
        })
    elif dataset_id == "MSCIDATA000199":
        fields.update({
            "injury_model": "lesion-remote spinal-cord repair context",
            "cell_type": "lesion-remote astrocytes",
            "sample_count": "16",
        })
    fields["sample_scope"] = fields["sample_scope"] or protocol_text
    return fields


def spatial_transcriptomic_rows(spatial_catalog_path: Path, artifact_hash: str) -> tuple[list[dict[str, str]], dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, int]]:
    """Import SCI-specific spatial-transcriptomic context, not gene/spot measurements."""
    contexts: dict[str, dict[str, str]] = {}
    context_meta: dict[str, dict[str, Any]] = {}
    observations: dict[str, dict[str, Any]] = {}
    assessed = {"catalog_rows_assessed": 0, "datasets_imported": 0, "datasets_excluded": 0, "excluded_dataset_ids": []}
    with sqlite3.connect(spatial_catalog_path) as db:
        db.row_factory = sqlite3.Row
        datasets = [dict(row) for row in db.execute(
            "SELECT * FROM datasets WHERE assay_family = 'spatial_transcriptomics' ORDER BY dataset_id"
        )]
        for dataset in datasets:
            assessed["catalog_rows_assessed"] += 1
            dataset_id = dataset["dataset_id"]
            if dataset_id not in SCI_SPATIAL_TRANSCRIPTOMIC_DATASETS:
                assessed["datasets_excluded"] += 1
                assessed["excluded_dataset_ids"].append(dataset_id)
                continue
            assessed["datasets_imported"] += 1
            metadata = json.loads(dataset["dataset_metadata_json"] or "{}")
            citation = json.loads(dataset["citation_metadata_json"] or "[]")
            protocols = json.loads(dataset["protocol_metadata_json"] or "[]")
            fields = transcriptomic_context_fields(dataset_id, dataset, protocols)
            captures = [dict(row) for row in db.execute(
                "SELECT * FROM captures WHERE dataset_id = ? ORDER BY capture_id", (dataset_id,)
            )]
            context_specs: list[dict[str, Any]] = []
            if captures:
                for capture in captures:
                    context_specs.append({
                        "label": f"capture {capture['capture_id']}",
                        "capture": capture,
                        "timepoints": transcriptomic_timepoints(dataset_id, metadata.get("curator_notes") or "", capture),
                        "sample_id": f"{dataset_id}:{capture['capture_id']}",
                    })
            else:
                timepoints = transcriptomic_timepoints(dataset_id, metadata.get("curator_notes") or "", None)
                context_specs.append({
                    "label": "dataset context",
                    "capture": None,
                    "timepoints": timepoints or [(None, "")],
                    "sample_id": "",
                })
            for spec in context_specs:
                for timepoint_value, timepoint_unit in spec["timepoints"]:
                    timepoint_suffix = f":{display_number(timepoint_value)}{timepoint_unit}" if timepoint_value is not None else ""
                    context_id = stable_id("sci:transcriptomics", dataset_id, spec["sample_id"], timepoint_value, timepoint_unit)
                    if context_id not in contexts:
                        context_status = "defined"
                        context_name = f"{dataset['accession']} {spec['label']} transcriptomic context"
                        contexts[context_id] = {
                            "context_id": context_id, "context_name": context_name,
                            "context_kind": "sample_context" if spec["sample_id"] else "study_context",
                            "disease_context": "spinal_cord_injury", "anatomical_context": "spinal_cord",
                            "species": fields["species"], "injury_model": fields["injury_model"],
                            "injury_level": fields["injury_level"], "injury_severity": fields["injury_severity"],
                            "sex": fields["sex"], "timepoint_value": display_timepoint(timepoint_value),
                            "timepoint_unit": timepoint_unit, "perturbation": fields["perturbation"],
                            "treatment": fields["treatment"], "experimental_condition": fields["experimental_condition"],
                            "study_perturbation_status": fields["study_perturbation_status"], "injury_distance": "",
                            "injury_distance_unit": "", "sample_scope": fields["sample_scope"],
                            "sample_count": fields["sample_count"],
                            "cell_type": fields["cell_type"], "sample_id": spec["sample_id"],
                            "study_id": metadata.get("study_id") or "", "tissue": fields["tissue"],
                            "context_status": context_status,
                            "provenance_note": source_locator(
                                "mSCS/data/spatial/spatial_catalog.sqlite",
                                f"datasets.dataset_id={dataset_id}", f"datasets.accession={dataset['accession']}",
                                f"datasets.source_row_hash={dataset.get('source_row_hash')}",
                                f"datasets.source_manifest={dataset.get('source_manifest')}",
                                f"captures.capture_id={spec['capture']['capture_id']}" if spec["capture"] else None,
                                f"captures.source_row_hash={spec['capture'].get('source_row_hash')}" if spec["capture"] else None,
                            ),
                        }
                        context_meta[context_id] = {
                            "study_id": metadata.get("study_id") or "", "study_title": dataset.get("title"),
                            "injury_model": fields["injury_model"], "timepoint_id": spec["capture"].get("capture_id") if spec["capture"] else "",
                            "timepoint_value": timepoint_value, "timepoint_unit": timepoint_unit,
                            "sample_id": spec["sample_id"], "tissue": fields["tissue"],
                        }
                    observation_id = f"TRANSCRIPTOMIC_CONTEXT:{dataset_id}:{spec['sample_id'] or 'dataset'}{timepoint_suffix}"
                    capture_locator = (
                        f"captures.capture_id={spec['capture']['capture_id']};captures.timepoint={spec['capture']['timepoint']};captures.replicate={spec['capture']['replicate']}"
                        if spec["capture"] else None
                    )
                    source_loc = source_locator(
                        f"spatial_catalog.datasets.dataset_id={dataset_id}",
                        f"spatial_catalog.datasets.accession={dataset['accession']}",
                        capture_locator,
                        f"source_manifest={dataset.get('source_manifest')}",
                    )
                    observations[observation_id] = {
                        "observation_id": observation_id, "context_id": context_id,
                        "source_system": "mSCS", "source_database": "spatial_catalog",
                        "source_record_type": "spatial_transcriptomic_dataset_context",
                        "source_record_key": f"{dataset_id}:{spec['sample_id'] or 'dataset'}{timepoint_suffix}",
                        "source_version": f"sha256:{artifact_hash}", "modality": "transcriptomics",
                        "assay": metadata.get("technology_reported") or metadata.get("assay_family"),
                        "measurement_kind": "dataset context annotation",
                        "measured_entity_name": dataset["accession"], "measured_entity_type": "spatial_transcriptomic_dataset",
                        "feature_id": dataset["accession"], "value_numeric": None,
                        "value_text": "SCI-context dataset annotation; gene-level and spot-level values not imported in this release",
                        "value_kind": "unreported", "unit": "", "direction_vs_control": "not_reported",
                        "comparator": "", "biological_replicates": "",
                        "timepoint_value": timepoint_value, "timepoint_unit": timepoint_unit,
                        "perturbation": fields["perturbation"], "cell_type": fields["cell_type"],
                        "sample_id": spec["sample_id"], "observation_status": "reported",
                        "evidence_role": "contextual_annotation", "dependency_group": f"mSCS:spatial_catalog:{dataset_id}",
                        "source_artifact_path": "mSCS/data/spatial/spatial_catalog.sqlite",
                        "source_artifact_sha256": artifact_hash, "source_locator": source_loc,
                        "provenance_note": json_text({
                            "dataset_id": dataset_id, "accession": dataset["accession"], "title": dataset["title"],
                            "study_id": metadata.get("study_id"), "organism": dataset.get("organism"), "tissue": dataset.get("tissue"),
                            "dataset_metadata": metadata, "protocol_metadata": protocols, "citation_metadata": citation,
                            "source_manifest": dataset.get("source_manifest"), "source_row_hash": dataset.get("source_row_hash"),
                            "capture": spec["capture"], "selection": "explicit SCI-context spatial-transcriptomic catalog record; annotation only",
                        }),
                        "_gene_symbol": None, "_entity": None, "_context_meta": context_meta[context_id],
                        "_study_key": metadata.get("study_id") or dataset_id, "_injury_model": fields["injury_model"] or "unknown",
                        "_timepoint_key": timepoint_label(timepoint_value, timepoint_unit), "_evidence_label": "contextual_annotation",
                    }
    return list(contexts.values()), context_meta, observations, assessed


def external_transcriptomic_rows(evidence_path: Path, artifact_hash: str) -> tuple[list[dict[str, str]], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    """Import only explicit SCI qRT-PCR transcript observations from the pinned release."""
    contexts: dict[str, dict[str, str]] = {}
    context_meta: dict[str, dict[str, Any]] = {}
    observations: dict[str, dict[str, Any]] = {}
    rows = [row for row in read_tsv(evidence_path) if row.get("record_id") in EXTERNAL_TRANSCRIPTOMIC_RECORDS]
    if len(rows) != len(EXTERNAL_TRANSCRIPTOMIC_RECORDS):
        missing = sorted(EXTERNAL_TRANSCRIPTOMIC_RECORDS - {row.get("record_id") for row in rows})
        raise ValueError(f"missing curated external transcriptomic evidence records: {', '.join(missing)}")
    try:
        source_artifact_path = str(evidence_path.relative_to(ROOT))
    except ValueError:
        source_artifact_path = str(evidence_path)
    for row in rows:
        record_id = row["record_id"]
        context_id = stable_id("sci:external_transcriptomics", record_id)
        target = "ppET-1 qRT-PCR target (source wording)" if record_id.endswith("4631") else "ECE1/ECE2/ECE3 qRT-PCR targets (source wording)"
        perturbation = "thrombin; PAR1-pathway inhibition" if record_id.endswith("4631") else "thrombin; ECE1 siRNA"
        contexts[context_id] = {
            "context_id": context_id, "context_name": f"{row['source_locator']} external SCI transcript context",
            "context_kind": "sample_context", "disease_context": "spinal_cord_injury", "anatomical_context": "spinal_cord",
            "species": row.get("species_context") or "", "injury_model": "rat spinal-cord contusion", "injury_level": "",
            "injury_severity": "", "sex": "", "timepoint_value": "", "timepoint_unit": "",
            "perturbation": perturbation, "treatment": "", "experimental_condition": row.get("context_scope") or "",
            "study_perturbation_status": "", "injury_distance": "", "injury_distance_unit": "",
            "sample_scope": row.get("context_scope") or "", "sample_count": "", "cell_type": "primary rat astrocytes",
            "sample_id": "", "study_id": "PMID:40443301", "tissue": "spinal cord lesion site; primary rat astrocyte assay",
            "context_status": "defined",
            "provenance_note": source_locator(source_artifact_path, f"record_id={record_id}", f"source_locator={row.get('source_locator')}"),
        }
        context_meta[context_id] = {"study_id": "PMID:40443301", "study_title": row.get("citation_note"), "injury_model": "rat spinal-cord contusion", "timepoint_id": "", "tissue": "spinal cord lesion site; primary rat astrocyte assay"}
        observation_id = f"EXTERNAL_TRANSCRIPTOMIC:{record_id}"
        observations[observation_id] = {
            "observation_id": observation_id, "context_id": context_id, "source_system": "mSCIdblit",
            "source_database": "mechanism_downstream_evidence_records", "source_record_type": "external_transcriptomic_observation",
            "source_record_key": record_id, "source_version": f"sha256:{artifact_hash}", "modality": "transcriptomics",
            "assay": "qRT-PCR", "measurement_kind": "transcript expression", "measured_entity_name": target,
            "measured_entity_type": "transcript_target_set", "feature_id": "", "value_numeric": None,
            "value_text": "increased/induced as reported in the evidence summary; scalar value not retained in the mechanism evidence record",
            "value_kind": "qualitative", "unit": "", "direction_vs_control": "increased", "comparator": "",
            "biological_replicates": "", "timepoint_value": "", "timepoint_unit": "", "perturbation": perturbation,
            "cell_type": "primary rat astrocytes", "sample_id": "", "observation_status": "reported",
            "evidence_role": "context_matched_external_observation", "dependency_group": f"mSCIdblit:external_transcriptomics:{row['source_locator']}",
            "source_artifact_path": source_artifact_path, "source_artifact_sha256": artifact_hash,
            "source_locator": source_locator(
                f"record_id={record_id}", row.get("source_locator"),
                f"evidence_node_id={row.get('evidence_node_id')}" if row.get("evidence_node_id") else None,
            ),
            "provenance_note": json_text({
                "record_id": record_id, "source_locator": row.get("source_locator"), "source_evidence_ids": row.get("source_evidence_ids"),
                "citation_note": row.get("citation_note"), "evidence_summary": row.get("evidence_summary"),
                "limitations": row.get("limitations"), "context_scope": row.get("context_scope"),
                "assay_or_perturbation": row.get("assay_or_perturbation"), "selection": "explicit SCI qRT-PCR observation; no upstream causality inferred",
            }),
            "_gene_symbol": None, "_entity": None, "_context_meta": context_meta[context_id], "_study_key": "PMID:40443301",
            "_injury_model": "rat spinal-cord contusion", "_timepoint_key": "unknown", "_evidence_label": "external_qRT_PCR",
        }
    return list(contexts.values()), context_meta, observations


def transcriptomic_rows(spatial_catalog_path: Path, spatial_hash: str, evidence_path: Path, evidence_hash: str) -> tuple[list[dict[str, str]], dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, int]]:
    spatial_contexts, spatial_meta, spatial_obs, assessment = spatial_transcriptomic_rows(spatial_catalog_path, spatial_hash)
    external_contexts, external_meta, external_obs = external_transcriptomic_rows(evidence_path, evidence_hash)
    return spatial_contexts + external_contexts, {**spatial_meta, **external_meta}, {**spatial_obs, **external_obs}, assessment


def link_for_observation(observation: dict[str, Any], node_index: dict[str, list[dict[str, str]]]) -> dict[str, str]:
    node, reason = exact_node(node_index, observation.get("_gene_symbol"), observation.get("_entity"))
    if node is not None:
        if observation["modality"] == "epigenomics":
            route_stage = "tf" if observation.get("measured_entity_type") in {"promoter", "transcription_factor"} else "context"
            role = "tf_support" if route_stage == "tf" else "regulatory_context"
        else:
            route_stage = "intracellular" if "phosph" in (observation.get("measured_entity_type") or "") or observation.get("measurement_kind") == "protein_state" else "output"
            role = "intracellular_support" if route_stage == "intracellular" else "output_support"
        basis = f"{reason}; source measurement is retained as an observation-level state and does not infer upstream ligand/receptor causality."
        notes = "Exact stable node identifier resolved in the pinned bundle; no graph edge or route promotion is created."
        return {
            "link_id": f"LINK:{observation['observation_id']}", "observation_id": observation["observation_id"],
            "mechanism_release_id": RELEASE_ID, "mechanism_target_kind": "node",
            "mechanism_target_key": node["node_id"], "mechanism_route_id": "",
            "route_stage": route_stage, "link_role": role, "context_match": "related",
            "support_status": "supporting", "release_status": "included", "link_basis": basis,
            "source_field_locator": observation["source_locator"], "notes": notes,
        }
    unresolved = (
        f"{reason}; staged at module boundary 21B because the source observation has explicit SCI context "
        "but no exact stable route/node/edge/pathway mapping was resolved. The module boundary is a "
        "dependency scope only and does not assert a graph edge, route, or causal mechanism."
    )
    return {
        "link_id": f"LINK:{observation['observation_id']}", "observation_id": observation["observation_id"],
        "mechanism_release_id": RELEASE_ID, "mechanism_target_kind": "module",
        "mechanism_target_key": "21B", "mechanism_route_id": "", "route_stage": "context",
        "link_role": "unresolved", "context_match": "unknown", "support_status": "unresolved",
        "release_status": "staging", "link_basis": unresolved,
        "source_field_locator": observation["source_locator"],
        "notes": "Unresolved mapping retained for review; no generic mechanism evidence copied into the SCI pack.",
    }


def count_values(rows: Iterable[dict[str, Any]], key: str) -> dict[str, int]:
    counter = Counter(str(row.get(key) or "unknown") for row in rows)
    return dict(sorted(counter.items()))


def metabolomics_assessment(db_path: Path, imported_ids: set[str]) -> dict[str, Any]:
    """Report metabolite-oriented records that were included or held out."""
    query = """
        SELECT po.observation_id, po.study_id, po.protein, po.assay, po.protein_form,
               po.measurement_kind, po.extraction_status, po.direction_vs_control,
               st.injury_model
        FROM protein_observations po
        JOIN studies st USING(study_id)
        ORDER BY po.observation_id
    """
    with sqlite3.connect(db_path) as db:
        db.row_factory = sqlite3.Row
        rows = [dict(row) for row in db.execute(query)]
    assessed = []
    for row in rows:
        if not nonempty_context(row.get("injury_model")):
            continue
        kind = metabolomics_candidate_kind(row)
        if not kind:
            continue
        oid = row["observation_id"]
        if oid in imported_ids:
            decision, reason = "included", "explicit SCI metabolite/lipid-mediator assay"
        elif "ambiguous" in (row.get("extraction_status") or ""):
            decision, reason = "excluded", "canonical queue record retains an assay/context mismatch; no assay remapping"
        elif "microdialysis" in (row.get("assay") or "").lower():
            decision, reason = "excluded", "dynamic metabolite release readout reserved for functional evidence"
        elif "fluorescence" in (row.get("assay") or "").lower() or "fret" in (row.get("measurement_kind") or "").lower():
            decision, reason = "excluded", "metabolite imaging readout reserved for imaging evidence"
        else:
            decision, reason = "excluded", "does not satisfy the direct metabolomics import rule"
        assessed.append({
            "observation_id": oid, "study_id": row.get("study_id"), "entity": row.get("protein"),
            "candidate_kind": kind, "assay": row.get("assay"), "measurement_kind": row.get("measurement_kind"),
            "extraction_status": row.get("extraction_status"),
            "decision": decision, "reason": reason,
        })
    return {
        "candidate_rows_assessed": len(assessed),
        "included_rows": sum(row["decision"] == "included" for row in assessed),
        "excluded_rows": sum(row["decision"] == "excluded" for row in assessed),
        "records": assessed,
    }


def build(mscs_root: Path, pack: Path, bundle: Path, curation_overrides_path: Path = DEFAULT_CURATION_OVERRIDES) -> dict[str, Any]:
    global DEFAULT_MSCS_ROOT
    DEFAULT_MSCS_ROOT = mscs_root
    protein_db = mscs_root / "data/flow_protein/flow_protein.sqlite"
    phospho_view = mscs_root / "data/derived/phosphorylation_support_observations.tsv"
    epigenetic_db = mscs_root / "data/epigenetic/epigenetic.sqlite"
    spatial_catalog = mscs_root / "data/spatial/spatial_catalog.sqlite"
    spatial_pilot = mscs_root / "data/spatial/pilot_all_studies/gse269377_cluster_proxy/spatial_pair_percentages_all_samples.tsv"
    downstream_evidence = bundle / "mechanism_downstream_evidence_records.tsv"
    for path in (protein_db, phospho_view, epigenetic_db, spatial_catalog, spatial_pilot, bundle / "mechanism_nodes.tsv", downstream_evidence, curation_overrides_path):
        if not path.exists():
            raise FileNotFoundError(path)

    protein_hash = sha256(protein_db)
    phospho_hash = sha256(phospho_view)
    epigenetic_hash = sha256(epigenetic_db)
    spatial_catalog_hash = sha256(spatial_catalog)
    spatial_pilot_hash = sha256(spatial_pilot)
    downstream_evidence_hash = sha256(downstream_evidence)
    curation_overrides_hash = sha256(curation_overrides_path)
    metabolomics_transcription_paths = {
        relative_path: mscs_root / relative_path
        for relative_path in sorted(set(METABOLOMICS_TRANSCRIPTION_ARTIFACTS.values()))
    }
    for path in metabolomics_transcription_paths.values():
        if not path.exists():
            raise FileNotFoundError(path)
    metabolomics_transcription_hashes = {
        relative_path: sha256(path) for relative_path, path in metabolomics_transcription_paths.items()
    }
    curation_overrides = load_curation_overrides(curation_overrides_path)
    selected = read_tsv(phospho_view)
    selected_ids = {row["observation_id"] for row in selected}
    metabolomics_contexts, metabolomics_meta, metabolomics_obs = metabolomics_rows(
        protein_db, protein_hash, curation_overrides, mscs_root,
    )
    metabolomics_ids = set(metabolomics_obs)
    protein_contexts, protein_meta, protein_obs = protein_context_rows(protein_db, selected_ids, protein_hash, curation_overrides)
    expression_contexts, expression_meta, expression_obs = protein_expression_rows(
        protein_db, selected_ids | metabolomics_ids, protein_hash, curation_overrides,
    )
    protein_context_by_id = {row["context_id"]: row for row in protein_contexts}
    for row in expression_contexts:
        protein_context_by_id.setdefault(row["context_id"], row)
    protein_contexts = list(protein_context_by_id.values())
    protein_meta.update(expression_meta)
    protein_obs.update(expression_obs)
    epi_contexts, epi_meta, epi_obs = epigenetic_rows(epigenetic_db, epigenetic_hash)
    transcriptomic_contexts, transcriptomic_meta, transcriptomic_obs, transcriptomic_assessment = transcriptomic_rows(
        spatial_catalog, spatial_catalog_hash, downstream_evidence, downstream_evidence_hash,
    )
    protein_context_ids = {item["context_id"] for item in protein_contexts}
    all_contexts = protein_contexts + [
        row for row in metabolomics_contexts if row["context_id"] not in protein_context_ids
    ] + [
        row for row in epi_contexts if row["context_id"] not in protein_context_ids
    ] + [
        row for row in transcriptomic_contexts if row["context_id"] not in protein_context_ids
    ]
    scope = {
        "context_id": "sci_scope", "context_name": "Spinal cord injury evidence scope",
        "context_kind": "ontology_scope", "disease_context": "spinal_cord_injury",
        "anatomical_context": "spinal_cord", "species": "", "injury_model": "",
        "injury_level": "", "timepoint_value": "", "timepoint_unit": "",
        "perturbation": "", "treatment": "", "cell_type": "", "sample_id": "",
        "experimental_condition": "", "study_perturbation_status": "",
        "injury_severity": "", "sex": "", "injury_distance": "",
        "injury_distance_unit": "", "sample_scope": "", "sample_count": "",
        "study_id": "", "tissue": "",
        "context_status": "defined", "provenance_note": "Scope-level context only; study/sample observations are listed separately.",
    }
    all_contexts = [scope] + all_contexts
    node_index = load_nodes(bundle)
    observations = list(protein_obs.values()) + list(metabolomics_obs.values()) + list(epi_obs.values()) + list(transcriptomic_obs.values())
    curation_counts = Counter(
        item["curation_id"]
        for observation in observations
        for item in [curation_provenance(observation)]
        if item
    )
    links = [link_for_observation(observation, node_index) for observation in observations]
    context_by_id = {row["context_id"]: row for row in all_contexts}
    for observation in observations:
        observation.pop("_gene_symbol", None)
        observation.pop("_entity", None)
        observation.pop("_context_meta", None)
        observation.pop("_context_curation", None)
        observation.pop("_study_key", None)
        observation.pop("_injury_model", None)
        observation.pop("_timepoint_key", None)
        observation.pop("_evidence_label", None)

    pack.mkdir(parents=True, exist_ok=True)
    write_tsv(pack / "contexts.tsv", CONTEXT_FIELDS, all_contexts)
    write_tsv(pack / "observations.tsv", OBSERVATION_FIELDS, observations)
    write_tsv(pack / "mechanism_links.tsv", LINK_FIELDS, links)

    enriched = []
    link_by_observation = {row["observation_id"]: row for row in links}
    meta_by_modality = {
        "protein": protein_meta, "metabolomics": metabolomics_meta, "epigenomics": epi_meta,
        "transcriptomics": transcriptomic_meta,
    }
    for original in list(protein_obs.values()) + list(metabolomics_obs.values()) + list(epi_obs.values()) + list(transcriptomic_obs.values()):
        row = dict(original)
        context = context_by_id[row["context_id"]]
        link = link_by_observation[row["observation_id"]]
        row.update({
            "study_id": meta_by_modality[row["modality"]][row["context_id"]]["study_id"],
            "injury_model": context["injury_model"], "timepoint_key": timepoint_label(context["timepoint_value"], context["timepoint_unit"]),
            "perturbation_key": context["perturbation"], "treatment_key": context["treatment"],
            "linked_status": "linked" if link["release_status"] == "included" else "unlinked",
            "unresolved_mapping_reason": "" if link["release_status"] == "included" else link["link_basis"],
        })
        enriched.append(row)

    metabolomics_audit = metabolomics_assessment(protein_db, metabolomics_ids)

    audit = {
        "audit_version": "sci_context_pack_audit_v1",
        "scope_rule": "Only source records with explicit spinal-cord, spinal-cord-injury, or injury-model context were selected; no generic mechanism evidence was copied.",
        "selected_evidence": {
            "protein_state_view_rows": len(selected),
            "protein_state_observations_imported": len(selected_ids),
            "protein_expression_candidate_rows": len(expression_obs),
            "protein_observations_imported": len(protein_obs),
            "metabolomics_candidate_rows_assessed": metabolomics_audit["candidate_rows_assessed"],
            "metabolomics_observations_imported": len(metabolomics_obs),
            "metabolomics_observations_excluded": metabolomics_audit["excluded_rows"],
            "epigenetic_observations_imported": len(epi_obs),
            "epigenetic_binary_feature_observations_imported": sum(
                observation["source_record_type"] == "epigenetic_binary_feature"
                for observation in epi_obs.values()
            ),
            "spatial_pilot_rows_assessed_but_excluded": 144,
            "spatial_exclusion_reason": "GSE269377 is a healthy/mutant FUS spinal-cord spatial dataset without an explicit spinal-cord-injury model; mSCS spatial_evidence has zero rows.",
            "transcriptomic_catalog_rows_assessed": transcriptomic_assessment["catalog_rows_assessed"],
            "transcriptomic_catalog_datasets_imported": transcriptomic_assessment["datasets_imported"],
            "transcriptomic_catalog_datasets_excluded": transcriptomic_assessment["datasets_excluded"],
            "transcriptomic_catalog_excluded_dataset_ids": transcriptomic_assessment["excluded_dataset_ids"],
            "transcriptomic_observation_rows_imported": len(transcriptomic_obs),
            "transcriptomic_context_annotation_rows_imported": sum(
                observation["evidence_role"] == "contextual_annotation" for observation in transcriptomic_obs.values()
            ),
            "transcriptomic_external_observation_rows_imported": sum(
                observation["evidence_role"] == "context_matched_external_observation" for observation in transcriptomic_obs.values()
            ),
            "transcriptomic_gene_level_matrix_rows_imported": 0,
            "transcriptomic_exclusion_reason": "Healthy/mutant FUS GSE269377 lacks explicit SCI; the human GSE305911 organoid record is related to the SCI study but is not injured spinal-cord tissue and is excluded from this injured-spinal-cord overlay.",
            "imaging_observation_rows_imported": 0,
            "perturbation_observation_rows_imported": 0,
            "functional_observation_rows_imported": 0,
            "context_curation_overrides_applied": len(curation_overrides),
            "observations_with_context_curation": sum(curation_counts.values()),
        },
        "source_artifacts": [
            {"path": "mSCS/data/flow_protein/flow_protein.sqlite", "sha256": protein_hash, "size_bytes": protein_db.stat().st_size},
            {"path": "mSCS/data/derived/phosphorylation_support_observations.tsv", "sha256": phospho_hash, "size_bytes": phospho_view.stat().st_size},
            {"path": "mSCS/data/epigenetic/epigenetic.sqlite", "sha256": epigenetic_hash, "size_bytes": epigenetic_db.stat().st_size},
            {"path": "mSCS/data/spatial/spatial_catalog.sqlite", "sha256": spatial_catalog_hash, "size_bytes": spatial_catalog.stat().st_size},
            {"path": "mSCS/data/spatial/pilot_all_studies/gse269377_cluster_proxy/spatial_pair_percentages_all_samples.tsv", "sha256": spatial_pilot_hash, "size_bytes": spatial_pilot.stat().st_size},
            {"path": str(downstream_evidence.relative_to(ROOT)), "sha256": downstream_evidence_hash, "size_bytes": downstream_evidence.stat().st_size},
            {"path": "context_packs/spinal_cord_injury/protein_context_curation_overrides.tsv", "sha256": curation_overrides_hash, "size_bytes": curation_overrides_path.stat().st_size},
            *[
                {"path": f"mSCS/{relative_path}", "sha256": digest, "size_bytes": metabolomics_transcription_paths[relative_path].stat().st_size}
                for relative_path, digest in metabolomics_transcription_hashes.items()
            ],
        ],
        "counts_by": {
            "modality": count_values(enriched, "modality"),
            "study": count_values(enriched, "study_id"),
            "injury_model": count_values(enriched, "injury_model"),
            "timepoint": count_values(enriched, "timepoint_key"),
            "perturbation": count_values(enriched, "perturbation_key"),
            "treatment": count_values(enriched, "treatment_key"),
            "observation_status": count_values(enriched, "observation_status"),
            "evidence_role": count_values(enriched, "evidence_role"),
            "linked_status": count_values(enriched, "linked_status"),
            "unresolved_mapping_reason": count_values([row for row in enriched if row["linked_status"] == "unlinked"], "unresolved_mapping_reason"),
            "context_curation": dict(sorted(curation_counts.items())),
        },
        "metabolomics_assessment": metabolomics_audit,
        "mechanism_link_counts": {
            "included": sum(row["release_status"] == "included" for row in links),
            "staging_unresolved": sum(row["release_status"] == "staging" for row in links),
            "graph_edges_created": 0,
            "partial_routes_promoted": 0,
            "numeric_modality_weights_created": 0,
            "route_confidence_created": 0,
        },
        "notes": [
            "Protein observations combine the 110-row mSCS phosphorylation-support selection with directly measured, source-extracted non-phosphorylated protein records; they are not the full 1,259-row canonical store.",
            "Epigenomics imports all explicitly reported assay contexts from the mSCS epigenetic store and retains exact binary feature-status records with their own source artifact paths and checksums; binary status is not converted into a directional comparison.",
            "Protein-expression selection excludes phosphoprotein/active-form duplicates, ambiguous or inaccessible extraction states, reporter/activity-only assays, and records without a measured value or reported direction.",
            "Metabolomics imports explicit ATP, anandamide, prostaglandin E2, and leukotriene B4 assay records from the canonical mSCS store; queue rows with assay mismatch, imaging, or dynamic-release endpoints remain excluded from this modality.",
            "Dependency groups are source/study/timepoint/population or source/study/assay/context groups; they are intended to prevent correlated readouts from being double-counted.",
            "Downstream protein and phosphoprotein measurements are linked only to the measured state/node when an exact stable node match exists; no upstream ligand/receptor causality is inferred.",
            "Missing values and source ambiguity remain unreported or unknown; they are not converted to negative protein evidence.",
            "Transcriptomic context annotations are imported from explicit SCI-related spatial-catalog records, with capture-level or reported timepoint context retained where available; gene/spot-level matrix values are reserved for a later spatial release.",
            "The two external transcriptomic observations are the exact SCI qRT-PCR records M21B-DOWNSTREAM-EVID:004631 and M21B-DOWNSTREAM-EVID:004632 from the pinned mechanism release. Their source records do not provide an exact stable mechanism-node identifier, so both remain staged and do not establish upstream causality.",
        ],
    }
    (pack / "audit_report.json").write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    manifest = {
        "context_pack_id": "spinal_cord_injury",
        "context_pack_version": CONTEXT_PACK_VERSION,
        "status": "populated",
        "pack_type": "disease_injury_evidence_overlay",
        "source_repo": "mSCIdblit",
        "target_consumer": "mSCS",
        "scope": {
            "disease_context": "spinal_cord_injury", "anatomical_context": "spinal_cord",
            "study_level_fields_required_when_reported": ["study_id", "species", "tissue", "injury_model", "injury_severity", "injury_level", "sex", "timepoint", "injury_distance", "sample_scope", "perturbation", "treatment", "experimental_condition", "study_perturbation_status", "cell_type", "sample_id"],
        },
        "mechanism_dependency": {
            "release_id": RELEASE_ID, "release_tag": RELEASE_TAG,
            "bundle_metadata": "../../data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627/bundle_metadata.json",
            "generic_graph_is_unchanged": True, "context_links_are_not_graph_edges": True,
        },
        "evidence_policy": {
            "context_attaches_to": "observation_or_reviewed_mechanism_link",
            "not_measured_is_not_negative": True, "source_dependency_groups_required": True,
            "route_confidence_stored": False, "numeric_modality_weights_stored": False,
            "mSCS_evaluates_route_plausibility": True,
        },
        "modalities": [
            {"modality": "protein", "status": "populated", "selection": "mSCS phosphorylation_support_observations.tsv plus direct source-extracted non-phosphorylated protein observations from flow_protein.sqlite", "observation_file": "observations.tsv"},
            {"modality": "metabolomics", "status": "populated", "selection": "Explicit SCI metabolite/lipid-mediator assay records from mSCS flow_protein.sqlite, with exact transcription artifacts retained in provenance", "observation_file": "observations.tsv"},
            {"modality": "transcriptomics", "status": "populated", "selection": "Explicit SCI-context external qRT-PCR observations plus SCI-related spatial-transcriptomic dataset context annotations; no gene-level matrix values are imported.", "observation_file": "observations.tsv"},
            {"modality": "spatial", "status": "context_annotations_only", "reason": "Spatial transcriptomic datasets are represented as transcriptomic contextual annotations; spot/gene-level spatial evidence remains reserved for a later spatial release."},
            {"modality": "epigenomics", "status": "populated", "selection": "mSCS epigenetic observations, all explicit assay contexts, and exact binary feature-status records", "observation_file": "observations.tsv"},
            {"modality": "imaging", "status": "represented_as_protein_assay_context", "reason": "Immunofluorescence observations remain protein observations; no separate imaging claim is created."},
            {"modality": "perturbation", "status": "represented_in_context_fields", "reason": "Perturbation and treatment fields are preserved when reported; no intervention-only observation is fabricated."},
            {"modality": "functional", "status": "assessed_not_imported", "reason": "No standalone functional observation table was selected for this release."},
        ],
        "artifacts": {
            "contexts": "contexts.tsv", "observations": "observations.tsv",
            "mechanism_links": "mechanism_links.tsv", "audit_report": "audit_report.json",
            "protein_context_coverage": "protein_context_coverage.tsv",
            "protein_context_gap_audit": "protein_context_gap_audit.json",
            "protein_context_gap_candidates": "protein_context_gap_candidates.tsv",
            "protein_context_curation_overrides": "protein_context_curation_overrides.tsv",
        },
        "counts": {
            "context_profiles": len(all_contexts), "observations": len(observations),
            "mechanism_links": len(links), "included_mechanism_links": sum(row["release_status"] == "included" for row in links),
        },
        "provenance_note": "Generated by scripts/build_sci_context_pack.py from exact mSCS source artifacts, the pinned mechanism-release downstream evidence table, and explicitly applied context curation overrides. Transcriptomic catalog records are contextual annotations only; gene/spot-level matrix values are not imported. Generic Module 20B-24B graph files were read for stable identifier resolution only and were not modified or duplicated.",
    }
    (pack / "context_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"manifest": manifest, "audit": audit}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mscs-root", type=Path, default=DEFAULT_MSCS_ROOT)
    parser.add_argument("--pack", type=Path, default=DEFAULT_PACK)
    parser.add_argument("--bundle", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--curation-overrides", type=Path, default=DEFAULT_CURATION_OVERRIDES)
    args = parser.parse_args()
    result = build(args.mscs_root, args.pack, args.bundle, args.curation_overrides)
    print(json.dumps({"counts": result["manifest"]["counts"], "audit": result["audit"]["selected_evidence"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
