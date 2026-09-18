# mSCIdblit v1.9.34

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations from the
highest-priority unresolved downstream queue. The batch expands evidence for
soluble decoy and antagonist proteins, BMP receptor context, and extracellular
ligand sequestration. These routes are available to mSCS as plausibility
evidence; they do not create causal graph edges or database confidence scores.

Added route families:

- IL-18--IL-18BP soluble decoy binding and IFN-gamma inhibition
  (PMID:18797176; PMID:10655506; PMID:10023777).
- BMP6--ACVR1/ALK2 type-II-receptor-context activation and Smad-associated
  osteogenic output (PMID:10504300; DOI:10.1242/jcs.112.20.3519).
- GREM1 antagonism of BMP2, BMP4 and BMP7, retaining the measured affinity
  ranking and BMP-pathway output modulation (PMID:25378054;
  DOI:10.1042/BJ20140771).
- Glycosylation-dependent TWSG1--BMP2 binding and craniofacial BMP-modulation
  output (PMID:21941513; PMCID:PMC3170884).
- Chordin--BMP4 receptor-competition output (PMCID:PMC3070603;
  PMCID:PMC2280033).
- USAG1/SOSTDC1--BMP7 renal-protection modulation (PMCID:PMC1307562).
- Full-length Cerberus--BMP4 neutralization (PMCID:PMC2323273).
- PRDC/GREM2--BMP2 binding and BMP-responsive reporter inhibition
  (PMID:22381466; PMCID:PMC3319168; PMID:15039429).

All ten records remain in the receptor-to-functional-output tier. Soluble
antagonists and decoys are explicitly retained as extracellular modulation
evidence rather than being treated as productive transmembrane receptors.
Intracellular, transcription-factor, and terminal target-gene layers remain
unresolved where the primary studies do not establish them. Every record keeps
`causal_status=not_asserted` and `traversal_status=evidence_route_not_causal`.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 17,071 signaling-route evidence records
- 1,024 cumulative literature-expansion routes
- 994 covered downstream-curation queue candidates
- 2,337 remaining downstream-curation queue candidates
- 1,305 remaining P1 candidates
