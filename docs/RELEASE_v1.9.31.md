# mSCIdblit v1.9.31

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The routes retain ligand--receptor--
output evidence across growth-factor, neural, immune, chemokine and cytokine
contexts while leaving intracellular continuation and transcription-factor
layers explicitly unasserted. They are available to mSCS as bounded
plausibility evidence and are not promoted to causal graph edges or database
confidence scores.

Added route families:

- FGF8b–FGFR4 receptor activation and mitogenic output
  (PMID:16597617; PMCID:PMC2080618; DOI:10.1074/jbc.M601252200;
  PMID:10736564).
- EGFL7–NOTCH1 Notch antagonism and neural stem-cell renewal
  (PMID:19503073; DOI:10.1038/ncb1896).
- RAET1G/ULBP5–NKG2D NK-cell degranulation and receptor downregulation
  (PMID:19424970; DOI:10.1002/eji.200839074; PMID:15240696).
- RAET1L/ULBP6–NKG2D NK-cell killing and degranulation
  (PMID:19658097; DOI:10.1002/eji.200939502).
- ICAM5–alpha5beta1 neuronal adhesion and synapse maturation
  (PMID:22433866; PMCID:PMC3603512; DOI:10.1242/jcs.101030).
- SEMA4A–NRP1 regulatory T-cell survival and suppressive function
  (PMID:23913274; PMCID:PMC3867145; DOI:10.1038/nature12428).
- CCL12/MCP-5–CCR2 monocyte chemotaxis and recruitment
  (PMID:18334747).
- Persephin–GFRA4:RET receptor-complex activation and neuronal survival
  (PMID:11116144).
- Reelin–EPHB2 noncanonical neuronal receptor crosstalk
  (PMID:23318582; PMCID:PMC3616423).
- OSM–gp130:LIFR receptor-complex activation
  (PMID:8999038; PMID:10586060).

All ten records use the bounded route expression
`ligand>receptor>????>????>output`, with
`causal_status=not_asserted`, `traversal_status=evidence_route_not_causal`,
and no intracellular or TF edge fields populated. Output classes preserve the
reported evidence type, including phosphorylation/activation, reporter,
gene-expression/transcription and cellular functional readouts. Isoform,
receptor-complex, species, assay, crosstalk and non-SCI limitations are
retained in the evidence records.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 17,041 signaling-route evidence records
- 994 cumulative literature-expansion routes
- 964 covered downstream-curation queue candidates
- 2,367 remaining downstream-curation queue candidates
- 1,322 remaining P1 candidates
