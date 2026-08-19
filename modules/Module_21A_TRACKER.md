# Module 21A: Cytokine, Chemokine, Growth-Factor, and gp130-Family Relay Signaling - Pathway-Graph Corpus Building Tracker

## Overview

This module curates the intracellular relay logic downstream of secreted-signal receptor engagement. It is the main bridge between Module 20 ligand-receptor curation and the receiver-state program logic needed by `mSCS`.

**Status**: ACTIVE FIRST-PASS RELAY INTAKE / HIGH PRIORITY FOR `mSCS`.

## Core Questions

- Once a receptor is engaged, which adaptor, kinase, and transcription-factor branches are actually supported?
- Which branches are context-dependent by ligand, cell type, or compartment?
- Which pathways converge on the same receiver TFs?
- Which branches are best supported in mouse versus only in human or comparator systems?

## Priority Relay Families

- IL6/LIF/OSM/CNTF -> JAK/STAT
- IFN -> JAK/STAT/IRF
- TNF -> NF-kappaB/MAPK/cell-death branches
- IL1 -> MyD88/NF-kappaB/MAPK
- chemokine receptor GPCR signaling
- BMP/TGF-beta -> SMAD and noncanonical branches
- EGF/FGF/PDGF/VEGF -> ERK/AKT/SRC and related relay logic
- WNT -> beta-catenin and noncanonical branches
- Notch -> NICD/RBPJ/HES/HEY logic

## Scope Boundaries

| Boundary ID | Include | Exclude / Route Elsewhere | Notes |
|---|---|---|---|
| M21A-B001 | Receptor-to-adaptor-to-kinase-to-TF logic for secreted-signal pathways | Ligand-receptor binding itself | Binding belongs in Module 20. |
| M21A-B002 | Canonical and noncanonical branches when experimentally distinguished | Flattening all pathway branches into a single generic edge | Branch structure matters for simulation. |
| M21A-B003 | Cell-type or compartment-specific branch logic when supported | Assuming the same downstream route in all cells | Keep context explicit. |
| M21A-B004 | Cross-talk and branch intersections when experimentally grounded | Review-only cascade expansion without edge support | Preserve review context separately. |

## Required Extraction Objects

- receptor branch identity
- adaptor and kinase steps
- TF outputs
- branch-specific inhibitors, knockouts, or rescue evidence
- species support
- direct edge versus contextual support distinction

## First-Pass Relay Packet: IL-6/gp130/JAK/STAT3

The first curated relay packet is stored under `work/module21_relay/module21a_il6_family_batch1_*`.

| Edge family | Current evidence posture | Main boundary |
|---|---|---|
| IL-6 receptor complex -> JAK1 | Retained as a high-confidence, primary perturbation-supported kinase requirement in the tested human cell system. | Do not generalize JAK1 dominance to every gp130-family ligand or cell type. |
| IL-6 receptor complex -> JAK2/TYK2 | Retained as activated ancillary kinase branches. | JAK2/TYK2 activation does not establish a sequential three-kinase cascade or JAK1 equivalence. |
| IL6ST/gp130 -> STAT3 | Retained as the canonical gp130-to-STAT3 branch with human biochemical and mouse genetic support. | Mouse evidence is mammary/acute-phase comparator evidence, not SCI-specific. |
| IL6ST/gp130 -> SHP2/PTPN11 -> GRB2/MAPK | Retained as a distinct SHP2/MAPK branch with gp130 Tyr759 and receptor-crosstalk context. | Do not flatten SHP2/MAPK into the STAT3 route; EGFR crosstalk can contribute to STAT3 activation. |

### First-pass decision

The IL-6/gp130 relay is ready for continued family expansion, not yet for unrestricted astrocyte simulation. The next required slice is LIFR/OSMR/CNTFR receptor-complex comparison with explicit gp130-sharing and branch-specific evidence.

## First-Pass Saturation Packet: All Priority Families

