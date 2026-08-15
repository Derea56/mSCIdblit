# Module 21A batch 151 review summary

Batch 151 reviewed exactly the 25 supplied priority-8 low/uncertain queue rows corresponding to filtered queue ordinals 3226–3250. The review is recorded in `work/module21_relay/module21a_batch151_review.tsv` using the existing 13-column batch-review schema.

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
| reviewed_relay_candidate | 6 |
| reviewed_binding_only | 9 |
| reviewed_function_only | 1 |
| reviewed_unresolved | 9 |

| Evidence layer | Count |
|---|---:|
| ligand_receptor_binding_or_activation | 18 |
| receptor_proximal_relay | 5 |
| downstream_pathway_function | 2 |

## Main evidence retained

- **POSTN–ITGAV_ITGB5:** periostin/αV-integrin evidence supports αVβ5 participation in adhesion or migration and ILK/FAK-associated responses, but receptor stoichiometry and SCI-cell weighting remain context dependent (PMID 18753297; PMID 19695571).
- **PRL–ERBB2:** prolactin/PRLR cross-talk can activate ERBB2 through JAK2 and Grb2–Ras–MAPK in human breast-cancer models. This is transactivation, not direct PRL–ERBB2 binding (PMID 10938266; PMID 16785991).
- **Prn–Rpsa and Prnd–Rpsa:** primary studies support physical binding of PrP or Doppel to the RPSA/37–67-kDa laminin-receptor system, without assigning a canonical intracellular relay (PMID 9396609; PMID 12675517; PMID 15246873).
- **PROC family:** protein-C-derived peptide motifs bind Mac-1/ITGAM, activated protein C binds and activates TEK/Tie2, and thrombomodulin accelerates thrombin-mediated protein-C activation. These were kept distinct from native inactive PROC exact-pair signaling (PMID 25613106; PMID 28005151; PMID 32632109).
- **PRSS2/PARs:** PRSS2/anionic trypsin supports PAR1 and PAR2 activation in cell-context-dependent assays; PAR4 evidence is retained at medium confidence because the recent direct platelet study used trypsin without isolating PRSS2. PAR3 was left unresolved (PMID 16231009; PMID 41248893; PMID 24030758).
- **PSAP:** PSAP/saposin-C effects on AR were recorded as downstream function only; PSAP–LRP1 was recorded as uptake/trafficking evidence, not a classical signaling relay (PMID 17044040; PMID 9707421; PMID 26370502).
- **PSEN1:** PSEN1-dependent CD44 intramembrane cleavage was recorded as enzyme-substrate processing and downstream signaling potential; PSEN1–NCSTN was recorded as γ-secretase complex assembly/maturation, not ligand-receptor activation (PMID 12223485; PMID 12629514; PMID 11943765; PMID 15591316).

## Explicit unresolved boundaries

No qualifying exact pair-specific evidence was located for Postn–Ptk7, Ppy–Adra2a/Gpr83/Grm7/Mtnr1a, Psap–Celsr1, or Prss2–Pard3. PP–Npy1r, PP–Npy2r, and PP–Npy5r were retained as binding-only/low-affinity records without an assigned PP-specific downstream relay. The review does not infer direct molecular interaction from pathway, expression, family, or functional-output evidence.
