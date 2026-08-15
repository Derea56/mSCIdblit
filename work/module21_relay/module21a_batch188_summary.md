# Module 21A Batch 188 review summary

Batch 188 reviews exactly filtered queue ordinals **4151–4175**: 25
priority-8, low/uncertain Module20A LIANA-remaining rows, in the supplied
order. The raw artifact is `module21a_batch188_review.tsv` and uses the exact
13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 1 |
| `reviewed_unresolved` | 7 |
| `no_evidence_boundary` | 17 |
| **total** | **25** |

Confidence counts: low 19; low-medium 6. Every `terminal_TF` value is the
literal `null`.

## Queue alignment

| filtered ordinal | review ID range | pairs |
|---:|---|---|
| 4151–4175 | `M20A-LIANA-REMAINING-0423`–`0447` | Wnt3a Fzd6_lrp6; Wnt3a Fzd7_lrp5; Wnt3a Fzd7_lrp6; Wnt3a Fzd8_lrp5; Wnt3a Fzd8_lrp6; Wnt3a Fzd9_lrp5; Wnt3a Fzd9_lrp6; Wnt3a Ryk; Wnt4 Fzd10_lrp5; Wnt4 Fzd10_lrp6; Wnt4 Fzd1_lrp5; Wnt4 Fzd1_lrp6; Wnt4 Fzd2_lrp5; Wnt4 Fzd2_lrp6; Wnt4 Fzd3_lrp5; Wnt4 Fzd3_lrp6; Wnt4 Fzd4_lrp5; Wnt4 Fzd4_lrp6; Wnt4 Fzd5_lrp5; Wnt4 Fzd5_lrp6; Wnt4 Fzd6_lrp5; Wnt4 Fzd6_lrp6; Wnt4 Fzd7_lrp5; Wnt4 Fzd7_lrp6; Wnt4 Fzd8_lrp5 |

## Evidence decisions

- The adjudication packet at
  `work/module20_db_seed/evidence_search_agents/liana_remaining_adjudication.tsv`
  was used as the exact-pair baseline. It classifies rows 0423–0425,
  0428–0429, and 0443–0444 as manual-review boundaries; row 0427 as a
  low-evidence exact ternary-complex candidate; and the remaining rows as
  no-evidence boundaries.
- The primary multiplex CRISPR/rescue study (PMID:28733458; PMCID:PMC5636703)
  supports WNT3A-to-FZD-level functional mapping in human cells, but it does
  not isolate LRP5 from LRP6 or establish a full-length WNT-FZD-LRP composite.
  Therefore rows 0423–0425 and 0428–0429 remain unresolved, with no direct
  ternary binding or LRP-specific relay inferred.
- The primary purified-protein study (PMID:20093360; PMCID:PMC2838336;
  DOI:10.1074/jbc.M109.092130) directly reconstitutes a Wnt3a–Fz8 CRD–LRP6
  extracellular ternary complex and measures Wnt3a/LRP6 binding and
  Wnt-dependent complex formation. Row 0427 is retained as a
  `reviewed_relay_candidate`, but the soluble-fragment and non-SCI context
  limits transfer to full-length SCI receiver signaling.
- The primary Wnt4 study (PMID:15265686;
  DOI:10.1016/j.yexcr.2004.04.036) reports a Wnt4–Fzd6 CRD biochemical complex
  and canonical Wnt responsiveness in MDCK kidney epithelial cells. It does
  not identify LRP5 versus LRP6, so rows 0443–0444 remain unresolved rather
  than being promoted to exact Wnt4–Fzd6–LRP5/6 complexes.
- For no-evidence rows, WNT-FZD/LRP comparator studies and the Wnt4–Fzd6
  primary study are retained only to define the search boundary. Generic WNT
  family membership, receptor expression, pathway annotations, database
  co-mentions, structurally related complexes, and beta-catenin output were
  not combined into the submitted exact composite.

## Limitations and handoff boundary

The retained positive evidence is comparator- or fragment-specific and is not
an SCI astrocyte mechanism. Exact ligand–FZD–LRP stoichiometry, LRP5-versus-
LRP6 selectivity, full-length receptor presentation, species, cell context,
and downstream branch identity remain unresolved wherever stated. TCF/LEF or
beta-catenin reporter output is not treated as a terminal-TF assignment.

Only the requested batch TSV and this summary were written. Module20A files,
the adjudication packet, shared Module21A/Module22A ledgers, coverage tables,
and integration outputs were not modified. No commit was created.
