# Cross-module path linkage batch 02: TNF/TNFR1/TNFR2→NF-κB

This batch links existing Module 20B TNF receptor candidates to Module 21B
TNFR1/TNFR2 relays and Module 22B RELA/NF-κB/NFKB2 records. It is an
audit-layer linkage table, not canonical SignalingEdge materialization.

## Batch result

- 6 linkage records were added.
- 1 TNFR1 path is supported across the 21A and 22A layers through canonical
  NF-κB/RELA and FAS regulation, while the 20B LR candidate remains a boundary.
- 1 TNFR2→RELA record remains receptor-specificity unresolved at the terminal
  step.
- 1 TNFR2→NFKB2/RELB branch is supported by 21B and a supplemental TNFR2-selective
  primary study, but no 22B TNFR2-specific terminal record was assigned.
- 2 TNFR2 functional CNS/SCI records remain separate from terminal TF evidence.
- 1 TNF-p100/NFKB2 modulation record is retained as a contextual branch because
  the exact TNFR1/TNFR2 assignment is unresolved.
- No Module 20A LR classification or frozen manifest was changed.

## Layer and branch handling

Canonical RELA and alternative NFKB2/RELB branches are not collapsed. The
TNFR1 TRADD/TRAF2/RIPK1 pathway is kept distinct from the TNFR2 TRAF2 relay,
and the TNFR2 functional records do not become direct RELA or NFKB2 edges.

## Supplemental primary-literature search

The focused search added four supplemental evidence records:

- TNF-induced FAS regulation depends on RelA-containing NF-κB complexes in
  primary/comparator systems (PMID 11290773).
- TNF induces a broader NF-κB/RelA target network with selected promoter binding
  supported by ChIP (PMID 15722553).
- TNFR2-selective ligation induces NFKB2 and RELB and promotes RelB nuclear
  translocation in human T cells (PMID 30104686).
- TNF modulates Nfkb2/p100 and noncanonical NF-κB signaling in inflamed mouse
  lymphoid/stromal systems (PMID 29061763).

These records are supplemental intake candidates and are not silently promoted
into Module 21A or 22A registers.

Full linkage details are in
`module20_24_path_linkage_batch02_tnf_nfkb.tsv`.

Supplemental records and mappings are in
`module20_24_path_linkage_batch02_external_evidence.tsv` and
`module20_24_path_linkage_batch02_external_evidence_links.tsv`.
