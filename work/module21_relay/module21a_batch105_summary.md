# Module 21A batch 105 review

Batch 105 covers the exact filtered priority-8 queue ordinal slice 1926–1950, review IDs `M20A-EXT-1036` through `M20A-EXT-1068` as represented in the filtered queue. All 25 requested review IDs are present exactly once and match the queue pair labels.

## Disposition

- 3 `reviewed_relay_candidate`: CAMP–EGFR, CAMP–FPR2, and CAMP–P2RX7.
- 22 `reviewed_unresolved`.
- 0 `reviewed_binding_only`.
- 0 `reviewed_function_only`.
- 0 terminal TF assignments.

## Evidence notes

- Cathelicidin evidence was kept receptor-specific. LL-37/CRAMP supported EGFR-proximal, FPR2-dependent, and P2X7 channel-modulation branches in defined cell or animal models.
- The LL-37–IGF1R paper was found but is retracted. Its binding, receptor-phosphorylation, and ERK claims were retained only as an audit boundary and were not promoted.
- CALR–SCARF1 was not promoted: SCARF1 scavenger biology involves apoptotic-cell/C1q recognition, and the reviewed study reported negligible direct SCARF1 binding to calreticulin.
- Chemokine rows were held at unresolved when evidence supported a different cognate subtype, a different atypical receptor, or a processing/scavenging context rather than the exact submitted pair. CCL20–CCR6, CCL21–CCR7, CCL2–CCR2/ACKR1/ACKR2, and CCL11–CCR3 evidence were not transferred to the submitted non-cognate receptor rows.
- DPP4 was treated as a protease/processing candidate, not as a receptor. CCL11–DPP4 was not promoted without an exact primary processing assay.

## Search boundary

Searches covered PubMed, PMC full text, publisher pages, and IUPHAR/Guide to Pharmacology boundary annotations. Primary evidence was preferred. For unresolved rows, the TSV records the closest cognate-receptor or scavenger/processing evidence and explicitly states why it does not support the exact pair. No pathway-level or functional observation was converted into a direct molecular edge, and no terminal TF was inferred.

## Files changed

- `work/module21_relay/module21a_batch105_review.tsv`
- `work/module21_relay/module21a_batch105_summary.md`

Shared Module 21A registers, Module 20A LR ledgers, the frozen manifest, and integration outputs were not modified.
