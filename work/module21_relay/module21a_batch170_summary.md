# Module 21A batch 170 review

Batch 170 reviews exactly the 25 requested filtered-queue rows, ordinals
3701–3725. The raw output is
`module21a_batch170_review.tsv` and uses the exact 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

## Disposition

- 1 `reviewed_function_only`: Wnt5a–Lrp5.
- 7 rows retain partial binding, receptor-proximal relay, or downstream-function context but remain `reviewed_unresolved` because the submitted composite receptor pair was not tested as a complete WNT5B–FZD–LRP5/6 complex: Wnt5b–Fzd1_Lrp5, Wnt5b–Fzd2_Lrp5, Wnt5b–Fzd2_Lrp6, Wnt5b–Fzd3_Lrp5, Wnt5b–Fzd3_Lrp6, Wnt5b–Fzd8_Lrp5, and Wnt5b–Fzd8_Lrp6.
- 13 additional `reviewed_unresolved` rows: Wnt5a–Ldlr, Wnt5a–Lrp2, Wnt5a–Ptprk, Wnt5a–Vangl2, Wnt5b–Fzd10_Lrp5, Wnt5b–Fzd10_Lrp6, Wnt5b–Fzd5_Lrp5, Wnt5b–Fzd5_Lrp6, Wnt5b–Fzd6_Lrp5, Wnt5b–Fzd6_Lrp6, Wnt5b–Fzd7_Lrp5, Wnt5b–Fzd7_Lrp6, and Wnt5b–Fzd9_Lrp5.
- 4 `no_evidence_boundary` rows: Wnt4–Smo, Wnt5a–Adrb2, Wnt5a–Antxr1, and Wnt5a–Epha7.

The disposition counts are therefore: 1 function-only, 20 reviewed-unresolved, and 4 no-evidence-boundary rows; total 25.

## Evidence-layer decisions

The Wnt5a–Lrp5 row is kept at the downstream-function layer. The primary
endometrial study used FZD5 neutralization/knockdown and DKK1 blockade of LRP
coreceptors, together with WNT5A binding-to-cell, active-beta-catenin,
TCF/LEF-reporter, clonogenicity, and self-renewal readouts. It supports a
WNT5A–FZD5/LRP5-associated response, but does not isolate direct
WNT5A–LRP5 binding or define an adaptor/kinase relay.

Primary studies support partial WNT5B–FZD2 and WNT5B–FZD3/FZD8 relay contexts,
and WNT5B binding to selected isolated FZD CRDs. These are retained in their
own `evidence_layer` fields. They are not promoted to the submitted
FZD–LRP5/6 composite edge because the LRP5/6 component was not tested as the
required or directly engaged subunit. Downstream cytokine, STAT3, SMAD3, YAP,
JNK, migration, stemness, and tumor outputs remain downstream function and do
not establish direct ligand–receptor interaction.

The Wnt5a–Ldlr row records only lipid/vascular context from LDLR-deficient
models; LRP1 studies were not transferred to LDLR. Wnt5a–Lrp2 remains
unresolved because the relevant primary work concerns LRP1, not LRP2.
Wnt5a–Vangl2 remains unresolved because PCP pathway membership is not direct
WNT5A–VANGL2 ligand evidence. Wnt4–Smo remains a no-evidence boundary because
the primary developmental study treats Wnt4/5 and Shh/Smo as parallel
patterning inputs.

## Source and search boundary

Primary research was prioritized, including the WNT5A–FZD2 receptor study
(PMID 19910923), WNT5A–FZD5/LRP5-associated endometrial functional study
(PMID 35295855), WNT5B–FZD interaction mapping (PMID 25605717), WNT5B–FZD2
lung-fibroblast relay work (PMID 27036869), WNT5B–FZD7 breast-cancer work
(PMCID PMC7487719; DOI 10.1186/s12964-020-00646-2), WNT5B–FZD3 relay work
(PMID 39094673; DOI 10.1016/j.cellsig.2024.111330), and Wnt4/5 versus Shh/Smo
developmental perturbation (PMID 19285468). Exact-pair PubMed query URLs are
included in each row for unresolved boundaries.

All 25 `terminal_TF` values are literal `null`. No terminal TF was assigned
from a reporter, pathway annotation, cytokine output, or phenotype alone.
Every row has a populated limitations field, stable citation locators, and an
explicit evidence layer. Only this batch TSV and summary are intended to be
written; Module20A files, shared Module21A registers, frozen manifests, and
integration outputs remain untouched.
