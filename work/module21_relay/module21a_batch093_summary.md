# Module 21A batch 093 review summary

## Scope

This isolated batch covers exactly the filtered priority-8 queue ordinal rows 1626–1650 from `module20a_external_review_queue.tsv`. The explicit review IDs are:

`M20A-EXT-0644`–`M20A-EXT-0652`, `M20A-EXT-0654`–`M20A-EXT-0661`, `M20A-EXT-0663`–`M20A-EXT-0665`, `M20A-EXT-0667`, `M20A-EXT-0669`, and `M20A-EXT-0671`–`M20A-EXT-0673`.

The omitted IDs in this ordinal interval were not backfilled. The batch contains 25 exact review rows and preserves the queue’s exact ADAM10/11/12/15/17/2/23 and TSPAN/integrin boundaries.

## Disposition

- 15 `reviewed_relay_candidate`
- 8 `reviewed_binding_only`
- 2 `reviewed_unresolved`
- 0 `reviewed_function_only`
- 0 terminal TF assignments

## Additions

- ADAM10 was supported as a direct complex partner of TSPAN10, TSPAN14, TSPAN15, TSPAN17 and TSPAN5 through the TspanC8/ADAM10 trafficking and sheddase literature. TSPAN12 was retained separately because it has direct co-immunoprecipitation and ADAM10-dependent APP-shedding evidence but is not interchangeable with the canonical TspanC8 subgroup.
- ADAM12–ITGA9 and ADAM12–ITGB1 were retained as alpha9beta1 complex-level adhesion/spreading edges, with PI3K-linked spreading evidence kept separate from the direct binding claim.
- ADAM15–ITGA5/ITGB1 retained both the reported integrin-recognition context and the distinct ERK-dependent adhesion/motility modulation evidence; the CHO study’s failure to detect direct co-immunoprecipitation was recorded as a limitation.
- ADAM17–ERBB4, –IL6RA, –ITGA5, –MET and –RHBDF2 were retained as receptor-processing, integrin-complex, or sheddase-cofactor relay edges. These are not treated as conventional soluble ligand–receptor binding events.
- ADAM2–ITGA6/ITGB1 and ADAM23–ITGA4/ITGB3 were retained as defined integrin-complex adhesion edges, not isolated-subunit molecular interactions.

## Unresolved cases

- `M20A-EXT-0664` ADAM17–NOTCH1 remains unresolved. Canonical ligand-dependent mammalian NOTCH1 processing is ADAM10-dominant in the cited knockout/reconstitution work; ADAM17 evidence is context-specific and includes Jagged1 shedding, which cannot be transferred to the NOTCH1 receptor.
- `M20A-EXT-0672` ADAM23–ITGA5 remains unresolved. Primary evidence in the searched boundary supports ADAM23–alpha4 and ADAM23–alphaVbeta3 adhesion, not ITGA5.

## Search boundary and limitations

Searches covered PubMed, PMC, and publisher pages for exact gene/subunit combinations and relevant primary assays, including co-immunoprecipitation, recombinant disintegrin-domain binding, defined-integrin adhesion panels, cleavage/shedding assays, knockout or inhibitor perturbations, and cell migration/fusion outputs. Pathway-level reviews were used only to locate or corroborate primary studies; direct molecular claims were retained only where the cited assay supported the exact protein or defined receptor complex. No terminal TF was promoted because this batch did not provide exact pair-specific direct TF-occupancy evidence.

## Files

- `module21a_batch093_review.tsv`
- `module21a_batch093_summary.md`

No shared Module 21A registers, Module 20A ledgers, frozen manifest, or integration outputs were modified.
