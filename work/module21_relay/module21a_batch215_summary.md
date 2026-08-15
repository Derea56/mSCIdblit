# Module 21A batch 215 review summary

## Adjudication decision

The review TSV is the authoritative evidence artifact for batch 215. A prior
stale summary version was rejected because it did not match the validated
row-level records. The final TSV disposition is **11 relay, 1 binding-only, 1
scavenging-only, 5 unresolved, and 7 no-evidence**, with
`SMAD1;SMAD5;SMAD8` retained only on `M20A-EXT-1765` and literal `null` on the
other 24 rows. The TSV required no evidence-row reclassification after
validation; this summary has been reconciled to it.

Batch 215 reviews exactly 25 currently queued Module20A pairs, preserving the
submitted receptor labels and keeping receptor-complex, receptor-proximal, and
downstream/function evidence separate. No Module20A ledger, Module21A ledger,
frozen manifest, or SQL materialization was changed.

## Disposition

- 11 `reviewed_relay_candidate`
- 5 `reviewed_unresolved`
- 1 `reviewed_binding_only`
- 1 `reviewed_scavenging_only`
- 7 `no_evidence_boundary`

The positive relay records cover GDF1/EGF-CFC Activin-Nodal complexes,
GDF10-BMPR2/ALK3-SMAD1/5/8 signaling, GDF11 ActRIIA/ACVR2A and
ACVR2B-TGFBR1/ALK5 branches, GDF2/ACVR2A-ACVRL1 and ENG/ALK1 endothelial
contexts, and GDF3/EGF-CFC Activin-Nodal complexes. The GDF11-ACVR1C row is
binding-only because ALK7 interaction/capacity was reported but productive
signaling was not shown to be the predominant exact branch. The GDF2-
ACVR2B-ACVRL1 and GDF1/GDF3 ACVR1C composites remain unresolved rather than
being promoted from receptor-family or comparator evidence.

GC/DBP–LRP2 is recorded as `reviewed_scavenging_only`: primary work supports
megalin-dependent uptake of the vitamin-D-binding-protein complex, often with
cubilin/CUBAM context, but does not establish an intracellular LRP2 relay.

## Terminal-TF handling

Only `M20A-EXT-1765` carries a provisional endpoint, `SMAD1;SMAD5;SMAD8`,
because the primary GDF10 study directly measured pSMAD1/5/8 and SMAD1/5
occupancy at the Smad7 promoter. All other rows use the literal `null`; pathway
readouts, developmental phenotypes, ID1/ID3, Hox outputs, and generic SMAD
activation were not converted into a terminal-TF assignment without an exact
pair-specific endpoint.

## Search boundaries and limitations

Searches covered exact ligand/receptor names and aliases across PubMed, PMC,
publisher pages, Europe PMC, and pathway-resource leads. For no-evidence rows,
the stable search URLs are retained in the TSV. Family-level Activin/Nodal,
BMP9/GDF2, serotonin/HTR4, anthrax-receptor, orphan-GPCR, and megalin
annotations were not transferred to untested exact pairs. Receptor-complex
records retain CFC1/Cripto, ACVR2A/B, ACVRL1, ENG, and BMPR1A/ALK3 context where
the primary assay required those components; no direct binary interaction is
inferred from pathway or functional evidence alone.

## Validation

- 25 data rows; exact requested queue order and labels
- 25 unique review IDs and 25 unique pair labels
- Exact 13-column schema
- All required fields populated, including stable citations and limitations
- Confidence values restricted to the established vocabulary
- `terminal_TF` is literal `null` except for the explicitly supported GDF10 endpoint
- No edits outside `module21a_batch215_review.tsv` and this summary file
