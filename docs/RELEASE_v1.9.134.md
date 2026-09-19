# mSCIdblit v1.9.134

This release adds ten primary-literature ligand–receptor-output and receptor-output evidence routes to the Module 21b evidence layer. The records cover immune checkpoint and activating-receptor interactions, complement regulation and clearance, CSF1R-associated trafficking, and LRP1-associated glial myelin uptake. Intracellular, transcription-factor, and target-gene layers remain explicitly unresolved where the source does not establish them.

## Added routes

- PVR/CD155 → CD226/DNAM-1: activating NK/T-cell cytotoxicity.
- PD-L1 → PD-1: inhibitory immune-checkpoint output.
- CD160 → HVEM: context-dependent T-cell/NK signaling.
- C1q → CD91/LRP1: scavenger-receptor clearance.
- CSF1R → CBLB-associated trafficking: macrophage macropinosome output.
- C3b → CD46/MCP: complement-regulatory cofactor output.
- C4b → CD46/MCP: complement-regulatory cofactor output.
- LRP1/CD91 → oligodendrocyte myelin-vesicle uptake and repair.
- LRP1/CD91 → microglial myelin-vesicle uptake and clearance.
- LRP1/CD91 → astrocyte myelin-vesicle uptake and repair.

## Bundle accounting

- Route evidence records: 19,857 → 19,867 (+10).
- Graph nodes: 11,952 (unchanged).
- Graph edges: 14,722 (unchanged).
- Downstream evidence queue: 3,331 (unchanged).
- Literature-expansion rows: 10.
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion229`.

These additions expand the traversable evidence layer for mSCS plausibility evaluation without asserting causal relay, confidence score, or terminal transcriptional mechanism.
