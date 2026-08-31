# Module 17A: TLR Signaling Cascade and Innate Receptor Pathway Architecture - Corpus Building Tracker

## Overview

This module assembles experiment-level evidence for Toll-like receptor (TLR) signaling from receptor engagement through adaptor routing, compartment-specific trafficking, proximal kinases, transcription factors, feedback regulators, pathway intersections, and phenotypes. It is designed to answer pathway questions that cannot be answered reliably from a paper list alone:

- Which pathway or pathways contain protein X?
- Where does protein X intersect with receptor Y?
- Which TLRs signal to transcription factor X, under which ligand, compartment, and cell-state conditions?
- What phenotypes follow knockout, knockdown, inhibition, activation, or rescue of a node?
- Which edges are direct, which are inferred from perturbation, and which are only review-level context?

Module 12 remains the primary home for innate conditioning, tolerance, and LPS-preconditioning evidence. Module 17 cross-indexes those papers when they provide receptor-to-cascade evidence, without duplicating paper records.

**Status**: SATURATED / FROZEN FIRST PASS; TARGETED FULL-TEXT UPGRADES QUEUED.

## Scope Boundaries

| Boundary ID | Include | Exclude / Route Elsewhere | Notes |
|---|---|---|---|
| M17A-B001 | TLR1/2, TLR2/6, TLR3, TLR4, TLR5, TLR7, TLR8, TLR9, and species-specific TLRs when experimentally relevant | General pattern-recognition receptor biology with no TLR edge or intersection | Preserve species-specific receptor repertoires and ligand boundaries. |
| M17A-B002 | Ligand, co-receptor, receptor compartment, sorting adaptor, proximal adaptor, kinase, transcription-factor, negative-feedback, and effector evidence | A receptor is not assigned a downstream node solely because a review lists it in a pathway | Every edge must carry evidence type and context. |
| M17A-B003 | Knockout, conditional knockout, knockdown, inhibitor, agonist, antagonist, overexpression, mutation, rescue, and epistasis experiments | Unqualified expression correlations as proof of pathway membership | Perturbation specificity and cell compartment are mandatory fields. |
| M17A-B004 | Intersections with IL-1R/IL-18R, NOD, RIG-I-like, cGAS-STING, cytokine/JAK-STAT, PI3K-AKT, inflammasome, autophagy, and cell-death pathways | Unbounded pathway catalogs without a TLR anchor | Store intersections as directed edges with context, not as a flat overlap list. |
| M17A-B005 | Molecular, cellular, tissue, behavioral, and safety phenotypes in SCI and comparator systems | Treating non-SCI comparator phenotypes as direct SCI evidence | Model, species, injury, and translation boundaries remain explicit. |

## Cascade Layer Map

| Layer | Required extraction objects | Representative examples |
|---|---|---|
| Receptor and ligand | Receptor, co-receptor, ligand, agonist, antagonist | TLR2/TLR1, TLR2/TLR6, TLR3, TLR4/MD-2/CD14, TLR7/8/9 |
| Compartment and trafficking | Surface/endosome, internalization, sorting adaptor | TIRAP/MAL, TRAM, endocytosis, endosomal TLR routing |
| Proximal adaptors | Recruitment and assembly evidence | MyD88, TICAM1/TRIF, TIRAP, TRAM |
| Kinase relays | Activation, phosphorylation, inhibitor or knockout evidence | IRAK4, IRAK1, TRAF6, TAK1, TBK1, IKKepsilon, IKK complex, MAPKs |
| Transcriptional outputs | Direct or perturbation-supported transcription factor routing | NF-kappaB, AP-1, IRF3, IRF5, IRF7, STAT1, STAT3 |
| Feedback and resolution | Negative regulators and tolerance mechanisms | MyD88S, IRAK-M, A20/TNFAIP3, SOCS1, phosphatases, IL-10 |
| Intersections | Shared nodes, branch points, convergence, divergence | IL-1R, NOD, RIG-I, STING, PI3K-AKT, inflammasome, autophagy |
| Phenotype | Perturbation-linked outcome | Cytokines, microglial state, oligodendrocytes, axons, lesion, locomotion, pain, survival |

