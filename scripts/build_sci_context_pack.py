#!/usr/bin/env python3
"""Build the populated spinal-cord-injury context evidence overlay.

The builder reads the current mSCS protein-state support view and the curated
mSCS epigenetic SQLite store.  It writes only the file-based context pack; it
does not modify mSCS or the neutral Module 20B-24B mechanism bundle.

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
DEFAULT_CURATION_OVERRIDES = DEFAULT_PACK / "protein_context_curation_overrides.tsv"

CURATION_OVERRIDE_FIELDS = {
    "injury_model", "injury_level", "injury_severity", "sex",
    "perturbation_status", "condition", "sample_scope",
    "timepoint_value", "timepoint_unit",
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


def epigenetic_rows(db_path: Path, artifact_hash: str) -> tuple[list[dict[str, str]], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    contexts: dict[str, dict[str, str]] = {}
    context_meta: dict[str, dict[str, Any]] = {}
    observations: dict[str, dict[str, Any]] = {}
    query = """
        SELECT o.*, a.assay_name, a.epigenetic_class, a.target AS assay_target,
               a.directness, a.evidence_scope, a.evidence_level,
               c.condition, c.post_injury_value, c.post_injury_unit, c.tissue,
               c.tissue_region, c.cell_type, c.replicate_count, c.sample_unit,
               s.study_id, s.title AS study_title, s.species, s.injury_model,
               s.injury_level, s.pmid, s.doi, s.curation_status,
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
        context_id = stable_id("sci:epigenetic", row["study_id"], row["context_id"] or row["assay_id"])
        sample_id = row.get("sample_unit") or ""
        context_cell = row.get("cell_type") or ""
        contexts.setdefault(context_id, {
            "context_id": context_id,
            "context_name": f"{row['study_id']} epigenetic context at {timepoint_label(row.get('post_injury_value'), row.get('post_injury_unit'))}",
            "context_kind": "sample_context" if sample_id or context_cell else "study_context",
            "disease_context": "spinal_cord_injury", "anatomical_context": "spinal_cord",
            "species": row.get("species") or "", "injury_model": row.get("injury_model") or "",
            "injury_level": row.get("injury_level") or "",
            "injury_severity": "", "sex": "",
            "timepoint_value": display_timepoint(row.get("post_injury_value")),
            "timepoint_unit": row.get("post_injury_unit") or "",
            "perturbation": row.get("condition") or "", "treatment": "",
            "experimental_condition": row.get("condition") or "",
            "study_perturbation_status": row.get("condition") or "",
            "injury_distance": "", "injury_distance_unit": "",
            "sample_scope": "", "sample_count": row.get("replicate_count"),
            "cell_type": context_cell, "sample_id": sample_id,
            "study_id": row["study_id"], "tissue": row.get("tissue_region") or row.get("tissue") or "",
            "context_status": "defined",
            "provenance_note": source_locator(
                "mSCS/data/epigenetic/epigenetic.sqlite",
                f"studies.study_id={row['study_id']}",
                f"assays.assay_id={row['assay_id']}",
                f"assay_contexts.context_id={row['context_id']}",
                f"study_title={row['study_title']}",
            ),
        })
        context_meta.setdefault(context_id, {
            "study_id": row["study_id"], "study_title": row["study_title"],
            "species": row["species"], "injury_model": row["injury_model"],
            "injury_level": row["injury_level"], "timepoint_id": row["context_id"],
            "condition": row["condition"], "source_location": row["source_location"],
        })
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
            "perturbation": row.get("condition"), "cell_type": context_cell, "sample_id": sample_id,
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
                "source_location": row.get("source_location"), "notes": row.get("notes"),
            }),
            "_gene_symbol": row.get("gene_symbol"), "_entity": feature_name,
            "_context_meta": context_meta[context_id], "_study_key": row["study_id"],
            "_injury_model": row.get("injury_model") or "unknown",
            "_timepoint_key": timepoint_label(row.get("post_injury_value"), row.get("post_injury_unit")),
            "_evidence_label": f"{row.get('epigenetic_class')}:{row.get('directness')}:{row.get('evidence_level')}",
        }
    return list(contexts.values()), context_meta, observations


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


