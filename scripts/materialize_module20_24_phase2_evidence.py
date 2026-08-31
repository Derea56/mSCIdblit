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

from materialize_module20_24_paper_provenance import sql, xml_records


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
PHASE2 = REVIEW_ROOT / "module20_24_integrated_phase2_extractions.tsv"
LEDGER = REVIEW_ROOT / "module20_24_evidence_grade_ledger.tsv"
OUT_SQL = REVIEW_ROOT / "module20_24_phase2_evidence_materialization.sql"
REPORT = REVIEW_ROOT / "module20_24_phase2_evidence_materialization.md"
METADATA = ROOT / "work" / "cross_module_synthesis" / "module20_24_canonical_paper_metadata.tsv"
MODULES = ("20B", "21B", "22B", "23B", "24B")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


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
    available_pmids = set(xml_records())
    if METADATA.exists():
        available_pmids.update(row["pmid"] for row in read_tsv(METADATA) if row.get("paper_ready") == "true" and row.get("pmid"))

    candidates: list[dict[str, str]] = []
    for row in phase2:
        stable = [pmid for pmid in pmids(row.get("canonical_paper_key", "")) if pmid in available_pmids]
        if not stable or not valid_observation(row) or not valid_claim(row):
            continue
        grading = ledger.get(row["b_evidence_id"], {})
        candidate = dict(row)
        candidate["pmid"] = stable[0]
        candidate["evidence_grade"] = grading.get("evidence_grade", "")
        candidate["context_level"] = grading.get("context_level", "")
        candidate["grading_basis"] = grading.get("grading_basis", "")
        candidate["context_basis"] = grading.get("context_basis", "")
        candidate["citation_note"] = grading.get("citation_note", "")
        candidate["support_kind"] = grading.get("support_kind", "")
        candidate["source_scope"] = grading.get("source_scope", "")
        candidate["species_support"] = grading.get("species_support", "")
        candidate["outcome_type"], candidate["outcome_basis"] = outcome_type(row)
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
        "CREATE TEMP TABLE m2024_phase2_experiments (extraction_id TEXT PRIMARY KEY, experiment_id BIGINT NOT NULL);",
        "CREATE TEMP TABLE m2024_phase2_observations (extraction_id TEXT PRIMARY KEY, observation_id BIGINT NOT NULL);",
        "CREATE TEMP TABLE m2024_phase2_claims (extraction_id TEXT PRIMARY KEY, claim_id BIGINT NOT NULL);",
        "UPDATE AuthorClaim SET claim_type='curated_evidence_claim', notes=replace(notes, '\"record_type\": \"canonical_author_claim\"', '\"record_type\": \"canonical_claim\"') WHERE claim_type='source_author_claim' AND notes LIKE '%\"canonicalization_batch\": \"module20_24_phase2\"%';",
        "",
    ]

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
        observation_note.update({"record_type": "canonical_observation", "context_basis": row["context_basis"], "full_observation_value": row["observation_value_or_blocker"]})
        claim_note = dict(experiment_note)
        claim_note.update({"record_type": "canonical_author_claim", "context_basis": row["context_basis"]})
        link_note = dict(experiment_note)
        link_note.update({"record_type": "canonical_evidence_link"})
        source_note = dict(experiment_note)
        source_note.update({"record_type": "canonical_edge_source", "register_source_locator": row["source_locator"]})
        description = " | ".join(part for part in (
            "Source-defined evidence unit; original experiment number not separately preserved in Phase-2.",
            "model=" + row["observation_cell_or_model"],
            "assay=" + row["observation_assay"],
            "perturbation=" + row["observation_perturbation"],
            "source_section=" + row["observation_source_section"],
        ) if part and part.split("=", 1)[-1].strip())
        lines.extend([
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
        obs_note.update({"record_type": "canonical_observation", "context_basis": row["context_basis"]})
        claim_note = dict(experiment_note)
        claim_note.update({"record_type": "canonical_claim", "claim_origin": "phase2_curated_evidence_assertion", "source_claim_status": row["claim_status"], "context_basis": row["context_basis"]})
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
            "  AND NOT EXISTS (SELECT 1 FROM Observation existing WHERE " + note_match("existing.notes", row["extraction_id"]) + ");",
            "INSERT INTO m2024_phase2_observations (extraction_id, observation_id)",
            "SELECT " + sql(row["extraction_id"]) + ", o.observation_id FROM Observation o WHERE " + note_match("o.notes", row["extraction_id"]) + " ON CONFLICT (extraction_id) DO NOTHING;",
            "",
            "INSERT INTO AuthorClaim (paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes)",
            "SELECT p.paper_id,",
            f"  {sql(row['claim_text_or_blocker'])}, {sql('curated_evidence_claim')}, {sql(normalize_confidence(row['confidence']))},",
            f"  {sql(db_text(row['claim_source_section'], 100))}, {sql(normalize_confidence(row['confidence']))}, {json_sql(claim_note)}",
            "FROM Paper p WHERE p.pmid=" + sql("PMID:" + row["pmid"]) + " AND NOT EXISTS (SELECT 1 FROM AuthorClaim ac WHERE " + note_match("ac.notes", row["extraction_id"]) + ");",
            "INSERT INTO m2024_phase2_claims (extraction_id, claim_id)",
            "SELECT " + sql(row["extraction_id"]) + ", claim_id FROM AuthorClaim WHERE " + note_match("notes", row["extraction_id"]) + " ON CONFLICT (extraction_id) DO NOTHING;",
            "",
            "INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)",
            "SELECT c.claim_id, o.observation_id, 'supports',",
            f"  {json_sql({'canonicalization_batch': 'module20_24_phase2', 'extraction_id': row['extraction_id'], 'b_evidence_id': row['b_evidence_id'], 'evidence_grade': row['evidence_grade'], 'context_level': row['context_level']})}",
            "FROM m2024_phase2_claims c JOIN m2024_phase2_observations o ON o.extraction_id=c.extraction_id",
            "WHERE c.extraction_id=" + sql(row["extraction_id"]) + " ON CONFLICT (claim_id, observation_id) DO NOTHING;",
            "",
        ])

        source_note = dict(experiment_note)
        source_note.update({"record_type": "canonical_edge_source", "register_source_locator": row["source_locator"]})
        grading_basis = " ".join(part for part in (row["grading_basis"], row["context_basis"]) if part)
        lines.extend([
            "INSERT INTO SignalingEdgeSource (edge_id, paper_id, observation_id, claim_id, support_kind, species_support, source_scope, confidence_tier, citation_note, notes, evidence_grade, context_level, grading_basis, grading_status)",
            "SELECT s.edge_id, p.paper_id, o.observation_id, c.claim_id,",
            f"  {sql(normalize_support(row['support_kind']))}, {sql(normalize_species(row['species_support'] or row['observation_species']))}, {sql(normalize_scope(row['source_scope']))}, {sql(normalize_confidence(row['confidence']))},",
            f"  {sql(row['citation_note'])}, {json_sql(source_note)}, {sql(row['evidence_grade'])}, {sql(row['context_level'])}, {sql(grading_basis)}, {sql('phase2_canonical_source_unit')}",
            "FROM SignalingEdgeRegisterSource s",
            "JOIN Paper p ON p.pmid=" + sql("PMID:" + row["pmid"]),
            "JOIN m2024_phase2_observations o ON o.extraction_id=" + sql(row["extraction_id"]),
            "JOIN m2024_phase2_claims c ON c.extraction_id=" + sql(row["extraction_id"]),
            "WHERE s.module=" + sql(row["module"]) + " AND s.register_evidence_id=" + sql(row["b_evidence_id"]),
            "  AND NOT EXISTS (SELECT 1 FROM SignalingEdgeSource existing WHERE " + note_match("existing.notes", row["extraction_id"]) + ");",
            "UPDATE SignalingEdgeSource SET evidence_grade=" + sql(row["evidence_grade"]) + ", context_level=" + sql(row["context_level"]) + ", grading_basis=" + sql(grading_basis) + ", grading_status='phase2_canonical_source_unit' WHERE " + note_match("notes", row["extraction_id"]) + ";",
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
        "units when the original experiment number was not preserved.",
        "",
        f"- Candidate extraction rows: {len(candidates):,}",
        f"- Unique PMID papers used: {len(papers):,}",
        "",
        "| Module | Source-defined evidence units |",
        "|---|---:|",
    ]
    report.extend(f"| {module} | {by_module[module]:,} |" for module in MODULES)
    report.extend([
        "",
        "Rows with abstract-only, unresolved, metadata-only, boundary, missing",
        "PMID, or action-token claim text remain in the staging ledger. The",
        "generated SQL does not invent original experiment numbers, mechanisms,",
        "or unsupported paper metadata.",
        "",
    ])
    REPORT.write_text("\n".join(report))
    print(f"candidate_rows={len(candidates)} papers={len(papers)} sql={OUT_SQL}")


if __name__ == "__main__":
    main()