## Corpus and Wide-Net Search Inventory

| Paper ID | Source Module Record | TLR / Cascade Focus | Evidence Role | Status |
|---|---|---|---|---|
| M17A-P001 | M12A-P001 | TLR4 preconditioning, resident microglia, IL-10/IRF3 | SCI conditioning phenotype | INDEXED / SOURCE MODULE |
| M17A-P002 | M12A-P005 | TLR signaling redirection, TRIF-IRF3 tolerance | Ischemic comparator mechanism | INDEXED / SOURCE MODULE |
| M17A-P003 | M12A-P008 / M13A-P012 | TLR4 deficiency and oligodendrocyte formation | SCI knockout phenotype | INDEXED / SOURCE MODULE |
| M17A-P004 | M12A-P027 | MyD88-biased trained-immunity routing | Adaptor convergence comparator | INDEXED / SOURCE MODULE |
| M17A-P005 | M12A-P031 | TLR2 TIR-domain binding to MyD88 | Receptor-adaptor structural edge | INDEXED / SOURCE MODULE |
| M17A-P006 | M12A-P032 | TLR2 MyD88 TIR assembly | Myddosome mechanism | INDEXED / SOURCE MODULE |
| M17A-P007 | M12A-P033 | TLR2/TIRAP/MyD88 and TLR3/TRIF pathway map | Review boundary | BOUNDARY ONLY |
| M17A-P008 | M12A-P035 | TLR4 endocytosis, TRAM, and TRIF | Compartment-specific edge | INDEXED / SOURCE MODULE |
| M17A-P009 | M12A-P039 | MyD88 alternative splicing and NF-kappaB feedback | Negative-regulator mechanism | INDEXED / SOURCE MODULE |
| M17A-P010 | M12A-P045 | TLR2/TLR4 IL-10 mRNA stability comparison | Branch-output intersection | INDEXED / SOURCE MODULE |
| M17A-P011 | M12A-P029 | TLR2 and PI3K-AKT neuroprotection | Survival-pathway intersection | INDEXED / SOURCE MODULE |
| M17A-P012 | M12A-P048 | TLR2/MAPK/NF-kappaB endothelial barrier signaling | Cell-type-specific intersection | INDEXED / SOURCE MODULE |
| M17A-P013 | PMID 17403033; Kigerl et al. | SCI increases TLR1/2/4/5/7 and MyD88/NF-kappaB; TLR2 knockout and TLR4-mutant phenotypes | Direct SCI receptor-phenotype study | EXTRACTED / ABSTRACT |
| M17A-P014 | PMID 25990044 | TLR4 deficiency after SCI increases NF-kappaB/inflammatory injury while reducing IRF3/IFN-beta | Direct SCI branch-balance study | EXTRACTED / ABSTRACT |
| M17A-P015 | PMC3622773 | Intrathecal TLR2, TLR3, and TLR4 ligands separate TNF-dependent and TRIF/IFN-beta spinal outputs | Primary spinal signaling comparator | EXTRACTED / FULL-TEXT |
| M17A-P016 | JCI Insight 2019; doi:10.1172/jci.insight.134552 | TLR3 agonism with poly(I:C) is neuroprotective after zebrafish spinal cord lesion | SCI receptor-activation phenotype | EXTRACTED / SOURCE-PAGE |
| M17A-P017 | doi:10.1016/j.nbd.2012.12.012 | TLR9 antagonist reduces SCI pain hypersensitivity and inflammatory response | Direct SCI antagonist study | EXTRACTED / ABSTRACT |
| M17A-P018 | PMCID PMC10352897 | TBK1 inhibition changes astrocyte YAP, IRF3, and noncanonical NF-kappaB outputs after SCI | Downstream kinase convergence | EXTRACTED / FULL-TEXT |
| M17A-P019 | PMCID PMC7935532 | TLR7 expression and knockout shape antiviral humoral immunity in spinal cord infection | Viral comparator; not sterile SCI evidence | BOUNDARY ONLY |
| M17A-P020 | Search gap | TLR5/8-specific causal signaling and RIG-I/MDA5 intersection in sterile traumatic SCI | Residual receptor/branch gap after confirmation search | SEARCHED / NO NEW SCI CATEGORY |

