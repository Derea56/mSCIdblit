# Module 23B: ECM and Mechanotransduction Evidence Consolidation - Graph Evidence Linkage and Query Readiness

## Overview

This module converts Module 23A into queryable matrix-to-receptor and adhesion-to-TF graph records.

**Status**: AUDIT LAYER GENERATED / SQL MATERIALIZATION PENDING.

## Second-pass promotion batch (2026-09-04)

The B023 second-pass batch promotes two existing MMRN2-CLEC14A edges and adds five source-linked B edges for MMRN2-CD93, MMRN2-CD248, and the three separated SLIT2 C-terminal LG-domain–glycosylated DAG1 layers. The B register now contains 1,080 edges and the B evidence register contains 1,506 evidence rows; the boundary register is unchanged at 289 rows. These are audit-layer promotions only: canonical signaling tables and simulator outputs remain untouched. Non-SCI vascular/pericyte and developmental spinal-cord comparator limits are explicit.

The subsequent source-backed promotion gate moved 701 additional B edges from `staged`/`staged_primary_review` to `reviewed_supported`. Each passed the one-to-one A mapping and primary-paper evidence gate; the single remaining staged A/B candidate, EFNA3–EPHA2, is held as `held_unresolved_exact_directness` and remains non-exportable. The B register therefore has 773 `reviewed_supported` edges while retaining the directness exception explicitly.

## Consolidation Goals

- preserve extracellular matrix composition and receptor context
- distinguish contact-mediated signaling from soluble ligand signaling
- retain cell-type and compartment boundaries

## Handoff Goal

Provide exportable edges for matrix-sensitive receiver-state transitions in astrocytes, fibroblasts, endothelial cells, and related compartments.
## Review-led expansion: B024 (2026-09-04)

B024 promotes six new 23B edges paired one-to-one with Module 23A: decorin-to-EGFR binding/activation, decorin anti-scarring and axon-growth function in acute rat SCI, and biglycan CD14 binding, TLR2/TLR4/MyD88 relay, TLR2/TLR4–P2X4/P2X7–NLRP3 inflammasome relay, and macrophage inflammatory output. These are audit-layer promotions with review and primary-source lineage; non-SCI comparator scope, intact soluble biglycan, receptor-complex context, and function-only versus receptor-proximal distinctions are retained. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B025 (2026-09-04)

B025 promotes seven new 23B edges paired one-to-one with Module 23A: three tenascin-C FBG/TLR4 layers covering direct binding, TLR4-dependent NF-kappaB/proximal signaling, and macrophage/microglial inflammatory function; and four low-molecular-weight hyaluronan layers covering TLR4-MyD88, TLR4-TRIF/TBK1/IRF3, cPLA2alpha/COX2-eicosanoid, and IFN-beta outputs. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. FBG-domain and fragment-size specificity, adaptor separation, endotoxin controls, non-SCI comparator scope, and the absence of direct HA-TLR4 binding or terminal-TF transfer remain explicit; canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B026 (2026-09-04)

B026 promotes three new 23B edges paired one-to-one with Module 23A for FN-EDA: TLR4-MD2 engagement, TLR4-dependent proximal signaling, and measured fibroblast/myofibroblast and macrophage inflammatory-fibrotic output. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. EDA-domain and MD-2 requirements, comparator-only scope, no structural DAMP-receptor claim, and the absence of traumatic-SCI or terminal-TF transfer remain explicit; alpha4beta1 cooperation was identified but not promoted without locally acquired full text. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B027 (2026-09-04)

B027 promotes four new 23B edges paired one-to-one with Module 23A for SPARC: direct TLR4 binding, TLR4-TBK1-IRF3 proximal signaling, the IFN-beta-IFNAR-STAT1 relay, and measured IRF3/IRF7-dependent macrophage interferon/inflammatory output. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. SCI extracellular-proteome abundance is retained as context, while aging/obesity macrophage comparator scope, no MD-2 or structural receptor-complex claim, and the absence of traumatic-SCI causal transfer remain explicit. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B028 (2026-09-04)

