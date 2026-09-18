# mSCIdblit v1.9.33

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The batch expands traversable
ligand--receptor-to-output evidence for EphB4/ephrin-B2, atypical chemokine
receptors, semaphorin and Robo guidance, integrin engagement, and selectin
adhesion. These records are available to mSCS as plausibility evidence and are
not promoted to causal graph edges or database confidence scores.

Added route families:

- Ephrin-B2--EphB4 vascular-development output (PMID:16867992;
  PMID:10518221).
- CXCL12--ACKR3/CXCR7 beta-arrestin and chemokine-scavenging output
  (PMCID:PMC5217689; PMID:27875312; DOI:10.1074/jbc.M116.762252).
- CCL19--ACKR4 and CCL21--ACKR4 scavenging with immune-cell trafficking
  outputs (PMID:26976955; PMID:33875601; PMCID:PMC8092586).
- SEMA3F--NRP2/Plexin-A guidance output (PMCID:PMC2868107;
  PMID:15721238; PMID:26319580).
- NELL2--ROBO3 commissural-axon guidance output (PMID:32198364;
  PMCID:PMC7083938).
- Fibronectin--alpha5beta1 and laminin-511--alpha6beta1 integrin engagement
  and receptor-proximal output (PMID:12970173; PMID:33962943;
  PMCID:PMC8104898; DOI:10.1126/sciadv.abe9716; PMID:34188035).
- E-selectin--PSGL1 and L-selectin--PSGL1 glycoform-dependent leukocyte
  tethering and rolling outputs (PMID:8621728; PMID:9128259; PMID:11071658;
  PMID:8892633; PMID:12403782).

All ten records use the receptor-to-functional-output tier with unresolved
intracellular, transcription-factor, and target-gene layers. The records keep
`causal_status=not_asserted` and `traversal_status=evidence_route_not_causal`,
and preserve receptor-complex, glycoform, ligand-processing, species, assay,
and non-SCI context limitations.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 17,061 signaling-route evidence records
- 1,014 cumulative literature-expansion routes
- 984 covered downstream-curation queue candidates
- 2,347 remaining downstream-curation queue candidates
- 1,315 remaining P1 candidates
