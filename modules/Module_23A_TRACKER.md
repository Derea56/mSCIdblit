# Module 23A: ECM, Integrin, Adhesion, and Mechanotransduction Signaling - Pathway-Graph Corpus Building Tracker

## Overview

This module curates matrix, adhesion, and mechanosensing relay logic relevant to scar organization, vessel remodeling, astrocyte/fibroblast states, and mechanically sensitive CNS responses after SCI.

**Status**: FIRST-PASS BATCH WORKFLOW COMPLETE / AUDIT LAYER ACTIVE FOR SECOND-PASS EXPANSION / MEDIUM-HIGH PRIORITY FOR `mSCS`.

## Second-pass expansion: B023 (2026-09-04)

B023 adds three newly searched primary-literature candidates and five new audit-layer edges. Acquired open-access full text supports direct MMRN2 binding to CD93 and correctly folded CD248 CTLD/ECD-Fc constructs, and supports direct binding of the SLIT2 C-terminal LG domain to glycosylated DAG1/dystroglycan. The SLIT2-DAG1 record is layer-separated into direct binding, DAG1-dependent Slit localization at the developing spinal-cord floor plate, and developmental commissural axon-guidance function. The existing MMRN2-CLEC14A direct and functional edges are promoted from staged review to supported review. These records remain non-SCI vascular or developmental neural comparators; glycosylation, domain, receptor-complex, and model limits are retained, and no Module 20A–22A ledger is modified.

The follow-on source-backed promotion gate reviewed the remaining staged mappings against the existing A evidence register. Of 702 staged A edges, 701 had a one-to-one B mapping, a primary-research-paper evidence row, a stable source locator, a non-boundary support type, and populated evidence summary/limitations; those 701 A and B edges are now `reviewed_supported`. The EFNA3–EPHA2 candidate remains staged because its source supports pathway/function context but not exportable direct binary binding, and its B edge remains `held_unresolved_exact_directness` with `exportable=false`.

## Priority Signaling Axes

- integrins and focal adhesion signaling
- FAK/SRC relays
- cadherin and adhesion signaling
- YAP/TAZ/TEAD
- mechanosensitive matrix-response pathways
- matricellular ligands and receptor interactions

## Handoff Goal

Provide a mechanotransduction layer so `mSCS` can eventually reason about tissue-state signaling that is not reducible to classic soluble cytokines.

## First-Pass Queue (2026-08-17)

The initial review queue is maintained at:

- `work/module23a/module23a_extraction_queue.tsv`
- `work/module23a/module23a_batch_plan.tsv`

The queue contains 1,092 review targets:

- 435 CellChatDB ECM-Receptor candidates;
- 182 ConnectomeDB guidance/ECM adhesion candidates;
- 464 Module 21A pathway-reuse candidates covering existing FAK/SRC, ILK, cadherin, laminin, collagen, tenascin, THBS, SPP1, VCAM, EDIL3, and related adhesion branches;
- 11 SCI-specific mechanism targets seeded from prior scar, stiffness, integrin, matricellular, and ECM-glycan work.

The queue is a candidate inventory, not an evidence register. Database rows remain provenance-only until primary research validation. Each target explicitly separates the three extraction layers: ligand/receptor binding or activation, receptor-proximal relay, and downstream pathway or cellular function. The queue also retains an explicit boundary for the conflicting chronic-scar mechanics anchors M1A-P026 and M1A-P027.

Review is organized into 22 batches of at most 50 targets. P1 targets prioritize integrin, syndecan, CD44, dystroglycan, validated 21A FAK/SRC/ILK branches, and SCI-specific mechanics branches. P2/P3 targets remain queued for broader receptor-specific and guidance/adhesion review. No Module 20A, 21A, or 22A evidence ledger is modified by queue construction.

Batch 001 anchor validation has retained twenty-eight evidence-backed context, relay, or functional edges and twenty-five explicit boundary records in the new 23A audit registers. These include β1-integrin/N-cadherin astrocyte relay context, stiffness–β1-integrin/ILK response, fibronectin-EDA scar function, chronic ECM/GAG mechanics, α9-integrin/kindlin-1 sensory regeneration, glycan/ECM-myeloid function, ApoE-LRP1 binding/trafficking/function, cell-surface CALR-LRP1 coreceptor signaling, the ApoC3-LDLR/LRP1 functional clearance axis, CCN4-alpha5beta1, CD40LG-Mac-1, processed DSP-ITGB6, EDIL3-LFA1 and EDIL3-alphaV complex/function boundaries, EGFL7-alphaVbeta3 binding/FAK-Akt/angiogenic outputs, FGA Aalpha-RGD and FGG gammaC motif binding to assembled alphaIIbbeta3, FN1-alphaVbeta3 reuse, and processed irisin-alphaVbeta5 reuse. FBLN2 remains function-only beta3-complex context; FGB free-chain, FN1 free-ITGB3, and full-length FNDC5/free-subunit candidates remain unresolved. The ADAM17/ADAM2, ANGPT1–ITGB1, ANGPTL2 and CCN4 free-subunit, CD40LG-ITGAM free-subunit, EDIL3 free-subunit, FBLN2 direct/relay, FGB free-chain, FN1 free-ITGB3, FNDC5/free-subunit, and APOC3 direct-binding candidates remain explicit no-evidence boundaries; assembled complexes, processed ligands, motifs, and functional axes are not split into unsupported direct molecular edges.
Batch 001 anchor validation has retained forty evidence-backed context, relay, or functional edges and twenty-six explicit boundary records in the new 23A audit registers. These include β1-integrin/N-cadherin astrocyte relay context, stiffness–β1-integrin/ILK response, fibronectin-EDA scar function, chronic ECM/GAG mechanics, α9-integrin/kindlin-1 sensory regeneration, glycan/ECM-myeloid function, ApoE-LRP1 binding/trafficking/function, cell-surface CALR-LRP1 coreceptor signaling, the ApoC3-LDLR/LRP1 functional clearance axis, CCN4-alpha5beta1, CD40LG-Mac-1, processed DSP-ITGB6, EDIL3-LFA1 and EDIL3-alphaV complex/function boundaries, EGFL7-alphaVbeta3 binding/FAK-Akt/angiogenic outputs, FGA Aalpha-RGD and FGG gammaC motif binding to assembled alphaIIbbeta3, FN1-alphaVbeta3 reuse, processed irisin-alphaVbeta5 reuse, extracellular HSP90alpha-LRP1/Akt motility, released gp96-LRP1/CD91 APC signaling, context-specific Hsp70-LRP1/CD91 evidence with conflicting affinity literature, and ICAM5-alpha5beta1 neuronal adhesion/function. FBLN2 remains function-only beta3-complex context; FGB free-chain, FN1 free-ITGB3, full-length FNDC5/free-subunit, HSPA4-LRP1, and generic free-ITGB1 candidates remain unresolved. The ADAM17/ADAM2, ANGPT1–ITGB1, ANGPTL2 and CCN4 free-subunit, CD40LG-ITGAM free-subunit, EDIL3 free-subunit, FBLN2 direct/relay, FGB free-chain, FN1 free-ITGB3, FNDC5/free-subunit, HSPA4-LRP1, and APOC3 direct-binding candidates remain explicit no-evidence boundaries; assembled complexes, processed ligands, motifs, and functional axes are not split into unsupported direct molecular edges.

