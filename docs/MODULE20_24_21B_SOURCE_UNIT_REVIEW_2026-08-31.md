# Module 21B source-unit promotion review

Read-only review completed against the 25 `promotion_candidate` rows in
`/private/tmp/module20_24_21b_anchor_recovery_report.md`. The exact retained
source artifacts were inspected at the source sections, figure captions, and
methods described below. No repository file, database, ledger, register, or
canonical import artifact was modified.

## Interpretation of gate results

`PASS` means the listed source supports an atomic measured/tested observation
and a separate author interpretation for the registered evidence unit.
`FAIL` means the source supports only a neighboring observation, correlation,
or mechanism, or does not establish the registered pair/direction. A row with
either gate failed is retained as `needs_manual_source_review`; no evidence
grade or context level is upgraded.

The current ledger values are preserved exactly: evidence grade `B` for every
row, context level `L1` except `M21B-EVID-000017` and
`M21B-EVID-000023`, which remain `L2`.

## Review rows

### 1. `P2MAN-M21B-M21B-EVID-000003-PMID_9653170`

- Evidence ID: `M21B-EVID-000003`; identifier: `PMID:9653170; PMCID:PMC20959`.
- Paper/title: Lu et al., “Targeted disruption of the interferon-γ receptor 2 gene results in severe immune defects in mice.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_external_PMC20959.html`.
- Exact source locus: Materials and Methods; Results, “Mutation of IFN-γR2 Results in Defective IFN-γ Signaling,” “IFN-γR2 Is Required for the Regulation of Ig Class Switching by IFN-γ,” and “Compromised Cellular Immunity of IFN-γR2−/− Mice”; Figs. 2–5; Discussion.
- Observation: IFN-γ stimulation activated Jak1/Jak2 and Stat1 in wild-type mouse embryonic fibroblasts/splenocytes, but not IFN-γR2-null cells; IFN-γ-induced IRF-1 and GBP-1 transcripts and IgG2a switching were reduced or absent in null cells (Fig. 2A–C; Fig. 3).
- Author claim: The authors conclude that IFN-γR2 is essential for IFN-γ signaling and IFN-γ-mediated immune responses in vivo.
- Species/model/cells: Mouse IFN-γR2 wild-type and knockout mice; embryonic fibroblasts, splenocytes, IgM+ B cells, CD4+ T cells, lymph-node cells.
- Assay/perturbation: Targeted IFN-γR2 disruption; IFN-γ stimulation; immunoprecipitation/immunoblotting, EMSA, Northern blot, ELISA, class-switching, contact-hypersensitivity, and Listeria-survival assays.
- Limitations: Mouse immune systems, not CNS/SCI; establishes receptor-chain requirement but not a new extracellular binding edge or astrocyte-specific response.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 2. `P2MAN-M21B-M21B-EVID-000004-PMID_16611992`

- Evidence ID: `M21B-EVID-000004`; identifier: `PMID:16611992; PMCID:PMC1447428`.
- Paper/title: Zheng et al., “Competitive Control of Independent Programs of Tumor Necrosis Factor Receptor-Induced Cell Death by TRADD and RIP1.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC1447428_article.html`.
- Exact source locus: Materials and Methods; Results, “TRADD is not essential…,” “RIP1 and TRADD are both essential for TNF-α-induced NF-κB activation,” “TRADD and RIP1 can independently and competitively associate with TNFR1,” and “TRAF2 is recruited to TNFR1 through TRADD”; Figs. 1–5; Discussion.
- Observation: In Jurkat cells, TNF-α-induced TNFR1 complexes recruited TRADD, RIP1, TRAF2, and FADD; TRADD/RIP1 depletion separated NF-κB, caspase-8 apoptosis, and RIP1-dependent nonapoptotic death branches (Figs. 2–5).
- Author claim: The authors conclude that TNFR1 signals diverge proximally through competing TRADD and RIP1 associations, with distinct apoptosis, necrosis-like death, and NF-κB outputs.
- Species/model/cells: Human Jurkat T-cell leukemia cells, including wild-type, FADD-deficient, RIP1-deficient, and caspase-8-deficient lines.
- Assay/perturbation: TNF-α; TRADD/RIP1 siRNA; genetic deficiencies; zVAD-FMK and BHA; cell-death assays, co-immunoprecipitation/Western blot, NF-κB microscopy/luciferase, cytochrome-c and ROS assays.
- Limitations: Transformed human-cell model; no SCI receiver-cell context; does not establish one ternary TNFR1–TRADD–TRAF2–RIP1 complex.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 3. `P2MAN-M21B-M21B-EVID-000005-PMID_11416133`

