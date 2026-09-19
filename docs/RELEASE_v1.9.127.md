# mSCIdblit v1.9.127

This release adds ten primary-literature receptor-proximal evidence routes to the Module 21b evidence layer. The records cover activating-receptor association, auxiliary-protein maturation, synaptic-receptor trafficking, channel-complex regulation, receptor heteromerization, and adaptor-dependent localization. They remain non-causal evidence routes with ligand input, terminal transcription-factor, and target-gene layers explicitly unresolved.

## Added routes

- SIGLEC16 → DAP12/TYROBP: activating receptor-complex and macrophage-association output.
- SHISA6/CKAMP53 → GluA2/GRIA2: postsynaptic trapping and AMPA-receptor desensitization output.
- RIC3 → CHRNA7: alpha7 nicotinic-receptor folding, assembly, and surface-expression output.
- ANK3/ankyrin-G → KCNQ2: axon-initial-segment retention and excitability output.
- STIM1 → TRPV4: trafficking and calcium-channel function output.
- PSD-95/DLG4 → ASIC2: PDZ-scaffold and synaptic-localization output.
- DPP10 → Kv4.2/KCND2: auxiliary-subunit trafficking and channel-gating output.
- P2Y1 → P2Y2: heteromeric purinergic signaling and granulocyte-response output.
- CD99 → CD99L2: receptor association and cell-surface-trafficking output.
- NHERF1/SLC9A3R1 → 5-HT4a/HTR4A: PDZ-adaptor and microvillar-localization output.

## Bundle accounting

- Route evidence records: 19,787 → 19,797 (+10).
- Graph nodes: 11,952 (unchanged).
- Graph edges: 14,722 (unchanged).
- Downstream evidence queue: 3,331 (unchanged).
- Literature-expansion rows: 10.
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion222`.

The additions expand the traversable evidence layer for mSCS plausibility evaluation without asserting ligand identity, causal relay, confidence score, or terminal transcriptional mechanism.
