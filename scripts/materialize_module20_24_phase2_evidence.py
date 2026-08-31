#!/usr/bin/env python3
"""Generate canonical Paper/Experiment/Observation/Claim/Link SQL.

The Phase-2 packet contains validated atomic observations and claims, but it
does not always preserve the publication's original experiment number. This
materializer therefore creates explicitly labelled *source-defined evidence
units* only for rows that pass conservative text/status gates. It never calls
those units original paper experiment IDs, and it leaves all other rows in
staging.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from materialize_module20_24_paper_provenance import bioc_records, html_records, sql, xml_records


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
PHASE2 = REVIEW_ROOT / "module20_24_integrated_phase2_extractions.tsv"
LEDGER = REVIEW_ROOT / "module20_24_evidence_grade_ledger.tsv"
OUT_SQL = REVIEW_ROOT / "module20_24_phase2_evidence_materialization.sql"
REPORT = REVIEW_ROOT / "module20_24_phase2_evidence_materialization.md"
METADATA = ROOT / "work" / "cross_module_synthesis" / "module20_24_canonical_paper_metadata.tsv"
IDENTITY = REVIEW_ROOT / "module20_24_phase2_paper_identity_resolution.tsv"
MODULES = ("20B", "21B", "22B", "23B", "24B")
# These five reviewed records explicitly reject promotion of the queued exact
# edge. Keep their evaluated observations and claims, but never treat them as
# positive support for that edge. The IDs are taken from the Phase-2 review
# packet; no text-only heuristic is used for this boundary classification.
BOUNDARY_ONLY_EVIDENCE_IDS = frozenset({
    "M20B-EVID-002177",
    "M20B-EVID-002204",
    "M20B-EVID-002899",
    "M20B-EVID-003366",
    "M24B-EVID-000105",
})


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def identity_records() -> dict[str, dict[str, str]]:
    """Load exact per-extraction paper identity resolutions."""
    return {
        row["extraction_id"]: row
        for row in read_tsv(IDENTITY)
        if row.get("extraction_id")
    }


def json_text(payload: dict[str, object]) -> str:
    return json.dumps(payload, sort_keys=True)


def json_sql(payload: dict[str, object]) -> str:
    return sql(json_text(payload))


def pmids(value: str) -> list[str]:
    return sorted(set(re.findall(r"\bPMID:(\d+)\b", value or "", flags=re.I)))


def useful(value: str) -> bool:
    normalized = (value or "").strip().lower()
    return bool(normalized) and normalized not in {
        "not located", "not verified", "not available", "not applicable",
        "not specified", "not specified at atomic experiment level", "unresolved",
    }


def valid_observation(row: dict[str, str]) -> bool:
    status = row.get("observation_status", "").lower()
    value = row.get("observation_value_or_blocker", "")
    if not status.startswith("validated"):
        return False
    if any(token in status for token in ("abstract", "metadata", "unresolved", "boundary", "not_required", "no_pair")):
        return False
    return useful(value) and len(value.strip()) >= 40 and "do_not_create" not in value.lower()


def valid_claim(row: dict[str, str]) -> bool:
    status = row.get("claim_status", "").lower()
    value = row.get("claim_text_or_blocker", "")
    if not status.startswith("validated"):
        return False
    if any(token in status for token in ("abstract", "metadata", "unresolved", "boundary", "not_required", "no_pair", "unknown")):
        return False
    if value.strip().startswith("M21B-C-") or value.strip().startswith("M22B-C-"):
        return False
    return useful(value) and len(value.strip()) >= 40 and "do_not_create" not in value.lower()


def boundary_only_claim(row: dict[str, str]) -> bool:
    """Identify reviewed text that explicitly does not support the queued edge."""
    return row.get("b_evidence_id", "") in BOUNDARY_ONLY_EVIDENCE_IDS


def outcome_type(row: dict[str, str]) -> tuple[str, str]:
    text = " ".join(row.get(k, "") for k in ("observation_value_or_blocker", "observation_source_section", "observation_assay", "claim_text_or_blocker")).lower()
    if any(token in text for token in ("spinal cord injury", "spinal-cord injury", "after sci", "acute sci", "mouse sci", "rat sci", "locomotor recovery", "lesion")):
        return "spinal_cord_injury_outcome", "The extracted evidence text explicitly includes spinal-cord injury or lesion outcome context."
    if any(token in text for token in ("promoter", "transcription", "gene expression", "transcription factor", "chromatin", "occupancy", "reporter")):
        return "transcriptional_regulatory_output", "The extracted evidence text includes a transcriptional or regulatory output."
    if any(token in text for token in ("proliferation", "migration", "neurite", "apoptosis", "inflammation", "functional recovery", "behavior", "scar", "differentiation")):
        return "cellular_functional_output", "The extracted evidence text includes a cellular or functional output."
    return "molecular_signaling_output", "The extracted evidence text is molecular/signaling-focused without a more specific output category."


def normalize_species(value: str) -> str:
    value = value.lower()
    mouse = "mouse" in value
    human = "human" in value
    if mouse and human:
        return "mixed"
    if mouse:
        return "mouse"
    if human:
        return "human"
    return "not_applicable"


def normalize_scope(value: str) -> str:
    value = value.lower()
    if "negative" in value:
        return "negative_evidence"
    if "direct" in value:
        return "direct_edge"
    if "pathway" in value:
        return "pathway_membership"
    return "contextual_support"


def normalize_support(value: str) -> str:
    value = value.lower()
    if "database" in value:
        return "database_curated"
    if "review" in value:
        return "review_statement"
    if "primary" in value or "experiment" in value:
        return "primary_experiment"
    return "manual_background"


def normalize_confidence(value: str) -> str:
    value = value.strip().lower()
    return value if value in {"high", "medium", "low"} else "uncertain"


def db_text(value: str, limit: int) -> str:
    """Fit a SQL_ASCII display column while retaining full source text."""
    value = value or ""
    encoded = value.encode("utf-8")
    if len(encoded) <= limit:
        return value
    # PostgreSQL SQL_ASCII counts stored bytes for varchar limits. Keep the
    # truncation marker ASCII and decode only on a character boundary.
    prefix = encoded[: max(0, limit - 3)].decode("utf-8", errors="ignore")
    return prefix + "..."


def note_match(column: str, extraction_id: str) -> str:
    """Match a canonical row by stable batch/extraction identity, not mutable grading."""
    return (
        f"{column} LIKE {sql('%\"canonicalization_batch\": \"module20_24_phase2\"%')}"
        f" AND {column} LIKE {sql('%\"extraction_id\": \"' + extraction_id + '\"%')}"
    )


def main() -> None:
    phase2 = read_tsv(PHASE2)
    ledger = {row["b_evidence_id"]: row for row in read_tsv(LEDGER)}
    identities = identity_records()
    identity_manifest_present = IDENTITY.exists()
    available_pmids = set(xml_records())
    available_pmids.update(html_records())
    available_pmids.update(bioc_records())
    if METADATA.exists():
        available_pmids.update(row["pmid"] for row in read_tsv(METADATA) if row.get("paper_ready") == "true" and row.get("pmid"))
    # HTML/JSON/TSV source artifacts can carry exact bibliographic metadata
    # without being PubMed XML. The identity manifest is allowed to extend
    # the paper gate only when it contains both a resolved PMID and a title.
    available_pmids.update(
        row["resolved_pmid"]
        for row in identities.values()
        if row.get("resolved_pmid") and row.get("source_metadata_title")
    )

    candidates: list[dict[str, str]] = []
    for row in phase2:
        identity = identities.get(row.get("extraction_id", ""), {})
        resolved = identity.get("resolved_pmid", "")
        if resolved and resolved in available_pmids:
            stable = [resolved]
        elif not identity_manifest_present:
            # Preserve the pre-bridge behavior only when the resolver has not
            # been run. Once the manifest exists, an explicit unresolved or
            # ambiguous result must remain staged rather than being silently
            # re-admitted through a legacy PMID key.
            stable = [pmid for pmid in pmids(row.get("canonical_paper_key", "")) if pmid in available_pmids]
        else:
            stable = []
        if not stable or not valid_observation(row) or not valid_claim(row):
            continue
        grading = ledger.get(row["b_evidence_id"], {})
        candidate = dict(row)
        candidate["pmid"] = stable[0]
        candidate["identity_resolution_status"] = identity.get("identity_resolution_status", "legacy_canonical_key")
        candidate["identity_resolution_basis"] = identity.get("resolution_basis", "legacy canonical PMID resolution")
        candidate["identity_authoritative_source"] = identity.get("authoritative_source", "canonical_paper_key")
        candidate["evidence_grade"] = grading.get("evidence_grade", "")
        candidate["context_level"] = grading.get("context_level", "")
        candidate["grading_basis"] = grading.get("grading_basis", "")
        candidate["context_basis"] = grading.get("context_basis", "")
        candidate["citation_note"] = grading.get("citation_note", "")
        candidate["support_kind"] = grading.get("support_kind", "")
        candidate["source_scope"] = grading.get("source_scope", "")
        candidate["species_support"] = grading.get("species_support", "")
        candidate["outcome_type"], candidate["outcome_basis"] = outcome_type(row)
        candidate["edge_support_status"] = "boundary_not_supporting_requested_edge" if boundary_only_claim(row) else "supports_requested_edge"
        if candidate["edge_support_status"] == "boundary_not_supporting_requested_edge":
            candidate["evidence_grade"] = "E"
            candidate["context_level"] = "L0"
            candidate["grading_basis"] = (
                "The reviewed claim explicitly rejects promotion of the requested exact edge; "
                "retain the source-defined observation as bounded negative/context evidence only."
            )
            candidate["context_basis"] = "The reviewed claim does not establish the requested exact relationship or SCI-context transfer."
        if not candidate["evidence_grade"]:
            candidate["evidence_grade"] = "U"
            candidate["grading_basis"] = "No final A-E grade is assigned in the current ledger; retained as U until source adjudication is complete."
        candidates.append(candidate)

    papers = sorted({row["pmid"] for row in candidates})
    paradigm_name = "Module 20-24 source-defined evidence extraction"
    lines = [
        "-- Module 20B-24B Phase-2 canonical evidence materialization.",
        "-- Experiments are explicitly source-defined evidence units when the",
        "-- packet does not identify an original publication experiment number.",
        "-- Rows failing stable-paper, validated-observation, or validated-claim",
        "-- gates remain in staging and are not silently synthesized.",
        "BEGIN;",
        "",
        "CREATE TEMP TABLE m2024_phase2_candidates (extraction_id TEXT PRIMARY KEY);",
        "CREATE TEMP TABLE m2024_phase2_experiments (extraction_id TEXT PRIMARY KEY, experiment_id BIGINT NOT NULL);",
        "CREATE TEMP TABLE m2024_phase2_observations (extraction_id TEXT PRIMARY KEY, observation_id BIGINT NOT NULL);",
        "CREATE TEMP TABLE m2024_phase2_claims (extraction_id TEXT PRIMARY KEY, claim_id BIGINT NOT NULL);",
        "UPDATE AuthorClaim SET claim_type='curated_evidence_claim', notes=replace(notes, '\"record_type\": \"canonical_author_claim\"', '\"record_type\": \"canonical_claim\"') WHERE claim_type='source_author_claim' AND notes LIKE '%\"canonicalization_batch\": \"module20_24_phase2\"%';",
        "",
    ]

    if candidates:
        lines.extend([
            "INSERT INTO m2024_phase2_candidates (extraction_id) VALUES",
            ",\n".join(f"  ({sql(row['extraction_id'])})" for row in candidates) + ";",
            "",
            "-- Remove only stale rows previously created by this exact bridge batch.",
            "DELETE FROM SignalingEdgeSource s",
            "WHERE s.notes LIKE '%\"canonicalization_batch\": \"module20_24_phase2\"%'",
            "  AND COALESCE(substring(s.notes FROM '\"extraction_id\": \"([^\"]+)\"'), '') NOT IN (SELECT extraction_id FROM m2024_phase2_candidates);",
            "DELETE FROM EvidenceLink l",
            "WHERE l.notes LIKE '%\"canonicalization_batch\": \"module20_24_phase2\"%'",
            "  AND COALESCE(substring(l.notes FROM '\"extraction_id\": \"([^\"]+)\"'), '') NOT IN (SELECT extraction_id FROM m2024_phase2_candidates);",
            "-- AuthorClaim and Observation rows are retained as immutable audit records.",
            "-- Their EvidenceLink and SignalingEdgeSource rows are the promotion gate.",
            "DELETE FROM Experiment e",
            "WHERE e.notes LIKE '%\"canonicalization_batch\": \"module20_24_phase2\"%'",
            "  AND COALESCE(substring(e.notes FROM '\"extraction_id\": \"([^\"]+)\"'), '') NOT IN (SELECT extraction_id FROM m2024_phase2_candidates)",
            "  AND NOT EXISTS (SELECT 1 FROM Observation o WHERE o.experiment_id=e.experiment_id);",
            "-- If an overlapping run left duplicate source-defined experiments, retain",
            "-- the one with observations and then the lowest stable database ID.",
            "WITH ranked AS (",
            "  SELECT e.experiment_id,",
            "         row_number() OVER (",
            "           PARTITION BY substring(e.notes FROM '\"extraction_id\": \"([^\"]+)\"')",
            "           ORDER BY (EXISTS (SELECT 1 FROM Observation o WHERE o.experiment_id=e.experiment_id)) DESC, e.experiment_id",
            "         ) AS rn",
            "  FROM Experiment e",
            "  WHERE e.notes LIKE '%\"canonicalization_batch\": \"module20_24_phase2\"%'",
            ")",
            "DELETE FROM Experiment e USING ranked r",
            "WHERE e.experiment_id=r.experiment_id AND r.rn>1",
            "  AND NOT EXISTS (SELECT 1 FROM Observation o WHERE o.experiment_id=e.experiment_id);",
            "DELETE FROM ExperimentalParadigm ep",
            "WHERE ep.paradigm_name='Module 20-24 source-defined evidence extraction'",
            "  AND NOT EXISTS (SELECT 1 FROM Experiment e WHERE e.paradigm_id=ep.paradigm_id);",
            "",
        ])

    for pmid in papers:
        lines.extend([
            "INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)",
            "SELECT p.paper_id,",
            f"  {sql(paradigm_name)},",
            f"  {sql('Curated Module 20-24 normalization of exact Phase-2 source evidence; this is a curation paradigm, not a claim about the publication protocol.')},",
            f"  {sql('Phase-2 paper/observation/claim extraction with explicit source-defined evidence-unit labeling.')}",
            "FROM Paper p",
            f"WHERE p.pmid = {sql('PMID:' + pmid)}",
            "  AND NOT EXISTS (SELECT 1 FROM ExperimentalParadigm ep WHERE ep.paper_id=p.paper_id AND ep.paradigm_name=" + sql(paradigm_name) + ");",
            "",
        ])

    evidence_layers = sorted({row["evidence_layer"] for row in candidates})
    for layer in evidence_layers:
        lines.extend([
            "INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description)",
            f"VALUES ({sql(layer)}, {sql('Module 20-24 evidence layer retained from the reviewed B-layer register: ' + layer + '.')})",
            "ON CONFLICT (evidence_type_name) DO NOTHING;",
            "",
        ])
    outcome_types = sorted({row["outcome_type"] for row in candidates})
    outcome_descriptions = {
        "molecular_signaling_output": "Molecular or receptor-proximal signaling result extracted from the source packet.",
        "cellular_functional_output": "Cellular, tissue, or functional result extracted from the source packet.",
        "transcriptional_regulatory_output": "Transcriptional or regulatory result extracted from the source packet.",
        "spinal_cord_injury_outcome": "Spinal-cord injury or lesion-associated result extracted from the source packet.",
    }
    for outcome in outcome_types:
        lines.extend([
            "INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description)",
            f"VALUES ({sql(outcome)}, {sql(outcome_descriptions[outcome])})",
            "ON CONFLICT (outcome_type_name) DO NOTHING;",
            "",
        ])

    for row in candidates:
        experiment_note = {
            "canonicalization_batch": "module20_24_phase2",
            "extraction_id": row["extraction_id"],
            "module": row["module"],
            "b_edge_id": row["b_edge_id"],
            "b_evidence_id": row["b_evidence_id"],
            "canonical_paper_key": row["canonical_paper_key"],
            "pmid": row["pmid"],
            "identity_resolution_status": row.get("identity_resolution_status", "legacy_canonical_key"),
            "identity_resolution_basis": row.get("identity_resolution_basis", "legacy canonical PMID resolution"),
            "identity_authoritative_source": row.get("identity_authoritative_source", "canonical_paper_key"),
            "experiment_identity_status": "source_defined_evidence_unit; original_publication_experiment_number_not_separately_preserved",
            "source_locator": row["source_locator"],
            "source_section": row["observation_source_section"],
            "figure_or_table": row["observation_figure_or_table"],
            "species": row["observation_species"],
            "cell_or_model": row["observation_cell_or_model"],
            "assay": row["observation_assay"],
            "perturbation": row["observation_perturbation"],
            "evidence_grade": row["evidence_grade"],
            "context_level": row["context_level"],
        }
        observation_note = dict(experiment_note)
        observation_note.update({"record_type": "canonical_boundary_observation" if row["edge_support_status"] == "boundary_not_supporting_requested_edge" else "canonical_observation", "context_basis": row["context_basis"], "full_observation_value": row["observation_value_or_blocker"]})
        claim_note = dict(experiment_note)
        claim_note.update({"record_type": "canonical_boundary_claim" if row["edge_support_status"] == "boundary_not_supporting_requested_edge" else "canonical_author_claim", "context_basis": row["context_basis"]})
        link_note = dict(experiment_note)
        link_note.update({"record_type": "canonical_evidence_link"})
        source_note = dict(experiment_note)
        source_note.update({"record_type": "canonical_edge_boundary" if row["edge_support_status"] == "boundary_not_supporting_requested_edge" else "canonical_edge_source", "register_source_locator": row["source_locator"], "edge_support_status": row["edge_support_status"]})
        description = " | ".join(part for part in (
            "Source-defined evidence unit; original experiment number not separately preserved in Phase-2.",
            "model=" + row["observation_cell_or_model"],
            "assay=" + row["observation_assay"],
            "perturbation=" + row["observation_perturbation"],
            "source_section=" + row["observation_source_section"],
        ) if part and part.split("=", 1)[-1].strip())
        lines.extend([
            "UPDATE Experiment e",
            "SET paper_id=p.paper_id,",
            "    notes=regexp_replace(e.notes, '\"pmid\": \"[0-9]+\"', '\"pmid\": \"" + row["pmid"] + "\"')",
            "FROM Paper p",
            "WHERE p.pmid=" + sql("PMID:" + row["pmid"]) + " AND " + note_match("e.notes", row["extraction_id"]) + ";",
            "",
            "INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes)",
            "SELECT p.paper_id, ep.paradigm_id, NULL,",
            f"  {sql(db_text(row['observation_figure_or_table'], 100))}, {sql('Source-defined evidence unit ' + row['extraction_id'])},",
            f"  {sql(description)}, {sql(json_text(experiment_note))}",
            "FROM Paper p JOIN ExperimentalParadigm ep ON ep.paper_id=p.paper_id AND ep.paradigm_name=" + sql(paradigm_name),
            f"WHERE p.pmid={sql('PMID:' + row['pmid'])}",
            f"  AND NOT EXISTS (SELECT 1 FROM Experiment e WHERE {note_match('e.notes', row['extraction_id'])});",
            "",
        ])

    for row in candidates:
        experiment_note = {
            "canonicalization_batch": "module20_24_phase2",
            "extraction_id": row["extraction_id"],
            "module": row["module"],
            "b_edge_id": row["b_edge_id"],
            "b_evidence_id": row["b_evidence_id"],
            "canonical_paper_key": row["canonical_paper_key"],
            "pmid": row["pmid"],
            "identity_resolution_status": row.get("identity_resolution_status", "legacy_canonical_key"),
            "identity_resolution_basis": row.get("identity_resolution_basis", "legacy canonical PMID resolution"),
            "identity_authoritative_source": row.get("identity_authoritative_source", "canonical_paper_key"),
            "experiment_identity_status": "source_defined_evidence_unit; original_publication_experiment_number_not_separately_preserved",
            "source_locator": row["source_locator"],
            "source_section": row["observation_source_section"],
            "figure_or_table": row["observation_figure_or_table"],
            "species": row["observation_species"],
            "cell_or_model": row["observation_cell_or_model"],
            "assay": row["observation_assay"],
            "perturbation": row["observation_perturbation"],
            "evidence_grade": row["evidence_grade"],
            "context_level": row["context_level"],
        }
        obs_note = dict(experiment_note)
        obs_note.update({"record_type": "canonical_boundary_observation" if row["edge_support_status"] == "boundary_not_supporting_requested_edge" else "canonical_observation", "context_basis": row["context_basis"]})
        claim_note = dict(experiment_note)
        claim_note.update({"record_type": "canonical_boundary_claim" if row["edge_support_status"] == "boundary_not_supporting_requested_edge" else "canonical_claim", "claim_origin": "phase2_curated_evidence_assertion", "source_claim_status": row["claim_status"], "context_basis": row["context_basis"]})
        lines.extend([
            "INSERT INTO m2024_phase2_experiments (extraction_id, experiment_id)",
            "SELECT " + sql(row["extraction_id"]) + ", experiment_id FROM Experiment WHERE " + note_match("notes", row["extraction_id"]) + " ON CONFLICT (extraction_id) DO NOTHING;",
            "INSERT INTO Observation (experiment_id, evidence_type_id, outcome_type_id, observation_value, measurement_method, raw_observation_text, normalized_observation_value, source_section, figure_panel_reference, extraction_confidence, notes)",
            "SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,",
            f"  {sql(db_text(row['observation_value_or_blocker'], 500))}, {sql(db_text(row['observation_assay'], 255))}, {sql(row['observation_value_or_blocker'])}, {sql(db_text(row['observation_value_or_blocker'], 500))},",
            f"  {sql(db_text(row['observation_source_section'], 100))}, {sql(db_text(row['observation_figure_or_table'], 100))}, {sql(normalize_confidence(row['confidence']))}, {json_sql(obs_note)}",
            "FROM m2024_phase2_experiments e",
            "JOIN ControlledVocabulary_EvidenceType et ON et.evidence_type_name=" + sql(row["evidence_layer"]),
            "JOIN ControlledVocabulary_OutcomeType ot ON ot.outcome_type_name=" + sql(row["outcome_type"]),
            "WHERE e.extraction_id=" + sql(row["extraction_id"]),
            "  AND NOT EXISTS (SELECT 1 FROM Observation existing WHERE " + note_match("existing.notes", row["extraction_id"]) + " AND existing.notes LIKE '%\"pmid\": \"" + row["pmid"] + "\"%');",
            "INSERT INTO m2024_phase2_observations (extraction_id, observation_id)",
            "SELECT " + sql(row["extraction_id"]) + ", o.observation_id FROM Observation o WHERE " + note_match("o.notes", row["extraction_id"]) + " AND o.notes LIKE '%\"pmid\": \"" + row["pmid"] + "\"%' ORDER BY o.observation_id DESC LIMIT 1 ON CONFLICT (extraction_id) DO UPDATE SET observation_id=EXCLUDED.observation_id;",
            "",
            "INSERT INTO AuthorClaim (paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes)",
            "SELECT p.paper_id,",
            f"  {sql(row['claim_text_or_blocker'])}, {sql('curated_evidence_claim')}, {sql(normalize_confidence(row['confidence']))},",
            f"  {sql(db_text(row['claim_source_section'], 100))}, {sql(normalize_confidence(row['confidence']))}, {json_sql(claim_note)}",
            "FROM Paper p WHERE p.pmid=" + sql("PMID:" + row["pmid"]) + " AND NOT EXISTS (SELECT 1 FROM AuthorClaim ac WHERE " + note_match("ac.notes", row["extraction_id"]) + ");",
            "UPDATE AuthorClaim ac SET paper_id=p.paper_id, notes=regexp_replace(ac.notes, '\"pmid\": \"[0-9]+\"', '\"pmid\": \"" + row["pmid"] + "\"') FROM Paper p WHERE p.pmid=" + sql("PMID:" + row["pmid"]) + " AND " + note_match("ac.notes", row["extraction_id"]) + ";",
            "UPDATE AuthorClaim SET claim_type=" + sql("curated_boundary_assertion" if row["edge_support_status"] == "boundary_not_supporting_requested_edge" else "curated_evidence_claim") + ", notes=replace(notes, '" + '"record_type": "canonical_author_claim"' + "', '" + ('"record_type": "canonical_boundary_claim"' if row["edge_support_status"] == "boundary_not_supporting_requested_edge" else '"record_type": "canonical_claim"') + "') WHERE " + note_match("notes", row["extraction_id"]) + ";",
            "INSERT INTO m2024_phase2_claims (extraction_id, claim_id)",
            "SELECT " + sql(row["extraction_id"]) + ", claim_id FROM AuthorClaim WHERE " + note_match("notes", row["extraction_id"]) + " ON CONFLICT (extraction_id) DO NOTHING;",
            "",
            "DELETE FROM EvidenceLink l WHERE " + note_match("l.notes", row["extraction_id"]) + " AND l.observation_id <> (SELECT observation_id FROM m2024_phase2_observations WHERE extraction_id=" + sql(row["extraction_id"]) + ");",
            "INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)",
            "SELECT c.claim_id, o.observation_id, 'supports',",
            f"  {json_sql({'canonicalization_batch': 'module20_24_phase2', 'extraction_id': row['extraction_id'], 'b_evidence_id': row['b_evidence_id'], 'evidence_grade': row['evidence_grade'], 'context_level': row['context_level']})}",
            "FROM m2024_phase2_claims c JOIN m2024_phase2_observations o ON o.extraction_id=c.extraction_id",
            "WHERE c.extraction_id=" + sql(row["extraction_id"]) + " ON CONFLICT (claim_id, observation_id) DO NOTHING;",
            "",
        ])

        source_note = dict(experiment_note)
        source_note.update({"record_type": "canonical_edge_boundary" if row["edge_support_status"] == "boundary_not_supporting_requested_edge" else "canonical_edge_source", "register_source_locator": row["source_locator"], "edge_support_status": row["edge_support_status"]})
        grading_basis = " ".join(part for part in (row["grading_basis"], row["context_basis"]) if part)
        source_scope = "negative_evidence" if row["edge_support_status"] == "boundary_not_supporting_requested_edge" else normalize_scope(row["source_scope"])
        grading_status = "phase2_boundary_not_support" if row["edge_support_status"] == "boundary_not_supporting_requested_edge" else "phase2_canonical_source_unit"
        lines.extend([
            "INSERT INTO SignalingEdgeSource (edge_id, paper_id, observation_id, claim_id, support_kind, species_support, source_scope, confidence_tier, citation_note, notes, evidence_grade, context_level, grading_basis, grading_status)",
            "SELECT s.edge_id, p.paper_id, o.observation_id, c.claim_id,",
            f"  {sql(normalize_support(row['support_kind']))}, {sql(normalize_species(row['species_support'] or row['observation_species']))}, {sql(source_scope)}, {sql(normalize_confidence(row['confidence']))},",
            f"  {sql(row['citation_note'])}, {json_sql(source_note)}, {sql(row['evidence_grade'])}, {sql(row['context_level'])}, {sql(grading_basis)}, {sql(grading_status)}",
            "FROM SignalingEdgeRegisterSource s",
            "JOIN Paper p ON p.pmid=" + sql("PMID:" + row["pmid"]),
            "JOIN m2024_phase2_observations o ON o.extraction_id=" + sql(row["extraction_id"]),
            "JOIN m2024_phase2_claims c ON c.extraction_id=" + sql(row["extraction_id"]),
            "WHERE s.module=" + sql(row["module"]) + " AND s.register_evidence_id=" + sql(row["b_evidence_id"]),
            "  AND NOT EXISTS (SELECT 1 FROM SignalingEdgeSource existing WHERE " + note_match("existing.notes", row["extraction_id"]) + ");",
            "UPDATE SignalingEdgeSource SET paper_id=(SELECT paper_id FROM Paper WHERE pmid=" + sql("PMID:" + row["pmid"]) + "), observation_id=(SELECT observation_id FROM m2024_phase2_observations WHERE extraction_id=" + sql(row["extraction_id"]) + "), claim_id=(SELECT claim_id FROM m2024_phase2_claims WHERE extraction_id=" + sql(row["extraction_id"]) + "), source_scope=" + sql(source_scope) + ", evidence_grade=" + sql(row["evidence_grade"]) + ", context_level=" + sql(row["context_level"]) + ", grading_basis=" + sql(grading_basis) + ", grading_status=" + sql(grading_status) + ", notes=regexp_replace(notes, '\"pmid\": \"[0-9]+\"', '\"pmid\": \"" + row["pmid"] + "\"') WHERE " + note_match("notes", row["extraction_id"]) + ";",
            "",
        ])

    lines.extend(["COMMIT;", ""])
    OUT_SQL.write_text("\n".join(lines))

    by_module = Counter(row["module"] for row in candidates)
    report = [
        "# Module 20B–24B Phase-2 canonical evidence materialization",
        "",
        "This generated SQL is conservative and idempotent. It materializes",
        "only stable-PMID rows with validated non-abstract observations and",
        "validated claim text. Experiments are labeled source-defined evidence",
        "units when the original experiment number was not preserved. Explicit",
        "non-promotable claims are retained as boundary evidence and cannot",
        "support promotion of the requested exact edge.",
        "",
        f"- Candidate extraction rows: {len(candidates):,}",
        f"- Unique PMID papers used: {len(papers):,}",
        f"- Explicit boundary-only extraction rows: {sum(row['edge_support_status'] == 'boundary_not_supporting_requested_edge' for row in candidates):,}",
        "",
        "| Module | Source-defined evidence units |",
        "|---|---:|",
    ]
    report.extend(f"| {module} | {by_module[module]:,} |" for module in MODULES)
    report.extend([
        "",
        "Rows with abstract-only, unresolved, metadata-only, missing PMID, or",
        "action-token claim text remain in the staging ledger. Boundary-only",
        "rows are retained as explicit negative/context evidence (E/L0) and",
        "are not treated as support for the requested exact edge. The generated",
        "SQL does not invent original experiment numbers, mechanisms, or",
        "unsupported paper metadata. On rerun, stale promotable links and edge",
        "sources from this batch are pruned; immutable historical extraction",
        "records are retained for audit when the database rejects their deletion.",
        "",
    ])
    REPORT.write_text("\n".join(report))
    print(f"candidate_rows={len(candidates)} papers={len(papers)} sql={OUT_SQL}")


if __name__ == "__main__":
    main()
