#!/usr/bin/env python3
"""Stage conservative, provenance-preserving evidence findings for a public-TF batch."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/"
    "candidate_triage_v1/evidence_batches/batch_032/"
    "public_tf_evidence_collection_batch_032.tsv"
)

PAIR_FIELDS = [
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol", "species_scope",
    "source_registry", "source_record_id", "raw_tf_symbol", "target_symbol", "target_graph_modules",
    "candidate_membership_status", "exact_pair_search_url", "exact_pair_status",
    "regulator_general_evidence_status", "target_cell_presence_status", "binding_or_association_status",
    "downstream_expression_or_perturbation_status", "downstream_activation_status", "upstream_relay_status",
    "disposition", "primary_citation", "corroborating_citation", "near_match_exclusions", "review_notes",
    "exportable", "canonical_write_performed",
]
REGISTER_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer", "support_kind",
    "cell_or_model", "assay_or_perturbation", "observation", "effect_direction", "primary_citation",
    "corroborating_citation", "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]


def gene_url(symbol: str, species: str) -> str:
    organism = "Homo sapiens" if species == "human" else "Mus musculus"
    return "https://www.ncbi.nlm.nih.gov/gene/?term=" + quote_plus(
        f"{symbol}[Gene Name] AND {organism}[Organism]"
    )


def uniprot_url(symbol: str) -> str:
    return "https://www.uniprot.org/uniprotkb?query=" + quote_plus(f"gene:{symbol}")


ROLE_INFO = {
    "arhgap35": ("ARHGAP35", "human", "Rho-family GTPase-activating protein and cytoskeletal/transcriptional regulator; not a sequence-specific TF", "RhoGAP, actin/cytoskeletal and transcriptional-complex annotations", "noncanonical RhoGAP/transcriptional-regulator capacity only"),
    "ptpn18": ("PTPN18", "human", "protein tyrosine phosphatase; not a sequence-specific TF", "phosphatase, receptor and signaling annotations", "noncanonical phosphatase/signaling capacity only"),
    "tox3": ("TOX3/Tox3", "mouse", "HMG-box family transcriptional regulator; exact queued targets not validated", "DNA-binding/regulatory and neuronal/immune expression annotations", "regulator-level evidence only; target pair pending"),
    "myo1c": ("MYO1C", "mouse", "class I myosin motor and membrane/cytoskeletal protein; not a TF", "actin motor, membrane trafficking and protein-interaction assays", "noncanonical motor/cytoskeletal capacity only"),
    "srpk2": ("SRPK2", "human", "serine/arginine-rich protein kinase controlling RNA splicing; not a TF", "kinase, SR-protein phosphorylation and splicing assays", "noncanonical RNA-processing capacity; ACSS2 edge routed separately"),
    "skp2": ("SKP2", "human", "F-box substrate-recognition component of an SCF ubiquitin ligase; not a TF", "ubiquitin ligase, cell-cycle and substrate-stability assays", "noncanonical protein/cell-cycle capacity only"),
    "phc1": ("PHC1/Phc1", "mouse", "Polycomb-group chromatin-complex component; not a sequence-specific TF", "PRC1, chromatin architecture and DNA-damage annotations", "noncanonical chromatin-complex capacity only"),
    "flii": ("FLII/Flii", "mouse", "actin-remodeling protein and transcriptional cofactor; not a standalone TF", "actin, cofactor-interaction and inflammatory-expression assays", "noncanonical cytoskeletal/cofactor capacity only"),
    "npat": ("NPAT", "human", "cell-cycle and histone-gene transcriptional regulator/cofactor; strict TF role unresolved", "histone-locus, cell-cycle and chromatin-complex assays", "noncanonical nuclear/chromatin capacity only"),
    "wdhd1": ("WDHD1", "human", "DNA-replication and genome-maintenance protein; not a TF", "replication, centrosome and genome-maintenance annotations", "noncanonical genome-maintenance capacity only"),
    "snrnp70": ("SNRNP70", "human", "U1 spliceosomal RNA-binding protein; not a TF", "U1 snRNP, RNA binding and splicing assays", "noncanonical RNA-processing capacity only"),
    "ndufs2": ("NDUFS2/Ndufs2", "mouse", "mitochondrial respiratory-complex I subunit; not a TF", "mitochondrial complex-I and bioenergetic annotations", "noncanonical mitochondrial capacity only"),
    "dicer1": ("DICER1", "human", "RNase III microRNA-processing enzyme; not a DNA-binding TF", "small-RNA processing, RNA binding and perturbation assays", "noncanonical RNA-regulatory capacity only"),
    "brf1": ("BRF1", "human", "TFIIIB/RNA-polymerase-III initiation factor; not a sequence-specific TF", "Pol-III initiation and general transcription machinery assays", "noncanonical transcriptional-machinery capacity only"),
    "efna2": ("EFNA2/Efna2", "mouse", "ephrin-A ligand and membrane-associated signaling protein; not a TF", "cell-surface ligand, Eph receptor and axon-guidance assays", "noncanonical ligand/signaling capacity only"),
    "btn3a2": ("BTN3A2", "human", "butyrophilin-family membrane immunoregulatory protein; not a TF", "immunoglobulin-superfamily and cell-surface receptor annotations", "noncanonical membrane/immunoregulatory capacity only"),
    "btn3a3": ("BTN3A3", "human", "butyrophilin-family membrane immunoregulatory protein; not a TF", "immunoglobulin-superfamily, antiviral and cell-surface annotations", "noncanonical membrane/immunoregulatory capacity only"),
    "zrsr1": ("ZRSR1/Zrsr1", "mouse", "U12-type spliceosome RNA-binding factor; not a TF", "minor spliceosome, RNA binding and splicing annotations", "noncanonical RNA-processing capacity only"),
    "litaf": ("LITAF/Litaf", "mouse", "inflammatory transcriptional regulator, but queued target edges are unvalidated", "TNF/LPS response, promoter and inflammatory-expression assays", "regulator-level inflammatory capacity only"),
    "mrtfa": ("MRTFA/MKL1/Mrtfa", "human_and_mouse", "signal-regulated SRF coactivator rather than a standalone sequence-specific TF", "SRF coactivator, promoter/reporter, ChIP and perturbation assays", "noncanonical transcriptional-coactivator evidence; no SCI-cell materialization"),
    "tasor": ("TASOR", "human", "HUSH-complex chromatin-silencing component; not a sequence-specific TF", "HUSH complex, heterochromatin and transcriptional-silencing annotations", "noncanonical chromatin-silencing capacity only"),
    "tox4": ("TOX4/Tox4", "human", "nuclear regulatory/PP1-complex protein; exact TF role not established", "nuclear-complex and transcriptional-regulatory annotations", "noncanonical nuclear-complex capacity only"),
    "champ1": ("CHAMP1", "human", "kinetochore/chromosome-segregation protein; not a TF", "centromere, kinetochore and mitotic assays", "noncanonical chromosome-maintenance capacity only"),
    "sipa1": ("SIPA1", "human", "Rap GTPase-activating protein and signaling/adhesion regulator; not a TF", "Rap signaling, adhesion, migration and EMT assays", "noncanonical signaling/adhesion capacity only"),
    "ahcy": ("AHCY/Ahcy", "mouse", "adenosylhomocysteinase metabolic enzyme; not a TF", "methionine-cycle and metabolic enzyme annotations", "noncanonical metabolic capacity only"),
    "trip13": ("TRIP13", "human", "AAA+ ATPase involved in meiotic checkpoint and chromosome maintenance; not a TF", "chromosome, spindle-checkpoint and DNA-repair assays", "noncanonical chromosome-maintenance capacity only"),
    "znf622": ("ZNF622", "human", "nucleolar/ribosome-associated regulatory protein; exact TF role unestablished", "ribosome biogenesis, translation and protein-interaction annotations", "noncanonical nuclear/ribosome capacity only"),
    "rpa2": ("RPA2/Rpa2", "mouse", "replication-protein-A subunit; not a TF", "single-stranded-DNA binding, replication and repair assays", "noncanonical DNA-replication capacity only"),
    "sqstm1": ("SQSTM1/p62", "human", "autophagy receptor and signaling scaffold; not a TF", "autophagy, stress signaling and protein-interaction assays", "noncanonical autophagy/signaling capacity only"),
    "mcrs1": ("MCRS1", "human", "nuclear chromatin-complex and ribosome-biogenesis factor; not a TF", "INO80/NuA4, chromatin and nucleolar-complex assays", "noncanonical chromatin/nuclear-machinery capacity only"),
    "nufip1": ("NUFIP1", "human", "RNA-processing and ribosome-biogenesis factor; not a TF", "RNA binding, ribosome biogenesis and stress-response assays", "noncanonical RNA/nuclear capacity only"),
    "pgbd5": ("PGBD5", "human", "piggyBac transposase-domain protein; not a TF", "DNA rearrangement and genome-maintenance assays", "noncanonical genome-rearrangement capacity only"),
    "gatd3b": ("GATD3B", "human", "mitochondrial glutamine amidase-associated protein; not a TF", "mitochondrial and metabolic annotations", "noncanonical mitochondrial capacity only"),
    "rpa1": ("RPA1", "human", "replication-protein-A large subunit; not a TF", "single-stranded-DNA binding, replication and repair assays", "noncanonical DNA-replication capacity only"),
    "sigmar1": ("SIGMAR1", "human", "ER membrane chaperone/signaling receptor; not a TF", "ER stress, membrane signaling and protein-interaction assays", "noncanonical receptor/chaperone capacity only"),
    "klrg1": ("KLRG1/Klrg1", "mouse", "inhibitory immune-cell surface receptor; not a TF", "NK/T-cell receptor and immune-signaling assays", "noncanonical immune-receptor capacity only"),
    "adcyap1": ("ADCYAP1", "human", "secreted neuropeptide ligand; not a TF", "neuropeptide secretion and GPCR-signaling assays", "noncanonical ligand/signaling capacity only"),
    "cop1": ("COP1/RFWD2", "human", "RING E3 ubiquitin ligase; not a TF", "ubiquitin-dependent c-Jun and transcriptional-target regulation", "noncanonical protein-regulatory capacity; MMP1 expression routed separately"),
    "cbll2": ("CBLL2", "human", "RING-type ubiquitin ligase-family protein; exact TF role unestablished", "ubiquitin, nuclear-complex and protein-interaction annotations", "noncanonical protein-regulatory capacity only"),
    "cd8a": ("CD8A", "human", "T-cell coreceptor membrane protein; not a TF", "T-cell receptor complex and immune-cell assays", "noncanonical immune-receptor capacity only"),
    "gc": ("GC/VDBP/Gc", "human_and_mouse", "secreted vitamin-D-binding carrier protein; not a TF", "vitamin-D transport and extracellular protein annotations", "noncanonical extracellular-carrier capacity only"),
    "polr1h": ("POLR1H", "human", "RNA-polymerase-I subunit; general transcription machinery, not a sequence-specific TF", "Pol-I complex and rRNA-transcription assays", "noncanonical transcriptional-machinery capacity only"),
    "tirap": ("TIRAP", "human", "Toll-like-receptor adaptor protein; not a TF", "TLR/MyD88 signaling and inflammatory-expression assays", "noncanonical receptor-relay capacity only"),
    "dpep1": ("DPEP1/Dpep1", "mouse", "membrane dipeptidase; not a TF", "membrane enzyme and epithelial trafficking annotations", "noncanonical membrane-enzyme capacity only"),
    "krt3": ("KRT3", "human", "epithelial keratin structural protein; not a TF", "intermediate-filament and epithelial differentiation assays", "noncanonical structural capacity only"),
    "mau2": ("MAU2/Mau2", "mouse", "cohesin-loader component; not a TF", "cohesin loading, chromosome and genome-organization assays", "noncanonical chromatin-architecture capacity only"),
    "naa10": ("NAA10/Naa10", "mouse", "N-terminal acetyltransferase; not a TF", "protein N-terminal acetylation and proteostasis assays", "noncanonical protein/PTM capacity only"),
    "hjurp": ("HJURP", "human", "centromeric histone chaperone; not a TF", "CENP-A deposition, centromere and chromosome assays", "noncanonical chromosome-maintenance capacity only"),
}

CATEGORY_LABELS = {
    "catalog_concordant_tf_candidate": "catalog-concordant TF candidate",
    "dual_role_tf_chromatin_candidate": "dual-role TF/chromatin candidate",
    "noncanonical_transcriptional_regulator": "noncanonical transcriptional regulator",
    "provisional_nuclear_transcriptional_regulator": "provisional nuclear transcriptional regulator",
    "regulon_lead_unclassified": "regulon lead with role unclassified",
    "dna_repair_or_genome_maintenance": "DNA-repair/genome-maintenance protein, not assumed TF",
    "nuclear_structure_or_transport": "nuclear-structure/transport protein, not assumed TF",
    "nuclear_machinery_or_structural_not_regulatory": "nuclear machinery/structural protein, not assumed TF",
    "rna_binding_or_post_transcriptional": "RNA-binding/post-transcriptional regulator, not a DNA TF",
    "signaling_metabolic_membrane_or_cell_cycle": "signaling/metabolic/membrane/cell-cycle protein, not assumed TF",
    "alias_or_ingestion_artifact_review": "alias/ingestion-artifact review hold",
}


def role_info_for(row: dict[str, str]) -> tuple[str, str, str, str, str]:
    """Return only evidence supported by the queue metadata for new regulators.

    The queue is intentionally the authority for literal symbols.  Unknown
    keys therefore receive a conservative role label from its triage category;
    no biological identity or TF activity is inferred from the symbol.
    """
    key = row["regulator_key"]
    if key in ROLE_INFO:
        return ROLE_INFO[key]
    category = row.get("primary_role_category", "regulon_lead_unclassified")
    subcategory = row.get("role_subcategory", "") or "not provided"
    display = (row.get("display_symbols") or row.get("raw_tf_symbol") or key).replace(";", "/")
    species = row.get("species_scope", "")
    label = CATEGORY_LABELS.get(category, category)
    role = f"{label}; source subcategory {subcategory}; exact queued targets require review"
    assay = f"Role category from public_tf_role_triage.tsv ({category}); no target-specific assay inferred"
    relevance = f"staged outside canonical TF materialization pending exact pair evidence ({category})"
    return display, species, role, assay, relevance

# Exact target-specific findings are retained only where the regulator, target,
# species, direction and assay class are supported. They are deliberately
# routed outside strict canonical TF evidence when the regulator is a cofactor,
# kinase or chromatin/RNA regulator.
SPECIAL_EDGES = {
    ("mrtfa", "col1a1", "human"): {
        "status": "functional_noncanonical_coactivator_candidate_not_tf",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/29807221/",
        "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6692381/",
        "cell": "human_MCF7_breast-cancer_cells_not_SCI_target_cell",
        "binding": "MRTF-A_physically_interacted_with_COL1A1_promoter;_SRF-coactivator_context;_not_standalone_sequence-specific_MRTFA_DNA_binding",
        "downstream": "MRTF-A_depletion_abrogated_TGF-beta_or_Wnt_induction_of_COL1A1_in_MCF7;_independent_human_MSC_study_did_not_replicate_COL1A1_dependence",
        "disposition": "retain_noncanonical_coactivator_candidate_pending_SCI_context",
        "exclusions": "Exact human COL1A1 transcriptional evidence is context-dependent and does not establish a standalone TF edge or SCI target-cell activity.",
        "notes": "Primary breast-cancer study supports promoter association and perturbation; the independent MSC study is retained as a conflicting context qualifier, not silently treated as corroboration.",
    },
    ("mrtfa", "myl9", "human"): {
        "status": "functional_noncanonical_coactivator_candidate_not_tf",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/24084383/",
        "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5880600/",
        "cell": "human_MCF7_breast-cancer_cells_not_SCI_target_cell",
        "binding": "MRTF-A/SRF_CArG-promoter_context_and_MYL9_promoter-reporter_assays;_not_standalone_MRTFA_DNA_binding",
        "downstream": "MRTF-A_overexpression_increased_MYL9_expression_and_migration;_RNAi_or_activity_inhibition_reduced_MYL9_response",
        "disposition": "retain_noncanonical_coactivator_candidate_pending_SCI_context",
        "exclusions": "Human MYL9 evidence is a coactivator/SRF-context relationship in breast-cancer cells, not a standalone sequence-specific TF promotion or SCI-cell result.",
        "notes": "Two independent human breast-cancer studies support the target-specific coactivator relationship; both remain staging-only.",
    },
    ("mrtfa", "mmp9", "human"): {
        "status": "functional_noncanonical_coactivator_candidate_not_tf",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8024553/",
        "corr": "https://pubmed.ncbi.nlm.nih.gov/33722605/",
        "cell": "human_BGC823_and_related_gastric-cancer_cells_not_SCI_target_cell",
        "binding": "EGF-induced_MRTF-A_enrichment_at_MMP9_promoter_by_ChIP;_coactivator/SRF_context",
        "downstream": "MRTF-A_depletion_reduced_MMP9_RNA_and_protein;_MICAL2/EGF-induced_response_was_suppressed",
        "disposition": "retain_noncanonical_coactivator_candidate_pending_SCI_context",
        "exclusions": "The study supports promoter occupancy and perturbation in gastric-cancer cells, but MRTF-A is a coactivator and the model is not an SCI target cell.",
        "notes": "Exact human MRTFA-to-MMP9 evidence is routed to transcriptional-coactivator and downstream-expression staging.",
    },
    ("mrtfa", "id3", "mouse"): {
        "status": "functional_noncanonical_coactivator_candidate_not_tf",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3258938/",
        "corr": "https://www.ncbi.nlm.nih.gov/gene/15902",
        "cell": "mouse_C2C12_myoblast_myogenic-differentiation_model_not_SCI_target_cell",
        "binding": "endogenous_MRTF-A_associated_with_Id3_promoter_by_ChIP;_MRTF-A/Smad-dependent_promoter_context;_not_standalone_MRTFA_DNA_binding",
        "downstream": "constitutively_active_MRTF-A_increased_Id3_promoter_activity;_RhoA-ROCK/MRTF-A/Smad_context_changed_Id3_transcription",
        "disposition": "retain_noncanonical_coactivator_candidate_pending_SCI_context",
        "exclusions": "Mouse Id3 evidence is a cooperative MRTF-A/Smad transcriptional mechanism in C2C12 myoblasts, not strict standalone TF evidence or SCI-cell validation.",
        "notes": "Exact mouse Mrtfa-to-Id3 transcriptional evidence is routed to coactivator/signaling-relay staging.",
    },
    ("srpk2", "acss2", "human"): {
        "status": "functional_noncanonical_rna_regulation_candidate_not_tf",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/29153836/",
        "corr": "https://www.nature.com/articles/s41416-019-0650-z",
        "cell": "human_and_mouse_mTORC1-S6K1-SRPK2_lipogenesis_models_not_SCI_target_cell",
        "binding": "no_ACSS2_locus_occupancy;_SRPK2_controls_SR-protein-dependent_splicing",
        "downstream": "SRPK2_inhibition_caused_ACSS2_intron_retention_and_nonsense-mediated_mRNA_decay_with_reduced_lipogenic_expression",
        "disposition": "retain_noncanonical_RNA-splicing_candidate_pending_SCI_context",
        "exclusions": "This is an indirect post-transcriptional RNA-splicing/stability relationship, not SRPK2 DNA binding or promoter-TF evidence.",
        "notes": "Exact SRPK2-to-ACSS2 RNA-regulatory evidence is routed to RNA-processing and downstream-expression evidence.",
    },
    ("mrtfa", "tagln", "mouse"): {
        "status": "binding_and_cofactor_dependence_near_match_not_promotable",
        "primary": "https://www.nature.com/articles/s41598-022-06135-5",
        "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3801009/",
        "cell": "mouse_NIH3T3_and_dermal-fibroblast_MRTF-A/SRF_models_not_SCI_target_cell",
        "binding": "MRTF-A/SRF_ChIP-seq_and_classical_Tagln_target-program_context",
        "downstream": "Tagln_expression_changed_after_LAP2alpha_cofactor_depletion;_Mrtfa_was_not_isolated_as_the_perturbed_variable_for_this_edge",
        "disposition": "retain_binding_and_cofactor_dependence_near_match_separately",
        "exclusions": "The evidence establishes MRTF-A/SRF target context and cofactor dependence, but not isolated Mrtfa perturbation for this exact Tagln pair.",
        "notes": "Mouse Mrtfa-to-Tagln remains a binding/cofactor near-match without export or materialization.",
    },
    ("mrtfa", "edn1", "mouse"): {
        "status": "reverse_direction_near_match_not_promotable",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4176337/",
        "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2781563/",
        "cell": "mouse_and_human_vascular-smooth-muscle_or_collecting-duct_models_not_SCI_target_cell",
        "binding": "ET-1/Edn1_is_an_upstream_signal_that_changes_MRTF-A_activity;_no_Mrtfa-to-Edn1_locus_binding_established",
        "downstream": "ET-1_induced_MRTF-A_nuclear_enrichment_and_MRTF-A-dependent_inflammatory_transcription;_direction_is_not_Mrtfa-to-Edn1",
        "disposition": "retain_reverse_direction_near_match_separately",
        "exclusions": "The located evidence is ET-1/Edn1-to-MRTF-A signaling or MR/GR-to-Edn1 regulation, not Mrtfa regulation of Edn1.",
        "notes": "Reverse-direction and unrelated Edn1 promoter evidence is retained as an explicit exclusion.",
    },
    ("mrtfa", "scai", "human"): {
        "status": "reverse_direction_near_match_not_promotable",
        "primary": "https://ajp.amjpathol.org/article/S0002-9440%2812%2900803-6/fulltext",
        "corr": "",
        "cell": "human_and_mouse_renal-fibrosis_or_promoter-reporter_models_not_SCI_target_cell",
        "binding": "SCAI_interacted_with_or_inhibited_MRTF-A/SRF-dependent_promoter_activation;_not_MRTFA_regulation_of_SCAI",
        "downstream": "SCAI_overexpression_reduced_MRTF-A-induced_SMA_promoter_activity",
        "disposition": "retain_reverse_direction_near_match_separately",
        "exclusions": "The evidence supports SCAI inhibition of MRTF-A-dependent transcription, not MRTFA regulation of SCAI expression.",
        "notes": "MRTFA-to-SCAI is retained as a directionality/interaction near-match outside exact target regulation.",
    },
    ("cop1", "mmp1", "human"): {
        "status": "functional_noncanonical_downstream_expression_candidate_not_tf",
        "primary": "https://www.spandidos-publications.com/10.3892/or.2013.2664/download",
        "corr": "https://www.jci.org/articles/view/45784",
        "cell": "human_MKN45_and_NUGC4_gastric-cancer_cells_not_SCI_target_cell",
        "binding": "COP1_E3-ligase_and_c-Jun/AP-1_target-context;_no_COP1_DNA-locus_binding_or_direct_MMP1_transcription_factor_claim",
        "downstream": "COP1_siRNA_increased_MMP1_mRNA_in_gastric-cancer_cells;_substrate/pathway_link_to_MMP1_expression_not_fully_resolved",
        "disposition": "retain_noncanonical_ubiquitin_and_downstream-expression_candidate_pending_SCI_context",
        "exclusions": "This is target-expression response after COP1 perturbation in cancer cells, not canonical COP1 TF evidence; COP1 regulates protein stability and the direct MMP1 mechanism remains unresolved.",
        "notes": "Exact human COP1-to-MMP1 expression evidence is routed to noncanonical ubiquitin/protein regulation and downstream-expression staging.",
    },
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
    return "https://pubmed.ncbi.nlm.nih.gov/?term=" + quote_plus(
        f'"{regulator}" AND "{target}" AND {species}'
    )


def classify(row: dict[str, str]) -> dict[str, str]:
    key = row["regulator_key"]
    display, role_species, role, assay, relevance = role_info_for(row)
    target = row["target_symbol"].lower()
    special = SPECIAL_EDGES.get((key, target, row["species_scope"]))
    if special:
        return {"symbol": display, "general_primary": gene_url(row["raw_tf_symbol"], row["species_scope"]),
                "general_corr": uniprot_url(row["raw_tf_symbol"]), "kind": "primary_literature_target_specific",
                "model": special["cell"], "assay": special["binding"] + "; " + special["downstream"],
                "observation": special["notes"], "relevance": relevance, **special}
    return {
        "symbol": display,
        "general_primary": gene_url(row["raw_tf_symbol"], row["species_scope"]),
        "general_corr": uniprot_url(row["raw_tf_symbol"]),
        "kind": "authoritative_identity_and_role_annotation",
        "model": f"{role_species}_{role}", "assay": assay,
        "observation": f"{role}; no exact queued regulator-target evidence was validated.",
        "relevance": relevance,
        "status": "database_membership_only_not_promotable",
        "primary": "https://tflink.net/download/#interaction-gmt", "corr": "",
        "cell": "not_assessed_for_exact_pair",
        "binding": "TFLink_membership_only_no_target-locus_or_pairwise_assay_validated",
        "downstream": "not_assessed_for_exact_pair",
        "disposition": "retain_provenance_traceable_candidate_without_promotion",
        "exclusions": "TFLink membership and regulator-level annotation are search leads; co-expression, pathway membership, orthologs, paralogs, general machinery and reverse-direction findings were not transferred to this exact pair.",
        "notes": "No exact target-specific causal edge was established; target-cell presence, downstream activation and upstream relay are not inferred.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_BATCH.parent)
    parser.add_argument("--batch-number", type=int, default=32)
    args = parser.parse_args()
    rows = read_tsv(args.batch)
    if not rows:
        raise SystemExit("expected at least one literal queue row")

    batch_token = f"batch{args.batch_number:03d}"
    batch_id = rows[0]["batch_id"] if rows else f"public_tf_evidence_batch_{args.batch_number:03d}"
    pairs: list[dict[str, str]] = []
    register: list[dict[str, str]] = []
    seen_regulators: set[str] = set()
    status_counts: Counter[str] = Counter()
    for row in rows:
        info = classify(row)
        status_counts[info["status"]] += 1
        pairs.append({
            "review_id": f"public_tf_evidence_{batch_token}_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"],
            "regulator_key": row["regulator_key"], "regulator_symbol": info["symbol"],
            "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"],
            "target_symbol": row["target_symbol"], "target_graph_modules": row["target_graph_modules"],
            "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": info["status"],
            "regulator_general_evidence_status": "supported_regulator_role_only_not_pair_evidence",
            "target_cell_presence_status": info["cell"],
            "binding_or_association_status": info["binding"],
            "downstream_expression_or_perturbation_status": info["downstream"],
            "downstream_activation_status": "not_established_for_SCI_target_cell",
            "upstream_relay_status": "not_tested_for_exact_pair",
            "disposition": info["disposition"], "primary_citation": info["primary"],
            "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"],
            "review_notes": info["notes"] + " " + info["observation"],
            "exportable": "false", "canonical_write_performed": "false",
        })
        key = row["regulator_key"]
        if key not in seen_regulators:
            species = "human_and_mouse" if key == "mrtfa" else row["species_scope"]
            display, _, role, assay, relevance = role_info_for(row)
            register.append({
                "evidence_id": f"public_tf_evidence_{batch_token}_regulator_{key}",
                "regulator_key": key, "regulator_symbol": display, "species_scope": species,
                "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": "authoritative_identity_and_role_annotation",
                "cell_or_model": role, "assay_or_perturbation": assay,
                "observation": f"{role}; exact queued pair evidence was reviewed separately.",
                "effect_direction": "queued-pair direction not established except explicitly scoped target-specific findings",
                "primary_citation": gene_url(row["raw_tf_symbol"], row["species_scope"]),
                "corroborating_citation": uniprot_url(row["raw_tf_symbol"]),
                "route_or_module_relevance": relevance,
                "target_pair_scope": "Regulator-level identity/role does not establish any queued target pair, target-cell presence, effect direction, SCI activation or upstream relay.",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "TFLink membership is a search lead only. Noncanonical protein, membrane, ligand, chromatin, RNA, machinery and cofactor findings are routed outside strict canonical TF evidence.",
            })
            seen_regulators.add(key)

    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = output_dir / f"public_tf_evidence_review_{batch_token}_pairs.tsv"
    register_path = output_dir / f"public_tf_evidence_review_{batch_token}_regulator_register.tsv"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, REGISTER_FIELDS, register)

    provenance_keys = [(r["regulator_key"], r["target_symbol"], r["species_scope"], r["source_record_id"]) for r in pairs]
    flags = [r[field].casefold() for r in pairs for field in ("exportable", "canonical_write_performed")]
    validation = {
        "status": "pass" if len(set(provenance_keys)) == len(provenance_keys) and all(v in {"true", "false"} for v in flags) and all(v == "false" for v in flags) else "fail",
        "checks": {
            "literal_queue_rows": len(rows), "review_pair_rows": len(pairs),
            "regulator_register_rows": len(register), "unique_provenance_keys": len(set(provenance_keys)),
            "duplicate_provenance_keys": len(provenance_keys) - len(set(provenance_keys)),
            "malformed_flags": sum(v not in {"true", "false"} for v in flags),
            "exportable_true_rows": sum(v == "true" for v in flags),
            "canonical_write_true_rows": sum(r["canonical_write_performed"] == "true" for r in pairs),
            "duplicate_review_ids": len(pairs) - len({r["review_id"] for r in pairs}),
        },
    }
    validation_path = output_dir / f"batch_{args.batch_number:03d}_validation.json"
    validation_path.write_text(json.dumps(validation, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if validation["status"] != "pass":
        raise SystemExit(json.dumps(validation, sort_keys=True))

    noncanonical = sum(v for k, v in status_counts.items() if k.startswith("functional_noncanonical_"))
    near = sum(v for k, v in status_counts.items() if "near_match" in k or "binding_and_cofactor" in k or "without_direct_binding" in k)
    summary = {
        "status": "staging_only", "batch_id": batch_id,
        "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs),
        "unique_regulators_reviewed": len(seen_regulators), "unique_provenance_aware_pairs": len(set(provenance_keys)),
        "exact_pair_status_counts": dict(sorted(status_counts.items())), "regulator_register_rows": len(register),
        "strict_tf_promotion_candidate_rows": 0, "noncanonical_exact_candidate_rows": noncanonical,
        "profile_only_rows": 0, "identity_review_hold_rows": 0,
        "database_only_rows": status_counts["database_membership_only_not_promotable"],
        "partial_or_near_match_rows": near, "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False,
        "provenance_preserved": True, "validation": str(validation_path.relative_to(ROOT)),
        "limitations": [
            "TFLink membership is a search lead, not causal regulation.",
            "MRTFA/Mrtfa is retained as a signal-regulated SRF coactivator, not promoted as a standalone sequence-specific TF.",
            "Exact functional findings are routed to their noncanonical coactivator, RNA-splicing, ubiquitin or downstream-expression categories and remain outside canonical and Module 22B materialization.",
            "Near-matches retain their directionality and interaction limitations; they are not transferred to exact regulator-target evidence.",
            "All models are outside the SCI target-cell context; exact-pair negatives are bounded-search results, not global absence.",
            "No canonical TF or Module 22B write was performed.",
        ],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT)), str(validation_path.relative_to(ROOT))],
    }
    summary_path = output_dir / f"batch_{args.batch_number:03d}_evidence_review_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path = output_dir / f"EVIDENCE_REVIEW_BATCH{args.batch_number:03d}.md"
    report_path.write_text("\n".join([
        f"# Evidence review: public TF batch {args.batch_number:03d}", "",
        f"Reviewed {len(pairs)} literal exact regulator-target-species pairs across 25 TFLink source-set ranks.", "",
        f"- **{noncanonical}** exact functional noncanonical candidates were staged where target-specific perturbation or expression evidence was traceable.",
        f"- **{near}** binding, cofactor or directionality near-matches were retained separately.",
        f"- **{status_counts['database_membership_only_not_promotable']}** rows remain TFLink/database-membership-only leads.",
        "- **0** strict TF promotions, exportable rows, canonical writes, or Module 22B writes were performed.", "",
        "All exact target-specific findings are routed outside strict canonical TF evidence when the regulator is a coactivator, kinase, ubiquitin ligase or other noncanonical regulator. All rows retain the literal raw regulator symbol, species, target, source record, raw snapshot hash and source locator from the queue.", "",
        f"Validation status: **{validation['status']}** (`{validation_path.relative_to(ROOT)}`).",
    ]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