- Evidence ID: `M21B-EVID-000005`; identifier: `PMID:11416133; PMCID:PMC87113`.
- Paper/title: Jefferies et al., “Transactivation by the p65 Subunit of NF-κB in Response to Interleukin-1 (IL-1) Involves MyD88, IL-1 Receptor-Associated Kinase 1, TRAF-6, and Rac1.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC87113_article.html`.
- Exact source locus: Materials and Methods; Results, “MyD88, IRAK-1, and TRAF-6 drive p65-mediated transactivation,” “Rac1 lies downstream of MyD88…,” and “Rac1 is detected in a complex with MyD88 and IL-1RAcP”; Figs. 1–6; Discussion.
- Observation: Wild-type MyD88, IRAK-1, and TRAF-6 enhanced IL-1-induced Gal4-p65 activity, while dominant-negative forms, MyD88 deficiency, or IRAK deficiency reduced it; dominant-negative Rac1 blocked the response and Rac1 associated with MyD88/IL-1RAcP (Figs. 1–6).
- Author claim: The authors conclude that a MyD88–IRAK-1–TRAF-6–Rac1 signaling complex is required for IL-1-induced p65-dependent transactivation.
- Species/model/cells: EL4.NOB-1 mouse T-cell line; MyD88-null mouse-derived cells; IRAK-deficient 293 cells; transfected human 293 cells.
- Assay/perturbation: IL-1; wild-type and dominant-negative MyD88, IRAK-1, TRAF-6, and Rac1; Gal4-p65/luciferase reporters, Western blotting, GST pull-down, and co-immunoprecipitation.
- Limitations: Reporter/transfection systems; Rac1/IRAK/TRAF6 ordering is specific to the measured p65-transactivation output and is not a direct TRAF6-activation assay.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 4. `P2MAN-M21B-M21B-EVID-000005-PMID_12538665`

- Evidence ID: `M21B-EVID-000005`; identifier: `PMID:12538665; PMCID:PMC2193806`.
- Paper/title: Burns et al., “Inhibition of Interleukin 1 Receptor/Toll-like Receptor Signaling through the Alternatively Spliced, Short Form of MyD88 Is Due to Its Failure to Recruit IRAK-4.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC2193806_article.html`.
- Exact source locus: Introduction; Materials and Methods; Results and Discussion, “The ID of MyD88 Is Critical for IRAK-1 Phosphorylation,” “MyD88 Is Required for IRAK-4-induced IRAK-1 Phosphorylation,” and “MyD88s Does not Bind to IRAK-4 and Blocks Recruitment of IRAK-4 to the IL-1Rs”; Figs. 1–4.
- Observation: MyD88, but not MyD88s, enabled IRAK-4-associated IRAK-1 phosphorylation and IL-1β-induced IκB degradation; MyD88s failed to bind IRAK-4 and inhibited IRAK-4 recruitment to IL-1 receptors (Figs. 1–4).
- Author claim: The authors conclude that MyD88 links IRAK-1 and IRAK-4, whereas the short MyD88 isoform negatively regulates IL-1/TLR signaling by preventing IRAK-4 access to IRAK-1.
- Species/model/cells: MyD88-null mouse embryo fibroblasts reconstituted with MyD88 or MyD88s; HEK293T cells; yeast interaction system.
- Assay/perturbation: IL-1β/TNFα; MyD88/MyD88s reconstitution; IRAK-1 kinase-dead and IRAK-4 kinase-dead mutants; co-immunoprecipitation, yeast two-hybrid, in-vitro kinase, and immunoblot assays.
- Limitations: Reconstituted/overexpression systems; the paper states that activation of IRAK-4 at the receptor was not formally demonstrated; no CNS/SCI context.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 5. `P2MAN-M21B-M21B-EVID-000006-PMID_31289212`

- Evidence ID: `M21B-EVID-000006`; identifier: `PMID:31289212; PMCID:PMC7059217`.
- Paper/title: Spinosa et al., “Short-term Cellular Memory Tunes CXCR4 Signaling Responses.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC7059217_article.html`.
- Exact source locus: Results, “Growth factor conditioning potentiates subsequent CXCR4 signaling,” “Maps of the signaling landscape…,” “MEK inhibition potentiates subsequent CXCR4-mediated Akt signaling,” and “mTORC1 inhibition potentiates subsequent CXCR4-mediated Akt and ERK signaling”; Figs. 1–8; Discussion; Materials and Methods.
- Observation: CXCL12-CXCR4 stimulation activated ERK and Akt; FBS/EGF conditioning increased the fraction and amplitude of subsequent CXCR4-Akt/ERK responses, while trametinib or ridaforolimus conditioning potentiated Akt and/or ERK in defined subpopulations (Figs. 1, 4, 7, 8).
- Author claim: The authors conclude that short-term cellular signaling states, especially PI3K, Ras, and mTORC1 state, tune CXCR4 responsiveness and create heterogeneous Akt/ERK outputs.
- Species/model/cells: Human breast-cancer cell lines MDA-MB-231 and SUM-159 and patient-derived Vari-068 cells engineered to express CXCR4 reporters.
- Assay/perturbation: CXCL12; FBS/EGF conditioning; MEK inhibitor trametinib and mTORC1 inhibitor ridaforolimus; live-cell ERK/Akt kinase-translocation reporters plus conditional signaling model.
- Limitations: No direct CXCR4–GNAI binding or Src–EGFR transactivation assay; 2-D cancer-cell systems, not SCI receiver cells; computational pathway details are model assumptions.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS` for the measured CXCR4-to-Akt/ERK unit; `source_supported_atomic_candidate` (not imported).

### 6. `P2MAN-M21B-M21B-EVID-000008-PMID_16765933`

