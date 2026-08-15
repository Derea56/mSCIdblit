# Module 21A batch 166 review

Scope: the exact 25 frozen Module 20A queue rows assigned to filtered queue ordinals 3601–3625. Queue IDs and order are preserved. This review writes only `module21a_batch166_review.tsv` and this summary; Module 20A files and shared registers were not modified, and no commit was made.

## Disposition

- 25/25 exact rows reviewed.
- 3 `reviewed_relay_candidate`: `M20A-EXT-3359` (Trf Lrp2), `M20A-EXT-3369` (Try4 F2rl1), and `M20A-EXT-3386` (Tshb Tshr).
- 22 `reviewed_unresolved`: no qualifying exact pair evidence sufficient for a direct edge or relay promotion.
- No downstream pathway/function-only row was promoted, and no terminal TF was assigned. Every TSV row therefore uses literal `terminal_TF=null`.

## Layered evidence decisions

| Exact pair | Binding/activation layer | Receptor-proximal relay | Downstream pathway/function | Decision |
|---|---|---|---|---|
| Trf Lrp2 | Transferrin binds Cubn in affinity/SPR assays; Lrp2/megalin is required for internalization of the Cubn-ligand complex. Direct Trf-Lrp2 binding was not isolated. | Apical Cubn-Lrp2/MCRC endocytic uptake is supported in proximal-tubule and yolk-sac systems. | Lysosomal iron uptake is contextual endocytic function, not evidence of a kinase or TF relay. | Medium relay candidate with coreceptor limitation. |
| Try4 F2rl1 | Recombinant mouse Try4 cleaves PAR2-derived substrate and activates mouse F2rl1/PAR2-dependent calcium signaling. | Receptor-dependent calcium signaling is supported in heterologous mPAR2 cells. | Inflammation/pain results are kept as contextual function; the in-vivo experiments did not identify Try4 as the endogenous protease. | Medium relay candidate. |
| Tshb Tshr | Primary studies support assembled TSH binding to TSHR and show that beta-subunit-directed antibodies block TSH receptor binding. | TSHR couples to Gs/adenylyl cyclase/cAMP; Gq/11-PKC/ERK is retained as a context-dependent branch. | Thyroid development/iodide-metabolism effects are not used to infer a direct TSHB-only edge or a terminal TF. | Medium relay candidate with heterodimer limitation. |

For the 22 unresolved rows, canonical trypsin-PAR, thrombin-PAR3, TSH/TSHR, and receptor-family comparator studies were retained only as explicit boundaries. They were not reassigned to an untested Try5/Try10 isoform, PAR paralog, PARD3 scaffold, or non-TSHR receptor. Pathway membership, shared GPCR coupling, co-expression, and downstream function were never used as evidence of direct interaction.

## Primary source anchors

- Transferrin/cubilin/megalin: PMID 11606717 / PMCID PMC60081 / DOI 10.1073/pnas.211291398; PMID 30833328 / PMCID PMC6497946 / DOI 10.1074/jbc.RA118.006390.
- Mouse Try4/PAR2: PMID 24749982 / PMCID PMC4128045 / DOI 10.1111/bph.12738.
- Trypsin/PAR comparator boundaries: PMID 16231009 / PMCID PMC1751236 / DOI 10.1038/sj.bjp.0706410; PMID 9618465 / PMCID PMC22580 / DOI 10.1073/pnas.95.12.6642; PMID 9087410 / DOI 10.1038/386502a0.
- Mouse trypsinogen regulation: PMID 23814066 / DOI 10.1074/jbc.M113.478800.
- TSH beta-subunit/TSHR and receptor signaling: PMID 1694490 / DOI 10.1210/endo-127-1-149; PMID 18216391 / PMCID PMC2653065 / DOI 10.1177/1087057107313786; PMID 18719020 / PMCID PMC2630889 / DOI 10.1210/en.2008-0878; PMID 12432093.

## Limitations and unresolved boundaries

- The Trf-Lrp2 result is a Cubn-presented, megalin-dependent uptake mechanism. It does not establish isolated direct binding of transferrin to Lrp2 or a conventional intracellular kinase cascade.
- The Try4 result is exact for mouse Try4 and F2rl1/PAR2, but the recombinant/heterologous assay does not establish native SCI-cell weighting. The broader inflammatory phenotype does not identify Try4 as the causal endogenous protease.
- The Tshb-Tshr result concerns assembled glycoprotein hormone TSH, not free TSHB. Beta-subunit contribution to binding is supported, but standalone TSHB agonism was not tested.
- Try5 and Try10 primary evidence located in this bounded review addressed zymogen/protease biology or other trypsin isoforms, not the submitted isoform-receptor pairs. Human or family-level PAR evidence was therefore not promoted.
- `Pard3` is treated as the PARD3 polarity scaffold, not as a PAR receptor. PAR signaling studies cannot establish a Try-Pard3 ligand-receptor edge.
- No row has a terminal TF assignment because the reviewed exact-pair evidence did not separately validate a terminal transcription-factor activation event.
