# mSCIdblit v1.9.131

This release adds ten primary-literature receptor-proximal evidence routes to the Module 21b evidence layer. The records cover auxiliary-subunit regulation, scaffold/channel coupling, channel trafficking and gating, receptor localization, heteromeric purinergic and angiotensin-receptor signaling, calcium-channel regulation, and serotonin-receptor regulation. They remain non-causal evidence routes with ligand input, terminal transcription-factor, and target-gene layers explicitly unresolved.

## Added routes

- MiRP1/KCNE2 → KCNQ1/Kv7.1: auxiliary-subunit regulation of potassium-current output.
- CIPP → ASIC3/ACCN3: PDZ-scaffold coupling and acid-sensing current output.
- TRIP8b/PEX5L → HCN4: channel trafficking and gating regulation.
- FGF13 → Nav1.5/SCN5A: sodium-channel localization and conduction output.
- MRAP2 → MC4R: receptor trafficking and primary-cilia energy-homeostasis signaling.
- P2Y1/P2RY1 → P2Y4/P2RY4: heteromeric purinergic calcium signaling.
- P2Y6/P2RY6 → AT1/AGTR1: heteromeric angiotensin-II receptor signaling.
- CaBP1/CABP1 → CaV2.1/CACNA1A: calcium-dependent channel-gating regulation.
- Calmodulin/CALM1 → 5-HT2A/HTR2A: agonist-dependent receptor coupling and phosphorylation.
- RSK2/RPS6KA3 → 5-HT2A/HTR2A: receptor phosphorylation and signaling selectivity.

## Bundle accounting

- Route evidence records: 19,827 → 19,837 (+10).
- Graph nodes: 11,952 (unchanged).
- Graph edges: 14,722 (unchanged).
- Downstream evidence queue: 3,331 (unchanged).
- Literature-expansion rows: 10.
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion226`.

These additions expand the traversable evidence layer for mSCS plausibility evaluation without asserting ligand identity, causal relay, confidence score, or terminal transcriptional mechanism.