- Evidence ID: `M21B-EVID-000008`; identifier: `PMID:16765933; PMCID:PMC7116376`.
- Paper/title: Arnold et al., “Dose-dependent Smad1, Smad5 and Smad8 signaling in the early mouse embryo.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC7116376_article.html`.
- Exact source locus: Introduction; Materials and Methods; Results, “Highly restricted Smad8 expression…,” “Smad8 mutant mice develop normally…,” and Smad1/Smad5 dosage sections; Figs. 1–8; Discussion.
- Observation: Smad1 and Smad5 were broadly expressed in early mouse embryos, Smad8 expression was spatially restricted, and Smad1/Smad5 dosage affected embryonic and primordial-germ-cell phenotypes (Figs. 2, 6, 8).
- Author claim: The authors interpret Smad8 as a context-dependent modulator of BMP signaling, but explicitly present the possibility that Smad8 expression is a BMP target as speculation.
- Species/model/cells: Mouse embryos, embryonic tissues, Smad8 reporter/null alleles, and Smad1/Smad5 heterozygous genetic crosses.
- Assay/perturbation: Whole-mount in-situ hybridization, RNase protection, LacZ reporter, histology, and germline Smad8/Smad1/Smad5 genetics; no BMP ligand stimulation or receptor-complex perturbation.
- Limitations: The artifact does not establish a BMP receptor→Smad1/5/8 activation event, BMPR paralog composition, or Smad–Smad4 complex; no adult SCI context.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `FAIL` for the registered BMP-receptor activation unit; claim `FAIL` for a validated BMP→Smad mechanism; `needs_manual_source_review`.

### 7. `P2MAN-M21B-M21B-EVID-000010-PMID_11447289`

- Evidence ID: `M21B-EVID-000010`; identifier: `PMID:11447289; PMCID:PMC37478`.
- Paper/title: Hadari et al., “Critical role for the docking-protein FRS2α in FGF receptor-mediated signal transduction pathways.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC37478_article.html`.
- Exact source locus: Methods; Results, “FRS2α Is Required for Recruitment of PI-3 Kinase via the Docking Protein Gab1,” “FRS2α-Dependent and -Independent MAP Kinase (ERK) Stimulation,” “FRS2α Is Required for FGF-Induced Cell Proliferation,” and “FRS2α Is Required for FGF-Induced Cell Migration”; Figs. 1–5; Discussion.
- Observation: FRS2α-deficient mouse fibroblasts showed impaired FGF-induced MAPK/ERK and PI3K/Gab1 signaling, proliferation, and migration; wild-type FRS2α rescued these responses, with partial rescue by selected binding-site mutants (Figs. 2–5).
- Author claim: The authors conclude that FRS2α is a docking platform linking FGFR stimulation to Ras/MAPK, PI3K, proliferation, and migration.
- Species/model/cells: Mouse FRS2α-null embryonic-stem-cell-derived fibroblasts and rescued fibroblasts.
- Assay/perturbation: FGF stimulation; Frs2α gene targeting and wild-type/4F/6F/2F rescue; phospho-MAPK immunoblot, PI3K assay, proliferation assay, and Boyden-chamber migration.
- Limitations: Requirement/deficiency does not alone prove direct FGFR–FRS2α recruitment; ligand and FGFR paralog specificity and SCI relevance are unresolved.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 8. `P2MAN-M21B-M21B-EVID-000010-PMID_11997436`

- Evidence ID: `M21B-EVID-000010`; identifier: `PMID:11997436; PMCID:PMC124463`.
- Paper/title: Wong et al., “FRS2α attenuates FGF receptor signaling by Grb2-mediated recruitment of the ubiquitin ligase Cbl.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC124463_article.html`.
- Exact source locus: Materials and Methods; Results, “Cbl Forms a Complex with FRS2α Primarily Through Interactions with Grb2…,” “The Recruitment of Cbl by FRS2α Results in the Ubiquitination of FRS2α and FGFR,” and “Partial Attenuation of FGFR Down-Regulation in FRS2α-Deficient Cells”; Figs. 1–5; Discussion.
- Observation: FGF-stimulated tyrosine-phosphorylated FRS2α joined a pre-existing Grb2/Cbl complex; Cbl/FRS2α promoted ubiquitination of FRS2α and FGFR, and FRS2α deficiency or Grb2-binding mutants slowed FGF internalization and FGFR down-regulation (Figs. 1, 4, 5).
- Author claim: The authors conclude that FRS2α recruits Cbl indirectly through Grb2 to provide a negative/attenuating FGF-receptor signaling mechanism.
- Species/model/cells: NIH 3T3 cells, mouse embryonic fibroblasts, PC12 cells, HeLa cells, HEK293 cells, and FRS2α-deficient/rescued fibroblasts.
- Assay/perturbation: FGF; Cbl/FRS2α/FGFR expression and FRS2α binding-site mutants; pull-down/co-immunoprecipitation, ubiquitination immunoblotting, and 125I-FGF internalization/FGFR half-life assays.
- Limitations: Overexpression contributes to the complex/ubiquitination measurements; FGFR down-regulation remained only partially affected, with redundant mechanisms possible; no SCI context.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 9. `P2MAN-M21B-M21B-EVID-000012-PMID_22174934`

- Evidence ID: `M21B-EVID-000012`; identifier: `PMID:22174934; PMCID:PMC3236226`.
- Paper/title: Dellinger and Brekken, “Phosphorylation of Akt and ERK1/2 Is Required for VEGF-A/VEGFR2-Induced Proliferation and Migration of Lymphatic Endothelium.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC3236226_article.html`.
- Exact source locus: Introduction; Results, “VEGFR2 is the primary signaling VEGF-A receptor in LECs,” “VEGF-A promotes PKC dependent phosphorylation of ERK1/2,” and “Phosphorylation of ERK1/2 and Akt is required…”; Figs. 1–5; Discussion; Materials and Methods.
- Observation: In primary lymphatic endothelial cells, VEGF-A/VEGFR2 activated PLCγ/PKC/ERK1/2 and PI3K/Akt; inhibition of VEGFR2, ERK1/2, or Akt reduced proliferation/migration (Figs. 2–5).
- Author claim: The authors conclude that VEGF-A activation of VEGFR2, rather than VEGFR1, drives LEC proliferation and migration through ERK1/2 and PI3K/Akt.
- Species/model/cells: Primary human lymphatic endothelial cells and mouse tumor lymphangiogenesis model.
- Assay/perturbation: VEGF-A; VEGFR2-selective anti-VEGF-A antibody, receptor comparison, PKC/MEK/PI3K inhibitors; immunoblot, proliferation/viability, migration, and tissue analyses.
- Limitations: Vascular-endothelial comparator, not SCI astrocytes; in-vivo antibody effects can involve other tumor-microenvironment cell types.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 10. `P2MAN-M21B-M21B-EVID-000012-PMID_22745786`

