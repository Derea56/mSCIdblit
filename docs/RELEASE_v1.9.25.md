# mSCIdblit v1.9.25

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The routes retain ligand--receptor--
output evidence while leaving intracellular continuation and transcription
factor layers explicitly unasserted. They are therefore available to mSCS as
plausible evidence routes without being promoted to causal graph edges or
receiving database-level confidence scores.

Added route families:

- IGF1/alpha6beta4 and IGF2/alpha6beta4 IGF1R crosstalk outputs
  (PMID:22351760; PMID:28873464; PMCID:PMC5584928).
- ANGPT1/alpha5beta1 adhesion (PMID:11346644; PMID:27695111).
- VEGFA/alpha9beta1 cooperative VEGFR2 adhesion and angiogenesis
  (PMID:17363377).
- NGF, BDNF, and NT3 alpha9beta1 adhesion/neurotrophin outputs
  (PMID:18230652).
- Immobilized VEGF165/189 alpha3beta1 and alphaVbeta3 adhesion/survival
  outputs (PMID:12709411).
- ANGPTL3/alphaVbeta3 endothelial angiogenesis output
  (PMID:11877390; DOI:10.1074/jbc.M109768200).

All ten records use the bounded route expression
`ligand>receptor>????>????>output`, with `causal_status=not_asserted`,
`traversal_status=evidence_route_not_causal`, and no intracellular or TF edge
fields populated. No base graph nodes, edges, edge-source records, or
confidence scores were added.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 16,981 signaling-route evidence records
- 934 cumulative literature-expansion routes
- 904 covered downstream-curation queue candidates
- 2,427 remaining downstream-curation queue candidates
- 1,382 remaining P1 candidates
