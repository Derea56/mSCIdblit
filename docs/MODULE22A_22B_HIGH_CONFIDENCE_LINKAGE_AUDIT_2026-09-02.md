# Module 22A-to-22B High-Confidence Linkage Audit

This audit identifies exact Module 22A handoffs that can reuse existing
high-confidence Module 22B TF-target evidence. It is deliberately bounded:
it does not edit the Module 22A handoff register, promote a new canonical
edge, or infer SCI receiver-cell activity from comparator models.

## Gate

A link requires an exact handoff ID with the expected terminal TF, or an
explicit bounded terminal-TF assignment when the handoff has no TF, an
exportable 22B edge already marked `high`, and exportable evidence marked
`high` or covered by a reviewed primary extraction marked `High`.

- Total 22A handoffs: 5,906
- Pending TF-program candidates: 274
- No-terminal-TF handoffs: 5,632
- Promotion-ready bounded links: 32
- Links adding an evidence-backed terminal-TF assignment: 2
- Candidate handoffs without an exact reusable high-confidence link: 247

## Promotion-ready bounded links

| Link | 22A handoff | Pair | TF | 22B edge | Target | Evidence |
|---|---|---|---|---|---|---|
| M22A22B-LINK-001 | M22A-HANDOFF-001300 | il3 il3ra_csf2rb | STAT5 | M22B-E000448 | Ccnd1 | M22B-EVID-000007 |
| M22A22B-LINK-002 | M22A-HANDOFF-001300 | il3 il3ra_csf2rb | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-003 | M22A-HANDOFF-001300 | il3 il3ra_csf2rb | STAT5A;STAT5B | M22B-E000456 | Cish | M22B-EVID-000028 |
| M22A22B-LINK-004 | M22A-HANDOFF-001307 | il4 il4r_il13ra1 | STAT6 | M22B-E000459 | Arg1 | M22B-EVID-000010 |
| M22A22B-LINK-005 | M22A-HANDOFF-001307 | il4 il4r_il13ra1 | STAT6 | M22B-E000460 | Chil3 (Ym1) | M22B-EVID-000009 |
| M22A22B-LINK-006 | M22A-HANDOFF-001312 | il6 il6r_il6st | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-007 | M22A-HANDOFF-001802 | bdnf ntrk2 | CREB | M22B-E000036 | Bdnf promoter IV | M22B-EVID-000137 |
| M22A22B-LINK-008 | M22A-HANDOFF-000449 | eda edar | RELB | M22B-E000336 | Ltb;Tnfrsf9 | M22B-EVID-000620 |
| M22A22B-LINK-009 | M22A-HANDOFF-000450 | egf egfr | ELK1 | M22B-E000158 | EGR1 promoter | M22B-EVID-000622 |
| M22A22B-LINK-010 | M22A-HANDOFF-005464 | il10 il10ra_il10rb | STAT3 | M22B-E000432 | Zfp36 | M22B-EVID-000083 |
| M22A22B-LINK-011 | M22A-HANDOFF-000440 | e2-cyp19a1 esr1 | ESR1 | M22B-E000167 | CYP19A1 | M22B-EVID-000105 |
| M22A22B-LINK-012 | M22A-HANDOFF-003978 | il4 il13_il13ra1_il4ra | STAT6 | M22B-E000459 | Arg1 | M22B-EVID-000054 |
| M22A22B-LINK-013 | M22A-HANDOFF-003979 | il4 il13ra1_il4ra | STAT6 | M22B-E000459 | Arg1 | M22B-EVID-000054 |
| M22A22B-LINK-014 | M22A-HANDOFF-005070 | thpo mpl | STAT5A;STAT5B | M22B-E000455 | Ccnd1 | M22B-EVID-000077 |
| M22A22B-LINK-015 | M22A-HANDOFF-003039 | col1a1 ddr2 | PEA3 | M22B-E000299 | DDR1 promoter | M22B-EVID-000198 |
| M22A22B-LINK-016 | M22A-HANDOFF-003267 | ebi3_il12a il12rb2_il6st | STAT1;STAT4 | M22B-E000417 | IL-35-induced iTr35 suppressor program | M22B-EVID-000030 |
| M22A22B-LINK-017 | M22A-HANDOFF-001806 | bmp2 bmpr1a_acvr2a | SMAD1;SMAD4 | M22B-E000353 | Id1 | M22B-EVID-000037 |
| M22A22B-LINK-018 | M22A-HANDOFF-001808 | bmp2 bmpr1a_bmpr2 | SMAD1;SMAD4 | M22B-E000353 | Id1 | M22B-EVID-000037 |
| M22A22B-LINK-019 | M22A-HANDOFF-001811 | bmp2 bmpr1b_bmpr2 | SMAD1;SMAD4 | M22B-E000353 | Id1 | M22B-EVID-000037 |
| M22A22B-LINK-020 | M22A-HANDOFF-001284 | il12ab il12rb1_il12rb2 | STAT4 | M22B-E000443 | Tbx21 target enhancer | M22B-EVID-000050 |
| M22A22B-LINK-021 | M22A-HANDOFF-001446 | nodal acvr1c_acvr2b_cfc1 | FOXH1 | M22B-E000181 | Foxh1-bound Nodal direct-target module including gsc,nodal1,cer1,hhex,and lefty | M22B-EVID-000158 |
| M22A22B-LINK-022 | M22A-HANDOFF-003270 | edil3 itgb5 | HOXD3 | M22B-E000207 | EDIL3-alphaVbeta5 angiogenic HOXD3 program | M22B-EVID-000207 |
| M22A22B-LINK-023 | M22A-HANDOFF-003608 | gip gipr | CREB | M22B-E000095 | LPL promoter CRE-II | M22B-EVID-000215 |
| M22A22B-LINK-024 | M22A-HANDOFF-004124 | lep lepr | STAT3 | M22B-E000425 | Nhlh2 | M22B-EVID-000059 |
| M22A22B-LINK-025 | M22A-HANDOFF-004583 | prl prlr | STAT5A;STAT5B | M22B-E000457 | Csn2 | M22B-EVID-000072 |
| M22A22B-LINK-026 | M22A-HANDOFF-002399 | a2m lrp1 | CREB | M22B-E000032 | Activated alpha2M-LRP1-Src/Trk-ERK/Akt-CREB neural response program | M22B-EVID-000192 |
| M22A22B-LINK-027 | M22A-HANDOFF-001861 | fgf10 fgfr2 | ETV5 | M22B-E000174 | Shh MACS1 long-range enhancer | M22B-EVID-000141 |
| M22A22B-LINK-028 | M22A-HANDOFF-001885 | fgf23 fgfr4 | NFAT | M22B-E000272 | FGF23-FGFR4-PLCgamma-calcineurin-NFAT cardiac hypertrophy program | M22B-EVID-000179 |
| M22A22B-LINK-029 | M22A-HANDOFF-003909 | il12a_il12b il12rb1_il12rb2 | STAT4 | M22B-E000443 | Tbx21 target enhancer | M22B-EVID-000050 |
| M22A22B-LINK-030 | M22A-HANDOFF-003349 | epo epor | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-031 | M22A-HANDOFF-003988 | il6 il6ra_il6st | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000057 |
| M22A22B-LINK-032 | M22A-HANDOFF-005380 | edil3 itgav | HOXD3 | M22B-E000207 | EDIL3-alphaVbeta5 angiogenic HOXD3 program | M22B-EVID-000207 |

