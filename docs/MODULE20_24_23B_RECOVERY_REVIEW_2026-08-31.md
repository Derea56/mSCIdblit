# Module 23B phase-2 recovery review

Read-only review of the live repository at `/Users/derea/Documents/SCI/mSCIdblit`.
No repository or database files were modified. Artifact paths below are
repository-relative unless stated otherwise. The artifact crosswalk is
conservative: every crosswalk row is `filename_token_candidate`, not
content-level validation.

## Counts inspected

| Scope | Count |
|---|---:|
| Module 23B B-layer evidence rows | 1,501 |
| Module 23B B-layer edge rows | 1,075 |
| Module 23B phase-2 rows | 1,308 |
| Distinct phase-2 evidence IDs / edge IDs | 1,290 / 366 |
| Phase-2 evidence-grade rows | 1,501 |
| Grade A / B / E / unassigned | 34 / 1,171 / 182 / 114 |
| Context L0 / L1 / L2 / L3 / L4 | 182 / 1,202 / 112 / 0 / 5 |
| Exportable / non-exportable evidence rows | 1,324 / 177 |
| 23B artifact-crosswalk rows | 1,919 |
| Distinct existing crosswalk artifact paths | 605 |
| Distinct existing full-text-like artifact paths | 448 |

The report selects the highest-yield rows with stable paper anchors and local
full-text-like artifacts. “Source-supported atomic candidate” means the
existing phase-2 row is already marked `validated_primary_observation` or
`validated_full_text` and has an explicit locus/model/assay/perturbation. It
does not upgrade the ledger grade or context. `validated_full_text_importable`,
abstract-only, metadata-only, and unresolved rows are retained as manual review
leads, not promoted here.

## Source-supported atomic candidates

These rows have a source-backed atomic observation in the existing phase-2
staging. The registered claim is reported separately; none should be treated
as a TF-target claim unless a future source review explicitly establishes one.