- Evidence ID: `M21B-EVID-000012`; identifier: `PMID:22745786; PMCID:PMC3382126`.
- Paper/title: Coso et al., “Vascular Endothelial Growth Factor Receptor-3 Directly Interacts with Phosphatidylinositol 3-Kinase to Regulate Lymphangiogenesis.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC3382126_article.html`.
- Exact source locus: Background/Methods and Results; Results, “VEGF-C Induces PI3K-dependent Akt Activation…,” “P70S6K, eNOS and PLCγ…,” “Blocking PI3K…,” and “VEGFR-3 and PI3K Form a Complex”; Figs. 1–7; Discussion.
- Observation: VEGF-C/VEGFR3 activated PI3K/Akt, P70S6K, eNOS, PLCγ1, and ERK-related outputs in LECs; PI3K blockade reduced tube formation/migration; VEGFR3 and PI3K p85 were detected in a complex (Figs. 1–5).
- Author claim: The authors conclude that VEGFR3-associated PI3K/Akt signaling is a central VEGF-C lymphangiogenic pathway and that VEGFR3–PI3K interaction is associated with metastatic specimens.
- Species/model/cells: Primary human lymphatic endothelial cells and human lung, melanoma, breast, and colon tumor specimens.
- Assay/perturbation: VEGF-C; PI3K inhibition, PLCγ1 knockdown, and receptor stimulation; Western blot, tube formation, migration, co-immunoprecipitation, and proximity-ligation assay.
- Limitations: Tumor/LEC comparator evidence; physical association is not a purified direct-binding or SCI-cell mechanism; ligand-specific branch differences remain.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 11. `P2MAN-M21B-M21B-EVID-000013-PMID_18077588`

- Evidence ID: `M21B-EVID-000013`; identifier: `PMID:18077588; PMCID:PMC5328672`.
- Paper/title: Zeng et al., “Initiation of Wnt signaling: control of Wnt coreceptor Lrp6 phosphorylation/activation via frizzled, dishevelled and axin functions.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC5328672_article.html`.
- Exact source locus: Introduction; Materials and Methods; Results, Figs. 1–5; Discussion and Fig. 6 model.
- Observation: Wnt-induced LRP6 phosphorylation required Frizzled and Dishevelled; forced Frizzled–LRP6 association activated LRP6; Dishevelled recruited Axin, and Axin/GSK3 functions were required for LRP6 phosphorylation and β-catenin signaling (Figs. 1–5).
- Author claim: The authors propose a sequential Frizzled→Dishevelled→Axin/GSK3 recruitment and amplification model for Wnt-induced LRP6 activation.
- Species/model/cells: Mammalian cell lines and Xenopus laevis embryonic animal-pole explants.
- Assay/perturbation: Wnt stimulation; Frizzled knockdown/mutants, forced Frizzled–LRP6 association, Dishevelled domain mutants, membrane-tethered Axin/GSK3 manipulations; immunoblotting, reporter assays, and embryonic immunofluorescence.
- Limitations: Supports the signalosome/pathway sequence but not direct molecular edges for every registered pair; noncanonical Wnt branches and SCI relevance are unresolved.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 12. `P2MAN-M21B-M21B-EVID-000014-PMID_16287852`

- Evidence ID: `M21B-EVID-000014`; identifier: `PMID:16287852; PMCID:PMC1291242`.
- Paper/title: Oswald et al., “RBP-Jκ/SHARP Recruits CtIP/CtBP Corepressors To Silence Notch Target Genes.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC1291242_article.html`.
- Exact source locus: Materials and Methods; Results, “SHARP associates with the CtBP corepressor,” “SHARP interacts with the CtIP corepressor directly,” “SHARP, CtIP, and CtBP act together to repress transcription,” and “Formation of the endogenous corepressor complex”; Figs. 1–7; Discussion.
- Observation: SHARP associated with CtBP and directly interacted with CtIP; RBP-Jκ/SHARP/CtIP/CtBP complexes repressed reporter transcription and endogenous Notch target-gene expression (Figs. 1–7).
- Author claim: The authors conclude that SHARP recruits CtIP/CtBP corepressors to RBP-Jκ to silence Notch target genes.
- Species/model/cells: Mammalian cultured cells and Xenopus laevis embryos/extracts.
- Assay/perturbation: SHARP/CtIP/CtBP/RBP-Jκ expression and domain mutants; reporter assays, GST pull-down, yeast two-hybrid, co-immunoprecipitation, EMSA, RNA analysis, and Xenopus injection.
- Limitations: This exact artifact does not show gamma-secretase-dependent NICD release or establish the registered receptor-processing→NICD→RBP-Jκ unit; it is a downstream corepressor study.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `FAIL` for the registered NICD-processing unit; claim `FAIL` for that unit; `needs_manual_source_review`.

### 13. `P2MAN-M21B-M21B-EVID-000015-PMID_38569939`

- Evidence ID: `M21B-EVID-000015`; identifier: `PMID:38569939; PMCID:PMC11039321`.
- Paper/title: Rafii et al., “Engineered interleukin-6-derived cytokines recruit artificial receptor complexes and disclose CNTF signaling via the OSMR.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC11039321_article.html`.
- Exact source locus: Results, “CNTF signals via the CNTFR:gp130:OSMR complex”; Figs. 6–7 and related receptor-complex results; Discussion; Experimental procedures.
- Observation: CNTF induced proliferation and STAT3 phosphorylation in Ba/F3 cells expressing CNTFR:gp130:LIFR or CNTFR:gp130:OSMR; the OSMR-containing complex showed high sensitivity (Fig. 6).
- Author claim: The authors conclude that CNTF can use CNTFR:gp130:OSMR as an alternative high-affinity receptor complex in addition to CNTFR:gp130:LIFR.
- Species/model/cells: Murine Ba/F3 pre-B cells reconstituted with human CNTFR, gp130, LIFR, or OSMR; mouse tissue signaling after designer-cytokine injection.
- Assay/perturbation: CNTF and engineered cytokimeras; receptor-complex reconstitution; proliferation assays, phospho-STAT3/ERK immunoblotting, transcriptomics, and receptor-complex comparisons.
- Limitations: Artificial receptor-complex/overexpression system; branch weights and relevance to injured SCI astrocytes are not established.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 14. `P2MAN-M21B-M21B-EVID-000016-PMID_15342787`

