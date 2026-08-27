#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 020 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_020/"
    "public_tf_evidence_collection_batch_020.tsv"
)
TF_LINK_URL = "https://tflink.net/download/#interaction-gmt"
PAIR_FIELDS = [
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol", "species_scope",
    "source_registry", "source_record_id", "raw_tf_symbol", "target_symbol", "target_graph_modules",
    "candidate_membership_status", "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status",
    "target_cell_presence_status", "binding_or_association_status", "downstream_expression_or_perturbation_status",
    "downstream_activation_status", "upstream_relay_status", "disposition", "primary_citation",
    "corroborating_citation", "near_match_exclusions", "review_notes", "exportable", "canonical_write_performed",
]
EVIDENCE_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer", "support_kind",
    "cell_or_model", "assay_or_perturbation", "observation", "effect_direction", "primary_citation",
    "corroborating_citation", "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]


# symbol, primary regulator-level citation, corroborating citation, support kind,
# model, assay, observation, role relevance
REGULATORS = {
    "scml2": ("SCML2", "https://elifesciences.org/articles/02637", "https://pubmed.ncbi.nlm.nih.gov/24358021/", "primary_literature_regulator_level", "human SCML2A/PRC1 chromatin models", "SCML2 ChIP-seq, knockdown, and Polycomb/RNA recruitment studies", "SCML2 is a noncanonical Polycomb/chromatin regulator with broad promoter-proximal occupancy and derepression after depletion; no queued target was validated.", "noncanonical chromatin regulator capacity only"),
    "cxxc4": ("CXXC4/IDAX", "https://pubmed.ncbi.nlm.nih.gov/29262584/", "https://pubmed.ncbi.nlm.nih.gov/10944533/", "primary_literature_regulator_level", "human gastric-cancer and Wnt-signaling models", "CXXC4 ChIP-qPCR, Sp1 cooperation, expression, apoptosis, and Dvl/Axin interaction studies", "CXXC4 has complex-dependent promoter and Wnt-regulatory evidence at GDF15 and other nonqueued loci.", "noncanonical transcriptional coregulator capacity only"),
    "taf15": ("TAF15", "https://pubmed.ncbi.nlm.nih.gov/34285657/", "https://pubmed.ncbi.nlm.nih.gov/41244301/", "primary_literature_regulator_level", "human fibroblast, macrophage, and cholangiocarcinoma models", "promoter association, CUT&Tag, knockdown/overexpression, reporter, and expression studies", "TAF15 has noncanonical promoter evidence at TLR4 and SOCS1, but none of the queued ADAM or ACVR1C targets.", "noncanonical transcriptional modifier/coregulator capacity only"),
    "ash2l": ("ASH2L", "https://pubmed.ncbi.nlm.nih.gov/25258321/", "https://pubmed.ncbi.nlm.nih.gov/32279431/", "primary_literature_regulator_level", "human ERalpha and endometrial-cancer chromatin models", "COMPASS/MLL recruitment, enhancer occupancy, depletion, and target expression studies", "ASH2L is a COMPASS/MLL chromatin cofactor recruited through other DNA-binding factors; queued targets were not validated.", "noncanonical chromatin cofactor capacity only"),
    "ssu72": ("SSU72", "https://pubmed.ncbi.nlm.nih.gov/25319827/", "https://pubmed.ncbi.nlm.nih.gov/34987641/", "primary_literature_regulator_level", "human and mammalian Pol II transcription-cycle models", "promoter ChIP, phosphatase perturbation, elongation, and termination studies", "SSU72 is a transcription-cycle phosphatase/elongation factor, not a sequence-specific TF for queued targets.", "noncanonical transcriptional machinery capacity only"),
    "ncapd3": ("NCAPD3", "https://pubmed.ncbi.nlm.nih.gov/38432395/", "https://pubmed.ncbi.nlm.nih.gov/35085770/", "primary_literature_regulator_level", "human condensin/TF-complex cancer models", "chromatin-complex recruitment, expression, and locus-regulatory studies", "NCAPD3 is a condensin/chromatin-architecture component; the queued mouse edges are unverified.", "noncanonical chromosome-architecture capacity only"),
    "phf5a": ("PHF5A", "https://pubmed.ncbi.nlm.nih.gov/29700004/", "https://pubmed.ncbi.nlm.nih.gov/27749823/", "primary_literature_regulator_level", "human spliceosomal and Pol II elongation models", "promoter-enriched occupancy, PAF1C/SF3B interaction, and elongation studies", "PHF5A is a nuclear spliceosomal/elongation factor; no queued target-specific edge was validated.", "noncanonical nuclear machinery capacity only"),
    "l3mbtl2": ("L3MBTL2", "https://pubmed.ncbi.nlm.nih.gov/21596310/", "", "primary_literature_regulator_level", "human PRC1.6 chromatin models", "TSS-proximal chromatin binding and depletion-associated derepression", "L3MBTL2 is a PRC1.6 chromatin repressor; no queued target-specific evidence was found.", "noncanonical chromatin-repressor capacity only"),
    "cbx2": ("CBX2", "https://pubmed.ncbi.nlm.nih.gov/29541019/", "", "primary_literature_regulator_level", "human neuronal-cell chromatin models", "promoter ChIP-qPCR and CBX2 knockdown", "CBX2 occupies and represses neuronal promoters such as GAP43, but none of the queued targets was tested.", "noncanonical chromatin-reader/repressor capacity only"),
    "gatad1": ("GATAD1", "https://pubmed.ncbi.nlm.nih.gov/29266303/", "https://pubmed.ncbi.nlm.nih.gov/31286678/", "primary_literature_regulator_level", "human cancer and mouse endothelial models", "promoter binding, chromatin-loop, reporter, and perturbation studies", "GATAD1 has genuine complex-dependent promoter evidence at PTP4A3/PRL3 and CCND1, not the queued targets.", "noncanonical transcriptional coregulator capacity only"),
    "kat8": ("KAT8/MOF", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6446880/", "https://pubmed.ncbi.nlm.nih.gov/36894639/", "primary_literature_regulator_level", "human immune and cancer chromatin models", "histone-acetyltransferase occupancy, promoter assays, and perturbation", "KAT8/MOF is a chromatin acetyltransferase with functional evidence at IRF3 and CD274/PD-L1, not queued targets.", "noncanonical chromatin-enzyme capacity only"),
    "stag2": ("STAG2", "https://pubmed.ncbi.nlm.nih.gov/32253279/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9439679/", "primary_literature_regulator_level", "human cohesin and chromatin-architecture models", "cohesin occupancy, looping, ChIP-qPCR, knockout, and expression studies", "STAG2 is a cohesin-associated genome-architecture regulator; human ABCA1 is recorded as a provisional exact noncanonical candidate below.", "noncanonical chromatin-architecture capacity; exact ABCA1 edge kept separate"),
    "cxxc1": ("CXXC1/CFP1", "https://pubmed.ncbi.nlm.nih.gov/25470594/", "https://pubmed.ncbi.nlm.nih.gov/35918532/", "primary_literature_regulator_level", "mouse hematopoietic and meiotic chromatin models", "CpG-promoter binding, SET1 recruitment, depletion, and transcription studies", "CXXC1 binds unmethylated CpG-rich promoters and recruits SET1 complexes, but queued Actr2/Adam targets were not validated.", "noncanonical chromatin cofactor capacity only"),
    "ino80": ("INO80", "https://pubmed.ncbi.nlm.nih.gov/27428271/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6534818/", "primary_literature_regulator_level", "human chromatin-remodeling and cancer models", "ATP-dependent chromatin remodeling, ChIP, and expression studies", "INO80 is an ATP-dependent chromatin remodeler with nonqueued locus evidence; ACTR2 was not confused with ACTR8/ARP8.", "noncanonical chromatin-remodeler capacity only"),
    "kmt2c": ("KMT2C/MLL3", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7257146/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7762615/", "primary_literature_regulator_level", "human and mouse enhancer/chromatin models", "enhancer H3K4 methylation, ATAC/ChIP, eRNA, and perturbation studies", "KMT2C/MLL3 is an enhancer coactivator, not a sequence-specific TF; no queued target was functionally validated.", "noncanonical chromatin methyltransferase capacity only"),
    "mier3": ("MIER3", "https://pubmed.ncbi.nlm.nih.gov/34242623/", "https://pubmed.ncbi.nlm.nih.gov/28046085/", "primary_literature_regulator_level", "human breast-cancer EMT models", "HDAC/Snail complex recruitment, CDH1 promoter binding, and expression studies", "MIER3 participates in complex-dependent CDH1 repression in some contexts, with context-dependent recruitment; no queued target was validated.", "noncanonical transcriptional coregulator capacity only"),
    "lmo1": ("LMO1", "https://pubmed.ncbi.nlm.nih.gov/29695398/", "https://pubmed.ncbi.nlm.nih.gov/31819055/", "primary_literature_regulator_level", "human neuroblastoma models", "ChIP-seq, knockdown, and associated-complex expression studies", "LMO1 lacks a DNA-binding domain and acts through associated complexes at nonqueued loci such as LIMS1, RSU1, RLN2, and ASCL1.", "noncanonical transcriptional coregulator capacity only"),
    "ccnt2": ("CCNT2/Cyclin T2", "https://pubmed.ncbi.nlm.nih.gov/15563843/", "", "primary_literature_regulator_level", "human HeLa Pol II/P-TEFb models", "Pol II CTD interaction and tethered transcription assays", "CCNT2 is a CDK9/P-TEFb elongation component; tethering evidence does not establish sequence-specific queued-target regulation.", "noncanonical transcriptional machinery capacity only"),
    "setdb1": ("SETDB1", "https://pubmed.ncbi.nlm.nih.gov/19884257/", "https://pubmed.ncbi.nlm.nih.gov/30446626/", "primary_literature_regulator_level", "mouse ESC and BMP/chromatin models", "H3K9me3 occupancy, repression, ChEA profiles, and pathway studies", "SETDB1 is a chromatin repressor with evidence at Cdx2/Tcfap2a and BMP-related loci; two queued rows are profile-only and Acvrl1 is a paralog of queued Acvr1.", "noncanonical chromatin methyltransferase capacity only"),
    "brd1": ("BRD1", "https://pubmed.ncbi.nlm.nih.gov/27142060/", "https://pubmed.ncbi.nlm.nih.gov/35941107/", "primary_literature_regulator_level", "human chromatin and mitochondrial-program models", "ChIP-seq, knockdown/overexpression, and expression studies", "BRD1 has broad chromatin-coregulatory evidence, but no queued locus had validated occupancy plus perturbation.", "noncanonical chromatin-coregulator capacity only"),
    "ints12": ("INTS12", "https://pubmed.ncbi.nlm.nih.gov/28335732/", "https://pubmed.ncbi.nlm.nih.gov/40207620/", "primary_literature_regulator_level", "human bronchial epithelial and Integrator models", "siRNA/RNA-seq, ChIP-seq, and transcription-termination studies", "INTS12 is an Integrator-complex subunit with broad promoter/TSS-associated effects, not an isolated sequence-specific TF for queued targets.", "noncanonical transcriptional machinery capacity only"),
    "brpf3": ("BRPF3", "https://pubmed.ncbi.nlm.nih.gov/26620551/", "https://pubmed.ncbi.nlm.nih.gov/26677226/", "primary_literature_regulator_level", "human and mouse HBO1/KAT7 chromatin models", "replication-origin occupancy, H3K14 acetylation, depletion, and knockout studies", "BRPF3 is an HBO1/KAT7 chromatin/replication cofactor; no queued target-level regulation was established.", "noncanonical chromatin-cofactor capacity only"),
    "cdk9": ("CDK9", "https://pubmed.ncbi.nlm.nih.gov/17998334/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2223422/", "primary_literature_regulator_level", "human breast-cancer and Pol II elongation models", "PPARgamma phosphorylation, inhibitor/genetic perturbation, and elongation studies", "CDK9 is a P-TEFb elongation kinase; ABCA1 is an indirect human PPARgamma-associated near-match and ADAM9 is a complex/axis near-match.", "noncanonical transcriptional machinery capacity only"),
    "cdk8": ("CDK8", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3580287/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3681429/", "primary_literature_regulator_level", "human and mouse Mediator-kinase models", "occupancy, perturbation, and IFN/p53/HIF-responsive gene studies", "CDK8 has functional occupancy evidence at nonqueued loci but is a Mediator kinase/co-regulator, not a sequence-specific TF for queued targets.", "noncanonical transcriptional machinery capacity only"),
    "cbfa2t2": ("CBFA2T2/MTGR1", "https://pubmed.ncbi.nlm.nih.gov/27281218/", "https://pubmed.ncbi.nlm.nih.gov/25398765/", "primary_literature_regulator_level", "human and mouse germline/intestinal corepressor models", "complex-associated occupancy, repression, and perturbation studies", "CBFA2T2 is a corepressor/scaffold recruited with other factors; no queued ACVR1C or ADAM target was validated.", "noncanonical transcriptional coregulator capacity only"),
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def search_url(regulator: str, target: str, species: str) -> str:
    return "https://pubmed.ncbi.nlm.nih.gov/?term=" + quote_plus(f'"{regulator}" AND "{target}" AND {species}')


def classify(row: dict[str, str]) -> dict[str, str]:
    key = row["regulator_key"]
    target = row["target_symbol"].lower()
    symbol, general_primary, general_corr, kind, model, assay, observation, relevance = REGULATORS[key]
    status = "database_membership_only_not_promotable"
    primary = TF_LINK_URL
    corr = ""
    cell = "not_established_for_exact_pair"
    binding = "TFLink_membership_only_no_retrieved_target_locus_call"
    downstream = "not_found_for_exact_pair"
    disposition = "retain_provenance_traceable_candidate_without_promotion"
    exclusions = "TFLink membership is a search lead; general regulator evidence, orthologs, paralogs, reverse directions, and complex-level associations were not transferred to this exact pair."
    notes = "No exact target-specific causal edge was established in the reviewed literature; no target-cell presence, downstream activation, or upstream relay is inferred."

    if key == "stag2" and row["species_scope"] == "human" and target == "abca1":
        status = "functional_noncanonical_chromatin_architecture_candidate_not_strict_tf"
        primary = "https://www.aacr.org/wp-content/uploads/2025/05/AACR2025_Proceedings_050725.pdf"
        corr = "https://www.biorxiv.org/content/10.64898/2026.06.10.731379v1"
        cell = "human_cancer_model_not_SCI_target_cell"
        binding = "STAG2_ChIP_seq_and_ChIP_qPCR_at_ABCA1_promoter"
        downstream = "STAG2_knockout_reduced_ABCA1_and_promoter_H3K4_H3K27_acetylation"
        disposition = "retain_noncanonical_chromatin_architecture_candidate_pending_independent_corroboration_and_SCI_context"
        exclusions = "The exact result is reported in an AACR 2025 abstract and same-study bioRxiv preprint; it is not independent corroboration, and STAG2 is a cohesin/chromatin-architecture factor rather than a strict sequence-specific TF."
        notes = "Exact human STAG2-to-ABCA1 occupancy plus knockout-associated expression/acetylation change is staged as a noncanonical candidate only; it is not exportable or a strict TF promotion."
    elif key == "ncapd3" and row["species_scope"] == "mouse" and target == "ackr3":
        status = "contextual_ortholog_near_match_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/19832994/"
        cell = "human_LNCaP_model_not_mouse_SCI_target_cell"
        binding = "no_NCAPD3_ACKR3_binding_assay"
        downstream = "androgen_treatment_increased_NCAPD3_and_decreased_CXCR7_ACKR3"
        disposition = "retain_contextual_near_match_separately"
        exclusions = "Human androgen-response co-variation is not a mouse Ncapd3 perturbation, binding, or causal target assay; no corroborating paper was found."
        notes = "Contextual human/ortholog co-expression only; not transferred to the exact mouse Ncapd3-to-Ackr3 edge."
    elif key == "setdb1" and row["species_scope"] == "mouse" and target in {"actr2", "acvr1c"}:
        status = "binding_profile_only_not_promotable"
        primary = "https://maayanlab.cloud/Harmonizome/gene_set/SETDB1-19884257-MESC-mouse/CHEA%2BTranscription%2BFactor%2BBinding%2BSite%2BProfiles"
        corr = "https://pubmed.ncbi.nlm.nih.gov/19884257/"
        cell = "mouse_ESC_profile_not_SCI_target_cell"
        binding = "mouse_ChEA_SETDB1_binding_profile_membership"
        downstream = "no_target_specific_perturbation_or_expression_direction"
        disposition = "retain_mouse_binding_profile_lead_separately"
        exclusions = "The ChEA/Harmonizome profile is occupancy/profile evidence only and does not provide target-specific perturbation, direction, or SCI context."
        notes = "Exact mouse profile membership is retained as a binding-profile lead only; it is not a functional TF edge."
    elif key == "cdk9" and row["species_scope"] == "mouse" and target == "abca1":
        status = "contextual_ortholog_near_match_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/17998334/"
        corr = "https://pmc.ncbi.nlm.nih.gov/articles/PMC2223422/"
        cell = "human_MDA_MB_231_model_not_mouse_SCI_target_cell"
        binding = "no_CDK9_ABCA1_locus_occupancy; indirect_PPARgamma_axis"
        downstream = "CDK9_perturbation_changed_PPARgamma_phosphorylation_and_ABCA1_in_human_model"
        disposition = "retain_indirect_cross_species_near_match_separately"
        exclusions = "The result is human, indirect through PPARgamma, and lacks endogenous CDK9 occupancy at the ABCA1 locus; no mouse exact edge is established."
        notes = "Indirect human PPARgamma/ABCA1 association is not evidence for a direct mouse Cdk9-to-Abca1 edge."
    elif key == "cdk9" and row["species_scope"] == "mouse" and target == "adam9":
        status = "contextual_complex_axis_near_match_not_promotable"
        primary = "https://doi.org/10.1093/neuped/wuag026.338"
        cell = "human_STAT3_CDK9_axis_and_mouse_xenograft_context_not_exact_mouse_Cdk9_locus_assay"
        binding = "no_direct_endogenous_mouse_CDK9_Adam9_occupancy"
        downstream = "STAT3_CDK9_axis_and_CDK9_perturbation_associated_with_ADAM9"
        disposition = "retain_complex_axis_near_match_separately"
        exclusions = "The report supports a STAT3-CDK9 axis using perturbation and model systems but does not establish direct mouse Cdk9 occupancy or isolated Cdk9 causality at Adam9; no independent corroboration was found."
        notes = "Axis-level ADAM9 association is retained separately from an exact TF-like edge."

    return {
        "symbol": symbol, "general_primary": general_primary, "general_corr": general_corr, "kind": kind,
        "model": model, "assay": assay, "observation": observation, "relevance": relevance,
        "status": status, "primary": primary, "corr": corr, "cell": cell, "binding": binding,
        "downstream": downstream, "disposition": disposition, "exclusions": exclusions, "notes": notes,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_BATCH.parent)
    args = parser.parse_args()
    rows = read_tsv(args.batch)
    if len(rows) != 100:
        raise SystemExit(f"expected 100 rows, found {len(rows)}")

    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        info = classify(row)
        pairs.append({
            "review_id": f"public_tf_evidence_batch020_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
            "source_registry": row["source_registry"], "source_record_id": row["source_record_id"],
            "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": info["status"], "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence",
            "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"],
            "downstream_expression_or_perturbation_status": info["downstream"], "downstream_activation_status": "not_established_for_SCI_target_cell",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"],
            "primary_citation": info["primary"], "corroborating_citation": info["corr"],
            "near_match_exclusions": info["exclusions"], "review_notes": info["notes"] + " " + info["observation"],
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch020_regulator_{key}", "regulator_key": key,
                "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
                "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"],
                "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"],
                "effect_direction": "queued-pair direction not established except explicitly recorded limited associations",
                "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"],
                "route_or_module_relevance": info["relevance"], "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay. Chromatin-associated, cofactor, machinery, profile, and indirect axis evidence is retained separately from canonical promoter-TF evidence.",
            })
            seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch020_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch020_regulator_register.tsv"
    summary_path = args.output_dir / "batch_020_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH020.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(item["regulator_key"], item["target_symbol"], item["species_scope"], item["source_record_id"]) for item in pairs}
    noncanonical = status_counts.get("functional_noncanonical_chromatin_architecture_candidate_not_strict_tf", 0)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_020", "source_set_ranks_reviewed": list(range(1, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "strict_tf_promotion_candidate_rows": 0,
        "noncanonical_exact_candidate_rows": noncanonical, "exportable_pair_rows": 0, "canonical_writes_performed": False,
        "module22b_promotions_performed": False, "provenance_preserved": True,
        "limitations": ["TFLink membership/profile resources are search leads, not causal regulation.", "Exact-pair negatives are bounded search results, not global absence.", "STAG2-to-ABCA1 is a provisional noncanonical cohesin candidate from an AACR abstract and same-study preprint, without independent corroboration or SCI-cell validation.", "Ncapd3-to-Ackr3, Cdk9-to-Abca1, and Cdk9-to-Adam9 are contextual/indirect near-matches, not exact promoted edges.", "No canonical or Module 22B write was performed."],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join([
        "# Evidence review: public TF batch 020", "", "Reviewed 100 exact regulator-target-species pairs across 25 noncanonical TFLink source-set ranks.", "",
        f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.",
        f"- **{noncanonical}** exact noncanonical candidate was staged: human STAG2-to-ABCA1, supported by STAG2 promoter occupancy and knockout-associated ABCA1 loss/acetylation change in an AACR abstract and same-study preprint.",
        f"- **{status_counts.get('binding_profile_only_not_promotable', 0)}** mouse SETDB1 binding-profile rows and **{status_counts.get('contextual_ortholog_near_match_not_promotable', 0)}** contextual cross-species/indirect rows were retained without promotion.",
        "- **0** strict TF promotion candidates, exportable rows, canonical writes, or Module 22B writes.", "",
        "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping, and local source snapshot. Regulator-level chromatin, cofactor, machinery, profile, and axis evidence is recorded separately from exact canonical TF evidence.", "",
    ]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