The integrated B002/B003 review added 21 supported direct, receptor-proximal, and downstream ECM/adhesion records, including PECAM1-alphaVbeta3, uPA-alphaMbeta2, POSTN, Reelin, Sema7A, SPP1, TIMP1-LRP1, Agrin-DAG1, CHAD, collagen-I beta1, and collagen-IV family anchors. Non-SCI direct-binding studies remain mechanistic anchors only; family-level evidence is not transferred to chain-specific or untested SCI pairs. Three bounded no-evidence records preserve unresolved receptor assignments. Module 20A, 21A, and 22A ledgers remain unchanged.

Batches 004–006 are now reviewed. They add collagen-VI and collagen-IX family boundaries, Col6a3-alpha2beta1/FAK context, fibronectin-alpha5beta1 SCI scar context, COMP and DMP1 integrin relays, perlecan-DAG1, IBSP integrin comparators, and laminin-1/2-DAG1 and integrin neural relays. The integrated 23A audit layer contains 59 supported edges and 23 explicit no-evidence boundaries. Chain resolution, SCI relevance, and direct-versus-relay limitations remain recorded per evidence row; no Module 20A–22A ledger was modified.

Batches 007–009 are now integrated. They add assembled laminin-332/411/511/521 receptor complexes, laminin-DAG1 and alpha7 splice-form boundaries, NPNT-alpha8beta1, Reelin-alpha3beta1, THBS1/2 receptor layers, TNC-alpha8/9/V integrin branches, VTN and VWF integrin contexts, SCI stiffness-mechanotransduction context, activated A2M-LRP1 relay/function, and PACAP-PAC1 signaling. The integrated 23A audit layer contains 100 supported edges and 37 explicit no-evidence boundaries. Isolated laminin chains, free receptor subunits, processed/domain ligands, and pathway-level versus functional evidence remain explicitly bounded; no Module 20A–22A ledger was modified.

