# Module 21A batch 165 review summary

## Scope

This bounded review covers exactly the 25 requested queue rows, review IDs `M20A-EXT-3333` through `M20A-EXT-3358` with the explicitly listed gaps at `3336`, and no other queue rows. The pair labels were treated literally as submitted; enzyme, adaptor, decoy, metabolite-source, and receptor-family relationships were not silently normalized into ligand-receptor edges.

Exact reviewed IDs, in request order:

```text
M20A-EXT-3333 Tnfsf12 Cd163
M20A-EXT-3334 Tnfsf12 Tnfrsf25
M20A-EXT-3335 Tnfsf12 Tnfrsf8
M20A-EXT-3337 Tnfsf13 Sdc2
M20A-EXT-3338 Tnfsf13 Tnfrsf11b
M20A-EXT-3339 Tnfsf13 Tnfrsf14
M20A-EXT-3340 Tnfsf13 Tnfrsf1a
M20A-EXT-3341 Tnfsf13b Cd40
M20A-EXT-3342 Tnfsf13b Tfrc
M20A-EXT-3343 Tnfsf4 Traf2
M20A-EXT-3344 Tph1 Htr1a
M20A-EXT-3345 Tph1 Htr1b
M20A-EXT-3346 Tph1 Htr1d
M20A-EXT-3347 Tph1 Htr1f
M20A-EXT-3348 Tph1 Htr2a
M20A-EXT-3349 Tph1 Htr2b
M20A-EXT-3350 Tph1 Htr2c
M20A-EXT-3351 Tph1 Htr4
M20A-EXT-3352 Tph1 Htr5a
M20A-EXT-3353 Tph1 Htr6
M20A-EXT-3354 Tph1 Htr7
M20A-EXT-3355 Tpsb2 F2rl1
M20A-EXT-3356 Trf Adrb2
M20A-EXT-3357 Trf Hfe
M20A-EXT-3358 Trf Ldlr
```

## Disposition

- `reviewed_relay_candidate`: 1 (`Tpsb2-F2rl1`)
- `reviewed_binding_only`: 1 (`Tnfsf13-Sdc2`)
- `reviewed_scavenging_only`: 1 (`Tnfsf12-Cd163`)
- `reviewed_unresolved`: 13 (`Tnfsf12-Tnfrsf25`, `Tph1-Htr1a/Htr1b/Htr1d/Htr1f/Htr2a/Htr2b/Htr2c/Htr4/Htr5a/Htr6/Htr7`, and `Trf-Hfe`)
- `no_evidence_boundary`: 9
- Terminal TF assignments: 1 (`BCL6` for the Tpsb2-F2rl1 relay); all other rows use `terminal_TF=null`.

## Evidence-layer findings

1. **TWEAK/Tnfsf12-Cd163:** primary studies support direct TWEAK binding to CD163 and CD163-mediated sequestration/decoy activity. Mouse ischemic-limb experiments separately show TWEAK/Fn14-associated canonical NF-kB and Notch outputs modulated by CD163 loss. This is scavenging/ligand-availability evidence plus separate downstream function, not a CD163-proximal signaling relay.
2. **TWEAK/Tnfsf12-Tnfrsf25:** an early APO3L/TWEAK paper reported DR3 binding, but later primary binding and DR3-knockout work did not confirm the interaction. The validated ligand for DR3 is TL1A/TNFSF15, while TWEAK signaling is assigned to Fn14/TNFRSF12A. The row remains unresolved with the historical conflict documented.
3. **APRIL/Tnfsf13-Sdc2:** APRIL binding to heparan-sulfate-rich proteoglycan/syndecan contexts is supported, but the primary work does not isolate an SDC2 core-protein epitope or couple APRIL-SDC2 binding to a downstream relay. A separate SDC2-TACI study was not transferred into direct APRIL-SDC2 relay evidence.
4. **Tpsb2/F2rl1:** recombinant mouse mMCP-6/Tpsb2 and mast-cell experiments support PAR2-dependent signaling in CD4 T cells, with PAR2 knockdown and p38/ERK inhibition reducing the BCL6 response. Older tryptase studies support proteolytic PAR2 activation at the tryptase-family level. The row is relay-supported but remains limited by isoform, native-substrate, heparin, and non-SCI context.
5. **Tph1-Htr1a/Htr1b/Htr1d/Htr1f/Htr2a/Htr2b/Htr2c/Htr4/Htr5a/Htr6/Htr7:** TPH1 is the serotonin-biosynthetic enzyme; serotonin, not TPH1 protein, is the receptor agonist. Receptor-specific 5-HT pharmacology and pathway/function studies are retained as metabolite-level comparators only. No row infers a direct TPH1-receptor interaction or source-enzyme-to-receptor relay.
6. **Adaptor and receptor-complex boundaries:** TNFSF4/OX40L evidence terminates at OX40/TNFRSF4 before TRAF2 recruitment; BAFF evidence terminates at BAFF-R/TACI/BCMA rather than CD40 or TFRC; transferrin/HFE evidence concerns competition through TfR1, not direct Trf-Hfe binding. These distinctions are recorded as limitations rather than promoted edges.

## Search and citation boundaries

The TSV uses stable PMIDs, PMCIDs, DOIs, and bounded PubMed exact-pair query URLs. Primary studies were prioritized for direct binding, receptor-specific perturbation, reconstitution, knockout, and pathway readouts. Family-level, expression-only, database, pathway, nomenclature-collision, and noncognate-receptor findings were retained only as explicit limitations or comparator boundaries.

No pathway/function result was used to infer direct interaction. No terminal TF was assigned without a measured, pair-relevant transcription-factor endpoint; the sole assignment is BCL6 in the mMCP-6/PAR2 mouse T-cell experiment.

## Validation and file scope

- Exactly 25 data rows plus the requested 13-column header.
- Review IDs and pair labels are unique and match the supplied request order.
- Every row has populated limitations and a stable citation field.
- `terminal_TF=null` is used wherever no TF is assigned.
- Module 20A files, shared Module 21A registers, integration outputs, and database tables were not modified.
- No commit was created.

## Files written

- `work/module21_relay/module21a_batch165_review.tsv`
- `work/module21_relay/module21a_batch165_summary.md`