B028 promotes four new 23B edges paired one-to-one with Module 23A for galectin-3: TLR4 ligand activity, comparator-specific TLR4-dependent microglial activation, rat SCI ROS/TXNIP/NLRP3/IL-1beta inflammatory output, and mouse SCI Gal3/PDGFRbeta+ fibroblast fibrotic-scar function. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Neuroinflammation comparator scope, separate SCI inflammasome and scar-function evidence, no universal TLR4-to-NLRP3 relay, and no TLR4 mechanism transfer into the SCI scar edge remain explicit. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B029 (2026-09-04)

B029 promotes five new 23B edges paired one-to-one with Module 23A for HMGB1: direct TLR4/MD2 binding, a TLR4-NF-kappaB/MAPK relay, astrocytic CCL5 with myeloid recruitment/M1 output, SCI pro-inflammatory cytokine and microglial NF-kappaB output, and secondary-injury/motor-function output. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Redox, endotoxin, alternate receptor usage, cell-context, human biomarker non-causality, and the absence of a universal adaptor order remain explicit; canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B030 (2026-09-04)

B030 promotes four new 23B edges paired one-to-one with Module 23A for S100A8/A9 calprotectin dimers: direct TLR4/MD2 binding, the TLR4-MyD88-IRAK-1/NF-kappaB/MAPK relay, TNF/IL-8 phagocyte output, and an SCI-associated myeloid context edge. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Dimer/tetramer state, calcium/zinc and protein-preparation limits, RAGE/Mac-1 separation, and the medium-confidence observational/non-causal SCI context remain explicit; canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B031 (2026-09-04)

B031 promotes four new 23B edges paired one-to-one with Module 23A for extracellular histone H3/H4: non-SCI histone H4 direct TLR4/MD2 binding, SCI histone TLR2-YB-1 retrograde relay, SCI neurite/axon-growth inhibition, and observational histone H3 accumulation in injured CNS. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. The TLR4/MD2 result remains a non-SCI histone-H4 comparator; SCI causal evidence is separated at TLR2/YB-1 and neurite-inhibition layers, and the medium-confidence accumulation edge remains observational. Histone subtype, mixed-preparation, cleavage, and injury-model limits remain explicit; canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B032 (2026-09-05)

B032 promotes four new 23B edges paired one-to-one with Module 23A for chondroitin sulfate proteoglycans (CSPGs): TLR4-dependent immune-cell inflammatory activation, macrophage/microglial inflammatory output, SCI immune-cell clearance and inflammation-resolution failure, and TLR4-independent neurite-growth inhibition. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Direct CSPG-TLR4 binding and individual proteoglycan-core assignment remain unresolved; intact CSPG versus GAG digestion, cell-state, and rodent-model limits remain explicit, and neuronal growth inhibition is kept separate from CSPG-TLR4 immune modulation. Canonical signaling tables and simulator outputs remain untouched.
## Review-led expansion: B033 (2026-09-05)

B033 promotes four new 23B edges paired one-to-one with Module 23A for tenascin-R: isolated FBG-R direct TLR4 binding, TLR4-dependent NF-kB activity, macrophage IL-6/IL-8/TNF output, and whole-TNR restriction of selected posttraumatic SCI locomotor recovery with altered synaptic remodeling. FBG-R receptor and cytokine findings remain non-SCI comparator layers, while the SCI genotype result carries no TLR4 mechanism assignment; full-length presentation, motor-task specificity, axonal-regrowth mechanism, and terminal-TF limits remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.
## Review-led expansion: B034 (2026-09-05)

B034 promotes five new 23B edges paired one-to-one with Module 23A for tenascin-R axon-associated interactions: direct TNR-MAG binding, MAG-cell repulsion, direct TNR-F11/CNTN1 domain interaction, enhanced F11-mediated neurite outgrowth, and TNR substrate inhibition of retinal axon growth. MAG/F11 domain resolution, substrate presentation, non-SCI comparator scope, amphibian injury model, and absence of a defined cytoplasmic relay or terminal TF remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B035 (2026-09-05)

