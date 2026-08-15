# Module 21A evidence review — Batch 168

Scope: the exact 25 supplied filtered-queue rows at ordinals 3651–3675, reviewed in the submitted order. The companion TSV is raw and uses exactly the required 13-column schema:

`review_id`, `pair`, `status`, `stable_citations`, `species`, `cell_type_model`, `assay_or_perturbation`, `relation_type`, `evidence_layer`, `pathway_branch`, `confidence`, `limitations`, `terminal_TF`

Exact reviewed rows, in request order:

```text
M20A-EXT-3427 Vegfa Itgb3
M20A-EXT-3429 Vegfa Ret
M20A-EXT-3430 Vegfa Sirpa
M20A-EXT-3431 Vegfa Tyro3
M20A-EXT-3432 Vegfb Adrb2
M20A-EXT-3433 Vegfb Flt1_Kdr
M20A-EXT-3435 Vegfb Ret
M20A-EXT-3436 Vegfc Ccbe1
M20A-EXT-3437 Vegfc Flt1
M20A-EXT-3438 Vegfc Itga9
M20A-EXT-3439 Vegfc Itgb1
M20A-EXT-3440 Vegfc Lyve1
M20A-EXT-3442 Vegfc Vipr2
M20A-EXT-3443 Vgf Ntrk1
M20A-EXT-3446 Vip Adrb1
M20A-EXT-3447 Vip Adrb2
M20A-EXT-3448 Vip Adrb3
M20A-EXT-3449 Vip Avpr1a
M20A-EXT-3450 Vip Dpp4
M20A-EXT-3451 Vip Gpr20
M20A-EXT-3452 Vip Gpr84
M20A-EXT-3453 Vip Npr3
M20A-EXT-3454 Vip Pth1r
M20A-EXT-3455 Vip Ramp1
M20A-EXT-3456 Vip Ramp2
```

## Disposition

- `reviewed_relay_candidate`: 3 — Vegfa–Itgb3, Vegfc–Itga9, Vegfc–Itgb1.
- `reviewed_function_only`: 5 — Vegfa–Ret, Vegfc–Ccbe1, Vip–Adrb1, Vip–Adrb2, Vip–Dpp4.
- `reviewed_unresolved`: 5 — Vegfa–Tyro3, Vegfb–Flt1_Kdr, Vegfc–Flt1, Vegfc–Lyve1, Vgf–Ntrk1.
- `no_evidence_boundary`: 12 — the remaining exact rows.
- Exactly 25 data rows are present, with unique review IDs and exact submitted pair labels.
- Every row has populated limitations, and every `terminal_TF` is literal `null`; no pair-specific terminal TF activation experiment was established.

## Evidence-layer rules applied

Binding/activation, receptor-proximal relay, and downstream pathway/function were recorded as separate layers. Computational communication scores, co-expression, marker expression, receptor-family similarity, pathway membership, and reverse-direction relationships were not promoted to direct exact-pair interactions.

- **Direct binding/activation and relay:** VEGFA165 binding to the alphaVbeta3 heterodimer supports the queued ITGB3 subunit as part of a direct integrin interaction, with VEGFR2/FAK/ERK crosstalk retained as a separate relay/function layer. VEGFC directly binds alpha9beta1 and produces integrin-dependent Erk1/2 and paxillin responses; the queued ITGA9 and ITGB1 rows therefore retain the heterodimer caveat.
- **Processing/function rather than receptor relay:** CCBE1 is required with ADAMTS3 for VEGFC proteolytic activation and lymphangiogenesis, but the evidence is a ligand-maturation/processing context, not a CCBE1 receptor relay. DPP4 cleaves/truncates VIP in enzymatic studies and DPP4 inhibition preserves VIP-associated lung-graft function; this is enzyme/substrate processing, not VIP-DPP4 receptor signaling.
- **Indirect crosstalk only:** VEGFA–RET is retained only as VEGFA-associated VEGFR2/RET crosstalk in a myxoid-liposarcoma model. VIP–ADRB1 and VIP–ADRB2 retain adrenal catecholamine/antagonist context, while the primary binding result did not show VIP binding to beta-adrenergic receptors.
- **No direct exact-pair evidence:** VEGFA–SIRPA, VEGFB–ADRB2, VEGFB–RET, VEGFC–VIPR2, and the unrelated VIP receptor/enzyme-modifier rows retain explicit no-evidence boundaries. VEGFB–FLT1_KDR is not promoted because the primary evidence supports VEGFB–FLT1, not the submitted composite receptor notation. VGF–NTRK1 is reverse-direction evidence: NTRK1/NGF signaling changes VGF abundance, not VGF activation of NTRK1. VEGFC–LYVE1 studies use LYVE1 as a lymphatic marker or report LYVE1-associated tissue changes while assigning VEGFC signaling to VEGFR3.

