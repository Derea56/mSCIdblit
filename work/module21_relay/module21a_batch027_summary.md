# Module 21A batch 027 review summary

## Scope

Fourteen exact Module20A priority-7/low rows were checked against PubMed, PMC, publisher pages, Reactome, KEGG, and exact-symbol web searches. The frozen queue was verified before review; all 14 requested review IDs were present and matched the requested pair labels.

## Outcome

- 14/14 rows reviewed.
- 14 `reviewed_unresolved`.
- 0 `reviewed_relay_candidate`.
- 0 `reviewed_function_only`.
- 0 `reviewed_binding_only`.
- 0 `reviewed_no_downstream_evidence`.
- 0 terminal TF assignments.

The strongest evidence located was boundary evidence rather than a promotable exact edge:

- Gamma-3-containing laminin preparations were reported not to bind integrins in a comparative recombinant assay, but this did not establish every possible LAMC3-containing complex or a downstream relay for LAMC3–alpha1beta1.
- SV2-family association with an alpha5-containing laminin was reported in electric-organ synaptosomes, but the laminin was not LAMC3 and the SV2 isoform was not resolved to SV2A, SV2B, or SV2C.
- Netrin-4 pathway curation supports DCC/UNC5A and laminin gamma-1/gamma-3 branches, not NTRK2/TrkB.
- Thrombospondin-1/CD36, thrombospondin-1/CD47, and thrombospondin-1/SDC4 primary signaling studies were retained as family-specific boundaries and were not transferred to THBS3 or THBS4.
- THBS4–SDC4 and TNXB–SDC4 reports were computational/spatial communication inferences without direct binding or receptor-dependent perturbation for the exact pair.

## Search boundaries and limitations

Exact gene symbols, protein names, receptor-complex notation, laminin-chain aliases, SV2 isoform aliases, thrombospondin/syndecan aliases, and tenascin aliases were searched. Reactome and KEGG were used for pathway context only. Family-level evidence, intact-complex evidence, co-expression, spatial inference, and noncognate ligand/receptor studies were retained as limitations but not promoted to direct molecular or receptor-proximal edges. No exact pair had direct terminal-TF activation evidence.

## File changed

- `work/module21_relay/module21a_batch027_review.tsv`

Module20A ledgers, the frozen Module20A release manifest, and shared Module21A registers were not modified.