Batch 010 is now integrated. It adds PACAP/secretin and adiponectin receptor boundaries, AngII/AT1B, angiopoietin-integrin/Tie2 branches, CCL28/CCR10, CD177/PECAM1, podoplanin/CLEC-2, collagen-XI, processed collagen-NC1 fragments, ephrin contacts, FN1 coreceptor pathways, irisin, GNRHR, and perlecan/endorepellin. The integrated 23A audit layer contains 150 supported edges and 43 explicit no-evidence boundaries. Free receptor subunits, processed ligands, alternative receptors, cytosolic chaperone complexes, and non-SCI model boundaries remain separated; no Module 20A–22A ledger was modified.
B014 is now integrated. It adds family-bounded Eph/ephrin receptor evidence, class-3/4/5/6 semaphorin receptor-complex and Plexin relays, and explicit SCI downstream anchors for SPP1, periostin, fibroblast/pericyte scar ECM, glycan sulfation, chronic lesion mechanics, and fibrillar collagen I–GPVI/FcRγ. The batch contributes 32 supported edges and 8 no-evidence boundaries; isolated Eph/semaphorin subunits, unresolved exact pairs, isolated COL1A1–GP6, and downstream-only SCI anchors remain separated. No Module 20A–22A ledger was modified.
B011 is now integrated. It adds perlecan/ITGA5:ITGB1-PDGFRB, ICAM1-LFA1/Mac-1, IL34-PTPRZ1, INSL5-RXFP4, VCAM1, THY1, KIT, laminin, LGALS1, LGI3, MAdCAM1, MDK, MFGE8, MIF, MMP9, MST1R, NCAM, netrin, PDGF, podoplanin, PlGF, tPA/uPA, periostin, and NGF comparator branches. The batch contributes 63 supported edges and 8 explicit source-context boundaries; free subunits, co-receptors, cytosolic complexes, processed ligands, and the adrenergic sender-to-receptor claims remain bounded. No Module 20A–22A ledger was modified.
B012 is now integrated. It adds PROCR/HSP90AA1, PROK1/PROKR1, PTN-integrin/PTPRZ1 and PTN-PTPRZ1, PYY/NPY1R, Reelin/LRP8-VLDLR, RGMA/NEO1, SDC2/PTPRJ, selectin/GLG1 and PSGL1-integrin function, semaphorin complexes, SEMA7A/alpha1beta1, SPP1/CD44v, TDGF1/GPC1, TGM2, thrombospondin, talin, VCAN, VEGFA, VIP/PAC1, vitronectin, VWF, WNT5B/FZD7, and Eph receptor branches. It contributes 45 supported edges and 4 exact-pair boundaries; free integrin subunits, intracellular adaptor binding, receptor crosstalk, and binding-only Eph rows remain explicitly scoped. No Module 20A–22A ledger was modified.
B013 is now integrated. It adds exact and functional EphA/ephrin-A and EphB/ephrin-B evidence, reverse-signaling distinctions, and six explicit no-evidence boundaries for unresolved cross-class or subclass pairs. It contributes 26 supported edges; no SCI-specific transfer is asserted, and Ephrin-A GPI versus Ephrin-B transmembrane topology, cis/trans direction, and family-level uncertainty remain preserved. No Module 20A–22A ledger was modified.
B016 is now integrated. It adds KGD/αIIbβ3 platelet outside-in signaling, processed and matrix-restricted ECM/integrin branches, vascular and guidance complexes, Eph/ephrin and semaphorin branches, and context-specific downstream cellular functions. It contributes 129 supported edges and 21 explicit boundaries; duplicate aliases, reverse signaling, processed ligands, receptor complexes, and non-SCI transfer limits remain separated. No Module 20A–22A ledger was modified.
B015 is now integrated. It adds collagen-IV/VI/IX matrix recognition boundaries, COMP/thrombospondin/CD47 branches, CALR and matrix-associated adhesion contexts, and explicit collagen-chain versus assembled-complex limitations. It contributes 53 supported edges and 4 no-evidence or family/chain boundaries; isolated collagen chains, GP6/GPVI complex resolution, and non-SCI transfer limits remain explicit. No Module 20A–22A ledger was modified.
B017 is now integrated. It adds guidance, matrix, semaphorin, Eph/ephrin, integrin, and functional-output evidence across Q0801–Q0850, with 107 supported edges and 35 explicit boundaries. The declared aliases Q0831/Q0830, Q0833/Q0832, and Q0846/Q0845 were deduplicated at central integration while their evidence rows were retained and re-pointed to canonical edges; receptor complexes, reverse signaling, processed ligands, and no-SCI-transfer limits remain explicit. No Module 20A–22A ledger was modified.
B018 is now integrated. It adds laminin-211/GPR126, laminin alpha2/alpha3/alpha4 integrin and dystroglycan complexes, matrix and lectin receptor branches, and downstream guidance/adhesion outputs. It contributes 76 supported edges and 4 explicit boundaries; LAMB2–SV2A/B/C exact receptor claims and the MATN1–ITGB1 subunit-resolution issue remain evidence-only boundaries. No Module 20A–22A ledger was modified.
B020 is now integrated. It adds processed osteopontin, collagen/laminin and integrin branches, intracellular talin/integrin-tail associations, vascular and adhesion complexes, and explicit boundaries for unresolved exact pairs, free subunits, and duplicate aliases. It contributes 102 supported edges and 48 explicit boundaries; no Module 20A–22A ledger was modified.
B019 is now integrated. It adds matrix, adhesion, receptor-complex, processed-ligand, and intracellular adaptor evidence across Q0901–Q0950, contributing 108 staged edges and 26 explicit boundaries; eight exact duplicate edge-content rows were consolidated onto canonical edges at final integration, with all evidence retained. Free subunits, intracellular tail interactions, processed ligands, and non-SCI transfer limitations remain separated. No Module 20A–22A ledger was modified.
B021 is now integrated. It covers Q1001–Q1050 with 68 evidence records: 32 supported records, 36 explicit no-evidence or source-context boundaries, and 32 layer-separated edges. The missing Reelin/ephrin-B3 functional-output row was materialized as its own edge rather than merged into the receptor-proximal relay; Sema3A–CNTN2, Sema6C–NRCAM, and laminin–SV2 exact-pair limits remain explicit. No Module 20A–22A ledger was modified.
B022 is now integrated. It covers Q1051–Q1092 with 107 evidence records: 99 supported records, 8 explicit boundaries, and 99 layer-separated edges. Integrin heterodimers, receptor complexes, processed ligands, transactivation, and function-only adhesome evidence remain at their reported resolution; no direct binary interaction was inferred from pathway or functional records. No Module 20A–22A ledger was modified.
During B021/B022 integration, nine exact duplicate edge-content rows from earlier 23A batches were consolidated onto canonical lower-ID edges while all supporting evidence records were retained and re-pointed. This removes edge duplication without discarding provenance.
The legacy B008 edge-reference gap is now resolved. Nineteen B008 evidence rows were re-pointed to existing canonical edges, while nine new layer-specific edges were added for NPNT and Reelin functional outputs plus THBS1/THBS2 receptor-proximal relays and binding. All 29 B008 evidence rows now reference materialized edges; direct, relay, and functional evidence remain separate. No Module 20A–22A ledger was modified.

## Review-led expansion: B031 (2026-09-04)

