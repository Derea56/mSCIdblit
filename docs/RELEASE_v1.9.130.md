# mSCIdblit v1.9.130

This release adds ten primary-literature receptor-proximal evidence routes to the Module 21b evidence layer. The records cover cytoskeletal receptor transport, receptor maturation, channel-complex stoichiometry and trafficking, auxiliary-subunit regulation, purinergic receptor trafficking, auditory mechanotransduction, and calcium-channel localization. They remain non-causal evidence routes with ligand input, terminal transcription-factor, and target-gene layers explicitly unresolved.

## Added routes

- KIF5/Kinesin-1 → GABA-B receptor complex: cytoskeletal receptor transport.
- RIC3 → 5-HT3A/HTR3A: receptor maturation and surface expression.
- TRIP8b/PEX5L → HCN2: channel-complex stoichiometry, trafficking, and gating.
- α1-Syntrophin/SNTA1 → Nav1.5/SCN5A: membrane density and sodium-current output.
- DPP10 → Kv4.3/KCND3: inactivation and potassium-current output.
- S100A10 → TRPV6: epithelial calcium-channel trafficking.
- HSP90α → P2X1/P2RX1: receptor trafficking and platelet-response output.
- TOMT → TMC1: hair-cell mechanotransduction-complex integration.
- Cadherin-23/CDH23 → PCDH15: auditory tip-link and mechanotransduction output.
- α2δ2/CACNA2D2 → CaV2.1/CACNA1A: lipid-raft localization and calcium-current output.

## Bundle accounting

- Route evidence records: 19,817 → 19,827 (+10).
- Graph nodes: 11,952 (unchanged).
- Graph edges: 14,722 (unchanged).
- Downstream evidence queue: 3,331 (unchanged).
- Literature-expansion rows: 10.
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion225`.

These additions expand the traversable evidence layer for mSCS plausibility evaluation without asserting ligand identity, causal relay, confidence score, or terminal transcriptional mechanism.
