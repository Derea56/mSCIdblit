#!/usr/bin/env python3
"""Generate evidence-only route rows from explicit output language in the queue.

This is deliberately conservative. It reads only the stored primary-supported
summary and assay fields; it never infers intracellular intermediates, TFs, or
target genes. Records that contain only binding/structure language remain
unresolved for manual review.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


RULES: tuple[tuple[str, str], ...] = (
    (
        "reporter_readout",
        r"\b(?:luciferase|reporter(?: assay| activity| construct)|beta.?galactosidase)\b",
    ),
    (
        "gene_expression_or_transcription",
        r"\b(?:gene expression|transcription(?:al)?|transcript(?:ion)?|mRNA|qRT.?PCR|RT.?PCR|promoter|target gene|RNA-seq)\b",
    ),
    (
        "cleavage_or_processing_readout",
        r"\b(?:cleavage|cleaved|proteolysis|processing|deacylation|shedding)\b",
    ),
    (
        "phagocytosis_or_engulfment",
        r"\b(?:phagocytosis|phagocytic|engulfment|engulf)\b",
    ),
    (
        "secreted_protein_or_release",
        r"\b(?:secretion|secret(?:ed|ion)|release(?:d)?|extracellular release)\b",
    ),
    (
        "translocation_or_localization_readout",
        r"\b(?:translocation|localization|localized|internalization|internalized|trafficking|endocytosis|endocytic|nuclear import|nuclear export|surface expression)\b",
    ),
    (
        "phosphorylation_or_activation_readout",
        r"\b(?:phosphorylat(?:e|ed|ion)|autophosphorylat(?:e|ed|ion)|activation|activates|activated|signaling|signalling|kinase|NF.?k.?B|ERK(?:1/2)?|JNK(?:1/2)?|p38|STAT\d*|SMAD\d*|MYD88|PI3K|AKT|G.?protein|GTPase|GTP.?gamma.?S|Rho|ROS|reactive oxygen|autophagy|ubiquitin(?:ation)?|aggregation|channel opening|NMDAR|excitotoxicity|cross.?talk|HIV p24|activin.?antagonism)\b",
    ),
    (
        "cellular_functional_readout",
        r"\b(?:chemotaxis|chemotactic|migration|migrat(?:e|ion)|proliferat(?:e|ion)|mitogenic|growth|survival|apoptosis|apoptotic|differentiation|differenti(?:ate|ation)|adhesion|rolling|repulsion|repulsive|neurite|axon|growth.?cone|contraction|injury|inflammation|inflammatory|tolerance|cytotoxic|cytotoxicity|lysis|killing|homeostasis|plasticity|myelination|scaveng(?:e|ing)|uptake|cellular response|cell response|barrier|permeability|degranulation|osteoclast|osteoblast|osteogenic|alkaline phosphatase|ALP|morphogenesis|organogenesis|synap(?:se|tic|togenesis)|angiogenesis|vascular|wound|regeneration|branching|spreading|lamellipodia|costimulation|immune response|cytokine|antiviral|antiproliferative|antimicrobial|pathogen|infection|infectivity|viral entry|disease resistance|platelet aggregation|thrombosis|hemostasis|electrophysiolog|membrane current|cell death|death response|hemolysis|clotting|anticoagulant|thrombus|entry|clearance|degradation|recruitment|sorting|turnover|depletion|inhibition|inhibitory|suppression|suppresses|neutraliz|blockade|blocked|antagon|phenotype|phenotypic|functional|function|bioactivity|potency|response|readout|outcome|developmental activity|organizer activity|neural induction|dorsalization|ganglion assembly|osteoclastogenesis|hepcidin|FSH|transformation|immune suppression|T-cell response|NKT|induction|production|modulatory activity|externalization|transport|cofactor activity|decay activity|convertase|complement deposition|serum resistance|mechanosensitivity|mechanotransduction|cointernalization|transmigration|physiological response|BMP response|developmental assay|antigen-specific response|receptor-specific activity|enzymatic activity|protease activity|ligand-induced|agonist response|sensitivity|LTP|hemisynapse clustering|surface/stability|stability and insertion|motor recovery|perineuronal-net architecture|AChR.?clustering|fibrillogenesis|receptor availability|NK-cell stimulation|patterning|patterning ability|organizing activity|mid.?hindbrain|midbrain explants|chick embryos|ectodermal.?development|developmental defect|developmental phenotype|PCP pathway|canonical pathway|developmental abnormalit(?:y|ies))\b",
    ),
    (
        "generic_functional_readout",
        r"(?:\b(?:calcium|adenylyl|adenylate|beta.?arrestin|arrestin|second messenger|functional assays?|functional response|bioactivity|biological.?activity|receptor response|ligand response|phosphatidylinositol|phosphoinositide|inositol.?phosphate|IP1|IP3|agonist.?evoked|evoked response|evoked currents|GABA-induced currents|desensitization|patch.?clamp|voltage.?clamp|cytokine|interleukin|TSLP|externalization|lipase activity|specific activity|activity reduction|chylomicron|receptor pharmacology|peptide activity|complement evasion|complement resistance|complement.?regulatory|complement-control consequences|MAC deposition|C3 deposition|C4b deposition|C4b.?C4dg|C9 deposition|serum bactericidal|lectin-pathway readouts|MBL-to-mannose interference|adherence|cell attachment|bacterial penetration|postattachment MHC-I|axonal Nav delivery|cotransport|genetic interaction|mutant phenotypes|antigen-specific responses|BMP responses|developmental assays|plasminogen.?activator|uPA|PAI.?1|surface stabilization|dendritic targeting|excitability|cross.?presentation|channel.?gating|electroretinograph|visual.?adaptation|perineuronal.?net|architecture readout|AChR.?clustering|cell.?death|deacetylation|nucleocytoplasmic shuttling|cell.?surface organization|Schwann.?cell organization|active.?monomer stabilization|ligand stabilization|synaptogenic competition|Treg effects|Treg assays|GlyR clustering|actin bundling|spine assays|process morphology|cytoskeletal/process morphology|coenrichment|tight.?junction|strand analysis|surface GluA2 mobility|AMPAR-EPSC|membrane clustering|sodium extrusion|Wnt/BMP activity readouts|pathway assay|BMP patterning|ligand.?activity|cytoplasmic sequestration|glycine-receptor clustering|destruction complex|Wnt response|Wnt regulation)\b|(?-i:\bcAMP\b)|\bCa2\+|\b(?:inward current|outward current|chloride current|whole.?cell current|ion current|conductance|electrophysiolog))",
    ),
)


# A small, source-reviewed override table for records whose stored queue
# summary is too compressed for the classifier to preserve the readout that
# is explicit in the cited primary paper. These remain evidence-only route
# annotations; they do not assert topology, causality, or confidence.
CURATION_OVERRIDES: dict[str, dict[str, str]] = {
    "M21B-DOWNSTREAM:02329": {
        "output_class": "reporter_readout",
        "output_label": "EDA/TNFSF27-EDAR/TNFRSF27 documented NF-kB reporter activation and ectodermal developmental phenotype",
        "primary_locator": "PMID:36765055; PMCID:PMC9918506",
        "citation_note": "Primary study: PMID:36765055; PMCID:PMC9918506; primary locator: PMID:36765055; PMCID:PMC9918506",
        "evidence_summary": "Primary study reports the EDA-EDAR ectodomain structure and validates pathogenic variants with biochemical and cellular assays; full-length EDAR luciferase reporter assays show wild-type EDA activates NF-kB dose-dependently, and EDA/EDAR disruption produces ectodermal dysplasia phenotypes in developmental models.",
        "assay_or_perturbation": "EDAR NF-kB luciferase reporter assays in HEK293T cells, HaCaT cellular assays, recombinant EDA/EDAR binding and mouse ectodermal-development models",
    },
    "M21B-DOWNSTREAM:02349": {
        "output_class": "gene_expression_or_transcription",
        "output_label": "FGF8b-FGFR3c documented mid-hindbrain patterning and developmental gene-expression readout",
        "primary_locator": "PMID:16384934; PMCID:PMC1356110",
        "citation_note": "Primary study: PMID:16384934; PMCID:PMC1356110; primary locator: PMID:16384934; PMCID:PMC1356110",
        "evidence_summary": "Primary study measures FGF8 splice-isoform receptor binding and shows in chick embryos and murine midbrain explants that the FGF8b F32A mutation changes mid-hindbrain patterning ability; the reported patterning differences correlate with expression of Gbx2, Otx2, En1/2 and Spry1/2.",
        "assay_or_perturbation": "SPR receptor-binding panel, FGF8b-FGFR2c structure, FGF8b mutant analysis, chick embryo electroporation and murine midbrain explants",
    },
    "M21B-DOWNSTREAM:03007": {
        "output_class": "phosphorylation_or_activation_readout",
        "output_label": "CTHRC1-FZD5 documented Wnt/PCP pathway activation and canonical-pathway suppression",
        "primary_locator": "PMID:18606138; DOI:10.1016/j.devcel.2008.05.007",
        "citation_note": "Primary study: PMID:18606138; DOI:10.1016/j.devcel.2008.05.007; primary locator: PMID:18606138; DOI:10.1016/j.devcel.2008.05.007",
        "evidence_summary": "Primary study shows that CTHRC1 binds Wnt and Frizzled/Ror2 complexes, activates the planar-cell-polarity pathway, suppresses canonical Wnt signaling in HEK293T cells, and is associated with PCP-related developmental abnormalities in genetic comparator models.",
        "assay_or_perturbation": "Cell-surface-anchored CTHRC1, Wnt/FZD/Ror2 interaction assays, HEK293T PCP and canonical-pathway assays, and mouse genetic comparator models",
    },
    "M21B-DOWNSTREAM:03308": {
        "output_class": "generic_functional_readout",
        "output_label": "YAP1-AXIN1/Axin documented Wnt response regulation",
        "primary_locator": "PMID:24976009; DOI:10.1016/j.cell.2014.06.013",
        "citation_note": "Primary study: PMID:24976009; DOI:10.1016/j.cell.2014.06.013; primary locator: PMID:24976009; DOI:10.1016/j.cell.2014.06.013",
        "evidence_summary": "Primary study provides biochemical, functional and genetic evidence that YAP1 is incorporated into the beta-catenin destruction complex through Axin1; Wnt-on release of YAP1/TAZ supports nuclear accumulation and Wnt/YAP/TAZ-dependent biological responses, while APC-loss models link the mechanism to crypt overgrowth and regeneration.",
        "assay_or_perturbation": "Biochemical destruction-complex assays, Wnt-on/Wnt-off cellular perturbations, APC-loss intestinal models and ex vivo crypt regeneration assays",
    },
    "M21B-DOWNSTREAM:03309": {
        "output_class": "generic_functional_readout",
        "output_label": "WWTR1/TAZ-AXIN1/Axin documented Wnt response regulation",
        "primary_locator": "PMID:24976009; DOI:10.1016/j.cell.2014.06.013",
        "citation_note": "Primary study: PMID:24976009; DOI:10.1016/j.cell.2014.06.013; primary locator: PMID:24976009; DOI:10.1016/j.cell.2014.06.013",
        "evidence_summary": "Primary study provides biochemical, functional and genetic evidence that WWTR1/TAZ is incorporated into the beta-catenin destruction complex through Axin1; Wnt-on release of YAP1/TAZ supports nuclear accumulation and Wnt/YAP/TAZ-dependent biological responses, while APC-loss models link the mechanism to crypt overgrowth and regeneration.",
        "assay_or_perturbation": "Biochemical destruction-complex assays, Wnt-on/Wnt-off cellular perturbations, APC-loss intestinal models and ex vivo crypt regeneration assays",
    },
    "M21B-DOWNSTREAM:02295": {
        "output_class": "phosphorylation_or_activation_readout",
        "output_label": "IL5-IL5RA:CSF2RB receptor complex documented pSTAT5 signaling",
        "primary_locator": "PMID:38614096; PMID:22528658",
        "citation_note": "Primary studies: PMID:38614096; PMID:22528658; primary locator: PMID:38614096; PMID:22528658",
        "evidence_summary": "Primary IL-5 receptor-complex studies show ligand-dependent assembly of the IL-5Ralpha/beta-common signaling complex; engineered receptor systems demonstrate IL-5 signaling with JAK association and pSTAT5 dose-response readouts.",
        "assay_or_perturbation": "Human IL-5/IL-5Ralpha/beta-common cryo-EM and live-cell single-molecule receptor assembly; engineered chimeric receptors with JAK association and pSTAT5 dose-response assays",
    },
    "M21B-DOWNSTREAM:02454": {
        "output_class": "cellular_functional_readout",
        "output_label": "C9-complement C9-CD59 documented membrane-attack-complex inhibition",
        "primary_locator": "PMID:7523406",
        "citation_note": "Primary study: PMID:7523406; primary locator: PMID:7523406",
        "evidence_summary": "Primary C9 peptide-mapping study identifies the CD59-binding region exposed during C5b-9 assembly and frames the interaction as inhibition of membrane-attack-complex assembly; related CD59 functional assays measure protection from complement-mediated lysis.",
        "assay_or_perturbation": "Recombinant C9b peptides, CD59 binding and blocking assays during C5b-9 assembly; complement membrane-attack-complex inhibition context",
    },
    "M21B-DOWNSTREAM:02619": {
        "output_class": "cellular_functional_readout",
        "output_label": "PFN1-profilin I-GPHN/gephyrin documented inhibitory-synapse receptor packing and dynamics",
        "primary_locator": "PMID:12967995; PMCID:PMC6740687",
        "citation_note": "Primary study: PMID:12967995; primary locator: PMID:12967995; PMCID:PMC6740687",
        "evidence_summary": "Primary neuronal study shows profilin I directly associates with gephyrin, colocalizes at inhibitory synapses, and may regulate microfilament-dependent receptor packing density and dynamics at those synapses.",
        "assay_or_perturbation": "Rat spinal-cord and cultured-neuron colocalization, gephyrin/profilin co-immunoprecipitation, recombinant binding and gephyrin-cluster assays",
    },
    "M21B-DOWNSTREAM:02620": {
        "output_class": "cellular_functional_readout",
        "output_label": "PFN2-profilin IIa-GPHN/gephyrin documented inhibitory-synapse receptor packing and dynamics",
        "primary_locator": "PMID:12967995; PMCID:PMC6740687",
        "citation_note": "Primary study: PMID:12967995; primary locator: PMID:12967995; PMCID:PMC6740687",
        "evidence_summary": "Primary neuronal study shows profilin IIa directly associates with gephyrin, colocalizes at inhibitory synapses, and may regulate microfilament-dependent receptor packing density and dynamics at those synapses.",
        "assay_or_perturbation": "Rat spinal-cord and cultured-neuron colocalization, gephyrin/profilin co-immunoprecipitation, recombinant binding and gephyrin-cluster assays",
    },
    "M21B-DOWNSTREAM:02621": {
        "output_class": "cellular_functional_readout",
        "output_label": "ENAH/Mena-GPHN/gephyrin documented inhibitory-synapse receptor packing and dynamics",
        "primary_locator": "PMID:12967995; PMCID:PMC6740687",
        "citation_note": "Primary study: PMID:12967995; primary locator: PMID:12967995; PMCID:PMC6740687",
        "evidence_summary": "Primary neuronal study shows Mena directly associates with gephyrin, colocalizes at inhibitory synapses, and may contribute to microfilament-dependent receptor packing density and dynamics at those synapses.",
        "assay_or_perturbation": "Rat spinal-cord and cultured-neuron colocalization, gephyrin/Mena co-immunoprecipitation, recombinant binding and gephyrin-cluster assays",
    },
    "M21B-DOWNSTREAM:02622": {
        "output_class": "cellular_functional_readout",
        "output_label": "VASP-GPHN/gephyrin documented inhibitory-synapse receptor packing and dynamics",
        "primary_locator": "PMID:12967995; PMCID:PMC6740687",
        "citation_note": "Primary study: PMID:12967995; primary locator: PMID:12967995; PMCID:PMC6740687",
        "evidence_summary": "Primary neuronal study shows VASP-family proteins directly associate with gephyrin, colocalize at inhibitory synapses, and may contribute to microfilament-dependent receptor packing density and dynamics at those synapses.",
        "assay_or_perturbation": "Rat spinal-cord and cultured-neuron colocalization, gephyrin/VASP co-immunoprecipitation, recombinant binding and gephyrin-cluster assays",
    },
    "M21B-DOWNSTREAM:02648": {
        "output_class": "cellular_functional_readout",
        "output_label": "S100A10/p11-CTSB/procathepsin B documented tumor-invasion and metastasis-associated surface function",
        "primary_locator": "PMID:10777578",
        "citation_note": "Primary study: PMID:10777578; primary locator: PMID:10777578",
        "evidence_summary": "Primary tumor-cell study shows procathepsin B associates with the annexin-II/p11 complex at the cell surface and interprets the interaction as a mechanism that may facilitate tumor invasion and metastasis.",
        "assay_or_perturbation": "Recombinant binding and yeast two-hybrid assays, tumor-cell co-immunoprecipitation and surface colocalization in breast-carcinoma and glioma cells",
    },
    "M21B-DOWNSTREAM:02652": {
        "output_class": "generic_functional_readout",
        "output_label": "P2Y4/P2RY4-P2Y6/P2RY6 documented UTP-dependent receptor oligomerization and membrane-domain regulation",
        "primary_locator": "PMID:17481575; DOI:10.1016/j.bbamem.2007.03.020",
        "citation_note": "Primary study: PMID:17481575; DOI:10.1016/j.bbamem.2007.03.020; primary locator: PMID:17481575; DOI:10.1016/j.bbamem.2007.03.020",
        "evidence_summary": "Primary neuronal study detects endogenous P2Y4/P2Y6 hetero-oligomers in PC12 cells, shows UTP-dependent shifting of P2Y6 oligomerization, and links receptor quaternary structure to lipid-raft partitioning and functional regulation.",
        "assay_or_perturbation": "Rat PC12 and transfected receptor systems, blue-native electrophoresis, immunoprecipitation, synaptosome/lipid-raft partitioning and UTP perturbation",
    },
    "M21B-DOWNSTREAM:02995": {
        "output_class": "cellular_functional_readout",
        "output_label": "CBLN2-NRXN2beta documented cerebellar synaptic function and motor-rescue phenotype",
        "primary_locator": "PMID:22117778; PMCID:PMC3259274",
        "citation_note": "Primary study: PMID:22117778; PMCID:PMC3259274; primary locator: PMID:22117778; PMCID:PMC3259274",
        "evidence_summary": "Primary mouse study shows Cbln2 binds beta-neurexin splice variants including Nrxn2beta, and ectopic Cbln2 expression rescues cerebellar deficits and motor performance in Cbln1-null animals, supporting a synaptic-organizing output in the shared receptor context.",
        "assay_or_perturbation": "HEK293T beta-neurexin binding assays, Cbln1-null/L7-Cbln2 transgenic rescue, cerebellar histology and accelerating rotarod performance",
    },
    "M21B-DOWNSTREAM:02996": {
        "output_class": "cellular_functional_readout",
        "output_label": "CBLN2-NRXN3beta documented cerebellar synaptic function and motor-rescue phenotype",
        "primary_locator": "PMID:22117778; PMCID:PMC3259274",
        "citation_note": "Primary study: PMID:22117778; PMCID:PMC3259274; primary locator: PMID:22117778; PMCID:PMC3259274",
        "evidence_summary": "Primary mouse study shows Cbln2 binds beta-neurexin splice variants including Nrxn3beta, and ectopic Cbln2 expression rescues cerebellar deficits and motor performance in Cbln1-null animals, supporting a synaptic-organizing output in the shared receptor context.",
        "assay_or_perturbation": "HEK293T beta-neurexin binding assays, Cbln1-null/L7-Cbln2 transgenic rescue, cerebellar histology and accelerating rotarod performance",
    },
    "M21B-DOWNSTREAM:03162": {
        "output_class": "phosphorylation_or_activation_readout",
        "output_label": "RSPO1-RNF43 documented Wnt signaling potentiation",
        "primary_locator": "PMID:23756651",
        "citation_note": "Primary study: PMID:23756651; primary locator: PMID:23756651",
        "evidence_summary": "Primary structural and functional study identifies RNF43 as an RSPO1 effector receptor in the LGR5-RSPO1-RNF43 complex and reports that R-spondins enhance Wnt signaling and stem-cell-related responses.",
        "assay_or_perturbation": "Purified LGR5/RSPO1/RNF43 ternary-complex structure, interface analysis and Wnt-signaling functional context",
    },
    "M21B-DOWNSTREAM:03212": {
        "output_class": "generic_functional_readout",
        "output_label": "BMP10 prodomain-FBN1/fibrillin-1 documented extracellular BMP bioavailability control",
        "primary_locator": "PMID:18339631; PMCID:PMC2376219",
        "citation_note": "Primary study: PMID:18339631; PMCID:PMC2376219; primary locator: PMID:18339631; PMCID:PMC2376219",
        "evidence_summary": "Primary study shows BMP10 prodomain binding to fibrillin microfibrils and interprets prodomain-fibrillin interactions as extracellular targeting and control of BMP growth-factor bioavailability.",
        "assay_or_perturbation": "BMP10 prodomain/fibrillin-1 binding by SPR, complex formation and extracellular-matrix targeting assays",
    },
    "M21B-DOWNSTREAM:03214": {
        "output_class": "generic_functional_readout",
        "output_label": "BMP4 prodomain-FBN2/fibrillin-2 documented extracellular BMP bioavailability control",
        "primary_locator": "PMID:18339631; PMCID:PMC2376219",
        "citation_note": "Primary study: PMID:18339631; PMCID:PMC2376219; primary locator: PMID:18339631; PMCID:PMC2376219",
        "evidence_summary": "Primary study shows BMP4 prodomain binding within fibrillin microfibril networks and interprets prodomain-fibrillin interactions as extracellular targeting and control of BMP growth-factor bioavailability.",
        "assay_or_perturbation": "BMP4 prodomain/fibrillin-2 binding by SPR, complex formation and extracellular-matrix targeting assays",
    },
    "M21B-DOWNSTREAM:03216": {
        "output_class": "generic_functional_readout",
        "output_label": "BMP10 prodomain-FBN2/fibrillin-2 documented extracellular BMP bioavailability control",
        "primary_locator": "PMID:18339631; PMCID:PMC2376219",
        "citation_note": "Primary study: PMID:18339631; PMCID:PMC2376219; primary locator: PMID:18339631; PMCID:PMC2376219",
        "evidence_summary": "Primary study shows BMP10 prodomain binding to fibrillin microfibril components and interprets prodomain-fibrillin interactions as extracellular targeting and control of BMP growth-factor bioavailability.",
        "assay_or_perturbation": "BMP10 prodomain/fibrillin-2 binding by SPR, complex formation and extracellular-matrix targeting assays",
    },
    "M21B-DOWNSTREAM:03218": {
        "output_class": "generic_functional_readout",
        "output_label": "BMP5 prodomain-FBN1/fibrillin-1 documented extracellular BMP bioavailability control",
        "primary_locator": "PMID:21135108; PMCID:PMC3037620",
        "citation_note": "Primary study: PMID:21135108; PMCID:PMC3037620; primary locator: PMID:21135108; PMCID:PMC3037620",
        "evidence_summary": "Primary study shows BMP5 prodomain binding to fibrillin-1 and interprets TGF-beta-superfamily prodomain interactions with extracellular-matrix macromolecules as mechanisms controlling growth-factor targeting and bioavailability.",
        "assay_or_perturbation": "BMP5 prodomain/fibrillin-1 SPR and competition assays, growth-factor complex formation and BMP bioactivity assays",
    },
    "M21B-DOWNSTREAM:03219": {
        "output_class": "generic_functional_readout",
        "output_label": "BMP5 prodomain-FBN2/fibrillin-2 documented extracellular BMP bioavailability control",
        "primary_locator": "PMID:21135108; PMCID:PMC3037620",
        "citation_note": "Primary study: PMID:21135108; PMCID:PMC3037620; primary locator: PMID:21135108; PMCID:PMC3037620",
        "evidence_summary": "Primary study shows BMP5 prodomain binding to fibrillin-2 and interprets TGF-beta-superfamily prodomain interactions with extracellular-matrix macromolecules as mechanisms controlling growth-factor targeting and bioavailability.",
        "assay_or_perturbation": "BMP5 prodomain/fibrillin-2 SPR and competition assays, growth-factor complex formation and BMP bioactivity assays",
    },
    "M21B-DOWNSTREAM:03220": {
        "output_class": "generic_functional_readout",
        "output_label": "GDF8/myostatin prodomain-perlecan documented extracellular growth-factor sequestration",
        "primary_locator": "PMID:21135108; PMCID:PMC3037620",
        "citation_note": "Primary study: PMID:21135108; PMCID:PMC3037620; primary locator: PMID:21135108; PMCID:PMC3037620",
        "evidence_summary": "Primary study shows GDF8/myostatin prodomain binding to glycosaminoglycan-bearing perlecan domain V and interprets the interaction as extracellular-matrix targeting that regulates growth-factor bioavailability.",
        "assay_or_perturbation": "GDF8 prodomain/perlecan binding by blot overlay, ELISA and SPR with heparinase and domain controls",
    },
    "M21B-DOWNSTREAM:03236": {
        "output_class": "phosphorylation_or_activation_readout",
        "output_label": "COLEC11/collectin-11-MASP1 documented lectin-complement activation",
        "primary_locator": "PMID:20956340; PMID:23220946; PMCID:PMC6741501",
        "citation_note": "Primary studies: PMID:20956340; PMID:23220946; PMCID:PMC6741501; primary locator: PMID:20956340; PMID:23220946; PMCID:PMC6741501",
        "evidence_summary": "Primary studies show collectin-11 associates with MASP-1/3 and, in the collectin-11/MASP complex, initiates lectin-pathway complement activation with C4b, C3b and terminal-complex deposition on microbial surfaces.",
        "assay_or_perturbation": "Human serum and recombinant collectin-11/MASP assays, microbial binding, C4b/C3b deposition and terminal complement-complex assays",
    },
    "M21B-DOWNSTREAM:03237": {
        "output_class": "phosphorylation_or_activation_readout",
        "output_label": "COLEC11/collectin-11-MASP3 documented lectin-complement activation",
        "primary_locator": "PMID:20956340; PMID:23220946; PMCID:PMC6741501",
        "citation_note": "Primary studies: PMID:20956340; PMID:23220946; PMCID:PMC6741501; primary locator: PMID:20956340; PMID:23220946; PMCID:PMC6741501",
        "evidence_summary": "Primary studies show collectin-11 associates with MASP-3 and, in the collectin-11/MASP complex, initiates lectin-pathway complement activation with C4b, C3b and terminal-complex deposition on microbial surfaces.",
        "assay_or_perturbation": "Human serum and recombinant collectin-11/MASP assays, microbial binding, C4b/C3b deposition and terminal complement-complex assays",
    },
    "M21B-DOWNSTREAM:03256": {
        "output_class": "cellular_functional_readout",
        "output_label": "extracellular vimentin-IGF1R documented IGF1R phosphorylation and axonal growth",
        "primary_locator": "PMID:26170015; PMCID:PMC4501001",
        "citation_note": "Primary study: PMID:26170015; PMCID:PMC4501001; primary locator: PMID:26170015; PMCID:PMC4501001",
        "evidence_summary": "Primary cortical-neuron study identifies IGF1R as highly phosphorylated after extracellular vimentin stimulation; IGF1R blockade reduces vimentin-induced axonal growth, linking the extracellular interaction to a bounded growth readout.",
        "assay_or_perturbation": "Cultured cortical neurons, IGF1R phosphorylation assays, IGF1R-neutralizing blockade, recombinant binding and axonal-growth measurements",
    },
    "M21B-DOWNSTREAM:03265": {
        "output_class": "cellular_functional_readout",
        "output_label": "BNIP3-LC3B documented autophagy, mitophagy and ER-phagy",
        "primary_locator": "PMID:22505714",
        "citation_note": "Primary study: PMID:22505714; primary locator: PMID:22505714",
        "evidence_summary": "Primary cell study shows BNIP3-LC3 interaction is required in part for BNIP3-induced mitochondrial and ER removal; BNIP3 increases GFP-LC3 autophagosomes and induces mitophagy and ER-phagy, while LC3-binding mutants reduce those outputs.",
        "assay_or_perturbation": "HeLa-cell BNIP3 and LC3 perturbations, GFP-LC3/GABARAP autophagosome assays, organelle-targeted BNIP3 constructs and LC3-binding mutants",
    },
    "M21B-DOWNSTREAM:03266": {
        "output_class": "cellular_functional_readout",
        "output_label": "FUNDC1-LC3B documented selective mitophagy",
        "primary_locator": "PMID:27757847; PMCID:PMC5233613",
        "citation_note": "Primary study: PMID:27757847; PMCID:PMC5233613; primary locator: PMID:27757847; PMCID:PMC5233613",
        "evidence_summary": "Primary structural and biochemical study shows phosphorylation-state-dependent FUNDC1-LC3B recognition and interprets the interaction as a regulatory switch for selective hypoxia-induced mitophagy.",
        "assay_or_perturbation": "LC3B/FUNDC1 phosphopeptide crystal structure, site-directed mutants and isothermal-titration-calorimetry binding assays",
    },
    "M21B-DOWNSTREAM:03267": {
        "output_class": "gene_expression_or_transcription",
        "output_label": "WWTR1/TAZ pS89-SFN/14-3-3sigma documented cytoplasmic retention and transcriptional inactivation",
        "primary_locator": "PMCID:PMC2268418; PMID:18227151",
        "citation_note": "Primary study: PMCID:PMC2268418; PMID:18227151; primary locator: PMCID:PMC2268418; PMID:18227151",
        "evidence_summary": "Primary Hippo-pathway study shows Lats-dependent TAZ Ser89 phosphorylation creates a 14-3-3 binding site, promotes cytoplasmic retention and functionally inactivates TAZ; TAZ reporter activity, proliferation and epithelial-mesenchymal-transition outputs are altered by this axis.",
        "assay_or_perturbation": "TAZ Ser89 phosphorylation and 14-3-3 association, Gal4/TEAD luciferase reporter, cytoplasmic-localization, proliferation and EMT assays",
    },
    "M21B-DOWNSTREAM:03307": {
        "output_class": "gene_expression_or_transcription",
        "output_label": "WWTR1/TAZ-beta-catenin documented Wnt-target gene-expression suppression",
        "primary_locator": "PMID:22234184; PMCID:PMC3297994",
        "citation_note": "Primary study: PMID:22234184; PMCID:PMC3297994; primary locator: PMID:22234184; PMCID:PMC3297994",
        "evidence_summary": "Primary Hippo-Wnt study shows TAZ co-immunoprecipitates with beta-catenin and that YAP/TAZ suppress Wnt signaling through prevention of beta-catenin nuclear translocation, reducing Wnt-target gene expression in the tested cellular context.",
        "assay_or_perturbation": "293T and Caco-2 co-immunoprecipitation, purified-protein pull-down, beta-catenin nuclear-translocation and Wnt-target gene-expression assays",
    },
    "M21B-DOWNSTREAM:02299": {
        "output_class": "phosphorylation_or_activation_readout",
        "output_label": "BMP9-ACVRL1:ACVR2B documented ALK1/pSMAD1/5/8 and ID1 endothelial signaling readout",
        "primary_locator": "PMID:22718755; PMCID:PMC3431715; PMID:17068149",
        "citation_note": "Primary studies: PMID:22718755; PMCID:PMC3431715; PMID:17068149; primary locator: PMID:22718755; PMCID:PMC3431715; PMID:17068149",
        "evidence_summary": "Primary structural and functional studies show BMP9 forms a signaling complex with ALK1 and the type-II receptor ActRIIB, while BMP9/10 stimulation produces Smad1/5/8 phosphorylation and ID1 transcriptional readouts in endothelial cells. This record retains output evidence without asserting that the structural receptor assignment alone establishes the complete route topology.",
        "assay_or_perturbation": "BMP9-ALK1-ActRIIB structural and receptor-binding assays; endothelial BMP9/10 stimulation with pSMAD1/5/8, BRE/ID1 and migration/growth assays",
    },
    "M21B-DOWNSTREAM:02583": {
        "output_class": "cellular_functional_readout",
        "output_label": "LRRTM1-NRXN1alpha/beta documented hemisynapse clustering and hemisynaptogenesis",
        "primary_locator": "PMID:20519524; PMID:30262834",
        "citation_note": "Primary studies: PMID:20519524; PMID:30262834; primary locator: PMID:20519524; PMID:30262834",
        "evidence_summary": "Primary neuronal studies identify LRRTM1 as a neurexin ligand and report LRRTM1-dependent hemisynapse clustering/hemisynaptogenesis in the tested synaptic-organizing assays, with splice-dependent interaction involving NRXN1alpha/beta forms.",
        "assay_or_perturbation": "Neurexin-binding and cell-surface interaction assays, heterologous synapse-induction assays and neuronal hemisynapse-clustering measurements",
    },
    "M21B-DOWNSTREAM:02730": {
        "output_class": "cellular_functional_readout",
        "output_label": "MUC16-Siglec9 documented inhibitory NK/immune-cell response and anti-tumor immune evasion",
        "primary_locator": "PMID:20497550; PMCID:PMC2890604",
        "citation_note": "Primary study: PMID:20497550; PMCID:PMC2890604; primary locator: PMID:20497550; PMCID:PMC2890604",
        "evidence_summary": "Primary ovarian-cancer study identifies Siglec-9 as an inhibitory receptor engaged by soluble and cell-surface MUC16; the reported MUC16-Siglec-9 interaction is associated with suppression of anti-tumor immune responses in the tested NK-cell and tumor-cell context.",
        "assay_or_perturbation": "MUC16/Siglec-9 binding and cell-surface assays, NK-cell functional assays and ovarian-tumor immune-response analyses",
    },
    "M21B-DOWNSTREAM:03055": {
        "output_class": "cellular_functional_readout",
        "output_label": "IZUMO1-JUNO documented sperm-egg adhesion, fusion and fertilization output",
        "primary_locator": "PMID:27309818; PMCID:PMC4947182",
        "citation_note": "Primary study: PMID:27309818; PMCID:PMC4947182; primary locator: PMID:27309818; PMCID:PMC4947182",
        "evidence_summary": "Primary reproductive-cell study identifies JUNO as the IZUMO1 receptor and shows that Juno-deficient eggs fail sperm fusion while wild-type Juno rescues fertilization competence; the heterologous binding and complementation assays provide a bounded sperm-egg adhesion/fusion output.",
        "assay_or_perturbation": "IZUMO1-JUNO structure and binding assays, Juno-knockout egg fertilization/fusion assays, wild-type and mutant complementation and heterologous cell-surface binding",
    },
    "M21B-DOWNSTREAM:03147": {
        "output_class": "phosphorylation_or_activation_readout",
        "output_label": "LACRT-SDC1 documented prosecretory and mitogenic signaling output",
        "primary_locator": "PMID:16982797; PMID:16923831; PMCID:PMC2712882",
        "citation_note": "Primary studies: PMID:16982797; PMID:16923831; PMCID:PMC2712882; primary locator: PMID:16982797; PMID:16923831; PMCID:PMC2712882",
        "evidence_summary": "Primary ocular-surface studies identify syndecan-1 as a heparan-sulfate-dependent lacritin-binding partner and show lacritin-dependent epithelial prosecretory and mitogenic signaling through Gi/o, PKCalpha, PLC, calcium/calcineurin-NFATC1 and PLD-mTOR readouts. The intracellular cascade is retained as supporting evidence rather than asserted as a complete route for this ligand-receptor record.",
        "assay_or_perturbation": "Lacritin/syndecan-1 binding and deglycanation assays, epithelial secretion and proliferation assays, Gi/o/PKCalpha/PLC/Ca2+/calcineurin-NFATC1 and PLD-mTOR pathway perturbations",
    },
    "M21B-DOWNSTREAM:02688": {
        "output_class": "translocation_or_localization_readout",
        "output_label": "DAT-RACK1/GNB2L1 documented PKC-linked transporter trafficking regulation",
        "primary_locator": "PMID:15202772",
        "citation_note": "Primary study: PMID:15202772; primary locator: PMID:15202772",
        "evidence_summary": "Primary DAT-interaction study identifies RACK1/GNB2L1 in a functional regulatory complex with the dopamine transporter and proposes that the complex modulates DAT phosphorylation by PKC and transporter trafficking.",
        "assay_or_perturbation": "DAT N-terminal yeast-two-hybrid and heterologous interaction assays with syntaxin 1A/RACK1; PKC-linked phosphorylation and transporter-trafficking regulatory context",
    },
    "M21B-DOWNSTREAM:02926": {
        "output_class": "cellular_functional_readout",
        "output_label": "EBV gp350/220-CR2/CD21 documented B-cell viral attachment",
        "primary_locator": "PMID:3033269; PMCID:PMC254117; PMID:17925391; PMID:18786993",
        "citation_note": "Primary studies: PMID:3033269; PMCID:PMC254117; PMID:17925391; PMID:18786993; primary locator: PMID:3033269; PMCID:PMC254117; PMID:17925391; PMID:18786993",
        "evidence_summary": "Primary EBV studies show gp350/220 binding to CR2/CD21 on B cells and identify this interaction as the initial viral-attachment step preceding later penetration events. The annotation therefore records attachment output without claiming that gp350-CR2 alone completes EBV entry.",
        "assay_or_perturbation": "Purified gp350/EBV and CR2 binding, CR2-positive versus CR2-negative B-cell attachment assays, gp350/CR2 mutagenesis and EBV B-cell entry context",
    },
    "M21B-DOWNSTREAM:02948": {
        "output_class": "cellular_functional_readout",
        "output_label": "HSV-2 gC-C3b documented complement-evasion and neutralization-resistance output",
        "primary_locator": "PMID:1602532; PMCID:PMC241204; PMID:16571820",
        "citation_note": "Primary studies: PMID:1602532; PMCID:PMC241204; PMID:16571820; primary locator: PMID:1602532; PMCID:PMC241204; PMID:16571820",
        "evidence_summary": "Primary HSV glycoprotein-C studies show gC binding to C3b and link gC expression to protection from complement-mediated neutralization; the original gC1/gC2 comparison also maps C3b interaction and alternative-pathway effects. The output is recorded as complement-evasion evidence, not as a complete viral-entry route.",
        "assay_or_perturbation": "Purified gC/C3b binding and truncation assays, alternative-pathway complement assays, infected-cell and gC-null virus comparisons, and complement-mediated neutralization assays",
    },
    "M21B-DOWNSTREAM:03170": {
        "output_class": "cellular_functional_readout",
        "output_label": "TIMP2-MMP14/MT1-MMP documented protease-inhibition and pro-MMP2-activation context",
        "primary_locator": "PMID:9422789; DOI:10.1074/jbc.273.2.1216",
        "citation_note": "Primary study: PMID:9422789; DOI:10.1074/jbc.273.2.1216; primary locator: PMID:9422789; DOI:10.1074/jbc.273.2.1216",
        "evidence_summary": "Primary MT1-MMP study demonstrates direct cell-surface TIMP2 binding and defines the TIMP2-MT1-MMP complex in the competing contexts of catalytic inhibition and cell-surface pro-MMP2 activation. The annotation preserves that bounded protease-regulatory output without treating TIMP2 as a transcriptional signaling ligand.",
        "assay_or_perturbation": "Radiolabeled TIMP2 binding to MT1-MMP-transfected cells, catalytic-site competition, cross-linking/immunoprecipitation and cell-surface pro-MMP2 activation assays",
    },
    "M21B-DOWNSTREAM:03262": {
        "output_class": "secreted_protein_or_release",
        "output_label": "CD23-CD11b/CD18-Mac-1 documented monocyte activation with IL-6 production",
        "primary_locator": "PMID:7621072; PMID:9341771",
        "citation_note": "Primary studies: PMID:7621072; PMID:9341771; primary locator: PMID:7621072; PMID:9341771",
        "evidence_summary": "Primary CD23-integrin studies show CD23 binding to CD11b/CD18 and CD11c/CD18 on monocytes/macrophages and demonstrate a functional cytokine output: soluble CD23 engagement induces IL-6 production, with blocking antibodies reducing the response. The route remains evidence-only and does not assert an intracellular intermediate chain.",
        "assay_or_perturbation": "Soluble CD23 and CD23-liposome binding to beta2-integrin-expressing cells, antibody-blocking experiments, primary monocyte/macrophage activation and IL-6 production assays",
    },
    "M21B-DOWNSTREAM:03278": {
        "output_class": "phosphorylation_or_activation_readout",
        "output_label": "EDA-A2-XEDAR/EDA2R documented TRAF3/TRAF6-dependent NF-kB and JNK signaling",
        "primary_locator": "PMID:12270937",
        "citation_note": "Primary study: PMID:12270937; primary locator: PMID:12270937",
        "evidence_summary": "Primary XEDAR signaling study shows EDA-A2-dependent activation of NF-kB and JNK, recruitment of TRAF3 and TRAF6 to the aggregated receptor complex, and pathway dependence on IKK/NEMO and ASK1 components. This is a bounded receptor-proximal signaling readout rather than a complete TF-target-gene chain.",
        "assay_or_perturbation": "EDA-A2 stimulation of XEDAR-expressing cells, TRAF3/TRAF6 recruitment, NF-kB and JNK pathway assays, deletion/point-mutant mapping and IKK/ASK1 perturbations",
    },
    "M21B-DOWNSTREAM:02594": {
        "output_class": "translocation_or_localization_readout",
        "output_label": "GlyR-beta-GPHN/gephyrin documented postsynaptic glycine-receptor localization and matrix assembly",
        "primary_locator": "PMID:7546736; DOI:10.1016/0896-6273(95)90145-0",
        "citation_note": "Primary study: PMID:7546736; DOI:10.1016/0896-6273(95)90145-0; primary locator: PMID:7546736; DOI:10.1016/0896-6273(95)90145-0",
        "evidence_summary": "Primary neuronal study identifies the GlyR-beta cytoplasmic gephyrin-binding motif and reports that beta-subunit expression is essential for formation of the postsynaptic glycine-receptor matrix. The annotation records receptor localization/scaffolding output without adding an unobserved intracellular relay.",
        "assay_or_perturbation": "Recombinant gephyrin/GlyR-beta-loop binding, overlay assays, transfected mammalian cells and beta-loop insertion tests for postsynaptic matrix assembly",
    },
    "M21B-DOWNSTREAM:03251": {
        "output_class": "generic_functional_readout",
        "output_label": "IL1A-IL1R2:IL1RAP soluble decoy complex documented IL-1alpha antagonism",
        "primary_locator": "PMID:12530978; DOI:10.1016/S1074-7613(02)00514-9",
        "citation_note": "Primary study: PMID:12530978; DOI:10.1016/S1074-7613(02)00514-9; primary locator: PMID:12530978; DOI:10.1016/S1074-7613(02)00514-9",
        "evidence_summary": "Primary soluble-decoy-receptor study shows IL-1RAcP increases the affinity of soluble IL-1R2 for IL-1alpha and concludes that this complex contributes to antagonism of IL-1 action. The route is retained as a molecular neutralization output, not a canonical signaling chain.",
        "assay_or_perturbation": "Recombinant soluble IL-1alpha, IL-1R2 and IL-1RAcP affinity/complex assays with comparison to IL-1 receptor antagonist binding",
    },
    "M21B-DOWNSTREAM:03252": {
        "output_class": "generic_functional_readout",
        "output_label": "IL1B-IL1R2:IL1RAP soluble decoy complex documented IL-1beta antagonism",
        "primary_locator": "PMID:12530978; DOI:10.1016/S1074-7613(02)00514-9",
        "citation_note": "Primary study: PMID:12530978; DOI:10.1016/S1074-7613(02)00514-9; primary locator: PMID:12530978; DOI:10.1016/S1074-7613(02)00514-9",
        "evidence_summary": "Primary soluble-decoy-receptor study shows IL-1RAcP increases the affinity of soluble IL-1R2 for IL-1beta by approximately 100-fold and concludes that the complex contributes to antagonism of IL-1 action. The route is retained as a molecular neutralization output, not a canonical signaling chain.",
        "assay_or_perturbation": "Recombinant soluble IL-1beta, IL-1R2 and IL-1RAcP affinity/complex assays with comparison to IL-1 receptor antagonist binding",
    },
    "M21B-DOWNSTREAM:02285": {
        "output_class": "cellular_functional_readout",
        "output_label": "LAMC1/LAM511-ITGA6:ITGB1 documented laminin adhesion and TAZ-linked breast-cancer-stem-cell function",
        "primary_locator": "PMID:34188035; PMCID:PMC4281560",
        "citation_note": "Primary studies: PMID:34188035; PMCID:PMC4281560; primary locator: PMID:34188035; PMCID:PMC4281560",
        "evidence_summary": "Primary laminin-integrin studies establish alpha6beta1 recognition of laminin-511, while functional breast-cancer-stem-cell experiments show laminin-511-dependent adhesion and activation of the Hippo transducer TAZ with effects on self-renewal and tumor initiation. The annotation retains the functional output without asserting a complete integrin relay.",
        "assay_or_perturbation": "Laminin-511/alpha6beta1 structural and binding assays, cell-adhesion assays, alpha6B depletion, TAZ readouts, mammosphere formation and tumor-initiation assays",
    },
    "M21B-DOWNSTREAM:02365": {
        "output_class": "cellular_functional_readout",
        "output_label": "CD274/PD-L1-PDCD1/PD-1 documented inhibitory T-cell activation and cytokine output",
        "primary_locator": "PMID:26602187; PMCID:PMC4752817; PMID:11857337; PMID:12538684",
        "citation_note": "Primary studies: PMID:26602187; PMCID:PMC4752817; PMID:11857337; PMID:12538684; primary locator: PMID:26602187; PMCID:PMC4752817; PMID:11857337; PMID:12538684",
        "evidence_summary": "Structural studies establish PD-L1 recognition by PD-1, and primary T-cell functional studies show PD-1/PD-L1 engagement inhibits proliferation, IL-2/cytokine production and T-cell activation; blockade of PD-L1 reverses the inhibition. The route is retained as an immune-checkpoint output without assigning unmeasured intracellular intermediates.",
        "assay_or_perturbation": "PD-1/PD-L1 structural and binding assays, antigen-presenting-cell/T-cell co-culture, PD-L1 blockade, proliferation and cytokine-production assays",
    },
    "M21B-DOWNSTREAM:02368": {
        "output_class": "cellular_functional_readout",
        "output_label": "HLA-G-LILRB1/ILT2 documented inhibitory NK/APC immune response",
        "primary_locator": "PMID:17056715; PMCID:PMC1637596; PMID:17549736; PMID:22144141",
        "citation_note": "Primary studies: PMID:17056715; PMCID:PMC1637596; PMID:17549736; PMID:22144141; primary locator: PMID:17056715; PMCID:PMC1637596; PMID:17549736; PMID:22144141",
        "evidence_summary": "Primary structural and functional studies establish HLA-G recognition by LILRB1 and show HLA-G/LILRB1-associated inhibition of antigen-presenting-cell or NK-cell responses, including reduced cytolytic function and altered APC/lymphocyte responses. The annotation preserves immune-inhibitory output without asserting a complete phosphatase relay.",
        "assay_or_perturbation": "HLA-G/LILRB1 structural and binding assays, decidual APC/lymphocyte functional assays, NK-cell calcium/cytotoxicity assays and HLA-G blockade/comparator experiments",
    },
    "M21B-DOWNSTREAM:02369": {
        "output_class": "cellular_functional_readout",
        "output_label": "HLA-G-LILRB2/ILT4 documented inhibitory myeloid and dendritic-cell response",
        "primary_locator": "PMID:17056715; PMCID:PMC1637596; PMID:20702625",
        "citation_note": "Primary studies: PMID:17056715; PMCID:PMC1637596; PMID:20702625; primary locator: PMID:17056715; PMCID:PMC1637596; PMID:20702625",
        "evidence_summary": "Primary structural and functional studies establish HLA-G recognition by LILRB2 and show soluble HLA-G/LILRB2-associated suppression of myeloid dendritic-cell function and maturation in the tested immune context. The annotation retains the observed immune output without assigning a complete intracellular cascade.",
        "assay_or_perturbation": "HLA-G/LILRB2 structural and binding assays, monocyte-derived dendritic-cell exposure to soluble HLA-G, maturation-marker/costimulatory assays and receptor-dependence analysis",
    },
    "M21B-DOWNSTREAM:02440": {
        "output_class": "translocation_or_localization_readout",
        "output_label": "HFE-beta2M-TfR1 documented reduced transferrin-receptor endocytosis and cellular iron uptake",
        "primary_locator": "PMID:10556042; PMID:11196670",
        "citation_note": "Primary studies: PMID:10556042; PMID:11196670; primary locator: PMID:10556042; PMID:11196670",
        "evidence_summary": "Primary HFE/TfR studies show HFE competes with diferric transferrin at the transferrin receptor and, in cells, reduces transferrin-receptor endocytosis and transferrin-bound iron uptake while increasing receptor phosphorylation and surface accumulation.",
        "assay_or_perturbation": "HFE-beta2M/TfR binding and competition assays, HFE-expressing cells, transferrin endocytosis kinetics, receptor phosphorylation and cellular iron-uptake measurements",
    },
    "M21B-DOWNSTREAM:02578": {
        "output_class": "cellular_functional_readout",
        "output_label": "COL4A1/COL4-collagen IV-ITGA1:ITGB1 documented collagen adhesion",
        "primary_locator": "PMID:8344274; PMID:1646206; PMID:10457223",
        "citation_note": "Primary studies: PMID:8344274; PMID:1646206; PMID:10457223; primary locator: PMID:8344274; PMID:1646206; PMID:10457223",
        "evidence_summary": "Primary studies map collagen-IV binding to alpha1beta1 and demonstrate that alpha1beta1-dependent cell adhesion to collagen matrices is blocked by integrin antibodies. The route records collagen adhesion as the bounded output without extending it to a universal integrin signaling mechanism.",
        "assay_or_perturbation": "Purified alpha1beta1/collagen-IV binding assays, collagen-matrix adhesion assays, integrin-subunit blocking and divalent-cation perturbations",
    },
    "M21B-DOWNSTREAM:02579": {
        "output_class": "cellular_functional_readout",
        "output_label": "COL4A1/COL4-collagen IV-ITGA2:ITGB1 documented collagen adhesion and keratinocyte migration",
        "primary_locator": "PMID:8344274; PMID:1646206; PMID:7933990",
        "citation_note": "Primary studies: PMID:8344274; PMID:1646206; PMID:7933990; primary locator: PMID:8344274; PMID:1646206; PMID:7933990",
        "evidence_summary": "Primary studies map collagen-IV binding to alpha2beta1 and show that alpha2beta1 blockade inhibits keratinocyte migration on collagen-IV matrices. The route records adhesion/migration output without inferring an unmeasured intracellular relay.",
        "assay_or_perturbation": "Purified alpha2beta1/collagen-IV binding assays, collagen-IV matrix migration assays, integrin-blocking antibodies and collagen-fragment substrate tests",
    },
    "M21B-DOWNSTREAM:02580": {
        "output_class": "phosphorylation_or_activation_readout",
        "output_label": "NPHS1/nephrin-KIRREL1/NEPH1 documented outside-in actin polymerization and slit-diaphragm organization",
        "primary_locator": "PMID:12660326; PMCID:PMC2169393",
        "citation_note": "Primary studies: PMID:12660326; PMCID:PMC2169393; primary locator: PMID:12660326; PMCID:PMC2169393",
        "evidence_summary": "Primary studies establish nephrin-NEPH1 complex formation and show that the complex can transduce an outside-in signal resulting in actin polymerization at the plasma membrane, consistent with podocyte-foot-process/slit-diaphragm organization. The route remains evidence-only and does not assert every intermediate.",
        "assay_or_perturbation": "Nephrin/NEPH1 ectodomain and full-length interaction assays, cell-surface clustering, cytoplasmic signaling-complex perturbation and actin-polymerization readouts",
    },
    "M21B-DOWNSTREAM:02581": {
        "output_class": "cellular_functional_readout",
        "output_label": "NLGN2-NRXN1beta documented inhibitory-synapse differentiation and receptor clustering",
        "primary_locator": "PMID:18334217; PMID:8576240; PMCID:PMC2826211",
        "citation_note": "Primary studies: PMID:18334217; PMID:8576240; PMCID:PMC2826211; primary locator: PMID:18334217; PMID:8576240; PMCID:PMC2826211",
        "evidence_summary": "Primary neuroligin-neurexin studies show splice-dependent NLGN2/NRXN1beta recognition and demonstrate that beta-neurexin/neuroligin-2 contacts organize inhibitory synaptic specializations, including postsynaptic gephyrin/GABA-receptor clustering and functional synaptic readouts.",
        "assay_or_perturbation": "Neurexin/neuroligin binding and splice-isoform assays, neuron-fibroblast coculture synapse induction, gephyrin/GABA-receptor clustering and miniature inhibitory-postsynaptic-current measurements",
    },
    "M21B-DOWNSTREAM:02582": {
        "output_class": "cellular_functional_readout",
        "output_label": "NLGN3-NRXN1beta documented synaptic adhesion and postsynaptic scaffold coaggregation",
        "primary_locator": "PMID:8576240; PMID:17042500; PMID:17897391",
        "citation_note": "Primary studies: PMID:8576240; PMID:17042500; PMID:17897391; primary locator: PMID:8576240; PMID:17042500; PMID:17897391",
        "evidence_summary": "Primary studies establish splice-dependent NLGN3/beta-neurexin binding and show that neurexin-expressing cells cluster neuroligin-3 together with glutamatergic and GABAergic synaptic scaffold proteins. The annotation records synaptic-organizing output without assuming that every neuroligin-neurexin context is equivalent.",
        "assay_or_perturbation": "NLGN3/beta-neurexin binding and splice comparisons, neurexin-expressing-cell coculture, neuronal clustering and synaptic-scaffold coaggregation assays",
    },
    "M21B-DOWNSTREAM:02767": {
        "output_class": "translocation_or_localization_readout",
        "output_label": "MUC1-Tn-MGL/CLEC10A documented dendritic-cell internalization and HLA-compartment delivery",
        "primary_locator": "PMID:17195076; PMID:17804752",
        "citation_note": "Primary studies: PMID:17195076; PMID:17804752; primary locator: PMID:17195076; PMID:17804752",
        "evidence_summary": "Primary studies identify MGL as the receptor for tumor-associated Tn-MUC1 and show receptor-dependent internalization by immature dendritic cells with delivery of the glycoprotein into HLA class-II, but not class-I, compartments.",
        "assay_or_perturbation": "MGL/MUC1-Tn binding and competition, immature dendritic-cell internalization, confocal localization and subcellular HLA-class-I/class-II compartment assays",
    },
    "M21B-DOWNSTREAM:02821": {
        "output_class": "translocation_or_localization_readout",
        "output_label": "YAP1 pS127-SFN/14-3-3sigma documented cytoplasmic retention and transcriptional attenuation",
        "primary_locator": "PMID:20823509; PMCID:PMC2935210; PMID:12535517",
        "citation_note": "Primary studies: PMID:20823509; PMCID:PMC2935210; PMID:12535517; primary locator: PMID:20823509; PMCID:PMC2935210; PMID:12535517",
        "evidence_summary": "Primary studies show that YAP Ser127 phosphorylation creates a 14-3-3 binding site, promotes cytoplasmic retention and reduces nuclear YAP coactivator function, including attenuation of p73-dependent proapoptotic gene expression.",
        "assay_or_perturbation": "YAP pSer127/14-3-3 binding and structure, Akt/Lats phosphorylation perturbations, subcellular localization and p73/Bax transcriptional-apoptosis assays",
    },
    "M21B-DOWNSTREAM:03014": {
        "output_class": "cellular_functional_readout",
        "output_label": "ICAM1-ITGAX:ITGB2/CR4 documented leukocyte and cell-matrix adhesion interaction",
        "primary_locator": "PMID:16252253; DOI:10.1002/eji.200425914",
        "citation_note": "Primary study: PMID:16252253; DOI:10.1002/eji.200425914; primary locator: PMID:16252253; DOI:10.1002/eji.200425914",
        "evidence_summary": "Primary study maps direct ICAM-1/CD11c-CD18 interaction and frames CD11c/CD18 as an adhesion integrin; ICAM-1 domain and peptide competition experiments define the ligand interface. The annotation retains adhesion output while avoiding a stronger claim about downstream signaling.",
        "assay_or_perturbation": "Purified ICAM-1/CD11c-CD18 binding, monocyte phage-display binding, surface-plasmon resonance, ICAM-1 deletion constructs and peptide competition",
    },
    "M21B-DOWNSTREAM:03062": {
        "output_class": "translocation_or_localization_readout",
        "output_label": "APOE-ApoER2/LRP8 documented ligand-triggered endocytosis and APP/secretase trafficking",
        "primary_locator": "PMID:12950167; DOI:10.1021/bi027093c; PMCID:PMC6672528",
        "citation_note": "Primary studies: PMID:12950167; DOI:10.1021/bi027093c; PMCID:PMC6672528; primary locator: PMID:12950167; DOI:10.1021/bi027093c; PMCID:PMC6672528",
        "evidence_summary": "Primary ApoE/ApoER2 studies establish ApoE particle binding to ApoER2 and show that ApoE engagement triggers ApoER2-dependent endocytosis/redistribution of APP and beta-secretase in neuronal cells, with an amyloidogenic processing output in the tested model.",
        "assay_or_perturbation": "ApoE/ApoER2 binding and isoform assays, ApoE stimulation of neuronal cells, surface/intracellular receptor and APP measurements, endocytosis and amyloid-beta production assays",
    },
    "M21B-DOWNSTREAM:03097": {
        "output_class": "translocation_or_localization_readout",
        "output_label": "FMDV VP1-alphaVbeta3/ITGAV:ITGB3 documented viral attachment and receptor-mediated internalization",
        "primary_locator": "PMID:9343190; PMCID:PMC192296; PMID:7533862",
        "citation_note": "Primary studies: PMID:9343190; PMCID:PMC192296; PMID:7533862; primary locator: PMID:9343190; PMCID:PMC192296; PMID:7533862",
        "evidence_summary": "Primary FMDV studies establish RGD-dependent VP1 binding to alphaVbeta3 and identify alphaVbeta3 as a receptor for FMDV internalization; blocking the vitronectin receptor inhibits viral binding and infection in cultured cells.",
        "assay_or_perturbation": "Purified alphaVbeta3/FMDV binding, RGD/RGE competition, integrin-blocking antibodies, cultured-cell attachment and infection assays",
    },
    "M21B-DOWNSTREAM:03255": {
        "output_class": "cellular_functional_readout",
        "output_label": "NLK-GRP78/HSPA5 documented Akt-linked axonal growth and motor-recovery output",
        "primary_locator": "PMID:30459611; PMCID:PMC6232869; PMID:32547396; PMCID:PMC7273965",
        "citation_note": "Primary studies: PMID:30459611; PMCID:PMC6232869; PMID:32547396; PMCID:PMC7273965; primary locator: PMID:30459611; PMCID:PMC6232869; PMID:32547396; PMCID:PMC7273965",
        "evidence_summary": "Primary studies identify cell-surface GRP78 as an NLK receptor and show that NLK-GRP78 signaling activates Akt, promotes axonal growth, and improves motor recovery after spinal-cord injury; GRP78-neutralizing antibodies suppress the axonal-growth output.",
        "assay_or_perturbation": "NLK/GRP78 binding and immunoprecipitation, GRP78-neutralization, Akt inhibition, cultured-neuron axonal-growth assays and spinal-cord-injury motor-recovery models",
    },
    "M21B-DOWNSTREAM:02345": {
        "output_class": "cellular_functional_readout",
        "output_label": "LAMC2/LAM411-ITGA7:ITGB1 documented laminin-dependent adhesive interaction",
        "primary_locator": "PMID:16413178",
        "citation_note": "Primary study: PMID:16413178; primary locator: PMID:16413178",
        "evidence_summary": "The primary recombinant-integrin survey shows that laminin-411 binds the alpha7X1beta1 integrin variant, although with only modest affinity, and frames these laminin-integrin interactions as the molecular basis of basement-membrane adhesive interactions. The annotation retains this bounded adhesion output and does not infer a downstream signaling relay.",
        "assay_or_perturbation": "Purified recombinant alpha7X1beta1 and laminin-411, solid-phase binding and affinity measurements across a laminin isoform panel",
    },
    "M21B-DOWNSTREAM:02346": {
        "output_class": "cellular_functional_readout",
        "output_label": "LAMC2/LAM421-ITGA7:ITGB1 documented laminin-dependent adhesive interaction",
        "primary_locator": "PMID:16413178",
        "citation_note": "Primary study: PMID:16413178; primary locator: PMID:16413178",
        "evidence_summary": "The primary recombinant-integrin survey shows alpha7X1beta1 binding across the laminin panel, including laminin-421, and frames these laminin-integrin interactions as the molecular basis of basement-membrane adhesive interactions. The annotation retains the isoform-specific adhesion output and does not infer a downstream signaling relay.",
        "assay_or_perturbation": "Purified recombinant alpha7X1beta1 and laminin-421, solid-phase binding and affinity measurements across a laminin isoform panel",
    },
    "M21B-DOWNSTREAM:02631": {
        "output_class": "cellular_functional_readout",
        "output_label": "P2RX2/P2X2-TUBB/beta-tubulin-I documented ATP-gated-channel/cytoskeleton interaction",
        "primary_locator": "PMID:17664027; DOI:10.1016/j.neuint.2007.06.032",
        "citation_note": "Primary study: PMID:17664027; DOI:10.1016/j.neuint.2007.06.032; primary locator: PMID:17664027; DOI:10.1016/j.neuint.2007.06.032",
        "evidence_summary": "The primary study shows that the long P2X2 isoform binds beta-tubulin I directly in biochemical assays and associates with beta-tubulin at the surface in heterologous cells, supporting a functional interaction between an ATP-gated channel and the cytoskeleton. The annotation records that bounded cellular interaction without inferring a complete ATP-dependent signaling cascade.",
        "assay_or_perturbation": "P2X2/P2X2b C-terminal constructs, purified brain tubulin, GST pull-down, co-sedimentation, co-immunoprecipitation, isoform comparison and surface biotinylation in heterologous cells",
    },
    "M21B-DOWNSTREAM:02677": {
        "output_class": "translocation_or_localization_readout",
        "output_label": "CASK-MAGUK/NRXN1-neurexin documented presynaptic active-zone organization and neurexin stability",
        "primary_locator": "PMID:8786425; PMCID:PMC6578772; PMID:27015872; PMCID:PMC4982824",
        "citation_note": "Primary studies: PMID:8786425; PMCID:PMC6578772; PMID:27015872; PMCID:PMC4982824; primary locator: PMID:8786425; PMCID:PMC6578772; PMID:27015872; PMCID:PMC4982824",
        "evidence_summary": "Primary studies establish CASK binding to the neurexin C terminus and show that the CASK-neurexin complex links neurexin to liprin-alpha/Mint1 presynaptic active-zone machinery, modulates neurexin phosphorylation and regulates neurexin stability in neuronal culture. The annotation retains active-zone organization and receptor-stability output without claiming a complete intracellular relay.",
        "assay_or_perturbation": "Neurexin/CASK interaction and deletion mapping, recombinant protein and complex assays, neurexin phosphorylation, neuronal-culture stability measurements and liprin-alpha/Mint1 active-zone complex analysis",
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def suffix(value: str) -> int:
    match = re.search(r"(\d+)$", value)
    return int(match.group(1)) if match else 0


def has_positive_match(text: str, pattern: str) -> bool:
    for match in re.finditer(pattern, text, flags=re.IGNORECASE):
        prefix = text[max(0, match.start() - 35) : match.start()]
        if not re.search(
            r"(?:no|not|without|lack(?:s|ing)?|absence of|failed to|did not|does not)\s+[^.]{0,25}$",
            prefix,
            flags=re.IGNORECASE,
        ):
            return True
    return False


def classify(row: dict[str, str]) -> str:
    text = " ".join(row.get(field, "") for field in ("evidence_summary", "assay_or_perturbation"))
    for output_class, pattern in RULES:
        if has_positive_match(text, pattern):
            return output_class
    return ""


def read_historical_rows(bundle: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(bundle.parent.glob("mechanism_graph_module20_24_v2026_09_21_literature_expansion*/mechanism_literature_expansion.tsv")):
        rows.extend(read_tsv(path))
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--start-queue-suffix", type=int, default=0)
    parser.add_argument(
        "--exclude-queue-id",
        action="append",
        default=[],
        help="Exclude a specific queue record when its language is structural or binding-only.",
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    bundle = args.bundle_dir.resolve()
    queue = read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")
    evidence = read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")
    prior = read_historical_rows(bundle)
    already_curated = {row.get("source_queue_id", "") for row in prior}
    records_by_queue: dict[str, list[dict[str, str]]] = {}
    for record in evidence:
        records_by_queue.setdefault(record["source_queue_id"], []).append(record)

    eligible = []
    for row in queue:
        if row["queue_id"] in already_curated:
            continue
        if row["queue_id"] in set(args.exclude_queue_id):
            continue
        if row.get("output_class") != "unknown":
            continue
        if row.get("evidence_status") != "validated_primary_exact_layer":
            continue
        if row.get("evidence_scope") not in {"direct_edge", "contextual_support", "pathway_membership"}:
            continue
        if not row.get("source_locator") or not row.get("evidence_summary"):
            continue
        if suffix(row["queue_id"]) < args.start_queue_suffix:
            continue
        output_class = CURATION_OVERRIDES.get(row["queue_id"], {}).get("output_class", "") or classify(row)
        if output_class:
            eligible.append((row, output_class))
    eligible.sort(key=lambda item: (item[0].get("curation_priority", "P9"), suffix(item[0]["queue_id"])))
    selected = eligible[: args.limit] if args.limit > 0 else eligible

    counts: dict[str, int] = {}
    for _, output_class in eligible:
        counts[output_class] = counts.get(output_class, 0) + 1
    preview = {
        "eligible_rows": len(eligible),
        "selected_rows": len(selected),
        "eligible_output_classes": dict(sorted(counts.items())),
        "selected_queue_ids": [row["queue_id"] for row, _ in selected],
    }
    if args.dry_run:
        print(json.dumps(preview, indent=2, sort_keys=True))
        return 0

    if not selected:
        raise ValueError("No explicit output-supported unknown records found")

    next_id = max((suffix(row.get("expansion_id", "")) for row in prior), default=0) + 1
    output: list[dict[str, str]] = []
    for index, (row, output_class) in enumerate(selected):
        records = records_by_queue.get(row["queue_id"], [])
        if not records:
            raise ValueError(f"No downstream evidence record for {row['queue_id']}")
        record = records[0]
        evidence_ids = [row["edge_id"], *filter(None, row.get("source_evidence_ids", "").split(";")), record["record_id"], *filter(None, row.get("source_locator", "").split(";"))]
        limitations = row.get("limitations", "").rstrip()
        topology_boundary = "Ligand-receptor topology remains unresolved; output evidence is retained without assigning source or target roles. Output class was assigned from explicit output/readout language in the source-reviewed primary paper or its stored primary-supported summary."
        if topology_boundary not in limitations:
            limitations = f"{limitations} {topology_boundary}".strip()
        expansion = f"M21B-LITEXP-{next_id + index}"
        override = CURATION_OVERRIDES.get(row["queue_id"], {})
        output_class = override.get("output_class", output_class)
        output.append(
            {
                "expansion_id": expansion,
                "source_queue_id": row["queue_id"],
                "route_status": "retained_evidence_route",
                "path_expression": "????>????>????>????>output",
                "route_tier": "downstream_output_annotation_unlinked_topology",
                "known_layers": "output",
                "missing_layers": "ligand_receptor_pair|receptor|intracellular_continuation|transcription_factor",
                "intracellular_status": "not_mapped",
                "ligand_node_id": "",
                "ligand_label": "",
                "ligand_receptor_edge_id": "",
                "receptor_node_id": "",
                "receptor_label": "",
                "transcription_factor_node_id": "",
                "transcription_factor_label": "",
                "target_gene_node_id": "",
                "target_gene_label": "",
                "output_label": override.get("output_label", f"{row['source_label']}-{row['target_label']} documented {output_class}"),
                "pathway_name": row.get("pathway_name", ""),
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_documented_output_unlinked_topology",
                "evidence_ids": ";".join(dict.fromkeys(evidence_ids)),
                "source_chain_id": expansion,
                "source_evidence_record_id": record["record_id"],
                "route_linkage_status": "literature_expansion:output_supported_topology_unresolved",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": row.get("evidence_polarity", "supports"),
                "negative_evidence_status": row.get("negative_evidence_status", "not_evaluated"),
                "evidence_directness": row.get("evidence_directness", "source_claim"),
                "output_class": output_class,
                "primary_locator": override.get("primary_locator", row["source_locator"]),
                "citation_note": override.get("citation_note", row.get("citation_note", "")),
                "evidence_summary": override.get("evidence_summary", row["evidence_summary"]),
                "limitations": limitations,
                "curation_status": "curated_primary_route",
                "species_context": row.get("species_context", ""),
                "cell_type_context": row.get("cell_type_context", ""),
                "assay_or_perturbation": override.get("assay_or_perturbation", row.get("assay_or_perturbation", "")),
                "effect_polarity": row.get("effect_polarity", ""),
                "source_scope": row.get("source_scope", row.get("evidence_scope", "direct_edge")),
            }
        )
    args.output.resolve().write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    preview["output"] = str(args.output.resolve())
    print(json.dumps(preview, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
