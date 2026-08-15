# Module 21A evidence review — Batch 177

## Scope

This bounded review covers only Batch 177, filtered queue ordinals 3876–3900:
25 exact Module20A LIANA-remaining rows, `M20A-LIANA-REMAINING-0148` through
`M20A-LIANA-REMAINING-0172`. The raw output is
[`module21a_batch177_review.tsv`](./module21a_batch177_review.tsv) and uses the
requested 13-column schema exactly:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

Module20A files, the frozen queue, and shared Module21A/Module22A registers
were read-only context. No shared register or Module20A file was modified.

## Disposition

| disposition | count | rows |
|---|---:|---|
| reviewed_relay_candidate | 16 | 0148–0151, 0155–0156, 0158, 0160–0168 |
| reviewed_unresolved | 4 | 0152–0154, 0159 |
| no_evidence_boundary | 5 | 0157, 0169–0172 |
| total | 25 | exact requested batch |

Confidence counts: high 6; medium-high 3; medium 3; medium-low 4; low 9.

## Evidence-layer rules applied

- `binding_activation` records ligand binding, receptor engagement, or
  activation evidence only.
- `receptor_proximal_relay` records receptor-complex/adaptor/kinase relay
  evidence only when supported by perturbation, reconstitution, structural,
  or receptor-dependent assays.
- `downstream_pathway_function` records measured pathway or functional outputs
  separately from the ligand-receptor claim.
- A pathway or phenotype result was never used by itself to infer a direct
  ligand-receptor interaction.
- `terminal_TF` is `null` unless a TF endpoint was explicitly assigned from the
  reviewed evidence. STAT3 is assigned only for IL-10 because receptor-domain
  recruitment and STAT3-dependent promoter output were directly tested.

## Main findings

- Strong exact or near-exact relay support was retained for HGF–MET, IL-10–
  IL10RA/IL10RB, IL-17B–IL17RB in an IL17RA-dependent context, IL-17C–
  IL17RA/IL17RE, IL-1α/β–IL1R1/IL1RAP, IL-20/IL-24/IL-19–IL20RA/IL20RB,
  and IL-25–IL17RA/IL17RB.
- GDF6/GDF7 receptor-panel studies support SMAD1/5/8 BMP signaling and the
  submitted BMPR1A/B–BMPR2 contexts at low-to-medium confidence, but the
  experiments are mainly recombinant/reconstituted rather than native SCI
  receiver models.
- GDF9–ACVR1B/BMPR2 remains unresolved: the primary literature supports a
  BMPR2/ALK5-family model but does not isolate the exact submitted ACVR1B
  complex.
- GRN–TNFRSF1A and GRN–TNFRSF1B remain unresolved because positive direct-
  binding/antagonism results conflict with a later primary cellular-binding
  study that found no relevant PGRN-TNFR binding or competition.
- HB-EGF directly binds/activates EGFR/HER4, while ErbB2 phosphorylation is a
  partner-level receptor-complex readout. It was not treated as proof of a
  standalone HB-EGF–ErbB2 binary interaction or a purified submitted ternary
  complex.
- HRG (`Hc`)–C5AR1 has no qualifying exact primary binding, activation, relay,
  or receptor-dependent functional evidence in the bounded search. Primary HRG
  binding to plasminogen/C1q was retained only as a negative boundary.
- IFNA11–IFNAR1/IFNAR2 is unresolved at subtype level: family type-I
  interferon receptor evidence does not establish the submitted rare subtype.
- All four INHBC composite receptor rows remain explicit no-evidence
  boundaries; activin/inhibin/GDF family or expression/pathway evidence was not
  transferred to INHBC-specific complexes.

## Limitations and handoff boundary

Most positive relay evidence comes from recombinant, engineered-cell, epithelial,
immune, ovarian, cardiac, or developmental systems rather than spinal-cord
injury receiver cells. Ligand processing, receptor stoichiometry, co-receptor
requirements, species differences, and cell-state dependence are recorded in
each row’s `limitations` field. No Module22A terminal-TF program or SCI-specific
functional claim should be created from these rows without a separate TF-level
review.

## Validation target

The TSV should contain one header plus exactly 25 data rows, 25 unique review
IDs matching the requested queue slice, 13 fields per row, populated
limitations in every row, and literal `null` in `terminal_TF` for rows without
an assigned TF.
