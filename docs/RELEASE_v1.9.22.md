# mSCIdblit v1.9.22

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The routes retain ligand--receptor--
output evidence while leaving intracellular continuation and transcription
factor layers explicitly unasserted. They are therefore available to mSCS as
plausible evidence routes without being promoted to causal graph edges or
receiving database-level confidence scores.

Added route families:

- ICAM1--Mac-1 and EPCR--Mac-1 adhesion under static and flow conditions
  (PMID:1980124; PMID:23408932; PMCID:PMC3567096).
- Thy-1--alphaVbeta3 astrocyte adhesion/focal-adhesion signaling and
  Thy-1--Mac-1 neutrophil adhesion (PMID:11470407; PMID:22479590;
  PMID:16374458).
- CD40L--Mac-1, ICAM4--Mac-1, and ICAM4--LFA-1 adhesion
  (PMID:17372166; PMCID:PMC3291815; PMID:10846180).
- Pleiotrophin--Mac-1, LL-37--Mac-1, and myeloperoxidase--Mac-1 outputs
  (PMID:28939773; PMCID:PMC5704470; PMID:26876535; PMCID:PMC5157691;
  PMID:9175709).

All ten records use the bounded route expression
`ligand>receptor>????>????>output`, with `causal_status=not_asserted`,
`traversal_status=evidence_route_not_causal`, and no intracellular or TF edge
fields populated. No base graph nodes, edges, edge-source records, or
confidence scores were added.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 16,951 signaling-route evidence records
- 904 cumulative literature-expansion routes
- 874 covered downstream-curation queue candidates
- 2,457 remaining downstream-curation queue candidates
- 1,412 remaining P1 candidates