## Main limitations and unresolved boundaries

- Integrin rows are heterodimer-specific. Evidence for alphaVbeta3 or alpha9beta1 cannot be reduced to ITGB3, ITGA9, or ITGB1 alone, and VEGFA isoform/domain and mature VEGFC form matter.
- VEGFB–Flt1_Kdr preserves the exact composite queue notation but records only the supported FLT1/VEGFR1 component. KDR/VEGFR2 was not silently added to or removed from the submitted pair.
- VEGFC–Ccbe1 is an extracellular maturation complex involving ADAMTS3; CCBE1 is not treated as the VEGFC signaling receptor, and ADAMTS3 cleavage of VEGFC is not reversed into direct VEGFC–CCBE1 binding.
- The RET, TYRO3, SIRPA, LYVE1, and VIP-related comparator studies do not establish the queued ligand–protein edge. Function, pathway proximity, or shared cell context was retained only as a limitation or boundary.
- No SCI-specific receiver-cell weighting or terminal TF assignment was supported by the bounded primary-source review.

## Representative primary-source anchors

- VEGFA165/alphaVbeta3 direct binding and VEGFR2/KDR domain work: [PMID 38803393](https://pubmed.ncbi.nlm.nih.gov/38803393/), [DOI 10.3389/fcell.2024.1347616](https://doi.org/10.3389/fcell.2024.1347616), [PMCID PMC514852](https://pmc.ncbi.nlm.nih.gov/articles/PMC514852/).
- VEGFA-associated RET/VEGFR2 crosstalk: [PMID 20522586](https://pubmed.ncbi.nlm.nih.gov/20522586/), [DOI 10.1158/1078-0432.CCR-09-2912](https://doi.org/10.1158/1078-0432.CCR-09-2912).
- VEGFB–FLT1 specificity: [PMID 9751730](https://pubmed.ncbi.nlm.nih.gov/9751730/).
- VEGFC maturation by CCBE1/ADAMTS3: [PMID 27159393](https://pubmed.ncbi.nlm.nih.gov/27159393/), [DOI 10.1172/JCI83967](https://doi.org/10.1172/JCI83967).
- VEGFC–alpha9beta1 direct binding and integrin-dependent signaling: [PMID 15590642](https://pubmed.ncbi.nlm.nih.gov/15590642/), [PMCID PMC1368959](https://pmc.ncbi.nlm.nih.gov/articles/PMC1368959/), [DOI 10.1074/jbc.M412816200](https://doi.org/10.1074/jbc.M412816200).
- VIP receptor specificity and beta-adrenergic comparator: [PMID 7988457](https://pubmed.ncbi.nlm.nih.gov/7988457/), [PMID 10194528](https://pubmed.ncbi.nlm.nih.gov/10194528/), [PMID 6118184](https://pubmed.ncbi.nlm.nih.gov/6118184/).
- VIP processing by DPP4/CD26: [DOI 10.1016/S0014-5793(01)02982-9](https://doi.org/10.1016/S0014-5793(01)02982-9), [PMID 20018218](https://pubmed.ncbi.nlm.nih.gov/20018218/).
- Reverse NTRK1-to-VGF evidence: [PMID 34771457](https://pubmed.ncbi.nlm.nih.gov/34771457/), [PMCID PMC8582546](https://pmc.ncbi.nlm.nih.gov/articles/PMC8582546/).

No Module20A file, shared register, integrated register, or other shared artifact was modified. No commit was made.