- Evidence ID: `M21B-EVID-000016`; identifier: `PMID:15342787; PMCID:PMC524725`.
- Paper/title: Ozog et al., “The Complex of Ciliary Neurotrophic Factor-Ciliary Neurotrophic Factor Receptor α Up-Regulates Connexin43 and Intercellular Coupling in Astrocytes via the Janus Tyrosine Kinase/Signal Transducer and Activator of Transcription Pathway.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC524725_article.html`.
- Exact source locus: Materials and Methods, “Exposure to CNTF and CNTFRα”; Results, “CNTF Complex Increases Cx43 Protein Expression and Intercellular Coupling,” “Complex-Induced Increase in Cx43 Expression Is Mediated by the JAK/STAT Pathway,” and promoter/coupling results; Figs. 1–10; Discussion.
- Observation: CNTF plus soluble CNTFRα, but neither alone, increased Cx43 mRNA/protein and dye-transfer coupling in mature mouse cortical astrocytes; AG490 blocked the Cx43 response and nuclear phospho-STAT3 was observed (Figs. 2–9).
- Author claim: The authors conclude that the CNTF–CNTFRα complex increases astrocyte Cx43 and intercellular coupling through JAK/STAT signaling.
- Species/model/cells: Mature mouse cortical astrocytes and ROS17/2.8 astrocyte-like cells.
- Assay/perturbation: CNTF, soluble CNTFRα, CNTF–CNTFRα complex; JAK/STAT inhibitor AG490 and MEK inhibitor U0126; immunoblot, RT-PCR, immunocytochemistry, dye transfer, and Cx43-promoter reporter assays.
- Limitations: In-vitro astrocytes; receptor subunit stoichiometry in injured spinal cord is not resolved; soluble receptor complex is not the same as endogenous SCI signaling.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 15. `P2MAN-M21B-M21B-EVID-000017-PMID_18615534`

- Evidence ID: `M21B-EVID-000017`; identifier: `PMID:18615534; PMCID:PMC5518483`.
- Paper/title: Tripathi and McTigue, “Chronically Increased Ciliary Neurotrophic Factor and Fibroblast Growth Factor-2 Expression After Spinal Contusion in Rats.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC5518483_article.html`.
- Exact source locus: Materials and Methods; Results, “CNTF protein expression increases following SCI,” “Astrocytes and OLs display CNTF immunoreactivity,” “CNTFRα expression following SCI,” “FGF-2 expression following SCI,” and “pSTAT3 expression and localization following SCI”; Figs. 1, 5–11; Discussion.
- Observation: After rat spinal contusion, CNTF and CNTFRα protein increased over the post-injury time course, CNTF localized to astrocytes and oligodendrocytes, FGF-2+ cells increased near lesion borders, and pSTAT3 remained elevated in lesion-border astrocytes/OL-lineage cells (Figs. 1, 5–11).
- Author claim: The authors conclude that components associated with CNTF signaling are up-regulated after contusion and may contribute to the injury response; they did not test CNTF perturbation or prove a CNTF-driven functional output.
- Species/model/cells: Adult rat spinal cord contusion; spinal astrocytes, oligodendrocytes, NG2+ cells, and lesion-border tissue.
- Assay/perturbation: T9 contusion with untreated recovery; Western blot, immunohistochemistry/confocal colocalization, CNTF/CNTFRα/FGF-2/pSTAT3 measurements; no ligand or receptor perturbation.
- Limitations: Correlational SCI tissue study; no isolated CNTFRa–gp130–LIFR/OSMR mechanism, no causal CNTF-to-STAT3 test, and no single receiver-cell functional endpoint.
- Ledger: evidence grade `B`; context `L2`.
- Gates/disposition: observation `FAIL` for the registered causal CNTF astrocyte-function unit; claim `FAIL` for that causal unit; `needs_manual_source_review`.

### 16. `P2MAN-M21B-M21B-EVID-000018-PMID_37725008`

