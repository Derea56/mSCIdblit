# Module 21A batch 122 review

Batch 122 covers exactly the 25 requested queue rows `M20A-EXT-1848` through `M20A-EXT-1872`.

## Disposition

- 1 `reviewed_binding_only`: `Gm2023 Ackr4`, supported by mouse CCL19-ACKR4 uptake/scavenging evidence; no canonical G-protein relay was assigned.
- 1 `reviewed_relay_candidate`: `Gm2023 Ccr7`, supported by CCL19-CCR7 Gi/GNAI2 chemotaxis and receptor-signaling evidence.
- 23 `reviewed_unresolved`: all remaining exact pairs, including the contested CCL19-CCRL2 claim, Ccl27al/Ccl27b duplicate boundaries, and generic MHC-I/CD8 family boundaries.

## Evidence notes

`Gm2023` resolves to mouse `Ccl19`. The exact `Ccr7` row was promoted to a receptor-proximal relay candidate from mouse Ccr7/Gnai2/Rgs1 chemotaxis genetics and complementary CCR7 signaling assays. The exact `Ackr4` row was retained as binding/scavenging only because ACKR4 is atypical and the primary studies found no canonical G-protein, Erk1/2, Akt, or Src activation.

`Gm13306` and `Gm2506` map to the Ccl27al/Ccl27b locus. Canonical CCL27-CCR10 and predictive CCR3 annotations were not promoted to duplicate-resolved exact edges because the primary literature did not isolate the queue-labeled duplicate. `Gm2002` resolves to the Il11ra3 receptor-subunit locus, `Gm3934` to the Gstp-ps pseudogene/model locus, and `Gm7030` to H2-T25/H2-t9. These identity annotations do not establish the submitted receptor pairs.

The CCL19-CCRL2/CRAM-B row remains unresolved: an early human study reported binding and internalization, while later work disputed CCL19 as a CCRL2 ligand, and no exact mouse confirmation was recovered. Generic chemokine-receptor similarity, pathway co-occurrence, predicted database annotations, and MHC-I/CD8 family biology were not promoted to direct molecular edges.

## Search boundary and validation

Searches covered exact gene/protein pairs across PubMed, PMC, publisher pages, NCBI Gene, Reactome, KEGG/IUPHAR-style receptor resources, and exact-symbol web queries, with primary research prioritized. Search boundaries and conflicting or family-level evidence are recorded in each unresolved row. No terminal transcription factor was assigned.

- Exactly 25 data rows and 13 tab-delimited columns.
- Review IDs and pair labels match the requested exact batch.
- Fields contain no embedded tabs or newlines.
- Only `module21a_batch122_review.tsv` and `module21a_batch122_summary.md` were written; shared Module 21A registers, Module 20A ledgers, frozen manifest, and integration outputs were not modified.
