# mSCIdblit v1.9.32

Release date: 2026-09-17

This release adds ten selective primary-literature route annotations to the
Module 21B downstream evidence bundle. The batch extends traversable evidence
from ligand--receptor pairs into bounded JNK, ERK and SMAD-associated outputs,
while retaining receptor-complex and inflammatory readouts where the
intracellular continuation or terminal transcription-factor layer is not
resolved. These records are available to mSCS as plausibility evidence and are
not promoted to causal graph edges or database confidence scores.

Added route families:

- WNT5B–ROR2 paracrine JNK signaling with cytoneme-mediated complex transfer
  (PMCID:PMC10764289; DOI:10.1038/s41586-023-06850-7).
- FGF20–FGFR1c–ERK activation and mitogenic output (PMID:19564416).
- GDF11–ACVR2B:ALK5–SMAD2/3 activation and reporter output
  (PMID:29783655; PMCID:PMC5983757; DOI:10.3390/ijms19051508).
- FGF9–FGFR1c, FGF16–FGFR, FGF17b–FGFR and FGF18–FGFR ERK-associated
  outputs (PMID:25854632; DOI:10.1007/s00018-015-1856-8).
- IFNL3–IFNLR1:IL10RB receptor-complex activity and cellular response
  (PMID:28329704).
- IL-33–ST2:IL1RAP receptor-complex assembly and cellular signaling
  (PMID:19836339; PMCID:PMC2766095; PMID:17675517;
  DOI:10.1016/j.str.2009.08.009; DOI:10.4049/jimmunol.179.4.2551).
- Disulfide HMGB1–TLR4:MD2 inflammatory cytokine/chemokine output
  (PMID:25559892; PMCID:PMC4291531; DOI:10.1084/jem.20141318).

The records use route-specific tiers: six preserve a source-supported
intracellular continuation with TF/target-gene layers unresolved, three retain
ligand--receptor-to-output evidence without an assigned intracellular or TF
layer, and one retains a source-supported TF-associated output while the
intracellular continuation and target genes remain unresolved. All records
retain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`; context, species, assay,
isoform, receptor-complex and non-SCI limitations remain explicit.

Bundle totals:

- 11,952 nodes
- 14,722 retained graph edges
- 14,998 retained edge-source records
- 17,051 signaling-route evidence records
- 1,004 cumulative literature-expansion routes
- 974 covered downstream-curation queue candidates
- 2,357 remaining downstream-curation queue candidates
- 1,315 remaining P1 candidates