- Evidence ID: `M21B-EVID-000018`; identifier: `PMID:37725008; PMCID:PMC10517332`.
- Paper/title: Mesev et al., “Synthetic Heterodimers of Type III Interferon Receptors Require TYK2 for STAT Activation.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC10517332_article.html`.
- Exact source locus: Introduction; Materials and Methods; Results, “Signaling by IFN-λ subtypes is unaffected in Tyk2−/− U2OS epithelial cells,” “Heterodimeric type III IFN receptor chimeras require TYK2 for STAT1 activation,” and “Noncanonical IFN receptor pairs reveal TYK2-independent signaling complexes”; Figs. 1–5; Discussion and Fig. 6.
- Observation: In synthetic type-III receptor heterodimers, TYK2 CRISPR loss or receptor-pair changes altered IFN-λ-induced STAT1 activation, while some noncanonical receptor pairs retained TYK2-independent signaling (Figs. 1–5).
- Author claim: The authors conclude that receptor-chain composition determines whether type-III IFN signaling requires TYK2 for STAT activation.
- Species/model/cells: Human U2OS epithelial cells engineered with synthetic IFN receptor pairs.
- Assay/perturbation: IFN-λ subtypes; TYK2 CRISPR knockout; synthetic receptor chimeras; phospho-STAT immunoblotting, confocal microscopy, and RT-qPCR.
- Limitations: Synthetic receptor context; does not transfer directly to IFNAR/IFNGR or establish the same branch in astrocytes/SCI.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 17. `P2MAN-M21B-M21B-EVID-000019-PMID_20878770`

- Evidence ID: `M21B-EVID-000019`; identifier: `PMID:20878770; PMCID:PMC3082435`.
- Paper/title: Li et al., “Interferon Lambda Inhibits Herpes Simplex Virus Type I Infection of Human Astrocytes and Neurons.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC3082435_article.html`.
- Exact source locus: Materials and Methods; Results, “IFN-λ Inhibits HSV-1 Infection…,” “Anti-HSV-1 Effect of IFN-λ is Mediated through Its Receptor,” “IFN-λ Activates Type I IFN Pathway,” and “IFN-λ Modulates the Key Regulators…”; Figs. 1–7; Discussion.
- Observation: IFN-λ1/2 pretreatment reduced HSV-1 DNA/protein in primary human astrocytes and neurons; anti-IL-10Rβ attenuated the antiviral effect, and IFN-λ induced type-I-IFN/ISG-associated transcripts (Figs. 2–7).
- Author claim: The authors conclude that IFN-λ receptor signaling contributes to antiviral protection in human astrocytes and neurons.
- Species/model/cells: Primary human astrocytes, primary human neurons, and human astrocyte cultures.
- Assay/perturbation: IFN-λ1/2 pretreatment; HSV-1 infection; anti-IL-10Rβ and anti-IFNAR antibodies; qPCR for viral gD/host genes, immunofluorescence, and protein-expression assays.
- Limitations: The source does not test a necessary JAK/STAT kinase or IRF5/IRF7 perturbation; the type-I-IFN-pathway interpretation is not a direct kinase-mechanism demonstration.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS` for the IFN-λ receptor-dependent antiviral outcome; claim `FAIL` for a causal IFN-λ→JAK/STAT→IRF mechanism; `needs_manual_source_review`.

### 18. `P2MAN-M21B-M21B-EVID-000019-PMID_22057682`

- Evidence ID: `M21B-EVID-000019`; identifier: `PMID:22057682; PMCID:PMC3411314`.
- Paper/title: Li et al., “Induction of IFN-lambda contributes to TLR3-mediated HSV-1 inhibition in astrocytes.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_PMC3411314_article.html`.
- Exact source locus: Materials and Methods; Results, “IFN-λ and IFN-λ Receptor Expression…,” “TLR3 Activation Induced IFN-λ Expression…,” “Induction of Endogenous IFN-λ Contributes to HSV-1 Inhibition,” and “TLR3-mediated IFN-λ Induction is Regulated by IRF3 and IRF7”; Figs. 1–7; Discussion.
- Observation: PolyI:C/TLR3 stimulation induced IFN-λ1 and IFN-λ2/3 in human astrocytes; anti-IL-10Rβ attenuated PolyI:C-mediated HSV-1 inhibition; recombinant IFN-λ also inhibited HSV-1; IRF3/IRF7 knockdown reduced pathway induction (Figs. 2–7).
- Author claim: The authors conclude that endogenous IFN-λ is a contributor to TLR3-mediated antiviral activity in human astrocytes.
- Species/model/cells: Primary human astrocytes, U373 astrocytoma cells, and NT2-N controls.
- Assay/perturbation: PolyI:C, recombinant IFN-λ, anti-IL-10Rβ, IRF3/IRF7 shRNA, and HSV-1; RT-qPCR, receptor-expression assays, immunofluorescence, and viral DNA/protein assays.
- Limitations: Strong TLR3→IFN-λ→antiviral evidence, but no direct JAK/STAT kinase perturbation or traumatic-SCI model; do not infer a terminal IRF mechanism beyond the tested IRF3/IRF7 induction results.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS` for the registered TLR3/IFN-λ antiviral unit; `source_supported_atomic_candidate` (not imported).

### 19. `P2MAN-M21B-M21B-EVID-000021-PMID_20038584`

- Evidence ID: `M21B-EVID-000021`; identifier: `PMID:20038584; PMCID:PMC2844188`.
- Paper/title: Rauert et al., “Membrane Tumor Necrosis Factor (TNF) Induces p100 Processing via TNF Receptor-2 (TNFR2).”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_B21B_PMC2844188_TNFR2_p100_full.html`.
- Exact source locus: Introduction; Experimental Procedures; Results; Discussion.
- Observation: Oligomerized/membrane TNF activated TNFR2-associated p100 processing and nuclear translocation of p52/RelB in multiple cell lines, whereas non-oligomerized soluble TNF was weak or inactive for this alternative NF-κB output.
- Author claim: The authors conclude that TNFR2, unlike TNFR1 in the tested setting, can trigger p100 processing and that ligand form controls this branch.
- Species/model/cells: Mammalian transfected/reconstituted cell lines, including receptor-mutant systems.
- Assay/perturbation: Membrane versus soluble/oligomerized TNF; TNFR2/TNFR1 receptor-selective mutants; immunoblotting for p100/p52, nuclear translocation, and receptor-signaling assays.
- Limitations: Cell-line/receptor-expression system; ligand multimerization is decisive; no SCI receiver-cell or terminal-transcription-factor occupancy evidence.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 20. `P2MAN-M21B-M21B-EVID-000022-PMID_22933014`

