# Module 20B even-suffix Phase-2 source-unit review

Review date: 2026-09-01. Lane: A. Scope: Module 20B Phase-2 source units whose resolver status is exact, whose queue artifact exists, whose observation is already validated, and whose claim gate was pending source review. Only extraction IDs with an even numeric suffix were eligible.

## Result

The integrated promotion queue contains 157 Module 20B rows. Seven rows were in the exact-identity `identity_resolved_source_review` route. The even-suffix rule selected two rows, both under register edge `M20B-E003831`:

- `M20B-P2-R-003831-R110B` — PMID 24434631, functional neural-stem-cell evidence.
- `M20B-P2-R-003831-R110A` — PMID 20828410, receptor-proximal recombinant perlecan-D1/FGF-2/FGFR1c evidence.

The five odd-suffix source-review rows were excluded by the lane rule. No unassigned or ambiguous extraction ID was processed.

## Evidence review

The cited papers support source-bounded observations and author interpretations when the linked primary full text is consulted. The PMID 24434631 paper reports that perlecan deficiency attenuated FGF-2-induced Akt/Erk1/2 activation, cyclin D2 induction, and neurosphere formation in mouse neural-stem-cell models, with corresponding neurogenic niche effects. Its relevant source locations are the Results sections on impaired FGF-2 stimulation, perlecan/FGF-2 localization, and neurosphere formation, together with Figures 5–7 and the Discussion section on the extracellular-matrix niche. [Primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3952240/)

The PMID 20828410 paper reports heparan-sulfate-dependent FGF-2 binding by recombinant human perlecan domain 1 and an FGF-2-dependent mitogenic response in FGFR1c-expressing BaF32 cells. The relevant source locations are the Results sections on FGF-2 binding and mitogenic activity, Figures 6, 7, and 9, and the Discussion section describing FGFR1c co-receptor activity. [Primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2944331/)

## Alignment and grading decision

Neither source establishes the exact registered direct edge `Hspg2 → Fgfr1` with relation `binds_receptor`:

- The PMID 24434631 study is functional perlecan-associated FGF-2 signaling in a neural-stem-cell niche; it does not test direct HSPG2–FGFR1 binding.
- The PMID 20828410 study supports an HS/perlecan-D1–FGF-2–FGFR1c receptor-proximal relay, but its binding assays test perlecan D1–FGF-2 and its cell assay tests FGF-2-dependent proliferation through FGFR1c. Direct HSPG2–FGFR1 binding is not measured.

Both rows therefore retain evidence grade B and their queue context levels (R110B: L2; R110A: L1). No directness, grade, or context upgrade was made. Both final dispositions are `negative_or_boundary_evaluated` and are explicitly excluded from direct-edge promotion.

## Artifact-content blocker

The queue records both local artifacts as `full_text_xml`, and both paths exist with matching queue checksums and byte sizes. Content inspection shows that each file is a PubMed XML record containing article metadata and abstract text, not a full article body with Results/Discussion/figure sections. The figure-level review above was consequently performed against the resolver-approved PMCID full-text pages linked by the records. This mismatch is preserved in the overlay as an explicit blocker; it does not justify treating the local artifacts as figure-level full text or upgrading either row.

## Output and focused checks

The lane overlay is:

`work/cross_module_synthesis/canonical_evidence_review/phase2_K_20B_even_source_unit_overlay.tsv`

It contains two data rows and preserves the original extraction IDs, register IDs, evidence IDs, paper keys, resolver PMIDs, artifact paths, checksums, grade, and context level. The overlay also includes the source-bounded observation and claim, model/species, assay, perturbation, outcome, source locators, edge-alignment disposition, final disposition, and blockers.

Focused validation performed:

- Header/field-count check: pass; every data row has the same number of tab-separated fields as the header.
- Extraction-ID uniqueness check: pass; two unique extraction IDs, with no duplicates.
- Module check: pass; every row is `20B`.
- Even-suffix check: pass; numeric suffixes are 110 and 110.
- Resolver check: pass; both rows have `exact_identifier_match` and a non-null resolver-approved PMID.
- Artifact existence/checksum check: pass; both queue paths resolve through the local archive and match the recorded SHA-256 and byte size.
- Observation/claim coverage check: pass; both rows contain validated observation text, validated source-bounded claim text, source locator, model/species, assay, perturbation, outcome, grade, context, alignment, disposition, and blocker fields.
- Boundary exclusion check: pass; both rows are explicitly excluded from direct-edge promotion, and no PostgreSQL, shared script, schema, release export, or existing file was modified.