## Experiment-Level Extraction Table

| Experiment ID | Paper ID | Figure/Table Ref | Species / Strain | TLR | Ligand / Stimulus | Perturbation | Cell / Compartment | Receptor Compartment | Adaptor Route | Kinase Relay | Transcription Factor | Intersection | Phenotype | Evidence Type | Extraction Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M17A-P001-E001 | M17A-P001 | Pending full extraction | As reported | TLR4 | LPS | Conditioning / comparator as reported | Resident microglia and SCI tissue | As reported | MyD88/TRIF to be resolved | As reported | IRF3/NF-kappaB to be resolved | IL-10 and endothelial relay | Tissue and locomotor outcomes | Primary experiment | QUEUED |
| M17A-P013-E001 | M17A-P013 | Abstract; Figs. as reported | C3H/HeJ TLR4-mutant, TLR2-null, and wild-type mice | TLR2/TLR4; endogenous injury ligands unresolved | SCI | TLR2 knockout or TLR4 signaling-defective mutation | Spinal cord, glia, macrophage compartment | Surface receptor; trafficking not resolved | MyD88/NF-kappaB-associated injury response | MyD88/NF-kappaB | TLR4-mutant and TLR2-null mice had impaired locomotor recovery with altered demyelination, astrogliosis, and macrophage activation | Myelin sparing and inflammation | Primary SCI experiment | EXTRACTED / MEDIUM |
| M17A-P014-E001 | M17A-P014 | Abstract; 24 h endpoint | TLR4-deficient and wild-type mice | TLR4 | SCI vascular-clip injury | TLR4 knockout/deficiency | Injured spinal cord; glia and neurons | Surface/endosomal branch not resolved | MyD88-associated NF-kappaB and TRIF-associated IRF3 | NF-kappaB, IRF3 | TLR4 deficiency worsened motor dysfunction, neuronal death, TNF/IL-1beta, gliosis, iNOS, and oxidative injury while reducing p-IRF3 and IFN-beta | Acute tissue injury and apoptosis | Primary SCI knockout experiment | EXTRACTED / MEDIUM |
| M17A-P015-E001 | M17A-P015 | Primary spinal-cell and intrathecal ligand experiments | Mouse spinal microglia, astrocytes, and intact mice | TLR2, TLR3, TLR4 | HKLM, poly(I:C), LPS | Tnf-null, Trif-null, or type-I-IFN-receptor-deficient backgrounds; IFN-beta rescue | Spinal glia and nociceptive circuits | TLR2/4 surface; TLR3 endosomal | TIRAP/MyD88 versus TRIF | TNF, IFN-beta | TLR2/4 ligand effects were TNF-dependent; TLR3 ligand effects were distinct; loss of TRIF or IFN signaling prolonged allodynia, and IFN-beta relieved TLR2/4 effects | Pain hypersensitivity and spinal cytokines | Primary comparator experiment | EXTRACTED / HIGH |
| M17A-P016-E001 | M17A-P016 | Fig. 3 and linked behavioral figures | Zebrafish spinal cord lesion | TLR3 | Poly(I:C) | TLR3 agonist or pharmacologic inhibitor | Injured spinal cord and neurons | Endosomal | TRIF branch inferred from receptor identity; direct adaptor test not reported | Neuroprotective output; TF unresolved | Poly(I:C) increased neuron volume and swimming distance, whereas TLR3 inhibition reduced neuroprotection and locomotor activity | Neuron preservation and locomotion | Primary SCI experiment | EXTRACTED / MEDIUM |
| M17A-P017-E001 | M17A-P017 | Abstract; behavioral and inflammatory endpoints | Mouse traumatic SCI | TLR9 | Endogenous DNA danger signal presumed; ligand not isolated | TLR9 antagonist | Injured spinal cord and pain circuitry | Endosomal | MyD88 route not directly resolved | Inflammatory cytokines unresolved | TLR9 antagonism reduced pain hypersensitivity and inflammatory response; locomotor benefit was not established | Chronic pain and inflammation | Primary antagonist experiment | EXTRACTED / MEDIUM |
| M17A-P018-E001 | M17A-P018 | Figs. 1-7; inhibitor and histology assays | Mouse SCI; primary astrocytes and microglia | TLR receptor not directly assigned | Injury-associated innate activation | TBK1 inhibitor ALX | Astrocytes, microglia, injured spinal cord | Not receptor-specific | TBK1 relay | IRF3, YAP, noncanonical NF-kappaB | TBK1/YAP inhibition reduced reactive astrocyte proliferation, IL-6/IL-1beta, inflammatory infiltration, and IRF3 phosphorylation | Neuroinflammation and recovery environment | Primary downstream-kinase experiment | EXTRACTED / HIGH |
| M17A-P019-E001 | M17A-P019 | FACS and TLR7-knockout infection assays | Mouse EV71 spinal infection model | TLR7 | Viral RNA/infection | TLR7 knockout | Spinal cord immune and neuronal compartments | Endosomal | MyD88 branch expected; not directly resolved in captured extraction | Antiviral humoral output | Microglia were the major TLR7-expressing spinal myeloid population; TLR7 supported antiviral humoral immunity | Infection-specific immune phenotype | Primary comparator experiment | EXTRACTED / MEDIUM |
| M17A-P005-E001 | M17A-P005 | Structural/biochemical assay | Receptor-adaptor comparator | TLR2 | TIR-domain interaction | Binding and specificity assay | Purified or reconstituted signaling domains | Surface receptor context | MyD88 recruitment | Downstream kinase not tested | MyD88 binding specificity | Receptor-adaptor edge | Structural/biochemical experiment | EXTRACTED / MEDIUM |
| M17A-P006-E001 | M17A-P006 | Structural assembly assay | Receptor-adaptor comparator | TLR2 | TIR-domain interaction | Assembly/mutation comparison | Reconstituted TLR2-MyD88 signaling components | Surface receptor context | MyD88/Myddosome assembly | Downstream output as reported | Receptor-proximal signaling competence | Structural mechanism | EXTRACTED / MEDIUM |
| M17A-P009-E001 | M17A-P009 | Splicing and signaling assays | Innate signaling comparator | TLR/IL-1R MyD88 pathway | Innate stimulation | MyD88S alternative splice isoform | Innate immune cells | Surface/endosomal receptor not assigned | MyD88S fails IRAK4 recruitment | NF-kappaB | Attenuated inflammatory signaling and feedback | Negative regulation | Primary mechanism | EXTRACTED / HIGH |
| M17A-P010-E001 | M17A-P010 | Transcript stability assays | Macrophage comparator | TLR2/TLR4 | Receptor-specific agonists | Receptor/ligand comparison | Macrophages | Surface receptor | MyD88-associated route | IL-10 output | Differential IL-10 mRNA stability | Branch-specific output | Primary comparator experiment | EXTRACTED / MEDIUM |
| M17A-P011-E001 | M17A-P011 | Neuronal injury and pathway assays | Ischemic brain and ex vivo SCI comparator | TLR2 | Pam3CSK4 | Agonist and pathway inhibition | Neurons and spinal tissue | Surface receptor | MyD88; PI3K-AKT intersection | AKT and survival program | Reduced neuronal injury in a context- and timing-dependent manner | Neuroprotection | Primary comparator experiment | EXTRACTED / MEDIUM |

