# Module 19B: Histone Modification and Chromatin-State Regulation in SCI - Evidence Consolidation and Query Readiness

## Overview

This tracker converts Module 19A experiments into mark-, enzyme-, locus-, and phenotype-linked evidence using the shared signaling graph schema. It separates measured histone modifications from writer/eraser/reader relationships, chromatin-state observations, transcriptional consequences, perturbations, and author claims.

**Input corpus**: Module 19A histone-modification literature, initially seeded from Modules 3, 5, 9, and 14.

**Status**: FIRST-PASS CONSOLIDATION COMPLETE; TARGETED FULL-TEXT UPGRADES QUEUED.

## Evidence Topic Map

| Topic ID | Consensus-Ready Topic | Required Evidence |
|---|---|---|
| M19B-T001 | Histone mark identity and locus | Histone, residue, modification, genomic location, direction, and assay |
| M19B-T002 | Writers, erasers, and readers | Enzyme or reader identity, recruitment, perturbation, and specificity |
| M19B-T003 | Injury-responsive enhancer and promoter states | H3K4me1/H3K27ac enhancer state, H3K4me3 promoter comparison, accessibility, and target genes |
| M19B-T004 | Histone lactylation and metabolic chromatin signaling | Lactate source, H3K9la or other mark, writer/reader, TXNIP/NLRP3, and immune phenotype |
| M19B-T005 | Neuronal regenerative chromatin programs | CITED2, WNT3A, PTEN, axon-growth genes, and neuronal state transitions |
| M19B-T006 | Chromatin intersections with danger and innate signaling | DAMP, TLR, NF-kappaB, NLRP3, STAT, and metabolic-state edges |
| M19B-T007 | Perturbation phenotypes | HDAC/HAT/methyltransferase/demethylase inhibition, locus editing, knockout, and rescue |
| M19B-T008 | SCI translation boundaries | Microglia, macrophage, neuron, astrocyte, oligodendrocyte, organoid, axon, lesion, locomotor, pain, and safety outcomes |

## Pass 4A: Atomic Chromatin Observations

