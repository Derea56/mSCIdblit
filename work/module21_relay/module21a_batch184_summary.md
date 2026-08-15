# Module 21A Batch 184 review summary

Batch 184 reviews exactly filtered queue ordinals **4051–4075**: 25 priority-8,
low/uncertain Module20A LIANA-remaining rows, in the supplied order. The raw
artifact is `module21a_batch184_review.tsv` and uses the exact 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 4 |
| `no_evidence_boundary` | 21 |
| **total** | **25** |

Confidence counts: low 3; low-medium 1. Every `terminal_TF` value is the
literal `null`.

## Queue alignment

| filtered ordinal | review ID range | pairs |
|---:|---|---|
| 4051–4057 | `M20A-LIANA-REMAINING-0323`–`0329` | Wnt11 Fzd4; Wnt11 Fzd5; Wnt11 Fzd6; Wnt11 Fzd7; Wnt11 Fzd8; Wnt11 Fzd9; Wnt11 Musk |
| 4058–4075 | `M20A-LIANA-REMAINING-0330`–`0347` | Wnt16 Fzd10_lrp5; Wnt16 Fzd10_lrp6; Wnt16 Fzd1_lrp5; Wnt16 Fzd1_lrp6; Wnt16 Fzd2_lrp5; Wnt16 Fzd2_lrp6; Wnt16 Fzd3_lrp5; Wnt16 Fzd3_lrp6; Wnt16 Fzd4_lrp5; Wnt16 Fzd4_lrp6; Wnt16 Fzd5_lrp5; Wnt16 Fzd5_lrp6; Wnt16 Fzd6_lrp5; Wnt16 Fzd6_lrp6; Wnt16 Fzd7_lrp5; Wnt16 Fzd7_lrp6; Wnt16 Fzd8_lrp5; Wnt16 Fzd8_lrp6 |

## Evidence decisions

- The existing adjudication packet at
  `work/module20_db_seed/evidence_search_agents/liana_remaining_adjudication.tsv`
  was used as the bounded exact-pair baseline. It identifies three Wnt11
  candidates (Fzd4, Fzd7, and MuSK) and one Wnt16B/Fzd5/LRP6
  receptor-association candidate.
- Wnt11-Fzd4 is retained as a low-confidence receptor-proximal candidate from
  mouse P19 cardiac-cell pull-down/blockade and PKC/differentiation assays
  (PMID:21041481). Wnt11-Fzd7 is retained from human/mouse melanoma and
  xenograft functional evidence (PMID:33082334), with the DAAM1-Rho/ROCK
  branch kept explicit. Wnt11-MuSK is retained only with its zebrafish
  Wnt11r-Unplugged/MuSK species boundary (PMID:19285469).
- Wnt16 Fzd5_lrp6 is retained as low-medium receptor-proximal evidence because
  WNT16B promoted FZD5-LRP6 association in BRET and single-molecule assays
  (PMID:40413190). The record does not promote efficient canonical signalosome
  activation and preserves the WNT16B isoform limitation.
- The other 21 rows remain explicit `no_evidence_boundary` outcomes. Primary
  WNT-FZD receptor-selectivity and LRP5/6 comparator papers
  (PMID:25605717, PMID:21887268, and PMID:22433869) were used only to define
  the search boundary. Evidence for another WNT ligand, another FZD subtype,
  an LRP component alone, generic pathway activity, expression, reporter
  output, or beta-catenin function was not transferred to the exact submitted
  pair.
- Composite rows are treated as exact WNT-ligand–FZD–LRP receptor-complex
  claims. Component evidence is not silently combined, and no direct binding
  claim is inferred from generic pathway/function annotations.

## Limitations and handoff boundary

The candidate rows are context-specific and do not establish a universal
mammalian or SCI receiver mechanism. The unresolved rows lack a qualifying
exact primary binding, receptor-reconstitution, structure, or selective
receptor-dependent perturbation assay in the reviewed packet. FZD subtype,
LRP5 versus LRP6, receptor stoichiometry, ligand processing/presentation,
species, and cell context remain explicit limitations. No terminal TF
assignment is made.

Only the requested batch TSV and this summary were written. Module20A files,
the adjudication packet, shared Module21A/Module22A ledgers, coverage tables,
and integration outputs were not modified. No commit was created.

