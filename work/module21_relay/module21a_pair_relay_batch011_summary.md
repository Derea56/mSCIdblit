# Module 21A priority-6 batch 011 summary

Date: 2026-08-14

## Scope

Reviewed the exact Module 20A priority-6 rows M20A-EXT-0470, 0472, 0477,
0479, 0482-0485, 0487, 0489, 0503, and 0506-0515. The batch covers
THBS2/THBS4, TNC/TNN, TNXB, VCAM1, VTN, and VWF receptor assignments.

## Results

- 21 exact ligand-receptor pairs reviewed.
- 17 reusable Module 21A relay/function candidates added.
- 3 cases retained as unresolved or negative-boundary evidence:
  THBS2-CD47, THBS4-CD47, and TNN-alpha8beta1.
- 1 case retained as binding-only with no downstream relay:
  TNXB-alphaVbeta3.
- 21 stable batch evidence IDs added to the detailed evidence register.
- No terminal TF activation candidate added. NF-kB, FAK/Src, MAPK, and
  related pathway readouts remain pathway-level evidence; they are not
  promoted to Module 22A TF-target programs.

## Evidence-layer handling

Binding-only and unresolved rows remain in the ligand-receptor evidence layer.
Validated relay/function candidates are represented in the downstream pathway
or cellular-function layer, with receptor-proximal adhesion and complex
evidence kept in the relation field. Presentation-dependent fragments,
cryptic motifs, multimeric vWF, matrix context, and uPAR-integrin composite
complexes are retained as explicit limitations.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batch011.tsv`
- `module21a_all_pair_relay_handoff.md`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