| Observation ID | Topic ID | Paper ID | Experiment ID | Mark or Edge | Evidence Type | Observation Value | Context | Extraction Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| M19B-O001 | M19B-T003 | M19A-P003 | M19A-P003-E001 | H3K4me1/H3K27ac enhancer state and H3K4me3 promoter comparison at WNT3A | Primary chromatin experiment | Injury increased H3K4me1 at WNT3A e5/e7 enhancer regions and increased enhancer-associated eRNAs; WNT3A promoter H3K4me3 did not show the same increase | Rat injured cortical neurons | high | EXTRACTED |
| M19B-O002 | M19B-T003 | M19A-P004 | M19A-P004-E001 | Injury-responsive enhancer accessibility | Primary chromatin-state experiment | Mouse spinal cord contusion produced cell-state-specific enhancer accessibility programs that supported reactive-astrocyte targeting; no direct histone mark was reported in the captured source | Mouse CNS glial cells | medium | EXTRACTED |
| M19B-O003 | M19B-T001 | M19A-P001 | M19A-P001-E001 | H3K9 methylation and histone deacetylation at PTEN promoter | Primary tool experiment | dCas9-KRAB repression induced PTEN promoter H3 methylation/deacetylation and reduced PTEN expression in neural cells | Human neural cells and rat PC-12 cells | medium | EXTRACTED |
| M19B-O004 | M19B-T002 | M19A-P005 | M19A-P005-E001 | Targeted H3K27ac deposition | Primary tool experiment | dCas9-p300 Core increased H3K27ac at targeted enhancer/promoter loci and activated transcription | Mammalian cultured cells | high | EXTRACTED |
| M19B-O005 | M19B-T004 | M19A-P007 | M19A-P007-E001 | SCI-associated macrophage H3K9la | Primary mark-identification experiment | H3K9la was elevated in lesion macrophages and circulating monocytes at 14 dpi; H3K14la/H3K18la were not comparably increased in the primary comparison | Mouse SCI and human serum-linked context | high | EXTRACTED |
| M19B-O006 | M19B-T004 | M19A-P007 | M19A-P007-E002 | H3K9la-associated TXNIP activation | Primary causal mechanism experiment | CUT&Tag/RNA-seq identified TXNIP as a direct H3K9la-associated inflammatory target; lactate increased TXNIP/NLRP3 signaling and mitochondrial dysfunction | Mouse lesion macrophages and macrophage cultures | high | EXTRACTED |
| M19B-O007 | M19B-T007 | M19A-P007 | M19A-P007-E002 | H3K9la inhibition phenotype | Primary perturbation experiment | 2-DG, TXNIP knockdown, or H3K9la-peptide inhibition reduced inflammatory signaling; in vivo inhibition improved axon and functional outcomes | Mouse SCI | high | EXTRACTED |
| M19B-O008 | M19B-T005 | M19A-P008 | M19A-P008-E001 | Cited2-linked regenerative chromatin state | Primary chromatin-state experiment | Cited2 overexpression reinstated developmental growth-associated transcriptional and epigenetic signatures in regenerative neuronal contexts | Mouse DRG neurons and SCI model | high | EXTRACTED |
| M19B-O009 | M19B-T007 | M19A-P008 | M19A-P008-E002 | Panobinostat/Cited2 perturbation phenotype | Primary pharmacologic perturbation | Panobinostat promoted sensory axon growth, 5-HT sprouting, and neurological recovery; Cited2 knockdown blocked the in vitro growth benefit | Mouse SCI and cultured neurons | high | EXTRACTED |
| M19B-O010 | M19B-T007 | M19A-P014 | M19A-P014-E001 | Neuronal HDAC3 knockdown phenotype | Primary SCI enzyme perturbation | HDAC3 knockdown/deletion promoted neurite outgrowth, propriospinal detour-circuit formation, and locomotor recovery after incomplete SCI; no benefit after full transection | Mouse SCI and neuronal cultures | medium | EXTRACTED |
| M19B-O011 | M19B-T002 | M19A-P015 | M19A-P015-E001 | SCI-associated HDAC3 in innate immune cells | Primary SCI enzyme perturbation | HDAC3 increased in lesion microglia/macrophages; selective RGFP966 suppressed inflammatory cytokines and improved neuroprotective/functional outcomes | Mouse SCI innate immune compartment | high | EXTRACTED |
| M19B-O012 | M19B-T007 | M19A-P016 | M19A-P016-E001 | SCI-associated global histone hypoacetylation | Primary pharmacologic experiment | Ac-H3 and Ac-H4 decreased after SCI; valproate prevented the decrease, reduced apoptosis, increased Hsp70/Bcl-2, and improved locomotion | Rat SCI | medium | EXTRACTED |
| M19B-O013 | M19B-T007 | M19A-P017 | M19A-P017-E001 | Class-I HDAC inhibition and acetyl-H3 | Primary pharmacologic experiment | CI-994 increased acetylated-H3 signal and promoted functional recovery after SCI | Mouse SCI | high | EXTRACTED |
| M19B-O014 | M19B-T002 | M19A-P018 | M19A-P018-E001 | BET/BRD reader inhibition | Primary reader perturbation | JQ1/BET inhibition attenuated acute inflammatory responses after SCI; exact mark occupancy and reader-specific rescue remain pending | Mouse SCI and primary neural cells | medium | EXTRACTED |
| M19B-O015 | M19B-T007 | M19A-P019 | M19A-P019-E001 | HDAC3 contradiction | Primary pharmacologic contradiction | HDAC3 inhibition promoted alternative macrophage activation but did not improve functional recovery, preventing a universal HDAC3-neuroprotection rule | SCI model context | medium | EXTRACTED |
| M19B-O016 | M19B-T002 | M19A-P020 | M19A-P020-E001 | JMJD3/H3K27me3 at IL-6 promoter | Primary demethylase mechanism | Jmjd3 recruitment coincided with H3K27me3 loss and H3K27me1 gain at the IL-6 promoter; siRNA reduced OGD/R-induced IL-6 | Endothelial cells and injured spinal-cord vessels | high | EXTRACTED |
| M19B-O017 | M19B-T007 | M19A-P021 | M19A-P021-E001 | JMJD3 inhibition and oligodendrocyte-lineage commitment | Primary enzyme perturbation | GSK-J4 altered JMJD3/H3K27me3-associated progenitor states and supported endogenous oligodendrocyte-lineage commitment after SCI | Mouse spinal progenitor/oligodendrocyte lineage | high | EXTRACTED |
| M19B-O018 | M19B-T003 | M19A-P022 | M19A-P022-E001 | Persistent H3K27ac in chronic microglia and scar | Primary mark perturbation | H3K27ac remained elevated in microglia and astrocytes at subacute/chronic time points and tracked cholesterol metabolism and SPP1-linked scar communication | Mouse compression SCI | high | EXTRACTED |
| M19B-O019 | M19B-T007 | M19A-P022 | M19A-P022-E001 | L002/H3K27ac inhibition phenotype | Primary mark perturbation | L002 reduced H3K27ac, cholesterol accumulation, neuroinflammation, SPP1, and excessive scar formation | Mouse compression SCI | high | EXTRACTED |
| M19B-O020 | M19B-T004 | M19A-P023 | M19A-P023-E001 | H4K12la/PD-1 repair axis | Primary lactylation mechanism | Lactate elevated microglial H4K12la and PD-1 transcription; PD-1 inhibition or microglial shRNA reversed lactate-associated repair effects | Mouse SCI microglia | high | EXTRACTED |
| M19B-O021 | M19B-T004 | M19A-P024 | M19A-P024-E001 | H4K12la/Spp1 repair axis | Primary lactylation/locus experiment | H4K12la promoted Spp1 transcription in reprogrammed microglia; SPP1 validation improved functional recovery and axonal mitochondrial outcomes | Mouse SCI microglia | medium | EXTRACTED |
| M19B-O022 | M19B-T004 | M19A-P025 | M19A-P025-E001 | Glis1/p300/H3K18la/SCG2 axis | Primary lactylation mechanism | Post-SCI lactate and senescence were linked to Glis1-associated p300/H3K18la regulation of SCG2 and reduced neuronal senescence | Mouse SCI neurons | medium | EXTRACTED |
| M19B-O023 | M19B-T003 | M19A-P026 | M19A-P026-E001 | OGD-associated H3K27ac loss | Primary ex vivo chromatin-state experiment | OGD reduced H3K27ac in organotypic spinal-cord slices and altered Apoc1, Spp1, Aff1, Brd4, KCNN3, and Rgma programs | Organotypic spinal-cord slices | medium | EXTRACTED |
| M19B-O024 | M19B-T003 | M19A-P027 | M19A-P027-E001 | Human spinal-cord active/poised/silenced enhancer states | Primary atlas comparator | H3K27ac/H3K4me1/H3K27me3 and ATAC profiles define cell-type-specific regulatory elements in adult human spinal cord | Human spinal-cord donor nuclei | high | EXTRACTED |
| M19B-O025 | M19B-T005 | M19A-P029 | M19A-P029-E001 | Regenerative versus central DRG epigenomic state | Primary CNS/PNS comparator | Peripheral axotomy produced H3K9ac/H3K27ac/accessibility signatures distinct from central axotomy; CTCF deletion impaired regeneration | Mouse DRG neurons | high | EXTRACTED |
| M19B-O026 | M19B-T005 | M19A-P030 | M19A-P030-E001 | HDAC5 export and Ac-H3 after axotomy | Primary CNS/PNS comparator | Sciatic injury exported HDAC5 from DRG nuclei and increased Ac-H3; calcium chelation blocked the response | Mouse DRG neurons | high | EXTRACTED |
| M19B-O027 | M19B-T005 | M19A-P031 | M19A-P031-E001 | EZH2 and optic-nerve regeneration | Primary CNS comparator | Ezh2 gain-of-function promoted optic-nerve regeneration through catalytic and non-catalytic mechanisms | Mouse retinal ganglion cells | high | EXTRACTED |
| M19B-O028 | M19B-T005 | M19A-P033 | M19A-P033-E001 | HDAC3/p300/H3K27ac in peripheral remyelination | Primary CNS/PNS comparator | HDAC3 inhibition increased H3K27ac at promyelinating loci and enhanced myelin growth and recovery after peripheral nerve injury | Mouse Schwann cells and peripheral nerve | high | EXTRACTED |