- Evidence ID: `M21B-EVID-000022`; identifier: `PMID:22933014; PMCID:PMC3508279`.
- Paper/title: Patel et al., “Astrocyte TNFR2 is required for CXCL12-mediated regulation of oligodendrocyte progenitor proliferation and differentiation within the adult CNS.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_B21B_PMC3508279_TNFR2_CXCL12_full.html`.
- Exact source locus: Introduction; Materials and Methods; Results, “TNFR2 mediates expression of CXCL12 within activated astrocytes during CPZ-induced demyelination,” “TNFR2-deficient mice exhibit reduced numbers of CXCR4+ OPCs,” and CXCL12-rescue results; Figs. 1–6; Discussion and Fig. 7 model.
- Observation: Cuprizone exposure increased TNFR2 in activated corpus-callosum astrocytes; TNFR2-null mice had lower astrocyte CXCL12, fewer CXCR4+ OPCs, and impaired remyelination-related OPC responses; CXCL12 lentiviral delivery rescued OPC proliferation/myelin measures (Figs. 1–6).
- Author claim: The authors conclude that astrocyte TNFR2 promotes OPC proliferation/differentiation through induction of CXCL12 and downstream CXCR4 signaling.
- Species/model/cells: C57BL/6 and TNFR2-null mice; activated corpus-callosum astrocytes and OPCs in cuprizone demyelination.
- Assay/perturbation: Cuprizone; TNFR2 deficiency; CXCR4 antagonist AMD3100; CXCL12 lentiviral rescue; qPCR, confocal IHC, BrdU, myelin analysis, and OPC assays.
- Limitations: Adult CNS demyelination rather than traumatic SCI; supports a functional relay, not direct TNFR2–CXCL12 binding or a fully resolved TRAF2/NF-κB biochemical sequence.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

### 21. `P2MAN-M21B-M21B-EVID-000023-PMID_11517251`

- Evidence ID: `M21B-EVID-000023`; identifier: `PMID:11517251; PMCID:PMC6763083`.
- Paper/title: Kim et al., “Tumor Necrosis Factor Receptor Deletion Reduces Nuclear Factor-κB Activation, Cellular Inhibitor of Apoptosis Protein 2 Expression, and Functional Recovery after Traumatic Spinal Cord Injury.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_B21B_PMC6763083_TNFR2_SCI_full.html`.
- Exact source locus: Materials and Methods; Results, “Functional assessment in TNFR-deficient mice,” “NF-κB binding activity,” “c-IAP2 and caspase-3 expression,” “TUNEL-positive cells,” and “Myelin and axonal damage”; Figs. 1–8; Discussion.
- Observation: TNFR2-null mice had poorer BBB recovery after SCI, and TNFR2/TNFR1 deficiency was associated with blunted NF-κB activity and altered c-IAP2/caspase-3/TUNEL measures (Figs. 1–5).
- Author claim: The authors propose a TNFR–NF-κB–c-IAP2 anti-apoptotic mechanism after SCI and state that TNFR1, and probably to a lesser extent TNFR2, contributes to limiting injury and cell death.
- Species/model/cells: Mouse traumatic SCI with TNFR1-null, TNFR2-null, and wild-type controls; spinal-cord tissue, neurons, and oligodendrocytes.
- Assay/perturbation: TNFR1/TNFR2 genetic deletion; BBB scoring, EMSA, Western blot, immunohistochemistry, TUNEL, ex-vivo MRI, MBP, and neurofilament staining.
- Limitations: The study does not isolate a TNFR2-specific molecular branch from TNFR1, does not identify one receiver cell, and does not establish a terminal TF mechanism; functional recovery is a whole-cord outcome.
- Ledger: evidence grade `B`; context `L2`.
- Gates/disposition: observation `PASS` for TNFR2-loss-associated SCI outcomes; claim `FAIL` for a TNFR2-specific NF-κB/c-IAP2 causal unit; `needs_manual_source_review`.

### 22. `P2MAN-M21B-M21B-EVID-000023-PMID_30941924`

