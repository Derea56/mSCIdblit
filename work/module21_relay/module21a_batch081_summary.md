# Module 21A batch 081 review summary

## Scope

Reviewed the exact filtered priority-8 queue ordinal slice 1326–1350 from `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`. The slice contains 25 rows with review IDs 1460, 1462–1469, 1471–1478, and 1480–1487. The missing IDs 1461, 1470, and 1479 are not present in this exact filtered slice.

The review searched PubMed, PMC, publisher pages, and targeted stable PubMed query URLs for NRG4–ERBB4, neurexin–calsyntenin, neurexin–dystroglycan, neurexin–LRRTM, neurexin–neuroligin, and OCLN self-association evidence. Primary research was prioritized. Family-level, gene-level, or pathway annotations were not promoted to exact molecular edges when the neurexin promoter, splice state, receptor partner, or calsyntenin isoform was unresolved.

## Disposition

- 25 exact queue rows reviewed.
- 1 `reviewed_relay_candidate`: NRG4–ERBB4.
- 17 `reviewed_binding_only`: exact or isoform-bounded synaptic adhesion/self-association evidence without a demonstrated intracellular receptor relay.
- 7 `reviewed_unresolved`: NRXN1–CLSTN1, NRXN1–CLSTN2, NRXN2–CLSTN1, NRXN2–CLSTN2, NRXN2–DAG1, NRXN2–LRRTM4, and NRXN3–LRRTM4.

No terminal TFs were assigned. Synaptic adhesion, homophilic junction assembly, synapse number, AMPAR surface expression, and barrier readouts were retained as cellular functions only; none were converted into a direct TF or receptor-proximal kinase claim.

## Evidence boundaries

- NRG4–ERBB4 has direct ligand/receptor activation and downstream PI3K–AKT and neuronal growth/survival evidence, but the neuronal studies do not resolve every ERBB4 branch.
- NRXN1/2/3–CLSTN3 is supported by direct, calcium- and splice-sensitive adhesion work, but the literature contains discrepant CLSTN3 binding results and the queue rows do not specify alpha/beta promoter or splice state.
- NRXN1–DAG1 is supported primarily for glycosylated alpha-dystroglycan with NRXN1alpha; evidence for NRXN2–DAG1 was not found and was not inferred from NRXN1 or NRXN3 studies.
- NRXN1/2/3–LRRTM1 and –LRRTM2 have strong splice-coded binding evidence; LRRTM3 and LRRTM4 are more dependent on exact neurexin splice/HS states, so unresolved cases remain explicit.
- NRXN3–NLGN1/2/3 have direct beta-neurexin/neuroligin binding evidence, but alpha/beta and splice states are not represented in the queue row.
- OCLN self-association is direct homophilic cis/trans oligomerization with tight-junction barrier output, not a canonical receptor relay.

## Files changed

- `work/module21_relay/module21a_batch081_review.tsv`
- `work/module21_relay/module21a_batch081_summary.md`

No shared Module 21A registers, Module 20A ledgers, frozen manifest, or integration outputs were modified.
