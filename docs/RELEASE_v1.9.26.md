# mSCIdblit v1.9.26

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The routes retain ligand--receptor--
output evidence while leaving intracellular continuation and transcription
factor layers explicitly unasserted. They are available to mSCS as bounded
plausibility evidence and are not promoted to causal graph edges or database
confidence scores.

Added route families:

- GPNMB/alpha5beta1 adhesion and metastasis output
  (PMID:25772243; DOI:10.1038/onc.2015.8).
- ANGPTL4/alphaVbeta5 glomerular endothelial protection
  (PMID:24317117; PMCID:PMC4114723; DOI:10.1038/nm.3396).
- L1CAM/alphaVbeta3 adhesion and migration
  (PMID:8636223; PMCID:PMC2120722; DOI:10.1083/jcb.132.3.475).
- CDH26/alpha4beta7 mucosal adhesion
  (PMID:28051089; PMCID:PMC5496811; DOI:10.1038/mi.2016.120).
- T4/alphaVbeta3 MAPK and angiogenesis
  (PMID:15802494; DOI:10.1210/en.2005-0102).
- trans-resveratrol/alphaVbeta3 ERK-p53 apoptosis and angiostasis
  (PMID:16790523; PMID:19074851; DOI:10.1096/fj.06-5743fje;
  DOI:10.1158/1535-7163.MCT-07-2351).
- T3/alphaVbeta3 Src-PI3K-MAPK and proliferation
  (PMID:19158403; DOI:10.1111/j.1471-4159.2008.05889.x).
- DHT/alphaVbeta3 breast-cancer proliferation
  (PMID:19159686; DOI:10.1016/j.jsbmb.2008.12.010).
- JAML/CAR-dependent neutrophil transepithelial migration
  (PMID:15800062; PMCID:PMC2951132; DOI:10.1126/science.1187996).
- PVR/CD96-dependent NK-cell adhesion and cytotoxicity
  (PMID:15034010; PMID:19056733; DOI:10.4049/jimmunol.172.7.3994;
  DOI:10.1074/jbc.M807698200).

All ten records use the bounded route expression
`ligand>receptor>????>????>output`, with
`causal_status=not_asserted`, `traversal_status=evidence_route_not_causal`,
and no intracellular or TF edge fields populated. Output classes remain
specific to the reported readout, including cellular function, localization,
and phosphorylation/activation evidence.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 16,991 signaling-route evidence records
- 944 cumulative literature-expansion routes
- 914 covered downstream-curation queue candidates
- 2,417 remaining downstream-curation queue candidates
- 1,372 remaining P1 candidates
