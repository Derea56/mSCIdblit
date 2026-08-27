#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 028 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/"
    "candidate_triage_v1/evidence_batches/batch_028/"
    "public_tf_evidence_collection_batch_028.tsv"
)
TF_LINK_URL = "https://tflink.net/download/"
PAIR_FIELDS = [
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol", "species_scope",
    "source_registry", "source_record_id", "raw_tf_symbol", "target_symbol", "target_graph_modules",
    "candidate_membership_status", "exact_pair_search_url", "exact_pair_status",
    "regulator_general_evidence_status", "target_cell_presence_status", "binding_or_association_status",
    "downstream_expression_or_perturbation_status", "downstream_activation_status", "upstream_relay_status",
    "disposition", "primary_citation", "corroborating_citation", "near_match_exclusions", "review_notes",
    "exportable", "canonical_write_performed",
]
EVIDENCE_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer", "support_kind",
    "cell_or_model", "assay_or_perturbation", "observation", "effect_direction", "primary_citation",
    "corroborating_citation", "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]


# symbol, primary, corroboration, support kind, model, assay, observation,
# route/module relevance, profile URL.
REGULATORS = {
    "elob": ("ELOB", "https://www.ncbi.nlm.nih.gov/gene/67673", "https://pubmed.ncbi.nlm.nih.gov/9869640/", "authoritative_annotation_and_primary_literature", "mouse elongin/VHL-complex models", "Elongin-complex and protein-adaptor assays", "ELOB is an elongin-complex adaptor, not a strict sequence-specific TF; no queued target was shown.", "noncanonical protein/transcriptional-complex capacity only", ""),
    "u2af1": ("U2AF1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4429597/", "https://pubmed.ncbi.nlm.nih.gov/10617206/", "primary_literature_regulator_level", "human spliceosome/RNA-binding models", "RNA binding, splice-site recognition and splicing perturbation", "U2AF1 is an RNA-binding spliceosomal regulator; no queued transcript was linked with target-specific direction.", "noncanonical RNA-processing capacity only", ""),
    "taf9b": ("TAF9B", "https://pubmed.ncbi.nlm.nih.gov/25006164/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC1140618/", "primary_literature_regulator_level", "mouse neuronal core-promoter models", "ChIP-seq, knockout and TAF9/TAF9B complex assays", "TAF9B is a noncanonical core-promoter regulator with nonqueued neuronal target evidence; queued targets were not validated.", "noncanonical transcriptional-machinery capacity only", ""),
    "palb2": ("PALB2", "https://www.ncbi.nlm.nih.gov/gene/79728", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4094107/", "authoritative_annotation_and_primary_literature", "human BRCA1/BRCA2/RAD51 DNA-repair models", "DNA-repair, chromatin and protein-complex assays", "PALB2 is a DNA-repair scaffold, not a strict TF; no queued receptor/transporter target mechanism was found.", "noncanonical DNA-repair/chromatin capacity only", ""),
    "gspt2": ("GSPT2/eRF3b", "https://www.ncbi.nlm.nih.gov/gene/23708", "https://pmc.ncbi.nlm.nih.gov/articles/PMC1168810/", "authoritative_annotation_and_primary_literature", "human translation-termination models", "eRF1-dependent translation and protein-complex assays", "GSPT2 is a translation-termination/protein regulator; GSPT1 paralog context is not transferable to queued targets.", "noncanonical translation/protein-regulator capacity only", ""),
    "sumo1": ("SUMO1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3488252/", "https://www.uniprot.org/uniprotkb/P63166/entry", "primary_literature_regulator_level", "human and mouse SUMO/chromatin models", "chromatin-affinity sequencing, sumoylation and expression assays", "SUMO1 is a ubiquitin-like protein modifier, not a sequence-specific TF; the queued mouse rows lack target-specific direction.", "noncanonical chromatin/protein-modifier capacity only", ""),
    "morc3": ("MORC3", "https://pubmed.ncbi.nlm.nih.gov/27528681/", "https://www.nature.com/articles/s41467-021-26288-7", "primary_literature_regulator_level", "mouse ES-cell chromatin/ERV models", "ChIP-seq, H3K4 localization, ERV silencing and perturbation", "MORC3 is a noncanonical chromatin/ATPase regulator; queued target loci were not validated.", "noncanonical chromatin-silencing capacity only", ""),
    "safb": ("SAFB", "https://pubmed.ncbi.nlm.nih.gov/19901029/", "https://pubmed.ncbi.nlm.nih.gov/37468167/", "primary_literature_regulator_level", "human and mouse DNA/RNA-binding scaffold models", "ChIP, S/MAR binding, RNA association and perturbation", "SAFB is a DNA/RNA-binding chromatin scaffold and transcription/splicing cofactor, but none of the queued targets was validated.", "noncanonical chromatin/RNA-coregulator capacity only", ""),
    "ddx20": ("DDX20/Gemin3", "https://pubmed.ncbi.nlm.nih.gov/10601333/", "https://pubmed.ncbi.nlm.nih.gov/14699164/", "primary_literature_regulator_level", "human RNA-helicase/protein-complex models", "RNA helicase, EGR interaction and promoter-repression assays", "DDX20 is primarily an RNA helicase and protein-complex cofactor; queued targets were not validated.", "noncanonical RNA/protein-coregulator capacity only", ""),
    "tcf25": ("TCF25/NULP1", "https://www.uniprot.org/uniprotkb/Q9BQ70/entry", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7660797/", "primary_literature_regulator_level", "human NFAT and ribosome-quality-control models", "protein interaction, reporter and RQC assays", "TCF25 has uncertain historical DNA-binding annotation; stronger evidence supports noncanonical protein/RQC functions, not queued mRNA targets.", "noncanonical protein/transcriptional-coregulator capacity only", ""),
    "prkdc": ("PRKDC/DNA-PKcs", "https://www.ncbi.nlm.nih.gov/gene/5591", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5355436/", "authoritative_annotation_and_primary_literature", "human DNA-repair and transcriptional-coregulator models", "DNA-dependent kinase, chromatin and AR-coregulator assays", "PRKDC is a DNA-repair kinase with noncanonical transcriptional roles; ACTR2 is only a GTRD profile lead and other queued targets were unsupported.", "noncanonical kinase/chromatin capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/PRKDC_TARGET_GENES.html"),
    "setx": ("SETX", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10085699/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8915885/", "primary_literature_regulator_level", "human R-loop/transcription-termination models", "R-loop binding/unwinding, RNAPII termination and chromatin assays", "SETX is a noncanonical RNA/DNA helicase and termination factor with nonqueued KRT1/ZNF750 context; queued targets were unsupported.", "noncanonical RNA/transcription-termination capacity only", ""),
    "zc3h11a": ("ZC3H11A", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5910864/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10266022/", "primary_literature_regulator_level", "mouse RNA-export/developmental models", "RNA binding, mRNA export and knockout assays", "ZC3H11A is an RNA-binding/post-transcriptional regulator; queued target rows are GTRD profile-only.", "noncanonical RNA-processing capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/ZC3H11A_TARGET_GENES.html"),
    "prkcq": ("PRKCQ/PKCtheta", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2193906/", "https://www.ncbi.nlm.nih.gov/gene/5588", "primary_literature_regulator_level", "mouse T-cell kinase/signaling models", "kinase, TCR signaling and NFAT/NF-kB/AP-1 assays", "PRKCQ is a T-cell signaling kinase, not a DNA-binding TF; queued targets were unsupported.", "noncanonical kinase/signaling capacity only", ""),
    "ogt": ("OGT", "https://pubmed.ncbi.nlm.nih.gov/12150998/", "https://pubmed.ncbi.nlm.nih.gov/22371499/", "primary_literature_regulator_level", "human and mouse chromatin/O-GlcNAc models", "promoter recruitment, O-GlcNAc and GR-transrepression assays", "OGT is an O-GlcNAc transferase and chromatin-associated protein; queued mouse rows are profile-only.", "noncanonical chromatin/protein-modifier capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/OGT_TARGET_GENES.html"),
    "tex10": ("TEX10", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4458159/", "", "primary_literature_regulator_level", "mouse ESC chromatin/transcription models", "FLAG-ChIP occupancy, depletion and expression assays", "TEX10 is a noncanonical chromatin/transcription regulator; queued mouse rows are aggregate profile leads.", "noncanonical chromatin/transcriptional capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/TEX10_TARGET_GENES"),
    "ebp": ("EBP", "https://www.uniprot.org/uniprotkb/Q15125/entry", "https://pubmed.ncbi.nlm.nih.gov/12760743/", "authoritative_annotation_and_primary_literature", "human ER/microsomal sterol-isomerase models", "sterol-isomerase, ligand-binding and structural assays", "EBP is an ER sterol isomerase/ligand-binding protein, not a TF; EBP1/PA2G4 and C/EBP evidence are distinct regulators.", "noncanonical protein/ligand capacity only", ""),
    "msl1": ("MSL1", "https://www.uniprot.org/uniprotkb/Q6PDM1/entry", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE57698", "primary_literature_regulator_level", "mouse MSL chromatin-complex models", "ChIP-seq, knockdown RNA-seq and histone-acetyltransferase complex assays", "MSL1 is a noncanonical chromatin-complex scaffold; queued rows are profile-only.", "noncanonical chromatin-complex capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/MSL1_TARGET_GENES.html"),
    "supt16h": ("SUPT16H/SPT16", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10403911/", "https://www.uniprot.org/uniprotkb/Q920B9/entry", "primary_literature_regulator_level", "mouse FACT/ESC transcription-elongation models", "AID depletion, CUT&RUN, TT-seq and nascent-transcription assays", "SUPT16H is a FACT histone-chaperone/elongation regulator; queued rows are profile-only.", "noncanonical transcriptional-machinery capacity only", ""),
    "prpf4": ("PRPF4", "https://pubmed.ncbi.nlm.nih.gov/9404889/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4226509/", "primary_literature_regulator_level", "human spliceosomal U4/U6-U5 models", "snRNP complex purification and splicing assays", "PRPF4 is a spliceosomal factor, not a DNA-binding regulator; queued targets were unsupported.", "noncanonical RNA-processing capacity only", ""),
    "zmynd8": ("ZMYND8", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6152903/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4742736/", "primary_literature_regulator_level", "human chromatin-reader/cofactor models", "ChIP, P-TEFb/cofactor and neuronal perturbation assays", "ZMYND8 is a noncanonical chromatin reader/cofactor; ADIPOR2 evidence belongs to ATF3, not ZMYND8.", "noncanonical chromatin-reader capacity only", ""),
    "pdhx": ("PDHX", "https://www.uniprot.org/uniprotkb/O00330-3/entry", "", "authoritative_annotation_only", "human mitochondrial pyruvate-dehydrogenase models", "complex and metabolic assays", "PDHX is a mitochondrial pyruvate-dehydrogenase-complex component, not a DNA-binding regulator.", "not a transcriptional-regulator mechanism", ""),
    "myh11": ("MYH11", "https://www.uniprot.org/uniprotkb/P35749/entry", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5355061/", "authoritative_annotation_and_primary_literature", "human smooth-muscle/fusion-oncoprotein models", "myosin and CBFB-MYH11 fusion transcriptional assays", "Wild-type MYH11 is a myosin motor; CBFB-MYH11 fusion effects do not establish wild-type MYH11 regulation of queued targets.", "not a wild-type transcriptional-regulator mechanism", ""),
    "spin1": ("SPIN1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5775400/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4467114/", "primary_literature_regulator_level", "mouse histone-reader/myoblast models", "histone-mark binding, ChIP and conditional-loss assays", "SPIN1 is a noncanonical histone-mark reader/coactivator with nonqueued Myf5/Myod1/GDNF evidence.", "noncanonical chromatin-reader/coactivator capacity only", ""),
    "sigmar1": ("SIGMAR1", "https://pubmed.ncbi.nlm.nih.gov/26560551/", "", "primary_literature_regulator_level", "mouse ER/MAM chaperone and ligand-response models", "ligand treatment, receptor/chaperone and neuronal expression assays", "SIGMAR1 is a ligand-regulated ER/MAM chaperone/signaling scaffold, not a DNA-binding TF; queued rows have only pharmacologic or other-regulator near-matches.", "noncanonical receptor/chaperone signaling capacity only", ""),
}

PROFILE_TARGETS = {
    "prkdc": {"actr2"}, "zc3h11a": {"acvr1c", "adgre5", "alcam", "app"},
    "ogt": {"adgrl1", "anxa2", "c1ql1", "c1ql4"}, "tex10": {"ackr4", "adcyap1", "adgrb1", "adgrb3"},
    "msl1": {"adgrl2", "apoe", "bmp6", "ccl25"}, "supt16h": {"actr2", "acvr1", "acvr1c", "adam22"},
    "mier1": {"adcyap1"}, "sumo1": set(),
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


def profile_status(row: dict[str, str], info: tuple[str, ...]) -> dict[str, str]:
    _symbol, primary, corr, _kind, _model, _assay, _obs, _rel, profile = info
    return {"status": "binding_profile_only_not_promotable", "primary": profile or TF_LINK_URL, "corr": corr if profile else "", "cell": f"{row['species_scope']}_aggregate_profile_not_SCI_target_cell", "binding": f"{row['species_scope']}_promoter_profile_membership_without_queued_locus_validation", "downstream": "no_target_specific_perturbation_or_direction_found", "disposition": "retain_binding_profile_lead_separately", "exclusions": "Aggregate TFLink/GTRD/profile membership is a search lead; it does not establish target-cell presence, causal direction, downstream activation or an upstream relay.", "notes": "Profile-only evidence was retained without promoting the exact pair."}


def classify(row: dict[str, str]) -> dict[str, str]:
    key = row["regulator_key"]
    target = row["target_symbol"].lower()
    info = REGULATORS[key]
    symbol, general_primary, general_corr, kind, model, assay, observation, relevance, _profile = info
    out = {"symbol": symbol, "general_primary": general_primary, "general_corr": general_corr, "kind": kind, "model": model, "assay": assay, "observation": observation, "relevance": relevance, "status": "database_membership_only_not_promotable", "primary": TF_LINK_URL, "corr": "", "cell": "not_established_for_exact_pair", "binding": "TFLink_membership_only_no_queued_locus_validation", "downstream": "not_found_for_exact_pair", "disposition": "retain_provenance_traceable_candidate_without_promotion", "exclusions": "TFLink/database membership is a search lead; broad regulator evidence, orthologs, paralogs, reverse directions and complex-level findings were not transferred to this exact pair.", "notes": "No exact target-specific causal edge was established; target-cell presence, downstream activation and upstream relay are not inferred."}
    if key == "sumo1" and target == "adgrl1":
        out.update(status="cross_species_profile_near_match_not_promotable", primary="https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/SUMO1_TARGET_GENES.html", cell="human_profile_not_mouse_SCI_target_cell", binding="human_SUMO1_profile_contains_ADGRL1_without_mouse_locus_validation", disposition="retain_cross_species_profile_near_match_separately", exclusions="Human SUMO1 profile membership does not establish mouse Sumo1 occupancy or target direction.", notes="Cross-species profile near-match only.")
    elif key == "ebp" and target in {"bcl2", "bdnf"}:
        out.update(status="paralog_or_other_regulator_near_match_not_promotable", primary="https://pubmed.ncbi.nlm.nih.gov/16396631/" if target == "bcl2" else "https://pmc.ncbi.nlm.nih.gov/articles/PMC7044735/", cell="human_near_match_model_not_SCI_target_cell", binding="EBP1_or_C_EBP_family_evidence_not_EBP", downstream="other_regulator_direction_not_EBP_specific", disposition="retain_paralog_or_other_regulator_near_match_separately", exclusions="EBP1/PA2G4 or C/EBP evidence is not interchangeable with EBP/sterol-isomerase and does not validate the exact EBP edge.", notes="Near-match evidence was explicitly excluded from EBP-to-target promotion.")
    elif key == "zmynd8" and target == "adipor2":
        out.update(status="other_regulator_near_match_not_promotable", primary="https://pubmed.ncbi.nlm.nih.gov/20423458/", cell="human_HepG2_ATF3_model_not_SCI_target_cell", binding="ATF3_not_ZMYND8_binds_ADIPOR2_promoter", downstream="ATF3_increase_repressed_ADIPOR2", disposition="retain_other_regulator_near_match_separately", exclusions="The ADIPOR2 promoter study supports ATF3, not ZMYND8; regulator identity was not substituted.", notes="ATF3-to-ADIPOR2 evidence is preserved as an explicit regulator-identity exclusion.")
    elif key == "myh11" and target == "bcl2":
        out.update(status="fusion_protein_near_match_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC8321512/", cell="human_AML_CBFB_MYH11_fusion_model_not_wild_type_MYH11_SCI_target_cell", binding="CBFB_MYH11_fusion_transcriptional_effects_not_wild_type_MYH11_occupancy", downstream="fusion_associated_transcriptional_program_not_MYH11_BCL2_specific", disposition="retain_fusion_near_match_separately", exclusions="CBFB-MYH11 fusion activity cannot be assigned to wild-type MYH11 or transferred to the exact queued edge.", notes="Fusion-oncoprotein evidence was not used for wild-type MYH11.")
    elif key == "spin1" and target == "acvr1":
        out["notes"] = "The apparent profile association resolves to Activin/Smad2 data rather than Spin1 ChIP; it was not treated as Spin1 occupancy."
    elif key == "sigmar1" and target == "abca1":
        out.update(status="other_regulator_near_match_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC166346/", corr="https://pmc.ncbi.nlm.nih.gov/articles/PMC207565/", cell="mouse_macrophage_LXR_RARgamma_models_not_SIGMAR1_specific", binding="LXR_or_RARgamma_RXR_not_SIGMAR1_at_ABCA1_promoter", downstream="LXR_or_RARgamma_RXR_induced_Abca1", disposition="retain_other_regulator_near_match_separately", exclusions="The Abca1 promoter evidence belongs to LXR/RARgamma-RXR, not Sigmar1.", notes="Other-regulator promoter evidence was preserved but not transferred.")
    elif key == "sigmar1" and target == "anxa1":
        out.update(status="other_regulator_near_match_not_promotable", primary="https://www.jci.org/articles/view/91445", cell="mouse_muscle_GR_FOXO1_models_not_SIGMAR1_specific", binding="GR_or_FOXO1_not_SIGMAR1_at_Anxa1_promoter", downstream="GR_FOXO1_signaling_induced_Anxa1", disposition="retain_other_regulator_near_match_separately", exclusions="The Anxa1 promoter evidence belongs to glucocorticoid receptor/FOXO1, not Sigmar1.", notes="Other-regulator promoter evidence was preserved but not transferred.")
    elif key == "sigmar1" and target == "arc":
        out.update(status="pharmacologic_cross_species_near_match_not_promotable", primary="https://link.springer.com/article/10.1007/s13311-022-01280-1", cell="rat_primary_hippocampal_and_mouse_APP_PS1_models_not_mouse_SIGMAR1_genetic_model", binding="SIGMAR1_ligand_treatment_not_direct_SIGMAR1_locus_mechanism", downstream="ligand_dependent_Arc_expression_in_rat_with_no_consistent_mouse_tissue_result", disposition="retain_pharmacologic_near_match_separately", exclusions="Pharmacologic ligand response, rat culture and inconsistent mouse tissue results do not establish a direct mouse Sigmar1-to-Arc mechanism.", notes="Pharmacologic cross-species evidence was not promoted.")
    elif key in PROFILE_TARGETS and target in PROFILE_TARGETS[key]:
        out.update(profile_status(row, info))
    return out


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
        info = classify(row)
        pairs.append({"review_id": f"public_tf_evidence_batch028_pair_{int(row['batch_rank']):02d}_{row['target_rank']}", "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": row["regulator_key"], "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"], "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"], "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"], "exact_pair_search_url": search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]), "exact_pair_status": info["status"], "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence", "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"], "downstream_expression_or_perturbation_status": info["downstream"], "downstream_activation_status": "not_established_for_SCI_target_cell", "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"], "primary_citation": info["primary"], "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"], "review_notes": info["notes"] + " " + info["observation"], "exportable": "false", "canonical_write_performed": "false"})
        key = row["regulator_key"]
        if key not in seen:
            evidence.append({"evidence_id": f"public_tf_evidence_batch028_regulator_{key}", "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"], "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"], "effect_direction": "queued-pair direction not established except explicitly recorded limited associations", "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"], "route_or_module_relevance": info["relevance"], "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred", "exportable": "false", "canonical_write_performed": "false", "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation or upstream relay. Profile, chromatin, machinery, protein, RNA, ligand and cross-species evidence is retained separately from canonical promoter-TF evidence."})
            seen.add(key)
    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch028_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch028_regulator_register.tsv"
    summary_path = args.output_dir / "batch_028_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH028.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(x["regulator_key"], x["target_symbol"], x["species_scope"], x["source_record_id"]) for x in pairs}
    summary = {"status": "staging_only", "batch_id": "public_tf_evidence_batch_028", "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys), "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "strict_tf_promotion_candidate_rows": 0, "noncanonical_exact_candidate_rows": 0, "exportable_pair_rows": 0, "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True, "limitations": ["TFLink/profile resources are search leads, not causal regulation.", "Exact-pair negatives are bounded search results, not global absence.", "No row met the exact same-regulator, target, species, direct mechanism and direction standard. Other-regulator, fusion, pharmacologic, cross-species and profile near-matches were kept separate.", "No canonical or Module 22B write was performed."], "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))]}
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join(["# Evidence review: public TF batch 028", "", f"Reviewed {len(pairs)} exact regulator-target-species pairs across 25 TFLink source-set ranks.", "", f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.", f"- **{status_counts.get('binding_profile_only_not_promotable', 0)}** profile-only rows were retained without promotion.", f"- **{status_counts.get('paralog_or_other_regulator_near_match_not_promotable', 0) + status_counts.get('other_regulator_near_match_not_promotable', 0) + status_counts.get('fusion_protein_near_match_not_promotable', 0) + status_counts.get('pharmacologic_cross_species_near_match_not_promotable', 0) + status_counts.get('cross_species_profile_near_match_not_promotable', 0)}** other-regulator, fusion, pharmacologic or cross-species near-match rows were retained separately.", "- **0** strict TF or exact noncanonical promotion candidates, exportable rows, canonical writes or Module 22B writes.", "", "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping and local source snapshot. Profile, chromatin, machinery, protein, RNA, ligand and near-match evidence is recorded separately from exact canonical TF evidence.", ""]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