## Cross-Module Experiment Ledger

These rows promote already extracted source-module experiments into Module 17's receptor-to-cascade index. The primary experiment remains owned by its source module; this ledger preserves the TLR-specific query handle without duplicating the paper record.

| Cross-Index Experiment | Source Experiment | TLR / Cascade Handle | Model / Context | Perturbation or Comparison | Finding Relevant to Module 17 | Source Status |
|---|---|---|---|---|---|---|
| M17A-X001 | M12A-P001-E001 | TLR4 -> microglial IL-10/IRF3 | Mouse thoracic contusion SCI | Systemic low-dose LPS 48 h pre-injury | TLR4 preconditioning shifted resident microglia toward an IL-10/IRF3-associated repair state with tissue and locomotor benefit. | SOURCE FULL-TEXT / MEDIUM |
| M17A-X002 | M12A-P002-E001 | TLR4 -> spinal microglia/endothelium | Spinal cord ischemia | Repeated systemic LPS | Repeated LPS primed spinal microglia/endothelium and protected against ischemic injury; IL-1 cross-talk is a boundary. | SOURCE FULL-TEXT / HIGH |
| M17A-X003 | M12A-P003-E001 | TLR4 -> IL-1R1 relay | Spinal ischemia | Repeated LPS and IL-1R1 testing | Repeated LPS protection involved spinal microglia-vascular communication through IL-1R1. | SOURCE FULL-TEXT / HIGH |
| M17A-X004 | M12A-P005-E001 | TLR4 -> TRIF/IRF3 tolerance | Brain ischemia comparator | LPS preconditioning; TRIF/IRF3 comparisons | Tolerance was redirected toward TRIF-IRF3 with altered NF-kappaB output rather than simple pathway suppression. | SOURCE FULL-TEXT / HIGH |
| M17A-X005 | M12A-P007-E001 | TLR4 -> endothelial MyD88/CXCL10 | Brain ischemia comparator | Peripheral LPS preconditioning | Endothelial MyD88/CXCL10 acted as an upstream regulatory relay for CNS protection. | SOURCE SOURCE-PAGE / MEDIUM |
| M17A-X006 | M12A-P008-E001 | TLR4 -> oligodendrocyte formation | Traumatic SCI | TLR4 deficiency | TLR4 deficiency impaired oligodendrocyte formation and recovery-associated myelin biology. | SOURCE SOURCE-PAGE / MEDIUM |
| M17A-X007 | M12A-P009-E001 | TLR4-associated post-injury LPS response | Traumatic SCI | LPS plus indomethacin after injury | Post-injury LPS treatment improved repair and locomotion in a context distinct from preconditioning. | SOURCE SOURCE-PAGE / MEDIUM |
| M17A-X008 | M12A-P010-E001 | TLR4-associated chronic microglial reactivation | Chronic SCI | LPS challenge after chronic injury | Chronic SCI microglia remained inducible; LPS reawakened inflammatory and plasticity-linked states. | SOURCE SOURCE-PAGE / MEDIUM |
| M17A-X009 | M12A-P011-E001 | TLR4 -> hemorrhage-dependent microglial activation | Hemorrhagic/compressive SCI | Lesion-context comparison | TLR4 expression and microglia/macrophage activation varied with hemorrhagic injury context. | SOURCE SOURCE-PAGE / MEDIUM |
| M17A-X010 | M12A-P025-E001 | TLR4 preconditioning -> apoptosis control | Traumatic SCI | Systemic LPS 72 h pre-injury | Low-dose LPS preconditioning reduced apoptotic and neuropathologic readouts. | SOURCE ABSTRACT / MEDIUM |
| M17A-X011 | M12A-P026-E001 | TLR4 preconditioning -> Nrf2 | Traumatic SCI | Systemic LPS pre-injury | LPS preconditioning was linked to Nrf2/antioxidant signaling and recovery. | SOURCE ABSTRACT / MEDIUM |
| M17A-X012 | M12A-P027-E001 | MyD88-biased trained immunity | Macrophage comparator | MPLA, CpG, Poly(I:C), MyD88/TRIF perturbation | Durable MPLA training required MyD88 and persisted in TRIF-deficient macrophages; Poly(I:C) did not reproduce it. | SOURCE FULL-TEXT / HIGH |
| M17A-X013 | M12A-P028-E001 | TLR2/1 -> CNS preconditioning | Brain ischemia comparator | Systemic Pam3CSK4 | TLR2/1 agonism reduced infarct, edema, barrier leakage, and neurologic injury. | SOURCE FULL-TEXT / HIGH |
| M17A-X014 | M12A-P029-E001 | TLR2 -> PI3K-AKT | Brain ischemia comparator | Pam3CSK4 with TLR2/PI3K-AKT perturbations | Protection required TLR2 and PI3K-AKT-associated survival signaling. | SOURCE FULL-TEXT / HIGH |
| M17A-X015 | M12A-P030-E001 | TLR2/1 -> spinal tissue protection | Ex vivo SCI | Pam3CSK4 after injury | TLR2/1 agonism reduced axonal dieback and oligodendroglial loss ex vivo; route and timing remain bounded. | SOURCE SOURCE-PAGE / MEDIUM |
| M17A-X016 | M12A-P031-E001 | TLR2 TIR -> MyD88 binding | Receptor-domain comparator | Cytoplasmic-domain binding assays | TLR2 TIR-domain binding specificity supports MyD88 as the proximal adaptor. | SOURCE SOURCE-PAGE / MEDIUM |
| M17A-X017 | M12A-P032-E001 | TLR2 TIR -> MyD88 assembly | Structural comparator | TIR-domain assembly | TLR2 TIR domains nucleated higher-order MyD88 assemblies. | SOURCE SOURCE-PAGE / MEDIUM |
| M17A-X018 | M12A-P035-E001 | TLR4 -> TRAM/TRIF | Receptor-trafficking comparator | LPS-induced endocytosis | TRAM coupled TLR4 endocytosis to IFN-beta induction, supporting a surface-to-endosome signaling pivot. | SOURCE FULL-TEXT / HIGH |
| M17A-X019 | M12A-P038-E001 | TLR4 compartment -> pathway output | Endocytic signaling comparator | Endocytosis pathway perturbation | Endocytic routing altered TLR4 signaling outputs. | SOURCE SOURCE-PAGE / MEDIUM |
| M17A-X020 | M12A-P039-E001 | MyD88 -> alternative splicing/NF-kappaB feedback | Mouse macrophages | LPS stimulation and MyD88/TRIF/NF-kappaB comparisons | LPS-induced MyD88 alternative splicing created a measurable negative-regulatory layer. | SOURCE FULL-TEXT / HIGH |
| M17A-X021 | M12A-P040-E001 | MyD88S -> reduced IRAK4 recruitment | Signaling comparator | MyD88S versus full-length MyD88 | MyD88S inhibited TLR/IL-1R signaling because it failed to recruit IRAK4. | SOURCE SOURCE-PAGE / MEDIUM |
| M17A-X022 | M12A-P043-E001 | TLR2 -> IL-10/sphingolipid resolution | TLR2 macrophage comparator | Pam3CysK4-linked IL-10 context | IL-10 constrained sphingolipid metabolism in TLR2-activated macrophages. | SOURCE SOURCE-PAGE / MEDIUM |
| M17A-X023 | M12A-P045-E001 | TLR2 versus TLR4 -> IL-10 mRNA stability | Bone-marrow-derived macrophages | Receptor-specific activation comparison | TLR4/TRIF/p38 stabilized Il10 mRNA more strongly than TLR2, separating shared proximal signaling from branch-specific output. | SOURCE FULL-TEXT / HIGH |
| M17A-X024 | M12A-P046-E001 | TLR4 -> endothelial tolerance | Human HUVECs | MPLA priming, LPS challenge, MyD88/TRIF knockdown | MPLA induced endothelial tolerance; the reported tolerance phenotype was MyD88-dependent rather than TRIF-dependent. | SOURCE FULL-TEXT / HIGH |
| M17A-X025 | M12A-P047-E001 | TLR4/MPLA -> endothelial cytokine modulation | Human HUVECs | MPLA, LPS, and combined exposure | MPLA weakly stimulated cytokines and reduced LPS-induced endothelial cytokine/chemokine output. | SOURCE FULL-TEXT / HIGH |
| M17A-X026 | M12A-P048-E001 | TLR2 -> MAPK/NF-kappaB endothelial output | Primary brain microvascular endothelial cells | Pam3CSK4 and pathway inhibition | TLR2 activation regulated MMP-2/9 and tight-junction-associated outputs, creating a barrier-risk boundary. | SOURCE FULL-TEXT / HIGH |
| M17A-X027 | M13A-P018-E001 | TLR4-associated chronic microglial reactivation | Chronic SCI | LPS challenge after chronic injury | LPS reactivated diverse chronic microglial states, supporting a persistent but context-dependent TLR4-responsive lesion state. | SOURCE SOURCE-PAGE / MEDIUM |