- Evidence ID: `M21B-EVID-000023`; identifier: `PMID:30941924; PMCID:PMC6630008; DOI:10.1111/cns.13125`.
- Paper/title: Gerald et al., “Continuous infusion of an agonist of the tumor necrosis factor receptor 2 in the spinal cord improves recovery after traumatic contusive injury.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_B21B_batch055_PMC6630008_TNFR2_PI3Kgamma_SCI_bioc.json`.
- Exact source locus: Introduction; Materials and Methods, “Cell death assay,” “Mice and spinal cord injury,” and “Drug administration”; Results and figure captions for Figs. 1–5; Discussion.
- Observation: TNFR2-specific agonist EHD2-sc-mTNFR2 protected rat cortical neurons from glutamate toxicity, and PI3Kγ inhibition reduced that protection (Fig. 1); continuous intraspinal delivery after mouse T9 contusion improved BMS locomotion and cortical sensory-evoked responses and altered neural/tissue measures (Figs. 2–5).
- Author claim: The authors conclude that TNFR2 activation improves locomotor and cortical responses after contusive SCI and protects neurons through PI3Kγ in vitro.
- Species/model/cells: E18 rat cortical neurons; adult female C57BL/6 mouse T9 contusion model.
- Assay/perturbation: EHD2-sc-mTNFR2; glutamate; PI3Kα inhibitor A66, PI3Kγ inhibitor AS605240, p38 inhibitor SB203580; osmotic-pump delivery, LIVE/DEAD assay, BMS, qPCR, Western blot, histology, and sensory-evoked potentials.
- Limitations: The PI3Kγ mechanism is shown in cultured neurons, not an astrocyte-specific SCI perturbation; in-vivo agonist effects are whole-cord and do not establish a single receiver cell or terminal TF.
- Ledger: evidence grade `B`; context `L2`.
- Gates/disposition: observation `PASS`; claim `PASS` for the registered TNFR2 agonism/SCI-recovery unit; `source_supported_atomic_candidate` (not imported).

### 23. `M21B-P2-000026`

- Evidence ID: `M21B-EVID-000026`; identifier: `PMCID:PMC9527244; DOI:10.1038/s41467-022-33463-x` (no PMID was present in the retained artifact).
- Paper/title: “The alarmin interleukin-1α triggers secondary degeneration through reactive astrocytes and endothelium after spinal cord injury.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_B21B_batch050_PMC9527244_IL1R1_astrocyte_bioc.json`.
- Exact source locus: Introduction; Results and figure passages for Figs. 1–10; Discussion; Methods.
- Observation: After SCI or central rmIL-1α administration, astrocyte- and endothelial-IL-1R1 conditional restoration produced IL-1α-associated neutrophil infiltration and mature-oligodendrocyte loss; astrocyte-specific Il1r1 deletion reduced these effects; IL-1α-stimulated astrocytes produced ROS and conditioned medium toxic to oligodendrocytes (Figs. 4–10).
- Author claim: The authors conclude that damaged microglia release IL-1α, which acts through astrocytic and endothelial IL-1R1 to drive secondary degeneration, with astrocyte-derived ROS contributing to oligodendrocyte loss.
- Species/model/cells: Mouse SCI and intra-cisterna-magna rmIL-1α model; primary astrocytes, endothelial cells, microglia, oligodendrocytes, and conditional Il1r1 mouse lines.
- Assay/perturbation: rmIL-1α, anakinra, global Il1r1/Il1a deletion, astrocyte/endothelial conditional restoration or deletion, microglia depletion, NAC; confocal/IHC, LDH, ROS, qPCR, Western blot, and BMS scoring.
- Limitations: Establishes downstream IL-1α/IL-1R1 astrocyte function, not an IL-1R1–IL-1RAP binding edge, IL-1R2 decoy mechanism, or all intracellular receptor-proximal steps.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS` for the astrocyte IL-1R1/SCI-function unit; `source_supported_atomic_candidate` (not imported).

### 24. `M21B-P2-000027`

- Evidence ID: `M21B-EVID-000027`; identifier: `PMID:33921794; PMCID:PMC8073111; DOI:10.3390/ijms22084232`.
- Paper/title: Lim et al., “Systematic Assessment of Chemokine Signaling at Chemokine Receptors CCR4, CCR7 and CCR10.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_external_PMC8073111.html`.
- Exact source locus: Sections 1–4; Results 2.1–2.2; Figs. 1–4; Tables 1–2; Materials and Methods.
- Observation: In matched engineered receptor assays, CCL17/CCL22 recruited β-arrestin to CCR4 without robust G-protein signaling, while CCL19/CCL21 activated both G-protein and β-arrestin responses at CCR7, with CCL19 generally more potent (Figs. 1–3; Tables 1–2).
- Author claim: The authors conclude that CCR4 and CCR7 have distinct signaling arrays and that the tested ligands did not show the proposed ligand-biased agonism under the matched assay conditions.
- Species/model/cells: Human CCR4-, CCR7-, and CCR10-expressing CHO cell systems.
- Assay/perturbation: Cognate chemokines CCL17, CCL22, CCL19, CCL21, CCL27, and CCL28 forms; BRET β-arrestin recruitment, G-protein activation, cAMP inhibition, and NFAT assays.
- Limitations: Engineered receptor-expression systems; no SCI receiver-cell branch weights, endogenous receptor abundance, or injury-state ligand context.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS` for the measured CCR4/CCR7 branch-bias unit; `source_supported_atomic_candidate` (not imported).

### 25. `M21B-P2-000029`

- Evidence ID: `M21B-EVID-000029`; identifier: `PMCID:PMC2621323; PMID:18922473; DOI:10.1016/j.molcel.2008.09.002`.
- Paper/title: Yamashita et al., “TRAF6 mediates Smad-independent activation of JNK and p38 by TGF-β.”
- Artifact: `/Users/derea/Documents/SCI/mSCIdblit/data/raw/evidence/module20_24_supervised_cli_phase2/retry_B21B_batch050_PMC2621323_TGFBR1_TAK1_bioc.json`.
- Exact source locus: Introduction; Results and Discussion, “TRAF6 is essential to the TGF-β-induced activation of JNK and p38,” “TRAF6 is physically associated with activated TGF-β receptors,” “TGF-β promotes K63 ubiquitination of TRAF6 and interaction with TAK1,” and “TRAF6 functions specifically in the Smad-independent branch”; Experimental Procedures; Figs. 1–4.
- Observation: TGF-β receptor activation required TRAF6 for JNK/p38 activation; TRAF6 associated with activated TβRI/TβRII complexes, underwent transient K63-linked ubiquitination, and interacted with TAK1; TRAF6 loss reduced JNK/p38 and apoptosis/EMT outputs while leaving Smad activation intact (Figs. 1–4).
- Author claim: The authors conclude that receptor-associated TRAF6 connects activated TGF-β receptors to a Smad-independent TAK1/JNK/p38 branch.
- Species/model/cells: RIBL17 mink lung epithelial cells, AML12 mouse hepatocytes, TRAF6-deficient mouse MEFs, HEK293/HEK293T, Hep3B, and NMuMG cells.
- Assay/perturbation: TGF-β; TRAF6 dominant-negative/RING mutants, siRNA, knockout/rescue, receptor kinase mutants; immunoblot, co-immunoprecipitation, crosslinking, in-vitro JNK kinase, ubiquitination, reporter, apoptosis, and EMT assays.
- Limitations: Reconstituted and cell-line systems; association/crosslinking does not establish every direct physical step or receptor compartment; no adult SCI context.
- Ledger: evidence grade `B`; context `L1`.
- Gates/disposition: observation `PASS`; claim `PASS`; `source_supported_atomic_candidate` (not imported).

## Final disposition

Rows passing both source gates are source-supported candidates only; they are not
promoted into the canonical evidence layer by this review. Rows 6, 12, 15,
17, and 21 require `needs_manual_source_review` because the exact registered
pair, causal mechanism, or receptor-specific direction is not established by
the retained source unit. All ledger grades/context levels remain unchanged.