B031 adds one review-led extracellular histone H3/H4 candidate and four source-backed A-layer edges: non-SCI histone H4 binding to TLR4/MD2, SCI-associated histone TLR2-YB-1 relay, SCI neurite/axon-growth inhibition, and observational histone H3 accumulation in injured CNS. Primary records were acquired locally and linked through the source manifest. The TLR4/MD2 result remains a non-SCI histone-H4 comparator; SCI causal evidence is retained at TLR2/YB-1 and neurite-inhibition layers, with histone subtype, mixed-preparation, cleavage, and injury-model limits explicit. No TLR4 relay is transferred into SCI, and no Module 20A–22A ledger is modified.

## Review-led expansion: B032 (2026-09-05)

B032 adds one review-led CSPG candidate and four source-backed A-layer edges: TLR4-dependent immune-cell inflammatory activation, macrophage/microglial inflammatory output, SCI immune-cell clearance and inflammation-resolution failure, and TLR4-independent neurite-growth inhibition. The primary rodent SCI study was acquired locally and linked through the source manifest. Direct CSPG-TLR4 binding and individual proteoglycan-core assignment remain unresolved; intact CSPG versus GAG digestion, cell-state, and rodent-model limits are explicit, and neuronal growth inhibition is not assigned to the CSPG-TLR4 immune relay. No Module 20A–22A ledger is modified.

The B001 continuation through Q0041 is now complete. Q0032–Q0036 added extracellular HSP90alpha-LRP1/Akt motility, released gp96-LRP1/CD91 APC signaling, context-specific Hsp70-LRP1/CD91 evidence with conflicting affinity literature, ICAM5-alpha5beta1 neuronal adhesion/function, and an HSPA4-LRP1/CD91 boundary. Q0037–Q0041 added ISG15-to-assembled-LFA-1 binding/Src-family relay/cytokine output, JAM3-to-assembled-Mac-1 binding and platelet-leukocyte function, laminin-332-to-assembled-alpha3beta1 binding/FAK-Src-Rac1 relay/epithelial output, and free-subunit boundaries. B001 now contributes 48 supported edges and 29 explicit boundaries across 77 validated records. The integrated audit layer contains 1,063 supported edges and 1,155 supported evidence records plus 280 explicit no-evidence or source-context boundaries; no Module 20A–22A ledger was modified.

B001 is fully complete through Q0050. Q0042–Q0046 added LGALS3/glycan-resolved alpha3beta1, MFGE8-alpha8beta1 PTEN/RhoA, and MFGE8-alphaVbeta5 DOCK180/Rac1/phagocytic branches with free-subunit boundaries. Q0047 added processed MMP9-PEX-LRP1 binding, ERK/Akt relay, and Schwann-cell function. Q0048–Q0049 reused canonical NPNT-alpha8beta1 binding/relay/function records with free-subunit boundaries, and Q0050 reused canonical PECAM1-alphaVbeta3 binding with a free-ITGAV boundary. B001 now contributes 60 supported edges and 37 explicit boundaries across 97 validated records; all 50 targets are reviewed. The integrated audit layer contains 1,075 supported edges and 1,158 supported evidence records plus 283 explicit no-evidence or source-context boundaries. No Module 20A–22A ledger was modified.
## Review-led expansion: B024 (2026-09-04)

B024 adds two review-led ECM candidates and three candidate branches: decorin-to-EGFR receptor binding/activation, decorin-mediated anti-scarring and axon-growth function in acute rat SCI, and biglycan-mediated CD14/TLR2/TLR4 inflammatory signaling. The new audit layer contains six source-backed A/B edges: one decorin EGFR edge, one decorin SCI function-only edge, and four biglycan CD14, TLR2/TLR4, inflammasome, and macrophage-output layers. Review and primary records were acquired locally with hashes recorded in the source manifest. Non-SCI comparator limits, soluble/intact biglycan requirements, multireceptor context, and the absence of terminal-TF claims remain explicit; no Module 20A–22A ledger is modified.

## Review-led expansion: B025 (2026-09-04)

B025 adds two review-led matrix danger-signal candidates and seven source-backed A/B edges: tenascin-C FBG-domain binding to TLR4, its TLR4-dependent NF-kappaB/proximal relay, and macrophage/microglial inflammatory function; plus low-molecular-weight hyaluronan TLR4-MyD88 and TLR4-TRIF/TBK1/IRF3 relays, cPLA2alpha/COX2-eicosanoid output, and IFN-beta output. Primary records were acquired locally and linked through the source manifest. Exact FBG-domain, HA fragment-size, receptor/adaptor, cell-model, endotoxin-control, and non-SCI comparator limits remain explicit; direct HA-TLR4 binding and universal MyD88 or terminal-TF assignments are not inferred, and no Module 20A–22A ledger is modified.

## Review-led expansion: B026 (2026-09-04)

B026 adds one review-led FN-EDA danger-signal candidate and three source-backed A/B edges: EDA-domain engagement of the TLR4-MD2 receptor context, a TLR4-dependent proximal inflammatory/profibrotic relay, and measured fibroblast/myofibroblast and macrophage inflammatory-fibrotic outputs. Primary records were acquired locally and linked through the source manifest. EDA-domain and MD-2 requirements, non-SCI tissue-injury/fibrosis comparator scope, the absence of a structural DAMP-receptor complex, and the absence of traumatic-SCI or terminal-TF transfer remain explicit. The identified alpha4beta1 cooperation paper was not used for promotion because its local full text was not acquired.

## Review-led expansion: B027 (2026-09-04)

B027 adds one review-led SPARC danger-signal candidate and four source-backed A/B edges: direct TLR4 binding, the TLR4-TBK1-IRF3 proximal relay, the IFN-beta-IFNAR-STAT1 relay, and measured IRF3/IRF7-dependent macrophage interferon/inflammatory output. Primary records were acquired locally and linked through the source manifest, while SCI proteomics supplies extracellular-abundance context. Mouse aging/obesity macrophage comparator scope, the absence of an MD-2 requirement or structural receptor-complex claim, and the absence of traumatic-SCI causal transfer remain explicit.

