# Module 21A batch 029 review summary

## Scope

Reviewed the exact frozen Module20A priority-8 low/uncertain rows `M20A-CELLCHAT-REMAINING-0026` through `M20A-CELLCHAT-REMAINING-0050`. The queued labels represent serotonin (`5-HT`) with alternative upstream production or vesicular-source annotations and the indicated HTR receptor. Module20A and the shared Module21A registers were not modified.

## Classification

- Exact rows reviewed: 25
- `reviewed_relay_candidate`: 25
- `reviewed_function_only`: 0
- `reviewed_binding_only`: 0
- `reviewed_no_downstream_evidence`: 0
- `reviewed_unresolved`: 0
- Terminal TF assignments: 0

The promoted layer is `receptor_proximal_relay`. The records retain receptor activation and relay separately from downstream cellular outputs. No transcription factor was entered because the reviewed primary assays did not directly measure a terminal TF activation endpoint for these exact source branches.

## Main additions

- HTR1A, HTR1B, HTR1D, HTR1E, and HTR1F: direct 5-HT receptor assays support Gi/o-linked inhibition of adenylyl cyclase/cAMP, with context-dependent ERK, PLC, Ca2+, or growth outputs.
- HTR2A, HTR2B, and HTR2C: direct 5-HT assays support Gq/11-linked PLC/Ca2+ relay; HTR2A and HTR2C also have pERK measurements, and HTR2B has astrocyte glycogenolytic output.
- HTR3 complex: 5-HT-evoked cation currents are supported in human HTR3A homomeric and HTR3A/3B heteromeric preparations. The receptor-complex composition remains explicit because native subunit assemblies differ by tissue.
- HTR4: 5-HT stimulation supports Gs→cAMP→PKA and T-type Ca2+ relay with cortisol secretion in primary human adrenocortical cells.
- HTR5A: 5-HT stimulation supports Gi/o-linked cAMP inhibition and IP3-sensitive Ca2+ mobilization in human HTR5A-expressing C6 glioma cells.
- HTR6 and HTR7: 5-HT stimulation supports Gs-linked cAMP relay; HTR7 additionally has PKC-MAPK-dependent synaptic-function evidence in mouse cerebellar slices.

## Limitations and search boundaries

Searches covered exact receptor symbols and subtype names in PubMed, PMC, publisher-indexed records, IUPHAR/BPS pharmacology context, and cAMP/GPCR pathway context. Primary studies were preferred. Pathway databases and pharmacology resources were used for branch context and nomenclature, not as substitutes for pair-specific experiments.

The source enzymes/transporters (`DOPA/DDC`, `TPH1`, `SLC18A1`, and `SLC18A2`) were not manipulated in the receptor signaling experiments. Therefore these records support the downstream response to serotonin at the indicated receptor, not a demonstrated enzyme-to-receptor transfer, local production event, or vesicular-release mechanism. Studies using receptor-selective agonists such as DOI or 5-CT are cited only alongside direct 5-HT evidence and are not used to claim that those analogues are the queued ligand. HTR3 evidence is retained as a receptor-complex node rather than collapsed to a single subunit. Recombinant-cell and overexpression contexts are recorded as limitations.

## File

- `module21a_batch029_review.tsv`

