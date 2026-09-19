# mSCIdblit v1.9.133

This release adds ten primary-literature receptor-proximal and receptor-output evidence routes to the Module 21b evidence layer. The records cover XEDAR adaptor recruitment, collagen-activated DDR2 signaling, P2X7 inflammasome association, retinal GPR179 channel coupling, microglial purinergic and complement outputs, astrocytic GPC4–PTPRD signaling, and GPER1 accessory-complex function. They remain non-causal evidence routes with unresolved layers explicitly retained.

## Added routes

- XEDAR/EDA2R → TRAF3: NF-κB/JNK and ectodermal-differentiation output.
- XEDAR/EDA2R → TRAF6: NF-κB/JNK and ectodermal-differentiation output.
- DDR2 → SHC1: collagen-I/Src-associated phosphorylation output.
- P2X7 → ASC/PYCARD: neuronal inflammasome and membrane-breakdown output.
- GPR179 → TRPM1: retinal channel-complex output.
- P2Y12 → microglial synaptic remodeling: visual-cortex plasticity output.
- C1q → microglial synapse elimination: developmental complement output.
- P2Y6 → microglial synapse phagocytosis: developmental pruning output.
- GPC4 → PTPRD/PTPδ: astrocyte-to-neuron synaptogenesis output.
- RAMP3 → GPER1/GPR30: accessory-complex and cardioprotection output.

## Bundle accounting

- Route evidence records: 19,847 → 19,857 (+10).
- Graph nodes: 11,952 (unchanged).
- Graph edges: 14,722 (unchanged).
- Downstream evidence queue: 3,331 (unchanged).
- Literature-expansion rows: 10.
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion228`.

These additions expand the traversable evidence layer for mSCS plausibility evaluation without asserting causal relay, confidence score, or terminal transcriptional mechanism.