B035 promotes six new 23B edges paired one-to-one with Module 23A for tenascin-R lectican/CSPG interactions: direct TNR FNIII3-5 binding to aggrecan, versican, neurocan, and brevican C-type lectin domains, plus full-length TNR binding to neurocan and phosphacan/PTPRZ1 through core-protein interactions. Lectican-domain versus full-length extracellular-domain resolution, rat/recombinant non-SCI CNS comparator scope, and the absence of a downstream relay or traumatic-SCI transfer remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B036 (2026-09-05)

B036 promotes two new 23B edges paired one-to-one with Module 23A for tenascin-R sodium-channel interactions: direct TNR FNIII1-2/6-8 binding to the purified type-IIA rat brain sodium-channel complex and to the beta2 extracellular domain. Exact domain and subunit resolution, proposed channel clustering/localization/activity interpretation, native-complex beta2 mediation, non-SCI comparator scope, and the absence of a downstream relay or traumatic-SCI transfer remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B037 (2026-09-05)

B037 promotes three new 23B edges paired one-to-one with Module 23A for tenascin-R oligodendrocyte interactions: direct TNR-sulfatide binding, TNR-substrate adhesion of O4-positive oligodendrocytes, and TNR-induced myelin-gene expression/terminal differentiation of O4-positive progenitors. Isoform, cell-stage, glycolipid, in-vitro, non-SCI myelination, and no-relay limits remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B038 (2026-09-05)

B038 promotes six new 23B edges paired one-to-one with Module 23A for tenascin-R microglial interactions and reverse expression feedback: activated-microglia antiadhesion, EGF-like/FNIII6-8 domain-specific microglial adhesion/migration effects, domain-specific neurotrophic-factor secretion, and microglia/TNF-alpha-associated oligodendrocyte TNR downregulation. PKA/PKC dependence, peripheral-nerve injury, primary-microglia, in-vitro comparator, reverse-feedback, and no-relay limits remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B039 (2026-09-05)

B039 promotes two new 23B edges paired one-to-one with Module 23A for tenascin-R perineuronal-net organization: TNR-dependent perineuronal-net formation/stabilization and aggrecan clustering as the reported extracellular mechanism. Mouse loss-of-function, organotypic/dissociated-culture, add-back/rescue, and no-traumatic-SCI-transfer limits remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B040 (2026-09-05)

B040 promotes one new 23B edge paired one-to-one with Module 23A for the tenascin-R/RPTPζ perineuronal-net structural interface: ectodomain association and interface-mutagenesis effects support a contribution to PNN architecture. Extracellular interface, mouse neuronal-culture, cytoplasmic-relay boundary, and no-traumatic-SCI-transfer limits remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B041 (2026-09-05)

B041 promotes one new 23B edge paired one-to-one with Module 23A for tenascin-R optic-nerve conduction function: TNR-deficient mice show reduced compound-action-potential conduction velocity despite preserved nodal Na+-channel distribution. In-vivo mouse electrophysiology, non-SCI comparator, and no-channel-organization-transfer limits remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B042 (2026-09-05)

B042 promotes four new 23B edges paired one-to-one with Module 23A for PACAP signaling through the shared VPAC receptor family: direct PACAP association with recombinant VPAC1/VIPR1 and VPAC2/VIPR2, plus VPAC1- and VPAC2-linked Gs/adenylate-cyclase/cAMP relay edges. Historical VIP1/VIP2 nomenclature, shared PACAP/VIP pharmacology, recombinant-system and receptor-state limits, and no-native-SCI or subtype-exclusive downstream transfer remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B043 (2026-09-05)

B043 promotes two new 23B edges paired one-to-one with Module 23A for the S100A8/A9–Mac-1 branch: exact tested-preparation-level Mac-1 activation and Mac-1-dependent neutrophil adhesion/chemotaxis. The primary study’s mixed S100 preparations, antibody-sensitive Mac-1 function, non-SCI inflammatory models, no-direct-binding boundary, and no-native-SCI-transfer limit remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B044 (2026-09-05)