The bounded saturation packet is stored under `work/module21_relay/module21a_saturation_*`.

| Family | Canonical relay coverage | Explicit branch or boundary | Posture |
|---|---|---|---|
| IL6/LIF/OSM/CNTF-gp130 | IL-6 receptor -> JAK1/STAT3; LIFR-gp130 and OSMR-gp130 -> JAK/STAT3 | OSMR-specific STAT5B; gp130 SHP2/GRB2/MAPK; JAK2/TYK2 ancillary activation | Saturated first pass; CNTFR-specific evidence remains open |
| IFN-alpha/beta/gamma | IFNAR -> JAK1/TYK2 -> STAT1/STAT2/ISGF3; IFNGR -> JAK1/JAK2 -> STAT1 | IFN-gamma Pyk2/ERK branch; IFN-lambda kept separate | Saturated first pass; astrocyte-specific weighting remains open |
| TNF | TNFR1 -> TRADD -> TRAF2/NF-kappaB and FADD/CASP8; RIPK1 complex | TRADD-independent RIPK1 necrosis boundary | Saturated first pass; TNFR2 remains open |
| IL-1 | IL1R1/IL1RAP -> MyD88 -> IRAK4/IRAK1 -> TRAF6/TAK1 -> NF-kappaB/JNK | MyD88S inhibitory isoform | Saturated first pass; IL-1R2 remains open |
| Chemokine GPCR | CXCL12-CXCR4-Gi -> PI3K/AKT and ERK | Src-EGFR transactivation | Saturated first pass; broader CCL/CCR coverage remains open |
| BMP/TGF-beta | TGFBR -> SMAD2/3-SMAD4; BMPR -> SMAD1/5/9-SMAD4 | Noncanonical MAPK/PI3K/RHO branches bounded | Saturated first pass; noncanonical and SCI cell-type evidence remain open |
| EGF/FGF/PDGF/VEGF RTK | EGFR-Shc-Grb2-Sos-Ras-ERK; FGFR-FRS2; PDGFR-PI3K; VEGFR2-PLC/ERK and PI3K/AKT | Adaptor-specific PI3K/SRC/PLC branches | Saturated first pass; receptor-paralog and SCI receiver mapping remain open |
| WNT | FZD-LRP6-DVL signalosome -> beta-catenin-TCF | Noncanonical PCP/JNK and WNT-Ca2+ bounded | Saturated first pass; noncanonical branch remains open |
| Notch | Ligand-triggered processing -> NICD-RBPJ/CSL -> HES1/HEY1 | Noncanonical Notch outputs bounded | Saturated first pass; ligand/paralog-specific weights remain open |

### Saturation decision

The module is now saturated for a bounded first-pass relay corpus: 57 directed edges, 14 source-group evidence records, and 17 perturbation records. This means every priority family has canonical receptor-to-adaptor/kinase-to-TF or transcriptional-output coverage plus at least one experimentally distinguished branch or explicit unresolved boundary. It does not mean every receptor paralog, ligand bias, noncanonical branch, or SCI cell-state weight is resolved.

The packet remains pre-materialization. No SQL `SignalingEdge` rows are created until complex-level nodes, source registration, species context, and branch semantics are reconciled against Modules 20A, 15B, 17B, and 18B.

### Export boundaries

- Comparator evidence is not used to assign SCI astrocyte branch weights.
- Complex-level nodes such as ISGF3, destruction complexes, and NICD-RBPJ are intentional modeling abstractions and require consistent decomposition if materialized.
- Low-priority ancillary or receptor-specific branches should not drive receiver-state predictions without matched context.
- The next handoff is cross-module reconciliation and candidate export of canonical medium-priority edges with evidence context preserved.

## Handoff Goal

Produce simulator-facing pathway relay edges that can connect a ligand-receptor event to candidate TF shifts in receiver astrocytes and other SCI cell states.
