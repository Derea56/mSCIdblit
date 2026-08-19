# Module 24A saturation tranche 014

This tranche performed an evidence-association accuracy audit on the legacy
Module 18 reuse block before further saturation promotions. The audit found an
off-by-one pattern in the first legacy evidence associations: several stable
evidence records were valid records but were attached to the wrong Module 24A
edge. The source records themselves were preserved; only their edge references
were repaired.

## Association repairs

- Repaired the foam-cell/C1q and C1q/synaptic-engulfment associations so both
  functional edges point to the two validated primary SCI records.
- Reattached the myelin-debris/TREM2 evidence to the TREM2 edge.
- Reattached activated-protein-C/histone evidence to the APC edge.
- Reattached LTB4/BLT1, 5-LO/CysLT1-context, RvD3, RvD1, ATP/P2X7R,
  P2X7R-function, and extracellular-trap/LL37 evidence to their matching
  edges.
- Split the P2Y12R ATP-to-adenosine study across its receptor-proximal relay
  and downstream mitophagy edges, while retaining the multi-step attribution
  limitation.

No new biological edge or evidence record was created, and no matrix status was
promoted in this tranche. This was deliberate: the priority was to make the
existing evidence-to-edge map trustworthy before further disposition work.

## Validation disposition

- 151 edges, 200 evidence records, 172 edge/evidence associations, 189 matrix
  rows, 31 explicit no-evidence boundaries, and 0 perturbation rows.
- 0 unsupported edges after reload.
- 0 duplicate edge keys.
- Stable evidence IDs and edge IDs remain unique.
- Register widths remain exact.
- The isolated PostgreSQL staging reload passed all embedded assertions.
- The frozen Module 20A LR manifest SHA256 remains
  `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Search and interpretation boundary

This tranche corrected association metadata only. It does not convert pathway
or functional evidence into direct binding claims, does not collapse receptor,
relay, and downstream layers, and does not modify the frozen Module 20A LR
ledger. The remaining first-pass rows retain their stated unresolved receptor,
species, model-transfer, and specificity gaps for the next review batch.
