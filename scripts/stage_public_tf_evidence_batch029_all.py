#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 029 pairs.

This batch is deliberately staging-only.  Database membership and aggregate
regulon profiles remain provenance-bearing search leads; they are not written
to the canonical models without target-cell validation.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/"
    "candidate_triage_v1/evidence_batches/batch_029/"
    "public_tf_evidence_collection_batch_029.tsv"
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


# symbol, general primary, corroboration, support kind, model, assay,
# observation, route/module relevance, optional aggregate-profile URL.
REGULATORS = {
    "gsk3b": ("GSK3B", "https://www.ncbi.nlm.nih.gov/gene/2932", "https://pmc.ncbi.nlm.nih.gov/articles/PMC317244/", "authoritative_annotation_and_primary_literature", "mouse kinase and cell-cycle models", "kinase assays, mutant cyclin-D1, active/kinase-dead GSK3B and expression assays", "GSK3B is a serine/threonine kinase, not a strict sequence-specific TF; exact mouse Ccnd1 protein regulation is retained separately.", "noncanonical kinase/protein-regulation capacity; exact Ccnd1 protein edge", ""),
    "mcrs1": ("MCRS1", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE239359", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11572484/", "primary_literature_regulator_level", "mouse pancreatic-cancer chromatin models", "MCRS1/YY1 ChIP-seq, accessibility and perturbation assays", "MCRS1 is a noncanonical chromatin/complex regulator with direct occupancy and MHC-I regulation at nonqueued loci; queued targets were not validated.", "noncanonical chromatin/complex capacity only", ""),
    "jph2": ("JPH2/JP2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6336677/", "https://pubmed.ncbi.nlm.nih.gov/30647131/", "primary_literature_regulator_level", "mouse stressed-heart chromatin models", "calpain cleavage, nuclear JP2NT ChIP-seq, EMSA, luciferase, qPCR and pressure-overload assays", "JPH2 can yield nuclear JP2NT, a stress-responsive chromatin regulator with direct nonqueued targets; queued targets were not validated.", "noncanonical stress-responsive chromatin capacity only", ""),
    "hbz": ("HBZ/HBAZ", "https://www.ncbi.nlm.nih.gov/gene?cmd=Retrieve&list_uids=3050", "https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1005560", "authoritative_identity_and_contextual_literature", "human endogenous HBAZ annotation and HTLV-1 HBZ models", "gene identity, viral HBZ protein expression and CADM1 expression assays", "The queued human HBZ symbol is endogenous hemoglobin-zeta/HBAZ; much HBZ literature instead concerns the unrelated HTLV-1 viral protein. No queued endogenous-HBAZ edge was validated.", "identity correction and viral-HBZ near-match only", ""),
    "msl2": ("MSL2", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE183766", "https://pubmed.ncbi.nlm.nih.gov/38030723/", "primary_literature_regulator_level", "mouse neural-progenitor MSL2 knockout/ChIP models", "MSL2 ChIP-seq peak calls and knockout/control RNA-seq", "MSL2 is a noncanonical chromatin/dosage regulator. The queued genes show only dataset-level expression changes without called interval-overlapping MSL2 peaks.", "noncanonical chromatin/dosage capacity; exact rows profile-only", ""),
    "iglv5-37": ("IGLV5-37", "https://www.ncbi.nlm.nih.gov/gene/28783", "https://link.springer.com/article/10.1186/s12885-025-13641-y", "authoritative_identity_and_profile_context", "human immunoglobulin-variable-region and cancer-expression contexts", "gene annotation, aggregate target-set membership and expression studies", "IGLV5-37 is an immunoglobulin variable-region gene, not a sequence-specific TF; the apparent target set is associated with a fusion/other context and does not establish IGLV5-37 regulation.", "not a canonical transcriptional-regulator mechanism", ""),
    "gtf3c1": ("GTF3C1", "https://www.uniprot.org/uniprotkb/Q8K284", "https://reactome.org/content/detail/R-MMU-83697", "authoritative_annotation_and_primary_literature", "mouse TFIIIC and Pol III transcription models", "TFIIIC complex and RNA-polymerase-III recruitment assays", "GTF3C1 is a TFIIIC transcription-machinery subunit for Pol III, not a validated sequence-specific regulator of the queued mRNA loci.", "noncanonical transcriptional-machinery capacity only", ""),
    "mbtd1": ("MBTD1", "https://www.uniprot.org/uniprotkb/Q05BQ5/entry", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2747274/", "authoritative_annotation_and_primary_literature", "human MBTD1 histone-reader/chromatin models", "histone-mark binding, complex and structural assays", "MBTD1 is a chromatin histone-reader/complex component; no queued target-specific occupancy or direction was validated.", "noncanonical chromatin-reader capacity only", ""),
    "nucks1": ("NUCKS1", "https://www.sciencedirect.com/science/article/pii/S2211124714004240", "https://www.uniprot.org/uniprotkb/Q80XU3/entry", "primary_literature_regulator_level", "mouse NUCKS1 chromatin and developmental models", "chromatin association, depletion and expression assays", "NUCKS1 is a chromatin-associated DNA-binding protein with nonqueued regulatory evidence; Adam9, Agrp and Ang are aggregate profile leads only.", "noncanonical chromatin/DNA-associated capacity; profile-only queued rows", "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/NUCKS1_TARGET_GENES.html"),
    "wrnip1": ("WRNIP1", "https://www.uniprot.org/uniprotkb/Q96S55/entry", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4931187/", "authoritative_annotation_and_primary_literature", "human replication-fork and DNA-repair models", "fork protection, DNA-crosslink repair and protein-complex assays", "WRNIP1 is a replication/DNA-repair factor, not a strict TF; queued rows are aggregate profile leads without exact target mechanisms.", "noncanonical DNA-repair/chromatin capacity; profile-only queued rows", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/WRNIP1_TARGET_GENES"),
    "zfp809": ("ZFP809", "https://www.ncbi.nlm.nih.gov/gene/235047", "https://pubmed.ncbi.nlm.nih.gov/19270682/", "primary_literature_regulator_level", "mouse KRAB-ZFP/retroviral-silencing models", "KRAB recruitment, H3K9 methylation and proviral silencing assays", "ZFP809 has genuine KRAB-zinc-finger silencing evidence at retroviral targets, but no queued locus was validated.", "canonical TF identity supported generally; queued edges unsupported", ""),
    "snapc1": ("SNAPC1", "https://www.uniprot.org/uniprotkb/Q16533/entry", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3486178/", "authoritative_annotation_and_primary_literature", "human SNAP complex and Pol II/Pol III promoter models", "SNAP complex assembly and promoter-recognition assays", "SNAPC1 is a general transcription factor complex subunit, not a validated sequence-specific regulator of the queued targets.", "noncanonical transcriptional-machinery capacity only", ""),
    "znf843": ("ZNF843", "https://www.uniprot.org/uniprotkb/Q8N446/entry", "https://tflink.net/protein/q8n446/", "authoritative_identity_and_database_context", "human annotation and zinc-binding database context", "domain annotation and database interaction/profile records", "ZNF843 is undercharacterized; its zinc-finger annotation does not by itself establish queued target occupancy or direction.", "undercharacterized zinc-finger capacity only", ""),
    "smn1": ("SMN1", "https://www.uniprot.org/uniprotkb/Q16637/entry", "https://pubmed.ncbi.nlm.nih.gov/15024064/", "authoritative_annotation_and_primary_literature", "human SMN/RNA-processing and neuronal models", "SMN-complex, RNA-processing and neuronal perturbation assays", "SMN1 is an RNA-processing/RNP-assembly factor, not a strict sequence-specific TF; queued targets were not validated.", "noncanonical RNA/protein-complex capacity only", ""),
    "utp3": ("UTP3", "https://www.ncbi.nlm.nih.gov/gene/65961", "https://pubmed.ncbi.nlm.nih.gov/34516797/", "authoritative_annotation_and_primary_literature", "mouse SSU-processome/ribosome-biogenesis models", "pre-rRNA processing and nucleolar complex assays", "UTP3 is an SSU-processome component, not a regulator of the queued mRNA loci.", "noncanonical RNA-processing machinery only", ""),
    "u2af2": ("U2AF2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4671683/", "https://www.uniprot.org/uniprotkb/P26368/entry", "primary_literature_regulator_level", "human spliceosomal RNA-binding models", "RNA binding, splice-site recognition and interactome assays", "U2AF2 is a spliceosomal RNA-binding factor; queued rows lack direct target-RNA or target-locus validation. APOA1 is only a complex-level near-match.", "noncanonical RNA-processing capacity only", ""),
    "greb1": ("GREB1", "https://pubmed.ncbi.nlm.nih.gov/23403292/", "https://www.gsea-msigdb.org/gsea/msigdb/cards/GREB1_TARGET_GENES", "primary_literature_regulator_level", "human estrogen-responsive cancer models", "ER-associated expression and aggregate regulon profiling", "GREB1 is an estrogen-responsive nuclear regulator; queued target rows are aggregate profile-only and do not establish GREB1 target-gene causality.", "noncanonical estrogen-responsive regulator capacity; profile-only queued rows", "https://www.gsea-msigdb.org/gsea/msigdb/cards/GREB1_TARGET_GENES"),
    "pcna": ("PCNA", "https://www.uniprot.org/uniprotkb/P17918/entry", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6374483/", "authoritative_annotation_and_primary_literature", "mouse replication and cell-cycle models", "DNA-replication, protein-complex and cell-cycle assays", "PCNA is a replication clamp, not a sequence-specific TF; queued rows were unsupported except a reverse beta-catenin/PCNA near-match.", "noncanonical replication/protein-complex capacity only", ""),
    "sumo1": ("SUMO1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3488252/", "https://www.uniprot.org/uniprotkb/P63166/entry", "primary_literature_regulator_level", "human and mouse SUMO/chromatin models", "sumoylation, chromatin association and expression assays", "SUMO1 is a ubiquitin-like protein modifier, not a sequence-specific TF; queued human rows are aggregate profile-only.", "noncanonical chromatin/protein-modifier capacity; profile-only queued rows", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/SUMO1_TARGET_GENES"),
    "zc3h11a": ("ZC3H11A", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5910864/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10266022/", "primary_literature_regulator_level", "human RNA-export and stress-response models", "RNA binding, mRNA export and perturbation assays", "ZC3H11A is an RNA-binding/post-transcriptional regulator; ADA is an aggregate profile lead and the other queued rows lacked target-specific support.", "noncanonical RNA-processing capacity; ADA profile-only lead", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZC3H11A_TARGET_GENES"),
    "zscan5dp": ("ZSCAN5DP", "https://www.ebi.ac.uk/gxa/genes/ENSG00000267908", "https://humantfs.ccbr.utoronto.ca/dbdsTable.php?dbd=C2H2+ZF", "authoritative_identity_and_database_context", "human pseudogene/undercharacterized zinc-finger annotation", "expression and family-level database annotation", "ZSCAN5DP is annotated as a pseudogene/undercharacterized locus; ZSCAN5D-family evidence is not evidence for ZSCAN5DP or the queued targets.", "identity uncertainty and paralog evidence only", ""),
    "ddx21": ("DDX21", "https://graveleylabweb.cam.uchc.edu/encore/gene/index.php?rbp_name=DDX21", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4827702/", "primary_literature_regulator_level", "human RNA-helicase/ribosome-biogenesis models", "iCLIP/ChIP, RNA binding and knockdown assays", "DDX21 is an RNA helicase/RNA-processing regulator with nonqueued ribosomal and snoRNA-associated targets; queued rows were not validated.", "noncanonical RNA-processing capacity only", ""),
    "zfp449": ("ZFP449", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4278888/", "https://www.ncbi.nlm.nih.gov/gene/78619", "primary_literature_regulator_level", "mouse cartilage-development TF models", "yeast one-hybrid, enhancer reporter and expression assays", "ZFP449 has genuine TF-like evidence at nonqueued CES6/Sox6/Sox9/Col2a1 contexts, not the queued targets.", "canonical TF identity supported generally; queued edges unsupported", ""),
    "fxr1": ("FXR1", "https://www.ncbi.nlm.nih.gov/gene/8087", "https://www.encodeproject.org/experiments/ENCSR248TXP/", "authoritative_annotation_and_primary_literature", "human RNA-binding and cancer models", "eCLIP, RNA-binding, depletion and expression assays", "FXR1 is an RNA-binding/post-transcriptional regulator with direct cMYC and other RNA evidence; queued rows lack direct target-RNA validation.", "noncanonical RNA/protein-regulator capacity only", ""),
    "ccl5": ("CCL5", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5127185/", "https://pubmed.ncbi.nlm.nih.gov/27898058/", "primary_literature_regulator_level", "mouse hypothalamic chemokine/CCR5 models", "ligand treatment, receptor antagonism, ex vivo tissue and primary-neuron qPCR assays", "CCL5 is a secreted chemokine ligand; exact Ccl5-to-Agrp evidence is a CCR5-mediated extracellular/RNA-regulatory relationship, not DNA occupancy.", "ligand/receptor signaling and downstream RNA regulation; exact Agrp candidate", ""),
}

PROFILE_TARGETS = {
    "msl2": {"adam17", "adam22", "ang", "ctnnb1"},
    "nucks1": {"adam9", "agrp", "ang"},
    "wrnip1": {"ackr3", "agrn", "artn", "calcrl"},
    "greb1": {"adipoq", "bdkrb1", "ccr3", "cd22"},
    "sumo1": {"adgrl1", "adora2a", "ang", "artn"},
    "zc3h11a": {"ada"},
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
    _symbol, _primary, corr, _kind, _model, _assay, _obs, _rel, profile = info
    return {
        "status": "binding_profile_only_not_promotable",
        "primary": profile or TF_LINK_URL,
        "corr": corr if profile else "",
        "cell": f"{row['species_scope']}_aggregate_profile_not_SCI_target_cell",
        "binding": f"{row['species_scope']}_promoter_profile_membership_without_queued_locus_validation",
        "downstream": "no_target_specific_perturbation_or_direction_found",
        "disposition": "retain_binding_profile_lead_separately",
        "exclusions": "Aggregate TFLink/GTRD/MSigDB/profile membership is a search lead; it does not establish target-cell presence, causal direction, downstream activation or an upstream relay.",
        "notes": "Profile-only evidence was retained without promoting the exact pair.",
    }


def classify(row: dict[str, str]) -> dict[str, str]:
    key = row["regulator_key"]
    target = row["target_symbol"].lower()
    if key not in REGULATORS:
        raise SystemExit(f"missing evidence map for {key}")
    info = REGULATORS[key]
    symbol, general_primary, general_corr, kind, model, assay, observation, relevance, _profile = info
    out = {
        "symbol": symbol, "general_primary": general_primary, "general_corr": general_corr,
        "kind": kind, "model": model, "assay": assay, "observation": observation, "relevance": relevance,
        "status": "database_membership_only_not_promotable", "primary": TF_LINK_URL, "corr": "",
        "cell": "not_established_for_exact_pair", "binding": "TFLink_membership_only_no_queued_locus_validation",
        "downstream": "not_found_for_exact_pair", "disposition": "retain_provenance_traceable_candidate_without_promotion",
        "exclusions": "TFLink/database membership is a search lead; broad regulator evidence, orthologs, paralogs, reverse directions and complex-level findings were not transferred to this exact pair.",
        "notes": "No exact target-specific causal edge was established; target-cell presence, downstream activation and upstream relay are not inferred.",
    }

    if key == "gsk3b" and target == "ccnd1":
        out.update(status="target_protein_regulation_not_transcriptional", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC317244/", corr="https://research.bioinformatics.udel.edu/iptmnet/entry/P25322/", cell="mouse_NIH_3T3_fibroblast_model_not_SCI_target_cell", binding="GSK3B_directly_phosphorylated_Ccnd1_T286;_no_Ccnd1_locus_occupancy", downstream="active_GSK3B_increased_Ccnd1_T286_phosphorylation_and_reduced_nuclear_Ccnd1_stability;_mRNA_direction_not_established", disposition="retain_target_protein_regulation_in_noncanonical_evidence_category", exclusions="This is exact protein phosphorylation/stability regulation, not transcriptional regulation. It must not be used as evidence that GSK3B activates or represses the Ccnd1 gene.", notes="Exact mouse GSK3B-to-Ccnd1 post-translational evidence is routed outside canonical TF evidence.")
    elif key == "ccl5" and target == "agrp":
        out.update(status="functional_noncanonical_ligand_rna_candidate_not_tf", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC5127185/", corr="https://pubmed.ncbi.nlm.nih.gov/27898058/", cell="mouse_hypothalamus_ex_vivo_tissue_and_primary_neuron_models_not_SCI_target_cell", binding="CCL5_ligand_signaling_through_CCR5;_no_Agrp_locus_occupancy", downstream="Ccl5_or_Ccr5_loss_increased_hypothalamic_Agrp_mRNA;_ligand_antagonist_and_ex_vivo_assays_supported_CCR5-mediated_direction", disposition="retain_noncanonical_ligand_rna_candidate_pending_SCI_context", exclusions="The exact relationship is extracellular chemokine/CCR5 signaling with downstream Agrp RNA change, not a TF-to-promoter edge. No target-cell validation or direct Agrp occupancy was established.", notes="Exact mouse Ccl5-to-Agrp evidence is routed to ligand/receptor and downstream RNA-regulation evidence, not canonical TF evidence.")
    elif key == "gsk3b" and target == "axl":
        out.update(status="reverse_direction_near_match_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC9899255/", cell="human_leukemia_signaling_model_not_mouse_SCI_target_cell", binding="AXL_signaling_inhibited_or_inactivated_GSK3B;_not_GSK3B_occupancy_at_Axl", downstream="reverse_direction_only", disposition="retain_reverse_direction_evidence_separately", exclusions="The evidence supports AXL upstream of GSK3B, in a different species/context; it does not establish GSK3B regulation of Axl.", notes="Reverse-direction evidence was not transferred to the queued edge.")
    elif key == "hbz" and target == "cadm1":
        out.update(status="viral_paralog_near_match_not_promotable", primary="https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1005560", corr="https://pubmed.ncbi.nlm.nih.gov/15592508/", cell="human_CEM_T_cell_HTLV1_viral_HBZ_model_not_endogenous_HBAZ_SCI_target_cell", binding="viral_HTLV1_HBZ_protein_context_without_HBAZ_CADM1_locus_occupancy", downstream="viral_HBZ_reduced_stimulated_CADM1_expression", disposition="retain_viral_HBZ_near_match_separately", exclusions="Viral HTLV-1 HBZ is not the endogenous HBAZ/HBZ gene in the queued human TFLink row; no direct CADM1-locus mechanism was shown.", notes="Viral-HBZ evidence was explicitly excluded from endogenous-HBAZ promotion.")
    elif key == "iglv5-37" and target in {"agrn", "bcl2", "c1ql4", "clec11a"}:
        out.update(status="fusion_or_other_context_near_match_not_promotable", primary="https://link.springer.com/article/10.1186/s12885-025-13641-y", corr="https://pmc.ncbi.nlm.nih.gov/articles/PMC3756901/", cell="human_cancer_fusion_or_immunoglobulin_context_not_IGLV5_37_target_cell", binding="apparent_target_set_not_validated_as_IGLV5_37_locus_occupancy", downstream="no_IGLV5_37-specific_target_direction_found", disposition="retain_contextual_near_match_separately", exclusions="Immunoglobulin-variable-region identity and fusion-associated target-set evidence are not interchangeable with a sequence-specific IGLV5-37 regulator mechanism.", notes="The apparent target-set support was preserved as an identity/context exclusion, not promoted.")
    elif key == "u2af2" and target == "apoa1":
        out.update(status="target_protein_complex_association_not_transcriptional", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC4671683/", cell="human_spliceosomal_interactome_model_not_SCI_target_cell", binding="U2AF2_complex_or_interactome_association_without_APOA1_locus_or_RNA_direction", downstream="no_APOA1_transcriptional_direction_established", disposition="retain_target_complex_evidence_separately", exclusions="Complex/interactome association is not evidence that U2AF2 regulates APOA1 transcription or RNA abundance.", notes="The APOA1 association was kept outside TF evidence.")
    elif key == "pcna" and target == "ctnnb1":
        out.update(status="reverse_direction_near_match_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC6374483/", cell="human_or_mouse_beta_catenin_PCNA_context_not_mouse_SCI_target_cell", binding="beta_catenin_or_cell_cycle_context_not_PCNA_occupancy_at_Ctnnb1", downstream="reverse_or_complex_level_association_only", disposition="retain_reverse_direction_evidence_separately", exclusions="The reported association does not establish PCNA regulation of the Ctnnb1 locus or target RNA.", notes="Reverse/complex-level evidence was not transferred.")
    elif key == "zscan5dp":
        out.update(status="paralog_or_pseudogene_near_match_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC5340127/", cell="human_ZSCAN5D_family_model_not_ZSCAN5DP_SCI_target_cell", binding="ZSCAN5D_family_evidence_at_nonqueued_PolIII_or_ETC_loci_not_ZSCAN5DP", downstream="no_target_specific_direction_found", disposition="retain_paralog_identity_near_match_separately", exclusions="ZSCAN5D-family evidence cannot be assigned to ZSCAN5DP, which is annotated as a pseudogene/undercharacterized locus, and does not validate the queued targets.", notes="Paralog/family evidence was not transferred.")
    elif key == "ddx21" and target == "adipor2":
        out.update(status="perturbation_only_not_promotable", primary="https://graveleylabweb.cam.uchc.edu/encore/gene/index.php?rbp_name=DDX21", cell="human_HepG2_ENCORE_shRNA_model_not_SCI_target_cell", binding="ENCORE_Bound_by_RBP_field_blank_for_ADIPOR2", downstream="ADIPOR2_decreased_after_DDX21_perturbation_log2FC_minus_0_5183", disposition="retain_perturbation_only_evidence_separately", exclusions="A target-expression change after DDX21 perturbation without direct RNA occupancy or locus mechanism is insufficient for a DDX21-to-ADIPOR2 regulatory edge.", notes="Perturbation-only evidence was retained without promotion.")
    elif key == "fxr1" and target == "amh":
        out.update(status="perturbation_only_not_promotable", primary="https://graveleylabweb.cam.uchc.edu/ENCORE_TEST/gene/?rbp_name=AMH", cell="human_K562_ENCORE_knockdown_model_not_SCI_target_cell", binding="ENCORE_FXR1-associated_perturbation_without_direct_AMH_RNA_occupancy", downstream="AMH_increased_after_FXR1_perturbation_log2FC_plus_0_7830", disposition="retain_perturbation_only_evidence_separately", exclusions="The ENCORE perturbation signal lacks direct FXR1-AMH RNA occupancy and does not establish a causal target mechanism.", notes="Perturbation-only evidence was retained without promotion.")
    elif key == "fxr1" and target == "ccnd1":
        out.update(status="expression_response_without_direct_mechanism_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC8675433/", cell="human_HeyA8_ovarian_cancer_model_not_SCI_target_cell", binding="FXR1_direct_RNA_mechanism_reported_for_cMYC_not_CCND1", downstream="FXR1_depletion_reduced_CCND1_expression_or_protein", disposition="retain_expression_response_separately", exclusions="The direct FXR1 RNA mechanism was shown for cMYC, not CCND1; the CCND1 expression response does not establish direct regulation.", notes="Target direction without direct mechanism was not promoted.")
    elif key == "ccl5" and target == "adam9":
        out.update(status="reverse_direction_near_match_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC6298633/", cell="mouse_cigarette_smoke_Adam9_knockout_lung_model_not_hypothalamic_SCI_target_cell", binding="Adam9_deficiency_changed_Ccl5;_not_CCL5_occupancy_or_regulation_of_Adam9", downstream="reverse_direction_only", disposition="retain_reverse_direction_evidence_separately", exclusions="The study supports Adam9 upstream of Ccl5, not Ccl5 regulation of Adam9.", notes="Reverse-direction evidence was not transferred.")
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
        pairs.append({
            "review_id": f"public_tf_evidence_batch029_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"],
            "regulator_key": row["regulator_key"], "regulator_symbol": info["symbol"],
            "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"],
            "target_symbol": row["target_symbol"], "target_graph_modules": row["target_graph_modules"],
            "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": info["status"],
            "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence",
            "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"],
            "downstream_expression_or_perturbation_status": info["downstream"],
            "downstream_activation_status": "not_established_for_SCI_target_cell",
            "upstream_relay_status": "not_tested_for_exact_pair",
            "disposition": info["disposition"], "primary_citation": info["primary"],
            "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"],
            "review_notes": info["notes"] + " " + info["observation"],
            "exportable": "false", "canonical_write_performed": "false",
        })
        key = row["regulator_key"]
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch029_regulator_{key}",
                "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
                "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"],
                "cell_or_model": info["model"], "assay_or_perturbation": info["assay"],
                "observation": info["observation"],
                "effect_direction": "queued-pair direction not established except explicitly recorded limited associations",
                "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"],
                "route_or_module_relevance": info["relevance"],
                "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation or upstream relay. Profile, chromatin, machinery, protein, RNA, ligand and near-match evidence is retained separately from canonical promoter-TF evidence.",
            })
            seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch029_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch029_regulator_register.tsv"
    summary_path = args.output_dir / "batch_029_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH029.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(x["regulator_key"], x["target_symbol"], x["species_scope"], x["source_record_id"]) for x in pairs}
    noncanonical = sum(v for k, v in status_counts.items() if k.startswith("functional_noncanonical_"))
    near_match = sum(v for k, v in status_counts.items() if k not in {
        "binding_profile_only_not_promotable",
        "database_membership_only_not_promotable",
        "functional_noncanonical_ligand_rna_candidate_not_tf",
    })
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_029",
        "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs),
        "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence),
        "strict_tf_promotion_candidate_rows": 0, "noncanonical_exact_candidate_rows": noncanonical,
        "partial_or_near_match_rows": near_match, "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False,
        "provenance_preserved": True,
        "limitations": [
            "TFLink/profile resources are search leads, not causal regulation.",
            "Exact-pair negatives are bounded-search results, not global absence.",
            "GSK3B-to-Ccnd1 is exact protein regulation and Ccl5-to-Agrp is exact ligand/RNA regulation; neither is a canonical promoter-TF edge.",
            "MSL2, NUCKS1, WRNIP1, GREB1, SUMO1 and ZC3H11A profile rows remain nonpromotable without exact target-cell and mechanism evidence.",
            "No canonical or Module 22B write was performed.",
        ],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join([
        "# Evidence review: public TF batch 029", "",
        f"Reviewed {len(pairs)} exact regulator-target-species pairs across 25 TFLink source-set ranks.", "",
        f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.",
        f"- **{noncanonical}** exact noncanonical candidate row(s) were staged: Ccl5-to-Agrp is ligand/RNA regulation; GSK3B-to-Ccnd1 is protein regulation and is kept separate.",
        f"- **{status_counts.get('binding_profile_only_not_promotable', 0)}** profile-only rows were retained without promotion.",
        f"- **{near_match}** near-match, perturbation-only, protein-complex, expression-only or identity-limited rows were retained separately.",
        "- **0** strict TF, exportable, canonical or Module 22B writes were performed.", "",
        "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping and local source snapshot. Ligand/RNA, protein, chromatin, machinery, profile and near-match evidence is recorded separately from exact canonical TF evidence.", "",
    ]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
