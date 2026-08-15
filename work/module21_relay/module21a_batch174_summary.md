# Module 21A batch 174 review summary

## Scope

This bounded review covers exactly the 25 supplied LIANA queue rows at
filtered-queue ordinals `3801-3825`, in the supplied order. The raw TSV uses
the exact requested 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

Exact reviewed rows:

```text
M20A-LIANA-REMAINING-0072 Dll1 Notch2
M20A-LIANA-REMAINING-0073 Dll1 Notch3
M20A-LIANA-REMAINING-0074 Dll4 Notch1
M20A-LIANA-REMAINING-0075 Dll4 Notch2
M20A-LIANA-REMAINING-0076 Edil3 Itgav
M20A-LIANA-REMAINING-0077 Edil3 Itgb3
M20A-LIANA-REMAINING-0078 Efna2 Epha2
M20A-LIANA-REMAINING-0079 Efna2 Epha3
M20A-LIANA-REMAINING-0080 Efna2 Epha4
M20A-LIANA-REMAINING-0081 Efna2 Epha5
M20A-LIANA-REMAINING-0082 Efna2 Epha6
M20A-LIANA-REMAINING-0083 Efna2 Epha7
M20A-LIANA-REMAINING-0084 Efna2 Epha8
M20A-LIANA-REMAINING-0085 Efna3 Epha4
M20A-LIANA-REMAINING-0086 Efna3 Epha5
M20A-LIANA-REMAINING-0087 Efna4 Epha3
M20A-LIANA-REMAINING-0088 Efna4 Epha4
M20A-LIANA-REMAINING-0089 Efna4 Epha5
M20A-LIANA-REMAINING-0090 Efna4 Epha6
M20A-LIANA-REMAINING-0091 Efna4 Epha7
M20A-LIANA-REMAINING-0092 Efna4 Epha8
M20A-LIANA-REMAINING-0093 Efna5 Epha4
M20A-LIANA-REMAINING-0094 Efna5 Epha5
M20A-LIANA-REMAINING-0095 Efna5 Epha8
M20A-LIANA-REMAINING-0096 Efnb1 Epha4
```

## Disposition

- `reviewed_relay_candidate`: 10 rows (`0072`, `0074-0077`, `0079`,
  `0085`, `0092`, `0093`, `0096`).
- `reviewed_binding_only`: 14 rows (`0078`, `0080-0084`, `0086-0091`,
  `0094-0095`).
- `no_evidence_boundary`: 1 row (`0073`, DLL1-NOTCH3).
- Terminal TF assignments: `HOXD3` for `Edil3 Itgav`, `RUNX2` for
  `Edil3 Itgb3`, and `HES1;HEY1` for `Dll4 Notch1`. The other 22 rows use
  `terminal_TF=null`.

## Evidence-layer decisions

1. **Notch.** Primary work supports DLL1-NOTCH2 binding/activation and DLL4
   activation of NOTCH1 and NOTCH2, with DLL4 preferentially activating
   NOTCH1. DLL4-NOTCH1 has direct structural/binding evidence, mechanical
   activation evidence, and endothelial HES1/HEY1 function. The mast-cell
   DLL1/DLL4 paper was used carefully because it distinguishes Notch-family
   adhesion from productive Notch signaling. No qualifying exact DLL1-NOTCH3
   primary assay was recovered; NOTCH3 expression in a comparator system was
   not promoted to evidence.

2. **EDIL3/integrins.** EDIL3/Del-1 evidence is recorded at the heterodimer
   level even though the queue labels are `Itgav` and `Itgb3`. The alphaV row
   retains the alphaVbeta5-initiated HoxD3 branch and the alphaVbeta3
   downstream angiogenesis boundary. The beta3 row retains direct
   alphaVbeta3 binding and the independent beta3-FAK-ERK1/2-RUNX2 osteogenic
   branch. Subunit labels were not treated as standalone receptor complexes.

3. **Ephrin-A/EphA.** The primary EphA-panel study supports direct binding of
   the submitted ephrin-A/EphA combinations, while additional primary studies
   resolve selected activation or function: EFNA2-EPHA3 reverse signaling,
   EFNA3-EPHA4 astrocytic reverse signaling, EFNA5-EPHA4 structural and
   cellular responses, and EFNA4-EPHA8 phosphorylation. Binding-only rows do
   not receive an inferred adaptor/kinase relay. Recombinant-positive versus
   endogenous-rat-striatal-negative results are retained as explicit
   limitations for EFNA2-EPHA4 and EFNA4-EPHA7.

4. **Cross-class exception.** EFNB1-EPHA4 is retained because primary mouse
   cortical work shows cell-based binding, native co-immunoprecipitation,
   EPHA4 phosphorylation, and cortical progenitor proliferation. This is a
   cross-class EphA/ephrin-B interaction and is not flattened into the
   canonical ephrin-A branch.

## Citation and limitation policy

Stable PMIDs, PMCIDs, DOIs, and bounded PubMed URLs are recorded in every TSV
row. Primary sources were prioritized for direct binding, receptor
phosphorylation, reconstitution, structural interaction, loss/gain of
function, or receptor-specific perturbation. Family-level promiscuity,
expression, pathway membership, reporter function without pair-specific
engagement, and comparator biology were retained only as limitations or
separate downstream layers. Every row has a populated `limitations` field.

Representative primary sources include [DLL1/DLL4 selectivity toward
NOTCH1/NOTCH2](https://pubmed.ncbi.nlm.nih.gov/30289388/), [structural DLL4-
NOTCH1 engagement](https://pubmed.ncbi.nlm.nih.gov/25700513/), [Del-1/EDIL3
integrin-dependent angiogenesis](https://pubmed.ncbi.nlm.nih.gov/12840057/),
[the EphA/ephrin binding panel](https://pubmed.ncbi.nlm.nih.gov/22568954/),
[EFNA3-EPHA4 astrocytic reverse signaling](https://pubmed.ncbi.nlm.nih.gov/25040798/),
and [EFNB1-EPHA4 cortical signaling](https://pubmed.ncbi.nlm.nih.gov/19542359/).

## Validation and write boundary

- Exactly 25 data rows plus the requested header are present.
- Review IDs and pair labels are unique and match the supplied request order.
- No embedded tabs or newlines were added to data fields.
- `terminal_TF=null` is used wherever no TF is assigned.
- Only the batch TSV and this batch summary were written. Module20A files,
  shared Module21A registers, frozen queues, handoff/integration outputs, and
  database tables were not modified.
- No commit was created.

## Files written

- [`module21a_batch174_review.tsv`](/Users/derea/Documents/SCI/mSCIdblit/work/module21_relay/module21a_batch174_review.tsv)
- [`module21a_batch174_summary.md`](/Users/derea/Documents/SCI/mSCIdblit/work/module21_relay/module21a_batch174_summary.md)