B044 promotes two new 23B edges paired one-to-one with Module 23A for the Sema4A–Plexin-B2 branch: receptor-dependent synaptogenic relay and Plexin-B2-dependent glutamatergic synapse development in rat hippocampal cultures. Plexin-B2 knockdown, soluble mouse Sema4A-Fc, rodent-culture, no-direct-binding, complete-relay, and no-traumatic-SCI-transfer limits remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B045 (2026-09-05)

B045 promotes one new 23B edge paired one-to-one with Module 23A for the EFNA1–EPHA5 branch: ephrin-A1 recombinant-fusion stimulation produces time-dependent EPHA5 tyrosine phosphorylation in human U-118 MG glioblastoma cells. The evidence is retained at the receptor-proximal layer with explicit recombinant-fusion, glioblastoma-cell-line, no-direct-binding, no-neural, and no-traumatic-SCI-transfer limits. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B046 (2026-09-05)

B046 promotes one new 23B edge paired one-to-one with Module 23A for the EFNA1–EPHA8 branch: ephrin-A1-Fc binds EphA8 and induces EphA8/EphA8-TrkB tyrosine phosphorylation in NIH3T3 fibroblast receptor systems. The evidence is retained at the receptor-proximal layer with explicit recombinant-fusion, heterologous-fibroblast, no-downstream-program, no-native-neural, and no-traumatic-SCI-transfer limits. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B047 (2026-09-05)

B047 promotes one new 23B edge paired one-to-one with Module 23A for the EFNA2–EPHA5 branch: EphA5/ephrin-A2 binding context is associated with topographically selective retinal axon repulsion in vitro and normal dLGN mapping in vivo. The evidence is retained at the retinal guidance-function layer with explicit receptor-association rather than receptor-exclusive causality, non-SCI visual-system, no-complete-relay, and no-traumatic-SCI-transfer limits. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B048 (2026-09-05)

B048 promotes the existing EFNA2–EPHA8 binding/activation edge using primary mouse-brain ligand and NIH3T3 receptor-system evidence: the historical Elf-1/Cek7-L ligand represented in the local register by EFNA2 binds and activates Eek/EphA8 and Eek-TrkB. The evidence is retained at the direct-binding and receptor-proximal activation layers with explicit historical-alias, recombinant/heterologous, no-downstream-program, no-native-neural, and no-traumatic-SCI-transfer limits. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B049 (2026-09-05)

B049 promotes one new 23B edge paired one-to-one with Module 23A for VTN–alphaVbeta8 direct binding. Primary affinity-chromatography assays support exact alphaVbeta8 binding to vitronectin in recombinant secreted and intact beta8-expressing cell systems; the direct-binding edge is retained separately from the existing function-only edge because intact alphaVbeta8 did not promote adhesion. The evidence is non-SCI recombinant/heterologous, with no receptor-proximal signaling, neural, or traumatic-SCI transfer asserted. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B050 (2026-09-05)

B050 promotes the existing 23B Sema4A–Plexin-B2 receptor-proximal edge paired one-to-one with Module 23A. Primary activated mouse CD8+ T-cell assays show Sema4A-Fc surface binding reduced by Plexin-B2 blockade and reduced IFN-gamma after Plexin-B2 knockdown. The evidence supports receptor assignment and proximal function at medium-high confidence, without purified binary affinity, a complete Rho-family/mTOR relay, native neural context, or traumatic-SCI transfer. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B051 (2026-09-05)

B051 promotes the existing 23B EFNA2–EPHA5 binding edge paired one-to-one with Module 23A. Primary EphA5-AP affinity-probe labeling of ephrin-A2-expressing fibroblasts and complementary retinal EphA5/ephrin-A2 binding/guidance evidence support the cell-associated direct-binding layer at medium-high confidence. Purified affinity, receptor-exclusive guidance causality, complete intracellular relay, and traumatic-SCI transfer remain unasserted. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B052 (2026-09-05)

