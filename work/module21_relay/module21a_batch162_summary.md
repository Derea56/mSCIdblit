# Module 21A Batch 162 review summary

Batch 162 reviewed exactly the 25 supplied filtered-queue rows at queue ordinals 3501–3525. The raw output is [`module21a_batch162_review.tsv`](/Users/derea/Documents/SCI/work/module21_relay/module21a_batch162_review.tsv) and uses the exact 13-column schema:

`review_id`, `pair`, `status`, `stable_citations`, `species`, `cell_type_model`, `assay_or_perturbation`, `relation_type`, `evidence_layer`, `pathway_branch`, `confidence`, `limitations`, `terminal_TF`.

## Validation and scope

- 25/25 exact supplied review IDs written in the supplied order.
- 25/25 exact supplied pair labels preserved.
- 25 unique review IDs and 25 unique pair labels.
- Every data row has 13 fields, a populated limitations field, and explicit `null` terminal TF.
- Binding/activation, receptor-proximal relay, downstream pathway/function, and ligand-processing evidence are recorded as separate layers; pathway/function evidence was not used to infer direct interaction.
- No Module20A file, shared Module21A register, Module22A handoff, integration output, or source register was modified.
- No commit was created.

## Disposition

| Status | Rows |
|---|---:|
| `reviewed_relay_candidate` | 10 |
| `reviewed_function_only` | 5 |
| `reviewed_binding_only` | 2 |
| `reviewed_unresolved` | 8 |
| **Total** | **25** |

## Evidence decisions

- **Spectrin/PTPRA and SST receptor substitutions:** SPTAN1–PTPRA was retained as unresolved because the primary source is computational single-cell communication inference, not a direct ligand/receptor experiment. SPTBN2–PTPRA is likewise unresolved. SST evidence supports SSTR subtypes, not ADRA2A, GRM7, or MTNR1A.
- **ST6GAL1:** ST6GAL1–CD22 is function-only glycan-ligand generation: ST6GAL1 controls alpha2,6-sialylated CD22 ligands and CD22-dependent BCR signaling, but no direct ST6GAL1 protein–CD22 receptor interaction was assigned (PMID:9539767; PMID:16782884; DOI:10.1038/ni1283). ST6GAL1–EGFR is a glycosylation-dependent receptor-modulation candidate with EGFR activation and AKT/NF-kappaB outputs in epithelial cancer models (PMID:29402301; PMCID:PMC10520885).
- **TAC1/TAC2:** TAC1–DPP4 and TAC1–FAP are explicit peptide-processing edges, not receptor relays: both enzymes cleave substance P (PMID:24516103; PMID:21314817). Mature TAC1-derived peptides can activate TACR3, while Tac2/NKB can cross-activate TACR1 and TACR2 at lower potency than their preferred ligands; the precursor/source annotation and mature-peptide assays remain separate (PMID:38065934; PMID:9276127; PMID:7961636).
- **TCN2, TCTN1, and TDGF1:** TCN2–CNR1 is unresolved because the cognate TCN2 receptor is CD320, not CNR1 (PMID:27411955). TCTN1–TMEM67 is a ciliary transition-zone protein-complex/function edge, not a secreted ligand-receptor relay (PMCID:PMC3145011). TDGF1/Cripto has direct co-receptor evidence with ACVR1B/ALK4, ACVR1C/ALK7, and GPC1, with Nodal-dependent or Src-dependent pathway outputs; ACVR2A/ACVR2B binary TDGF1 edges were not promoted because type-II receptor participation is complex- and ligand-dependent (PMID:11909953; PMCID:PMC312747; PMID:12649175; PMCID:PMC5354514).
- **Trefoil factors and TFPI:** TFF1–MUC5AC and TFF2–MUC6 are mucin-complex/function edges, not intracellular receptor relays (PMID:15289936; PMCID:PMC4183777). TFF2–CXCR4 and TFF3–CXCR4/ACKR3 retain receptor-dependent function/relay evidence, but the TFF3 studies rely on blockade and structure-based modeling, and ERK1/2 activation was not receptor-dependent in the cited ocular model (PMID:19064997; PMID:26780310). TFPI–F3 is a tissue-factor coagulation inhibition context involving TF-FVIIa-Xa-TFPI complexes, not an isolated TFPI–F3 receptor edge (PMID:8982054; PMID:11985578).

No terminal TF was assigned. Even where SMAD2/3, MAPK, AKT, NF-kappaB, beta-arrestin, or ERK-related outputs were measured, they were kept in receptor-proximal or downstream-function fields unless the exact queued pair and a terminal-TF activation experiment were both directly resolved. Species, mature-peptide processing, receptor-complex stoichiometry, glycoform, assay model, and lack of SCI receiver-cell validation are recorded per row in the TSV limitations.
