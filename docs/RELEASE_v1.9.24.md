# mSCIdblit v1.9.24

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The routes retain ligand--receptor--
output evidence while leaving intracellular continuation and transcription
factor layers explicitly unasserted. They are therefore available to mSCS as
plausible evidence routes without being promoted to causal graph edges or
receiving database-level confidence scores.

Added route families:

- IGF1/alphaVbeta3 and IGF2/alphaVbeta3 ternary crosstalk with IGF1R
  (PMID:19578119; PMCID:PMC2782004; PMID:28873464; PMCID:PMC5584928).
- CD40L/alphaIIbbeta3 platelet outside-in activation (PMID:14519852).
- CCL5, CXCL12, and CX3CL1 allosteric activation of alphaIIbbeta3
  (PMID:36231020; PMCID:PMC9563052).
- CX3CL1 alphaVbeta3-CX3CR1 and alpha4beta1-CX3CR1 coreceptor outputs
  (PMID:23125415; PMCID:PMC3518660).
- CCL5 and CXCL12 allosteric alphaVbeta3 activation
  (PMID:36231020; PMCID:PMC9563052).

All ten records use the bounded route expression
`ligand>receptor>????>????>output`, with `causal_status=not_asserted`,
`traversal_status=evidence_route_not_causal`, and no intracellular or TF edge
fields populated. No base graph nodes, edges, edge-source records, or
confidence scores were added.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 16,971 signaling-route evidence records
- 924 cumulative literature-expansion routes
- 894 covered downstream-curation queue candidates
- 2,437 remaining downstream-curation queue candidates
- 1,392 remaining P1 candidates
