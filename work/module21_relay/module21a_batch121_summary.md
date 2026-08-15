# Module 21A batch 121 review

Batch 121 covers exactly the 25 requested queue rows `M20A-EXT-1821` through `M20A-EXT-1847`.

## Disposition

- 1 `reviewed_binding_only`: Ghrl-Gpr39, retaining the original obestatin-GPR39 binding/activation report as a contested boundary.
- 2 `reviewed_function_only`: Gip-Dpp4 and Gip-Fap, both direct peptide-processing edges without receptor-proximal intracellular relay evidence.
- 22 `reviewed_unresolved`: all remaining exact pairs.

## Evidence notes

The Ghrl-Gpr39 row is deliberately conservative. Positive primary work reported obestatin binding and GPR39-dependent c-fos/ERK outputs, but independent primary studies did not reproduce obestatin signaling or food-intake effects consistently. Because GHRL is a precursor gene and the evidence concerns obestatin rather than mature ghrelin, no downstream relay or terminal TF was assigned.

GIP-DPP4 is supported by direct biochemical degradation of GIP(1-42) to GIP(3-42) in purified-enzyme and rat-serum assays. GIP-FAP is also supported as a direct biochemical cleavage edge, but GIP was a very inefficient FAP substrate and required prolonged incubation. Neither enzyme-processing row is a ligand-receptor binding or receptor-proximal signaling claim.

Gm11127 is annotated as an H2-T15/H2-T27 MHC-I-family gene, but generic MHC-I-CD8 binding was not transferred to the exact CD8A or CD8B1 rows. Gm13306 is annotated as Ccl27b; canonical CCL27a-CCR10 evidence was not transferred because mouse annotation resources distinguish Ccl27b receptor specificity and no exact Ccl27b-CCR10 assay was recovered. Gm13305 remains a predicted mouse gene, so no CD40 edge was promoted.

## Search boundary and validation

Searches covered exact gene/protein pairs across PubMed, PMC, publisher pages, Reactome, NCBI Gene, and chemokine/receptor resources, with primary research prioritized. Family-level receptor similarity, pathway co-occurrence, canonical ligand aliases, and generic MHC-I/CD8 evidence were not promoted to unsupported exact molecular edges. No terminal transcription factor was assigned.

- Exactly 25 data rows and 13 tab-delimited columns.
- Review IDs and pair labels match the requested exact batch.
- Fields contain no embedded tabs or newlines.
- Only `module21a_batch121_review.tsv` and `module21a_batch121_summary.md` were written; shared Module 21A registers, Module 20A ledgers, frozen manifest, and integration outputs were not modified.
