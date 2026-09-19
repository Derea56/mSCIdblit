# mSCIdblit v1.9.126

This release adds ten primary-literature receptor-proximal evidence routes to the Module 21b evidence layer. The records capture auxiliary-protein, receptor-crosstalk, synaptic-receptor, mechanosensitive-channel, and neuroprotective-complex outputs. They remain non-causal evidence routes with ligand input, terminal transcription-factor, and target-gene layers explicitly unresolved.

## Added routes

- SHISA7/CKAMP59 → GABRG2: receptor abundance, trafficking, and inhibitory transmission.
- GABARAP → GRIP1: inhibitory-synapse trafficking and receptor localization.
- CAML → GABRG2: receptor recycling, surface expression, and inhibitory-current output.
- KIF21B → GABRG2: gamma2 receptor transport and surface delivery.
- DRD5 → GABRG2: direct receptor coupling and mutually inhibitory cAMP/current crosstalk.
- NETO2 → GluK2/GRIK2: kainate-receptor gating and desensitization modulation.
- P2Y2 → A1/ADORA1: heteromeric Gi/o, Gq/11, cAMP, and calcium crosstalk.
- EphB2 → GluN1/GRIN1: NMDA-receptor synaptic localization and calcium-current regulation.
- STOML3 → PIEZO1: mechanosensitive-current threshold modulation.
- TrkB/NTRK2 → GluN1/GRIN1: BDNF-stimulated neuroprotective-complex output.

## Bundle accounting

- Route evidence records: 19,777 → 19,787 (+10).
- Graph nodes: 11,952 (unchanged).
- Graph edges: 14,722 (unchanged).
- Downstream evidence queue: 3,331 (unchanged).
- Literature-expansion rows: 10.
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion221`.

These additions strengthen mSCS plausibility evaluation for receptor-proximal signaling and receptor-complex context without asserting a ligand, causal relay, confidence score, or terminal transcriptional mechanism.
