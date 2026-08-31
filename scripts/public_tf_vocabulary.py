"""Shared vocabulary for public-TF role, context, and materialization lanes."""

from __future__ import annotations


ROLE_CANONICAL = "canonical_sequence_specific_tf"
ROLE_NONCANONICAL = "noncanonical_gene_expression_regulator"
ROLE_NONTRANSCRIPTIONAL = "non_transcriptional_regulator"
ROLE_UNRESOLVED = "unresolved_regulator_role"
ROLE_LOW_TIER = "low_tier_role_unassigned"

CANONICAL_STATUS_CANONICAL = "canonical_tf"
CANONICAL_STATUS_NONCANONICAL = "noncanonical_regulator"
CANONICAL_STATUS_NOT_ASSIGNED = "not_assigned_low_tier"
CANONICAL_STATUS_UNRESOLVED = "unresolved"

SCI_CONTEXT_DIRECT = "direct_sci_context"
SCI_CONTEXT_INDIRECT = "indirect_sci_context"
SCI_CONTEXT_NON_SCI = "non_sci_transferable_context"
SCI_CONTEXT_LIMITED = "non_sci_context_limited"
SCI_CONTEXT_UNRESOLVED = "unresolved_sci_context"
SCI_CONTEXT_NOT_ASSESSED = "not_assessed"
SCI_CONTEXT_NOT_APPLICABLE = "not_applicable"

LANE_CANONICAL = "canonical_tf_regulon_candidate"
LANE_NONCANONICAL = "noncanonical_module_context_candidate"
LANE_EXTERNAL = "external_regulatory_evidence_candidate"
LANE_CATALOG_ONLY = "catalog_only_external_context"
LANE_LOW_TIER = "screened_out_low_tier"

CONTEXT_L0 = "L0_no_context_evidence"
CONTEXT_L1 = "L1_non_CNS_context"
CONTEXT_L2 = "L2_CNS_context"
CONTEXT_L3 = "L3_spinal_cord_tissue_context"
CONTEXT_L4 = "L4_SCI_context"

CONTEXT_SCOPE_EXACT_PAIR = "exact_pair"
CONTEXT_SCOPE_REGULATOR_ONLY = "regulator_only"
CONTEXT_SCOPE_TARGET_ONLY = "target_only"
CONTEXT_SCOPE_COMPONENT_ONLY = "pathway_or_component_only"
CONTEXT_SCOPE_NOT_ASSESSED = "not_assessed"
CONTEXT_SCOPE_NO_QUALIFYING = "no_qualifying_context_found"

CONTEXT_LANE_SCI_PAIR = "sci_pair_candidate"
CONTEXT_LANE_SPINAL_CORD = "spinal_cord_context_candidate"
CONTEXT_LANE_CNS = "cns_context_candidate"
CONTEXT_LANE_NON_CNS = "non_cns_context_candidate"
CONTEXT_LANE_COMPONENT = "sci_relevant_component_context"
CONTEXT_LANE_REVIEW = "context_review_pending"
CONTEXT_LANE_REVIEWED_NONE = "context_reviewed_no_qualifying_context"
CONTEXT_LANE_NO_ROUTE = "no_module_route"
CONTEXT_LANE_LOW_TIER = "screened_out_low_tier"

MECHANISM_DIRECT_TF = "direct_sequence_specific_tf_binding"
MECHANISM_CHROMATIN_COFACTOR = "chromatin_or_transcriptional_cofactor_to_gene_expression"
MECHANISM_RNA_LEVEL = "rna_or_post_transcriptional_regulation"
MECHANISM_SIGNAL_TO_RNA = "indirect_extracellular_signal_to_target_rna"
MECHANISM_SIGNAL_RELAY = "extracellular_signal_or_receptor_relay"
MECHANISM_PROTEIN = "protein_modification_or_target_protein_regulation"
MECHANISM_ASSOCIATION = "expression_or_perturbation_association"
MECHANISM_COMPLEX = "complex_or_architecture_association"
MECHANISM_UNRESOLVED = "unresolved_mechanism"

MECHANISM_DEFINITIONS = {
    MECHANISM_DIRECT_TF: "Sequence-specific TF binding or occupancy at the target regulatory locus is the proposed mechanism.",
    MECHANISM_CHROMATIN_COFACTOR: "A chromatin regulator, coactivator, coregulator, or transcriptional complex affects gene expression; direct sequence-specific TF binding by this regulator is not established.",
    MECHANISM_RNA_LEVEL: "The regulator acts at RNA processing, stability, translation, or another post-transcriptional level; promoter occupancy is not implied.",
    MECHANISM_SIGNAL_TO_RNA: "An extracellular ligand, protease, or receptor relay is associated with a downstream target-RNA change; intermediate steps and promoter occupancy are not fully established.",
    MECHANISM_SIGNAL_RELAY: "An extracellular ligand, receptor, or pathway relay is supported, without claiming direct regulation of the target gene locus.",
    MECHANISM_PROTEIN: "The relationship concerns protein modification, proteolysis, kinase activity, or target-protein regulation rather than direct gene transcription.",
    MECHANISM_ASSOCIATION: "Expression or perturbation changes associate the regulator and target, but the causal molecular bridge remains unresolved.",
    MECHANISM_COMPLEX: "The evidence concerns a multiprotein complex or genome-architecture relationship; the exact regulator-to-target mechanism remains unresolved.",
    MECHANISM_UNRESOLVED: "The record supports a regulator-target relationship, but the available evidence does not resolve the molecular mechanism.",
}


