# Module 21A Batch 186 review summary

Batch 186 reviews exactly the 25 supplied filtered-queue ordinals **4101–4125**, corresponding to M20A-LIANA-REMAINING-0373 through M20A-LIANA-REMAINING-0397, in the supplied order. The raw artifact is module21a_batch186_review.tsv and uses the exact 13-column batch-review schema.

## Disposition

| status | count |
|---|---:|
| no_evidence_boundary | 25 |
| **total** | **25** |

All 25 rows have unique queue-derived review IDs and unique canonical pair labels. Confidence is **low** for every row, and every terminal_TF value is the literal null.

## Evidence decisions

The existing Module20A adjudication packet at work/module20_db_seed/evidence_search_agents/liana_remaining_adjudication.tsv was used as the bounded exact-pair baseline. It records no_evidence for every requested WNT-FZD-LRP composite after expanded exact-pair searches, with no established exact-pair species support.

Primary comparator sources were retained only to document the search boundary:

- Wang et al. established WNT7B signaling through FZD1/FZD10 with LRP5 in mouse developmental cell systems (PMID:15923619; PMCID:PMC1140585; DOI:10.1128/MCB.25.12.5022-5030.2005).
- WNT1/LRP5 and LRP5-dependent Lef1/beta-catenin responses were used as separate LRP5 component comparators (PMID:11956231; PMCID:PMC2199263; DOI:10.1083/jcb.200201089).
- WNT-FZD/LRP6 receptor-association and signaling studies were used as different-ligand or different-FZD comparators (PMID:11029007; DOI:10.1038/35035117; PMID:35513706; PMCID:PMC9072438; DOI:10.1038/s42003-022-03370-4).
- The WNT10B-FZD6-LRP6 study was retained only as a different-ligand FZD6/LRP6 comparator where relevant (PMID:34769487; PMCID:PMC8584856; DOI:10.3390/ijms222112057).

These sources do not establish any requested Wnt2b- or Wnt3-specific ternary complex. Evidence for another WNT ligand, another FZD subtype, LRP5 or LRP6 alone, generic pathway membership, expression, engineered surrogate systems, reporter output, or beta-catenin function was not combined into direct binding, receptor activation, or an exact relay claim. No WNT-FZD-LRP composite was promoted to a relay candidate, and no pathway output was handed off as a terminal TF.

Module20A ledgers, the adjudication packet, shared Module21A coverage/handoff registers, and integration outputs were preserved. Only this requested TSV and summary were written; no commit was created.

