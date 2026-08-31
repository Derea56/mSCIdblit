# Module 22B even-evidence TF/program overlay report

Read-only first-pass review completed from the local repository. No repository or database files were modified.

## Scope and inputs

- Integrated TSV: `/Users/derea/Documents/SCI/mSCIdblit/work/cross_module_synthesis/canonical_evidence_review/module20_24_integrated_phase2_extractions.tsv`; Module 22B rows: 965; even-suffix rows: 459; unique even evidence IDs: 408.
- Priority existing-status candidates (`DIRECT_TF`, `TF_PROGRAM`, `DOWNSTREAM_PROGRAM`, plus `validated_functional_program`): 47 unique evidence IDs / 71 integrated rows.
- Additional full-text-backed validated candidates screened in detail: 3 evidence IDs (`000028`, `000030`, `000198`).
- Grade ledger matches: 2953 of 408 unique even evidence IDs; ledger rows: 2953. Artifact crosswalk candidate rows for even IDs: 0.
- Gate: an emitted row requires an atomic source observation plus a separately stated TF/defined-program author claim, exact source locus/figure, model/species, assay or defined perturbation, and limitations. Receptor/pathway-only, promoter/enhancer-only without a TF claim, expression/function-only, co-occurrence, abstract-only/no-figure, and rows with unresolved model/assay fields were not emitted.

## Results

- Emitted promotion-ready rows: **38**.
- Emitted evidence IDs: **27**.
- Priority/full-text evidence IDs with at least one emitted row: **27**.
- Priority/full-text evidence IDs screened but with no emitted row: **23**.
- All 408 even evidence IDs are listed below; generic rows are marked as screened out without additional source expansion per the requested timebox.

| Disposition | Evidence IDs | Count |
|---|---|---:|
| PASS_STRICT_TF_PROGRAM | 000010, 000028, 000052, 000080, 000088, 000164, 000198, 000254, 000272, 000336, 000350, 000352, 000378, 000616, 000620, 000622, 000942, 001120 | 18 |
| MIXED_PASS_AND_EXCLUDED_ROWS | 000006, 000020, 000030, 000048, 000054, 000150, 000330, 000332, 000340 | 9 |
| DEFER_OR_FAIL_PRIORITY_CANDIDATE | 000016, 000046, 000050, 000072, 000096, 000162, 000182, 000292, 000298, 001134, 001146, 001160, 001172, 001190, 001198, 001212, 001230, 001256, 001264, 001282, 001308, 001326, 001340 | 23 |
| SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE | 000002, 000008, 000018, 000022, 000032, 000036, 000056, 000058, 000060, 000062, 000066, 000074, 000086, 000092, 000098, 000106, 000134, 000156, 000166, 000168, 000170, 000172, 000180, 000192, 000202, 000210, 000220, 000226, 000258, 000266, 000270, 000274, 000302, 000304, 000312, 000314, 000334, 000344, 000346, 000354, 000356, 000358, 000368, 000370, 000374, 000380, 000386, 000392, 000404, 000618, 000774, 000828, 000830, 000832, 000870, 000872, 000954, 000956, 000962, 000986, 000992, 001012, 001036, 001038, 001046, 001048, 001068, 001072, 001074, 001088, 001094, 001098, 001192, 001216, 001222, 001226, 001228, 001242, 001248, 001252, 001254, 001268, 001274, 001278, 001280, 001294, 001300, 001304, 001306, 001344, 001354, 001356, 001376, 002674, 002692, 002882, 002886, 002950, 003016, 003028, 003084, 003354, 003362, 003364, 003368, 003646, 003654, 003664, 003668, 003672, 003674, 004800, 004802, 004804, 004806, 004812, 004814, 004818, 004824, 004834, 004846, 004852, 004856, 004886, 004888, 004898, 004900, 004904, 004906, 004908, 004914, 004916, 004926, 004930, 004942, 004966, 004970, 004982, 004988, 004992, 004996, 004998, 005000, 005002, 005004, 005018, 005028, 005032, 005034, 005036, 005042, 005050, 005052, 005054, 005056, 005062, 005070, 005078, 005080, 005082, 005086, 005088, 005090, 005094, 005096, 005110, 005112, 005114, 005126, 005130, 005132, 005184, 005194, 005200, 005202, 005204, 005206, 005208, 005212, 005218, 005220, 005232, 005254, 005258, 005262, 005264, 005270, 005276, 005278, 005280, 005292, 005298, 005314, 005316, 005320, 005322, 005324, 005328, 005330, 005334, 005342, 005346, 005348, 005352, 005362, 005368, 005378, 005380, 005382, 005384, 005386, 005388, 005392, 005394, 005406, 005410, 005424, 005426, 005430, 005434, 005436, 005444, 005448, 005452, 005456, 005458, 005460, 005462, 005466, 005470, 005472, 005474, 005476, 005478, 005490, 005492, 005494, 005498, 005500, 005502, 005504, 005514, 005516, 005522, 005526, 005528, 005542, 005544, 005546, 005548, 005550, 005552, 005554, 005556, 005558, 005564, 005572, 005574, 005580, 005630, 005758, 005764, 005794, 005796, 005804, 005806, 005808, 005814, 005836, 005906 | 270 |
| SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF | 000004, 000026, 000038, 000042, 000044, 000070, 000078, 000084, 000090, 000130, 000138, 000142, 000148, 000158, 000160, 000174, 000186, 000190, 000196, 000200, 000204, 000208, 000214, 000216, 000218, 000224, 000230, 000232, 000236, 000238, 000242, 000246, 000248, 000252, 000256, 000264, 000276, 000278, 000282, 000284, 000288, 000290, 000294, 000296, 000300, 000348, 000390, 000394, 000396, 000402, 000410, 000414, 000416, 000418, 000420, 000422, 000826, 000948, 000958, 000996, 000998, 001006, 001018, 001022, 001024, 001032, 001042, 001050, 001062, 001076, 001100, 001102, 001124, 001126, 001150, 001152, 001176, 001178, 001202, 001204, 001330, 001332, 001350, 001358, 001380, 001382, 001470, 001472 | 88 |

