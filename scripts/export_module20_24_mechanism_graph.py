#!/usr/bin/env python3
"""Export a conservative Module 20B–24B mechanism graph release.

The local Module 20B–24B registers are the source for this release artifact.
Only edge-register rows marked ``exportable=true`` become graph edges. Every
node label is preserved as curated; composite labels are not silently split.
Narrow, explicit aliases are applied only where they identify the same intact
receptor-complex label. Evidence rows for exported edges remain attached as
source records, including non-exportable boundary evidence so the graph stays
auditable. Gene/product forms and conditional role transitions are exported as
an auxiliary layer; they are not causal graph edges.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULES = ("20", "21", "22", "23", "24")
ROLE_NAMES = ("ligand", "receptor", "transcription_factor", "target_gene", "signaling_cascade")
OUTPUT_BRIDGE_FIELDS = [
    "candidate_id", "review_record_path", "review_source_namespace", "review_evidence_id",
    "source_edge_ids", "review_handoff_ids", "review_status", "tf_entity",
    "target_or_program_label", "target_class", "relation_type", "evidence_layer",
    "stable_citations", "species", "cell_type_model", "assay_or_perturbation",
    "output_evidence_class", "output_language", "output_product_labels", "gene_form_id",
    "product_form_id", "product_form_ids", "transition_id", "transition_ids",
    "traversal_status", "causal_status", "candidate_status", "context_limitations",
]
PRIMARY_ROLE_ORDER = ("ligand", "receptor", "transcription_factor", "target_gene")
LIGAND_RECEPTOR_LAYER_TOKENS = {
    "ligand_receptor_or_direct_molecular",
    "ligand_receptor_binding_or_activation",
}


def has_evidence_layer(layer_value: str, token: str) -> bool:
    """Match one layer token without flattening composite layer values."""
    return any(part.strip().casefold() == token for part in layer_value.split(";"))

# These are deliberately narrow role hints for labels whose role is explicit
# in the Module 20B–24B evidence handoff. Composite labels remain composite;
# the role table records them as a TF or receptor complex without splitting
# them into unsupported entities.
CURATED_ROLE_HINTS = {
    "smad2": ("transcription_factor", "Module 21B TGF-beta-SMAD receptor-proximal relay and nuclear transcriptional relay."),
    "smad3": ("transcription_factor", "Module 21B TGF-beta-SMAD receptor-proximal relay and nuclear transcriptional relay."),
    "smad4": ("transcription_factor", "Module 21B TGF-beta-SMAD SMAD2/3-SMAD4 complex and nuclear relay."),
    "smad2-smad3": ("transcription_factor", "Module 21B TGF-beta-SMAD SMAD2/3 complex."),
    "smad2/3": ("transcription_factor", "Module 22B SMAD2/3 transcriptional signaling program."),
    "smad2/3;smad4": ("transcription_factor", "Module 22B SMAD2/3-SMAD4 transcriptional signaling program."),
    "smad2;smad3": ("transcription_factor", "Module 22B SMAD2/3 transcriptional signaling program."),
    "smad3;smad4": ("transcription_factor", "Module 22B SMAD3-SMAD4 transcriptional signaling program."),
    "smad1/5/8": ("transcription_factor", "Module 22B SMAD1/5/8 transcriptional signaling program."),
    "smad1/5/8;smad4": ("transcription_factor", "Module 22B SMAD1/5/8-SMAD4 transcriptional signaling program."),
    "smad1/5;smad4": ("transcription_factor", "Module 22B SMAD1/5-SMAD4 transcriptional signaling program."),
    "smad1;smad4": ("transcription_factor", "Module 22B SMAD1-SMAD4 transcriptional signaling program."),
    "tgfbr1-tgfbr2 receptor complex": ("receptor", "Module 21B TGF-beta-SMAD receptor-proximal relay."),
}

# Explicit, chain-critical label aliases. These aliases normalize formatting or
# an unambiguous synonym for the same intact receptor complex; they do not
# split composite entities or merge distinct receptor subunits/configurations.
# Keys and values are the exact whitespace-normalized/case-folded forms used by
# node_key(). Keep this list narrow and auditable.
CANONICAL_NODE_ALIASES = {
    "tgfbr1-tgfbr2 receptor complex": "tgfbr1-tgfbr2 receptor complex",
    "tgfbr1:tgfbr2 receptor complex": "tgfbr1-tgfbr2 receptor complex",
    "tgfbr1:tgfbr2": "tgfbr1-tgfbr2 receptor complex",
    "tgfbr1_tgfbr2": "tgfbr1-tgfbr2 receptor complex",
    "cntfr-alpha-gp130-lifr receptor complex": "cntfr-alpha-gp130-lifr receptor complex",
    "cntf:cntfra:gp130:lifr receptor complex": "cntfr-alpha-gp130-lifr receptor complex",
    "ifnlr1-il10rb receptor complex": "ifnlr1-il10rb receptor complex",
    "ifnlr1:il10rb receptor complex": "ifnlr1-il10rb receptor complex",
}

CANONICAL_NODE_LABELS = {
    "tgfbr1-tgfbr2 receptor complex": "TGFBR1-TGFBR2 receptor complex",
    "cntfr-alpha-gp130-lifr receptor complex": "CNTFR-alpha-gp130-LIFR receptor complex",
    "ifnlr1-il10rb receptor complex": "IFNLR1-IL10RB receptor complex",
}

# This is intentionally a label-level mapping, not a causal or secretion
# assertion. The current registers use both ``Il6`` for a target-gene/role
# label and ``IL-6`` for a ligand label. They must remain separate graph nodes
# while still being available for a manually validated intercellular bridge.
EXPLICIT_GENE_PRODUCT_MAPPINGS = (
    {
        "gene_key": "il6",
        "protein_key": "il-6",
        "notes": (
            "Explicit register-label mapping between the IL6 target-gene form "
            "and the IL-6 ligand form; this does not assert transcription, "
            "translation, secretion, transport, or receptor activation."
        ),
    },
    {
        "gene_key": "il6 inflammatory target gene",
        "protein_key": "il-6",
        "notes": (
            "Explicit register-label mapping from the IL6 inflammatory "
            "target-gene label to the IL-6 ligand form; this does not assert "
            "transcription, translation, secretion, transport, or receptor activation."
        ),
    },
    {
        "gene_key": "bdnf promoter iv",
        "protein_key": "bdnf",
        "notes": (
            "Explicit mapping from the Bdnf promoter-IV target-gene label to "
            "the BDNF ligand form; this does not assert expression, translation, "
            "secretion, transport, or receptor activation."
        ),
    },
    {
        "gene_key": "il1b (pro-il-1β)",
        "protein_key": "il1b",
        "notes": (
            "Explicit mapping from the IL1B/pro-IL-1β target-gene label to "
            "the IL-1β ligand form; maturation, secretion, transport, and "
            "receptor activation remain conditional on output evidence."
        ),
    },
    {
        "gene_key": "tgfb1 promoter",
        "protein_key": "tgfb1",
        "notes": (
            "Explicit mapping from the Tgfb1 promoter target-gene label to "
            "the TGFB1 ligand form; this does not assert expression, latent "
            "complex processing, secretion, activation, or receptor binding."
        ),
    },
    {
        "gene_key": "shh macs1 long-range enhancer",
        "protein_key": "shh",
        "notes": (
            "Explicit mapping from the Shh MACS1 enhancer target-gene label "
            "to the SHH ligand form; this does not assert expression, processing, "
            "secretion, transport, or receptor activation."
        ),
    },
)

# These are measured protein products that are not exported as ligand-role
# nodes.  They receive a separate form type so an output observation can be
# traversed as a protein product without silently making the canonical node a
# ligand or asserting receptor activity.  Each form is useful only when a
# validated output bridge supplies the corresponding protein-level evidence.
CURATED_OUTPUT_PRODUCT_FORMS = (
    {
        "node_key": "adamts9",
        "canonical_name": "ADAMTS9",
        "notes": "Curated output-protein form for primary-backed ADAMTS9 release measurements; this form does not assert a ligand role or receptor activity.",
    },
    {
        "node_key": "reg3g",
        "canonical_name": "Reg3gamma",
        "notes": "Curated output-protein form for primary-backed Reg3gamma production measurements; this form does not assert a ligand role or receptor activity.",
    },
    {
        "node_key": "opg/tnfrsf11b",
        "canonical_name": "OPG/TNFRSF11B",
        "notes": "Curated output-protein form for primary-backed soluble OPG secretion measurements; this form does not assert a receptor role or intracellular signaling.",
    },
    {
        "node_key": "neural-progenitor-derived 4931414p19rik/p19",
        "canonical_name": "P19",
        "notes": "Curated output-protein form for primary-backed neural-progenitor P19 secretion measurements; this form does not assert a receptor identity.",
    },
    {
        "node_key": "gja1/cx43",
        "canonical_name": "GJA1/Cx43",
        "notes": "Curated output-protein form for primary-backed GJA1/Cx43 protein measurements; this form does not assert secretion or ligand activity.",
    },
    {
        "node_key": "hmox1",
        "canonical_name": "HMOX1/HO-1",
        "notes": "Curated output-protein form for primary-backed HMOX1/HO-1 protein measurements; this form does not assert secretion or ligand activity.",
    },
    {
        "node_key": "uchl1/uch-l1",
        "canonical_name": "UCHL1/UCH-L1",
        "notes": "Curated output-protein form for primary-backed UCHL1 protein measurements; this form does not assert secretion or ligand activity.",
    },
    {
        "node_key": "lama5",
        "canonical_name": "LAMA5",
        "notes": "Curated output-protein form for primary-backed LAMA5 RNA/protein output measurements; this form does not assert secretion or ligand activity.",
    },
    {
        "node_key": "col1a2",
        "canonical_name": "COL1A2",
        "notes": "Curated output-protein form for primary-backed collagen-I production/expression measurements; this form does not assert mature fibril assembly or secretion.",
    },
    {
        "node_key": "col3a1",
        "canonical_name": "COL3A1",
        "notes": "Curated output-protein form for primary-backed collagen-III production/expression measurements; this form does not assert mature fibril assembly or secretion.",
    },
    {
        "node_key": "mmp2",
        "canonical_name": "MMP2",
        "notes": "Curated output-protein form for primary-backed MMP2 activity/expression measurements; this form does not assert a particular precursor-processing or secretion step.",
    },
    {
        "node_key": "mmp9/matrix metalloproteinase-9",
        "canonical_name": "MMP9",
        "notes": "Curated output-protein form for primary-backed MMP9 activity/expression measurements; this form does not assert a particular precursor-processing or secretion step.",
    },
    {
        "node_key": "sdc1 ectodomain; itga2:itgb1 context",
        "canonical_name": "SDC1 ectodomain",
        "notes": "Curated output-protein form for primary-backed shed SDC1 ectodomain measurements; this is a cleavage/shedding product, not de novo SDC1 synthesis or a ligand-role assertion.",
    },
    {
        "node_key": "acan/aggrecan",
        "canonical_name": "ACAN/aggrecan",
        "notes": "Curated output-protein form for primary-backed aggrecan/ECM output measurements; this form does not assert a complete transcript-to-proteoglycan-processing or secretion sequence.",
    },
    {
        "node_key": "ncan",
        "canonical_name": "NCAN/neurocan",
        "notes": "Curated output-protein form for primary-backed neurocan/ECM output measurements; this form does not assert a complete transcript-to-proteoglycan-processing or secretion sequence.",
    },
    {
        "node_key": "acsl4",
        "canonical_name": "ACSL4",
        "notes": "Curated output-protein form for primary-backed ACSL4 protein/pathway output measurements; this form does not assert S1PR2-to-ACSL4 direct binding, transcription, or secretion.",
    },
    {
        "node_key": "cyp11b2",
        "canonical_name": "CYP11B2",
        "notes": "Curated output-protein form for primary-backed CYP11B2 protein-localization measurements; this form does not assert Cyp11b2 transcription, secretion, or direct mineralocorticoid-receptor binding.",
    },
    {
        "node_key": "nlrp3",
        "canonical_name": "NLRP3",
        "notes": "Curated output-protein form for primary-backed NLRP3 mRNA/protein output measurements; this form does not assert extracellular NLRP3 secretion, inflammasome assembly, or a direct upstream receptor mechanism.",
    },
    {
        "node_key": "prommp2:timp2 complex",
        "canonical_name": "proMMP2:TIMP2 complex",
        "notes": "Curated output-protein form for primary-backed proMMP2:TIMP2 secretion/activation measurements; this preserves the precursor/inhibitor complex and does not assert free mature MMP2 release.",
    },
    {
        "node_id": "NODE01123",
        "canonical_name": "CCL2",
        "notes": "Curated output-protein form for primary-backed CCL2 cargo in astrocyte-derived extracellular-vesicle release; this form does not assert free chemokine secretion, transcription, or purified receptor binding.",
    },
    {
        "node_key": "fth1/h-ferritin",
        "canonical_name": "FTH1/H-ferritin",
        "notes": "Curated output-protein form for primary-backed H-ferritin-containing exosome export; this form does not assert FTH1 transcription, direct PROM2 binding, or free extracellular ferritin.",
    },
    {
        "node_key": "ftl/l-ferritin",
        "canonical_name": "FTL/L-ferritin",
        "notes": "Curated output-protein form for primary-backed L-ferritin-containing exosome export; this form does not assert FTL transcription, direct PROM2 binding, or free extracellular ferritin.",
    },
    {
        "node_key": "ctsb/cathepsin b",
        "canonical_name": "CTSB/cathepsin B",
        "notes": "Curated output-protein form for primary-backed lysosomal cathepsin-B release after MLKL-associated permeabilization; this form does not assert Ctsb transcription or de novo protein production.",
    },
    {
        "node_id": "NODE01950",
        "canonical_name": "CYCS/cytochrome c",
        "notes": "Curated output-protein form for primary-backed mitochondrial intermembrane-space cytochrome-c release downstream of BAX/BAK pore formation; this form does not assert secretion or receptor activity.",
    },
    {
        "node_id": "NODE05282",
        "canonical_name": "MIF",
        "notes": "Curated output-protein form for primary-backed measured MIF protein production in astrocyte and other cellular-output contexts; this form does not assert transcription, secretion mechanism, receptor activation, or a universal intracellular route.",
    },
    {
        "node_id": "NODE01421",
        "canonical_name": "CDH2/N-cadherin",
        "notes": "Curated output-protein form for primary-backed N-cadherin protein or histologic marker measurements in adhesion and astrocyte-state contexts; this form does not assert secretion, a unidirectional ligand role, or a complete transcriptional mechanism.",
    },
    {
        "node_id": "NODE02091",
        "canonical_name": "DLL4/Delta-like ligand 4",
        "notes": "Curated output-protein form for primary-backed DLL4 protein measurements in endothelial and Notch-context outputs; this form does not assert transcription, membrane presentation, receptor activation, or a secretory mechanism.",
    },
    {
        "node_id": "NODE01843",
        "canonical_name": "CSPG4/NG2",
        "notes": "Curated output-protein form for primary-backed CSPG4/NG2 protein or immunohistochemical measurements in glial-scar and extracellular-matrix contexts; this form does not assert shedding, secretion, receptor activity, or a complete transcript-to-proteoglycan mechanism.",
    },
    {
        "node_id": "NODE01956",
        "canonical_name": "CYP19A1",
        "notes": "Curated output-protein form for primary-backed CYP19A1/aromatase protein measurements; this form does not assert transcription-to-translation order, secretion, or steroid-product release.",
    },
    {
        "node_id": "NODE03778",
        "canonical_name": "ID3",
        "notes": "Curated output-protein form for primary-backed ID3 protein measurements; this form does not assert secretion or a universal upstream transcriptional mechanism.",
    },
    {
        "node_id": "NODE03404",
        "canonical_name": "GRIA4",
        "notes": "Curated output-protein form for primary-backed GRIA4/GluA4 protein measurements; this form does not assert secretion, receptor assembly, or synaptic trafficking.",
    },
    {
        "node_id": "NODE01849",
        "canonical_name": "CTGF",
        "notes": "Curated output-protein form for primary-backed CTGF protein measurements; this form does not assert secretion, matrix incorporation, or a direct upstream transcription-factor binding event.",
    },
    {
        "node_id": "NODE08294",
        "canonical_name": "TXNIP",
        "notes": "Curated output-protein form for primary-backed TXNIP protein measurements; this form does not assert extracellular release, inflammasome assembly, or a direct upstream receptor mechanism.",
    },
    {
        "node_id": "NODE02810",
        "canonical_name": "FOS",
        "notes": "Curated output-protein form for primary-backed FOS/c-FOS protein or immunostaining measurements; this form does not assert secretion or a universal terminal-transcription mechanism.",
    },
    {
        "node_id": "NODE05511",
        "canonical_name": "NEDD4L-short",
        "notes": "Curated output-protein form for primary-backed NEDD4L-short protein measurements; this form does not assert secretion, ubiquitin-ligase activity, or a complete promoter-to-protein mechanism.",
    },
    {
        "node_id": "NODE04378",
        "canonical_name": "ITGB3",
        "notes": "Curated output-protein form for primary-backed ITGB3/integrin-beta-3 protein measurements; this form does not assert autonomous receptor activity, heterodimer composition, or secretion.",
    },
    {
        "node_id": "NODE01181",
        "canonical_name": "CCND1",
        "notes": "Curated output-protein form for primary-backed CCND1/cyclin-D1 protein measurements; this form does not assert secretion or a universal upstream transcriptional mechanism.",
    },
    {
        "node_id": "NODE08673",
        "canonical_name": "ZMAT3",
        "notes": "Curated output-protein form for primary-backed ZMAT3/Wig-1 protein induction measurements; this form does not assert secretion or a complete p53-to-protein mechanism.",
    },
    {
        "node_id": "NODE08190",
        "canonical_name": "TREM2",
        "notes": "Curated output-protein form for primary-backed TREM2 protein immunostaining or quantification; this form does not assert secretion, ligand binding, or a complete receptor-signaling mechanism.",
    },
    {
        "node_id": "NODE04122",
        "canonical_name": "IRF5",
        "notes": "Curated output-protein form for primary-backed IRF5 mRNA/protein measurements in the ischemia-reperfusion microglial polarization context; this form does not assert secretion or a universal upstream mechanism.",
    },
    {
        "node_id": "NODE00752",
        "canonical_name": "BCL2L11/BIM",
        "notes": "Curated output-protein form for primary-backed BIM protein measurements in neuronal-injury assays; this form does not assert secretion or a complete apoptotic mechanism.",
    },
    {
        "node_id": "NODE06180",
        "canonical_name": "PARP1/PARP-1",
        "notes": "Curated output-protein form for primary-backed PARP1 cleavage measurements in neuronal-injury assays; this form does not assert secretion or a complete caspase mechanism.",
    },
    {
        "node_id": "NODE00611",
        "canonical_name": "AQP4 (IL-1β/HMGB1/ATP astrocyte context)",
        "notes": "Curated output-protein form for primary-backed AQP4 mRNA/protein measurements in the IL-1β/HMGB1/ATP astrocyte context; this form does not assert a universal AQP4 induction mechanism or intercellular transport.",
    },
    {
        "node_id": "NODE00612",
        "canonical_name": "AQP4 (IL-6/TBI astrocyte context)",
        "notes": "Curated output-protein form for primary-backed AQP4 mRNA/protein measurements in the IL-6/TBI astrocyte context; this form does not assert a universal AQP4 induction mechanism or intercellular transport.",
    },
    {
        "node_id": "NODE03873",
        "canonical_name": "IL-6",
        "notes": "Curated output-protein form for primary-backed measured IL-6 release in cytokine-output and cross-cell conditioned-medium contexts; this form does not assert IL6 transcription, secretion mechanism, or receptor activation.",
    },
    {
        "node_id": "NODE04051",
        "canonical_name": "Il6",
        "notes": "Curated output-protein form for primary-backed measured Il6/IL-6 protein release or secretion on the target-gene/ligand node; this form does not assert transcription-to-translation order or receptor activation.",
    },
    {
        "node_id": "NODE03948",
        "canonical_name": "Il1b",
        "notes": "Curated output-protein form for primary-backed measured IL-1β release, secretion, or mature-cytokine output; this form preserves pro-IL-1β processing/inflammasome context and does not assert a direct receptor-to-cytokine mechanism.",
    },
    {
        "node_id": "NODE08072",
        "canonical_name": "TNF",
        "notes": "Curated output-protein form for primary-backed measured TNF release or secretion; this form does not assert TNF transcription, processing mechanism, or receptor activation.",
    },
    {
        "node_id": "NODE01922",
        "canonical_name": "CXCL8/IL-8",
        "notes": "Curated output-protein form for primary-backed measured CXCL8/IL-8 release or secretion; this form does not assert transcription, processing, or receptor activation.",
    },
    {
        "node_id": "NODE01886",
        "canonical_name": "Cxcl10",
        "notes": "Curated output-protein form for primary-backed measured CXCL10 release; this form does not assert transcription, processing, or receptor activation and preserves the exact Cxcl10 node identity.",
    },
    {
        "node_id": "NODE01889",
        "canonical_name": "CXCL10/IP-10",
        "notes": "Curated output-protein form for primary-backed measured CXCL10/IP-10 release; this form preserves the recorded chemokine nomenclature and does not assert transcription or receptor activation.",
    },
    {
        "node_id": "NODE01893",
        "canonical_name": "Cxcl12",
        "notes": "Curated output-protein form for primary-backed measured CXCL12 release; this form does not assert transcription, chemokine oligomer state, or receptor activation.",
    },
    {
        "node_id": "NODE01811",
        "canonical_name": "Csf2",
        "notes": "Curated output-protein form for primary-backed measured GM-CSF/CSF2 secreted-mediator output; this form does not assert transcription, processing, or receptor activation.",
    },
    {
        "node_id": "NODE03802",
        "canonical_name": "Ifng",
        "notes": "Curated output-protein form for primary-backed measured IFN-γ release or secretion; this form does not assert IFNG transcription, antiviral mechanism, or receptor activation.",
    },
    {
        "node_id": "NODE03919",
        "canonical_name": "IL17A",
        "notes": "Curated output-protein form for primary-backed measured IL-17A cytokine output or secretion; this form does not assert transcription, processing, receptor activation, or assignment to a particular producing-cell program.",
    },
    {
        "node_id": "NODE03977",
        "canonical_name": "Il2",
        "notes": "Curated output-protein form for primary-backed measured IL-2 secretion or cytokine output; this form does not assert transcription, receptor activation, or a universal T-cell costimulation route.",
    },
    {
        "node_id": "NODE04063",
        "canonical_name": "Il9",
        "notes": "Curated output-protein form for primary-backed measured IL-9 cytokine output; this form does not assert transcription, receptor activation, or a universal Th9/ILC2 source.",
    },
    {
        "node_id": "NODE00767",
        "canonical_name": "Bdnf",
        "notes": "Curated output-protein form for primary-backed measured BDNF release or secretion; this form does not assert Bdnf transcription, processing, or TrkB activation.",
    },
    {
        "node_id": "NODE05632",
        "canonical_name": "Ngf",
        "notes": "Curated output-protein form for primary-backed measured NGF production/release; this form does not assert NGF maturation, secretion mechanism, or receptor activation.",
    },
    {
        "node_id": "NODE01164",
        "canonical_name": "Ccl5",
        "notes": "Curated output-protein form for primary-backed measured CCL5/RANTES release or secretion; this form does not assert transcription or receptor activation.",
    },
    {
        "node_id": "NODE01157",
        "canonical_name": "Ccl3",
        "notes": "Curated output-protein form for primary-backed measured CCL3/MIP-1α release or secretion; this form does not assert transcription or receptor activation.",
    },
    {
        "node_id": "NODE03893",
        "canonical_name": "IL12A/IL12B",
        "notes": "Curated output-protein form for primary-backed measured IL-12 heterodimer/p70 release or secretion; preserve the IL12A/IL12B product composition and do not assert either subunit alone as the secreted cytokine.",
    },
    {
        "node_id": "NODE03894",
        "canonical_name": "Il12a_Il12b",
        "notes": "Curated output-protein form for primary-backed measured IL-12A/IL-12B heterodimer output; this form preserves the composite cytokine topology and does not assert independent subunit secretion.",
    },
    {
        "node_id": "NODE03798",
        "canonical_name": "Ifnb1",
        "notes": "Curated output-protein form for primary-backed measured IFN-β production or secretion; this form does not assert IFNB1 transcription, antiviral mechanism, or receptor activation.",
    },
    {
        "node_id": "NODE03863",
        "canonical_name": "IL-1alpha",
        "notes": "Curated output-protein form for primary-backed measured IL-1α release; this form preserves injury/inflammasome context and does not assert transcription or receptor activation.",
    },
    {
        "node_id": "NODE03944",
        "canonical_name": "Il1a",
        "notes": "Curated output-protein form for primary-backed measured Il1a/IL-1α release; this form does not assert transcription, processing, or receptor activation.",
    },
    {
        "node_id": "NODE01883",
        "canonical_name": "CXCL1",
        "notes": "Curated output-protein form for primary-backed measured CXCL1/GRO/CINC-1 release or secretion; this form does not assert transcription or receptor activation.",
    },
    {
        "node_id": "NODE01908",
        "canonical_name": "Cxcl2",
        "notes": "Curated output-protein form for primary-backed measured CXCL2/MIP-2 release or secretion; this form does not assert transcription or receptor activation.",
    },
    {
        "node_id": "NODE04038",
        "canonical_name": "Il4",
        "notes": "Curated output-protein form for primary-backed measured IL-4 cytokine output or secretion; this form does not assert transcription or receptor activation.",
    },
    {
        "node_id": "NODE04049",
        "canonical_name": "Il5",
        "notes": "Curated output-protein form for primary-backed measured IL-5 cytokine output or secretion; this form does not assert transcription or receptor activation.",
    },
    {
        "node_id": "NODE03907",
        "canonical_name": "Il13",
        "notes": "Curated output-protein form for primary-backed measured IL-13 cytokine output or secretion; this form does not assert transcription or receptor activation.",
    },
    {
        "node_id": "NODE08457",
        "canonical_name": "Vegfa",
        "notes": "Curated output-protein form for primary-backed measured VEGF-A secretion; this form does not assert VEGFA transcription, isoform identity, or receptor activation.",
    },
    {
        "node_id": "NODE01923",
        "canonical_name": "CXCL9",
        "notes": "Curated output-protein form for primary-backed measured CXCL9/MIG release; this form does not assert transcription or receptor activation.",
    },
    {
        "node_id": "NODE01924",
        "canonical_name": "CXCL9/MIG",
        "notes": "Curated output-protein form for primary-backed measured CXCL9/MIG release; this form preserves the recorded chemokine label and does not assert transcription or receptor activation.",
    },
    {
        "node_id": "NODE02673",
        "canonical_name": "Fgf2",
        "notes": "Curated output-protein form for primary-backed measured astrocytic FGF2 production/release; this form does not assert a CNTF receptor-to-FGF2 transcription or secretion mechanism.",
    },
    {
        "node_id": "NODE07860",
        "canonical_name": "Tgfb1",
        "notes": "Curated output-protein form for primary-backed measured TGF-β1 release; preserve latent-complex/activation uncertainty and do not assert mature active ligand availability or receptor activation.",
    },
    {
        "node_id": "NODE00176",
        "canonical_name": "ADAMTS1",
        "notes": "Curated output-protein form for primary-backed measured ADAMTS1 release; this form does not assert protease maturation, substrate cleavage, or receptor activity.",
    },
    {
        "node_id": "NODE08531",
        "canonical_name": "Vwf",
        "notes": "Curated output-protein form for primary-backed measured VWF secretion; this form does not assert multimerization or downstream receptor activity.",
    },
    {
        "node_id": "NODE05790",
        "canonical_name": "Nptx1",
        "notes": "Curated output-protein form for primary-backed measured NPTX1/NP1 release; this form does not assert processing, receptor activity, or synaptic sufficiency.",
    },
    {
        "node_id": "NODE03934",
        "canonical_name": "Il18",
        "notes": "Curated output-protein form for primary-backed measured IL-18 release; preserve precursor processing/inflammasome context and do not assert transcription or receptor activation.",
    },
    {
        "node_id": "NODE03586",
        "canonical_name": "Hgf",
        "notes": "Curated output-protein form for primary-backed measured microglial HGF secretion; this form does not assert the upstream TGF-β-to-HGF transcriptional step or MET activation.",
    },
    {
        "node_id": "NODE02652",
        "canonical_name": "Fgf10",
        "notes": "Curated output-protein form for primary-backed release of pre-existing matrix-bound FGF10; preserve perlecan-heparan-sulfate presentation and heparanase dependence, without asserting de novo synthesis or receptor activation.",
    },
    {
        "node_id": "NODE07871",
        "canonical_name": "Tgfb3",
        "notes": "Curated output-protein form for primary-backed activation/release of latent TGFB3; preserve the LAP3-containing latent complex and alphaVbeta6 requirement, without asserting TGFB3 transcription or de novo secretion.",
    },
    {
        "node_id": "NODE07330",
        "canonical_name": "Shh",
        "notes": "Curated output-protein form for primary-backed SHH release or receptor handoff; this form does not assert SHH processing, transport, or receptor activation.",
    },
    {
        "node_id": "NODE00089",
        "canonical_name": "ACTH",
        "notes": "Curated output-protein/peptide form for primary-backed ACTH release; this form does not assert POMC processing details or receptor activation.",
    },
    {
        "node_id": "NODE06589",
        "canonical_name": "Prolactin",
        "notes": "Curated output-protein form for primary-backed prolactin secretion; this form does not assert transcriptional control or prolactin-receptor activation.",
    },
    {
        "node_id": "NODE04102",
        "canonical_name": "Insulin",
        "notes": "Curated output-protein form for primary-backed insulin secretion; preserve precursor processing and glucose-dependent secretory context, without asserting receptor activation.",
    },
    {
        "node_id": "NODE01179",
        "canonical_name": "CCN3/NOV",
        "notes": "Curated output-protein form for primary-backed CCN3/NOV protein in Treg-conditioned medium and depletion/rescue assays; this form does not assert a receptor identity or universal secretion mechanism.",
    },
    {
        "node_id": "NODE04561",
        "canonical_name": "KPI-containing secreted APP/APPs770",
        "notes": "Curated output-protein form for primary-backed secreted KPI-containing APPs770 uptake/clearance; preserve the APP isoform and LRP1/RAP-sensitive endocytic context, without asserting kinase signaling.",
    },
    {
        "node_id": "NODE06675",
        "canonical_name": "Ptn",
        "notes": "Curated output-protein form for primary-backed pericyte PTN protein abundance and rescue measurements; this form does not assert a secretion mechanism or identify the neuronal receptor.",
    },
    {
        "node_id": "NODE06184",
        "canonical_name": "PCB/pyruvate carboxylase",
        "notes": "Curated output-protein form for primary-backed PCB/pyruvate-carboxylase mRNA and protein measurements; this form does not assert secretion or a new ligand role.",
    },
    {
        "node_id": "NODE04960",
        "canonical_name": "MAG/myelin-associated glycoprotein",
        "notes": "Curated output-protein form for primary-backed MAG protein measurements downstream of TNR-associated oligodendrocyte differentiation; this form does not assert secretion or receptor activity.",
    },
    {
        "node_id": "NODE02793",
        "canonical_name": "FMRP",
        "notes": "Curated output-protein form for primary-backed FMRP immunoblot measurements downstream of GABA-B/CREB-associated Fmr1 regulation; this form does not assert secretion or a receptor role.",
    },
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "data" / "processed" / "mechanism_graph_module20_24_v2026_09_01",
        help="Directory for the release bundle.",
    )
    parser.add_argument(
        "--source-root",
        type=Path,
        default=ROOT / "work" / "module_b_consolidation",
        help="Directory containing module20b–module24b register directories.",
    )
    parser.add_argument(
        "--module20b-family-layer",
        type=Path,
        default=ROOT / "data" / "processed" / "module20b_pathway_family_layer_v1" / "module20b_pathway_family_layer.tsv",
        help="Optional conservative Module 20B receptor-family grouping layer.",
    )
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            delimiter="\t",
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def split_ids(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def node_key(label: str) -> str:
    normalized = unicodedata.normalize("NFKC", label).strip()
    key = " ".join(normalized.split()).casefold()
    return CANONICAL_NODE_ALIASES.get(key, key)


def canonical_node_label(label: str) -> str:
    """Return the stable display label for an explicit node alias group."""
    return CANONICAL_NODE_LABELS.get(node_key(label), label.strip())


def node_alias_metadata() -> dict[str, list[str]]:
    """Return display-label aliases for release provenance."""
    grouped: dict[str, list[str]] = defaultdict(list)
    for alias, canonical in CANONICAL_NODE_ALIASES.items():
        grouped[CANONICAL_NODE_LABELS.get(canonical, canonical)].append(alias)
    return {canonical: sorted(aliases) for canonical, aliases in sorted(grouped.items())}


def is_self_loop(edge: dict[str, str]) -> bool:
    return node_key(edge.get("source_entity", "")) == node_key(edge.get("target_entity", ""))


def add_role(
    role_map: dict[str, dict[str, dict[str, set[str]]]],
    node_id: str,
    role: str,
    role_source: str,
    role_evidence: str,
) -> None:
    if role not in ROLE_NAMES:
        raise ValueError(f"Unsupported mechanism node role: {role}")
    entry = role_map.setdefault(node_id, {}).setdefault(
        role,
        {"sources": set(), "evidence": set()},
    )
    entry["sources"].add(role_source)
    entry["evidence"].add(role_evidence)


def primary_node_type(roles: set[str]) -> str:
    for role in PRIMARY_ROLE_ORDER:
        if role in roles:
            return role
    # mSCS uses node_type for legacy feature typing. Keep the many-to-many
    # signaling_cascade role in mechanism_node_roles.tsv, but use the
    # recognized legacy fallback for generic relay/complex/program nodes.
    return "signaling_effector"


def safe_gene_symbol(label: str, roles: set[str]) -> str:
    """Keep only simple role-bearing labels as gene symbols.

    Composite labels, pathway names, and phenotype/program labels remain
    addressable through canonical_name but are not silently converted into a
    gene symbol.
    """
    if not roles.intersection({"ligand", "receptor", "transcription_factor", "target_gene"}):
        return ""
    normalized = label.strip()
    if re.fullmatch(r"[A-Za-z][A-Za-z0-9-]{1,31}", normalized):
        return normalized
    return ""


def build_entity_forms(
    node_rows: list[dict[str, object]],
    role_map: dict[str, dict[str, dict[str, set[str]]]],
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    """Export typed gene/product forms without changing canonical graph nodes.

    A canonical node may legitimately carry both ``target_gene`` and
    ``ligand`` roles. Those roles are represented as distinct forms so a
    target-gene observation does not silently become a secreted ligand. The
    transitions are conditional metadata and never enter ``mechanism_edges``.
    """
    labels_by_node = {str(row["node_id"]): str(row["canonical_name"]) for row in node_rows}
    node_id_by_key = {node_key(label): node_id for node_id, label in labels_by_node.items()}
    forms: list[dict[str, object]] = []
    form_by_node_and_type: dict[tuple[str, str], str] = {}
    for node_id in sorted(role_map):
        roles = set(role_map[node_id])
        label = labels_by_node[node_id]
        if "target_gene" in roles:
            form_id = f"GENE:{node_id}"
            form_by_node_and_type[(node_id, "gene")] = form_id
            forms.append(
                {
                    "entity_form_id": form_id,
                    "node_id": node_id,
                    "form_type": "gene",
                    "canonical_name": label,
                    "source_role": "target_gene",
                    "form_status": "role_derived",
                    "notes": "Target-gene form derived from an exported target_gene role; expression is not asserted by this form record.",
                }
            )
        if "ligand" in roles:
            form_id = f"PROTEIN:{node_id}"
            form_by_node_and_type[(node_id, "protein_ligand")] = form_id
            forms.append(
                {
                    "entity_form_id": form_id,
                    "node_id": node_id,
                    "form_type": "protein_ligand",
                    "canonical_name": label,
                    "source_role": "ligand",
                    "form_status": "role_derived",
                    "notes": "Ligand/protein form derived from an exported ligand role; secretion is not asserted by this form record.",
                }
            )

    for mapping in CURATED_OUTPUT_PRODUCT_FORMS:
        node_id = mapping.get("node_id") or node_id_by_key.get(node_key(mapping.get("node_key", "")))
        if not node_id:
            continue
        forms.append(
            {
                "entity_form_id": f"OUTPUT_PROTEIN:{node_id}",
                "node_id": node_id,
                "form_type": "protein_output",
                "canonical_name": mapping["canonical_name"],
                "source_role": "validated_output_product",
                "form_status": "curated_output_product",
                "notes": mapping["notes"],
            }
        )

    transitions: list[dict[str, object]] = []

    # Same-node role co-occurrence is the safest correspondence available from
    # the graph alone. It is explicitly conditional on output/secretion
    # evidence and therefore cannot create an intercellular path by itself.
    for node_id in sorted(role_map):
        if "target_gene" not in role_map[node_id] or "ligand" not in role_map[node_id]:
            continue
        gene_form = form_by_node_and_type[(node_id, "gene")]
        protein_form = form_by_node_and_type[(node_id, "protein_ligand")]
        transitions.append(
            {
                "transition_id": f"TRN:{len(transitions) + 1:05d}",
                "source_form_id": gene_form,
                "target_form_id": protein_form,
                "source_node_id": node_id,
                "target_node_id": node_id,
                "source_form_type": "gene",
                "target_form_type": "protein_ligand",
                "transition_type": "gene_product_correspondence",
                "relation_type": "gene_to_ligand_identity",
                "traversal_status": "requires_output_evidence",
                "causal_status": "not_asserted",
                "evidence_status": "role_cooccurrence_only",
                "source_label": labels_by_node[node_id],
                "target_label": labels_by_node[node_id],
                "evidence_ids": "",
                "notes": "Same canonical node has both roles; this transition does not assert transcription, translation, secretion, transport, or receptor activation.",
            }
        )

    # Keep known punctuation/formatting differences separate in the graph and
    # expose only an auditable identity candidate for later manual review.
    transition_count = len(transitions)
    node_id_by_key = {
        " ".join(unicoded.split()).casefold(): str(row["node_id"])
        for row in node_rows
        for unicoded in [str(row["canonical_name"])]
    }
    for mapping in EXPLICIT_GENE_PRODUCT_MAPPINGS:
        gene_node_id = node_id_by_key.get(mapping["gene_key"])
        protein_node_id = node_id_by_key.get(mapping["protein_key"])
        if not gene_node_id or not protein_node_id:
            continue
        gene_form = form_by_node_and_type.get((gene_node_id, "gene"))
        protein_form = form_by_node_and_type.get((protein_node_id, "protein_ligand"))
        if not gene_form or not protein_form:
            continue
        transition_count += 1
        transitions.append(
            {
                "transition_id": f"TRN:{transition_count:05d}",
                "source_form_id": gene_form,
                "target_form_id": protein_form,
                "source_node_id": gene_node_id,
                "target_node_id": protein_node_id,
                "source_form_type": "gene",
                "target_form_type": "protein_ligand",
                "transition_type": "gene_product_correspondence",
                "relation_type": "gene_to_ligand_identity",
                "traversal_status": "requires_secretion_evidence",
                "causal_status": "not_asserted",
                "evidence_status": "explicit_label_mapping",
                "source_label": labels_by_node[gene_node_id],
                "target_label": labels_by_node[protein_node_id],
                "evidence_ids": "",
                "notes": mapping["notes"],
            }
        )
    return forms, transitions


def source_files(source_root: Path, module: str) -> tuple[Path, Path]:
    directory = source_root / f"module{module}b"
    return (
        directory / f"module{module}b_edge_register.tsv",
        directory / f"module{module}b_evidence_register.tsv",
    )


def public_locator(value: str) -> tuple[str, str]:
    """Keep stable public locators and classify local-only provenance."""
    stable: list[str] = []
    local_or_unstable = False
    for token in value.split(";"):
        token = token.strip()
        if not token:
            continue
        if token.startswith(("PMID:", "PMCID:", "DOI:", "http://", "https://")):
            stable.append(token)
        else:
            local_or_unstable = True
    if stable and local_or_unstable:
        return "; ".join(dict.fromkeys(stable)), "stable_plus_local"
    if stable:
        return "; ".join(dict.fromkeys(stable)), "stable"
    if local_or_unstable:
        return "", "local_only_or_unresolved"
    return "", "missing"


def effect_polarity(value: str) -> str:
    """Normalize register prose without inventing a sign for mixed relations."""
    lowered = value.casefold()
    negative = any(token in lowered for token in ("inhibit", "suppress", "repress", "decrease", "negative"))
    positive = any(token in lowered for token in ("activat", "promot", "induc", "increase", "positive"))
    if negative and positive:
        return "unknown"
    if negative:
        return "inhibitory"
    if positive:
        return "activating"
    return "unknown"


def canonical_relation_type(edge: dict[str, str], target_gene_edge: bool) -> str:
    """Emit the exact relation names used by mSCS while preserving the register relation."""
    relation = edge["relation_type"].casefold()
    if (
        any(has_evidence_layer(edge["evidence_layer"], token) for token in LIGAND_RECEPTOR_LAYER_TOKENS)
        and edge["module"] != "22B"
        and not target_gene_edge
    ):
        return "binds_receptor"
    if target_gene_edge:
        if any(token in relation for token in ("repress", "inhibit", "suppress", "decrease")):
            return "represses_target_gene"
        if any(token in relation for token in ("induc", "activat", "promot", "increase")):
            return "induces_target_gene"
        return "regulates_target_gene"
    return edge["relation_type"]


def normalize_species_support(value: str) -> str:
    lowered = value.casefold()
    has_mouse = "mouse" in lowered or "murine" in lowered
    has_human = "human" in lowered
    if has_mouse and has_human:
        return "both"
    if has_mouse:
        return "mouse"
    if has_human:
        return "human"
    if lowered.strip():
        return "mixed"
    return "not_applicable"


def normalize_confidence(value: str) -> str:
    lowered = value.casefold().strip()
    if lowered.startswith("high"):
        return "high"
    if lowered.startswith("medium"):
        return "medium"
    if lowered.startswith("low"):
        return "low"
    return "uncertain"


def normalize_export_priority(value: str) -> str:
    lowered = value.casefold().strip()
    return {
        "p1": "high",
        "p2": "medium",
        "p3": "low",
        "high": "high",
        "medium": "medium",
        "low": "low",
        "exclude": "exclude",
        "": "",
    }.get(lowered, "")


def normalize_support_kind(source_kind: str, support_kind: str) -> str:
    value = f"{source_kind} {support_kind}".casefold()
    if "primary" in value or "validated" in value:
        return "primary_experiment"
    if "review" in value:
        return "review_statement"
    if "database" in value or "frozen_" in value:
        return "database_curated"
    if "consensus" in value:
        return "consensus_summary"
    return "manual_background"


def normalize_source_scope(source_scope: str, source_kind: str, support_kind: str) -> str:
    scope = source_scope.casefold().strip()
    kind = source_kind.casefold().strip()
    support = support_kind.casefold().strip()
    boundary_kind = (
        kind.startswith("search")
        or kind.endswith("_boundary")
        or kind in {"no_evidence_boundary", "unresolved"}
    )
    boundary_scope = (
        scope.startswith("search")
        or "_search" in scope
        or any(token in scope for token in ("negative", "boundary", "unresolved", "no_evidence"))
    )
    if (
        boundary_kind
        or boundary_scope
        or support in {"negative_evidence", "no_exact_primary_packet"}
        or "no exact" in support
    ):
        return "negative_evidence"
    if "direct" in scope:
        return "direct_edge"
    if "pathway" in scope:
        return "pathway_membership"
    return "contextual_support"


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_release(source_root: Path, module20b_family_layer: Path | None = None) -> dict[str, object]:
    all_edges: list[dict[str, str]] = []
    exportable_edges: list[dict[str, str]] = []
    evidence_rows: list[dict[str, str]] = []
    module_stats: list[dict[str, object]] = []
    family_by_edge: dict[str, str] = {}
    if module20b_family_layer and module20b_family_layer.exists():
        family_by_edge = {
            row["b_edge_id"]: row["family_label"]
            for row in read_tsv(module20b_family_layer)
            if row.get("b_edge_id") and row.get("family_label")
        }

    for module in MODULES:
        edge_path, evidence_path = source_files(source_root, module)
        edges = read_tsv(edge_path)
        evidence = read_tsv(evidence_path)
        for row in edges:
            row = dict(row)
            row["module"] = f"{module}B"
            if row["module"] == "20B" and row["b_edge_id"] in family_by_edge:
                row["register_pathway_name"] = row.get("pathway_name", "")
                row["pathway_name"] = family_by_edge[row["b_edge_id"]]
            all_edges.append(row)
            if row.get("exportable") == "true" and not is_self_loop(row):
                exportable_edges.append(row)
        for row in evidence:
            row = dict(row)
            row["module"] = f"{module}B"
            evidence_rows.append(row)
        module_rows = [row for row in all_edges if row["module"] == f"{module}B"]
        module_stats.append(
            {
                "module": f"{module}B",
                "edge_count": len(module_rows),
                "exportable_edge_count": sum(
                    row.get("exportable") == "true" and not is_self_loop(row) for row in module_rows
                ),
                "evidence_count": len(evidence),
                "pathway_count": len({row.get("pathway_name", "") for row in module_rows}),
                "nonexportable_edge_count": sum(
                    row.get("exportable") != "true" or is_self_loop(row) for row in module_rows
                ),
            }
        )

    exportable_ids = {row["b_edge_id"] for row in exportable_edges}
    evidence_by_edge: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in evidence_rows:
        for edge_id in split_ids(row.get("b_edge_ids", "")):
            if edge_id in exportable_ids:
                evidence_by_edge[edge_id].append(row)

    node_records: dict[str, dict[str, object]] = {}
    for row in exportable_edges:
        for side in ("source_entity", "target_entity"):
            label = row.get(side, "").strip()
            key = node_key(label)
            if not key:
                continue
            record = node_records.setdefault(
                key,
                {
                    "label": canonical_node_label(label),
                    "labels": set(),
                    "modules": set(),
                    "pathways": set(),
                    "edge_ids": set(),
                    "exportable_edge_count": 0,
                },
            )
            record["labels"].add(label)
            record["modules"].add(row["module"])
            record["pathways"].add(row.get("pathway_name", ""))
            record["edge_ids"].add(row["b_edge_id"])
            record["exportable_edge_count"] += 1

    node_id_by_key = {
        key: f"NODE{index:05d}"
        for index, key in enumerate(sorted(node_records), start=1)
    }
    role_map: dict[str, dict[str, dict[str, set[str]]]] = {}
    for key, node_id in node_id_by_key.items():
        add_role(
            role_map,
            node_id,
            "signaling_cascade",
            "module20_24_export",
            "Node participates in at least one evidence-gated exported mechanism edge.",
        )
        if key in CURATED_ROLE_HINTS:
            hint_role, hint = CURATED_ROLE_HINTS[key]
            add_role(role_map, node_id, hint_role, "curated_role_hint", hint)

    node_rows: list[dict[str, object]] = []
    for key in sorted(node_records):
        record = node_records[key]
        label_variants = "; ".join(sorted(record["labels"]))
        modules = ";".join(sorted(record["modules"]))
        pathways = ";".join(sorted(filter(None, record["pathways"])))
        node_id = node_id_by_key[key]
        roles = set(role_map[node_id])
        node_rows.append(
            {
                "node_id": node_id,
                # Required mSCS contract fields. The source registers contain
                # curated labels, not a safe gene-symbol/entity-type mapping.
                "canonical_name": record["label"],
                "node_type": primary_node_type(roles),
                "node_subtype": "",
                "gene_symbol": safe_gene_symbol(record["label"], roles),
                "organism_scope": "",
                "compartment": "",
                "notes": (
                    f"modules={modules}; pathways={pathways}; "
                    f"label_variants={label_variants}; "
                    f"exportable_edge_count={len(record['edge_ids'])}"
                ),
                # Extra audit fields retained for the mSCIdblit release.
                "canonical_label": record["label"],
                "label_variants": label_variants,
                "modules": modules,
                "pathways": pathways,
                "exportable_edge_count": len(record["edge_ids"]),
            }
        )

    edge_rows: list[dict[str, object]] = []
    source_rows: list[dict[str, object]] = []
    pathway_edges: dict[tuple[str, str], set[str]] = defaultdict(set)
    pathway_nodes: dict[tuple[str, str], set[str]] = defaultdict(set)
    pathway_evidence: dict[tuple[str, str], set[str]] = defaultdict(set)

    for edge in sorted(exportable_edges, key=lambda row: (row["module"], row["b_edge_id"])):
        source_key = node_key(edge["source_entity"])
        target_key = node_key(edge["target_entity"])
        edge_id = edge["b_edge_id"]
        pathway = edge.get("pathway_name", "")
        pathway_key = (edge["module"], pathway)
        linked_evidence = evidence_by_edge.get(edge_id, [])
        evidence_ids = sorted({row["b_evidence_id"] for row in linked_evidence})
        locator_count = sum(bool(public_locator(row.get("source_locator", ""))[0]) for row in linked_evidence)
        role_evidence = f"edge={edge_id}; evidence={';'.join(evidence_ids) or 'none'}"
        pathway_lower = pathway.casefold()
        layer_lower = edge["evidence_layer"].casefold()
        target_gene_edge = "target_gene" in pathway_lower or has_evidence_layer(
            edge["evidence_layer"], "target_gene"
        )
        if target_gene_edge:
            add_role(
                role_map,
                node_id_by_key[source_key],
                "transcription_factor",
                "register_target_gene_layer",
                role_evidence,
            )
            add_role(
                role_map,
                node_id_by_key[target_key],
                "target_gene",
                "register_target_gene_layer",
                role_evidence,
            )
        elif (
            any(has_evidence_layer(edge["evidence_layer"], token) for token in LIGAND_RECEPTOR_LAYER_TOKENS)
            and edge["module"] != "22B"
        ):
            # Modules 20B, 21B, 23B, and 24B use this layer for their
            # receptor-facing molecular handoffs. Module 22B also uses the
            # layer for TF-target rows, so those are handled above instead of
            # being mislabeled as ligand/receptor pairs.
            add_role(
                role_map,
                node_id_by_key[source_key],
                "ligand",
                "register_ligand_receptor_layer",
                role_evidence,
            )
            add_role(
                role_map,
                node_id_by_key[target_key],
                "receptor",
                "register_ligand_receptor_layer",
                role_evidence,
            )
        edge_rows.append(
            {
                "edge_id": edge_id,
                "module": edge["module"],
                "source_node_id": node_id_by_key[source_key],
                "target_node_id": node_id_by_key[target_key],
                "pathway_label": pathway,
                "effect_polarity": effect_polarity(edge["relation_type"]),
                "evidence_status": edge["edge_status"],
                "notes": edge["consolidation_note"],
                "source_label": edge["source_entity"],
                "relation_type": canonical_relation_type(edge, target_gene_edge),
                "register_relation_type": edge["relation_type"],
                "target_label": edge["target_entity"],
                "pathway_name": pathway,
                "evidence_layer": edge["evidence_layer"],
                "edge_status": edge["edge_status"],
                "context_scope": edge["context_scope"],
                "cell_type_context": edge["cell_type_context"],
                "compartment_context": edge["compartment_context"],
                "species_context": edge["species_context"],
                "injury_context": edge["injury_context"],
                "confidence_tier": edge["confidence_tier"],
                "export_priority": normalize_export_priority(edge["export_priority"]),
                "evidence_ids": ";".join(evidence_ids),
                "evidence_count": len(evidence_ids),
                "source_locator_count": locator_count,
                "exportable": "true",
                "consolidation_note": edge["consolidation_note"],
            }
        )
        pathway_edges[pathway_key].add(edge_id)
        pathway_nodes[pathway_key].update((node_id_by_key[source_key], node_id_by_key[target_key]))
        pathway_evidence[pathway_key].update(evidence_ids)

        for evidence in sorted(linked_evidence, key=lambda row: row["b_evidence_id"]):
            locator, locator_status = public_locator(evidence["source_locator"])
            source_rows.append(
                {
                    "edge_source_id": f"SRC{len(source_rows) + 1:06d}",
                    "edge_id": edge_id,
                    # The register evidence ID is an explicit external
                    # observation token, not a fabricated database integer.
                    "paper_id": "",
                    "observation_id": f"REGISTER:{evidence['b_evidence_id']}",
                    "claim_id": "",
                    "support_kind": normalize_support_kind(
                        evidence["source_kind"], evidence["support_kind"]
                    ),
                    "species_support": normalize_species_support(evidence["species_support"]),
                    "source_scope": normalize_source_scope(
                        evidence["source_scope"], evidence["source_kind"], evidence["support_kind"]
                    ),
                    "confidence_tier": normalize_confidence(evidence["confidence_tier"]),
                    "citation_note": evidence["citation_note"],
                    "notes": (
                        f"register_evidence_id={evidence['b_evidence_id']}; "
                        f"original_source_kind={evidence['source_kind']}; "
                        f"original_support_kind={evidence['support_kind']}; "
                        f"source_locator_status={locator_status}"
                    ),
                    "module": edge["module"],
                    "evidence_id": evidence["b_evidence_id"],
                    "source_kind": evidence["source_kind"],
                    "source_locator": locator,
                    "source_locator_status": locator_status,
                    "evidence_summary": evidence["evidence_summary"],
                    "limitations": evidence["limitations"],
                    "evidence_layer": evidence["evidence_layer"],
                    "evidence_exportable": evidence["exportable"],
                    "consolidation_note": evidence["consolidation_note"],
                }
            )

    role_rows: list[dict[str, object]] = []
    node_rows_by_id = {str(row["node_id"]): row for row in node_rows}
    for node_id in sorted(role_map):
        roles = set(role_map[node_id])
        node_row = node_rows_by_id[node_id]
        node_row["node_type"] = primary_node_type(roles)
        node_row["gene_symbol"] = safe_gene_symbol(str(node_row["canonical_name"]), roles)
        for role in sorted(roles):
            assignment = role_map[node_id][role]
            role_rows.append(
                {
                    "node_id": node_id,
                    "role": role,
                    "role_source": ";".join(sorted(assignment["sources"])),
                    "role_evidence": " || ".join(sorted(assignment["evidence"])),
                }
            )

    entity_forms, entity_transitions = build_entity_forms(node_rows, role_map)

    pathway_rows = [
        {
            "module": module,
            "pathway_name": pathway,
            "edge_count": len(pathway_edges[(module, pathway)]),
            "node_count": len(pathway_nodes[(module, pathway)]),
            "evidence_count": len(pathway_evidence[(module, pathway)]),
        }
        for module, pathway in sorted(pathway_edges)
    ]

    boundary_counter: Counter[tuple[str, str, str, str, str]] = Counter()
    for edge in all_edges:
        if edge.get("exportable") == "true" and not is_self_loop(edge):
            continue
        key = (
            edge["module"],
            edge.get("pathway_name", ""),
            edge.get("evidence_layer", ""),
            edge.get("edge_status", ""),
            edge.get("export_priority", ""),
        )
        boundary_counter[key] += 1
    boundary_rows = [
        {
            "module": key[0],
            "pathway_name": key[1],
            "evidence_layer": key[2],
            "edge_status": key[3],
            "export_priority": key[4],
            "nonexportable_edge_count": count,
        }
        for key, count in sorted(boundary_counter.items())
    ]

    input_registers = []
    for module in MODULES:
        edge_path, evidence_path = source_files(source_root, module)
        input_registers.extend(
            {
                "module": f"{module}B",
                "file": path.name,
                "sha256": file_sha256(path),
            }
            for path in (edge_path, evidence_path)
        )

    metadata = {
        "release_name": "mSCIdblit Module 20B-24B mechanism graph",
        "bundle_name": "module20_24_mechanism_graph",
        "release_id": f"module20_24_mechanism_graph:{date.today().isoformat()}",
        "release_status": "conservative_register_backed_snapshot",
        "source_repo": "mSCIdblit",
        "target_repo": "mSCS",
        "source_scope": "validated Module 20B-24B edge and evidence registers",
        "generated_at": date.today().isoformat(),
        "canonical_database_materialization": False,
        "authoritative_pathway_snapshot": True,
        "replacement_policy": (
            "Importing this bundle replaces the selected active mechanism release in mSCS; "
            "it does not alter atlas-derived tables."
        ),
        "input_registers": input_registers,
        "graph_policy": {
            "exportable_edges_only": True,
            "composite_labels_preserved": True,
            "explicit_node_aliases_applied": True,
            "node_aliases": node_alias_metadata(),
            "unresolved_and_nonexportable_edges_excluded_from_graph": True,
            "evidence_rows_retained_for_exported_edges": True,
            "self_loops_excluded_from_traversable_graph": True,
        },
        "counts": {
            "nodes": len(node_rows),
            "edges": len(edge_rows),
            "edge_sources": len(source_rows),
            "node_roles": len(role_rows),
            "entity_forms": len(entity_forms),
            "entity_transitions": len(entity_transitions),
            "nodes_with_ligand_role": sum("ligand" in role_map[node_id] for node_id in role_map),
            "nodes_with_receptor_role": sum("receptor" in role_map[node_id] for node_id in role_map),
            "nodes_with_transcription_factor_role": sum(
                "transcription_factor" in role_map[node_id] for node_id in role_map
            ),
            "nodes_with_target_gene_role": sum("target_gene" in role_map[node_id] for node_id in role_map),
            "pathways": len(pathway_rows),
            "boundary_groups": len(boundary_rows),
            "nonexportable_edges": sum(row["nonexportable_edge_count"] for row in boundary_rows),
        },
        "source_locator_status_counts": dict(
            Counter(row["source_locator_status"] for row in source_rows)
        ),
        "module_counts": module_stats,
        "files": {
            "nodes": "mechanism_nodes.tsv",
            "node_roles": "mechanism_node_roles.tsv",
            "edges": "mechanism_edges.tsv",
            "edge_sources": "mechanism_edge_sources.tsv",
            "pathways": "mechanism_pathways.tsv",
            "boundaries": "mechanism_boundary_summary.tsv",
            "entity_forms": "mechanism_entity_forms.tsv",
            "entity_transitions": "mechanism_entity_transitions.tsv",
            "validation": "validation_report.json",
        },
        "accuracy_contract": [
            "Every exported edge must reference existing source and target nodes.",
            "Every exported node must have a signaling_cascade role; specialized roles are only added from explicit register layers or curated role hints.",
            "Every exported edge must retain at least one evidence-register source row.",
            "Every exported edge must belong to a pathway row.",
            "Role-aware edges use canonical binds_receptor or target-gene relation types with matching endpoint roles; original register relations remain audit fields.",
            "Self-loop register rows are retained as boundaries and are not inserted into the normalized graph.",
            "Non-exportable edges remain summarized as boundaries and are not traversable graph edges.",
            "Stable PMID/PMCID/DOI/URL locators are retained in edge-source rows where available; local paths are not released.",
            "Gene and protein/ligand forms are typed auxiliary records; a shared label or role co-occurrence does not assert transcription, translation, secretion, or transport.",
            "Entity transitions are conditional metadata, never causal graph edges; intercellular continuation requires explicit output/secretion evidence or a separately validated bridge.",
        ],
    }

    return {
        "metadata": metadata,
        "nodes": node_rows,
        "node_roles": role_rows,
        "edges": edge_rows,
        "sources": source_rows,
        "pathways": pathway_rows,
        "boundaries": boundary_rows,
        "entity_forms": entity_forms,
        "entity_transitions": entity_transitions,
    }


def main() -> None:
    args = parse_args()
    family_layer = args.module20b_family_layer.resolve()
    release = build_release(args.source_root.resolve(), family_layer if family_layer.exists() else None)
    if family_layer.exists():
        release["metadata"]["module20b_pathway_family_layer"] = {
            "file": str(family_layer.relative_to(ROOT)),
            "assignment_type": "conservative_receptor_family_grouping",
            "downstream_pathway_claim": False,
            "register_unchanged": True,
            "sha256": file_sha256(family_layer),
        }
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    write_tsv(
        output_dir / "mechanism_nodes.tsv",
        [
            "node_id", "canonical_name", "node_type", "node_subtype", "gene_symbol",
            "organism_scope", "compartment", "notes", "canonical_label", "label_variants",
            "modules", "pathways", "exportable_edge_count",
        ],
        release["nodes"],
    )
    write_tsv(
        output_dir / "mechanism_node_roles.tsv",
        ["node_id", "role", "role_source", "role_evidence"],
        release["node_roles"],
    )
    write_tsv(
        output_dir / "mechanism_edges.tsv",
        [
            "edge_id", "source_node_id", "target_node_id", "pathway_label", "relation_type",
            "effect_polarity", "species_context", "cell_type_context", "compartment_context",
            "injury_context", "evidence_status", "context_scope", "export_priority", "notes",
            "module", "source_label", "target_label", "register_relation_type", "pathway_name", "evidence_layer", "edge_status",
            "confidence_tier", "evidence_ids",
            "evidence_count", "source_locator_count", "exportable", "consolidation_note",
        ],
        release["edges"],
    )
    write_tsv(
        output_dir / "mechanism_edge_sources.tsv",
        [
            "edge_source_id", "edge_id", "paper_id", "observation_id", "claim_id", "support_kind",
            "species_support", "source_scope", "confidence_tier", "citation_note", "notes",
            "module", "evidence_id", "source_kind", "source_locator", "source_locator_status",
            "evidence_summary", "limitations", "evidence_layer", "evidence_exportable",
            "consolidation_note",
        ],
        release["sources"],
    )
    write_tsv(
        output_dir / "mechanism_pathways.tsv",
        ["module", "pathway_name", "edge_count", "node_count", "evidence_count"],
        release["pathways"],
    )
    write_tsv(
        output_dir / "mechanism_boundary_summary.tsv",
        [
            "module", "pathway_name", "evidence_layer", "edge_status", "export_priority",
            "nonexportable_edge_count",
        ],
        release["boundaries"],
    )
    write_tsv(
        output_dir / "mechanism_entity_forms.tsv",
        [
            "entity_form_id", "node_id", "form_type", "canonical_name", "source_role",
            "form_status", "notes",
        ],
        release["entity_forms"],
    )
    write_tsv(
        output_dir / "mechanism_entity_transitions.tsv",
        [
            "transition_id", "source_form_id", "target_form_id", "source_node_id",
            "target_node_id", "source_form_type", "target_form_type", "transition_type",
            "relation_type", "traversal_status", "causal_status", "evidence_status",
            "source_label", "target_label", "evidence_ids", "notes",
        ],
        release["entity_transitions"],
    )
    # Output bridges are intentionally exported as a review queue rather than
    # graph edges. They preserve review records, stable citations, and links
    # back to existing source edges while keeping causal/traversal status
    # explicitly gated until primary evidence is manually validated.
    from audit_mechanism_output_bridges import (
        audit as audit_output_bridges,
        audit_edge_register_outputs,
        audit_validated_output_bridges,
        VALIDATED_OUTPUT_FIELDS,
    )

    output_bridge_rows: list[dict[str, object]] = []
    for review_root in (ROOT / "work" / "module22a", ROOT / "work" / "module21_relay"):
        if review_root.exists():
            output_bridge_rows.extend(audit_output_bridges(review_root, output_dir))
    output_bridge_rows.extend(
        audit_edge_register_outputs(ROOT / "work" / "module_b_consolidation", output_dir)
    )
    output_bridge_rows.sort(
        key=lambda row: (
            str(row.get("review_source_namespace", "")),
            str(row.get("target_or_program_label", "")),
            str(row.get("output_product_labels", "")),
            str(row.get("review_record_path", "")),
        )
    )
    for index, row in enumerate(output_bridge_rows, start=1):
        row["candidate_id"] = f"OUT:{index:05d}"
    write_tsv(
        output_dir / "mechanism_output_bridge_candidates.tsv",
        OUTPUT_BRIDGE_FIELDS,
        output_bridge_rows,
    )
    release["metadata"]["counts"]["output_bridge_candidates"] = len(output_bridge_rows)
    release["metadata"]["files"]["output_bridge_candidates"] = "mechanism_output_bridge_candidates.tsv"
    validated_output_bridge_rows = audit_validated_output_bridges(
        ROOT / "work" / "module_b_consolidation", output_dir
    )
    write_tsv(
        output_dir / "mechanism_output_bridges_validated.tsv",
        VALIDATED_OUTPUT_FIELDS,
        validated_output_bridge_rows,
    )
    release["metadata"]["counts"]["output_bridges_validated"] = len(validated_output_bridge_rows)
    release["metadata"]["files"]["output_bridges_validated"] = "mechanism_output_bridges_validated.tsv"
    release["metadata"]["graph_policy"]["output_bridge_candidates_are_review_only"] = True
    release["metadata"]["graph_policy"]["output_bridge_candidates_are_not_graph_edges"] = True
    release["metadata"]["graph_policy"]["validated_output_bridges_are_not_graph_edges"] = True
    (output_dir / "bundle_metadata.json").write_text(json.dumps(release["metadata"], indent=2) + "\n")
    print(json.dumps(release["metadata"]["counts"], sort_keys=True))


if __name__ == "__main__":
    main()
