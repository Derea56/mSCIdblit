# Module 24A Saturation Tranche 005

Date: 2026-08-18

## Scope

This tranche revisits three high-value first-pass gaps without changing any
Module 20A LR classification or prior-module ledger:

- BDKRB1/des-Arg9-bradykinin in SCI-associated autonomic/bladder dysfunction;
- C3a/C3aR1 downstream signaling in spinal neural stem cells after SCI;
- RvD1/GPR32 receptor pharmacology and proresolution function.

## Additions

Six edges and six primary-paper evidence records were added:

- `M24A-E131` — C3aR1 to the NF-kB p65/Nrf2/UCHL1-proteasome downstream relay;
- `M24A-E132` — C3a/C3aR1 suppression of spinal cord neural-stem-cell activation;
- `M24A-E133` — des-Arg9-bradykinin pharmacologic activation of BDKRB1 after SCI;
- `M24A-E134` — BDKRB1-associated post-SCI overactive-bladder functional output;
- `M24A-E135` — human RvD1 activation of GPR32/DRV1;
- `M24A-E136` — GPR32-associated proresolution phagocytosis and leukocyte-resolution output.

Stable primary sources:

- C3a/SCI NSC pathway: PMID 41044292; PMCID PMC12789345; DOI 10.1007/s12264-025-01488-z.
- Kinin B1/B2 receptors after SCI: PMID 22862305; PMCID PMC3525875; DOI 10.1111/j.1476-5381.2012.02127.x.
- RvD1/GPR32 receptor pharmacology: PMID 22449948; PMCID PMC3349829; DOI 10.1016/j.ajpath.2012.01.028.

## Promotions and limits

- `M24A-Q0002` is promoted to supported-with-pair-limit: BDKRB1 pharmacology
  and post-SCI bladder function are supported, but purified binding,
  endogenous kallikrein processing, and lesion-core receiver attribution are
  unresolved.
- `M24A-Q0003` now includes the C3aR1-dependent NF-kB p65/Nrf2/UCHL1 neural
  stem-cell relay; C5aR2, cross-receptor assignments, and intact precursor
  edges remain unresolved.
- `M24A-Q0065` is promoted to supported-with-pair-limit for human GPR32;
  SCI-specific GPR32 causality and rodent GPR32 orthology remain unresolved.
- The prior BDKRB1 and GPR32 no-evidence records were retained and narrowed;
  they now document the remaining molecular/species/SCI boundaries rather than
  asserting absence of all evidence.
- The C3a ChIP result for Nrf2-to-UCHL1 is retained as contextual evidence for
  Module 22A and is not promoted as a direct Module 24A receptor edge.

## Files changed

- `work/module24a/module24a_edge_register.tsv`
- `work/module24a/module24a_evidence_register.tsv`
- `work/module24a/module24a_saturation_matrix.tsv`
- `work/module24a/module24a_first_pass_queue_summary.md`
- `work/module24a/module24a_saturation_batch005_summary.md`

The audit-layer SQL staging artifact was updated to the new 136-edge/185-evidence
counts, but no canonical database load or commit was performed in this tranche.