## Emitted row candidates

| Evidence ID | Extraction ID(s) | TF/program basis | Local artifact check |
|---|---|---|---|
| M22B-EVID-000006 | M22B-P2-R-000006-R096; M22B-P2-R-RECOVERY-STAT5-CISH-000001 | PASS: direct STAT5-to-Cish/Cis promoter occupancy and perturbation; abstract-only base row excluded, figure-backed rows retained. | M22B-P2-R-000006-R096: verified local artifact; M22B-P2-R-RECOVERY-STAT5-CISH-000001: verified local artifact |
| M22B-EVID-000010 | M22B-P2-R-000010; M22B-P2-R-000010-R096; M22B-P2-R-RECOVERY-STAT6-ARG1-000001 | PASS: direct STAT6/PGC-1beta-to-Arg1 enhancer/promoter record with reporter mutation, ChIP, and perturbation. | M22B-P2-R-000010: verified local artifact; M22B-P2-R-000010-R096: verified local artifact; M22B-P2-R-RECOVERY-STAT6-ARG1-000001: verified local artifact |
| M22B-EVID-000020 | M22B-P2-R-000053; M22B-P2-R-RECOVERY-SMAD3-SMAD4-JUN-000001 | PASS: Smad3/Smad4 plus AP-1 direct c-Jun promoter record with EMSA/supershift, site mutation, reporter, and Smad3 loss; abstract-only duplicate excluded. | M22B-P2-R-000053: verified local artifact; M22B-P2-R-RECOVERY-SMAD3-SMAD4-JUN-000001: verified local artifact |
| M22B-EVID-000028 | M22B-P2-R-000028 | PASS: full-text STAT5 recruitment and perturbation at the endogenous Cis promoter. | M22B-P2-R-000028: verified local artifact |
| M22B-EVID-000030 | M22B-P2-R-000028C | MIXED: PASS only for the STAT1/STAT4 ChIP/re-ChIP promoter row; receptor/function-only rows excluded. | M22B-P2-R-000028C: verified local artifact |
| M22B-EVID-000048 | M22B-P2-R-000048-R099 | PASS: Smad2 ChIP-seq/ChIP-qPCR and Nodal-responsive target program in zebrafish embryos. | M22B-P2-R-000048-R099: verified local artifact |
| M22B-EVID-000052 | M22B-P2-R-000089 | PASS: IFN-induced ISGF3/ISRE multi-locus program with ChIP-seq, RNA-seq, DNA binding, and factor perturbation. | M22B-P2-R-000089: verified local artifact |
| M22B-EVID-000054 | M22B-P2-R-000054-R100 | PASS: STAT6-to-Arg1 direct regulatory record in mouse macrophages. | M22B-P2-R-000054-R100: verified local artifact |
| M22B-EVID-000080 | M22B-P2-R-000028F; M22B-P2-R-000028G; M22B-P2-R-000112 | PASS: TSLP/JAK2/STAT5 TH2 transcriptional program with defined cytokine-locus outputs and factor perturbation. | M22B-P2-R-000028F: verified local artifact; M22B-P2-R-000028G: verified local artifact; M22B-P2-R-000112: verified local artifact |
| M22B-EVID-000088 | M22B-P2-R-000088-R092 | PASS: GDF10-pSMAD1/5/8-to-Smad7 promoter record with ChIP, reporter, and perturbation. | M22B-P2-R-000088-R092: verified local artifact |
| M22B-EVID-000150 | M22B-P2-R-000028I; M22B-P2-R-000152 | MIXED: PASS for the defined CREB-family/c-fos program with exact figures and MEK perturbation; proliferation-only row excluded. | M22B-P2-R-000028I: verified local artifact; M22B-P2-R-000152: verified local artifact |
| M22B-EVID-000164 | M22B-P2-R-000162 | PASS: beta-catenin/LEF regulatory occupancy at the ID3 TCF element with receptor/pathway perturbation. | M22B-P2-R-000162: verified local artifact |
| M22B-EVID-000198 | M22B-P2-B090-003 | PASS: full-text PEA3 recruitment to the DDR1 promoter with collagen/DDR2 pathway perturbation and exact human cell models. | M22B-P2-B090-003: verified local artifact |
| M22B-EVID-000254 | M22B-P2-R-000227 | PASS: Nkx2.2/Nkx6.1/Olig2 ChIP-seq/qPCR and DNA-binding-mutant-supported neural-fate/Shh target module. | M22B-P2-R-000227: verified local artifact |
| M22B-EVID-000272 | M22B-P2-R-000029D; M22B-P2-R-000240 | PASS: RelA/NF-kappaB binding and regulation of the Notch1 -300/-270 promoter region. | M22B-P2-R-000029D: verified local artifact; M22B-P2-R-000240: verified local artifact |
| M22B-EVID-000330 | M22B-P2-R-000277 | PASS: pCREB occupancy at the Bdnf1 promoter with exact cortical figures and perturbation boundary. | M22B-P2-R-000277: verified local artifact |
| M22B-EVID-000332 | M22B-P2-R-000279 | PASS: pCREB occupancy at the cFos promoter with receptor/CREB perturbation. | M22B-P2-R-000279: verified local artifact |
| M22B-EVID-000336 | M22B-P2-R-000282 | PASS: CREB-to-CycD1 promoter record with ChIP and promoter assays. | M22B-P2-R-000282: verified local artifact |
| M22B-EVID-000340 | M22B-P2-R-000283 | MIXED: PASS for the bounded 5-HT2A/PLC/MAPK/CaMKII-pCREB multi-gene program with promoter ChIP; pCREB/function-only row excluded. | M22B-P2-R-000283: verified local artifact |
| M22B-EVID-000350 | M22B-P2-R-000288 | PASS: reuse of the validated pCREB-to-Bdnf1 direct promoter observation with preserved limits. | M22B-P2-R-000288: verified local artifact |
| M22B-EVID-000352 | M22B-P2-R-000290 | PASS: reuse of the validated pCREB-to-cFos direct promoter observation with preserved limits. | M22B-P2-R-000290: verified local artifact |
| M22B-EVID-000378 | M22B-P2-R-000305 | PASS: Smad3/FoxL2-to-Fst enhancer record with ChIP, reporter, and perturbation. | M22B-P2-R-000305: verified local artifact |
| M22B-EVID-000616 | M22B-P2-R-000025A; M22B-P2-R-000334 | PASS: CREB binding/mutagenesis at the prodynorphin DynCRE elements with D1 perturbation. | M22B-P2-R-000025A: verified local artifact; M22B-P2-R-000334: verified local artifact |
| M22B-EVID-000620 | M22B-P2-R-000338 | PASS: RelB occupancy at Eda/EDAR-responsive target promoters with perturbation; species/context caveats retained. | M22B-P2-R-000338: verified local artifact |
| M22B-EVID-000622 | M22B-P2-R-000017A; M22B-P2-R-000017B; M22B-P2-R-000340 | PASS: Elk-1 occupancy and EGF-dependent EGR1 promoter activation with exact locus coordinates and perturbation. | M22B-P2-R-000017A: verified local artifact; M22B-P2-R-000017B: verified local artifact; M22B-P2-R-000340: verified local artifact |
| M22B-EVID-000942 | M22B-P2-R-000347 | PASS: CREB/CRTC2 regulation of Nedd4l-short CRE2 with ChIP, reporter mutation, and dominant-negative CREB. | M22B-P2-R-000347: verified local artifact |
| M22B-EVID-001120 | M22B-P2-R-000450 | PASS: NFATc4-dependent BDNF promoter-IV reporter/site-mutation program with defined factor perturbation; endogenous occupancy limitation retained. | M22B-P2-R-000450: verified local artifact |

