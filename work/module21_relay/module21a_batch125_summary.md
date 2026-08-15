# Module 21A Batch 125 summary

The supplied Batch 125 list contains 24 exact Module 20A rows (M20A-EXT-1923, M20A-EXT-1924, M20A-EXT-1925, M20A-EXT-1926, M20A-EXT-1927, M20A-EXT-1930, M20A-EXT-1931, M20A-EXT-1933, M20A-EXT-1934, M20A-EXT-1936, M20A-EXT-1937, M20A-EXT-1940, M20A-EXT-1941, M20A-EXT-1945, M20A-EXT-1947, M20A-EXT-1948, M20A-EXT-1949, M20A-EXT-1951, M20A-EXT-1952, M20A-EXT-1954, M20A-EXT-1955, M20A-EXT-1956, M20A-EXT-1957, and M20A-EXT-1958), although the request states “exactly 25 rows.” Searches covered exact-symbol queries across PubMed, PMC, publisher pages, and Reactome, prioritizing primary research. Intracellular signaling evidence was evaluated separately from Module20A ligand-receptor evidence. No unlisted or adjacent queue row was invented to fill the missing 25th item.

## Outcomes

- 7 receptor-proximal relay candidates: GNAS-LHCGR, GNAS-TSHR, GNAS-VIPR1, GPC3-IGF1R, GRN-EGFR, GSTP1-EGFR, and GSTP1-TRAF2.
- 1 direct binding candidate: GP1BA-Mac-1/ITGAM-ITGB2.
- 16 unresolved or boundary cases: GNAS-PTGDR, GNB3-GABBR2, GP49A-LAIR1, GPC3-FLT1, GPC3-LRP2, GPC3-TNFRSF11B, GPC3-VSIG10L, GPHA2-EPHA6, GPI1-NTRK1, GRN-CD209A, GRN-NTRK1, GRP-BRS3, GRP-FAP, GRP-NMBR, GSTM7-RYR2, and GSTO1-RYR1.
- No terminal TF assignments; every `terminal_TF` value is `null`.

## Evidence boundaries

GNAS rows were treated as intracellular Gs-alpha relay reviews rather than extracellular ligand claims. Exact receptor-proximal evidence was retained for LHCGR, TSHR, and VIPR1; generic Gs annotations were not transferred to PTGDR. GPC3-IGF1R was retained as an IGF-II-dependent receptor-complex/pathway edge, while GPC3 evidence for other receptor families was not generalized. GRN-EGFR was retained as an EGFR/RYK receptor-network relay because the strongest direct binding in the cited mesothelioma study is GRN-RYK, not GRN-EGFR. GP1BA-Mac-1 was retained as a direct trans-cellular adhesion interaction, separate from its vascular functional consequences. GRP-BRS3 and GRP-NMBR remain unresolved because mammalian BRS3 is orphan/low-affinity for GRP and NMBR is NMB-preferring. GSTP1-EGFR and GSTP1-TRAF2 are direct intracellular molecular/pathway edges; their downstream JNK, c-Jun, ASK1, apoptosis, and survival outputs were not used to assign a terminal TF.

Only this raw review TSV and this batch summary were written. Shared Module 21A registers, Module20A ledgers, the frozen manifest, and integration outputs were not modified.
