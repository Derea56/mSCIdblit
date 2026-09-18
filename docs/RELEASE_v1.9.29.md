# mSCIdblit v1.9.29

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The routes retain ligand--receptor--
output evidence while leaving intracellular continuation and transcription
factor layers explicitly unasserted. They are available to mSCS as bounded
plausibility evidence and are not promoted to causal graph edges or database
confidence scores.

Added route families:

- Teneurin-2–Latrophilin-1 trans-cellular adhesion output
  (PMID:24273166; PMCID:PMC3879561; DOI:10.1074/jbc.M113.504779).
- Teneurin-4–Latrophilin-1 trans-cellular adhesion output
  (PMID:24273166; PMCID:PMC3879561; DOI:10.1074/jbc.M113.504779).
- Teneurin-4–Latrophilin-2 trans-cellular adhesion output
  (PMID:24273166; PMCID:PMC3879561; DOI:10.1074/jbc.M113.504779).
- Teneurin-4–Latrophilin-3 trans-cellular adhesion output
  (PMID:24273166; PMCID:PMC3879561; DOI:10.1074/jbc.M113.504779).
- Chondroitin sulfate–EMR2 calcium/sulfation-dependent attachment output
  (PMID:12829604; DOI:10.1182/blood-2002-11-3540).
- Chondroitin sulfate–CD97 extracellular attachment output
  (PMID:12829604; DOI:10.1182/blood-2002-11-3540).
- C1QL3–BAI3 neuronal adhesion and synapse-density output
  (PMID:21262840; PMCID:PMC3038708; DOI:10.1073/pnas.1019577108;
  PMID:33337553; PMCID:PMC11565477).
- WNT7B–GPR124/RECK/LRP5/6 beta-catenin reporter output
  (PMID:40914247; PMCID:PMC12514574; DOI:10.1016/j.jbc.2025.110682).
- FLRT2–Latrophilin-2 endothelial adhesion/barrier output
  (PMID:34581723; PMCID:PMC8480966; DOI:10.1083/jcb.202006033).
- IL-9–IL2RG receptor-complex growth output
  (PMID:7718508; DOI:10.1093/intimm/7.1.115).

All ten records use the bounded route expression
`ligand>receptor>????>????>output`, with
`causal_status=not_asserted`, `traversal_status=evidence_route_not_causal`,
and no intracellular or TF edge fields populated. Output classes preserve the
reported evidence type, including adhesion, generic functional, cellular
functional, and reporter readouts. Isoform, domain, receptor-complex, species,
and assay limitations are retained in the evidence records.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 17,021 signaling-route evidence records
- 974 cumulative literature-expansion routes
- 944 covered downstream-curation queue candidates
- 2,387 remaining downstream-curation queue candidates
- 1,342 remaining P1 candidates
