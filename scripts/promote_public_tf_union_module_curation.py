#!/usr/bin/env python3
"""Materialize a manually adjudicated public-TF curation batch.

This is an evidence-promotion ledger, not a canonical database migration.  It
keeps public TF-target assertions in Module 22B, records exact-pair primary
and corroborating citations, and emits explicit holds for target mismatches or
cross-module citation reuse.  It never writes the frozen mechanism graph or
the local PostgreSQL database.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_v1"
DEFAULT_OUTPUT = DEFAULT_INPUT / "module_curation" / "batch001"


def decision(
    species: str,
    tf: str,
    target: str,
    status: str,
    evidence_scope: str,
    effect: str,
    confidence: str,
    primary: str,
    note: str,
    *,
    corroborating: str = "",
    excluded: str = "",
    cell_type: str = "",
    stimulus: str = "",
    reuse: str = "",
    cross_module: str = "",
    hold_reason: str = "",
) -> dict[str, str]:
    return {
        "species": species,
        "tf": tf,
        "target": target,
        "promotion_decision": status,
        "evidence_scope": evidence_scope,
        "effect_polarity": effect,
        "confidence_tier": confidence,
        "primary_pmids": primary,
        "corroborating_pmids": corroborating,
        "excluded_pmids": excluded,
        "cell_type_context": cell_type,
        "stimulus_context": stimulus,
        "reuse_audit_status": reuse,
        "cross_module_overlap": cross_module,
        "hold_reason": hold_reason,
        "curation_note": note,
    }


# Each row is a pair-level adjudication.  The source-record links are joined
# below from the public snapshot, so a pair can have several TRRUST/DoRothEA
# records without losing source-specific provenance.
DECISIONS = [
    decision("human", "TP53", "BCL2", "promote_to_22B_staging", "perturbation_response", "context_dependent", "medium", "19411072", "RITA-reactivated p53 represses BCL2 in human cancer models; independent BCL2 repression paper corroborates the shared p53 paper.", corroborating="11313951", cell_type="human cancer cell lines", stimulus="RITA-mediated p53 reactivation", reuse="shared_primary_with_independent_BCL2_corroboration"),
    decision("human", "TP53", "CTNNB1", "promote_to_22B_staging", "perturbation_response", "context_dependent", "medium", "19411072", "RITA-reactivated p53 downregulates beta-catenin/CTNNB1 in the tested human cancer models; retained as context-limited, not direct occupancy.", cell_type="human cancer cell lines", stimulus="RITA-mediated p53 reactivation", reuse="shared_primary_group_corroborated_on_BCL2_MCL1"),
    decision("human", "TP53", "MAP4", "promote_to_22B_staging", "perturbation_response", "context_dependent", "medium", "19411072", "RITA-reactivated p53 represses MAP4 in the tested human cancer models; no direct-binding claim is made.", cell_type="human cancer cell lines", stimulus="RITA-mediated p53 reactivation", reuse="shared_primary_group_corroborated_on_BCL2_MCL1"),
    decision("human", "TP53", "MCL1", "promote_to_22B_staging", "perturbation_response", "context_dependent", "medium", "19411072", "RITA-reactivated p53 represses MCL1; independent p53-dependent MCL1 promoter work corroborates the shared p53 paper.", corroborating="18208354", cell_type="human cancer cell lines", stimulus="RITA-mediated p53 reactivation", reuse="shared_primary_with_independent_MCL1_corroboration"),
    decision("human", "TP53", "MYC", "promote_to_22B_staging", "perturbation_response", "context_dependent", "medium", "19411072", "RITA-reactivated p53 downregulates c-MYC in the tested human cancer models; retained as perturbation response rather than direct promoter binding.", cell_type="human cancer cell lines", stimulus="RITA-mediated p53 reactivation", reuse="shared_primary_group_corroborated_on_BCL2_MCL1"),
    decision("human", "TP53", "DDR1", "promote_to_22B_staging", "direct_binding", "activating_target", "high", "12628922", "Independent primary evidence identifies DDR1 as a direct p53 transcriptional target. The overlapping Module 23B collagen citation is not reused.", excluded="21398698", cell_type="human cancer models", stimulus="DNA damage/p53 induction", reuse="independent_of_module23b_citation", cross_module="23B",),

    decision("human", "JUN", "MMP1", "promote_to_22B_staging", "complex_cooperative_promoter", "context_dependent", "medium", "9334186", "c-Jun/c-Fos/Ets promoter cooperation supports MMP1 regulation; an independent MMP1 promoter study corroborates JUN/AP-1 involvement.", corroborating="9178763", cell_type="human promoter/in-vitro systems", stimulus="AP-1/Ets promoter activation", reuse="shared_AP1_primary_with_independent_JUN_MMP1_corroboration"),
    decision("human", "JUN", "MMP3", "promote_to_22B_staging", "complex_cooperative_promoter", "context_dependent", "medium", "9334186", "c-Jun/c-Fos/Ets promoter cooperation supports MMP3/stromelysin regulation; the edge is retained as complex-dependent, not Jun-only universal control.", cell_type="human promoter/in-vitro systems", stimulus="AP-1/Ets promoter activation", reuse="shared_AP1_primary_group_corroborated_on_JUN_MMP1"),
    decision("human", "FOS", "MMP1", "promote_to_22B_staging", "complex_cooperative_promoter", "context_dependent", "medium", "9334186", "c-Fos/c-Jun/Ets promoter cooperation supports MMP1 regulation; independent AP-1-site work shows c-Fos-containing complexes at the MMP1 promoter.", corroborating="8785586", cell_type="human promoter/in-vitro systems", stimulus="AP-1/Ets promoter activation", reuse="shared_AP1_primary_with_independent_FOS_MMP1_corroboration"),
    decision("human", "FOS", "MMP3", "promote_to_22B_staging", "perturbation_response", "context_dependent", "medium", "9334186", "c-Fos/c-Jun/Ets promoter cooperation plus c-fos knockout evidence supports MMP3 induction dependence in comparator systems.", corroborating="8039503", cell_type="human and mouse fibroblast comparator systems", stimulus="growth-factor/oncogene-induced metalloprotease expression", reuse="shared_AP1_primary_with_independent_FOS_MMP3_corroboration"),

    decision("human", "MYC", "HLA-B", "promote_to_22B_staging", "direct_binding", "repressing_target", "medium", "8206526", "The primary paper supports c-MYC-mediated repression of HLA-B promoter activity. The public activation label is a direction conflict resolved in favor of the pair-specific primary experiment.", cell_type="human melanoma cells and c-MYC transfectants", stimulus="c-MYC overexpression", reuse="single_target_primary_direction_conflict_resolved"),

    decision("human", "STAT1", "CCL3", "promote_to_22B_staging", "perturbation_response", "activating_target", "medium", "16628196", "STAT1 perturbation supports poly(I:C)-induced CCL3/MIP-1alpha response; independent ChIP/perturbation work corroborates STAT1–CCL3 regulation.", corroborating="38730482", cell_type="human keratinocytes; human myeloid comparator", stimulus="poly(I:C)/TLR3 or inflammatory stimulation", reuse="shared_STAT1_primary_with_independent_CCL3_corroboration"),
    decision("human", "STAT1", "IRF7", "promote_to_22B_staging", "perturbation_response", "activating_target", "medium", "16628196", "The dsRNA/TLR3 study supports STAT1-SOCS1 regulation of IRF7 response; retained as context-limited pathway-response evidence.", cell_type="human keratinocytes", stimulus="poly(I:C)/TLR3-induced innate immune response", reuse="shared_STAT1_primary_group_corroborated_on_CCL3"),
    decision("human", "STAT1", "TLR3", "promote_to_22B_staging", "perturbation_response", "activating_target", "medium", "16628196", "The dsRNA study supports STAT1-linked TLR3 regulation; this remains a TF-target record in Module 22B and does not create a Module 20 receptor edge.", cell_type="human keratinocytes", stimulus="poly(I:C)/TLR3-induced innate immune response", reuse="shared_STAT1_primary_group_corroborated_on_CCL3"),

    decision("human", "HIF1A", "ALDOA", "promote_to_22B_staging", "direct_binding", "activating_target", "high", "8955077", "HIF-1 binding-site and promoter-mutagenesis evidence supports ALDOA regulation under hypoxia.", cell_type="mammalian cultured cells and promoter constructs", stimulus="hypoxia", reuse="shared_HIF1_primary_group_corroborated_on_VEGFA"),
    decision("human", "HIF1A", "ENO1", "promote_to_22B_staging", "direct_binding", "activating_target", "high", "8955077", "HIF-1 binding-site and promoter-mutagenesis evidence supports ENO1 regulation under hypoxia.", cell_type="mammalian cultured cells and promoter constructs", stimulus="hypoxia", reuse="shared_HIF1_primary_group_corroborated_on_VEGFA"),
    decision("human", "HIF1A", "LDHA", "promote_to_22B_staging", "direct_binding", "activating_target", "high", "8955077", "HIF-1 binding-site and promoter-mutagenesis evidence supports LDHA regulation under hypoxia.", cell_type="mammalian cultured cells and promoter constructs", stimulus="hypoxia", reuse="shared_HIF1_primary_group_corroborated_on_VEGFA"),
    decision("human", "HIF1A", "VEGFA", "promote_to_22B_staging", "direct_binding", "activating_target", "high", "8756616", "Independent HIF-1/VEGF HRE promoter evidence supports VEGFA; a second primary study corroborates HIF1A/VEGFA promoter regulation. The shared Module 20B SCUBE2-KDR citation is not reused.", corroborating="15735682", cell_type="cultured mammalian/human cancer comparator systems", stimulus="hypoxia", reuse="independent_pair_evidence_replaces_incidental_module20b_overlap", cross_module="20B"),
    decision("mouse", "Hif1a", "Vegfa", "promote_to_22B_staging", "direct_binding", "activating_target", "medium", "28686658", "Mouse HIF binding-site deletion in the Vegfa promoter reduces Vegfa expression and vascular wound-healing outputs; comparator context is wound healing, not SCI.", cell_type="mouse wound-healing model", stimulus="wound healing/hypoxia", reuse="mouse_pair_primary_context_limited"),

    decision("human", "SP1", "C4A", "promote_to_22B_staging", "direct_binding", "activating_target", "high", "9574539", "EMSA, DNase footprinting, and promoter mutagenesis support an Sp1 site required for human C4 promoter transcription; this is Module 22B TF-target evidence only.", cell_type="human HepG2 and HeLa promoter assays", stimulus="basal promoter transcription", reuse="shared_C4_promoter_single_primary; no_exact_independent_pair_located", cross_module="24B"),
    decision("human", "SP1", "C4B", "promote_to_22B_staging", "direct_binding", "activating_target", "high", "9574539", "The shared C4A/C4B promoter study supports Sp1-dependent C4 transcription; no separate complement receptor/function edge is inferred.", cell_type="human HepG2 and HeLa promoter assays", stimulus="basal promoter transcription", reuse="shared_C4_promoter_single_primary; no_exact_independent_pair_located", cross_module="24B"),

    decision("human", "ETS1", "CA9", "promote_to_22B_staging", "perturbation_response", "context_dependent", "medium", "18381358", "ETS1 reporter/siRNA evidence supports context-dependent CA9 regulation with HIF-1 cooperation; no universal hypoxia rule is inferred.", cell_type="human lung epithelial cells", stimulus="high cell density/hypoxia-related induction", reuse="shared_ETS1_primary_group"),
    decision("human", "ETS1", "NDRG1", "promote_to_22B_staging", "perturbation_response", "context_dependent", "medium", "18381358", "ETS1 reporter/siRNA evidence supports context-dependent NDRG1 regulation with HIF-1 cooperation.", cell_type="human lung epithelial cells", stimulus="high cell density/hypoxia-related induction", reuse="shared_ETS1_primary_group"),
    decision("mouse", "Ets1", "Ndrg1", "promote_to_22B_staging", "perturbation_response", "context_dependent", "medium", "18381358", "The primary study includes mouse fibroblast comparator evidence for Ets1/Ndrg1 response; retained as species-specific context-limited evidence.", cell_type="mouse fibroblast comparator", stimulus="high cell density/hypoxia-related induction", reuse="shared_ETS1_primary_group"),

    decision("human", "RUNX1", "CCL3", "promote_to_22B_staging", "direct_binding", "activating_target", "high", "12771199", "RUNX1 binding at two CCL3/MIP-1alpha promoter sites, ChIP enrichment, and promoter mutation support direct regulation in Jurkat cells.", cell_type="human Jurkat T cells", stimulus="PMA/PHA promoter activation", reuse="single_pair_primary"),
    decision("human", "GATA3", "FOXC1", "promote_to_22B_staging", "direct_binding", "repressing_target", "high", "22120723", "GATA3/BRCA1 promoter binding and repression support the human GATA3→FOXC1 pair in basal-like breast cancer cells.", cell_type="human basal-like breast cancer cell lines", stimulus="BRCA1/GATA3 corepressor context", reuse="single_pair_primary"),
    decision("human", "NFKB2", "CCND2", "promote_to_22B_staging", "perturbation_response", "activating_target", "medium", "18504428", "p100/NFKB2 perturbation reduces Tax-induced CCND2 promoter activation and cell-cycle output in T-cell/HTLV-I comparator systems.", cell_type="human T cells with HTLV-I Tax", stimulus="HTLV-I Tax-induced NF-kappaB activation", reuse="shared_NFKB2_primary; corroboration_search_attempted_not_located"),
    decision("human", "NFKB2", "CDK6", "promote_to_22B_staging", "perturbation_response", "activating_target", "medium", "18504428", "p100/NFKB2 perturbation reduces Tax-induced CDK6 promoter activation in the tested T-cell comparator system; not direct occupancy.", cell_type="human T cells with HTLV-I Tax", stimulus="HTLV-I Tax-induced NF-kappaB activation", reuse="shared_NFKB2_primary; corroboration_search_attempted_not_located"),

    decision("human", "STAT1", "CCR1", "hold_exact_pair_review", "unresolved", "unknown", "uncertain", "16628196", "The cited dsRNA study supports CCL3, IRF7, and TLR3 responses but does not establish STAT1→CCR1; hold rather than transfer CCL3 evidence to a receptor target.", cell_type="human keratinocytes", stimulus="poly(I:C)/TLR3-induced innate immune response", hold_reason="priority paper does not support exact CCR1 target"),
    decision("human", "HIF1A", "EPO", "hold_exact_pair_review", "unresolved", "unknown", "uncertain", "8955077", "The cited HIF-1 paper is centered on ALDOA, ENO1, and LDHA HREs; EPO is not promoted from that citation without exact-pair verification.", cell_type="mammalian cultured cells and promoter constructs", stimulus="hypoxia", hold_reason="priority paper target scope mismatch"),
    decision("human", "JUN", "MMP13", "hold_exact_pair_review", "unresolved", "unknown", "uncertain", "9334186", "The reviewed paper supports MMP1/MMP3 promoter cooperation, not a sufficiently specific JUN→MMP13 claim.", cell_type="human promoter/in-vitro systems", stimulus="AP-1/Ets promoter activation", hold_reason="primary paper does not establish exact MMP13 pair"),
    decision("human", "MYC", "HLA-A", "hold_exact_pair_review", "unresolved", "unknown", "uncertain", "8206526", "The verified paper is HLA-B-specific; do not transfer its promoter result to HLA-A.", hold_reason="target-specific primary evidence absent"),
    decision("human", "MYC", "HLA-C", "hold_exact_pair_review", "unresolved", "unknown", "uncertain", "8206526", "The verified paper is HLA-B-specific; do not transfer its promoter result to HLA-C.", hold_reason="target-specific primary evidence absent"),
    decision("human", "MYC", "HLA-E", "hold_exact_pair_review", "unresolved", "unknown", "uncertain", "8206526", "The verified paper is HLA-B-specific; do not transfer its promoter result to HLA-E.", hold_reason="target-specific primary evidence absent"),
    decision("human", "MYC", "HLA-F", "hold_exact_pair_review", "unresolved", "unknown", "uncertain", "8206526", "The verified paper is HLA-B-specific; do not transfer its promoter result to HLA-F.", hold_reason="target-specific primary evidence absent"),
    decision("human", "MYC", "HLA-G", "hold_exact_pair_review", "unresolved", "unknown", "uncertain", "8206526", "The verified paper is HLA-B-specific; do not transfer its promoter result to HLA-G.", hold_reason="target-specific primary evidence absent"),
    decision("human", "GATA3", "CDH3", "hold_exact_pair_review", "contextual_support", "repressing_target", "uncertain", "22120723", "The paper reports broader GATA3/BRCA1-associated repression, but the strongest mapped promoter evidence is FOXC1; hold CDH3 pending exact-pair evidence.", hold_reason="contextual multi-gene repression not enough for direct pair promotion"),
    decision("human", "GATA3", "CXCL1", "hold_exact_pair_review", "contextual_support", "repressing_target", "uncertain", "22120723", "The paper reports broader GATA3/BRCA1-associated repression, but the strongest mapped promoter evidence is FOXC1; hold CXCL1 pending exact-pair evidence.", hold_reason="contextual multi-gene repression not enough for direct pair promotion"),
    decision("human", "GATA3", "FOXC2", "hold_exact_pair_review", "contextual_support", "repressing_target", "uncertain", "22120723", "The paper reports broader GATA3/BRCA1-associated repression, but the strongest mapped promoter evidence is FOXC1; hold FOXC2 pending exact-pair evidence.", hold_reason="contextual multi-gene repression not enough for direct pair promotion"),
    decision("human", "CEBPB", "CSF3R", "hold_exact_pair_review", "unresolved", "unknown", "uncertain", "10453008", "The cited paper is about the common beta-chain CSF2RB promoter, not CSF3R; no CEBPB→CSF3R promotion is allowed.", hold_reason="paper target mismatch: CSF2RB versus CSF3R"),
    decision("human", "CEBPB", "IL3", "hold_exact_pair_review", "unresolved", "unknown", "uncertain", "10453008", "The cited paper is about a composite C/EBP site in the CSF2RB promoter, not an IL3 target assay.", hold_reason="paper target mismatch"),
    decision("human", "CEBPB", "IL5", "hold_exact_pair_review", "unresolved", "unknown", "uncertain", "10453008", "The cited paper is about a composite C/EBP site in the CSF2RB promoter, not an IL5 target assay.", hold_reason="paper target mismatch"),

    decision("human", "STAT1", "IFNG", "hold_cross_module_reuse", "unresolved", "unknown", "uncertain", "", "Shared PMID 7796811 with a Module 20B TPO/MPL record is incidental and does not prove STAT1→IFNG; keep the candidate in Module 22B review.", cross_module="20B", hold_reason="shared Module 20B citation is incidental; exact STAT1→IFNG evidence not reviewed"),
    decision("human", "STAT1", "IFNA1", "hold_cross_module_reuse", "unresolved", "unknown", "uncertain", "", "Shared PMID 7796811 with a Module 20B TPO/MPL record is incidental and does not prove STAT1→IFNA1; keep the candidate in Module 22B review.", cross_module="20B", hold_reason="shared Module 20B citation is incidental; exact STAT1→IFNA1 evidence not reviewed"),
    decision("human", "JUN", "FOS", "hold_cross_module_reuse", "unresolved", "unknown", "uncertain", "", "Shared PMID 36634215 with a Module 24B S100A8/TLR4 record is incidental; it is not a JUN→FOS target experiment.", cross_module="24B", hold_reason="shared Module 24B citation is incidental"),
    decision("human", "JUN", "IFNG", "hold_cross_module_reuse", "unresolved", "unknown", "uncertain", "", "Shared IL-12/STAT4/AP-1 references do not establish a JUN-specific IFNG occupancy or causal target edge.", cross_module="20B;22B", hold_reason="AP-1/STAT4 cooperation does not resolve exact JUN pair"),
    decision("mouse", "Jun", "Fos", "hold_cross_module_reuse", "unresolved", "unknown", "uncertain", "", "The human AP-1 evidence and Module 24B citation overlap do not establish this mouse pair; keep species-specific review separate.", cross_module="24B", hold_reason="mouse exact-pair evidence not verified"),
    decision("mouse", "Jun", "Ifng", "hold_cross_module_reuse", "unresolved", "unknown", "uncertain", "", "The shared IL-12/STAT4 references do not establish a mouse Jun-specific IFNG target edge.", cross_module="20B", hold_reason="mouse exact-pair evidence not verified"),
    decision("mouse", "Tp53", "Ddr1", "hold_cross_module_reuse", "unresolved", "unknown", "uncertain", "", "The independent p53→DDR1 paper used for the human pair is not sufficient to promote the mouse assertion; the overlapping collagen/DDR1 citation is retracted and excluded.", excluded="21398698", cross_module="23B", hold_reason="mouse species-specific evidence not verified; retracted overlap excluded"),
]


DECISION_FIELDS = [
    "curation_id", "module", "species", "tf_symbol", "target_symbol",
    "external_record_keys", "source_registries", "public_effect_polarities",
    "public_verification_statuses", "public_reference_pmids", "source_pmids",
    "corroborating_pmids", "excluded_pmids", "tf_entity_ids", "target_entity_ids",
    "tf_frozen_match_status", "target_frozen_match_status", "tf_role_present",
    "target_role_present", "evidence_scope", "effect_polarity", "confidence_tier",
    "cell_type_context", "stimulus_context", "module_boundary",
    "cross_module_overlap", "reuse_audit_status", "promotion_decision",
    "graph_materialization_status", "hold_reason", "curation_note",
]

SOURCE_LINK_FIELDS = [
    "curation_id", "pair_key", "link_type", "source_registry", "source_version",
    "species", "tf_symbol", "target_symbol", "external_record_key", "source_pmid",
    "source_locator", "source_locator_status", "source_kind", "support_kind",
    "evidence_scope", "citation_note", "limitations",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: "" if row.get(field) is None else row.get(field, "") for field in fields} for row in rows)


def split_values(value: str) -> list[str]:
    return [item for item in (value or "").split(";") if item and item != r"\N"]


def unique_join(values: list[str]) -> str:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            output.append(value)
    return ";".join(output)


def pair_key(species: str, tf: str, target: str) -> tuple[str, str, str]:
    return species.casefold(), tf.casefold(), target.casefold()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    source_rows = read_tsv(args.input_dir / "source_records.tsv")
    mapping_rows = read_tsv(args.input_dir / "frozen_entity_mapping.tsv")
    source_by_pair: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in source_rows:
        source_by_pair[pair_key(row["species_context"], row["tf_normalized_symbol"], row["target_normalized_symbol"])].append(row)

    mapping_index: dict[tuple[str, str, str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in mapping_rows:
        mapping_index[(row["source_registry"], row["source_version"], row["species_context"], row["identity_role"], row["normalized_symbol_key"].casefold())].append(row)

    decisions: list[dict[str, str]] = []
    source_links: list[dict[str, str]] = []
    promoted: list[dict[str, str]] = []
    held: list[dict[str, str]] = []

    for index, item in enumerate(DECISIONS, start=1):
        key = pair_key(item["species"], item["tf"], item["target"])
        pair_rows = source_by_pair.get(key, [])
        external_keys = unique_join([row["external_record_key"] for row in pair_rows])
        registries = unique_join([row["source_registry"] for row in pair_rows])
        public_effects = unique_join([row["effect_polarity"] for row in pair_rows])
        public_statuses = unique_join([row["verification_status"] for row in pair_rows])
        public_refs = unique_join([pmid for row in pair_rows for pmid in split_values(row.get("reference_pmids", ""))])

        tf_maps = [
            mapped
            for row in pair_rows
            for mapped in mapping_index[(row["source_registry"], row["source_version"], row["species_context"], "tf", row["tf_normalized_symbol_key"].casefold())]
        ]
        target_maps = [
            mapped
            for row in pair_rows
            for mapped in mapping_index[(row["source_registry"], row["source_version"], row["species_context"], "target", row["target_normalized_symbol_key"].casefold())]
        ]
        tf_entity_ids = unique_join([row.get("mscidblit_entity_id", "") for row in tf_maps if row.get("mscidblit_entity_id") not in {"", r"\N"}])
        target_entity_ids = unique_join([row.get("mscidblit_entity_id", "") for row in target_maps if row.get("mscidblit_entity_id") not in {"", r"\N"}])
        tf_match = unique_join([row.get("frozen_entity_match_status", "") for row in tf_maps])
        target_match = unique_join([row.get("frozen_entity_match_status", "") for row in target_maps])
        tf_role = "true" if any(row.get("frozen_tf_role_present") == "t" for row in tf_maps) else "false"
        target_role = "true" if any(row.get("frozen_target_role_present") == "t" for row in target_maps) else "false"

        graph_status = "not_canonical_materialization;entity_role_review_required"
        if not pair_rows:
            graph_status = "blocked;no_matching_public_record"
        elif item["promotion_decision"] == "promote_to_22B_staging":
            graph_status = "staged_evidence_only;canonical_entity_role_gate_pending"

        record = {
            "curation_id": f"PUBTF-M22B-B001-{index:04d}",
            "module": "22B",
            "species": item["species"],
            "tf_symbol": item["tf"],
            "target_symbol": item["target"],
            "external_record_keys": external_keys,
            "source_registries": registries,
            "public_effect_polarities": public_effects,
            "public_verification_statuses": public_statuses,
            "public_reference_pmids": public_refs,
            "source_pmids": item["primary_pmids"],
            "corroborating_pmids": item["corroborating_pmids"],
            "excluded_pmids": item["excluded_pmids"],
            "tf_entity_ids": tf_entity_ids,
            "target_entity_ids": target_entity_ids,
            "tf_frozen_match_status": tf_match,
            "target_frozen_match_status": target_match,
            "tf_role_present": tf_role,
            "target_role_present": target_role,
            "evidence_scope": item["evidence_scope"],
            "effect_polarity": item["effect_polarity"],
            "confidence_tier": item["confidence_tier"],
            "cell_type_context": item["cell_type_context"],
            "stimulus_context": item["stimulus_context"],
            "module_boundary": "22B TF-to-target/downstream program only; no automatic 20B/21B/23B/24B edge",
            "cross_module_overlap": item["cross_module_overlap"],
            "reuse_audit_status": item["reuse_audit_status"],
            "promotion_decision": item["promotion_decision"],
            "graph_materialization_status": graph_status,
            "hold_reason": item["hold_reason"],
            "curation_note": item["curation_note"],
        }
        decisions.append(record)
        (promoted if item["promotion_decision"] == "promote_to_22B_staging" else held).append(record)

        for row in pair_rows:
            source_links.append({
                "curation_id": record["curation_id"],
                "pair_key": f"{item['species']}|{item['tf']}|{item['target']}",
                "link_type": "public_record_provenance",
                "source_registry": row["source_registry"],
                "source_version": row["source_version"],
                "species": row["species_context"],
                "tf_symbol": row["tf_normalized_symbol"],
                "target_symbol": row["target_normalized_symbol"],
                "external_record_key": row["external_record_key"],
                "source_pmid": row.get("reference_pmids", ""),
                "source_locator": row.get("source_locator", ""),
                "source_locator_status": "public_record_locator",
                "source_kind": "public_tf_union_record",
                "support_kind": row.get("evidence_basis", "database_curated"),
                "evidence_scope": "public_record_reference_lead",
                "citation_note": "Public record retained as provenance lead; not treated as proof without the pair-level adjudication above.",
                "limitations": row.get("limitations", ""),
            })
        for link_type, pmids, support_kind, note in (
            ("verified_primary", item["primary_pmids"], "primary_experiment", "Exact-pair primary source selected during bounded evidence review."),
            ("corroborating_primary", item["corroborating_pmids"], "primary_experiment", "Independent corroborating primary source; kept separate from the public record citation."),
            ("excluded_citation", item["excluded_pmids"], "negative_evidence", "Citation excluded from support; do not reuse for promotion."),
        ):
            for pmid in split_values(pmids):
                source_links.append({
                    "curation_id": record["curation_id"],
                    "pair_key": f"{item['species']}|{item['tf']}|{item['target']}",
                    "link_type": link_type,
                    "source_registry": "manual_pair_review",
                    "source_version": "batch001",
                    "species": item["species"],
                    "tf_symbol": item["tf"],
                    "target_symbol": item["target"],
                    "external_record_key": external_keys,
                    "source_pmid": pmid,
                    "source_locator": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                    "source_locator_status": "pubmed_locator",
                    "source_kind": "primary_literature",
                    "support_kind": support_kind,
                    "evidence_scope": item["evidence_scope"],
                    "citation_note": note,
                    "limitations": item["curation_note"],
                })

    write_tsv(args.output_dir / "priority_curation_batch001_decisions.tsv", DECISION_FIELDS, decisions)
    write_tsv(args.output_dir / "priority_curation_batch001_promoted_22B.tsv", DECISION_FIELDS, promoted)
    write_tsv(args.output_dir / "priority_curation_batch001_hold_queue.tsv", DECISION_FIELDS, held)
    write_tsv(args.output_dir / "priority_curation_batch001_source_links.tsv", SOURCE_LINK_FIELDS, source_links)

    manifest = {
        "batch": "public_tf_union_priority_batch001",
        "module_assignment": "22B",
        "decision_rows": len(decisions),
        "promoted_to_22B_staging": len(promoted),
        "held": len(held),
        "source_link_rows": len(source_links),
        "promotions_with_cross_module_overlap_review": sum(1 for row in promoted if row["cross_module_overlap"]),
        "promotions_to_modules_other_than_22B": 0,
        "cross_module_holds": sum(1 for row in held if row["cross_module_overlap"]),
        "canonical_database_writes": False,
        "frozen_release_modified": False,
        "policy": {
            "public_tf_default_module": "22B",
            "shared_paper_requires_pair_scope": True,
            "independent_corroboration_used_for_shared_groups": ["TP53", "JUN/FOS", "STAT1", "HIF1A"],
            "retracted_citations_excluded": ["21398698"],
            "receptor_ecm_complement_boundary": "TF-target evidence stays in 22B; no 20B/21B/23B/24B promotion by citation overlap alone",
        },
    }
    (args.output_dir / "priority_curation_batch001_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
