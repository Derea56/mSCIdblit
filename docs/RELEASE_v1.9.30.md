# mSCIdblit v1.9.30

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The routes retain ligand--receptor--
output evidence, including receptor-proximal or cellular readouts where
available, while leaving intracellular continuation and transcription-factor
layers explicitly unasserted. They are available to mSCS as bounded
plausibility evidence and are not promoted to causal graph edges or database
confidence scores.

Added route families:

- Amyloid-beta–TREM2:DAP12:SYK microglial response
  (PMID:36306735; PMCID:PMC9625082; DOI:10.1016/j.cell.2022.09.033).
- Amyloid-beta–CD36-Fyn-p130Cas-Pyk2-paxillin migration pathway
  (PMID:17623670; DOI:10.1074/jbc.M702887200).
- Aβ fibrils–CD36:CD47:alpha6beta1 receptor-complex activation
  (PMID:12684452; PMCID:PMC6742111; DOI:10.1523/JNEUROSCI.23-07-02665.2003).
- EDIL3/DEL-1–alphaVbeta3 endothelial adhesion
  (PMCID:PMC529342).
- EDIL3/DEL-1–alphaVbeta6 latent TGF-beta modulation
  (PMCID:PMC7018852).
- EDIL3/DEL-1–Mac-1 complement-phagocytosis inhibition
  (PMCID:PMC4013214).
- ICAM1/CD54–LFA-1 leukocyte adhesion
  (PMID:3315233).
- PGD2–CRTH2/PTGDR2 leukocyte chemotaxis
  (PMID:11208866; DOI:10.1073/pnas.031554698).
- C3b–VSIG4/CRIg complement-opsonized particle clearance
  (PMID:16530040; DOI:10.1038/nature04358).
- iC3b–VSIG4/CRIg complement-opsonized particle clearance
  (PMID:16530040; DOI:10.1038/nature04358).

All ten records use the bounded route expression
`ligand>receptor>????>????>output`, with
`causal_status=not_asserted`, `traversal_status=evidence_route_not_causal`,
and no intracellular or TF edge fields populated. Output classes preserve the
reported evidence type, including generic functional, cellular functional,
gene-expression/transcription, and phagocytosis readouts. Receptor-complex,
species, topology, assay, and non-SCI limitations are retained in the evidence
records.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 17,031 signaling-route evidence records
- 984 cumulative literature-expansion routes
- 954 covered downstream-curation queue candidates
- 2,377 remaining downstream-curation queue candidates
- 1,332 remaining P1 candidates
