# Module 21A batch 120 review

Batch 120 covers exactly the 25 requested rows `M20A-EXT-1772` through `M20A-EXT-1820`.

## Disposition

- 3 `reviewed_relay_candidate`: GDF15-RET, GDF9-BMPR2, and GHRH-GHSR.
- 2 `reviewed_binding_only`: GDF2-ACVR1 and GHRH-VIPR1.
- 2 `reviewed_function_only`: GDNF-EDNRB and GHRH-DPP4.
- 19 `reviewed_unresolved`: the remaining exact pairs, including GDF11 with BMPR1A/BMPR1B/BMPR2, GDF5-ACVR1, GDF9 with ACVR2A/BMPR1A/BMPR1B/FXYD6/ORAI2, GDNF-GFRA3, and the remaining GHRH receptor/accessory candidates.

## Evidence notes

The strongest receptor-complex relay is GDF15-GFRAL-RET. Primary studies establish high-affinity GDF15 binding to GFRAL and require RET as the signaling coreceptor; the row therefore preserves the GFRAL-RET complex and does not assert direct ligand binding to RET. GDF9-BMPR2 is supported as a type-II receptor component in granulosa-cell assays, with ALK5 as the type-I signaling partner. GHRH-GHSR is supported by direct binding, calcium/inositol-phosphate activation, cooperativity with ghrelin, and receptor endocytosis in GHSR1a-expressing cells, but the heterologous low-potency context is retained.

GDF2/BMP9 showed weak direct binding to ACVR1/ALK2 in transfected receptor systems, while the primary signaling receptor was ALK1; this was retained as binding-only. GHRH-VIPR1 was retained as low-affinity binding/cross-reactivity only. GDNF-EDNRB is functional cross-talk in enteric neural-crest migration: EDNRB signaling modulates GDNF responsiveness, but EDN3 is the EDNRB ligand and no direct GDNF-EDNRB binding was inferred. GHRH-DPP4 is direct enzymatic processing of GHRH at the Ala2-Asp3 bond and is not a receptor edge.

The GDF11 BMPR1A/B/BMPR2 boundaries were kept unresolved because primary structural and receptor-spectrum studies support ALK4/5/7 and ACVR2A/ACVR2B usage, with GDF11 absent from the tested BMPR2-binding set. GDF5-ACVR1 and GDF9-ACVR2A/BMPR1A/B were likewise not promoted from related BMP/activin receptor evidence. No direct GDF9-FXYD6 or GDF9-ORAI2 mechanism was recovered. GDNF-GFRA3 remains unresolved/negative in the reviewed ligand-panel context because GFRA3 is artemin-preferring and was not shown to mediate GDNF-RET signaling.

## Search boundary and validation

Searches covered exact pair terms across PubMed, PMC, publisher pages, IUPHAR/BPS Guide to PHARMACOLOGY, Reactome/pathway-resource comparators, and receptor-family literature, with primary research prioritized. Related-family evidence, co-expression, generic GPCR or TGF-beta receptor promiscuity, and pathway overlap were not promoted to unsupported direct edges. All terminal_TF fields are `null` because no exact batch row contained separately validated terminal transcription-factor activation evidence.

- Exactly 25 data rows and 13 tab-delimited columns.
- Review IDs and pair labels match the requested exact batch.
- Fields contain no embedded tabs or newlines.
- Only `module21a_batch120_review.tsv` and `module21a_batch120_summary.md` were written; shared Module 21A registers, Module 20A ledgers, frozen manifest, and integration outputs were not modified.