## Review-led expansion: B028 (2026-09-04)

B028 adds one review-led galectin-3 candidate and four source-backed A/B edges: Gal3-TLR4 ligand activity, comparator-specific TLR4-dependent microglial activation, rat SCI ROS/TXNIP/NLRP3/IL-1beta inflammatory output, and mouse SCI Gal3/PDGFRbeta+ fibroblast fibrotic-scar function. Primary records were acquired locally and linked through the source manifest. Neuroinflammation comparator scope, the separation of TLR4 ligand evidence from SCI inflammasome and scar-function evidence, and the absence of a universal TLR4-to-NLRP3 relay remain explicit.

## Review-led expansion: B029 (2026-09-04)

B029 adds one review-led HMGB1 candidate and five source-backed A/B edges: direct TLR4/MD2 binding, a TLR4-NF-kappaB/MAPK relay, astrocytic CCL5 with myeloid recruitment/M1 output, SCI pro-inflammatory cytokine and microglial NF-kappaB output, and secondary-injury/motor-function output. Primary records were acquired locally and linked through the source manifest. HMGB1 redox state, endotoxin controls, TLR2/RAGE/TLR4 cell-context differences, human biomarker non-causality, and the absence of a universal receptor or adaptor ordering remain explicit.

## Review-led expansion: B030 (2026-09-04)

B030 adds one review-led S100A8/A9 calprotectin-dimer candidate and four source-backed A/B edges: direct TLR4/MD2 binding, the TLR4-MyD88-IRAK-1/NF-kappaB/MAPK relay, TNF/IL-8 phagocyte output, and an SCI-associated myeloid context edge. Primary records were acquired locally and linked through the source manifest. Dimer-versus-tetramer state, calcium/zinc and preparation requirements, RAGE/Mac-1 separation, and the observational/non-causal status of SCI abundance are retained explicitly.
## Review-led expansion: B033 (2026-09-05)

B033 adds one review-led tenascin-R candidate and four source-backed A-layer edges: isolated FBG-R direct TLR4 binding, TLR4-dependent NF-kB activity, macrophage IL-6/IL-8/TNF output, and whole-TNR restriction of selected posttraumatic SCI locomotor recovery with altered synaptic remodeling. The FBG-R findings are non-SCI comparator evidence, while the SCI finding is an adult mouse genotype study; no traumatic-SCI TLR4 mechanism, full-length presentation equivalence, axonal-regrowth mechanism, or terminal TF is asserted. No Module 20A–22A ledger is modified.
## Review-led expansion: B034 (2026-09-05)

B034 adds one review-led tenascin-R axon-associated candidate and five source-backed A-layer edges: direct TNR-MAG binding, MAG-cell repulsion, direct TNR-F11/CNTN1 domain interaction, enhanced F11-mediated neurite outgrowth, and TNR substrate inhibition of retinal axon growth. MAG/F11 domain resolution, substrate presentation, non-SCI comparator scope, amphibian injury model, and absence of a defined cytoplasmic relay or terminal TF remain explicit. No Module 20A–22A ledger is modified.

## Review-led expansion: B035 (2026-09-05)

B035 adds one review-led tenascin-R lectican/CSPG candidate and six source-backed A-layer edges: direct TNR FNIII3-5 binding to the C-type lectin domains of aggrecan, versican, neurocan, and brevican, plus saturable full-length TNR binding to neurocan and phosphacan/PTPRZ1 through proteoglycan core-protein interactions. Lectican-domain versus full-length core-protein resolution, rat/recombinant non-SCI CNS comparator scope, and the absence of a downstream relay or traumatic-SCI transfer remain explicit. No Module 20A–22A ledger is modified.

## Review-led expansion: B036 (2026-09-05)

B036 adds one review-led tenascin-R sodium-channel candidate and two source-backed A-layer edges: direct TNR FNIII1-2/6-8 binding to the purified type-IIA rat brain sodium-channel complex and to the beta2 extracellular domain. Proposed channel clustering, localization, activity effects, native-complex beta2 mediation, non-SCI comparator scope, and the absence of a downstream relay or traumatic-SCI transfer remain explicit. No Module 20A–22A ledger is modified.

## Review-led expansion: B037 (2026-09-05)

B037 adds one review-led tenascin-R oligodendrocyte candidate and three source-backed A-layer edges: direct TNR binding to membrane sulfatide, TNR-substrate adhesion of O4-positive oligodendrocytes, and TNR-induced myelin-gene expression/terminal differentiation of O4-positive progenitors. Isoform, cell-stage, glycolipid, in-vitro, non-SCI myelination, and no-relay limits remain explicit. No Module 20A–22A ledger is modified.

## Review-led expansion: B038 (2026-09-05)

B038 adds one review-led tenascin-R microglial candidate and six source-backed A-layer edges: activated-microglia antiadhesion, opposing EGF-like/FNIII6-8 domain effects on primary microglial adhesion and migration, domain-specific microglial BDNF/TGF-beta and NGF/TGF-beta secretion, and microglia/TNF-alpha-associated TNR downregulation in oligodendrocytes. PKA/PKC dependence, peripheral-nerve injury, primary-microglia, in-vitro comparator, reverse-feedback, and no-relay limits remain explicit. No Module 20A–22A ledger is modified.

## Review-led expansion: B039 (2026-09-05)