def role_class_for_promotion(promotion_class: str) -> str:
    """Return role identity without making an evidence or SCI-context claim."""
    value = promotion_class.casefold()
    if value.startswith("role_specific_noncanonical"):
        return ROLE_NONCANONICAL
    if value.startswith("sequence_specific_tf"):
        return ROLE_CANONICAL
    if not value:
        return ROLE_LOW_TIER
    return ROLE_UNRESOLVED


def canonical_status_for_role(role_class: str) -> str:
    if role_class == ROLE_CANONICAL:
        return CANONICAL_STATUS_CANONICAL
    if role_class == ROLE_NONCANONICAL:
        return CANONICAL_STATUS_NONCANONICAL
    if role_class == ROLE_LOW_TIER:
        return CANONICAL_STATUS_NOT_ASSIGNED
    return CANONICAL_STATUS_UNRESOLVED


def sci_context_status(row: dict[str, str], *, not_applicable: bool = False) -> str:
    """Classify only what the existing record says about SCI context.

    The public-TF staging pass did not establish SCI context de novo. Explicit
    pending-SCI language is therefore unresolved, while records without such
    language remain not_assessed. This function never upgrades context.
    """
    if not_applicable:
        return SCI_CONTEXT_NOT_APPLICABLE
    text = " ".join(
        row.get(field, "")
        for field in ("disposition", "review_notes", "decision_basis", "context_triage_basis")
    ).casefold()
    if "sci" in text or "spinal cord" in text:
        return SCI_CONTEXT_UNRESOLVED
    return SCI_CONTEXT_NOT_ASSESSED


def mechanism_evidence_type(row: dict[str, str]) -> str:
    """Classify the proposed molecular bridge without upgrading evidence."""
    text = " ".join(
        row.get(field, "")
        for field in (
            "promotion_class", "module_route", "disposition", "review_notes",
            "mechanism_scope", "functional_mechanism", "regulator_mechanism",
        )
    ).casefold()
    if "ligand_rna" in text or "downstream_rna" in text or "ligand/protease" in text:
        return MECHANISM_SIGNAL_TO_RNA
    if "sequence_specific_tf" in text and "role_specific_noncanonical" not in text:
        return MECHANISM_DIRECT_TF
    if any(token in text for token in ("chromatin", "coactivator", "coregulator", "epigenetic")):
        return MECHANISM_CHROMATIN_COFACTOR
    if any(token in text for token in ("rna", "epitranscriptomic", "post_transcriptional", "rna_binding", "rna_processing")):
        return MECHANISM_RNA_LEVEL
    if any(token in text for token in ("ligand_receptor", "secreted_factor", "receptor_autoregulation", "pathway", "ligand_response", "relay")):
        return MECHANISM_SIGNAL_RELAY
    if any(token in text for token in ("protein_ptm", "protein_ptм", "kinase", "proteolysis", "target_protein", "cytoskeletal")):
        return MECHANISM_PROTEIN
    if any(token in text for token in ("complex", "architecture")):
        return MECHANISM_COMPLEX
    if any(token in text for token in ("expression", "perturbation", "response", "association")):
        return MECHANISM_ASSOCIATION
    return MECHANISM_UNRESOLVED


def graded_context_profile(
    row: dict[str, str],
    *,
    low_tier: bool = False,
    no_module_route: bool = False,
) -> dict[str, str]:
    """Return conservative context fields for a row awaiting context review."""
    if low_tier:
        lane = CONTEXT_LANE_LOW_TIER
    elif no_module_route:
        lane = CONTEXT_LANE_NO_ROUTE
    else:
        lane = CONTEXT_LANE_REVIEW
    return {
        "context_level_regulator": CONTEXT_L0,
        "context_level_target": CONTEXT_L0,
        "context_level_exact_pair": CONTEXT_L0,
        "context_evidence_scope": CONTEXT_SCOPE_NOT_ASSESSED,
        "context_evidence_basis": (
            "No graded CNS/spinal-cord context adjudication has been completed for this row; "
            "do not infer context from regulator or target identity alone."
        ),
        "context_promotion_lane": lane,
    }
