# Module 21A priority-7 batches 012-013 summary

Date: 2026-08-14

## Scope

Reviewed all 22 priority-7 high/medium rows M20A-EXT-0516 through 0616 that
were selected for this pass. The rows cover C1QL/BAI3, cholesterol/RORA,
collagen and laminin matrix pairs, DSPP, fibronectin/SDC4, MMP2/MT1-MMP/
alphaVbeta3, NCAM/L1, nephronectin/alpha8beta1, netrin-4/UNC5, THBS2/SDC4,
and VWF/GPIb-IX-V.

## Results

- 22 exact ligand-receptor or receptor-complex rows reviewed.
- 15 reusable Module 21A relay/function candidates added.
- 6 rows retained as binding-only or unresolved boundaries:
  C1QL2-BAI3, cholesterol-DHCR24-RORA, LAMA1-alpha1beta1,
  LAMA2-alpha1beta1, LAMA5-alpha1beta1, and LAMA5-SV2A. The exact status
  for each row is in the review TSV.
- 1 row retained as no exact downstream evidence:
  COL1A1-SDC4.
- 22 stable batch evidence IDs added to the detailed evidence register.
- One directly measured ELK1 activation readout from processed DSPP/DPP-
  alphaVbeta1 evidence was handed to Module22A. CREB and RORA observations
  were not assigned to the frozen exact pairs because receptor attribution or
  the composite pair was unresolved.

## Evidence-layer handling

Direct binding, receptor-complex/proximal relay, and downstream cellular
function remain distinct in the detailed evidence fields. Shared NPNT rows
are linked to separate pair-level records but explicitly retain the caveat
that the two queue “complex” labels are not independently molecularly
resolved. NTN4-UNC5B is represented as recruitment into a neogenin-UNC5B
complex, not as isolated NTN4-UNC5B binding. Matrix-family, laminin-fragment,
SV2-family, and composite cholesterol-DHCR24-RORA observations were not
promoted beyond their exact evidence scope.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches012_013.tsv`
- `module21a_all_pair_relay_handoff.md`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