B039 adds one review-led tenascin-R perineuronal-net candidate and two source-backed A-layer edges: TNR-dependent perineuronal-net formation/stabilization and aggrecan clustering as the reported extracellular organization mechanism. Mouse loss-of-function, organotypic/dissociated-culture, add-back/rescue, and no-traumatic-SCI-transfer limits remain explicit. No Module 20A–22A ledger is modified.

## Review-led expansion: B040 (2026-09-05)

B040 adds one review-led tenascin-R/RPTPζ candidate and one source-backed A-layer edge: the TNR–RPTPζ/phosphacan extracellular interface contributes to perineuronal-net architecture, supported by ectodomain binding and interface-mutagenesis effects in mouse neuronal cultures. Cytoplasmic phosphatase-relay, neuronal-culture, and no-traumatic-SCI-transfer limits remain explicit. No Module 20A–22A ledger is modified.

## Review-led expansion: B041 (2026-09-05)

B041 adds one review-led tenascin-R conduction candidate and one source-backed A-layer edge: TNR promotes normal optic-nerve compound-action-potential conduction velocity in mice. The TNR-deficient genotype, in-vivo electrophysiology, preserved nodal Na+-channel distribution, non-SCI comparator, and no-traumatic-SCI-transfer limits remain explicit. No Module 20A–22A ledger is modified.

## Review-led expansion: B042 (2026-09-05)

B042 adds one review-led PACAP receptor candidate and four source-backed A-layer edges: direct PACAP association with recombinant VPAC1/VIPR1 and VPAC2/VIPR2 systems, plus VPAC1- and VPAC2-linked Gs/adenylate-cyclase/cAMP activation. Historical VIP1/VIP2 nomenclature, shared PACAP/VIP pharmacology, receptor-state and heterologous-system limits, and no-native-SCI or subtype-exclusive downstream transfer remain explicit. No Module 20A–22A ledger is modified.

## Review-led expansion: B043 (2026-09-05)

B043 adds one review-led S100A8/A9 candidate and two source-backed A-layer edges: Mac-1 (ITGAM:ITGB2) up-regulation/activation and Mac-1-dependent neutrophil adhesion/chemotaxis. The primary study’s mixed S100A8, S100A9, and S100A8/A9 preparations, antibody-sensitive Mac-1 function, non-SCI inflammatory models, no-direct-binding boundary, and no-native-SCI-transfer limit remain explicit. No Module 20A–22A ledger is modified.

## Review-led expansion: B044 (2026-09-05)

B044 adds one review-led Sema4A receptor candidate and two source-backed A-layer edges: Plexin-B2-dependent synaptogenic relay and glutamatergic synapse development in rat hippocampal cultures. Plexin-B2 knockdown, soluble mouse Sema4A-Fc, rodent-culture, no-direct-binding, complete-relay, and no-traumatic-SCI-transfer limits remain explicit. No Module 20A–22A ledger is modified.

## Review-led expansion: B045 (2026-09-05)

B045 adds one review-led EFNA1–EPHA5 candidate and one source-backed A-layer edge: ephrin-A1 recombinant-fusion stimulation produces time-dependent EPHA5 tyrosine phosphorylation in human U-118 MG glioblastoma cells. The receptor-proximal phosphorylation layer is promoted without inferring direct binary binding, a downstream program, neural context, or traumatic-SCI transfer. No Module 20A–22A ledger is modified.

## Review-led expansion: B046 (2026-09-05)

B046 adds one review-led EFNA1–EPHA8 candidate and one source-backed A-layer edge: ephrin-A1-Fc binds EphA8 and induces EphA8/EphA8-TrkB tyrosine phosphorylation in NIH3T3 fibroblast receptor systems. The receptor-proximal activation layer is promoted with explicit recombinant-fusion and heterologous-fibroblast limits; no downstream cellular program, native neural context, or traumatic-SCI transfer is inferred. No Module 20A–22A ledger is modified.

## Review-led expansion: B047 (2026-09-05)

B047 adds one review-led EFNA2–EPHA5 candidate and one source-backed A-layer edge: EphA5/ephrin-A2 binding context is associated with topographically selective retinal axon repulsion in vitro and normal dLGN mapping in vivo. The retinal guidance function is promoted with explicit receptor-association rather than receptor-exclusive causality, non-SCI visual-system, and no-complete-relay limits. No Module 20A–22A ledger is modified.

## Review-led expansion: B048 (2026-09-05)

B048 promotes the existing EFNA2–EPHA8 binding/activation edge using primary mouse-brain ligand and NIH3T3 receptor-system evidence: the historical Elf-1/Cek7-L ligand represented in the local register by EFNA2 binds and activates Eek/EphA8 and Eek-TrkB. Historical nomenclature, recombinant/heterologous context, no-downstream-program, no-native-neural, and no-traumatic-SCI-transfer limits remain explicit. No Module 20A–22A ledger is modified.

## Review-led expansion: B049 (2026-09-05)

B049 adds one review-led VTN–alphaVbeta8 direct-binding edge: primary affinity-chromatography assays support exact alphaVbeta8 binding to vitronectin in recombinant secreted and intact beta8-expressing cell systems. The existing function-only edge remains separate because intact alphaVbeta8 did not promote adhesion on vitronectin-coated substrate. No beta8 cytoplasmic relay, neural, or traumatic-SCI transfer is established. No Module 20A–22A ledger is modified.

## Review-led expansion: B050 (2026-09-05)

B050 promotes the existing Sema4A–Plexin-B2 receptor-proximal edge using primary activated mouse CD8+ T-cell evidence: Sema4A-Fc surface binding is reduced by Plexin-B2 blocking antibody, and Plexin-B2 knockdown reduces IFN-gamma output. The edge is promoted to medium-high with explicit cell-surface, blocking/knockdown, non-SCI immune-comparator, no-purified-affinity, and no-complete-relay limits. No Module 20A–22A ledger is modified.

