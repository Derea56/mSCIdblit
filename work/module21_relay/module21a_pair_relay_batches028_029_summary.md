# Module 21A priority-8 batches 028-029 summary

Date: 2026-08-14

## Scope

Reviewed the first 50 priority-8 low/uncertain CellChat-derived rows, covering
2-AG, 22(R)-hydroxycholesterol, dopamine/serotonin processing branches, and
multiple serotonin receptor subtypes.

## Results

- 50 unique exact Module20A rows reviewed.
- Batch028: 8 receptor-relay candidates, 2 downstream functional-output cases,
  and 15 unresolved cases.
- Batch029: 25 receptor-relay candidates across Gi/o, Gq/11, Gs, and HTR3
  cation-channel branches.
- No terminal TF was directly measured in either batch.
- 50 stable batch evidence IDs were added to the detailed evidence register.

## Evidence-layer handling

Metabolite-processing enzymes and transporters were not treated as signaling
receptors. 2-AG–CB1/CB2 evidence was separated from conflicting GPR55
pharmacology. Serotonin receptor subtype pharmacology was recorded as
receptor-proximal relay; the upstream TPH/DDC/SLC18A/SLC6A4 labels were kept as
ligand-production or transport context, not direct receptor evidence. No TF
was assigned from GPCR branch identity alone.

The raw agent TSVs are retained as `module21a_batch028_review.tsv` and
`module21a_batch029_review.tsv`; the normalized combined review is
`module21a_pair_relay_review_batches028_029.tsv`.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches028_029.tsv`
- `module21a_pair_relay_batches028_029_summary.md`
- `module21a_all_pair_relay_handoff.md`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
