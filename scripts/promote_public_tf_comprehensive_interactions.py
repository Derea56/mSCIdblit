#!/usr/bin/env python3
"""Promote evidence-supported public-TF interactions into a broad catalog.

This is deliberately separate from the strict canonical TF/Module 22B write
path.  It promotes exact regulator-target-species findings for a comprehensive
interaction catalog, while retaining whether the mechanism is a sequence-
specific TF or a role-specific noncanonical interaction.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_ROOT = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/"
    "candidate_triage_v1/evidence_batches"
)
OUT_ROOT = ROOT / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1"
QUEUE_PATH = OUT_ROOT / "evidence_priority_queue.tsv"
OUTCOME_PATH = OUT_ROOT / "evidence_search_outcomes.tsv"
TFLink_AUDIT_GLOB = "tflink_*_source_audit.tsv"

PROMOTABLE_PREFIXES = ("functional_noncanonical_", "functional_chromatin_")
PROMOTABLE_EXACT = "functional_direct_binding_promotion_candidate"

# New independent primary-source hits found during the follow-up search. The
# original corroborating citation is retained; this field records the added
# source without rewriting the historical batch review.
ADDITIONAL_CORROBORATION = {
    ("msgn1", "dll3", "mouse"): "https://pubmed.ncbi.nlm.nih.gov/25371364/",
    ("bhlha15", "rab3d", "human"): "https://pmc.ncbi.nlm.nih.gov/articles/PMC6026875/",
}

# Reviewed literature cases that meet the broadened comprehensive-catalog
# gate: a peer-reviewed same-species pathway, expression, or post-transcriptional
# relationship is sufficient even when the historical batch status was not a
# strict direct TF-edge promotion. These remain separate from canonical TF and
# Module 22B materialization.
BROAD_LITERATURE_PROMOTIONS = {
    "public_tf_evidence_batch014_pair_19_2": {
        "promotion_class": "sequence_specific_tf_broad_functional_pair",
        "module_route": "general_public_interaction_catalog",
        "promotion_confidence": "broad_exact_binding_and_expression_evidence_with_corroboration",
        "promotion_basis": "MIST1 binds the RAB3D regulatory region and MIST1 induction/loss changes RAB3D expression in peer-reviewed secretory-cell models.",
    },
    "public_tf_evidence_batch025_pair_10_1": {
        "promotion_class": "role_specific_noncanonical_complex_expression_association",
        "module_route": "20B_target_interaction",
        "promotion_confidence": "broad_complex_dependent_expression_evidence_primary_only",
        "promotion_basis": "Peer-reviewed human-cell evidence places BAHD1 in a chromatin-repressor complex whose inhibition changes interferon-response expression including IFNB1; this is complex-dependent pathway evidence, not isolated BAHD1 promoter occupancy.",
    },
    "public_tf_evidence_batch016_pair_22_2": {
        "promotion_class": "role_specific_noncanonical_pathway_expression_association",
        "module_route": "20B_target_interaction",
        "promotion_confidence": "broad_pathway_expression_evidence_primary_only",
        "promotion_basis": "Peer-reviewed mouse atherosclerosis and foam-cell evidence links KDM1A perturbation to the PPARgamma-LXR-ABCA1 cholesterol-efflux pathway; this is an indirect pathway association, not direct Abca1-locus regulation.",
    },
    "public_tf_evidence_batch015_pair_04_1": {
        "promotion_class": "role_specific_noncanonical_post_transcriptional_association",
        "module_route": "general_public_interaction_catalog",
        "promotion_confidence": "broad_post_transcriptional_evidence_primary_only",
        "promotion_basis": "Peer-reviewed mouse adipogenesis evidence shows Hzf/Zfp385a binding the Cebpa mRNA 3-prime UTR, changing translation and adipogenesis; this is post-transcriptional RNA regulation, not promoter-TF evidence.",
    },
    "public_tf_evidence_batch015_pair_04_2": {
        "promotion_class": "role_specific_noncanonical_post_transcriptional_association",
        "module_route": "general_public_interaction_catalog",
        "promotion_confidence": "broad_post_transcriptional_evidence_primary_only",
        "promotion_basis": "Peer-reviewed mouse-cell evidence shows Hzf/Zfp385a binding the Tp53 mRNA 3-prime UTR and contributing to p53 expression after ARF induction; this is post-transcriptional RNA regulation, not promoter-TF evidence.",
    },
    # Second-pass promotions from the direction/species hold queue. These use
    # only evidence already recorded in the batch review files and preserve
    # the distinction between a broad interaction record and a canonical TF
    # or Module 22B write.
    "public_tf_evidence_batch016_pair_11_1": {
        "promotion_class": "role_specific_noncanonical_indirect_expression_association",
        "module_route": "20B_target_interaction",
        "promotion_confidence": "broad_mouse_perturbation_expression_evidence_primary_only",
        "promotion_basis": "Peer-reviewed mouse LPS-liver evidence associates BET/BRD4 perturbation with reduced A2M/A2m expression; no A2m-locus occupancy or BRD4-selective causal rescue was shown, so this is an indirect expression association.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch016_pair_11_2": {
        "promotion_class": "role_specific_noncanonical_indirect_expression_association",
        "module_route": "20B_target_interaction",
        "promotion_confidence": "broad_mouse_perturbation_expression_evidence_primary_only",
        "promotion_basis": "Peer-reviewed mouse renal-model evidence associates BET/BRD4 perturbation with increased Abca1 expression alongside PPAR-gamma/LXR changes; no Abca1-locus occupancy or BRD4-selective causal rescue was shown, so this is an indirect expression association.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch014_pair_14_1": {
        "promotion_class": "sequence_specific_tf_direct_binding_association",
        "module_route": "general_public_interaction_catalog",
        "promotion_confidence": "broad_mouse_direct_promoter_binding_primary_only",
        "promotion_basis": "Peer-reviewed mouse retinal evidence reports WT ZNF513 binding at the Arr3 promoter; activation/repression direction and SCI-cell context were not established, so this is a direct-binding association only.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch014_pair_14_2": {
        "promotion_class": "sequence_specific_tf_direct_binding_association",
        "module_route": "general_public_interaction_catalog",
        "promotion_confidence": "broad_mouse_direct_promoter_binding_primary_only",
        "promotion_basis": "Peer-reviewed mouse retinal evidence reports WT ZNF513 binding at the Pax6 promoter; activation/repression direction and SCI-cell context were not established, so this is a direct-binding association only.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch014_pair_14_3": {
        "promotion_class": "sequence_specific_tf_direct_binding_association",
        "module_route": "general_public_interaction_catalog",
        "promotion_confidence": "broad_mouse_direct_promoter_binding_with_corroboration",
        "promotion_basis": "Peer-reviewed mouse retinal evidence reports WT ZNF513 binding at the Rbp3 promoter, with an independent Rbp3-related study retained as corroboration; activation/repression direction and SCI-cell context were not established.",
        "literature_weight_override": ("independent_literature_corroborated", "2", "A_independent_literature_corroborated"),
    },
    "public_tf_evidence_batch014_pair_14_4": {
        "promotion_class": "sequence_specific_tf_direct_binding_association",
        "module_route": "general_public_interaction_catalog",
        "promotion_confidence": "broad_mouse_direct_promoter_binding_primary_only",
        "promotion_basis": "Peer-reviewed mouse retinal evidence reports WT ZNF513 binding at the Sp4 promoter; activation/repression direction and SCI-cell context were not established, so this is a direct-binding association only.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch015_pair_07_1": {
        "promotion_class": "sequence_specific_tf_reporter_binding_association",
        "module_route": "general_public_interaction_catalog",
        "promotion_confidence": "broad_human_promoter_reporter_evidence_primary_only",
        "promotion_basis": "Peer-reviewed promoter-element and reporter assays support HOXD10/HOX4D binding and transactivation involving the HOXD9/HOX4C promoter element; endogenous HOXD9 expression was not established, so this remains reporter-supported evidence.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch032_pair_21_4": {
        "promotion_class": "role_specific_noncanonical_coactivator_expression_association",
        "module_route": "general_public_interaction_catalog",
        "promotion_confidence": "broad_mouse_cofactor_binding_context_with_corroboration",
        "promotion_basis": "Peer-reviewed mouse MRTF-A/SRF target-program and cofactor studies support MRTF-A participation in Tagln transcriptional regulation; isolated Mrtfa perturbation was not established, so this is a coactivator association rather than a standalone TF edge.",
        "literature_weight_override": ("independent_literature_corroborated", "2", "A_independent_literature_corroborated"),
    },
    "public_tf_evidence_batch027_pair_07_1": {
        "promotion_class": "role_specific_noncanonical_ligand_receptor_response_association",
        "module_route": "20B_ligand_receptor_response",
        "promotion_confidence": "broad_human_ligand_receptor_response_primary_only",
        "promotion_basis": "Peer-reviewed human evidence supports ACVR1 mutation-dependent response to HMGB1 stimulation; this is a ligand–receptor response association routed to the receptor/ligand category, not HMGB1 transcriptional regulation of ACVR1.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch029_pair_01_4": {
        "promotion_class": "role_specific_noncanonical_protein_ptm_association",
        "module_route": "22B_target_interaction",
        "promotion_confidence": "broad_mouse_kinase_substrate_ptm_evidence_with_corroboration",
        "promotion_basis": "Peer-reviewed biochemical and cellular studies show GSK3B phosphorylates mouse Ccnd1/cyclin D1 at Thr286, promoting nuclear export and proteolytic turnover; this is an exact protein/PTM mechanism, not a canonical TF-target-gene edge.",
        "literature_weight_override": ("independent_literature_corroborated", "2", "A_independent_literature_corroborated"),
    },
    "public_tf_evidence_batch030_pair_10_2": {
        "promotion_class": "role_specific_noncanonical_protein_ptm_association",
        "module_route": "22B_target_interaction",
        "promotion_confidence": "broad_human_kinase_substrate_ptm_evidence_with_corroboration",
        "promotion_basis": "Peer-reviewed human-cell and mouse neural-progenitor studies show DYRK1A directly interacts with and phosphorylates Cyclin D1/CCND1 at Thr286, promoting nuclear export and turnover; this is an exact protein/PTM mechanism, not a canonical TF-target-gene edge.",
        "literature_weight_override": ("independent_literature_corroborated", "2", "A_independent_literature_corroborated"),
    },
    "public_tf_evidence_batch025_pair_09_2": {
        "promotion_class": "role_specific_noncanonical_protein_ptm_association",
        "module_route": "22B_target_interaction",
        "promotion_confidence": "broad_human_protein_ptm_stability_evidence_primary_only",
        "promotion_basis": "Peer-reviewed human cancer-cell and xenograft studies support direct PRMT5 binding and dimethylation of EphA2 at R816, reduced Cbl-mediated degradation, and EphA2 stabilization; this is a protein/PTM mechanism, not a canonical TF-target-gene edge.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch027_pair_04_1": {
        "promotion_class": "role_specific_noncanonical_ligand_receptor_relay",
        "module_route": "20B_ligand_receptor_relay",
        "promotion_confidence": "broad_human_ligand_receptor_relay_with_corroboration",
        "promotion_basis": "Peer-reviewed human studies support AMH binding through AMHR2 with ACVR1 as a type-I receptor component in responsive signaling systems; this is a ligand-receptor relay, not a TF-target interaction.",
        "literature_weight_override": ("independent_literature_corroborated", "2", "A_independent_literature_corroborated"),
    },
    "public_tf_evidence_batch030_pair_14_1": {
        "promotion_class": "role_specific_noncanonical_secreted_factor_expression_association",
        "module_route": "20B_secreted_factor_association;23B_secreted_factor_association;24B_secreted_factor_association",
        "promotion_confidence": "broad_human_secreted_factor_expression_association_primary_only",
        "promotion_basis": "Peer-reviewed human disease/expression evidence associates secreted ADA2/CECR1 with ANXA2 in the reported network; no direct binding or causal regulator-target mechanism was established, so this remains a secreted-factor association.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch025_pair_18_3": {
        "promotion_class": "role_specific_noncanonical_chromatin_occupancy_association",
        "module_route": "general_public_interaction_catalog",
        "promotion_confidence": "broad_mouse_direct_chromatin_occupancy_primary_only",
        "promotion_basis": "Peer-reviewed mouse hippocampal qChIP evidence reports CDYL occupancy at the Cacng3 locus; individual perturbation direction was not established, so this is chromatin occupancy rather than directed transcriptional regulation.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch025_pair_18_4": {
        "promotion_class": "role_specific_noncanonical_chromatin_occupancy_association",
        "module_route": "general_public_interaction_catalog",
        "promotion_confidence": "broad_mouse_direct_chromatin_occupancy_primary_only",
        "promotion_basis": "Peer-reviewed mouse hippocampal qChIP evidence reports CDYL occupancy at the Glra1 locus; individual perturbation direction was not established, so this is chromatin occupancy rather than directed transcriptional regulation.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch027_pair_08_1": {
        "promotion_class": "role_specific_noncanonical_rna_binding_association",
        "module_route": "20B_rna_association",
        "promotion_confidence": "broad_human_rna_binding_evidence_primary_only",
        "promotion_basis": "Human eCLIP/RNA-binding evidence supports FXR2 association with the ABCA1 transcript; no genomic promoter occupancy or transcriptional direction was established, so this is an RNA-binding association.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch025_pair_09_1": {
        "promotion_class": "role_specific_noncanonical_indirect_expression_association",
        "module_route": "20B_target_interaction",
        "promotion_confidence": "broad_human_selective_perturbation_expression_evidence_primary_only",
        "promotion_basis": "Peer-reviewed human adenoid-cystic-carcinoma cell and organoid evidence shows selective PRMT5 inhibition reduces AXL expression; direct PRMT5 occupancy and genetic causal rescue were not established, so this is an indirect expression association.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch024_pair_09_4": {
        "promotion_class": "role_specific_noncanonical_indirect_expression_association",
        "module_route": "20B_target_interaction",
        "promotion_confidence": "broad_human_perturbation_expression_evidence_primary_only",
        "promotion_basis": "Peer-reviewed human CD4 differentiation evidence shows full-length TET1 overexpression changes IL5 expression relative to a catalytically inactive control; direct TET1 occupancy was not established, so this is an expression association.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch023_pair_16_4": {
        "promotion_class": "role_specific_noncanonical_epigenetic_locus_association",
        "module_route": "20B_chromatin_epigenetic_association;23B_chromatin_epigenetic_association",
        "promotion_confidence": "broad_mouse_locus_epigenetic_evidence_primary_only",
        "promotion_basis": "Peer-reviewed mouse zygote evidence supports TET3-dependent protection/demethylation at the Agrn promoter CGI; direct occupancy and standalone expression direction were not established, so this is an epigenetic locus association.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch030_pair_08_3": {
        "promotion_class": "role_specific_noncanonical_chromatin_expression_association",
        "module_route": "22B_chromatin_expression_association",
        "promotion_confidence": "broad_human_chromatin_factor_expression_evidence_primary_only",
        "promotion_basis": "Peer-reviewed human evidence shows SPT16/FACT depletion changes CCND1 protein expression; direct SPT16 occupancy and a CCND1-specific causal mechanism were not established, so this is a chromatin-factor expression association.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch009_pair_11_3": {
        "promotion_class": "role_specific_noncanonical_indirect_expression_association",
        "module_route": "20B_target_interaction",
        "promotion_confidence": "broad_human_perturbation_expression_with_nearest_peak",
        "promotion_basis": "Peer-reviewed human ZNF507-disruption evidence reports an IGF2R expression change with a nearby ZNF507 peak; direct promoter causality was not established, so this is an indirect expression association.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch001_pair_086": {
        "promotion_class": "role_specific_noncanonical_indirect_expression_association",
        "module_route": "20B_target_interaction",
        "promotion_confidence": "broad_human_perturbation_expression_evidence_primary_only",
        "promotion_basis": "Peer-reviewed human THP-1 foam-cell evidence shows ZNF580 overexpression increases ABCA1 mRNA/protein and silencing decreases it; direct occupancy and independent corroboration were not established, so this is an indirect expression association.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch029_pair_16_3": {
        "promotion_class": "role_specific_noncanonical_rna_processing_association",
        "module_route": "20B_rna_processing_association",
        "promotion_confidence": "broad_human_rna_processing_context_primary_only",
        "promotion_basis": "Peer-reviewed human evidence places U2AF2 in an APOA1-related RNA-processing/protein-complex context; sequence-specific transcriptional regulation of APOA1 was not established, so this is routed as RNA-processing evidence.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
    "public_tf_evidence_batch021_pair_10_2": {
        "promotion_class": "role_specific_noncanonical_indirect_expression_association",
        "module_route": "20B_target_interaction",
        "promotion_confidence": "broad_human_pathway_expression_evidence_primary_only",
        "promotion_basis": "Peer-reviewed human evidence links YAP-pathway activation with increased ACKR2 expression and pharmacologic pathway blockade; direct YAP1 occupancy and YAP1-specific causal isolation were not established, so this is an indirect pathway-expression association.",
        "literature_weight_override": ("independent_literature_single_source", "1", "B_independent_literature_single_source"),
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def merge_citations(*values: str) -> str:
    citations: list[str] = []
    seen: set[str] = set()
    for value in values:
        for citation in value.split(";"):
            citation = citation.strip()
            if citation and citation not in seen:
                seen.add(citation)
                citations.append(citation)
    return ";".join(citations)


def load_outcome_citations(path: Path) -> dict[tuple[str, str, str], str]:
    if not path.exists():
        return {}
    result: dict[tuple[str, str, str], str] = {}
    for row in read_tsv(path):
        key = (row.get("regulator_symbol", "").casefold(), row.get("target_symbol", "").casefold(), row.get("species_scope", ""))
        result[key] = merge_citations(result.get(key, ""), row.get("source_citations", ""))
    return result


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def is_promotable(status: str) -> bool:
    return status == PROMOTABLE_EXACT or status.startswith(PROMOTABLE_PREFIXES)


def promotion_class(status: str) -> str:
    if status == "tflink_source_table_exact_pair":
        if "database_profile_hold" in CURRENT_SOURCE_REVIEW_FILE:
            return "tflink_source_table_small_scale_or_curated_association" if CURRENT_TFLINK_SMALL_SCALE == "Yes" else "tflink_source_table_high_throughput_association"
        return "sequence_specific_tf_high_throughput_binding_association"
    if status == PROMOTABLE_EXACT:
        return "sequence_specific_tf_exact_pair"
    return "role_specific_noncanonical_exact_pair"


def module_route(row: dict[str, str]) -> str:
    key = (row["regulator_key"], row["target_symbol"].casefold(), row["species_scope"])
    special = {
        ("nfam1", "il2", "mouse"): "21B_receptor_relay_and_cytokine",
        ("igf1r", "apob", "human"): "24B_lipid_and_vascular_transport",
        ("f10", "ccn1", "human"): "24B_ligand_protease_and_downstream_rna",
    }
    if key in special:
        return special[key]
    modules = row.get("target_graph_modules", "")
    return ";".join(f"{module}_target_interaction" for module in modules.split(";") if module) or "general_public_interaction_catalog"


def confidence_label(row: dict[str, str], additional_citation: str = "") -> str:
    if row["exact_pair_status"] == "tflink_source_table_exact_pair":
        if row.get("tflink_small_scale_evidence") == "Yes":
            return "tflink_exact_small_scale_or_curated_association_record_primary_source_metadata"
        return "tflink_exact_high_throughput_binding_record_primary_source_metadata"
    if row["exact_pair_status"] == PROMOTABLE_EXACT:
        return "strong_exact_pair_evidence_context_limited"
    if row.get("corroborating_citation") or additional_citation:
        return "exact_role_specific_evidence_with_corroboration"
    return "exact_role_specific_evidence_primary_only"


def followup_gap(row: dict[str, str], additional_citation: str = "") -> tuple[str, str]:
    if row["exact_pair_status"] == "tflink_source_table_exact_pair":
        return (
            "edge_specific_primary_literature_and_function",
            "Resolve the underlying experiment accession or original paper and assess locus specificity, target expression direction, perturbation, and model context; TFLink metadata establish ChIP-seq association but not causal regulation.",
        )
    if row["exact_pair_status"] == PROMOTABLE_EXACT:
        if row.get("corroborating_citation") or additional_citation:
            return (
                "orthogonal_mechanism_and_context",
                "Seek an orthogonal assay or perturbation and confirm target presence, direction, and model boundaries.",
            )
        return (
            "independent_corroboration_and_context",
            "Seek an independent primary study plus target-cell or tissue-context evidence; retain the exact species and direction.",
        )
    if not row.get("corroborating_citation"):
        return (
            "independent_corroboration",
            "Seek an independent primary study with the same regulator, target, species, and mechanism.",
        )
    return (
        "orthogonal_mechanism_and_context",
        "Seek an orthogonal assay or perturbation and confirm target presence, direction, and model boundaries.",
    )


def literature_weight(
    row: dict[str, str],
    additional_citation: str = "",
    override: dict[str, object] | None = None,
) -> tuple[str, str, str]:
    """Classify independent literature separately from aggregator citations."""
    if override and override.get("literature_weight_override"):
        return tuple(override["literature_weight_override"])  # type: ignore[arg-type]
    if row["exact_pair_status"] == "tflink_source_table_exact_pair":
        return "not_identified_outside_tflink_source_table", "0", "C_tflink_source_table_only"
    citations = []
    for value in (row.get("primary_citation", ""), row.get("corroborating_citation", ""), additional_citation):
        citations.extend(part.strip() for part in value.split(";") if part.strip())
    unique_citations = list(dict.fromkeys(citations))
    if row.get("corroborating_citation") or additional_citation:
        return "independent_literature_corroborated", str(len(unique_citations)), "A_independent_literature_corroborated"
    if unique_citations:
        return "independent_literature_single_source", str(len(unique_citations)), "B_independent_literature_single_source"
    return "not_identified", "0", "D_no_literature_support"


def main() -> int:
    global CURRENT_SOURCE_REVIEW_FILE, CURRENT_TFLINK_SMALL_SCALE
    outcome_citations = load_outcome_citations(OUTCOME_PATH)
    source_rows: list[dict[str, str]] = []
    for path in sorted(EVIDENCE_ROOT.glob("batch_*/public_tf_evidence_review_batch*_pairs.tsv")):
        for row in read_tsv(path):
            if is_promotable(row["exact_pair_status"]) or row["review_id"] in BROAD_LITERATURE_PROMOTIONS:
                copied = dict(row)
                copied["source_review_file"] = str(path.relative_to(ROOT))
                source_rows.append(copied)

    # The original queue classified these as database-only because the GMT
    # snapshot had no pair-level metadata.  Once the per-protein TFLink target
    # tables are recovered, exact rows with method, PubMed ID, organism, and
    # source database become exportable to the broad binding/association tier.
    # They remain separate from functional and canonical promotions.
    audit_paths = sorted(OUT_ROOT.glob(TFLink_AUDIT_GLOB))
    if audit_paths and QUEUE_PATH.exists():
        queue_by_key = {row["queue_key"]: row for row in read_tsv(QUEUE_PATH)}
        tflink_rows: list[dict[str, str]] = []
        for audit_path in audit_paths:
            for audit in read_tsv(audit_path):
                if audit.get("exact_pair_match") != "true":
                    continue
                queue = queue_by_key.get(audit["queue_key"])
                if not queue:
                    raise SystemExit(f"TFLink audit row has no queue row: {audit['queue_key']}")
                pmid_urls = ";".join(
                    f"https://pubmed.ncbi.nlm.nih.gov/{pmid.strip()}/"
                    for pmid in audit.get("pubmed_id", "").split(";")
                    if pmid.strip()
                )
                source_suffix = audit["source_record_id"].replace(":", "_")
                review_id = f"tflink_source_{audit['queue_key'].replace('|', '_')}_{source_suffix}"
                tflink_rows.append({
                "review_id": review_id,
                "batch_id": "TFLink_database_only_source_recovery_v1",
                "batch_rank": "",
                "regulator_key": queue["queue_key"].split("|")[0],
                "regulator_symbol": audit["regulator_symbol"],
                "species_scope": audit["species_scope"],
                "source_registry": "TFLink",
                "source_record_id": audit["source_record_id"],
                "raw_tf_symbol": audit["raw_tf_symbol"],
                "target_symbol": audit["target_symbol"],
                "target_graph_modules": audit["target_graph_modules"],
                "candidate_membership_status": "database_membership_plus_exact_tflink_source_table_record",
                "exact_pair_search_url": pmid_urls or audit["tflink_source_url"],
                "exact_pair_status": "tflink_source_table_exact_pair",
                "regulator_general_evidence_status": "TFLink target table reports an exact regulator-target record from a ChIP-seq-derived source.",
                "target_cell_presence_status": "not_assessed_in_tflink_source_table",
                "binding_or_association_status": (
                    f"Exact TFLink target-table row; detection_method={audit['detection_method']}; "
                    f"source_database={audit['source_database']}; large-scale association record."
                ),
                "downstream_expression_or_perturbation_status": "not_assessed_in_tflink_source_table",
                "downstream_activation_status": "not_assessed",
                "upstream_relay_status": "not_assessed",
                "disposition": "promote_to_comprehensive_binding_association_catalog",
                "primary_citation": pmid_urls,
                "corroborating_citation": "",
                "near_match_exclusions": "Exact TFLink organism match; no cross-species or reverse-direction inference. ChIP-seq association does not establish causal expression or activation direction.",
                "review_notes": (
                    "Recovered from the TFLink per-protein target table rather than GMT membership alone. "
                    "The attached PubMed ID identifies the source database paper; the underlying experiment accession/original paper was not supplied in this TFLink row."
                ),
                "exportable": "true",
                "canonical_write_performed": "false",
                "source_review_file": str(audit_path.relative_to(ROOT)),
                "tflink_source_database": audit["source_database"],
                "tflink_detection_method": audit["detection_method"],
                "tflink_pubmed_id": audit["pubmed_id"],
                "tflink_small_scale_evidence": audit["small_scale_evidence"],
                "tflink_source_url": audit["tflink_source_url"],
                "tflink_raw_snapshot_path": audit["raw_snapshot_path"],
                "tflink_raw_snapshot_sha256": audit["raw_snapshot_sha256"],
                "tflink_source_selection": audit_path.stem.replace("tflink_", "").replace("_source_audit", ""),
                "promotion_basis_override": (
                    "Exact regulator-target-species match recovered from TFLink's per-protein target table with "
                    f"{audit['detection_method']} and source database {audit['source_database']}; "
                    "promoted as high-throughput binding/association evidence only."
                ),
                })
        source_rows.extend(tflink_rows)

    source_rows.sort(key=lambda row: row["review_id"])
    if len(source_rows) != len({row["review_id"] for row in source_rows}):
        raise SystemExit("duplicate review IDs in promotion input")

    promoted_fields = list(source_rows[0]) + [
        "promotion_id", "promotion_scope", "promotion_class", "module_route",
        "promotion_confidence", "promotion_basis", "canonical_write_performed",
    ]
    promoted: list[dict[str, str]] = []
    followup: list[dict[str, str]] = []
    for index, row in enumerate(source_rows, start=1):
        status = row["exact_pair_status"]
        broad_override = BROAD_LITERATURE_PROMOTIONS.get(row["review_id"])
        CURRENT_SOURCE_REVIEW_FILE = row.get("source_review_file", "")
        CURRENT_TFLINK_SMALL_SCALE = row.get("tflink_small_scale_evidence", "")
        klass = broad_override["promotion_class"] if broad_override else promotion_class(status)
        route = broad_override["module_route"] if broad_override else module_route(row)
        pair_key = (row["regulator_key"], row["target_symbol"].casefold(), row["species_scope"])
        additional_citation = ADDITIONAL_CORROBORATION.get(pair_key, "")
        if broad_override:
            additional_citation = merge_citations(additional_citation, outcome_citations.get(pair_key, ""))
        confidence = broad_override["promotion_confidence"] if broad_override else confidence_label(row, additional_citation)
        literature_status, literature_count, evidence_weight_tier = literature_weight(row, additional_citation, broad_override)
        promotion_id = f"public_tf_comprehensive_{index:03d}"
        item = dict(row)
        item.update({
            "promotion_id": promotion_id,
            "promotion_scope": "comprehensive_public_interaction_catalog",
            "promotion_class": klass,
            "module_route": route,
            "promotion_confidence": confidence,
            "independent_literature_support_status": literature_status,
            "independent_literature_source_count": literature_count,
            "evidence_weight_tier": evidence_weight_tier,
            "promotion_basis": broad_override["promotion_basis"] if broad_override else row.get("promotion_basis_override", row["binding_or_association_status"] + "; " + row["downstream_expression_or_perturbation_status"]),
            "additional_corroborating_citation": additional_citation,
            "exportable": "true",
            "canonical_write_performed": "false",
            "module22b_write_performed": "false",
        })
        promoted.append(item)
        gap, requirement = followup_gap(row, additional_citation)
        followup.append({
            "followup_id": f"public_tf_comprehensive_followup_{index:03d}",
            "promotion_id": promotion_id,
            "regulator_symbol": row["regulator_symbol"],
            "target_symbol": row["target_symbol"],
            "species_scope": row["species_scope"],
            "module_route": route,
            "promotion_class": klass,
            "independent_literature_support_status": literature_status,
            "independent_literature_source_count": literature_count,
            "evidence_weight_tier": evidence_weight_tier,
            "current_primary_citation": row["primary_citation"],
            "current_corroborating_citation": ";".join(filter(None, [row["corroborating_citation"], additional_citation])),
            "current_cell_or_model": row["target_cell_presence_status"],
            "evidence_gap": gap,
            "next_evidence_requirement": requirement,
            "exact_pair_search_url": row["exact_pair_search_url"],
            "status": "followup_needed",
        })

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    common_fields = [
        "promotion_id", "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol",
        "species_scope", "source_registry", "source_record_id", "raw_tf_symbol", "target_symbol",
        "target_graph_modules", "candidate_membership_status", "exact_pair_search_url", "exact_pair_status",
        "regulator_general_evidence_status", "target_cell_presence_status", "binding_or_association_status",
        "downstream_expression_or_perturbation_status", "downstream_activation_status", "upstream_relay_status",
        "disposition", "primary_citation", "corroborating_citation", "additional_corroborating_citation", "near_match_exclusions", "review_notes",
        "exportable", "canonical_write_performed", "module22b_write_performed", "source_review_file", "promotion_scope", "promotion_class",
        "module_route", "promotion_confidence", "promotion_basis",
        "independent_literature_support_status", "independent_literature_source_count", "evidence_weight_tier",
        "tflink_source_database", "tflink_detection_method", "tflink_pubmed_id",
        "tflink_small_scale_evidence", "tflink_source_url", "tflink_raw_snapshot_path",
        "tflink_raw_snapshot_sha256", "tflink_source_selection",
    ]
    write_tsv(OUT_ROOT / "promoted_interactions.tsv", common_fields, promoted)
    write_tsv(OUT_ROOT / "promotion_followup_evidence_queue.tsv", list(followup[0]), followup)

    keys = [(r["regulator_key"], r["target_symbol"], r["species_scope"], r["source_record_id"]) for r in promoted]
    validation = {
        "status": "pass" if (
            len(keys) == len(set(keys))
            and all(r["exportable"] == "true" for r in promoted)
            and all(r["canonical_write_performed"] == "false" for r in promoted)
            and all(r["module22b_write_performed"] == "false" for r in promoted)
        ) else "fail",
        "checks": {
            "promoted_rows": len(promoted),
            "unique_provenance_keys": len(set(keys)),
            "duplicate_provenance_keys": len(keys) - len(set(keys)),
            "exportable_true_rows": sum(r["exportable"] == "true" for r in promoted),
            "canonical_write_true_rows": sum(r["canonical_write_performed"] == "true" for r in promoted),
            "module22b_write_true_rows": sum(r["module22b_write_performed"] == "true" for r in promoted),
            "followup_rows": len(followup),
        },
    }
    (OUT_ROOT / "promotion_validation.json").write_text(json.dumps(validation, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    manifest = {
        "status": "exportable_staging_only",
        "promotion_scope": "comprehensive_public_interaction_catalog",
        "canonical_write_performed": False,
        "module22b_write_performed": False,
        "promotion_class_counts": dict(Counter(r["promotion_class"] for r in promoted)),
        "module_route_counts": dict(Counter(r["module_route"] for r in promoted)),
        "promotion_confidence_counts": dict(Counter(r["promotion_confidence"] for r in promoted)),
        "independent_literature_support_counts": dict(Counter(r["independent_literature_support_status"] for r in promoted)),
        "evidence_weight_tier_counts": dict(Counter(r["evidence_weight_tier"] for r in promoted)),
        "promoted_rows": len(promoted),
        "followup_rows": len(followup),
        "validation": str((OUT_ROOT / "promotion_validation.json").relative_to(ROOT)),
        "outputs": [
            str((OUT_ROOT / "promoted_interactions.tsv").relative_to(ROOT)),
            str((OUT_ROOT / "promotion_followup_evidence_queue.tsv").relative_to(ROOT)),
            str((OUT_ROOT / "promotion_validation.json").relative_to(ROOT)),
        ],
        "policy": [
            "Exact regulator-target-species findings can be exported for a comprehensive interaction catalog even when the model is not an SCI target cell.",
            "Noncanonical mechanisms remain role-specific and are not converted into sequence-specific TF edges.",
            "Canonical TF and Module 22B writes remain separate and were not performed.",
            "TFLink source-table rows are promoted only as high-throughput binding/association records; the attached database-paper citation is not treated as pair-specific functional validation.",
            "Species, model, assay, direction, source record, citation, and limitations are preserved from the reviewed row.",
        ],
    }
    (OUT_ROOT / "promotion_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0 if validation["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