| Candidate ID; edge | Authoritative source anchor | Atomic observation | Registered program/author claim | Exact locus; model; assay; perturbation | Current grade/context | Artifact; reason |
|---|---|---|---|---|---|---|
| `M23B-EVID-000069`; `M23B-E000044` | PMCID:PMC4507358; PMID:25492623; DOI:10.1089/neu.2014.3703 | Yes; `validated_primary_observation` | Yes; `validated_author_claim` | Results on fibronectin matrix assembly and alpha5beta1 receptor expression; mouse contusion SCI lesion with CD11b+ macrophage/microglia and Col1a1-GFP fibroblast compartments, rat injured-spinal-cord comparator; soluble/insoluble FN Western blot, IHC/co-localization, qRT-PCR; lysM-Cre/floxed-FN deletion | B; L4 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC4507358_article.html`. Highest-yield exact SCI/context row, but no alpha5beta1-specific blockade or knockout. |
| `M23B-EVID-000004`; `M23B-E000002` | PMCID:PMC6978780; PMID:31516087; DOI:10.1089/neu.2019.6540 | Yes; `validated_primary_observation` | Yes; `validated_author_claim` | Results on chronic stiffening, IMP rescue, and glial-fiber alignment; severe T11 contusion SCI, chronic lesion core/rim and glial/fibrotic interface; AFM microindentation, stiffness mapping, GFAP/FN IHC, CurveAlign, locomotor assessment; vehicle versus IMP at 2/24/48 h, 12-week endpoint | B; L1 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC6978780_article.html`. Strong SCI mechanics observation; receptor attribution remains limited. |
| `M23B-EVID-000005`; `M23B-E000003` | PMCID:PMC5995671; PMID:29705186; DOI:10.1016/j.nbd.2018.04.014 | Yes; `validated_primary_observation` | Yes; `validated_author_claim` | Results on attenuated fibrotic scar, higher axonal density, and functional recovery; male/female FnEDA-null and littermate WT mice after contusion SCI; RT-PCR, Western, matrix fractionation, IHC, 3-D reconstruction, SMI-312, BMS/mBBB; FnEDA deletion versus WT, with TGF-beta fibroblast culture ancillary | B; L1 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC5995671_article.html`; `data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC5995671_bioc.json`. Whole-lesion phenotype; no receptor-proximal assignment. |
| `M23B-EVID-000006`; `M23B-E000004` | PMCID:PMC7509206; PMID:32957245; DOI:10.1016/j.jmbbm.2020.103953 | Yes; `validated_full_text` | Yes; `validated_author_claim` | Results on AFM mechanics, CNS-cell/ECM scar composition, and dysregulated GAGs; approximately 18-week chronic hemisection SCI tissue with glial/fibrotic regions and naive WM/GM comparators; AFM/Young’s modulus, cell morphometry, GFAP/vimentin/neuronal/myelin IHC, sPG/CSPG/HA assays; chronic hemisection SCI versus naive tissue | B; L2 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_C23B_fulltext/PMC7509206_bioc.json`. Direct chronic SCI tissue observation; no receptor-binding assay. |
| `M23B-EVID-000008`; `M23B-E000007` | PMCID:PMC12394907; PMID:40876929; DOI:10.26508/lsa.202503469 | Yes; `validated_primary_observation` | Yes; `validated_author_claim` | Results on GlcNAc6ST1/4 expression, recovery, myeloid-cell reduction, serotonergic axon sprouting, and collagen/ECM genes; SCI-injured mouse cord and CD11b+ myeloid cells; qPCR, CD11b isolation, IHC, RNA-seq/GO, glycan analysis, BMS, 5-HT/WM staining; constitutive double deficiency versus controls after SCI | B; L1 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_external_PMC12394907.html`. Atomic phenotype/program observation; proposed CD44/hyaluronan or Siglec mechanisms were not tested. |
| `M23B-EVID-000017`; `M23B-E000016` | PMCID:PMC6672107; PMID:17392476; DOI:10.1523/JNEUROSCI.4805-06.2007 | Yes; `validated_primary_observation` | Yes; `validated_author_claim` | Results on OPN expression, locomotion, white matter, neurons, immune cells, and astroglial scar; adult male 129 OPN-KO/WT mice after T13 contusion SCI; qRT-PCR, Western, BMS, Luxol fast blue, NeuN/CD11b/CD3/GFAP IHC; constitutive OPN KO versus WT after 5.6/10 g injury | B; L2 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_external_PMC6672107.html`. Strong SCI observation; receptor was not manipulated, so alpha8beta1 assignment is not established. |
| `M23B-EVID-000018`; `M23B-E000017` | PMCID:PMC4116228; PMID:24932026; DOI:10.1371/journal.pone.0103839 | Yes; `validated_primary_observation` | Yes; `validated_author_claim` | Results on direct TIMP-1/LRP-1 binding and neuronal internalization; CHO LRP-1 mini-receptors, recombinant TIMP-1/LRP-1 domains, primary mouse embryonic cortical neurons; SPR, co-IP, surface biotinylation, fluorescent uptake/confocal; LRP-1 domains II/IV versus SPCT, RAP, exogenous TIMP-1, receptor constructs | B; L2 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_external_PMC4116228.html`. High-yield direct molecular plus neural-context pair; not SCI-specific. |
| `M23B-EVID-000023`; `M23B-E000022` | PMCID:PMC6758826; PMID:12040032; DOI:10.1523/JNEUROSCI.22-11-04274.2002 | Yes; `validated_primary_observation` | Yes; `validated_author_claim` | Results on beta-dystroglycan at inhibitory synapses and genetic requirements for clustering; primary mouse hippocampal neurons/GABAergic synapses; immunocytochemistry/colocalization; agrin-null, gephyrin-null, mdx, conditional DG deletion/Cre | B; L1 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_external_PMC6758826.html`. Atomic synaptic observation; not an SCI or direct agrin-binding experiment. |
| `M23B-EVID-000071`; `M23B-E000046` | PMCID:PMC4315246; PMID:25646087; DOI:10.1083/jcb.201403111 | Yes; `validated_primary_observation` | Yes; `validated_author_claim` | Results on alpha-DG shedding, perlecan binding, and node-compartment effects; rat Schwann cells/sciatic nerve/DRG-Schwann cocultures and mouse DG-deficient nerves; DGFc2/5/6 binding, perlecan Far-Western/ELISA, teased-fiber IHC, clustering assays; DG domain deletion/deficiency, perlecan mutants, heparin/heparinase | B; L2 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC4315246_article.html`. Direct domain/binding evidence with peripheral-neural context; preserve domain and complex scope. |
| `M23B-EVID-000078`; `M23B-E000053` | PMID:7542940; PMCID:PMC301201; DOI:10.1091/mbc.6.4.419 | Yes; `validated_full_text` | Yes; `validated_author_claim` | Results on beta8 characterization and laminin-1/collagen-IV/FN receptor activity; embryonic chick DRG sensory neurons on ECM substrates; surface biotinylation/IP, substrate-coated neurite outgrowth, affinity-purified antibody/Fab blockade, fragment mapping; anti-beta8/alphaV/beta1, intact or heat-inactivated laminin-1 and FN fragments | B; L2 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC301201_article.html`; `data/raw/evidence/module20_24_supervised_cli_phase2/retry_C23B_PMC301201_beta8_neural_fulltext_7542940.pdf`. Atomic neural ECM observation; preserve beta8/composite-receptor scope. |

