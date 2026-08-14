# Module 21A targeted second-pass summary: Q007, Q008, Q009

Date: 2026-08-14

## Additions

- Q007 added `M21A-E104` for FGF10/FGFR2-associated PI3K-AKT signaling after SCI, with a neuronal/microglial receiver boundary.
- Q007 added `M21A-E105` for PDGFR-beta pathway control of fibrotic scar formation after SCI, with astrocyte, fibroblast, and microglia/macrophage ligand-source context.
- Q007 added `M21A-E106` and `M21A-E107` for VEGF-to-EGFR transactivation and spinal neural stem-cell activation after SCI; VEGFR paralog identity remains unresolved.
- Q008 added `M21A-E108` for astrocytic RYK regulation of scar-border formation and wound healing after SCI; the source measured canonical WNT changes and proposed, but did not test, a noncanonical PCP branch.
- Q009 added `M21A-E109` and `M21A-E110` for DLL4-NOTCH1 control of IL-6 transcription, STAT3 phosphorylation, and reactive astrocyte state in CNS neuroinflammation models.

The batch adds 7 edges, 5 grouped evidence records (`M21A-SAT-EVID-042`–`046`), 5 perturbation records (`M21A-SAT-P047`–`P051`), and 7 evidence-layer rows. All added edges are pathway-complex or functional-output records; no direct molecular interaction was inferred from a pathway-level or functional result.

## Unresolved cases

- Q007 remains partially resolved: FGFR2, PDGFR-beta, and VEGF-EGFR branches are supported, but astrocyte-specific FGFR identity and VEGFR paralog-specific receiver signaling remain open.
- Q008 remains partially resolved: astrocytic RYK is functionally linked to SCI wound healing, but the noncanonical PCP branch is not directly tested.
- Q009 remains partially resolved: DLL4-NOTCH1 astrocyte signaling is supported in EAE/CNS neuroinflammation, while comprehensive NOTCH2/3/4 branch resolution in contusive SCI remains open. Nonspecific Notch inhibition was not promoted to paralog-specific evidence.

## Validation

Post-update checks passed: unique IDs, unique cross-register edge keys, evidence support for every edge, complete layer assignment for added edges, preserved receptor/pathway nodes, and unchanged Module 20A manifest SHA-256 `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

Main registers now contain 102 edges, 46 grouped evidence records, 51 perturbations, and 45 evidence-layer rows. SQL materialization remains deferred.

