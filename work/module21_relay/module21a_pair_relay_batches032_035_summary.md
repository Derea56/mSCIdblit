# Module 21A priority-8 batches 032-035 summary

Date: 2026-08-14

## Scope

Reviewed 100 priority-8 low/uncertain rows spanning acetylcholine and
nicotinic/muscarinic receptors, adenosine receptors, adrenergic receptors,
activin receptor complexes, steroid receptors, annexin/FPR branches, and
apolipoprotein/TREM2 or related receptor complexes.

## Results

- 100 unique exact Module20A rows reviewed.
- 84 reusable relay/function candidates were retained.
- 1 binding-only case was retained: 5alphaP-DHRS9–Pgr.
- 15 exact rows remain unresolved.
- Three direct TF handoffs were retained from batch035: NR3C2, SMAD1/5/8,
  and AR. Activin SMAD2 phosphorylation was not assigned as an exact TF
  handoff where receptor-subtype composition was not isolated.
- 100 stable batch evidence IDs were added to the detailed evidence register.

## Evidence-layer handling

Acetylcholine synthesis/storage/transport, adenosine metabolism/transport,
catecholamine storage, and ligand-processing enzymes were kept distinct from
receptor activation. Muscarinic, nicotinic, adenosine, adrenergic, activin,
steroid, annexin/FPR, and apolipoprotein receptor-complex branches were
recorded at the molecular or proximal-relay scope actually supported by the
primary studies. TF assignments were withheld when the exact queued receptor
complex was not selectively isolated.

The raw agent TSVs are retained as `module21a_batch032_review.tsv` through
`module21a_batch035_review.tsv`; the normalized combined review is
`module21a_pair_relay_review_batches032_035.tsv`.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches032_035.tsv`
- `module21a_pair_relay_batches032_035_summary.md`
- `module21a_all_pair_relay_handoff.md`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