## Priority and full-text candidate dispositions

| Evidence ID | Integrated extraction candidate(s) | Existing claim status(es) | Grade/context | Disposition and reason |
|---|---|---|---|---|
| M22B-EVID-000006 | M22B-P2-R-000006 [exclude]; M22B-P2-R-000006-R096 [EMIT]; M22B-P2-R-RECOVERY-STAT5-CISH-000001 [EMIT] | validated_author_claim; VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS: direct STAT5-to-Cish/Cis promoter occupancy and perturbation; abstract-only base row excluded, figure-backed rows retained. |
| M22B-EVID-000010 | M22B-P2-R-000010 [EMIT]; M22B-P2-R-000010-R096 [EMIT]; M22B-P2-R-RECOVERY-STAT6-ARG1-000001 [EMIT] | validated_author_claim; VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS: direct STAT6/PGC-1beta-to-Arg1 enhancer/promoter record with reporter mutation, ChIP, and perturbation. |
| M22B-EVID-000016 | M22B-P2-R-000016 [exclude]; M22B-P2-R-000016-R097 [exclude]; M22B-P2-R-RECOVERY-SMAD-ID1-000001 [exclude] | unresolved; VALIDATED_DIRECT_TF_TARGET; abstract_only_not_import_ready | B/L1 | DEFER: direct Id1 candidate is retained only at abstract/PubMed scope; no exact figure-level local source was retained. |
| M22B-EVID-000020 | M22B-P2-R-000020 [exclude]; M22B-P2-R-000053 [EMIT]; M22B-P2-R-000072 [exclude]; M22B-P2-R-RECOVERY-SMAD3-SMAD4-JUN-000001 [EMIT] | unresolved; validated_author_claim; validated_direct_tf_target_support; validated_direct_tf_target | B/L1 | PASS: Smad3/Smad4 plus AP-1 direct c-Jun promoter record with EMSA/supershift, site mutation, reporter, and Smad3 loss; abstract-only duplicate excluded. |
| M22B-EVID-000028 | M22B-P2-R-000028 [EMIT] | validated_author_claim | B/L1 | PASS: full-text STAT5 recruitment and perturbation at the endogenous Cis promoter. |
| M22B-EVID-000030 | M22B-P2-R-000028B [exclude]; M22B-P2-R-000028C [EMIT]; M22B-P2-R-000028D [exclude]; M22B-P2-R-000030 [exclude] | validated_author_claim; unresolved | B/L1 | MIXED: PASS only for the STAT1/STAT4 ChIP/re-ChIP promoter row; receptor/function-only rows excluded. |
| M22B-EVID-000046 | M22B-P2-R-000046-R099 [exclude]; M22B-P2-R-000083 [exclude] | REUSE_DIRECT_TF_TARGET_SUPPORT; unresolved | U/L0 | FAIL: reused direct-TF candidate lacks a retained exact figure/source-locus mapping in the integrated row. |
| M22B-EVID-000048 | M22B-P2-R-000048-R099 [EMIT]; M22B-P2-R-000085 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED; unresolved | U/L0 | PASS: Smad2 ChIP-seq/ChIP-qPCR and Nodal-responsive target program in zebrafish embryos. |
| M22B-EVID-000050 | M22B-P2-R-000050-R089 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER: direct STAT1/STAT4 enhancer candidate lacks retained exact figure/local full-text support. |
| M22B-EVID-000052 | M22B-P2-R-000089 [EMIT] | validated_direct_tf_program_support | B/L1 | PASS: IFN-induced ISGF3/ISRE multi-locus program with ChIP-seq, RNA-seq, DNA binding, and factor perturbation. |
| M22B-EVID-000054 | M22B-P2-R-000054-R100 [EMIT]; M22B-P2-R-000091 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED; REUSE_FUNCTIONAL_CONTEXT | B/L1 | PASS: STAT6-to-Arg1 direct regulatory record in mouse macrophages. |
| M22B-EVID-000072 | M22B-P2-B090-002 [exclude]; M22B-P2-R-RECOVERY-STAT5-CSN2-000001 [exclude] | validated_fulltext; validated_direct_tf_target_support_abstract_bounded | B/L1 | DEFER: beta-casein/STAT5 candidate is abstract-bounded in the retained local source; no figure-level mapping was imported. |
| M22B-EVID-000080 | M22B-P2-R-000028F [EMIT]; M22B-P2-R-000028G [EMIT]; M22B-P2-R-000112 [EMIT] | validated_author_claim; validated_direct_tf_program_support | B/L1 | PASS: TSLP/JAK2/STAT5 TH2 transcriptional program with defined cytokine-locus outputs and factor perturbation. |
| M22B-EVID-000088 | M22B-P2-R-000088-R092 [EMIT] | VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS: GDF10-pSMAD1/5/8-to-Smad7 promoter record with ChIP, reporter, and perturbation. |
| M22B-EVID-000096 | M22B-P2-R-000125 [exclude] | validated_direct_tf_target_support | ?/L1 | DEFER: direct FXR/PXR candidate has PubMed-only retained support and no exact full-text artifact. |
| M22B-EVID-000150 | M22B-P2-R-000028I [EMIT]; M22B-P2-R-000028J [exclude]; M22B-P2-R-000152 [EMIT] | validated_author_claim; validated_downstream_program | B/L1 | MIXED: PASS for the defined CREB-family/c-fos program with exact figures and MEK perturbation; proliferation-only row excluded. |
| M22B-EVID-000162 | M22B-P2-R-000160 [exclude] | validated_downstream_program | B/L1 | FAIL: SOX9 expression/differentiation record explicitly lacks SOX9 DNA occupancy or a direct target-locus assay. |
| M22B-EVID-000164 | M22B-P2-R-000162 [EMIT] | validated_direct_tf_target | B/L1 | PASS: beta-catenin/LEF regulatory occupancy at the ID3 TCF element with receptor/pathway perturbation. |
| M22B-EVID-000182 | M22B-P2-R-000177 [exclude] | validated_downstream_program | B/L1 | FAIL: MyoD/Myogenin expression and regeneration phenotype; no direct TF target-gene assay. |
| M22B-EVID-000198 | M22B-P2-B090-003 [EMIT] | validated_fulltext | B/L1 | PASS: full-text PEA3 recruitment to the DDR1 promoter with collagen/DDR2 pathway perturbation and exact human cell models. |
| M22B-EVID-000254 | M22B-P2-R-000227 [EMIT] | validated_direct_tf_target | B/L1 | PASS: Nkx2.2/Nkx6.1/Olig2 ChIP-seq/qPCR and DNA-binding-mutant-supported neural-fate/Shh target module. |
| M22B-EVID-000272 | M22B-P2-R-000029D [EMIT]; M22B-P2-R-000240 [EMIT] | validated_author_claim; validated_direct_tf_target | B/L1 | PASS: RelA/NF-kappaB binding and regulation of the Notch1 -300/-270 promoter region. |
| M22B-EVID-000292 | M22B-P2-R-000255 [exclude] | validated_direct_tf_target | B/L1 | DEFER: direct TF candidate lacks an exact retained local source artifact/figure mapping. |
| M22B-EVID-000298 | M22B-P2-R-000260 [exclude] | validated_direct_tf_target_bounded | B/L1 | DEFER: direct RELA/E2F1 module is described, but retained row has no exact figure mapping/local full text. |
| M22B-EVID-000330 | M22B-P2-R-000030C [exclude]; M22B-P2-R-000277 [EMIT] | validated_author_claim; validated_direct_tf_target_bounded | B/L1 | PASS: pCREB occupancy at the Bdnf1 promoter with exact cortical figures and perturbation boundary. |
| M22B-EVID-000332 | M22B-P2-R-000030E [exclude]; M22B-P2-R-000279 [EMIT] | validated_author_claim; validated_direct_tf_target | B/L1 | PASS: pCREB occupancy at the cFos promoter with receptor/CREB perturbation. |
| M22B-EVID-000336 | M22B-P2-R-000282 [EMIT] | validated_direct_tf_target_bounded | B/L1 | PASS: CREB-to-CycD1 promoter record with ChIP and promoter assays. |
| M22B-EVID-000340 | M22B-P2-R-000030A [exclude]; M22B-P2-R-000283 [EMIT] | validated_author_claim; validated_functional_program | B/L1 | MIXED: PASS for the bounded 5-HT2A/PLC/MAPK/CaMKII-pCREB multi-gene program with promoter ChIP; pCREB/function-only row excluded. |
| M22B-EVID-000350 | M22B-P2-R-000288 [EMIT] | REUSE_DIRECT_TF_TARGET_BOUNDED | ?/L1 | PASS: reuse of the validated pCREB-to-Bdnf1 direct promoter observation with preserved limits. |
| M22B-EVID-000352 | M22B-P2-R-000290 [EMIT] | REUSE_DIRECT_TF_TARGET | ?/L1 | PASS: reuse of the validated pCREB-to-cFos direct promoter observation with preserved limits. |
| M22B-EVID-000378 | M22B-P2-R-000305 [EMIT] | VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS: Smad3/FoxL2-to-Fst enhancer record with ChIP, reporter, and perturbation. |
| M22B-EVID-000616 | M22B-P2-R-000025A [EMIT]; M22B-P2-R-000334 [EMIT] | validated_author_claim; VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS: CREB binding/mutagenesis at the prodynorphin DynCRE elements with D1 perturbation. |
| M22B-EVID-000620 | M22B-P2-R-000338 [EMIT] | VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS: RelB occupancy at Eda/EDAR-responsive target promoters with perturbation; species/context caveats retained. |
| M22B-EVID-000622 | M22B-P2-R-000017A [EMIT]; M22B-P2-R-000017B [EMIT]; M22B-P2-R-000340 [EMIT] | validated_author_claim; VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS: Elk-1 occupancy and EGF-dependent EGR1 promoter activation with exact locus coordinates and perturbation. |
| M22B-EVID-000942 | M22B-P2-R-000347 [EMIT] | VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS: CREB/CRTC2 regulation of Nedd4l-short CRE2 with ChIP, reporter mutation, and dominant-negative CREB. |
| M22B-EVID-001120 | M22B-P2-R-000450 [EMIT] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | PASS: NFATc4-dependent BDNF promoter-IV reporter/site-mutation program with defined factor perturbation; endogenous occupancy limitation retained. |
| M22B-EVID-001134 | M22B-P2-R-000456 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct NF-YB candidate has local artifact but integrated row lacks retained model and assay details. |
| M22B-EVID-001146 | M22B-P2-R-000459 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct NFATc4 candidate has local artifact but integrated row lacks retained assay/model details. |
| M22B-EVID-001160 | M22B-P2-R-000465 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct NF-YB candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001172 | M22B-P2-R-000468 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct NFATc4 candidate has local artifact but integrated row lacks retained assay/model details. |
| M22B-EVID-001190 | M22B-P2-R-000474 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct Elk-1 candidate has local artifact but integrated row lacks retained model and assay details. |
| M22B-EVID-001198 | M22B-P2-R-000479 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct NFATc4 candidate has local artifact but integrated row lacks retained assay/model details. |
| M22B-EVID-001212 | M22B-P2-R-000485 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct NF-YB candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001230 | M22B-P2-R-000493 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct Elk-1 candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001256 | M22B-P2-R-000502 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct Elk-1 candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001264 | M22B-P2-R-000503 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct NF-YB candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001282 | M22B-P2-R-000511 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct Elk-1 candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001308 | M22B-P2-R-000520 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct Elk-1 candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001326 | M22B-P2-R-000524 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct NFATc4 candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001340 | M22B-P2-R-000530 [exclude] | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | FAIL: direct NF-YB candidate has local artifact but integrated row lacks retained model details. |

