#!/usr/bin/env python3
"""Shared, non-probabilistic fields for mechanism evidence exports.

The mechanism database preserves evidence atoms and their qualifiers.  It does
not assign a route-level biological confidence score.  mSCS may combine these
fields with an observed cell context later.
"""

from __future__ import annotations

import re
from collections.abc import Iterable, Mapping


MECHANISM_EVIDENCE_CONTRACT_VERSION = "mechanism_evidence_v1"

OUTPUT_CLASSES = (
    "target_gene_expression",
    "gene_expression_or_transcription",
    "secreted_protein_or_release",
    "cellular_functional_readout",
    "phagocytosis_or_engulfment",
    "phosphorylation_or_activation_readout",
    "reporter_readout",
    "translocation_or_localization_readout",
    "cleavage_or_processing_readout",
    "second_messenger_readout",
    "generic_functional_readout",
    "unknown",
)
EVIDENCE_POLARITIES = ("supports", "contradicts", "mixed", "unknown")
NEGATIVE_EVIDENCE_STATUSES = (
    "not_evaluated",
    "not_supporting_requested_claim",
    "measured_absent",
    "below_threshold",
    "observed_contradiction",
    "not_assayed",
    "insufficient_samples",
    "unknown",
)


def _text(value: object) -> str:
    return "" if value is None else str(value).strip()


def _normalized(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", " ", _text(value).casefold()).strip()


def normalize_output_class(
    *,
    record_type: object = "",
    output_term: object = "",
    output_label: object = "",
    target_gene: object = "",
) -> str:
    """Map an observed output/readout to a controlled class.

    The original term/label remains in the export.  This function only adds a
    reproducible category and never creates a target-gene claim.
    """

    record = _normalized(record_type)
    text = _normalized(" ".join(value for value in (output_term, output_label) if _text(value)))
    if "target gene" in record or _text(target_gene):
        return "target_gene_expression"
    if "gene expression" in text or "transcription" in text or "mrna" in text:
        return "gene_expression_or_transcription"
    if "secret" in text or "release" in text:
        return "secreted_protein_or_release"
    if "phagocyt" in text or "engulf" in text or "efferocyt" in text:
        return "phagocytosis_or_engulfment"
    if "phosphory" in text or "activation" in text or "activated" in text:
        return "phosphorylation_or_activation_readout"
    if "reporter" in text:
        return "reporter_readout"
    if "translocation" in text or "localization" in text or "localisation" in text or "nuclear" in text:
        return "translocation_or_localization_readout"
    if "cleavage" in text or "cleaved" in text or "processing" in text:
        return "cleavage_or_processing_readout"
    if any(token in text for token in ("camp", "pip3", "calcium", "rac1", "mapk", "akt", "erk")):
        return "second_messenger_readout"
    if "cellular function" in text or "cellular functional" in text or any(
        token in text for token in ("proliferation", "migration", "adhesion", "outgrowth", "survival", "invasion")
    ):
        return "cellular_functional_readout"
    if "generic output" in record or "output" in record or text:
        return "generic_functional_readout"
    return "unknown"


def classify_evidence_polarity(
    source_scopes: Iterable[object] = (),
    *,
    evidence_status: object = "",
    evidence_text: object = "",
) -> str:
    """Classify the direction of a retained claim without scoring it."""

    scopes = {_normalized(value).replace(" ", "_") for value in source_scopes if _text(value)}
    status = _normalized(evidence_status)
    text = _normalized(evidence_text)
    negative = "negative_evidence" in scopes or any(
        token in status or token in text
        for token in ("contradict", "not support", "does not support", "negative evidence", "failed to support")
    )
    positive = bool(scopes & {"direct_edge", "pathway_membership", "contextual_support", "register_evidence"})
    if negative and positive:
        return "mixed"
    if negative:
        return "contradicts"
    if positive or _text(evidence_status) or _text(evidence_text):
        return "supports"
    return "unknown"


def classify_negative_evidence_status(
    source_scopes: Iterable[object] = (),
    *,
    evidence_status: object = "",
    evidence_text: object = "",
) -> str:
    """Expose explicit negative/support-boundary states; otherwise unknown."""

    scopes = {_normalized(value).replace(" ", "_") for value in source_scopes if _text(value)}
    status = _normalized(evidence_status)
    text = _normalized(evidence_text)
    if "negative_evidence" in scopes:
        if "not assayed" in text or "not assayed" in status:
            return "not_assayed"
        if any(token in text or token in status for token in ("below threshold", "absent", "no expression")):
            return "measured_absent"
        if any(token in text or token in status for token in ("contradict", "not support", "failed to support")):
            return "observed_contradiction"
        return "not_supporting_requested_claim"
    return "not_evaluated"


def evidence_directness(record_type: object, claim_status: object) -> str:
    record = _normalized(record_type).replace(" ", "_")
    claim = _normalized(claim_status).replace(" ", "_")
    if record == "unresolved_downstream_claim" or "unresolved" in claim:
        return "unresolved"
    if record == "intracellular_cascade_evidence":
        return "explicit_exported_edge"
    if record in {"transcription_factor_evidence", "target_gene_output_evidence"}:
        return "exact_node_mention"
    if record == "generic_output_evidence":
        return "assay_or_readout_term"
    return "source_claim"


def contract_fields(prefix: str = "") -> tuple[str, ...]:
    """Return the additive fields used by queue and route evidence records."""

    return tuple(
        prefix + field
        for field in (
            "evidence_contract_version",
            "evidence_polarity",
            "negative_evidence_status",
            "evidence_directness",
            "output_class",
            "species_context",
            "cell_type_context",
            "compartment_context",
            "injury_context",
            "context_scope",
            "assay_or_perturbation",
            "effect_polarity",
            "source_scope",
        )
    )
