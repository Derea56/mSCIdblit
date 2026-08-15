# Module 21A priority-8 batches 040-041 summary

Date: 2026-08-14

## Scope

Reviewed 50 priority-8 low/uncertain rows spanning CLEC/KLRB1 species
boundaries, CNTF/CLCF1 receptor complexes, contactin and collagen adhesion,
GPR126, corticosteroid and DHEA composites, CTSG/PAR/FPR branches, and
desmosterol/sterol receptor labels.

## Results

- 50 unique exact Module20A rows reviewed.
- 14 reusable relay/function candidates were retained.
- 3 binding-only or disarming-boundary cases were retained.
- 33 exact rows remain unresolved.
- Direct TF handoffs were retained for STAT3, NR3C1, and NR3C2 only where
  matched receptor-complex or direct nuclear-receptor studies supported them.
- 50 stable batch evidence IDs were added to the detailed evidence register.

## Evidence-layer handling

Receptor-complex shorthand (CNTFR/LIFR and LIFR/gp130) was preserved as a
complex/pathway edge, not split into unsupported binary receptor interactions.
Steroid-processing enzymes and desmosterol/DHEA biosynthesis labels were kept
separate from mature nuclear-receptor activation. CTSG PAR activation,
disarming, and FPR1 chemotaxis were recorded as distinct relations. Claudin,
contactin, and collagen adhesion evidence was not promoted to intracellular
signaling without matched perturbation.

The raw agent TSVs are retained as `module21a_batch040_review.tsv` and
`module21a_batch041_review.tsv`; the normalized combined review is
`module21a_pair_relay_review_batches040_041.tsv`.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches040_041.tsv`
- `module21a_pair_relay_batches040_041_summary.md`
- `module21a_all_pair_relay_handoff.md`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
