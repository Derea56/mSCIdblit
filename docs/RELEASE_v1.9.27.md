# mSCIdblit v1.9.27

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The routes retain ligand--receptor--
output evidence while leaving intracellular continuation and transcription
factor layers explicitly unasserted. They are available to mSCS as bounded
plausibility evidence and are not promoted to causal graph edges or database
confidence scores.

Added route families:

- PVRL2/Nectin-2–PVRIG/CD112R inhibitory checkpoint output
  (PMID:30659054; DOI:10.1038/s41586-019-1275-5).
- CD58/LFA-3–CD2 adhesion and activation output
  (PMID:1723296; PMID:11575926; DOI:10.1006/jmbi.2001.4980;
  PMCID:PMC16325).
- CD48–CD244/2B4 immune-regulatory output
  (PMID:9841922; PMCID:PMC2212392; PMID:18523281;
  DOI:10.4049/jimmunol.180.12.8159).
- CD80/B7-1–CTLA4 inhibitory checkpoint output
  (PMID:9053440; PMCID:PMC2196039; PMID:7545666; PMID:7534620).
- PD-L2–PD-1 inhibitory output
  (PMID:18641123; PMCID:PMC2492495; PMID:11224527).
- ICOSL/B7-H2–ICOS costimulation output
  (PMID:10617205; PMID:16951355; PMCID:PMC7545189).
- ALCAM/CD166–CD6 adhesion and costimulation output
  (PMID:7760007; PMCID:PMC2192054; PMID:16352806).
- CEACAM1–TIM-3 inhibitory checkpoint output
  (PMID:25363763; PMCID:PMC4297519; DOI:10.1038/nature13848;
  DOI:10.1038/nature17421), retaining the corrected biophysical caveat.
- LSECtin/CLEC4G–LAG-3 melanoma immune-suppression output
  (PMID:24769443; DOI:10.1158/0008-5472.CAN-13-2690).
- Surfactant protein D–LAIR1 inhibitory reporter/ROS output
  (PMID:24585933; DOI:10.1189/jlb.3AB0213-092RR).

All ten records use the bounded route expression
`ligand>receptor>????>????>output`, with
`causal_status=not_asserted`, `traversal_status=evidence_route_not_causal`,
and no intracellular or TF edge fields populated. Output classes preserve the
reported evidence type, including gene-expression, cellular-function,
phosphorylation, secreted-protein, and reporter readouts.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 17,001 signaling-route evidence records
- 954 cumulative literature-expansion routes
- 924 covered downstream-curation queue candidates
- 2,407 remaining downstream-curation queue candidates
- 1,362 remaining P1 candidates