## Pass 4B: Directed Chromatin-Edge Register

| Edge ID | Source Entity | Relation | Target Entity | Pathway | Context | Evidence IDs | Status |
|---|---|---|---|---|---|---|---|
| M19B-E001 | H3K4me1/H3K27ac | marks / supports activity at | WNT3A e5/e7 enhancer | Injury-responsive enhancer regulation | Injured cortical neurons | M19B-O001 | EXTRACTED / ASSOCIATIONAL |
| M19B-E002 | H3K9la | activates / is associated with | TXNIP locus | Metabolic chromatin signaling | SCI macrophages; lactate-rich state | M19B-O005, M19B-O006 | EXTRACTED |
| M19B-E003 | TXNIP | activates | NLRP3 inflammatory pathway | H3K9la-linked macrophage inflammation | SCI macrophages | M19B-O006, M19B-O007 | EXTRACTED |
| M19B-E004 | dCas9-KRAB / KRAB-KAP1 | recruits methylation and deacetylation | PTEN promoter | Programmable transcriptional repression | Neural cells | M19B-O003 | EXTRACTED / TOOL-COMPARATOR |
| M19B-E005 | dCas9-p300 Core | deposits H3K27ac at | Target enhancer/promoter | Programmable transcriptional activation | Mammalian cultured cells | M19B-O004 | EXTRACTED / TOOL-COMPARATOR |
| M19B-E006 | Cited2 | regulates | Growth-associated chromatin program | Neuronal maturation and regenerative decline | DRG neurons and SCI | M19B-O008, M19B-O009 | EXTRACTED |
| M19B-E007 | HDAC3 | constrains | Neuronal growth and propriospinal detour program | Incomplete SCI repair | Mouse neuronal circuits | M19B-O010 | EXTRACTED / MARK-LEVEL LINK PENDING |
| M19B-E008 | HDAC3 | deacetylates / promotes | Inflammatory innate-immune program | SCI myeloid response | Lesion microglia/macrophages | M19B-O011 | EXTRACTED |
| M19B-E009 | H3K27me3 | represses / is removed from | IL-6 promoter | Jmjd3-linked endothelial inflammation | SCI vessels and OGD/R endothelial cells | M19B-O016 | EXTRACTED |
| M19B-E010 | JMJD3 | erases | H3K27me3 at IL-6 promoter | Acute SCI endothelial response | Endothelial cells | M19B-O016 | EXTRACTED |
| M19B-E011 | H3K27ac | supports | Cholesterol-metabolism and SPP1 program | Chronic microglial scar biology | SCI microglia/astrocyte/fibroblast compartment | M19B-O018, M19B-O019 | EXTRACTED |
| M19B-E012 | H4K12la | activates | PD-1 transcription | Lactate-linked microglial repair | SCI microglia | M19B-O020 | EXTRACTED |
| M19B-E013 | H4K12la | activates | Spp1 transcription | Glycolytic microglial repair | SCI microglia | M19B-O021 | EXTRACTED |
| M19B-E014 | H3K18la | regulates | SCG2 and neuronal senescence program | Glis1/lactate metabolic state | SCI neurons | M19B-O022 | EXTRACTED / SOURCE-PAGE |
| M19B-E015 | BRD4/BET reader | reads acetylated histones / promotes | Acute inflammatory transcription | JQ1 after SCI | Neural cells and injured cord | M19B-O014 | EXTRACTED / READER-LEVEL |
| M19B-E016 | HDAC5 nuclear export | increases | Ac-H3 and regenerative gene program | Peripheral axotomy | DRG neurons | M19B-O026 | EXTRACTED |
| M19B-E017 | EZH2 | regulates | Optic-nerve regenerative program | CNS axon injury comparator | Retinal ganglion cells | M19B-O027 | EXTRACTED |
| M19B-E018 | HDAC3/p300 balance | regulates H3K27ac at | Promyelinating loci | Peripheral nerve remyelination | Schwann cells | M19B-O028 | EXTRACTED |