## Review-led expansion: B051 (2026-09-05)

B051 promotes the existing EFNA2–EPHA5 binding edge using primary EphA5-AP affinity-probe labeling of ephrin-A2-expressing fibroblasts and complementary retinal binding/guidance evidence. The edge is promoted to medium-high with explicit cell-associated probe, shared-ephrin, developmental visual-system, no-purified-affinity, no-receptor-exclusive-causality, and no-traumatic-SCI limits. No Module 20A–22A ledger is modified.

## Review-led expansion: B052 (2026-09-05)

B052 promotes the existing EFNA1–EPHA5 binding edge using primary exact-pair ephrin-A1-Fc/EphA5-Fc ELISA binding and independent human U-118 MG-cell EPHA5 phosphorylation evidence. The edge is promoted to medium-high with explicit Fc-avidity, EphA-class promiscuity, receptor-proximal-only, non-neural cell-line, no-purified-monovalent-affinity, no-downstream-program, and no-traumatic-SCI limits. No Module 20A–22A ledger is modified.

## Review-led expansion: B053 (2026-09-05)

B053 promotes the existing EFNA1–EPHA8 binding edge using the primary NIH3T3 study reporting ephrin-A1-Fc binding and ligand-dependent EphA8/EphA8-TrkB tyrosine phosphorylation. The edge is promoted to medium-high with explicit recombinant-fusion, heterologous-fibroblast, receptor-proximal-only, no-downstream-program, no-native-neural, and no-traumatic-SCI limits. No Module 20A–22A ledger is modified.

## Review-led expansion: B054 (2026-09-05)

B054 adds two review-led EFNA2–EPHA2 functional edges from a primary mouse bone-remodeling study: ephrin-A2 reverse signaling and EphA2 forward signaling enhance osteoclast differentiation, while EphA2-associated signaling suppresses osteoblast differentiation. The two downstream branches are recorded separately with explicit mouse bone-remodeling, directionality, no-purified-binding, incomplete-ordering, and no-traumatic-SCI limits; the existing low-tier direct-binding edge remains unchanged. No Module 20A–22A ledger is modified.

## Review-led expansion: B055 (2026-09-05)

B055 promotes the existing EFNA1–EPHA6 and EFNA2–EPHA6 binding edges using the primary all-pair dimeric Fc-fusion ELISA: mEphrin-A1–mEphA6 apparent K_D 5.2 ± 1.1 nM and mEphrin-A2–mEphA6 apparent K_D 3.6 ± 0.74 nM. The exact mouse binding layer is promoted to medium-high while comparative apparent-K_D, Fc-avidity, no-receptor-proximal, and non-SCI biochemical limits remain explicit. No Module 20A–22A ledger is modified.

## Review-led expansion: B056 (2026-09-05)

B056 adds a separate EFNB1–EPHB6 receptor-proximal edge from the primary study reporting ephrin-B1-induced EphB6 tyrosine phosphorylation, EphB1-dependent transphosphorylation, ligand dependence, and stable EphB1–EphB6 heterocomplex formation. The new edge is recorded at medium-high confidence with explicit engineered receptor-complex, species-not-resolved-in-abstract, no-direct-binary-affinity, no-JNK/Rac1, no-native-neural, and no-traumatic-SCI limits. The existing low/conflicted EphB6 JNK/Rac1 edge remains unchanged. No Module 20A–22A ledger is modified.
## Review-led expansion: B057 (2026-09-05)

B057 promotes the existing EFNB3–EPHB1 functional-context edge using the primary BALB/c LPS intestinal-injury study. In mouse colon and primary enteric neuronal/glial cultures, LPS reduced EphB1/ephrin-B3-associated signaling markers, while stable ephrin-B3 overexpression partially rescued cell injury, inflammatory cytokines, Akt/Src/NF-κB activation, and β-catenin nuclear translocation. The edge is promoted to medium with explicit functional-context, overexpression, no-purified-binding, no-receptor-proximal-relay, incomplete-ordering, and no-traumatic-SCI limits. No Module 20A–22A ledger is modified.
## Review-led expansion: B058 (2026-09-05)

B058 promotes the existing EFNA2–EPHA2 direct-binding edge using the primary all-pair dimeric Fc-fusion ELISA. Figure 1 reports weak mEphrin-A2 binding to hEphA2 with apparent K_D >50 nM. The edge is promoted to medium with explicit weak comparative-affinity, Fc-avidity, no-receptor-proximal, no-downstream, and non-SCI biochemical limits. No Module 20A–22A ledger is modified.

## Review-led expansion: B059 (2026-09-05)

B059 promotes the existing PLAU/uPA–PLAUR/uPAR–β1-integrin complex relay using acquired primary PubMed and PMC snapshots. Human lung-fibroblast and related beta1-integrin/uPAR studies support uPAR–β1 complex association and uPA-dependent adhesion/migration signaling at medium confidence; purified direct uPA–β1 binding, a single α-integrin partner, complete relay ordering, native neural context, and traumatic-SCI transfer remain unasserted. No Module 20A–22A ledger was modified.

## Review-led expansion: B060 (2026-09-05)

B060 promotes the existing EFNA5/ephrin-A5–EPHA10 edges using acquired primary PMC and PubMed snapshots. The study supports EphA10s/ephrin-A5 cellular association by co-immunoprecipitation and isoform-specific effects on β-catenin localization, migration/invasion, and xenograft outcomes; the result is recorded at medium confidence with secreted EphA10s versus membrane pseudo-kinase EphA10, possible EphA2 contribution, no canonical full-length activation, and no-traumatic-SCI limits explicit. No Module 20A–22A ledger was modified.

