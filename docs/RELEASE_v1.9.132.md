# mSCIdblit v1.9.132

This release adds ten primary-literature receptor-proximal evidence routes to the Module 21b evidence layer. The records cover TLR2/TLR4 adaptor branches, EGFR phosphosite docking, CSF1R and PDGFRB phosphosite signaling, EPOR adaptor and trafficking branches, and VEGFR2-to-ERK output. They remain non-causal evidence routes with ligand input, terminal transcription-factor, and target-gene layers explicitly unresolved.

## Added routes

- TLR2 TIR domain → MyD88: receptor-proximal NF-κB/MAPK signaling.
- TLR2 TIR domain → TIRAP/MAL: sorting-adaptor signaling.
- TLR4 TIR domain → MyD88: receptor-proximal NF-κB/MAPK signaling.
- TLR4 TIR domain → TIRAP/MAL: sorting-adaptor signaling.
- EGFR pY992 → PLCγ1: phosphoinositide and calcium signaling.
- CSF1R pY697 → GRB2: Ras/ERK-associated morphology and growth output.
- PDGFRβ pY771 → RasGAP: negative-Ras-regulation branch.
- EPOR pY429/pY431 → p85: clathrin-mediated receptor internalization.
- EPOR pY343/pY401 → SH2B1: adaptor/phosphorylation branch.
- VEGFR2/KDR pY1175 → ERK1/2: endothelial activation output.

## Bundle accounting

- Route evidence records: 19,837 → 19,847 (+10).
- Graph nodes: 11,952 (unchanged).
- Graph edges: 14,722 (unchanged).
- Downstream evidence queue: 3,331 (unchanged).
- Literature-expansion rows: 10.
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion227`.

These additions expand the traversable evidence layer for mSCS plausibility evaluation without asserting ligand identity, causal relay, confidence score, or terminal transcriptional mechanism.
