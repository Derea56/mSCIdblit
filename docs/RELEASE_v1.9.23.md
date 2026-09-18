# mSCIdblit v1.9.23

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The routes retain ligand--receptor--
output evidence while leaving intracellular continuation and transcription
factor layers explicitly unasserted. They are therefore available to mSCS as
plausible evidence routes without being promoted to causal graph edges or
receiving database-level confidence scores.

Added route families:

- Neutrophil elastase, high-molecular-weight kininogen, factor X, and
  dynorphin A interactions with Mac-1 (PMID:8879192; PMCID:PMC2192826;
  PMID:8034694; PMID:2835359; PMID:1957171; PMID:26036990;
  PMCID:PMC4481117).
- FGF1 and FGF2 direct alphaVbeta3 binding and functional outputs
  (PMID:18441324; PMCID:PMC2440593; PMID:9398667).
- Processed VEGF-C and VEGF-D alpha9beta1 adhesion/migration outputs
  (PMCID:PMC1368959; DOI:10.1074/jbc.M412816200).
- NRG1 alphaVbeta3/ErbB3 and alpha6beta4/ErbB3 crosstalk outputs
  (PMID:20682778; PMCID:PMC2951213).

All ten records use the bounded route expression
`ligand>receptor>????>????>output`, with `causal_status=not_asserted`,
`traversal_status=evidence_route_not_causal`, and no intracellular or TF edge
fields populated. No base graph nodes, edges, edge-source records, or
confidence scores were added.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 16,961 signaling-route evidence records
- 914 cumulative literature-expansion routes
- 884 covered downstream-curation queue candidates
- 2,447 remaining downstream-curation queue candidates
- 1,402 remaining P1 candidates