## Wide-Net Search Phases and Saturation Record

| Phase | Search focus | New categories added | Saturation interpretation |
|---|---|---|---|
| 1 | Cross-module inventory plus TLR receptor/adaptor/kinase queries | TLR2/TLR4 SCI phenotypes, TLR3/TRIF, TLR4/TRAM, MyD88 and PI3K-AKT intersections | Added direct receptor-to-phenotype and compartment-routing categories. |
| 2 | TLR3/7/9, TBK1/IRF3, TLR9 pain, and SCI repair searches | TLR3 neuroprotection, TLR9 pain modulation, TBK1/IRF3/YAP convergence, antiviral TLR7 boundary | No unrepresented core cascade layer remained. |
| 3 | Confirmation searches for TLR5/8, RIG-I/MDA5, and repeat receptor-branch combinations | No new sterile-SCI mechanistic category; TLR5/8 and RIG-I/MDA5 remain underrepresented | Practical saturation reached with explicit evidence gaps retained. |

## Saturation Checklist

- Receptor branches covered by direct or comparator evidence: TLR2, TLR3, TLR4, TLR7, and TLR9.
- Adaptor/trafficking layers covered: MyD88, TIRAP, TRAM, TRIF, and endosomal routing.
- Downstream relays covered: IRAK/TRAF6/TAK1 context, TBK1/IRF3, NF-kappaB, MAPK, STAT/IFN, and PI3K-AKT intersections.
- Direct SCI causal gaps retained: TLR5/8-specific perturbation, sterile-SCI TLR7 signaling, and RIG-I/MDA5-MAVS intersection.
- Two confirmation phases added no new mechanistic category; module frozen for first-pass graph consolidation.

## Required Extraction Fields

Every full-text upgrade should capture: receptor and ligand identity; co-receptors; surface versus endosomal compartment; adaptor recruitment; kinase and transcription-factor evidence; perturbation type and specificity; cell type; species; injury or comparator model; timing and dose; molecular/cellular/tissue/behavioral phenotypes; rescue or epistasis results; direct versus inferred edge status; and figure/section provenance.

## Boundary Notes

- TLR pathway membership is context-dependent when receptor trafficking, ligand, cell type, or species changes.
- A knockout phenotype supports necessity only for the tested context; it does not establish that every ligand or cell type uses the same route.
- Review diagrams are pathway maps, not primary evidence for a directed edge.
- Module 17 should preserve contradictory edges rather than collapsing them into a single canonical pathway.
