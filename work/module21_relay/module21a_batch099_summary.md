# Module 21A batch 099 review summary

Reviewed the exact filtered priority-8 queue ordinals 1776–1800, corresponding to 25 review IDs `M20A-EXT-0875` through `M20A-EXT-0902` with the documented ordinal gaps.

## Disposition

- 5 `reviewed_relay_candidate`: ARF1–CHRM3, ARF1–INSR, ARF1–PLD2, ARF6–PLD1, ARF6–SMAP1.
- 2 `reviewed_binding_only`: APP–VLDLR and ARTN–GFRA2.
- The APP/TSPAN processing boundary was not promoted beyond function-only; ARTN–GFRA2 remains at the binding layer because its exact receptor-complex relay is not sufficiently isolated.
- 1 `reviewed_function_only`: APP–TSPAN12.
- 16 `reviewed_unresolved`: APP–RPSA, APP–TSPAN15, AREG–ERBB3, ARPC5–ADRB2/LDLR/LRP2, AVP–ADCYAP1R1/ADRB2/ADRB3/GPR20/GPR84/LDLR/LRP2/PTH1R/RAMP2/RAMP3.
- 1 `reviewed_relay_candidate`: AVP–OXTR, supported as noncanonical receptor crosstalk in a defined mouse preoptic circuit.
- 0 terminal TF assignments. Generic vasopressin, adrenergic, APP-processing, and intracellular trafficking pathways were not used to infer TF endpoints.

The TSV therefore contains 6 relay candidates, 1 function-only record, 2 binding-only records, and 16 unresolved records. ARTN–GFRA2 is intentionally kept at the binding layer because GFRα3 is the preferred ARTN coreceptor and the exact GFRα2 cross-reactive receptor-complex relay is not sufficiently isolated. APP–VLDLR is an adaptor-mediated receptor-complex/trafficking association, not a soluble ligand-receptor activation claim.

## Search boundaries and limitations

- APP-related searches covered PubMed, PMC, and publisher records for APP–RPSA, APP–TSPAN12, APP–TSPAN15, and APP–VLDLR. Strong evidence was found for TSPAN12/ADAM10-dependent APP shedding and FE65-linked APP–VLDLR association. TSPAN15 regulates ADAM10 and other substrates, but the primary knockout study reported unchanged APP alpha-secretase cleavage, so the exact APP–TSPAN15 edge remains unresolved.
- AREG–ERBB3 searches found AREG/EGFR and NRG1/ERBB3 evidence, but no exact AREG–ERBB3 binding or activation assay.
- ARF1/6 searches found direct intracellular relay evidence for PLD1/PLD2, CHRM3-to-ARF/PLD, INSR-to-ARF/PLD, and SMAP1 Arf6-GAP activity. These are intracellular trafficking/signaling edges and are not treated as extracellular ligand-receptor pairs.
- ARPC5 searches found generic ARP2/3/clathrin/endocytic pathway evidence, but no exact ARPC5 association with ADRB2, LDLR, or LRP2.
- ARTN–GFRA2 searches found lower-preference/cross-reactive GDNF-family binding evidence, with ARTN–GFRα3 remaining the preferred complex. No terminal TF was inferred.
- AVP searches covered PubMed, PMC, and publisher sources for each exact receptor/composition. Only AVP–OXTR had an exact primary functional/circuit report in this pass. ADCYAP1R1, ADRB2, ADRB3, GPR20, GPR84, LDLR, LRP2, PTH1R, RAMP2, and RAMP3 were retained as no-evidence boundaries. RAMP2/3 were treated as accessory components of CLR-based adrenomedullin complexes, not as standalone AVP receptors.

No shared Module 21A registers, Module 20A ledgers, frozen manifest, or integration outputs were modified.

