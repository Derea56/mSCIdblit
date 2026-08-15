# Module 21A batch 153 review summary

Batch 153 reviewed exactly the 25 supplied priority-8 low/uncertain queue rows for filtered queue ordinals 3276–3300. The review uses the existing 13-column batch-review schema in `work/module21_relay/module21a_batch153_review.tsv` and preserves the supplied canonical pair labels.

## Validation summary

- Rows written: **25/25**
- Unique review IDs: **25/25**
- Unique canonical pair labels: **25/25**
- Evidence fields: **13/13 populated in every row**
- Invented or out-of-scope rows: **none**
- Terminal TF assignments: **none**
- Module 20A ledgers, frozen manifest, shared Module 21A registers, and integration outputs: **not modified**

## Disposition counts

| Status | Count |
|---|---:|
| reviewed_relay_candidate | 1 |
| reviewed_binding_only | 4 |
| reviewed_unresolved | 20 |

| Evidence layer | Count |
|---|---:|
| ligand_receptor_binding_or_activation | 25 |
| receptor_proximal_relay | 1 |
| downstream_pathway_function | 2 |

Rows with multiple layers are counted in each applicable layer; this is intentional and does not collapse binding, receptor-proximal relay, or downstream function into one claim.

## Main evidence retained

- **Pth2/TIP39 rows:** primary pharmacology supports TIP39/PTH2R, not GPR20, GPR84, TSHR, VIPR1, or the RAMP proteins. RAMP2 and RAMP3 evidence concerns receptor-component interactions with PTH1R/PTH2R, not direct TIP39-RAMP ligand binding (PMID:11159842; PMID:12446722).
- **Pthlh/PTHrP rows:** primary structural and pharmacology studies support PTHrP/PTH1R. PAC1, adrenergic, GPR84, PRLHR, TSHR, VIPR1, and RAMP-family findings were retained as cognate or receptor-complex comparators, not transferred to PTHrP (PMID:19674967; PMID:12446722; PMID:16966319).
- **Ptn–Cdh10:** a human proteome-scale yeast-two-hybrid network reports a low-confidence physical interaction, without dedicated extracellular receptor activation or downstream follow-up (PMID:16169070).
- **Ptn–Ncl:** PTN-NCL physical association and NCL-dependent migration/internalization or PRAS40-associated function are supported, but the RPTPβ/ζ-integrin-c-Src context remains distinct from a standalone PTN-NCL kinase relay (PMID:16156786; PMID:22423616; PMID:23161541; PMID:38302728).
- **Ptn–Sdc1/Sdc4:** PTN binds syndecan-associated heparan- and chondroitin-sulfate chains, with SDC1 core-protein contribution reported; no SDC1/SDC4-specific intracellular relay was assigned (PMID:15226297).
- **Ptn–Sdc3:** direct HB-GAM/PTN binding to N-syndecan/SDC3 and SDC3-dependent c-Src/cortactin neurite or migration outputs are supported in developmental neural and osteoblast models (PMID:8175719; PMCID:PMC2064262; PMID:9749725).

## Explicit unresolved boundaries

Pth2/Pthlh noncognate GPCR rows, Pth2/Pthlh-to-RAMP ligand rows, and Ptn–Plxnb2/Ptprb/Ptprs remain unresolved for the exact queued edge. Ptn–Sdc2 is also unresolved as a native binary pair because the positive study requires Y-P30 in a PTN–Y-P30–SDC2/3 ternary complex. Expression, single-cell communication scores, receptor-family similarity, high-throughput interaction records, pathway output, or a related cognate ligand were not used to infer direct molecular activation. No terminal TF was assigned.