## Interpretation boundary

The `high` label applies to the tested direct TF-target evidence in the
cited comparator systems. It does not mean that the same receptor complex
produces the same target in an SCI receiver cell. IL-3 and IL-4 retain
hematopoietic/macrophage model limits; IL-6 and IL-10 retain cytokine
receptor/soluble-receptor and macrophage-comparator limits; EDA/EDAR and
EGF/EGFR retain skin and PC3 cancer-cell limits; and BDNF/TrkB retains
cortical-neuron limits. Estradiol/ESR1 retains a hypothalamic-neuron
limit, TPO/MPL retains a UT7-mpl hematopoietic limit, and the IL-4
rows retain an infected macrophage and alpha7nAChR co-stimulus limit. The
COL1A1/DDR2 row retains its human lung-fibroblast and receptor-feedback
limits. IL-35 retains an activated-T-cell and partial-receptor-signaling
limit, and its link is restricted to the Il12a/Ebi3 promoter module. The
BMP2 links retain the tested Id1-promoter and comparator-cell limits; the
primary paper does not test every submitted type-II receptor complex,
BMP-family ligand transfer, or an SCI receiver cell.
IL12/STAT4 retains the CD8 T-cell and enhancer-specific limit; Nodal/FOXH1
retains the Xenopus developmental target-module and receptor-composition
limits; GIP/CREB retains the human adipocyte insulin co-treatment limit;
leptin/STAT3 retains the hypothalamic LEPR context; PRL/STAT5 retains the
mammary epithelial and glucocorticoid-cofactor context; and A2M/CREB and
EDIL3/HOXD3 are explicitly bounded program-level links, with activated-A2M
or alphaVbeta5 heterodimer requirements respectively.

The remaining 247 candidate handoffs require new
exact-ligand/source review or a bounded program-level assignment. The new
terminal-TF assignments are RELB for EDA-EDAR and ELK1 for EGF-EGFR;
the IL-10 row extends an existing STAT3 assignment to an evidence-backed
target. The related IL-13 receptor-family row is not included because the
strict Arg1 extraction is IL-4-specific. The 5,632 no-terminal-TF handoffs
remain the broader Module 22A search-expansion pool and were not
force-filled from pathway plausibility.

Generated by `scripts/audit_module22a_22b_high_confidence_links.py`.