B052 promotes the existing 23B EFNA1–EPHA5 binding edge paired one-to-one with Module 23A. Primary exact-pair ephrin-A1-Fc/EphA5-Fc ELISA binding and independent human U-118 MG-cell EPHA5 phosphorylation evidence support the direct-binding and receptor-proximal branch at medium-high confidence. Fc avidity, EphA-class promiscuity, receptor-proximal-only activation, non-neural cell-line context, no-purified-monovalent-affinity, no-downstream-program, and no-traumatic-SCI-transfer limits remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B053 (2026-09-05)

B053 promotes the existing 23B EFNA1–EPHA8 binding edge paired one-to-one with Module 23A. The primary NIH3T3 study reports ephrin-A1-Fc binding and ligand-dependent EphA8/EphA8-TrkB tyrosine phosphorylation, supporting the direct-binding and receptor-proximal branch at medium-high confidence. Recombinant-fusion, heterologous-fibroblast, receptor-proximal-only, no-downstream-program, no-native-neural, and no-traumatic-SCI-transfer limits remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B054 (2026-09-05)

B054 adds two new 23B functional edges paired one-to-one with Module 23A for the EFNA2–EPHA2 branch. Primary mouse bone-remodeling assays support EFNA2/EphA2-associated enhancement of osteoclast differentiation and EphA2-associated suppression of osteoblast differentiation. The downstream function is promoted at medium-high confidence with explicit reverse/forward directional limits, mouse comparator context, no-purified-binding, incomplete-ordering, and no-traumatic-SCI-transfer boundaries. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B055 (2026-09-05)

B055 promotes two existing 23B binding edges paired one-to-one with Module 23A for EFNA1–EPHA6 and EFNA2–EPHA6. Primary Figure 1 all-pair dimeric Fc-fusion ELISA supports exact mouse mEphrin-A1–mEphA6 and mEphrin-A2–mEphA6 binding with comparative apparent K_D values of 5.2 ± 1.1 nM and 3.6 ± 0.74 nM, respectively. The direct-binding layer is promoted to medium-high while Fc-avidity, comparative apparent-K_D, no-receptor-proximal, and non-SCI biochemical limits remain explicit. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B056 (2026-09-05)

B056 adds one new 23B receptor-proximal edge paired one-to-one with Module 23A for EFNB1–EPHB6. The primary study supports ephrin-B1-induced EphB6 phosphorylation and EphB1-dependent transphosphorylation within a stable EphB1–EphB6 heterocomplex. The edge is consolidated at medium-high confidence with explicit engineered receptor-complex, no-direct-binary-affinity, no-downstream-JNK/Rac1, species-not-resolved-in-abstract, no-native-neural, and no-traumatic-SCI limits. The existing low/conflicted EphB6 JNK/Rac1 edge remains separate. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.
## Review-led expansion: B057 (2026-09-05)

B057 promotes one existing 23B functional-context edge paired one-to-one with Module 23A for EFNB3–EPHB1. The primary BALB/c mouse LPS intestinal-injury study reports EphB1/ephrin-B3-associated signaling changes in colon and primary enteric neuronal/glial cultures and partial rescue by stable ephrin-B3 overexpression. The edge is consolidated at medium confidence with explicit functional-context, overexpression, no-purified-binding, no-receptor-proximal-relay, incomplete-ordering, no-native-SCI, and no-traumatic-SCI limits. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.
## Review-led expansion: B058 (2026-09-05)

B058 promotes one existing 23B direct-binding edge paired one-to-one with Module 23A for EFNA2–EPHA2. Primary Figure 1 all-pair dimeric Fc-fusion ELISA supports weak mEphrin-A2 binding to hEphA2 with apparent K_D >50 nM. The direct-binding layer is consolidated at medium confidence with explicit weak comparative-affinity, Fc-avidity, no-receptor-proximal, no-downstream, and non-SCI biochemical limits. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B059 (2026-09-05)

