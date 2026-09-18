# mSCIdblit v1.9.21

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The routes retain ligand--receptor--
output evidence while leaving intracellular continuation and transcription
factor layers explicitly unasserted. They are therefore available to mSCS as
plausible evidence routes without being promoted to causal graph edges or
receiving database-level confidence scores.

Added route families:

- E-cadherin--alphaEbeta7 and E-cadherin--alpha2beta1 heterotypic adhesion
  (PMID:8940076; PMID:10790430; PMID:12392763).
- JAM-A--LFA-1 and JAM-C--Mac-1 leukocyte adhesion/transmigration
  (PMID:11812992; PMID:15528364; PMID:12208882; PMID:15485832).
- VCAM1--alphaDbeta2 and VCAM1--alpha9beta1 adhesion/transmigration
  (PMID:9841932; PMID:10438935; PMID:10209034).
- SIRPalpha--Mac-1, GPIbalpha--Mac-1, and RAGE--Mac-1 counter-receptor
  outputs (PMID:30910815; PMCID:PMC6514624; PMID:10899906; PMID:14623906).
- ICAM3--LFA-1 T-cell adhesion (PMID:8798624; PMID:7518468; PMID:8547030).

All ten records use the bounded route expression
`ligand>receptor>????>????>output`, with `causal_status=not_asserted`,
`traversal_status=evidence_route_not_causal`, and no intracellular or TF edge
fields populated. No base graph nodes, edges, edge-source records, or
confidence scores were added.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 16,941 signaling-route evidence records
- 894 cumulative literature-expansion routes
- 864 covered downstream-curation queue candidates
- 2,467 remaining downstream-curation queue candidates
- 1,422 remaining P1 candidates
