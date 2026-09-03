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
- Promotion-ready bounded links: 113
- Links adding an evidence-backed terminal-TF assignment: 2
- Candidate handoffs without an exact reusable high-confidence link: 172

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
| M22A22B-LINK-033 | M22A-HANDOFF-001315 | inhba acvr1b_acvr2a | SMAD2/3 | M22B-E000378 | Fst | M22B-EVID-000378 |
| M22A22B-LINK-034 | M22A-HANDOFF-001316 | inhba acvr1b_acvr2b | SMAD2/3 | M22B-E000378 | Fst | M22B-EVID-000378 |
| M22A22B-LINK-035 | M22A-HANDOFF-005094 | tnf fas | RELA | M22B-E000310 | FAS target gene | M22B-EVID-000271 |
| M22A22B-LINK-036 | M22A-HANDOFF-002935 | cfc1 acvr1b | FOXH1 | M22B-E000181 | Foxh1-bound Nodal direct-target module including gsc,nodal1,cer1,hhex,and lefty | M22B-EVID-000158 |
| M22A22B-LINK-037 | M22A-HANDOFF-002936 | cfc1 acvr2a | FOXH1 | M22B-E000181 | Foxh1-bound Nodal direct-target module including gsc,nodal1,cer1,hhex,and lefty | M22B-EVID-000158 |
| M22A22B-LINK-038 | M22A-HANDOFF-004332 | nodal acvr1b_acvr2a_cfc1 | FOXH1 | M22B-E000181 | Foxh1-bound Nodal direct-target module including gsc,nodal1,cer1,hhex,and lefty | M22B-EVID-000158 |
| M22A22B-LINK-039 | M22A-HANDOFF-004334 | nodal acvr1b_acvr2b_cfc1 | FOXH1 | M22B-E000181 | Foxh1-bound Nodal direct-target module including gsc,nodal1,cer1,hhex,and lefty | M22B-EVID-000158 |
| M22A22B-LINK-040 | M22A-HANDOFF-004336 | nodal acvr1c_acvr2a | FOXH1 | M22B-E000181 | Foxh1-bound Nodal direct-target module including gsc,nodal1,cer1,hhex,and lefty | M22B-EVID-000158 |
| M22A22B-LINK-041 | M22A-HANDOFF-004910 | shh boc | NKX2-2;OLIG2 | M22B-E000284 | NKX2-2/OLIG2-bound neural-progenitor fate determinant and Shh-feedback target module | M22B-EVID-000254 |
| M22A22B-LINK-042 | M22A-HANDOFF-004912 | shh gas1 | NKX2-2;OLIG2 | M22B-E000284 | NKX2-2/OLIG2-bound neural-progenitor fate determinant and Shh-feedback target module | M22B-EVID-000254 |
| M22A22B-LINK-043 | M22A-HANDOFF-001287 | il13 il4r_il13ra1 | STAT6 | M22B-E000459 | Arg1 | M22B-EVID-000054 |
| M22A22B-LINK-044 | M22A-HANDOFF-003913 | il13 il13_il13ra1_il4ra | STAT6 | M22B-E000459 | Arg1 | M22B-EVID-000054 |
| M22A22B-LINK-045 | M22A-HANDOFF-003918 | il15 il15ra_il2rb_il2rg | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-046 | M22A-HANDOFF-003960 | il2 il2ra_il2rb_il2rg | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-047 | M22A-HANDOFF-003961 | il2 il2rb_il2rg | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-048 | M22A-HANDOFF-003990 | il7 il2rg_il7r | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-049 | M22A-HANDOFF-003964 | il21 il21r_il2rg | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-050 | M22A-HANDOFF-001296 | il22 il22ra1_il10rb | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-051 | M22A-HANDOFF-001301 | il31 il31ra_osmr | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-052 | M22A-HANDOFF-001360 | lif lifr_il6st | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-053 | M22A-HANDOFF-004156 | lif il6st_lifr | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-054 | M22A-HANDOFF-001489 | osm osmr_il6st | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-055 | M22A-HANDOFF-000382 | ctf1 lifr_il6st | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-056 | M22A-HANDOFF-000368 | cntf cntfr_lifr | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-057 | M22A-HANDOFF-001311 | il5 il5ra_csf2rb | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-058 | M22A-HANDOFF-003984 | il5 csf2rb_il5ra | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-059 | M22A-HANDOFF-001313 | il7 il7r_il2rg | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-060 | M22A-HANDOFF-001282 | il11 il11r complex 1 | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-061 | M22A-HANDOFF-003904 | il11 il11ra1_il6st | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-062 | M22A-HANDOFF-001299 | il27 complex il27ra_il6st | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-063 | M22A-HANDOFF-003268 | ebi3_il27 il27ra_il6st | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-064 | M22A-HANDOFF-003581 | gh ghr | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-065 | M22A-HANDOFF-001375 | lta1b2 ltbr | RELB | M22B-E000336 | Ltb;Tnfrsf9 | M22B-EVID-000620 |
| M22A22B-LINK-066 | M22A-HANDOFF-003178 | ctf1 il6st_lifr | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-067 | M22A-HANDOFF-001747 | tslp il7r_crlf2 | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-068 | M22A-HANDOFF-005163 | tslp crlf2_il7r | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-069 | M22A-HANDOFF-001854 | csf2 csf2ra_csf2rb | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-070 | M22A-HANDOFF-003349 | epo epor | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-071 | M22A-HANDOFF-001314 | il9 il9r_il2rg | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-072 | M22A-HANDOFF-003991 | il9 il2rg_il9r | STAT5 | M22B-E000449 | Cish | M22B-EVID-000006 |
| M22A22B-LINK-079 | M22A-HANDOFF-001908 | ifnb1 ifnar1_ifnar2 | STAT1;STAT2;IRF9 | M22B-E000414 | ISRE-containing interferon-stimulated antiviral gene program | M22B-EVID-000011 |
| M22A22B-LINK-080 | M22A-HANDOFF-001279 | ifnl2 ifnlr1_il10rb | STAT1;STAT2;IRF9 | M22B-E000414 | ISRE-containing interferon-stimulated antiviral gene program | M22B-EVID-000011 |
| M22A22B-LINK-081 | M22A-HANDOFF-001280 | ifnl3 ifnlr1_il10rb | STAT1;STAT2;IRF9 | M22B-E000414 | ISRE-containing interferon-stimulated antiviral gene program | M22B-EVID-000011 |
| M22A22B-LINK-082 | M22A-HANDOFF-001269 | ifna1 ifnar1_ifnar2 | STAT1;STAT2;IRF9 | M22B-E000414 | ISRE-containing interferon-stimulated antiviral gene program | M22B-EVID-000011 |
| M22A22B-LINK-083 | M22A-HANDOFF-001274 | ifna2 ifnar1_ifnar2 | STAT1;STAT2;IRF9 | M22B-E000414 | ISRE-containing interferon-stimulated antiviral gene program | M22B-EVID-000011 |
| M22A22B-LINK-084 | M22A-HANDOFF-001275 | ifna4 ifnar1_ifnar2 | STAT1;STAT2;IRF9 | M22B-E000414 | ISRE-containing interferon-stimulated antiviral gene program | M22B-EVID-000011 |
| M22A22B-LINK-085 | M22A-HANDOFF-001276 | ifna5 ifnar1_ifnar2 | STAT1;STAT2;IRF9 | M22B-E000414 | ISRE-containing interferon-stimulated antiviral gene program | M22B-EVID-000011 |
| M22A22B-LINK-086 | M22A-HANDOFF-001277 | ifna6 ifnar1_ifnar2 | STAT1;STAT2;IRF9 | M22B-E000414 | ISRE-containing interferon-stimulated antiviral gene program | M22B-EVID-000011 |
| M22A22B-LINK-087 | M22A-HANDOFF-001278 | ifna7 ifnar1_ifnar2 | STAT1;STAT2;IRF9 | M22B-E000414 | ISRE-containing interferon-stimulated antiviral gene program | M22B-EVID-000011 |
| M22A22B-LINK-088 | M22A-HANDOFF-001908 | ifnb1 ifnar1_ifnar2 | STAT1;STAT2;IRF9 | M22B-E000414 | ISRE-containing interferon-stimulated antiviral gene program | M22B-EVID-000011 |
| M22A22B-LINK-089 | M22A-HANDOFF-001279 | ifnl2 ifnlr1_il10rb | STAT1;STAT2;IRF9 | M22B-E000414 | ISRE-containing interferon-stimulated antiviral gene program | M22B-EVID-000011 |
| M22A22B-LINK-090 | M22A-HANDOFF-001280 | ifnl3 ifnlr1_il10rb | STAT1;STAT2;IRF9 | M22B-E000414 | ISRE-containing interferon-stimulated antiviral gene program | M22B-EVID-000011 |
| M22A22B-LINK-091 | M22A-HANDOFF-001314 | il9 il9r_il2rg | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-092 | M22A-HANDOFF-003991 | il9 il2rg_il9r | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-093 | M22A-HANDOFF-001488 | osm lifr_il6st | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-094 | M22A-HANDOFF-004439 | osm il6st_lifr | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-095 | M22A-HANDOFF-003973 | il24 il20rb_il22ra1 | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-101 | M22A-HANDOFF-000204 | areg egfr | ELK1 | M22B-E000158 | EGR1 promoter | M22B-EVID-000622 |
| M22A22B-LINK-102 | M22A-HANDOFF-003150 | crh crhr1 | CREB | M22B-E000108 | cFos | M22B-EVID-000332 |
| M22A22B-LINK-103 | M22A-HANDOFF-001905 | gdnf gfra1_ret | CREB | M22B-E000108 | cFos | M22B-EVID-000332 |
| M22A22B-LINK-104 | M22A-HANDOFF-005137 | trh trhr | CREB | M22B-E000108 | cFos | M22B-EVID-000332 |
| M22A22B-LINK-105 | M22A-HANDOFF-001323 | ins1 insr | CREB;FOXO1 | M22B-E000135 | Ndn (necdin) promoter | M22B-EVID-000129 |
| M22A22B-LINK-106 | M22A-HANDOFF-004689 | rbp4 stra6 | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-107 | M22A-HANDOFF-001814 | bmp4 bmpr1a_bmpr2 | SMAD1/5/8 | M22B-E000346 | ID1 | M22B-EVID-000016 |
| M22A22B-LINK-108 | M22A-HANDOFF-001827 | bmp6 acvr1_acvr2a | SMAD1/5/8 | M22B-E000346 | ID1 | M22B-EVID-000016 |
| M22A22B-LINK-109 | M22A-HANDOFF-001829 | bmp6 acvr1_bmpr2 | SMAD1/5/8 | M22B-E000346 | ID1 | M22B-EVID-000016 |
| M22A22B-LINK-110 | M22A-HANDOFF-001830 | bmp6 bmpr1a_acvr2a | SMAD1/5/8 | M22B-E000346 | ID1 | M22B-EVID-000016 |
| M22A22B-LINK-111 | M22A-HANDOFF-001832 | bmp6 bmpr1a_bmpr2 | SMAD1/5/8 | M22B-E000346 | ID1 | M22B-EVID-000016 |
| M22A22B-LINK-112 | M22A-HANDOFF-000209 | bmp7 bmpr1a_acvr2a | SMAD1/5/8 | M22B-E000346 | ID1 | M22B-EVID-000016 |
| M22A22B-LINK-113 | M22A-HANDOFF-000211 | bmp7 bmpr1b_acvr2a | SMAD1/5/8 | M22B-E000346 | ID1 | M22B-EVID-000016 |
| M22A22B-LINK-114 | M22A-HANDOFF-002971 | cntf cntfr_il6st | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-115 | M22A-HANDOFF-002975 | cntf il6st_lifr | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-116 | M22A-HANDOFF-001799 | areg egfr_erbb2 | ELK1 | M22B-E000158 | EGR1 promoter | M22B-EVID-000622 |
| M22A22B-LINK-117 | M22A-HANDOFF-000004 | 22hc-cyp3a4 nr1h4 | NR1H4 | M22B-E000288 | CYP3A4 | M22B-EVID-000096 |
| M22A22B-LINK-118 | M22A-HANDOFF-002586 | apoa1 abca1 | STAT3 | M22B-E000431 | Socs3 | M22B-EVID-000001 |
| M22A22B-LINK-119 | M22A-HANDOFF-001309 | il4 il4r_il2rg | STAT6 | M22B-E000459 | Arg1 | M22B-EVID-000010 |
| M22A22B-LINK-120 | M22A-HANDOFF-003982 | il4 il2rg_il4ra | STAT6 | M22B-E000459 | Arg1 | M22B-EVID-000010 |
| M22A22B-LINK-121 | M22A-HANDOFF-000444 | e2-hsd17b1 esr1 | ESR1 | M22B-E000167 | CYP19A1 | M22B-EVID-000105 |
| M22A22B-LINK-122 | M22A-HANDOFF-001408 | mstn tgfbr1_acvr2b | SMAD3;SMAD4 | M22B-E000394 | SERPINE1/PAI-1 | M22B-EVID-000019 |
| M22A22B-LINK-123 | M22A-HANDOFF-004274 | mstn acvr1b_acvr2a | SMAD3;SMAD4 | M22B-E000394 | SERPINE1/PAI-1 | M22B-EVID-000019 |
| M22A22B-LINK-124 | M22A-HANDOFF-004276 | mstn acvr2a_tgfbr1 | SMAD3;SMAD4 | M22B-E000394 | SERPINE1/PAI-1 | M22B-EVID-000019 |

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
Activin A links retain the ACVR1B/ALK4 gonadotrope context and the
unresolved ACVR2A-versus-ACVR2B composition; they reuse the Fst enhancer
edge as a bounded receptor-complex branch. The TNF/FAS link is an
indirect TNF-induced RELA-to-FAS transcription chain and does not claim
TNF-FAS binding or a TNF receptor-proximal interaction.
BMP2 links retain the tested Id1-promoter and comparator-cell limits; the
primary paper does not test every submitted type-II receptor complex,
BMP-family ligand transfer, or an SCI receiver cell.
IL12/STAT4 retains the CD8 T-cell and enhancer-specific limit; Nodal/FOXH1
retains the Xenopus developmental target-module and receptor-composition
limits; GIP/CREB retains the human adipocyte insulin co-treatment limit;
leptin/STAT3 retains the hypothalamic LEPR context; PRL/STAT5 retains the
mammary epithelial and glucocorticoid-cofactor context; and A2M/CREB and
EDIL3/HOXD3 are explicitly bounded program-level links, with activated-A2M
or alphaVbeta5 heterodimer requirements respectively. The CRH/CRHR1,
GDNF/GFRA1-RET, and TRH/TRHR additions reuse the existing CREB-cFOS edge
as bounded comparator programs without direct ligand-specific CREB
occupancy at c-fos. Ins1/InsR is bounded to the insulin/IGF-I CREB/FOXO1
recruitment study at the Ndn promoter, and RBP4/STRA6 is bounded to the
holo-RBP-retinol/JAK2/STAT/SOCS3 comparator program; neither is an SCI
receiver-cell claim or an isoform-specific molecular assignment.

The remaining 172 candidate handoffs require new
exact-ligand/source review or a bounded program-level assignment. The new
terminal-TF assignments are RELB for EDA-EDAR and ELK1 for EGF-EGFR;
the IL-10 row extends an existing STAT3 assignment to an evidence-backed
target. The related IL-13 receptor-family row is not included because the
strict Arg1 extraction is IL-4-specific. The 5,632 no-terminal-TF handoffs
remain the broader Module 22A search-expansion pool and were not
force-filled from pathway plausibility.

Generated by `scripts/audit_module22a_22b_high_confidence_links.py`.
