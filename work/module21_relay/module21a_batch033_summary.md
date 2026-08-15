# Module 21A batch 033 review summary

Batch 033 reviewed the 25 exact frozen Module20A queue IDs `M20A-CELLCHAT-REMAINING-0126` through `M20A-CELLCHAT-REMAINING-0150` without modifying shared Module21A registers, Module20A ledgers, or the frozen manifest.

## Queue verification

All 25 requested IDs were present exactly once in `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`. The frozen queue differs from the prose grouping in the request: IDs 0138–0141 are `Activin Ab` receptor-complex rows, while `Adm` begins at IDs 0142–0147. The TSV follows the frozen queue labels and does not substitute ADM for Activin AB.

## Classification

- 17 `reviewed_relay_candidate`
- 6 `reviewed_unresolved` exact ADM–CALCR/RAMP rows
- 2 Activin AB receptor-complex relay candidates were supported at pathway level with direct Activin AB-induced SMAD2 phosphorylation, but receptor-subtype isolation was limited.
- No terminal TF was assigned for acetylcholine, ADM, or adenosine rows. Activin AB rows retain `SMAD2` only because direct Activin AB stimulation and SMAD2 phosphorylation were measured; the exact receptor combination was not isolated.

## Evidence boundaries

Acetylcholine receptor activation was supported separately from CHAT/SLC5A7/SLC18A3 handling. Muscarinic M1/M3/M5 branches were kept distinct from M2/M4 Gi/o branches, and nicotinic ligand-gated channel activation was kept distinct from downstream CaMKII/PLC/IP3R or neuromuscular function.

ADM evidence strongly supported `CALCRL/CLR–RAMP2` and `CALCRL/CLR–RAMP3`, with lower/context-dependent support for `CALCRL/CLR–RAMP1`. Exact `CALCR–RAMP1/2/3` edges were left unresolved because the primary reconstitution evidence centered on CALCRL/CLR and did not establish those exact complexes.

ADO receptor relay was supported for ADORA1, ADORA2A, and ADORA2B, while NT5E/SLC29A1 metabolism/transport was not treated as receptor activation. Analog agonist studies were retained with explicit limitations.

Primary search boundaries included exact pair aliases, PubMed, PMC, publisher pages, Reactome pathway context, recombinant receptor assays, receptor-complex studies, pharmacology, and downstream perturbation studies. Database/pathway membership was not used alone to promote an exact molecular edge.
