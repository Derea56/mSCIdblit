# Module 21A priority-8 batches 036-039 summary

Date: 2026-08-14

## Scope

Reviewed 100 priority-8 low/uncertain rows spanning opioid and calcitonin
receptors, CEACAM/CD immune-adhesion pairs, cadherins, claudins, CLCF1
receptor complexes, cholesterol/nuclear-receptor labels, and CLEC2/KLRB1
branches.

## Results

- 100 unique exact Module20A rows reviewed.
- 36 reusable relay/function candidates were retained.
- 14 binding-only cases were retained.
- 50 exact rows remain unresolved.
- Direct TF handoffs were retained for ATF2, RORA, RORC, and STAT3 only where
  matched receptor or ligand-receptor-complex studies directly measured the
  relevant downstream node.
- 100 stable batch evidence IDs were added to the detailed evidence register.

## Evidence-layer handling

Cadherin and claudin adhesion was not promoted to intracellular signaling
without receptor-dependent perturbation. Sterol-processing enzymes were not
treated as nuclear-receptor ligands; cholesterol/RORA/RORC evidence was kept
distinct from CEL or DHCR7 flux. CLCF1–CNTFR/LIFR was retained as a
receptor-complex edge with STAT3 support. CLEC2/KLRB1 species and nomenclature
boundaries were preserved.

The raw agent TSVs are retained as `module21a_batch036_review.tsv` through
`module21a_batch039_review.tsv`; the normalized combined review is
`module21a_pair_relay_review_batches036_039.tsv`.

## Files changed

- `module21a_all_pair_relay_coverage.tsv`
- `module22a_ligand_tf_handoff.tsv`
- `module21a_pathway_reuse_registry.tsv`
- `module21a_pair_relay_evidence_detail.tsv`
- `module21a_pair_relay_review_batches036_039.tsv`
- `module21a_pair_relay_batches036_039_summary.md`
- `module21a_all_pair_relay_handoff.md`

Module 20A ledgers and the frozen Module 20A release manifest were not
modified.
