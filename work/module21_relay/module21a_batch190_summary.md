# Module 21A Batch 190 review summary

Batch 190 reviews exactly filtered Module20A external-review queue ordinals **4201–4225** in the established priority-8 order: `M20A-EXT-3204` through `M20A-EXT-3228`. The raw artifact is [`module21a_batch190_review.tsv`](/Users/derea/Documents/SCI/mSCIdblit/work/module21_relay/module21a_batch190_review.tsv) and uses the exact 13-column schema.

## Validation and scope

- 25/25 exact queue-derived review IDs written in supplied order.
- 25/25 exact submitted pair labels preserved.
- 25 unique review IDs and 25 unique pair labels.
- Every row has 13 fields, populated stable citation, species/model, assay, relation, evidence layer, pathway, confidence, and limitation fields.
- Every `terminal_TF` is the literal `null`; no terminal TF was assigned.
- Existing Module20A LR files, Module21A ledgers/registers, Module22A handoff, and integration outputs were not modified. No commit was created.

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 9 |
| `reviewed_binding_only` | 5 |
| `reviewed_function_only` | 3 |
| `reviewed_unresolved` | 8 |
| **total** | **25** |

Confidence counts: `low`=8, `low-medium`=3, `medium`=13, `medium-high`=1.

## Evidence decisions

- **SPP1/SPTAN1/SPTBN2 and SST substitutions:** SPP1–S1PR1, SPTAN1–PTPRA, and SPTBN2–PTPRA remain unresolved because the cited studies are organ-crosstalk/computational or cytoskeletal comparator contexts without exact-pair binding, activation, or relay assays. SST evidence was kept separate from ADRA2A, GRM7, and MTNR1A; receptor-family or shared Gi/o coupling was not transferred.
- **SST–SSTR1–5:** Primary pharmacology supports somatostatin-family ligand binding across SSTR1–5 in recombinant human receptor systems (PMID:24587133; PMCID:PMC3937410). SSTR2 and SSTR3 additionally have receptor-specific cAMP/ERK1/2 readouts and are retained as bounded relay candidates; SSTR1, SSTR4, and SSTR5 remain binding-only in this batch because their exact downstream activation was not isolated in the cited assay.
- **ST6GAL1 and tachykinins:** ST6GAL1–CD22 is glycan-ligand generation plus B-cell function, not ST6GAL1 protein binding to CD22; ST6GAL1–EGFR is glycosylation-dependent receptor modulation. TAC1–DPP4 and TAC1–FAP are peptide-processing edges outside the three relay layers, retained as explicit processing boundaries. TAC1/TAC2 receptor records distinguish mature tachykinin pharmacology from precursor/source-gene identity; Tac2–TACR3 is supported as a low-medium receptor-proximal candidate by recombinant mouse/human NK3 assays (PMID:11226387).
- **TCN2, TCTN1, and TDGF1:** TCN2–CNR1 remains unresolved because the cognate transcobalamin receptor is CD320, not CNR1. TCN2–LRP2 is function-only: holo-TC uptake was LRP2-dependent in a variant/overexpression context (PMID:28903415), without purified binding or intracellular relay. TCTN1–TMEM67 is a ciliary transition-zone complex/function edge. TDGF1/Cripto–ACVR1B and –ACVR1C retain Nodal receptor-complex evidence; TDGF1–ACVR2A remains unresolved because type-II receptor participation does not establish a direct binary TDGF1 edge.

Pathway names such as Gi/o, cAMP, ERK1/2, AKT/NF-kappaB, SMAD2/3, and Ca2+ are recorded as contextual relay or functional outputs only. No pathway-level or functional observation was used to infer a direct molecular interaction, and no terminal-TF assignment was made.
