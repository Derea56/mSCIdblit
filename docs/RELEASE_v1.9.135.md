# mSCIdblit v1.9.135

This release adds ten primary-literature receptor-output and ligand–receptor-output evidence routes to the Module 21b evidence layer. The records extend synaptic organization, inhibitory synapse anchoring, complement and lipid-handling outputs, immune checkpoint signaling, and a receptor-linked intracellular Gq output. Intracellular, transcription-factor, and target-gene layers remain explicitly unresolved where the source does not establish them.

## Added routes

- CRRY/complement inhibition → reduced microglial synaptic engulfment.
- GPC4 → GPR158: hippocampal synaptogenesis output.
- APP → LRP4: agrin/NMJ organization output.
- IL1RAPL2 → PTPRD: excitatory synapse and spine-formation output.
- PVR/CD155 → KIR2DL5B: inhibitory NK-cell checkpoint output.
- NLGN1 → DLG4/PSD-95: synaptic-scaffold output.
- SLC12A5/KCC2 → GPHN/gephyrin: inhibitory-synapse anchoring output.
- NID2 → LGR4 → GNAQ/GNA11: receptor-linked Gq/PKC/AMPK output.
- CLU/ApoJ → TREM2: microglial lipoprotein-uptake output.
- GABRA3 → GPHN/gephyrin: inhibitory post-synapse output.

## Bundle accounting

- Route evidence records: 19,867 → 19,877 (+10).
- Graph nodes: 11,952 (unchanged).
- Graph edges: 14,722 (unchanged).
- Downstream evidence queue: 3,331 (unchanged).
- Literature-expansion rows: 10.
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion230`.

These additions expand the traversable evidence layer for mSCS plausibility evaluation without asserting causal relay, confidence score, or terminal transcriptional mechanism.