B059 promotes the existing 23B PLAU/uPA–PLAUR/uPAR–β1-integrin complex edge paired one-to-one with Module 23A using acquired primary PubMed and PMC snapshots. The complex-level relay is consolidated at medium confidence; purified direct uPA–β1 binding, a single α-integrin partner, complete relay ordering, native neural context, and traumatic-SCI transfer remain unasserted. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B060 (2026-09-05)

B060 promotes the existing paired 23B EFNA5/ephrin-A5–EPHA10 edges using acquired primary PMC and PubMed snapshots. EphA10s/ephrin-A5 cellular association and isoform-specific β-catenin/invasion function are consolidated at medium confidence, while secreted EphA10s versus membrane pseudo-kinase EphA10, possible EphA2 contribution, no canonical full-length activation, and no-traumatic-SCI limits remain explicit. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B061 (2026-09-05)

B061 adds two new paired 23B COL15A1/COLXV–DDR1 edges. Primary pancreatic-adenocarcinoma assays support COLXV–DDR1 cellular complex association by co-immunoprecipitation and COLXV-associated suppression of DDR1/Pyk2 signaling with reduced cell scatter and invasion. The two edges are consolidated at medium and medium-high confidence with explicit no-purified-affinity, no-direct-α2β1-binding, no-linear-ordering, no-terminal-TF, and no-traumatic-SCI limits. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B062 (2026-09-05)

B062 promotes the existing paired 23B EGF–EGFR-Src-CAV1/Grb7 relay using acquired primary PubMed and PMC snapshots. EGF/growth-factor assays support CAV1 Tyr14 phosphorylation, Grb7 binding, and migration, while hypoxia/CAV1 perturbation assays support CAV1–EGFR association, dimerization, and ligand-independent EGFR phosphorylation. The edge is consolidated at medium confidence with distinct-context, downstream-scaffold, no-direct-EGF-CAV1, incomplete-linear-ordering, no-terminal-TF, and no-traumatic-SCI limits. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B063 (2026-09-05)

B063 promotes the existing paired 23B HGF–β1-integrin/ILK repair-function edge using an acquired primary PMC and PubMed snapshot. Primary rat wound and epidermal-cell assays support HGF-enhanced reepithelialization, β1-integrin/ILK induction, and ILK-dependent proliferation, migration, and invasion. The edge is consolidated at medium confidence with canonical-MET, functional-dependence, no-direct-HGF–ITGB1, preliminary-dedifferentiation, non-SCI wound, no-terminal-TF, and no-traumatic-SCI limits. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B064 (2026-09-05)

B064 promotes the existing paired 23B COL4A3/α3(IV) collagen–α2β1 edge at the downstream renal-function layer using an acquired primary PubMed snapshot. Primary COL4A3/ITGA2 knockout phenotyping supports altered glomerular-basement-membrane maturation and renal fibrosis, while the older collagen-IV adhesion study remains a broader comparator. The edge is consolidated at medium confidence with layer-separation, broader-comparator, no-direct-chain-specific-binding, incomplete-ordering, no-terminal-TF, and no-traumatic-SCI limits. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B065 (2026-09-05)

B065 promotes the existing paired 23B FN1–uPAR/β1-integrin/CAV1/Src relay using acquired primary PMC and PubMed snapshots. Primary human receptor-complex and migration assays support uPAR stabilization of β1-integrin/CAV1 complexes, Src association, focal-adhesion signaling, adhesion, and migration on fibronectin. The edge is consolidated at medium confidence with complex/function resolution, no-purified-FN1–uPAR binding, no-defined-α partner, incomplete-ordering, no-terminal-TF, and no-traumatic-SCI limits. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B066 (2026-09-05)

B066 promotes the existing paired 23B broader COL15A1-associated matrix → α2β1/DDR1/Pyk2 function edge using the already acquired primary COLXV/DDR1 PMC and PubMed snapshots. Primary COLXV exposure and DDR1/Pyk2/EMT assays support reduced pancreatic-cell scatter and invasion and suppression of DDR1 signaling and Pyk2 phosphorylation. The edge is consolidated at medium confidence with downstream-function, no-direct-COL15A1–α2β1, incomplete-ordering, matrix/model, no-terminal-TF, and no-traumatic-SCI limits. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B067 (2026-09-05)

