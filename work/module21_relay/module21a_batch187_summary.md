# Module 21A Batch 187 review summary

Batch 187 reviews exactly filtered queue ordinals **4126–4150**: 25 priority-8,
low/uncertain Module20A LIANA-remaining rows, in the supplied order. The raw
artifact is `module21a_batch187_review.tsv` and uses the exact 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

## Disposition

| status | count |
|---|---:|
| `reviewed_unresolved` | 12 |
| `no_evidence_boundary` | 13 |
| **total** | **25** |

Confidence counts: low 13; low-medium 12. Every `terminal_TF` value is the
literal `null`.

## Queue alignment

| filtered ordinal | review ID range | pairs |
|---:|---|---|
| 4126–4137 | `M20A-LIANA-REMAINING-0398`–`0410` | Wnt3 Fzd4_lrp5; Wnt3 Fzd4_lrp6; Wnt3 Fzd5_lrp5; Wnt3 Fzd5_lrp6; Wnt3 Fzd6_lrp5; Wnt3 Fzd6_lrp6; Wnt3 Fzd7_lrp5; Wnt3 Fzd7_lrp6; Wnt3 Fzd8_lrp5; Wnt3 Fzd8_lrp6; Wnt3 Fzd9_lrp5; Wnt3 Fzd9_lrp6; Wnt3a Fzd10_lrp5 |
| 4138–4150 | `M20A-LIANA-REMAINING-0410`–`0422` | Wnt3a Fzd10_lrp5; Wnt3a Fzd10_lrp6; Wnt3a Fzd1_lrp5; Wnt3a Fzd1_lrp6; Wnt3a Fzd2_lrp5; Wnt3a Fzd2_lrp6; Wnt3a Fzd3_lrp5; Wnt3a Fzd3_lrp6; Wnt3a Fzd4_lrp5; Wnt3a Fzd4_lrp6; Wnt3a Fzd5_lrp5; Wnt3a Fzd5_lrp6; Wnt3a Fzd6_lrp5 |

## Evidence decisions

- The adjudication packet at
  `work/module20_db_seed/evidence_search_agents/liana_remaining_adjudication.tsv`
  was used as the bounded exact-pair baseline. Its exact rows classify
  Wnt3-Fzd4/5/6-LRP5/6, Wnt3-Fzd9-LRP5/6, Wnt3A-Fzd10-LRP5/6, Wnt3A-Fzd2-LRP5,
  and Wnt3A-Fzd4-LRP5 as `no_evidence`; the remaining retained rows are
  `manual_review` or `low_evidence` because FZD-level or cell-context evidence
  exists while the submitted LRP suffix remains unresolved.
- The primary multiplex CRISPR/rescue study (PMID:28733458) supports functional
  WNT3 or WNT3A responses through selected FZD paralogs in human cells. It does
  not isolate the submitted LRP5-versus-LRP6 component for the Wnt3-Fzd7,
  Wnt3-Fzd8, Wnt3A-Fzd1, Wnt3A-Fzd3, or Wnt3A-Fzd6 rows. Those 9 rows therefore
  remain `reviewed_unresolved`, not direct ternary binding claims.
- The primary WNT3A-FZD mapping study (PMID:25605717; PMCID:PMC4358105;
  DOI:10.1074/jbc.M114.612648) directly measured WNT3A-FZD2, FZD4, and FZD5
  CRD binding and cell-based signaling with endogenous LRP5/6, including LRP6
  phosphorylation. This supports the FZD2/4/5 receptor-proximal context for
  the three LRP6 rows, but does not isolate an exact full-length
  WNT3A-FZD-LRP6 complex; the LRP5 counterparts remain boundary outcomes.
- PMID:12121999 and PMID:25902418 were used as primary co-receptor and
  receptor-complex boundary sources. Their LRP/FZD findings were not combined
  with a different WNT ligand or FZD subtype to promote an exact submitted
  WNT-FZD-LRP composite. Generic pathway, expression, database, family, or
  beta-catenin evidence was not promoted to direct binding.

## Limitations and handoff boundary

The retained rows are low-confidence FZD-level or endogenous-LRP5/6 functional
contexts, not universal mammalian or SCI receiver mechanisms. Exact ternary
binding, full-length receptor stoichiometry, LRP5-versus-LRP6 selectivity,
ligand presentation, species, and cell context remain unresolved wherever
stated. Reporter and beta-catenin readouts are not terminal-TF measurements.
No terminal TF assignment is made.

Only the requested batch TSV and this summary were written. Module20A files,
the adjudication packet, shared Module21A/Module22A ledgers, coverage tables,
and integration outputs were not modified. No commit was created.
