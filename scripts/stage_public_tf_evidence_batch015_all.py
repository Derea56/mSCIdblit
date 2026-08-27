#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 015 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_015/"
    "public_tf_evidence_collection_batch_015.tsv"
)
TF_LINK_URL = "https://tflink.net/download/#interaction-gmt"
GTRD_URL = "https://pubmed.ncbi.nlm.nih.gov/27924024/"
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

REGULATORS = {
    "znf280c": ("ZNF280C", "https://pubmed.ncbi.nlm.nih.gov/30567999/", "https://pubmed.ncbi.nlm.nih.gov/35605119/", "primary_literature_regulator_level", "human DNA-damage/epigenetic models", "perturbation and repression studies", "ZNF280C has regulator-level repression evidence, but no queued target direction/function was established."),
    "znf624": ("ZNF624", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched binding-set membership", "ZNF624 occupancy lead does not establish queued target direction/function."),
    "znf746": ("ZNF746", "https://pubmed.ncbi.nlm.nih.gov/21376232/", "https://pubmed.ncbi.nlm.nih.gov/24234451/", "primary_literature_regulator_level", "human metabolic models", "PPARGC1A/NRF1 perturbation and curator-inferred relation", "ZNF746 evidence concerns PPARGC1A and NRF1, not G6PC or PCK1."),
    "znf385a": ("Znf385a/Hzf", "https://pubmed.ncbi.nlm.nih.gov/18418387/", "https://pubmed.ncbi.nlm.nih.gov/21402775/", "primary_literature_regulator_level", "mouse adipogenesis and p53 models", "RNA 3-prime-UTR binding, translation, and perturbation", "Hzf/Zfp385a is a post-transcriptional RNA-binding regulator at Cebpa and Tp53, not a promoter-DNA TF edge."),
    "dmrta1": ("DMRTA1", "https://tflink.net/protein/q5vzb9/", "https://pubmed.ncbi.nlm.nih.gov/22900683/", "authoritative_binding_dataset_only", "human HTRI/TFLink candidate set", "curator-inferred target-set membership", "DMRTA1-CDKN2A is a database/curation lead; the linked screen functionally validates MEOX2, not DMRTA1."),
    "esx1": ("ESX1", "https://pubmed.ncbi.nlm.nih.gov/15897875/", "", "primary_literature_regulator_level", "human KRAS and proliferation model", "processed homeodomain-fragment binding and repression", "ESX1/ESXR1 fragment evidence supports KRAS repression but is not full-length ESX1 evidence."),
    "hoxd10": ("HOXD10", "https://pmc.ncbi.nlm.nih.gov/articles/PMC453170/", "", "primary_literature_regulator_level", "human HOX promoter assay", "DNA binding and promoter reporter", "HOXD10/HOX4D promoter-element evidence supports HOXD9/HOX4C transactivation but not endogenous target expression."),
    "lhx5": ("LHX5", "https://pubmed.ncbi.nlm.nih.gov/39418382/", "", "primary_literature_regulator_level", "human and mouse neural/enteroendocrine models", "regulator expression and occupancy resources", "LHX5 regulator evidence does not establish RBPJL or Mt-Cyb functional regulation."),
    "pou6f2": ("POU6F2", "https://pubmed.ncbi.nlm.nih.gov/27425396/", "", "primary_literature_regulator_level", "human RPF-1/POU6F2 models", "DNA binding, ChIP-chip candidates, and transactivation", "POU6F2 regulator capacity does not validate CDKN2A."),
    "thap7": ("THAP7", "https://pubmed.ncbi.nlm.nih.gov/15561719/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6634299/", "primary_literature_regulator_level", "human chromatin/corepressor models", "HDAC3/NCoR corepression and CDKN1A studies", "THAP7 evidence concerns nonqueued promoters and CDKN1A, not CDKN2A."),
    "znf114": ("ZNF114", "https://tflink.net/protein/q8nc26/", "https://pubmed.ncbi.nlm.nih.gov/27924024/", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "ChIP-derived target-set membership", "ZNF114 target-set evidence is occupancy/database support without functional direction."),
    "znf135": ("ZNF135", "https://remap.univ-amu.fr/target_page/ZNF135%3A9606", "https://pubmed.ncbi.nlm.nih.gov/22900683/", "authoritative_binding_dataset_only", "human ReMap/HTRI resources", "regulator-level occupancy and curator-inferred target membership", "ZNF135 occupancy does not establish CDKN2A regulation."),
    "znf174": ("ZNF174", "https://pubmed.ncbi.nlm.nih.gov/7673192/", "https://tflink.net/protein/q15697/", "primary_literature_regulator_level", "human promoter-reporter and GTRD models", "DNA-binding repression at nonqueued promoters", "ZNF174 regulates nonqueued PDGF-B/TGF-beta1 promoters; RNF216 remains a binding/database lead."),
    "znf417": ("ZNF417", "https://pubmed.ncbi.nlm.nih.gov/32923624/", "https://pubmed.ncbi.nlm.nih.gov/38345497/", "primary_literature_regulator_level", "human heterochromatin/stress models", "repression and depletion phenotypes", "ZNF417 evidence involves HERVK/SVA and stress phenotypes, not CDKN2A."),
    "znf621": ("ZNF621", "https://remap.univ-amu.fr/target_page/ZNF621%3A9606", "https://tflink.net/protein/q6zss3/", "authoritative_binding_dataset_only", "human ReMap/GTRD resources", "regulator-level occupancy and target-set membership", "ZNF621 occupancy does not establish RALB regulation."),
    "znf653": ("ZNF653", "https://pubmed.ncbi.nlm.nih.gov/12920234/", "https://pubmed.ncbi.nlm.nih.gov/25690854/", "primary_literature_regulator_level", "human nuclear-receptor/C2H2 models", "coregulator function and broad binding", "ZNF653 regulator evidence does not establish CDKN2A."),
    "znf671": ("ZNF671", "https://pubmed.ncbi.nlm.nih.gov/36436566/", "https://pubmed.ncbi.nlm.nih.gov/32158264/", "primary_literature_regulator_level", "human cancer models", "tumor-suppressive pathway perturbation", "ZNF671 evidence involves Notch/Wnt pathways, not CDKN2A."),
    "z xda": ("ZXDA", "https://doi.org/10.1016/j.jmb.2007.04.033", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9260856/", "primary_literature_regulator_level", "human MHC-II and centromeric chromatin models", "CIITA transcription and chromatin studies", "ZXDA/ZXDC and ZXDA/B evidence does not establish CDKN2A regulation."),
    "zxda": ("ZXDA", "https://doi.org/10.1016/j.jmb.2007.04.033", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9260856/", "primary_literature_regulator_level", "human MHC-II and centromeric chromatin models", "CIITA transcription and chromatin studies", "ZXDA/ZXDC and ZXDA/B evidence does not establish CDKN2A regulation."),
    "nkx2-8": ("Nkx2-8/Nkx2-9", "https://pubmed.ncbi.nlm.nih.gov/23604637/", "https://www.ncbi.nlm.nih.gov/gene/18094", "primary_literature_regulator_level", "human ESCC and mouse airway models", "AKIP1 promoter binding/perturbation in human; mouse regulator studies", "Human NKX2-8-AKIP1 evidence is not exact mouse Nkx2-9-Akip1 evidence."),
    "nobox": ("NOBOX", "https://pubmed.ncbi.nlm.nih.gov/16997917/", "https://pubmed.ncbi.nlm.nih.gov/17494914/", "primary_literature_regulator_level", "mouse oocyte models", "Pou5f1 promoter ChIP, reporter, and loss-of-function", "NOBOX-Pou5f1 is an exact functional pair, but evidence is from oocyte models rather than SCI cells."),
    "znf488": ("Znf488", "https://pubmed.ncbi.nlm.nih.gov/22355521/", "https://pubmed.ncbi.nlm.nih.gov/16908628/", "primary_literature_regulator_level", "mouse oligodendrocyte models", "myelin program and reverse Olig1-to-Zfp488 evidence", "The queued Znf488-to-Olig1 direction is not established; Olig1-to-Zfp488 evidence was not reversed."),
    "zfp57": ("Zfp57", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3210328/", "", "primary_literature_regulator_level", "mouse imprinting-control models", "methylated DNA recognition and KAP1 recruitment", "ZFP57 imprinting evidence does not establish Abca1 or Ackr regulation."),
    "prdm9": ("PRDM9", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5705219/", "", "primary_literature_regulator_level", "human and mouse meiotic chromatin models", "recombination hotspot binding", "PRDM9 meiotic chromatin evidence does not establish the queued targets."),
    "zhx1": ("ZHX1", "https://pubmed.ncbi.nlm.nih.gov/12237128/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6059674/", "primary_literature_regulator_level", "human transcriptional-repressor and cancer-network models", "NF-YA interaction, reporter repression, and network co-occurrence", "ZHX1 regulator evidence does not establish ACKR2, ACTR2, ADAM10, or ADAM17 regulation."),
}

SET_URL = {
    "znf280c": "https://tflink.net/protein/q8nd82/", "znf624": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF624_TARGET_GENES.html", "znf114": "https://tflink.net/protein/q8nc26/", "znf174": "https://tflink.net/protein/q15697/", "znf621": "https://tflink.net/protein/q6zss3/", "znf491": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF491_TARGET_GENES.html", "lhx5": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/LHX5_TARGET_GENES.html", "znf211": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF211_TARGET_GENES.html", "znf248": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF248_TARGET_GENES.html",
}

BINDING_KEYS = {"znf280c", "znf624", "znf114", "znf174", "znf621", "lhx5", "znf211", "znf248"}
DATABASE_KEYS = {"znf746", "dmrta1", "znf135", "znf417", "znf653", "znf671", "zxda", "nobox", "znf488", "zfp57", "prdm9", "zhx1", "pou6f2", "thap7"}


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
    symbol, general_primary, general_corr, kind, model, assay, observation = REGULATORS[key]
    status = "binding_dataset_only_not_promotable" if key in BINDING_KEYS else "database_membership_only_not_promotable"
    primary = SET_URL.get(key, TF_LINK_URL)
    corr = GTRD_URL if key in BINDING_KEYS else ""
    binding = "species_matched_occupancy_or_target_set_lead" if key in BINDING_KEYS else "TFLink_or_curated_database_membership_only"
    downstream = "not_found_for_exact_pair"
    disposition = "retain_as_staging_search_lead_only"
    cell = "not_established_for_exact_pair"
    exclusions = "Regulator-level evidence at nonqueued targets, orthologs, paralogs, reverse-direction relationships, and cross-species models was not transferred."
    notes = "The source record is retained as a search lead only; it does not establish causal direction, target-cell presence, downstream activation, or upstream relay."

    if key == "znf385a" and target in {"cebpa", "tp53"}:
        status = "functional_rna_binding_noncanonical_candidate"
        primary = "https://pubmed.ncbi.nlm.nih.gov/18418387/" if target == "cebpa" else "https://pubmed.ncbi.nlm.nih.gov/21402775/"
        binding = "direct_mouse_mRNA_3prime_UTR_binding"
        downstream = "Hzf_binding_supported_Cebpa_translation_or_p53_expression_and_perturbation"
        disposition = "retain_noncanonical_post_transcriptional_candidate_separately"
        cell = "mouse_adipogenesis_or_p53_models_not_SCI_target_cell"
        notes = "Direct Hzf/Zfp385a RNA 3-prime-UTR binding and perturbation support a post-transcriptional regulator relationship, not promoter-DNA TF evidence; keep in the noncanonical regulator category."
    elif key == "esx1" and target == "kras":
        status = "fragment_context_functional_candidate_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/15897875/"
        binding = "ESX1_ESXR1_N_terminal_homeodomain_fragment_binds_KRAS_intron"
        downstream = "fragment_reduced_KRAS_mRNA_protein_and_proliferation"
        disposition = "retain_fragment_context_candidate_separately"
        cell = "human_model_processed_ESX1_fragment_not_full_length_SCI_context"
        exclusions = "The study used an ectopic processed ESX1/ESXR1 N-terminal homeodomain fragment; it was not treated as full-length ESX1 evidence."
        notes = "This is strong target-specific fragment binding/function, but the tested product is a processed ESX1 fragment, so it remains below an exact full-length TF promotion."
    elif key == "hoxd10" and target == "hoxd9":
        status = "direct_binding_reporter_candidate_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC453170/"
        binding = "HOX4D_HOXD10_binds_HOX4C_HOXD9_promoter_element"
        downstream = "cotransfection_reporter_transactivation_without_endogenous_HOXD9_validation"
        disposition = "retain_promoter_reporter_candidate_separately"
        notes = "Older human promoter-element assays support binding and reporter activation, but endogenous HOXD9 expression and SCI-cell context were not established."
    elif key == "znf385a":
        status = "database_membership_only_not_promotable"
        primary = TF_LINK_URL
        notes = "Only the queued RNA-regulator target pairs have direct post-transcriptional evidence; no other queued relationship was inferred."
    elif key == "znf513":
        pass
    elif key == "nkx2-8" and target == "akip1":
        status = "ortholog_species_near_match_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/23604637/"
        corr = "https://www.ncbi.nlm.nih.gov/gene/18094"
        binding = "human_NKX2_8_AKIP1_promoter_binding_not_mouse_Nkx2_9"
        downstream = "human_AKIP1_expression_promoter_reporter_and_angiogenesis_effects"
        disposition = "retain_ortholog_species_near_match_separately"
        cell = "human_ESCC_model_not_exact_mouse_Nkx2-9_or_SCI_cell"
        exclusions = "Human NKX2-8-AKIP1 evidence was not transferred to the mouse Nkx2-9/Akip1 row."
        notes = "Strong human NKX2-8-AKIP1 binding/function exists, but the queued row is mouse and the official mouse record is Nkx2-9; do not promote the mouse edge."
    elif key == "nobox" and target == "pou5f1":
        status = "functional_direct_binding_promotion_candidate"
        primary = "https://pubmed.ncbi.nlm.nih.gov/16997917/"
        corr = "https://pubmed.ncbi.nlm.nih.gov/17494914/"
        binding = "NOBOX_direct_Pou5f1_promoter_ChIP_and_reporter_binding"
        downstream = "Nobox_loss_reduced_Pou5f1_and_NOBOX_increased_Pou5f1_reporter_activity"
        disposition = "promotion_candidate_pending_SCI_target_cell_context"
        cell = "mouse_oocyte_models_not_SCI_target_cell"
        exclusions = "The exact NOBOX-Pou5f1 evidence is retained as staging evidence from mouse oocyte models; oocyte context was not transferred to SCI cells."
        notes = "NOBOX binds the mouse Pou5f1 promoter, increases reporter activity, and Nobox loss reduces Pou5f1 expression. This meets the exact functional/binding staging threshold but remains non-exportable pending SCI-cell context."
    elif key == "znf488" and target == "olig1":
        status = "reverse_direction_near_match_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/16908628/"
        binding = "Olig1_to_Zfp488_direction_not_Zfp488_to_Olig1"
        downstream = "reverse_direction_reporter_or_lineage_evidence"
        disposition = "retain_reverse_direction_near_match_separately"
        notes = "The literature supports Olig1 preceding/regulating Zfp488, not Zfp488 regulating Olig1; direction was not reversed."
    elif key in {"hoxd8", "isl2"}:
        status = "contextual_near_match_not_promotable"
    elif key == "isl2" and target == "foxp2":
        status = "contextual_near_match_not_promotable"
    elif key == "znf653" or key == "znf671" or key == "zxda":
        status = "database_membership_only_not_promotable"
        primary = TF_LINK_URL
        binding = "TFLink_membership_only_no_queued_target_occupancy_verified"
    elif key == "zfp57" or key == "prdm9" or key == "zhx1":
        status = "database_membership_only_not_promotable"
        primary = TF_LINK_URL
        binding = "TFLink_membership_only_no_queued_target_occupancy_verified"

    return {"symbol": symbol, "general_primary": general_primary, "general_corr": general_corr, "kind": kind, "model": model, "assay": assay, "observation": observation, "status": status, "primary": primary, "corr": corr, "cell": cell, "binding": binding, "downstream": downstream, "disposition": disposition, "exclusions": exclusions, "notes": notes}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_BATCH.parent)
    args = parser.parse_args()
    rows = read_tsv(args.batch)
    if len(rows) != 38:
        raise SystemExit(f"expected 38 rows, found {len(rows)}")
    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        info = classify(row)
        pairs.append({"review_id": f"public_tf_evidence_batch015_pair_{int(row['batch_rank']):02d}_{row['target_rank']}", "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"], "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"], "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"], "exact_pair_search_url": search_url(info["symbol"], row["target_symbol"], row["species_scope"]), "exact_pair_status": info["status"], "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence", "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"], "downstream_expression_or_perturbation_status": info["downstream"], "downstream_activation_status": "not_established_for_SCI_target_cell", "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"], "primary_citation": info["primary"], "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"], "review_notes": info["notes"] + " " + info["observation"], "exportable": "false", "canonical_write_performed": "false"})
        if key not in seen:
            relevance = "regulator-level evidence only"
            if key == "znf385a":
                relevance = "noncanonical post-transcriptional regulator candidate; not Module 22B promoter-TF evidence"
            evidence.append({"evidence_id": f"public_tf_evidence_batch015_regulator_{key}", "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"], "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"], "effect_direction": "queued-pair direction not established except explicitly staged exact candidates", "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"], "route_or_module_relevance": relevance, "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred", "exportable": "false", "canonical_write_performed": "false", "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay. Noncanonical RNA-binding evidence is not treated as promoter TF evidence."})
        seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch015_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch015_regulator_register.tsv"
    summary_path = args.output_dir / "batch_015_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH015.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(item["regulator_key"], item["target_symbol"], item["species_scope"], item["source_record_id"]) for item in pairs}
    summary = {"status": "staging_only", "batch_id": "public_tf_evidence_batch_015", "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys), "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "exact_pair_support_rows": status_counts.get("functional_direct_binding_promotion_candidate", 0), "promotion_candidate_rows": status_counts.get("functional_direct_binding_promotion_candidate", 0), "noncanonical_rna_binding_candidate_rows": status_counts.get("functional_rna_binding_noncanonical_candidate", 0), "partial_or_near_match_rows": sum(v for k, v in status_counts.items() if "near_match" in k or "candidate_not_promotable" in k or "partial_" in k), "binding_dataset_only_not_promotable_rows": status_counts.get("binding_dataset_only_not_promotable", 0) + status_counts.get("direct_binding_only_not_promotable", 0), "database_membership_only_not_promotable_rows": status_counts.get("database_membership_only_not_promotable", 0), "bounded_negative_rows": status_counts.get("no_exact_pair_support_found_in_bounded_search", 0), "exportable_pair_rows": 0, "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True, "limitations": ["TFLink/GTRD/HTRI membership or occupancy is not causal regulation.", "Exact pair negatives are bounded-search results, not global absence.", "Near matches across genes, directions, isoforms, species, and regulator categories were retained separately and not transferred.", "ZNF385A/Hzf Cebpa and Tp53 evidence is post-transcriptional RNA binding and is not treated as canonical promoter-TF evidence.", "No canonical or Module 22B write was performed."], "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))]}
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join(["# Evidence review: public TF batch 015", "", "Reviewed 38 exact regulator-target-species pairs across 25 selected source-set ranks.", "", f"- **{len(pairs)} / 38** pairs were reviewed.", f"- **{summary['promotion_candidate_rows']}** exact TF promotion candidates were staged; NOBOX-Pou5f1 remains pending SCI-cell context.", f"- **{summary['noncanonical_rna_binding_candidate_rows']}** exact noncanonical RNA-binding candidates were kept separate from promoter-TF evidence.", f"- **{summary['binding_dataset_only_not_promotable_rows']}** pairs had occupancy/binding leads.", f"- **{summary['database_membership_only_not_promotable_rows']}** pairs remained database/curation-only leads.", f"- **{summary['partial_or_near_match_rows']}** partial, fragment, ortholog, reverse-direction, or reporter-limited cases were kept separate.", "- **0** rows are exportable; no canonical or Module 22B writes were performed.", "", "ESX1-KRAS and HOXD10-HOXD9 were retained as strong but limited context candidates; human NKX2-8-AKIP1 evidence was not transferred to the queued mouse row. Target-cell presence, downstream activation, and upstream relay remain unestablished.", ""]), encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