## Review-led expansion: B061 (2026-09-05)

B061 adds two paired COL15A1/COLXV–DDR1 edges using acquired primary PMC and PubMed snapshots. The primary pancreatic-adenocarcinoma study supports cellular COLXV–DDR1 association by co-immunoprecipitation and separately supports COLXV-associated suppression of DDR1 signaling, Pyk2 phosphorylation, pancreatic-cell scatter, and invasion. The edges are recorded at medium and medium-high confidence, respectively, with no purified COLXV–DDR1 affinity, no direct COLXV–α2β1 binding or linear α2β1→DDR1 ordering, no terminal TF, and no-traumatic-SCI limits explicit. No Module 20A–22A ledger was modified.

## Review-led expansion: B062 (2026-09-05)

B062 promotes the existing EGF–EGFR-Src-CAV1/Grb7 relay using acquired primary PubMed and PMC snapshots. The primary studies support EGF/growth-factor-associated CAV1 Tyr14 phosphorylation, Grb7 binding, and migration, together with CAV1–EGFR association and ligand-independent EGFR activation under hypoxia. The edge is promoted to medium with distinct cell and perturbation contexts, downstream-scaffold, no-direct-EGF-CAV1, incomplete-linear-ordering, no-terminal-TF, and no-traumatic-SCI limits explicit. No Module 20A–22A ledger was modified.

## Review-led expansion: B063 (2026-09-05)

B063 promotes the existing HGF–β1-integrin/ILK repair-function edge using an acquired primary PMC and PubMed snapshot. The primary rat study reports HGF-enhanced wound reepithelialization and β1-integrin/ILK induction, while ILK silencing reduces β1-integrin, c-MET, proliferation, migration, and invasion. The edge is promoted to medium with canonical-MET, functional-dependence, no-direct-HGF–ITGB1, preliminary-dedifferentiation, non-SCI wound, no-terminal-TF, and no-traumatic-SCI limits explicit. No Module 20A–22A ledger was modified.

## Review-led expansion: B064 (2026-09-05)

B064 promotes the existing COL4A3/α3(IV) collagen–α2β1 edge at the downstream renal-function layer using an acquired primary PubMed snapshot. The exact COL4A3/ITGA2 knockout study supports altered glomerular-basement-membrane maturation and renal fibrosis phenotypes; a broader collagen-IV adhesion study is retained as comparator evidence without assigning COL4A3-chain-specific binding. The edge is promoted to medium with layer separation, broader-comparator, no-direct-chain-specific-binding, incomplete-ordering, no-terminal-TF, and no-traumatic-SCI limits explicit. No Module 20A–22A ledger was modified.

## Review-led expansion: B065 (2026-09-05)

B065 promotes the existing FN1–uPAR/β1-integrin/CAV1/Src relay using acquired primary PMC and PubMed snapshots. The primary human study reports uPAR stabilization of β1-integrin/CAV1 complexes, Src association, focal-adhesion signaling, adhesion, and migration on fibronectin, with functional disruption after caveolin depletion or uPAR-peptide treatment. The edge is promoted to medium with complex/function resolution, no-purified-FN1–uPAR binding, no-defined-α partner, incomplete-ordering, no-terminal-TF, and no-traumatic-SCI limits explicit. No Module 20A–22A ledger was modified.

## Review-led expansion: B066 (2026-09-05)

B066 promotes the existing broader COL15A1-associated matrix → α2β1/DDR1/Pyk2 function edge using the already acquired primary COLXV/DDR1 PMC and PubMed snapshots. The primary study supports COLXV-associated suppression of DDR1 signaling and Pyk2 phosphorylation with reduced pancreatic-cell scatter and invasion, supporting the matrix-function edge at medium confidence. Direct COL15A1–α2β1 binding, linear α2β1→DDR1 ordering, matrix specificity, terminal TF, and traumatic-SCI transfer remain explicit limits. No Module 20A–22A ledger was modified.

## Review-led expansion: B067 (2026-09-05)

B067 promotes the existing VTN–αVβ8 function edge from medium-low to medium using acquired primary mouse renal and microglia studies. The renal study reports β8-dependent migration on vitronectin matrices, and the microglia study identifies αVβ8 as a functional vitronectin receptor; recombinant binding evidence remains represented on the separate direct edge. Non-SCI model limits, no-single-relay, no-terminal-TF, and no-traumatic-SCI boundaries remain explicit.

## Review-led expansion: B068 (2026-09-05)

B068 adds a new dimer-level S100A8/A9–Mac-1 cellular-binding edge at medium-high confidence using a primary CR3-transfectant study. Recombinant S100A8/A9 binds more strongly to CR3-transfected CHO cells than vector controls, while CD11b/CD18 inhibition reduces only part of the associated neutrophil-survival effect. The record is bounded to cell-based receptor-complex binding, dimer state, alternate receptors, non-SCI comparator models, and no complete downstream relay or traumatic-SCI transfer.

## Review-led expansion: B069 (2026-09-05)

B069 promotes the existing S100A9-containing preparation → Mac-1 function edge to medium confidence using a primary human neutrophil study of MRP-14/S100A9. The study reports Mac-1-mediated adhesion and affinity activation through a distinct upstream receptor and explicitly excludes direct MRP-14–Mac-1 binding. Upstream-receptor identity, MRP-8 heterodimer inhibition, complete relay, terminal TF, non-SCI comparator scope, and traumatic-SCI transfer remain bounded.
