# Module 21A batch 090 review

## Scope

Reviewed the exact filtered priority-8 queue ordinal rows 1551–1575 from `module20a_external_review_queue.tsv`, corresponding to review IDs `M20A-CELLCHAT-REMAINING-1698` through `M20A-CELLCHAT-REMAINING-1723` (25 explicit IDs; the queue slice intentionally skips `-1710`). One row was written for every requested review ID.

The review searched PubMed, PMC, publisher full text, and stable NCBI records. Primary research was used for SLURP-2 pharmacology (PMID 27485575), thyroid-receptor transcription (PMIDs 21292823, 16794015, 2608064, 16581794), TAFA4/FAM19A4–FPR1 (PMID 25109685), and teneurin–latrophilin/FLRT complexes (PMIDs 21724987, 24273166, 30792275, 31928845, 32358586). TAX1BP3–ADGRB1/2 remained a bounded no-evidence search because TAX1BP3 is a cytosolic scaffold and no exact extracellular ligand assay was located.

## Disposition

- `reviewed_relay_candidate`: 5
  - SLURP2–CHRNA7 and SLURP2–CHRNB2: exact complex-level nicotinic-channel modulation; no isolated-subunit claim.
  - T3-DIO3–THRA and T3-DIO3–THRB: direct T3 nuclear-receptor transcription with DIO3 retained as a local deiodinase context, not a receptor chain; terminal TFs are THRA and THRB respectively.
  - TAFA4/FAM19A4–FPR1: direct binding plus FPR1-dependent macrophage migration, phagocytosis and ROS output.
- `reviewed_function_only`: 3
  - TENM2–ADGRL1/2/3: direct teneurin–latrophilin adhesion with synapse, target-recognition or guidance outputs; no intracellular kinase/TF relay was inferred.
- `reviewed_binding_only`: 1
  - SLURP2–CHRNB4: affinity association with beta4-containing cortical nAChR material without a defined functional complex assay.
- `reviewed_unresolved`: 16
  - SLURP2–CHRNA6/9, CHRNB1/3, CHRND/E/G: exact subunit or functional complex not established.
  - TAX1BP3–ADGRB1/2: invalid extracellular LR interpretation; no exact ligand assay.
  - TENM1–ADGRL1/2/3 and TENM3–ADGRL1: exact paralog-pair evidence not located.
  - TENM2_FLRT1/3–ADGRL1/2 composites: pairwise and ternary-family evidence exists, but exact submitted cofactor/stoichiometric boundaries were not resolved.

## Audit notes

- Channel evidence remains complex-level: CHRNA7 is supported as a homomeric receptor and CHRNB2 as part of tested alpha3beta2/alpha4beta2 receptors; no beta1/beta3/delta/epsilon/gamma relay was transferred.
- T3-DIO3 rows do not claim physical DIO3–THRA/THRB interaction. DIO3 is a T3-inactivating enzyme/context label, while THRA/THRB are ligand-activated transcription factors.
- Teneurin/latrophilin evidence is retained as adhesion, synapse-specification or guidance evidence. It is not converted into a direct intracellular pathway or terminal TF assignment.
- No shared Module 21A registers, Module 20A LR ledgers, frozen manifest, or integration outputs were modified.

## Output

- `work/module21_relay/module21a_batch090_review.tsv`
- `work/module21_relay/module21a_batch090_summary.md`
