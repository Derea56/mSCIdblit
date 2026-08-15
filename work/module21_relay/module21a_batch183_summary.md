# Module 21A Batch 183 review summary

Batch 183 reviews exactly filtered queue ordinals **4026–4050**: 25 priority-8,
low/uncertain Module20A LIANA-remaining rows, in the supplied order. The raw
artifact is `module21a_batch183_review.tsv` and uses the exact 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 1 |
| `no_evidence_boundary` | 24 |
| **total** | **25** |

Confidence counts: low 24; low-medium 1. Every `terminal_TF` value is the
literal `null`.

## Queue alignment

| filtered ordinal | review ID range | pairs |
|---:|---|---|
| 4026–4027 | `M20A-LIANA-REMAINING-0298`–`0299` | Wnt10a Fzd9_lrp5; Wnt10a Fzd9_lrp6 |
| 4028–4047 | `M20A-LIANA-REMAINING-0300`–`0319` | Wnt10b Fzd10/Fzd1/Fzd2/Fzd3/Fzd4/Fzd5/Fzd6/Fzd7/Fzd8/Fzd9 with Lrp5 or Lrp6, including the exact Fzd6_lrp6 exception at ordinal 4041 |
| 4048–4050 | `M20A-LIANA-REMAINING-0320`–`0322` | Wnt11 Fzd10; Wnt11 Fzd2; Wnt11 Fzd3 |

## Evidence decisions

- The existing adjudication packet at
  `work/module20_db_seed/evidence_search_agents/liana_remaining_adjudication.tsv`
  was used as the bounded exact-pair baseline. It records 24 `no_evidence`
  outcomes and one `low_evidence` outcome for Wnt10b Fzd6_lrp6.
- The Wnt10b Fzd6_lrp6 exception is retained as a low-medium
  `reviewed_relay_candidate`: Neuhaus et al. (PMID:34769487; PMCID:PMC8584856;
  DOI:10.3390/ijms222112057) measured WNT10B-dependent endogenous FZD6-LRP6
  proximity in PC-3 cells and rapid nuclear beta-catenin accumulation. This is
  receptor-complex association and early pathway function, not purified direct
  WNT10B-FZD6-LRP6 binding or a reconstituted ternary structure.
- The other 24 rows remain explicit `no_evidence_boundary` outcomes. Primary
  WNT-FZD receptor-selectivity and LRP5/6 comparator studies were used only to
  define the search boundary: PMID:25605717, PMID:22433869, PMID:21887268,
  PMID:17130287, and PMID:21041481. Evidence for another WNT ligand, another
  FZD subtype, an LRP component alone, generic pathway activity, expression,
  reporter output, or beta-catenin function was not transferred to the exact
  submitted pair.
- Composite rows are treated as exact WNT-ligand–FZD–LRP receptor-complex
  claims. Component evidence is not silently combined, and no direct binding
  claim is inferred from generic WNT pathway or beta-catenin function.

## Limitations and handoff boundary

The positive exception is human prostate-cancer-cell proximity/function
evidence, not an SCI receiver model. The unresolved rows lack a qualifying
exact primary binding, receptor-reconstitution, structure, or selective
receptor-dependent perturbation assay in the reviewed packet. LRP5 versus LRP6,
FZD subtype, receptor stoichiometry, ligand presentation, species, and cell
context therefore remain explicit limitations. No Module22A terminal-TF
handoff is created from these rows.

Only the requested batch TSV and this summary were written. Module20A files,
the adjudication packet, shared Module21A/Module22A ledgers, coverage tables,
and integration outputs were not modified. No commit was created.
