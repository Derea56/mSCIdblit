# mSCIdblit v1.9.28

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The routes retain ligand--receptor--
output evidence while leaving intracellular continuation and transcription
factor layers explicitly unasserted. They are available to mSCS as bounded
plausibility evidence and are not promoted to causal graph edges or database
confidence scores.

Added route families:

- Adiponectin–LAIR1 inhibitory T-cell/SHP-2 output
  (PMID:34403808; DOI:10.1016/j.bbrc.2021.08.025).
- Decorin–MET antagonistic receptor-downregulation and migration output
  (PMCID:PMC2711571).
- Lumican–CD14 bacterial-uptake and LPS-presentation output
  (PMID:17616530; PMID:22865855).
- Lumican–beta2-integrin neutrophil-migration output
  (PMID:19531489).
- Lumican–alphaM-beta2/Mac-1-associated neutrophil-migration output
  (PMID:19531489).
- Lumican–alphaL-beta2/LFA-1-associated neutrophil-migration output
  (PMID:19531489).
- Mindin/SPON2–Mac-1 macrophage-phagocytic output
  (PMID:30910815; PMCID:PMC1895097).
- Soluble CD93–alphaX-beta2 apoptotic-cell efferocytosis output
  (PMID:30656676).
- Oxidized phosphatidylserine–CD36 apoptotic-cell efferocytosis output
  (PMCID:PMC2118161).
- Tenascin-R–contactin-1 adhesion and neurite-outgrowth output
  (PMID:7615642).

All ten records use the bounded route expression
`ligand>receptor>????>????>output`, with
`causal_status=not_asserted`, `traversal_status=evidence_route_not_causal`,
and no intracellular or TF edge fields populated. Output classes preserve the
reported evidence type, including cellular-function, phosphorylation,
phagocytosis, and adhesion/readout outputs. Domain, receptor-complex,
species, and assay limitations are retained in the evidence records.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 17,011 signaling-route evidence records
- 964 cumulative literature-expansion routes
- 934 covered downstream-curation queue candidates
- 2,397 remaining downstream-curation queue candidates
- 1,352 remaining P1 candidates