## Needs manual source review

These are high-yield because a stable anchor and local full-text-like artifact
are present, but the existing phase-2 status is abstract-bounded,
`validated_full_text_importable`, or unresolved. Do not promote without a
manual check of the cited passage and claim scope.

| Candidate ID; edge | Source anchor | Atomic observation / registered claim | Exact locus; model; assay; perturbation | Current grade/context | Artifact; reason |
|---|---|---|---|---|---|
| `M23B-EVID-000002`; `M23B-E000001` | PMID:36336030; DOI:10.1016/j.expneurol.2022.114264 | Observation `validated_full_text_importable`; claim `validated_author_claim`; not yet treated as fully verified here | Results §§3.2–3.5 and Discussion; primary neonatal mouse astrocytes, collagen-I-grown scar-forming astrocytes, T9 70-kdyn contusion/transplant context; IF GFAP/N-cadherin/GAP43, qPCR, transplantation, laser-microdissection expression; IL-6+sIL-6R, collagen-I, anti-beta1/N-cadherin blockade, post-SCI anti-beta1 | B; L1 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_C23B_batch285_Tamaru_36336030_fulltext.pdf`; `data/raw/evidence/module20_24_supervised_cli_phase2/retry_C23B_batch285_Tamaru_36336030_fulltext.txt`. Verify exact quantitative passage and whether blockade supports the registered program claim. |
| `M23B-EVID-000007`; `M23B-E000006` | PMCID:PMC12048928; PMID:40317093; DOI:10.1186/s40478-025-01995-0 | Observation `validated_primary_observation`; claim `validated_author_claim`; retained for manual review because the combined kindlin-1 plus alpha9 intervention lacks an alpha9-only arm | Results/Mechanisms of axon regeneration; adult female rat DRG neurons after C4/T10 complete dorsal-column crush; AAV transduction, IHC, tissue clearing/light-sheet, sensory behavior, cFOS/VGLUT; AAV-K1-GFP + AAV-alpha9-V5 versus AAV-GFP, no alpha9-only group | B; L1 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_C23B_batch286_PMC12048928_alpha9_kindlin1.html`. Atomic functional observation, but causal attribution is joint-intervention limited. |
| `M23B-EVID-000009`; `M23B-E000008` | PMCID:PMC2199946; PMID:7542249; DOI:10.1083/jcb.130.2.451 | Observation and claim `validated_full_text_importable`; manual verification needed | Abstract/Results on CD31 adhesion and alphaVbeta3 precipitation; recombinant CD31, leukocytes/endothelial lysates; soluble-recombinant adhesion, alphaVbeta3 antibody inhibition, IP/precipitation; recombinant CD31, domain-2 constructs, alphaVbeta3 antibodies | B; L1 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_C23B_batch062_PMC2199946_PECAM1_alphaVbeta3.html`. Verify complete alphaVbeta3 requirement and directness wording. |
| `M23B-EVID-000025`; `M23B-E000024` | PMID:28628111; DOI:10.1038/nm.4354 | Observation `validated_abstract_bounded`; claim `validated_author_claim`; not atomic/full-text verified | Abstract; mouse spinal-cord injury collagen-I/integrin/N-cadherin pathway study; model/assay details remain abstract-bounded; collagen-I/integrin/N-cadherin pathway perturbation as registered | B; L4 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_external_pubmed_28628111.xml`. High SCI relevance, but ITGA1 is not isolated from other beta1 integrins and purified collagen-I–alpha1beta1 binding is absent. |
| `M23B-EVID-000250`; `M23B-E000176` | PMCID:PMC3755723; PMID:23966707 | Observation and claim `unresolved`; exact source passage not retained in phase-2 staging | Results/source sections not located; perivascular fibroblasts in perivascular lesion scar; lineage tracing, light-sheet imaging, IHC, NG2 analysis; lineage-tracing model/controls require manual extraction | B; L4 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_C23B085_PMC3755723_ncbi.xml`. Stable anchor plus local artifact, but no verified atomic observation or author claim in the staged row. |
| `M23B-EVID-000346`; `M23B-E000249` | DOI:10.1083/jcb.200602043; PMCID:PMC2064262; PMID:16908672; comparator PMIDs:8175719, 9749725 | Observation and claim `abstract_only_not_import_ready` | Primary abstracts/Introduction/receptor-ligand context; perinatal rat brain neurons, brain membranes, mouse embryonic forebrain neurons; affinity-matrix receptor isolation, solid-phase binding, antibody blockade, matrix migration; immobilized HB-GAM/PTN, heparin/N-syndecan competition or deficiency | B; L2 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_C23B_PMC2064262_PTN_syndecan3_full.html`; `data/raw/evidence/module20_24_supervised_cli_phase2/retry_C23B_fulltext_batch2/PMC2064262_bioc.json`. Likely recoverable, but exact source unit and claim wording remain unverified. |
| `M23B-EVID-000083`; `M23B-E000058` | PMID:17598176; DOI:10.1002/glia.20536 | Observation and claim `abstract_only_not_import_ready` | PubMed abstract; Schwann cells and differentiating neuron-Schwann cocultures; laminin-2-Sepharose binding, antibody-blocking adhesion, siRNA, co-localization, alpha7beta1-FAK co-IP; alpha7 antibody/siRNA and DG combined knockdown | B; L2 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMID17598176.html`. Manual review can resolve the exact tissue/species and whether the registered alpha7beta1 claim is supported. |
| `M23B-EVID-000878`; `M23B-E000655` | PMCID:PMC4578660 | Observation and claim `unresolved` | Source sections not located in staging; hippocampal neurons/co-cultures; heterologous adhesion and synaptogenic differentiation assays; perturbation details not resolved | B; L2 | `data/raw/evidence/module20_24_supervised_cli_phase2/retry_C23B268_PMC4578660_bioc.json`; `data/raw/evidence/module20_24_supervised_cli_phase2/retry_C23B172_PMC4578660_LRFN4_PTPRD_fulltext.html`. Artifact exists, but current row does not establish an atomic observation or registered claim. |

## Unresolved disposition

The remaining 23B rows with no retained content-level source resolution, no
stable paper anchor, or only negative/bounded search evidence remain
`unresolved`. Filename-token matches alone do not change that disposition.
In particular, the ledger’s 182 E-grade rows and 114 unassigned rows must not
be upgraded from the presence of a local artifact; the 177 non-exportable rows
remain outside the traversable evidence set. No TF/program identity, receptor
subunit, species, assay, or causal direction was inferred beyond the existing
phase-2 fields above.