def build(mscs_root: Path, pack: Path, bundle: Path, curation_overrides_path: Path = DEFAULT_CURATION_OVERRIDES) -> dict[str, Any]:
    global DEFAULT_MSCS_ROOT
    DEFAULT_MSCS_ROOT = mscs_root
    protein_db = mscs_root / "data/flow_protein/flow_protein.sqlite"
    phospho_view = mscs_root / "data/derived/phosphorylation_support_observations.tsv"
    epigenetic_db = mscs_root / "data/epigenetic/epigenetic.sqlite"
    spatial_catalog = mscs_root / "data/spatial/spatial_catalog.sqlite"
    spatial_pilot = mscs_root / "data/spatial/pilot_all_studies/gse269377_cluster_proxy/spatial_pair_percentages_all_samples.tsv"
    for path in (protein_db, phospho_view, epigenetic_db, spatial_catalog, spatial_pilot, bundle / "mechanism_nodes.tsv", curation_overrides_path):
        if not path.exists():
            raise FileNotFoundError(path)

    protein_hash = sha256(protein_db)
    phospho_hash = sha256(phospho_view)
    epigenetic_hash = sha256(epigenetic_db)
    spatial_catalog_hash = sha256(spatial_catalog)
    spatial_pilot_hash = sha256(spatial_pilot)
    curation_overrides_hash = sha256(curation_overrides_path)
    curation_overrides = load_curation_overrides(curation_overrides_path)
    selected = read_tsv(phospho_view)
    selected_ids = {row["observation_id"] for row in selected}
    protein_contexts, protein_meta, protein_obs = protein_context_rows(protein_db, selected_ids, protein_hash, curation_overrides)
    expression_contexts, expression_meta, expression_obs = protein_expression_rows(protein_db, selected_ids, protein_hash, curation_overrides)
    protein_context_by_id = {row["context_id"]: row for row in protein_contexts}
    for row in expression_contexts:
        protein_context_by_id.setdefault(row["context_id"], row)
    protein_contexts = list(protein_context_by_id.values())
    protein_meta.update(expression_meta)
    protein_obs.update(expression_obs)
    epi_contexts, epi_meta, epi_obs = epigenetic_rows(epigenetic_db, epigenetic_hash)
    all_contexts = protein_contexts + [row for row in epi_contexts if row["context_id"] not in {item["context_id"] for item in protein_contexts}]
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
    observations = list(protein_obs.values()) + list(epi_obs.values())
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
    for original in list(protein_obs.values()) + list(epi_obs.values()):
        row = dict(original)
        context = context_by_id[row["context_id"]]
        link = link_by_observation[row["observation_id"]]
        row.update({
            "study_id": (protein_meta if row["modality"] == "protein" else epi_meta)[row["context_id"]]["study_id"],
            "injury_model": context["injury_model"], "timepoint_key": timepoint_label(context["timepoint_value"], context["timepoint_unit"]),
            "perturbation_key": context["perturbation"], "linked_status": "linked" if link["release_status"] == "included" else "unlinked",
            "unresolved_mapping_reason": "" if link["release_status"] == "included" else link["link_basis"],
        })
        enriched.append(row)

    audit = {
        "audit_version": "sci_context_pack_audit_v1",
        "scope_rule": "Only source records with explicit spinal-cord, spinal-cord-injury, or injury-model context were selected; no generic mechanism evidence was copied.",
        "selected_evidence": {
            "protein_state_view_rows": len(selected),
            "protein_state_observations_imported": len(selected_ids),
            "protein_expression_candidate_rows": len(expression_obs),
            "protein_observations_imported": len(protein_obs),
            "epigenetic_observations_imported": len(epi_obs),
            "spatial_pilot_rows_assessed_but_excluded": 144,
            "spatial_exclusion_reason": "GSE269377 is a healthy/mutant FUS spinal-cord spatial dataset without an explicit spinal-cord-injury model; mSCS spatial_evidence has zero rows.",
            "transcriptomic_observation_rows_imported": 0,
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
            {"path": "context_packs/spinal_cord_injury/protein_context_curation_overrides.tsv", "sha256": curation_overrides_hash, "size_bytes": curation_overrides_path.stat().st_size},
        ],
        "counts_by": {
            "modality": count_values(enriched, "modality"),
            "study": count_values(enriched, "study_id"),
            "injury_model": count_values(enriched, "injury_model"),
            "timepoint": count_values(enriched, "timepoint_key"),
            "perturbation": count_values(enriched, "perturbation_key"),
            "observation_status": count_values(enriched, "observation_status"),
            "evidence_role": count_values(enriched, "evidence_role"),
            "linked_status": count_values(enriched, "linked_status"),
            "unresolved_mapping_reason": count_values([row for row in enriched if row["linked_status"] == "unlinked"], "unresolved_mapping_reason"),
            "context_curation": dict(sorted(curation_counts.items())),
        },
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
            "Protein-expression selection excludes phosphoprotein/active-form duplicates, ambiguous or inaccessible extraction states, reporter/activity-only assays, and records without a measured value or reported direction.",
            "Dependency groups are source/study/timepoint/population or source/study/assay/context groups; they are intended to prevent correlated readouts from being double-counted.",
            "Downstream protein and phosphoprotein measurements are linked only to the measured state/node when an exact stable node match exists; no upstream ligand/receptor causality is inferred.",
            "Missing values and source ambiguity remain unreported or unknown; they are not converted to negative protein evidence.",
        ],
    }
    (pack / "audit_report.json").write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    manifest = {
        "context_pack_id": "spinal_cord_injury",
        "context_pack_version": "0.5.16",
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
            {"modality": "transcriptomics", "status": "assessed_not_imported", "reason": "No curated transcriptomic observation table with exact SCI context was selected in this release."},
            {"modality": "spatial", "status": "assessed_excluded", "reason": audit["selected_evidence"]["spatial_exclusion_reason"]},
            {"modality": "epigenomics", "status": "populated", "observation_file": "observations.tsv"},
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
        "provenance_note": "Generated by scripts/build_sci_context_pack.py from exact mSCS source artifacts plus explicitly applied protein context curation overrides. Generic Module 20B-24B graph files were read for stable identifier resolution only and were not modified or duplicated.",
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