B067 promotes the existing paired 23B VTN–αVβ8 adhesion/migration function edge from medium-low to medium using primary mouse renal and microglia studies. The renal study reports β8-dependent migration on vitronectin matrices, and the microglia study identifies αVβ8 as a functional vitronectin receptor. Direct recombinant VTN–αVβ8 binding remains separate from this function edge; non-SCI model, no-single-relay, no-terminal-TF, and no-traumatic-SCI limits are preserved. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B068 (2026-09-05)

B068 adds a new paired 23B dimer-level S100A8/A9–Mac-1 cellular-binding edge at medium-high confidence using primary CR3-transfectant binding assays. Recombinant S100A8/A9 binds more strongly to CR3-transfected CHO cells than vector controls, while CD11b/CD18 inhibition reduces only part of the associated neutrophil-survival effect. The record is bounded to cell-based receptor-complex binding, dimer state, alternate receptors, non-SCI comparator models, and no complete downstream relay or traumatic-SCI transfer. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B069 (2026-09-05)

B069 promotes the existing paired 23B S100A9-containing preparation → Mac-1 function edge to medium confidence using a primary human neutrophil study of MRP-14/S100A9. The study reports Mac-1-mediated adhesion and affinity activation through a distinct upstream receptor and explicitly excludes direct MRP-14–Mac-1 binding. Upstream-receptor identity, MRP-8 heterodimer inhibition, complete relay, terminal TF, non-SCI comparator scope, and traumatic-SCI transfer remain bounded. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B070 (2026-09-05)

B070 adds two new paired 23B PACAP receptor-proximal pathway edges at medium confidence from a primary PAC1-negative MCF-7 study. The paper assigns PACAP-induced Src/Raf/ERK and PI3K/AKT signaling to a VPAC1-dependent branch and PLC/PKA/cAMP-p38 signaling to a VPAC2-dependent branch. The assignment is bounded to a single pharmacologic cancer-cell study; purified receptor reconstitution, the older broad E132/E133 cAMP/ERK or neuronal claims, native neural/SCI transfer, and terminal TFs remain separate. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B071 (2026-09-05)

B071 promotes the existing paired 23B S100A8-containing preparation -> Mac-1 function edge to medium confidence using primary neutrophil and murine air-pouch assays. The study separately tests S100A8 and reports Mac-1 up-regulation/activation, Mac-1-neutralization-sensitive fibrinogen adhesion, calcium increase, and chemotaxis. Preparation-level material, mixed S100A9/heterocomplex comparators, no direct binary binding, no isolated ITGB2 mechanism, no complete relay, non-SCI comparator scope, no terminal TF, and no traumatic-SCI transfer remain explicit. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B072 (2026-09-05)

B072 adds a new paired 23B medium-high-confidence VPAC2 -> PKA-dependent cortical neurite-maturation function edge using primary mouse cortical neurons. A selective VPAC2 agonist reduces axon and dendrite outgrowth and branching, and the effect is blocked by VPAC2 antagonism or receptor loss and by PKA inhibition. The edge is receptor-to-function evidence rather than a PACAP ligand claim: PACAP38 effects in the same study are not assigned exclusively to VPAC2, and direct ligand binding, terminal TF, and traumatic-SCI transfer remain separate. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B073 (2026-09-05)

B073 adds a new paired 23B medium-high-confidence EFNB1 ligand-side reverse-signaling relay using a primary HEK293 transfection study. Ephrin-B1 expression activates JNK through TAK1/MKK4/MKK7, requires the cytoplasmic domain, persists after removal of all six intracellular tyrosines, and is blocked by JNK inhibition but not Src inhibition. The edge is deliberately receptor-unassigned: no EphB receptor, direct binary interaction, exact relay ordering, terminal TF, native tissue mechanism, or traumatic-SCI transfer is asserted; the existing low/conflicted EFNB1-to-EphB6 JNK/Rac1 edge remains separate. Canonical signaling tables and simulator outputs remain untouched.
