# Module 21A batch 107 review

Batch 107 covers the exact filtered priority-8 queue ordinal slice 1976–2000. All 25 requested review IDs are present exactly once and match the queue pair labels: `M20A-EXT-1095` through `M20A-EXT-1143` with the queue’s intervening ID gaps preserved.

## Disposition

- 6 `reviewed_relay_candidate`: CD14–TLR1, CD14–TLR4, CD14–TLR6, CD14–TLR9, CD40LG–TRAF3, and CDH1–EGFR.
- 1 `reviewed_function_only`: CD14–RIPK1.
- 1 `reviewed_binding_only`: CD200–CD200R4.
- 17 `reviewed_unresolved`.
- 0 terminal TF assignments.

## Evidence notes

- CD14/TLR rows were kept as receptor-complex or accessory-cofactor relays. CD14 has no cytosolic signaling domain; TLR1 and TLR6 require their partner-receptor context, TLR4 requires MD-2, and TLR9 is endosomal. No CD14–integrin edge was inferred from monocyte adhesion or TLR-associated integrin activation.
- CD14–RIPK1 was retained only as a functional association from the primary FasL/CD14 study. RIPK1 is part of a Fas/TRIF-containing death-complex boundary; the study does not demonstrate direct CD14–RIPK1 binding.
- CD200–CD200R4 was retained at binding-only because early murine CD200R-family studies reported physical interaction with R4, but R4-specific intracellular signaling was not isolated. CD200R1 pathway evidence was not transferred to R4.
- CCL5–CCRL2 was held unresolved because early CCL5/CCRL2 reports were not independently confirmed; chemerin is the accepted CCRL2 ligand. CCL5–CXCR3 was held unresolved because primary receptor comparisons assign CCL5 to CCR1/CCR5 and CXCR3 to CXCL9/10/11.
- CCL5–DPP4 was not promoted to a signaling edge. DPP4/CD26 is a processing enzyme that generates N-terminally truncated CCL5 variants with altered receptor selectivity; it is a source/processing context label rather than a receptor relay.
- CD40LG–TRAF3 was kept as a ligand-to-adaptor relay only through the required CD40 receptor node. CD40LG–CD53 and CD40LG–CD9 were not inferred from tetraspanin expression or CD9-stratified CD40L responses.
- CD59B–CD2, CD59B–STAB1, CD5L–CD5, CD70–TNFRSF13B, and CD70–TNFRSF17 remain unresolved. The closest evidence supports CD59 cross-linking, CD5L–CD36, CD70–CD27, and BAFF/APRIL–TACI/BCMA branches, respectively, not the submitted exact pairs.
- CDH1–EGFR has direct complex and receptor-proximal evidence, but the direction of EGFR modulation is context-dependent: adhesion, force, EGF availability, and trafficking determine whether E-cadherin restrains, permits, or promotes EGFR signaling. No terminal TF was assigned.

## Search boundary

Searches covered PubMed, PMC full text, publisher pages, Reactome boundary annotations, and exact-pair queries for all 25 IDs. Primary research was preferred. For unresolved rows, the TSV records the closest cognate-receptor, paralog, processing, or pathway evidence and explicitly states why it does not support the exact pair. No pathway-level or functional observation was converted into a direct molecular interaction, and no terminal TF was inferred without exact pathway evidence.

## Files changed

- `work/module21_relay/module21a_batch107_review.tsv`
- `work/module21_relay/module21a_batch107_summary.md`

Shared Module 21A registers, Module 20A LR ledgers, the frozen manifest, and integration outputs were not modified.