## Complete even-ID disposition ledger

This table documents every unique even evidence ID found in the integrated Module 22B rows. “Screened out” entries were not expanded into generic pathway/function source review in accordance with the requested prioritization.

| Evidence ID | Integrated rows | Existing claim status(es) | Grade/context | Disposition |
|---|---:|---|---|---|
| M22B-EVID-000002 | 3 | validated_author_claim; VALIDATED_RECEPTOR_PATHWAY_BOUNDED; validated_functional_context | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000004 | 3 | abstract_only_not_import_ready; VALIDATED_RECEPTOR_PATHWAY_BOUNDED; validated_functional_context | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000006 | 3 | validated_author_claim; VALIDATED_DIRECT_TF_TARGET | B/L1 | MIXED_PASS_AND_EXCLUDED_ROWS: PASS: direct STAT5-to-Cish/Cis promoter occupancy and perturbation; abstract-only base row excluded, figure-backed rows retained. |
| M22B-EVID-000008 | 4 | validated_author_claim; VALIDATED_RECEPTOR_PATHWAY_BOUNDED; validated_functional_context | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000010 | 3 | validated_author_claim; VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: direct STAT6/PGC-1beta-to-Arg1 enhancer/promoter record with reporter mutation, ChIP, and perturbation. |
| M22B-EVID-000016 | 3 | unresolved; VALIDATED_DIRECT_TF_TARGET; abstract_only_not_import_ready | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: DEFER: direct Id1 candidate is retained only at abstract/PubMed scope; no exact figure-level local source was retained. |
| M22B-EVID-000018 | 3 | unresolved; VALIDATED_RECEPTOR_PATHWAY_BOUNDED; validated_functional_context | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000020 | 4 | unresolved; validated_author_claim; validated_direct_tf_target_support; validated_direct_tf_target | B/L1 | MIXED_PASS_AND_EXCLUDED_ROWS: PASS: Smad3/Smad4 plus AP-1 direct c-Jun promoter record with EMSA/supershift, site mutation, reporter, and Smad3 loss; abstract-only duplicate excluded. |
| M22B-EVID-000022 | 3 | unresolved; VALIDATED_RECEPTOR_PATHWAY_BOUNDED; validated_author_claim | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000026 | 3 | unresolved; UNRESOLVED_EXACT_EDGE; validated_author_claim | U/L0 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000028 | 1 | validated_author_claim | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: full-text STAT5 recruitment and perturbation at the endogenous Cis promoter. |
| M22B-EVID-000030 | 4 | validated_author_claim; unresolved | B/L1 | MIXED_PASS_AND_EXCLUDED_ROWS: MIXED: PASS only for the STAT1/STAT4 ChIP/re-ChIP promoter row; receptor/function-only rows excluded. |
| M22B-EVID-000032 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000036 | 1 | unknown_after_primary_review | U/L0 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000038 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000042 | 2 | VALIDATED_RECEPTOR_CONTEXT_BOUNDED; VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000044 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000046 | 2 | REUSE_DIRECT_TF_TARGET_SUPPORT; unresolved | U/L0 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: reused direct-TF candidate lacks a retained exact figure/source-locus mapping in the integrated row. |
| M22B-EVID-000048 | 2 | VALIDATED_DIRECT_TF_TARGET_BOUNDED; unresolved | U/L0 | MIXED_PASS_AND_EXCLUDED_ROWS: PASS: Smad2 ChIP-seq/ChIP-qPCR and Nodal-responsive target program in zebrafish embryos. |
| M22B-EVID-000050 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: DEFER: direct STAT1/STAT4 enhancer candidate lacks retained exact figure/local full-text support. |
| M22B-EVID-000052 | 1 | validated_direct_tf_program_support | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: IFN-induced ISGF3/ISRE multi-locus program with ChIP-seq, RNA-seq, DNA binding, and factor perturbation. |
| M22B-EVID-000054 | 2 | VALIDATED_DIRECT_TF_TARGET_BOUNDED; REUSE_FUNCTIONAL_CONTEXT | B/L1 | MIXED_PASS_AND_EXCLUDED_ROWS: PASS: STAT6-to-Arg1 direct regulatory record in mouse macrophages. |
| M22B-EVID-000056 | 2 | M22B-C-PH2-B085-001; REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000058 | 1 | validated_functional_context | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000060 | 1 | validated_functional_context | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000062 | 1 | validated_functional_context | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000066 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000070 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000072 | 2 | validated_fulltext; validated_direct_tf_target_support_abstract_bounded | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: DEFER: beta-casein/STAT5 candidate is abstract-bounded in the retained local source; no figure-level mapping was imported. |
| M22B-EVID-000074 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000078 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000080 | 3 | validated_author_claim; validated_direct_tf_program_support | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: TSLP/JAK2/STAT5 TH2 transcriptional program with defined cytokine-locus outputs and factor perturbation. |
| M22B-EVID-000084 | 1 | validated_functional_context | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000086 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000088 | 1 | VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: GDF10-pSMAD1/5/8-to-Smad7 promoter record with ChIP, reporter, and perturbation. |
| M22B-EVID-000090 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000092 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000096 | 1 | validated_direct_tf_target_support | ?/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: DEFER: direct FXR/PXR candidate has PubMed-only retained support and no exact full-text artifact. |
| M22B-EVID-000098 | 2 | M22B-C-PH2-B085-003; REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000106 | 1 | validated_functional_context | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000130 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000134 | 2 | validated_author_claim | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000138 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000142 | 2 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED; REUSE_FUNCTIONAL_CONTEXT | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000148 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000150 | 3 | validated_author_claim; validated_downstream_program | B/L1 | MIXED_PASS_AND_EXCLUDED_ROWS: MIXED: PASS for the defined CREB-family/c-fos program with exact figures and MEK perturbation; proliferation-only row excluded. |
| M22B-EVID-000156 | 1 | validated_functional_context | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000158 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000160 | 1 | validated_functional_context | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000162 | 1 | validated_downstream_program | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: SOX9 expression/differentiation record explicitly lacks SOX9 DNA occupancy or a direct target-locus assay. |
| M22B-EVID-000164 | 1 | validated_direct_tf_target | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: beta-catenin/LEF regulatory occupancy at the ID3 TCF element with receptor/pathway perturbation. |
| M22B-EVID-000166 | 1 | validated_receptor_proximal_relay | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000168 | 1 | validated_functional_context | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000170 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000172 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000174 | 1 | validated_functional_context | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000180 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000182 | 1 | validated_downstream_program | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: MyoD/Myogenin expression and regeneration phenotype; no direct TF target-gene assay. |
| M22B-EVID-000186 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000190 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000192 | 2 | validated_author_claim | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000196 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000198 | 1 | validated_fulltext | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: full-text PEA3 recruitment to the DDR1 promoter with collagen/DDR2 pathway perturbation and exact human cell models. |
| M22B-EVID-000200 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000202 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000204 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000208 | 1 | REUSE_AUTHOR_CLAIM_STAGING:M22B-C-PH2-000207 | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000210 | 2 | validated_author_claim | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000214 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000216 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000218 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000220 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000224 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000226 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000230 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000232 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000236 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000238 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000242 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000246 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000248 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000252 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000254 | 1 | validated_direct_tf_target | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: Nkx2.2/Nkx6.1/Olig2 ChIP-seq/qPCR and DNA-binding-mutant-supported neural-fate/Shh target module. |
| M22B-EVID-000256 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000258 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000264 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000266 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000270 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000272 | 2 | validated_author_claim; validated_direct_tf_target | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: RelA/NF-kappaB binding and regulation of the Notch1 -300/-270 promoter region. |
| M22B-EVID-000274 | 1 | validated_promoter_regulatory_context | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000276 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000278 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000282 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000284 | 1 | validated_receptor_pathway | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000288 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000290 | 1 | validated_receptor_pathway | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000292 | 1 | validated_direct_tf_target | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: DEFER: direct TF candidate lacks an exact retained local source artifact/figure mapping. |
| M22B-EVID-000294 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000296 | 1 | validated_receptor_pathway_bounded | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000298 | 1 | validated_direct_tf_target_bounded | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: DEFER: direct RELA/E2F1 module is described, but retained row has no exact figure mapping/local full text. |
| M22B-EVID-000300 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000302 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000304 | 1 | validated_receptor_pathway_bounded | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000312 | 1 | validated_receptor_pathway_bounded | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000314 | 1 | validated_receptor_pathway_bounded | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000330 | 2 | validated_author_claim; validated_direct_tf_target_bounded | B/L1 | MIXED_PASS_AND_EXCLUDED_ROWS: PASS: pCREB occupancy at the Bdnf1 promoter with exact cortical figures and perturbation boundary. |
| M22B-EVID-000332 | 2 | validated_author_claim; validated_direct_tf_target | B/L1 | MIXED_PASS_AND_EXCLUDED_ROWS: PASS: pCREB occupancy at the cFos promoter with receptor/CREB perturbation. |
| M22B-EVID-000334 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000336 | 1 | validated_direct_tf_target_bounded | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: CREB-to-CycD1 promoter record with ChIP and promoter assays. |
| M22B-EVID-000340 | 2 | validated_author_claim; validated_functional_program | B/L1 | MIXED_PASS_AND_EXCLUDED_ROWS: MIXED: PASS for the bounded 5-HT2A/PLC/MAPK/CaMKII-pCREB multi-gene program with promoter ChIP; pCREB/function-only row excluded. |
| M22B-EVID-000344 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000346 | 1 | validated_receptor_pathway_bounded | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000348 | 1 | validated_receptor_pathway_bounded | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000350 | 1 | REUSE_DIRECT_TF_TARGET_BOUNDED | ?/L1 | PASS_STRICT_TF_PROGRAM: PASS: reuse of the validated pCREB-to-Bdnf1 direct promoter observation with preserved limits. |
| M22B-EVID-000352 | 1 | REUSE_DIRECT_TF_TARGET | ?/L1 | PASS_STRICT_TF_PROGRAM: PASS: reuse of the validated pCREB-to-cFos direct promoter observation with preserved limits. |
| M22B-EVID-000354 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000356 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000358 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000368 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000370 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000374 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000378 | 1 | VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: Smad3/FoxL2-to-Fst enhancer record with ChIP, reporter, and perturbation. |
| M22B-EVID-000380 | 1 | UNRESOLVED_PRIMARY_EVIDENCE | U/L0 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000386 | 1 | VALIDATED_PATHWAY_PROMOTER_FUNCTION | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000390 | 1 | VALIDATED_PATHWAY_PROMOTER_FUNCTION | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000392 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000394 | 1 | VALIDATED_ENHANCER_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000396 | 1 | REUSE_FUNCTIONAL_CONTEXT | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000402 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000404 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000410 | 1 | UNRESOLVED_PRIMARY_EVIDENCE | U/L0 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000414 | 1 | unresolved | U/L0 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000416 | 1 | UNRESOLVED_PRIMARY_EVIDENCE | U/L0 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000418 | 1 | UNRESOLVED_PRIMARY_EVIDENCE | U/L0 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000420 | 1 | unresolved | U/L0 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000422 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000616 | 2 | validated_author_claim; VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: CREB binding/mutagenesis at the prodynorphin DynCRE elements with D1 perturbation. |
| M22B-EVID-000618 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000620 | 1 | VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: RelB occupancy at Eda/EDAR-responsive target promoters with perturbation; species/context caveats retained. |
| M22B-EVID-000622 | 3 | validated_author_claim; VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: Elk-1 occupancy and EGF-dependent EGR1 promoter activation with exact locus coordinates and perturbation. |
| M22B-EVID-000774 | 1 | validated_author_claim | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000826 | 1 | validated_author_claim | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000828 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000830 | 2 | validated_author_claim; VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000832 | 2 | validated_author_claim; VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000870 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000872 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000942 | 1 | VALIDATED_DIRECT_TF_TARGET | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: CREB/CRTC2 regulation of Nedd4l-short CRE2 with ChIP, reporter mutation, and dominant-negative CREB. |
| M22B-EVID-000948 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000954 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000956 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000958 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000962 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000986 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000992 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000996 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-000998 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001006 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001012 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001018 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001022 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001024 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001032 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001036 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001038 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001042 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001046 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001048 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001050 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001062 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001068 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001072 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001074 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001076 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001088 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001094 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001098 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001100 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001102 | 1 | unresolved | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001120 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | PASS_STRICT_TF_PROGRAM: PASS: NFATc4-dependent BDNF promoter-IV reporter/site-mutation program with defined factor perturbation; endogenous occupancy limitation retained. |
| M22B-EVID-001124 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001126 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001134 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct NF-YB candidate has local artifact but integrated row lacks retained model and assay details. |
| M22B-EVID-001146 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct NFATc4 candidate has local artifact but integrated row lacks retained assay/model details. |
| M22B-EVID-001150 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001152 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001160 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct NF-YB candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001172 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct NFATc4 candidate has local artifact but integrated row lacks retained assay/model details. |
| M22B-EVID-001176 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001178 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001190 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct Elk-1 candidate has local artifact but integrated row lacks retained model and assay details. |
| M22B-EVID-001192 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001198 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct NFATc4 candidate has local artifact but integrated row lacks retained assay/model details. |
| M22B-EVID-001202 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001204 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001212 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct NF-YB candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001216 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001222 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001226 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001228 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001230 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct Elk-1 candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001242 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001248 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001252 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001254 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001256 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct Elk-1 candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001264 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct NF-YB candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001268 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001274 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001278 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001280 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001282 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct Elk-1 candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001294 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001300 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001304 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001306 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001308 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct Elk-1 candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001326 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct NFATc4 candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001330 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001332 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001340 | 1 | VALIDATED_DIRECT_TF_TARGET_BOUNDED | B/L1 | DEFER_OR_FAIL_PRIORITY_CANDIDATE: FAIL: direct NF-YB candidate has local artifact but integrated row lacks retained model details. |
| M22B-EVID-001344 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001350 | 1 | UNKNOWN_NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001354 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001356 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001358 | 1 | UNKNOWN_NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001376 | 1 | UNKNOWN_NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001380 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001382 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001470 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-001472 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NOT_IN_PRIORITY_PASS_GENERIC_OR_NON_TF: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-002674 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-002692 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-002882 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-002886 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-002950 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-003016 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-003028 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-003084 | 1 | eCIRP; TREM1 siRNA/LP17; Trem1 knockout | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-003354 | 1 | Decorin; MET; HGF competition | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-003362 | 1 | Dkk2; Kremen2; LRP6; Wnt/Frizzled pathway | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-003364 | 1 | Dkk1; Kremen1/2; LRP5/6 | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-003368 | 1 | No perturbation accepted | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-003646 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-003654 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-003664 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-003668 | 1 | UNKNOWN_EXACT_TERMINAL_TF | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-003672 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-003674 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004800 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004802 | 2 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004804 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004806 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004812 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004814 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004818 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004824 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004834 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004846 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004852 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004856 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004886 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004888 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004898 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004900 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004904 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004906 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004908 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004914 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004916 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004926 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004930 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004942 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004966 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004970 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004982 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004988 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004992 | 1 | UNKNOWN_EXACT_TERMINAL_TF | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004996 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-004998 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005000 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005002 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005004 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005018 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005028 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005032 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005034 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005036 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005042 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005050 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005052 | 2 | NO_TERMINAL_TF_EVIDENCE; VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005054 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005056 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005062 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005070 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005078 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005080 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005082 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005086 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005088 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005090 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005094 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005096 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005110 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005112 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005114 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005126 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005130 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005132 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005184 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005194 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005200 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005202 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005204 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005206 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005208 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005212 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005218 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005220 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005232 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005254 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005258 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005262 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005264 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005270 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005276 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005278 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005280 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005292 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005298 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005314 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005316 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005320 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005322 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005324 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005328 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005330 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005334 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005342 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005346 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005348 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005352 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005362 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005368 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005378 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005380 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005382 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005384 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005386 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005388 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005392 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005394 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005406 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005410 | 1 | unresolved | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005424 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005426 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005430 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005434 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005436 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005444 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005448 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005452 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005456 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005458 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005460 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005462 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005466 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005470 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005472 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005474 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005476 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005478 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005490 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005492 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005494 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005498 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005500 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005502 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005504 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005514 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005516 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005522 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005526 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005528 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005542 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005544 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005546 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005548 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005550 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005552 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005554 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005556 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005558 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005564 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005572 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005574 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005580 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005630 | 1 | VALIDATED_PATHWAY_FUNCTION_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005758 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005764 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005794 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005796 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005804 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005806 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005808 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005814 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005836 | 1 | VALIDATED_RECEPTOR_PATHWAY_BOUNDED | B/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |
| M22B-EVID-005906 | 1 | NO_TERMINAL_TF_EVIDENCE | ?/L1 | SCREENED_OUT_NO_DIRECT_TF_OR_DEFINED_PROGRAM_GATE: Generic/non-TF or pathway/function record screened out; no overlay row emitted. |

## Validation checks

- Output header field count: 25 (exactly the integrated TSV 25-field header).
- Output data-row count: 38; every output row has 25 fields and is copied unchanged from the integrated TSV.
- Exact existing identifiers preserved for every output row: `extraction_id`, `module`, `b_edge_id`, `b_evidence_id`, `evidence_layer`, and `canonical_paper_key`; ABC/L0-L4 values and context fields were not edited.
- All output evidence IDs are Module 22B and have even numeric suffixes.
- Local source artifact existence checks passed for every emitted row; no web search was used.
- Repository/database state: read-only; no commit or repository artifact was created.
