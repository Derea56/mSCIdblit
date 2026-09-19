# mSCIdblit v1.9.129

This release adds ten primary-literature receptor-proximal evidence routes to the Module 21b evidence layer. The records cover trans-synaptic organization, GPCR trafficking, calcium-channel regulation, receptor heteromerization, auxiliary-channel trafficking, purinergic receptor complexes, and presynaptic release. They remain non-causal evidence routes with ligand input, terminal transcription-factor, and target-gene layers explicitly unresolved.

## Added routes

- TrkC/NTRK3 → PTPσ/PTPRS: trans-synaptic excitatory-synapse organization.
- GISP → GABA-B1/GABBR1: receptor trafficking and ERK/GIRK output.
- KChIP2/KCNIP2 → CaV1.2/CACNA1C: cardiac calcium-current regulation.
- P2Y1 → A1/ADORA1: heteromeric purinergic and Gi/o output.
- S100A10 → TRPV5: epithelial calcium-channel trafficking.
- S100A10 → mGluR5/GRM5: receptor localization and neuronal output.
- HSP90α → P2X7/P2RX7: receptor-complex phosphorylation and activation output.
- EROS/CYBC1 → P2X7/P2RX7: receptor abundance and phagocyte purinergic function.
- CIB2 → TMC2: auditory hair-cell mechanotransduction-complex output.
- RIM1/RIMS1 → CaV2.1/CACNA1A: presynaptic channel anchoring and release output.

## Bundle accounting

- Route evidence records: 19,807 → 19,817 (+10).
- Graph nodes: 11,952 (unchanged).
- Graph edges: 14,722 (unchanged).
- Downstream evidence queue: 3,331 (unchanged).
- Literature-expansion rows: 10.
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion224`.

These additions expand the traversable evidence layer for mSCS plausibility evaluation without asserting ligand identity, causal relay, confidence score, or terminal transcriptional mechanism.
