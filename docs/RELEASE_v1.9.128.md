# mSCIdblit v1.9.128

This release adds ten primary-literature receptor-proximal evidence routes to the Module 21b evidence layer. The records cover receptor-complex crosstalk, ion-channel auxiliary subunits, synaptic receptor trafficking, mechanotransduction, and endosomal second-messenger signaling. They remain non-causal evidence routes with ligand input, terminal transcription-factor, and target-gene layers explicitly unresolved.

## Added routes

- CaSR → GABBR1: calcium-sensing receptor-complex expression and PLC output.
- Stargazin/CACNG2 → GluA1:GluA2: AMPA-receptor trafficking and gating output.
- KChIP1/KCNIP1 → Kv4.2/KCND2: channel-complex assembly and gating output.
- KCNE1 → KCNQ1: channel-complex assembly and membrane-current output.
- LYNX2 → CHRNA7: alpha7 nicotinic-receptor complex and agonist-response output.
- TRIP8b/PEX5L → HCN1: channel trafficking and cyclic-nucleotide-gating output.
- Ankyrin-G/ANK3 → KCNQ3: axon-initial-segment retention output.
- P2Y12 → PAR4: receptor dimerization, beta-arrestin recruitment, and Akt output.
- PRRT1/SynDIG4 → AMPA-receptor complex: extrasynaptic localization and surface-level output.
- CIB2 → TMC1: hair-cell mechanotransduction-complex output.

## Bundle accounting

- Route evidence records: 19,797 → 19,807 (+10).
- Graph nodes: 11,952 (unchanged).
- Graph edges: 14,722 (unchanged).
- Downstream evidence queue: 3,331 (unchanged).
- Literature-expansion rows: 10.
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion223`.

These additions expand the traversable evidence layer for mSCS plausibility evaluation without asserting ligand identity, causal relay, confidence score, or terminal transcriptional mechanism.
