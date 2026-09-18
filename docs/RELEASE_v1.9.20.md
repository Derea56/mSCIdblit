# mSCIdblit v1.9.20

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The routes retain ligand--receptor--
output evidence while leaving intracellular continuation and transcription
factor layers explicitly unasserted, so downstream mSCS traversal can treat
them as plausible evidence routes without promoting them to causal graph
edges or assigning confidence scores.

Added route families:

- MDK--LRP1-associated embryonic-neuron survival output (PMID:10772929).
- FGF18--FGFR2c and FGF18--FGFR3c chondrocyte trophic responses
  (PMID:11950254).
- Fibronectin--alpha8beta1 and vitronectin--alphaVbeta5 adhesion outputs
  (PMID:7559467; PMID:1694173; PMID:9137089).
- FGF1--FGFR4, FGF10--FGFR1b, and FGF18--FGFR4 receptor-specific outputs
  (PMID:16597617; PMCID:PMC2080618; PMID:9843417; PMID:11950254).
- MAdCAM1--alpha4beta7 and VCAM1--alpha4beta7 adhesion outputs
  (PMID:7687523; PMID:8640376).

All ten records use the bounded route expression
`ligand>receptor>????>????>output`, with `causal_status=not_asserted`,
`traversal_status=evidence_route_not_causal`, and no intracellular or TF edge
fields populated. No base graph nodes, edges, edge-source records, or
confidence scores were added.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 16,931 signaling-route evidence records
- 884 cumulative literature-expansion routes
- 854 covered downstream-curation queue candidates
- 2,477 remaining downstream-curation queue candidates
- 1,432 remaining P1 candidates