## Pass 4C: Perturbation and Phenotype Matrix

| Perturbation ID | Experiment ID | Entity | Perturbation Type | Scope | Phenotype ID | Effect Direction | Rescue / Epistasis | Evidence ID | Status |
|---|---|---|---|---|---|---|---|---|---|
| M19B-PERT001 | M19A-P007-E002 | H3K9 lactylation / TXNIP | 2-DG, TXNIP knockdown, or H3K9la-peptide inhibition | SCI macrophage context | NLRP3 inflammation, mitochondrial dysfunction, axon and functional outcomes | Reduced inflammatory signaling and improved recovery with inhibition | No direct rescue beyond pathway attenuation reported in current extraction | M19B-O006, M19B-O007 | EXTRACTED |
| M19B-PERT002 | M19A-P001-E001 | dCas9-KRAB | Locus-specific repression | Neural-cell PTEN promoter | PTEN expression and neurite outgrowth | Increased neurite outgrowth after PTEN repression | shRNA comparison; no rescue | M19B-O003 | EXTRACTED / TOOL-COMPARATOR |
| M19B-PERT003 | M19A-P005-E001 | dCas9-p300 Core | Locus-specific H3K27 acetylation | Mammalian enhancer/promoter | Target-gene activation | Increased H3K27ac and transcription | Catalytic-dead and dCas9 controls | M19B-O004 | EXTRACTED / TOOL-COMPARATOR |
| M19B-PERT004 | M19A-P008-E001 | Cited2 | Overexpression or knockdown | Regenerative versus mature DRG neuronal state | Growth-associated transcription and chromatin accessibility | Overexpression restored immature/regenerative signatures | Knockdown and GFP/empty-vector controls | M19B-O008 | EXTRACTED |
| M19B-PERT005 | M19A-P008-E002 | Panobinostat / HDAC inhibition | Pharmacologic inhibition | Mouse SCI and cultured neurons | Axon growth, sprouting, neurological recovery | Improved outcomes; Cited2 knockdown blocked in vitro growth benefit | Cited2 knockdown | M19B-O009 | EXTRACTED |
| M19B-PERT006 | M19A-P014-E001 | HDAC3 | siRNA knockdown or neuronal deletion | Incomplete SCI and neuronal cultures | Neurite outgrowth, detour pathways, locomotion | Improved recovery after incomplete SCI; no benefit after full transection | Stat3 deletion and mTOR inactivation epistasis | M19B-O010 | EXTRACTED / ABSTRACT-LEVEL |
| M19B-PERT007 | M19A-P015-E001 | HDAC3 | RGFP966 selective inhibition | SCI innate immune compartment | Cytokines, neuroprotection, functional recovery | Suppressed inflammatory cytokines and improved outcomes | Cell-state specificity and broad HDAC-independent effects remain to resolve | M19B-O011 | EXTRACTED |
| M19B-PERT008 | M19A-P016-E001 | HDACs | Valproate treatment | Rat SCI | Ac-H3/Ac-H4, apoptosis, Hsp70/Bcl-2, locomotion | Prevented post-SCI hypoacetylation and improved recovery | Broad HDAC and non-histone targets remain possible | M19B-O012 | EXTRACTED |
| M19B-PERT009 | M19A-P017-E001 | Class-I HDACs | CI-994 | Mouse SCI | Ac-H3 and functional recovery | Increased Ac-H3 and improved behavior | Specific HDAC member and locus effects unresolved | M19B-O013 | EXTRACTED |
| M19B-PERT010 | M19A-P018-E001 | BRD2/3/4 | JQ1 BET inhibition | Acute SCI inflammation | Inflammatory transcription | Attenuated acute inflammation | Exact reader occupancy and mark dependence pending | M19B-O014 | EXTRACTED / SOURCE-PAGE |
| M19B-PERT011 | M19A-P019-E001 | HDAC3 | RGFP966 or Scriptaid | SCI macrophage context | Alternative activation and function | Alternative activation increased without functional recovery | Direct contradiction to M19B-PERT007 retained | M19B-O015 | EXTRACTED |
| M19B-PERT012 | M19A-P020-E001 | JMJD3 | siRNA depletion | SCI endothelial/OGD-R context | IL-6 transcription and barrier-related inflammation | Reduced IL-6 induction | Promoter mark change after depletion requires quantitative upgrade | M19B-O016 | EXTRACTED |
| M19B-PERT013 | M19A-P021-E001 | JMJD3 | GSK-J4 inhibition | Mouse SCI progenitor compartment | Oligodendrocyte-lineage commitment | Altered H3K27me3-associated progenitor state and supported lineage commitment | Dose and timing boundaries retained | M19B-O017 | EXTRACTED |
| M19B-PERT014 | M19A-P022-E001 | H3K27ac | L002 inhibition | Mouse chronic compression SCI | Microglial cholesterol, SPP1, scar, function | Reduced H3K27ac and scar-associated pathology | HAT/HDAC specificity unresolved | M19B-O018, M19B-O019 | EXTRACTED |
| M19B-PERT015 | M19A-P023-E001 | H4K12la/PD-1 | Lactate; PD-1 inhibitor; microglial AAV-sh-PD-1 | Mouse SCI microglia | Scar, axon regeneration, locomotion | PD-1 blockade reversed lactate-associated effects | Lactate has non-histone effects; mark-specific rescue boundary retained | M19B-O020 | EXTRACTED |
| M19B-PERT016 | M19A-P024-E001 | H4K12la/Spp1 | Metabolic manipulation, rSPP1, C646 comparison | Mouse SCI microglia | SPP1, neuronal maturation, axonal mitochondria, function | SPP1 validation improved recovery | Writer identity and causal mark deposition require upgrade | M19B-O021 | EXTRACTED / SOURCE-PAGE |
| M19B-PERT017 | M19A-P025-E001 | Glis1/p300/H3K18la | Glis1 manipulation | Mouse SCI neurons | SCG2, lactate metabolism, senescence | Reduced neuronal senescence and altered SCG2 program | Full-text quantitative extraction pending | M19B-O022 | EXTRACTED / SOURCE-PAGE |
| M19B-PERT018 | M19A-P029-E001 | CTCF | Neuronal conditional deletion | Mouse DRG regeneration comparator | Chromatin organization and regeneration | CTCF deletion impaired nerve regeneration | Comparator, not direct SCI evidence | M19B-O025 | EXTRACTED |
| M19B-PERT019 | M19A-P030-E001 | HDAC5 | Axotomy, EGTA, and Hdac5 knockout | Mouse DRG peripheral injury comparator | Ac-H3 and axon regeneration | Injury increased Ac-H3 through HDAC5 export; EGTA blocked response | Peripheral versus central injury boundary | M19B-O026 | EXTRACTED |
| M19B-PERT020 | M19A-P031-E001 | EZH2 | Post-injury gain-of-function and catalytic mutant | Mouse optic-nerve injury comparator | Axon regeneration | Ezh2 overexpression promoted regeneration | Catalytic and non-catalytic contributions separated | M19B-O027 | EXTRACTED |

## Query Readiness Requirements

- Mark queries must distinguish global abundance, locus occupancy, and inferred chromatin activity.
- Writer, eraser, and reader relationships must remain distinct edge types.
- A mark-to-gene relationship needs locus and assay provenance before being treated as causal.
- Histone-modification phenotypes must retain cell type, stimulus, injury, and time boundaries.
- Contradictory mark functions and context-specific enzyme effects must remain queryable rather than overwritten.
