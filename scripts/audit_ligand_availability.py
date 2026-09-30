#!/usr/bin/env python3
"""Audit source evidence for ligand physical-availability classes.

This produces a reviewable, generic ligand-availability layer keyed to the
pinned Module 20B-24B mechanism release. It does not modify mechanism nodes,
edges, route confidence, or SCI evidence tables. Form classifications are
staged candidates unless the source text places an availability term near the
exact ligand label; assay-format language is kept separate.
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
DEFAULT_RELEASE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627"
DEFAULT_LEDGER = ROOT / "work/cross_module_synthesis/canonical_evidence_review/module20_24_integrated_phase2_extractions.tsv"
DEFAULT_PACK = ROOT / "context_packs/spinal_cord_injury"
DEFAULT_OUTPUT = ROOT / "data/processed/ligand_availability_audit_v1"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.audit_sci_module_spatial_reconciliation import index_pack_rows, source_identifiers, unique_values
from scripts.build_sci_context_pack import read_tsv

SOURCE_FIELDS = (
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

CONTEXT_FORM_CLASSES = {
    "soluble": "soluble",
    "soluble cytokine": "soluble",
    "membrane_bound": "membrane_bound",
    "surface receptor": "membrane_bound",
    "surface CD3/CD4 or CD3/CD8α proteins": "membrane_bound",
}
CONTEXT_FORM_PATTERNS = (
    (re.compile(r"\b(?:soluble|secreted)\b", re.IGNORECASE), "soluble"),
    (re.compile(r"\b(?:extracellular[ _-]+matrix|matrix[ _-](?:associated|assembled|bands?)|fibrillar[ _-]+(?:matrix|network))\b", re.IGNORECASE), "ecm_retained"),
)

SOURCE_FORM_OVERRIDES = {
    "M20B-EVID-001936": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("observation_value_or_blocker", "observation_perturbation"),
        "pattern": re.compile(r"\bcollagen[- ]I\b.*\bmatrix\b|\bcollagen[- ]I\s+matrix\b", re.IGNORECASE),
    },
    "M20B-EVID-002127": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("observation_value_or_blocker", "claim_text_or_blocker"),
        "pattern": re.compile(r"\b(?:perlecan|HSPG2)\b.*\bextracellular[- ]matrix\b", re.IGNORECASE),
    },
    "M20B-EVID-002232": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("observation_value_or_blocker",),
        "pattern": re.compile(r"\bsoluble\s+netrin\b", re.IGNORECASE),
    },
    "M23B-EVID-000749": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "ecm_retained"],
        "fields": ("observation_value_or_blocker",),
        "pattern": re.compile(r"\b(?:soluble/cellular\s+FN|FN\s+matrix)\b", re.IGNORECASE),
    },
    "M20B-EVID-002154": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "ecm_retained"],
        "fields": ("observation_value_or_blocker", "observation_perturbation"),
        "pattern": re.compile(r"\b(?:polymerized laminin-332 matrices|matrix versus soluble ligand comparison)\b", re.IGNORECASE),
    },
    "M20B-EVID-002199": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "ecm_retained"],
        "fields": ("observation_value_or_blocker", "observation_perturbation"),
        "pattern": re.compile(r"\b(?:polymerized laminin-332 matrices|matrix versus soluble ligand comparison)\b", re.IGNORECASE),
    },
    "M20B-EVID-003229": {
        "candidate": "both_or_context_dependent",
        "signals": ["soluble", "ecm_retained"],
        "fields": ("observation_perturbation",),
        "pattern": re.compile(r"\bsoluble/immobilized decorin\b", re.IGNORECASE),
    },
    "M20B-EVID-002904": {
        "candidate": "membrane_bound",
        "signals": ["membrane_bound"],
        "fields": ("observation_value_or_blocker",),
        "pattern": re.compile(r"\bCD47 displayed on cell membranes\b", re.IGNORECASE),
    },
    "M20B-EVID-004969": {
        "candidate": "soluble",
        "signals": ["soluble"],
        "fields": ("observation_value_or_blocker",),
        "pattern": re.compile(r"\bmacrophage-secreted osteopontin\b", re.IGNORECASE),
    },
    "M20B-EVID-002994": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("observation_value_or_blocker", "observation_perturbation"),
        "pattern": re.compile(r"\bcollagen XI(?:-containing matrices| in collagen I matrices)\b", re.IGNORECASE),
    },
    "M20B-EVID-003007": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("claim_text_or_blocker", "observation_value_or_blocker"),
        "pattern": re.compile(r"\bdirect matrix-receptor adhesion edge\b|\bcollagen XIV/undulin\b", re.IGNORECASE),
    },
    "M20B-EVID-004966": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("observation_value_or_blocker",),
        "pattern": re.compile(r"\bMindin/SPON2 matrix\b", re.IGNORECASE),
    },
    "M23B-EVID-000346": {
        "candidate": "ecm_retained",
        "signals": ["ecm_retained"],
        "fields": ("observation_value_or_blocker", "observation_perturbation", "claim_text_or_blocker"),
        "pattern": re.compile(r"\b(?:matrix-associated ligand context|PTN immobilization|matrix-presentation boundaries)\b", re.IGNORECASE),
    },
}

FORM_PATTERNS = {
    "soluble": re.compile(
        r"\b(?:soluble|secreted|diffusible|free[- ]form)\b",
        re.IGNORECASE,
    ),
    "membrane_bound": re.compile(
        r"\b(?:membrane[- ]bound|membrane[- ]tethered|cell[- ]surface|surface[- ]bound|"
        r"transmembrane|juxtacrine|cell[- ]associated|GPI[- ]anchored|"
        r"glycosylphosphatidylinositol[- ]anchored|anchored)\b",
        re.IGNORECASE,
    ),
    "ecm_retained": re.compile(
        r"\b(?:extracellular matrix|ECM[- ]bound|matrix[- ]bound|matrix[- ]retained|"
        r"proteoglycan[- ]bound|heparan[- ]sulfate[- ]bound|basement membrane)\b",
        re.IGNORECASE,
    ),
}
FORM_EXCLUSION = re.compile(
    r"\b(?:not|rather than|without|does not|did not|no longer)\s+(?:an?\s+)?"
    r"(?:soluble|secreted|membrane[- ]bound|cell[- ]surface|"
    r"transmembrane|ECM[- ]bound|matrix[- ]bound)(?:\s+(?:ligand|protein|receptor|form))?\b",
    re.IGNORECASE,
)

OUTPUT_FIELDS = [
    "assertion_origin",
    "mechanism_node_id",
    "ligand_canonical_name",
    "ligand_source_label",
    "mechanism_edge_id",
    "target_node_id",
    "target_label",
    "relation_type",
    "pathway_name",
    "module",
    "b_evidence_id",
    "extraction_id",
    "dependency_group",
    "context_observation_id",
    "context_evidence_role",
    "context_study_id",
    "context_timepoint_id",
    "context_species",
    "context_injury_model",
    "context_injury_level",
    "context_injury_severity",
    "context_tissue",
    "context_cell_type",
    "context_sample_id",
    "context_timepoint_value",
    "context_timepoint_unit",
    "context_perturbation",
    "context_treatment",
    "context_sample_scope",
    "context_protein_form",
    "context_protein_resolution",
    "context_source_locator",
    "context_source_record_key",
    "canonical_paper_key",
    "module_source_locator",
    "observation_status",
    "evidence_layer",
    "confidence",
    "observation_value_or_blocker",
    "observation_cell_or_model",
    "observation_assay",
    "observation_perturbation",
    "claim_text_or_blocker",
    "availability_class_candidate",
    "availability_evidence_state",
    "availability_signal_terms",
    "availability_evidence_snippet",
    "availability_basis_fields",
    "sci_context_match_status",
    "sci_context_observation_ids",
    "sci_context_ids",
    "sci_context_source_artifact_paths",
    "sci_context_source_artifact_sha256",
    "promotion_state",
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


def label_tokens(*labels: str) -> list[str]:
    tokens: set[str] = set()
    for label in labels:
        if not label:
            continue
        tokens.add(label.strip())
        tokens.update(token for token in re.split(r"[^A-Za-z0-9]+", label) if len(token) >= 4)
    return sorted(tokens, key=len, reverse=True)


def exact_label_positions(text: str, labels: list[str]) -> list[tuple[int, int, str]]:
    positions: list[tuple[int, int, str]] = []
    for label in labels:
        pattern = re.compile(rf"(?<![A-Za-z0-9]){re.escape(label)}(?![A-Za-z0-9])", re.IGNORECASE)
        positions.extend((match.start(), match.end(), label) for match in pattern.finditer(text))
    return positions


def compact_snippet(text: str, start: int, end: int) -> str:
    left = max(0, start - 100)
    right = min(len(text), end + 100)
    return " ".join(text[left:right].split())


def directly_attached(text: str, match: re.Match[str], positions: list[tuple[int, int, str]]) -> bool:
    """Require a short form-to-ligand phrase, not merely same-sentence proximity."""

    assay_words = re.compile(r"\b(?:assay|assays|binding|screen|screening|expression|cells?)\b", re.IGNORECASE)
    for start, end, _label in positions:
        if start >= match.end():
            between = text[match.end():start]
        elif end <= match.start():
            between = text[end:match.start()]
        else:
            return True
        words = re.findall(r"[A-Za-z0-9-]+", between)
        if (
            (len(words) <= 4 or (len(words) <= 8 and re.search(r"\bforms?\b", between, re.IGNORECASE)))
            and not assay_words.search(between)
        ):
            return True
    return False


def classify_availability(text: str, labels: list[str]) -> tuple[str, str, list[str], str, list[str]]:
    positions = exact_label_positions(text, labels)
    attached: dict[str, list[str]] = defaultdict(list)
    unattached: dict[str, list[str]] = defaultdict(list)
    basis: dict[str, list[str]] = defaultdict(list)
    snippets: list[str] = []
    for kind, pattern in FORM_PATTERNS.items():
        for match in pattern.finditer(text):
            exclusion_window = text[max(0, match.start() - 80):min(len(text), match.end() + 80)]
            if FORM_EXCLUSION.search(exclusion_window):
                continue
            nearby = [item for item in positions if abs(item[0] - match.end()) <= 48 or abs(item[1] - match.start()) <= 48]
            snippet = compact_snippet(text, match.start(), match.end())
            if nearby and directly_attached(text, match, nearby):
                attached[kind].append(match.group(0))
                snippets.append(snippet)
            else:
                unattached[kind].append(match.group(0))
    for kind in attached:
        basis[kind].append(kind)
    attached_kinds = set(attached)
    if attached_kinds:
        if "ecm_retained" in attached_kinds and attached_kinds == {"ecm_retained"}:
            candidate = "ecm_retained"
        elif attached_kinds == {"soluble"}:
            candidate = "soluble"
        elif attached_kinds == {"membrane_bound"}:
            candidate = "membrane_bound"
        else:
            candidate = "both_or_context_dependent"
        return candidate, "source_reported_candidate", sorted(attached_kinds), "; ".join(sorted(set(snippets))), sorted(basis)
    if unattached:
        return "unknown", "assay_or_form_language_not_attached_to_exact_ligand", sorted(unattached), "", sorted(unattached)
    return "unknown", "not_reported_in_source_record", [], "", []


def normalized_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def context_form_class(protein_form: str) -> str:
    normalized_form = protein_form.lower()
    if (
        "exact molecular form not further specified" in normalized_form
        or "exact processing state not resolved" in normalized_form
    ):
        return ""
    if "secreted" in normalized_form and "total" in normalized_form:
        return ""
    if protein_form in CONTEXT_FORM_CLASSES:
        return CONTEXT_FORM_CLASSES[protein_form]
    for pattern, candidate in CONTEXT_FORM_PATTERNS:
        if pattern.search(protein_form):
            return candidate
    return ""


def context_form_matches(
    observations: list[dict[str, str]],
    ligand_nodes: dict[str, dict[str, str]],
) -> list[tuple[dict[str, str], dict[str, str], dict[str, Any], str, str, list[str], str]]:
    """Return exact node/observation matches with an explicit SCI protein form.

    The match is deliberately limited to exact normalized mechanism labels or
    label variants. It does not infer gene-to-protein aliases, receptor
    families, or form from assay type alone.
    """

    label_index: dict[str, list[dict[str, str]]] = defaultdict(list)
    for node in ligand_nodes.values():
        for field in ("canonical_name", "canonical_label"):
            label = node.get(field, "")
            if label:
                label_index[normalized_key(label)].append(node)
        for label in filter(None, node.get("label_variants", "").split(";")):
            label_index[normalized_key(label)].append(node)

    matches: dict[tuple[str, str], tuple[dict[str, str], dict[str, str], dict[str, Any], str, str, list[str], str]] = {}
    for observation in observations:
        if observation.get("modality") != "protein":
            continue
        try:
            provenance = json.loads(observation.get("provenance_note", "{}"))
        except json.JSONDecodeError:
            continue
        protein_form = str(provenance.get("protein_form", "")).strip()
        form_evidence: tuple[str, list[str], str] | None = None
        direct_class = context_form_class(protein_form)
        if direct_class:
            form_evidence = (direct_class, ["observations.tsv:provenance_note.protein_form"], protein_form)
        else:
            observed_labels = [observation.get("measured_entity_name", ""), observation.get("feature_id", "")]
            label_patterns = [
                re.compile(rf"(?<![A-Za-z0-9]){re.escape(label)}(?![A-Za-z0-9])", re.IGNORECASE)
                for label in observed_labels
                if label
            ]
            for field in ("value_text", "direction_vs_control"):
                text = observation.get(field, "")
                if not text or not any(pattern.search(text) for pattern in label_patterns):
                    continue
                candidate = context_form_class(text)
                if candidate:
                    signal_match = next(
                        match for pattern, _candidate in CONTEXT_FORM_PATTERNS for match in pattern.finditer(text)
                        if _candidate == candidate
                    )
                    form_evidence = (
                        candidate,
                        [f"observations.tsv:{field}"],
                        compact_snippet(text, signal_match.start(), signal_match.end()),
                    )
                    break
        if not form_evidence:
            continue
        candidate_nodes: dict[str, dict[str, str]] = {}
        for field in ("measured_entity_name", "feature_id"):
            key = normalized_key(observation.get(field, ""))
            for node in label_index.get(key, []):
                candidate_nodes[node["node_id"]] = node
        for node in candidate_nodes.values():
            matches[(node["node_id"], observation["observation_id"])] = (
                node,
                observation,
                provenance,
                protein_form,
                form_evidence[0],
                form_evidence[1],
                form_evidence[2],
            )
    return list(matches.values())


def source_form_override(module_row: dict[str, str]) -> tuple[str, str, list[str], str, list[str]] | None:
    """Apply only explicitly keyed, source-text-backed form curation rules."""

    rule = SOURCE_FORM_OVERRIDES.get(module_row.get("b_evidence_id", ""))
    if not rule:
        return None
    for field in rule["fields"]:
        text = module_row.get(field, "")
        match = rule["pattern"].search(text)
        if match:
            return (
                rule["candidate"],
                "source_reported_candidate",
                rule["signals"],
                compact_snippet(text, match.start(), match.end()),
                [field],
            )
    return None


def build(
    release_dir: Path = DEFAULT_RELEASE,
    ledger_path: Path = DEFAULT_LEDGER,
    pack: Path = DEFAULT_PACK,
    output_dir: Path = DEFAULT_OUTPUT,
) -> dict[str, Any]:
    release_dir = release_dir.resolve()
    ledger_path = ledger_path.resolve()
    pack = pack.resolve()
    output_dir = output_dir.resolve()
    nodes = {row["node_id"]: row for row in read_tsv(release_dir / "mechanism_nodes.tsv")}
    ligand_nodes = {node_id: row for node_id, row in nodes.items() if row.get("node_type") == "ligand"}
    edges = read_tsv(release_dir / "mechanism_edges.tsv")
    evidence_to_edges: dict[str, list[dict[str, str]]] = defaultdict(list)
    for edge in edges:
        if edge.get("source_node_id") not in ligand_nodes:
            continue
        for evidence_id in filter(None, edge.get("evidence_ids", "").split(";")):
            evidence_to_edges[evidence_id].append(edge)

    ledger_rows = read_tsv(ledger_path)
    observations = read_tsv(pack / "observations.tsv")
    contexts = {row["context_id"]: row for row in read_tsv(pack / "contexts.tsv")}
    context_index = index_pack_rows(observations, ("source_locator", "source_record_key"))
    output_rows: list[dict[str, Any]] = []
    counts_by: dict[str, Counter[str]] = {
        "module": Counter(),
        "availability_class_candidate": Counter(),
        "availability_evidence_state": Counter(),
        "observation_status": Counter(),
        "evidence_layer": Counter(),
        "sci_context_match_status": Counter(),
        "assertion_origin": Counter(),
        "context_form_class": Counter(),
    }
    matched_ledger_rows = 0
    ligand_associations = 0

    for module_row in ledger_rows:
        evidence_id = module_row.get("b_evidence_id", "")
        associated_edges = evidence_to_edges.get(evidence_id, [])
        if not associated_edges:
            continue
        matched_ledger_rows += 1
        source_ids = source_identifiers(module_row.get("canonical_paper_key", ""), module_row.get("source_locator", ""))
        matched_context = [row for source_id in source_ids for row in context_index.get(source_id, [])]
        matched_context = list({row["observation_id"]: row for row in matched_context}.values())
        context_status = "matched_exact_source_identifier" if matched_context else "no_exact_source_identifier_match"
        unique_edges = {edge["edge_id"]: edge for edge in associated_edges}
        for edge in unique_edges.values():
            ligand = ligand_nodes[edge["source_node_id"]]
            labels = label_tokens(ligand.get("canonical_name", ""), ligand.get("canonical_label", ""), edge.get("source_label", ""), ligand.get("label_variants", ""))
            field_results = [
                (field, classify_availability(module_row.get(field, ""), labels))
                for field in SOURCE_FIELDS
                if module_row.get(field, "")
            ]
            attached_results = [result for _field, result in field_results if result[1] == "source_reported_candidate"]
            unattached_results = [result for _field, result in field_results if result[1] == "assay_or_form_language_not_attached_to_exact_ligand"]
            attached_signals = {signal for _candidate, _state, signals, _snippet, _basis in attached_results for signal in signals}
            override = source_form_override(module_row)
            if override:
                candidate, state, signals, snippet, basis = override
            elif attached_signals:
                if attached_signals == {"ecm_retained"}:
                    candidate = "ecm_retained"
                elif attached_signals == {"soluble"}:
                    candidate = "soluble"
                elif attached_signals == {"membrane_bound"}:
                    candidate = "membrane_bound"
                else:
                    candidate = "both_or_context_dependent"
                state = "source_reported_candidate"
                signals = sorted(attached_signals)
                snippet = "; ".join(sorted({snippet for _candidate, _state, _signals, snippet, _basis in attached_results if snippet}))
                basis = [field for field, result in field_results if result[1] == "source_reported_candidate"]
            elif unattached_results:
                candidate = "unknown"
                state = "assay_or_form_language_not_attached_to_exact_ligand"
                signals = sorted({signal for _candidate, _state, signals, _snippet, _basis in unattached_results for signal in signals})
                snippet = ""
                basis = [field for field, result in field_results if result[1] == "assay_or_form_language_not_attached_to_exact_ligand"]
            else:
                candidate = "unknown"
                state = "not_reported_in_source_record"
                signals = []
                snippet = ""
                basis = []
            ligand_associations += 1
            row = {
                "assertion_origin": "source_linked_mechanism_evidence",
                "mechanism_node_id": ligand["node_id"],
                "ligand_canonical_name": ligand.get("canonical_name", ""),
                "ligand_source_label": edge.get("source_label", ""),
                "mechanism_edge_id": edge.get("edge_id", ""),
                "target_node_id": edge.get("target_node_id", ""),
                "target_label": edge.get("target_label", ""),
                "relation_type": edge.get("relation_type", ""),
                "pathway_name": edge.get("pathway_name", ""),
                "module": module_row.get("module", ""),
                "b_evidence_id": evidence_id,
                "extraction_id": module_row.get("extraction_id", ""),
                "dependency_group": f"{evidence_id}|{ligand['node_id']}",
                "context_observation_id": "",
                "context_evidence_role": "",
                "context_study_id": "",
                "context_timepoint_id": "",
                "context_species": "",
                "context_injury_model": "",
                "context_injury_level": "",
                "context_injury_severity": "",
                "context_tissue": "",
                "context_cell_type": "",
                "context_sample_id": "",
                "context_timepoint_value": "",
                "context_timepoint_unit": "",
                "context_perturbation": "",
                "context_treatment": "",
                "context_sample_scope": "",
                "context_protein_form": "",
                "context_protein_resolution": "",
                "context_source_locator": "",
                "context_source_record_key": "",
                "canonical_paper_key": module_row.get("canonical_paper_key", ""),
                "module_source_locator": module_row.get("source_locator", ""),
                "observation_status": module_row.get("observation_status", ""),
                "evidence_layer": module_row.get("evidence_layer", ""),
                "confidence": module_row.get("confidence", ""),
                "observation_value_or_blocker": module_row.get("observation_value_or_blocker", ""),
                "observation_cell_or_model": module_row.get("observation_cell_or_model", ""),
                "observation_assay": module_row.get("observation_assay", ""),
                "observation_perturbation": module_row.get("observation_perturbation", ""),
                "claim_text_or_blocker": module_row.get("claim_text_or_blocker", ""),
                "availability_class_candidate": candidate,
                "availability_evidence_state": state,
                "availability_signal_terms": ";".join(signals),
                "availability_evidence_snippet": snippet,
                "availability_basis_fields": ";".join(basis),
                "sci_context_match_status": context_status,
                "sci_context_observation_ids": ";".join(unique_values(matched_context, "observation_id")),
                "sci_context_ids": ";".join(unique_values(matched_context, "context_id")),
                "sci_context_source_artifact_paths": ";".join(unique_values(matched_context, "source_artifact_path")),
                "sci_context_source_artifact_sha256": ";".join(unique_values(matched_context, "source_artifact_sha256")),
                "promotion_state": "audit_only_not_promoted",
                "audit_note": (
                    "Availability class is a staged source-text candidate, not a finalized protein property. "
                    "Assay format is not treated as physical localization; no graph edge, route confidence, or numeric weight was created."
                ),
            }
            output_rows.append(row)
            counts_by["module"][row["module"] or "unknown"] += 1
            counts_by["availability_class_candidate"][candidate] += 1
            counts_by["availability_evidence_state"][state] += 1
            counts_by["observation_status"][row["observation_status"] or "unknown"] += 1
            counts_by["evidence_layer"][row["evidence_layer"] or "unknown"] += 1
            counts_by["sci_context_match_status"][context_status] += 1
            counts_by["assertion_origin"][row["assertion_origin"]] += 1

    context_matches = context_form_matches(observations, ligand_nodes)
    for ligand, observation, provenance, protein_form, context_class, form_basis, form_snippet in context_matches:
        context_curation = provenance.get("context_curation", {})
        context = contexts.get(observation.get("context_id", ""), {})
        context_source_locator = provenance.get("source_location", "") or observation.get("source_locator", "")
        row = {
            "assertion_origin": "sci_context_observation",
            "mechanism_node_id": ligand["node_id"],
            "ligand_canonical_name": ligand.get("canonical_name", ""),
            "ligand_source_label": "",
            "mechanism_edge_id": "",
            "target_node_id": "",
            "target_label": "",
            "relation_type": "",
            "pathway_name": "",
            "module": ligand.get("modules", ""),
            "b_evidence_id": "",
            "extraction_id": "",
            "dependency_group": f"{observation['dependency_group']}|{ligand['node_id']}",
            "context_observation_id": observation.get("observation_id", ""),
            "context_evidence_role": observation.get("evidence_role", ""),
            "context_study_id": context.get("study_id", "") or provenance.get("study_id", ""),
            "context_timepoint_id": provenance.get("timepoint_id", ""),
            "context_species": context.get("species", ""),
            "context_injury_model": context.get("injury_model", ""),
            "context_injury_level": context.get("injury_level", ""),
            "context_injury_severity": context.get("injury_severity", ""),
            "context_tissue": context.get("tissue", ""),
            "context_cell_type": context.get("cell_type", "") or observation.get("cell_type", ""),
            "context_sample_id": context.get("sample_id", "") or observation.get("sample_id", ""),
            "context_timepoint_value": context.get("timepoint_value", "") or observation.get("timepoint_value", ""),
            "context_timepoint_unit": context.get("timepoint_unit", "") or observation.get("timepoint_unit", ""),
            "context_perturbation": context.get("perturbation", "") or provenance.get("study_perturbation_status", "") or observation.get("perturbation", ""),
            "context_treatment": context.get("treatment", ""),
            "context_sample_scope": context.get("sample_scope", "") or provenance.get("sample_scope", ""),
            "context_protein_form": protein_form,
            "context_protein_resolution": provenance.get("protein_resolution", ""),
            "context_source_locator": context_source_locator,
            "context_source_record_key": observation.get("source_record_key", ""),
            "canonical_paper_key": "",
            "module_source_locator": "",
            "observation_status": observation.get("observation_status", ""),
            "evidence_layer": "context_matched_external_observation",
            "confidence": provenance.get("evidence_grade", ""),
            "observation_value_or_blocker": observation.get("value_text", ""),
            "observation_cell_or_model": observation.get("cell_type", ""),
            "observation_assay": observation.get("assay", ""),
            "observation_perturbation": observation.get("perturbation", ""),
            "claim_text_or_blocker": (
                f"Explicit SCI protein-form annotation: protein_form={protein_form}; "
                f"protein_resolution={provenance.get('protein_resolution', '')}"
            ),
            "availability_class_candidate": context_class,
            "availability_evidence_state": "context_observation_explicit_protein_form",
            "availability_signal_terms": context_class,
            "availability_evidence_snippet": form_snippet,
            "availability_basis_fields": ";".join(form_basis),
            "sci_context_match_status": "matched_exact_ligand_observation",
            "sci_context_observation_ids": observation.get("observation_id", ""),
            "sci_context_ids": observation.get("context_id", ""),
            "sci_context_source_artifact_paths": observation.get("source_artifact_path", ""),
            "sci_context_source_artifact_sha256": observation.get("source_artifact_sha256", ""),
            "promotion_state": "audit_only_not_promoted",
            "audit_note": (
                "SCI observation explicitly annotates the measured protein form. This is context-matched "
                "evidence for the observed SCI sample, not a universal protein property and not causal "
                "evidence for a mechanism edge."
            ),
        }
        output_rows.append(row)
        counts_by["module"][row["module"] or "unknown"] += 1
        counts_by["availability_class_candidate"][context_class] += 1
        counts_by["availability_evidence_state"][row["availability_evidence_state"]] += 1
        counts_by["observation_status"][row["observation_status"] or "unknown"] += 1
        counts_by["evidence_layer"][row["evidence_layer"]] += 1
        counts_by["sci_context_match_status"][row["sci_context_match_status"]] += 1
        counts_by["assertion_origin"][row["assertion_origin"]] += 1
        counts_by["context_form_class"][context_class] += 1

    output_rows.sort(key=lambda row: (row["mechanism_node_id"], row["mechanism_edge_id"], row["b_evidence_id"], row["extraction_id"]))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_tsv = output_dir / "ligand_availability_audit.tsv"
    output_json = output_dir / "ligand_availability_audit.json"
    write_tsv(output_tsv, output_rows)

    metadata = json.loads((release_dir / "bundle_metadata.json").read_text(encoding="utf-8"))
    input_paths = [
        release_dir / "bundle_metadata.json",
        release_dir / "mechanism_nodes.tsv",
        release_dir / "mechanism_edges.tsv",
        ledger_path,
        pack / "observations.tsv",
        pack / "contexts.tsv",
    ]
    input_artifacts = [
        {"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "size_bytes": path.stat().st_size, "rows": len(read_tsv(path)) if path.suffix == ".tsv" else None}
        for path in input_paths
    ]
    summary = {
        "audit_version": "ligand_availability_audit_v1",
        "scope": "Source-linked ligand evidence in the pinned Module 20B-24B mechanism release; SCI context is linked by exact source identifiers when present.",
        "mechanism_release_id": metadata.get("release_id", ""),
        "mechanism_release_path": str(release_dir.relative_to(ROOT)),
        "input_artifacts": input_artifacts,
        "release_ligand_node_count": len(ligand_nodes),
        "phase2_ledger_rows_scanned": len(ledger_rows),
        "phase2_rows_with_pinned_ligand_edge": matched_ledger_rows,
        "ligand_evidence_associations": ligand_associations,
        "ligand_context_form_assertions": len(context_matches),
        "ligand_context_form_assertion_nodes": len({ligand["node_id"] for ligand, _observation, _provenance, _form, _class, _basis, _snippet in context_matches}),
        "unique_dependency_groups": len({row["dependency_group"] for row in output_rows}),
        "counts_by": {key: dict(sorted(counter.items())) for key, counter in sorted(counts_by.items())},
        "interpretation": {
            "availability_classes": "soluble, membrane_bound, both_or_context_dependent, and ecm_retained are staged candidates; unknown is retained when the source does not resolve physical availability.",
            "assay_format_gate": "Soluble ectodomain, recombinant-receptor, cell-surface-binding, SPR, or immobilized-assay language is not sufficient by itself to classify the ligand form.",
            "sci_context_linking": "SCI context is linked only through exact PMID, PMCID, or DOI intersections with observations.tsv; absence of a match is not negative protein evidence.",
            "context_form_assertions": "Exact ligand-label matches to observations.tsv provenance_note protein_form values are emitted as context_matched_external_observation rows; they describe the observed SCI sample and do not establish a universal protein property.",
            "dependency_policy": "Rows sharing b_evidence_id and ligand node_id share a dependency group and must not be counted as independent experiments.",
            "promotion_policy": "This audit does not modify mechanism_nodes.tsv, mechanism_edges.tsv, observations.tsv, mechanism_links.tsv, or the pinned graph release.",
            "next_step": "Manually review source-reported candidates before exposing them as soft spatial filters; preserve unknown and assay-only states separately.",
        },
        "artifacts": {"tsv": output_tsv.name, "json": output_json.name},
    }
    output_json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-dir", type=Path, default=DEFAULT_RELEASE)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--pack", type=Path, default=DEFAULT_PACK)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    summary = build(args.release_dir, args.ledger, args.pack, args.output_dir)
    print(json.dumps({"release_id": summary["mechanism_release_id"], "ligand_evidence_associations": summary["ligand_evidence_associations"], "counts_by": summary["counts_by"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
