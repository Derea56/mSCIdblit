# Module 21A batch 068 review

Reviewed the exact filtered priority-8 queue rows 1001–1025 from `module20a_external_review_queue.tsv`, corresponding to review IDs `M20A-CELLCHAT-REMAINING-1093` through `M20A-CELLCHAT-REMAINING-1117`.

## Results

- 25/25 queue rows reviewed with one TSV row per queue ID.
- 23 `reviewed_relay_candidate` rows: exact NMDA, mGlu, AMPA, and kainate receptor-complex activation/coupling evidence.
- 2 `reviewed_unresolved` rows: exact GRIK3/GRIK4 and GRIK3/GRIK5 complex activation remains unresolved.
- 0 `reviewed_function_only` rows.
- 0 `reviewed_binding_only` rows.
- 0 terminal TF assignments.
- SLC1A6, SLC1A7, GLS, and GLS2 were retained as glutamate-source context only; no direct molecular edge was inferred from transporter or glutaminase labels.

## Search and evidence boundaries

Primary PubMed records and linked PMC/publisher records were searched for recombinant receptor activation, heteromeric complex composition, patch-clamp/electrophysiology, agonist-site perturbation, and mGlu receptor/G-protein coupling. Representative sources include NMDA receptor subtype electrophysiology (PMID 9463421; PMCID PMC2614009 / PMID 18635641; PMID 9625862), kainate receptor subunit composition and gating (PMID 20026616; PMID 25139762; PMID 23975096), and mGlu receptor G-protein specificity (PMID 25193666). Group-III mGlu receptor/cAMP function was additionally bounded by the primary microglial study PMID 12657674.

For GRIK3/GRIK4 and GRIK3/GRIK5, cited studies establish ligand-binding/assembly context and comparator GluK1/2 heteromers, but do not isolate the exact GluK3-containing heteromer in a receptor-specific functional assay. These rows therefore remain unresolved rather than being promoted to receptor-proximal relay candidates.

No exact receptor-context evidence was found in this batch that supports a downstream pathway-to-TF assignment. The TSV therefore stops at the receptor-proximal relay layer and records the limitation explicitly for every promoted row.

## Files written

- `work/module21_relay/module21a_batch068_review.tsv`
- `work/module21_relay/module21a_batch068_summary.md`

Shared Module 21A registers, integration outputs, Module 20A ledgers, and the frozen Module 20A LR manifest were not modified.
