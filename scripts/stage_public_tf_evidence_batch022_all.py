#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 022 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_022/"
    "public_tf_evidence_collection_batch_022.tsv"
)
TF_LINK_URL = "https://tflink.net/download/#interaction-gmt"
PAIR_FIELDS = ["review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol", "species_scope", "source_registry", "source_record_id", "raw_tf_symbol", "target_symbol", "target_graph_modules", "candidate_membership_status", "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status", "target_cell_presence_status", "binding_or_association_status", "downstream_expression_or_perturbation_status", "downstream_activation_status", "upstream_relay_status", "disposition", "primary_citation", "corroborating_citation", "near_match_exclusions", "review_notes", "exportable", "canonical_write_performed"]
EVIDENCE_FIELDS = ["evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer", "support_kind", "cell_or_model", "assay_or_perturbation", "observation", "effect_direction", "primary_citation", "corroborating_citation", "route_or_module_relevance", "target_pair_scope", "exportable", "canonical_write_performed", "limitations"]

# symbol, primary citation, corroborating citation, support kind, model, assay, observation, relevance
REGULATORS = {
    "wiz": ("WIZ", "https://elifesciences.org/articles/15082", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE76909", "primary_literature_regulator_level", "mouse brain chromatin models", "ChIP-seq/RNA-seq and haploinsufficiency", "WIZ occupies active promoters and CTCF-associated regions; queued targets were not validated.", "noncanonical chromatin regulator capacity only"),
    "ubn1": ("UBN1", "https://pubmed.ncbi.nlm.nih.gov/30285846/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3974909/", "primary_literature_regulator_level", "human and mouse HIRA/H3.3 models", "ChIP-seq and UBN1/HIRA perturbation", "UBN1 is an HIRA-complex histone chaperone with active-promoter/enhancer evidence; queued target function was not shown.", "noncanonical chromatin chaperone capacity only"),
    "emsy": ("EMSY", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4817164/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3309773/", "primary_literature_regulator_level", "human chromatin and interferon models", "ChIP-seq, knockout/rescue, and promoter repression", "EMSY/KDM5A/SIN3B has noncanonical promoter and interferon-regulatory evidence at nonqueued loci.", "noncanonical chromatin-coregulator capacity only"),
    "supt5h": ("SUPT5H/SPT5", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5897773/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5732849/", "primary_literature_regulator_level", "mouse DSIF/Pol II models", "conditional depletion, ChIP, processivity, and differentiation assays", "SUPT5H is a DSIF Pol II pausing/elongation factor; no queued target edge was validated.", "noncanonical transcriptional machinery capacity only"),
    "ints3": ("INTS3", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4349240/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9974566/", "primary_literature_regulator_level", "human Integrator/SOSS models", "promoter-proximal and 3-prime-end recruitment studies", "INTS3 is an Integrator/SOSS component with RNA-processing and termination evidence, not a sequence-specific queued-target TF.", "noncanonical transcriptional machinery capacity only"),
    "phf6": ("PHF6", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11344777/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5495126/", "primary_literature_regulator_level", "human chromatin and B-ALL models", "ChIP-seq, SWI/SNF interaction, chromatin accessibility, and perturbation", "PHF6 is a chromatin-associated transcriptional regulator at nonqueued loci.", "noncanonical chromatin regulator capacity only"),
    "cbx3": ("CBX3/HP1gamma", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5318867/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5358721/", "primary_literature_regulator_level", "mouse activated CD8 T-cell and human chromatin models", "ChIP, deficiency, and chromatin-mark assays", "CBX3/HP1gamma regulates nonqueued immune loci such as Prf1, Gzmb, and Ifng.", "noncanonical chromatin-reader capacity only"),
    "kat8": ("KAT8/MOF", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5482993/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8551339/", "primary_literature_regulator_level", "mouse oocyte and metabolic models", "promoter ChIP, deletion, and expression assays", "KAT8/MOF has direct chromatin and metabolic-gene evidence at nonqueued loci.", "noncanonical chromatin-enzyme capacity only"),
    "zmym3": ("ZMYM3", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9943726/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11224304/", "primary_literature_regulator_level", "human KDM1A/RCOR1 chromatin models", "occupancy, complex, and perturbation studies", "ZMYM3 is a chromatin coregulator with nonqueued CTTN/KDM1A-associated evidence.", "noncanonical transcriptional coregulator capacity only"),
    "med12": ("MED12", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6238599/", "https://pubmed.ncbi.nlm.nih.gov/40888963/", "primary_literature_regulator_level", "human Mediator and ERalpha/STAT1 models", "ChIP, promoter cooperation, and perturbation", "MED12 has coregulator evidence at nonqueued ERalpha and STAT1 target promoters.", "noncanonical transcriptional coregulator capacity only"),
    "zmiz1": ("ZMIZ1", "https://pubmed.ncbi.nlm.nih.gov/17584785/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10370198/", "primary_literature_regulator_level", "human p53/Notch and lymphatic-endothelial models", "promoter cooperation, chromatin accessibility, and expression studies", "ZMIZ1 is a transcriptional co-regulator with nonqueued p21, MYC, and PROX1 evidence.", "noncanonical transcriptional coregulator capacity only"),
    "leo1": ("LEO1", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE130689", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5467213/", "primary_literature_regulator_level", "mouse ESC and PAF1C models", "ChIP-seq and elongation studies", "LEO1 is a PAF1C elongation component; queued mouse targets remain profile-only.", "noncanonical transcriptional machinery capacity only"),
    "smarcc2": ("SMARCC2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11794516/", "https://pubmed.ncbi.nlm.nih.gov/38852505/", "primary_literature_regulator_level", "human SWI/SNF/BAF models", "chromatin occupancy, enhancer accessibility, and perturbation", "SMARCC2 is a SWI/SNF chromatin-remodeling subunit with nonqueued enhancer evidence.", "noncanonical chromatin-remodeler capacity only"),
    "smc5": ("SMC5", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4852767/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11379904/", "primary_literature_regulator_level", "mouse and human SMC5/6 models", "depletion, chromatin association, p53, and proliferation assays", "SMC5 is a genome-architecture/DNA-repair complex component; queued targets were not validated.", "noncanonical chromosome-architecture capacity only"),
    "sirt6": ("SIRT6", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3128103/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6468300/", "primary_literature_regulator_level", "mouse and human fibroblast chromatin models", "ChIP, siRNA, expression, and enhancer studies", "SIRT6 has broad chromatin-regulatory evidence; queued human profile rows and mouse Adam12 are separately limited below.", "noncanonical chromatin-enzyme capacity only"),
    "usp16": ("USP16", "https://pubmed.ncbi.nlm.nih.gov/24784029/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9178006/", "primary_literature_regulator_level", "mouse ESC and oocyte models", "H2A deubiquitinase perturbation, ChIP, and differentiation/ZGA assays", "USP16 is an H2A deubiquitinase with nonqueued promoter and developmental evidence.", "noncanonical chromatin regulator capacity only"),
    "sfmbt1": ("SFMBT1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3585059/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3779763/", "primary_literature_regulator_level", "human and mouse chromatin-corepressor models", "occupancy, LSD1/CoREST/Polycomb interaction, and perturbation", "SFMBT1 is a chromatin reader/corepressor with nonqueued Myogenin, histone, SIX2, and EMT evidence.", "noncanonical chromatin-corepressor capacity only"),
    "l3mbtl4": ("L3MBTL4", "https://pubmed.ncbi.nlm.nih.gov/27480026/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4969609/", "primary_literature_regulator_level", "human vascular smooth-muscle models", "ChIP-seq, repression, and MAPK readouts", "L3MBTL4 regulates nonqueued LTBP1 and downstream MAPK signaling.", "noncanonical chromatin-coregulator capacity only"),
    "znf687": ("ZNF687", "https://pubmed.ncbi.nlm.nih.gov/38326409/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4746367/", "primary_literature_regulator_level", "human bone and zebrafish transcriptional models", "transcriptional repression, BRD4/SMRT interaction, and disease models", "ZNF687 has nonqueued bone and gfi1aa-associated regulatory evidence.", "noncanonical transcriptional regulator capacity only"),
    "kdm5c": ("KDM5C", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4749408/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10785505/", "primary_literature_regulator_level", "mouse cortical-neuron and human chromatin models", "ChIP-seq, knockout, ChIP-qPCR, and expression studies", "KDM5C has chromatin demethylase evidence at nonqueued loci; mouse Abca1 is separately recorded as perturbation-only.", "noncanonical chromatin-demethylase capacity only"),
    "kdm4a": ("KDM4A", "https://pubmed.ncbi.nlm.nih.gov/22569126/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7517301/", "primary_literature_regulator_level", "mouse myogenesis and human colorectal chromatin models", "demethylase, ChIP, knockdown, and expression assays", "KDM4A is a chromatin demethylase/coregulator; the queued mouse ADAM10 row has only a human near-match.", "noncanonical chromatin-demethylase capacity only"),
    "rybp": ("RYBP", "https://pubmed.ncbi.nlm.nih.gov/10369680/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10630410/", "primary_literature_regulator_level", "human and mouse PRC1/ESC models", "PRC1 interaction, occupancy, and chromatin perturbation", "RYBP is a Polycomb-associated chromatin regulator with nonqueued target evidence.", "noncanonical chromatin-coregulator capacity only"),
    "chd2": ("CHD2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4305392/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6479120/", "primary_literature_regulator_level", "mouse neuronal chromatin models", "chromatin-remodeler occupancy and neural transcription phenotypes", "CHD2 has chromatin-remodeler evidence at nonqueued neuronal loci; Aplp2 profile and Alcam interaction are separately limited.", "noncanonical chromatin-remodeler capacity only"),
    "chaf1b": ("CHAF1B/CAF-1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6235627/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9054786/", "primary_literature_regulator_level", "mouse and human hematopoietic chromatin models", "chromatin assembly, depletion, and lineage-expression studies", "CHAF1B is a chromatin-assembly/lineage regulator with nonqueued CEBPA, FLI1, and RUNX1 evidence.", "noncanonical chromatin-assembly capacity only"),
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
    binding = "TFLink_or_profile_membership_only_no_queued_locus_validation"
    downstream = "not_found_for_exact_pair"
    disposition = "retain_provenance_traceable_candidate_without_promotion"
    exclusions = "TFLink/profile membership is a search lead; broad regulator evidence, orthologs, paralogs, reverse directions, and interaction-only findings were not transferred to this exact pair."
    notes = "No exact target-specific causal edge was established; target-cell presence, downstream activation, and upstream relay are not inferred."

    if key == "ubn1" and row["species_scope"] == "human" and target == "ackr2":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/UBN1_TARGET_GENES.html"
        binding = "GTRD_MSigDB_UBN1_promoter_profile_at_ACKR2_TSS"
        disposition = "retain_binding_profile_lead_separately"
        exclusions = "GTRD/MSigDB promoter-profile membership is occupancy/profile evidence only and lacks UBN1-specific perturbation, direction, and SCI context."
        notes = "Human UBN1-to-ACKR2 profile lead only; not a functional edge."
    elif key == "kat8" and row["species_scope"] == "mouse" and target == "adam10":
        status = "genetic_cooccurrence_only_not_promotable"
        primary = ""
        binding = "no_queued_locus_occupancy_assay_retrieved"
        downstream = "Alzheimer_GWAS_co_locus_reported_without_regulatory_assay"
        disposition = "retain_genetic_cooccurrence_lead_separately"
        exclusions = "A KAT8/ADAM10 genetic co-locus was identified in the search, but it is not a regulator occupancy, perturbation, or expression-direction assay; no qualifying citation was registered."
        notes = "Genetic co-occurrence is not treated as transcriptional regulation."
    elif key == "kdm5a" and row["species_scope"] == "mouse":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE28343"
        cell = "mouse_ESC_profile_not_SCI_target_cell"
        binding = "mouse_KDM5A_ChIP_seq_profile_without_queued_locus_validation"
        disposition = "retain_mouse_binding_profile_lead_separately"
        notes = "Mouse KDM5A rows are broad ChIP/profile leads only."
    elif key == "zmiz1" and row["species_scope"] == "mouse":
        status = "binding_profile_only_not_promotable"
        cell = "mouse_profile_not_SCI_target_cell"
        binding = "TFLink_or_ChIP_profile_lead_without_queued_locus_validation"
        disposition = "retain_mouse_profile_lead_separately"
    elif key == "leo1" and row["species_scope"] == "mouse":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE130689"
        cell = "mouse_ESC_profile_not_SCI_target_cell"
        binding = "mouse_LEO1_ChIP_seq_profile_without_queued_locus_validation"
        disposition = "retain_mouse_binding_profile_lead_separately"
    elif key == "sirt6" and row["species_scope"] == "human" and target in {"actr2", "adipor2", "adm"}:
        status = "binding_profile_only_not_promotable"
        primary = "https://maayanlab.cloud/Harmonizome/gene_set/SIRT6/ENCODE%2BTranscription%2BFactor%2BTargets"
        cell = "human_ENCODE_profile_not_SCI_target_cell"
        binding = "aggregated_SIRT6_ENCODE_profile_membership"
        disposition = "retain_human_binding_profile_lead_separately"
        notes = "Harmonizome/ENCODE SIRT6 profile membership is retained as binding-profile evidence only."
    elif key == "usp16" and target == "adam17":
        status = "binding_profile_only_not_promotable"
        primary = "https://dbarchive.biosciencedbc.jp/kyushu-u/mm9/target/SRX1706970.5.html"
        binding = "aggregated_mouse_ChIP_Atlas_USP16_profile_includes_Adam17"
        disposition = "retain_mouse_binding_profile_lead_separately"
        notes = "Aggregated ChIP-Atlas target-page membership does not establish regulator-specific occupancy or target direction."
    elif key == "kdm5c" and row["species_scope"] == "mouse" and target == "abca1":
        status = "perturbation_association_without_direct_binding_not_promotable"
        primary = "https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202602292131894912"
        cell = "mouse_ApoE_null_and_RAW264_7_oxLDL_models_not_SCI_target_cell"
        binding = "no_KDM5C_ABCA1_occupancy_or_promoter_assay"
        downstream = "KDM5C_reduction_associated_with_increased_ABCA1_and_KDM5C_overexpression_reversed_effect"
        disposition = "retain_same_species_perturbation_association_separately"
        exclusions = "The report provides a perturbation/expression association but no ChIP/promoter occupancy or independent corroboration."
        notes = "Same-species KDM5C-to-Abca1 association is staged without promoting a direct edge."
    elif key == "kdm4a" and row["species_scope"] == "mouse" and target == "adam10":
        status = "contextual_ortholog_near_match_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC7517301/"
        cell = "human_SW480_HCT116_models_not_mouse_SCI_target_cell"
        binding = "human_KDM4A_ChIP_signal_at_ADAM10_promoter_weaker_than_ADAM17"
        downstream = "human_KDM4_family_perturbation_changed_ADAM_expression"
        disposition = "retain_cross_species_near_match_separately"
        exclusions = "Human KDM4A promoter signal and perturbation do not establish the exact mouse Kdm4a-to-Adam10 edge."
        notes = "Human ortholog/species near-match only."
    elif key == "chd2" and row["species_scope"] == "mouse" and target == "alcam":
        status = "protein_interaction_only_not_promotable"
        primary = "https://thebiogrid.org/interaction/3678875"
        binding = "ALCAM_CHD2_crosslinking_mass_spectrometry_interaction"
        disposition = "retain_protein_interaction_lead_separately"
        exclusions = "BioGRID records a protein interaction, not promoter occupancy, transcriptional perturbation, or target-expression direction."
        notes = "Interaction-only evidence is not treated as regulation."
    elif key == "chd2" and row["species_scope"] == "mouse" and target == "aplp2":
        status = "binding_profile_only_not_promotable"
        primary = "https://maayanlab.cloud/Harmonizome/gene_set/CHD2/ENCODE%2BTranscription%2BFactor%2BTargets"
        corr = "https://chip-atlas.org/target_genes"
        binding = "aggregated_CHD2_ENCODE_profile_membership"
        disposition = "retain_mouse_binding_profile_lead_separately"
        notes = "CHD2 profile membership is potential binding evidence only and has no target-specific perturbation direction."

    return {"symbol": symbol, "general_primary": general_primary, "general_corr": general_corr, "kind": kind, "model": model, "assay": assay, "observation": observation, "relevance": relevance, "status": status, "primary": primary, "corr": corr, "cell": cell, "binding": binding, "downstream": downstream, "disposition": disposition, "exclusions": exclusions, "notes": notes}


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
            "review_id": f"public_tf_evidence_batch022_pair_{int(row['batch_rank']):02d}_{row['target_rank']}", "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"], "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"], "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"], "exact_pair_search_url": search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]), "exact_pair_status": info["status"], "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence", "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"], "downstream_expression_or_perturbation_status": info["downstream"], "downstream_activation_status": "not_established_for_SCI_target_cell", "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"], "primary_citation": info["primary"], "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"], "review_notes": info["notes"] + " " + info["observation"], "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen:
            evidence.append({"evidence_id": f"public_tf_evidence_batch022_regulator_{key}", "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"], "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"], "effect_direction": "queued-pair direction not established except explicitly recorded limited associations", "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"], "route_or_module_relevance": info["relevance"], "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred", "exportable": "false", "canonical_write_performed": "false", "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay. Profile, chromatin, cofactor, machinery, genetic, interaction, and cross-species evidence is retained separately from canonical promoter-TF evidence."})
            seen.add(key)
    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch022_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch022_regulator_register.tsv"
    summary_path = args.output_dir / "batch_022_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH022.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(item["regulator_key"], item["target_symbol"], item["species_scope"], item["source_record_id"]) for item in pairs}
    summary = {"status": "staging_only", "batch_id": "public_tf_evidence_batch_022", "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys), "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "strict_tf_promotion_candidate_rows": 0, "noncanonical_exact_candidate_rows": 0, "exportable_pair_rows": 0, "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True, "limitations": ["TFLink/profile resources are search leads, not causal regulation.", "Exact-pair negatives are bounded search results, not global absence.", "KDM5C-to-Abca1 is perturbation-only without direct occupancy; KDM4A-to-Adam10 and SIRT6-to-Adam12 are cross-species/contextual leads; CHD2 interaction/profile evidence is not regulation.", "No canonical or Module 22B write was performed."], "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))]}
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join(["# Evidence review: public TF batch 022", "", "Reviewed 100 exact regulator-target-species pairs across 25 noncanonical TFLink source-set ranks.", "", f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.", f"- **{status_counts.get('binding_profile_only_not_promotable', 0)}** profile-only rows, one genetic co-occurrence, one same-species perturbation association, one protein-interaction row, and two contextual/profile near-match classes were retained without promotion.", "- **0** strict TF or exact noncanonical functional promotion candidates, exportable rows, canonical writes, or Module 22B writes.", "", "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping, and local source snapshot. Regulator-level chromatin, cofactor, machinery, profile, genetic, interaction, and cross-species evidence is recorded separately from exact canonical TF evidence.", ""]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
